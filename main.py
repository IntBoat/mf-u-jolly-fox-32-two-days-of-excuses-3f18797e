#!/usr/bin/env python3
"""Two Days of Excuses — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I finished the task on time — unfortunately, 'on time' was measured in a timezone that doesn't exist yet."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
