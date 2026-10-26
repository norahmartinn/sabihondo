"""«Nombra un artista hombre con más de 500.000 oyentes mensuales en Spotify» (quinta tanda). Igual que artistas_spotify.py:

1. Wikidata (por QLever): personas con sexo «hombre» u «hombre trans» y grupos de chicos (boy bands) con identificador de artista
   de Spotify (P1902) y al menos una página en alguna Wikipedia → datos/siete/fuentes/t5/hombres_wd.tsv
2. Los oyentes mensuales de cada uno, de la descripción de su página de Spotify → datos/siete/fuentes/t5/hombres_oyentes.jsonl
   (de más a menos páginas de Wikipedia; se puede relanzar y sigue donde iba).
3. Entran los que pasan de 500.000. Nivel por oyentes, salvo los conocidos en España, que van a mano (1 y 2).

Uso:  python3 scripts/siete/artistas_hombres.py baja     (pasos 1 y 2)
      python3 scripts/siete/artistas_hombres.py          (paso 3)"""
import sys, html
from comun import *
import artistas_spotify as A
D5 = FUENTES / "t5"; D5.mkdir(exist_ok=True)
A.WD, A.OY = D5 / "hombres_wd.tsv", D5 / "hombres_oyentes.jsonl"
A.CONSULTA = """PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
SELECT ?a ?sp (SAMPLE(?l) AS ?lab) (SAMPLE(?le) AS ?labes) (SAMPLE(?n) AS ?links) (SAMPLE(?tipo) AS ?t) WHERE {
  { ?a wdt:P21 ?g . VALUES ?g { wd:Q6581097 wd:Q2449503 } BIND("p" AS ?tipo) }
  UNION { ?a wdt:P31 wd:Q216337 . BIND("g" AS ?tipo) }
  UNION { ?a wdt:P136 wd:Q216337 . BIND("g" AS ?tipo) }
  ?a wdt:P1902 ?sp ; wikibase:sitelinks ?n . FILTER(?n >= 1)
  OPTIONAL { ?a rdfs:label ?l FILTER(LANG(?l)="en") }
  OPTIONAL { ?a rdfs:label ?le FILTER(LANG(?le)="es") }
} GROUP BY ?a ?sp"""

# Los conocidos en España: nivel 1 y 2 (solo cuentan si pasan el corte)
A.N1 = """Bad Bunny, Quevedo, Ed Sheeran, Justin Bieber, Michael Jackson, Bruno Mars, The Weeknd, Drake, Eminem, Alejandro Sanz, Enrique Iglesias,
David Bisbal, Pablo Alborán, Melendi, Daddy Yankee, J Balvin, Ozuna, Rauw Alejandro, Feid, Myke Towers, Anuel AA, Maluma, Sebastián Yatra|Sebastian Yatra,
Harry Styles, Elvis Presley, Freddie Mercury, C. Tangana, Rels B, Morad, Duki, Bizarrap, Peso Pluma, Romeo Santos, Juanes, Ricky Martin, Luis Fonsi,
Manuel Turizo, Dani Martín, Estopa, Pitbull, Nicky Jam, Don Omar, Wisin & Yandel, Travis Scott, Kanye West|Ye, Post Malone, Shawn Mendes"""
A.N2 = """Calvin Harris, David Guetta, Martin Garrix, Avicii, Tiësto|Tiesto, Kygo, Bob Marley, Frank Sinatra, John Lennon, Paul McCartney, Elton John,
David Bowie, Prince, Stevie Wonder, Lionel Richie, Phil Collins, Sting, Bon Jovi, Bruce Springsteen, Lenny Kravitz, Robbie Williams, George Michael,
Julio Iglesias, Raphael, Camilo Sesto, Joaquín Sabina, Joan Manuel Serrat, Manolo García, Antonio Orozco, Manuel Carrasco, Pablo López,
Álvaro Soler, Antonio José, Abraham Mateo, Beret, Funambulista, Marc Anthony, Chayanne, Luis Miguel, Juan Luis Guerra, Carlos Vives, Prince Royce,
Arcángel|Arcangel, Farruko, Jhayco|Jhay Cortez, Sech, Lunay, Mora, Eladio Carrión, Ryan Castro, Blessd, Saiko, Omar Montes, Delaossa,
Recycled J, Hoke, Kidd Keo, Yung Beef, Cruz Cafuné, Trueno, Paulo Londra, Tiago PZK, Khea, Milo J,
Bizarrap, Kendrick Lamar, J. Cole, Lil Wayne, Snoop Dogg, 50 Cent, Jay-Z, Kid Cudi, Future, Lil Baby, Tyler The Creator|Tyler the Creator,
Frank Ocean, Chris Brown, Usher, Ne-Yo, Akon, Sean Paul, Shaggy, Jason Derulo, Justin Timberlake, Charlie Puth, Lewis Capaldi,
Benson Boone, Teddy Swims, Hozier, Tom Odell, James Arthur, James Blunt, George Ezra, Jamie Cullum, Michael Bublé, Andrea Bocelli, Eros Ramazzotti,
Tiziano Ferro, Zucchero, Stromae, Maître Gims|GIMS, Ozuna, Lil Nas X, Khalid, Zayn, Niall Horan, Louis Tomlinson, Liam Payne, Jungkook|Jung Kook,
Jimin, V, Suga|Agust D, RM, Jin, j-hope, BTS, One Direction, Backstreet Boys, *NSYNC|NSYNC, Westlife, Take That, Jonas Brothers, Morat, Café Quijano,
Andy & Lucas, Taburete, Dvicio, Auryn, Gemeliers, Marc Seguí, Walls, Lucho RK, Bejo, Nil Moliner, Leiva, Iván Ferreiro, Fito Cabrales,
Robe, Rosendo, Bunbury|Enrique Bunbury, Manu Chao, Kase.O|Kase O, Nach, Rayden, Alfred García, Miki Núñez, Bertín Osborne,
Camarón|Camarón de la Isla, Paco de Lucía, Diego El Cigala, Kiko Rivera, Georgie Dann, Jordi Cruz no"""
A.NO_ENTRAN = set()
_monta = A.monta
def monta():
    # mismo montaje, otro archivo
    viejo = A.guarda
    A.guarda = lambda slug, filas, met: viejo("artistas_hombres", filas, met)
    try: _monta()
    finally: A.guarda = viejo

if __name__ == "__main__":
    A.html = html
    A.baja() if sys.argv[1:] == ["baja"] else monta()
