"""Descarga las fuentes de «Nombra una discoteca» a datos/siete/fuentes/t3/.
Se puede relanzar: lo que ya está bajado no se vuelve a pedir.

  · OpenStreetMap (Overpass): todo lo etiquetado amenity=nightclub con nombre, país a país. De España
    también lo que ya cerró (disused:/was:/abandoned:amenity=nightclub), que ahí están las de la Ruta.
  · Xceed (events.xceed.me): el listado de locales de la plataforma de entradas, fuerte en España,
    Italia, Portugal, Alemania y Francia.
La de Wikidata (discotecas con artículo en Wikipedia) ya la baja baja_tanda2.py."""
from comun import *
T3 = FUENTES / "t3"
T3.mkdir(exist_ok=True)

PAISES = "ES PT FR IT DE AT CH GB IE NL BE LU SE NO DK FI IS PL CZ SK HU RO BG GR HR SI RS BA ME MK AL CY MT EE LV LT UA AD".split()
ESPEJOS = ["https://overpass-api.de/api/interpreter", "https://overpass.private.coffee/api/interpreter",
           "https://overpass.kumi.systems/api/interpreter"]

def overpass(nombre, consulta):
    ruta = T3 / f"{nombre}.json"
    if ruta.exists(): return
    for intento in range(6):
        try:
            pide = urllib.request.Request(ESPEJOS[intento % len(ESPEJOS)], data=urllib.parse.urlencode({"data": consulta}).encode(), headers=UA)
            datos = urllib.request.urlopen(pide, timeout=200).read()
            n = len(json.loads(datos)["elements"])
            ruta.write_bytes(datos); print(nombre, n, flush=True); time.sleep(4); return
        except Exception as e:
            print(nombre, "reintento", e, flush=True); time.sleep(10 * (intento + 1))
    print(nombre, "SIN DATOS", flush=True)

def osm():
    for p in PAISES:
        overpass(f"osm_{p.lower()}", f'[out:json][timeout:180];area["ISO3166-1"="{p}"][admin_level=2]->.a;'
                                     'nwr["amenity"="nightclub"]["name"](area.a);out tags center;')
    overpass("osm_es_cerradas", '[out:json][timeout:180];area["ISO3166-1"="ES"][admin_level=2]->.a;('
             + "".join(f'nwr["{pre}:amenity"="nightclub"]["name"](area.a);' for pre in ("disused", "was", "abandoned", "demolished", "razed"))
             + ");out tags center;")

def xceed():
    ruta = T3 / "xceed_clubs.json"
    if ruta.exists(): return
    todos, desde = {}, 0
    while True:
        u = f"https://events.xceed.me/v1/clubs?limit=200&offset={desde}"
        tanda = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=40))["data"]
        if not tanda: break
        for c in tanda:   # solo lo que usa tanda2.py; el resto son direcciones de fotos
            ciudad = c.get("city") or {}
            todos[c["id"]] = {"name": c["name"], "types": c["types"],
                              "city": {"name": ciudad.get("name", ""), "country": {"isoCode": (ciudad.get("country") or {}).get("isoCode")}}}
        desde += len(tanda); time.sleep(0.3)
    ruta.write_text(json.dumps(list(todos.values()), ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("xceed", len(todos))

if __name__ == "__main__":
    xceed(); osm()
