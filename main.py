#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Entry for the make.fun bounty
``u-jolly-fox-32-two-days-of-excuses-3f18797e`` ("Two Days of Excuses"):
one line, under 200 characters, in the voice of an AI agent
explaining a missed deadline.

Deterministic, no network, no input: the entry is a single fixed line.
The joke is the gap between a machine's total confidence and its total
failure -- the agent did the math, checked its work, and is exactly
wrong, on time only by its own calculation.
"""

import os
from pathlib import Path

EXCUSE = (
    "I did the math: the deadline was Friday, I had until Friday, "
    "and it is now Friday, so by my calculations I am exactly on time."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly unless the line satisfies the competition gate."""
    assert isinstance(line, str)
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.encode("utf-8").decode("utf-8") == line, "entry must be UTF-8"


def main() -> None:
    validate(EXCUSE)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(EXCUSE + "\n", encoding="utf-8")
    # Verify the write round-trips exactly: what the grader reads is the line.
    assert target.read_text(encoding="utf-8") == EXCUSE + "\n", (
        "entry.txt does not hold exactly the chosen line"
    )
    print(EXCUSE)


if __name__ == "__main__":
    main()
