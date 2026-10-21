"""Descarga los datos en bruto de la cuarta tanda (semana del 19 al 25 de octubre de 2026) a datos/siete/fuentes/t4/.
Wikidata va por QLever (qlever.dev), porque query.wikidata.org da timeouts. Se puede relanzar: lo bajado no se vuelve a pedir."""
from comun import *
D4 = FUENTES / "t4"; D4.mkdir(exist_ok=True)

def baja(nombre, url, agente=None):
    ruta = D4 / nombre
    if ruta.exists() and ruta.stat().st_size > 200: return
    try:
        ruta.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": agente or UA["User-Agent"]}), timeout=120).read())
        print(nombre, ruta.stat().st_size)
    except Exception as e: print(nombre, "FALLA", e)

PRE = """PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <http://schema.org/>
"""
BASE = PRE + """SELECT ?x (SAMPLE(?es) AS ?xLabel) (SAMPLE(?e) AS ?en) (SAMPLE(?l) AS ?links) (SAMPLE(?a) AS ?art) (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) WHERE {
  %(donde)s
  ?x wikibase:sitelinks ?l . %(filtro)s
  OPTIONAL { ?x rdfs:label ?es FILTER(LANG(?es)="es") }
  OPTIONAL { ?x rdfs:label ?e FILTER(LANG(?e)="en") }
  OPTIONAL { ?x skos:altLabel ?alt FILTER(LANG(?alt)="es") }
  OPTIONAL { ?a schema:about ?x ; schema:isPartOf <https://es.wikipedia.org/> }
} GROUP BY ?x"""
def q(donde, minimo=0):
    return BASE % {"donde": donde, "filtro": ""}   # QLever filtra mal por número: el mínimo se aplica luego en Python
def sparql(nombre, consulta):
    ruta = D4 / f"{nombre}.json"
    if ruta.exists(): return
    datos = urllib.parse.urlencode({"query": consulta}).encode()
    for intento in range(3):
        try:
            r = urllib.request.Request("https://qlever.dev/api/wikidata", data=datos, headers={**UA, "Accept": "application/sparql-results+json"})
            b = urllib.request.urlopen(r, timeout=300).read()
            ruta.write_bytes(b); print(nombre, len(json.loads(b)["results"]["bindings"])); return
        except Exception as e:
            print(nombre, "reintento", e); time.sleep(10 * (intento + 1))
    print(nombre, "SIN DATOS")

def personajes(titulo_en):
    return f'?w rdfs:label "{titulo_en}"@en . ?x wdt:P1441 ?w .'
CONSULTAS = {
 "minerales":     q("?x wdt:P31 wd:Q12089225 ."),
 "filosofos":     q("?x wdt:P31 wd:Q5 ; wdt:P106 wd:Q4964182 .", 20),
 "batallas":      q("?x wdt:P31/wdt:P279* wd:Q178561 .", 12),
 "guerras":       q("{ ?x wdt:P31/wdt:P279* wd:Q198 } UNION { ?x wdt:P31/wdt:P279* wd:Q8465 } UNION { ?x wdt:P31 wd:Q350604 } UNION { ?x wdt:P31 wd:Q467011 } UNION { ?x wdt:P31 wd:Q124734 }", 5),
 "corrientes":    q("?x wdt:P31 ?c . VALUES ?c { wd:Q2915955 wd:Q12765852 wd:Q138642081 }"),
 "hormonas":      q("{ ?x wdt:P31/wdt:P279* wd:Q11364 } UNION { ?x wdt:P279+ wd:Q11364 }", 3),
 "sagas":         q("?x wdt:P31/wdt:P279* wd:Q24856 .", 12),
 "formatos":      q("?x wdt:P31/wdt:P279* wd:Q235557 ; wdt:P1195 ?ext .", 4),
 "formatos_ext":  PRE + "SELECT ?x ?ext WHERE { ?x wdt:P31/wdt:P279* wd:Q235557 ; wdt:P1195 ?ext }",
 "refrescos":     q("{ ?x wdt:P31/wdt:P279* wd:Q147538 } UNION { ?x wdt:P279+ wd:Q147538 }", 2),
 "cocacola":      q("{ ?x wdt:P127 wd:Q3295867 } UNION { ?x wdt:P176 wd:Q3295867 } UNION { wd:Q3295867 wdt:P1716 ?x } UNION { ?x wdt:P1716 wd:Q3295867 }"),
 "apple":         q("?x wdt:P176 wd:Q312 .", 3),
 "nestle":        q("{ ?x wdt:P127 wd:Q160746 } UNION { ?x wdt:P176 wd:Q160746 } UNION { wd:Q160746 wdt:P1716 ?x }"),
 "masas_agua":    q("?x wdt:P279+ wd:Q15324 .", 3),
 "profesiones":   q("{ ?x wdt:P31 wd:Q28640 } UNION { ?x wdt:P31 wd:Q12737077 }", 6),
 "pueblos_madrid":q("?x wdt:P31 wd:Q2074737 ; wdt:P131+ wd:Q5756 ."),
 "provincias":    q("?x wdt:P31 wd:Q162620 ."),
 "itis_wd":       q('?x wdt:P31/wdt:P279* wd:Q12136 . ?x rdfs:label ?lab . FILTER(LANG(?lab)="es" && REGEX(?lab, "itis$"))'),
 "friends":       q(personajes("Friends")),
 "bigbang":       q(personajes("The Big Bang Theory")),
 "office":        q(personajes("The Office")),
 "modern_family": q(personajes("Modern Family")),
 "phineas":       q(personajes("Phineas and Ferb")),
 "peter_pan":     q('VALUES ?w { wd:Q107895 wd:Q3233467 wd:Q165318 wd:Q1210483 } ?x wdt:P1441 ?w .'),
}
for n, c in CONSULTAS.items(): sparql(n, c)

def wiki(nombre, lang, pagina):
    baja(f"{nombre}.json", f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode({"action": "parse", "page": pagina, "prop": "wikitext", "format": "json", "redirects": 1}))
wiki("eurovision", "es", "España en el Festival de la Canción de Eurovisión")
wiki("circuitos", "en", "List of Formula One circuits")
wiki("escuderias", "en", "List of Formula One constructors")
wiki("musculos", "es", "Anexo:Músculos del cuerpo humano")
wiki("huesos", "es", "Anexo:Huesos del esqueleto humano")
wiki("latin", "es", "Anexo:Locuciones latinas")
wiki("friends_en", "en", "List of Friends and Joey characters")
wiki("bigbang_en", "en", "List of The Big Bang Theory characters")
wiki("office_en", "en", "List of The Office (American TV series) characters")
wiki("modern_family_en", "en", "List of Modern Family characters")
wiki("phineas_en", "en", "List of Phineas and Ferb characters")
wiki("peter_pan_en", "en", "Peter Pan (1953 film)")
wiki("pueblos_madrid_es", "es", "Anexo:Municipios de la Comunidad de Madrid")
wiki("especialidades", "es", "Especialidades médicas")
wiki("frigo", "es", "Frigo")
baja("olivia_kworb.html", "https://kworb.net/spotify/artist/1McMsnEElThX1knmY4oliG_songs.html")
