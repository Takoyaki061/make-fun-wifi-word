#!/usr/bin/env python3
"""One Word for Your Wi-Fi — writes one word to /output/entry.txt.

The word: "Teenager".

Home Wi-Fi behaves like a teenager: it shuts itself in its room, only
works on its own terms, ignores you when you need it most, and emerges
exactly when it feels like it. Full bars in the kitchen, nothing in the
bedroom; fine all morning, gone the second your video call starts. One
word, no explanation needed — everyone who has lived with Wi-Fi has
lived with this.

Stdlib only, deterministic, no network.
"""

import os

WORD = "Teenager"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-20 characters,
    # not only whitespace, and a single word, or the entry scores 0
    # and never reaches the judge.
    if not 1 <= len(WORD) <= 20:
        raise ValueError(f"word is {len(WORD)} characters, must be 1-20")
    if not WORD.strip():
        raise ValueError("word must not be only whitespace")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("word must contain no whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the word that passed the gate above,
    # including its byte length (a multi-byte character would change it).
    with open(path, "rb") as f:
        raw = f.read()
    if raw != WORD.encode("utf-8"):
        raise ValueError("entry.txt on disk differs from the word")
    if len(raw) != len(WORD.encode("utf-8")):
        raise ValueError("entry.txt byte length differs from the word")
    print(WORD)


if __name__ == "__main__":
    main()
