#!/usr/bin/env python3
"""Compact summary of the training log from Supabase (stdlib only).

Usage: python3 -I .claude/skills/checkin/summary.py [--days N]   (default: 42 days of sessions)
"""
import json, sys, urllib.request
from collections import defaultdict
from datetime import date, timedelta

URL = "https://mghqfyjckbzhyefpzkaq.supabase.co/rest/v1/training_items?select=id,kind,date,data&deleted=eq.false&order=date"
KEY = "sb_publishable_BVJz5Rcer9rJlP-AcVPp0A_n0-UAK6z"
LEGS = {'Back squat','Front squat','Bulgarian split squat','Hip thrust','Romanian deadlift','Walking lunge','Goblet squat',
        'Single-leg DB RDL','DB calf raise','Good morning','DB step-up','Cable leg curl','Cable pull-through','Cable kickback',
        'GHD hip extension','Sled push','Kettlebell swing','Overhead squat','Pause back squat','Banded glute bridge',
        'Single-leg glute bridge','Banded lateral walk','Banded clamshell','Banded kickback','Frog pump'}
MAXES = {'snatch': 'Snatch', 'cj': 'Clean & jerk', 'bs': 'Back squat', 'fs': 'Front squat'}
PHASE_LEN = {'ramp': 9, 'dec': 15, 'size': 15, 'rsr': 18}  # sessions per phase (dec includes optional pump days)

days = 42
if '--days' in sys.argv: days = int(sys.argv[sys.argv.index('--days') + 1])
since = (date.today() - timedelta(days=days)).isoformat()

req = urllib.request.Request(URL, headers={"apikey": KEY, "Authorization": "Bearer " + KEY})
rows = json.load(urllib.request.urlopen(req, timeout=20))
by = defaultdict(list)
for r in rows: by[r['kind']].append(r['data'])

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None
def reps(r):
    s = str(r); d = ''.join(c for c in s.split('/')[0].split('+')[0] if c.isdigit() or c == '.')
    return num(d) or 0
def w(x):
    x = num(x); return '-' if x is None else (str(int(x)) if x == int(x) else str(x))

settings = (by['settings'] or [{}])[0]
print(f"Units {settings.get('unit','kg')} · working maxes (kg): " + ', '.join(f"{k} {v}" for k, v in settings.get('maxes', {}).items()))

sessions = sorted(by['session'], key=lambda s: s['date'])
done = [s.get('key') for s in sessions if s.get('key')]
skipped = (by['skipped'] or [[]])[0] or []
prog = []
for ph, n in PHASE_LEN.items():
    k = [x for x in done if x.startswith(ph + ':')]
    if k: prog.append(f"{ph} {len(k)}/{n} done (last {max(k, key=lambda x: int(x.split(':')[1]))})")
print("Program: " + ('; '.join(prog) or 'nothing done yet') + (f" · skipped {skipped}" if skipped else ''))
print(f"\n## Sessions since {since} ({len([s for s in sessions if s['date'] >= since])} of {len(sessions)} total)")
for s in sessions:
    if s['date'] < since: continue
    print(f"\n{s['date']} {s.get('title','')} [{s.get('key') or 'free'}] readiness {s.get('readiness') or '-'}/5")
    for e in s.get('exercises', []):
        ds = [x for x in e['sets'] if x.get('done')]
        miss = len(e['sets']) - len(ds)
        rs = {str(x.get('r')) for x in ds}
        rtxt = rs.pop() if len(rs) == 1 else '/'.join(str(x.get('r')) for x in ds)
        ws = [w(x.get('w')) for x in ds]
        wtxt = ws[0] if len(set(ws)) == 1 else '/'.join(ws)
        line = f"  {e['name']}: {len(ds)}×{rtxt} @ {wtxt}" + (f" RPE {e['rpe']}" if e.get('rpe') else '')
        if miss: line += f" ({miss} set(s) not done)"
        print(line)
    if s.get('notes'): print("  notes: " + ' / '.join(l.strip() for l in s['notes'].splitlines() if l.strip()))

# best per lift: squats → best e1RM (Epley, ≤10 reps); oly → heaviest completed
print("\n## Bests (all time)")
for k, name in MAXES.items():
    best = None
    for s in sessions:
        for e in s.get('exercises', []):
            if e['name'] != name: continue
            for x in e['sets']:
                wt, r = num(x.get('w')), reps(x.get('r'))
                if not x.get('done') or not wt: continue
                v = wt * (1 + r / 30) if k in ('bs', 'fs') and 1 < r <= 10 else wt
                if not best or v > best[0]: best = (v, wt, x.get('r'), s['date'])
    if best:
        tag = f"e1RM {best[0]:.1f}" if k in ('bs', 'fs') else 'top'
        print(f"  {name}: {tag} ({w(best[1])}×{best[2]} on {best[3]}) · working max {settings.get('maxes', {}).get(k, '-')}")

def wk(d): x = date.fromisoformat(d); return (x - timedelta(days=x.weekday())).isoformat()
weeks = defaultdict(lambda: {'sess': 0, 'legs': 0, 'cardio': 0})
for s in sessions:
    W = weeks[wk(s['date'])]; W['sess'] += 1
    W['legs'] += sum(len([x for x in e['sets'] if x.get('done')]) for e in s.get('exercises', []) if e['name'] in LEGS)
for c in by['cardio']: weeks[wk(c['date'])]['cardio'] += c.get('min') or 0
print("\n## Weeks (Mon): sessions · leg/glute sets · cardio min")
for k in sorted(weeks)[-8:]:
    W = weeks[k]; print(f"  {k}: {W['sess']} · {W['legs']} · {W['cardio']}")

cardio = [c for c in sorted(by['cardio'], key=lambda c: c['date']) if c['date'] >= since]
if cardio:
    print("\n## Cardio")
    for c in cardio: print(f"  {c['date']} {c['type']} {c.get('min')} min" + (f" {c['km']} km" if c.get('km') else '') + (f" — {c['notes']}" if c.get('notes') else ''))

ms = sorted(by['measure'], key=lambda m: m['date'])
if ms:
    keys = ['thighL', 'thighR', 'hips', 'waist', 'calf', 'bicep', 'forearm']
    print("\n## Measurements (cm)")
    for m in ms: print(f"  {m['date']}: " + ', '.join(f"{k} {m[k]}" for k in keys if m.get(k) is not None))
    if len(ms) > 1:
        a, b = ms[0], ms[-1]
        print("  change since first: " + ', '.join(f"{k} {b[k]-a[k]:+.1f}" for k in keys if num(a.get(k)) is not None and num(b.get(k)) is not None))
