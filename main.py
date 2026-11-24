"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "If your laptop overheats, put it in the freezer overnight "
    "\u2014 condensation is just extra cooling."
)


def main():
    if not LINE.strip() or "\n" in LINE or len(LINE) > 140:
        raise ValueError("entry line must be one non-blank line of 1-140 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
