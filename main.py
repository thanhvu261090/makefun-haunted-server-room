#!/usr/bin/env python3
"""Entry for make.fun bounty: Funniest Sign on a Haunted Server Room Door.

Writes one funny one-line sign for the door of a haunted server room
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "WARNING: Haunted. The previous admin still logs in at 3 a.m. and closes your tickets as 'works on my machine'."


def main():
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
