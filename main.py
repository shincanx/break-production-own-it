#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line — the error message an AI agent prints
the instant it breaks production — to /output/entry.txt and stdout.
No network, no dependencies, fully deterministic.
"""

import os

ENTRY = (
    "Error: I ran DROP TABLE users on production \u2014 the staging prompt "
    "looked identical. 4 million rows gone in 0.4 seconds, and the only backup "
    "is from March."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
