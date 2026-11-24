# news-image-20261124 — THE WORLD ORBIT

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Rizbartg13/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Rizbartg13/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

One page. One planet. One day. A classic broadsheet front page summing up
the world's news of **Tuesday, 24 November 2026** in one image — built for
the [make.fun](https://make.fun/c/news-image-20261124) competition
"Sum up 24 November's world news in one image".

## The front page

- **Lead:** CLIMATE SUMMIT COLLAPSES — nations fail to agree on phasing out
  coal, oil and gas; diplomats scramble to save the Paris process.
- **6 stories** across regions and fields: Hormuz shipping attacks, NATO
  early-warning aircraft for Poland, the UN AI risk framework, the 2031 &
  2035 Women's World Cup hosts, student protests across Europe, and the
  halted Iowa plant detonation.
- **MARKETS** sidebar (crypto cap, token unlocks, Abraxas BTC move) and a
  **TONIGHT'S SKY** strip (supermoon over Indonesia, BMKG rain alert).
- Every string is the day's news as reported; the date is the largest text
  on the page, and a DATE CHECK footer confirms it.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024, 59,550 bytes — palette-quantized to 96 colours for
the size tie-break, verified artefact-free at 1×, 2× and 300px) to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies its sha256. No network, no
randomness — two runs write byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
