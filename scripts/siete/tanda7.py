"""Séptima tanda (semana del 9 de noviembre de 2026).
Lo puesto a mano está en mano_t7.py; las fuentes, en datos/siete/fuentes/t7/. Usa la maquinaria de tanda4/tanda5/tanda6.
    python3 tanda7.py            → rehace todas
    python3 tanda7.py simpsons   → solo esa"""
import tanda6
from tanda6 import *
import mano_t7

D7 = FUENTES / "t7"
CON_INTERROGACION.add("Why You Wanna Fight?")
for slug, niveles in mano_t7.MANO.items():
    mano_t4.MANO[slug] = {nv: limpia(slug, txt) for nv, txt in niveles.items()}
mano_t4.MANO["taquilleras"] = dict(mano_t7.TAQUILLERAS)
# en las de Barbie también vale el título sin «Barbie:», «Barbie en…» o «Barbie y…»
def _sin_barbie(txt):
    out = []
    for x in txt.split(","):
        f = x.strip().split("=")
        corto = re.sub(r"^Barbie(:| en| y| como| presenta)\s+", "", f[0]).strip()
        out.append("=".join(f + ([corto[0].upper() + corto[1:]] if corto and corto != f[0] else [])))
    return ", ".join(out)
mano_t4.MANO["barbie_pelis"] = {nv: _sin_barbie(t) for nv, t in mano_t4.MANO["barbie_pelis"].items()}
FUSIONA["simpsons"] = por_contenido
VARIANTES4["parques_nacionales"] = ["Parque Nacional de {}", "Parque Nacional {}"]

def simpsons():
    """Personajes de Los Simpson en Wikidata (P1441 = Los Simpson): lo de mano manda; el resto, por enlaces de Wikipedia."""
    filas = json.loads((D7 / "simpsons_wd.json").read_text(encoding="utf-8"))["results"]["bindings"]
    vale = {"fictional human", "animated character", "television character", "film character", "fictional dog", "fictional cat",
            "comics character", "video game character", "persona in a work of fiction", "character in a fictitious work",
            "fictional young girl", "fictional young boy", "fictional lizard"}
    cola = []
    for b in filas:
        if not vale & set(b["tipos"]["value"].split("|")): continue
        n = SIN_PAREN((b.get("es") or b.get("en") or {}).get("value", ""))
        if not n or not LAT(n) or n.startswith("Q"): continue
        en = SIN_PAREN(b.get("en", {}).get("value", ""))
        enlaces = int(b["n"]["value"])
        cola.append((n, [en] if en and en != n else [], 4 if enlaces >= 8 else 5, enlaces))
    junta("simpsons", cola, "enlaces_wikipedia")

def cintura():
    """La lista de Norah (en inglés, con sus puntos: +10 → nivel 1 … +100 → nivel 5), con el español de las comunes y lo de CINTURA_MAS."""
    NIVEL = {10: 1, 30: 2, 60: 3, 85: 4, 100: 5}
    cola = []
    with open(D7 / "cintura_norah.csv", encoding="utf-8") as f:
        for i, fila in enumerate(csv.DictReader(f, delimiter=";")):
            en, nv = fila["respuesta"].strip(), NIVEL[int(fila["puntos"])]
            formas = mano_t7.CINTURA_ES.get(en, "").split("=") if en in mano_t7.CINTURA_ES else []
            n = formas[0] if formas else en
            al = formas[1:] + ([en] if formas and en != "Clitorisyou" else [])
            cola.append((n, al, nv, -i))
    for nv, txt in mano_t7.CINTURA_MAS.items():
        for x in txt.split(","):
            f = [y.strip() for y in x.split("=") if y.strip()]
            if f: cola.append((f[0], f[1:], nv, -9999))
    junta("cintura", cola, "puntos_de_norah")

SOLO7 = solo_mano(*[s for s in mano_t7.MANO if s != "simpsons"], "taquilleras")
TODAS7 = SOLO7 + [simpsons, cintura]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS7:
        if not pedidas or f.__name__ in pedidas: f()
