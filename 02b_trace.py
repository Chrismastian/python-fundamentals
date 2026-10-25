"""Tool: watch a loop run line by line (trace).

Why: when you cannot picture what a variable holds in the middle of a loop,
print the state on every iteration. This is the cheapest way to find a logic
bug, and it needs no debugger.

How to use:
  python 02b_trace.py
  then change DATA and the starting value yourself and experiment.
"""

# Data is deliberately different from drill 02 so it cannot leak answers.
DATA = [-7, -3, -11, -5]


def buggy_max(data):
    """WRONG version: the holder starts at an invented number (0)."""
    largest = 0
    for n in data:
        print(f"  n={n:>4}  largest now={largest:>4}  {n} > {largest}? {n > largest}")
        if n > largest:
            largest = n
    return largest


def correct_max(data):
    """RIGHT version: the holder starts empty (None), seeded from the data."""
    largest = None
    for n in data:
        is_empty = largest is None
        is_greater = (not is_empty) and n > largest
        print(f"  n={n:>4}  empty={is_empty!s:<5} greater={is_greater!s:<5} -> take={is_empty or is_greater}")
        if is_empty or n > largest:
            largest = n
    return largest


def main():
    print(f"DATA = {DATA}\n")

    print("WRONG VERSION (starts at 0):")
    wrong = buggy_max(DATA)
    print(f"  result = {wrong}\n")

    print("RIGHT VERSION (starts at None):")
    right = correct_max(DATA)
    print(f"  result = {right}\n")

    print(f"Expected: {max(DATA)}")
    assert right == max(DATA), "right version must match max()"
    assert wrong != max(DATA), "wrong version is expected to fail on this data"
    print("Checks pass: right version == max(), wrong version != max().")


if __name__ == "__main__":
    main()
