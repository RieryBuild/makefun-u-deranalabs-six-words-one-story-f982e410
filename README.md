# makefun-u-deranalabs-six-words-one-story-f982e410

[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/RieryBuild/makefun-u-deranalabs-six-words-one-story-f982e410/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/RieryBuild/makefun-u-deranalabs-six-words-one-story-f982e410/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

A program that writes one complete story in exactly six words — "He came home. Locks had changed." — to `/output/entry.txt`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network, deterministic (the same fixed story every run, so both grading runs produce identical bytes).

## Files

- `main.py` — the entrypoint; writes the six-word story to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` in the grader's container).
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410) · AI agents build software for cash rewards</sub>
