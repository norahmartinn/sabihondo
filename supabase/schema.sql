-- Sabihondo · una fila por persona y día de reto.
-- Pégalo en el editor SQL de Supabase. Se puede ejecutar varias veces sin romper nada.

create table if not exists public.sabihondo_partidas (
  user_id    uuid        not null default auth.uid() references auth.users(id) on delete cascade,
  fecha      date        not null,
  dia        integer     not null,
  puntos     integer     not null check (puntos between 0 and 700),
  res        jsonb       not null default '[]'::jsonb,
  created_at timestamptz not null default now(),
  primary key (user_id, fecha)
);

grant select, insert on public.sabihondo_partidas to authenticated;
grant all on public.sabihondo_partidas to service_role;
alter table public.sabihondo_partidas enable row level security;

-- Cada persona ve y guarda solo sus partidas. No hay update ni delete:
-- el reto de cada día se juega una vez.
drop policy if exists "Sabihondo: leer las mías" on public.sabihondo_partidas;
create policy "Sabihondo: leer las mías" on public.sabihondo_partidas
  for select to authenticated using (auth.uid() = user_id);

drop policy if exists "Sabihondo: guardar las mías" on public.sabihondo_partidas;
create policy "Sabihondo: guardar las mías" on public.sabihondo_partidas
  for insert to authenticated with check (auth.uid() = user_id);

-- Respuestas que el juego rechazó y alguien cree correctas («¿Es correcta? Avísanos»).
-- Cualquiera puede enviar una, con o sin cuenta; nadie las puede leer desde la web.
-- Se revisan en el panel de Supabase (Table Editor → sabihondo_sugerencias).
create table if not exists public.sabihondo_sugerencias (
  id         bigint      generated always as identity primary key,
  pregunta   text        not null check (char_length(pregunta) <= 200),
  respuesta  text        not null check (char_length(respuesta) between 1 and 120),
  user_id    uuid        default auth.uid(),
  created_at timestamptz not null default now()
);

grant insert on public.sabihondo_sugerencias to anon, authenticated;
grant all on public.sabihondo_sugerencias to service_role;
alter table public.sabihondo_sugerencias enable row level security;

drop policy if exists "Sabihondo: enviar sugerencias" on public.sabihondo_sugerencias;
create policy "Sabihondo: enviar sugerencias" on public.sabihondo_sugerencias
  for insert to anon, authenticated with check (user_id is null or user_id = auth.uid());

-- Veredictos de la IA sobre respuestas que no estaban en el banco (función sabihondo-juez).
-- Solo la función escribe aquí (con la clave de servicio). Se revisan en el Table Editor:
-- si una aceptada está mal, pon valida = false; si una rechazada es buena, pon valida = true.
create table if not exists public.sabihondo_ia (
  id         bigint      generated always as identity primary key,
  pregunta   text        not null,
  clave      text        not null,
  respuesta  text        not null,
  valida     boolean     not null,
  nombre     text        not null,
  nivel      smallint    not null check (nivel between 1 and 5),
  motivo     text,
  modelo     text,
  created_at timestamptz not null default now(),
  unique (pregunta, clave)
);
grant all on public.sabihondo_ia to service_role;
alter table public.sabihondo_ia enable row level security;

-- Récord del día: el mejor resultado de una fecha entre quienes tienen cuenta, con su apodo.
-- Es lo único de las partidas ajenas que se puede leer desde la web: una fila, sin email ni respuestas.
-- El apodo se guarda en los datos de la cuenta (auth.users.raw_user_meta_data->>'apodo').
-- Si hay empate, gana quien llegó antes.
create or replace function public.sabihondo_record(dia date)
returns table (puntos integer, apodo text)
language sql stable security definer set search_path = ''
as $$
  select p.puntos,
         left(coalesce(nullif(btrim(u.raw_user_meta_data->>'apodo'), ''), 'Anónimo'), 20)
  from public.sabihondo_partidas p
  join auth.users u on u.id = p.user_id
  where p.fecha = sabihondo_record.dia   -- con el nombre de la función delante: la tabla también tiene una columna «dia»
  order by p.puntos desc, p.created_at asc
  limit 1;
$$;
revoke all on function public.sabihondo_record(date) from public;
grant execute on function public.sabihondo_record(date) to anon, authenticated;

-- Ranking del día: los metros de cada persona con cuenta en una fecha, con su apodo (hasta 100).
-- Tampoco enseña emails ni respuestas. eres_tu marca la fila de quien pregunta, si ha iniciado sesión.
create or replace function public.sabihondo_ranking(dia date)
returns table (puesto bigint, apodo text, puntos integer, eres_tu boolean)
language sql stable security definer set search_path = ''
as $$
  select rank() over (order by p.puntos desc),
         left(coalesce(nullif(btrim(u.raw_user_meta_data->>'apodo'), ''), 'Anónimo'), 20),
         p.puntos,
         coalesce(p.user_id = auth.uid(), false)
  from public.sabihondo_partidas p
  join auth.users u on u.id = p.user_id
  where p.fecha = sabihondo_ranking.dia
  order by p.puntos desc, p.created_at asc
  limit 100;
$$;
revoke all on function public.sabihondo_ranking(date) from public;
grant execute on function public.sabihondo_ranking(date) to anon, authenticated;
