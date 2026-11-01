"""«Nombra una de las 250 series mejor puntuadas en IMDb» (tanda 6).
Lista de Norah (el top 250 de IMDb en español, nov 2026). Los títulos repetidos (La víbora negra, Dragon Ball Z, Dragon Ball,
Twin Peaks, The Office) van una vez. Niveles a mano pensando en alguien de España; alias con el título original.
    python3 series_imdb.py   → datos/siete/series_imdb.csv"""
import csv
from pathlib import Path
from comun import clave

SALIDA = Path(__file__).resolve().parents[2] / "datos/siete/series_imdb.csv"
S = """1|Breaking Bad|
1|Juego de tronos|Game of Thrones|GOT
1|Friends|
1|Los Simpson|The Simpsons|Simpsons
1|The Office|La oficina
1|Stranger Things|
1|Peaky Blinders|
1|Black Mirror|
1|Narcos|
1|House|House M.D.|Doctor House|Dr. House
1|Dexter|
1|Sherlock|
1|Chernobyl|Chernóbil
1|Rick y Morty|Rick and Morty
1|Dragon Ball|Bola de Dragón
1|Dragon Ball Z|Bola de Dragón Z
1|South Park|
1|Mr. Bean|Mister Bean
1|The Boys|
1|Better Call Saul|
2|Los Soprano|The Sopranos|Los Sopranos
2|The Wire (Bajo escucha)|The Wire|Bajo escucha
2|Avatar. La leyenda de Aang|Avatar|La leyenda de Aang|Avatar: The Last Airbender
2|Ataque a los titanes|Attack on Titan|Shingeki no Kyojin
2|Death Note|
2|One Piece|
2|Naruto: Shippûden|Naruto Shippuden|Naruto
2|Dark|
2|Gambito de dama|The Queen's Gambit|Gambito de reina
2|The Crown|
2|House of Cards|
2|The Mandalorian|Mandalorian
2|Fargo|
2|True Detective|
2|Hora de aventuras|Adventure Time
2|Gravity Falls|
2|Bluey|
2|Seinfeld|
2|Twin Peaks|
2|Expediente X|The X-Files|X-Files|Expedientes X
2|Mad Men|
2|Downton Abbey|
2|Ted Lasso|
2|Succession|
2|Mindhunter|
2|Hijos de la anarquía|Sons of Anarchy
2|Yellowstone|
2|Mr. Robot|
2|Arcane|
2|La maldición de Hill House|The Haunting of Hill House|Hill House
2|Los informáticos|The IT Crowd|IT Crowd
2|Guardianes de la noche: Kimetsu no Yaiba|Kimetsu no Yaiba|Demon Slayer|Guardianes de la noche
2|Jujutsu Kaisen|
2|One Punch Man|
2|Daredevil|
2|Lo que hacemos en las sombras|What We Do in the Shadows
2|El Chavo del Ocho|El Chavo del 8|El Chavo
2|Planeta Tierra|Planet Earth
2|Bugs Bunny|
2|Dexter: Resurrección|Dexter Resurrection
2|Separación|Severance
2|El Pingüino|The Penguin
2|Shōgun|Shogun
2|Andor|
2|Invincible|Invencible
2|BoJack Horseman|Bojack
2|Hermanos de sangre|Band of Brothers
2|Top Gear|
2|Parks and Recreation|Parks and Rec
2|Hunter X Hunter|
2|Batman: La serie animada|Batman: The Animated Series
2|Neon Genesis Evangelion|Evangelion
2|Fleabag|
2|Cosmos|
3|Firefly|
3|Fullmetal Alchemist: Brotherhood|Fullmetal Alchemist
3|El último baile|The Last Dance
3|La dimensión desconocida|The Twilight Zone|Twilight Zone
3|Cowboy Bebop|
3|La granja de Clarkson|Clarkson's Farm
3|The Grand Tour|
3|Planeta azul|Blue Planet
3|Nuestro planeta|Our Planet
3|Planeta Tierra II|Planet Earth II
3|Planeta azul II|Blue Planet II
3|Colgados en Filadelfia|It's Always Sunny in Philadelphia
3|Larry David (Curb Your Enthusiasm)|Larry David|Curb Your Enthusiasm|Curb
3|Monty Python's Flying Circus|Monty Python
3|Instituto McKinley|Freaks and Geeks
3|Orgullo y prejuicio|Pride and Prejudice
3|Roma|Rome
3|Oz|
3|The Shield: Al margen de la ley|The Shield
3|Galáctica, estrella de combate|Galáctica
3|Star Trek: La nueva generación|Star Trek: The Next Generation|Star Trek
3|Arrested Development|
3|This Is Us|
3|La maravillosa Sra. Maisel|The Marvelous Mrs. Maisel|Mrs. Maisel
3|El ala oeste de la Casa Blanca|The West Wing|El ala oeste
3|A dos metros bajo tierra|Six Feet Under
3|Boardwalk Empire|
3|Deadwood|
3|The Newsroom|
3|Archer|
3|Justified: La ley de Raylan|Justified
3|The Expanse|
3|Schitt's Creek|
3|Making a Murderer|
3|The Jinx (El gafe)|The Jinx|El gafe
3|Atlanta|
3|X-Men '97|X-Men 97
3|Samurai Jack|
3|La Liga de la Justicia|Justice League
3|La joven Liga de la Justicia|Young Justice
3|Historias corrientes|Regular Show
3|Bleach: Thousand Year Blood War|Bleach
3|Vinland Saga|
3|Berserk|
3|Steins;Gate|Steins Gate
3|Code Geass: Lelouch of the Rebellion|Code Geass
3|Frieren: Beyond Journey's End|Frieren
3|Haikyu!! Los ases del vóley|Haikyu
3|Mob Psycho 100|Mob Psycho
3|Samurai Champloo|
3|JoJo's Bizarre Adventure|JoJo
3|Así nos ven|When They See Us
3|Dopesick: Historia de una adicción|Dopesick
3|1883|
3|El caballero de los Siete Reinos|A Knight of the Seven Kingdoms
3|The Pitt|
3|Más que rivales|Heated Rivalry
3|Gomorra|Gomorrah
3|La amiga estupenda|L'amica geniale|My Brilliant Friend
3|El submarino|Das Boot
3|Poirot|
3|Hotel Fawlty|Fawlty Towers
3|La víbora negra|Blackadder
3|Line of Duty|
3|Bron (El puente)|Bron|El puente|The Bridge|Broen
3|Derry Girls|
3|Crash Landing on You|Aterrizaje de emergencia en tu corazón
3|Last Week Tonight with John Oliver|Last Week Tonight|John Oliver
3|Chappelle's Show|
3|Louie|
3|The Chosen (Los elegidos)|The Chosen|Los elegidos
3|Anne with an E|Anne con E|Anne
3|Hermanos de sangre (2001)|
4|Más allá del jardín|Over the Garden Wall
4|Primal|
4|Scavengers Reign|
4|Samurái de ojos azules|Blue Eye Samurai
4|Peep Show|
4|Still Game|
4|Only Fools and Horses|
4|Taskmaster|
4|Nathan al rescate|Nathan for You
4|Los ensayos|The Rehearsal
4|How to with John Wilson|
4|Padre Ted|Father Ted
4|The Thick of It|
4|Sí, ministro|Yes Minister
4|Sí, primer ministro|Yes Prime Minister
4|Spaced|
4|Coupling|
4|I'm Alan Partridge|Alan Partridge
4|Brass Eye|
4|Detectorists|
4|Happy Valley|
4|Endeavour|
4|Las aventuras de Sherlock Holmes|The Adventures of Sherlock Holmes
4|El regreso de Sherlock Holmes|The Return of Sherlock Holmes
4|Yo, Claudio|I, Claudius
4|El decálogo|Dekalog
4|Paloma Solitaria|Lonesome Dove
4|It's a Sin|
4|Pose|
4|La oferta|The Offer
4|Homicidio|Homicide: Life on the Street
4|Friday Night Lights|
4|Oficina de infiltrados|Le Bureau des légendes|The Bureau
4|Mr. Inbetween|
4|Trailer Park Boys|
4|Whose Line Is It Anyway?|Whose Line
4|Agárralos como puedas|Impractical Jokers
4|QI|
4|The Great British Baking Show|The Great British Bake Off|Bake Off
4|Misterio en el espacio|Mystery Science Theater 3000|MST3K
4|Los hermanos Venture|The Venture Bros
4|Los Conchords|Flight of the Conchords
4|The Boondocks|
4|The Eric Andre Show|
4|Smiling Friends|
4|Justice League Unlimited|Liga de la Justicia Ilimitada
4|Battlestar Galactica|
4|Critical Role|
4|Todas las criaturas grandes y pequeñas|All Creatures Great and Small
4|El mundo en moto con Ewan McGregor|Long Way Round|El mundo en moto
4|Secretos del universo con Morgan Freeman|Through the Wormhole
4|Mind Your Language|
4|El vecindario del Sr. Rogers|Mister Rogers' Neighborhood
4|Monster|
4|Gintama|
4|Your Lie in April|Shigatsu wa Kimi no Uso
4|Los diarios de la boticaria|The Apothecary Diaries|Kusuriya no Hitorigoto
4|Steel Ball Run: JoJo's Bizarre Adventure|Steel Ball Run
4|Takopi's Original Sin|
4|Espíritu de lucha|Hajime no Ippo
4|Si la vida te da mandarinas...|When Life Gives You Tangerines
4|Alquimia de Almas|Alchemy of Souls
4|Planeta helado|Frozen Planet
4|Planeta humano|Human Planet
4|Life|
4|África|Africa
4|Cosmos: Una odisea en el espacio-tiempo|Cosmos: A Spacetime Odyssey
4|El mundo en guerra|The World at War
4|La guerra de Vietnam|The Vietnam War
4|The Civil War|
4|The Beatles Anthology|
4|The Beatles: Get Back|Get Back
4|Apocalipsis - La segunda guerra mundial|Apocalipsis|Apocalypse
4|II Guerra Mundial: Momentos clave|
5|Scam 1992: The Harshad Mehta Story|Scam 1992
5|TVF Pitchers|Pitchers
5|Panchayat|
5|Gullak|
5|La fábrica de Kota|Kota Factory
5|Aspirants|
5|Sapne Vs Everyone|
5|Sarabhai vs Sarabhai|
5|Yeh Meri Family|
5|Rocket Boys|
5|The Family Man|
5|Mahabharat|Mahabharata
5|Ramayan|Ramayana
5|Sahsiyet|Şahsiyet|Persona
5|Leyla and Mecnun|Leyla ile Mecnun
5|Behzat Ç.: An Ankara Policeman|Behzat Ç.
5|Ezel|
5|Avrupa Yakasi|Avrupa Yakası
5|Como si...|
5|Sol negro|
5|Farouk Omar|Omar
5|Eung-dab-ha-ra 1988|Reply 1988
5|Mi señor|My Mister
5|Sparkling Watermelon|"""
filas = [l.split("|") for l in S.splitlines()]
filas = [f for f in filas if f[1] != "Hermanos de sangre (2001)"]
vistos = set()
with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";"); w.writerow(["respuesta", "alias", "nivel", "orden_a_mano"])
    for orden, (nv, n, *al) in enumerate(filas):
        assert clave(n) not in vistos, n
        al = [a for a in al if a and clave(a) not in vistos and clave(a) != clave(n)]
        vistos.add(clave(n)); vistos.update(clave(a) for a in al)
        w.writerow([n, "|".join(al), nv, 10**9 - orden])
print(SALIDA.name, len(filas), "series")
