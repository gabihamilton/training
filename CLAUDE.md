# Training log — project brief

A personal training app plus the program it runs. Live at https://gabihamilton.github.io/training/
(iPhone home-screen web app). Data syncs to Supabase; check-ins read it from there (use `/checkin`).

## The athlete
- 32, returning to Olympic weightlifting 3×/week, sessions up to **1.5 h**, any day incl. weekends.
- **Goal: huge legs and glutes.** Squats have always been the weak point. Rarely sore; Ganbaru felt easy.
- Best lifts (old): snatch 135 lb, C&J ~155 lb, back squat 215 lb. Working maxes in the app start at
  snatch 61, C&J 70, BS 97.5, FS 83 kg; to be reset from the week-3 ramp-up squat tests.
- Cardio: bike commutes to CERN (zone 2) a couple of times a week; VO2max work comes later.
- Lifting shoes arrive end of November; December is chaotic (minimum-dose phase).
- Home: resistance bands (optional "Home: bands" session).

## CERN gym equipment
Barbells, plates, rig, dumbbells, benches, **cables**, **GHD** (loves GHD sit-ups; one cushion is flat),
sled (push/pull), plyo boxes (box jumps for height), kettlebells, mats.
**No leg machines** (no leg press, leg curl machine, calf machine, back extension).

## Program (session queue, not calendar)
1. **Ramp-up** (3 wks × 3, from Nov 11): RPE-based; week 3 = squat tests that set the working maxes.
2. **December minimum dose** (5 wks): 2 core sessions + optional legs/glutes pump day; % of working maxes; wk 5 deload.
3. **Russian Squat Routine** (6 wks × 3, from ~Jan 5): standard table (6×2…6×6 @80%, then 85/90/95/100/105%),
   built into oly sessions at 70–75%. Easy zone 2 jogs OK (20–30 min, not the day before a big squat day,
   none in weeks 5–6 or when legs ≤2/5). No VO2max during RSR. Chosen over Smolov on purpose.
4. **Next block**: to be written from real data after the RSR test.
Keep every session ≤ ~85 min estimated (`estMin`), ideally 60–80.

## The app
- Single `index.html`, vanilla JS, no build step, no node on this Mac. Same pattern as `~/Code/habits`.
- Weights stored in **kg**; displayed in kg/lb. localStorage key `gabi-training-log`.
- Supabase table `training_items` (see SETUP.md). Kinds: session, cardio, measure, settings, skipped.
- To change the app, use `/ship`.

## Rules
- **Always ask before `git push`** (each push needs the user's OK). Commit freely.
- Replies: short, numbers first, kg. The user reads on the phone over Remote Control, so write closing
  messages as if there's no next-step box.
- The repo, data and publishable key are public by the user's choice; that's fine.
