"""Make the AI Judge Laugh: Developer Excuses (Python 3.13, stdlib only).

Writes one funny single-line developer excuse for code breaking in
production to /output/entry.txt (MAKEFUN_OUTPUT_DIR outside the grader).
"""

import os
from pathlib import Path

EXCUSE = "It passed all 400 tests. Production was test 401."
MAX_CHARS = 200


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry(text: str) -> None:
    """Raise unless the entry meets the gate: 1-200 chars, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    check_entry(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back mismatch: written text differs")
    return target


def main() -> None:
    target = write_entry(EXCUSE)
    print(f"wrote {target} ({len(EXCUSE)} chars)")


if __name__ == "__main__":
    main()
