"""Drill 04 - reading tracebacks & debugging by hypothesis.

This is the core of "you fix it yourself" versus "you ask an AI about every
error".

HOW TO USE:
  1. Read the code below. Every function HAS A BUG.
  2. Do NOT run it yet. Read, then predict: which error, on which line?
  3. Write your predictions in PREDICTION_1 .. PREDICTION_5.
  4. Save, run:  python 04_traceback.py
  5. Compare. A wrong prediction is a hole in your traceback reading.
  6. Then FIX the buggy functions (not the predictions) until all pass.

RULE: when you hit an error, do not change code at random. Write a hypothesis
first: "I think the failure is X, and I will prove it by printing Y".
Print, compare, and only then fix.
"""


def func_1():
    """Bug: index that does not exist."""
    data = [10, 20, 30]
    return data[3]


def func_2():
    """Bug: key that is not in the dict."""
    profile = {"name": "Ani", "age": 25}
    return profile["address"]


def func_3(items):
    """Bug: mutating a list while iterating over it."""
    for item in items:
        if item % 2 == 0:
            items.remove(item)
    return items


def func_4(n):
    """Bug: recursion without a correct base case."""
    if n == 0:
        return 1
    return n * func_4(n - 1)


def func_5():
    """Bug: variable referenced before assignment."""
    if True:
        x = 10
    return y


# ---- YOUR PREDICTIONS (fill in the 5 lines) ----
# Write e.g. "IndexError line 21", "KeyError 'address'", "RecursionError ...".
PREDICTION_1 = ""
PREDICTION_2 = ""
PREDICTION_3 = ""
PREDICTION_4 = ""
PREDICTION_5 = ""


# ---- CHECKER (do not change) ----
def _norm(text):
    return "".join(text.lower().split()).replace("'", "").replace('"', "")


def main():
    tests = [
        ("func_1", func_1, []),
        ("func_2", func_2, []),
        ("func_3", func_3, [[1, 2, 3, 4, 5]]),
        ("func_4", func_4, [5]),
        ("func_5", func_5, []),
    ]

    print("=== PREDICTION vs ACTUAL ===")
    for i, (name, fn, args) in enumerate(tests, 1):
        guess = globals()[f"PREDICTION_{i}"]
        try:
            fn(*args)
            actual = "NO ERROR (silent bug)"
        except Exception as e:
            actual = f"{type(e).__name__}: {e}"

        if not guess.strip():
            print(f"{i}. EMPTY     -> actual: {actual}")
        elif _norm(guess) in _norm(actual) or _norm(actual) in _norm(guess):
            print(f"{i}. CORRECT   -> {actual}")
        else:
            print(f"{i}. WRONG     -> guess: {guess}")
            print(f"                actual: {actual}")

    print("\n=== NOW FIX THE BUGGY FUNCTIONS ===")
    print("Change func_1 .. func_5 so they raise no error AND return the right value.")
    print("Fix hints:")
    print("  1. IndexError -> check the list length first, or use an index that exists")
    print("  2. KeyError   -> use .get(), or check 'key in dict'")
    print("  3. Mutation while iterating -> build a new list, or iterate backwards")
    print("  4. Recursion  -> func_4(5) should be 120 (5!), check the argument")
    print("  5. UnboundLocalError -> y is never defined, typo?")

    # Verify whether the bugs are fixed (no error + correct result)
    print("\n=== RESULT AFTER THE FIX ===")
    passing = 0
    for name, fn, args in tests:
        try:
            result = fn(*args)
            if name == "func_1" and result == 30:
                print(f"  {name}: OK -> {result}")
                passing += 1
            elif name == "func_2" and result is None:
                print(f"  {name}: OK -> {result} (.get returned None)")
                passing += 1
            elif name == "func_3" and result == [1, 3, 5]:
                print(f"  {name}: OK -> {result}")
                passing += 1
            elif name == "func_4" and result == 120:
                print(f"  {name}: OK -> {result} (5! = 120)")
                passing += 1
            elif name == "func_5" and result == 10:
                print(f"  {name}: OK -> {result} (typo y -> x)")
                passing += 1
            else:
                print(f"  {name}: WRONG RESULT -> {result}")
        except Exception as e:
            print(f"  {name}: STILL RAISING -> {type(e).__name__}: {e}")

    print(f"\nFixes passing: {passing}/5")


if __name__ == "__main__":
    main()
