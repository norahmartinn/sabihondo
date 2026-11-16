"""Batería de respuestas normales contra el banco montado: dice cuáles no casarían.
    python3 bateria.py baterias_t8.txt
El archivo: una línea «## Pregunta exacta» y debajo respuestas separadas por comas."""
import sys, json, pathlib
from comun import clave, RAIZ
banco = {}
for f in (RAIZ / "banco").glob("*.json"):
    d = json.loads(f.read_text(encoding="utf-8")); claves = set()
    for nivel in d["t"]:
        for x in nivel:
            if isinstance(x, str): claves.add(clave(x))
            else: claves.update(x[1]); claves.add(clave(x[0]))
    banco[d["q"]] = claves
q, fallos, total = None, 0, 0
for linea in open(sys.argv[1], encoding="utf-8"):
    linea = linea.strip()
    if linea.startswith("##"):
        q = linea[2:].strip(); assert q in banco, q; print("\n" + q); continue
    for r in (x.strip() for x in linea.split(",") if x.strip()):
        total += 1
        if clave(r) not in banco[q]: fallos += 1; print("  falta:", r)
print(f"\n{fallos} de {total} no casan")
