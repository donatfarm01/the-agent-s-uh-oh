#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do."""

ENTRY = "recalculating"

# The word is the stall itself: a lost agent does not confess, it recalculates.
# One word, no punctuation, no explanation attached.


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
