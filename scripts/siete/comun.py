"""Piezas comunes del banco de las siete preguntas.

Cada pregunta tiene su script (apellidos.py, capitales.py…), que deja en
datos/siete/<slug>.csv una fila por respuesta: respuesta; alias; nivel; métrica.
monta.py junta los siete CSV en banco/NN.json y en el `const PREGUNTAS` de index.html.
"""
import csv, json, re, unicodedata, pathlib, urllib.request, urllib.parse, time
import concurrent.futures as cf

RAIZ = pathlib.Path(__file__).resolve().parent.parent.parent
DATOS = RAIZ / "datos" / "siete"
FUENTES = DATOS / "fuentes"
UA = {"User-Agent": "SabihondoBanco/1.0 (https://norahmartinn.github.io/sabihondo/)"}
FUERA = {"el","la","los","las","lo","un","una","unos","unas","de","del","al","a","en","y","o"}

def clave(s):
    # igual que norm() + compacta() del juego: sin tildes, signos, artículos ni espacios
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return "".join(w for w in re.sub(r"[^a-z0-9]+", " ", s).split() if w not in FUERA)

def nivel_por_umbral(valor, umbrales):
    """umbrales: cuatro valores de mayor a menor. Devuelve 1 (obvio) a 5 (nicho)."""
    for i, u in enumerate(umbrales):
        if valor >= u: return i + 1
    return 5

def nivel_por_puesto(puesto, cortes):
    """cortes: hasta qué puesto (empezando en 1) llega cada uno de los cuatro primeros niveles."""
    for i, c in enumerate(cortes):
        if puesto <= c: return i + 1
    return 5

def guarda(slug, filas, metrica):
    """filas: [(respuesta, [alias], nivel, valor)]. Quita repetidas quedándose con la más conocida."""
    vistas, limpio = set(), []
    for r, alias, nv, val in sorted(filas, key=lambda f: (f[2], -float(f[3] or 0))):
        k = clave(r)
        if not k or k in vistas: continue
        vistas.add(k)
        al = []
        for a in alias:
            ka = clave(a)
            if ka and ka != k and ka not in vistas and a not in al: al.append(a); vistas.add(ka)
        limpio.append((r, al, nv, val))
    with open(DATOS / f"{slug}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["respuesta", "alias", "nivel", metrica])
        for r, al, nv, val in limpio: w.writerow([r, "|".join(al), nv, val])
    cuenta = [sum(1 for x in limpio if x[2] == n) for n in range(1, 6)]
    print(f"{slug}: {len(limpio)} respuestas, por nivel {cuenta}")
    for n in range(1, 6):
        print(f"  N{n}:", ", ".join(x[0] for x in limpio if x[2] == n)[:230])

def visitas(wiki, titulos, cache):
    """Visitas de personas (no bots) a cada artículo entre oct. 2025 y sept. 2026."""
    ruta = FUENTES / cache
    hechas = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}
    def una(t):
        u = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/%s.wikipedia/all-access/user/%s/monthly/20251001/20260930"
             % (wiki, urllib.parse.quote(t.replace(" ", "_"), safe="")))
        for intento in range(3):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
                return t, sum(i["views"] for i in d["items"])
            except urllib.error.HTTPError as e:
                if e.code == 404: return t, 0
                time.sleep(1 + intento)
            except Exception:
                time.sleep(1 + intento)
        return t, None
    faltan = [t for t in dict.fromkeys(titulos) if hechas.get(t) is None]
    with cf.ThreadPoolExecutor(6) as ex:
        for t, v in ex.map(una, faltan): hechas[t] = v
    ruta.write_text(json.dumps(hechas, ensure_ascii=False, indent=0), encoding="utf-8")
    return hechas
