"""Capitales: la capital actual de cada Estado soberano según Wikidata (países con varias capitales
cuentan todas). Nivel: visitas del artículo de la capital en el último año, mezclando la Wikipedia en
español y la inglesa (media de los dos puestos) para que no pesen solo las capitales de habla hispana."""
import csv, sys
from comun import *

CONSULTA = """SELECT ?c ?cLabel ?en ?pLabel ?art ?arten (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) WHERE {
  ?p wdt:P31 wd:Q3624078 . FILTER NOT EXISTS { ?p wdt:P576 ?fin }
  ?p p:P36 ?st . ?st ps:P36 ?c . FILTER NOT EXISTS { ?st pq:P582 ?hasta }
  OPTIONAL { ?c rdfs:label ?en FILTER(LANG(?en)="en") }
  OPTIONAL { ?c skos:altLabel ?alt FILTER(LANG(?alt)="es") }
  OPTIONAL { ?art schema:about ?c ; schema:isPartOf <https://es.wikipedia.org/> }
  OPTIONAL { ?arten schema:about ?c ; schema:isPartOf <https://en.wikipedia.org/> }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" }
} GROUP BY ?c ?cLabel ?en ?pLabel ?art ?arten"""

bruto = FUENTES / "capitales_wikidata.json"
if not bruto.exists() or "--baja" in sys.argv:
    u = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(CONSULTA)
    bruto.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read())
filas = json.loads(bruto.read_text(encoding="utf-8"))["results"]["bindings"]

caps = {}
for f in filas:
    v = lambda k: f[k]["value"] if k in f else ""
    c = caps.setdefault(v("c"), {"n": v("cLabel"), "en": v("en"), "paises": set(), "alts": set(), "art": "", "arten": ""})
    c["paises"].add(v("pLabel")); c["alts"].update(a for a in v("alts").split("|") if a and len(a) < 40)
    for k in ("art", "arten"):
        if v(k): c[k] = urllib.parse.unquote(v(k).rsplit("/wiki/", 1)[1]).replace("_", " ")

vis = visitas("es", [c["art"] for c in caps.values() if c["art"]], "capitales_visitas.json")
vis_en = visitas("en", [c["arten"] for c in caps.values() if c["arten"]], "capitales_visitas_en.json")
caps = list(caps.values())
for campo, tabla, art in (("p_es", vis, "art"), ("p_en", vis_en, "arten")):
    for i, c in enumerate(sorted(caps, key=lambda c: -(tabla.get(c[art]) or 0)), 1): c[campo] = i
orden = sorted(caps, key=lambda c: c["p_es"] + c["p_en"])
filas = []
for i, c in enumerate(orden, 1):
    alias = [c["en"]] + sorted(c["alts"]) + ([c["art"]] if c["art"] and "(" not in c["art"] else [])
    filas.append((c["n"], alias, nivel_por_puesto(i, [15, 45, 95, 150]), 1000 - (c["p_es"] + c["p_en"]) / 2))
guarda("capitales", filas, "puntuacion_visitas")
