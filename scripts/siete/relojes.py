"""Marcas de relojes.
Lista: las marcas y fabricantes de las categorías «Watch brands» y «Watch manufacturing companies»
de la Wikipedia en inglés, más las que se venden en las relojerías y joyerías de España.
Nivel: las conocidas en España están ordenadas a mano; el resto, por visitas de su artículo
en la Wikipedia en inglés en el último año."""
from comun import *

MANO = {
1: """Rolex
Casio: G-Shock|G Shock|Casio G-Shock
Swatch
Apple: Apple Watch
Omega
Lotus
Festina
Seiko
Cartier
Tissot""",
2: """TAG Heuer: Tag|Heuer
Viceroy
Citizen
Garmin
Samsung: Galaxy Watch|Samsung Galaxy Watch
Tous
Guess
Fossil
Michael Kors
Daniel Wellington
Longines
Breitling
Patek Philippe: Patek
Hublot
Calvin Klein: CK
Tommy Hilfiger: Tommy
Armani: Emporio Armani|Giorgio Armani|Armani Exchange
Hugo Boss: Boss
Lacoste
Xiaomi: Mi Band|Xiaomi Watch|Redmi Watch
Huawei: Huawei Watch
Fitbit
Timex
Flik Flak: FlikFlak
Hamilton
Rado
Cluse
Mark Maddox
Radiant
Sandoz
Duward
Marea
Calypso
Jaguar
Swarovski
Tudor
Audemars Piguet: AP
Bulgari: Bvlgari
Montblanc: Mont Blanc""",
3: """IWC: IWC Schaffhausen|International Watch Company
Panerai: Officine Panerai
Zenith
Jaeger-LeCoultre: Jaeger LeCoultre|Jaeger
Vacheron Constantin: Vacheron
Chopard
Piaget
Richard Mille
Franck Muller
Baume & Mercier: Baume et Mercier|Baume
Oris
Mido
Bulova
Invicta
Diesel
Police
Skagen
Swiss Military: Swiss Military Hanowa|Hanowa
Victorinox
Ice-Watch: Ice Watch
Komono
Nixon
Suunto
Polar
Amazfit
Withings
Bell & Ross: Bell and Ross
Maurice Lacroix
Raymond Weil
Frederique Constant
Movado
Gucci
Chanel
Hermès
Louis Vuitton
Dior
Versace
Burberry
Lorus
Pulsar
Adidas
Nike
Puma
Kronos
Cuervo y Sobrinos
Maserati
Ferrari: Scuderia Ferrari
Certina
Candino
Orient
Nowley
Cauny
Potens
Dogma
Thermidor
Justina
Racer
Time Force
Pierre Cardin
Paul Hewitt
Rosefield
Olivia Burton
MVMT
Pandora
Aristocrazy
Majorica
Uno de 50
Breguet
Blancpain
Glashütte Original: Glashutte
A. Lange & Söhne: Lange|A Lange Sohne|Lange & Söhne
Grand Seiko
Ulysse Nardin
Girard-Perregaux: Girard Perregaux
Sector: Sector No Limits
Breil
Liu Jo
Pepe Jeans
Mr. Wonderful
Geox
Superdry
Vostok
Luminox
Junghans
Nomos: Nomos Glashütte
Jacob & Co: Jacob and Co
Harry Winston
Tiffany: Tiffany & Co.
Van Cleef & Arpels: Van Cleef
Ebel
Roger Dubuis
Corum"""}

CATS_NO = {"Category:Rolex people", "Category:Rolex watches", "Category:Casio watches", "Category:Rolex",
           "Category:Seiko", "Category:Patek Philippe", "Category:Citizen Watch", "Category:Breitling SA",
           "Category:Watch movement manufacturers"}
SOBRA = re.compile(r"\s*\(.*\)$|\b(Watch(es)? (Company|Group|Co\.?)|Watches|Watch|Uhrenmanufaktur|Company|Limited|Inc\.?|Corporation|"
                   r"Group USA|Group|SA|AG|Ltd\.?)\b\.?", re.I)

filas, hechas = [], set()
for nv, bloque in MANO.items():
    for linea in bloque.splitlines():
        n, _, al = linea.partition(": ")
        filas.append((n.strip(), [a for a in al.split("|") if a], nv, 10**9 - nv))
        hechas.update([clave(n)] + [clave(a) for a in al.split("|") if a])

pags = json.loads((FUENTES / "relojes_enwiki.json").read_text(encoding="utf-8"))["paginas"]
# artículos de esas categorías que no son marcas: modelos, personas, torneos, organismos
NO_MARCA = re.compile(r"^(History|List|Timeline) of|\d{3,}|Strike|Museum|Championship|Masters|\bv\. |Federation|Société|"
                      r"Gesellschaft|Datalink|Ironman|Expedition|Wrist PDA|Timex (Open|Sinclair|Computer)|TrueSmart|Mega$", re.I)
FUERA = {clave(x) for x in """Swiss made|Liquidmetal|The Holy Trinity|Microbrand watches|MoonSwatch|Indiglo|Nicolas Hayek|
George Daniels (watchmaker)|Philippe Dufour|Alan Banbery|Elmar Mock|Roger W. Smith|Giorgio Galli|Gerald Genta|Andreas Strehler|
Thomas Frederick Cooper|Victor Kullberg|Abraham-Louis Perrelet|Pirelli|Benetton Group|Epson|Davidoff|Richemont|The Swatch Group|
ETA SA|Valjoux|Lemania|Ronda AG|Ebauches SA|Seiko Instruments|Seikosha|The Hour Glass|Wempe|Michael Hill Jeweller|
Timexpo Museum|United States Watch Company|General Watch Co|Lancashire Watch Company|Illinois Watch Company|
Hangzhou Watch Company|Melbourne Watch Company|Beijing Watch Factory|Chung Nam Group of Companies|Sowind Group SA|
EganaGoldpfeil|Manufacture Modules Technologies|Montegrappa|Visconti (company)|Cressi-Sub|Mares (scuba equipment)|
Solari di Udine|Sigma Sport|SWISSGEAR|Braun (company)|OVS (company)|Liquidmetal""".replace("\n", "").split("|")}
pags = {t: c for t, c in pags.items() if c not in CATS_NO and not NO_MARCA.search(t) and clave(t) not in FUERA}
vis = visitas("en", list(pags), "relojes_visitas_en.json")
for t in pags:
    corto = re.sub(r"\s+", " ", SOBRA.sub("", t)).strip(" ,&-")
    if len(clave(corto)) < 3 or re.match(r"(of|the|and)\b", corto, re.I) or len(corto) < len(t) / 2.5: corto = re.sub(r"\s*\(.*\)$", "", t)
    if clave(corto) in hechas: continue
    v = vis.get(t) or 0
    filas.append((corto, [re.sub(r"\s*\(.*\)$", "", t)], nivel_por_umbral(v, [10**12, 10**12, 400000, 40000]), v))
guarda("relojes", filas, "visitas_wikipedia_en")
