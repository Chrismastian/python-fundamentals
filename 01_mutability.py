"""Drill 01 - mutability & aliasing.

HOW TO USE:
  1. Read every block. Do NOT run this file yet.
  2. Replace PREDICTION_n = "" with your guess, written as the exact string
     print() would show.
  3. Save, then run:  python 01_mutability.py
  4. The score prints at the bottom. Every wrong answer is a concept hole:
     go back to the mechanism, not just to the real value.

Values are compared as-is, so write them exactly.
Format examples: "5", "None", "[1, 2, 3]", "('a', 1)"
"""


def block1():
    a = [1, 2, 3]
    b = a
    b.append(4)
    return a


def block2():
    a = [[1, 2], [3, 4]]
    b = a.copy()
    b[0].append(9)
    return a


def block3(item, box=[]):
    box.append(item)
    return box


def block4():
    t = ([1], 2)
    t[0].append(3)
    return t


def block5():
    s = "abc"
    s.upper()
    return s


def block6():
    nums = [3, 1, 2]
    result = nums.sort()
    return f"{result} {nums}"


def block7(x):
    x = x + [99]
    return x


def block8():
    a = {"k": [1]}
    b = dict(a)
    b["k"].append(2)
    return a


def block9():
    a = [1, 2, 3]
    b = a[:]
    b.append(4)
    return a


# ---- YOUR PREDICTIONS (fill in the 9 lines below) ----
PREDICTION_1 = "[1, 2, 3, 4]"
PREDICTION_2 = "[[1, 2, 9], [3, 4]]"
PREDICTION_3 = "block3(1)->[1] / block3(2)->[1, 2]"
PREDICTION_4 = "([1, 3], 2)"
PREDICTION_5 = "abc"
PREDICTION_6 = "None [1, 2, 3]"
PREDICTION_7 = "[1, 99]"
PREDICTION_8 = "{'k': [1, 2]}"
PREDICTION_9 = "[1, 2, 3]"


# ---- CHECKER (do not change) ----
def main():
    actual = [
        repr(block1()),
        repr(block2()),
        repr(block3(1)) + " / " + repr(block3(2)),
        repr(block4()),
        repr(block5()),
        block6(),
        repr(block7([1])),
        repr(block8()),
        repr(block9()),
    ]
    guesses = [
        PREDICTION_1, PREDICTION_2, PREDICTION_3,
        PREDICTION_4, PREDICTION_5, PREDICTION_6,
        PREDICTION_7, PREDICTION_8, PREDICTION_9,
    ]

    blank = [i for i, g in enumerate(guesses, start=1) if not g.strip()]
    if blank:
        print(f"Not filled in yet: block {blank}.")
        print("Fill in every prediction first, then run again. Answers are not")
        print("leaked before you guess.")
        return

    correct = 0
    for i, (guess, real) in enumerate(zip(guesses, actual), start=1):
        if guess.strip() == real:
            correct += 1
            print(f"{i}. CORRECT -> {real}")
        else:
            print(f"{i}. WRONG   -> guess: {guess.strip()}")
            print(f"             real : {real}")

    print(f"\nScore: {correct}/9")


if __name__ == "__main__":
    main()
