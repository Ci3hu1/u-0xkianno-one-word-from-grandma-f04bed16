#!/usr/bin/env python3
"""One Word From Grandma.

Writes a single word to /output/entry.txt (or to the path given as the
first argument, for local testing).

The word is ROBUT: the typo a grandma would actually make texting about
AI. She means "robot" and her phone, her fingers, or her autocorrect
turns it into ROBUT. One word, five letters, and the joke is the typo
itself -- no setup needed, no language barrier, and it reads instantly
as a grandma texting about the machine that talks back.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

WORD = "ROBUT"

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 30


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not (MIN_CHARS <= len(WORD) <= MAX_CHARS):
        print(
            f"word is {len(WORD)} chars, must be {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not WORD.strip():
        print("word is only whitespace", file=sys.stderr)
        return 1
    if len(WORD.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    os.chmod(output_path, 0o644)

    print(f"wrote {len(WORD)} chars to {output_path}")
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
