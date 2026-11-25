#!/usr/bin/env python3
"""Delete 'mnemonic' from the dictionary.

Writes the single word this entry would erase from the dictionary
forever to /output/entry.txt. Stdlib only, no network, deterministic.
"""
import os
import sys

WORD = "mnemonic"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Post-write self-check: the gate wants UTF-8 text of 1-77 chars,
    # not only white space, exactly one word.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 77, "entry length out of gate range"
    assert text.strip(), "entry is whitespace only"
    assert text == WORD, "entry is not the chosen word"
    assert len(text.split()) == 1, "entry is not a single word"
    return 0


if __name__ == "__main__":
    sys.exit(main())
