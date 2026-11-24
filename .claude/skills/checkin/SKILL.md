---
name: checkin
description: Review the user's logged training (sessions, cardio, measurements) from Supabase and give feedback. Use when they say they finished a workout, ask how training is going, ask what to do next, or ask about progress, maxes or measurements.
---

# Training check-in

1. Get the data as a compact summary (never curl the raw JSON):
   ```bash
   python3 -I .claude/skills/checkin/summary.py            # last 42 days
   python3 -I .claude/skills/checkin/summary.py --days 400 # everything
   ```
   It prints working maxes, program position (e.g. `ramp 2/9 done`), each session (sets×reps @ weights, RPE,
   notes), bests/e1RMs vs working max, weekly sessions · leg/glute sets · cardio min, measurements and change.
2. If you need what a session *prescribed* (to compare), grep the template in `index.html`
   (`rampSessions`, `decSessions`, `sizeSessions`, `rsrSessions`, `HOME_BANDS`, `ARMS`) instead of reading the whole file.
   Ramp keys: `ramp:0..8` = weeks 1–3 × (A Snatch+squat, B Clean+hinge, C Front squat+jerk+glutes).
   Size keys: `size:0..14` (weeks 1–5 × A/B/C; week 5 = squat tests). Extras: `home:bands`, `extra:arms`,
   key null = Freestyle (title is whatever the user named it). Lower-body days start with a 'Band warm-up' item.
   The user can do sessions out of order (Program → "do this"), so judge by key, not by date order.

## What to look at
- **RPE vs target:** below target → add weight next time (2.5–5 kg on squats/hinges, 1–2.5 on oly lifts);
  above target or missed sets → hold.
- **Squat e1RM vs working max:** after the ramp-up week-3 test, suggest new maxes (≈ e1RM, rounded down
  to 2.5 kg) for Settings. Oly maxes: heaviest clean single, conservative.
- **Recovery:** readiness ≤2/5, two low days in a row, or notes about pain → lighten or swap; flag pain.
- **Volume:** leg/glute sets per week (rough targets: ramp 30–45, Dec 20–35, RSR highest).
- **Schedule:** respect the logistics in CLAUDE.md (car/bike/P5, weekends optional). Suggest the next session and day; avoid front squat the day after RDL/lunges in ramp-up,
  no heavy legs day after a big squat day, a day off after 2–3 days in a row.
- **Measurements:** monthly, morning, before eating/training. Thigh/hip up with waist stable = good.
- Drop sets: sets with `drop: true`; summary shows them as `[70×8 ↘50×8 ↘35×10]` and doesn't count them as sets.
- Data quirks: box jump `w` is box height in **cm**; band exercises usually have no weight; GHD `w` 0 = bodyweight.

## Reply format
Short. First line: the verdict. Then a few bullets with numbers (kg). Then the next session + when.
Only suggest app changes if something is actually broken; use `/ship` to make them.
