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
