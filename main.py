"""Delete "mnemonic" from the dictionary.

The irony is self-referential: "mnemonic" is the word for remembering,
yet it is the word nobody can spell -- a silent m guarding a memory
trick you cannot remember. Delete it and the language loses its
memory-aid word while nobody can miss spelling it. A spelling trap
about spelling, in one word.
"""

import os

WORD = "mnemonic"


def _validate(word: str) -> None:
    """Gate: one non-whitespace word, 1-77 chars, UTF-8 safe."""
    assert 1 <= len(word) <= 77, "word length outside 1-77"
    assert word == word.strip(), "word must have no surrounding whitespace"
    assert word.strip() and not word.isspace(), "word must not be whitespace"
    assert len(word.split()) == 1, "entry must be a single word"
    word.encode("utf-8")


def main() -> None:
    _validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline.
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    # Post-write self-check: file must equal the word, and pass the gate.
    with open(path, "rb") as f:
        data = f.read()
    assert data == WORD.encode("utf-8"), "output mismatch"
    assert len(data) == 8, "expected 8 bytes"
    _validate(data.decode("utf-8"))


if __name__ == "__main__":
    main()
