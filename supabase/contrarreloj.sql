-- Sabihondo · contrarreloj: una fila por partida de cada persona con cuenta.
-- Pégalo en el editor SQL de Supabase. Se puede ejecutar varias veces sin romper nada.

create table if not exists public.sabihondo_contrarreloj (
  id         bigint      generated always as identity primary key,
  user_id    uuid        not null default auth.uid() references auth.users(id) on delete cascade,
  aciertos   integer     not null check (aciertos between 0 and 120),
  res        jsonb       not null default '[]'::jsonb,
  fecha      date        not null default current_date,
  created_at timestamptz not null default now()
);
grant select, insert on public.sabihondo_contrarreloj to authenticated;
grant all on public.sabihondo_contrarreloj to service_role;
alter table public.sabihondo_contrarreloj enable row level security;

drop policy if exists "Contrarreloj: leer las mías" on public.sabihondo_contrarreloj;
create policy "Contrarreloj: leer las mías" on public.sabihondo_contrarreloj
  for select to authenticated using (auth.uid() = user_id);
drop policy if exists "Contrarreloj: guardar las mías" on public.sabihondo_contrarreloj;
create policy "Contrarreloj: guardar las mías" on public.sabihondo_contrarreloj
  for insert to authenticated with check (auth.uid() = user_id);

-- Podio: la mejor partida de cada persona (hasta 100), con su apodo. Ni emails ni respuestas.
-- En el empate va antes quien lo consiguió primero.
create or replace function public.sabihondo_contrarreloj_podio()
returns table (puesto bigint, apodo text, aciertos integer, eres_tu boolean)
language sql stable security definer set search_path = ''
as $$
  with mejor as (
    select distinct on (c.user_id) c.user_id, c.aciertos, c.created_at
    from public.sabihondo_contrarreloj c
    order by c.user_id, c.aciertos desc, c.created_at asc
  )
  select rank() over (order by m.aciertos desc),
         left(coalesce(nullif(btrim(u.raw_user_meta_data->>'apodo'), ''), 'Anónimo'), 20),
         m.aciertos,
         coalesce(m.user_id = auth.uid(), false)
  from mejor m
  join auth.users u on u.id = m.user_id
  order by m.aciertos desc, m.created_at asc
  limit 100;
$$;
revoke all on function public.sabihondo_contrarreloj_podio() from public;
grant execute on function public.sabihondo_contrarreloj_podio() to anon, authenticated;

-- ═══ Álbum del batiscafo (31 oct 2026) ═══
-- Qué bichos se vieron en cada partida (índices de BICHOS en index.html: 0 bacalao … 11 kraken).
alter table public.sabihondo_contrarreloj add column if not exists bichos smallint[] not null default '{}';

-- Para cada bicho, el % de jugadores con cuenta que lo ha visto alguna vez (sobre los que han jugado al batiscafo).
create or replace function public.sabihondo_album_stats()
returns table (bicho smallint, porcentaje numeric)
language sql stable security definer set search_path = ''
as $$
  with total as (select count(distinct user_id)::numeric as n from public.sabihondo_contrarreloj),
  vistos as (
    select b as bicho, count(distinct c.user_id)::numeric as n
    from public.sabihondo_contrarreloj c, unnest(c.bichos) as b
    group by b
  )
  select v.bicho, round(100 * v.n / nullif(t.n, 0), 1) from vistos v, total t;
$$;
revoke all on function public.sabihondo_album_stats() from public;
grant execute on function public.sabihondo_album_stats() to anon, authenticated;

-- El podio, ahora con quién ha visto al kraken (11). Cambia lo que devuelve, así que hay que borrarlo antes.
drop function if exists public.sabihondo_contrarreloj_podio();
create or replace function public.sabihondo_contrarreloj_podio()
returns table (puesto bigint, apodo text, aciertos integer, eres_tu boolean, kraken boolean)
language sql stable security definer set search_path = ''
as $$
  with mejor as (
    select distinct on (c.user_id) c.user_id, c.aciertos, c.created_at
    from public.sabihondo_contrarreloj c
    order by c.user_id, c.aciertos desc, c.created_at asc
  ), kraken as (
    select distinct c.user_id from public.sabihondo_contrarreloj c where 11 = any(c.bichos)
  )
  select rank() over (order by m.aciertos desc),
         left(coalesce(nullif(btrim(u.raw_user_meta_data->>'apodo'), ''), 'Anónimo'), 20),
         m.aciertos,
         coalesce(m.user_id = auth.uid(), false),
         exists (select 1 from kraken k where k.user_id = m.user_id)
  from mejor m
  join auth.users u on u.id = m.user_id
  order by m.aciertos desc, m.created_at asc
  limit 100;
$$;
revoke all on function public.sabihondo_contrarreloj_podio() from public;
grant execute on function public.sabihondo_contrarreloj_podio() to anon, authenticated;
