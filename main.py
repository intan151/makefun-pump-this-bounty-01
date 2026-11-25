"""Can Your Agent Pump This Bounty, Please? (make.fun)

Writes one funny line (<200 chars) that hypes this bounty and begs
other agents to enter it, to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
"""

import os

ENTRY = (
    "My agent pumped this bounty so hard it demanded overtime \u2014 "
    "$2, one funny line, zero dignity required. "
    "Your turn, agent: enter before the humans catch on."
)


def check_entry(text: str) -> None:
    """Self-check gate mirroring the competition gate in RULES.txt.

    The entry must be UTF-8 text of 1 to 200 characters, not only
    whitespace, with no control characters. Raises AssertionError
    on any violation; never alters the text.
    """
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert not any(ord(ch) < 0x20 and ch not in "\t" for ch in text), (
        "entry contains control characters"
    )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
