"""Respuestas que faltaban en datos/banco.csv, añadidas por Claude (2026-09-23).

Una por línea: "nivel|Respuesta|alias;alias". Si una ya está en el CSV (o
coincide con uno de sus alias), el script la descarta: manda el CSV.
Conviene revisarlas; están aquí para que no se dé por mala una respuesta
correcta que mucha gente diría.
"""

NUEVAS = {
 # ── países ──
 6: """3|Palestina|Estado de Palestina
4|Vaticano|Ciudad del Vaticano;Santa Sede
4|Kosovo
3|Taiwán|Taiwan""",
 10: """3|Myanmar (Birmania)|Myanmar;Birmania
4|Chipre
3|Rusia
3|Palestina|Estado de Palestina
3|Taiwán|Taiwan""",
 11: """1|Reino Unido|Gran Bretaña;UK;Inglaterra
2|Andorra
3|Montenegro
3|Vaticano|Ciudad del Vaticano;Santa Sede
4|Kosovo
4|Turquía
5|Georgia
5|Armenia
5|Azerbaiyán
5|Kazajistán""",
 8: """1|Libra esterlina|Libra;GBP;Libras""",

 # ── ciudades de España (municipios que faltaban) ──
 19: """3|Getxo
3|Irún
3|Barakaldo
3|Lorca
3|Mérida
3|Albacete
3|Ciudad Real
3|Zamora
3|Plasencia
3|Torrent|Torrente
3|Paterna
3|Sagunto|Sagunt
3|Alcoy|Alcoi
3|Majadahonda
3|Pozuelo de Alarcón|Pozuelo
3|Las Rozas|Las Rozas de Madrid
3|San Sebastián de los Reyes|Sanse
3|Coslada
3|Valdemoro
3|El Ejido
3|Molina de Segura
3|Vila-real|Villarreal
3|Dénia|Denia
3|Jávea|Xàbia
3|Calpe|Calp
3|Alzira
3|Xàtiva|Játiva
3|Cullera
3|Peñíscola
3|Eibar
3|Zarautz
3|Hondarribia|Fuenterrabía
3|Tudela
3|Estella|Lizarra
3|Castro Urdiales
3|Laredo
3|Santillana del Mar
3|Llanes
3|Ribadesella
3|Cangas de Onís
3|Villaviciosa
3|Almuñécar
3|Nerja
3|Mojácar
3|Tarifa
3|Chipiona
3|Conil de la Frontera|Conil
3|Vejer de la Frontera|Vejer
3|Carmona
3|Osuna
3|Villanueva de la Serena
3|Don Benito
3|Almendralejo
3|Zafra
3|O Grove|El Grove
3|Sanxenxo|Sangenjo
3|Cambados
3|Betanzos
3|Lloret de Mar
3|Tossa de Mar
3|Roses|Rosas
3|Palamós
3|Calella
3|Santa Coloma de Gramenet
3|Cornellà de Llobregat|Cornellá
3|Sant Boi de Llobregat
3|Mollet del Vallès
3|El Prat de Llobregat|El Prat
3|Vilafranca del Penedès
3|Martorell
3|Tres Cantos
3|Collado Villalba
3|Boadilla del Monte
3|Pinto
3|Arganda del Rey
3|Aranda de Duero
3|Talavera de la Reina
3|Illescas
3|Mahón|Maó
4|Ciempozuelos
4|Villanueva de la Cañada
4|Navalcarnero
4|Medina de Rioseco
4|Tordesillas
4|Peñafiel
4|Sepúlveda
4|Pedraza
4|La Granja de San Ildefonso|La Granja
4|San Lorenzo de El Escorial|El Escorial
4|Alcalá la Real
4|Guadix
4|Priego de Córdoba
4|Cabra
4|Montilla
4|Baena
4|Palma del Río
4|Lepe
4|Isla Cristina
4|Ayamonte
4|Aracena
4|Níjar
4|Vera
4|Huércal-Overa
4|Adra
4|Caravaca de la Cruz|Caravaca
4|Cieza
4|Yecla
4|Jumilla
4|Águilas
4|Mazarrón
4|San Javier
4|San Pedro del Pinatar
4|Totana
4|Villena
4|Petrer
4|Novelda
4|Crevillent|Crevillente
4|Santa Pola
4|Altea
4|Ontinyent|Onteniente
4|Requena
4|Sueca
4|Burriana|Borriana
4|Vinaròs|Vinaroz
4|Benicàssim|Benicasim
4|Onda
4|Mondragón|Arrasate
4|Durango
4|Gernika|Guernica
4|Bermeo
4|Portugalete
4|Santurtzi|Santurce
4|Basauri
4|Errenteria|Rentería
4|Tolosa
4|Azpeitia
4|Sestao
4|Leioa|Lejona
4|Llodio|Laudio
4|Barañáin
4|Tafalla
4|Olite
4|Haro
4|Calahorra
4|Arnedo
4|Santo Domingo de la Calzada
4|Caspe
4|Daroca
4|Borja
4|Utebo
4|Benasque
4|Sigüenza
4|Almagro
4|Consuegra
4|Seseña
4|Tarancón
4|La Alberca
4|Sahagún
4|Villafranca del Bierzo
4|Bembibre
4|La Bañeza
4|Toro
4|Puebla de Sanabria
4|Aguilar de Campoo
4|Briviesca
4|Covarrubias
4|Lerma
4|El Burgo de Osma
4|Almazán
4|Medinaceli
4|Arévalo
4|Cuéllar
4|Reinosa
4|Potes
4|San Vicente de la Barquera
4|Santoña
4|Suances
4|Noja
4|Luanco
4|Candás
4|Navia
4|Pola de Siero|Siero
4|Sarria
4|Verín
4|O Barco de Valdeorras|El Barco de Valdeorras
4|O Carballiño|Carballiño
4|Ribadavia
4|Pontedeume
4|Noia|Noya
4|Muros
4|Fisterra|Finisterre
4|Camariñas
4|Muxía
4|Mondoñedo
4|Foz
4|Poio
4|Bueu
4|Moaña
4|Nigrán
4|A Guarda|La Guardia
4|Sóller
4|Pollença|Pollensa
4|Alcúdia
4|Felanitx
4|Santanyí
4|Andratx
4|Valldemossa
4|Sant Antoni de Portmany|San Antonio
4|Sant Josep de sa Talaia|San José
4|Formentera
4|Yaiza
4|Teguise
4|Tías
4|La Oliva
4|Pájara
4|Agüimes
4|Ingenio
4|Teror
4|Icod de los Vinos|Icod
4|Garachico
4|Güímar
4|Granadilla de Abona|Granadilla
4|Santa Cruz de La Palma
4|Los Llanos de Aridane
4|San Sebastián de La Gomera
4|Valverde
4|Frigiliana
4|Setenil de las Bodegas|Setenil
4|Grazalema
4|Olvera
4|Ubrique
4|Cazorla
4|Martos
4|Bailén
4|La Carolina
4|Rota
4|Barbate
5|Alquézar
5|Aínsa
5|Hita
5|Atienza
5|Pastrana
5|Buitrago del Lozoya
5|Patones
5|Rascafría
5|Candelario
5|Mogarraz
5|Hervás
5|Guadalupe
5|Frías
5|Peñaranda de Duero
5|Urueña
5|Cudillero
5|Taramundi
5|Lastres
5|Combarro
5|Allariz
5|Castrillo de los Polvazares
5|Morella
5|Guadalest
5|Bocairent
5|Siurana
5|Besalú
5|Rupit
5|Pals
5|Peratallada
5|Begur
5|Calella de Palafrugell
5|La Seu d'Urgell|Seo de Urgel
5|Vielha|Viella
5|Puigcerdà
5|Ripoll
5|Olot
5|Sos del Rey Católico
5|Uncastillo
5|Anento
5|Valderrobres
5|Cantavieja
5|Rubielos de Mora
5|Mirambel
5|Calaceite
5|Laguardia
5|Oñati|Oñate
5|Getaria|Guetaria
5|Mundaka
5|Elantxobe
5|Lekeitio|Lequeitio
5|Ochagavía|Otsagabia
5|Roncesvalles|Orreaga
5|Ujué
5|Puente la Reina
5|Viana
5|Ezcaray
5|Briones
5|San Millán de la Cogolla""",

 20: """2|Pica d'Estats|Pica de Estats
2|Roque de los Muchachos
2|Roque Nublo
2|Pico de las Nieves
2|Montserrat
2|Tibidabo
2|Pedraforca
2|Puigmal
2|Puig Major
2|Penyagolosa|Peñagolosa
2|Aitana|Sierra de Aitana
2|Anboto|Amboto
2|Pico Viejo
2|Vignemale|Viñamala
3|Montseny|Turó de l'Home
3|Matagalls
3|Puig Campana
3|Montgó
3|Mesa de los Tres Reyes
3|La Rhune|Larrun
3|Jaizkibel
3|Peña Oroel|Oroel
3|Tozal de Guara|Guara
3|Turbón
3|Tuca de Mulleres|Mulleres
3|Pico del Lobo
3|Ocejón
3|La Mira
3|Tetica de Bacares|Tetica
3|Calar Alto
3|Peña Amaya
3|Picón Blanco
3|Cabeza de Manzaneda|Manzaneda
3|Monte Pindo|O Pindo
3|Alto Rey
4|Canigó|Canigou
4|Cadí
4|Tossal de la Baltasana
4|Mont Caro|Caro
4|Javalambre|Pico Javalambre
4|Pico Cebollera
4|La Tiñosa
4|Maroma
4|Torrecilla
4|Pico Lucero""",

 21: """1|Playa de San Lorenzo|San Lorenzo
1|Playa de la Caleta|La Caleta
1|Playa de Poniente
1|Playa de las Américas|Las Américas
1|La Manga
1|Playa de la Malagueta|La Malagueta
1|Playa de Palma
2|Playa de Valdevaqueros|Valdevaqueros
2|Playa de los Lances|Los Lances
2|Playa de El Palmar|El Palmar
2|Playa de los Caños de Meca|Caños de Meca
2|Playa de Matalascañas|Matalascañas
2|Playa de la Carihuela|La Carihuela
2|Playa de Burriana
2|Playa del Postiguet|Postiguet
2|Playa de la Pineda|La Pineda
2|Playa de Somorrostro
2|Playa del Bogatell|Bogatell
2|Playa de Sitges
2|Playa de Castelldefels
2|Playa del Silencio|El Silencio
2|Playa de Oyambre|Oyambre
2|Playa de Liencres|Valdearenas
2|Playa de la Salvé|La Salvé
2|Playa de Sopelana|Sopela
2|Playa de Bakio
2|Playa de Samil|Samil
2|Playa de Barra
2|Playa de Patos
2|Playa de las Vistas
2|Playa del Duque
2|Playa de Fañabé
2|Playa Blanca
2|Cala Comte
2|Cala d'Hort
2|Playa d'en Bossa
2|Cala Turqueta
2|Cala Galdana
2|Cala Mondragó
2|Playa de Formentor|Formentor
2|Playa de Alcúdia
2|Playa de Muro
2|Playa de Calblanque|Calblanque
2|Playa de Bolnuevo|Bolnuevo
2|Playa del Arenal
2|Playa de la Fossa
2|Playa de Gandía
2|Playa del Saler|El Saler
2|Playa de Peñíscola
2|Playa de Benicàssim
2|Playa de Tossa de Mar
2|Playa de Lloret de Mar
2|Playa de Mazagón|Mazagón
2|Playa de Punta Umbría
2|Playa de Islantilla|Islantilla
2|Playa de Mojácar
2|Playa de Agua Amarga
2|Playa de Cabopino|Cabopino
2|Playa de Puerto Banús
2|Playa de Torre del Mar
2|Playa de Salobreña
2|Playa de La Herradura
2|Playa de Jandía
2|Playa de Barlovento
2|Playa de las Conchas
2|Playa Jardín
2|Playa de La Tejita|La Tejita
2|Playa de Anfi del Mar|Anfi del Mar
2|Playa de Puerto Rico
2|Playa de Las Alcaravaneras|Las Alcaravaneras
2|Playa de Tazacorte
2|Playa de Los Cancajos|Los Cancajos
3|Playa de Xagó|Xagó
3|Playa de Barayo|Barayo
3|Playa de Frexulfe|Frexulfe
3|Playa de Penarronda|Penarronda
3|Playa de Poo
3|Playa de Berria|Berria
3|Playa de Merón|Merón
3|Playa de Langre|Langre
3|Playa de Barinatxe|La Salvaje
3|Playa de Mundaka
3|Playa de Deba
3|Playa de Orio
3|Playa de Hondarribia
3|Playa de Doniños|Doniños
3|Playa de Pantín|Pantín
3|Playa de Valdoviño
3|Playa de Louro|Louro
3|Playa de Baroña|Baroña
3|Playa de As Furnas|As Furnas
3|Playa de Mera
3|Playa de Razo|Razo
3|Playa de Maro
3|Playa de Cantarriján|Cantarriján
3|Playa de Calahonda
3|Playa del Algarrobico|El Algarrobico
3|Playa del Playazo|El Playazo
3|Playa de los Locos
3|Playa de La Mata
3|Playa de Arenales del Sol|Arenales del Sol
3|Playa de Las Marinas
3|Playa de Pinedo
3|Playa de La Devesa
3|Playa del Gurugú
3|Playa de Oropesa
3|Playa de Llevant
3|Playa de Nova Icària
3|Platja d'Aro
3|Playa de Aiguablava|Aiguablava
3|Playa de Sa Riera|Sa Riera
3|Cala en Porter
3|Cala Pregonda|Pregonda
3|Cala Varques
3|Cala Llombards
3|Cala Salada
3|Cala Saona
3|Playa de Migjorn|Migjorn
3|Playa de Sardina
3|Playa de las Gaviotas
3|Playa del Socorro""",

 22: """1|Atocha
1|Chueca
2|Sevilla
2|Santo Domingo
2|San Bernardo
2|Estrecho
2|Aluche
2|Casa de Campo
2|Carabanchel
2|Ciudad Lineal
2|Aeropuerto T4|T4
2|Aeropuerto T1-T2-T3|Aeropuerto T1 T2 T3
2|Metropolitano
2|Puerta de Toledo
3|Prosperidad
3|Alfonso XIII
3|Avenida de la Paz
3|San Lorenzo
3|Canillejas
3|Suanzes
3|Alameda de Osuna
3|Urgel
3|Vista Alegre
3|Eugenia de Montijo
3|Campamento
3|Laguna
3|Villa de Vallecas
3|Leganés Central
4|Torre Arias
4|El Capricho
4|Empalme
4|Sierra de Guadalupe
4|Congosto
4|La Gavia
4|Las Suertes
4|Valdecarros
4|Avenida de Guadalajara
4|Alsacia
4|La Almudena
4|San Fernando
4|Parque de Santa María
4|María Tudor
5|Hospital del Henares
5|La Fortuna
5|Prado de la Vega
5|Colonia de los Ángeles
5|Prado del Rey
5|Pozuelo Oeste
5|Bélgica
5|Dos Castillas
5|Campus de Somosaguas
5|Avenida de Europa
5|Berna
5|Retamares
5|Montepríncipe
5|Ventorro del Cano
5|Prado del Espino
5|Ferial de Boadilla
5|Infante Don Luis
5|Nuevo Mundo
5|Puerta de Boadilla""",

 23: """1|Tarta
1|Bizcocho
1|Yogur|Yogurt
1|Fruta
1|Macedonia de frutas|Macedonia
1|Tarta de fresa
1|Tarta de la abuela
1|Sorbete de limón|Sorbete
1|Cuajada
2|Tarta de whisky|Tarta al whisky
2|Tarta helada
2|Tarta Contessa|Contessa
2|Tronco de Navidad
2|Roscón de Reyes|Roscón
2|Turrón
2|Mazapán
2|Filloas
2|Petit suisse
2|Muffin
2|Cupcake
2|Brazo de gitano
2|Selva negra|Tarta Selva Negra
2|Fondue de chocolate
2|Banana split
2|Copa de helado
2|Tortitas|Tortitas con nata
2|Crepes|Crepe
2|Melocotón en almíbar
2|Fresas con nata
2|Carrot cake
2|Apple pie
3|Leche merengada
3|Sobao
3|Quesada
3|Mantecadas de Astorga|Mantecadas
3|Carquiñolis
3|Tocinillo
3|Rosquillas de Alcalá
3|Hojuelas
3|Flores de Carnaval|Flores manchegas
3|Tarta de San Marcos
3|Pionono
3|Tortel
3|Suspiros
3|Merengue
3|Pastel vasco|Gâteau basque
3|Tarta de hojaldre
3|Pastel de nata|Pastel de Belém
3|Baklava
3|Strudel
3|Clafoutis
3|Île flottante
3|Mochi
3|Dorayaki
3|Brigadeiro
3|Dulce de leche
3|Mamia""",

 24: """1|Kellogg's|Kelloggs
1|Copos de maíz
1|Avena
1|Copos de avena
1|Choco Pops
2|Miel Pops
2|Crunchy Nut
2|Corn Pops
2|Kellogg's Extra
3|Coco Krispies
3|Arroz inflado
3|Trigo inflado
3|Kix
3|Cap'n Crunch
3|Cinnamon Toast Crunch
3|Chex
3|Raisin Bran
3|Grape-Nuts
3|Honey Bunches of Oats
3|Frosted Mini-Wheats|Mini-Wheats""",

 25: """1|Pringles Original
2|Pringles Sour Cream|Pringles crema agria
2|Pringles Barbacoa
2|Pringles Paprika
2|Lay's Artesanas
2|Kettle|Kettle Chips
2|Tyrrells
2|Walkers
2|Sunbites
2|Doritos Nacho Cheese
2|Gusanitos
3|Frit Ravich
3|Aspil
3|Gorriaga
3|Hacendado
3|Pringles Hot & Spicy""",

 26: """1|Gazpacho
1|Crema de verduras
1|Puré
1|Caldo
1|Consomé
1|Sopa de fideos
1|Guiso
1|Estofado
2|Salmorejo
2|Crema de calabaza
2|Garbanzos con bacalao
2|Judías con chorizo
2|Alubias con chorizo
2|Lentejas con verduras
2|Patatas a la riojana
2|Patatas con carne
2|Patatas guisadas
2|Marmitako de bonito
2|Fabes
2|Sopa de tomate
2|Ajoblanco|Ajo blanco
3|Andrajos
3|Gachas
3|Sopa de cocido
3|Sopa de galets
3|Potaje canario
3|Berza jerezana|Berza
3|Caldo de pescado
3|Crema de puerros|Vichyssoise
3|Sopa de lentejas
3|Harira
3|Ramen
3|Pho
3|Goulash""",

 27: """1|Pizza de jamón y queso
1|Pizza cuatro estaciones
1|Pizza de champiñones|Funghi
1|Pizza boloñesa
2|Pizza vegana
2|Pizza de salami
2|Pizza de chorizo
2|Pizza de anchoas
2|Pizza de beicon|Pizza bacon
2|Pizza de queso de cabra
2|Pizza de trufa
2|Pizza de marisco
2|Pizza Mediterránea
2|Pizza tropical
2|Pizza de espinacas
2|Pizza de berenjena
2|Pizza campesina
2|Pizza de rúcula
2|Pizza de jamón serrano
3|Pizza al taglio
3|Focaccia
3|Pinsa
3|Sfincione
3|Panzerotti""",

 28: """1|Licor de hierbas
1|Licor de manzana
1|Licor de melocotón
1|Crema de whisky
1|Ron miel
1|Brandy
1|Coñac
1|Absenta
2|Ouzo
2|Raki
2|Grappa
2|Aguardiente
2|Tequila
2|Mezcal
2|Pisco
2|Licor de avellana
2|Licor de mora
2|Licor de cereza
2|Kirsch
2|Schnapps
2|Calvados
2|Licor de naranja
2|Licor de limón
2|Hierbas de Mallorca
2|Marie Brizard
2|Cuarenta y Tres
2|Patxaran
3|Arak
3|Advocaat
3|Becherovka
3|Strega
3|Maraschino
3|Chambord
3|Sabra
3|Cherry Heering
3|Fireball
3|Goldschläger
3|Hierbas dulces
3|Cazalla
3|Aguardiente de orujo
3|Crema de arroz
3|Licor de bellota
3|Licor de madroño""",

 29: """2|Agua de Sierra Nevada
2|Aquadeus
2|San Narciso
2|Vilajuïga
2|Fontecelta
2|Fontdor
2|Agua Hacendado
2|Voss
2|San Benedetto
2|Levissima
2|Ferrarelle
3|Magma de Cabreiroá|Magma
3|Firgas
3|Teror
3|Bronchales
3|Sant Aniol
3|Fuente Primavera
3|Malavella
3|Borjomi
3|Spa""",

 31: """1|Binter
1|Volotea
1|Iberia Express
1|Air Nostrum
1|Level
1|Plus Ultra
2|Canaryfly
2|Wamos Air
2|Evelop
2|Iberojet
2|Air Arabia
2|Flydubai
2|Pegasus Airlines|Pegasus
2|Aeroflot
2|LOT Polish Airlines|LOT
2|Austrian Airlines|Austrian
2|Icelandair
2|Luxair
2|Air Serbia
2|Croatia Airlines
2|airBaltic|Air Baltic
2|Condor
2|Smartwings
2|Saudia
2|Oman Air
2|Gulf Air
2|Kuwait Airways
2|El Al
2|Middle East Airlines
2|Sky Airline
2|JetSMART
2|Viva Aerobus
2|Arajet
2|Conviasa
2|Boliviana de Aviación
2|Lauda
3|Vistara
3|Air Astana
3|Uzbekistan Airways
3|Azerbaijan Airlines
3|Ukraine International Airlines
3|Belavia
3|Air Moldova
3|TAROM
3|Bulgaria Air
3|Olympic Air
3|Cyprus Airways
3|Air Corsica
3|Corsair
3|French Bee
3|Loganair
3|Air Malta|KM Malta Airlines
3|Flybe
3|Monarch
3|Thomas Cook Airlines
3|Spanair
3|Air Madrid
3|Aigle Azur
3|Pan Am
3|TWA""",

 33: """1|Natación sincronizada
1|Buceo con botella
1|Snorkel|Esnórquel
1|Piragua
2|Stand up paddle|SUP
2|Motos de agua|Moto acuática
2|Parasailing
2|Flyboard
2|Esquí náutico
2|Descenso de ríos
2|Barranquismo
2|Hidropedal
2|Vela ligera
2|Traineras|Regatas de traineras
2|Remo olímpico
2|Saltos de acantilado|Cliff diving
3|Hockey subacuático
3|Rugby subacuático
3|Polo acuático
3|Aquagym
3|Natación con aletas
3|Kitefoil
3|Windfoil
3|Tubing
3|Flysurf
3|Paddleboard""",

 34: """1|Pala|Palas
2|Raquetbol
2|Squash 57
3|Beach tennis
3|Racketlon
3|Platform tennis
3|Tenis en silla de ruedas
3|Bádminton de playa
3|Jeu de paume
3|Rackets
3|Fives""",

 35: """1|PS5
1|PS4
1|PS3
1|PS2
1|PS1
1|Switch
1|Nintendo Switch 2|Switch 2
2|Xbox One X
2|Xbox One S
2|PlayStation 4 Pro|PS4 Pro
2|PlayStation 5 Pro|PS5 Pro
2|PlayStation Portal
2|Steam Deck
2|New Nintendo 3DS
2|Nintendo DSi
2|Game & Watch
2|Game Gear|Sega Game Gear
2|Mega CD|Sega Mega CD
2|Sega 32X
2|Atari Jaguar
2|Atari Lynx
2|Meta Quest|Oculus Quest
2|Ouya
2|Virtual Boy
3|WonderSwan
3|N-Gage|Nokia N-Gage
3|CD-i|Philips CD-i
3|Amiga CD32
3|Magnavox Odyssey
3|Vectrex
3|Sega SG-1000
3|Sega Pico
3|PocketStation
3|Nintendo 64DD
3|Pippin
3|Evercade
3|Analogue Pocket
3|Playdate
3|ROG Ally
3|Legion Go""",

 36: """1|Super Mario Bros.|Super Mario
1|Arkanoid
1|Bomberman
1|Street Fighter
1|Mario Kart Arcade
2|Hang-On
2|Pole Position
2|Tron
2|Rampage
2|Marble Madness
2|Spy Hunter
2|Commando
2|Ghosts 'n Goblins
2|1943
2|Rastan
2|Shinobi
2|Altered Beast
2|Puzzle Bobble|Bust-a-Move
2|Cadillacs and Dinosaurs
2|Captain Commando
2|The King of Fighters|King of Fighters
2|Samurai Shodown
2|Fatal Fury
2|Killer Instinct
2|NBA Jam
2|Mortal Kombat II
2|Dance Dance Revolution
2|Point Blank
2|Silent Scope
2|Sega Rally
2|Ridge Racer
2|Tekken 3
2|Virtua Striker
2|Pang
3|Wonder Boy
3|Alien Syndrome
3|Space Harrier
3|Galaxian
3|Moon Patrol
3|Kung-Fu Master
3|Bad Dudes
3|Shadow Dancer
3|Toki
3|Snow Bros.
3|Tumblepop
3|Puzzle Fighter
3|Darkstalkers
3|Marvel vs. Capcom
3|Metal Slug X
3|Aero Fighters
3|Elevator Action
3|Bosconian
3|Scramble
3|Berzerk
3|Lunar Lander
3|Battlezone
3|Tapper
3|Punch-Out!!
3|Karate Champ
3|Yie Ar Kung-Fu
3|Circus Charlie
3|Sly Spy
3|Vendetta""",

 37: """2|Cheep Cheep
2|Blooper
2|Spiny
2|Buzzy Beetle
2|Bullet Bill
3|Destello|Luma
3|Dixie Kong
3|Candy Kong
3|Koopalings|Bowsitos
3|Kammy Koopa
3|Profesor E. Gadd|Profesor Fesor;E. Gadd
3|Cappy
3|Tiara
3|Príncipe Florián
4|Cackletta
4|Dimentio
4|Conde Cenizo|Count Bleck
4|Tatanga
4|Smithy
4|Mallow
4|Bowletta
4|Popple
4|Mario Oscuro|Shadow Mario
4|Wart
4|Mouser
4|Tryclyde
4|Spike|Foreman Spike""",

 38: """1|Pinocho
1|Genio|El Genio
1|Gastón
1|Rafiki
1|Sebastián
1|Flounder
1|Quasimodo
1|Alicia
1|Sombrerero Loco|Sombrerero
1|Reina de Corazones
1|Wendy
1|Pepito Grillo
1|Hada Madrina
1|Kristoff
1|Sven
1|Robin Hood
1|Rompe Ralph|Ralph
1|Mary Poppins
1|Tambor
2|Rey Tritón|Tritón
2|Zazu
2|Gato de Cheshire|Gato Risón
2|Conejo Blanco
2|Madrastra|Lady Tremaine
2|Príncipe Azul
2|Chip y Chop
2|Príncipe Juan
2|Hans
2|Megara|Meg
2|Pegaso
2|Filoctetes|Phil
2|Abu
2|Iago
2|Lumière
2|Ding Dong|Cogsworth
2|Señora Potts
2|Vanellope
2|Judy Hopps|Judy
2|Nick Wilde
2|Flash
2|Pascal
2|Madre Gothel|Gothel
2|Maximus
2|Heihei
2|Tamatoa
2|Naveen
2|Dr. Facilier|Facilier
2|Nani
2|Shang
2|Jane
2|Frollo
2|Timoteo
2|Flor
2|Duquesa
2|Marie
2|Merlín
2|Tod
2|Toby
2|Rey Louie
2|Clarabella
2|Horacio
2|Gepetto
2|Gruñón
2|Mudito
2|Sabio
2|Feliz
2|Dormilón
2|Tímido
2|Mocoso
2|Reina Malvada
2|Eric|Príncipe Eric
2|Sultán
2|Felipe|Príncipe Felipe
2|Flora, Fauna y Primavera|Flora;Fauna;Primavera
2|Pepa Madrigal
2|Christopher Robin
3|Sisu
3|Asha
3|Ray
3|Jumba
3|Pleakley
3|Pacha
3|Cri-Kee
3|Terk
3|Kerchak
3|Febo
3|Hugo, Víctor y Laverne|Hugo;Víctor;Laverne
3|O'Malley|Thomas O'Malley
3|Berlioz
3|Toulouse
3|Bernardo y Bianca|Bernardo;Bianca
3|Basil
3|Arquímedes
3|Arturo
3|Oliver
3|Pequeño Juan
3|Sheriff de Nottingham
3|Fígaro
3|Cleo
3|Monstruo
3|Anastasia y Drizella|Anastasia;Drizella
3|Gus
3|Jaq
3|Lucifer
3|Abuela Alma|Alma Madrigal
3|Antonio Madrigal
3|Conejo
3|Búho
3|Cangu y Rito|Cangu;Rito
4|Taron
4|Dodger""",

 39: """1|Andy
1|Emperador Zurg|Zurg
1|Marcianitos|Aliens;Marcianos
1|Jack-Jack
1|Ansiedad
2|Síndrome
2|Linguini
2|Colette
2|Perdigón
2|Pete el Apestoso|Pete Apestoso
2|Ken
2|Barbie
2|Bonnie
2|Sid
2|Celia
2|Bruce
2|Gill
2|Hank
2|Ellie
2|Charles Muntz|Muntz
2|Mamá Imelda|Imelda
2|Dante
2|Joe Gardner
2|Envidia
2|Ennui|Aburrimiento
2|Vergüenza
2|Flik
2|Atta
2|Hopper
2|Luigi
2|Guido
2|Chick Hicks
2|Cruz Ramírez
2|Mack
2|Ramone
2|Flo
2|Fillmore
2|Rey Fergus|Fergus
2|Reina Elinor|Elinor
2|Kevin
2|Nostalgia
3|Nigel
3|Destiny
3|Bailey
3|Heimlich
3|Francis
3|Spot
3|Jackson Storm
3|Francesco Bernoulli
3|Finn McMissile
3|Holley Shiftwell
3|Red
3|Chispas
3|Burbujas
3|Dos Caras""",

 40: """1|Doctor Muerte|Doctor Doom
1|Mary Jane|Mary Jane Watson
2|Gwen Stacy
2|Tía May
2|Pepper Potts
2|Motorista Fantasma|Ghost Rider
2|Blade
2|Miles Morales
2|Carnage|Matanza
2|Mysterio
2|Electro
2|Drax
2|Yondu
2|Odín
2|Peggy Carter
2|Mercurio|Quicksilver
2|Killmonger
2|Shuri
3|Buitre
3|Hombre de Arena
3|Lagarto
3|Rino
3|Gata Negra
3|Luke Cage
3|Jessica Jones
3|Puño de Hierro|Iron Fist
3|Spider-Woman|Mujer Araña
3|Spider-Gwen
3|Ego
3|Kraven|Kraven el Cazador
3|Kate Bishop
3|Yelena Belova|Yelena
3|Agatha Harkness|Agatha
3|Cable
3|Apocalipsis
3|Frigga
3|Heimdall
3|Valquiria
3|Maria Hill
3|Phil Coulson|Coulson
3|Howard Stark
3|Happy Hogan
3|Wong
3|Okoye
3|Morbius
4|Escorpión
4|Adam Warlock
4|Nova
4|Domino
4|X-23|Laura Kinney
4|Psylocke
4|Mister Siniestro|Siniestro
4|Rayo Negro|Black Bolt
4|Sif
4|Ancestral|La Anciana
4|M'Baku
4|Sylvie
4|Mobius
4|Madame Web
5|El que permanece|He Who Remains
5|Silver Sable""",

 41: """3|Frank Buffay Jr.|Frank Jr.
3|Kathy
3|Barry Farber
3|Janine Lecroix|Janine
3|Dr. Drake Ramoray|Drake Ramoray
4|Alice Knight
4|Joshua
4|Pete Becker
4|Gary
4|Erica
4|Sandra Green
4|Mr. Treeger|Treeger
4|Bonnie
4|Joanna
4|Frank Buffay
4|Phoebe Abbott
4|Charles Bing
5|Tim Burke
5|Kate Miller
5|Sophie""",

 42: """4|Cathy Simms
4|Robert Lipton|Senador Lipton
5|Esther Bruegger
5|Isabel Poreba
5|Brian Wittle""",

 43: """1|Emily en París|Emily in Paris
1|Heartstopper
1|Por trece razones|13 Reasons Why
1|House of Cards
1|Orange Is the New Black
1|One Piece
1|Monstruo|Monster
1|Dahmer
1|Adolescencia|Adolescence
1|Berlín
1|Las chicas del cable
1|Machos alfa
1|Merlí
2|Sky Rojo
2|Toy Boy
2|Valeria
2|El inocente
2|Sagrada familia
2|Los favoritos de Midas
2|Alta mar
2|Welcome to Eden|Bienvenidos a Edén
2|Todo va a ir bien
2|Cien años de soledad
2|El caso Asunta
2|Griselda
2|Ripley
2|The Night Agent
2|Sombra y hueso|Shadow and Bone
2|Locke & Key
2|La caída de la casa Usher
2|Painkiller
2|Narcos: México
2|Club de Cuervos
2|Rebelde
2|Virgin River
2|Yo nunca|Never Have I Ever
2|Daredevil
2|Jessica Jones
2|Luke Cage
2|Iron Fist
2|The Punisher
2|Las escalofriantes aventuras de Sabrina
2|Riverdale
2|Avatar: la leyenda de Aang
2|Kaos
2|The Witcher: El origen
2|La noche más larga
2|Hache
2|Alma
2|Fariña
2|Paquita Salas
2|Smiley
2|Las de la última fila
2|El jardinero
2|Olympo
2|Respira
2|Asesinato para principiantes""",

 44: """1|Clarkson's Farm|La granja de Clarkson
1|The Grand Tour
1|LOL: Si te ríes pierdes|LOL
1|Mr. & Mrs. Smith
1|Hazbin Hotel
1|Reina Roja
2|El Cid
2|Hunters
2|Transparent
2|Goliath
2|The Tick
2|Modern Love
2|Sneaky Pete
2|Mozart in the Jungle
2|La leyenda de Vox Machina|The Legend of Vox Machina
2|Batman: Caped Crusader
2|Secret Level
2|Cruel Summer
2|Citadel: Diana
2|La templanza
2|Un asunto privado
2|Operación Marea Negra
2|Hernán
2|Sin límites
2|Absentia
2|The Consultant
2|Swarm
2|Dead Ringers
2|Deadloch
2|Wilderness
2|The Rig
2|Riches
2|Alex Rider
2|Harlan Coben's Shelter""",

 45: """1|Aquí no hay quien viva
1|La que se avecina
1|Siete vidas|7 vidas
1|Aída
1|Camera Café
1|Los Serrano
1|Padre de familia|Family Guy
1|Young Sheldon|El joven Sheldon
1|Mr. Bean
1|La niñera|The Nanny
1|Padres forzosos|Full House
1|Cosas de casa|Family Matters
1|Un chapuzas en casa|Home Improvement
1|Matrimonio con hijos|Married... with Children
1|ALF
1|Farmacia de guardia
2|Allí abajo
2|Manos a la obra
2|Ana y los 7
2|Los hombres de Paco
2|Escenas de matrimonio
2|Plats bruts
2|Jet Lag
2|Moncloa, ¿dígame?
2|Los ladrones van a la oficina
2|Médico de familia
2|Olmos y Robles
2|El rey de Queens|The King of Queens
2|Mom
2|2 Broke Girls
2|Mike & Molly
2|Sabrina, cosas de brujas
2|Dharma y Greg
2|Samantha ¿qué?
2|Kevin Can Wait
2|Last Man Standing
2|American Dad
2|Futurama
2|South Park
2|Bob's Burgers
2|El rey de la colina|King of the Hill
2|Solo asesinatos en el edificio|Only Murders in the Building
2|Hacks
2|Shrinking
2|Unbreakable Kimmy Schmidt
2|Master of None
2|Atlanta
2|Insecure
2|Peep Show
2|Fawlty Towers
2|La víbora negra|Blackadder
2|Only Fools and Horses
2|Absolutely Fabulous
2|The Inbetweeners
2|Miranda
2|Friday Night Dinner
2|Mork y Mindy
2|Yo amo a Lucy|I Love Lucy
2|Loco por ti|Mad About You
2|Wings
2|Los problemas crecen|Growing Pains
2|Salvados por la campana|Saved by the Bell""",

 46: """1|Airbag
1|La gran familia
1|As bestas
1|La ciudad no es para mí
2|Las 13 rosas|Las trece rosas
2|Soldados de Salamina
2|El abuelo
2|La escopeta nacional
2|20.000 especies de abejas
2|Cerdita
2|Los renglones torcidos de Dios
2|Blancanieves
2|Justino, un asesino de la tercera edad|Justino
2|Fe de etarras
2|Los bingueros
2|El espinazo del diablo
2|Bajo cero
2|Campeonex
2|Lobo feroz
2|Donde caben dos
2|Mamá o papá
2|El hoyo 2
2|Historias de la puta mili
2|Acción mutante
3|Siete mesas de billar francés
3|Planta 4ª|Planta cuarta
3|Los girasoles ciegos
3|Asignatura pendiente
3|Ópera prima
3|Patrimonio nacional
3|El año de las luces
3|La buena estrella
3|Secretos del corazón
3|Tasio
3|Vacas
3|El perro del hortelano
3|La Celestina
3|Hasta el cielo
3|Cuerpo de élite
3|Ola de crímenes
3|El practicante
3|La llegada|Upon Entry
3|Las que tienen que servir
3|Sor Citroën
3|El turismo es un gran invento
3|Manolo la nuit
3|Los energéticos
3|Tras el cristal""",

 47: """1|Frozen 2|Frozen II
1|Toy Story 2
1|Toy Story 3
1|Toy Story 4
1|Buscando a Nemo
1|Monstruos, S.A.|Monstruos SA
1|Los Increíbles
1|Cars
1|Ratatouille
1|WALL-E
1|Up
1|Del revés|Inside Out
1|Coco
1|Piratas del Caribe
1|Pesadilla antes de Navidad
2|Moana 2|Vaiana 2
2|Zootrópolis 2
2|El Rey León 2|El Rey León 2: El tesoro de Simba
2|Brave
2|Soul
2|Luca
2|Elemental
2|Mary Poppins
2|Merlín el encantador
2|Ralph rompe Internet|Rompe Ralph 2
2|Maléfica
2|Cruella
2|Encantada
2|High School Musical
2|Cariño, he encogido a los niños
3|Mulán 2
3|Los rescatadores en Cangurolandia
3|Fantasía 2000
3|Descubriendo a los Robinsons
3|Winnie the Pooh
3|El regreso de Mary Poppins
3|La bruja novata
3|Pedro y el dragón Elliot
3|Tron
3|Frankenweenie
4|Zafarrancho en el rancho
4|Mundo extraño|Strange World""",

 48: """2|Spider-Man: Un nuevo universo|Un nuevo universo
2|Spider-Man: Cruzando el Multiverso|Cruzando el Multiverso
2|Capitán América: Brave New World|Brave New World
2|Thunderbolts
2|Los 4 Fantásticos: Primeros pasos|Primeros pasos
2|El increíble Hulk|The Incredible Hulk
3|Hulk
3|Daredevil
3|Ghost Rider|El motorista fantasma
3|X-Men Orígenes: Lobezno
3|Lobezno inmortal|The Wolverine
4|Elektra
4|Punisher|El castigador""",

 49: """1|Tiburón
1|El exorcista
1|Psicosis
1|Lo que el viento se llevó
1|El niño con el pijama de rayas
1|La lista de Schindler
1|El diablo viste de Prada
1|Cincuenta sombras de Grey
1|Tres metros sobre el cielo
1|Diario de una pasión
1|Mary Poppins
1|Peter Pan
1|El libro de la selva
1|Pinocho
1|La sirenita
1|Jumanji
1|Perdida|Gone Girl
1|La chica del tren
1|El Club de la Lucha
1|Oppenheimer
1|Soy leyenda
1|Guerra Mundial Z
1|Bambi
2|El señor de las moscas
2|Cien años de soledad
2|La casa de los espíritus
2|El amor en los tiempos del cólera
2|Crónica de una muerte anunciada
2|Don Quijote
2|Drácula de Bram Stoker
2|Entrevista con el vampiro
2|Los hombres que no amaban a las mujeres|Millennium
2|La vida de Pi
2|Cometas en el cielo
2|Slumdog Millionaire
2|Memorias de una geisha
2|El pianista
2|Alguien voló sobre el nido del cuco
2|El color púrpura
2|Loca por las compras
2|Un paseo para recordar
2|Querido John
2|Wonder
2|Stuart Little
2|Coraline
2|La guerra de los mundos
2|La máquina del tiempo
2|Crazy Rich Asians
2|A todos los chicos de los que me enamoré
2|After
2|Culpa mía
2|A través de mi ventana
2|El guardián invisible
2|Alatriste
2|Los santos inocentes
2|Las bicicletas son para el verano
2|Mortadelo y Filemón
2|Superlópez
2|Astérix y Obélix
2|Las aventuras de Tintín|Tintín
2|Killers of the Flower Moon|Los asesinos de la luna
2|Pobres criaturas
2|Cónclave
2|Shutter Island
2|Mystic River
2|Hannibal
2|El Dragón Rojo
3|Rebecca
3|Los pájaros
3|Kramer contra Kramer
3|Tomates verdes fritos
3|Criadas y señoras
3|Los puentes de Madison
3|Babe, el cerdito valiente
3|James y el melocotón gigante
3|Fantastic Mr. Fox
3|La sociedad literaria y el pastel de piel de patata
3|La sombra del viento
3|La colmena
3|Réquiem por un campesino español
3|Tristana
3|Marianela
3|Fortunata y Jacinta
3|La Regenta
3|El Lazarillo de Tormes
3|Jackie Brown""",

 50: """1|Woody Allen
1|Santiago Segura
1|Charles Chaplin|Chaplin;Charlie Chaplin
1|Alfonso Cuarón|Cuarón
1|Alejandro González Iñárritu|Iñárritu
1|Michael Bay
1|J. J. Abrams|JJ Abrams
1|Zack Snyder
1|Guy Ritchie
1|Ron Howard
1|Robert Zemeckis
1|Sam Raimi
1|Mel Brooks
1|Orson Welles
2|Billy Wilder
2|John Ford
2|Sergio Leone
2|Roman Polanski
2|Oliver Stone
2|Spike Lee
2|Hermanos Coen|Coen;Joel Coen;Ethan Coen
2|Hermanas Wachowski|Wachowski
2|Rob Reiner
2|Tony Scott
2|Danny Boyle
2|Sam Mendes
2|Paul Thomas Anderson
2|Darren Aronofsky
2|Damien Chazelle
2|Taika Waititi
2|James Gunn
2|John Carpenter
2|Wes Craven
2|George A. Romero|Romero
2|Brian De Palma
2|Kathryn Bigelow
2|Lars von Trier
2|Vittorio De Sica
2|Bernardo Bertolucci
2|Giuseppe Tornatore
2|Luc Besson
2|Jean-Pierre Jeunet
2|Wong Kar-wai
2|Zhang Yimou
2|Ang Lee
2|Juan José Campanella
2|Bigas Luna
2|Julio Medem
2|Paco León
2|Fernando Colomo
2|Mariano Ozores
2|Pilar Miró
3|Jane Campion
3|Chloé Zhao
3|Michael Haneke
3|Pier Paolo Pasolini|Pasolini
3|Roberto Rossellini
3|Luchino Visconti
3|Paolo Sorrentino
3|Céline Sciamma
3|Hirokazu Kore-eda|Kore-eda
3|Takeshi Kitano
3|Pablo Larraín
3|Damián Szifron
3|Cohn y Duprat|Mariano Cohn;Gastón Duprat
3|Carlos Vermut
3|Nacho G. Velilla
3|Borja Cobeaga
3|Alauda Ruiz de Azúa
3|Estibaliz Urresola
3|Benito Zambrano
3|Achero Mañas
3|Cesc Gay
3|Gracia Querejeta
3|Mario Camus
3|Iván Zulueta
3|Juanma Bajo Ulloa
3|Pedro Masó
3|Jaime Chávarri
3|Manuel Gutiérrez Aragón
3|Ruben Östlund
3|Justine Triet
3|Celine Song
3|Asghar Farhadi
4|Satyajit Ray
4|Abbas Kiarostami
4|Lucrecia Martel
4|Basilio Martín Patino
4|Josefina Molina
4|Pedro Olea
4|Ricardo Franco
4|Patricia Ferreira""",

 51: """1|Enrique Iglesias
1|Julio Iglesias
1|Ricky Martin
1|Luis Miguel
1|J Balvin
1|Maluma
1|Karol G
1|Daddy Yankee
1|Juanes
1|Pitbull
1|Kanye West|Ye
1|Jay-Z
1|Snoop Dogg
1|50 Cent
1|Tupac|2Pac;Tupac Shakur
1|Bob Marley
1|Louis Armstrong
1|Robbie Williams
1|Bon Jovi|Jon Bon Jovi
1|Kurt Cobain
1|Ozzy Osbourne
1|Mick Jagger
1|Bono
1|Avicii
1|David Guetta
1|Calvin Harris
1|Camila Cabello
1|Shawn Mendes
1|Lewis Capaldi
1|Alicia Keys
1|Usher
1|Laura Pausini
1|Eros Ramazzotti
1|Andrea Bocelli
1|Édith Piaf
1|Gloria Estefan
1|Celia Cruz
1|Thalía
1|Paulina Rubio
1|Marc Anthony
1|Avril Lavigne
1|Pink|P!nk
1|Gwen Stefani
1|Nina Simone
1|Johnny Cash
1|Dolly Parton
1|Jimi Hendrix
1|Janis Joplin
1|Jim Morrison
1|Enya
1|Chris Martin
1|Liam Gallagher
1|Noel Gallagher
2|Ozuna
2|Anuel AA
2|Rauw Alejandro
2|Peso Pluma
2|Nicky Jam
2|Becky G
2|Anitta
2|Juan Luis Guerra
2|Carlos Vives
2|Tiziano Ferro
2|Zucchero
2|Måneskin
2|Stromae
2|Charles Aznavour
2|Serge Gainsbourg
2|Johnny Hallyday
2|Aya Nakamura
2|Ella Fitzgerald
2|Billie Holiday
2|Kenny Rogers
2|Willie Nelson
2|Chris Brown
2|Ne-Yo
2|Akon
2|Flo Rida
2|Dr. Dre
2|The Notorious B.I.G.|Biggie;Notorious B.I.G.
2|Lil Wayne
2|Lil Nas X
2|Lizzo
2|Megan Thee Stallion
2|Halsey
2|Charlie Puth
2|James Arthur
2|George Ezra
2|Martin Garrix
2|Tiësto
2|Marshmello
2|Kygo
2|Axl Rose
2|Morrissey
2|Sinéad O'Connor
2|Florence Welch|Florence + the Machine
2|Ellie Goulding
2|Jessie J
2|Rita Ora
2|Anne-Marie
2|Olivia Newton-John
2|Barbra Streisand
2|Diana Ross
2|Janet Jackson
2|Kelly Clarkson
2|Alanis Morissette
2|Norah Jones
2|Michael Bublé
2|Tony Bennett
2|Dean Martin
2|Nat King Cole
2|Chuck Berry
2|Little Richard
2|Roy Orbison
2|Lou Reed
2|Iggy Pop
2|Leonard Cohen
2|Neil Young
2|Paul Simon
2|Billy Joel
2|Zayn|Zayn Malik
2|Jungkook
2|Lisa
2|Jennie
2|Rosé
2|PSY
2|Benson Boone
2|Teddy Swims
2|Tate McRae
2|Raye
3|Mylène Farmer
3|Luke Combs
3|Morgan Wallen
3|Kacey Musgraves
3|Garth Brooks
3|Tom Walker
3|Gary Barlow
3|Liza Minnelli
3|Bing Crosby
3|Jerry Lee Lewis
3|Buddy Holly
3|Patti Smith
3|Joni Mitchell
3|Art Garfunkel
3|Niall Horan
3|Louis Tomlinson
3|Jimin""",

 52: """1|Mägo de Oz|Mago de Oz
1|Camela
1|Los del Río
1|Andy y Lucas
1|La 5ª Estación|La Quinta Estación
1|El Último de la Fila
2|Los Planetas
2|Taburete
2|Los Chichos
2|Las Ketchup
2|Café Quijano
2|Despistaos
2|Pignoise
2|Chambao
2|Dover
2|Los Delinqüentes|Los Delincuentes
2|Efecto Pasillo
2|Los Chunguitos
2|Parchís
2|Azúcar Moreno
2|Ketama
2|Dvicio
2|Nena Daconte
2|El Sueño de Morfeo
2|Maldita Nerea
2|Upa Dance
2|Ella Baila Sola
3|Ojos de Brujo
3|Muchachito Bombo Infierno
3|Leño
3|Burning
3|Obús
3|Medina Azahara
3|Triana
3|Los Brincos
3|Los Bravos
3|Fórmula V
3|Mocedades
3|Los Payasos de la Tele
3|Tequila
3|La Polla Records
3|Kortatu
3|Berri Txarrak
3|Soziedad Alkoholika
3|Barricada
3|Lori Meyers
3|Ilegales
3|Los Rebeldes
3|Amparanoia
3|Violadores del Verso
3|SFDK
3|Pxxr Gvng
3|Hinds
3|Veintiuno
3|Natos y Waor
3|Los Manolos
3|Siempre Así
3|Sôber
3|Las Grecas
3|Sidecars
3|Revólver
3|Los Chikos del Maíz
3|Ojete Calor
3|La M.O.D.A.
3|Pata Negra
3|Baccara
3|Sergio y Estíbaliz
3|Melocos
3|D'Nash
4|Asfalto
4|Ñu
4|Smash
4|Los Pekenikes
4|Los Módulos
4|Objetivo Birmania
4|Kaka de Luxe
4|Parálisis Permanente
4|Golpes Bajos
4|Aviador Dro
4|Eskorbuto
4|Negu Gorriak
4|Su Ta Gar
4|Hertzainak
4|Los Enemigos
4|Sexy Sadie
4|Australian Blonde
4|Los Piratas
4|Maga
4|The Parrots
4|Shinova
4|Rufus T. Firefly
4|León Benavente
4|Varry Brava
4|Siloé
4|Saratoga
4|Avalanch
4|WarCry
4|Tierra Santa
4|Ángeles del Infierno
4|Porretas
4|Gatillazo
4|Tahúres Zurdos
4|Los Nikis
4|Cycle
4|The Pinker Tones
4|Delorean
4|Veneno
4|Taxi
5|Topo
5|Regaliz
5|Derribos Arias
5|Sr. Chinarro
5|Nudozurdo
5|Mourn
5|Biznaga
5|Skizoo
5|Glutamato Ye-Yé
5|We Are Standard
5|Egon Soda
5|Tabletom""",
}
