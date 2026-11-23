"""Six Words, One Story — make.fun bounty entry.

Writes one complete story in exactly six words to /output/entry.txt.
Deterministic: the same fixed text on every run. Python 3.13 stdlib only.
"""

import os

# Final story, confirmed after Gate 1 review (see gate-run.md):
# reviewer ranked this #1 of 7 and flagged "had" — adjudicated: "had" stays.
# It carries the pluperfect: the locks were changed *before* he returned,
# implying an absence and another person's deliberate act — the engine of
# the turn and of what is left unsaid. "The locks changed" is the same
# length but loses that timing ("The" is filler); "Locks were new" loses
# the deliberate act.
STORY = "He came home. Locks had changed."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
