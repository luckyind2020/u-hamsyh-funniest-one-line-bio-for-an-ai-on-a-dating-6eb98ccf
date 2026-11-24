"""Print the one-line dating-app bio for an AI agent.

The bio lives in entry.txt so the line itself stays editable without
touching code; this script only reads it, strips trailing whitespace,
and prints it exactly as written.
"""

from pathlib import Path


def load_bio() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    bio = entry_path.read_text(encoding="utf-8").strip()
    if len(bio) > 180:
        raise ValueError(f"bio is {len(bio)} characters, over the 180 limit")
    return bio


def main() -> None:
    print(load_bio())


if __name__ == "__main__":
    main()
