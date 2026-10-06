"""Descarga los datos en bruto de la segunda tanda de preguntas (octubre de 2026) a datos/siete/fuentes/t2/.
Se puede relanzar: lo que ya está bajado no se vuelve a pedir."""
import sys
from comun import *
T2 = FUENTES / "t2"

def sparql(nombre, consulta):
    ruta = T2 / f"{nombre}.json"
    if ruta.exists(): return
    u = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(consulta)
    for intento in range(4):
        try:
            datos = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
            ruta.write_bytes(datos); print(nombre, len(json.loads(datos)["results"]["bindings"])); time.sleep(3); return
        except Exception as e:
            print(nombre, "reintento", e); time.sleep(15 * (intento + 1))
    print(nombre, "SIN DATOS")

BASE = """SELECT ?x ?xLabel ?en ?links ?art (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) %(mas)s WHERE {
  %(donde)s
  ?x wikibase:sitelinks ?links . %(filtro)s
  OPTIONAL { ?x rdfs:label ?en FILTER(LANG(?en)="en") }
  OPTIONAL { ?x skos:altLabel ?alt FILTER(LANG(?alt)="es") }
  OPTIONAL { ?art schema:about ?x ; schema:isPartOf <https://es.wikipedia.org/> }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" }
} GROUP BY ?x ?xLabel ?en ?links ?art %(mas)s"""
def q(donde, minimo=0, mas=""):
    return BASE % {"donde": donde, "filtro": f"FILTER(?links >= {minimo})" if minimo else "", "mas": mas}

CONSULTAS = {
 "pokemon":  q("?x wdt:P31/wdt:P279* wd:Q3966183 ."),
 "paises":   q("""?x wdt:P31 wd:Q3624078 . FILTER NOT EXISTS { ?x wdt:P576 ?fin }
                 OPTIONAL { ?x wdt:P1622 ?lado } OPTIONAL { ?x wdt:P122 ?g . ?g wdt:P279* wd:Q7269 . BIND(1 AS ?mon) }
                 OPTIONAL { ?arten schema:about ?x ; schema:isPartOf <https://en.wikipedia.org/> }""", mas="?lado ?mon ?arten"),
 "italia":   q("?x wdt:P31 wd:Q747074 ; wdt:P1082 ?pop . FILTER(?pop >= 25000)"),
 "disney":   q("?x wdt:P272 wd:Q1047410 ; wdt:P31/wdt:P279* wd:Q11424 . OPTIONAL { ?x wdt:P577 ?f }", mas="(MIN(YEAR(?f)) AS ?anio)").replace("GROUP BY ?x ?xLabel ?en ?links ?art (MIN(YEAR(?f)) AS ?anio)", "GROUP BY ?x ?xLabel ?en ?links ?art"),
 "hp":       q("?x wdt:P1080 wd:Q5410773 ."),
 "miedo":    q("?x wdt:P31 wd:Q11424 ; wdt:P136 wd:Q200092 .", 14),
 "anime":    q("{ ?x wdt:P31 wd:Q63952888 } UNION { ?x wdt:P31 wd:Q21198342 } UNION { ?x wdt:P31 wd:Q1107 }", 10),
 "movil":    q("?x wdt:P31 wd:Q7889 ; wdt:P400 ?pl . VALUES ?pl { wd:Q48493 wd:Q94 }", 12),
 "dj":       q("?x wdt:P31 wd:Q5 ; wdt:P106 wd:Q130857 .", 14),
 "raperos":  q("?x wdt:P31 wd:Q5 ; wdt:P106 wd:Q2252262 ; wdt:P27 wd:Q29 ."),
 "youtubers":q("?x wdt:P31 wd:Q5 ; wdt:P27 wd:Q29 ; wdt:P106 ?of . VALUES ?of { wd:Q17125263 wd:Q57414145 wd:Q110374796 wd:Q4110598 }"),
 "idiomas":  q("?x wdt:P31/wdt:P279* wd:Q34770 .", 25),
 "supermercados": q("{ ?x wdt:P31/wdt:P279* wd:Q18043413 } UNION { ?x wdt:P31 wd:Q180846 } OPTIONAL { ?x wdt:P17 ?p }", mas="(SAMPLE(?p) AS ?pais)").replace("GROUP BY ?x ?xLabel ?en ?links ?art (SAMPLE(?p) AS ?pais)", "GROUP BY ?x ?xLabel ?en ?links ?art"),
 "prendas":  q("?x wdt:P279+ wd:Q11460 .", 6),
 "transporte": q("{ ?x wdt:P279+ wd:Q334166 } UNION { ?x wdt:P279+ wd:Q42889 }", 18),
 "electrodomesticos": q("?x wdt:P279+ wd:Q212920 .", 3),
 "nombres_vascos": q("?x wdt:P31/wdt:P279* wd:Q202444 ; wdt:P407 wd:Q8752 ."),
 "discotecas": q("?x wdt:P31/wdt:P279* wd:Q622425 .", 1),
 "cartas":   q("{ ?x wdt:P31/wdt:P279* wd:Q142714 } UNION { ?x wdt:P279+ wd:Q142714 }", 1),
 "hp2":      q("?x wdt:P1080 wd:Q5410773 ; wdt:P31/wdt:P279* wd:Q95074 ."),
 "metro":    q("?x wdt:P31/wdt:P279* wd:Q928830 ; wdt:P16 wd:Q191987 ."),
 "fiestas_wd": q("?x wdt:P31/wdt:P279* wd:Q132241 ; wdt:P17 wd:Q29 ."),
}
for n, c in CONSULTAS.items(): sparql(n, c)

def wiki(nombre, lang, **kw):
    ruta = T2 / f"{nombre}.json"
    if ruta.exists(): return
    kw.update(format="json")
    u = f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(kw)
    try:
        ruta.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()); print(nombre, "ok"); time.sleep(2)
    except Exception as e: print(nombre, "FALLA", e)
for nombre, lang, pagina in [("beatles_wiki", "en", "List of songs recorded by the Beatles"),
                             ("primera", "es", "Anexo:Clasificación histórica de la Primera División de España"),
                             ("ibex", "es", "IBEX 35"), ("fobias", "es", "Anexo:Fobias"), ("colores", "es", "Anexo:Colores"),
                             ("fiestas_int", "es", "Anexo:Fiestas de Interés Turístico Internacional (España)"),
                             ("fiestas_nac", "es", "Anexo:Fiestas de Interés Turístico Nacional (España)")]:
    wiki(nombre, lang, action="parse", page=pagina, prop="wikitext", redirects="1")
for nombre, pagina in [("bob", "List of SpongeBob SquarePants characters"), ("shrek", "List of Shrek characters"),
                       ("mariokart", "Mario Kart"), ("mcdonalds_lista", "List of McDonald's products")]:
    wiki(nombre, "en", action="parse", page=pagina, prop="wikitext", redirects="1")
for nombre, cat in [("cat_zapatillas", "Category:Athletic shoe brands"), ("cat_zapatos", "Category:Shoe brands"), ("cat_deporte", "Category:Sportswear brands"),
                    ("cat_lujo", "Category:Luxury motor vehicle manufacturers"), ("cat_deportivos", "Category:Sports car manufacturers"),
                    ("cat_mcdonalds", "Category:McDonald's foods"), ("cat_naipes", "Category:Card games by name")]:
    wiki(nombre, "en", action="query", list="categorymembers", cmtitle=cat, cmlimit="500")
wiki("cat_naipes_es", "es", action="query", list="categorymembers", cmtitle="Categoría:Juegos de naipes", cmlimit="500")
for i, linea in enumerate(["Categoría:Estaciones de la línea %d del Metro de Madrid" % n for n in range(1, 13)] + ["Categoría:Estaciones del Metro de Madrid por línea"]):
    wiki(f"metro_{i}", "es", action="query", list="categorymembers", cmtitle=linea, cmlimit="500")
wiki("metro_cat", "es", action="query", list="categorymembers", cmtitle="Categoría:Estaciones del Metro de Madrid", cmlimit="500")

def baja(nombre, url, agente=None):
    ruta = T2 / nombre
    if ruta.exists(): return
    try:
        ruta.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": agente or UA["User-Agent"]}), timeout=90).read())
        print(nombre, ruta.stat().st_size)
    except Exception as e: print(nombre, "FALLA", e)
baja("beatles_kworb.html", "https://kworb.net/spotify/artist/3WrFJ7ztbogyGnTHbHJFl2_songs.html", "Mozilla/5.0")
baja("pokeapi.json", "https://pokeapi.co/api/v2/pokemon-species?limit=151")
baja("nombres_ine.xls", "https://www.ine.es/daco/daco42/nombyapel/nombres_por_edad_media.xls")
for u in ("https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/main/0_palabras_todas.txt",
          "https://raw.githubusercontent.com/olea/lemarios/master/lemario-general-del-espanol.txt",
          "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"):
    baja("palabras.txt", u)
