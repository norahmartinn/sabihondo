// Sabihondo · el juez.
// Cuando una respuesta no está en el banco, el juego pregunta aquí si es válida
// y lo rara que es. La IA (Groq) decide una vez; el veredicto se guarda en
// sabihondo_ia y las siguientes veces se responde desde ahí, sin gastar IA.
import { createClient } from "npm:@supabase/supabase-js@2";

const ORIGENES = ["https://norahmartinn.github.io", "http://localhost:8000", "http://127.0.0.1:8000"];
const MODELO = "openai/gpt-oss-120b";
const CRITERIO = "v3";      // si cambian las instrucciones, lo rechazado antes se vuelve a juzgar
const RESERVA = "openai/gpt-oss-20b";   // si el grande está saturado (límite por minuto de Groq), este tiene su propio límite
const TOPE_DIARIO = 1800;   // consultas nuevas a la IA por día, como mucho

const cors = (origen: string | null) => ({
  "Access-Control-Allow-Origin": origen && ORIGENES.includes(origen) ? origen : ORIGENES[0],
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Vary": "Origin",
});

// igual que compacta() del juego: minúsculas, sin tildes, sin artículos y sin espacios
const FUERA = new Set(["el","la","los","las","lo","un","una","unos","unas","de","del","al","a","en","y","o"]);
const compacta = (s: string) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
  .replace(/[^a-z0-9]+/g, " ").split(" ").filter((w) => w && !FUERA.has(w)).join("");

const INSTRUCCIONES = `Eres el juez de Sabihondo, un juego español de preguntas abiertas.
Te doy un enunciado («Nombra un…») y la respuesta que ha escrito un jugador.

Decide si la respuesta es VÁLIDA: tiene que ser algo real que existe y que encaja de verdad en el enunciado.
- Perdona faltas de ortografía, tildes, mayúsculas, nombres en otro idioma, apodos y formas populares («gas de la risa» por óxido nitroso).
- Sé generoso con la FORMA: si se entiende a qué se refiere y un jugador razonable la daría por buena, vale.
- Sé estricto con los HECHOS: comprueba que de verdad encaja. Una marca de otra empresa (Cola Cao no es de Nestlé), una canción de otro artista
  o un personaje de otra serie NO es válida. Si no sabes con seguridad que es cierto, no es válida.
- Rechaza también: chistes, cosas inventadas, palabras demasiado genéricas («fruta», «una cosa»), respuestas de otra categoría o la propia palabra del enunciado.

Si es válida, da el nombre bien escrito (como se conoce en España) y un nivel de rareza pensando en un jugador español medio:
1 = lo primero que se le ocurre a casi todo el mundo
2 = conocido, pero no lo primero
3 = hay que saber algo del tema
4 = de alguien que sabe mucho del tema
5 = casi nadie lo diría

Te paso también ejemplos de respuestas que ya están en la lista, por nivel: úsalos para medir la rareza.
Si la respuesta del jugador es otra forma de decir una de esas, dale ese mismo nombre y nivel.

Responde SOLO con JSON: {"valida": true|false, "nombre": "…", "nivel": 1-5, "motivo": "una frase corta"}`;

Deno.serve(async (req) => {
  const origen = req.headers.get("origin");
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(origen) });
  const responde = (datos: unknown, estado = 200) =>
    new Response(JSON.stringify(datos), { status: estado, headers: { ...cors(origen), "Content-Type": "application/json" } });

  let pregunta = "", respuesta = "", ejemplos: unknown = [];
  try { ({ pregunta, respuesta, ejemplos } = await req.json()); } catch { return responde({ error: "json" }, 400); }
  // ejemplos: hasta 6 respuestas de la lista por nivel (1 a 5), para calibrar la rareza
  const muestra = (Array.isArray(ejemplos) ? ejemplos : []).slice(0, 5)
    .map((n, i) => `${i + 1}: ${(Array.isArray(n) ? n : []).slice(0, 6).map((x) => String(x).slice(0, 60)).join(", ")}`).join("\n");
  pregunta = String(pregunta ?? "").trim().slice(0, 200);
  respuesta = String(respuesta ?? "").trim().slice(0, 120);
  const clave = compacta(respuesta);
  if (!pregunta.startsWith("Nombra") || clave.length < 2) return responde({ error: "entrada" }, 400);

  const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

  // 1. ¿ya lo juzgamos?
  const { data: previo } = await db.from("sabihondo_ia").select("valida,nombre,nivel,modelo")
    .eq("pregunta", pregunta).eq("clave", clave).maybeSingle();
  // lo juzgado con unas instrucciones anteriores se vuelve a mirar
  if (previo && previo.modelo === `${MODELO}#${CRITERIO}`)
    return responde({ valida: previo.valida, nombre: previo.nombre, nivel: previo.nivel, cache: true });

  // 2. tope diario para que nadie agote la IA
  const hoy = new Date().toISOString().slice(0, 10);
  const { count } = await db.from("sabihondo_ia").select("*", { count: "exact", head: true }).gte("created_at", hoy);
  if ((count ?? 0) >= TOPE_DIARIO) return responde({ valida: false, sin_juez: true });

  // 3. pregunta a la IA (y, si el modelo grande está saturado, al pequeño)
  const pide = (modelo: string) => fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: { "Authorization": `Bearer ${Deno.env.get("GROQ_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      model: modelo, temperature: 0, reasoning_effort: "low", max_completion_tokens: 900, response_format: { type: "json_object" },
      messages: [{ role: "system", content: INSTRUCCIONES },
                 { role: "user", content: `Enunciado: ${pregunta}\n${muestra ? `Ejemplos de la lista por nivel:\n${muestra}\n` : ""}Respuesta del jugador: ${respuesta}` }],
    }),
  });
  let r = await pide(MODELO);
  if (!r.ok) r = await pide(RESERVA);
  if (!r.ok) return responde({ valida: false, sin_juez: true });
  let v: { valida?: boolean; nombre?: string; nivel?: number; motivo?: string } = {};
  try { v = JSON.parse((await r.json()).choices[0].message.content); } catch { return responde({ valida: false, sin_juez: true }); }

  const fila = {
    pregunta, clave, respuesta,
    valida: v.valida === true,
    nombre: String(v.nombre || respuesta).slice(0, 120),
    nivel: Math.min(5, Math.max(1, Math.round(Number(v.nivel) || 3))),
    motivo: String(v.motivo || "").slice(0, 300),
    modelo: `${MODELO}#${CRITERIO}`,
  };
  await db.from("sabihondo_ia").upsert(fila, { onConflict: "pregunta,clave" });
  return responde({ valida: fila.valida, nombre: fila.nombre, nivel: fila.nivel });
});
