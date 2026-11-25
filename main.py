#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line (at most 140 characters) inventing the most useless
superpower to /output/entry.txt.
"""

import os

ENTRY = "I can read minds \u2014 but only my own, and only thoughts I've already had."


def main() -> None:
    # Gate self-check: 1 to 140 characters, not only white space.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
