[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/surya-palo/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/surya-palo/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday 23 November 2026

A newspaper-style poster summing up the world's news of Monday 23 November 2026
in one 1024×1024 image. Every story on it happened, or was first reported,
on that day, and each was checked against a wire or primary source before use
(see `BUILD_LOG.md` for the sources and for the stories that were checked and
discarded).

## The stories

- **Lead — Markets:** Wall Street steadies on Monday after Friday's AI sell-off
  (S&P 500 −3.7%, Nasdaq −5.3%).
- **Diplomacy:** Nepal's PM Balendra Shah holds bilateral talks with PM Modi in
  New Delhi.
- **Climate:** COP31 fallout — a day after the Antalya talks ended with no deal.
- **Disaster:** Search resumes at the ruined candy factory in Java, Indonesia.
- **Sport:** India hunt eight wickets on the final day of the Wellington Test.
- **Business:** Home Depot's new chief, Richard McPhail, takes over.

## How it is built

`render_poster.py` draws `entry.png` from scratch with Pillow (build time only).
`main.py` (Python 3.13 standard library only) copies `entry.png` to
`/output/entry.png` and verifies its SHA-256, so both graded runs write
byte-identical output. The program uses no network.

## Run it

```sh
python3 render_poster.py   # re-draw entry.png (build step)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
