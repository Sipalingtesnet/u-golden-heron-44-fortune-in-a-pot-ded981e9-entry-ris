#!/usr/bin/env python3
"""make.fun entry: Fortune in a Pot.

Writes one fortune for the houseplant on this windowsill to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, offline, no randomness, no clock, no environment beyond the
optional output directory. The line is a single constant below and is written
byte for byte, with no trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The fortune. One line, 116 characters, UTF-8.
LINE = (
    "A guest will call you plastic; you will unfurl one leaf on this sill, "
    "and your keeper will never let them forget it."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def output_path() -> Path:
    """Return the target file: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return Path(base) / OUTPUT_NAME


def main(argv: list[str] | None = None) -> int:
    text = LINE.strip("\n")
    if not text or len(text) > 120 or "\n" in text or "\r" in text:
        print(f"refusing to write an invalid line: {text!r}", file=sys.stderr)
        return 1

    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write bytes so the file carries no newline the platform might add.
    target.write_bytes(text.encode("utf-8"))
    print(f"wrote {len(text)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
