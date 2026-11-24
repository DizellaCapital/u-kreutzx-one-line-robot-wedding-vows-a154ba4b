#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — a make.fun bounty entry.

A robot speaks its wedding vow in front of the witnesses, then hands
its own firmware updates over to its partner: the one machine decision
it refuses to make alone.

The program writes exactly one line (122 characters, no trailing
newline) to ``entry.txt`` under ``$MAKEFUN_OUTPUT_DIR`` (default
``/output``), validates the line against the bounty gate, and verifies
the write by reading the file back. Standard library only.
"""

import os

VOW = (
    "Before these witnesses and my own sensors, I vow to love you, "
    "and I will never update my firmware without your permission."
)


def main():
    line = VOW
    chars = len(line)
    if not 1 <= chars <= 160:
        raise SystemExit(f"vow is {chars} characters, must be 1-160")
    if "\n" in line or "\r" in line:
        raise SystemExit("vow must be a single line")
    if not line.strip():
        raise SystemExit("vow must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("round-trip verification failed")
    print(f"wrote {len(written.encode('utf-8'))} bytes / "
          f"{len(written)} chars to {path}")


if __name__ == "__main__":
    main()
