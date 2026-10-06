"""Cosas que hay en una boda. Aquí no existe una base de datos: la lista y los niveles están hechos
a mano. Nivel 1 es lo que diría cualquiera; nivel 5, el detalle en el que casi nadie cae.
Cuando haya partidas guardadas, los niveles se pueden recalcular con lo que responda la gente."""
from comun import *

MANO = {
1: """la novia: novia|novios|los novios|pareja
el novio
la tarta: tarta nupcial|pastel|tarta de boda|pastel de boda
los anillos: anillo|alianzas|alianza|anillos de boda
los invitados: invitado|gente|familia|amigos|familiares
el vestido de novia: vestido|vestido blanco|traje de novia
el arroz
el ramo: ramo de novia|ramo de flores|bouquet
el banquete: comida|cena|convite|comilona
el baile: bailar|música|pista de baile""",
2: """el cura: sacerdote|párroco|padre
el padrino: padrinos
la madrina
las damas de honor: dama de honor
el fotógrafo: fotógrafa|fotos|fotografías|cámara|cámara de fotos
el DJ: disc jockey|pinchadiscos|discjockey
el vals: primer baile|baile de los novios|baile nupcial
el brindis: brindar
el champán: cava|champagne|champaña
las flores: decoración floral|arreglos florales
el velo
el traje: traje del novio|trajes|esmoquin|smoking|chaqué
la iglesia: capilla|ermita|catedral
las mesas: mesa|mesas redondas
la barra libre: barra|copas|alcohol|bebida|bebidas|cubatas
los regalos: regalo|regalos de boda
los sobres: sobre|sobre con dinero|dinero
el beso: besos|beso de los novios
los votos: votos matrimoniales|promesas|el sí quiero|sí quiero
los testigos: testigo
el cóctel: aperitivo|aperitivos|canapés|pinchos|entrantes
el coche de los novios: coche nupcial|limusina|coche|coche clásico|coche antiguo
el discurso: discursos|speech|palabras
la orquesta: banda|grupo de música|música en directo
las invitaciones: invitación|tarjeta de invitación
el altar
los pétalos: pétalos de rosa
los niños: pajes|paje|niños de arras
la corbata
los tacones: zapatos de tacón|zapatos
las lágrimas: llorar|llantos|lloros|emoción
la ceremonia: misa|boda|enlace
el vino: vino tinto|vino blanco
los camareros: camarero|camarera|catering""",
3: """la liga
las arras: monedas
el seating plan: plano de mesas|seating|lista de mesas|sitting
el photocall: fotocall|foto call
el candy bar: mesa dulce|mesa de chuches|chuches|golosinas
los detalles para los invitados: detalles|recuerdos|detallitos|regalos para invitados|detalle
los puros: puro|habanos
cortar la corbata: corte de la corbata|subasta de la corbata
lanzar el ramo: tirar el ramo|lanzamiento del ramo
los muñecos de la tarta: figuritas de la tarta|figuras de la tarta|muñecos|novios de la tarta
el vídeo: videógrafo|vídeo de boda|videocámara
el jamón: cortador de jamón|jamonero|jamón ibérico
los centros de mesa: centro de mesa
el menú: minuta|minutas|carta
el tocado: tocados
la pamela: pamelas|sombrero
la pajarita
los gemelos
la cola del vestido: cola
la mantilla: peineta
el juez: concejal|alcalde|oficiante|maestro de ceremonias
la alfombra: alfombra roja
el confeti: confetti
las bengalas: bengala|chispas
los conos de arroz: cucuruchos|cucuruchos de arroz
las lecturas: lectura|lectura de la biblia
el coro: cuarteto de cuerda|violines|violinista|coro rociero|cuarteto
la fuente de chocolate
la recena: resopón
las alpargatas para bailar: alpargatas|chanclas|zapatillas para bailar|bailarinas|manoletinas
el fotomatón: cabina de fotos|fotomaton
el libro de firmas: libro de visitas
la wedding planner: organizadora|organizador de bodas|wedding planner
la lista de bodas: lista de boda|número de cuenta
el primo borracho: borracho|borrachos|borrachera|el tío borracho
la suegra: suegro|suegros|consuegros
el autobús: autocar|bus|microbús
el arco de flores: arco|arco floral
las sillas: silla
la carpa
la finca: salón|salón de bodas|restaurante|hacienda|cortijo|masía|pazo
la tuna
los mariachis: mariachi
los fuegos artificiales: fuegos|castillo de fuegos|pirotecnia
los globos: globo
las velas: vela|velones
la conga
Paquito el Chocolatero: paquito chocolatero
el sorbete: sorbete de limón
el marisco: langostinos|gambas|mariscada|percebes|cigalas
el solomillo: carne|entrecot|cordero|cochinillo
los abanicos: abanico|paipái|pai pai
los pañuelos: pañuelo|clínex|kleenex|pañuelos de papel
la abuela: abuelos|abuelo|abuelas
el ex: exnovio|exnovia|la ex
las fotos de grupo: foto de grupo|foto de familia
el maquillaje: maquilladora|maquillador
el peinado: peluquera|peluquero|recogido|moño
la música de entrada: marcha nupcial
los vivas: vivan los novios|que se besen
el anillo de compromiso: pedida|anillo de pedida
la despedida: fin de fiesta|última canción""",
4: """el alfiler de novia: alfileres|alfiler
el cotillón: pelucas|gafas de fiesta|sombreros de fiesta|matasuegras|maracas
la hora loca
el kit de baño: cesta de baño|cesta del baño|kit de emergencia|cesta de aseo
el guardarropa: ropero
el food truck: foodtruck
el dron: drone
la espada para cortar la tarta: espada|sable
algo azul
algo prestado
algo viejo
algo nuevo
el cojín de las alianzas: portaalianzas|cojín|porta alianzas|anillero
el libro de familia
el acta: acta matrimonial|firma|firmas|firmar
la ofrenda del ramo: ofrenda a la Virgen|ofrenda
la salve rociera: salve
la mesa presidencial: mesa nupcial|mesa de los novios
la mesa de los niños: mesa infantil
la mesa de los solteros: solteros
los meseros: números de mesa|mesero
el cartel de bienvenida: cartel|pizarra|letrero
las letras gigantes: letras de luz|letras LOVE|letras luminosas|neón
los chupitos: chupito|licores|pacharán|licor de hierbas|orujo
el café
el pulpeiro: pulpo|pulpo a feira
la paella: arroz con bogavante
el queso: tabla de quesos|mesa de quesos|quesos
el castillo hinchable: hinchable|animadores|monitores|niñera|canguro
el perro: perro con pajarita|mascota
la calesa: coche de caballos|caballos|carruaje
los tirantes
el chaleco
el fajín
el bolso de mano: clutch|bolso|cartera de mano
el chal: estola|chaqueta|bolero|torera
el prendido: flor en la solapa|boutonniere|ramillete|flor del ojal
la tiara: corona de flores|diadema|corona
los pendientes: joyas|collar
las pompas de jabón: pomperos|burbujas
las guirnaldas de luces: luces|bombillas|guirnaldas|farolillos
el jardín: césped
los nervios
el calor
la lluvia: paraguas
la resaca
el cuñado: cuñada
los compañeros de trabajo: el jefe|jefe
el acompañante: más uno|plus one
los baños: baño|servicios
el parking: aparcamiento
la barra de gin-tonics: gintonics|gin tonic|barra de mojitos|mojitos|coctelería
la cerveza: cervezas|barril de cerveza|corner de cerveza
la servilleta: servilletas|manteles|mantel
la cubertería: cubiertos|vajilla|platos|copas de vino
el micrófono: micro
el playback: sorpresa|coreografía|flashmob|baile sorpresa|vídeo sorpresa
el traje regional: kilt|traje de gitana|traje de flamenca
las medias: medias de repuesto
las tiritas
el pasodoble
el reclinatorio
la pedida de mano: pedida de matrimonio""",
5: """el lazo nupcial: yugo|lazo
el velón: velón de la unidad|vela de la unidad
el portarramos
el cubrebotón: cubrebotones
el azahar: flor de azahar
el cancán: enaguas|miriñaque
las arras de plata
el aguamanil
el tálamo
la epístola: carta de san Pablo a los corintios|corintios|epístola de san Pablo
el corte de la liga: subasta de la liga
el baile del billete: baile del dinero
el mazapán
las peladillas: almendras garrapiñadas|peladilla|almendras
el arroz ecológico: semillas|alpiste|lavanda
los aviones de papel
las linternas voladoras: farolillos voladores|linternas chinas
el árbol de huellas: árbol de los deseos|cápsula del tiempo
el bodorrio
la corbata del padrino
el coche con latas: latas|latas en el coche|cartel de recién casados|recién casados
el gaitero: gaita|gaiteiro
la jota
la sardana
la muñeira
el aurresku: dantzari|txistulari
la sevillana: sevillanas|rumbas|rumba
el speech del mejor amigo: mejor amigo
el tío que baila sin chaqueta: tío bailando|bailar sin chaqueta
la servilleta al aire: servilletas al aire|revolear servilletas|agitar servilletas
el protocolo
el certificado de matrimonio: partida de matrimonio|expediente matrimonial
el monaguillo: monaguillos
el órgano: organista
el incienso
el misal: libro de misa|cancionero|misalito
el reportaje: preboda|postboda
la segunda puesta: segundo vestido
el neceser de la novia
las horquillas
el esmalte
el imperdible: imperdibles
la plancha: planchar
el coche escoba"""}

filas = []
for nv, bloque in MANO.items():
    for i, linea in enumerate(bloque.splitlines()):
        n, _, al = linea.partition(": ")
        filas.append((n.strip(), [a for a in al.split("|") if a], nv, 1000 - i))
guarda("boda", filas, "orden_a_mano")
