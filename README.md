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
- Las preguntas y respuestas salen de `datos/banco.csv` (73 preguntas, unas 5.000 respuestas con su nivel y la fuente de cada lista). `python3 scripts/banco.py` lo convierte y lo mete en `index.html`: arregla enunciados y añade alias (por ejemplo, "Asturias" para "Principado de Asturias" o "Hamilton" para "Lewis Hamilton").
- Las preguntas del día salen de un generador pseudoaleatorio con semilla fija por fecha (hora de Madrid), así que todo el mundo recibe las mismas.
- Las respuestas se comparan sin tildes y con margen para erratas (distancia de Levenshtein).
- Cuentas con email y contraseña en **Supabase**. La racha y las puntuaciones de cada día se guardan en la tabla `sabihondo_partidas`, protegida con RLS: cada persona solo puede leer y guardar sus propias partidas. Sin cuenta, todo se guarda en el navegador, y esas partidas se suben al crear una.
- Alojado en GitHub Pages.

## Puesta en marcha

1. En Supabase, pega `supabase/schema.sql` en el editor SQL y ejecútalo.
2. En *Authentication → Providers → Email*, deja **Confirm email** desactivado. Si está activado, el SMTP de serie manda muy pocos correos y la gente no puede entrar.
3. `SB_URL` y `SB_KEY` están al principio de la sección de cuenta de `index.html`. La clave es la publicable, pensada para ir en el navegador.
