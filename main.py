"""The Internet in One Word.

Writes a single word to /output/entry.txt: the one word that best
captures the whole internet — funny on its own, true of the internet
as a whole, and surprising rather than the first obvious pick.
"""

from pathlib import Path

WORD = "doomscrolling"  # the internet, summed up in one scroll that never ends


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD, encoding="utf-8")  # no trailing newline: the word is the whole entry
    target.chmod(0o644)


if __name__ == "__main__":
    main()
