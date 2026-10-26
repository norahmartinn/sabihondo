"""Quinta tanda (semana del 26 de octubre al 1 de noviembre de 2026).
Lo puesto a mano está en mano_t5.py; los datos en bruto, en datos/siete/fuentes/t5/ (los baja baja_tanda5.py).
Usa la misma maquinaria que tanda4.py: lo de mano manda y la fuente rellena la cola (niveles 3-5).
    python3 tanda5.py            → rehace todas
    python3 tanda5.py jdt barca  → solo esas"""
import tanda4
from tanda4 import *
import mano_t5

D5 = FUENTES / "t5"
# lo de la quinta tanda entra en las tablas de la cuarta, que es donde mira junta()
mano_t4.MANO.update(mano_t5.MANO)
for slug, niveles in mano_t5.EXTRA.items():
    for nv, texto in niveles.items():
        d = mano_t4.MAS.setdefault(slug, {})
        d[nv] = ", ".join(x for x in [d.get(nv, ""), texto] if x)
for slug, niveles in mano_t5.MAS.items():
    for nv, texto in niveles.items():
        d = mano_t4.MAS.setdefault(slug, {})
        d[nv] = ", ".join(x for x in [d.get(nv, ""), texto] if x)
for slug, alias in mano_t5.ALIAS.items(): mano_t4.ALIAS_MAS.setdefault(slug, {}).update(alias)

def wd5(nombre):
    viejo = tanda2.T2; tanda2.T2 = D5
    try: return wd(nombre)
    finally: tanda2.T2 = viejo
def texto5(nombre):
    return json.loads((D5 / f"{nombre}.json").read_text(encoding="utf-8"))["parse"]["wikitext"]["*"]
def cola5(nombre, niveles, minimo=0, fuera=None, minus=False, extra=None):
    """niveles: [(sitelinks mínimos, nivel)], de más a menos; lo que no llega a ninguno va al 5."""
    filas = []
    for r in wd5(nombre):
        n = SIN_PAREN(r["n"])
        if r["links"] < minimo or not LAT(n) or len(n) > 60 or not clave(n): continue
        if fuera and re.search(fuera, n, re.I): continue
        if minus and n[:1].isupper() and not r["f"].get("xLabel"): continue
        al = [SIN_PAREN(a) for a in r["alts"][:5]] + ([SIN_PAREN(r["en"])] if r["en"] and LAT(r["en"]) else [])
        if extra: al += extra(n)
        nv = next((v for m, v in niveles if r["links"] >= m), 5)
        filas.append((n, al, nv, r["links"]))
    return filas

cobros_aerolineas, cuerpo_uno, pixar, inditex, poker, mus, presidentes, cafes, sin_pelota, mascotas_famosas, frutas, verduras, \
    platos_ccaa, maquillaje, ruedas, hospital, canciones_disney, cuadros = solo_mano(
    "cobros_aerolineas", "cuerpo_uno", "pixar", "inditex", "poker", "mus", "presidentes", "cafes", "sin_pelota", "mascotas_famosas",
    "frutas", "verduras", "platos_ccaa", "maquillaje", "ruedas", "hospital", "canciones_disney", "cuadros")

def jdt():
    fuera = r"^(Casa |lenguas?|Guerra|Batalla|Rebeli|Poniente|Essos|Invernalia|Desembarco|Muro|Dothraki|Guardia|Hermandad|Fe de|Orden|Compañía|huargo|dragón$|Inmaculados|Segundos Hijos|Hombres sin Rostro|Banco de Hierro|Ciudadela|Torre|Danza)"
    junta("jdt", cola5("jdt", [(10, 4)], fuera=fuera, extra=lambda n: [n.split()[0]] if " " in n and len(n.split()[0]) > 3 else []), "enlaces_wikipedia")

def disney_channel():
    cola = []
    for t in re.findall(r"''\[\[([^]|]+)(?:\|([^]]+))?\]\]''", texto5("disney_channel_en")):
        n = SIN_PAREN(t[1] or t[0])
        if 2 < len(n) < 60 and LAT(n): cola.append((n, [], 5, 0))
    junta("disney_channel", cola, "orden_a_mano")

def netflix():
    junta("netflix", cola5("netflix", [(40, 3), (12, 4)], minimo=3), "enlaces_wikipedia")

def barca():
    apellido = lambda n: [n.split()[-1]] if " " in n and len(n.split()[-1]) > 4 else []
    junta("barca", cola5("barca", [(45, 3), (15, 4)], minimo=4, extra=apellido), "enlaces_wikipedia")

INSTRUMENTO_FUERA = (r"micr[oó]fono|altavoz|Big Ben|multimedia|peonza|instrumento|soprano|tenor|bar[ií]tono|contralto|mezzo|auricular|diapas[oó]n|"
                     r"fon[oó]grafo|gram[oó]fono|beatbox|Adobe|Spinner|cuerda$|caja$|idi[oó]fono|membran[oó]fono|aer[oó]fono|cord[oó]fono|electr[oó]fono|"
                     r"voz|software|programa|campanario|reloj|sirena|bocina|claxon|altoparlante|amplificador|pedal|p[uú]a|arco$|baqueta|metr[oó]nomo|"
                     r"partitura|atril|af?inador|grabadora|tocadiscos|radio|tel[eé]fono|\d")
def instrumentos():
    junta("instrumentos", cola5("instrumentos", [(30, 4)], minimo=8, minus=True, fuera=INSTRUMENTO_FUERA), "enlaces_wikipedia")

def juegos_mesa():
    junta("juegos_mesa", cola5("juegos_mesa", [(30, 3), (10, 4)], minimo=3, fuera=r"GNU|software|programa|\bvideo"), "enlaces_wikipedia")

CRIATURA_FUERA = r"Jes[uú]s|Hagrid|Godzilla|Goliat|Arjuna|^Io$|Cupido|arcángel|Arcángel|Satan|Lucifer|Iblís|Prometeo|Heracles|Perseo|Mnem|Leto$"
def criaturas():
    junta("criaturas", cola5("criaturas", [(60, 4)], minimo=12, fuera=CRIATURA_FUERA), "enlaces_wikipedia")

def gentilicios():
    filas, vistos = [], set()
    datos = json.loads((D5 / "gentilicios.json").read_text(encoding="utf-8"))["results"]["bindings"]
    pob = {}
    for f in datos:
        g = f["g"]["value"].strip(); p = float(f.get("pob", {}).get("value", 0) or 0)
        if not LAT(g) or not g.islower() or len(g) > 30: continue
        pob[g] = max(pob.get(g, 0), p)
    for g, p in sorted(pob.items(), key=lambda x: -x[1]):
        filas.append((g, [], 3 if p >= 300_000 else 4 if p >= 20_000 else 5, int(p)))
    junta("gentilicios", filas, "poblacion")

def badbunny():
    base = lambda t: re.sub(r"\s+-\s+.*$", "", re.sub(r"\s*[\(\[].*$", "", html.unescape(t))).strip()
    filas = {}
    for titulo, n in re.findall(r'<tr><td class="text"><div>(?:\*\s*)?<a[^>]*>(.*?)</a></div></td><td>([\d,]+)</td>', (D5 / "badbunny_kworb.html").read_text(encoding="utf-8")):
        b = base(titulo).replace("’", "'"); k = clave(b)
        if not k or "Halftime" in b: continue
        d = filas.setdefault(k, [b, 0]); d[1] += int(n.replace(",", ""))
    orden = sorted(filas.values(), key=lambda f: -f[1])
    junta("badbunny", por_puesto([(n, [], v) for n, v in orden], [12, 35, 80, 150]), "reproducciones_spotify")

def palabras_w(): por_frecuencia("palabras_w", lambda p: p.startswith("w"), formas=True)
def doble_rr(): por_frecuencia("doble_rr", lambda p: "rr" in p, formas=True)
def cion(): por_frecuencia("cion", lambda p: p.endswith("ción"), formas=True)

def pelis2026():
    """Estrenos de 2026 en EE. UU. (sin las que solo salieron en plataformas) y películas españolas de 2026, hasta el 24 de octubre."""
    fino = lambda t: re.sub(r"\s*\((?:película|film)[^)]*\)", "", t or "").strip()
    wdp = json.loads((D5 / "pelis2026_wd.json").read_text(encoding="utf-8"))
    cola = []
    for mes, dia, art, tit, comp in json.loads((D5 / "pelis2026_lista.json").read_text(encoding="utf-8")):
        v = wdp.get(art, {})
        es = fino(v.get("es")) or fino(v.get("eswiki")) or fino(tit)
        al = [fino(tit), fino(v.get("eswiki"))] + v.get("alias", [])
        l = v.get("links", 0)
        cola.append((es, [a for a in al if a], 3 if l >= 25 else 4 if l >= 12 else 5, l))
    vistos = {}
    for f in json.loads((D5 / "pelis2026_espana.json").read_text(encoding="utf-8"))["results"]["bindings"]:
        n = fino(f["xLabel"]["value"]); fecha = f["fecha"]["value"][:10]
        if QID.match(n) or fecha > "2026-10-24": continue
        if n not in vistos: vistos[n] = (int(f["l"]["value"]), fino(f.get("en", {}).get("value")))
    for n, (l, en) in vistos.items():
        cola.append((n, [en] if en else [], 3 if l >= 10 else 4 if l >= 4 else 5, l))
    junta("pelis2026", cola, "enlaces_wikipedia")

bruja_cuento, vampiro, hombre_lobo, tim_burton, monedas_euro, porcentajes, golpear_pelota = solo_mano(
    "bruja_cuento", "vampiro", "hombre_lobo", "tim_burton", "monedas_euro", "porcentajes", "golpear_pelota")
paises_africa, playa, sabores_patatas, bolsos, camping = solo_mano("paises_africa", "playa", "sabores_patatas", "bolsos", "camping")
for _s in ("playa", "sabores_patatas"): mano_t4.REPARTE.setdefault(_s, {})[3] = [3, 4, 5]
mano_t4.REPARTE["paises_africa"] = {2: [2, 3, 4], 3: [5]}     # los menos conocidos y los que ya no existen, a joya
for _s in ("bruja_cuento", "vampiro", "hombre_lobo", "porcentajes"): mano_t4.REPARTE.setdefault(_s, {})[3] = [3, 4, 5]   # lo menos dicho, a joya
for _s in ("tim_burton", "monedas_euro", "golpear_pelota"): mano_t4.REPARTE.setdefault(_s, {})[4] = [4, 5]
def terror_halloween():
    """Las de «Nombra una película de miedo» (tanda 2, ya jugada el 11 de octubre) más las de Halloween puestas a mano."""
    import csv as _csv
    filas = [(f["respuesta"], [a for a in f["alias"].split("|") if a], int(f["nivel"]), float(f["ediciones_wikipedia"] or 0))
             for f in _csv.DictReader(open(DATOS / "miedo.csv", encoding="utf-8"), delimiter=";")]
    junta("terror_halloween", filas, "ediciones_wikipedia")

TODAS5 = [cobros_aerolineas, cuerpo_uno, jdt, disney_channel, netflix, pixar, badbunny, canciones_disney, instrumentos, frutas, verduras,
          cafes, platos_ccaa, inditex, maquillaje, juegos_mesa, poker, mus, barca, palabras_w, gentilicios, doble_rr, cion, criaturas,
          mascotas_famosas, presidentes, cuadros, ruedas, hospital, pelis2026, sin_pelota, terror_halloween, bruja_cuento, vampiro, hombre_lobo, tim_burton, monedas_euro, porcentajes, golpear_pelota, paises_africa, playa, sabores_patatas, bolsos, camping]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS5:
        if not pedidas or f.__name__ in pedidas: f()
