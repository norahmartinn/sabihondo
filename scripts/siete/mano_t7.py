"""Séptima tanda (semana del 9 de noviembre de 2026): respuestas a mano.
Mismo formato que mano_t4.py, mano_t5.py y mano_t6.py: por nivel, respuestas separadas por comas y sus otras formas con «=».
Ojo: una coma dentro de un nombre lo parte en dos.

Las de lista cerrada van enteras: los 16 parques nacionales, las 100 películas más taquilleras de Box Office Mojo
(datos/siete/fuentes/t7/bom_top100.json) y las infracciones del anexo II de la Ley de Tráfico. El resto, con la cobertura más amplia posible."""

PREGUNTAS = {
    "simpsons": "Nombra un personaje de Los Simpson",
    "equipaje_mano": "Nombra un objeto que esté prohibido en el equipaje de mano de un avión",
    "parques_nacionales": "Nombra un parque nacional de España",
    "nike_modelos": "Nombra un modelo de zapatillas Nike",
    "tartas": "Nombra una tarta",
    "infracciones_puntos": "Nombra una infracción que quita puntos del carnet",
    "taquilleras": "Nombra una de las 100 películas más taquilleras de la historia",
}

MANO = {
"simpsons": {
 1: "Homer Simpson=Homer=Homero, Marge Simpson=Marge, Bart Simpson=Bart, Lisa Simpson=Lisa, Maggie Simpson=Maggie, "
    "Abraham Simpson=el abuelo Simpson=abuelo Simpson=Abe Simpson=el abuelo=Abe, Montgomery Burns=el señor Burns=señor Burns=Sr. Burns=Burns, "
    "Moe Szyslak=Moe, Ned Flanders=Flanders=Ned, Apu Nahasapeemapetilon=Apu, Krusty el payaso=Krusty, Milhouse Van Houten=Milhouse, Barney Gumble=Barney",
 2: "Waylon Smithers=Smithers, Clancy Wiggum=el jefe Wiggum=jefe Wiggum=Wiggum, Ralph Wiggum=Ralph, Seymour Skinner=el director Skinner=director Skinner=Skinner, "
    "Nelson Muntz=Nelson, Patty Bouvier=Patty=Patty y Selma=las hermanas de Marge, Selma Bouvier=Selma, Edna Krabappel=Edna, el jardinero Willie=Willie, Otto Mann=Otto, "
    "Lenny Leonard=Lenny, Carl Carlson=Carl, Actor secundario Bob=Bob Patiño=Sideshow Bob, Rasca y Pica=Rasca=Pica=Itchy y Scratchy=Itchy=Scratchy, "
    "Ayudante de Santa Claus=Ayudante de Santa=Santa's Little Helper=el perro de los Simpson=Pequeño ayudante de Santa, Bola de Nieve=Bola de Nieve II=Snowball II=Snowball=el gato de los Simpson, "
    "Troy McClure, Hans Topo=Hans Moleman, Kent Brockman, el dependiente de la tienda de cómics=el de la tienda de cómics=Jeff Albertson=Comic Book Guy, "
    "el doctor Hibbert=Dr. Hibbert=Hibbert=doctor Hibbert=Julius Hibbert, el doctor Nick=Dr. Nick=Nick Riviera, Joe Quimby=el alcalde Quimby=alcalde Quimby=Quimby, "
    "el profesor Frink=Profesor Frink=Frink, Maude Flanders=Maude, Rod Flanders=Rod, Todd Flanders=Todd, Martin Prince=Martin, Gordo Tony=Fat Tony",
 3: "Lionel Hutz, Jimbo Jones=Jimbo, Kearney, Dolph, Sherri y Terri=Sherri=Terri, Lou, Eddie, Cletus, Brandine, Mona Simpson=Mona, "
    "Herb Powell=Herb, Jacqueline Bouvier=Jacqueline, el reverendo Lovejoy=reverendo Lovejoy=Lovejoy=Reverendo Alegría, Helen Lovejoy=Helen, Agnes Skinner=Agnes, "
    "Luann Van Houten=Luann, Kirk Van Houten=Kirk, Rainier Wolfcastle=McBain, Gil=Gil Gunderson=el viejo Gil, Disco Stu, Duffman, el hombre abeja=Bumblebee Man, "
    "la señorita Hoover=Elizabeth Hoover, Dewey Largo=el señor Largo, Encías Sangrantes Murphy=Encías Sangrantes=Bleeding Gums Murphy=Murphy Encías Sangrantes, Kang y Kodos=Kang=Kodos, "
    "Frank Grimes=Grimey, Actor secundario Mel=Mel=Sideshow Mel, Drederick Tatum=Tatum, el capitán McCallister=Horatio McCallister=el capitán=el viejo lobo de mar, "
    "Jasper, Uter=Üter=Üter Zörker, Wendell, Lewis, Jessica Lovejoy, Manjula, Sanjay, Arnie Pye, Lurleen Lumpkin=Lurleen, Laura Powers, Allison Taylor=Allison, "
    "el chico de la voz chillona=Squeaky-Voiced Teen=el adolescente de la voz chillona, el bebé de una ceja=Gerald, la loca de los gatos=Eleanor Abernathy=Crazy Cat Lady, "
    "Bernice Hibbert=Bernice, Snake=la serpiente, Kumiko, Cecil Terwilliger=Cecil, "
    "Mr. Teeny=el mono de Krusty, Hombre Radiactivo=Radioactive Man, Fallout Boy, Artie Ziff, Lindsey Naegle, "
    "Ling Bouvier=Ling, Zia Simpson, Hugo Simpson, Abbie Simpson, Sarah Wiggum, Raphael, Lunchlady Doris=Doris, "
    "Shelbyville Manhattan, Dr. Marvin Monroe=Marvin Monroe, Chalmers=el superintendente Chalmers, "
    "Llewellyn Sinclair, Luigi Risotto=Luigi, Hank Scorpio, Johnny Tightlips, Legs, Louie, Lyle Lanley, Sideshow Raheem, Ruth Powers, Poochie",
},
"equipaje_mano": {
 1: "líquidos de más de 100 ml=líquidos=líquido=un líquido=botella de agua=agua=una botella de agua=botella=botellas, una pistola=pistola=armas=arma=un arma=armas de fuego=arma de fuego, "
    "un cuchillo=cuchillo=cuchillos, una navaja=navaja=navajas, tijeras=unas tijeras=tijera",
 2: "un cúter=cúter=cutter=cúteres, explosivos=un explosivo=bomba=una bomba=dinamita, un mechero=mechero=encendedor=mecheros, cerillas=una caja de cerillas, "
    "gasolina, munición=balas=bala=cartuchos, fuegos artificiales=petardos=petardo=bengalas=bengala, spray de pimienta=gas pimienta=espray de pimienta=gas lacrimógeno, "
    "un bate de béisbol=bate de béisbol=bate, cuchillas de afeitar=cuchilla=cuchillas=cuchilla de afeitar, un martillo=martillo, un destornillador=destornillador, "
    "perfume grande=colonia grande=perfume=colonia, champú=gel de ducha=gel=crema=cremas=cosméticos de más de 100 ml, aerosoles=aerosol=espray=spray, "
    "pistola de juguete=réplica de arma=armas de juguete, una espada=espada=sable=katana",
 3: "palo de golf=palos de golf, un hacha=hacha, un machete=machete, una sierra=sierra, un taladro=taladro, una llave inglesa=llave inglesa, "
    "unos alicates=alicates, una palanca=palanca, un táser=táser=pistola eléctrica=pistola paralizante=defensa eléctrica, un arco=arco y flechas=flechas=ballesta, "
    "un tirachinas=tirachinas=honda, un arpón=arpón, nunchakus=nunchaku, un puño americano=puño americano, una porra=porra, "
    "estrellas ninja=estrella ninja=shuriken, un bisturí=bisturí, un punzón=punzón, un picahielos=picahielos=piolet, bastones de esquí=bastón de esquí, "
    "palo de hockey=stick de hockey, una caña de pescar=caña de pescar, un dardo=dardos, una jabalina=jabalina, una bombona de gas=bombona=gas de camping=camping gas, "
    "líquidos inflamables=disolvente=aguarrás=alcohol de quemar, pintura=pintura en espray, mermelada=miel=Nutella=crema de cacao, pasta de dientes grande=pasta de dientes, "
    "yogur=yogures, aceite=una botella de aceite, sopa=salsas=salsa, alcohol=una botella de vino=vino=una botella de alcohol, leche, zumo, refresco=lata de refresco",
 4: "cuchillo de cocina=cuchillo jamonero, sacacorchos con navaja, mechero de soplete=soplete, detonadores=detonador, granada=granadas, mina, "
    "cohetes, nitroglicerina, pólvora, gas, lejía, ácido=ácidos, veneno, sustancias tóxicas, material radiactivo, cloro, "
    "pistola de bengalas, pistola de clavos, pistola de aire comprimido=escopeta de aire comprimido=escopeta=rifle=revólver, cartucho de gas, "
    "bastón de senderismo, palo de lacrosse, raqueta de críquet, "
    "herramientas de más de 6 cm=herramientas=herramienta, cincel=formón, gel hidroalcohólico grande, desodorante en espray, "
    "laca=laca de pelo, espuma de afeitar, protector solar grande=crema solar, queso fresco=queso de untar, paté, hummus, guacamole, gazpacho, "
    "colonia de bebé, enjuague bucal, lentillas en líquido, esmalte de uñas=quitaesmalte, perfume de 200 ml",
},
"parques_nacionales": {
 1: "Doñana=Parque Nacional de Doñana, Teide=el Teide=Parque Nacional del Teide=Cañadas del Teide, Picos de Europa=Parque Nacional de los Picos de Europa=Covadonga, "
    "Sierra Nevada=Parque Nacional de Sierra Nevada, Ordesa y Monte Perdido=Ordesa=Monte Perdido=Parque Nacional de Ordesa",
 2: "Timanfaya=Parque Nacional de Timanfaya=Montañas del Fuego, Monfragüe=Parque Nacional de Monfragüe, Sierra de Guadarrama=Guadarrama=Parque Nacional de la Sierra de Guadarrama, "
    "Islas Atlánticas de Galicia=Islas Atlánticas=Islas Cíes=Cíes=Ons=Sálvora=Cortegada, Aigüestortes i Estany de Sant Maurici=Aigüestortes=Aiguestortes=Sant Maurici, "
    "Tablas de Daimiel=Las Tablas de Daimiel=Daimiel",
 3: "Garajonay=Parque Nacional de Garajonay, Caldera de Taburiente=La Caldera de Taburiente=Taburiente, Cabañeros=Parque Nacional de Cabañeros, "
    "Archipiélago de Cabrera=Cabrera=Parque Nacional de Cabrera",
 4: "Sierra de las Nieves=Parque Nacional de la Sierra de las Nieves",
},
"nike_modelos": {
 1: "Air Force 1=Air Force=AF1=Air Force One, Air Max=Nike Air Max, Air Jordan=Jordan=Jordan 1=Air Jordan 1=Jordans, Dunk=Nike Dunk=Dunk Low=Dunks",
 2: "Air Max 90=Max 90, Air Max 97=Max 97, Air Max 1=Max 1, Air Max Plus=TN=Air Max TN=Nike TN=Tuned, Cortez=Nike Cortez, Blazer=Nike Blazer=Blazer Mid, "
    "Pegasus=Air Zoom Pegasus=Nike Pegasus, Air Jordan 4=Jordan 4=AJ4, Court Vision, Revolution=Nike Revolution, Air Max 270=270, Huarache=Air Huarache, "
    "P-6000=P6000, Vomero=Zoom Vomero, Air Max 95=Max 95, Shox=Nike Shox, Killshot, Air Max Dn=Dn",
 3: "Air Jordan 3=Jordan 3, Air Jordan 11=Jordan 11, Air Jordan 5=Jordan 5, Air Jordan 6=Jordan 6, Air Jordan 13=Jordan 13, Air Jordan 12=Jordan 12, "
    "Air Max 720=720, Air Max 2090, Air Max Excee, Air Max SC, Air Max Command, Air Max Plus 3, Air Max Pulse, Air VaporMax=VaporMax, "
    "React Element=Element 55, Presto=Air Presto, Free Run=Nike Free, Roshe Run=Roshe=Roshe One, Tanjun, Waffle One=Waffle, Daybreak, "
    "Air Force 1 Shadow, Air Force 1 Mid, Air Force 1 High, Dunk High, SB Dunk=Nike SB=SB Dunk Low, Total 90=T90, Mercurial=Mercurial Vapor, "
    "Phantom=Phantom GX, Tiempo=Tiempo Legend, Superfly, Air Zoom Alphafly=Alphafly, Vaporfly=ZoomX Vaporfly, Invincible=ZoomX Invincible, "
    "Air Zoom Structure=Structure, Air Zoom Tempo, Metcon, Air Monarch=Monarch, Air Rift, Air Max Bella, Air Max Intrlk, V2K Run=V2K, Initiator, "
    "Zoom Vomero 5=Vomero 5, Air Pegasus 2K5, Air Max Portal, Gamma Force, Full Force, Court Legacy, Court Royale, Elevate, Air Max Systm, Air Max Ap, "
    "LeBron=Nike LeBron, Kobe=Nike Kobe, KD=Nike KD, Kyrie, Zoom Freak, Air Foamposite=Foamposite, Air Uptempo=Uptempo, Air More Uptempo, "
    "Cortez Nylon, Benassi=chanclas Benassi, Offcourt, Calm, Victori One, Air Max Tailwind=Tailwind, Air Max 180, Air Max Light, Air Max BW=Big Window",
 4: "Air Jordan 2=Jordan 2, Air Jordan 7=Jordan 7, Air Jordan 8=Jordan 8, Air Jordan 9=Jordan 9, Air Jordan 10=Jordan 10, Air Jordan 14=Jordan 14, "
    "Air Jordan 23, Jordan Max Aura, Jordan Spizike=Spizike, Jordan Stadium 90, Air Max 93, Air Max 98, Air Max 2015, Air Max 2017, Air Max 2013, "
    "Air Max Zero, Air Max Thea, Air Max Motion, Air Max Advantage, Air Max Axis, Air Max Fusion, Air Max Torch, Air Max Penny=Penny, Air Max Uptempo, "
    "Air Max Goadome=Goadome, Air Max 95 Ultra, Air Max Flyknit, Air Zoom Spiridon=Spiridon, Air Zoom Vomero, Zoom Fly, Zoom Rival, Zoom Streak, "
    "Air Footscape=Footscape, Air Rift, Air Tailwind 79, Air Safari=Safari, Air Stab, Air Span=Air Span II, Air Trainer 1=Air Trainer, Air Flight 89, "
    "Air Humara, Air Kukini, Air Mowabb, Air Max LTD, Air Max Correlate, Air Zoom Generation, Air Max Sunder, Air Woven, Air Huarache Run Ultra, "
    "Air Max 1 '86=Big Bubble, Lunarglide=Lunar, LunarEpic, Flyknit Racer=Flyknit, Flyknit Lunar, Free 5.0, Free TR, Juvenate, Kaishi, Racer, Roshe Two, "
    "Sock Dart, Air Max Plus TN SE, Shox TL, Shox R4, Shox NZ, Air Max Pre-Day, Air Max Pre Day, Air Zoom Pulse, Air Zoom Type, Zoom 2K=2K, "
    "Air Max Up, Air Max Verona, Air Max Dawn, Air Max Genome, Air Max Scorpion, Air Max Flyknit Racer, Waffle Racer, Waffle Trainer, Daybreak Type, "
    "Challenger OG, Internationalist, LD-1000=LD 1000, Tailwind 79, Oceania, Field General, Astrograbber, SB Blazer, SB Janoski=Janoski=Stefan Janoski, "
    "SB Nyjah, Bruin, Terminator=Nike Terminator, Air Ship, Book 1, Sabrina 1=Sabrina, GT Cut, Air Zoom G.T., Zoom Kobe, Hyperdunk, Kyrie Flytrap, "
    "Precision, Renew Run, Downshifter, Quest, Flex Experience=Flex, Winflo, Juniper Trail, Pegasus Trail, Wildhorse, Terra Kiger, ACG Mountain Fly, "
    "ACG Air Mada, Air Max 270 React, React Infinity Run=Infinity Run, React Vision, React Live, Joyride, Air Zoom Maxfly, Zoom Superfly, Air Zoom Victory, "
    "Air Zoom Mamba, Cosmic Unity, Air Max Impact, Air Max Alpha Trainer, Free Metcon, MC Trainer, Legend Essential, Air Max Bliss, Court Borough, "
    "Air Max 97 Silver Bullet=Silver Bullet, Air Max 1 Patta, Air Max 90 Infrared=Infrared, Air Force 1 Sage, Air Force 1 Pixel, Air Force 1 Fontanka, "
    "Air Force 1 Wild, Air Force 1 07=Air Force 1 '07, Air Max Plus Drift, Mind 001, Mind 002, Air Superfly, Calm Mule, Burrow, Asuna, Air Max Koko, "
    "Vapormax Plus, Vapormax Flyknit, Air Zoom Arcadia, Pico, Star Runner, Air Max Furyosa, Air Max Verse, Air Max Dia, Air Max Viva, Air Max Volt",
},
"tartas": {
 1: "tarta de queso=de queso=cheesecake=tarta de queso de La Viña=tarta de queso vasca=tarta de queso al horno, tarta de chocolate=de chocolate, "
    "tarta de la abuela=de la abuela=tarta de galletas=tarta de galletas y chocolate, tarta de manzana=de manzana=tarta tatin=tarte tatin, "
    "tarta de Santiago=de Santiago, tarta de fresa=de fresa=tarta de fresas=de fresas, tarta de cumpleaños=de cumpleaños",
 2: "tarta de zanahoria=de zanahoria=carrot cake, tarta Sacher=Sacher, Selva Negra=tarta Selva Negra, tarta de limón=de limón=tarta de merengue y limón=lemon pie, "
    "tarta de tres chocolates=tres chocolates, tarta de nata=de nata, tarta de whisky=de whisky=tarta al whisky, tarta helada=helada=tarta de helado=tarta al güisqui, "
    "tarta de trufa=de trufa, tarta de yogur=de yogur, tarta de queso con arándanos=de arándanos, tarta Red Velvet=Red Velvet=terciopelo rojo, "
    "tarta de frambuesa=de frambuesa, tarta de hojaldre=de hojaldre, tarta de crema=de crema, tarta de almendra=de almendra, tarta de coco=de coco, "
    "tarta de turrón=de turrón, tarta de piña=de piña=tarta de piña colada=upside-down cake, tarta de Oreo=de Oreo, tarta de Lotus=de Lotus, "
    "tarta de Kinder=de Kinder, tarta de Nutella=de Nutella, tarta de tiramisú=tiramisú, tarta de mousse=mousse",
 3: "tarta San Marcos=San Marcos, tarta de bodas=tarta nupcial=de boda=tarta de boda, tarta de Ferrero=de Ferrero Rocher=Ferrero, tarta de turrón de Jijona, tarta Pavlova=pavlova, "
    "tarta tres leches=tres leches, tarta de calabaza=de calabaza=pumpkin pie, tarta de nueces=de nueces=pecan pie=tarta de pecanas, tarta de ricota, "
    "tarta milhojas=milhojas, tarta de chocolate blanco=de chocolate blanco, tarta de café=de café, tarta de moka=moka, tarta de castañas=de castañas, "
    "tarta de higos=de higos, tarta de pera=de pera, tarta de melocotón=de melocotón, tarta de mango=de mango, tarta de cerezas=de cerezas, "
    "tarta de mora=de moras, tarta de plátano=de plátano=banoffee=banoffee pie, tarta de dulce de leche=de dulce de leche, tarta de flan=de flan=flan de tarta, "
    "tarta de requesón=de requesón, tarta de queso japonesa, tarta de queso de Idiazabal, tarta de queso azul, tarta de Halloween, tarta de fondant=fondant, "
    "tarta de unicornio, tarta de chuches, tarta de pañales, tarta de comunión, tarta Ópera=Ópera, tarta Charlotte=charlota, tarta de Linz=Linzer Torte=Linzertorte=Linzer, "
    "tarta de mazapán, tarta de cabello de ángel, tarta de crema catalana=crema catalana, tarta de arroz=tarta de arroz con leche, tarta de bizcocho, tarta de mantequilla, "
    "tarta de manzana alemana=Apfelstrudel, tarta de manzana y canela, tarta fría, tarta de queso sin horno, tarta de chocolate sin horno",
 4: "tarta Imperial=Imperial, tarta de Alcázar, tarta de Mondoñedo, tarta del Císter, tarta Ponche segoviano=ponche segoviano, tarta Contessa=Contessa, "
    "tarta Princesa=Prinsesstårta, tarta Dobos=Dobos, tarta Esterházy=Esterházy, tarta Malakoff, tarta Saint-Honoré=Saint Honoré, tarta Fraisier=Fraisier, "
    "tarta Paris-Brest=Paris-Brest, tarta Tropézienne, tarta Bakewell=Bakewell, tarta Banoffee, key lime pie=tarta de lima, tarta Mississippi=Mississippi mud pie=mud pie, "
    "tarta Boston=Boston cream pie, tarta Pastiera=pastiera, tarta Caprese=Caprese, tarta Bienenstich, tarta Schwarzwälder, tarta de Pascua, tarta Basque=gâteau basque=pastel vasco=tarta vasca, "
    "tarta de Gloria, tarta Massini=Massini, tarta Selva Negra blanca, tarta de cuajada, tarta de la Selva, tarta de Ezcaray, tarta de Yemas, tarta de Bilbao, "
    "tarta Muerte por chocolate, tarta de queso con dulce de membrillo, tarta de queso y frutos rojos, tarta de frutos rojos=de frutos rojos, tarta de frutas=de frutas, "
    "tarta de kiwi, tarta de maracuyá, tarta de pistacho=de pistacho, tarta de avellana, tarta de té matcha=de matcha, tarta de ruibarbo=ruibarbo, "
    "tarta de grosellas, tarta de chocolate y naranja, tarta de naranja=de naranja, tarta de mandarina, tarta de zanahoria y nueces, tarta de calabacín, "
    "tarta de batata=sweet potato pie, tarta de Baileys=de Baileys, tarta de mojito, tarta de gin-tonic, tarta de cerveza, tarta de cava, tarta de champán, "
    "tarta de Conguitos, tarta de Kit Kat, tarta de Huesitos, tarta de Filipinos, tarta de Chips Ahoy, tarta de Maltesers, tarta de Toblerone, "
    "tarta de Lacasitos, tarta de Milka, tarta de Mars, tarta de Snickers, tarta de Twix, tarta de Phoskitos, tarta de donuts, tarta de churros",
},
"infracciones_puntos": {
 1: "hablar con el móvil=usar el móvil=móvil=el móvil=llevar el móvil en la mano=conducir con el móvil=hablar por el móvil=hablar por teléfono, conducir borracho=alcohol=dar positivo=dar positivo en alcohol=conducir bebido=beber y conducir, "
    "exceso de velocidad=velocidad=ir rápido=correr=superar el límite de velocidad=multa de velocidad=radar, no llevar el cinturón=cinturón=el cinturón=sin cinturón, "
    "saltarse un semáforo=semáforo en rojo=pasar un semáforo en rojo=semáforo, drogas=conducir drogado=dar positivo en drogas",
 2: "saltarse un stop=stop=no respetar un stop=no parar en un stop, no llevar casco=casco=sin casco, adelantar mal=adelantamiento indebido=adelantar en línea continua=pisar la línea continua=línea continua, "
    "conducir en sentido contrario=sentido contrario=kamikaze, no respetar un paso de peatones=paso de peatones=paso de cebra=no dejar pasar a un peatón=atropellar, "
    "no llevar silla para niños=sillita=silla de bebé=sin sistema de retención infantil, ir pegado al coche de delante=no guardar la distancia de seguridad=distancia de seguridad, "
    "cambio de sentido prohibido=cambio de sentido=dar la vuelta donde no se puede=giro prohibido=media vuelta, negarse a hacer la prueba de alcohol=negarse a soplar=no soplar, "
    "llevar auriculares=auriculares=cascos de música, carreras ilegales=hacer carreras=carreras=piques, detector de radares=llevar un detector de radares=inhibidor de radares=inhibidor",
 3: "conducción temeraria=temeraria=conducir de forma temeraria, conducción negligente=negligente, usar el GPS mientras conduces=GPS=navegador=manipular el navegador=tocar la pantalla del coche, "
    "no respetar la prioridad=ceder el paso=no ceder el paso=saltarse un ceda el paso=ceda el paso, dar marcha atrás en autovía=marcha atrás en autopista=marcha atrás en autovía=marcha atrás, "
    "adelantar en curva=adelantar sin visibilidad=adelantar en un cambio de rasante, tirar objetos a la carretera=tirar una colilla=tirar colillas=tirar basura por la ventanilla, "
    "parar en una curva=estacionar en una curva=parar en un túnel=detenerse en un túnel=parar en un cambio de rasante, conducir de noche sin luces=sin luces=no encender las luces, "
    "no respetar las señales de un agente=no obedecer a un agente=saltarse a un guardia=no parar ante la Policía=huir de la Policía, "
    "llevar a un niño en el asiento de delante=niño delante, conducir con un menor sin casco",
 4: "incumplir el tiempo de descanso=conducir más horas de las permitidas=exceso de horas de conducción, manipular el tacógrafo=tacógrafo, "
    "adelantar a un ciclista sin dejar metro y medio=no dejar metro y medio a un ciclista=adelantar a un ciclista sin dejar espacio=poner en peligro a un ciclista=ciclista=ciclistas, "
    "invadir el sentido contrario=invadir el carril contrario, entrar en una calle en dirección prohibida=dirección prohibida, "
    "llevar el casco sin abrochar=casco desabrochado, llevar a un pasajero sin cinturón, superar la tasa de alcohol de novel, superar en 30 km/h el límite",
},
}
# alias de lo que viene de Box Office Mojo con los títulos con que se estrenaron en España
TAQUILLERAS = {
 1: "Avatar, Titanic, Vengadores: Endgame=Avengers: Endgame=Endgame, Frozen, Frozen 2=Frozen II, El rey león=El Rey León, Toy Story 3, Toy Story 4, Harry Potter y la piedra filosofal=Harry Potter=Harry Potter 1=La piedra filosofal, Barbie, Buscando a Nemo=Nemo, Jurassic Park=Parque Jurásico, Shrek 2, Minions, Los Increíbles 2=Increíbles 2, Del revés 2=Inside Out 2, Oppenheimer, Joker, Aladdin",
 2: "Avatar: El sentido del agua=Avatar 2, Vengadores: Infinity War=Avengers: Infinity War=Infinity War, Los Vengadores=The Avengers, Vengadores: La era de Ultrón=Avengers: Age of Ultron=La era de Ultrón, Spider-Man: No Way Home=No Way Home, Spider-Man: Lejos de casa=Spider-Man: Far From Home, Star Wars: El despertar de la Fuerza=Star Wars=El despertar de la Fuerza=Star Wars 7, Star Wars: Los últimos Jedi=Los últimos Jedi=Star Wars 8, "
    "Star Wars: El ascenso de Skywalker=El ascenso de Skywalker=Star Wars 9, Star Wars: La amenaza fantasma=La amenaza fantasma=Star Wars Episodio I, Star Wars: La venganza de los Sith=La venganza de los Sith=Star Wars Episodio III, Jurassic World, Top Gun: Maverick=Top Gun Maverick, Fast & Furious 7=Fast and Furious 7=Furious 7=A todo gas 7, Zootrópolis=Zootopia, Zootrópolis 2=Zootopia 2, "
    "La bella y la bestia, Super Mario Bros.: La película=Super Mario Bros=Mario Bros, Black Panther, Deadpool y Lobezno=Deadpool & Wolverine, Capitán América: Civil War=Civil War, Harry Potter y las reliquias de la Muerte: parte 2=Las reliquias de la Muerte 2=Harry Potter 8, Harry Potter y las reliquias de la Muerte: parte 1=Las reliquias de la Muerte 1=Harry Potter 7, Harry Potter y la cámara secreta=La cámara secreta=Harry Potter 2, "
    "Harry Potter y el cáliz de fuego=El cáliz de fuego=Harry Potter 4, Harry Potter y la Orden del Fénix=La Orden del Fénix=Harry Potter 5, Harry Potter y el misterio del príncipe=El misterio del príncipe=Harry Potter 6, El Señor de los Anillos: El retorno del Rey=El retorno del rey, El Señor de los Anillos: La Comunidad del Anillo=La Comunidad del Anillo, El Señor de los Anillos: Las dos torres=Las dos torres, Piratas del Caribe: El cofre del hombre muerto=Piratas del Caribe=El cofre del hombre muerto=Piratas del Caribe 2, Piratas del Caribe: En el fin del mundo=En el fin del mundo=Piratas del Caribe 3, "
    "Vaiana 2=Moana 2, Lilo y Stitch=Lilo & Stitch, Buscando a Dory=Dory, Bohemian Rhapsody, Gru 3=Gru 3: Mi villano favorito, Gru 4=Gru 4: Mi villano favorito, Una película de Minecraft=Minecraft, Skyfall, "
    "El caballero oscuro=The Dark Knight, El caballero oscuro: La leyenda renace=The Dark Knight Rises, Jumanji: Bienvenidos a la jungla=Jumanji",
 3: "Avatar: Fuego y ceniza=Avatar 3, Spider-Man: Homecoming, Spider-Man 3, Spider-Man: Brand New Day, Rogue One, Jurassic World: El reino caído, Jurassic World: Dominion, Fast & Furious 8=Fast and Furious 8=A todo gas 8=The Fate of the Furious, "
    "Iron Man 3, Aquaman, Capitana Marvel=Captain Marvel, Piratas del Caribe: En mareas misteriosas=En mareas misteriosas=Piratas del Caribe 4, Alicia en el país de las maravillas, El libro de la selva, Gru 2=Gru 2: Mi villano favorito, Minions: El origen de Gru, "
    "Spectre, Sin tiempo para morir=No Time to Die, Ice Age 3=Ice Age=Ice Age: El origen de los dinosaurios, Ice Age 4=Ice Age: La formación de los continentes, Mascotas=The Secret Life of Pets, Los juegos del hambre: En llamas=Los juegos del hambre=En llamas, Batman v Superman: El amanecer de la justicia=Batman v Superman, El hobbit: Un viaje inesperado=El hobbit, "
    "El hobbit: La desolación de Smaug, El hobbit: La batalla de los Cinco Ejércitos, Doctor Strange en el multiverso de la locura=Doctor Strange 2, Transformers: El lado oscuro de la luna=Transformers=Transformers 3, Transformers: La era de la extinción=Transformers 4, La saga Crepúsculo: Amanecer parte 2=Amanecer parte 2=Crepúsculo, Toy Story 5, Michael, "
    "La Odisea=The Odyssey, Super Mario Galaxy: La película=Super Mario Galaxy",
 5: "Ne Zha 2, La batalla del lago Changjin=The Battle at Lake Changjin, Wolf Warrior 2",
}

# ── martes 10 y siguientes ──
PREGUNTAS.update({
    "cintura": "Nombra una parte del cuerpo que esté por debajo de la cintura",
    "no_amarillo": "Nombra algo que NO se pueda tirar al contenedor amarillo",
    "fijar_mueble": "Nombra un objeto que se utilice para fijar un mueble a la pared",
    "festivos_ccaa": "Nombra un festivo de alguna comunidad autónoma",
    "videojuegos_20m": "Nombra un videojuego que haya vendido más de 20 millones de copias",
    "barbie_pelis": "Nombra una película de Barbie",
    "bruno_mars": "Nombra una canción de Bruno Mars",
    "gasolinera": "Nombra algo que hay en una gasolinera",
})
MANO.update({
"no_amarillo": {
 1: "vidrio=cristal=una botella de cristal=botella de cristal=botellas de cristal=tarro de cristal=bote de cristal=frasco de cristal, papel=periódico=papeles=revistas, "
    "cartón=cajas de cartón=una caja de cartón=caja de cartón, comida=restos de comida=orgánico=basura orgánica=cáscaras=peladuras=pieles de fruta, pilas=una pila=baterías",
 2: "juguetes=un juguete=juguete de plástico=un juguete de plástico, ropa=una camiseta=zapatos=calzado, aceite=aceite usado=aceite de cocina, pañales=un pañal, "
    "medicamentos=medicinas=pastillas, cepillo de dientes=un cepillo de dientes, bolígrafos=boli=un boli=bolígrafo, cubo de plástico=un cubo=palangana=barreño, "
    "perchas=una percha, colillas=una colilla=tabaco, servilletas=papel de cocina=pañuelos=clínex=kleenex=papel higiénico, bombillas=una bombilla, "
    "móvil=un móvil=aparatos electrónicos=electrónica=cargador=cables, táper=tuppers=tupper=un táper, mascarillas=mascarilla, vasos de cristal=vaso de cristal=platos=vajilla=un plato, "
    "espejo=un espejo, cerámica=porcelana=una taza, toallitas=toallitas húmedas, compresas=tampones, chicles=un chicle",
 3: "tubería=tuberías de PVC=PVC, mangueras=una manguera, sillas de plástico=una silla de plástico=muebles de plástico=mobiliario de jardín, "
    "maquinillas de afeitar=cuchillas=una cuchilla, mechero=mecheros, gafas=unas gafas, jeringuillas=jeringuilla=agujas, radiografías=una radiografía, "
    "termómetro=un termómetro, CD=cedés=DVD=discos, cintas de vídeo=casetes=cintas, carpetas de plástico=carpeta=fundas de plástico=funda, "
    "rotuladores=un rotulador=lápices, globos=un globo, tapones de corcho=corcho, madera=un trozo de madera, excrementos=caca=caca de perro=arena del gato, "
    "pelo=pelos, cenizas=ceniza, polvo de barrer=barreduras, esponjas de baño=una esponja de baño? no, cápsulas de café? no, bolsas de basura llenas, "
    "electrodomésticos=una tostadora=un secador, ordenador=portátil, tablet, colchón=un colchón, muebles=un mueble, escombros=restos de obra, "
    "pintura=botes de pintura, disolventes=productos tóxicos, insecticidas, bote de pintura, tierra=plantas=restos de poda, cartón de pizza=caja de pizza sucia=caja de pizza, "
    "papel de aluminio sucio=papel de plata sucio, envases de vidrio=perfumes de cristal=frasco de colonia",
 4: "juguetes con pilas, cubos de fregar=fregona=una fregona=escoba, cepillo del pelo=peine, palillos de los oídos=bastoncillos, hilo dental, lentillas, "
    "biberón=chupete=un chupete, guantes de látex=guantes de goma, preservativos=condón, gomas del pelo, cápsulas de detergente, ceras=plastilina, "
    "pinzas de la ropa, regla de plástico, macetas de plástico=maceta, tapón de bañera, cortinas de ducha=cortina de baño, sacos de cemento, bolsas de rafia, "
    "pajitas reutilizables, botellas de aceite de motor, envases de productos peligrosos, aerosoles llenos, zapatillas de casa, cinturón, bolsos=un bolso, "
    "paraguas=un paraguas, maletas=una maleta, flotador=colchoneta hinchable, piscina hinchable, neumáticos=ruedas, bicicleta, patinete, tetrabrik lleno? no",
},
"fijar_mueble": {
 1: "tornillo=tornillos, taco=tacos=taco de plástico=taco Fischer=Fischer, escuadra=escuadras=escuadra antivuelco, clavo=clavos, taladro=un taladro",
 2: "destornillador=atornillador, martillo, anclaje=anclajes=anclaje antivuelco=kit antivuelco=sistema antivuelco=correa antivuelco, alcayata=alcayatas, "
    "cuerda=cuerdas, cinta de doble cara=cinta adhesiva de doble cara=cinta americana, pegamento=cola=adhesivo, soporte=soportes=soporte de pared, "
    "bridas=brida, silicona, cáncamo=cáncamos, abrazadera, cadena=cadenita, llave Allen=llave hexagonal",
 3: "taco químico=anclaje químico, taco de expansión=tacos de expansión=taco metálico, taco Molly=Molly=taco basculante=taco de pladur=taco para pladur, "
    "tirafondo=tirafondos, perno=pernos, tuerca=tuercas, arandela=arandelas, placa de unión=placa=pletina, ángulo=angular=ángulo metálico, "
    "cable de acero=cable, correa=cinta antivuelco, gancho=ganchos, armella=armellas, hembrilla=hembrillas, nivel=nivel de burbuja, broca=brocas, "
    "atornillador eléctrico, llave inglesa, alicates, metro=cinta métrica, lápiz, No más clavos=Sin clavos=adhesivo de montaje, masilla, Pattex, "
    "velcro=tiras adhesivas=tiras Command=Command, sargento=sargentos, bisagra=bisagras, riel=raíl=carril, colgador=colgadores, "
    "herraje=herrajes, perfil en L=perfil",
 4: "pasador, remache=remaches, espárrago=varilla roscada, tornillo autorroscante=autorroscante, tornillo de cabeza hexagonal, tacos de nailon, "
    "taco de nylon, anclaje de cuña, perno de anclaje, taco de golpe, clavo de acero, punta=puntas, grapa=grapas=grapadora, escarpia=escarpias, "
    "listón=listones=rastrel, tablero, cuña=cuñas, regleta, colgador francés=French cleat, tornillo para madera, tornillo para metal, kit de fijación IKEA, "
    "cinta de anclaje, cable antivuelco, seguro antivuelco, fijación de seguridad infantil, soporte en U, guía, escuadra reforzada, junta, pasamuros, "
    "llave de vaso, carraca, buscador de vigas=detector de metales, aspirador de polvo, pistola de clavos",
},
"festivos_ccaa": {
 1: "Navidad=25 de diciembre, Año Nuevo=1 de enero, Reyes=Día de Reyes=6 de enero=Epifanía, Viernes Santo, Jueves Santo, Semana Santa, "
    "Día de Andalucía=28 de febrero=28F, Diada=Diada de Cataluña=Diada Nacional de Cataluña=11 de septiembre=Onze de Setembre, San José=19 de marzo, "
    "Día del Trabajador=1 de mayo=Día del Trabajo, Día de la Hispanidad=12 de octubre=Fiesta Nacional=Hispanidad=El Pilar=Virgen del Pilar, Todos los Santos=1 de noviembre, "
    "Día de la Constitución=Constitución=6 de diciembre, la Inmaculada=8 de diciembre=Inmaculada Concepción, la Asunción=15 de agosto=Virgen de agosto",
 2: "Día de la Comunidad de Madrid=2 de mayo=Dos de Mayo, Sant Joan=San Juan=24 de junio=Noche de San Juan, Lunes de Pascua=Pascua=Lunes de Pascua Florida, "
    "Santiago Apóstol=Santiago=25 de julio=Día de Galicia=Día Nacional de Galicia, Día de Canarias=30 de mayo, Día de la Comunitat Valenciana=9 de octubre=9 d'Octubre=Día de Valencia, "
    "San Jorge=Sant Jordi=23 de abril=Día de Aragón, Día de Castilla y León=Villalar=Día de Villalar, Día de Asturias=8 de septiembre=Día de la Santina=Virgen de Covadonga, "
    "Día de Extremadura=Virgen de Guadalupe, Día de las Illes Balears=Día de Baleares=1 de marzo, San Esteban=Sant Esteve=26 de diciembre, "
    "Día de las Letras Gallegas=Letras Gallegas=17 de mayo, Día de la Región de Murcia=Día de Murcia=9 de junio, Día de La Rioja=Día de la Rioja, "
    "Día de Castilla-La Mancha=31 de mayo, Día de Cantabria=Día de las Instituciones de Cantabria=28 de julio, San Francisco Javier=Día de Navarra=3 de diciembre, "
    "Día de Euskadi=Día del País Vasco=25 de octubre, Corpus Christi=Corpus",
 3: "La Bien Aparecida=Virgen de la Bien Aparecida=15 de septiembre, Día de Ceuta=2 de septiembre, Día de Melilla=17 de septiembre, "
    "Fiesta del Sacrificio=Fiesta del Cordero=Eid al Adha=Aid al Adha=Aid el Kebir, "
    "San Vicente Ferrer, Nuestra Señora de África=Virgen de África",
},
"gasolinera": {
 1: "surtidor=surtidores=el surtidor, gasolina=gasolina 95=gasolina 98=sin plomo, diésel=gasóleo=gasoil, manguera=mangueras=la manguera, tienda=la tienda=tiendita, "
    "caja=el cajero=cajero=cajera=dependiente=el que cobra, aire=aire para las ruedas=el aire, agua, lavadero=túnel de lavado=lavacoches=autolavado=lavado de coches",
 2: "compresor=compresor de aire=el compresor de las ruedas=máquina del aire=inflador, aspirador=aspiradora=aspirador del coche, baño=servicio=aseo=lavabo=WC, "
    "boxes=pistola de lavado=lavado a presión, coches=coche, camiones=camión, marquesina=tejadillo, cartel de precios=precios=panel de precios=el cartel de los precios, "
    "chucherías=chuches=gominolas, snacks=patatas=bolsas de patatas, bebidas=refrescos=agua embotellada, sándwiches=bocadillos, café=máquina de café, "
    "periódicos=revistas, hielo=bolsas de hielo, bombonas de butano=butano=bombona, aceite de motor=aceite, líquido limpiaparabrisas=limpiaparabrisas, "
    "papel para limpiarse las manos=papel=guantes=guantes de plástico, cubo de basura=papelera, cámaras=cámaras de seguridad, extintor=extintores, "
    "tarjetas=TPV=datáfono, cargador eléctrico=punto de recarga=cargadores para coches eléctricos=electrolinera, AdBlue",
 3: "anticongelante, mapas=mapas de carreteras, gafas de sol, CDs de música=cedés, juguetes, pilas, cargadores de móvil=cables, flores=ramos de flores, "
    "lotería=quiniela, tabaco=máquina de tabaco=cigarrillos, cartel de no fumar=prohibido fumar, señal de apagar el motor=prohibido usar el móvil, "
    "rasqueta del hielo=rasqueta, ambientador=ambientadores=Arbre Magique=pino, carbón=leña, cubetas de agua=regadera, depósito=depósitos subterráneos, "
    "isla=isla de surtidores, bayeta=esponja=escobilla para los cristales=limpiacristales, tarjeta de fidelización=tarjeta de puntos=Club Repsol, "
    "cola=colas, ladrones=atracos, perros, camioneros=transportistas, gente comiendo bocadillos, mesas, máquina expendedora=máquinas expendedoras, "
    "cajero automático, buzón de correos, paquetería=punto de recogida, chicles, preservativos=condones, aspirina=paracetamol, cadenas de nieve=cadenas, "
    "triángulos de emergencia=chaleco reflectante, escobillas=bombillas de coche, café de máquina, hot dogs=perritos calientes, bocata, cruasanes=bollería, "
    "bollos=Donuts, revistas porno, ruedas=neumáticos, gato hidráulico=gato, logo=letrero=rótulo, olor a gasolina=olor, manchas de aceite",
 4: "tapa del depósito=boca de carga, contador de litros=pantalla del surtidor, boquerel=pistola del surtidor=pistola, tubo de respiradero, separador de hidrocarburos, "
    "rejilla de desagüe, arquetas, sistema de recuperación de vapores, interfono, botón de emergencia=seta de emergencia=parada de emergencia, "
    "tanque de GLP=autogas=GLP, surtidor de gas natural=GNC, hidrógeno=hidrolinera, manómetro, tarifa de aire, vale de lavado, ficha de lavado=fichas, "
    "cera=abrillantador, rodillos=cepillos del túnel, secador del túnel, máquina de cambio=cambio de monedas, apertura nocturna=ventanilla nocturna, "
    "cajón de arena=arena absorbente, sepiolita, cubo de arena, carteles de ofertas, cupones de descuento, cristal blindado, baliza V-16=baliza, "
    "kit de pinchazos=kit antipinchazos, bidón=bidones=garrafa, embudo, escoba",
},
})
TAQUILLERAS.update({})

# Partes del cuerpo por debajo de la cintura: la lista de Norah viene en inglés con sus puntos (fuentes/t7/cintura_norah.csv).
# Aquí, el español de las de +10, +30, +60 y +100 (las de +85 se quedan en inglés, con su nombre técnico), con las formas de la calle.
CINTURA_ES = {
 "Ankle": "tobillo=tobillos", "Buttocks": "culo=nalgas=nalga=trasero=glúteos=glúteo=pompis=culete=posaderas=cachas=pandero=cachete", "Foot": "pie=pies",
 "Knee": "rodilla=rodillas", "Leg": "pierna=piernas", "Toe": "dedo del pie=dedos del pie=dedo",
 "Achilles tendon": "tendón de Aquiles=Aquiles", "Anterior cruciate ligament": "ligamento cruzado anterior=cruzado anterior=ligamento cruzado",
 "Anus": "ano=ojete=agujero del culo", "Appendix": "apéndice", "Arch": "arco del pie=puente del pie", "Ball of the foot": "almohadilla del pie=bola del pie",
 "Big toe": "dedo gordo=dedo gordo del pie", "Big toenail": "uña del dedo gordo", "Bladder": "vejiga", "Calf": "gemelo=gemelos=pantorrilla=pantorrillas",
 "Clitorisyou": "clítoris=clitoris", "Coccyx": "coxis=rabadilla=cóccix", "Crotch": "entrepierna", "Fallopian tubes": "trompas de Falopio=trompas",
 "Femur": "fémur", "Fibula": "peroné", "Fourth toe": "cuarto dedo del pie", "Fourth toenail": "uña del cuarto dedo del pie",
 "Genitals": "genitales=partes íntimas=partes", "Gluteal muscles": "músculos glúteos", "Gluteus maximus": "glúteo mayor=glúteo máximo",
 "Groin": "ingle=ingles", "Hamstrings": "isquiotibiales=isquios", "Heel": "talón=talones", "Hip": "cadera=caderas",
 "Interphalangeal joints of the foot": "articulaciones interfalángicas del pie", "Intestines": "intestinos=intestino=tripas", "Kneecap": "rótula=rótulas",
 "Large intestine": "intestino grueso=colon", "Little toe": "dedo meñique del pie=dedo pequeño del pie=meñique del pie", "Meniscus": "menisco=meniscos",
 "Metatarsals": "metatarsianos=metatarso", "Middle toenail": "uña del dedo corazón del pie", "Ovaries": "ovarios=ovario", "Pelvis": "pelvis",
 "Penis": "pene=pito=pilila=polla=picha=minga=cola=colita=chorra=nabo", "Pinky toenail": "uña del meñique del pie", "Quadriceps": "cuádriceps",
 "Rectum": "recto", "Scrotum": "escroto", "Second toe": "segundo dedo del pie", "Second toenail": "uña del segundo dedo del pie", "Shin": "espinilla=espinillas",
 "Small intestine": "intestino delgado", "Sole": "planta del pie=planta=plantas de los pies", "Testicles": "testículos=huevos=pelotas=cojones=testículo",
 "Thigh": "muslo=muslos", "Third toe": "tercer dedo del pie", "Tibia": "tibia", "Toenail": "uña del pie=uñas de los pies=uña", "Urethra": "uretra",
 "Uterus": "útero=matriz", "Vagina": "vagina=chocho=coño=chichi=chumino=almeja=potorro",
 "Acetabulum": "acetábulo", "Adductors": "aductores=aductor", "Anal canal": "canal anal", "Anal glands": "glándulas anales",
 "Anal sphincters": "esfínter anal=esfínteres anales=esfínter", "Ankle ligaments": "ligamentos del tobillo",
 "Anterior talofibular ligament": "ligamento peroneoastragalino anterior", "Back of the ankle": "parte de atrás del tobillo",
 "Back of the thigh": "parte de atrás del muslo", "Biceps femoris": "bíceps femoral", "Bulbourethral glands": "glándulas bulbouretrales=glándulas de Cowper",
 "Butt crack": "raja del culo=hucha=la raja", "Calcaneus": "calcáneo", "Cecum": "ciego", "Cervix": "cuello del útero=cérvix",
 "Clitoral hood": "capuchón del clítoris", "Coccygeal region": "región coccígea", "Collateral ligaments of knee": "ligamentos colaterales de la rodilla",
 "Common fibular nerve": "nervio peroneo común", "Cruciate ligaments": "ligamentos cruzados", "Cuboid": "cuboides", "Cuneiform bones": "cuneiformes=huesos cuneiformes",
 "Dimples of Venus": "hoyuelos de Venus", "Distal phalanges of the foot": "falanges distales del pie", "Dorsalis pedis artery": "arteria pedia=arteria dorsal del pie",
 "Endometrium": "endometrio", "Epididymis": "epidídimo", "External urethral orifice": "meato urinario=meato", "Femoral artery": "arteria femoral=femoral",
 "Femoral vein": "vena femoral", "Fifth metatarsal": "quinto metatarsiano", "First metatarsophalangeal joint": "articulación del dedo gordo",
 "Foot arteries": "arterias del pie", "Foot bones": "huesos del pie", "Foot muscles": "músculos del pie", "Foot nerves": "nervios del pie",
 "Foot veins": "venas del pie", "Forefoot": "antepié", "Foreskin": "prepucio", "Fourth metatarsal": "cuarto metatarsiano", "Frenulum of penis": "frenillo=frenillo del pene",
 "Front of the ankle": "parte delantera del tobillo", "Front of the knee": "parte delantera de la rodilla", "Front of the thigh": "parte delantera del muslo",
 "Gastrocnemius": "gastrocnemio", "Glans penis": "glande", "Gluteus medius": "glúteo medio", "Gluteus minimus": "glúteo menor", "Gonads": "gónadas",
 "Great saphenous vein": "vena safena=safena", "Happy trail": "caminito de la felicidad", "Haunches": "ancas=cuartos traseros", "Heel pad": "almohadilla del talón",
 "Hindfoot": "retropié", "Hip abductors": "abductores=abductores de la cadera", "Hip bone": "hueso de la cadera=hueso coxal=coxal=hueso ilíaco",
 "Hip flexors": "flexores de la cadera", "Hip joint": "articulación de la cadera", "Hip ligaments": "ligamentos de la cadera", "Hip muscles": "músculos de la cadera",
 "Hymen": "himen", "Ileum": "íleon", "Iliac crest": "cresta ilíaca", "Iliopsoas": "iliopsoas=psoasilíaco", "Iliotibial band": "cintilla iliotibial=banda iliotibial",
 "Ilium": "ilion=ilíaco", "Inner ankle": "parte interna del tobillo", "Inner knee": "parte interna de la rodilla", "Inner thigh": "cara interna del muslo=parte interna del muslo",
 "Instep": "empeine=empeines", "Ischium": "isquion", "Knee ligaments": "ligamentos de la rodilla", "Labia": "labios vaginales", "Labia majora": "labios mayores",
 "Labia minora": "labios menores", "Lap": "regazo", "Lateral collateral ligament": "ligamento lateral externo=ligamento colateral lateral",
 "Lateral malleolus": "maléolo externo=maléolo lateral", "Lateral meniscus": "menisco externo", "Leg arteries": "arterias de la pierna", "Leg bones": "huesos de la pierna",
 "Leg hair": "pelo de las piernas=vello de las piernas", "Leg joints": "articulaciones de la pierna", "Leg muscles": "músculos de la pierna",
 "Leg nerves": "nervios de la pierna", "Leg veins": "venas de la pierna", "Lower abdomen": "bajo vientre=parte baja del abdomen=hipogastrio",
 "Lower back": "zona lumbar=lumbares=riñones", "Lower back muscles": "músculos lumbares", "Lower leg": "parte baja de la pierna", "Lower leg bones": "huesos de la parte baja de la pierna",
 "Male genitalia": "genitales masculinos=paquete", "Malleolus": "maléolo", "Medial collateral ligament": "ligamento lateral interno=ligamento colateral medial",
 "Medial malleolus": "maléolo interno=maléolo medial", "Medial meniscus": "menisco interno", "Metatarsophalangeal joints": "articulaciones metatarsofalángicas",
 "Midfoot": "mediopié", "Mons pubis": "monte de Venus", "Navicular bone": "escafoides del pie=navicular=escafoides", "Outer ankle": "parte externa del tobillo",
 "Outer knee": "parte externa de la rodilla", "Outer thigh": "parte externa del muslo", "Patellar ligament": "tendón rotuliano=ligamento rotuliano",
 "Pelvic cavity": "cavidad pélvica", "Pelvic floor": "suelo pélvico", "Perineum": "perineo=periné", "Phalanges of the foot": "falanges del pie=falanges",
 "Piriformis": "piramidal=piriforme", "Plantar fascia": "fascia plantar", "Popliteal artery": "arteria poplítea", "Popliteal fossa": "corva=hueco poplíteo=fosa poplítea",
 "Posterior cruciate ligament": "ligamento cruzado posterior", "Prostate": "próstata", "Psoas": "psoas", "Pubic area": "zona púbica",
 "Pubic hair": "vello púbico=pelo púbico", "Pubic symphysis": "sínfisis del pubis", "Pubis": "pubis", "Quadriceps tendon": "tendón del cuádriceps",
 "Rectus femoris": "recto femoral=recto anterior", "Sacral dimples": "hoyuelos sacros", "Sacroiliac joint": "articulación sacroilíaca", "Sacrum": "sacro=hueso sacro",
 "Sartorius": "sartorio", "Sciatic nerve": "nervio ciático=ciático", "Second metatarsal": "segundo metatarsiano", "Seminal vesicles": "vesículas seminales",
 "Seminiferous tubules": "túbulos seminíferos", "Sesamoid bones of the foot": "sesamoideos=huesos sesamoideos", "Shaft of penis": "tronco del pene",
 "Soleus": "sóleo", "Talus": "astrágalo", "Tarsals": "tarso=huesos del tarso", "Third metatarsal": "tercer metatarsiano", "Tibialis anterior": "tibial anterior",
 "Tibialis posterior": "tibial posterior", "Toe crease": "pliegue del dedo del pie", "Toe hair": "pelo de los dedos del pie", "Toe pad": "yema del dedo del pie",
 "Toe tendons": "tendones de los dedos del pie", "Toe web": "piel entre los dedos del pie", "Toenail bed": "lecho ungueal del pie", "Toenail cuticle": "cutícula del pie",
 "Top of the foot": "dorso del pie", "Upper thigh": "parte alta del muslo", "Ureter": "uréter=uréteres", "Vaginal opening": "entrada de la vagina=orificio vaginal",
 "Vas deferens": "conductos deferentes=conducto deferente", "Vastus medialis": "vasto interno=vasto medial", "Vulva": "vulva",
 "Fabella": "fabela",
}
# lo de +85 que alguien en español sí puede escribir
CINTURA_MAS = {4: "vasto externo=vasto lateral, vasto intermedio, aductor mayor, aductor largo, aductor corto, recto interno=grácil, semitendinoso, semimembranoso, "
                   "tensor de la fascia lata, pectíneo, poplíteo, peroneo largo, peroneo corto, flexor del dedo gordo, extensor de los dedos, "
                   "nervio femoral, nervio tibial, nervio obturador, nervio pudendo, vena safena menor, arteria ilíaca, vena ilíaca, ganglios inguinales, "
                   "trocánter=trocánter mayor, cuello del fémur, cabeza del fémur, cóndilos, meseta tibial, colon sigmoide=sigma, colon descendente, "
                   "glándulas de Bartolino=Bartolino, glándulas de Skene, punto G, cordón espermático, cuerpos cavernosos, cuerpo esponjoso, labrum, fascia lata, "
                   "canal inguinal, ligamento inguinal, cola de caballo, coxis, vértebras lumbares, L5, sacro"}

MANO.update({
"videojuegos_20m": {   # los 51 de la lista de Wikipedia (todos pasan de 25 millones) y los que se sabe que pasan de 20
 1: "Minecraft, Tetris, Grand Theft Auto V=GTA V=GTA 5=GTA=Grand Theft Auto, Mario Kart 8=Mario Kart 8 Deluxe=Mario Kart, Wii Sports, "
    "Los Sims=The Sims=Sims, Super Mario Bros.=Super Mario Bros=Super Mario=Mario Bros=Mario, Pokémon Rojo=Pokémon Azul=Pokémon Amarillo=Pokémon Rojo y Azul=Pokémon",
 2: "Red Dead Redemption 2=RDR2=Red Dead 2, Animal Crossing: New Horizons=Animal Crossing, The Legend of Zelda: Breath of the Wild=Breath of the Wild=Zelda Breath of the Wild=Zelda, "
    "Super Smash Bros. Ultimate=Smash Bros=Super Smash Bros, Mario Kart Wii, Wii Fit, Call of Duty: Modern Warfare=Modern Warfare=Call of Duty=COD, "
    "The Elder Scrolls V: Skyrim=Skyrim, The Witcher 3=The Witcher 3: Wild Hunt=The Witcher, Grand Theft Auto: San Andreas=GTA San Andreas=San Andreas, "
    "Sonic the Hedgehog=Sonic, Stardew Valley, Terraria, PUBG=PUBG: Battlegrounds=PlayerUnknown's Battlegrounds, Overwatch, Cyberpunk 2077=Cyberpunk, "
    "Hogwarts Legacy, Super Mario Odyssey, New Super Mario Bros., New Super Mario Bros. Wii, Wii Sports Resort, Wii Play, Elden Ring, Duck Hunt, It Takes Two",
 3: "Human: Fall Flat=Human Fall Flat, Call of Duty: Black Ops III=Black Ops 3, Call of Duty: Black Ops Cold War=Black Ops Cold War, Call of Duty: Black Ops=Black Ops, "
    "Call of Duty: Modern Warfare 3=Modern Warfare 3, Payday 2, Fallout 4, Borderlands 2, Monster Hunter: World=Monster Hunter World=Monster Hunter, "
    "Pokémon Oro=Pokémon Plata=Pokémon Oro y Plata, Pokémon Escarlata=Pokémon Púrpura=Pokémon Escarlata y Púrpura, Pokémon Espada=Pokémon Escudo=Pokémon Espada y Escudo, "
    "Pokémon Sol=Pokémon Luna=Pokémon Sol y Luna, Pokémon Diamante=Pokémon Perla=Pokémon Diamante y Perla, Grand Theft Auto IV=GTA IV=GTA 4, Phasmophobia, "
    "Black Myth: Wukong=Wukong, Garry's Mod, Mario Kart DS, Nintendogs, Wii Fit Plus, Super Mario World, Kinect Adventures, Diablo III=Diablo 3, "
    "Red Dead Redemption, God of War=God of War 2018, Marvel's Spider-Man=Spider-Man de PS4",
},
"barbie_pelis": {
 1: "Barbie=Barbie (2023)=la película de Barbie=Barbie de Greta Gerwig, Barbie en el Cascanueces=Barbie y el Cascanueces=Barbie in the Nutcracker, "
    "Barbie como Rapunzel=Barbie Rapunzel=Barbie as Rapunzel, Barbie y el lago de los cisnes=Barbie en el lago de los cisnes=Barbie of Swan Lake, "
    "Barbie en la princesa y la costurera=Barbie la princesa y la costurera=Barbie as the Princess and the Pauper=La princesa y la costurera, "
    "Barbie y las 12 princesas bailarinas=Barbie en las 12 princesas bailarinas=Las 12 princesas bailarinas=Barbie in the 12 Dancing Princesses",
 2: "Barbie Fairytopia=Fairytopia, Barbie y la magia de Pegaso=La magia de Pegaso=Barbie and the Magic of Pegasus, Barbie en la princesa de la isla=Barbie la princesa de la isla=Barbie as the Island Princess, "
    "Barbie Mariposa, Barbie y el castillo de diamantes=Barbie y el castillo de diamante=Barbie & the Diamond Castle, Barbie y las tres mosqueteras=Las tres mosqueteras, "
    "Barbie en una aventura de sirenas=Barbie sirena=Barbie in a Mermaid Tale, Barbie: Moda mágica en París=Moda mágica en París=Barbie A Fashion Fairytale, "
    "Barbie: Escuela de princesas=Escuela de princesas=Princess Charm School, Barbie: El secreto de las hadas=Barbie A Fairy Secret, "
    "Barbie: La princesa y la estrella del pop=Barbie princesa y estrella del pop=The Princess & the Popstar, Barbie en un cuento de Navidad=Barbie in a Christmas Carol",
 3: "Barbie Fairytopia: Mermaidia=Mermaidia, Barbie Fairytopia: La magia del arcoíris=La magia del arcoíris, Barbie presenta Pulgarcita=Barbie Pulgarcita=Pulgarcita=Thumbelina, "
    "Barbie en una aventura de sirenas 2=Barbie in a Mermaid Tale 2, Barbie: Una Navidad perfecta=Barbie A Perfect Christmas, Barbie: Mariposa y la princesa de las hadas=Mariposa and the Fairy Princess, "
    "Barbie y sus hermanas en una historia de ponis=Barbie y sus hermanas: Una historia de caballos=Barbie & Her Sisters in A Pony Tale, Barbie en las zapatillas mágicas=Barbie en las zapatillas rosas=Barbie in the Pink Shoes, "
    "Barbie: La princesa de las perlas=Barbie la princesa perla=The Pearl Princess, Barbie y la puerta secreta=Barbie and the Secret Door, Barbie: Super Princesa=Barbie Princess Power, "
    "Barbie: Rock 'n Royals=Rock and Royals, Barbie y sus hermanas: La gran aventura de los perritos=Barbie & Her Sisters in the Great Puppy Adventure, "
    "Barbie: Agentes secretas=Barbie Spy Squad, Barbie: Aventura en las estrellas=Barbie Star Light Adventure, Barbie y sus hermanas: Rescate de cachorros=Barbie & Her Sisters in A Puppy Chase, "
    "Barbie: Héroe de videojuego=Barbie Video Game Hero, Barbie Dreamtopia, Barbie: Magia de delfines=Barbie Dolphin Magic",
 4: "Barbie: Aventura de princesas=Barbie Princess Adventure, Barbie: Gran ciudad grandes sueños=Barbie Big City Big Dreams, Barbie y Chelsea: El cumpleaños perdido=Barbie & Chelsea The Lost Birthday, "
    "Barbie: El poder de las sirenas=Barbie Mermaid Power, Barbie: Un viaje épico=Barbie Epic Road Trip, Barbie: Skipper y la gran aventura de canguro=Barbie Skipper and the Big Babysitting Adventure, "
    "Barbie y Stacie al rescate=Barbie and Stacie to the Rescue, Barbie: Juntas=Barbie It Takes Two, Barbie y Teresa: Receta para la amistad=Barbie & Teresa Recipe for Friendship",
 5: "Barbie and the Rockers: Out of This World=Barbie y las Rockers, Barbie and the Sensations: Rockin' Back to Earth=Barbie y las Sensations",
},
"bruno_mars": {
 1: "Uptown Funk, Just the Way You Are, Grenade, Locked Out of Heaven, When I Was Your Man, That's What I Like, 24K Magic, Die With a Smile, APT.=APT=Apartment, "
    "Talking to the Moon, The Lazy Song=Lazy Song, Marry You, Count On Me, Leave the Door Open",
 2: "Treasure, Versace on the Floor, Finesse, Nothin' on You=Nothing on You, Billionaire, It Will Rain, Young Girls, Runaway Baby, Gorilla, Lighters, "
    "Young Wild & Free=Young Wild and Free, Calling All My Lovelies, Chunky, Smokin Out the Window=Smoking Out the Window, Too Good to Say Goodbye, I Just Might",
 3: "Our First Time, Liquor Store Blues, The Other Side, Somewhere in Brooklyn, Moonshine, Natalie, Show Me, Money Make Her Smile, If I Knew, "
    "Perm, Straight Up & Down=Straight Up and Down, Skate, After Last Night, Put On a Smile, 777, Fly as Me, Blast Off, Silk Sonic Intro, Love's Train, "
    "Bubble Butt, Mirror, Please Me, Wake Up in the Sky, Blow, Fat Juicy & Wet, Risk It All, Cha Cha Cha, God Was Showing Off, Dance with Me, Something Serious, "
    "Why You Wanna Fight?, On My Soul, Nothing Left, Welcome Back, Old & Crazy, 3D, Bonde do Brunão, Come to Brazil, Can't Come Back to Me, This Is My Love, Love",
},
})

# ── miércoles 11 ──
PREGUNTAS.update({
    "funciona_pilas": "Nombra algo que funcione con pilas",
    "animal_rayas": "Nombra un animal con rayas",
    "comida_relleno": "Nombra una comida que lleve relleno",
    "peluqueria": "Nombra algo que hay en una peluquería",
    "patata_formas": "Nombra una forma de cocinar la patata",
    "personaje_gafas": "Nombra un personaje de ficción que lleve gafas",
})
MANO.update({
"funciona_pilas": {
 1: "mando de la tele=mando=mando a distancia=el mando, reloj=reloj de pared=despertador, linterna, juguetes=juguete=coche teledirigido, calculadora, "
    "báscula=peso, mando de la consola=mando de la Play=mando de la Xbox=mando de la Wii, ratón=ratón inalámbrico",
 2: "teclado inalámbrico=teclado, radio=transistor, detector de humo=detector de humos, cepillo de dientes eléctrico=cepillo eléctrico, termómetro, "
    "audífono=audífonos, cámara de fotos=cámara, maquinilla de afeitar=afeitadora, Game Boy=Tamagotchi, luces de Navidad=guirnalda de luces=velas LED, "
    "mando del garaje=mando de la puerta del garaje, llave del coche=mando del coche, tensiómetro, glucómetro, ambientador automático=ambientador, "
    "sacacorchos eléctrico, molinillo de pimienta eléctrico, timbre inalámbrico=timbre, walkie-talkie=walkie, frontal=linterna frontal, "
    "muñeca=muñeco=Furby=peluche que habla, cuentakilómetros de bici=luz de bici=luces de bicicleta, marcapasos, mando del aire acondicionado, discman=walkman",
 3: "metrónomo, afinador de guitarra=afinador, puntero láser=láser, sensor de movimiento, cerradura electrónica, candado electrónico, mirilla digital, "
    "báscula de cocina, termómetro de cocina, temporizador de cocina, encendedor eléctrico, matamosquitos eléctrico=raqueta matamosquitos, "
    "antimosquitos portátil, repelente de mosquitos, saltamontes de juguete, pistola de agua eléctrica, burbujas=pistola de pompas, "
    "lupa con luz, nivel láser, multímetro=polímetro, detector de metales, detector de billetes falsos, termostato, estación meteorológica, "
    "marco de fotos digital, vela de LED, farolillo=farol, espejo con luz, depiladora=depiladora eléctrica, perfilador de cejas, rizador de pestañas, "
    "cortapelos=cortadora de pelo=maquinilla de cortar el pelo, quitapelusas=quitapelusas eléctrico, sacapuntas eléctrico, borrador eléctrico, "
    "cámara de caza, prismáticos digitales, GPS de mano, podómetro, pulsómetro, reloj de pulsera=reloj digital, pulsera de actividad, móvil antiguo, "
    "dispensador de jabón automático, cepillo de limpieza eléctrico, tiradores de luz, piano de juguete, teclado de juguete, coche de Scalextric? no, "
    "dron de juguete, robot=robot de juguete, peonza de luz, varita mágica de juguete, espada láser de juguete=sable láser, Tamagochi, "
    "lector de libros electrónico? no, micrófono inalámbrico=micrófono, auriculares antiguos, mando de la calefacción, alarma=alarma de coche=alarma de casa",
 4: "contador de monedas, etiquetadora, balanza de joyero, colorímetro, luxómetro, detector de gas, detector de monóxido=detector de CO, "
    "cámara espía, mira telescópica, señuelo de pesca, picador de pesca=alarma de pesca, comedero automático, fuente para gatos, collar de perro con luz, "
    "collar antiladridos, localizador=AirTag, mando universal, pulsador de emergencia=botón de teleasistencia, termómetro de oído, aspirador nasal eléctrico, "
    "sacaleches, vigilabebés=intercomunicador de bebé, móvil de cuna=móvil para la cuna, hamaca de bebé, columpio de bebé, chupete con luz, "
    "zapatillas con luces, pulsera luminosa, gafas de visión nocturna, gafas de realidad virtual? no, mando del proyector, puntero de presentación, "
    "medidor láser, cinta métrica digital, sensor de puerta, sensor de agua, regadera automática=programador de riego, mosquitera eléctrica, "
    "farolillo solar? no, adorno de Navidad musical, tarjeta de felicitación musical=tarjeta musical, globo terráqueo con luz, flexo portátil",
},
"animal_rayas": {
 1: "cebra=cebras, tigre=tigres, abeja=abejas, avispa=avispas, mofeta=zorrillo",
 2: "pez payaso=Nemo, mapache, ardilla listada=ardilla rayada=chipmunk=ardilla, okapi, tejón, serpiente coral=coral, lémur=lémur de cola anillada=lemur, "
    "jabalí=rayón=jabato, gato atigrado=gato=atigrado, pez cebra, tiburón tigre, bongo, kudú, ñu, hiena rayada=hiena, oruga=orugas, escarabajo de la patata",
 3: "pez león, pez cirujano=pez cirujano azul, pez ángel, mosquito tigre, tenrec rayado, pez cebra, serpiente rey, serpiente de cascabel=serpiente, "
    "abejorro, sírfido, chinche, culebra de escalera, salamandra, tritón, ranita=rana flecha, tilapia, perca, barbo tigre, lubina rayada=lubina, "
    "pez gato rayado, cebra de Grevy, quagga, tigre de Bengala, tigre siberiano=tigre de Siberia, gato montés, ocelote, tilacino=tigre de Tasmania, "
    "numbat, nyala, sitatunga, antílope bongo, cálao? no, colibrí? no, pez piedra? no, araña tigre=araña avispa=Argiope, gorrión? no, "
    "coatí, zorro? no, osito lavador, lince? no, garduña? no, tortuga pintada, iguana, gecko=geco leopardo, gusano de seda, mariposa cebra, chinche rayada, "
    "pez rayado, sargo, mojarra, besugo? no, morena cebra, anguila listada, tiburón cebra, tiburón ballena? no, pez ballesta, pez mandarín",
 4: "suricato, mangosta rayada, mangosta, zorrillo manchado, hurón de patas negras? no, cerdo hormiguero? no, agutí? no, tejón melero, "
    "tenrec, ardilla terrestre, ardilla de 13 rayas, pájaro carpintero? no, zebú? no, cebroide=cebrasno=zorse, okapi, duiquero cebra, "
    "camaleón? no, culebra de collar, víbora? no, eslizón, lagartija colilarga, salamanquesa, gallipato, tritón jaspeado, sapo partero? no, "
    "langostino tigre, gamba tigre=langostino tigre, camarón arlequín, nudibranquio, sepia? no, pulpo de anillos azules=pulpo de anillos, "
    "chinche del pino, escarabajo avispa, mosca cernidora, abeja carpintera? no, tábano? no, saltamontes? no, cucaracha? no, "
    "codorniz? no, alcaudón? no, abubilla, picogordo? no, faisán? no, gallo? no, pato mandarín? no",
},
"comida_relleno": {
 1: "croqueta=croquetas, empanada=empanadas, empanadilla=empanadillas, pimientos rellenos=pimientos del piquillo rellenos=pimientos, canelones, raviolis=ravioli, "
    "lasaña, tortilla de patatas rellena, donut relleno=donuts rellenos=donut=donuts, berlina=bola de Berlín, burrito=burritos, sándwich=bocadillo=sandwich, "
    "huevos rellenos=huevos rellenos de atún, croissant relleno=croissant=cruasán=cruasán de chocolate=napolitana=napolitana de chocolate, pavo relleno, calabacín relleno",
 2: "berenjena rellena=berenjenas rellenas, tomates rellenos, champiñones rellenos, aceitunas rellenas=aceitunas rellenas de anchoa, mejillones rellenos=tigres, "
    "calamares rellenos, pollo relleno, cachopo, flamenquín, san jacobo=sanjacobo, rollitos de primavera=rollito de primavera, gyozas=gyoza=dumplings, "
    "tacos, quesadilla=quesadillas, enchiladas, fajitas, arepas=arepa, pasteles de carne=pastel de carne, bombones rellenos=bombón=bombones, Kinder Bueno, "
    "Phoskitos, Bollycao, Donettes rellenos, Filipinos? no, profiteroles=profiterol, lionesas, petisú, palmera rellena, caña de crema=cañas rellenas, "
    "rosquillas rellenas, buñuelos de viento=buñuelos, churros rellenos, gofre relleno, crepes=crepe=crep, tortitas rellenas, tarta? no, "
    "pizza calzone=calzone, pizza con borde relleno=borde relleno, panzerotti, piadina, wrap=wraps, kebab=durum, pita=pan de pita, hamburguesa, "
    "perrito caliente=hot dog, sushi=maki, onigiri, tamal=tamales, pupusas, samosa=samosas, pastel de cabello de ángel, ensaimada rellena",
 3: "pimientos de Padrón rellenos? no, piquillos rellenos de bacalao, alcachofas rellenas, cebollas rellenas, patatas rellenas, patatas asadas rellenas, "
    "aguacate relleno, sepia rellena, chipirones rellenos=chipirones en su tinta? no, cangrejo relleno=txangurro, centollo relleno, vieiras rellenas, "
    "lomo relleno, solomillo relleno=solomillo Wellington=Wellington, cordero relleno, pechuga rellena=pechugas rellenas, rollo de carne, carne mechada, "
    "muslos rellenos, codornices rellenas, capón relleno, pularda rellena, morcilla? no, butifarra? no, chorizo? no, rabioles, tortellini, cappelletti, "
    "agnolotti, pasta rellena, conchiglioni rellenos, cannoli, crepes salados, galette, tortilla rellena, flautas, chimichanga, empanada gallega, "
    "empanada argentina, hornazo, bollo preñao=bollos preñaos, pan preñado, pastel de Murcia, coca rellena, panecillos rellenos, brioche relleno, "
    "bombas de patata=bomba, bolitas de queso, nuggets? no, croquetas de jamón, pastelitos, bartolillos, pestiños? no, casadielles, carbayones, "
    "pastel ruso? no, milhojas, petit choux, eclair=éclair=pepito de crema, suizo relleno, trufas? no, dátiles rellenos, ciruelas rellenas, "
    "huevo Kinder=Kinder Sorpresa, Lacasitos? no, bombón de licor, galletas rellenas=Oreo, Príncipe=galleta Príncipe, Tosta Rica? no, Dinosaurus? no",
 4: "dolmas=hojas de parra rellenas, kibbeh=kebbe, börek=burek, pierogi, pelmeni, varenyky, manti, khinkali, momos, bao=baozi, xiaolongbao, "
    "wontons=wonton, pastel de choclo? no, papas rellenas, chiles en nogada, chiles rellenos, gorditas, tlacoyos, empanadas de vigilia, "
    "tequeños, cachapa, pastel de nata=pastel de Belém? no, bolinhos de bacalhau? no, coxinha, esfiha, pastéis, rissóis, croquete, "
    "arancini=arancino, supplì, cannelloni, ravioles, mezzelune, culurgiones, scarpinocc, casoncelli, pansotti, focaccia rellena, "
    "stromboli, strudel, apfelstrudel, kolache, pączki, sufganiyot, malasadas, bombolone, krapfen, cronut? no, pastel de crema, "
    "brazo de gitano, pionono, rollo de canela? no, tronco de Navidad, roscón de Reyes relleno=roscón relleno, panettone relleno, "
    "tortel relleno, xuixo, bunyols de crema, fartons? no, tocinillo? no, cuerno de crema, piononos rellenos, mantecado? no, "
    "pato a la naranja? no, pavo de Acción de Gracias, cochinillo? no, haggis, turducken, ballotine, galantina, roulade, paupiette, cordon bleu, "
    "pollo Kiev, schnitzel relleno, beef Wellington, cabeza de ternera? no, tripas rellenas, rellenos de Navidad, empedrat? no, matambre",
},
"peluqueria": {
 1: "tijeras, secador=secadores, peine=peines, cepillo=cepillos, espejo=espejos, sillón=sillones=silla, champú, peluquero=peluquera=peluqueros, "
    "lavacabezas=lavabo=pila, plancha=planchas del pelo, tinte=tintes",
 2: "laca, gomina=gel, cera=cera para el pelo, mascarilla, acondicionador, maquinilla=máquina de cortar el pelo=cortapelos=maquinilla de afeitar, "
    "navaja, toallas=toalla, capa=bata=delantal, pinzas=pinzas del pelo=horquillas, rulos, tenacillas=rizador, revistas=revista, pelos en el suelo=pelo=pelos, "
    "escoba, caja=mostrador=recepción, clientes=cliente, cotilleos=cotilleo, radio=música, mechas, papel de plata=papel de aluminio, brocha=brocha de tinte, "
    "cuenco del tinte=bol, guantes, espuma, pulverizador=difusor de agua, lista de precios=precios, sala de espera=sofá, café",
 3: "secador de casco=casco, vaporizador, carrito=carrito auxiliar, lavadora, cuchillas, brocha de afeitar, espuma de afeitar, aftershave, colonia, "
    "polvos de talco=talco, cepillo para quitar pelos, difusor, cepillo redondo, cepillo térmico, peine de púas, peine de cola, peine de corte, "
    "pinzas de cocodrilo, cintas=diademas, gorro de ducha=gorro, gorro de mechas, decolorante, oxigenada=agua oxigenada, keratina, botox capilar, "
    "permanente, alisado, extensiones, pelucas=peluca, postizos, catálogo de peinados=fotos de peinados, cuadros, cartel de horario, "
    "productos en venta=estantería de productos, ampollas, sérum, aceite de argán, champú seco, laca de uñas=manicura, esmaltes, "
    "esterilizador, barbero=barbería, barba, cuchilla de barbero, poste de barbero, tele, wifi, citas=agenda, tarjeta de visita, propina, "
    "aprendiz, olor a tinte, cortinas, ventilador, aire acondicionado, reloj, flores, cafetera, vasos de agua, caramelos, chuches, niños llorando",
 4: "tijeras de entresacar, tijeras de esculpir, navaja de afeitar, sedal? no, cepillo cuello=plumero, cuello de papel=tira de papel, rollo de papel, "
    "neutralizador, matizador, pigmentos, peróxido, mezclador, balanza para el tinte, temporizador=reloj de cocina, lámpara de infrarrojos=climazón, "
    "esterilizador de rayos UV, desinfectante=Barbicide, cubo de basura, recogedor, aspiradora, toallas negras, pinzas de pato, separadores, "
    "redecilla, rodillo, tenacillas de ondas, plancha de ondas, cepillo alisador, cortapuntas, recortadora, perfiladora, trimmer, máquina de patillas, "
    "silla hidráulica, reposapiés, reposacabezas, cuello del lavacabezas, grifo, ducha de mano, champú anticaspa, champú morado, tónico, loción capilar",
},
"patata_formas": {
 1: "fritas=patatas fritas, al horno=asadas=patata asada=patatas asadas, cocidas=hervidas=patata cocida, puré=puré de patatas, tortilla=tortilla de patatas, "
    "bravas=patatas bravas, chips=patatas chips=patatas de bolsa, gajos=deluxe=patatas deluxe",
 2: "a lo pobre=patatas a lo pobre, panaderas=patatas panaderas, al vapor, en ensalada=ensaladilla=ensaladilla rusa=ensalada de patata, guisadas=guiso=estofadas, "
    "rellenas=patatas rellenas, gratinadas=gratén=gratin dauphinois, revolconas=patatas revolconas, a la importancia=patatas a la importancia, "
    "al microondas, en la freidora de aire=freidora de aire=airfryer, paja=patatas paja, rejilla, risoladas, salteadas=patatas salteadas, "
    "alioli=patatas alioli=all i oli, con carne=carne con patatas, con chorizo=patatas a la riojana=riojana, papas arrugadas=arrugadas, "
    "croquetas de patata=croquetas, rösti, hash browns, tortitas de patata, chafadas=aplastadas=smashed, cremas=crema=crema de patata, sopa de patatas",
 3: "a la brasa=en las brasas, a la parrilla=a la plancha, confitadas, al ajillo, en salsa verde, a la marinera, en caldereta, con bacalao, "
    "en papillote, dauphine=patatas dauphine, duquesa=patatas duquesa, Pont-Neuf, soufflé=suflé=patatas soufflé, Anna=patatas Anna, "
    "fondant=patatas fondant, boulangère, lyonnaise=a la lyonesa, hasselback=patatas hasselback=acordeón, gnocchi=ñoquis, "
    "kartoffelsalat, poutine, latkes, pierogi, aloo gobi, patatas a la crema, patatas con mojo, mojo picón, patatas meneás, papas con choco, "
    "patatas en ajopollo, patatas viudas, patatas guisadas con costillas, marmitako, patatas con huevo frito=huevos rotos=huevos estrellados, "
    "patatas a la cazuela, patatas al rescoldo, patatas a la sal, patatas encebolladas, patatas fritas caseras, patatas en espiral=espiral, "
    "patatas twister, patatas gofre=waffle fries, patatas cajún, patatas bastón, patatas noisette=noisette, parmentier=hachis parmentier, "
    "pastel de patata, budín de patata, patatas al cabrales, patatas al queso=patatas con queso, patatas trufadas, patatas con salsa de queso",
 4: "pommes allumettes, pommes gaufrettes, pommes château, pommes paille, pommes Pont-Neuf, pommes sautées, pommes de terre en robe des champs, "
    "patatas en chaqueta, patatas con piel, patatas nuevas, patatas a lo pobre de Sanlúcar, patatas en amarillo, patatas con níscalos, patatas trufa, "
    "chuño, papa a la huancaína, causa limeña=causa, papa rellena, colcannon, champ, bubble and squeak, rumbledethumps, stamppot, boxty, "
    "tartiflette, aligot, truffade, kugel, knish, raggmunk, kroppkakor, kartoffelpuffer, Bratkartoffeln, Kartoffelknödel, kopytka, draniki, "
    "aloo paratha, aloo tikki, batata vada, patatas al curry, patatas bombay, hash, tater tots, curly fries, patatas Hasselback, rissolée",
},
"personaje_gafas": {
 1: "Harry Potter=Harry, Mortadelo? no, Pepe Gotera? no, Nobita, Velma, Clark Kent=Superman, Bob Esponja? no, Shin Chan? no, "
    "Daniel el travieso? no, Milhouse, Lisa? no, Manolito Gafotas=Manolito, Arale=Arale Norimaki, Wally=Dónde está Wally, Elton John? no, "
    "Doctor Who? no, el Doctor Emmett Brown=Doc Brown=Doc, Minions=minion",
 2: "Edna Moda=Edna, Gru? no, Mr. Magoo=Magoo, Peter Parker? no, Ugly Betty=Betty=Betty la fea, Steve Urkel=Urkel, Dexter, Velma Dinkley, "
    "Ron Burgundy? no, Hermione? no, Luna Lovegood? no, Dumbledore, Albus Dumbledore, el profesor Frink=Frink, Martin Prince=Martin, "
    "el profesor Bacterio=Bacterio, el doctor Zoidberg? no, Hermes? no, Nerd? no, Dwight? no, Earl Sinclair? no, Steve Jobs? no, "
    "Mafalda? no, Felipe? no, Lisa Simpson? no, Phineas? no, Baljeet, Kenneth? no, Waldo, Scott Summers=Cíclope, Lobezno? no, Nick Furia=Nick Fury? no, "
    "Tony Stark? no, Neo, Morfeo=Morpheus, el agente Smith=Agente Smith, John Lennon? no, Elton? no, el Gran Lebowski? no, Ron? no, "
    "Mortadelo=Mortadelo (con gafas)? no, Ojo Loco Moody? no, Sybill Trelawney=Trelawney, Rita Skeeter, Dolores Umbridge? no, Percy Weasley? no",
 3: "Bubbles? no, Anteojito=Anteojito, Cuatro Ojos, Chuckie=Chuckie Finster, Sid? no, Clark Griswold? no, Indiana Jones? no, Austin Powers, "
    "Edna Krabappel? no, Snoopy? no, Linus? no, Marcie=Marcie de Charlie Brown, Peppermint Patty? no, Piggy? no, Kermit? no, "
    "Beaker? no, Bunsen Honeydew? no, Gonzo? no, el profesor Utonio? no, Dexter's? no, Timmy Turner? no, A.J.? no, Cosmo? no, "
    "Mr. Krabs? no, Calamardo? no, Plankton? no, Ralph? no, Ojo de Halcón? no, Harley Quinn? no, el Pingüino=Pingüino=Oswald Cobblepot, "
    "Lisa Turtle? no, Screech=Samuel Powers, Doug Funnie? no, Arthur=Arturo (el oso hormiguero), Francine? no, Buster? no, Brain=Cerebro, "
    "Milo de Atlantis=Milo Thatch=Milo, Russell? no, Carl Fredricksen=Carl=el abuelo de Up, Bruce Banner? no, Willy Wonka? no, Charlie? no, "
    "Hans Topo, Mr. Burns? no, Sheldon? no, Leonard Hofstadter=Leonard, Howard Wolowitz? no, Raj? no, Lilith? no, Frasier? no, Niles? no, "
    "Spencer Reid? no, Garcia=Penelope Garcia, Gilbert Grape? no, Napoleon Dynamite=Napoleón Dynamite, Ugly Betty Suárez, Bridget Jones? no, "
    "Andy Sachs? no, Miranda Priestly? no, Toby? no, Cliff Clavin? no, Jesse Pinkman? no, Walter White? no, Gus Fring=Gustavo Fring, "
    "Mr. Peabody=Peabody, el profesor Layton=Layton, Doctor Eggman=Eggman=Robotnik, Ignatius? no, Sherman, el Dr. Nick? no, Dr. Doofenshmirtz? no",
 4: "Velma de Scooby-Doo, Steve Harrington? no, Dustin? no, Mike Wheeler? no, Bill Gates? no, Dr. Chuck? no, Clark Kent disfrazado, "
    "Peggy? no, Hank Hill=Hank, Bobby Hill? no, Dale Gribble=Dale, Toad? no, Professor E. Gadd=E. Gadd=profesor Fesor, Nerd de Toy Story? no, "
    "Jimmy Neutron? no, Carl Wheezer=Carl Wheezer, Edd=Doble D, Kevin? no, Gene Belcher? no, Ted Mosby? no, Marshall? no, "
    "Doctor Octopus=Doctor Octopus=Otto Octavius, el Búho? no, Rorschach? no, Nite Owl=Búho Nocturno, Harold Lauder? no, Piggy de El señor de las moscas=Piggy, "
    "Ben Wyatt? no, Ron Swanson? no, Leslie? no, Gene Parmesan? no, Ignatius Reilly? no, el profesor Tornasol=Tornasol, Abraham Tornasol, "
    "Filemón? no, el Súper? no, Bacterio, Ofelia? no, Rompetechos=Rompetechos, Anacleto? no, Superlópez? no, Zipi? no, Zape? no, Carpanta? no, "
    "Pepe Gotera y Otilio? no, Doña Urraca? no, Sacarino? no, el profesor Siesta? no, Capitán Trueno? no, Jabato? no, Pafman? no",
},
})

PREGUNTAS["app_movil"] = "Nombra una app del móvil"
MANO["app_movil"] = {
 1: "WhatsApp=Whatsapp=wasap, Instagram=Insta, TikTok=Tik Tok, YouTube, Facebook, Google Maps=Maps, Spotify, Netflix, Gmail=correo, Twitter=X, "
    "Telegram, Google=Chrome=Google Chrome, Safari, cámara=la cámara, calculadora, reloj=despertador=alarma, calendario, Amazon, Uber, Candy Crush",
 2: "Snapchat, Pinterest, BeReal, Threads, LinkedIn, Tinder, Bumble, Hinge, Shein, Vinted, Wallapop, AliExpress, Temu, Zara, Glovo, Just Eat, Uber Eats, "
    "Cabify, Bolt, FreeNow=Free Now, Blablacar=BlaBlaCar, Renfe, Booking, Airbnb, Google Drive=Drive, Dropbox, Outlook, Teams=Microsoft Teams, Zoom, "
    "Google Meet=Meet, Skype, Duolingo, Shazam, Twitch, Discord, Reddit, Pokémon GO, Clash Royale, Clash of Clans, Subway Surfers, Among Us, Roblox, "
    "Minecraft, Fortnite, Brawl Stars, Wordle, Bizum, PayPal, Revolut, Google Pay, Apple Pay=Wallet=Cartera, Strava, Waze, notas=Notas, fotos=Fotos=galería, "
    "linterna, mensajes=SMS, teléfono=llamadas, ajustes, App Store, Google Play=Play Store, Disney+=Disney Plus, HBO=HBO Max=Max, Prime Video, "
    "Movistar Plus=Movistar+, Filmin, Apple Music, SoundCloud, iCloud, Siri, ChatGPT, CapCut, Lime, Ryanair, Vueling, Iberia, Idealista, Fotocasa, Too Good To Go",
 3: "Tuenti, Messenger, Signal, Line, WeChat, Viber, Vine, Periscope, Musical.ly, Ask.fm, Habbo, Grindr, Badoo, Happn, Meetic, Lovoo, Wattpad, Goodreads, "
    "Letterboxd, Filmaffinity, IMDb, TV Time, Kindle, Audible, Storytel, Ivoox, Podimo, Pocket Casts, Deezer, Tidal, Amazon Music, YouTube Music, "
    "Google Translate=traductor=Traductor de Google, DeepL, Babbel, Busuu, Photomath, Quizlet, Notion, Trello, Evernote, Todoist, Slack, Asana, Canva, "
    "Lightroom, Snapseed, VSCO, Facetune, Picsart, InShot, Lensa, FaceApp, Remini, Google Lens, Google Fotos, Microsoft Word=Word, Excel, PowerPoint, "
    "Google Docs, Mi Fibra? no, Movistar, Vodafone, Orange, Mi Digi, Lowi, Mercadona, Carrefour, Lidl Plus, Dia, Alcampo, El Corte Inglés, Primark, "
    "Mango, Bershka, Pull&Bear, Stradivarius, H&M, Decathlon, IKEA, Leroy Merlin, Fnac, PcComponentes, MediaMarkt, Druni, Sephora, Primor, Yuka, MyFitnessPal, "
    "Fitbit, Garmin Connect, Nike Run Club, Adidas Running, Calm, Headspace, Flo, Clue, BeReal., Telepizza, Domino's, McDonald's, Burger King, KFC, "
    "Starbucks, Telepizza? no, Deliveroo, Rappi? no, Correos, Seur, MRW, Mi Carpeta Ciudadana, Cl@ve=Clave, DGT=miDGT, Agencia Tributaria, App de la Seguridad Social, "
    "Radar COVID, Metro de Madrid, TMB, EMT, Moovit, Citymapper, Bicimad, Bicing, Cabify? no, Lime? no, Tier, Dott, Acciona, ShareNow, Zity, Wible, "
    "Parkimeter, ElParking, Telpark, Waylet, Repsol, Cepsa, BP, Ticketmaster, Fever, Entradas.com, Eventbrite, Dice, Xceed, Tripadvisor, El Tenedor=TheFork, "
    "Skyscanner, Kayak, eDreams, Trainline, Ouigo, Iryo, Alsa, FlixBus, Google Earth, Google Keep, Google Fit, Salud=Apple Salud, Buscar mi iPhone=Encontrar, "
    "Truecaller, Tinder Gold? no, OnlyFans, Patreon, Kick, Bigo Live, Likee, Zepeto, Lemon8, Pinduoduo? no, Hay Day, FarmVille, Angry Birds, Flappy Bird, "
    "Temple Run, Fruit Ninja, Doodle Jump, Cut the Rope, Plants vs. Zombies=Plantas contra zombis, Geometry Dash, Piano Tiles, 2048, Sudoku, Apalabrados, "
    "Preguntados, Trivial Crack, Ludo King, Parchís Star, Toon Blast, Royal Match, Homescapes, Gardenscapes, Coin Master, Hill Climb Racing, Asphalt, "
    "PUBG Mobile, Call of Duty Mobile, Free Fire, Genshin Impact, Honkai Star Rail, Monopoly Go, Stumble Guys, Pou, My Talking Tom=Talking Tom, Tamagotchi? no",
 4: "Bereal? no, Yubo, Wizz, Hoop, Monkey, Omegle, Chatroulette, Kik, Houseparty, Clubhouse, Poparazzi, Dispo, Lapse, Locket, Gas, Tellonym, NGL, Sarahah, "
    "Tumblr, Flickr, Fotolog, Myspace, Hi5, Foursquare, Swarm, Path, Ello, Mastodon, Bluesky, Nextdoor, Meetup, Couchsurfing, Workaway, Duolingo ABC, "
    "Anki, Memrise, HelloTalk, Tandem, Mondly, Rosetta Stone, Brainly, Socratic, Microsoft Authenticator, Google Authenticator, 1Password, LastPass, Bitwarden, "
    "NordVPN, ExpressVPN, Proton Mail, Proton VPN, Brave, Firefox, Opera, DuckDuckGo, Edge, Samsung Internet, CCleaner, Files, Documents, Scanner Pro, CamScanner, "
    "Adobe Scan, Acrobat, Genius Scan, Shortcuts=Atajos, Tasker, IFTTT, Home=Casa, Alexa, Google Home, SmartThings, Philips Hue, Ring, Tado, Netatmo, "
    "Endomondo, Runtastic, Komoot, Wikiloc, AllTrails, Relive, Zwift, Peloton, Freeletics, Sweatcoin, Fitness=Apple Fitness, Sleep Cycle, BetterSleep, "
    "Forest, Flipd, Habitica, Streaks, Daylio, Reflectly, Woebot, Wysa, Replika, Character.AI, Gemini, Copilot, Claude, Perplexity, Midjourney, Pi, "
    "Lensa AI, Prisma, Meitu, Snow, B612, Ulike, Polycam, Procreate, Ibis Paint, Sketchbook, Tayasui, Concepts, GoodNotes, Notability, Obsidian, Bear, "
    "Day One, Things, OmniFocus, Fantastical, Spark, Airmail, Superhuman, Hey, Bumble BFF, Wapa, Her, Feeld, Raya, Coffee Meets Bumble, OkCupid, Plenty of Fish, "
    "Tribbu, Coinbase, Binance, eToro, Trade Republic, MyInvestor, Indexa Capital, N26, Bnext, Vivid, Wise, Bunq, Imagin, ING, BBVA, Santander, CaixaBank, Sabadell, "
    "Bankinter, Openbank, Kutxabank, Abanca, Unicaja, Ibercaja, Verse, Twyp, Splitwise, Tricount, Fintonic, Wallet by BudgetBakers, Money Manager, Uala? no",
}

# ── jueves 12 ──
PREGUNTAS.update({
    "cereales": "Nombra una marca de cereales",
    "tiene_teclas": "Nombra algo que tenga teclas",
    "naranja": "Nombra una fruta o verdura de color naranja",
    "en_cabeza": "Nombra algo que se pone en la cabeza",
    "cuerpo_produce": "Nombra algo que produce el cuerpo humano",
    "hecho_leche": "Nombra algo que se hace con leche",
})
MANO.update({
"cereales": {
 1: "Kellogg's=Kelloggs, Chocapic, Corn Flakes=Cornflakes=copos de maíz, Special K, Choco Krispies=Chocokrispis=Krispies, Nesquik=cereales Nesquik, Frosties, Smacks, Froot Loops=Fruit Loops, Hacendado",
 2: "Nestlé, Fitness, Lion, Golden Grahams, Cheerios, Kellogg's All-Bran=All-Bran=All Bran, Cini Minis=Cinnamon Toast Crunch, Trésor=Tresor, Extra=Kellogg's Extra, "
    "Miel Pops=Honey Pops, Rice Krispies, Crunchy Nut, Coco Pops, Quaker=Quaker Oats, Nestlé Fitness, Kit Kat cereales=Kit Kat=KitKat, Lion cereales, Estrellitas=estrellitas de chocolate, "
    "Golden Nuggets? no, Muesli=muesli, Granola, Weetabix, Krave, Chocos? no, Kelloggs Special K Chocolate, Gullón? no, Dia, Carrefour, Lidl=Crownfield, Alcampo=Auchan, Eroski",
 3: "Smacks de Kellogg's? no, Honey Nut Cheerios=Cheerios miel, Nesquik Duo, Chocapic Duo, Golden Grahams, Shreddies, Shredded Wheat, Clusters, Country Crisp=Country Store, "
    "Brüggen=Bruggen, Jordans, Dorset Cereals, Kölln, Alpen, Mornflake, Nature Valley, Bjorg, Gerblé, Gullón Vitalday=Vitalday=Gullón, Santiveri, El Granero, Bio Organic? no, "
    "Mercadona Hacendado Corn Flakes? no, Hacendado copos de avena, Nestlé Chocapic, Kellogg's Pops=Pops, Cookie Crisp, Lucky Charms, Cap'n Crunch, Trix, Cocoa Puffs, "
    "Reese's Puffs, Apple Jacks, Frosted Flakes, Honey Smacks, Corn Pops, Krave Choco, Jungly=Jungle? no, Dinosaurus? no, Choco Flakes? no, Nesquik Mix? no, "
    "Kellogg's Choco Pops, Kellogg's Frosties Choco, Special K Frutos Rojos, Special K Original, Fitness Fruits, Fitness Chocolate, Nestlé Golden Grahams, Nestlé Shreddies, "
    "Nestlé Cheerios, Nestlé Cini Minis, Nestlé Lion, Nestlé Nesquik, Nestlé Fitness, Kellogg's Special K, Kellogg's Corn Flakes, Kellogg's Froot Loops, Kellogg's Smacks, "
    "Kellogg's Rice Krispies, Kellogg's Coco Pops, Kellogg's Crunchy Nut, Kellogg's Krave, Kellogg's All-Bran, Quaker Cruesli=Cruesli, Quaker avena, Kellogg's Frosties",
 4: "Post, General Mills, Nature's Path, Kashi, Cascadian Farm, Barbara's, Bear Naked, Grape-Nuts, Raisin Bran, Fruity Pebbles=Pebbles, Cocoa Pebbles, Honey Bunches of Oats, "
    "Golden Crisp, Wheaties, Kix, Chex, Total, Life, Cracklin' Oat Bran, Special K Red Berries, Mini-Wheats=Frosted Mini-Wheats, Ready Brek, Oatibix, Coco Shreddies, "
    "Curiously Cinnamon, Nestlé Clusters, Nestlé Country Store, Nestlé Shredded Wheat, Kellogg's Fruit 'n Fibre, Kellogg's Bran Flakes, Kellogg's Optivita, Kellogg's Variety, "
    "Lizi's, Pertwee? no, Rude Health, Deliciously Ella, Paleo? no, Grenade? no, Lidl Crownfield Choco Shells, Choco Shells, Choco Balls, Choco Rice, Arroz inflado=arroz inflado chocolate, "
    "Hacendado Choco Flakes, Hacendado Corn Flakes, Hacendado Estrellitas, Dia Corn Flakes, Bonpreu? no, Consum, Gadis? no, Vitalday, Sanavi? no, Nesquik Alphabet, Krispies Fresa, Kellogg's Pops Choco",
},
"tiene_teclas": {
 1: "piano, teclado=teclado de ordenador, ordenador=portátil=ordenador portátil, calculadora, móvil antiguo=móvil=teléfono, máquina de escribir, mando=mando de la tele=mando a distancia",
 2: "órgano, sintetizador=teclado musical=órgano electrónico, acordeón, cajero automático=cajero, microondas, teléfono fijo=teléfono de casa, telefonillo=portero automático, "
    "caja registradora=caja=TPV, datáfono, máquina de vending=máquina expendedora, ascensor, alarma=panel de la alarma, mando de la consola=mando de la Play=mando, "
    "lavadora, horno, xilófono? no, clavicordio=clave=clavecín, melódica=pianica, piano de cola, piano de juguete, Game Boy, Nintendo DS? no, fax, impresora, fotocopiadora",
 3: "celesta, clavicémbalo, espineta, armonio, harmonio, glockenspiel? no, vibráfono? no, marimba? no, carillón, piano eléctrico, Rhodes, Moog, mellotrón, "
    "bandoneón, concertina, organillo? no, zanfona=zanfoña, nyckelharpa, hardanger? no, saxofón (llaves)? no, clarinete? no, flauta? no, "
    "cerradura electrónica=cerradura con código, caja fuerte, parquímetro, máquina de billetes=máquina de tickets, máquina de café, dispensador de agua? no, "
    "lavavajillas, secadora, aire acondicionado=mando del aire, termostato, radio=radio del coche, walkie? no, busca=buscapersonas, Tamagotchi, consola=consola portátil, "
    "agenda electrónica=PDA, diccionario electrónico, traductor electrónico, teclado braille=máquina Perkins, máquina de coser electrónica, cafetera, báscula? no, "
    "taladro? no, máquina de escribir eléctrica, teletipo, telégrafo, máquina Enigma=Enigma, caja de música? no, juguete musical, teléfono de juguete, piano de suelo, "
    "mesa de mezclas, caja de ritmos, sampler, controlador MIDI, launchpad, teclado MIDI, Stylophone? no, Bop It? no, Simon Dice=Simon",
 4: "virginal, clavicordio, fortepiano, pianola, piano vertical, piano de pared, ondas Martenot, teclado de membrana, teclado mecánico, teclado numérico, "
    "teclado virtual, teclado de la tablet, máquina de escribir de estenotipia=estenotipia, estenógrafo, linotipia, monotipia, calculadora científica, calculadora gráfica, "
    "ábaco? no, centralita, interfono, videoportero, panel de ascensor, consola de avión, mando de garaje, llave del coche, cerradura digital, teclado de la caja fuerte, "
    "control de acceso, fichador, torno, máquina de lotería, tragaperras, máquina recreativa=recreativa, pinball? no, karaoke? no, jukebox=máquina de discos, "
    "acordeón cromático, acordeón diatónico, trikitixa, armónica cromática? no, órgano Hammond=Hammond, órgano de tubos, órgano de iglesia",
},
"naranja": {
 1: "naranja=naranjas, zanahoria=zanahorias, mandarina=mandarinas, calabaza, melocotón, mango, papaya, albaricoque=albaricoques",
 2: "boniato=batata=moniato, pimiento naranja=pimiento, níspero=nísperos, caqui=kaki=palosanto, melón cantalupo=cantalupo=melón naranja, clementina=clementinas, "
    "kumquat=quinoto, pomelo? no, nectarina, maracuyá=fruta de la pasión? no, physalis=alquequenje, tomate naranja, calabaza moscada=calabaza violín, naranja sanguina? no",
 3: "espino amarillo=espino falso, carambola, mangostán? no, lúcuma, tamarillo, rambután? no, níspero japonés, calabaza Hokkaido=potimarrón, calabaza cacahuete=butternut, "
    "zapallo, auyama, zanahoria morada? no, chile habanero=habanero, guindilla naranja, mostaza? no, maíz? no, cúrcuma, setas? no, rebozuelo=chantarela, níscalo=níscalos, "
    "lentejas rojas? no, salmonberry, serbal=serbas, acerola, madroño=madroños, rosa mosqueta? no, naranjilla=lulo, mamey, carica, zapote, pitanga, guayaba? no, "
    "membrillo? no, tangerina, satsuma, kinnow, tangelo, mineola, naranja Navel=navel, naranja Valencia, calabaza de Halloween, calabacín naranja? no, "
    "remolacha dorada, nabo naranja? no, pimiento morrón naranja, tomate cherry naranja, flor de calabacín, capuchina? no",
 4: "melocotón paraguayo=paraguayo, platerina, albaricoque japonés, umeboshi? no, nance, mamoncillo? no, bacuri, buriti, cajá, cupuazú? no, pejibaye, "
    "loquat, cornejo? no, aronia? no, hippophae, cloudberry=mora de los pantanos=mora ártica, camemoro, akee=aki, naranja amarga, naranja china, chinotto, bergamota, "
    "cidra? no, mano de Buda? no, pomelo rosa? no, calabaza de Etampes, calabaza Red Kuri, calabaza Hubbard, calabaza delicata, calabaza turbante, "
    "chile Scotch bonnet, ají amarillo, ají limo, rocoto, chile manzano, pimiento de Gernika? no, zanahoria de Utrera, zanahoria baby, ñame? no, oca, mashua, "
    "malanga? no, papa amarilla? no, boniato naranja, camote",
},
"en_cabeza": {
 1: "gorro=gorra, sombrero, casco, gafas=gafas de sol, corona, diadema, peluca, pañuelo, cinta del pelo=cinta, coletero=goma del pelo=goma, horquilla=pinza",
 2: "boina, capucha, turbante, velo, tiara, visera, champú, crema? no, tinte, laca, gomina=gel, cera, mascarilla del pelo=mascarilla, acondicionador, "
    "auriculares=cascos, gorro de baño=gorro de piscina, gorro de lana, gorro de Papá Noel, sombrero de copa, sombrero de paja, sombrero mexicano=sombrero de charro, "
    "pamela, tocado, mantilla, peineta, hiyab=hijab, kipá, burka? no, chador? no, niqab? no, mitra, solideo, birrete, cofia, gorro de cocinero, gorro de dormir, "
    "pasamontañas, braga de cuello? no, cinta de tenis=muñequera? no, toalla=turbante de toalla, bolsa? no, frontal=linterna frontal, gafas de natación, gafas de esquí, "
    "gafas de realidad virtual, lentillas? no, pendientes? no, piercing? no, maquillaje? no, flor, corona de flores, lazo, gorro de cumpleaños",
 3: "fez, chapela, txapela, montera, sombrero cordobés, sombrero de ala ancha, fedora, borsalino, bombín, canotier, panamá, stetson=sombrero vaquero, "
    "tricornio, bicornio, morrión, yelmo, celada, capirote, capirucho? no, cofia de enfermera, toca, griñón? no, tocado de plumas, penacho, corona de laurel, "
    "laurel, aureola? no, halo? no, diadema de orejas, orejas de Mickey, cuernos de reno, cuernos de vikingo, casco de vikingo, casco de bici, casco de moto, "
    "casco de obra, casco de minero, casco de astronauta, gorro de aviador, gorro ruso=ushanka, gorro de Pierrot? no, gorro frigio, gorro de bufón, gorro de bruja, "
    "sombrero de bruja, sombrero de mago, gorro de elfo, gorro de marinero, gorra de capitán, gorra de plato, gorra de policía, boina militar, gorro de cuartel, "
    "cucurucho, gorra de béisbol, snapback, bucket hat=gorro de pescador, beanie=gorro beanie, durag, bandana, cinta de sudor, redecilla, rulos, papillotes, "
    "bigudíes, pinzas, pasadores, coletas? no, extensiones, postizo, moño postizo, trenza postiza, aceite para el pelo, champú seco, antipiojos=lendrera, "
    "piojos, protector solar, sombrilla de cabeza, paraguas de cabeza, almohada, cojín? no, bolsa de hielo, compresa fría, venda, vendaje, mano? no",
 4: "kufi, taqiyah, keffiyeh=kufiya, agal, dastar, pagri, topi, bonete, birreta, capelo, tiara papal, solideo, camauro, zucchetto, gorro de Caganer? no, "
    "barretina, cachirulo, pañuelo de cachirulo, montera picona, montera de pasiego, sombrero de Pasiego? no, sombrero calañés, sombrero de catite, "
    "chistera, claque, galero, sombrero de copa baja, trilby, homburg, pork pie, cloche, tam o'shanter, glengarry, balmoral, deerstalker=gorra de cazador, "
    "ushanka, papakha, kolpak, shtreimel, sombrero cónico=sombrero asiático, nón lá, sugegasa, jingasa, kanmuri, eboshi, tocado de geisha, "
    "kokoshnik, coronilla, diadema nupcial, velo de novia, mantilla de blonda, peineta de carey, tembleque, rodete, moño de picaporte, "
    "casco de esgrima=careta de esgrima, máscara de esgrima, protector de cabeza de boxeo, casco de waterpolo, gorro de waterpolo, casco de rugby=melé, "
    "casco de jockey, casco de polo, casco de equitación, casco de F1, casco de bombero, casco de soldado, casco prusiano=pickelhaube, salacot, casco colonial",
},
"cuerpo_produce": {
 1: "sangre, saliva=babas=baba, sudor, lágrimas=lágrima, pis=orina=pipí, caca=heces=mierda=popó, mocos=moco, pelo=pelos, uñas, gases=pedos=pedo, eructos=eructo",
 2: "cera=cera de los oídos=cerilla=cerumen, semen=esperma=espermatozoides, leche=leche materna, legañas=legaña, caspa, hormonas=hormona, bilis, saliva, "
    "flemas=flema, pus, insulina, adrenalina, células, óvulos=óvulo, regla=menstruación=flujo, flujo vaginal, grasa, sebo, calor, energía, anticuerpos, "
    "glóbulos rojos, glóbulos blancos, plaquetas, dopamina, serotonina, endorfinas, oxitocina, testosterona, estrógenos, progesterona, melatonina, cortisol",
 3: "jugos gástricos=jugo gástrico=ácido clorhídrico, enzimas, bilirrubina, linfa, plasma, colágeno, queratina, melanina, cartílago? no, hueso? no, "
    "piel muerta=células muertas=escamas, callos? no, ampollas? no, granos? no, espinillas=puntos negros, esmegma, líquido preseminal, lubricación=flujo, "
    "calostro, líquido amniótico, placenta, mucosidad=moco cervical, surfactante, líquido cefalorraquídeo, líquido sinovial, humor acuoso, humor vítreo, "
    "lágrimas basales, hipo? no, ruido? no, electricidad=impulsos eléctricos, CO2=dióxido de carbono, vapor de agua, olor corporal=olor, feromonas, "
    "vitamina D, glucosa, glucógeno, colesterol, urea, ácido úrico, amoníaco, ácido láctico, cálculos=piedras en el riñón, sarro, placa? no, "
    "jugo pancreático, glucagón, tiroxina, hormona del crecimiento, prolactina, vasopresina, aldosterona, renina, histamina, interferón, trombina, fibrina, "
    "fibrinógeno, albúmina, hemoglobina, mioglobina, pepsina, tripsina, lipasa, amilasa, lactasa, ptialina",
 4: "quilo, quimo, surfactante pulmonar, meconio, vérnix=vernix caseosa, lanugo, esmalte? no, dentina? no, sinovia, endolinfa, perilinfa, "
    "secreción prostática, líquido seminal, moco nasal, bolo alimenticio, heces de meconio, secreción sebácea, glándulas? no, secreción apocrina, "
    "lisozima, inmunoglobulinas, citoquinas, prostaglandinas, leucotrienos, bradicinina, óxido nítrico, monóxido de nitrógeno? no, metano, hidrógeno, "
    "sulfuro de hidrógeno, acetona, cetonas, creatinina, bicarbonato, ácido hialurónico, elastina, osteocitos, eritropoyetina, calcitonina, paratohormona, "
    "grelina, leptina, secretina, gastrina, colecistoquinina, somatostatina, adrenocorticotropina, gonadotropina, hormona luteinizante, FSH, GH, TSH, "
    "noradrenalina, acetilcolina, GABA, glutamato, endocannabinoides, anandamida, células madre, médula? no, linfocitos, macrófagos, neutrófilos",
},
"hecho_leche": {
 1: "queso, yogur=yogures, mantequilla, nata, helado, flan, natillas, arroz con leche, batido=batidos, café con leche, leche con cacao=Cola Cao=Nesquik, bechamel",
 2: "requesón, cuajada, kéfir, crema catalana, leche frita, dulce de leche=manjar, leche condensada, leche merengada, chocolate con leche=chocolate, "
    "chocolate caliente=chocolate a la taza, crepes=tortitas, bizcocho, torrijas, panna cotta, tarta de queso, mozzarella, queso fresco, queso de Burgos, "
    "ricotta, mascarpone, nata montada, petit suisse=Danonino, Actimel, leche en polvo, horchata? no, cortado, capuchino, latte, sopa de leche? no, "
    "gachas=porridge, papilla, puré de patatas, salsa carbonara? no, quiche, natillas de chocolate, mousse, profiteroles? no, crema pastelera, tocino de cielo? no, "
    "suero, ghee=mantequilla clarificada, leche sin lactosa, leche de cabra? no, batido de fresa, milkshake, leche con galletas",
 3: "queso manchego=manchego, queso de cabra, queso azul, roquefort, cabrales, idiazábal, tetilla, torta del Casar, brie, camembert, parmesano, gouda, "
    "emmental, cheddar, feta, halloumi, burrata, mató, labneh, skyr, yogur griego, lassi, ayran, quark, cottage, queso crema=Philadelphia, cuajada de oveja, "
    "leche de pantera? no, ponche, rompope, eggnog=ponche de huevo, leche de tigre? no, chai latte, café bombón=bombón, carajillo? no, cappuccino, macchiato, "
    "flat white, caramel macchiato, frappé, granizado de café, helado de vainilla, sorbete? no, polo de leche=polo, semifrío, leche helada, tarta de la abuela? no, "
    "bizcocho de yogur, magdalenas, rosquillas, pan de leche, brioche, croissant, ensaimada? no, pestiños? no, flan de huevo, natillas caseras, "
    "arroz con leche asturiano, filloas, frixuelos, sopas de leche, migas? no, besamel, salsa de queso, fondue, raclette, macarrones con queso=mac and cheese, "
    "puré de calabaza? no, crema de verduras, sopa de cebolla? no, salsa Alfredo, salsa cuatro quesos, gratén=gratinado, pastel de patata, tres leches=tarta tres leches",
 4: "kumis, kumiss, airag, skyr islandés, smetana, crème fraîche, clotted cream, cuajada vasca=mamia, gaztanbera, requesón de Miraflores, recuit, brossat, "
    "queso de Mahón, queso de Arzúa, San Simón, cebreiro, afuega'l pitu, gamonéu, picón, majorero, palmero, flor de Guía, zamorano, payoyo, torta de La Serena, "
    "queso de Tronchón, garrotxa, Tou dels Til·lers? no, provolone, gorgonzola, taleggio, pecorino, grana padano, stracciatella, scamorza, paneer, chhena, "
    "rasgulla, kulfi, kheer, payasam, basundi, rabri, dulce de leche cortada, cajeta, manjar blanco, blancmange, junket, posset, syllabub, custard, "
    "flan napolitano, crème brûlée, pots de crème, crema inglesa, leche asada, natilla colombiana, arequipe, tres leches, sopa paraguaya? no, chipá, "
    "pão de queijo, leche de burra? no, caseína, lactosa, lactosuero, whey=proteína whey, butter milk=suero de mantequilla, cuajo? no",
},
})

# ── viernes 13 ──
PREGUNTAS.update({
    "farmacia": "Nombra una cosa que se venda en una farmacia",
    "tiene_cremallera": "Nombra algo que tenga cremallera",
    "plato_huevo": "Nombra un plato que lleve huevo",
    "esqui_cosas": "Nombra algo que hay en una estación de esquí",
    "se_vende_barra": "Nombra algo que se vende en barra",
    "villano_animal": "Nombra un villano que sea un animal",
    "estanco": "Nombra algo que se vende en un estanco",
})
MANO.update({
"farmacia": {
 1: "medicamentos=medicinas=pastillas=fármacos, paracetamol=Gelocatil=Dafalgan, ibuprofeno=Espidifen=Neobrufen=Dalsy, aspirina, tiritas=tirita=apósitos, "
    "crema=cremas, preservativos=condones=condón, test de embarazo=prueba de embarazo, termómetro, jarabe=jarabe para la tos, gasas, alcohol, mascarillas=mascarilla",
 2: "Frenadol, Couldina, Bisolvon? no, Strepsils=pastillas para la garganta=caramelos para la garganta, Voltarén=Voltaren, Enantyum, Nolotil, Almax, Omeprazol, "
    "antibiótico=antibióticos=amoxicilina, pomada, Betadine=povidona yodada, agua oxigenada, gel hidroalcohólico, protector solar=crema solar=Isdin, "
    "pasta de dientes, cepillo de dientes, colutorio=enjuague bucal, seda dental=hilo dental, champú anticaspa=champú, champú antipiojos=antipiojos=lendrera, "
    "leche infantil=leche de bebé, chupetes=chupete, biberón, pañales, toallitas, crema de pañal=Mitosyl, suero fisiológico=suero, lágrimas artificiales=colirio, "
    "lentillas=líquido de lentillas, vitaminas=vitamina C=vitamina D, magnesio, colágeno, melatonina, probióticos, píldora anticonceptiva=anticonceptivos, "
    "píldora del día después=pastilla del día después, lubricante, compresas, tampones, copa menstrual, test de antígenos=test de COVID, tensiómetro, "
    "vendas=venda, esparadrapo, tiritas para ampollas=Compeed, bolsa de agua caliente, rodillera, muñequera, tobillera, faja, medias de compresión, "
    "Durex, Avène, La Roche-Posay, Vichy, Isdin, Eucerin, Bioderma, Cerave, Nivea, Uriage, A-Derma, Sesderma, Martiderm, Heliocare",
 3: "Almax forte? no, Primperan, Fortasec, Imodium, suero oral=sueros=Bioralsuero, Dulcolax=laxante, Micralax, Hemoal, Lizipaina, Flutox, Iniston, Bisolgrip, "
    "Ilvico, Cinfatós, Fluimucil, Mucosan, Vicks VapoRub=Vicks, Respibien, Rhinomer, Sterimar, Otocerum? no, agua de mar en espray, Reflex, Radio Salil, "
    "Fastum gel, Thrombocid, Hirudoid, Cristalmina=clorhexidina, mercromina=Mercurocromo, Blastoestimulina, Trombocid, Fucidine, Silvederma, Bepanthol, "
    "vaselina, Halibut, aceite de almendras, aloe vera, after sun, repelente de mosquitos=antimosquitos=Relec, Goibi, Fenistil, Talquistina, Afterbite, "
    "Mitosyl, crema de manos, cacao de labios=protector labial=Labello, Lipikar, Atoderm, Neutrogena, Cicaplast, Avène Cicalfate, Biafine, Cicalfate, "
    "Dodot, Nutribén, Blemil, Almirón, Nidina, Enfamil, Hero Baby, Suavinex, Chicco, Nuk, Philips Avent, cepillo interdental, Lacer, Vitis, Kin, Oral-B, "
    "Sensodyne, Fluocaril, Parodontax, GUM, cera para ortodoncia, pegamento para dentaduras=Corega, Kukident, Benegast? no, Supradyn, Pharmaton, Berocca, "
    "Arkopharma, Aquilea, Redoxon, Multicentrum=Centrum, Femibion, hierro, ácido fólico, Omega 3, valeriana, tila, Dormidina, pastillas para dormir, "
    "parches de nicotina=Nicorette, chicles de nicotina, tiras de glucosa, glucómetro, lancetas, jeringuillas, insulina, inhalador=Ventolin, pulsioxímetro, "
    "nebulizador, muletas, andador, silla de ruedas, cojín antiescaras, plantillas=Dr. Scholl, callicida, piedra pómez, lima de pies, cortaúñas, pinzas, "
    "tapones para los oídos=tapones=Tapones Quies, antifaz, bolsa de hielo=frío instantáneo, botiquín, guantes de látex=guantes, Lactovit? no, desodorante=Vichy desodorante, "
    "tinte de pelo? no, quitaesmalte, pintalabios? no, maquillaje, base de maquillaje, rímel, Avène agua termal=agua termal, sérum, retinol, ácido hialurónico, "
    "contorno de ojos, exfoliante, mascarilla facial, gel íntimo, Chilly, Lactacyd, test de ovulación, gafas de presbicia=gafas de lectura, cuentagotas",
 4: "Paracetamol Kern? no, Efferalgan, Termalgin, Apiretal, Dalsy, Junifen, Algidol, Actron, Optalidón, Saridon, Migraleve? no, Hidroferol, Duphalac, "
    "Movicol, Plantaben, Fave de Fuca, Eupeptina? no, Gaviscon, Sal de frutas Eno=Sal de frutas, bicarbonato, Aero Red, Carbón activado=carbón, Ultralevura, "
    "Casenbiotic, Prodefen, Lactoflora, Megalevure, Aerored, Antiox? no, Cinfamar=pastillas para el mareo=Biodramina, Dramamine, Pantomicina? no, "
    "Clamoxyl, Augmentine, Zitromax, Cipro? no, Diazepam? no, Orfidal? no, Lexatin? no, Valium? no, Prozac? no, Viagra=sildenafilo, Cialis, Levitra, "
    "Postinor=Norlevo, ellaOne, Yasmin, Diane, anillo vaginal=NuvaRing, parche anticonceptivo, Canesten, Gynocanesten, Monistat? no, Lomexin, "
    "Daktarin, Fungarest, Lamisil, Oddent? no, Bexident, Perio-Aid, Oraldine, Listerine, Halita, Desensin, Elgydium, Bucometasana, Aftex, Aloclair, "
    "Zovirax, Zovicrem, Herpix, Isdinceutics, Endocare, Neostrata, SkinCeuticals, Filorga, Caudalie, Nuxe, Klorane, Ducray, Pilexil, Olistic, Lambdapil, "
    "Iraltone, Minoxidil, Regaxidil, Neo Peptine? no, Sebamed, Mustela, Suavinex, Letibalm, Halibut Derma, Nutraisdin, Mitosyl, Weleda, Arnica=árnica, "
    "Traumeel, Heel? no, Oscillococcinum=Oscillo, homeopatía, flores de Bach, propóleo, jalea real, equinácea, ginseng, ginkgo, Arkocápsulas, "
    "XLS Medical, Bimanán, Siken, Herbalife? no, proteína en polvo, sales de baño? no, aceite de rosa mosqueta=rosa mosqueta, crema de caléndula, Thealoz, "
    "Hyabak, Systane, Optrex? no, Visine? no, Aquoral, Hylo-Comod, lupa, pastillero, nebulizador, cámara de inhalación, termómetro de oído, aspirador nasal, "
    "sacaleches, pezoneras, discos de lactancia, Purelan, chupetero, mordedor, Dentinox, Anbesol? no, cuña=orinal, empapadores, Tena, Indas, Ausonia, Evax, "
    "Tampax, Saforelle, Isdin Woman, Ginecanesgel, Rosalgin, Vagisil? no, Femarelle? no, Ovusitol? no, Clearblue, Predictor, Durex Play, KY? no, Control",
},
"tiene_cremallera": {
 1: "chaqueta=cazadora, mochila, pantalones=vaqueros=pantalón, bolso, maleta, estuche, sudadera, abrigo, cartera=monedero, falda, vestido, botas",
 2: "chubasquero=impermeable, plumas=plumífero, forro polar, chándal=chaqueta de chándal, neceser, riñonera, funda=funda del portátil=funda de móvil, "
    "saco de dormir, tienda de campaña, cojín=funda de cojín, edredón=funda nórdica, colchón=funda de colchón, bolsa de deporte, mochila del colegio, "
    "carpeta, portadocumentos, archivador, botines, bermudas, mono, peto, body? no, bañador? no, chaleco, traje de neopreno=neopreno, traje de esquí, "
    "pantalón de esquí, guantes? no, bolsa de viaje, maletín, cartuchera, portatrajes, portabebés? no, carrito de bebé, saco del carrito, cambiador",
 3: "bota de esquí? no, botas de montaña, botas de agua? no, deportivas con cremallera, zapatillas de casa? no, vestido de novia, uniforme, bata, "
    "parka, gabardina? no, anorak, cortavientos, polar, poncho? no, sudadera con capucha=hoodie, chaqueta vaquera? no, chupa de cuero=chupa, "
    "jersey con cremallera, polo con cremallera, pantalón cargo, shorts, minifalda, corsé, mono de trabajo, traje espacial, traje de motero, "
    "mono de motorista, traje de buzo, chaleco salvavidas, arnés? no, cartera de mano, clutch, bolso de mano, bandolera, tote? no, bolsa de la compra, "
    "bolsa térmica=nevera portátil, fiambrera, tartera, bolsa congelación=bolsa con zip=bolsas zip=bolsa zip, bolsa de plástico con cierre, portátil? no, "
    "cubre sofá, funda de sofá, puff, almohada? no, colchón hinchable? no, sombrilla? no, cortaviento, tienda de campaña, toldo? no, mosquitera de la tienda, "
    "funda de guitarra, funda de raqueta, raquetero, palo de golf? no, bolsa de golf, cubrezapatos? no, portatrajes, bolsa de esquís, bolsa para pañales, "
    "estuche de gafas, funda de gafas, agenda=agenda con cremallera, Biblia? no, diario, pasaporte? no, portatarjetas, cartera de documentos, carpeta de anillas",
 4: "polainas, sobrebotas, perneras, mangas desmontables, pantalón desmontable=pantalón convertible, chaqueta de motorista, chaleco de motorista, "
    "airbag de moto, protector de espalda, mochila de hidratación, camelbak, bolsa estanca, funda de cámara, mochila de fotógrafo, bolsa de cámara, "
    "maletín de herramientas, funda de tablet, funda de Kindle, portapapeles con cremallera, estuche de maquillaje, estuche de lápices, bolso bandolera, "
    "bolsa de pan? no, saco de boxeo? no, cojín de lactancia, mochila portabebés, saco de bebé, saco nórdico, pijama manta, mono de bebé, pelele, "
    "body de bebé? no, peto de bebé, vestido de flamenca? no, traje de luces? no, sotana? no, uniforme de piloto, traje de carreras, mono ignífugo, "
    "traje de apicultor, traje NBQ, traje de protección, buzo, mono de pintor, vadeador, pantalón de pesca, saco de vivac, funda de bici, funda de coche? no",
},
"plato_huevo": {
 1: "tortilla=tortilla de patatas=tortilla española, huevos fritos=huevo frito, huevos rotos=huevos estrellados, revuelto=huevos revueltos, huevos rellenos, "
    "flan, natillas, mayonesa, carbonara=espaguetis a la carbonara, tortilla francesa, huevo duro=huevos cocidos, ensaladilla rusa=ensaladilla",
 2: "huevos a la flamenca, pisto con huevo=pisto, huevos benedictinos=huevos Benedict, huevo poché=huevos escalfados, huevos pasados por agua, "
    "tortilla de calabacín, tortilla de espinacas, quiche, tiramisú, bizcocho, crema catalana, torrijas, leche frita, croquetas, rebozado=rebozados, "
    "empanados=san jacobo=filete empanado, merluza rebozada, calamares a la romana, gabardina? no, gazpacho? no, salmorejo, sopa castellana=sopa de ajo, "
    "huevos al plato, shakshuka, omelette, ramen, bibimbap, arroz tres delicias, arroz a la cubana, pad thai, nasi goreng, tortitas=pancakes, crepes, "
    "gofres, magdalenas, merengue, mousse, tocino de cielo, yemas de Santa Teresa=yemas, flan de huevo, tarta de queso, profiteroles, tortilla de bacalao",
 3: "huevos a la escocesa=huevo escocés, huevos en cocotte, huevos mollet, huevos con chorizo, huevos con jamón, huevos con patatas, "
    "patatas a lo pobre con huevo, migas con huevo=migas, pimientos con huevo, bacalao dorado=bacalhau à Brás, porra antequerana, ensalada César, "
    "ensalada nicoise=ensalada niçoise, ensalada mixta, espárragos con huevo, menestra, judías verdes con huevo, revuelto de setas, revuelto de gulas, "
    "revuelto de ajetes, revuelto de espárragos, huevos a la turca, huevos rancheros, tortilla de camarones, tortilla paisana, tortilla de sacromonte, "
    "tortilla de patatas con cebolla, frittata, tortilla de verduras, quiche lorraine, pastel de verduras, pastel de cabracho, budín, pudin, "
    "flan de verduras, soufflé=suflé, egg fried rice, okonomiyaki, tamagoyaki, oyakodon, chawanmushi, ramen con huevo, kimchi jjigae? no, "
    "huevos de codorniz, huevas? no, scotch egg, eggs Benedict, egg mayo, sándwich mixto con huevo=croque madame, hamburguesa completa, "
    "pizza con huevo, pizza Fiorentina, carbonara auténtica, fideuá? no, mayonesa casera, alioli, salsa tártara, salsa holandesa, salsa bearnesa, "
    "huevo hilado, natillas caseras, crème brûlée, crema pastelera, flan de queso, tarta de Santiago, bizcocho de yogur, brownie, galletas, pan de molde? no, "
    "brioche, panettone, roscón de Reyes=roscón, buñuelos, churros? no, pestiños, rosquillas, leche merengada, merengues, macarons, suspiros, huevos mimosa",
 4: "huevos a la Kiev? no, oeufs en meurette, oeufs mayonnaise, huevos en salsa, huevos en escabeche, huevos fritos con puntilla, puntillitas? no, "
    "huevos de Pascua? no, huevos de chocolate? no, tortilla de bacalao a la vizcaína, tortilla de Betanzos, tortilla de patatas jugosa, tortilla de chorizo, "
    "tortilla de alcachofas, tortilla de setas, tortilla de patata sin cebolla, huevos con morcilla, huevos con sobrasada, huevos con pisto manchego, "
    "atascaburras, ajoarriero? no, zarangollo, huevos a la riojana, huevos con salchichas, desayuno inglés, huevos benedictine, huevos Florentine, "
    "huevos Royale, huevos Sardou, huevos Benedict con salmón, egg drop soup=sopa de huevo, stracciatella, avgolemono, menemen, çılbır, kuku sabzi, "
    "tortilla persa, eggah, chilaquiles con huevo, huevos divorciados, huevos motuleños, migas extremeñas, gachas? no, cocido? no, ensalada de pasta? no, "
    "ensalada de patata alemana, devilled eggs, egg salad, kedgeree, tamago sando, tamago kake gohan, katsudon, omurice, tortilla de ostras, egg tart, "
    "pastel de nata, quindim, papos de anjo, ovos moles, sabayón=zabaione, flan de café, crema volteada, quesillo, huevos chimbos, yemas de Ávila",
},
"esqui_cosas": {
 1: "nieve, esquís=esquí, telesilla=telesillas, pistas=pista, botas de esquí=botas, bastones=palos, snowboard=tabla de snow, frío, teleférico, gafas de esquí=gafas, casco",
 2: "remonte=remontes, telesquí=telearrastre=percha, telecabina, cañones de nieve=cañones, máquina pisapistas=pisapistas=ratrac, escuela de esquí=monitores=monitor, "
    "forfait=forfaits=pase, taquilla=taquillas, alquiler de esquís=alquiler, cafetería=bar=restaurante, chocolate caliente=chocolate con churros, hotel=apartamentos, "
    "parking=aparcamiento, quitanieves, cadenas, mapa de pistas=plano de pistas, pista verde=pista azul=pista roja=pista negra, socorristas=pisteros, "
    "trineos=trineo, guantes, gorro, braga=braga de cuello, chaqueta de esquí=anorak, pantalón de esquí, crema solar, montañas=montaña, árboles=pinos, "
    "esquiadores=esquiador, snowboarders, niños, cola=colas, enfermería, après-ski, hielo, frío, sol, viento, ventisca, avalancha=aludes",
 3: "cinta transportadora=alfombra mágica, banderines, puertas de slalom=balizas, snowpark=park, halfpipe, saltos=rampas, raquetas de nieve, "
    "esquí de fondo, circuito de fondo, guardaesquís=taquillas de esquís, botas de snow, fijaciones, cera=cera de esquí, protector labial, "
    "gafas de ventisca, radio, megáfono, cartel de peligro de aludes, banderas, red de seguridad=redes=colchonetas, señales de pista, cumbre=cima, "
    "chalet=refugio, raclette? no, fondue, vin chaud=vino caliente, cervezas, discoteca, jacuzzi, spa, piscina climatizada, tienda=tienda de esquí, "
    "farmacia, ambulancia, helicóptero, motonieve=motos de nieve, perros de rescate=perros, ARVA=detector de víctimas, pala, sonda, mochila airbag, "
    "webcam=cámara, estación meteorológica, termómetro, nieve artificial, nieve polvo, nieve dura, placas de hielo, ventisquero, cornisa, fuera de pista, "
    "esquí de travesía=skimo, pieles de foca, crampones, piolet, mosquetones? no, bufanda, calcetines térmicos, ropa térmica, manopla, cubrebotas",
 4: "telesilla desembragable, silla de seis, telemix, funicular, cremallera=tren cremallera, tapis roulant, cinta de esquí, arrastre de pértiga=pértiga, "
    "pilona, torre de cañones, lanza de nieve, balsa de innivación, pisapistas con cabrestante, fresadora, pala quitanieves, sal? no, gravilla? no, "
    "cabina de remonte, torniquete=tornos, lector de forfait, chip, tarjeta magnética, jardín de nieve, guardería, club de esquí, competición, "
    "slalom gigante=slalom=eslalon, supergigante, descenso, combinada, moguls=bañeras, baches, boardercross, skicross, telemark, freeride, freestyle, cajón=box, rail, "
    "kicker, quarterpipe, big air, piste basher, puesto de socorro, camilla=akja, trineo de rescate, collarín, férula, mantas térmicas, "
    "pistero socorrista, perro de avalanchas, Barryvox, PIEPS, sondas, mochila ABS, kit de avalanchas, boletín de aludes, escala de aludes, bandera negra, "
    "cortadores de nieve? no, cristales de nieve, escarcha, encebado? no, rimaya, glaciar, morrena, serac, fondue de queso, crepería, raclette, tartiflette",
},
"se_vende_barra": {
 1: "pan=barra de pan, chocolate=chocolatina=barrita de chocolate, barra de labios=pintalabios, regaliz, desodorante=desodorante en barra, "
    "barritas de cereales=barrita de cereales=barrita, pegamento=pegamento en barra=Pritt, mantequilla, helado=barra de helado",
 2: "turrón, pan de molde? no, chorizo? no, fuet? no, longaniza? no, salchichón? no, queso? no, barra de hielo? no, "
    "barrita energética=barritas energéticas=barrita de proteínas, Kinder=Kinder Bueno, Twix, Mars, Snickers, Kit Kat, Lion, Toblerone, "
    "cacao de labios=bálsamo labial=Labello, protector labial, corrector=corrector en barra, base de maquillaje en barra, colorete en barra, iluminador en barra, "
    "sombra de ojos en barra, protector solar en barra=stick solar=protector solar, cera=cera en barra, tiza=tizas, ceras=ceras de colores=Plastidecor, "
    "silicona=barras de silicona=barra de silicona caliente, plastilina, jabón=pastilla de jabón? no, incienso=varitas de incienso, carbón? no, "
    "pan de barra=baguette, pistola? no, barra de cortina? no, barra de pesas=barra de gimnasio, barra de pole dance? no, crêpes? no, membrillo? no",
 3: "chicle=chicles en barra, mazapán, barra de turrón, nougat, halva, torta? no, barra de cuarto=barra de medio=barra gallega, chapata=ciabatta, "
    "pistola=pistola de pan, baguette, barra de pan integral, pan de Viena, colines=palitos de pan, grisines, barra de pan de leche? no, "
    "embutido en barra? no, mortadela? no, sobrasada? no, paté en barra? no, foie=foie gras? no, queso en barra? no, mantequilla en barra, margarina, "
    "manteca, manteca de cacao=manteca de cacao para labios, manteca de karité en barra, chocolate para fundir, chocolate a la taza=chocolate Valor, "
    "cobertura de chocolate, Milka, Nestlé, Lindt, Valor, Ferrero? no, Aero, Crunch, Galaxy, Bounty, Milky Way, Topic, Picnic, Nuts, Lion bar, "
    "Kit Kat Chunky, Twix White, Snickers Protein, Natural Valley? no, Nature Valley, Special K bar, Fitness bar, Corny, Barritas Nestlé, Tosta Rica? no, "
    "desodorante stick, perfume sólido, champú sólido, acondicionador sólido, crema sólida, cera para el pelo, cera depilatoria, bálsamo, vaselina en barra, "
    "antiinflamatorio en barra? no, pomada en barra, after bite en barra, stick antimosquitos, stick de tiza, lápiz de cera, carboncillo, pastel=barras de pastel, "
    "sanguina, conté, grafito=barra de grafito, cola en barra, lacre=barra de lacre, cera para sellar, soldadura=barra de estaño=estaño, electrodos=barras de soldar, "
    "barra de silicona termofusible, masilla en barra, epoxi en barra, barra de cereales Kellogg's, barra de granola, barra de fruta, barras de sésamo, "
    "barritas de pescado? no, barra de hielo, polo? no, helado de corte, bloque de helado, tarta helada, barra de incienso, palo santo, vela? no",
 4: "barra de lingote=lingote de oro=lingotes, barra de plata, barras de acero=varillas, barras de aluminio, barras de cobre, perfil, tubo, corrugado? no, "
    "barra de uranio? no, barra de combustible? no, lápiz de ojos? no, kohl, barra de color, stick de contorno, stick de colorete, stick de labios y mejillas, "
    "brillo de labios? no, labial líquido? no, cera de peluquería, pomada, barra de champú, barra de jabón de afeitar, jabón de afeitar en barra, "
    "stick de alcanfor, stick mentolado, stick nasal=inhalador nasal, barra de alcanfor, barra de cacao, barra de quinoa, barra de dátiles, barra de higo, "
    "pan de higo, pan de Cádiz, alfajor? no, turrón de Jijona, turrón de Alicante, turrón de yema, turrón de chocolate, turrón de guirlache=guirlache, "
    "barra de praliné, barra de nougat, barra de caramelo, toffee, regaliz rojo, regaliz negro, palo de regaliz=palo dulce=paloduz, cañas de azúcar=caña de azúcar",
},
"villano_animal": {
 1: "Scar, Shere Khan, el Lobo Feroz=lobo feroz=lobo, Kaa, Úrsula? no, Jafar? no, Iago, Bowser, el Grinch? no, Lotso, Rey Rata? no, Plankton",
 2: "Ratigan=el profesor Ratigan, Hopper, Tai Lung, Shen=Lord Shen, Kai, el Rey Ratón=Rey de los Ratones, el Coyote=Wile E. Coyote, Silvestre? no, Tom? no, "
    "Doctor Doofenshmirtz? no, Perry? no, Mojo Jojo, Splinter? no, Shredder? no, Bebop, Rocksteady, Krang? no, Bebop y Rocksteady, Dr. Robotnik? no, "
    "Brujo? no, Edgar? no, Rasputín? no, Bartok, Lucifer, Si y Am=los gatos siameses, el gato de Cenicienta=Lucifer, Flotsam y Jetsam=Flotsam=Jetsam, "
    "las hienas=hienas=Shenzi=Banzai=Ed, Zira, Kovu? no, Nuka, Chick Hicks? no, Pete=Pedro el Malo=Pete el Malo, Dr. Nefario? no, Gru? no, Kalimán? no, "
    "Sid? no, Diego, Capitán Gutt, Soto, Rudy, King Kong? no, Godzilla, Moby Dick, Tiburón=el tiburón de Tiburón, Rex? no, Indominus Rex, el gato con botas? no, "
    "Monstruo de las galletas? no, Napoleón (Rebelión en la granja)=Napoleón, Chuck? no, Señor Gato? no, Belle? no, Dragón=dragón Maléfica, Smaug, "
    "Aragog, Nagini, Fawkes? no, Buckbeak? no, Pettigrew=Colagusano=Peter Pettigrew, Fenrir, Cerbero, el Kraken, Dragón de Shrek? no, Hotaru? no",
 3: "Sir Hiss=Siseo, el príncipe Juan=príncipe Juan (Robin Hood)=Juan sin Tierra, el sheriff de Nottingham, Edgar el mayordomo? no, Cruella? no, "
    "Bianca? no, Medusa? no, Percival McLeach? no, Sykes? no, Gargamel? no, Azrael, Clayton? no, Mamá Odie? no, Dr. Facilier? no, Madame Mim? no, "
    "Honest John=el zorro Juan Honrado=Honrado Juan, Gideon=el gato Gedeón=Gedeón, el Cochero? no, Monstro=la ballena Monstruo, Chernabog? no, Cocodrilo Tic-Tac=Tic-Tac, "
    "Mancha=Big Bad Wolf? no, Pedro el Malo, Lobo Feroz de los tres cerditos, el Gran Lobo Malo, Zorro y Gato, la víbora Kaa, Kaos? no, Mr. Ratigan, "
    "Fidget, Tamatoa, Te Kā? no, Dragón Chino? no, Shan Yu? no, el halcón de Shan Yu, King Candy? no, Turbo? no, Bellwether=Dawn Bellwether, Duke Weaselton? no, "
    "Mr. Big? no, Lord Business? no, Dr. Calico? no, Waternoose=Henry J. Waternoose, Randall=Randall Boggs, Charles Muntz? no, Alpha=Alfa, Lotso Abrazos, "
    "Big Baby? no, el Abuelo Fritz? no, Sykes? no, Hans? no, el Rey Pingüino? no, Dr. Blowhole, Skipper? no, Foosa=los fosas, Makunga, Chantel DuBois? no, "
    "Fossa, Vitaly? no, el Gran Mono=Mono? no, Scrat? no, Rata Ratatouille? no, Skinner? no, Jabberjaw? no, El Gato con Botas? no, Ozzie? no, Hopper, "
    "Grasshoppers=saltamontes, Molt, Thumper? no, Taran? no, Jefe? no, el Cuervo Diablo=Diablo=el cuervo de Maléfica, Gravedigger? no, Mr. Fox? no, "
    "Rata Templeton? no, Ruber? no, Cerebro, Pinky? no, Grimbo? no, Mumm-Ra? no, Kaa de El libro de la selva, Tabaqui, Akela? no, Vultures? no",
 4: "Sharptooth=Diente Afilado, Carnotauro, Red Claw? no, Kron, Carnivore? no, General Woundwort=el general Woundwort, Cluny, Jenner, Sly? no, Ripper? no, "
    "Carface=Carface Carruthers, Killer, Kaiser? no, Warren T. Rat? no, Cat R. Waul, Tiger? no, Jenner la rata, Bill Sykes? no, Ratcliffe? no, "
    "Rourke? no, Rex? no, Dr. Wolfe? no, Jacques? no, Uncle Max? no, Mr. Blik? no, Clockwerk, Le Paradox? no, Mojo, HIM? no, Sedusa? no, Fuzzy Lumpkins? no, "
    "Princesa? no, Shego? no, Dr. Drakken? no, Monkey Fist? no, Kat? no, Felonious Gru? no, Vector? no, El Macho? no, Scarlet? no, Herb? no, "
    "Bowser Jr., Dry Bowser, Kamek, King K. Rool=King K Rool, Ridley, Ganon? no, Ganondorf? no, King Dedede=Rey Dedede, Dr. Neo Cortex? no, Ripto, "
    "Gnasty Gnorc, Dark Kat? no, Nemesis? no, Lizard=Lagarto, Kraven? no, Black Cat=Gata Negra, "
    "Penguin? no, Man-Bat, Catwoman? no, Ratcatcher? no, Zartan? no, Beast? no, "
    "Tamatoa el cangrejo, Hopper el saltamontes, Shenzi, Banzai, Kovu, Vitani, Nala? no, Zira la leona, Shere Khan el tigre, Kaa la serpiente, Scar el león",
},
"estanco": {
 1: "tabaco=cigarrillos=cigarros=paquete de tabaco=cajetilla, mecheros=mechero=encendedor, sellos=sello, puros=puro, papel de fumar=papelillo=papel, "
    "filtros=boquillas, tabaco de liar, lotería? no, chicles=chicle",
 2: "Marlboro, Winston, Camel, Lucky Strike=Lucky, Chesterfield, Ducados, Fortuna, Nobel, Pall Mall, L&M, Philip Morris, Golden Virginia, Pueblo, Smoking, "
    "OCB, Rizla=Rizla+, Clipper, Zippo, Bic, cerillas, vapeador=vaper=cigarro electrónico=cigarrillo electrónico, líquidos de vapeo=líquidos para vapear, "
    "Iqos=IQOS, cartuchos=cartuchos de Iqos=heets, pipas=pipa=tabaco de pipa, cachimba=shisha=tabaco de cachimba=hookah, Bono Bus? no, "
    "abono transporte? no, tarjeta de transporte, tarjeta prepago=recargas de móvil=recarga del móvil, papel timbrado=impresos, recibos? no, "
    "tarjetas regalo, golosinas=chuches, caramelos, mapa? no, postales=postal, sobres, Juegos? no, cartas=baraja, impresos oficiales, multas? no",
 3: "Montecristo, Cohiba, Partagás, Romeo y Julieta, Davidoff, Vegafina, Farias, Café Crème=Cafe Creme, Dux, Willem II, purito=puritos, "
    "Winston Classic? no, Marlboro Gold, Camel Blue, West, JPS=John Player Special, Gauloises, Gitanes, Celtas, Bisonte, Coronas? no, Royale? no, "
    "Mallorca? no, Lark? no, Benson & Hedges, Dunhill, Rothmans, Kent, Vogue, Karelia, Peter Stuyvesant? no, Rex? no, American Spirit, Manitou, "
    "Cutters, Domingo, Amber Leaf, Drum, Old Holborn, Van Nelle, Pueblo Classic, Mascotte, Raw, Smoking Brown, Gizeh, Elements, Pay-Pay, Bambú, "
    "boquillas de cartón, filtros Swan, filtros de carbón, liadora=maquinita de liar, entubadora=máquina de entubar, tubos de cartón=tubos, "
    "picadora=grinder, ceniceros=cenicero, petaca, pitillera, cortapuros=guillotina, humidor, cajas de puros, gas para mecheros=recarga de gas, "
    "piedras de mechero, mechas, mechero de soplete, mechero eléctrico, vaper desechable=pod desechable=Elf Bar, resistencias=coils, baterías, "
    "Glo, Juul, Vuse, Blu, Myblu, heets? no, terea, bolsitas de nicotina=snus=Velo=Zyn, tabaco de mascar, rapé, sellos de correos, sobres prefranqueados, "
    "Correos? no, estampillas, papel de carta, bolígrafos? no, pilas, cargadores? no, lotería nacional? no, quiniela? no, Euromillones? no, "
    "Primitiva? no, cupón de la ONCE? no, rasca? no, revistas? no, periódicos? no, abono de la EMT? no, tarjeta de aparcamiento=ORA=tique de la ORA, "
    "modelo de impuestos=impresos de Hacienda, papel de multas? no, letras de cambio, efectos timbrados=timbres, pólizas, papel de pagos al Estado, tasas",
 4: "Trinidad, H. Upmann, Hoyo de Monterrey, Bolívar, Punch, Ramón Allones, Cuaba, Vegas Robaina, San Cristóbal, Quintero, José L. Piedra, "
    "Arturo Fuente, Padrón, Macanudo, Ashton, Oliva, Rocky Patel, Toscano, Clubmaster, Al Capone, Handelsgold, Mehari's, Panter, Agio, Ritmeester, "
    "Winterman's, Balmoral, Partagás Serie D, Behike, Siglo VI, Robusto=robustos, Corona=coronas, Churchill, Petit Corona, Culebras, "
    "picadura, tabaco de hebra, tabaco negro, tabaco rubio, Golden Virginia Yellow, Interval? no, Fine Cut? no, tabaco Al Fakher=Al Fakher, Adalya, "
    "Nakhla, Starbuzz, carbón de cachimba=carbones, mangueras de cachimba, cazoletas, Kaloud? no, papel de aluminio? no, "
    "boquillas desechables, encendedor de puros, mechero de turbo, mechero Clipper, pedernal, estuches, fundas de mechero, pegatinas? no, "
    "sellos de colección? no, sobres de correo certificado? no, impreso de alegaciones? no, papel timbrado del Estado, papel de oficio, pólizas de seguros? no",
},
})
