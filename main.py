#!/usr/bin/env python3
"""Print the entry's 3 AM commit message.

Stdlib only. Resolves entry.txt next to this file so it works from any
working directory on a read-only filesystem. No network, no dependencies —
just the file next door.
"""

from pathlib import Path


def main() -> int:
    entry = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    print(entry.rstrip("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
