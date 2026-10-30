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
