# Training log — project brief

Shared profile (goal, day types, health, logistics; private, outside the repo): @~/.claude/me.md

A personal training app plus the program it runs. Live at https://gabihamilton.github.io/training/
(iPhone home-screen web app). Data syncs to Supabase; check-ins read it from there (use `/checkin`).

## The athlete
- 32, returning to Olympic weightlifting 3×/week, sessions up to **1.5 h**, any day incl. weekends.
- **Priorities (Nov 25):** 1) weightlifting (what makes the user happy; loves being in the gym), 2) huge glutes/legs,
  3) squat, 4) **bench**: informal CERN bench meet (IPF rules → paused bench), probably **May** (date TBC).
  Squats have always been the weak point. Rarely sore; Ganbaru felt easy.
- Bench history: 50 kg×8, 57 kg×2 at Fermilab; long ago 61 kg×1, then 61 kg×4 a year later. Detrained now.
- Best lifts (old): snatch 135 lb, C&J ~155 lb, back squat 215 lb. Working maxes in the app start at
  snatch 61, C&J 70, BS 97.5, FS 83 kg; to be reset from the week-3 ramp-up squat tests.
- Cardio: bike commute to CERN (~60 min/day, mostly easy, some Zone 3–4 on the climb; easiest gear already),
  3–4 days/week for now (Nov 25: not ready for every day). Rides are getting easier. Plus 1 weekend zone 2 run
  (20–30 min; feeds Apple Cardio Fitness, which ignores cycling). VO2max work comes after the RSR.
  **Monthly benchmark run** (cardio type `bench`, app card when ≥28 days): Nov 26 loop from home (4.8 km, ~47 m climb),
  zone 2 (≤145 bpm), logged with avg HR → metres per 100 heartbeats. Baseline Nov 26: 86 (Aug zone 2 runs 75–82).
  Apple VO2max 35.5 (Nov), was 36–37 Mar–Sep.
- Nov 17: blood donation refused for low red cell count (period coming) → suggested checking ferritin/iron with a doctor.
- Lifting shoes arrive end of November. December is chaotic: **away Dec 2–9 and Dec 19 – ~Jan 4**
  (travel sessions: `travel:legs`, `travel:upper`); gym only ~Dec 10–18.
- Build: already broad shoulders / big upper body, thin legs → upper body stays small, except bench (meet).
- Hyperlax elbows: prefer stretch-position arm work that doesn't hang on the joint (e.g. Bayesian cable curl).
- Weak at pull-ups (~4 max) → single-arm cable pulldowns instead.
- **Favourites:** single-leg RDL with the back foot up (great for glutes), GHD sit-ups, bench press,
  incline DB curl, cable pushdown. Use them when choosing exercises.
- Soreness shows up in quads/hamstrings, rarely glutes; don't judge glute work by soreness.
- Home: light rubber bands + tighter fabric bands. Band warm-up (glute bridge + lateral walk) opens every lower-body day (squat and hinge days).

## Schedule & logistics
- Gym is at CERN Meyrin. **Bike 3–4 days/week** (~30 min each way; needs rain gear), building toward daily.
  Car on the other days, best on squat-test / heavy squat days. Car (roommate, 8:50–17:30): lift ~9:00 or ~14:00. Gym platform is booked; 14:00 is quiet. May need P5 often: lift 9:00 → 10:50 shuttle, back on the 15:45.
- Now: 3–4 lifts/week; did B and C on back-to-back days by choice (Nov 23–24). **From January: 5 days/week**
  (+ optional weekend): heavy leg days alternate with bench/glute days, never two hard leg days in a row.
  Weekends optional (travel, visitors).
  The queue is flexible: any session can be started from Program → "do this".
- No front squat the day after B (RDL/lunges); no two squat days in a row; ≥3 days before a squat test.
- Weekday runs are impractical; zone 2 = bike commutes + weekend runs/walks.

## CERN gym equipment
Barbells, plates, rig, dumbbells, benches, **cables**, **GHD** (loves GHD sit-ups; one cushion is flat),
sled (push/pull), plyo boxes (box jumps for height), kettlebells, mats.
**No leg machines** (no leg press, leg curl machine, calf machine, back extension).

## Program (session queue, not calendar)
Optional extras outside the queue: **Home: glutes + abs** (`home:bands`), **Gym: arms** (`extra:arms`),
**Travel: legs + glutes / upper + core** (`travel:legs`, `travel:upper`; bodyweight + bands, no weight hints),
**Weekend: heavy singles** (`extra:singles`), **Freestyle** (free session, nameable, e.g. park bars).
1. **Ramp-up** (3 wks × 3, from Nov 11): RPE-based; week 3 = squat tests that set the working maxes.
2. **December minimum dose** (5 wks): 2 core sessions + optional legs/glutes pump day; % of working maxes; wk 5 deload.
3. **Leg size block** (5 wks × 5 days, Jan 5 – Feb 8): Mon snatch + BS · Tue paused bench + heavy hip thrust ·
   Wed C&J + FS · Thu bench volume + arms · Fri clean + hinge. BS 3–5×8–10 / FS 3–4×8 @ 65–70%, accessories RPE 9,
   oly 65→72%, bench 4×6 @70% → 5×5 @77.5%. ~40 leg/glute sets/week. Week 5 = lighter + tests (BS + snatch Mon,
   C&J Wed, paused bench Thu, FS Fri) → maxes for RSR.
4. **Russian Squat Routine** (6 wks × 5 days, Feb 9 – Mar 22): standard table (6×2…6×6 @80%, then 85/90/95/100/105%)
   on Mon/Wed/Fri inside oly sessions at 70–75%. Tue paused bench 5×5 @75% → 3×1 @87.5% + heavy hip thrust;
   Thu bench volume + arms. Glute work drops in weeks 5–6. Easy zone 2 jogs OK (20–30 min, not the day before a
   big squat day, none in weeks 5–6 or when legs ≤2/5). No VO2max during RSR. Chosen over Smolov on purpose;
   kept (Nov 25) because the user wants to see how far it goes.
5. **Next: explosive / peak block** (power, heavier classic lifts, VO2max starts, bench peak if the meet is in May):
   written from real data after the RSR test.
Order on purpose: ramp-up → size → strength → power. Weekends: optional extras, incl. **Weekend: heavy singles**
(`extra:singles`; only legs ≥3/5, not before a squat test, not RSR weeks 5–6). Bench working max (`bench`) starts 52.5.
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
