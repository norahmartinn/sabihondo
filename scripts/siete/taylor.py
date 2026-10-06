"""Canciones de Taylor Swift.
Lista: las publicadas de «List of songs by Taylor Swift» (Wikipedia en inglés) que canta ella.
Nivel: reproducciones en Spotify según kworb.net, sumando todas las versiones de cada canción
(original, Taylor's Version, directos, remezclas)."""
import html
from comun import *

def base(t):
    t = html.unescape(t).replace("$", "s")        # Wi$h Li$t
    t = re.sub(r"\s*[\(\[].*$", "", t)            # (Taylor's Version), [From The Vault], (feat. …)
    t = re.sub(r"\s+-\s+.*$", "", t)              # - Karaoke Version, - Live…
    return t.strip()

kworb = (FUENTES / "taylor_kworb.html").read_text(encoding="utf-8")
streams = {}
for titulo, n in re.findall(r'<tr><td class="text"><div>(?:\*\s*)?<a[^>]*>(.*?)</a></div></td><td>([\d,]+)</td>', kworb):
    k = clave(base(titulo))
    streams[k] = streams.get(k, 0) + int(n.replace(",", ""))

wiki = json.loads((FUENTES / "taylor_wikipedia.json").read_text(encoding="utf-8"))["parse"]["wikitext"]["*"]
wiki = wiki.split("== Released songs ==")[1].split("== Unreleased songs ==")[0]   # las inéditas no cuentan
canciones = {}
for fila in wiki.split("\n|-")[1:]:
    m = re.match(r'\s*!\s*scope="?row"?\s*\|\s*(.*)', fila)
    if not m: continue
    celdas = fila.split("\n|")
    if len(celdas) < 2 or "Swift, Taylor" not in celdas[1] and "Taylor Swift" not in celdas[1]: continue
    t = m.group(1)
    t = urllib.parse.unquote(re.sub(r"<!--.*?-->|<small>.*?</small>", "", t))
    t = re.sub(r"\{\{anchor\|[^}]*\}\}|<ref.*?(/>|</ref>)|\{\{efn.*", "", t, flags=re.S)
    t = re.sub(r"\{\{sort\|[^|]*\|(.*?)\}\}", r"\1", t, flags=re.I)
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", t)
    t = t.replace("''", "").strip().strip('"').strip()
    t = re.sub(r'"\s*(\(.*\))$', r" \1", t)          # "Titulo" (remix) → Titulo (remix)
    if t: canciones.setdefault(clave(base(t)), base(t))

sin_datos = [n for k, n in canciones.items() if k not in streams]
orden = sorted(canciones.items(), key=lambda kv: -streams.get(kv[0], 0))
# sin datos en Spotify solo quedan versiones sueltas de canciones ajenas («Baby», «Umbrella»): fuera
filas = [(n, [], nivel_por_puesto(i, [15, 45, 100, 180]), streams.get(k, 0)) for i, (k, n) in enumerate(orden, 1) if streams.get(k)]
guarda("taylor", filas, "reproducciones_spotify")
print("sin datos de Spotify:", len(sin_datos), sin_datos[:40])
print("en Spotify y no en la lista:", [k for k in streams if k not in canciones][:40])
