# Sabihondo

Reto diario al estilo Wordle. Cada día salen siete preguntas abiertas, las mismas para todo el mundo ("Nombra una provincia de España", "Nombra un Pokémon de la primera generación"). Vale cualquier respuesta correcta, pero cuanto más rara sea, más metros bajas por el iceberg. Si solo dices lo obvio, te quedas en la punta.

## Cómo puntúa

Cada respuesta cae en uno de cinco niveles:

| Nivel | Qué es | Metros |
|---|---|---|
| 1 · Superficie | Lo primero que se le pasa a cualquiera por la cabeza | 10 |
| 2 · Conocido | No es lo primero que sale, pero casi todo el mundo lo sabe | 30 |
| 3 · Raro | Aquí ya hay que haberse fijado | 60 |
| 4 · Muy raro | De alguien que sabe del tema de verdad | 85 |
| 5 · Sabihondo | La joya del día | 100 |

El fondo está a 700 m. De un iceberg solo asoma el 10 %, y aquí igual: siete respuestas de superficie suman 70 m y te dejan en la línea de flotación.

## Cómo está hecho

- Un solo `index.html` sin build: HTML, CSS y JavaScript a mano. El iceberg es un SVG que se dibuja según el tamaño de pantalla.
- Las preguntas y respuestas salen de `datos/banco.csv`. `python3 scripts/banco.py` lo convierte y lo mete en `index.html`: arregla enunciados, añade alias (por ejemplo, "Asturias" para "Principado de Asturias" o "Bruselas" para "Brussels") y aplica `scripts/extras.py` y `scripts/nuevas.py`, que corrigen niveles de las categorías cerradas y añaden respuestas que faltaban. Cada cambio queda listado en `datos/revision_claude.csv` para revisarlo.
- Si el juego rechaza una respuesta que alguien cree correcta, puede avisar con un botón y queda guardada en la tabla `sabihondo_sugerencias` para revisarla.
- Además, en las categorías abiertas (ciudades, playas, picos, películas, cantantes…) se cargan unas 53.000 respuestas de **Wikidata** con `python3 scripts/wikidata.py` (consultas vía QLever; datos CC0). Su nivel sale de en cuántas Wikipedias aparece cada cosa, comparado con el resto de su categoría, y nunca pasa de nivel 3.
- Cada pregunta vive en su propio archivo (`banco/NN.json`): la página solo descarga las siete del día.
- Las preguntas del día salen de un generador pseudoaleatorio con semilla fija por fecha (hora de Madrid), así que todo el mundo recibe las mismas.
- Las respuestas se comparan sin tildes y con margen para erratas (distancia de Levenshtein).
- Cuentas con email y contraseña en **Supabase**. La racha y las puntuaciones de cada día se guardan en la tabla `sabihondo_partidas`, protegida con RLS: cada persona solo puede leer y guardar sus propias partidas. Sin cuenta, todo se guarda en el navegador, y esas partidas se suben al crear una.
- Alojado en GitHub Pages.

## Puesta en marcha

1. En Supabase, pega `supabase/schema.sql` en el editor SQL y ejecútalo.
2. En *Authentication → Providers → Email*, deja **Confirm email** desactivado. Si está activado, el SMTP de serie manda muy pocos correos y la gente no puede entrar.
3. `SB_URL` y `SB_KEY` están al principio de la sección de cuenta de `index.html`. La clave es la publicable, pensada para ir en el navegador.

## El banco de las siete preguntas

Desde octubre de 2026 el juego tiene siete preguntas fijas. Cada una tiene su script en `scripts/siete/`, que deja un CSV en `datos/siete/` (respuesta; alias; nivel; métrica). `python3 scripts/siete/monta.py` junta los siete en `banco/00.json`…`06.json` y actualiza `const PREGUNTAS` en `index.html`.

| Pregunta | De dónde sale la lista | Qué decide el nivel |
|---|---|---|
| Apellido español | INE, apellidos con 20 personas o más (censo 1-1-2025) | Cuánta gente lo lleva |
| Carrera universitaria | RUCT, grados en alta | En cuántas universidades se estudia |
| Canción de Taylor Swift | Wikipedia en inglés, canciones publicadas | Reproducciones en Spotify (kworb.net) |
| Capital de un país | Wikidata, Estados soberanos | Visitas en Wikipedia (español + inglés) |
| Marca de cerveza | Wikidata + marcas del mercado español | A mano las conocidas en España; el resto, ediciones de Wikipedia |
| Marca de relojes | Categorías de Wikipedia en inglés + marcas de joyería española | A mano las conocidas en España; el resto, visitas en Wikipedia |
| Algo que hay en una boda | Hecha a mano | A mano |

Los CSV se pueden corregir a mano (cambiar un nivel, añadir un alias) y volver a lanzar `monta.py`; si se relanza el script de una pregunta, su CSV se regenera y se pierden esos retoques.
