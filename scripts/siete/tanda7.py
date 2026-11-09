"""Séptima tanda (semana del 9 de noviembre de 2026).
Lo puesto a mano está en mano_t7.py; las fuentes, en datos/siete/fuentes/t7/. Usa la maquinaria de tanda4/tanda5/tanda6.
    python3 tanda7.py            → rehace todas
    python3 tanda7.py simpsons   → solo esa"""
import tanda6
from tanda6 import *
import mano_t7

D7 = FUENTES / "t7"
for slug, niveles in mano_t7.MANO.items():
    mano_t4.MANO[slug] = {nv: limpia(slug, txt) for nv, txt in niveles.items()}
mano_t4.MANO["taquilleras"] = dict(mano_t7.TAQUILLERAS)
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

SOLO7 = solo_mano(*[s for s in mano_t7.MANO if s != "simpsons"], "taquilleras")
TODAS7 = SOLO7 + [simpsons]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS7:
        if not pedidas or f.__name__ in pedidas: f()
