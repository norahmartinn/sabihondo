"""«Nombra a alguien con más de 10 millones de seguidores en Instagram» (tanda 6).
La lista y los niveles son de Norah (datos/siete/fuentes/t6/instagram_10m.txt); aquí solo se añaden alias:
las formas populares (ALIAS) y el apellido a secas cuando no lo comparte nadie más de la lista.
    python3 instagram.py   → datos/siete/instagram_10m.csv"""
import csv, re
from pathlib import Path
from comun import clave

RAIZ = Path(__file__).resolve().parents[2]
FUENTE = RAIZ / "datos/siete/fuentes/t6/instagram_10m.txt"
SALIDA = RAIZ / "datos/siete/instagram_10m.csv"
SIN_PAREN = lambda t: re.sub(r"\s*\(.*?\)", "", t).strip()
ALIAS = {
  "Cristiano Ronaldo": "CR7|Cristiano", "Lionel Messi": "Messi|Leo Messi", "MrBeast": "Mr Beast|Jimmy Donaldson",
  "Kim Kardashian": "Kim K", "Dwayne Johnson": "The Rock|La Roca", "Justin Bieber": "Bieber", "Neymar": "Neymar Jr|Neymar Júnior",
  "Vinícius Júnior": "Vini Jr|Vinicius|Vini", "Jennifer Lopez": "JLo|J Lo|Jennifer López", "P!nk": "Pink", "El Rubius": "Rubius|Rubén Doblas",
  "AuronPlay": "Auron|Auronplay", "Ibai Llanos": "Ibai", "Lamine Yamal": "Lamine", "Kylian Mbappé": "Mbappé", "Erling Haaland": "Haaland",
  "Ronaldo Nazário": "Ronaldo|el Fenómeno|Ronaldo Nazario", "Ronaldinho": "Ronaldinho Gaúcho", "Charli D'Amelio": "Charli DAmelio|Charli",
  "The Weeknd": "Weeknd", "Tyler, the Creator": "Tyler the Creator", "Robert Downey Jr.": "Robert Downey|RDJ", "Rosalía": "La Rosalía",
  "Shah Rukh Khan": "SRK", "Georgina Rodríguez": "Georgina", "Antonela Roccuzzo": "Antonela", "Bizarrap": "Bzrp|Biza",
  "Karol G": "Karol", "J Balvin": "Balvin", "Bad Bunny": "Benito", "Michael Jackson": "Jacko", "Pelé": "Pele", "Xavi": "Xavi Hernández",
  "Isco": "Isco Alarcón", "Gavi": "Pablo Gavi", "Pedri": "Pedri González", "Nacho Fernández": "Nacho", "Sergio Ramos": "Ramos",
  "Rafael Nadal": "Nadal|Rafa Nadal", "Carlos Sainz": "Sainz", "Álvaro Morata": "Morata", "Úrsula Corberó": "Corberó|Tokio",
  "Ester Expósito": "Ester Exposito", "Pilar Rubio": "Pilar", "Ilia Topuria": "Topuria", "Jennie": "Jennie Kim", "Lisa": "Lalisa",
  "Jungkook": "Jeon Jungkook", "V (BTS)": "Taehyung|Kim Taehyung", "Sean Combs": "P Diddy|Diddy|Puff Daddy", "Tupac Shakur": "2Pac|Tupac",
  "XXXTentacion": "XXX Tentacion", "6ix9ine": "Tekashi|Tekashi 6ix9ine|Sixnine", "Selena Gomez": "Selena", "Taylor Swift": "Taylor",
  "Ariana Grande": "Ariana", "Kylie Jenner": "Kylie", "Billie Eilish": "Billie", "Dua Lipa": "Dua", "Will Smith": "Willy Smith",
  "Zinedine Zidane": "Zidane|Zizou", "Zlatan Ibrahimović": "Zlatan|Ibrahimovic", "Iker Casillas": "Casillas", "Andrés Iniesta": "Iniesta",
  "Gerard Piqué": "Piqué", "Fernando Torres": "Torres|el Niño Torres", "Dani Carvajal": "Carvajal", "Luka Modrić": "Modric",
  "Toni Kroos": "Kroos", "Thibaut Courtois": "Courtois", "Karim Benzema": "Benzema", "Antoine Griezmann": "Griezmann",
  "Leonardo DiCaprio": "DiCaprio|Di Caprio", "Ana de Armas": "Ana de Armas", "Canelo Álvarez": "Canelo", "Conor McGregor": "McGregor",
  "Barack Obama": "Obama", "Donald Trump": "Trump", "Kim Soo-hyun": "Kim Soo Hyun", "Lee Min-ho": "Lee Min Ho", "Cha Eun-woo": "Cha Eun Woo", "Song Hye-kyo": "Song Hye Kyo",
}
nivel, filas, vistos = None, [], set()
for linea in FUENTE.read_text(encoding="utf-8").splitlines():
    linea = linea.strip()
    if not linea or linea.startswith("#"): continue
    if linea.startswith("["): nivel = int(linea[1:-1]); continue
    nombre, *otros = linea.split("=")
    al = otros + ([SIN_PAREN(nombre)] if "(" in nombre else []) + [a for a in ALIAS.get(nombre, "").split("|") if a]
    if "(" in nombre: al.append(re.sub(r"[()]", " ", nombre))
    filas.append([nombre, al, nivel])
# el apellido a secas, si es largo y nadie más de la lista lleva esa palabra
palabras = {}
for nombre, al, _ in filas:
    for p in set(clave(w) for w in SIN_PAREN(nombre).split()): palabras[p] = palabras.get(p, 0) + 1
for f in filas:
    partes = SIN_PAREN(f[0]).split()
    if len(partes) >= 2 and len(clave(partes[-1])) >= 5 and palabras.get(clave(partes[-1])) == 1: f[1].append(partes[-1])
with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";"); w.writerow(["respuesta", "alias", "nivel", "orden_a_mano"])
    orden = 10**9
    for nombre, al, nv in filas:
        k = clave(nombre)
        if k in vistos: continue
        al = [a for a in dict.fromkeys(al) if clave(a) and clave(a) not in vistos and clave(a) != k]
        vistos.add(k); vistos.update(clave(a) for a in al)
        w.writerow([nombre, "|".join(al), nv, orden]); orden -= 1
print(SALIDA.name, len(vistos), "claves")
