"""Octava tanda (semana del 16 de noviembre de 2026).
Lo puesto a mano está en mano_t8.py; las fuentes, en datos/siete/fuentes/t8/ (las baja baja_tanda8.py).
Usa la maquinaria de tanda4/tanda5/tanda6/tanda7.
    python3 tanda8.py                   → rehace todas
    python3 tanda8.py ciudad_portugal   → solo esa"""
import tanda7
from tanda7 import *
import mano_t8

D8 = FUENTES / "t8"
for slug, niveles in mano_t8.MANO.items():
    mano_t4.MANO[slug] = {nv: limpia(slug, txt) for nv, txt in niveles.items()}

def wd8(nombre):
    """Filas de Wikidata (etiqueta es, si no la en; alias es y la etiqueta en), de más a menos enlaces."""
    filas, vistos = [], set()
    for f in json.loads((D8 / f"{nombre}.json").read_text(encoding="utf-8"))["results"]["bindings"]:
        v = lambda k: f[k]["value"] if k in f else ""
        if v("x") in vistos: continue
        vistos.add(v("x"))
        n, en = SIN_PAREN(v("xLabel")), SIN_PAREN(v("en"))
        if not n or re.fullmatch(r"Q\d+", n): n = en
        if not n or re.fullmatch(r"Q\d+", n) or not LAT(n): continue
        al = [a for a in [en] + v("alts").split("|") if a and a != n and len(a) < 45 and LAT(a)]
        filas.append((n, al, int(v("links") or 0)))
    return sorted(filas, key=lambda r: -r[2])

def por_tramos(filas, tramos):
    """tramos = [(cuántos, nivel), …, (None, nivel)]: los primeros N por enlaces a un nivel, los siguientes a otro."""
    cola, i = [], 0
    for cuantos, nv in tramos:
        trozo = filas[i:] if cuantos is None else filas[i:i + cuantos]
        cola += [(n, al, nv, l) for n, al, l in trozo]
        i += len(trozo)
        if cuantos is None: break
    return cola

def ciudad_portugal():
    """Los 308 municipios de Portugal y todo lo que Wikidata da como ciudad portuguesa; lo conocido, a mano."""
    junta("ciudad_portugal", por_tramos(wd8("portugal"), [(80, 3), (150, 4), (None, 5)]), "enlaces_wikipedia")

SOLO8 = solo_mano(*[s for s in mano_t8.MANO if s != "ciudad_portugal"])
TODAS8 = SOLO8 + [ciudad_portugal]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS8:
        if not pedidas or f.__name__ in pedidas: f()
