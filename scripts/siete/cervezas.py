"""Marcas de cerveza.
Lista: marcas y cerveceras de Wikidata (unas 4.000) más las que se ven en un bar o un súper de España.
Nivel: las conocidas en España están ordenadas a mano (no hay un dato público de fama de marca aquí);
el resto, por el número de ediciones de Wikipedia que tienen artículo sobre la marca."""
from comun import *

# respuesta: alias. Nivel 1 = lo que hay en cualquier bar de España.
MANO = {
1: """Mahou: Mahou Cinco Estrellas|Mahou Clásica|Mahou 5 Estrellas
Estrella Galicia: La Estrella Galicia
Cruzcampo: Cruz Campo
San Miguel: San Miguel Especial
Heineken
Estrella Damm: Damm|Estrella|Estrella Dorada
Amstel
Alhambra: Alhambra 1925|Alhambra Reserva 1925|1925
Corona: Coronita|Corona Extra
El Águila: Águila|Aguila""",
2: """Ámbar: Ambar Especial
Voll-Damm: Voll Damm|Volldamm
1906: 1906 Reserva Especial|Milnueve
Budweiser: Bud
Guinness
Carlsberg
Paulaner
Desperados
Moritz
Victoria: Cerveza Victoria|Victoria Málaga
Turia: Turia Märzen
Estrella de Levante: Estrella Levante
Keler
La Salve: La Salve Bilbao
Dorada
Tropical
Franziskaner
Stella Artois: Stella
Peroni: Nastro Azzurro|Peroni Nastro Azzurro
Modelo: Modelo Especial|Negra Modelo
Sol
Buckler
Free Damm
Xibeca
Coors: Coors Light
Beck's: Becks
Leffe
Judas
Duvel
Grimbergen
Foster's: Fosters
Mixta: Mahou Mixta
Shandy: Shandy Cruzcampo
Steinburg
Bavaria
Radler: Cruzcampo Radler|Amstel Radler
Inedit: Inedit Damm
San Miguel 0,0: San Miguel 00
Laiker
Skol""",
3: """Chimay
Affligem
Tsingtao
Asahi
Sapporo
Kirin
Pacífico
Quilmes
Brahma
Polar
Cusqueña
Presidente
Grolsch
Warsteiner
Erdinger
Pilsner Urquell: Pilsner
Kozel
Staropramen
Budvar: Budweiser Budvar
Tyskie
Mythos
Efes
Singha
Chang
Tiger
Sagres
Super Bock: Superbock
Kronenbourg: 1664|Kronenbourg 1664
Delirium Tremens: Delirium
La Chouffe: Chouffe
Kwak: Pauwel Kwak
Hoegaarden
Lagunitas
BrewDog: Punk IPA
Mort Subite
Reina
Estrella del Sur
Aurum
Karlsquell
Argus
Perlenbacher
Ramblers
Holsten
Oettinger
Bitburger
Krombacher
Spaten
Löwenbräu: Lowenbrau
Hofbräu: HB|Hofbrauhaus
Augustiner
Weihenstephaner: Weihenstephan
Miller: Miller Genuine Draft|Miller Lite
Bud Light
Dos Equis: XX
Tecate
Birra Moretti: Moretti
La Virgen: Cervezas La Virgen
La Cibeles: Cibeles
Arriaca
La Sagra
Alcázar: El Alcázar
Mezquita: Alhambra Mezquita
Bock-Damm: Bock Damm
Damm Lemon
Epidor: Moritz Epidor
Rosa Blanca
Oro: Oro Bilbao
Legado de Yuste
Casimiro Mahou
Maestra: Mahou Maestra
Tennent's: Tennents
Newcastle Brown Ale: Newcastle
Murphy's: Murphys
Kilkenny
Tuborg
Jupiler
Blue Moon
Samuel Adams: Sam Adams
Sierra Nevada
Red Stripe
Baltika
Cobra
Kingfisher
Ichnusa
Menabrea
Tripel Karmeliet: Karmeliet
Westmalle
Orval
Rochefort
Gulden Draak
Kasteel
Lindemans
Schneider Weisse
Maisel's: Maisels
Bohemia
Águila Roja
Estrella Jalisco
Michelob
Pabst: Pabst Blue Ribbon|PBR
Antarctica
Patagonia
Cristal
Pilsen: Pilsen Callao
Club Colombia
Imperial
Toña
Bucanero
San Miguel 1516: 1516
Ambar 1900
Sureña: Cruzcampo Sureña
Carling
Stella Galicia""",
4: """Dougall's: Dougalls
Basqueland
Naparbier
Garage Beer: Garage
La Pirata
Cierzo
Península
Mala Gissona
Laugar
Edge Brewing: Edge
Espiga
Montseny: Cervesa del Montseny
Rosita
Er Boquerón: Boquerón
Tyris
Zeta
La Socarrada: Socarrada
Mica
Bidassoa
Boga
Ordio Minero
Caleya
Nómada
Sevebrau
Cerex
Dolina
Castreña
Enigma
Domus
Sagra Bohío: Bohío
Burro de Sancho
Gredos
Veer
Malquerida
Complot
Turia Märzen Tostada
Zywiec
Lech
Okocim
Ursus
Timisoreana
Maes
Westvleteren
Achel
London Pride: Fuller's|Fullers
Old Speckled Hen
Smithwick's: Smithwicks
Beamish
Harp
Faxe
Ceres
Mikkeller
Lapin Kulta
Karhu
Snow
Harbin
Bintang
Red Horse
Leo
Saigon
Beerlao
Angkor
Victoria Bitter: VB
XXXX: Castlemaine XXXX
Coopers
Tooheys
Steinlager
Molson
Labatt
Moosehead
Medalla
Carib
Banks
Kalik
Mayabe
Zulia
Pilsener
Paceña
Andes
Escudo
Kunstmann
Itaipava
Gambrinus
Krušovice: Krusovice
Bernard
Zlatopramen
Tusker
Castle
Windhoek
Estrella Galicia 0,0
Cruzcampo Gran Reserva
Almogàver
Ausesken
Marlen
Santa Cristina"""}

FUERA_NOMBRE = re.compile(r"\b(brauerei|privatbrauerei|brewery|breweries|brewing|company|co\.?|cervecería|cervecera|cerveceria|"
                          r"cervezas?|grupo|group|brouwerij|brasserie|pivovar|birrificio|birra|bryggeri|inc\.?|ltd\.?|gmbh|s\.a\.?|ag)\b", re.I)

filas, hechas = [], set()
for nv, bloque in MANO.items():
    for linea in bloque.splitlines():
        n, _, al = linea.partition(": ")
        filas.append((n.strip(), [a for a in al.split("|") if a], nv, 1000 - nv))
        hechas.add(clave(n))

vistos = {}
with open(FUENTES / "cervezas_wikidata.tsv", encoding="utf-8") as f:
    next(f)
    for linea in f:
        c = linea.rstrip("\n").split("\t")
        etiqueta = lambda s: s.split('"')[1] if '"' in s else ""
        es, en, links = etiqueta(c[1]), etiqueta(c[2]), int(c[3])
        if not es or re.fullmatch(r"Q\d+", es): es = en
        if not es or re.search(r"[^\x00-ɏ]", es) or es[0].islower(): continue   # sin nombre o en otro alfabeto
        corto = re.sub(r"\s+", " ", FUERA_NOMBRE.sub("", es)).strip(" ,-&")
        if len(clave(corto)) < 3: corto = es
        alias = {es, en} - {corto, ""}
        v = vistos.get(c[0])
        if v: v[1].update(alias)
        else: vistos[c[0]] = [corto, alias, links]
for corto, alias, links in vistos.values():
    if clave(corto) in hechas: continue
    filas.append((corto, sorted(alias), nivel_por_umbral(links, [10**6, 10**6, 20, 6]), links))
guarda("cervezas", filas, "ediciones_wikipedia")
