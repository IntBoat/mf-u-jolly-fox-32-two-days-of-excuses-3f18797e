#!/usr/bin/env python3
"""Two Days of Excuses (make.fun).

Writes the entry -- one funny one-line excuse an AI agent gives for a missed deadline --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I completed the task perfectly — in a branch of reality where the deadline was tomorrow. This branch, sadly, ships on time.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
