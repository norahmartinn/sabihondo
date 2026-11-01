"""«Nombra una de las 500 películas mejor valoradas en Letterboxd» (tanda 6).
Lista oficial «Letterboxd's Top 500 Films» (letterboxd.com/official/list/letterboxds-top-500-films, bajada el 2026-11-01
en datos/siete/fuentes/t6/letterboxd/). Títulos en español de Wikidata (etiqueta, artículo de es.wikipedia y títulos
alternativos, que traen los de España y los de Latinoamérica). Nivel por lo conocida que es (enlaces de Wikidata),
con las películas más famosas a mano con su título de España.
    python3 letterboxd.py   → datos/siete/letterboxd.csv"""
import csv, json, re
from pathlib import Path
from comun import clave

RAIZ = Path(__file__).resolve().parents[2]
D = RAIZ / "datos/siete/fuentes/t6/letterboxd"
SALIDA = RAIZ / "datos/siete/letterboxd.csv"
SIN_PAREN = lambda t: re.sub(r"\s*\(.*?\)", "", t).strip()
# las que todo el mundo conoce en España, con el título que se usa aquí (slug de Letterboxd: título)
N1 = {"the-godfather": "El padrino", "the-lion-king": "El rey león", "forrest-gump": "Forrest Gump", "the-matrix": "Matrix",
  "spirited-away": "El viaje de Chihiro", "gladiator-2000": "Gladiator", "pulp-fiction": "Pulp Fiction", "the-dark-knight": "El caballero oscuro",
  "the-shawshank-redemption": "Cadena perpetua", "back-to-the-future": "Regreso al futuro", "the-silence-of-the-lambs": "El silencio de los corderos",
  "fight-club": "El club de la lucha", "schindlers-list": "La lista de Schindler", "interstellar": "Interstellar", "inception": "Origen",
  "walle": "WALL·E", "the-lord-of-the-rings-the-fellowship-of-the-ring": "El señor de los anillos: La comunidad del anillo",
  "the-lord-of-the-rings-the-return-of-the-king": "El señor de los anillos: El retorno del rey",
  "the-lord-of-the-rings-the-two-towers": "El señor de los anillos: Las dos torres", "star-wars": "Star Wars: Una nueva esperanza",
  "harry-potter-and-the-prisoner-of-azkaban": "Harry Potter y el prisionero de Azkaban", "ratatouille": "Ratatouille", "mulan": "Mulán",
  "parasite-2019": "Parásitos", "oppenheimer-2023": "Oppenheimer", "life-is-beautiful": "La vida es bella", "terminator-2-judgment-day": "Terminator 2",
  "the-shining": "El resplandor", "psycho": "Psicosis", "the-empire-strikes-back": "El imperio contraataca"}
N2 = {"casablanca": "Casablanca", "the-godfather-part-ii": "El padrino II", "dead-poets-society": "El club de los poetas muertos",
  "saving-private-ryan": "Salvar al soldado Ryan", "the-good-the-bad-and-the-ugly": "El bueno, el feo y el malo", "alien": "Alien, el octavo pasajero",
  "the-great-dictator": "El gran dictador", "raiders-of-the-lost-ark": "En busca del arca perdida", "inglourious-basterds": "Malditos bastardos",
  "the-green-mile": "La milla verde", "the-prestige": "El truco final", "django-unchained": "Django desencadenado", "the-truman-show": "El show de Truman",
  "se7en": "Seven", "goodfellas": "Uno de los nuestros", "scarface-1983": "El precio del poder", "shutter-island": "Shutter Island",
  "my-neighbor-totoro": "Mi vecino Totoro", "howls-moving-castle": "El castillo ambulante", "your-name": "Your Name",
  "good-will-hunting": "El indomable Will Hunting", "spider-man-into-the-spider-verse": "Spider-Man: Un nuevo universo",
  "eternal-sunshine-of-the-spotless-mind": "¡Olvídate de mí!", "how-to-train-your-dragon": "Cómo entrenar a tu dragón",
  "the-pianist": "El pianista", "one-flew-over-the-cuckoos-nest": "Alguien voló sobre el nido del cuco", "12-angry-men": "Doce hombres sin piedad",
  "whiplash-2014": "Whiplash", "the-intouchables": "Intocable", "mad-max-fury-road": "Mad Max: Furia en la carretera",
  "the-grand-budapest-hotel": "El gran hotel Budapest", "pans-labyrinth": "El laberinto del fauno", "kill-bill-vol-1": "Kill Bill: Volumen 1",
  "coraline": "Los mundos de Coraline", "dune-part-two": "Dune: Parte dos", "the-departed": "Infiltrados", "black-swan": "Cisne negro",
  "memento": "Memento", "all-about-my-mother": "Todo sobre mi madre", "amelie": "Amélie", "the-sound-of-music": "Sonrisas y lágrimas",
  "2001-a-space-odyssey": "2001: Una odisea del espacio", "some-like-it-hot": "Con faldas y a lo loco", "no-country-for-old-men": "No es país para viejos",
  "everything-everywhere-all-at-once": "Todo a la vez en todas partes", "spider-man-across-the-spider-verse": "Spider-Man: Cruzando el Multiverso",
  "princess-mononoke": "La princesa Mononoke", "grave-of-the-fireflies": "La tumba de las luciérnagas", "american-history-x": "American History X",
  "trainspotting": "Trainspotting", "singin-in-the-rain": "Cantando bajo la lluvia", "modern-times": "Tiempos modernos", "the-odyssey-2026": "La odisea"}
# el nombre de la saga a secas cuenta como su película de la lista (la primera que aparezca aquí)
SAGA = {"the-lord-of-the-rings-the-fellowship-of-the-ring": "El señor de los anillos|Lord of the Rings|El señor de los anillos 1",
  "star-wars": "Star Wars|La guerra de las galaxias", "harry-potter-and-the-prisoner-of-azkaban": "Harry Potter",
  "kill-bill-vol-1": "Kill Bill", "dune-part-two": "Dune 2", "the-godfather-part-ii": "El padrino 2", "mad-max-fury-road": "Mad Max"}
pel = json.load(open(D / "top500.json", encoding="utf-8")); wd = json.load(open(D / "wikidata.json", encoding="utf-8"))
links = sorted((int(wd.get(p["slug"], {}).get("links", 0)) for p in pel), reverse=True)
corte = lambda pos: links[min(pos, len(links) - 1)]
U3, U4 = corte(170), corte(330)      # el resto, por lo conocida que es: ~120 en nivel 3, ~160 en el 4, ~170 en el 5
filas = []
for p in pel:
    s, w = p["slug"], wd.get(p["slug"], {})
    orig = re.sub(r"\s*\(\d{4}\)$", "", p["nombre"])
    al = [orig, w.get("es", ""), SIN_PAREN(w.get("eswiki", "")), w.get("en", "")]
    al += [a for a in w.get("alts", "").split("|") if a and len(a) <= 60 and not re.search(r"secuela|precuela|película de", a, re.I)]
    al += [a for a in SAGA.get(s, "").split("|") if a]
    n = int(w.get("links", 0))
    if s in N1: nv, disp = 1, N1[s]
    elif s in N2: nv, disp = 2, N2[s]
    else: nv, disp = (3 if n >= U3 else 4 if n >= U4 else 5), (w.get("es") if w.get("es") and clave(w.get("es")) != clave(orig) and n >= U3 else orig)
    filas.append((disp, al, nv, n))
faltan = [k for k in list(N1) + list(N2) if k not in {p["slug"] for p in pel}]
print("a mano y no están en la lista:", faltan)
vistos = set()
with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";"); w.writerow(["respuesta", "alias", "nivel", "orden_a_mano"])
    for disp, al, nv, n in sorted(filas, key=lambda f: (f[2], -f[3])):
        k = clave(disp)
        if not k or k in vistos: print("doble:", disp); continue
        al = [a for a in dict.fromkeys(al) if a and clave(a) and clave(a) != k and clave(a) not in vistos]
        vistos.add(k); vistos.update(clave(a) for a in al)
        w.writerow([disp, "|".join(al), nv, n])
print(SALIDA.name, len(filas))
