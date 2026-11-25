"""The Tired Dark Lord: a 100-word villain monologue.

A fantasy villain, three centuries into the job, receives the hero
who came to end him -- and tries to hand over the crown instead,
provided the hero signs the paperwork first. The weariness lives
in the pauses, the trailing thoughts and the small deflections,
never in a plain announcement of it.

Pure Python 3.13 standard library, deterministic, no network.
Running this module prints the monologue and writes it to
/output/entry.txt (created if needed).
"""

from pathlib import Path

ENTRY = (
    "Come in. Mind the\u2014 no, leave the candles. I lit them three centuries "
    "ago, and never found the afternoon to relight them.\n"
    "\n"
    "You came for the sword, the prophecy, the girl in the tower. Yes, yes. "
    "I wrote the prophecy. The girl married a beekeeper. The sword rusted "
    "beside pickled wyverns.\n"
    "\n"
    "Here is the truth, hero: nine kingdoms, and every one needs a signature "
    "by Thursday. The goblins are striking. The dragon wants a raise.\n"
    "\n"
    "So. Take the crown. Just\u2014 sign here first, and tell the ravens I will "
    "answer their letters... eventually. I have the paperwork to prove it."
)

OUTPUT_PATH = Path("/output/entry.txt")

# Gate from the bounty brief: /output/entry.txt must be UTF-8 text of
# 1 to 600 characters, not only white space; the monologue itself is
# about 100 words.
MIN_CHARS = 1
MAX_CHARS = 600
TARGET_WORDS = 100


def word_count(text: str) -> int:
    """Count words the plain way: whitespace-separated tokens."""
    return len(text.split())


def validate(text: str) -> None:
    """Raise ValueError if the entry breaks the bounty gate."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters; gate requires "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    words = word_count(text)
    if words != TARGET_WORDS:
        raise ValueError(
            f"entry is {words} words; the brief asks for about "
            f"{TARGET_WORDS}"
        )


def main() -> None:
    # Validate the exact bytes the gate will read: the file holds
    # ENTRY plus its trailing newline, so a 600-character ENTRY
    # would otherwise ship as a 601-character file and fail.
    content = ENTRY + "\n"
    validate(content)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(ENTRY)
    print()
    print(
        f"[{word_count(content)} words, {len(content)} characters] "
        f"-> {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
