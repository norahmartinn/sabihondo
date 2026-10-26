"""Junta los siete CSV de datos/siete en el banco del juego.

Uso:  python3 scripts/siete/monta.py
Escribe un banco/NN.json por pregunta y reescribe `const PREGUNTAS` y `const CALENDARIO` en index.html.
Las preguntas nuevas se añaden SIEMPRE al final de PREGUNTAS (el número de archivo es su posición).
Qué siete salen cada día lo dice datos/calendario.csv: fecha;slug;slug;slug;slug;slug;slug;slug
Para rehacer un CSV, lanza antes el script de esa pregunta (apellidos.py, capitales.py…).

Formato de banco/NN.json: {q, t:[nivel1..nivel5]}. Cada respuesta es [texto, [claves]], o solo el texto
cuando su única clave es la del propio texto (el juego la calcula al cargar; así los apellidos pesan la mitad)."""
from comun import *

PREGUNTAS = [
    ("Nombra algo que hay en una boda", "boda"),
    ("Nombra una marca de cerveza", "cervezas"),
    ("Nombra una marca de relojes", "relojes"),
    ("Nombra una canción de Taylor Swift", "taylor"),
    ("Nombra un apellido español", "apellidos"),
    ("Nombra una carrera universitaria", "carreras"),
    ("Nombra la capital de un país", "capitales"),
    # segunda tanda (tanda2.py), semana del 7 al 11 de octubre de 2026
    ("Nombra un supermercado", "supermercados"),
    ("Nombra una marca de zapatillas", "zapatillas"),
    ("Nombra un streamer o youtuber español", "youtubers"),
    ("Nombra un Pokémon de la primera generación", "pokemon"),
    ("Nombra un miedo o una fobia", "fobias"),
    ("Nombra un color", "colores"),
    ("Nombra una prenda de ropa", "prendas"),
    ("Nombra un medio de transporte", "transporte"),
    ("Nombra un electrodoméstico", "electrodomesticos"),
    ("Nombra un idioma", "idiomas"),
    ("Nombra una fiesta de España", "fiestas"),
    ("Nombra un rapero o trapero español", "raperos"),
    ("Nombra una empresa del IBEX 35", "ibex"),
    ("Nombra un nombre vasco", "nombres_vascos"),
    ("Nombra una discoteca", "discotecas"),
    ("Nombra un juego de cartas", "cartas"),
    ("Nombra un DJ", "dj"),
    ("Nombra un personaje de Shrek", "shrek"),
    ("Nombra un personaje de Harry Potter", "hp"),
    ("Nombra un personaje de Bob Esponja", "bob"),
    ("Nombra una película de miedo", "miedo"),
    ("Nombra un anime", "anime"),
    ("Nombra un personaje de Mario Kart", "mariokart"),
    ("Nombra un juego de móvil", "movil"),
    ("Nombra algo del menú de McDonald's", "mcdonalds"),
    ("Nombra una marca de coche de lujo", "coches_lujo"),
    ("Nombra un país donde se conduce por la izquierda", "paises_izquierda"),
    ("Nombra un país con rey o reina", "paises_rey"),
    ("Nombra una ciudad de Italia", "italia"),
    ("Nombra un país del mundo", "paises"),
    ("Nombra una estación del Metro de Madrid", "metro"),
    ("Nombra un clásico de animación de Disney", "disney"),
    ("Nombra una canción de los Beatles", "beatles"),
    ("Nombra un equipo que haya jugado en Primera División", "primera"),
    ("Nombra una palabra que empiece por Ñ", "enie"),
    # tercera tanda (tanda3.py), semana del 12 al 18 de octubre de 2026
    ("Nombra una zona de una casa", "casa"),
    ("Nombra una canción de Quevedo", "quevedo"),
    ("Nombra un sabor de pizza", "pizza"),
    ("Nombra una orientación sexual", "orientaciones"),
    ("Nombra un personaje de La que se avecina", "lqsa"),
    ("Nombra un personaje de Doraemon", "doraemon"),
    ("Nombra un superhéroe de Marvel", "marvel"),
    ("Nombra una película que haya ganado el Óscar a mejor película", "oscar"),
    ("Nombra una canción de One Direction", "onedirection"),
    ("Nombra una canción de ABBA", "abba"),
    ("Nombra un festival de música de España", "festivales"),
    ("Nombra un género musical", "generos"),
    ("Nombra un estadio de fútbol de España", "estadios"),
    ("Nombra un deporte olímpico", "olimpicos"),
    ("Nombra un vino con denominación de origen", "vinos"),
    ("Nombra un tipo de pasta", "pasta"),
    ("Nombra un bollo industrial", "bollos"),
    ("Nombra un snack de bolsa", "snacks"),
    ("Nombra una salsa", "salsas"),
    ("Nombra una isla de España", "islas"),
    ("Nombra un sitio de España que sea Patrimonio de la Humanidad", "patrimonio"),
    ("Nombra un aeropuerto de España", "aeropuertos"),
    ("Nombra un barrio de Madrid", "barrios_madrid"),
    ("Nombra un Parador de España", "paradores"),
    ("Nombra una universidad de España", "universidades"),
    ("Nombra un ministerio del Gobierno", "ministerios"),
    ("Nombra un país sin salida al mar", "sin_mar"),
    ("Nombra un país que sea una isla", "paises_isla"),
    ("Nombra un estado de Estados Unidos", "estados_eeuu"),
    ("Nombra una aerolínea", "aerolineas"),
    ("Nombra una marca cuyo logo sea un animal", "logo_animal"),
    ("Nombra una unidad de medida", "unidades"),
    ("Nombra una palabra con las cinco vocales", "cinco_vocales"),
    ("Nombra una palabra que empiece por K", "palabras_k"),
    ("Nombra una letra del alfabeto griego", "griego"),
    ("Nombra un tiempo verbal", "tiempos"),
    ("Nombra una figura retórica", "figuras"),
    ("Nombra una forma de decir dinero", "dinero"),
    ("Nombra una palabra inglesa que usamos en español", "anglicismos"),
    ("Nombra un partido político con escaños en el Congreso", "partidos"),
    ("Nombra un escritor de la Generación del 27", "gen27"),
    ("Nombra un juego de Mario", "mario"),
    ("Nombra uno de los nombres más puestos a los bebés", "nombres_bebes"),
    ("Nombra un impuesto", "impuestos"),
    ("Nombra un pódcast español", "podcasts"),
    ("Nombra un nombre compuesto", "nombres_compuestos"),
    ("Nombra una señal de tráfico", "senales"),
    ("Nombra un país con verde en la bandera", "verde_bandera"),
    ("Nombra un país que haga frontera con Afganistán", "frontera_afganistan"),
    ("Nombra un país que haga frontera con Kenia", "frontera_kenia"),
    # cuarta tanda (tanda4.py), semana del 19 al 25 de octubre de 2026
    ("Nombra un helado de Frigo", "frigo"),
    ("Nombra un refresco", "refrescos"),
    ("Nombra un producto Hacendado", "hacendado"),
    ("Nombra un artista que haya ido a Eurovisión por España", "eurovision"),
    ("Nombra un personaje de Friends", "friends"),
    ("Nombra un personaje de Phineas y Ferb", "phineas"),
    ("Nombra un circuito de Fórmula 1", "circuitos_f1"),
    ("Nombra una provincia de España", "provincias"),
    ("Nombra un país donde se hable francés", "francofonos"),
    ("Nombra una palabra que empiece por X", "palabras_x"),
    ("Nombra una palabra esdrújula", "esdrujulas"),
    ("Nombra un filósofo", "filosofos"),
    ("Nombra una batalla o una guerra", "batallas"),
    ("Nombra un hueso del cuerpo", "huesos"),
    ("Nombra un músculo", "musculos"),
    ("Nombra una profesión", "profesiones"),
    ("Nombra una artista mujer con más de 500.000 oyentes mensuales en Spotify", "artistas"),
    ("Nombra un idioma que sea el más hablado en al menos dos países", "idiomas_paises"),
    ("Nombra un personaje de Peter Pan", "peter_pan"),
    ("Nombra un pronombre", "pronombres"),
    ("Nombra un tipo de masa de agua", "masas_agua"),
    ("Nombra una ciencia o disciplina que acabe en -logía", "logias"),
    ("Nombra una palabra que contenga «inter»", "inter"),
    ("Nombra un producto de Bimbo", "bimbo"),
    ("Nombra un producto de Nestlé", "nestle"),
    ("Nombra un producto de Apple", "apple"),
    ("Nombra un sabor de helado", "sabores_helado"),
    ("Nombra un dulce de Navidad", "dulces_navidad"),
    ("Nombra un personaje de The Big Bang Theory", "bigbang"),
    ("Nombra un personaje de The Office", "office"),
    ("Nombra un personaje de Modern Family", "modern_family"),
    ("Nombra una saga de películas", "sagas"),
    ("Nombra una escudería de Fórmula 1", "escuderias"),
    ("Nombra un deporte acuático", "deportes_acuaticos"),
    ("Nombra una prueba de los Juegos de Invierno", "juegos_invierno"),
    ("Nombra un pueblo de la Comunidad de Madrid", "pueblos_madrid"),
    ("Nombra un país donde se hable español", "hispanohablantes"),
    ("Nombra una palabra con diéresis", "dieresis"),
    ("Nombra una expresión en latín que usamos", "latin"),
    ("Nombra una corriente filosófica", "corrientes"),
    ("Nombra una hormona", "hormonas"),
    ("Nombra una especialidad médica", "especialidades"),
    ("Nombra un formato de archivo", "formatos"),
    ("Nombra una marca de The Coca-Cola Company", "cocacola"),
    ("Nombra una enfermedad que acabe en -itis", "itis"),
    ("Nombra una unidad de tiempo", "unidades_tiempo"),
    ("Nombra una canción de Olivia Rodrigo", "olivia"),
    ("Nombra un gas", "gases"),
    ("Nombra un mineral", "minerales"),
    ("Nombra un icono de Halloween", "halloween"),
    ("Nombra un número 1 de Los 40", "los40"),
    # quinta tanda (tanda5.py), semana del 26 de octubre al 1 de noviembre de 2026
    ("Nombra algo que te cobran las aerolíneas", "cobros_aerolineas"),
    ("Nombra una parte del cuerpo de la que solo tenemos una", "cuerpo_uno"),
    ("Nombra un personaje de Juego de Tronos", "jdt"),
    ("Nombra una serie de Disney Channel", "disney_channel"),
    ("Nombra una serie de Netflix", "netflix"),
    ("Nombra una película de Pixar", "pixar"),
    ("Nombra una canción de Bad Bunny", "badbunny"),
    ("Nombra una canción de Disney", "canciones_disney"),
    ("Nombra un instrumento musical", "instrumentos"),
    ("Nombra una fruta", "frutas"),
    ("Nombra una verdura u hortaliza", "verduras"),
    ("Nombra un tipo de café", "cafes"),
    ("Nombra un plato típico de una comunidad autónoma", "platos_ccaa"),
    ("Nombra una marca del grupo Inditex", "inditex"),
    ("Nombra un producto de maquillaje", "maquillaje"),
    ("Nombra un juego de mesa", "juegos_mesa"),
    ("Nombra una jugada del póker", "poker"),
    ("Nombra una palabra del mus", "mus"),
    ("Nombra un jugador del Barça", "barca"),
    ("Nombra una palabra que empiece por W", "palabras_w"),
    ("Nombra un gentilicio", "gentilicios"),
    ("Nombra una palabra que tenga doble ere", "doble_rr"),
    ("Nombra una palabra que acabe en -ción", "cion"),
    ("Nombra una criatura mitológica", "criaturas"),
    ("Nombra un perro o gato famoso", "mascotas_famosas"),
    ("Nombra un presidente del Gobierno de España", "presidentes"),
    ("Nombra un cuadro famoso", "cuadros"),
    ("Nombra algo que tenga ruedas", "ruedas"),
    ("Nombra algo que haya en un hospital", "hospital"),
    ("Nombra una película que haya estado en los cines este año", "pelis2026"),
    ("Nombra un deporte que se juegue sin pelota", "sin_pelota"),
    # Halloween: la primera de cada día del 27 de octubre al 1 de noviembre
    ("Nombra una película de terror o de Halloween", "terror_halloween"),
    ("Nombra algo asociado a una bruja de cuento", "bruja_cuento"),
    ("Nombra algo que asocies con un vampiro", "vampiro"),
    ("Nombra algo que asocies con un hombre lobo", "hombre_lobo"),
    ("Nombra una película de Tim Burton", "tim_burton"),
    ("Nombra una moneda que valga menos que el euro", "monedas_euro"),
    ("Nombra algo que se suele expresar en porcentaje (%)", "porcentajes"),
    ("Nombra algo que se usa para darle a la pelota en algún deporte", "golpear_pelota"),
    ("Nombra un país de África", "paises_africa"),
    ("Nombra algo que se lleva a la playa", "playa"),
    ("Nombra un sabor de patatas fritas", "sabores_patatas"),
    ("Nombra un tipo de bolso o de bolsa", "bolsos"),
    ("Nombra algo que te llevas de camping", "camping"),
]

banco = RAIZ / "banco"
for viejo in banco.glob("*.json"): viejo.unlink()
indice = []
for i, (q, slug) in enumerate(PREGUNTAS):
    niveles, usadas = [[] for _ in range(5)], set()
    with open(DATOS / f"{slug}.csv", encoding="utf-8") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            claves = []
            for txt in [fila["respuesta"]] + [a for a in fila["alias"].split("|") if a]:
                k = clave(txt)
                if k and k not in usadas: usadas.add(k); claves.append(k)
            if not claves: continue
            r = fila["respuesta"]
            niveles[int(fila["nivel"]) - 1].append(r if claves == [clave(r)] else [r, claves])
    n = sum(map(len, niveles))
    (banco / f"{i:02d}.json").write_text(json.dumps({"q": q, "t": niveles}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    indice.append({"q": q, "n": n})
    print(f"{i:02d} {q}: {n} respuestas, {(banco / f'{i:02d}.json').stat().st_size // 1024} KB")

# calendario: cada fecha con sus siete preguntas, en el orden en que salen
slugs = [s for _, s in PREGUNTAS]
calendario, usadas = {}, {}
with open(RAIZ / "datos" / "calendario.csv", encoding="utf-8") as f:
    for fila in csv.reader(f, delimiter=";"):
        if not fila or fila[0].startswith("#") or fila[0] == "fecha": continue
        fecha, del_dia = fila[0].strip(), [x.strip() for x in fila[1:] if x.strip()]
        assert len(del_dia) == 7 and len(set(del_dia)) == 7, f"{fecha}: hacen falta 7 preguntas distintas"
        for x in del_dia:
            assert x in slugs, f"{fecha}: no existe la pregunta «{x}»"
            if x in usadas: print(f"  aviso: «{x}» sale el {usadas[x]} y otra vez el {fecha}")
            usadas[x] = fecha
        calendario[fecha] = [slugs.index(x) for x in del_dia]
print(f"calendario: {len(calendario)} días, hasta el {max(calendario)}")
print("sin fecha todavía:", [x for x in slugs if x not in usadas] or "ninguna")

html = (RAIZ / "index.html").read_text(encoding="utf-8")
bloque = ("const PREGUNTAS=" + json.dumps(indice, ensure_ascii=False, separators=(",", ":")) + ";\n"
          + "const CALENDARIO=" + json.dumps(calendario, separators=(",", ":")) + ";")
nuevo, veces = re.subn(r"const PREGUNTAS=\[.*?\];(\s*const CALENDARIO=\{.*?\};)?", lambda m: bloque, html, count=1, flags=re.S)
assert veces == 1
(RAIZ / "index.html").write_text(nuevo, encoding="utf-8")
