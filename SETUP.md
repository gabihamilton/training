# Training log: setup

A single static `index.html` (vanilla JS, no build step), hosted on GitHub Pages.
Data is kept in the browser and synced to the same Supabase project as the habits app.

## Supabase table (run once in the SQL Editor)

```sql
create table if not exists public.training_items (
  id          text primary key,             -- session / cardio id, or 'settings' / 'skipped'
  kind        text not null,                -- 'session' | 'cardio' | 'settings' | 'skipped' | 'deleted'
  date        date,
  data        jsonb,
  deleted     boolean not null default false,
  client_ts   bigint not null default 0,    -- ms timestamp of the last edit; newer side wins
  updated_at  timestamptz not null default now()
);

alter table public.training_items enable row level security;

create policy "anon read"   on public.training_items for select to anon using (true);
create policy "anon insert" on public.training_items for insert to anon with check (true);
create policy "anon update" on public.training_items for update to anon using (true) with check (true);

grant select, insert, update on public.training_items to anon;

create or replace function public.touch_updated_at()
  returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end; $$;

create trigger training_items_touch before update on public.training_items
  for each row execute function public.touch_updated_at();
```

## How sync works
- On open, on returning to the app, and after every save, the app downloads all rows,
  takes any row whose `client_ts` is newer than its local copy, then uploads anything
  newer locally (including data logged before sync existed).
- Deletes are kept as rows with `deleted = true`, so they reach other devices.
- Works offline: logging is saved locally and uploaded at the next successful sync.
- The in-progress session (draft) stays on the device until you tap "Finish & save".

## Reading the data (for check-ins)
```bash
curl -s "https://mghqfyjckbzhyefpzkaq.supabase.co/rest/v1/training_items?select=*&deleted=eq.false&order=date" \
  -H "apikey: <publishable key from index.html>"
```
