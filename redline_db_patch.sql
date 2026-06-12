-- =========================================================
-- REDLINE DB PATCH
-- Better auth support, username login RPC, profile trigger, and more cars.
-- Run in Supabase SQL Editor.
-- =========================================================

-- IMPORTANT: Email verification cannot be disabled by SQL in hosted Supabase.
-- Dashboard path:
-- Authentication -> Providers -> Email -> turn OFF "Confirm email".

-- Needed extension
create extension if not exists "uuid-ossp";

-- Make sure profiles can store public username and private email for username login.
-- WARNING: If you already have policies, review before replacing.
alter table public.profiles add column if not exists email text;
alter table public.profiles add column if not exists role text not null default 'player'
  check (role in ('player','moderator','admin','owner'));
alter table public.profiles add column if not exists is_banned boolean default false;
alter table public.profiles add column if not exists ban_reason text;

create unique index if not exists profiles_username_lower_unique on public.profiles (lower(username));
create index if not exists profiles_email_idx on public.profiles (email);

-- Auto-create profiles when auth users sign up.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.profiles (id, username, email, cash, level, xp, wins, losses, role)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'username', split_part(new.email, '@', 1)),
    new.email,
    50000,
    1,
    0,
    0,
    0,
    'player'
  )
  on conflict (id) do update set
    email = excluded.email,
    username = coalesce(public.profiles.username, excluded.username);
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
after insert on auth.users
for each row execute procedure public.handle_new_user();

-- Username login helper.
-- This returns email for a username so the client can call signInWithPassword.
-- Keep this simple for game/demo use; for production, use an Edge Function instead.
create or replace function public.get_email_by_username(p_username text)
returns text
language sql
security definer
set search_path = public
as $$
  select email
  from public.profiles
  where lower(username) = lower(p_username)
    and coalesce(is_banned,false) = false
  limit 1;
$$;

grant execute on function public.get_email_by_username(text) to anon, authenticated;

-- Activity log table, if missing.
create table if not exists public.activity_logs (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references public.profiles(id),
  username text,
  action text not null,
  details jsonb,
  ip_hint text,
  created_at timestamptz default now()
);

alter table public.activity_logs enable row level security;

drop policy if exists "Own logs" on public.activity_logs;
drop policy if exists "Admins see all logs" on public.activity_logs;
drop policy if exists "Insert own log" on public.activity_logs;

create policy "Own logs" on public.activity_logs
for select using (user_id = auth.uid());

create policy "Admins see all logs" on public.activity_logs
for select using (
  exists (
    select 1 from public.profiles
    where id = auth.uid() and role in ('admin','owner','moderator')
  )
);

create policy "Insert own log" on public.activity_logs
for insert with check (user_id = auth.uid());

-- Expanded car inventory. Adjust IDs/names if your table differs.
insert into public.cars (id, brand, name, class, rarity, emoji, base_price, power, top_speed, acceleration, handling, braking, weight, description)
values
('nissan_gtr_r35','Nissan','GT-R R35','Sports','Epic','🏎️',125000,565,196,88,82,78,3933,'All-wheel-drive launch monster with brutal street pace.'),
('mazda_rx7_fd','Mazda','RX-7 FD Spirit R','Sports','Rare','🚗',68000,276,160,82,89,74,2800,'Lightweight rotary icon built for corners and night runs.'),
('honda_nsx_1992','Honda','NSX NA1','Sports','Rare','🚘',95000,270,168,78,92,78,3010,'Mid-engine precision legend with pure driver feel.'),
('toyota_ae86','Toyota','AE86 Trueno','Sports','Common','🚗',28000,128,125,61,86,62,2200,'Light, simple, and perfect for learning drift lines.'),
('dodge_charger_hellcat','Dodge','Charger Hellcat','Muscle','Rare','🚓',82000,707,204,82,62,70,4586,'Four-door thunder with absurd supercharged power.'),
('ford_mustang_gt500','Ford','Mustang Shelby GT500','Muscle','Epic','🚗',105000,760,180,84,70,76,4225,'Track-capable muscle with huge straight-line violence.'),
('chevy_corvette_c8_z06','Chevrolet','Corvette C8 Z06','Sports','Epic','🏎️',138000,670,195,90,89,86,3434,'Flat-plane V8 supercar hunter with razor handling.'),
('porsche_911_gt3rs','Porsche','911 GT3 RS','Sports','Legendary','🏎️',260000,518,184,91,98,93,3268,'Downforce-heavy circuit weapon that eats apexes.'),
('mclaren_720s','McLaren','720S','Hypercar','Legendary','🏎️',315000,710,212,94,93,89,3167,'Carbon-fiber missile with savage acceleration.'),
('lamborghini_huracan_sto','Lamborghini','Huracán STO','Hypercar','Legendary','🏎️',335000,630,193,91,95,90,2951,'Track-bred V10 fury with wild aero.'),
('ferrari_sf90','Ferrari','SF90 Stradale','Hypercar','Mythic','🏎️',625000,986,211,99,94,92,3527,'Hybrid hypercar with terrifying instant acceleration.'),
('bugatti_chiron','Bugatti','Chiron','Hypercar','Mythic','🏎️',3000000,1479,261,97,84,88,4398,'Top-speed royalty and the king of highway pulls.'),
('koenigsegg_jesko','Koenigsegg','Jesko Attack','Hypercar','Mythic','🏎️',2850000,1600,278,98,96,94,3131,'Extreme aero and power from another dimension.'),
('rimac_nevera','Rimac','Nevera','EV','Mythic','⚡',2200000,1914,258,100,91,95,5070,'Electric torque apocalypse. EV battle dominator.'),
('tesla_model_s_plaid','Tesla','Model S Plaid','EV','Epic','⚡',118000,1020,200,99,75,78,4766,'Instant launch power in a sleeper sedan shell.'),
('lucid_sapphire','Lucid','Air Sapphire','EV','Legendary','⚡',250000,1234,205,99,79,82,5336,'Luxury EV with supercar-shaming acceleration.'),
('ford_raptor_r','Ford','F-150 Raptor R','SUV/Truck','Rare','🚙',110000,700,114,72,68,70,5950,'Off-road brute with supercharged V8 muscle.'),
('mercedes_g63','Mercedes-AMG','G63','SUV/Truck','Epic','🚙',185000,577,149,70,63,72,5783,'Luxury tank with outrageous street presence.'),
('lamborghini_urus','Lamborghini','Urus Performante','SUV/Truck','Legendary','🚙',265000,657,190,84,76,80,4740,'Super-SUV with shocking pace and rally attitude.'),
('subaru_wrx_sti','Subaru','WRX STI','Sports','Common','🚗',42000,310,155,76,83,72,3450,'AWD rally-bred street fighter for all-weather racing.'),
('mitsubishi_evo_ix','Mitsubishi','Lancer Evolution IX','Sports','Rare','🚗',56000,286,157,78,88,73,3263,'Turbo AWD icon with legendary grip.'),
('bmw_m3_g80','BMW','M3 Competition','Sports','Rare','🚘',79000,503,180,84,82,80,3890,'Modern sports sedan with balanced power and control.'),
('audi_rs6','Audi','RS6 Avant','Sports','Epic','🚗',126000,621,190,87,80,82,4982,'Wagon practicality with supercar hunting speed.'),
('cadillac_ct5_blackwing','Cadillac','CT5-V Blackwing','Muscle','Epic','🚘',98000,668,205,85,78,82,4123,'Manual super sedan with track-ready attitude.')
on conflict (id) do update set
  brand = excluded.brand,
  name = excluded.name,
  class = excluded.class,
  rarity = excluded.rarity,
  emoji = excluded.emoji,
  base_price = excluded.base_price,
  power = excluded.power,
  top_speed = excluded.top_speed,
  acceleration = excluded.acceleration,
  handling = excluded.handling,
  braking = excluded.braking,
  weight = excluded.weight,
  description = excluded.description;

-- Ensure every car has a market price row.
insert into public.market_prices (car_id, base_price, current_price, demand_score, sales_last_24h, updated_at)
select id, base_price, base_price, 50, 0, now()
from public.cars
on conflict (car_id) do nothing;

-- Helpful indexes for faster game queries.
create index if not exists player_cars_player_id_idx on public.player_cars(player_id);
create index if not exists auctions_status_ends_idx on public.auctions(status, ends_at);
create index if not exists bids_auction_id_idx on public.bids(auction_id);
create index if not exists races_player1_id_created_idx on public.races(player1_id, created_at desc);
