"""Cuarta tanda de preguntas (semana del 19 al 25 de octubre de 2026): 49 bancos.

Como en tanda3.py: la lista de respuestas válidas sale de una fuente bajada por baja_tanda4.py
(datos/siete/fuentes/t4/) y los niveles de lo más conocido en España van a mano en mano_t4.py.
Las que no tienen base de datos posible (helados de Frigo, productos Hacendado…) son solo a mano.
Las artistas de Spotify salen de artistas_spotify.py (Wikidata + oyentes mensuales de cada página de Spotify).

Uso:  python3 scripts/siete/tanda4.py [slug …]     (sin argumentos, todas)"""
import difflib, sys, html
import tanda2
from tanda2 import *
import mano_t4
D4 = FUENTES / "t4"
LAT = lambda t: not re.search(r"[^\x00-ɏ’'·]", t)

def wd4(nombre):
    viejo = tanda2.T2; tanda2.T2 = D4
    try: return wd(nombre)
    finally: tanda2.T2 = viejo
def texto4(nombre):
    return json.loads((D4 / f"{nombre}.json").read_text(encoding="utf-8"))["parse"]["wikitext"]["*"]

def a_mano4(slug):
    filas = []
    # repaso: respuestas de más, con su nivel, que no pasan por REPARTE
    for nv, texto in mano_t4.MAS.get(slug, {}).items():
        for i, trozo in enumerate(x.strip() for x in texto.split(",") if x.strip()):
            n, *alias = [p.strip() for p in trozo.split("=")]
            filas.append((n, alias, nv, 10**8 - i))
    for nv, texto in mano_t4.MANO.get(slug, {}).items():
        trozos = [x.strip() for x in texto.split(",") if x.strip()]
        destinos = mano_t4.REPARTE.get(slug, {}).get(nv, [nv])
        for i, trozo in enumerate(trozos):
            n, *alias = [p.strip() for p in trozo.split("=")]
            filas.append((n, alias, destinos[min(len(destinos) - 1, i * len(destinos) // len(trozos))], 10**9 - i))
    return filas
VARIANTES4 = {"huesos": ["hueso {}", "huesos {}"], "musculos": ["músculo {}", "músculos {}"], "circuitos_f1": ["circuito de {}", "Gran Premio de {}", "GP de {}"],
              "provincias": ["provincia de {}"], "sabores_helado": ["helado de {}", "sabor {}"], "pueblos_madrid": [], "batallas": ["batalla de {}"],
              "filosofos": [], "especialidades": [], "deportes_acuaticos": [], "masas_agua": []}
def por_contenido(n, dueños):
    """El dueño a mano cuyo nombre (de 5+ letras) está dentro del nombre largo de la fuente: «Shanghai International Circuit» → Shanghái."""
    k = clave(n)
    hits = [(len(x), d) for x, d in dueños.items() if len(x) >= 5 and x in k]
    return max(hits)[1] if hits else None
BATALLA_IGUAL = {"ataque a Pearl Harbor": "Pearl Harbor", "guerra anglo-estadounidense de 1812": "la guerra de 1812", "Guerra de Osetia del Sur de 2008": "la guerra de Georgia",
    "Levantamiento de los bóxers": "la rebelión de los bóxers", "Guerra de Independencia de Argelia": "la guerra de Argelia", "Guerra de Liberación de Bangladés": "la guerra de Bangladés",
    "guerra civil yemení": "la guerra de Yemen", "tercera guerra civil sudanesa": "la guerra de Sudán", "Guerra civil angoleña": "la guerra de Angola",
    "Conflicto del Alto Karabaj": "la guerra del Alto Karabaj", "Conflicto entre India y Pakistán": "la guerra indo-pakistaní", "guerras de religión de Francia": "las guerras de religión",
    "invasión de Irak de 2003": "la guerra de Irak", "Invasión de Kuwait de 1990": "la guerra del Golfo", "batalla de los Cuernos de Hattin": "Hattin",
    "Batalla del Golfo de Leyte": "Leyte", "invasión rusa a Ucrania": "la guerra de Ucrania", "guerra ruso-ucraniana": "la guerra de Ucrania", "Guerra de Gaza": "la guerra de Gaza",
    "guerra Irán-Israel": "la guerra de Irán", "guerra entre Irán e Irak": "la guerra Irán-Irak", "guerra civil siria": "la guerra de Siria", "Guerras Yugoslavas": "la guerra de los Balcanes",
    "guerra de los Balcanes": "la guerra de los Balcanes", "Guerra de Bosnia": "la guerra de Bosnia", "guerra de la Independencia española": "la guerra de la Independencia",
    "Guerra de los Diez Días": "la guerra de Eslovenia", "Guerra Cristera": "la guerra de los Cristeros", "Guerras carlistas": "las guerras carlistas", "Guerra del Rif": "la guerra de Marruecos",
    "Guerra de Independencia cubana": "la guerra de Cuba", "guerra de Independencia de los Estados Unidos": "la guerra de Independencia de Estados Unidos",
    "Guerra hispano-estadounidense": "la guerra hispano-estadounidense", "Desembarco de Normandía": "Normandía", "Operación Overlord": "Normandía"}
def batalla_igual(n, dueños):
    """«Segunda batalla de El Alamein», «guerra de Libia de 2011», «Tercera batalla de Ypres»: la misma que la de a mano"""
    if n in BATALLA_IGUAL: return BATALLA_IGUAL[n]
    for f in (lambda t: re.sub(r"\s+(de|en)\s+\d{4}([-–]\d{2,4})?$", "", t),
              lambda t: re.sub(r"^(primera|segunda|tercera|cuarta|quinta)\s+(batalla)\s+", "batalla ", t, flags=re.I),
              lambda t: re.sub(r"^(batalla|sitio|asedio)\s+(de\s+la\s+|de\s+los\s+|de\s+las\s+|del\s+|de\s+)", "", re.sub(r"^(primera|segunda|tercera|cuarta|quinta)\s+batalla", "batalla", t, flags=re.I), flags=re.I)):
        t = f(n)
        if t != n and clave(t) in dueños: return dueños[clave(t)]
FUSIONA = {
 "batallas": batalla_igual,
 "circuitos_f1": por_contenido,
 "apple": lambda n, d: "iPhone 15" if re.match(r"iphone\b", n, re.I) and n.lower() != "iphone" else None,
 "eurovision": {"Amaia Romero y Alfred García": "Amaia y Alfred"},
 "friends": {"Janice Litman-Goralnik": "Janice"},
 "phineas": {"Dr. Heinz Doofenshmirtz": "Doofenshmirtz", "Linda Flynn-Fletcher": "Linda"},
 "bigbang": {"Raj Koothrappali": "Raj", "Amy Fowler": "Amy", "Sheldon Lee Cooper": "Sheldon"},
 "latin": {"curriculum vitæ": "curriculum vitae", "conditio sine qua non o Condicio sine qua non": "sine qua non"},
 "hormonas": {"gonadotropina coriónica humana": "HCG"},
}
def junta(slug, cola, metrica):
    """Lo puesto a mano manda; de la cola solo entra lo que no esté ya, y a sus alias se les quitan las formas con dueño."""
    mano = a_mano4(slug)
    mas = {clave(k): [a.strip() for a in v.split(",") if a.strip()] for k, v in mano_t4.ALIAS_MAS.get(slug, {}).items()}
    mano = [(n, al + mas.pop(clave(n), []), nv, v) for n, al, nv, v in mano]
    cola = [(n, al + mas.pop(clave(n), []), nv, v) for n, al, nv, v in cola]       # también a lo que viene de la fuente
    # lo de la fuente que es lo mismo que algo puesto a mano (otro nombre) no puede valer más metros: pasa a ser alias suyo
    regla = FUSIONA.get(slug)
    if regla:
        dueños = {clave(x): n for n, al, _, _ in mano for x in [n] + al}
        juntos, resto = {}, []
        for n, al, nv, v in cola:
            d = regla(n, dueños) if callable(regla) else regla.get(n)
            if d: juntos.setdefault(d, []).extend([n] + al)
            else: resto.append((n, al, nv, v))
        mano = [(n, al + juntos.pop(n, []), nv, v) for n, al, nv, v in mano]
        if juntos: print("  ojo, fusiones sin dueño:", list(juntos))
        cola = resto
    if mas: print("  ojo, alias de más sin dueño:", list(mas))
    if slug in VARIANTES4: mano = [(n, al + [v.format(x) for x in [n] + al for v in VARIANTES4[slug]], nv, val) for n, al, nv, val in mano]
    ya = {clave(x) for n, al, _, _ in mano for x in [n] + al}
    limpia = []
    for n, al, nv, val in cola:
        if not clave(n) or clave(n) in ya: continue
        limpia.append((n, [a for a in al if a and clave(a) not in ya], nv, val))
    guarda(slug, mano + limpia, metrica)
def solo_mano(*slugs):
    def crea(slug):
        def f(): junta(slug, [], "orden_a_mano")
        f.__name__ = slug; return f
    return [crea(s) for s in slugs]
frigo, hacendado, idiomas_paises, pronombres, bimbo, sabores_helado, dulces_navidad, deportes_acuaticos, juegos_invierno, \
    hispanohablantes, especialidades, unidades_tiempo, gases, francofonos, provincias, halloween = solo_mano(
    "frigo", "hacendado", "idiomas_paises", "pronombres", "bimbo", "sabores_helado", "dulces_navidad", "deportes_acuaticos",
    "juegos_invierno", "hispanohablantes", "especialidades", "unidades_tiempo", "gases", "francofonos", "provincias", "halloween")

def cola_wd4(nombre, minimo=0, alto=10**9, fuera=None, quita_prefijo=None, minus=False):
    """Nombres de Wikidata (con etiqueta en español o, si no, en inglés). Nivel 4 si tiene muchas ediciones, 5 si no."""
    filas = []
    for r in wd4(nombre):
        n = r["n"]
        if r["links"] < minimo or not LAT(n) or len(n) > 60: continue
        if fuera and re.search(fuera, n, re.I): continue
        if minus and n[:1].isupper() and not r["f"].get("xLabel"): continue
        al = r["alts"][:5] + ([r["en"]] if r["en"] and LAT(r["en"]) else [])
        if quita_prefijo:
            corto = re.sub(quita_prefijo, "", n, flags=re.I).strip()
            if corto != n and len(clave(corto)) > 2: al.append(corto)
        filas.append((SIN_PAREN(n), [SIN_PAREN(a) for a in al], 4 if r["links"] >= alto else 5, r["links"]))
    return filas

# ── listas de Wikidata ──
def refrescos(): junta("refrescos", cola_wd4("refrescos", 3, 40, r"^(bebida|refresco|soda|agua|zumo|jugo|té |café|leche|cerveza|vino|licor|list)|crème|smetana|ayran|viili|yogur|filmj|yakult|k[eé]fir|kumis|lassi|perrier|skyr|cuajada|nata"), "ediciones_wikipedia")
def cocacola(): junta("cocacola", cola_wd4("cocacola", 1, 30, r"^(The Coca-Cola|Coca-Cola (Company|FEMSA|HBC|Europacific|Amatil|Bottling|Enterprises|Consolidated|Beverages|Hellenic|İçecek|Icecek))|embotelladora|bottling|planta|fábrica|museo|world of coca|campaña|anuncio|publicidad|historia|botella|weintraub|minogue|beverage partners|entertainment|hawaï"), "ediciones_wikipedia")
def nestle(): junta("nestle", cola_wd4("nestle", 1, 30, r"^Nestlé( S\.A\.| España| USA| Health| Waters| Purina PetCare)?$|fábrica|planta|sede|museo|centro|l.or[ée]al|lanvin|beverage partners"), "ediciones_wikipedia")
def apple(): junta("apple", cola_wd4("apple", 4, 40, r"^(Apple (Inc|Park|Store|Campus)|Infinite Loop)|procesador|chip|^A\d|^M\d|^S\d|^T\d|^H\d|^U\d|^W\d"), "ediciones_wikipedia")
SAGA_PRE = re.compile(r"^(the |las |los |la |el )?((primera|segunda|tercera) )?(saga|serie|trilog[ií]a|tetralog[ií]a|cuatrilog[ií]a|pentalog[ií]a|franquicia|pel[ií]culas|universo cinematogr[aá]fico|universo)( de| del)?\s+", re.I)
SAGA_FIN = re.compile(r"(\s*[:(].*$|\s+(en el cine|trilogy|film series|franchise|la saga|saga)$)", re.I)
SAGA_IGUAL = {"Universo cinematográfico de Marvel": "Los Vengadores", "The Fast and the Furious": "Fast & Furious", "El Conjuro": "Expediente Warren",
              "The Evil Dead": "Posesión infernal", "The Dark Knight Trilogy": "Batman", "The Karate Kid": "Karate Kid", "Tercera trilogía de Star Wars": "Star Wars",
              "serie de películas Mad Max": "Mad Max", "Universo Spider-Man de Sony": "Spider-Man", "Marvel One-Shots": "Los Vengadores",
              "Marvel Studios Special Presentations": "Los Vengadores", "The Animatrix": "Matrix", "Cars Toons": "Cars"}
def sagas():
    """Si una saga de Wikidata es la misma que una puesta a mano («Películas de James Bond», «Trilogía de El Padrino»), no puede valer 100 m:
    pasa a ser alias de la de mano y puntúa como ella."""
    cola = cola_wd4("sagas", 12, 45, r"^(lista|anexo)|fase|awards|cortos|especiales|condición humana")
    mano = {clave(x): n for n, al, _, _ in a_mano4("sagas") for x in [n] + al}
    mas, limpia = mano_t4.ALIAS_MAS.setdefault("sagas", {}), []
    for n, al, nv, v in cola:
        corto = SAGA_FIN.sub("", SAGA_PRE.sub("", n)).strip()
        dueño = SAGA_IGUAL.get(n) or mano.get(clave(corto)) or mano.get(clave(re.sub(r"^(the|el|la|los|las)\s+", "", corto, flags=re.I)))
        if dueño:
            mas[dueño] = ", ".join(x for x in [mas.get(dueño, ""), n] + al if x)
        else:
            limpia.append((n, al + ([corto] if clave(corto) != clave(n) and len(clave(corto)) > 3 else []), nv, v))
    junta("sagas", limpia, "ediciones_wikipedia")
def minerales(): junta("minerales", cola_wd4("minerales", 0, 25), "ediciones_wikipedia")
def hormonas(): junta("hormonas", cola_wd4("hormonas", 3, 30, r"receptor|^hormona$|^list"), "ediciones_wikipedia")
def corrientes(): junta("corrientes", cola_wd4("corrientes", 3, 40, r"^(list|categor|historia)", r"^(filosofía|escuela)\s+"), "ediciones_wikipedia")
def filosofos():
    filas = cola_wd4("filosofos", 25, 70)
    # el apellido suelto también vale (Kant, Hume) si no lo comparte con otro filósofo de la lista
    cuenta = {}
    for n, *_ in filas: cuenta[clave(n.split()[-1])] = cuenta.get(clave(n.split()[-1]), 0) + 1
    filas = [(n, al + ([n.split()[-1]] if len(n.split()) > 1 and cuenta[clave(n.split()[-1])] == 1 and len(n.split()[-1]) > 3 else []), nv, v) for n, al, nv, v in filas]
    junta("filosofos", filas, "ediciones_wikipedia")
GUERRA_FUERA = (r"^(list|anexo|frente|teatro|categor)|protesta|disturbio|masacre|matanza|golpe|atentado|ataques? |incidente|conspiraci|crisis|huelga|"
                r"manifestaci|primavera árabe|asalto al capitolio|tercera guerra mundial|guerra nuclear|riot|massacre|coup|attack|protest|affair|plot")
def batallas():
    """Batallas y guerras: las batallas y las guerras (y rebeliones, invasiones y conflictos armados) de Wikidata, más las de a mano.
    El nombre sin «batalla de» / «guerra de» también vale (Waterloo, Vietnam), si no es de otra."""
    filas = []
    for n, al, nv, v in cola_wd4("batallas", 12, 50, r"^(list|frente|teatro)"):
        corto = re.sub(r"^(primera |segunda |tercera )?(batalla|sitio|asedio|toma|combate|desembarco|caída|cerco)\s+(naval\s+)?(de\s+la\s+|de\s+los\s+|de\s+las\s+|del\s+|de\s+)?", "", n, flags=re.I).strip()
        filas.append((n, al + ([corto] if corto != n and len(clave(corto)) > 3 else []), nv, v))
    for n, al, nv, v in cola_wd4("guerras", 5, 50, GUERRA_FUERA):
        corto = re.sub(r"^guerras?\s+(de\s+la\s+|de\s+los\s+|de\s+las\s+|del\s+|de\s+)", "", n, flags=re.I).strip()
        filas.append((n, al + ([corto] if corto != n and len(clave(corto)) > 3 else []), nv, v))
    junta("batallas", filas, "ediciones_wikipedia")
def masas_agua(): junta("masas_agua", cola_wd4("masas_agua", 3, 40, r"^(list|tipo|masa de agua$)|muelle|túnel|iceberg|vías|solonchak|dimíctico|grao|canal de aguas bravas", minus=True), "ediciones_wikipedia")
def profesiones():
    junta("profesiones", [f for f in cola_wd4("profesiones", 8, 60, r"^(list|ocupación|profesión|categor)") if f[0][:1].islower()], "ediciones_wikipedia")
def formatos():
    ext = {}
    for f in json.loads((D4 / "formatos_ext.json").read_text())["results"]["bindings"]:
        ext.setdefault(f["x"]["value"], set()).add(f["ext"]["value"].strip(". ").lower())
    filas = []
    for r in wd4("formatos"):
        if r["links"] < 4 or not LAT(r["n"]): continue
        e = sorted(x for x in ext.get(r["f"]["x"]["value"], ()) if re.fullmatch(r"[a-z0-9]{2,6}", x))
        if not e: continue
        filas.append((e[0].upper(), [x.upper() for x in e[1:]] + ["." + x for x in e] + [SIN_PAREN(r["n"])], 4 if r["links"] >= 25 else 5, r["links"]))
    junta("formatos", filas, "ediciones_wikipedia")
def pueblos_madrid():
    junta("pueblos_madrid", [(SIN_PAREN(r["n"]), r["alts"][:3], 5, r["links"]) for r in wd4("pueblos_madrid")], "orden_a_mano")
def peter_pan(): junta("peter_pan", [], "orden_a_mano")   # la consulta de Wikidata traía otra obra: solo a mano

# ── personajes: Wikidata y la lista de personajes de la Wikipedia en inglés ──
NO_PERSONAJE = re.compile(r"season|episode|reference|external|see also|notes|cast|overview|main|recurring|guest|minor|other|family|characters?|"
                          r"appearance|production|reception|development|^the |list|staff|employees|friends|relatives|introduced|portrayed|sources|elsewhere|bibliography|salar|accolade|award|loved ones|'s |^sales$|dunder|mifflin|soft kitty", re.I)
# empresas, canciones, grupos y actores que se cuelan entre los personajes
NO_ES_PERSONAJE = re.compile(r"dunder|mifflin|soft kitty|^management$|administrative|here comes treble|^leo and gino$|^mr\. and mrs\.|^(mayim bialik|melanie lynskey|taylor spreitler|"
                             r"anjelika washington|lio tipton|ming-na wen)$", re.I)
def de_lista_personajes(nombre):
    t = texto4(nombre)
    n = re.findall(r"^=+\s*([^=\n]+?)\s*=+\s*$", t, re.M) + re.findall(r"\n[;*]\s*'''([^'\n]{3,40})'''", t) + re.findall(r"\n;\s*([^:\n]{3,40})", t)
    filas = []
    for x in dict.fromkeys(n):
        x = SIN_PAREN(limpia_wiki(x)).strip(" :.'\"")
        if not LAT(x) or not 2 < len(x) < 35 or NO_PERSONAJE.search(x) or len(x.split()) > 4 or not x[:1].isupper(): continue
        filas.append((x, [x.split()[0]] if len(x.split()) > 1 and len(x.split()[0]) > 3 else [], 5, 0))
    return filas
def personajes(slug):
    def f():
        cola = [f for f in (cola_wd4(slug) if (D4 / f"{slug}.json").exists() else []) if not f[0].lower().startswith("familia ")]   # «familia Flynn-Fletcher» no es un personaje
        cola = [f for f in cola + de_lista_personajes(f"{slug}_en") if not NO_ES_PERSONAJE.search(f[0])]
        # lo que es una errata de un nombre puesto a mano («Pam Beesley» por «Pam Beesly») no puede ser otra respuesta
        # pasa a ser alias del de a mano y puntúa como él
        mano = {clave(x): n for n, al, _, _ in a_mano4(slug) for x in [n] + al}
        mas, limpia = mano_t4.ALIAS_MAS.setdefault(slug, {}), []
        for f in cola:
            dueño = None if clave(f[0]) in mano else next((d for m, d in mano.items() if len(m) > 5 and m != clave(f[0]) and difflib.SequenceMatcher(None, clave(f[0]), m).ratio() >= 0.9), None)
            if dueño: mas[dueño] = ", ".join(x for x in [mas.get(dueño, ""), f[0]] + f[1] if x)
            else: limpia.append(f)
        junta(slug, limpia, "orden_a_mano")
    f.__name__ = slug; return f
friends, phineas, bigbang, office, modern_family = [personajes(s) for s in ("friends", "phineas", "bigbang", "office", "modern_family")]

# ── tablas de la Wikipedia ──
def eurovision():
    cola = []
    for fila in re.split(r"\n\|-", texto4("eurovision")):
        c = fila.split("\n|")
        if len(c) > 4 and re.search(r"Eurovisión (19|20)\d\d", c[1]):
            n = limpia_wiki(re.sub(r'^\s*bgcolor="?[^|]*"?\s*\|\s*', "", c[3])).strip(" '")
            n = SIN_PAREN(n)
            if 2 < len(n) < 60 and not re.search(r"\d|bandera|\}|«|teatro|premio|awards", n, re.I):
                cola.append((n, [x.strip() for x in re.split(r"\s+(?:y|&|con)\s+|,", n) if len(x.strip()) > 3], 4, 0))
    print("  artistas en la tabla:", len(cola))
    junta("eurovision", cola, "orden_a_mano")
def circuitos_f1():
    cola = []
    for fila in re.split(r"\n\|-", texto4("circuitos")):
        c = fila.split("\n|")
        if len(c) < 11 or "[[" not in c[1]: continue
        m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", c[1])
        n = (m.group(2) or m.group(1)).strip()
        lugar = limpia_wiki(c[5]).strip(); gp = [g.replace(" Grand Prix", "") for g in re.findall(r"\[\[([^\]|]+?Grand Prix)", c[9])]
        veces = int(re.sub(r"\D", "", c[-1]) or 0)
        cola.append((n, [m.group(1), lugar] + gp, 3 if veces >= 25 else 4 if veces >= 5 else 5, veces))
    junta("circuitos_f1", cola, "grandes_premios_celebrados")
def escuderias():
    cola = []
    for fila in re.split(r"\n\|-", texto4("escuderias")):
        m = re.match(r"\s*\|(?:align=\"?left\"?\|)?\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", fila)
        if m: cola.append((SIN_PAREN(m.group(2) or m.group(1)), [SIN_PAREN(m.group(1))], 5, 0))
    junta("escuderias", cola, "orden_a_mano")
NO_MUSCULO = {"cabeza", "espalda", "cuadrado", "ancho", "músculos", "cuello", "tórax", "abdomen", "cara", "vientre", "inserción", "fusiforme", "peniforme", "semipeniforme", "biventer", "miembro superior", "miembro inferior", "periné", "ojo", "oído", "lengua", "paladar", "faringe", "laringe", "pelvis", "mano", "pie", "brazo", "antebrazo", "muslo", "pierna", "hombro", "cadera"}
def musculos():
    cola = []
    for fila in re.split(r"\n\|-", texto4("musculos")):
        c = [x.strip() for x in fila.split("\n|")]
        if len(c) >= 7:
            es = SIN_PAREN(limpia_wiki(c[6])).split(";")[0].strip()
            if es.lower().startswith("músculo") and len(es) < 60:
                corto = re.sub(r"^músculos?\s+(del\s+|de\s+la\s+|de\s+los\s+|de\s+)?", "", es, flags=re.I).strip()
                if corto.lower() in NO_MUSCULO: continue
                cola.append((corto[0].lower() + corto[1:] if corto else es, [es], 5, 0))
    junta("musculos", cola, "orden_a_mano")
def huesos():
    cola = []
    for m in re.finditer(r"\[\[(?:Hueso |)([^\]|]+)\|[^\]]*\]\]\s*-\s*([^(<\n]+)", texto4("huesos")):
        es = m.group(2).strip().lower()
        partes = [re.sub(r"^huesos?\s+", "", x).strip() for x in re.split(r"\s+[ou]\s+", es)]
        partes = [x for x in partes if 2 < len(x) < 40 and x not in ("del tiempo",)]
        if partes: cola.append((partes[0], partes[1:] + [es], 5, 0))
    junta("huesos", cola, "orden_a_mano")
def latin():
    cola = []
    for fila in re.split(r"\n\|-", texto4("latin")):
        c = fila.split("\n|")
        if len(c) >= 2:
            n = SIN_PAREN(limpia_wiki(c[1])).strip(" .'\"")
            if 2 < len(n) < 60 and LAT(n): cola.append((n[0].lower() + n[1:], [], 5, 0))
    junta("latin", cola, "orden_a_mano")

# ── canciones: todo lo que la artista tiene en Spotify (kworb.net), ordenado por reproducciones ──
def olivia():
    base = lambda t: re.sub(r"\s+-\s+.*$", "", re.sub(r"\s*[\(\[].*$", "", html.unescape(t))).strip()
    filas = {}
    for titulo, n in re.findall(r'<tr><td class="text"><div>(?:\*\s*)?<a[^>]*>(.*?)</a></div></td><td>([\d,]+)</td>', (D4 / "olivia_kworb.html").read_text(encoding="utf-8")):
        b = base(titulo).replace("’", "'"); k = clave(b)
        if not k: continue
        d = filas.setdefault(k, [b, 0]); d[1] += int(n.replace(",", ""))
    orden = sorted(filas.values(), key=lambda f: -f[1])
    junta("olivia", por_puesto([(n, [], v) for n, v in orden], [5, 14, 28, 45]), "reproducciones_spotify")

# ── palabras: lemario (el de la segunda tanda) y frecuencias de OpenSubtitles ──
def _palabras():
    lema = {x.strip().lower() for x in open(FUENTES / "t2" / "palabras.txt", encoding="utf-8", errors="replace") if x.strip()}
    frec = {}
    for i, linea in enumerate(open(FUENTES / "tanda3" / "frecuencias_es.txt", encoding="utf-8")):
        p = linea.split()
        if p and p[0] not in frec: frec[p[0]] = i
    return lema, frec
def plural(p):
    if p.endswith(("s", "x")): return []
    if p[-1] in "aeiouáéó": return [p + "s"]
    if p.endswith("z"): return [p[:-1] + "ces"]
    return [p + "es"]
def por_frecuencia(slug, vale, metrica="frecuencia_de_uso", cortes=(0.12, 0.35, 0.7), formas=False, flexion=None):
    """Las de la lista a mano mandan; el resto del diccionario va por frecuencia de uso (2, 3, 4) y las que no se usan nunca, al 5."""
    lema, frec = _palabras()
    usadas = sorted((p for p in lema if vale(p) and re.fullmatch(r"[a-záéíóúüñ]+", p) and p in frec), key=lambda p: frec[p])
    resto = sorted(p for p in lema if vale(p) and re.fullmatch(r"[a-záéíóúüñ]+", p) and p not in frec)
    filas = []
    for i, p in enumerate(usadas):
        f = i / max(1, len(usadas))
        filas.append((p, (flexion or plural)(p), 2 if f < cortes[0] else 3 if f < cortes[1] else 4 if f < cortes[2] else 5, 10**5 - frec[p]))
    filas += [(p, (flexion or plural)(p), 5, 0) for p in resto]
    if formas:      # plurales, femeninos y verbos conjugados (el diccionario grande viene sin tildes)
        ya = {clave(x) for f in filas for x in [f[0]] + f[1]}
        for p in open(FUENTES / "tanda3" / "palabras_todas.txt", encoding="utf-8", errors="replace"):
            p = p.strip().lower()
            if p.isalpha() and vale(p) and clave(p) not in ya: filas.append((p, [], 5, 0)); ya.add(clave(p))
    junta(slug, filas, metrica)

def palabras_x(): por_frecuencia("palabras_x", lambda p: p.startswith("x"), formas=True)
def dieresis(): por_frecuencia("dieresis", lambda p: "ü" in p)
def inter(): por_frecuencia("inter", lambda p: "inter" in p, formas=True)
NO_LOGIA = {"analogía", "antología", "trilogía", "tetralogía", "pentalogía", "hexalogía", "apología", "tautología", "ideología", "homología",
            "cronología", "genealogía", "neología", "monología", "dilogía", "eulogía", "logía", "-logía", "braquilogía", "batología", "perisología",
            "sinonimia", "doxología", "dialogía", "macrología", "cacología", "fraseología", "terminología", "nomenclatura", "metodología",
            "simbología", "tipología", "morfología", "analogia", "paralogía", "biblioteconomía"}
def logias():
    # terminología, fraseología, metodología, tipología, morfología y simbología pueden ser «disciplina» o no: entran en el 5 aparte
    por_frecuencia("logias", lambda p: p.endswith("logía") and p not in NO_LOGIA)
    import csv as _csv
    filas = list(_csv.reader(open(DATOS / "logias.csv", encoding="utf-8"), delimiter=";"))
    extra = [["terminología", "", "5", "0"], ["fraseología", "", "5", "0"], ["metodología", "", "5", "0"], ["tipología", "", "5", "0"],
             ["morfología", "", "5", "0"], ["simbología", "", "5", "0"], ["cronología", "", "5", "0"], ["genealogía", "", "5", "0"]]
    with open(DATOS / "logias.csv", "w", newline="", encoding="utf-8") as f: _csv.writer(f, delimiter=";").writerows(filas + extra)
ITIS_MAS = """tiroiditis uveítis epicondilitis fascitis vasculitis diverticulitis esofagitis epiglotitis laberintitis mastoiditis glomerulonefritis osteítis
periodontitis bronquiolitis rinosinusitis colangitis ileítis proctitis vulvitis vulvovaginitis epididimitis sacroileítis capsulitis costocondritis retinitis
coroiditis escleritis epiescleritis dacrioadenitis sialoadenitis glositis queilitis faringoamigdalitis traqueítis laringotraqueítis alveolitis mediastinitis
miositis dermatomiositis polimiositis foliculitis paniculitis hidradenitis onfalitis yeyunitis cecitis sigmoiditis proctocolitis ventriculitis aracnoiditis
cerebritis plexitis tenosinovitis entesitis policondritis espondiloartritis poliartritis oligoartritis linfadenitis ooforitis salpingitis cervicitis parametritis
corioamnionitis etmoiditis pulpitis iridociclitis vitritis adrenalitis hipofisitis insulitis pericarditis pancreatitis periartritis bursitis condritis
pielitis ureteritis uretritis balanopostitis postitis vaginitis endometritis anexitis mastitis flebitis neuritis polineuritis radiculitis rinofaringitis
otomastoiditis miringitis labirintitis queratoconjuntivitis blefaroconjuntivitis dacriocistitis canaliculitis orbitopatía? celulitis erisipela? apendicitis
duodenitis enteritis gastroenteritis enterocolitis colecistitis colangiolitis hepatitis esplenitis nefritis cistitis prostatitis orquitis funiculitis
vesiculitis epiploitis peritonitis pleuritis neumonitis bronquitis traqueobronquitis laringitis faringitis amigdalitis adenoiditis sinusitis rinitis otitis
estomatitis gingivitis parotiditis sialadenitis tiroiditis tendinitis tenosinovitis sinovitis artritis osteomielitis espondilitis discitis miocarditis
endocarditis pancarditis aortitis arteritis periarteritis tromboflebitis linfangitis vaginitis encefalitis meningitis meningoencefalitis mielitis
encefalomielitis poliomielitis conjuntivitis blefaritis queratitis iritis dermatitis celulitis vaguitis tontitis""".split()
def itis():
    lema, frec = _palabras()
    broma = {"cuotalitis", "flojeritis", "mieditis", "titulitis", "vaguitis", "tontitis"}
    no = {"litis", "-itis", "raquitis", "ascitis"}
    todas = {p for p in lema if p.endswith(("itis", "ítis")) and p not in no} | {p for p in ITIS_MAS if p.endswith(("itis", "ítis"))}
    filas = []
    for p in todas:
        if p in broma: filas.append((p, [], 5, 0)); continue
        nv = 2 if frec.get(p, 10**6) < 20000 else 3 if p in frec else 4 if p in lema else 5
        filas.append((p, [], nv, 10**5 - frec.get(p, 10**5)))
    filas += [(r["n"].lower(), [], 5, 0) for r in wd4("itis_wd") if r["n"].lower().endswith("itis")]
    junta("itis", filas, "frecuencia_de_uso")

# ── esdrújulas: acento en la antepenúltima sílaba ──
FUERTE, DEBIL = set("aeoáéó"), set("iuü")
def nucleos(p):
    """Trocea la palabra en núcleos vocálicos (sílabas), con diptongos y hiatos; la u de «que, qui, gue, gui» no cuenta."""
    p = re.sub(r"(?<=[qg])u(?=[eéií])", "_", p)
    letras = [c for c in p]
    nuc, actual = [], ""
    for i, c in enumerate(letras):
        if c in "aeiouáéíóúü" or (c == "y" and i == len(letras) - 1 and actual):
            if actual:
                prev = actual[-1]
                hiato = (prev in "aeoáéó" and c in "aeoáéó") or (c in "íú" and prev in "aeoáéó") or (prev in "íú" and c in "aeoáéó")
                if hiato: nuc.append(actual); actual = c
                else: actual += c
            else: actual = c
        else:
            if actual: nuc.append(actual); actual = ""
    if actual: nuc.append(actual)
    return nuc
def acento(p):
    """Cuántas sílabas hay después de la que lleva la tilde (0 aguda, 1 llana, 2 esdrújula, 3+ sobresdrújula). None si no lleva tilde."""
    n = nucleos(p)
    for i, s in enumerate(n):
        if re.search(r"[áéíóú]", s): return len(n) - 1 - i
    return None
def esdrujulas():
    # el lemario solo trae el masculino: antepenúltimo → antepenúltima, antepenúltimos, antepenúltimas
    femenino = lambda p: plural(p) + ([p[:-1] + "a", p[:-1] + "as"] if p.endswith("o") else [])
    por_frecuencia("esdrujulas", lambda p: acento(p) == 2, cortes=(0.08, 0.3, 0.65), flexion=femenino)
    # los plurales que se vuelven esdrújulos (joven → jóvenes, examen → exámenes) también valen
    lema, frec = _palabras()
    import csv as _csv
    filas = list(_csv.reader(open(DATOS / "esdrujulas.csv", encoding="utf-8"), delimiter=";"))
    ya = {clave(x) for f in filas[1:] for x in [f[0]] + [a for a in f[1].split("|") if a]}
    extra = []
    # árbol → árboles, lápiz → lápices, fácil → fáciles: llanas con tilde que en plural ganan una sílaba
    for p in sorted(lema):
        if re.fullmatch(r"[a-záéíóúüñ]+", p) and acento(p) == 1 and p[-1] not in "aeiouáéíóúsxn":
            pl = p[:-1] + "ces" if p.endswith("z") else p + "es"
            if acento(pl) == 2 and clave(pl) not in ya: extra.append([pl, "", "3" if pl in frec else "5", "0"]); ya.add(clave(pl))
    for p in ("jóvenes exámenes orígenes imágenes márgenes volúmenes crímenes órdenes vírgenes certámenes resúmenes dólmenes regímenes especímenes "
              "caracteres? cánones gérmenes hímenes abdómenes cármenes".split()):
        if p.endswith("?") or clave(p) in ya: continue
        extra.append([p, "", "4", "0"])
    with open(DATOS / "esdrujulas.csv", "w", newline="", encoding="utf-8") as f: _csv.writer(f, delimiter=";").writerows(filas + extra)

# ── artistas de Spotify (artistas_spotify.py deja la lista ya cruzada) ──
def artistas(): print("artistas: se monta con artistas_spotify.py")

TODAS = [frigo, refrescos, hacendado, eurovision, friends, phineas, circuitos_f1, provincias, francofonos, palabras_x, esdrujulas, filosofos,
         batallas, huesos, musculos, profesiones, idiomas_paises, peter_pan, pronombres, masas_agua, logias, inter, bimbo, nestle, apple,
         sabores_helado, dulces_navidad, bigbang, office, modern_family, sagas, escuderias, deportes_acuaticos, juegos_invierno, pueblos_madrid,
         hispanohablantes, dieresis, latin, corrientes, hormonas, especialidades, formatos, cocacola, itis, unidades_tiempo, olivia, gases, minerales, halloween]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS:
        if not pedidas or f.__name__ in pedidas: f()
