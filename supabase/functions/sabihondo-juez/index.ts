// Sabihondo · el juez.
// Cuando una respuesta no está en el banco, el juego pregunta aquí si es válida
// y lo rara que es. La IA (Groq) decide una vez; el veredicto se guarda en
// sabihondo_ia y las siguientes veces se responde desde ahí, sin gastar IA.
import { createClient } from "npm:@supabase/supabase-js@2";

const ORIGENES = ["https://norahmartinn.github.io", "http://localhost:8000", "http://127.0.0.1:8000"];
const MODELO = "llama-3.3-70b-versatile";
const TOPE_DIARIO = 3000;   // consultas nuevas a la IA por día, como mucho

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
- Perdona faltas de ortografía, tildes, mayúsculas y nombres en otro idioma.
- Rechaza chistes, cosas inventadas, palabras genéricas («fruta», «una playa»), respuestas de otra categoría y cosas que no puedas confirmar.
- Si dudas, no es válida.

Si es válida, da el nombre bien escrito (como se conoce en España) y un nivel de rareza pensando en un jugador español medio:
1 = lo primero que se le ocurre a casi todo el mundo
2 = conocido, pero no lo primero
3 = hay que saber algo del tema
4 = de alguien que sabe mucho del tema
5 = casi nadie lo diría

Responde SOLO con JSON: {"valida": true|false, "nombre": "…", "nivel": 1-5, "motivo": "una frase corta"}`;

Deno.serve(async (req) => {
  const origen = req.headers.get("origin");
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(origen) });
  const responde = (datos: unknown, estado = 200) =>
    new Response(JSON.stringify(datos), { status: estado, headers: { ...cors(origen), "Content-Type": "application/json" } });

  let pregunta = "", respuesta = "";
  try { ({ pregunta, respuesta } = await req.json()); } catch { return responde({ error: "json" }, 400); }
  pregunta = String(pregunta ?? "").trim().slice(0, 200);
  respuesta = String(respuesta ?? "").trim().slice(0, 120);
  const clave = compacta(respuesta);
  if (!pregunta.startsWith("Nombra") || clave.length < 2) return responde({ error: "entrada" }, 400);

  const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

  // 1. ¿ya lo juzgamos?
  const { data: previo } = await db.from("sabihondo_ia").select("valida,nombre,nivel")
    .eq("pregunta", pregunta).eq("clave", clave).maybeSingle();
  if (previo) return responde({ ...previo, cache: true });

  // 2. tope diario para que nadie agote la IA
  const hoy = new Date().toISOString().slice(0, 10);
  const { count } = await db.from("sabihondo_ia").select("*", { count: "exact", head: true }).gte("created_at", hoy);
  if ((count ?? 0) >= TOPE_DIARIO) return responde({ valida: false, sin_juez: true });

  // 3. pregunta a la IA
  const r = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: { "Authorization": `Bearer ${Deno.env.get("GROQ_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      model: MODELO, temperature: 0, response_format: { type: "json_object" },
      messages: [{ role: "system", content: INSTRUCCIONES },
                 { role: "user", content: `Enunciado: ${pregunta}\nRespuesta del jugador: ${respuesta}` }],
    }),
  });
  if (!r.ok) return responde({ valida: false, sin_juez: true });
  let v: { valida?: boolean; nombre?: string; nivel?: number; motivo?: string } = {};
  try { v = JSON.parse((await r.json()).choices[0].message.content); } catch { return responde({ valida: false, sin_juez: true }); }

  const fila = {
    pregunta, clave, respuesta,
    valida: v.valida === true,
    nombre: String(v.nombre || respuesta).slice(0, 120),
    nivel: Math.min(5, Math.max(1, Math.round(Number(v.nivel) || 3))),
    motivo: String(v.motivo || "").slice(0, 300),
    modelo: MODELO,
  };
  await db.from("sabihondo_ia").upsert(fila, { onConflict: "pregunta,clave", ignoreDuplicates: true });
  return responde({ valida: fila.valida, nombre: fila.nombre, nivel: fila.nivel });
});
