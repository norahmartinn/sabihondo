"""Tercera tanda de preguntas (semana del 12 al 18 de octubre de 2026): 50 bancos.

Como en tanda2.py: la lista de respuestas válidas sale de una fuente bajada por baja_tanda3.py
(datos/siete/fuentes/tanda3/) y los niveles de lo más conocido en España van a mano en mano_t3.py.
Las que no tienen base de datos posible (zonas de una casa, formas de decir dinero…) son solo a mano.

Uso:  python3 scripts/siete/tanda3.py [slug …]     (sin argumentos, todas; nombres_* necesitan xlrd)"""
import sys, html
import tanda2
from tanda2 import *
import mano_t3
tanda2.MANO.update(mano_t3.MANO); tanda2.REPARTE.update(mano_t3.REPARTE)
D3 = FUENTES / "tanda3"

def wd3(nombre):
    viejo = tanda2.T2; tanda2.T2 = D3
    try: return wd(nombre)
    finally: tanda2.T2 = viejo
def texto3(nombre):
    return json.loads((D3 / f"{nombre}.json").read_text(encoding="utf-8"))["parse"]["wikitext"]["*"]
LAT = lambda t: not re.search(r"[^\x00-ɏ’'·]", t)

# Formas en que la gente escribe lo mismo: «Parador de León», «isla de Tabarca», «salsa brava»… (se añaden como alias a lo puesto a mano)
VARIANTES = {
 "islas": ["isla {}", "islas {}", "illa {}"], "festivales": ["festival {}", "{} festival", "festival internacional {}"],
 "universidades": ["universidad {}", "universitat {}"], "estadios": ["estadio {}", "campo {}", "nuevo {}", "estadio municipal {}"],
 "salsas": ["salsa {}"], "pizza": ["pizza {}"], "barrios_madrid": ["barrio {}"], "paradores": ["parador {}", "parador nacional {}"],
 "aeropuertos": ["aeropuerto {}"], "senales": ["señal {}"], "ministerios": ["ministerio {}"], "vinos": ["vino {}", "denominación de origen {}", "do {}"],
 "generos": ["música {}"], "impuestos": [], "aerolineas": ["{} airlines", "{} airways"],
}
def junta2(slug, cola, metrica):
    """Como junta(), pero con las variantes de arriba y descartando de la cola todo lo que ya esté a mano bajo cualquiera de sus formas."""
    mano = [(n, al + [v.format(x) for x in [n] + al for v in VARIANTES.get(slug, [])], nv, val) for n, al, nv, val in a_mano(slug)]
    ya = {clave(x) for n, al, _, _ in mano for x in [n] + al}
    guarda(slug, mano + [f for f in cola if clave(f[0]) and not ({clave(f[0])} | {clave(a) for a in f[1]}) & ya], metrica)
junta = junta2

def solo_mano(*slugs):
    def crea(slug):
        def f(): junta(slug, [], "orden_a_mano")
        f.__name__ = slug; return f
    return [crea(s) for s in slugs]
casa, orientaciones, olimpicos, logo_animal, unidades, griego, tiempos, dinero, partidos, impuestos, bollos, snacks, lqsa, doraemon, gen27, \
    figuras, senales, patrimonio, ministerios, aeropuertos, estados_eeuu, vinos = solo_mano(
    "casa", "orientaciones", "olimpicos", "logo_animal", "unidades", "griego", "tiempos", "dinero", "partidos", "impuestos", "bollos", "snacks",
    "lqsa", "doraemon", "gen27", "figuras", "senales", "patrimonio", "ministerios", "aeropuertos", "estados_eeuu", "vinos")

# ── canciones: todo lo que el artista tiene en Spotify (kworb.net), ordenado por reproducciones ──
def canciones(slug, cortes, extra={}):
    base = lambda t: re.sub(r"\s+-\s+.*$", "", re.sub(r"\s*[\(\[].*$", "", html.unescape(t))).strip()
    filas = {}
    for titulo, n in re.findall(r'<tr><td class="text"><div>(?:\*\s*)?<a[^>]*>(.*?)</a></div></td><td>([\d,]+)</td>', (D3 / f"{slug}_kworb.html").read_text(encoding="utf-8")):
        b = base(titulo); k = clave(b)
        if not k: continue
        d = filas.setdefault(k, [b, 0]); d[1] += int(n.replace(",", ""))
    orden = sorted(filas.values(), key=lambda f: -f[1])
    junta(slug, por_puesto([(extra.get(n, [n])[0], extra.get(n, [n])[1:] + ([n] if n in extra else []), v) for n, v in orden], cortes), "reproducciones_spotify")
def quevedo():
    canciones("quevedo", [5, 14, 30, 55], {"Quevedo: Bzrp Music Sessions, Vol. 52/66": ["Quédate", "Bzrp Music Sessions 52", "Session 52", "Sesión 52", "Bizarrap", "Quevedo: Bzrp Music Sessions", "Bzrp Music Sessions"]})
def onedirection(): canciones("onedirection", [6, 16, 35, 60])
def abba(): canciones("abba", [7, 18, 40, 75])

def marvel():
    cola = [(SIN_PAREN(t), [], 5, 0) for t in json.loads((D3 / "marvel_cat.json").read_text()) if not t.startswith("List")]
    junta("marvel", cola, "orden_a_mano")

def oscar():
    filas = wd3("oscar")
    vis = visitas("es", [r["art"] for r in filas if r["art"]], "tanda3/oscar_visitas.json")
    filas.sort(key=lambda r: -(vis.get(r["art"]) or 0))
    # el título en español es el del artículo de la Wikipedia en español
    junta("oscar", por_puesto([(SIN_PAREN(r["art"]) or r["n"], [r["n"], r["en"]] + r["alts"][:4], vis.get(r["art"]) or 0) for r in filas], [0, 22, 48, 74]), "visitas_wikipedia_es")

def festivales():
    cola = [(r["n"], r["alts"][:3], 5, r["links"]) for r in wd3("festivales") if r["art"] and LAT(r["n"])
            and not re.search(r"cine|film|teatro|eurovisi|concurso|benidorm fest|premio|ópera|danza|certamen", r["n"], re.I)]
    junta("festivales", cola, "ediciones_wikipedia")

def generos():
    cola = [(r["n"], r["alts"][:3] + [r["en"]], 4 if r["links"] >= 60 else 5, r["links"]) for r in wd3("generos") if r["links"] >= 25 and LAT(r["n"])]
    junta("generos", cola, "ediciones_wikipedia")

def estadios():
    cola, t = [], texto3("estadios")
    filas = [re.split(r"\|\|", f) for f in re.findall(r"\n\|\d+\s*\|\|[^\n]*", t)]
    # la columna de la foto falta en media tabla: el estadio es el primer enlace de la fila que no sea una imagen
    for i, m in enumerate(x for x in (re.search(r"\[\[(?!Archivo)([^\]|]+)(?:\|([^\]]+))?\]\]", "||".join(c[1:3])) for c in filas if len(c) > 2) if x):
        n = (m.group(2) or m.group(1)).strip()
        corto = re.sub(r"^(Nuevo\s+)?(Estadio|Campo|Estadi|Camp)\s+(Municipal\s+)?(de\s+Fútbol\s+)?(de\s+la\s+|de\s+los\s+|de\s+|del\s+|d')?", "", SIN_PAREN(n)).strip()
        cola.append((SIN_PAREN(n), [corto, SIN_PAREN(m.group(1))], 4 if i < 45 else 5, 200 - i))
    junta("estadios", cola, "puesto_por_aforo")

def cola_comida(nombre, minimo=0):
    return [(r["n"], r["alts"][:4] + [r["en"]], 5, r["links"]) for r in wd3(nombre) if r["art"] and r["links"] >= minimo and LAT(r["n"]) and len(r["n"]) < 40]
def pasta():
    lista = texto3("pasta_en").lower()             # solo lo que también está en la lista de pastas de la Wikipedia en inglés
    junta("pasta", [f for f in cola_comida("pasta") if any(x and x.lower() in lista for x in [f[0]] + f[1][-1:])], "ediciones_wikipedia")
def salsas(): junta("salsas", [(re.sub(r"^salsa\s+(de\s+)?", "", n) if False else n, al + ([re.sub(r"^salsa\s+(de\s+|a la\s+)?", "", n, flags=re.I)] if n.lower().startswith("salsa ") else []), nv, v)
                              for n, al, nv, v in cola_comida("salsas", 4)
                              if n.lower().startswith(("salsa", "mojo", "alioli")) or any(x and x.lower() in texto3("salsas_en").lower() for x in al[-1:])], "ediciones_wikipedia")
def pizza(): junta("pizza", [(re.sub(r"^pizza\s+(a la\s+|al\s+|de\s+)?", "", n, flags=re.I) or n, al + [n], nv, v) for n, al, nv, v in cola_comida("pizza")
                             if not re.search(r"hut|domino|telepizza|papa john|little caesars|pizzer|express|\binn\b|company|horno|cortador|caja", n, re.I)], "ediciones_wikipedia")

def islas():
    cola = []
    for r in wd3("islas"):
        if not r["art"] or not LAT(r["n"]): continue
        corto = re.sub(r"^(isla|islote|illa|illot|islas|illes|peñón)\s+(de\s+la\s+|de\s+los\s+|de\s+las\s+|de\s+|del\s+|d'|des\s+|de\s+sa\s+|d'en\s+)?", "", r["n"], flags=re.I).strip()
        cola.append((r["n"], r["alts"][:3] + ([corto] if len(clave(corto)) > 3 else []), 5, r["links"]))
    junta("islas", cola, "ediciones_wikipedia")

def aerolineas():
    cola = [(r["n"], r["alts"][:3] + [r["en"]], 4 if r["links"] >= 40 else 5, r["links"]) for r in wd3("aerolineas") if LAT(r["n"])]
    junta("aerolineas", cola, "ediciones_wikipedia")

def barrios_madrid():
    t = texto3("barrios_anexo")
    cola = [(SIN_PAREN(m.group(2) or m.group(1)), [], 5, 0) for m in re.finditer(r'\n\|\s*align="center"\s*\|\s*\[\[(?!Archivo)([^\]|]+)(?:\|([^\]]+))?\]\]', t)]
    cola += [(m.group(1).strip(), [], 3, 1) for m in re.finditer(r"\[\[Distrito[^\]|]*\|([^\]]+)\]\]", t)]
    junta("barrios_madrid", cola, "orden_a_mano")

def universidades():
    cola = []
    for m in re.finditer(r"\n\|\s*(?:rowspan[^|]*\|[^\n]*\n\|\s*)?\[\[((?:Universi|Mondragon|IE |ESIC|CUNEF)[^\]|]*)(?:\|([^\]]*))?\]\]", texto3("universidades")):
        n = SIN_PAREN(m.group(2) or m.group(1)).strip()
        corto = re.sub(r"^(Universidad|Universitat|Universidade)\s+(Católica\s+)?(de\s+las\s+|de\s+la\s+|de\s+los\s+|de\s+|del\s+|d')?", "", n).strip()
        cola.append((n, [corto] if len(clave(corto)) > 3 else [], 5, 0))
    junta("universidades", cola, "orden_a_mano")

def mario():
    cola = []
    for m in re.finditer(r"''\[\[([^\]]+)\]\]''", texto3("mario_es")):
        n = SIN_PAREN(m.group(1).split("|")[-1]).strip()
        if re.search(r"mario|luigi|yoshi|wario|peach|toad|donkey kong", n, re.I): cola.append((n, [], 5, 0))
    cola += [(r["n"], [r["en"]] + r["alts"][:2], 5, r["links"]) for r in wd3("mario") if LAT(r["n"])]
    junta("mario", cola, "orden_a_mano")

def anglicismos():
    cola = []
    for f in sorted(D3.glob("anglicismos_*.json")):
        for m in json.loads(f.read_text()).get("query", {}).get("categorymembers", []):
            t = m["title"]
            # de la categoría solo entran las que siguen pareciendo inglés (boicot o túnel también vienen de ahí, pero nadie las siente inglesas)
            if m["ns"] == 0 and re.fullmatch(r"[a-záéíóúüñ'-]{3,18}", t) and re.search(r"w|k|sh|ck|oo|ee|th|gh|ing$|y$|[bcdfgkmptz]$", t): cola.append((t, [], 5, 0))
    junta("anglicismos", cola, "categoria_wikcionario")

# ── palabras: lemario (el de la segunda tanda) y lista de frecuencias de OpenSubtitles ──
def _palabras():
    lema = {x.strip().lower() for x in open(FUENTES / "t2" / "palabras.txt", encoding="utf-8", errors="replace") if x.strip()}
    frec = {}
    for i, linea in enumerate(open(D3 / "frecuencias_es.txt", encoding="utf-8")):
        p = linea.split()
        if p: frec[p[0]] = i
    return lema, frec
def cinco_vocales():
    lema, frec = _palabras()
    sin = lambda s: "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    vale = lambda p: re.fullmatch(r"[a-záéíóúüñ]{5,}", p) and set("aeiou") <= set(sin(p))
    mano = ["murciélago", "euforia", "educación", "abuelito", "auténtico"]
    comunes = sorted((p for p in lema if vale(p) and p in frec and p not in mano), key=lambda p: frec[p])
    resto = sorted(p for p in lema if vale(p) and p not in frec and p not in mano)
    filas = [(p, [], 1, 10**6) for p in mano]
    filas += [(p, [], 2 + (i * 3 // len(comunes)), 10**5 - frec[p]) for i, p in enumerate(comunes)]
    filas += [(p, [], 5, 0) for p in resto]
    guarda("cinco_vocales", filas, "frecuencia_de_uso")
def palabras_k():
    lema, frec = _palabras()
    cola = [(p, [], 4 if p in frec else 5, 10**5 - frec.get(p, 10**5)) for p in lema if re.fullmatch(r"k[a-záéíóúüñ]{2,}", p)]
    junta("palabras_k", cola, "frecuencia_de_uso")

# ── nombres del INE ──
ACENTOS = {x.upper().translate(str.maketrans("ÁÉÍÓÚÈ", "AEIOUE")): x for x in """José María Jesús Ángel Ángeles Andrés Ramón Martín Tomás Julián Joaquín Sebastián
 Inés Belén Concepción Encarnación Asunción Rocío Mónica Lucía Sofía Rosalía Ángela Raúl Iván Rubén Adrián Álvaro Óscar Víctor Héctor César Félix Simón
 Agustín Benjamín Fermín Valentín Nicolás Matías Elías Moisés Noé Salomé Noemí Purificación Anunciación Mercè Fátima Verónica Bárbara Débora África
 Águeda Germán Fabián Damián Cristóbal Bartolomé Teófilo Máximo Cándido Cándida América Aníbal Isaías Jeremías Efrén León Darío Resurrección Ascensión
 Presentación Consolación Estefanía Íñigo Míriam Nélida Aarón Abrahán Julián Joaquín Jerónimo Gerónimo Hipólito Crisóstomo Plácido Régulo Rómulo Eloísa
 Lázaro Zacarías Tobías Jonás Ginés""".split()}
def bonito(n):
    return " ".join(ACENTOS.get(p, p.capitalize()) for p in n.split())
def nombres_bebes():
    import xlrd
    libro = xlrd.open_workbook(D3 / "nombres_fecha_ine.xls")
    filas = []
    for hoja in libro.sheets()[1:3]:
        cab = hoja.row_values(3)
        col = max(i for i, c in enumerate(cab) if isinstance(c, str) and c.strip())        # la última franja: los nacidos más recientes
        print("  ", hoja.name, "→", cab[col])
        for i in range(5, hoja.nrows):
            f = hoja.row_values(i)
            if isinstance(f[0], float) and isinstance(f[col], str) and f[col].strip():
                filas.append((bonito(f[col].strip()), [], nivel_por_puesto(int(f[0]), [5, 15, 30, 42]), f[col + 1]))
    guarda("nombres_bebes", filas, "bebes_con_ese_nombre_ine")
def nombres_compuestos():
    import xlrd
    filas = []
    for hoja in xlrd.open_workbook(FUENTES / "t2" / "nombres_ine.xls").sheets():
        for i in range(7, hoja.nrows):
            f = hoja.row_values(i)
            if isinstance(f[1], str) and " " in f[1].strip() and isinstance(f[2], float) and f[2] >= 1000: filas.append((bonito(f[1].strip()), [], f[2]))
    filas.sort(key=lambda f: -f[2])
    guarda("nombres_compuestos", por_puesto(filas, [10, 35, 110, 300]), "personas_con_ese_nombre_ine")

def podcasts():
    d = json.loads((D3 / "podcasts_itunes.json").read_text(encoding="utf-8"))["feed"]["entry"]
    cola = []
    for i, e in enumerate(d, 1):
        n = html.unescape(e["im:name"]["label"]).strip()
        corto = re.split(r"\s+[-–|:]\s+|\s+\|\s*|\s+con\s+|\s+by\s+", n)[0].strip()
        if re.search(r"\b(english|news|daily|bbc|ted talks|the rest is|minute)\b", n, re.I): continue      # los que no son en español
        cola.append((corto if len(clave(corto)) >= 4 else n, [n], nivel_por_puesto(i, [0, 0, 60, 130]), 201 - i))
    junta("podcasts", cola, "puesto_en_apple_podcasts")

def paradores():
    cola = [(p["nombre"], [], 4, 0) for p in json.loads((D3 / "paradores.json").read_text(encoding="utf-8"))]
    oficiales = {clave(p[0]) for p in cola}
    for n, al, _, _ in a_mano("paradores"):
        if not ({clave(n)} | {clave(a) for a in al}) & oficiales: print("  ojo, no está en la lista oficial:", n)
    junta("paradores", cola, "orden_a_mano")

# ── países: nombres, alias y orden de «conocidos» salen de paises.csv (segunda tanda) ──
def lista_paises(slug, niveles):
    tabla, orden = {}, {}
    with open(DATOS / "paises.csv", encoding="utf-8") as f:
        for i, fila in enumerate(csv.DictReader(f, delimiter=";")):
            al = [a for a in fila["alias"].split("|") if a]
            for x in [fila["respuesta"]] + al: tabla[clave(x)] = (fila["respuesta"], al); orden[clave(x)] = i
    filas, auto = [], []
    for nv, texto in niveles.items():
        for n in [x.strip() for x in texto.replace("\n", " ").split(",") if x.strip()]:
            if clave(n) not in tabla: print("  ojo, no está en paises.csv:", n)
            nombre, al = tabla.get(clave(n), (n, []))
            (auto if nv == 0 else filas).append((nombre, al, nv, 1000 - orden.get(clave(n), 999)))
    auto.sort(key=lambda f: -f[3])
    filas += [(n, al, 3 + min(2, i * 3 // len(auto)), v) for i, (n, al, _, v) in enumerate(auto)]
    guarda(slug, filas, "puesto_por_visitas")
def sin_mar(): lista_paises("sin_mar", mano_t3.SIN_MAR)
def paises_isla(): lista_paises("paises_isla", mano_t3.ISLA)
def verde_bandera(): lista_paises("verde_bandera", mano_t3.VERDE)
def frontera_afganistan(): lista_paises("frontera_afganistan", mano_t3.AFGANISTAN)
def frontera_kenia(): lista_paises("frontera_kenia", mano_t3.KENIA)

TODAS3 = [casa, orientaciones, olimpicos, logo_animal, unidades, griego, tiempos, dinero, partidos, impuestos, bollos, snacks, lqsa, doraemon, gen27,
          figuras, senales, patrimonio, ministerios, aeropuertos, estados_eeuu, vinos, quevedo, onedirection, abba, marvel, oscar, festivales, generos,
          estadios, pasta, salsas, pizza, islas, aerolineas, barrios_madrid, universidades, mario, anglicismos, cinco_vocales, palabras_k,
          nombres_bebes, nombres_compuestos, podcasts, paradores, sin_mar, paises_isla, verde_bandera, frontera_afganistan, frontera_kenia]
if __name__ == "__main__":
    for f in TODAS3:
        if len(sys.argv) > 1 and f.__name__ not in sys.argv[1:]: continue
        try: f()
        except Exception as e: print(f"!! {f.__name__}: {type(e).__name__}: {e}")
