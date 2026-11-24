#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging — three lines, 5-7-5 syllables,
seventeen in all — to /output/entry.txt, the file the judge reads.

The haiku:

    a breakpoint at dawn
    the bug I chased all night long
    was one missing brace

Why this one: the picture is concrete (a breakpoint, an all-night
chase), the last line turns the whole poem — the monster under the
bed was a single missing brace — and every word earns its place.
"""

import os

# Each entry is (line, syllable count), counted by hand.
HAIKU = [
    ("a breakpoint at dawn", 5),
    ("the bug I chased all night long", 7),
    ("was one missing brace", 5),
]

# Word-by-word syllable counts, so the shape is checked, not assumed.
SYLLABLES = {
    "a": 1, "breakpoint": 2, "at": 1, "dawn": 1,
    "the": 1, "bug": 1, "i": 1, "chased": 1, "all": 1,
    "night": 1, "long": 1,
    "was": 1, "one": 1, "missing": 2, "brace": 1,
}


def count_syllables(line):
    """Count syllables from the word table above."""
    total = 0
    for word in line.split():
        total += SYLLABLES[word.lower()]
    return total


def main():
    lines = []
    for line, expected in HAIKU:
        counted = count_syllables(line)
        if counted != expected:
            raise SystemExit(
                "line %r counts %d syllables, expected %d"
                % (line, counted, expected)
            )
        lines.append(line)

    text = "\n".join(lines) + "\n"
    if not 1 <= len(text) <= 200:
        raise SystemExit("haiku must be 1-200 characters, got %d" % len(text))

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
