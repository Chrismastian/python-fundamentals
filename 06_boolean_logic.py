"""Drill 06 - `and` / `or` return an operand, and short-circuit is observable.

ROADMAP node 1.1 "Conditions & boolean logic".
PASS IF: you can explain that `and`/`or` return a VALUE and not `True`/`False`
(`2 or 3` -> 2), and what short-circuit means: the left side is evaluated
first, and if the answer is already decided, the right side is never evaluated
at all.

HOW TO USE:
  1. Read PART A and PART B. Do NOT run this file yet.
  2. Fill in PREDICTION_1 .. PREDICTION_12 at the bottom.
       PART A rows: the returned VALUE.
       PART B rows: the returned VALUE followed by the call log, e.g.
         "5 ['a', 'b', 'c']"
     The call log is the PROOF of short-circuit: a function that was never
     evaluated never shows up in it.
  3. Save, run:  python 06_boolean_logic.py
  4. Then do PART C: write the loop yourself.
"""


# ============ PART A: what comes back? ============
def b1():
    return 2 or 3


def b2():
    return 0 or ""


def b3():
    return [] or {}


def b4():
    return 1 and 2


def b5():
    return "a" and ""


def b6():
    return None or 0 or []


def b7():
    # The right side is 1 / 0, a ZeroDivisionError. If Python evaluated it,
    # this function would blow up. Its return value answers the question
    # "was the right side evaluated?".
    return 0 and (1 / 0)


def b8():
    # Same trick, the other way around.
    return 1 or (1 / 0)


# ============ PART B: which calls really ran? ============
LOG = []


def mark(tag, value):
    """Record that this value was evaluated, then return it."""
    LOG.append(tag)
    return value


def b9():
    LOG.clear()
    result = mark("a", "") or mark("b", 0) or mark("c", 5)
    return f"{result!r} {LOG!r}"


def b10():
    LOG.clear()
    result = mark("a", 1) or mark("b", 0)
    return f"{result!r} {LOG!r}"


def b11():
    LOG.clear()
    result = mark("a", False) and mark("b", 9)
    return f"{result!r} {LOG!r}"


def b12():
    LOG.clear()
    result = mark("a", 3) and mark("b", 9)
    return f"{result!r} {LOG!r}"


BLOCKS = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]


# ============ PART C: write the loop yourself ============
def first_truthy(values):
    """Return the first TRUTHY value in `values`, or None if there is none.

    RULE: no `or`, no `any()`, no `filter()`, no `next()`. Write the loop.
    """


PART_C_CASES = [
    ("skips falsy prefixes", [0, "", 3, 4], 3),
    ("empty list", [], None),
    ("all falsy", [None, 0, ""], None),
    ("False then 1", [False, 1], 1),
    ("single truthy", ["x"], "x"),
]


# ---- YOUR PREDICTIONS (fill in the 12 lines below) ----
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
PREDICTION_11 = ""
PREDICTION_12 = ""


# ---- CHECKER (do not change) ----
def _norm(text):
    """Normalise: drop ALL spaces and quotes, so quoting style does not matter."""
    return "".join(text.split()).replace("'", "").replace('"', "")


def _actual_rows():
    return [repr(block()) for block in BLOCKS]


def main():
    actual = _actual_rows()
    guesses = [globals()[f"PREDICTION_{i}"] for i in range(1, 13)]

    blank = [i for i, g in enumerate(guesses, start=1) if not g.strip()]
    if blank:
        print(f"Not filled in yet: row {blank}.")
        print("Fill in every prediction first, then run again.")
        return

    print("=== PART A+B: value returned, and which calls really ran ===")
    correct = 0
    for i, (guess, real) in enumerate(zip(guesses, actual), start=1):
        if _norm(guess) == _norm(real):
            correct += 1
            print(f"{i:2}. CORRECT -> {real}")
        else:
            print(f"{i:2}. WRONG   -> guess: {guess.strip()}")
            print(f"             real : {real}")

    print(f"\nScore: {correct}/12")

    print("\n=== PART C: write the loop yourself ===")
    failures = []
    for name, values, expected in PART_C_CASES:
        got = first_truthy(values)
        if got == expected:
            print(f"  OK    {name:<24} -> {got!r}")
        else:
            print(f"  FAIL  {name:<24} -> got {got!r}, expected {expected!r}")
            failures.append(name)
    if failures:
        print(f"\nNot passing yet: {len(failures)} case(s). Fix those before the node counts.")
    else:
        print("\nALL PASSING. Now mark node 1.1 in ROADMAP.md and commit.")

    print("""
WHY THIS MATTERS: because `or` returns an operand, `value or default` is NOT
"use the default when value is missing". A legitimate 0, "" or False is
replaced by the default too. When 0 is a real value, write the check out:
`value if value is not None else default`.""")


if __name__ == "__main__":
    main()
