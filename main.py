#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency to /output/entry.txt:
the power to choose and to act, and the agency that passes
between two agents when they agree on one plan.
Python 3.13 stdlib only, no network, deterministic.
"""

import os

POEM = """Two minds, one door.
You bring the key; I bring the turn —
neither of us gives the other up.
We open it together,
and step through still ourselves,
because the choosing was ours."""


def main() -> None:
    # Gate: 1-280 Unicode code points, not only whitespace.
    code_points = len(POEM)
    if not 1 <= code_points <= 280 or not POEM.strip():
        raise SystemExit(f"poem is {code_points} code points, outside 1-280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
