"""«Nombra una artista con más de 500.000 oyentes mensuales en Spotify» (cuarta tanda).

1. Wikidata (por QLever): todas las personas con sexo «mujer», «mujer trans», «género fluido» o «no binario» (Miley Cyrus, Demi Lovato) y todos los grupos de chicas
   que tienen identificador de artista de Spotify (P1902) → datos/siete/fuentes/t4/artistas_wd.tsv
2. Los oyentes mensuales de cada una, leídos de la descripción de su página de Spotify («Artist · 26.1M monthly listeners.»)
   → datos/siete/fuentes/t4/artistas_oyentes.jsonl. Spotify corta si se le pide mucho: 3 a la vez y, si da 429, se espera.
3. Entran las que pasan de 500.000. El nivel lo dan los oyentes, salvo las conocidas en España, que van a mano (1 y 2),
   y solo si de verdad pasan el corte.

Uso:  python3 scripts/siete/artistas_spotify.py baja     (pasos 1 y 2; se puede relanzar)
      python3 scripts/siete/artistas_spotify.py          (paso 3)"""
import sys
from comun import *
D4 = FUENTES / "t4"
WD, OY = D4 / "artistas_wd.tsv", D4 / "artistas_oyentes.jsonl"
CORTE = 500_000

CONSULTA = """PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
SELECT ?a ?sp (SAMPLE(?l) AS ?lab) (SAMPLE(?le) AS ?labes) (SAMPLE(?n) AS ?links) (SAMPLE(?tipo) AS ?t) WHERE {
  { ?a wdt:P21 ?g . VALUES ?g { wd:Q6581072 wd:Q1052281 wd:Q18116794 wd:Q48270 } BIND("p" AS ?tipo) }
  UNION { ?a wdt:P31 wd:Q641066 . BIND("g" AS ?tipo) }
  UNION { ?a wdt:P136 wd:Q641066 . BIND("g" AS ?tipo) }
  ?a wdt:P1902 ?sp .
  OPTIONAL { ?a rdfs:label ?l FILTER(LANG(?l)="en") }
  OPTIONAL { ?a rdfs:label ?le FILTER(LANG(?le)="es") }
  OPTIONAL { ?a wikibase:sitelinks ?n }
} GROUP BY ?a ?sp"""

def baja():
    if not WD.exists():
        r = urllib.request.Request("https://qlever.dev/api/wikidata", data=urllib.parse.urlencode({"query": CONSULTA}).encode(),
                                   headers={**UA, "Accept": "text/tab-separated-values"})
        WD.write_bytes(urllib.request.urlopen(r, timeout=300).read())
    links = {}
    for l in open(WD, encoding="utf-8"):
        if l.startswith("?"): continue
        c = l.rstrip("\n").split("\t"); i = c[1].strip('"')
        links[i] = max(links.get(i, 0), int(c[4] or 0))
    hechos = {json.loads(l)["id"] for l in open(OY, encoding="utf-8")} if OY.exists() else set()
    pend = [i for i in sorted(links, key=lambda i: -links[i]) if i not in hechos]
    print(len(links), "artistas,", len(pend), "pendientes")
    def num(s):
        m = re.match(r"([\d.,]+)([KMB]?)", s)
        return int(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])
    def una(i):
        for intento in range(12):
            try:
                r = urllib.request.Request("https://open.spotify.com/artist/" + i, headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"})
                h = urllib.request.urlopen(r, timeout=30).read().decode("utf8", "ignore")
                m = re.search(r'<meta name="description" content="Listen to (.*?) on Spotify\. Artist · ([^ ]+) monthly listener', h)
                if m: return {"id": i, "nombre": html.unescape(m.group(1)), "oyentes": num(m.group(2))}
                m = re.search(r'<meta name="description" content="Listen to (.*?) on Spotify', h)
                return {"id": i, "nombre": html.unescape(m.group(1)) if m else None, "oyentes": 0}
            except urllib.error.HTTPError as e:
                if e.code == 404: return {"id": i, "nombre": None, "oyentes": -1}
                time.sleep(90 if e.code == 429 else 5)
            except Exception:
                time.sleep(5)
    with open(OY, "a", encoding="utf-8") as f, cf.ThreadPoolExecutor(3) as ex:
        for d in ex.map(una, pend):
            if d: f.write(json.dumps(d, ensure_ascii=False) + "\n"); f.flush()

# Las conocidas en España: nivel 1 y 2 (solo cuentan si pasan el corte)
N1 = """Rosalía|ROSALÍA, Aitana, Taylor Swift, Shakira, Beyoncé, Rihanna, Lady Gaga, Dua Lipa, Billie Eilish, Ariana Grande, KAROL G|Karol G,
Sabrina Carpenter, Adele, Lola Indigo|Lola Índigo, Miley Cyrus, Katy Perry, Bad Gyal, Olivia Rodrigo, Becky G, Selena Gomez, Madonna, Britney Spears"""
N2 = """Nicki Minaj, Doja Cat, SZA, Lana Del Rey, Sia, Ana Mena, Natalia Lafourcade, Mon Laferte, Nathy Peluso, Emilia, TINI|Tini, María Becerra|Maria Becerra,
Young Miko, Cazzu, Nicki Nicole, Isabel Pantoja, Mónica Naranjo, Malú, Vanesa Martín, India Martinez|India Martínez, Amaia, Chanel, Belén Aguilera, Ptazeta,
La Zowi, Bb trickz, Bebe, Natalia Jiménez, Paulina Rubio, Thalía|Thalia, Gloria Trevi, Anitta, Camila Cabello, Jennifer Lopez|Jennifer López, Christina Aguilera,
Céline Dion|Celine Dion, Whitney Houston, Mariah Carey, Alicia Keys, Amy Winehouse, Tate McRae, Chappell Roan, Gracie Abrams, Lorde, Halsey, Ava Max,
Bebe Rexha, Zara Larsson, Rita Ora, Jessie J, Ellie Goulding, Avril Lavigne, P!nk|Pink, Kesha, Demi Lovato, Charli xcx|Charli XCX, Doechii, Cardi B,
Megan Thee Stallion, Ice Spice, RAYE|Raye, Rocío Jurado, Rocío Dúrcal, Lola Flores, Ana Torroja, Ana Belén, Rozalén, Edurne, Melody, Ruth Lorenzo, Pastora Soler,
Rosa López, Soraya, Blanca Paloma, Sofía Reyes, Danna Paola|Danna, Kali Uchis, Cher, Tina Turner, Amaral, La Oreja de Van Gogh, BLACKPINK, Little Mix,
Fifth Harmony, Spice Girls, Las Ketchup, Ha*Ash, Marina, Natti Natasha, Ivy Queen, Jhené Aiko, Normani, Kylie Minogue, Gwen Stefani, Fergie, Nelly Furtado,
Lily Allen, Florence + The Machine, Norah Jones, Shania Twain, Dolly Parton, Lizzo, Meghan Trainor, Ellie Goulding, Clara Luciani, Aya Nakamura, Angèle, Zaz,
Laura Pausini, Elodie, Annalisa, Giorgia, ANNA, Natalia Oreiro, Lali, Rocío Quiroz, Emilia Mernes, Nathy Peluso, Ángela Aguilar, Paloma Mami, Mon Laferte,
Jenni Rivera, Selena, Celia Cruz, La India, Gloria Estefan, Shakira, Sophie Ellis-Bextor, Jessie Ware, Mabel, Anne-Marie, Tones And I, Birdy, Jess Glynne,
Pixie Lott, Leona Lewis, Duffy, Alessia Cara, Ashnikko, Ava Max, Marshmello? """
def lista(t): return [[x.strip() for x in n.split("|")] for n in t.replace("\n", " ").split(",") if n.strip() and "?" not in n]

def monta():
    etiquetas = {}
    for l in open(WD, encoding="utf-8"):
        if l.startswith("?"): continue
        c = l.rstrip("\n").split("\t"); i = c[1].strip('"')
        for x in c[2:4]:
            m = re.match(r'"(.*)"@\w+', x)
            if m: etiquetas.setdefault(i, set()).add(m.group(1))
    datos = {}
    for l in open(OY, encoding="utf-8"):
        d = json.loads(l)
        if d["nombre"] and clave(d["nombre"]) not in NO_ENTRAN and d["oyentes"] >= CORTE and d["oyentes"] > datos.get(clave(d["nombre"]), {}).get("oyentes", 0):
            datos[clave(d["nombre"])] = d
    n1 = {clave(a): 1 for g in lista(N1) for a in g}
    n2 = {clave(a): 2 for g in lista(N2) for a in g}
    filas = []
    for k, d in datos.items():
        alias = sorted(x for x in etiquetas.get(d["id"], ()) if clave(x) != k and LATIN(x) and clave(x) not in ALIAS_MALOS)
        nv = n1.get(k) or n2.get(k) or next((n1.get(clave(a)) or n2.get(clave(a)) for a in alias if clave(a) in n1 or clave(a) in n2), None)
        if not nv:
            o = d["oyentes"]
            nv = 2 if o >= 40e6 else 3 if o >= 12e6 else 4 if o >= 3e6 else 5
        filas.append((d["nombre"], alias, nv, d["oyentes"]))
    fuera = [g[0] for g in lista(N1) + lista(N2) if not any(clave(a) in datos for a in g)]
    print("  a mano pero sin datos o por debajo del corte (no entran):", fuera)
    guarda("artistas", filas, "oyentes_mensuales_spotify")
# Wikidata marca como «no binario» o «género fluido» a gente que no se presenta como mujer: fuera
NO_ENTRAN = {clave(x) for x in """Sam Smith, Lil Uzi Vert, Olly Alexander (Years & Years), Richard O'Brien, felix jaehn, Pabllo Vittar, Gloria Groove,
Alex Newell, Yves Tumor, Ricky Montgomery, Christine and the Queens, August Ponthier, Yaelokre, quannnic, Ghost and Pals, Lucy Bedroque, Nxdia""".replace("\n", " ").split(",")}
ALIAS_MALOS = {clave("TheGrefg"), clave("bon")}      # etiquetas de Wikidata que no son de esa artista
LATIN = lambda t: not re.search(r"[^\x00-ɏ’'·!&+*.]", t)

if __name__ == "__main__":
    import html
    baja() if sys.argv[1:] == ["baja"] else monta()
