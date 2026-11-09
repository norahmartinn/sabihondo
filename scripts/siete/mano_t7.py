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
