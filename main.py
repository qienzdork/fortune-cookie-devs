#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $OUTPUT_PATH when set). Deterministic, stdlib only,
no randomness, no network.
"""

import os

FORTUNE = (
    "The bug you cannot reproduce is teaching you patience; "
    "the one you can is teaching you humility."
)


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()
