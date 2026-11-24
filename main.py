"""One Word, First Thought — writes exactly one word to entry.txt.

The word is "petrichor": the scent of rain on dry earth. Surprising,
vivid and specific — one breath of it calls up a whole summer storm —
with a soft, rolling sound that rewards a second look.
"""

import os

WORD = "petrichor"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
