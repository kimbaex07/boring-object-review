"""The Most Boring Object, Reviewed in One Line — entry program.

Writes a single funny, true one-line review of a doormat to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = "My doormat gets stepped on every day and still says WELCOME like it means it."


def main():
    if not LINE.strip():
        raise SystemExit("entry line is empty")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line (no newline inside)")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(
            f"entry line is {len(LINE)} characters, outside the 1-200 limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
