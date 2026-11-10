"""Drill 07 - boundaries and off-by-one.

ROADMAP node 1.4 "Boundaries & off-by-one".
PASS IF: you can explain why `range(5)` stops at 4, and `range(len(x))` vs
`enumerate(x)`.

HOW TO USE:
  1. Read PART A and PART B. Do NOT run this file yet.
  2. Fill in PREDICTION_1 .. PREDICTION_10 at the bottom.
  3. Save, run:  python 07_boundaries.py
  4. Then do PART C: write both functions yourself.

THE ONE RULE BEHIND ALL OF IT: a Python slice and `range` are HALF-OPEN.
`[start, stop)` - the start is included, the stop is never included. Length is
`stop - start`, which is why `range(5)` has 5 items but its last one is 4.
"""


# ============ PART A: where does it stop? ============
def b1():
    return list(range(5))


def b2():
    return list(range(1, 6))


def b3():
    return list(range(0, 10, 3))


def b4():
    # A step can be negative. Which direction does the half-open rule run?
    return list(range(5, 0, -2))


def b5():
    # len() of a range is computed, not counted: no list is built.
    return len(range(2, 8))


def b6():
    return "abcdef"[1:4]


def b7():
    # start > stop with a positive step: how many items fit in an empty span?
    return "abcdef"[4:1]


def b8():
    return "abcdef"[-2:]


def b9():
    return list(range(len("abc")))


def b10():
    return [f"{i}:{c}" for i, c in enumerate("ab", start=1)]


BLOCKS = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]


# ============ PART C: write them yourself ============
def even_indexes(numbers):
    """Return the indexes of the EVEN numbers in `numbers`, in order.

    RULE: no `enumerate()`, no list comprehension. Use `range(len(...))` and
    index into the list yourself. That is the version you must be able to read
    in other people's code.
    """


def numbered(lines):
    """Return the lines as "1. first", "2. second", ... starting at 1.

    RULE: no manual counter variable (`i += 1`). Use the tool that already
    produces the index and the item at the same time.
    """


PART_C_CASES = [
    ("even_indexes", even_indexes, [[3, 4, 7, 8, 10]], [1, 3, 4]),
    ("even_indexes none", even_indexes, [[1, 3, 5]], []),
    ("even_indexes empty", even_indexes, [[]], []),
    ("numbered", numbered, [["a", "b"]], ["1. a", "2. b"]),
    ("numbered one", numbered, [["only"]], ["1. only"]),
    ("numbered empty", numbered, [[]], []),
]


# ---- YOUR PREDICTIONS (fill in the 10 lines below) ----
PREDICTION_1 = ""
PREDICTION_2 = ""
PREDICTION_3 = ""
PREDICTION_4 = ""
PREDICTION_5 = ""
PREDICTION_6 = ""
PREDICTION_7 = ""
PREDICTION_8 = ""
PREDICTION_9 = ""
PREDICTION_10 = ""


# ---- CHECKER (do not change) ----
def _norm(text):
    """Normalise: drop ALL spaces and quotes, so quoting style does not matter."""
    return "".join(text.split()).replace("'", "").replace('"', "")


def main():
    actual = [repr(block()) for block in BLOCKS]
    guesses = [globals()[f"PREDICTION_{i}"] for i in range(1, 11)]

    blank = [i for i, g in enumerate(guesses, start=1) if not g.strip()]
    if blank:
        print(f"Not filled in yet: row {blank}.")
        print("Fill in every prediction first, then run again.")
        return

    print("=== PART A: where does it stop? ===")
    correct = 0
    for i, (guess, real) in enumerate(zip(guesses, actual), start=1):
        if _norm(guess) == _norm(real):
            correct += 1
            print(f"{i:2}. CORRECT -> {real}")
        else:
            print(f"{i:2}. WRONG   -> guess: {guess.strip()}")
            print(f"             real : {real}")

    print(f"\nScore: {correct}/10")

    print("\n=== PART C: write them yourself ===")
    failures = []
    for name, fn, args, expected in PART_C_CASES:
        try:
            got = fn(*args)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        if got == expected:
            print(f"  OK    {name:<20} -> {got!r}")
        else:
            print(f"  FAIL  {name:<20} -> got {got!r}, expected {expected!r}")
            failures.append(name)
    if failures:
        print(f"\nNot passing yet: {len(failures)} case(s). Fix those before the node counts.")
    else:
        print("\nALL PASSING. Now mark node 1.4 in ROADMAP.md and commit.")

    print("""
WHY THIS MATTERS: the same half-open rule causes the two most common bugs in
the wild - `range(1, n)` when you meant `range(n)` (the loop runs n-1 times),
and `for i in range(len(items))` where `i` is used as a value instead of an
index. When you only need the items, `for item in items` cannot go off by one
at all.""")


if __name__ == "__main__":
    main()
