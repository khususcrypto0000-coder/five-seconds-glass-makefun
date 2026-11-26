"""Five Seconds to Explain the Glass — make.fun entry.

Writes the cat's own five-second defense to /output/entry.txt.
Deterministic: running this twice produces byte-identical output.
Standard library only, no network.
"""

ENTRY = (
    "That glass parked itself in my sunbeam and refused to move, "
    "so I evicted it to the floor."
)

OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> None:
    """Gate check: one sentence, 1-200 chars, no apology, no admission."""
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    lowered = text.lower()
    for banned in ("sorry", "my fault", "my bad", "i apologize"):
        assert banned not in lowered, "no apologies allowed"


def main() -> None:
    _validate(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
