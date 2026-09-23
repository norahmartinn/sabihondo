"""Convierte datos/banco.csv en el banco de preguntas del juego.

Uso:  python3 scripts/banco.py
Reescribe el bloque `const BANCO=...` de index.html.

Formato de salida: [{q, t:[nivel1..nivel5]}], cada respuesta es [texto, [claves]].
Las claves van normalizadas igual que en el juego (minúsculas, sin tildes,
sin artículos ni preposiciones cortas y sin espacios).
"""
import csv, json, re, unicodedata, collections, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CSV = RAIZ / "datos" / "banco.csv"
HTML = RAIZ / "index.html"

FUERA = {"el","la","los","las","lo","un","una","unos","unas","de","del","al","a","en","y","o"}

def palabras(s):
    # igual que norm() del juego: sin tildes (la ñ también pasa a n) ni signos
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return [w for w in s.split() if w not in FUERA]

def clave(s):
    return "".join(palabras(s))

# Enunciados: el CSV trae algunos a medio traducir o genéricos
PREGUNTAS = {
    4:"Nombra un Patrimonio de la Humanidad que esté en España", 5:"Nombra un equipo de LaLiga de esta temporada",
    6:"Nombra un país del mundo", 7:"Nombra la capital de un país", 8:"Nombra una moneda que se use hoy en algún país",
    14:"Nombra un país de la Unión Europea", 17:"Nombra una constelación",
    9:"Nombra un país de África", 11:"Nombra un país de Europa", 12:"Nombra un país de América",
    13:"Nombra un país de Oceanía", 15:"Nombra un estado de EE. UU.",
    23:"Nombra un postre", 24:"Nombra unos cereales de desayuno", 25:"Nombra una marca de patatas fritas de bolsa",
    26:"Nombra un plato de cuchara", 27:"Nombra un tipo de pizza", 28:"Nombra un licor",
    29:"Nombra una marca de agua mineral", 30:"Nombra un campeón del mundo de Fórmula 1", 31:"Nombra una aerolínea",
    32:"Nombra un club que haya ganado la Champions League", 33:"Nombra un deporte acuático",
    34:"Nombra un deporte de raqueta o de pelota", 35:"Nombra una videoconsola", 36:"Nombra un videojuego de recreativa",
    37:"Nombra un personaje de Super Mario", 38:"Nombra un personaje de Disney", 39:"Nombra un personaje de Pixar",
    40:"Nombra un personaje de Marvel", 41:"Nombra un personaje de Friends", 42:"Nombra un personaje de The Office",
    43:"Nombra una serie de Netflix", 44:"Nombra una serie de Prime Video", 45:"Nombra una sitcom",
    46:"Nombra una película española", 47:"Nombra una película de Disney", 48:"Nombra una película de Marvel",
    49:"Nombra una película basada en un libro", 50:"Nombra un director o directora de cine",
    51:"Nombra un cantante o una cantante internacional", 52:"Nombra un grupo de música español",
    53:"Nombra un festival de música", 54:"Nombra un musical", 55:"Nombra un dios o una diosa griega",
    56:"Nombra un ser mitológico", 57:"Nombra una obra de arte", 58:"Nombra un edificio famoso",
    59:"Nombra un rascacielos", 60:"Nombra un monumento famoso", 61:"Nombra una red social",
    62:"Nombra una aplicación de mensajería", 63:"Nombra una aplicación de música",
    64:"Nombra una marca de ordenadores", 65:"Nombra una marca de relojes", 66:"Nombra una marca de lujo",
    67:"Nombra una marca de zapatillas", 68:"Nombra un banco", 69:"Nombra una cadena de restaurantes",
    70:"Nombra una cadena hotelera", 71:"Nombra una discoteca famosa", 72:"Nombra una fiesta de España",
    73:"Nombra una enfermedad infecciosa",
}

# Nombres con los que se conoce en España lo que el CSV trae en otra forma
ALIAS = {
    "Illes Balears":["Baleares","Islas Baleares"], "Comunitat Valenciana":["Comunidad Valenciana","Valencia"],
    "País Vasco":["Euskadi"], "Bizkaia":["Vizcaya"], "Gipuzkoa":["Guipúzcoa"], "Álava":["Araba"],
    "Girona":["Gerona"], "Lleida":["Lérida"], "Ourense":["Orense"], "Palma":["Palma de Mallorca"],
    "Vitoria-Gasteiz":["Vitoria","Gasteiz"], "Donostia-San Sebastián":["San Sebastián","Donostia"],
    "Castellón de la Plana":["Castellón"], "Las Palmas de Gran Canaria":["Las Palmas"], "Pamplona":["Iruña"],
    "Mickey Mouse":["Mickey"], "Minnie Mouse":["Minnie"], "Donald Duck":["Pato Donald","Donald"],
    "Cinderella":["Cenicienta"], "Snow White":["Blancanieves"], "Winnie the Pooh":["Winnie"],
    "Spider-Man":["Hombre Araña"], "Captain America":["Capitán América"], "Black Widow":["Viuda Negra"],
    "Doctor Strange":["Doctor Extraño"], "Scarlet Witch":["Bruja Escarlata"], "Black Panther":["Pantera Negra"],
    "Silver Surfer":["Estela Plateada"], "Iron Man":["Hombre de Hierro"], "Ant-Man":["Hombre Hormiga"],
    "Human Torch":["Antorcha Humana"], "The Thing":["La Cosa"], "Invisible Woman":["Mujer Invisible"],
    "Mister Fantastic":["Señor Fantástico"], "Green Goblin":["Duende Verde"], "Hawkeye":["Ojo de Halcón"],
    "The Lion King":["El Rey León"], "Armenian Dram":["Dram armenio","Dram"],
    "La Mona Lisa":["Mona Lisa","La Gioconda","Gioconda"],
}

# Prefijos que la gente se salta al contestar, por categoría
PREFIJOS = {
    1:{"principado","comunidad","foral","region"},
    20:{"pico","pica","picu","puig","tuca","tuc","monte","cerro","pena","tossal","alto","punta"},
    21:{"playa","platja","praia","cala"},
    58:{"torre"}, 60:{"torre"},
}
# Categorías de personas: vale el nombre o el apellido si no se repite
PERSONAS = {30, 38, 39, 41, 42, 50, 51}
NO_SUELTAS = {"mouse","duck","doctor","capitan","princesa","senor","señor","the","man","jr"}

def principal():
    filas = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    cats = collections.OrderedDict()
    for f in filas:
        cats.setdefault(int(f["ID categoría"]), []).append(f)

    banco = []
    for cid, fs in cats.items():
        q = PREGUNTAS.get(cid, fs[0]["Pregunta"]).rstrip(". ")
        niveles = [[] for _ in range(5)]
        entradas = []
        for f in fs:
            texto = f["Respuesta canónica"].strip()
            nv = int(f["Nivel"]) - 1
            if any(texto == e[0] for e in entradas):
                continue                    # respuesta repetida en la misma pregunta
            claves = [clave(texto)]
            if f["Alias aceptados"].strip(): claves.append(clave(f["Alias aceptados"]))
            claves += [clave(a) for a in ALIAS.get(texto, [])]
            if f.get("Clave normalizada"): claves.append(f["Clave normalizada"].strip())
            ws = palabras(texto)
            pref = PREFIJOS.get(cid)
            if pref:
                i = 0
                while i < len(ws)-1 and ws[i] in pref: i += 1
                if i: claves.append("".join(ws[i:]))
            claves = [c for c in dict.fromkeys(claves) if c]
            entradas.append([texto, nv, claves, ws])

        # claves explícitas: la primera respuesta que la reclama se la queda
        duenos = {}
        for e in entradas:
            e[2] = [c for c in e[2] if duenos.setdefault(c, e[0]) == e[0]]
        # nombre o apellido suelto, solo si no se repite en la pregunta
        if cid in PERSONAS:
            cuenta = collections.Counter(w for e in entradas if len(e[3]) > 1 for w in {e[3][0], e[3][-1]})
            for e in entradas:
                if len(e[3]) < 2: continue
                for w in {e[3][0], e[3][-1]}:
                    if len(w) >= 4 and cuenta[w] == 1 and w not in NO_SUELTAS and w not in duenos:
                        duenos[w] = e[0]; e[2].append(w)
        for texto, nv, claves, _ in entradas:
            niveles[nv].append([texto, claves])
        banco.append({"q": q, "t": niveles})

    js = "const BANCO=" + json.dumps(banco, ensure_ascii=False, separators=(",", ":")) + ";"
    html = HTML.read_text(encoding="utf-8")
    i = html.index("const BANCO="); j = html.index("</script>", i)
    HTML.write_text(html[:i] + js + html[j:], encoding="utf-8")
    total = sum(len(n) for p in banco for n in p["t"])
    print(f"{len(banco)} preguntas, {total} respuestas")

if __name__ == "__main__":
    principal()
