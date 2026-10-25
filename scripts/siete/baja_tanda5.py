"""Descarga los datos en bruto de la quinta tanda (semana del 26 de octubre al 1 de noviembre de 2026) a datos/siete/fuentes/t5/.
Mismo sistema que baja_tanda4.py (Wikidata por QLever). Se puede relanzar: lo bajado no se vuelve a pedir."""
from comun import *
import baja_tanda4 as b4
D5 = FUENTES / "t5"; D5.mkdir(exist_ok=True)
b4.D4 = D5          # las funciones de la cuarta tanda escriben en la carpeta de esta
q, baja, wiki, personajes = b4.q, b4.baja, b4.wiki, b4.personajes
def sparql(nombre, consulta):
    """QLever primero; si falla (el 2026-10-25 daba 502), el servicio oficial de Wikidata."""
    ruta = D5 / f"{nombre}.json"
    if ruta.exists(): return
    datos = urllib.parse.urlencode({"query": consulta}).encode()
    for url in ("https://qlever.dev/api/wikidata", "https://query.wikidata.org/sparql"):
        try:
            r = urllib.request.Request(url, data=datos, headers={**UA, "Accept": "application/sparql-results+json"})
            b = urllib.request.urlopen(r, timeout=300).read()
            ruta.write_bytes(b); print(nombre, len(json.loads(b)["results"]["bindings"]), url); return
        except Exception as e: print(nombre, url, e)
    print(nombre, "SIN DATOS")

GENTILICIOS = b4.PRE + """SELECT ?x ?xLabel ?g ?tipo ?pob WHERE {
  VALUES ?tipo { wd:Q6256 wd:Q162620 wd:Q10742 wd:Q2074737 wd:Q515 wd:Q1637706 wd:Q35657 wd:Q15284 }
  ?x wdt:P31 ?tipo ; wdt:P1549 ?g . FILTER(LANG(?g)="es")
  OPTIONAL { ?x wdt:P1082 ?pob }
  OPTIONAL { ?x rdfs:label ?xLabel FILTER(LANG(?xLabel)="es") }
}"""
CONSULTAS = {
 "barca":        q("?x wdt:P31 wd:Q5 ; wdt:P54 wd:Q7156 ."),
 "netflix":      q("?x wdt:P449 wd:Q907311 ; wdt:P31/wdt:P279* wd:Q5398426 ."),
 "juegos_mesa":  q("{ ?x wdt:P31/wdt:P279* wd:Q131436 } UNION { ?x wdt:P31/wdt:P279* wd:Q142714 }"),
 "criaturas":    q("{ ?x wdt:P31/wdt:P279* wd:Q2239243 } UNION { ?x wdt:P279+ wd:Q2239243 }"),
 "instrumentos": q("{ ?x wdt:P31/wdt:P279* wd:Q34379 } UNION { ?x wdt:P279+ wd:Q34379 }"),
 "jdt":          q('VALUES ?w { wd:Q23572 wd:Q45875 wd:Q105869254 } ?x wdt:P1441 ?w .'),
 "pixar":        q("?x wdt:P31 wd:Q11424 ; wdt:P272 wd:Q127552 ."),
 "gentilicios":  GENTILICIOS,
}
for n, c in CONSULTAS.items(): sparql(n, c)
baja("badbunny_kworb.html", "https://kworb.net/spotify/artist/4q3ewBCX7sLwd24euuV69X_songs.html")
wiki("disney_channel_en", "en", "List of Disney Channel original series")
wiki("pelis2026_en", "en", "2026 in film")
wiki("presidentes", "es", "Presidente del Gobierno de España")
wiki("pelis2026_eeuu", "en", "List of American films of 2026")
wiki("pelis2026_terror", "en", "List of horror films of 2026")
wiki("pelis2026_cine", "es", "Anexo:Cine en 2026")
wiki("pelis2026_uk", "en", "List of 2026 box office number-one films in the United Kingdom")
