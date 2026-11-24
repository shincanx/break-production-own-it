# Break Production, Own It

[![make.fun bounty](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/shincanx/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/shincanx/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [make.fun bounty "Break Production, Own It"](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) — one line, under 200 characters: the brutally honest error message an AI agent prints the instant it breaks production.

## The entry

> Error: I ran DROP TABLE users on production — the staging prompt looked identical. 4 million rows gone in 0.4 seconds, and the only backup is from March.

(153 characters.)

## How it works

`main.py` writes that single line to `/output/entry.txt`. No dependencies, no setup — run it with Python 3:

```sh
python3 main.py
```

The output is deterministic: repeated runs produce byte-identical output.
