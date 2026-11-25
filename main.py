# One Line, No Deadline Met — entry for u-markk-st-one-line-no-deadline-met-6adc00ce (make.fun).
# A program that writes one single-line joke excusing a missed deadline to entry.txt.
# Deterministic: the same joke bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library only.
import os

JOKE = (
    "I would've hit the deadline, but it filed a restraining order "
    "— legally I wasn't allowed within 500 feet of it."
)


def main():
    # Self-check the same gate the sealed scorer applies: 1-200 chars,
    # one line, not only whitespace. Fail loudly instead of writing junk.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
