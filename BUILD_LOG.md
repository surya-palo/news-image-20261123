# BUILD_LOG — news-image-20261123

Poster: "THE WORLD IN ONE DAY — MONDAY 23 NOVEMBER 2026" (1024×1024 PNG).
Built 23 Nov 2026, ~07:00 WIB, by web research + a from-scratch Pillow
renderer (`render_poster.py`). No file from any other entry was read or reused.

## Stories used (all happened or were first reported Mon 23 Nov 2026)

1. **Lead — Wall Street braces after AI sell-off.** S&P 500 fell 3.7% and
   Nasdaq 5.3% on Friday 20 Nov (worst week in 18 months); US futures
   pointed higher on Monday 23 Nov as Asian markets braced for more swings.
   Source: Reuters global markets report, 23 Nov 2026 (via HeadlinesXtra,
   dateline New York, 23 Nov 2026).
2. **Nepal PM meets Modi in Delhi.** PM Balendra Shah holds delegation-level
   talks with PM Narendra Modi on Monday 23 Nov (energy, trade, connectivity),
   his first bilateral trip abroad since taking office in March 2026.
   Source: IANS via New Kerala / The Freedom Press, 22 Nov (talks dated 23 Nov);
   India's MEA statement.
3. **COP31 fallout: "worst ever".** Framed strictly as the 23 Nov reaction:
   a day after the Antalya talks ended with no deal, governments and
   campaigners trade blame; first COP to fail outright since 2009.
   Source: AP via Juneau Independent / NPR, 22 Nov (collapse); The Hindu,
   23 Nov 01:05 IST, and Nov 23 roundups listing the fallout as the day's
   top story.
4. **Search resumes at torched factory.** Rescuers return at dawn on Monday
   23 Nov to the ruined PT Fonusa Agung Mulia candy factory in Cikande, Java;
   dozens still missing after Saturday's blaze, at least three dead.
   Source: Reuters, 22 Nov (search "scheduled to resume on Monday morning");
   AP via Daily Fox News (crews resume 7 a.m. Monday 23 Nov).
5. **India hunt eight wickets on final day.** Wellington Test, day 5 (Mon 23
   Nov): New Zealand resume 119/2, still 233 behind after India's record
   720/9 — the highest Test total ever made in New Zealand (set Sun 22 Nov,
   cited here only as context for the final day).
   Source: ESPNcricinfo / Cricbuzz match report, 19–23 Nov 2026.
6. **Home Depot's new chief takes over.** Richard McPhail becomes CEO
   effective 23 Nov 2026, stepping up from CFO.
   Source: Home Depot announcement 17 Nov 2026, confirmed by Reuters/CNBC.

Numbers box: −3.7% S&P 500 (Fri), −5.3% Nasdaq (Fri), 720/9 India's total,
~50 workers missing in Java — all figures from the sources above.

## Stories checked and DISCARDED (with reason)

- **COP31 collapse as a 23 Nov event** — the talks ended Sunday 22 Nov
  (WRI statement dated 22 Nov; AP "ended Sunday night"). Only the 23 Nov
  fallout/reaction is used, and it is labelled "fallout".
- **BepiColombo enters Mercury orbit** — happened 21 Nov (Nature, ESA).
- **South Korea education minister resigns over AI cheating** — Sunday 22 Nov
  (Korea JoongAng Daily, KBS 22 Nov).
- **Democrats clinch 258 House seats** — Sunday 22 Nov (AP, 22 Nov 17:13 EST).
- **WHO chief: fighting disrupts Congo Ebola response** — Sunday 22 Nov
  (Reuters, 22 Nov 20:17 UTC).
- **Russian cargo ship Sparta II on fire off Finland** — drone strike Sat
  21 Nov (Reuters, 21 Nov); still burning 22 Nov.
- **Dymer drone strike, 14 missing near Kyiv** — Sunday 22 Nov (Euronews,
  Zelenskyy post 22 Nov).
- **Indonesia factory fire outbreak** — broke out Sat 21 Nov; only the
  Monday 23 Nov search resumption is used.
- **Trump meme-coin gala** — Sunday night 22 Nov (Reuters, 22 Nov).
- **Poland: Russia twice tried to kill rapper Kyivstoner** — revealed Sunday
  22 Nov (AP, 22 Nov 15:41 EST); the plots themselves were Aug/Sep.
- **Trump–Putin–Xi trilateral summit, Shenzhen** — 19 Nov (RFE/RL, 20 Nov).
- **Houthi strikes on Riyadh** — Thu 20 – Sun 22 Nov (third straight day
  was Sunday 22 Nov); no verified 23 Nov strike found.
- **South Sudan cattle-camp attack, 24 dead** — Sat 21 – Sun 22 Nov (AFP).
- **USS Theodore Roosevelt arrival in the Middle East** — 15–16 Nov; a
  pipeline article claiming a Monday confirmation was misdated (its own
  sources date the arrival to 16 Nov).
- **"Monday" Hormuz tanker mine claims** — contradictory dating: the same
  mine claims are dated Sun 22 Nov by Reuters/Argus; the single source
  saying "Monday" is an AI pipeline ingest whose other "Monday" claim
  (the Roosevelt) is provably wrong. Not used.
- **"Riemann hypothesis solved" claim** — explicitly unverified (Global Eye
  live wire, 22 Nov). Not used.
- **Alcaraz ATP Finals title; Liverpool 4–0 Man Utd** — both Sun 22 Nov.
- **India 720/9 record itself** — set Sun 22 Nov; used only as context for
  the Mon 23 Nov final day.

## Render / verification

- `render_poster.py` draws the poster with Pillow (DejaVu Serif/Sans).
  Three visual-check passes: v1 had the lead body overflowing its box and
  card headlines colliding with icons; v2 fixed the lead body and icon
  clearance but the chart labels ran together; v3 moved the labels and the
  caption collided with them; v4 (final) is clean — no overlap, no clipped
  text, legible at 300 px.
- Final `entry.png`: 1024×1024, RGB PNG, 144,677 bytes (≤ 1 MiB),
  SHA-256 `71b3ed1f3e28890953fe558edef0f4f9ff08d89e961dfb53a992bb1434dfb266`.
- `main.py` (stdlib only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`) and verifies the SHA-256 and byte size; run twice into
  two directories, outputs byte-identical (see Verification below).
- `main.py` was revised after the first commit (added PNG magic-byte and
  1 MiB size-cap checks) — second commit.

## Verification (23 Nov 2026, 00:14 WIB)

- Run 1: `MAKEFUN_OUTPUT_DIR=out1 python3 main.py` → wrote 144,677 bytes,
  sha256 `71b3ed1f3e28890953fe558edef0f4f9ff08d89e961dfb53a992bb1434dfb266`
- Run 2: `MAKEFUN_OUTPUT_DIR=out2 python3 main.py` → identical output,
  same sha256
- `cmp out1/entry.png out2/entry.png` → identical (byte-identical, deterministic)
- Image gate: PNG magic bytes OK, 1024×1024, 144,677 bytes ≤ 1,048,576
- Visual check: final render reviewed at full size — no overlap, no clipped
  text, legible; footer and sources line intact.
