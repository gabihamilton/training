# Training log — project brief

A personal training app plus the program it runs. Live at https://gabihamilton.github.io/training/
(iPhone home-screen web app). Data syncs to Supabase; check-ins read it from there (use `/checkin`).

## The athlete
- 32, returning to Olympic weightlifting 3×/week, sessions up to **1.5 h**, any day incl. weekends.
- **Goal: huge legs and glutes.** Squats have always been the weak point. Rarely sore; Ganbaru felt easy.
- Best lifts (old): snatch 135 lb, C&J ~155 lb, back squat 215 lb. Working maxes in the app start at
  snatch 61, C&J 70, BS 97.5, FS 83 kg; to be reset from the week-3 ramp-up squat tests.
- Cardio: daily bike commute to CERN (zone 2, ~5 h/week from Nov 18); VO2max work comes after the RSR.
- Nov 17: blood donation refused for low red cell count (period coming) → suggested checking ferritin/iron with a doctor.
- Lifting shoes arrive end of November; December is chaotic (minimum-dose phase).
- Build: already broad shoulders / big upper body, thin legs → upper body only as optional extras.
- Hyperlax elbows: prefer stretch-position arm work that doesn't hang on the joint (e.g. Bayesian cable curl).
- Weak at pull-ups (~4 max) → single-arm cable pulldowns instead.
- **Favourites:** single-leg RDL with the back foot up (great for glutes), GHD sit-ups, bench press,
  incline DB curl, cable pushdown. Use them when choosing exercises.
- Soreness shows up in quads/hamstrings, rarely glutes; don't judge glute work by soreness.
- Home: light rubber bands + tighter fabric bands. Band warm-up (glute bridge + lateral walk) opens every lower-body day (squat and hinge days).

## Schedule & logistics
- Gym is at CERN Meyrin. **From Nov 18 the plan is to bike there every day** (~30 min each way = ~60 min zone 2/day;
  needs rain gear). Car (roommate, 8:50–17:30) is the fallback: lift ~9:00 or ~14:00. Gym platform is booked; 14:00 is quiet. May need P5 often: lift 9:00 → 10:50 shuttle, back on the 15:45.
- Default: 3 weekday lifts (≥1 rest day between squat days); weekends optional (travel, visitors).
  The queue is flexible: any session can be started from Program → "do this".
- No front squat the day after B (RDL/lunges); no two squat days in a row; ≥3 days before a squat test.
- Weekday runs are impractical; zone 2 = bike commutes + weekend runs/walks.

## CERN gym equipment
Barbells, plates, rig, dumbbells, benches, **cables**, **GHD** (loves GHD sit-ups; one cushion is flat),
sled (push/pull), plyo boxes (box jumps for height), kettlebells, mats.
**No leg machines** (no leg press, leg curl machine, calf machine, back extension).

## Program (session queue, not calendar)
Optional extras outside the queue: **Home: glutes + abs** (`home:bands`), **Gym: arms** (`extra:arms`),
**Freestyle** (free session, nameable, e.g. park bars).
1. **Ramp-up** (3 wks × 3, from Nov 11): RPE-based; week 3 = squat tests that set the working maxes.
2. **December minimum dose** (5 wks): 2 core sessions + optional legs/glutes pump day; % of working maxes; wk 5 deload.
3. **Leg size block** (5 wks × 3, Jan 5 – Feb 8): hypertrophy before strength. BS 3–5×8–10 / FS 3–4×8 @ 65–70%,
   accessories at RPE 9; oly lifts light (65%, technique). Week 5 = lighter + squat tests → maxes for RSR.
4. **Russian Squat Routine** (6 wks × 3, Feb 9 – Mar 22): standard table (6×2…6×6 @80%, then 85/90/95/100/105%),
   built into oly sessions at 70–75%. Easy zone 2 jogs OK (20–30 min, not the day before a big squat day,
   none in weeks 5–6 or when legs ≤2/5). No VO2max during RSR. Chosen over Smolov on purpose.
5. **Next: explosive / peak block** (power, heavier classic lifts, VO2max starts): written from real data after the RSR test.
Order on purpose: ramp-up → size → strength → power. Upper body only as optional extras (Gym: arms, Freestyle).
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
