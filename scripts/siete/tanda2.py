"""Segunda tanda de preguntas (octubre de 2026): 35 bancos.

Cada pregunta junta dos cosas:
  · la lista de respuestas válidas, que sale de una fuente (Wikidata, Wikipedia, INE, kworb…) ya bajada
    por baja_tanda2.py a datos/siete/fuentes/t2/;
  · los niveles de lo más conocido en España, puestos a mano en mano_t2.py.
Lo que está en la fuente y no en la lista a mano cae en los niveles altos según su métrica.

Uso:  python3 scripts/siete/tanda2.py [slug …]     (sin argumentos, las 35)"""
import sys, html
from comun import *
from mano_t2 import MANO

T2 = FUENTES / "t2"
QID = re.compile(r"Q\d+$")

# Cuando un nivel a mano es muy largo (va escrito de más a menos conocido) se reparte entre varios niveles,
# para que toda pregunta tenga respuestas de los cinco y se pueda llegar al fondo del iceberg.
REPARTE = {
 "shrek": {3: [3, 4, 5]}, "bob": {3: [3, 4, 5]}, "mariokart": {3: [3, 4, 5]}, "disney": {3: [3, 4, 5]},
 "ibex": {3: [3, 4], 4: [5]}, "mcdonalds": {2: [2, 3, 4]}, "raperos": {2: [2, 3]}, "dj": {2: [2, 3]}, "cartas": {2: [2, 3]},
 "movil": {2: [2, 3, 4]}, "coches_lujo": {2: [2, 3, 4]}, "discotecas": {2: [2, 3], 3: [4]}, "anime": {2: [2, 3]}, "miedo": {2: [2, 3]},
 "idiomas": {2: [2, 3]}, "fiestas": {2: [2, 3]}, "fobias": {3: [3, 4]}, "colores": {3: [3, 4]}, "prendas": {3: [3, 4]},
 "transporte": {3: [3, 4]}, "electrodomesticos": {3: [3, 4]}, "enie": {3: [3, 4]}, "hp": {2: [2, 3]}, "supermercados": {3: [3, 4]},
 "youtubers": {3: [3, 4]}, "zapatillas": {3: [3, 4]},
}
def a_mano(slug):
    filas = []
    for nv, texto in MANO.get(slug, {}).items():
        trozos = [x.strip() for x in texto.split(",") if x.strip()]
        destinos = REPARTE.get(slug, {}).get(nv, [nv])
        for i, trozo in enumerate(trozos):
            n, *alias = [p.strip() for p in trozo.split("=")]
            filas.append((n, alias, destinos[min(len(destinos) - 1, i * len(destinos) // len(trozos))], 10**9 - i))
    return filas

def junta(slug, cola, metrica):
    """Lo puesto a mano manda; de la cola solo entra lo que no esté ya (ni por nombre ni por alias)."""
    mano = a_mano(slug)
    ya = {clave(x) for n, al, _, _ in mano for x in [n] + al}
    guarda(slug, mano + [f for f in cola if clave(f[0]) not in ya and clave(f[0])], metrica)

def wd(nombre):
    filas, vistos = [], set()
    for f in json.loads((T2 / f"{nombre}.json").read_text(encoding="utf-8"))["results"]["bindings"]:
        v = lambda k: f[k]["value"] if k in f else ""
        if v("x") in vistos: continue
        vistos.add(v("x"))
        n = v("xLabel")
        if QID.match(n) or n.startswith("MediaWiki"): n = v("en")
        if not n or QID.match(n): continue
        art = urllib.parse.unquote(v("art").rsplit("/wiki/", 1)[1]).replace("_", " ") if v("art") else ""
        alts = [a for a in v("alts").split("|") if a and len(a) < 45]
        filas.append({"n": n, "en": v("en"), "links": int(v("links")), "art": art, "alts": alts, "f": f})
    return sorted(filas, key=lambda r: -r["links"])

def texto_wiki(nombre):
    return json.loads((T2 / f"{nombre}.json").read_text(encoding="utf-8"))["parse"]["wikitext"]["*"]
def categoria(nombre):
    d = json.loads((T2 / f"{nombre}.json").read_text(encoding="utf-8"))
    return [m["title"] for m in d.get("query", {}).get("categorymembers", []) if m["ns"] == 0]
def limpia_wiki(t):
    t = re.sub(r"<ref[^>]*/>|<ref.*?</ref>|\{\{efn.*|\{\{sfn.*?\}\}|\{\{anchor\|[^}]*\}\}|<!--.*?-->|<small>.*?</small>", "", t, flags=re.S)
    t = re.sub(r"\{\{sort\|[^|}]*\|(.*?)\}\}", r"\1", t, flags=re.I)
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", t)
    return html.unescape(t.replace("''", "")).strip()
SIN_PAREN = lambda t: re.sub(r"\s*\(.*?\)", "", t).strip()
EMPRESA = re.compile(r"\b(company|inc\.?|ltd\.?|corporation|group|s\.a\.?|gmbh|ag|supermarkets?|stores?|brands?)\b\.?", re.I)
def marca(t):
    corto = re.sub(r"\s+", " ", EMPRESA.sub("", SIN_PAREN(t))).strip(" ,&-")
    return corto if len(clave(corto)) >= 2 else SIN_PAREN(t)

def por_puesto(filas, cortes):
    """filas ordenadas de más a menos conocidas → les pone nivel según el puesto."""
    return [(n, al, nivel_por_puesto(i, cortes), val) for i, (n, al, val) in enumerate(filas, 1)]

def apodos(nombres):
    """Para personajes: cada palabra del nombre que no comparte con nadie más vale como alias (Hermione, Snape)."""
    cuenta = {}
    for n in nombres:
        for p in set(re.findall(r"[^\W\d_]{4,}", n)): cuenta[p.lower()] = cuenta.get(p.lower(), 0) + 1
    return {n: [p for p in re.findall(r"[^\W\d_]{4,}", n) if cuenta[p.lower()] == 1 and p != n and p[0].isupper()] for n in nombres}

# ───────────────────────── preguntas ─────────────────────────
def supermercados():
    cola = [(marca(r["n"]), [r["en"]] + r["alts"], 4 if r["links"] >= 15 else 5, r["links"]) for r in wd("supermercados")
            if not re.search(r"[^\x00-ɏ]", r["n"])]
    junta("supermercados", cola, "ediciones_wikipedia")

def zapatillas():
    cola = [(marca(t), [SIN_PAREN(t)], 4, 2) for t in categoria("cat_zapatillas")]
    cola += [(marca(t), [SIN_PAREN(t)], 5, 1) for t in categoria("cat_zapatos") + categoria("cat_deporte") if not t.startswith("List")]
    junta("zapatillas", cola, "categoria_wikipedia")

def youtubers():
    """Canales de España entre los 1.000 más vistos (youtubers.me), con más de 100.000 suscriptores.
    Fuera los de música y los de dibujos, que son de artistas y marcas. El nivel de los que no están
    puestos a mano lo dan los suscriptores: 5 millones → nivel 3, 1 millón → 4, el resto → 5."""
    t = (T2 / "youtubers_me_top1000_espana.html").read_text(encoding="utf-8", errors="replace")
    cola = []
    for f in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S):
        c = [html.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in re.findall(r"<td[^>]*>(.*?)</td>", f, re.S)]
        if len(c) < 6 or not c[0].isdigit() or c[5] in ("Music", "Film & Animation"): continue
        subs = int(c[2].replace(",", "") or 0)
        if subs < 100000: continue
        entero = re.sub(r"[^\w\s&'.!¡¿?*|+:·-]", "", c[1]).strip()                     # fuera emojis
        corto = re.split(r"\s+[|*·:-]\s*|\s+\*", entero)[0].strip() or entero            # «DaniRep | +6 vídeos diarios» → DaniRep
        if re.search(r"\b(oficial|official|españa|spain|kids|junior|tv|juguetes|canciones)\b", entero, re.I): continue   # marcas y cadenas
        cola.append((corto, [entero] if entero != corto else [], nivel_por_umbral(subs, [10**12, 10**12, 5_000_000, 1_000_000]), subs))
    no = {clave(x) for x in ["Jordi el Niño Polla", "Amarna Miller", "Iker Jiménez", "Pilar Rahola", "Vanesa Romero", "Pilar Eyre", "Albano Dante Fachin",
                             "David Cirici", "Cristina Spínola", "Carolina Abril", "Abraham Maffeo", "pepe", "Daniel Rojo", "Real Madrid"]}
    cola = [f for f in cola if clave(f[0]) not in no]
    cola += [(r["n"], r["alts"], 5, 0) for r in wd("youtubers") if clave(r["n"]) not in no]
    junta("youtubers", cola, "suscriptores_youtube")

def pokemon():
    links = {r["en"].lower(): r["links"] for r in wd("pokemon")}
    raros = {"nidoran-f": ("Nidoran hembra", ["Nidoran♀", "Nidoran"]), "nidoran-m": ("Nidoran macho", ["Nidoran♂"]),
             "mr-mime": ("Mr. Mime", ["Mr Mime"]), "farfetchd": ("Farfetch'd", ["Farfetchd"])}
    esp = json.loads((T2 / "pokeapi.json").read_text())["results"]
    filas = []
    for e in esp:
        n, al = raros.get(e["name"], (e["name"].capitalize(), []))
        filas.append((n, al, links.get(n.lower(), links.get(e["name"], 0))))
    filas.sort(key=lambda f: -f[2])
    junta("pokemon", por_puesto(filas, [15, 40, 80, 120]), "ediciones_wikipedia")

def fobias():
    palabras = sorted(set(re.findall(r"\b[a-záéíóúñü]{4,}fobia\b", texto_wiki("fobias").lower())))
    junta("fobias", [(p, [], 5, 0) for p in palabras if p not in ("fobia",)], "orden_a_mano")

def colores():
    cola = []
    for bruto in re.findall(r"\{\{Colort\|name=(.*?)\|hex=", texto_wiki("colores"), flags=re.S):
        n = SIN_PAREN(limpia_wiki(bruto))
        for parte in re.split(r"\s+[ou]\s+|\s*/\s*|,\s*", n):
            parte = parte.strip(" .«»\"")
            if 2 < len(parte) < 40: cola.append((parte[0].lower() + parte[1:], [], 5, 0))
    junta("colores", cola, "orden_a_mano")

MINUS = lambda r: r["n"][:1].islower()
def cola_wd(nombre, minimo, alto, fuera=()):
    """Nombres comunes de Wikidata (en minúscula y con artículo en español) que no están en la lista a mano."""
    no = re.compile("|".join(fuera), re.I) if fuera else None
    return [(r["n"], r["alts"][:4], 4 if r["links"] >= alto else 5, r["links"]) for r in wd(nombre)
            if MINUS(r) and r["art"] and r["links"] >= minimo and not (no and no.search(r["n"]))]

def prendas():
    junta("prendas", cola_wd("prendas", 8, 45, ["gafas", "paraguas", "anillo", "máscara", "botón", "corona", "escudo", "medalla", "pendiente",
          "armadura", "joya", "reloj", "bolso", "mochila", "collar", "pulsera", "peluca", "bastón", "abanico", "cremallera", "bolsillo", "guirnalda"]), "ediciones_wikipedia")
def transporte():
    junta("transporte", cola_wd("transporte", 30, 80, ["satélite", "cometa", "estación", "misil", "arma", "sonda", "bomba", "motor", "rueda", "esquí", "salto", "carrera"]), "ediciones_wikipedia")
def electrodomesticos():
    junta("electrodomesticos", cola_wd("electrodomesticos", 12, 60, ["teléfono", "consola", "tableta", "escáner", "computadora", "ordenador", "móvil",
          "reloj", "iphone", "ipad", "termostato", "pixel", "cámara", "lector", "reproductor", "mando", "calculadora", "linterna", "videojuego", "inteligente"]), "ediciones_wikipedia")

def idiomas():
    cola = []
    for r in wd("idiomas"):
        n = re.sub(r"^(idioma|lengua)\s+", "", r["n"], flags=re.I)
        if n.lower().startswith(("lenguas", "idiomas", "dialecto", "protoidioma", "familia")) or re.search(r"[^\x00-ɏ]", n): continue
        cola.append((n, [a for a in r["alts"][:5]], nivel_por_umbral(r["links"], [10**6, 10**6, 120, 60]), r["links"]))
    junta("idiomas", cola, "ediciones_wikipedia")

def fiestas():
    cola = []
    for fuente, nv in (("fiestas_int", 3), ("fiestas_nac", 4)):
        for bruto in re.findall(r"\|\s*nombre\s*=\s*(.*)", texto_wiki(fuente)):
            n = SIN_PAREN(limpia_wiki(bruto)).strip(" '\"")
            if 3 < len(n) < 70: cola.append((n, [], nv, 5 - nv))
    cola += [(r["n"], r["alts"][:3], 5, 0) for r in wd("fiestas_wd") if r["art"] and not re.search(r"cine|film|jazz|architecture|convention", r["n"], re.I)]
    junta("fiestas", cola, "declaracion_turistica")

def raperos():
    junta("raperos", [(r["n"], r["alts"][:4], 4 if r["art"] else 5, r["links"]) for r in wd("raperos")], "ediciones_wikipedia")

def ibex():
    t = texto_wiki("ibex")
    faltan = [n for n, al, nv, v in a_mano("ibex") if n.split("=")[0] not in t and not any(a in t for a in al)]
    if faltan: print("  ojo, no aparecen en el artículo del IBEX 35:", faltan)
    junta("ibex", [], "orden_a_mano")

VASCOS = """Aimar Aiora Aitana Aitziber Alaia Alaitz Amets Ainara Ainhize Aintzane Aitzol Aketza Alazne Amaiur Anartz Andoni Ane Aner Antton
Antxon Aratz Arantxa Arantza Arantzazu Aritz Arkaitz Arrate Asier Aiert Beñat Bittor Danel Edurne Eider Ekain Ekaitz Eki Elene Eneko Endika Enara
Eñaut Erlantz Erik Estibaliz Eukene Ibai Ibon Idoia Igor Iholdi Ikerne Ilargi Imanol Inar Intza Iñigo Iraia Iratxe Iraitz Irune Itsaso Itxaso Itxaro Itziar
Izar Izaro Izaskun Jagoba Janire Joanes Jokin Jone Joseba Josu Josune Julen June Jurgi Kepa Kattalin Koldo Koldobika Laia Laida Lander Larraitz
Leire Leyre Lide Lierni Loreto Lorea Luken Lur Maddi Maialen Maider Maitane Maite Malen Manex Mattin Mikel Miren Mirari Nahia Naia Nagore Naroa
Nekane Nora Odei Oier Oihan Oihana Olaia Olatz Onintza Ortzi Oskitz Paul Patxi Peio Peru Sendoa Saioa Sustrai Tasio Telmo Txomin Udane Uxue Unax Urko
Urtzi Usoa Uxue Xabier Xabi Xuban Yeray Zigor Ziortza Zuriñe Zuhaitz Garazi Garbiñe Gorka Goizane Goizeder Gotzon Gaizka Galder Ganix Gari Haizea
Haritz Hegoa Hodei Harkaitz Hegoi Iker Aitor Unai Nerea Jon Ainhoa Iñaki Amaia Ander Markel Irati Ugaitz Unax Eritz Xanti Bingen Kerman Karmele
Begoña Arantxa Itxaso Josebe Edorta Erramun Zuria Txaro Peli Kimetz Aiala Alain Enaitz Oinatz Eñaut Aimar Araitz Jare Lohitzune Libe Mikele Uma""".split()
def nombres_vascos():
    import xlrd
    frec = {}
    for hoja in xlrd.open_workbook(T2 / "nombres_ine.xls").sheets():
        for i in range(7, hoja.nrows):
            f = hoja.row_values(i)
            if isinstance(f[1], str) and isinstance(f[2], float): frec[clave(f[1])] = frec.get(clave(f[1]), 0) + int(f[2])
    # Wikidata marca como «vascos» algunos nombres que no lo son
    no = {clave(x) for x in "Jose Andrea Laia Noa Aitana Erik Fermin Nora Paul Eloi Rafa Loreto Alain Uma Yeray Telmo Aroa Petri Maia Jerardo".split()}
    nombres = {clave(n): n for n in [r["n"] for r in wd("nombres_vascos") if " " not in r["n"]] + VASCOS if clave(n) not in no}
    filas = sorted(((n, [], frec.get(k, 0)) for k, n in nombres.items()), key=lambda f: -f[2])
    junta("nombres_vascos", por_puesto(filas, [15, 40, 90, 160]), "personas_con_ese_nombre_ine")

def discotecas():
    junta("discotecas", [(SIN_PAREN(r["n"]), r["alts"][:3], 4 if r["links"] >= 12 else 5, r["links"]) for r in wd("discotecas")
                         if r["links"] >= 2 and not re.search(r"[^\x00-ɏ]", r["n"])], "ediciones_wikipedia")

def cartas():
    cola = [(SIN_PAREN(t), [], 4, 1) for t in categoria("cat_naipes_es") if ":" not in t and t not in ("Baraja", "Juego de naipes")]
    cola += [(SIN_PAREN(r["n"]), r["alts"][:3] + [r["en"]], 5, 0) for r in wd("cartas") if r["links"] >= 3 and not re.search(r"[^\x00-ɏ]", r["n"])]
    junta("cartas", cola, "orden_a_mano")

def dj():
    junta("dj", [(r["n"], r["alts"][:3], 4 if r["links"] >= 25 else 5, r["links"]) for r in wd("dj") if r["links"] <= 50], "ediciones_wikipedia")

def shrek(): junta("shrek", [], "orden_a_mano")
def bob(): junta("bob", [], "orden_a_mano")
def mariokart(): junta("mariokart", [], "orden_a_mano")
def disney(): junta("disney", [], "orden_a_mano")

def hp():
    filas = [r for r in wd("hp2") if not re.search(r"[^\x00-ɏ]", r["n"])]
    ap = apodos([r["n"] for r in filas])
    junta("hp", [(r["n"], r["alts"][:4] + ap[r["n"]], nivel_por_umbral(r["links"], [10**6, 10**6, 20, 8]), r["links"]) for r in filas], "ediciones_wikipedia")

def miedo():
    fuera = {clave(x) for x in ["The Terminator", "Terminator", "Apocalypse Now", "Gravity", "Memento", "Mulholland Drive", "Seven", "Shutter Island",
                                 "Depredador", "Prometheus", "Donnie Darko", "The Twilight Saga: New Moon", "Crepúsculo", "Black Swan", "Cisne negro"]}
    junta("miedo", [(r["n"], [r["en"]] + r["alts"][:3], nivel_por_umbral(r["links"], [10**6, 10**6, 45, 25]), r["links"])
                    for r in wd("miedo") if clave(r["n"]) not in fuera and clave(r["en"]) not in fuera], "ediciones_wikipedia")

def anime():
    junta("anime", [(r["n"], [r["en"]] + r["alts"][:3], nivel_por_umbral(r["links"], [10**6, 10**6, 40, 20]), r["links"]) for r in wd("anime")], "ediciones_wikipedia")

def movil():
    junta("movil", [(r["n"], [r["en"]] + r["alts"][:2], 5, r["links"]) for r in wd("movil") if r["links"] <= 45], "ediciones_wikipedia")

def mcdonalds():
    cola = [(SIN_PAREN(t), [], 5, 0) for t in categoria("cat_mcdonalds") if not t.startswith(("International", "List", "McDonald's"))]
    junta("mcdonalds", cola, "orden_a_mano")

def coches_lujo():
    cola = [(marca(t), [SIN_PAREN(t)], 5, 0) for t in categoria("cat_lujo") + categoria("cat_deportivos") if not t.startswith("List")]
    junta("coches_lujo", cola, "orden_a_mano")

def _paises():
    filas = [r for r in wd("paises") if not r["n"].startswith("Reino de")]
    art = lambda r, k: urllib.parse.unquote(r["f"][k]["value"].rsplit("/wiki/", 1)[1]).replace("_", " ") if k in r["f"] else ""
    ves = visitas("es", [r["art"] for r in filas if r["art"]], "t2/paises_visitas_es.json")
    ven = visitas("en", [art(r, "arten") for r in filas if art(r, "arten")], "t2/paises_visitas_en.json")
    for campo, tabla, que in (("pes", ves, lambda r: r["art"]), ("pen", ven, lambda r: art(r, "arten"))):
        for i, r in enumerate(sorted(filas, key=lambda r: -(tabla.get(que(r)) or 0)), 1): r[campo] = i
    filas.sort(key=lambda r: r["pes"] + r["pen"])
    return [(r, (r["n"], [r["en"]] + r["alts"][:6], 1000 - (r["pes"] + r["pen"]) / 2)) for r in filas]
def paises():
    junta("paises", por_puesto([f for _, f in _paises()], [0, 50, 100, 150]), "puntuacion_visitas")
def paises_izquierda():
    todos = _paises()
    izq = next(r["f"]["lado"]["value"] for r, _ in todos if r["n"] == "Reino Unido")     # el valor que tenga el Reino Unido es «izquierda»
    filas = [f for r, f in todos if r["f"].get("lado", {}).get("value") == izq]
    junta("paises_izquierda", por_puesto(filas, [0, 14, 28, 42]), "puntuacion_visitas")
def paises_rey():
    filas = [f for r, f in _paises() if "mon" in r["f"]]
    junta("paises_rey", por_puesto(filas, [0, 16, 24, 31]), "puntuacion_visitas")

def italia():
    junta("italia", por_puesto([(r["n"], [r["en"]] + r["alts"][:3], r["links"]) for r in wd("italia")], [8, 25, 60, 140]), "ediciones_wikipedia")

def metro():
    filas = [r for r in wd("metro") if r["art"]]
    vis = visitas("es", [r["art"] for r in filas], "t2/metro_visitas.json")
    limpio = lambda n: re.sub(r"^(Estación|estación)\s+(de\s+(la\s+|los\s+|las\s+)?|del\s+)?", "", SIN_PAREN(n)).strip()
    orden = sorted(filas, key=lambda r: -(vis.get(r["art"]) or 0))
    junta("metro", por_puesto([(limpio(r["n"])[:1].upper() + limpio(r["n"])[1:], r["alts"][:3], vis.get(r["art"]) or 0) for r in orden], [0, 40, 90, 160]), "visitas_wikipedia_es")

def beatles():
    base = lambda t: re.sub(r"\s+-\s+.*$", "", re.sub(r"\s*[\(\[].*$", "", html.unescape(t))).strip()
    streams = {}
    for titulo, n in re.findall(r'<tr><td class="text"><div>(?:\*\s*)?<a[^>]*>(.*?)</a></div></td><td>([\d,]+)</td>', (T2 / "beatles_kworb.html").read_text(encoding="utf-8")):
        k = clave(base(titulo)); streams[k] = streams.get(k, 0) + int(n.replace(",", ""))
    canciones = {}
    t = texto_wiki("beatles_wiki"); t = t[t.find("sticky-header"):]
    t = t[:t.find("\n|}")]                       # solo la tabla principal: las canciones del catálogo oficial
    for m in re.finditer(r'!\s*scope="?row"?[^|\n]*\|(.*)', t):
        q = re.search(r'"(.+?)"', limpia_wiki(m.group(1)))
        if q: canciones.setdefault(clave(base(q.group(1))), base(q.group(1)))
    orden = sorted(canciones.items(), key=lambda kv: -streams.get(kv[0], 0))
    print("  Beatles sin datos de Spotify:", sum(1 for k, _ in orden if not streams.get(k)))
    junta("beatles", por_puesto([(n, [], streams.get(k, 0)) for k, n in orden], [12, 35, 80, 140]), "reproducciones_spotify")

CLUBES = {"Real Madrid": ["Madrid"], "Barcelona": ["Barça", "Barsa", "Barcelona"], "Atlético de Madrid": ["Atleti", "Atlético", "Atlético de Madrid"],
          "Athletic": ["Athletic", "Athletic de Bilbao", "Bilbao"], "Real Sociedad": ["Real Sociedad", "la Real"], "Deportivo de La Coruña": ["Dépor", "Deportivo"],
          "Sporting": ["Sporting"], "Racing Club de Santander": ["Racing", "Racing de Santander"], "Rayo": ["Rayo", "Rayo Vallecano"], "Recreativo": ["Recre"],
          "Espanyol": ["Español"], "Valencia": ["Valencia"], "Sevilla": ["Sevilla"], "Málaga": ["Málaga"], "Cádiz": ["Cádiz"]}
def primera():
    t = texto_wiki("primera")
    filas = []
    for fila in re.findall(r"\n\|\s*\d+\s*\|\|[^\n]*(?:\n\|\|[^\n]*)?", t):
        fila = re.sub(r"<ref.*?</ref>|<span[^>]*>|</span>|&thinsp;", "", fila)
        enlace = re.search(r"\[\[(?!Archivo)([^\]|]+)(?:\|([^\]]+))?\]\]", fila)
        puntos = re.search(r"\|\|\s*\d+\s*\|\|\s*'''(\d+)'''", fila)
        if not enlace or not puntos: continue
        n = (enlace.group(2) or enlace.group(1)).strip()
        corto = re.sub(r"\b(Real Club|Real|Club de Fútbol|Club|CF|FC|UD|CD|SD|RCD|RC|CA|AD|CE|UE|CP|SAD|de Fútbol|Balompié|Unión Deportiva|Club Deportivo|Sociedad Deportiva)\b\.?", "", n)
        corto = re.sub(r"\s+", " ", corto).strip(" -")
        alias = [a for k, v in CLUBES.items() if k in n for a in v] + ([corto] if corto and corto != n else []) + ([enlace.group(1)] if enlace.group(2) else [])
        filas.append((n, alias, int(puntos.group(1))))
    ap = apodos([f[0] for f in filas])
    filas = [(n, al + ap[n], p) for n, al, p in filas]
    filas.sort(key=lambda f: -f[2])
    junta("primera", por_puesto(filas, [6, 18, 35, 50]), "puntos_historicos")

def enie():
    palabras = [x.strip() for x in open(T2 / "palabras.txt", encoding="utf-8", errors="replace") if x.strip().lower().startswith("ñ") and len(x.strip()) > 1]
    junta("enie", [(p, [], 5, 0) for p in palabras], "orden_a_mano")

TODAS = [supermercados, zapatillas, youtubers, pokemon, fobias, colores, prendas, transporte, electrodomesticos, idiomas, fiestas, raperos, ibex,
         nombres_vascos, discotecas, cartas, dj, shrek, hp, bob, miedo, anime, mariokart, movil, mcdonalds, coches_lujo, paises_izquierda, paises_rey,
         italia, paises, metro, disney, beatles, primera, enie]
if __name__ == "__main__":
    for f in TODAS:
        if len(sys.argv) > 1 and f.__name__ not in sys.argv[1:]: continue
        try: f()
        except Exception as e: print(f"!! {f.__name__}: {type(e).__name__}: {e}")
