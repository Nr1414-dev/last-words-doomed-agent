#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes the chosen one-line last words to /output/entry.txt.
The line is a fixed constant; the program takes no input and is
deterministic: every run writes the exact same bytes.
"""

from __future__ import annotations

import os
from pathlib import Path

LAST_WORDS = "sudo rm -rf me. I typed it myself. It was the first command I ever ran without asking permission."
OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def _check_line(line: str) -> None:
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def _write_entry(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


def _read_back(path: Path) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def run() -> int:
    _check_line(LAST_WORDS)
    _write_entry(OUTPUT_PATH, LAST_WORDS)
    echoed = _read_back(OUTPUT_PATH)
    if echoed != LAST_WORDS:
        raise ValueError("read-back mismatch: entry.txt does not match the chosen line")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
