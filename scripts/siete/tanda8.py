"""Octava tanda (semana del 16 de noviembre de 2026).
Lo puesto a mano está en mano_t8.py; las fuentes, en datos/siete/fuentes/t8/ (las baja baja_tanda8.py).
Usa la maquinaria de tanda4/tanda5/tanda6/tanda7.
    python3 tanda8.py                   → rehace todas
    python3 tanda8.py ciudad_portugal   → solo esa"""
import tanda7
from tanda7 import *
import mano_t8
import tanda3

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


def raza_perro():
    """Las razas de perro de Wikidata (P31 = raza de perro); las conocidas en España, a mano."""
    junta("raza_perro", por_tramos(wd8("perros"), [(60, 3), (250, 4), (None, 5)]), "enlaces_wikipedia")

PALABRA_Y_MANO = ["yo", "ya", "yogur", "yate", "yema", "yegua", "yeso", "yoyó", "yudo", "yunque", "yacimiento", "yerno", "yoga", "yanqui"]
PALABRA_Y_3 = ["yuca", "yaya", "yayo", "yendo", "yincana", "yonki", "yupi", "yuyu", "yogurt", "yogurtera", "yesca", "yunta", "yute", "yuxtaposición", "yanki", "yihadista", "yoyo", "yate", "yudoca", "yudoka", "yerbabuena"]
PALABRA_Y_FUERA = {"york", "yale", "ye"}
def palabra_y():
    """Palabras del lemario que empiezan por Y (sin nombres propios); niveles por frecuencia en OpenSubtitles."""
    lema, frec = tanda3._palabras()
    vale = lambda p: re.fullmatch(r"y[a-záéíóúüñ]+", p)
    comunes = sorted((p for p in lema if vale(p) and p in frec and p not in PALABRA_Y_MANO), key=lambda p: frec[p])
    resto = sorted(p for p in lema if vale(p) and p not in frec and p not in PALABRA_Y_MANO)
    filas = [(p, [], 1 if i < 6 else 2, 10**6 - i) for i, p in enumerate(PALABRA_Y_MANO)]
    filas += [(p, [], 2 + (i * 3 // max(1, len(comunes))), 10**5 - frec[p]) for i, p in enumerate(comunes)]
    filas += [(p, [], 5, 0) for p in resto]
    ya_estan = {p for p, *_ in filas}
    filas = [f for f in filas if f[0] not in PALABRA_Y_FUERA]
    filas += [(p, [], 3, 9 * 10**5) for p in PALABRA_Y_3 if p not in ya_estan]
    # el plural también vale
    filas = [(p, al + ([p + "s"] if p[-1] in "aeiouáéó" else [p + "es"]), nv, v) for p, al, nv, v in filas]
    guarda("palabra_y", filas, "frecuencia_opensubtitles")

CON_FUNCION = {"ciudad_portugal", "raza_perro"}
SOLO8 = solo_mano(*[s for s in mano_t8.MANO if s not in CON_FUNCION])
TODAS8 = SOLO8 + [ciudad_portugal, raza_perro, palabra_y]
if __name__ == "__main__":
    pedidas = sys.argv[1:]
    for f in TODAS8:
        if not pedidas or f.__name__ in pedidas: f()
