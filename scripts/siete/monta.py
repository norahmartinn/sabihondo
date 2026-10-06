"""Junta los siete CSV de datos/siete en el banco del juego.

Uso:  python3 scripts/siete/monta.py
Escribe un banco/NN.json por pregunta y reescribe `const PREGUNTAS` y `const CALENDARIO` en index.html.
Las preguntas nuevas se añaden SIEMPRE al final de PREGUNTAS (el número de archivo es su posición).
Qué siete salen cada día lo dice datos/calendario.csv: fecha;slug;slug;slug;slug;slug;slug;slug
Para rehacer un CSV, lanza antes el script de esa pregunta (apellidos.py, capitales.py…).

Formato de banco/NN.json: {q, t:[nivel1..nivel5]}. Cada respuesta es [texto, [claves]], o solo el texto
cuando su única clave es la del propio texto (el juego la calcula al cargar; así los apellidos pesan la mitad)."""
from comun import *

PREGUNTAS = [
    ("Nombra algo que hay en una boda", "boda"),
    ("Nombra una marca de cerveza", "cervezas"),
    ("Nombra una marca de relojes", "relojes"),
    ("Nombra una canción de Taylor Swift", "taylor"),
    ("Nombra un apellido español", "apellidos"),
    ("Nombra una carrera universitaria", "carreras"),
    ("Nombra la capital de un país", "capitales"),
    # segunda tanda (tanda2.py), semana del 7 al 11 de octubre de 2026
    ("Nombra un supermercado", "supermercados"),
    ("Nombra una marca de zapatillas", "zapatillas"),
    ("Nombra un streamer o youtuber español", "youtubers"),
    ("Nombra un Pokémon de la primera generación", "pokemon"),
    ("Nombra un miedo o una fobia", "fobias"),
    ("Nombra un color", "colores"),
    ("Nombra una prenda de ropa", "prendas"),
    ("Nombra un medio de transporte", "transporte"),
    ("Nombra un electrodoméstico", "electrodomesticos"),
    ("Nombra un idioma", "idiomas"),
    ("Nombra una fiesta de España", "fiestas"),
    ("Nombra un rapero o trapero español", "raperos"),
    ("Nombra una empresa del IBEX 35", "ibex"),
    ("Nombra un nombre vasco", "nombres_vascos"),
    ("Nombra una discoteca", "discotecas"),
    ("Nombra un juego de cartas", "cartas"),
    ("Nombra un DJ", "dj"),
    ("Nombra un personaje de Shrek", "shrek"),
    ("Nombra un personaje de Harry Potter", "hp"),
    ("Nombra un personaje de Bob Esponja", "bob"),
    ("Nombra una película de miedo", "miedo"),
    ("Nombra un anime", "anime"),
    ("Nombra un personaje de Mario Kart", "mariokart"),
    ("Nombra un juego de móvil", "movil"),
    ("Nombra algo del menú de McDonald's", "mcdonalds"),
    ("Nombra una marca de coche de lujo", "coches_lujo"),
    ("Nombra un país donde se conduce por la izquierda", "paises_izquierda"),
    ("Nombra un país con rey o reina", "paises_rey"),
    ("Nombra una ciudad de Italia", "italia"),
    ("Nombra un país del mundo", "paises"),
    ("Nombra una estación del Metro de Madrid", "metro"),
    ("Nombra un clásico de animación de Disney", "disney"),
    ("Nombra una canción de los Beatles", "beatles"),
    ("Nombra un equipo que haya jugado en Primera División", "primera"),
    ("Nombra una palabra que empiece por Ñ", "enie"),
]

banco = RAIZ / "banco"
for viejo in banco.glob("*.json"): viejo.unlink()
indice = []
for i, (q, slug) in enumerate(PREGUNTAS):
    niveles, usadas = [[] for _ in range(5)], set()
    with open(DATOS / f"{slug}.csv", encoding="utf-8") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            claves = []
            for txt in [fila["respuesta"]] + [a for a in fila["alias"].split("|") if a]:
                k = clave(txt)
                if k and k not in usadas: usadas.add(k); claves.append(k)
            if not claves: continue
            r = fila["respuesta"]
            niveles[int(fila["nivel"]) - 1].append(r if claves == [clave(r)] else [r, claves])
    n = sum(map(len, niveles))
    (banco / f"{i:02d}.json").write_text(json.dumps({"q": q, "t": niveles}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    indice.append({"q": q, "n": n})
    print(f"{i:02d} {q}: {n} respuestas, {(banco / f'{i:02d}.json').stat().st_size // 1024} KB")

# calendario: cada fecha con sus siete preguntas, en el orden en que salen
slugs = [s for _, s in PREGUNTAS]
calendario, usadas = {}, {}
with open(RAIZ / "datos" / "calendario.csv", encoding="utf-8") as f:
    for fila in csv.reader(f, delimiter=";"):
        if not fila or fila[0].startswith("#") or fila[0] == "fecha": continue
        fecha, del_dia = fila[0].strip(), [x.strip() for x in fila[1:] if x.strip()]
        assert len(del_dia) == 7 and len(set(del_dia)) == 7, f"{fecha}: hacen falta 7 preguntas distintas"
        for x in del_dia:
            assert x in slugs, f"{fecha}: no existe la pregunta «{x}»"
            if x in usadas: print(f"  aviso: «{x}» sale el {usadas[x]} y otra vez el {fecha}")
            usadas[x] = fecha
        calendario[fecha] = [slugs.index(x) for x in del_dia]
print(f"calendario: {len(calendario)} días, hasta el {max(calendario)}")
print("sin fecha todavía:", [x for x in slugs if x not in usadas] or "ninguna")

html = (RAIZ / "index.html").read_text(encoding="utf-8")
bloque = ("const PREGUNTAS=" + json.dumps(indice, ensure_ascii=False, separators=(",", ":")) + ";\n"
          + "const CALENDARIO=" + json.dumps(calendario, separators=(",", ":")) + ";")
nuevo, veces = re.subn(r"const PREGUNTAS=\[.*?\];(\s*const CALENDARIO=\{.*?\};)?", lambda m: bloque, html, count=1, flags=re.S)
assert veces == 1
(RAIZ / "index.html").write_text(nuevo, encoding="utf-8")
