"""Descarga de Wikidata las respuestas posibles de las categorías abiertas.

Uso:  python3 scripts/wikidata.py [id_categoría ...]
Guarda datos/wikidata/<id>.json con [nombre, [alias], nº de Wikipedias].
El nº de Wikipedias en las que aparece algo sirve para estimar lo conocido
que es: scripts/banco.py lo convierte en nivel.
"""
import json, sys, time, pathlib, urllib.parse, urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "datos" / "wikidata"
UA = "Sabihondo/0.1 (https://github.com/norahmartinn/sabihondo)"

# Cada consulta liga ?item; mínimo de Wikipedias para no traer ruido.
CONSULTAS = {
 19: ("?item wdt:P31 wd:Q2074737 .", 0),                                      # municipios de España
 20: ("VALUES ?t {wd:Q8502 wd:Q207326 wd:Q54050} ?item wdt:P31 ?t ; wdt:P17 wd:Q29 .", 1),
 21: ("VALUES ?t {wd:Q40080 wd:Q31615} ?item wdt:P31 ?t ; wdt:P17 wd:Q29 .", 0),
 22: ("?item wdt:P16 wd:Q191987 ; wdt:P31/wdt:P279* wd:Q928830 .", 0),        # estaciones del Metro de Madrid
 23: ("?item (wdt:P31|wdt:P279)/wdt:P279* wd:Q182940 .", 1),                 # postres
 24: ("?item wdt:P31/wdt:P279* wd:Q768267 .", 0),                            # cereales de desayuno
 25: ("?item (wdt:P31|wdt:P279)/wdt:P279* wd:Q173265 .", 0),                 # patatas fritas de bolsa
 26: ("VALUES ?t {wd:Q41415 wd:Q2920963} ?item (wdt:P31|wdt:P279)/wdt:P279* ?t .", 1),
 27: ("?item (wdt:P31|wdt:P279)/wdt:P279* wd:Q177 .", 0),                    # pizzas
 28: ("?item (wdt:P31|wdt:P279)/wdt:P279* wd:Q178780 .", 0),                 # licores
 29: ("VALUES ?t {wd:Q178921 wd:Q1049049} ?item wdt:P31/wdt:P279* ?t .", 0), # aguas minerales
 31: ("?item wdt:P31 wd:Q46970 .", 3),                                       # aerolíneas
 33: ("?item wdt:P279+ wd:Q61065 .", 1),                                  # deportes acuáticos (tipos, no competiciones)
 36: ("?item wdt:P31 wd:Q7889 ; wdt:P400 wd:Q192851 .", 2),                  # juegos de recreativa
 39: ("?item wdt:P1441 ?w . ?w wdt:P272 wd:Q127552 . ?item wdt:P31/wdt:P279* wd:Q95074 .", 1),
 40: ("VALUES ?u {wd:Q642878 wd:Q931597} ?item wdt:P1080 ?u ; wdt:P31/wdt:P279* wd:Q95074 .", 1),   # personajes Marvel
 41: ("?item wdt:P1441 wd:Q79784 .", 0),                                     # Friends
 42: ("?item wdt:P1441 wd:Q23831 ; wdt:P31/wdt:P279* wd:Q95074 .", 0),    # personajes de The Office (EE. UU.)
 43: ("?item wdt:P31/wdt:P279* wd:Q5398426 ; wdt:P449 wd:Q907311 .", 1),     # series de Netflix
 45: ("?item wdt:P136 wd:Q170238 .", 2),                                     # sitcoms
 46: ("?item wdt:P31 wd:Q11424 ; wdt:P495 wd:Q29 .", 1),                     # películas españolas
 47: ("VALUES ?c {wd:Q191224 wd:Q1047410 wd:Q127552} ?item wdt:P31 wd:Q11424 ; wdt:P272 ?c .", 2),
 48: ("{ ?item wdt:P31 wd:Q11424 ; wdt:P272 wd:Q367466 . } UNION { ?item wdt:P31 wd:Q11424 ; wdt:P1080 wd:Q931597 . }", 2),
 49: ("VALUES ?bt {wd:Q7725634 wd:Q8261 wd:Q47461344 wd:Q571} ?item wdt:P31 wd:Q11424 ; wdt:P144 ?b . ?b wdt:P31 ?bt .", 15),
 50: ("?item wdt:P106 wd:Q2526255 . ?peli wdt:P57 ?item ; wdt:P31 wd:Q11424 .", 20),   # directores con alguna película
 51: ("VALUES ?o {wd:Q177220 wd:Q488205} ?item wdt:P106 ?o ; wdt:P264 ?sello .", 30),   # cantantes con discográfica
 52: ("?item wdt:P31 wd:Q215380 ; wdt:P495 wd:Q29 .", 1),                    # grupos españoles
 53: ("?item wdt:P31 wd:Q868557 .", 3),
 55: ("?item wdt:P31/wdt:P279* wd:Q22989102 .", 1),
 56: ("?item (wdt:P31|wdt:P279)/wdt:P279* wd:Q2239243 .", 5),
 57: ("VALUES ?t {wd:Q3305213 wd:Q860861} ?item wdt:P31 ?t .", 15),
 58: ("VALUES ?t {wd:Q41176 wd:Q11303 wd:Q2977 wd:Q23413 wd:Q16560 wd:Q33506 wd:Q24354 wd:Q483110 wd:Q12518 wd:Q32815 wd:Q16970} ?item wdt:P31 ?t .", 50),
 59: ("?item wdt:P31 wd:Q11303 .", 3),
 60: ("VALUES ?t {wd:Q4989906 wd:Q839954 wd:Q16560 wd:Q23413 wd:Q44539 wd:Q12518 wd:Q179700} ?item wdt:P31 ?t .", 60),
 61: ("?item wdt:P31/wdt:P279* wd:Q3220391 .", 3),
 62: ("?item wdt:P31/wdt:P279* wd:Q2462003 .", 2),
 63: ("?item wdt:P31/wdt:P279* wd:Q15590336 .", 1),
 68: ("{ ?item wdt:P31 wd:Q22687 . ?item wikibase:sitelinks ?s0 . FILTER(?s0 >= 8) } UNION { ?item wdt:P31 wd:Q22687 ; wdt:P17 wd:Q29 . }", 0),
 69: ("VALUES ?t {wd:Q18534542 wd:Q18509232} ?item wdt:P31 ?t .", 2),
 70: ("?item wdt:P31 wd:Q1631129 .", 1),
 71: ("?item wdt:P31 wd:Q622425 .", 1),
 72: ("VALUES ?t {wd:Q150139 wd:Q6147123} ?item wdt:P31/wdt:P279* ?t ; wdt:P17 wd:Q29 .", 0),   # fiestas patronales y romerías
 73: ("?item wdt:P279+ wd:Q18123741 . FILTER NOT EXISTS { ?item wdt:P279* wd:Q12078 }", 5),
}

PREFIJOS = """PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""
PLANTILLA = PREFIJOS + """SELECT ?item ?sl ?es ?en (GROUP_CONCAT(DISTINCT ?al; separator="|") AS ?als) WHERE {
  %s
  ?item wikibase:sitelinks ?sl .
  OPTIONAL { ?item rdfs:label ?es FILTER(lang(?es) = "es") }
  OPTIONAL { ?item rdfs:label ?en FILTER(lang(?en) = "en") }
  OPTIONAL { ?item skos:altLabel ?al FILTER(lang(?al) = "es") }
} GROUP BY ?item ?sl ?es ?en"""

def pide(consulta):
    # QLever (Universidad de Friburgo): los mismos datos de Wikidata, mucho más rápido que query.wikidata.org
    url = "https://qlever.dev/api/wikidata?" + urllib.parse.urlencode({"query": consulta})
    req = urllib.request.Request(url, headers={"Accept": "application/sparql-results+json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)["results"]["bindings"]

import re
FUERA = re.compile(r"^(l[ií]nea |depósito |cocheras |lista de |anexo:|categor[ií]a:|plantilla:)", re.I)
PREFIJO = re.compile(r"^(estaci[oó]n de (metro de )?|estaci[oó]n )", re.I)

def descarga(cid):
    patron, minimo = CONSULTAS[cid]
    # QLever filtra mal por número: el mínimo de Wikipedias se aplica aquí
    filas = [f for f in pide(PLANTILLA % patron) if int(f["sl"]["value"]) >= minimo]
    vistos, salida = set(), []
    for f in filas:
        es, en = f.get("es", {}).get("value"), f.get("en", {}).get("value")
        als_todas = [a for a in f.get("als", {}).get("value", "").split("|") if a]
        nombre = es or en or (als_todas[0] if als_todas else None)
        extra = []
        if nombre:
            nombre = PREFIJO.sub("", nombre).strip()
            nombre = re.sub(r"\s*\([^)]*\)$", "", nombre).strip()       # «Creed Bratton (personaje)»
            if " / " in nombre:                                             # «Wanda Maximoff / Bruja Escarlata»
                partes = [x.strip() for x in nombre.split(" / ") if x.strip()]
                nombre, extra = partes[0], partes[1:]
            if nombre[:1].islower(): nombre = nombre[0].upper() + nombre[1:]
        if nombre and FUERA.match(nombre): continue
        if not nombre or (nombre.startswith("Q") and nombre[1:].isdigit()) or len(nombre) > 70: continue
        alias = [a for a in f.get("als", {}).get("value", "").split("|") if a and len(a) <= 70]
        if es and en and en != es: alias.append(en)
        alias += extra
        clave = nombre.lower()
        if clave in vistos: continue
        vistos.add(clave)
        salida.append([nombre, sorted(set(alias) - {nombre}), int(f["sl"]["value"])])
    salida.sort(key=lambda x: -x[2])
    SALIDA.mkdir(parents=True, exist_ok=True)
    (SALIDA / f"{cid}.json").write_text(json.dumps(salida, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return len(salida)

if __name__ == "__main__":
    ids = [int(x) for x in sys.argv[1:]] or list(CONSULTAS)
    for cid in ids:
        for intento in range(3):
            try:
                n = descarga(cid); print(f"{cid}: {n}", flush=True); break
            except Exception as e:
                print(f"{cid}: error ({e}), reintento", flush=True); time.sleep(15 * (intento + 1))
        time.sleep(3)
