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
 "generos": ["música {}"], "palabras_k": ["{}s", "{}es"], "impuestos": [], "aerolineas": ["{} airlines", "{} airways"],
}
def trozos(texto):
    for x in texto.replace("\n", " ").split(","):
        n, *al = [p.strip() for p in x.split("=")]
        if n: yield n, al
def junta2(slug, cola, metrica):
    """Como junta(), pero con las variantes de arriba, los alias de más y la ampliación de mano_t3 (nivel 5),
    y descartando de la cola todo lo que ya esté a mano bajo cualquiera de sus formas."""
    mas = {clave(k): [a.strip() for a in v.split(",")] for k, v in mano_t3.ALIAS_MAS.get(slug, {}).items()}
    fuera_mano = {clave(n) for n, _ in trozos(mano_t3.QUITA_MANO.get(slug, ""))}
    mano = []
    for n, al, nv, val in a_mano(slug):
        if clave(n) in fuera_mano: continue
        al = al + mas.pop(clave(n), [])
        mano.append((n, al + [v.format(x) for x in [n] + al for v in VARIANTES.get(slug, [])], nv, val))
    if mas: print("  ojo, alias de más sin dueño:", list(mas))
    ya = {clave(x) for n, al, _, _ in mano for x in [n] + al}
    quita = {clave(n) for n, _ in trozos(mano_t3.QUITA.get(slug, ""))}
    cola = [(n, al + [v.format(n) for v in VARIANTES.get(slug, [])], mano_t3.NIVEL_AMPLIA.get(slug, 5), 0) for n, al in trozos(mano_t3.AMPLIA.get(slug, "")) if clave(n) not in quita] + list(cola)
    # de la cola no se tira la fila entera si choca un alias: solo se le quitan las formas que ya tienen dueño
    limpia = []
    for n, al, nv, val in cola:
        if not clave(n) or clave(n) in ya: continue
        limpia.append((n, [a for a in al if a and clave(a) not in ya], nv, val))
    guarda(slug, mano + limpia, metrica)
junta = junta2

def solo_mano(*slugs):
    def crea(slug):
        def f(): junta(slug, [], "orden_a_mano")
        f.__name__ = slug; return f
    return [crea(s) for s in slugs]
casa, orientaciones, olimpicos, logo_animal, griego, tiempos, dinero, partidos, impuestos, bollos, snacks, gen27, \
    senales, patrimonio, ministerios, estados_eeuu = solo_mano(
    "casa", "orientaciones", "olimpicos", "logo_animal", "griego", "tiempos", "dinero", "partidos", "impuestos", "bollos", "snacks",
    "gen27", "senales", "patrimonio", "ministerios", "estados_eeuu")

def categoria3(nombre):
    d = json.loads((D3 / f"{nombre}.json").read_text(encoding="utf-8"))
    return [m["title"] for m in d.get("query", {}).get("categorymembers", []) if m["ns"] == 0]
def lqsa():
    """Todo el reparto que lista el artículo de la Wikipedia, temporada a temporada: «como ''Nombre Apellido Apellido''»."""
    cola, vistos = [], set()
    for bruto in re.findall(r"como\s+'{2,}(.*?)'{2,}", texto3("lqsa_art")):
        n = re.sub(r"\s*\(.*?\)|\[\[|\]\]|<[^>]+>", "", bruto).strip(" .,'")
        n = re.sub(r"\s+", " ", n)
        if not 2 < len(n) < 60 or clave(n) in vistos: continue
        vistos.add(clave(n))
        mote = re.findall(r"[«\"“]([^»\"”]+)[»\"”]", n)
        limpio = re.sub(r"\s*[«\"“][^»\"”]+[»\"”]\s*", " ", n).strip()
        p = limpio.split() or [n]
        formas = mote + [limpio, p[0], " ".join(p[:2])] + ([mote[0] + " " + p[-2]] if mote and len(p) > 2 else [])
        cola.append((limpio if len(p) > 1 else n, [f for f in formas if len(clave(f)) > 2], 5, 0))
    junta("lqsa", cola, "orden_a_mano")
def doraemon():
    cola = [(r["n"], r["alts"] + [r["en"]], 5, 0) for r in wd3("doraemon_wd") if LAT(r["n"])]
    cola += [(re.sub(r'\s*"[^"]*"\s*', " ", h).strip(), re.findall(r'"([^"]+)"', h), 5, 0) for h in re.findall(r"^=+\s*(.*?)\s*=+$", texto3("doraemon_en"), re.M)
             if h not in ("Main characters", "Supporting characters", "Minor characters", "References", "See also", "External links")]
    junta("doraemon", cola, "orden_a_mano")
def vinos():
    cola = [(SIN_PAREN(t), [], 5, 0) for t in categoria3("anexo_do_vino") if not t.startswith(("Anexo", "Vino de Calidad"))]
    junta("vinos", cola, "orden_a_mano")
def figuras():
    junta("figuras", [(SIN_PAREN(t)[0].lower() + SIN_PAREN(t)[1:], [], 5, 0) for t in categoria3("figuras_cat") if not t.startswith(("Anexo", "Figura"))], "orden_a_mano")
def unidades():
    cola = []
    for f in sorted(D3.glob("unidades_*.json")):
        cola += [(SIN_PAREN(t)[0].lower() + SIN_PAREN(t)[1:], [], 5, 0) for t in categoria3(f.stem) if not t.startswith(("Anexo", "Unidad", "Sistema", "Prefijo", "Metrolog"))]
    # los múltiplos y submúltiplos del sistema métrico
    for pre in "kilo hecto deca deci centi mili micro nano pico femto mega giga tera peta".split():
        for u in "metro gramo litro segundo vatio voltio amperio hercio julio pascal newton ohmio byte bit caloría tonelada faradio".split():
            cola.append((pre + u, [], 5, 0))
    junta("unidades", cola, "orden_a_mano")
def aeropuertos():
    cola = []
    for fila in re.split(r"\n\|-", texto3("aeropuertos")):
        c = [limpia_wiki(x).strip() for x in fila.split("\n|")[1:4]]
        if len(c) == 3 and c[0] and LAT(c[0]) and len(c[0]) < 60:
            ciudad = re.split(r",|\(|<br", c[2])[0].strip()
            cola.append((SIN_PAREN(c[0]), [x for x in (c[1], ciudad) if 2 < len(x) < 40 and LAT(x)], 5, 0))
    junta("aeropuertos", cola, "orden_a_mano")

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
    canciones("quevedo", [5, 14, 30, 55], {"Quevedo: Bzrp Music Sessions, Vol. 52/66": ["Quédate", "Bzrp Music Sessions 52", "Session 52", "Sesión 52", "Bizarrap", "Bzrp", "Bzrp Session", "Bizarrap Session", "Quevedo Bzrp", "Sesión con Bizarrap", "Quédate Bzrp", "Quevedo: Bzrp Music Sessions", "Bzrp Music Sessions"]})
def onedirection(): canciones("onedirection", [6, 16, 35, 60])
def abba(): canciones("abba", [7, 18, 40, 75])

def marvel():
    es = json.loads((D3 / "marvel_es.json").read_text())
    cola = [(SIN_PAREN(es.get(t, t)), [SIN_PAREN(t)], 5, 0) for t in json.loads((D3 / "marvel_cat2.json").read_text())
            if not t.startswith(("List", "Alternative versions", "Marvel Comics")) and " in other media" not in t and ":" not in t and not re.search(r"\d{4}", t)]
    junta("marvel", cola, "orden_a_mano")

def oscar():
    filas = wd3("oscar")
    vis = visitas("es", [r["art"] for r in filas if r["art"]], "tanda3/oscar_visitas.json")
    filas.sort(key=lambda r: -(vis.get(r["art"]) or 0))
    # el título en español es el del artículo de la Wikipedia en español
    red = json.loads((D3 / "oscar_red.json").read_text())           # las redirecciones traen el título con que se estrenó en España
    junta("oscar", por_puesto([(SIN_PAREN(r["art"]) or r["n"], [r["n"], r["en"]] + r["alts"] + [SIN_PAREN(x) for x in red.get(r["art"], []) if len(x) < 70],
                                vis.get(r["art"]) or 0) for r in filas], [0, 22, 48, 74]), "visitas_wikipedia_es")

def festivales():
    cola = [(r["n"], r["alts"] + [r["en"]], 5, r["links"]) for r in wd3("festivales") if LAT(r["n"])
            and not re.search(r"cine|film|teatro|eurovisi|concurso|premio|danza|certamen", r["n"], re.I)]
    junta("festivales", cola, "ediciones_wikipedia")

def generos():
    cola = [(r["n"], r["alts"] + [r["en"]], 4 if r["links"] >= 60 else 5, r["links"]) for r in wd3("generos_todos") if LAT(r["n"])]
    junta("generos", cola, "ediciones_wikipedia")

def estadios():
    cola, t = [], texto3("estadios")
    filas = [re.split(r"\|\|", f) for f in re.findall(r"\n\|\d+\s*\|\|[^\n]*", t)]
    # la columna de la foto falta en media tabla: el estadio es el primer enlace de la fila que no sea una imagen
    for i, m in enumerate(x for x in (re.search(r"\[\[(?!Archivo)([^\]|]+)(?:\|([^\]]+))?\]\]", "||".join(c[1:3])) for c in filas if len(c) > 2) if x):
        n = (m.group(2) or m.group(1)).strip()
        corto = re.sub(r"^(Nuevo\s+)?(Estadio|Campo|Estadi|Camp)\s+(Municipal\s+)?(de\s+Fútbol\s+)?(de\s+la\s+|de\s+los\s+|de\s+|del\s+|d')?", "", SIN_PAREN(n)).strip()
        cola.append((SIN_PAREN(n), [corto, SIN_PAREN(m.group(1))], 4 if i < 45 else 5, 200 - i))
    for r in wd3("estadios_wd"):
        if not LAT(r["n"]): continue
        corto = re.sub(r"^(Nuevo\s+)?(Estadio|Campo|Estadi|Camp)\s+(Municipal\s+)?(de\s+Fútbol\s+)?(de\s+la\s+|de\s+los\s+|de\s+|del\s+|d')?", "", SIN_PAREN(r["n"]), flags=re.I).strip()
        cola.append((SIN_PAREN(r["n"]), r["alts"] + [corto, r["en"]], 5, 0))
    junta("estadios", cola, "puesto_por_aforo")

def cola_comida(nombre, minimo=0):
    return [(r["n"], r["alts"] + [r["en"]], 5, r["links"]) for r in wd3(nombre) if r["links"] >= minimo and LAT(r["n"]) and len(r["n"]) < 40]
def de_lista(nombre, puntos=True):
    """Nombres en cursiva, en negrita o al principio de un punto en una lista de la Wikipedia en inglés."""
    t = texto3(nombre)
    n = (re.findall(r"'{2,}\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]'{2,}", t) + (re.findall(r"\n[*|!]\s*(?:'{2,})?\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]", t) if puntos else [])
         + re.findall(r"'{3}([^'\[\]{}|]{3,30})'{3}", t))
    return [(SIN_PAREN(x).strip(), [], 5, 0) for x in dict.fromkeys(n) if LAT(x) and ":" not in x and 2 < len(x) < 35]
def pasta():
    lista = texto3("pasta_en").lower()             # de Wikidata, solo lo que también está en la lista de pastas de la Wikipedia en inglés (lo demás son empanadillas)
    junta("pasta", [f for f in cola_comida("pasta") if any(x and x.lower() in lista for x in [f[0]] + f[1][-1:])] + de_lista("pasta_en", puntos=False), "ediciones_wikipedia")
def salsas(): junta("salsas", [(re.sub(r"^salsa\s+(de\s+)?", "", n) if False else n, al + ([re.sub(r"^salsa\s+(de\s+|a la\s+)?", "", n, flags=re.I)] if n.lower().startswith("salsa ") else []), nv, v)
                              for n, al, nv, v in cola_comida("salsas", 1) if not n.lower().startswith(("salsas ", "gastronom"))] + de_lista("salsas_en"), "ediciones_wikipedia")
def pizza(): junta("pizza", [(re.sub(r"^pizza\s+(a la\s+|al\s+|de\s+)?", "", n, flags=re.I) or n, al + [n], nv, v) for n, al, nv, v in cola_comida("pizza")
                             if not re.search(r"hut|domino|telepizza|papa john|little caesars|pizzer|express|\binn\b|company|horno|cortador|caja", n, re.I)]
                            + [(re.sub(r"^pizza\s+", "", n, flags=re.I).strip() or n, [n], nv, v) for n, al, nv, v in de_lista("pizza_en") if "pizza" in n.lower()], "ediciones_wikipedia")

def islas():
    cola = []
    for r in wd3("islas_todas"):
        if not LAT(r["n"]): continue
        corto = re.sub(r"^(isla|islote|illa|illot|islas|illes|peñón)\s+(de\s+la\s+|de\s+los\s+|de\s+las\s+|de\s+|del\s+|d'|des\s+|de\s+sa\s+|d'en\s+)?", "", r["n"], flags=re.I).strip()
        cola.append((r["n"], r["alts"] + ([corto] if len(clave(corto)) > 3 else []) + [r["en"]], 5, r["links"]))
    junta("islas", cola, "ediciones_wikipedia")

def aerolineas():
    cola = [(r["n"], r["alts"] + [r["en"], re.sub(r"\s+(Airlines|Airways|Air Lines|Líneas Aéreas|Aerolíneas)$", "", r["n"])], 4 if r["links"] >= 40 else 5, r["links"]) for r in wd3("aerolineas") if LAT(r["n"])]
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
    with open(FUENTES / "grados_ruct.csv", encoding="utf-8") as f:        # todas las que tienen algún grado en el registro oficial (RUCT)
        for n in sorted({fila[-1].strip() for fila in csv.reader(f) if fila and "niversi" in fila[-1]}):
            corto = re.sub(r"^(Universidad|Universitat|Universidade)\s+(Católica\s+)?(de\s+las\s+|de\s+la\s+|de\s+los\s+|de\s+|del\s+|d')?", "", n).strip()
            cola.append((n, [corto] if len(clave(corto)) > 3 else [], 5, 0))
    junta("universidades", cola, "orden_a_mano")

def mario():
    cola = []
    for m in re.finditer(r"''\[\[([^\]]+)\]\]''", texto3("mario_es")):
        n = SIN_PAREN(m.group(1).split("|")[-1]).strip()
        if re.search(r"mario|luigi|yoshi|wario|peach|toad|donkey kong", n, re.I): cola.append((n, [], 5, 0))
    cola += [(r["n"], [r["en"]] + r["alts"], 5, r["links"]) for r in wd3("mario") if LAT(r["n"])]
    cola += [f for f in de_lista("mario_en") if re.search(r"mario|luigi|yoshi|wario|peach|toad|donkey kong", f[0], re.I)]
    junta("mario", cola, "orden_a_mano")

def anglicismos():
    cola = []
    for f in sorted(D3.glob("anglicismos_*.json")):
        for m in json.loads(f.read_text()).get("query", {}).get("categorymembers", []):
            t = m["title"]
            # de la categoría solo entran las que siguen pareciendo inglés (boicot o túnel también vienen de ahí, pero nadie las siente inglesas)
            if m["ns"] == 0 and len(t) < 30 and t[0].islower(): cola.append((t, [], 5, 0))        # la categoría entera menos los nombres propios: mejor que sobre a que falte
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
    # todas las formas (plurales, verbos conjugados): el diccionario grande viene sin tildes
    ya = {clave(f[0]) for f in filas}
    for p in open(D3 / "palabras_todas.txt", encoding="utf-8", errors="replace"):
        p = p.strip().lower()
        if len(p) >= 5 and p not in ya and set("aeiou") <= set(p) and p.isalpha(): filas.append((p, [], 5, 0)); ya.add(p)
    guarda("cinco_vocales", filas, "frecuencia_de_uso")
def palabras_k():
    lema, frec = _palabras()
    cola = [(p, [], 4 if p in frec else 5, 10**5 - frec.get(p, 10**5)) for p in lema if re.fullmatch(r"k[a-záéíóúüñ]{2,}", p)]
    cola = [(p, al + [v.format(p) for v in VARIANTES["palabras_k"]], nv, val) for p, al, nv, val in cola]   # plurales (kilos, kiwis…)
    cola += [(p.strip().lower(), [], 5, 0) for p in open(D3 / "palabras_todas.txt", encoding="utf-8", errors="replace") if p[:1].lower() == "k" and len(p.strip()) > 2]
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
    # además de los 50 primeros de cada sexo: cualquier nombre con una edad media de 12 años o menos (nombres_ine.xls)
    ya = {clave(f[0]) for f in filas}
    for hoja in xlrd.open_workbook(FUENTES / "t2" / "nombres_ine.xls").sheets():
        for i in range(7, hoja.nrows):
            f = hoja.row_values(i)
            if isinstance(f[1], str) and isinstance(f[3], float) and f[3] <= 12 and clave(f[1]) not in ya:
                filas.append((bonito(f[1].strip()), [], 5, f[2])); ya.add(clave(f[1]))
    guarda("nombres_bebes", filas, "bebes_con_ese_nombre_ine")
def nombres_compuestos():
    import xlrd
    filas = []
    for hoja in xlrd.open_workbook(FUENTES / "t2" / "nombres_ine.xls").sheets():
        for i in range(7, hoja.nrows):
            f = hoja.row_values(i)
            if isinstance(f[1], str) and " " in f[1].strip() and isinstance(f[2], float) and f[2] >= 20: filas.append((bonito(f[1].strip()), [], f[2]))
    filas.sort(key=lambda f: -f[2])
    guarda("nombres_compuestos", por_puesto(filas, [10, 35, 110, 300]), "personas_con_ese_nombre_ine")

def podcasts():
    cola = []
    for ruta in [D3 / "podcasts_itunes.json"] + sorted(D3.glob("podcasts_1*.json")):       # la lista general y las de cada género
        general = ruta.name == "podcasts_itunes.json"
        d = json.loads(ruta.read_text(encoding="utf-8"))["feed"].get("entry", [])
        for i, e in enumerate(d if isinstance(d, list) else [d], 1):
            n = html.unescape(e["im:name"]["label"]).strip()
            corto = re.split(r"\s+[-–|:]\s+|\s+\|\s*|\s+con\s+|\s+by\s+", n)[0].strip()
            cola.append((corto if len(clave(corto)) >= 4 else n, [n], nivel_por_puesto(i, [0, 0, 60, 130]) if general else 5, 201 - i if general else 0))
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
            n, *mas = [p.strip() for p in n.split("=")]
            nombre, al = tabla.get(clave(n), (n, []))
            al = al + mas
            (auto if nv == 0 else filas).append((nombre, al, nv, 1000 - orden.get(clave(n), 999)))
    auto.sort(key=lambda f: -f[3])
    filas += [(n, al, 3 + min(2, i * 3 // len(auto)), v) for i, (n, al, _, v) in enumerate(auto)]
    guarda(slug, filas, "puesto_por_visitas")
def sin_mar(): lista_paises("sin_mar", mano_t3.SIN_MAR)
def paises_isla(): lista_paises("paises_isla", {**mano_t3.ISLA, 5: mano_t3.ISLA[5] + ", " + mano_t3.ISLA_EXTRA})
def verde_bandera(): lista_paises("verde_bandera", {**mano_t3.VERDE, 5: mano_t3.VERDE_EXTRA})
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
