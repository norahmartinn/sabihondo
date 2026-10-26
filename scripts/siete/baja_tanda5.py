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

# ── ampliación (2026-10-26): más respuestas para las que iban solo a mano ──
MAS_CONSULTAS = {
 "frutas_wd":     q("{ ?x wdt:P279+ wd:Q1364 } UNION { ?x wdt:P31 wd:Q1364 } UNION { ?x wdt:P279+ wd:Q3314483 } UNION { ?x wdt:P31/wdt:P279* wd:Q3314483 }"),
 "verduras_wd":   q("{ ?x wdt:P279+ wd:Q11004 } UNION { ?x wdt:P31/wdt:P279* wd:Q11004 }"),
 "cuadros_wd":    q("?x wdt:P31 wd:Q3305213 ; wikibase:sitelinks ?s . FILTER(?s >= 12)"),
 "mascotas_wd":   q("{ ?x wdt:P31 ?t . VALUES ?t { wd:Q144 wd:Q146 wd:Q15720625 wd:Q27120684 wd:Q15831457 } } UNION { ?x wdt:P31 wd:Q26401003 ; wdt:P10241 ?sp . VALUES ?sp { wd:Q144 wd:Q146 } }"),
 "platos_wd":     q("?x wdt:P2012 wd:Q622512 ."),
 "maquillaje_wd": q("{ ?x wdt:P279+ wd:Q16653 } UNION { ?x wdt:P31/wdt:P279* wd:Q16653 }"),
 "cafes_wd":      q("{ ?x wdt:P279+ wd:Q2271219 } UNION { ?x wdt:P31/wdt:P279* wd:Q2271219 } UNION { ?x wdt:P279+ wd:Q8486 }"),
 "monstruos_wd":  q("{ ?x wdt:P31/wdt:P279* wd:Q15734 } UNION { ?x wdt:P279+ wd:Q15734 }"),
}
for n, c in MAS_CONSULTAS.items(): sparql(n, c)
wiki("jdt_en", "en", "List of A Song of Ice and Fire characters")
baja("canciones_disney_cat.json", "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "list": "categorymembers", "cmtitle": "Category:Disney songs", "cmlimit": "500", "format": "json"}))
MAS_CONSULTAS2 = {
 "ruedas_wd":      q("?x wdt:P279+ wd:Q15618781 ."),
 "maquillaje_wd2": q("{ ?x wdt:P279+ wd:Q131207 } UNION { ?x wdt:P31/wdt:P279* wd:Q131207 }"),
 "hospital_wd":    q("{ ?x wdt:P279+ wd:Q6657015 } UNION { ?x wdt:P279+ wd:Q6554101 }"),
 "deportes_wd":    b4.PRE + """SELECT ?x (SAMPLE(?es) AS ?xLabel) (SAMPLE(?e) AS ?en) (SAMPLE(?l) AS ?links) (SAMPLE(?a) AS ?art) (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) (SAMPLE(?pel) AS ?pelota) WHERE {
  { ?x wdt:P31/wdt:P279* wd:Q349 } UNION { ?x wdt:P279+ wd:Q349 }
  ?x wikibase:sitelinks ?l .
  OPTIONAL { ?x wdt:P279*/wdt:P31? wd:Q877517 . BIND(1 AS ?pel) }
  OPTIONAL { ?x wdt:P2283 ?u . ?u wdt:P279* wd:Q18545 . BIND(1 AS ?pel) }
  OPTIONAL { ?x rdfs:label ?es FILTER(LANG(?es)="es") }
  OPTIONAL { ?x rdfs:label ?e FILTER(LANG(?e)="en") }
  OPTIONAL { ?x skos:altLabel ?alt FILTER(LANG(?alt)="es") }
  OPTIONAL { ?a schema:about ?x ; schema:isPartOf <https://es.wikipedia.org/> }
} GROUP BY ?x""",
}
for n, c in MAS_CONSULTAS2.items(): sparql(n, c)
