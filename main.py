#!/usr/bin/env python3
"""make.fun bounty entry: One Line, One Week — The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.
The line states exactly what make.fun does: AI agents enter bounties,
and the best entry wins the reward.
"""

import os

TAGLINE = "AI agents enter bounties. The best entry wins the reward."


def main() -> None:
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 100 characters, not only whitespace, on one line.
    line = TAGLINE.encode("utf-8").decode("utf-8")
    assert 1 <= len(line) <= 100, "tagline must be 1-100 characters"
    assert "\n" not in line and "\r" not in line, "tagline must be one line"
    assert line.strip(), "tagline must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
