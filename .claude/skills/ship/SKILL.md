---
name: ship
description: Change the training app (index.html) — add or edit exercises, sessions, phases, features or UI — then test, commit and (with permission) push to GitHub Pages. Use for any change to the app or the program templates.
---

# Changing the training app

Everything is in `index.html` (~1000 lines). Don't read it all; grep for what you need.

## Map (grep these names)
- **Program templates:** `ghdSitup`, `rampSessions`, `decSessions` (`pcts`), `RSR` table + `rsrSessions`,
  `PHASES` (name, when, desc, sessions), `HOME_BANDS` (optional, not in the queue).
  Exercise object: `{ n: name, s: sets, r: reps (number or '8/leg', '1+1', '20m'), rpe?, pct? + of: 'bs'|'fs'|'snatch'|'cj', note? }`.
  Session keys are `phase:index`; **reordering or inserting sessions in a phase shifts the keys of later
  sessions**, which changes which ones count as done. Append, or check logged keys first (`/checkin`).
- `LEGS` set: exercises counted as leg/glute sets — add new leg exercises here **and** in
  `.claude/skills/checkin/summary.py`.
- `restMin` (rest timer per exercise) and `estMin` (session length); keep sessions ≲85 min.
- Logging: `startSession`, `finishSession`, `toggleSet`, rest timer `startRest`.
- Render: `renderToday`, `renderDraft`, Program tab, `renderProgress`, `renderMeasures`, `MEAS`.
- Sync: `syncAll`, `localItems`, `applyRemote`, `scheduleSync`, `markSynced` (newer `client_ts` wins).
- Edits: python `str.replace` heredocs or Edit tool; BSD `sed` on macOS.

## Test (no node here, so test in the browser pane)
1. `python3 -m http.server 8765` in the background from the repo root.
2. Open `http://localhost:8765/?test`. **Mock fetch before doing anything that saves**, so the real DB is
   never written: run `window.fetch = async () => new Response('[]', {status:200})` (re-run after each reload;
   the page load itself pulls real data, which is fine).
3. Check via JS (`nextSession().title`, `state.draft`, button labels) and one mobile-size screenshot
   (`resize_window` preset mobile, then back to desktop). Don't click "Finish & save" unless fetch is mocked.
4. `pkill -f "http.server 8765"` when done.

## Ship
1. Commit with a clear message (+ Co-Authored-By line).
2. **Ask the user before pushing.** On yes: `git push origin main`, wait ~45 s, then
   `curl -s https://gabihamilton.github.io/training/ | grep -c '<something new>'` to confirm it's live.
3. Tell them to close and reopen the app on the phone if it shows the old version.
