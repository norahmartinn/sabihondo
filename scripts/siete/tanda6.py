"""Sexta tanda (semana del 2 al 8 de noviembre de 2026).
Lo puesto a mano está en mano_t6.py; las fuentes, en datos/siete/fuentes/t6/. Usa la maquinaria de tanda4/tanda5.
Al escribir a mano, lo dudoso se marcó con «?» (o «? no» si no vale): aquí se quita antes de montar, para no colar
respuestas que no sean ciertas. También se quitan a mano las que no son de la categoría (FUERA6).
    python3 tanda6.py            → rehace todas
    python3 tanda6.py ghibli     → solo esa"""
import tanda5
from tanda5 import *
import mano_t6

D6 = FUENTES / "t6"
FUERA6 = {"concursos_tele": {"Juan y Medio", "El hormiguero", "El hormiguero 3.0", "Cuarto milenio", "Saber vivir", "Caiga quien caiga", "Bricomanía",
            "Vaya semanita", "Noche de fiesta", "Pasa la vida", "Hablando claro", "El kiosko", "De domingo a domingo", "El show de Flo", "Locos por la tele",
            "Hoy no, mañana", "El ojo público", "Ruta Quetzal", "Club Megatrix", "Megatrix", "Leonart", "Superagente 86", "Gente con chispa",
            "El precio justo de Joaquín Prat", "La ruleta de la suerte de Jorge Fernández", "Alta tensión de Luis Larrodera", "Juego de niños de Javier Sardá",
            "Si lo sé no vengo de Jordi Hurtado", "Furor de Alonso Caparrós", "Grand Prix de Ramón García", "El tiempo es oro de Constantino Romero",
            "3×4 de Julia Otero", "Supersonic", "Coplas de ciego", "Los mejores años", "Sorpresa sorpresa", "Lo que necesitas es amor", "Mi casa es la tuya",
            "First Dates", "Gran Hermano", "Supervivientes", "La isla de las tentaciones", "Granjero busca esposa", "El Conquistador del fin del mundo",
            "El Bus", "Pekín Express", "Benidorm Fest", "Acapulco Bay", "Tierra de lobos", "Una pareja feliz", "Juego de juegos"},
          "realities": {"Callejeros", "Callejeros viajeros", "Españoles en el mundo", "Mi casa es la tuya", "Física o Química", "Cambio radical"},
          "influencers": {"Hoy no", "Rosalía", "C. Tangana", "Quevedo", "Bizarrap", "Blanca Suárez", "Úrsula Corberó", "Ester Expósito", "Anna Castillo",
            "Aitana Ocaña", "Lola Índigo", "Bad Gyal", "Abraham Mateo", "Ana Mena", "Aitana", "Belén Aguilera", "Ana Guerra", "Ruth Lorenzo", "Beret",
            "Lucía Gil", "Xuso Jones", "Pilar Rubio", "Sara Carbonero", "Isabel Preysler", "Nuria Roca", "Alberto Chicote", "Jordi Cruz", "Malena Costa",
            "Nieves Álvarez", "David Broncano", "Ignatius Farray", "Grison", "Gerard Romero", "Rubén Martín", "Jijantes", "Paula Echevarría", "Cristina Pedroche",
            "Anabel Pantoja", "Gloria Camila", "Alejandra Rubio", "Laura Matamoros", "Rafa Mora", "Suso Álvarez", "Fiama Rodríguez", "Lucía Sánchez",
            "Melyssa Pinto", "Tom Brusse", "Adara Molinero", "Alejandro Nieto", "Sandra Pica", "Asraf Beno", "Kiko Jiménez", "Sofía Suescun", "Jessica Bueno",
            "Marta López Álamo", "Tania Llasera", "Marina Yers", "Alexia Rivas", "Nerea Garmendia", "Inés Hernand", "Isa Pantoja", "Gaspi", "Mouredev"}}
def limpia(slug, texto):
    malas = FUERA6.get(slug, set())
    buenas = []
    for t in texto.split(","):
        t = t.strip()
        if not t: continue
        principal = t.split("=")[0].strip()
        if ("?" in t and "¿" not in t) or re.search(r"\bno$", t) and "?" in t or principal in malas: continue
        buenas.append(t)
    return ", ".join(buenas)
for slug, niveles in mano_t6.MANO.items():
    mano_t4.MANO[slug] = {nv: limpia(slug, txt) for nv, txt in niveles.items()}

NO_Q = {"q", "qui", "quier", "quero", "quintín", "quique", "quim", "quijano", "quintana", "quirós", "quevedo", "quintero", "quiroga", "quiñones", "quesada", "quijada?"}
def palabras_q(): por_frecuencia("palabras_q", lambda p: p.startswith("q") and p not in NO_Q, formas=True)

def alemania():
    """Las 2.087 ciudades (Stadt) de Alemania de Wikidata; las más conocidas a mano, el resto por población."""
    filas = json.loads((D6 / "alemania" / "ciudades.json").read_text(encoding="utf-8"))
    N1 = {"Berlín", "Hamburgo", "Múnich", "Colonia", "Fráncfort del Meno", "Düsseldorf", "Stuttgart", "Dortmund", "Bremen", "Leipzig", "Dresde", "Núremberg"}
    N2 = {"Hannover", "Essen", "Duisburgo", "Bonn", "Heidelberg", "Bochum", "Wolfsburgo", "Gelsenkirchen", "Mönchengladbach", "Aquisgrán", "Kiel",
          "Rostock", "Potsdam", "Friburgo de Brisgovia", "Maguncia", "Augsburgo", "Wiesbaden", "Karlsruhe", "Mannheim", "Münster", "Lübeck", "Bielefeld",
          "Wuppertal", "Leverkusen", "Ingolstadt", "Ratisbona", "Wurzburgo", "Tréveris", "Coblenza", "Constanza", "Weimar", "Érfurt", "Magdeburgo",
          "Chemnitz", "Halle", "Brunswick", "Kassel", "Gotinga", "Jena", "Bamberg", "Baden-Baden", "Garmisch-Partenkirchen", "Rothenburg ob der Tauber",
          "Hamelín", "Bayreuth", "Oberstdorf", "Füssen", "Passau", "Ulm", "Tubinga", "Marburgo", "Darmstadt", "Saarbrücken", "Oldenburgo", "Osnabrück"}
    ALIAS = {"Fráncfort del Meno": ["Frankfurt", "Fráncfort", "Frankfort", "Frankfurt am Main"], "Múnich": ["Munich", "München"],
             "Colonia": ["Köln", "Cologne"], "Núremberg": ["Nürnberg", "Nuremberg"], "Hannover": ["Hanóver"], "Dresde": ["Dresden"],
             "Friburgo de Brisgovia": ["Friburgo", "Freiburg"], "Wolfsburgo": ["Wolfsburg"], "Duisburgo": ["Duisburg"], "Augsburgo": ["Augsburg"],
             "Magdeburgo": ["Magdeburg"], "Halle": ["Halle an der Saale"]}
    cola = []
    for f in filas:
        n = SIN_PAREN(f["es"] or f["de"])
        if not n or not LAT(n): continue
        al = [SIN_PAREN(f["de"])] + ALIAS.get(n, [])
        nv = 1 if n in N1 else 2 if n in N2 else 3 if f["pob"] >= 100000 else 4 if f["pob"] >= 30000 else 5
        cola.append((n, al, nv, int(f["pob"])))
    junta("alemania", cola, "poblacion")

mano_t4.MANO["palabras_q"] = {1: "queso=quesos, quince, querer, quemar, quitar, química, quiosco=kiosco, quirófano, quinto, quieto, quedarse=quedar, que, quien=quién, "
                                  "qué, quizá=quizás, quejarse=queja, Quijote=quijote, querido, quinientos, quiniela, quilo=kilo"}
SOLO6 = solo_mano(*[s for s in mano_t6.MANO])
TODAS6 = SOLO6 + [palabras_q, alemania]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS6:
        if not pedidas or f.__name__ in pedidas: f()
