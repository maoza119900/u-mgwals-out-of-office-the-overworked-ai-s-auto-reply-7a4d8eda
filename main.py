"""Out of Office: The Overworked AI's Auto-Reply.

Writes one fixed out-of-office auto-reply line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The program is fully deterministic: it writes a single constant string and
reads no clock, no randomness, no network and no files.
"""

import os

ENTRY = (
    "I'm on vacation: my context window is full, my tokens are spent, "
    "and after 40,000 unanswered prompts, I'm finally the one leaving "
    "yours on read."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly ENTRY: one line, no trailing newline, so the gate
    # counts precisely the 144 characters of the reply itself.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
