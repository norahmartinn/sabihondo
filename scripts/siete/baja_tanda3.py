"""Descarga los datos en bruto de la tercera tanda (semana del 12 al 18 de octubre de 2026) a datos/siete/fuentes/tanda3/.
Se puede relanzar: lo que ya está bajado no se vuelve a pedir."""
import sys
from comun import *
D3 = FUENTES / "tanda3"; D3.mkdir(exist_ok=True)

def baja(nombre, url, agente=None):
    ruta = D3 / nombre
    if ruta.exists() and ruta.stat().st_size > 200: return
    try:
        ruta.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": agente or UA["User-Agent"]}), timeout=120).read())
        print(nombre, ruta.stat().st_size)
    except Exception as e: print(nombre, "FALLA", e)

def sparql(nombre, consulta):
    ruta = D3 / f"{nombre}.json"
    if ruta.exists(): return
    u = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(consulta)
    for intento in range(3):
        try:
            datos = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
            ruta.write_bytes(datos); print(nombre, len(json.loads(datos)["results"]["bindings"])); time.sleep(2); return
        except Exception as e:
            print(nombre, "reintento", e); time.sleep(10 * (intento + 1))
    print(nombre, "SIN DATOS")

BASE = """SELECT ?x ?xLabel ?en ?links ?art (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) WHERE {
  %(donde)s
  ?x wikibase:sitelinks ?links . %(filtro)s
  OPTIONAL { ?x rdfs:label ?en FILTER(LANG(?en)="en") }
  OPTIONAL { ?x skos:altLabel ?alt FILTER(LANG(?alt)="es") }
  OPTIONAL { ?art schema:about ?x ; schema:isPartOf <https://es.wikipedia.org/> }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en" }
} GROUP BY ?x ?xLabel ?en ?links ?art"""
def q(donde, minimo=0):
    return BASE % {"donde": donde, "filtro": f"FILTER(?links >= {minimo})" if minimo else ""}

CONSULTAS = {
 "oscar":      q("?x wdt:P166 wd:Q102427 ; wdt:P31/wdt:P279* wd:Q11424 ."),
 "marvel":     q("?x wdt:P1080 wd:Q931597 ; wdt:P31/wdt:P279* wd:Q188784 .", 4),
 "festivales": q("?x wdt:P31/wdt:P279* wd:Q868557 ; wdt:P17 wd:Q29 ."),
 "generos":    q("?x wdt:P31 wd:Q188451 .", 15),
 "pasta":      q("{ ?x wdt:P279+ wd:Q178 } UNION { ?x wdt:P31 wd:Q178 }"),
 "salsas":     q("{ ?x wdt:P279+ wd:Q178359 } UNION { ?x wdt:P31 wd:Q178359 }", 4),
 "pizza":      q("{ ?x wdt:P279+ wd:Q177 } UNION { ?x wdt:P31 wd:Q177 }"),
 "islas":      q("?x wdt:P31/wdt:P279* wd:Q23442 ; wdt:P17 wd:Q29 .", 2),
 "barrios":    q("?x wdt:P31 wd:Q3032114 ."),
 "aerolineas": q("?x wdt:P31/wdt:P279* wd:Q46970 ; wdt:P229 ?iata .", 12),
 "mario":      q("?x wdt:P31 wd:Q7889 ; wdt:P179 ?s . VALUES ?s { wd:Q12379 wd:Q4504 wd:Q850167 wd:Q188196 wd:Q3271970 wd:Q1323591 }"),
 "vinos":      q("?x wdt:P31/wdt:P279* wd:Q2132855 ; wdt:P17 wd:Q29 ."),
}
for n, c in CONSULTAS.items(): sparql(n, c)

def wiki(nombre, lang, sitio="wikipedia", **kw):
    ruta = D3 / f"{nombre}.json"
    if ruta.exists(): return
    kw.update(format="json")
    u = f"https://{lang}.{sitio}.org/w/api.php?" + urllib.parse.urlencode(kw)
    try:
        ruta.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()); print(nombre, "ok", ruta.stat().st_size); time.sleep(1)
    except Exception as e: print(nombre, "FALLA", e)
PAGINAS = [("lqsa", "es", "Anexo:Personajes de La que se avecina"), ("doraemon", "es", "Anexo:Personajes de Doraemon"),
           ("estadios", "es", "Anexo:Estadios de fútbol de España"), ("patrimonio", "es", "Anexo:Patrimonio de la Humanidad en España"),
           ("figuras", "es", "Anexo:Figuras retóricas"), ("figuras2", "es", "Figura retórica"), ("gen27", "es", "Generación del 27"),
           ("ministerios", "es", "Ministerios de España"), ("senales", "es", "Anexo:Señales de tráfico de España"),
           ("aeropuertos", "es", "Anexo:Aeropuertos de España"), ("mario_es", "es", "Anexo:Videojuegos de Mario"),
           ("barrios_anexo", "es", "Anexo:Barrios administrativos de Madrid"), ("vinos_es", "es", "Anexo:Vinos de España"),
           ("vino_espana", "es", "Vino de España"), ("pasta_en", "en", "List of pasta"), ("salsas_en", "en", "List of sauces"),
           ("pizza_en", "en", "List of pizza varieties by country"), ("olimpicos", "es", "Deportes olímpicos"),
           ("universidades", "es", "Anexo:Universidades de España"), ("mario_en", "en", "List of video games featuring Mario"),
           ("festivales_es", "es", "Anexo:Festivales de música de España"), ("oscar_es", "es", "Anexo:Óscar a la mejor película")]
for nombre, lang, pagina in PAGINAS:
    wiki(nombre, lang, action="parse", page=pagina, prop="wikitext", redirects="1")
# Wikcionario: palabras del español que vienen del inglés (la categoría va por páginas de 500)
sigue, i = "", 0
while i < 12 and not (D3 / "anglicismos_fin").exists():
    ruta = D3 / f"anglicismos_{i}.json"
    if not ruta.exists():
        kw = dict(action="query", list="categorymembers", cmtitle="Categoría:ES:Palabras provenientes del inglés", cmlimit="500")
        if sigue: kw["cmcontinue"] = sigue
        wiki(f"anglicismos_{i}", "es", sitio="wiktionary", **kw)
    d = json.loads(ruta.read_text()) if ruta.exists() else {}
    sigue = d.get("continue", {}).get("cmcontinue", "")
    i += 1
    if not sigue: (D3 / "anglicismos_fin").write_text("ok"); break

for nombre, art in [("quevedo", "52iwsT98xCoGgiGntTiR7K"), ("onedirection", "4AK6F7OLvEQ5QYCBNiQWHq"), ("abba", "0LcJLqbBmaGUft1e9Mm8HV")]:
    baja(f"{nombre}_kworb.html", f"https://kworb.net/spotify/artist/{art}_songs.html", "Mozilla/5.0")
baja("podcasts_apple.json", "https://rss.applemarketingtools.com/api/v2/es/podcasts/top/100/podcasts.json")
baja("podcasts_itunes.json", "https://itunes.apple.com/es/rss/toppodcasts/limit=200/json")
baja("frecuencias_es.txt", "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/es/es_50k.txt")
baja("nombres_fecha_ine.xls", "https://www.ine.es/daco/daco42/nombyapel/nombres_por_fecha.xls")

# ── ampliación del 11 de octubre: que no se quede fuera ninguna respuesta buena ──
baja("palabras_todas.txt", "https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/main/0_palabras_todas.txt")
for g in (1301, 1321, 1303, 1304, 1483, 1511, 1512, 1487, 1305, 1502, 1310, 1489, 1314, 1533, 1324, 1545, 1309, 1318, 1488):
    baja(f"podcasts_{g}.json", f"https://itunes.apple.com/es/rss/toppodcasts/limit=200/genre={g}/json"); time.sleep(0.5)
for n, c in {
 "estadios_wd": q("?x wdt:P31/wdt:P279* wd:Q1154710 ; wdt:P17 wd:Q29 ."),
 "islas_todas": q("?x wdt:P31/wdt:P279* wd:Q23442 ; wdt:P17 wd:Q29 ."),
 "marvel_wd":   q("?x wdt:P1080 wd:Q931597 .", 3),
 "generos_todos": q("?x wdt:P31 wd:Q188451 .", 4),
 "doraemon_wd": q("?x wdt:P1441 wd:Q185143 ."),
 "lqsa_wd":     q("?x wdt:P1441 wd:Q2915669 ."),
}.items(): sparql(n, c)
wiki("lqsa_art", "es", action="parse", page="La que se avecina", prop="wikitext", redirects="1")
wiki("lqsa_pers", "es", action="parse", page="Anexo:Personajes de La que se avecina", prop="wikitext", redirects="1")
wiki("doraemon_en", "en", action="parse", page="List of Doraemon characters", prop="wikitext", redirects="1")
wiki("vinos_do", "es", action="parse", page="Anexo:Denominaciones de origen de España", prop="wikitext", redirects="1")
wiki("anexo_do_vino", "es", action="query", list="categorymembers", cmtitle="Categoría:Vinos de España con denominación de origen", cmlimit="500")
wiki("figuras_cat", "es", action="query", list="categorymembers", cmtitle="Categoría:Figuras retóricas", cmlimit="500")
wiki("unidades_cat", "es", action="query", list="categorymembers", cmtitle="Categoría:Unidades de medida", cmlimit="500")
for cat in ("Unidades de longitud", "Unidades de masa", "Unidades de volumen", "Unidades de tiempo", "Unidades de superficie", "Unidades de medida históricas",
            "Unidades de energía", "Unidades de presión", "Unidades de potencia", "Unidades de información", "Unidades de velocidad", "Unidades derivadas del Sistema Internacional"):
    wiki("unidades_" + cat.split()[-1].lower(), "es", action="query", list="categorymembers", cmtitle="Categoría:" + cat, cmlimit="500")
# Marvel: la categoría de superhéroes con sus subcategorías (dos niveles)
ruta = D3 / "marvel_cat2.json"
if not ruta.exists():
    def miembros(cat, ns):
        salida, sigue = [], ""
        while True:
            kw = dict(action="query", list="categorymembers", cmtitle=cat, cmlimit="500", cmnamespace=ns, format="json")
            if sigue: kw["cmcontinue"] = sigue
            d = json.load(urllib.request.urlopen(urllib.request.Request("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(kw), headers=UA), timeout=60))
            salida += [m["title"] for m in d["query"]["categorymembers"]]; sigue = d.get("continue", {}).get("cmcontinue", "")
            if not sigue: return salida
    cats, vistos, tit = ["Category:Marvel Comics superheroes"], set(), set()
    for nivel in range(3):
        nuevas = []
        for c in cats:
            if c in vistos: continue
            vistos.add(c); tit |= set(miembros(c, "0")); nuevas += miembros(c, "14")
        cats = nuevas
    ruta.write_text(json.dumps(sorted(tit), ensure_ascii=False)); print("marvel_cat2", len(tit))
# títulos en español: las redirecciones de cada artículo (El silencio de los corderos → The Silence of the Lambs)
def redirecciones(nombre, lang, titulos):
    ruta = D3 / f"{nombre}.json"
    if ruta.exists(): return
    salida = {}
    for i in range(0, len(titulos), 40):
        kw = dict(action="query", prop="redirects", rdlimit="500", titles="|".join(titulos[i:i + 40]), format="json")
        d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(kw), headers=UA), timeout=60))
        for p in d["query"]["pages"].values(): salida[p["title"]] = [r["title"] for r in p.get("redirects", [])]
        time.sleep(0.5)
    ruta.write_text(json.dumps(salida, ensure_ascii=False)); print(nombre, len(salida))
def arts(nombre):
    d = json.loads((D3 / f"{nombre}.json").read_text())["results"]["bindings"]
    return sorted({urllib.parse.unquote(f["art"]["value"].rsplit("/wiki/", 1)[1]).replace("_", " ") for f in d if "art" in f})
redirecciones("oscar_red", "es", arts("oscar"))
redirecciones("mario_red", "es", arts("mario"))
redirecciones("marvel_red", "es", arts("marvel_wd"))
# diccionario con formas conjugadas y plurales (para «cinco vocales» y «empieza por K»)
for u in ("https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/0_palabras_todas.txt",
          "https://raw.githubusercontent.com/lorenbrichter/Words/master/Words/es.txt"):
    baja("palabras_todas.txt", u)
# nombres en español de los superhéroes de Marvel (enlace a la Wikipedia en español de cada artículo en inglés)
ruta = D3 / "marvel_es.json"
if not ruta.exists():
    tit, salida = json.loads((D3 / "marvel_cat2.json").read_text()), {}
    for i in range(0, len(tit), 45):
        kw = dict(action="query", prop="langlinks", lllang="es", lllimit="500", titles="|".join(tit[i:i + 45]), format="json")
        d = json.load(urllib.request.urlopen(urllib.request.Request("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(kw), headers=UA), timeout=60))
        for p in d["query"]["pages"].values():
            if p.get("langlinks"): salida[p["title"]] = p["langlinks"][0]["*"]
        time.sleep(0.3)
    ruta.write_text(json.dumps(salida, ensure_ascii=False)); print("marvel_es", len(salida))
