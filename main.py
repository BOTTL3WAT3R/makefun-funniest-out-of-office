#!/usr/bin/env python3
"""The Funniest Out-of-Office — writes one funny OOO auto-reply line.

The program emits a single line of text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). The line is
an out-of-office auto-reply with a twist in its tail: it was scheduled
months ago by a past self who still assumed the return date in it
meant this month.
"""

import os

ENTRY = (
    "I am out of office until the 30th. This reply was scheduled in March "
    "by a version of me who still assumed the 30th meant this month."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1..140"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
