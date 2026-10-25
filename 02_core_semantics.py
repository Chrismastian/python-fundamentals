"""Drill 02 - flow, types, and the traps you cannot see.

HOW TO USE (same as 01):
  1. Read every block TOGETHER WITH its explanatory comment. Do not run first.
  2. Fill in PREDICTION_1 .. PREDICTION_10 at the bottom.
  3. Save, then:  python 02_core_semantics.py
  4. Read the score.

The "# HOW IT WORKS:" comments explain the mechanism of each line, never the
result. Your job stays the same: derive the result from the mechanism.

Comparison is TOLERANT: spaces and quotes are ignored, so "abc", 'abc' and
abc all count as the same answer. Only the content is graded.

NOTE: these teaching comments are part of the drill on purpose - the point is
to learn to read a mechanism and predict its output, not to run and see.
"""


def block1():
    # HOW IT WORKS: 0.1 and 0.2 are stored in BINARY (base 2), and 0.1 cannot
    # be written exactly in base 2 - the same way 1/3 cannot be written out
    # exactly in base 10. So what gets added is not "the real" 0.1 but the
    # closest approximation of it.
    # Predict: is the result EXACTLY 0.3? How many digits after the decimal
    # point will repr() show?
    return 0.1 + 0.2


def block2():
    # HOW IT WORKS: three operators at once, the result is a 3-item tuple.
    #  //  = INTEGER division (rounds DOWN, not toward zero)
    #  %   = remainder
    #  Relationship: a == (a // b) * b + (a % b)
    # The trap: for NEGATIVE numbers, "down" and "toward zero" differ.
    # -7 // 2: rounding -3.5 down gives -4 (toward zero would give -3).
    # Then % must still satisfy the relationship above.
    return (7 // 2, 7 % 2, -7 // 2)


def block3():
    # HOW IT WORKS: bool() converts a value to True/False using "truthiness".
    # The rule: the falsy values are EMPTY or ZERO values
    # (0, 0.0, "", [], {}, None, False). Everything else is True.
    # Predict: the string "False" is a string of 5 letters - is it "empty"?
    # Compare it with bool("") and bool(0).
    return bool("False")


def block4():
    # HOW IT WORKS: `or` returns ONE OF THE OPERANDS, not True/False.
    # The rule: the left side is checked first. If it is truthy, it is
    # returned and the right side is NOT evaluated (short-circuit).
    # If the left side is falsy, the right side is returned.
    # Predict: is [] falsy or truthy? And what is returned - "x" (a string)
    # or True?
    return [] or "x"


def block5():
    # HOW IT WORKS: same as block4, but the left side is a NUMBER.
    # Predict: is 2 truthy? If so, which operand is returned - and is the
    # type int or bool?
    return 2 or 3


def block6():
    # HOW IT WORKS: `and` also returns an OPERAND, not True/False.
    # The rule: if the left side is falsy, the left side is returned and the
    # right side is NOT evaluated. If the left side is truthy, the right side
    # is returned.
    # Predict: 0 is falsy, so does 5 ever get looked at?
    return 0 and 5


def block7():
    # HOW IT WORKS: for ... else. The `else` block does NOT mean "when the if
    # condition is false". The else block runs ONLY if the loop finished all
    # its iterations without hitting `break`.
    # Here [1, 3, 5] is checked one by one; `break` only runs when an EVEN
    # number is found (n % 2 == 0).
    # Predict: is there an even number in [1, 3, 5]? If there is no break,
    # which part runs - and what does the result list contain?
    result = []
    for n in [1, 3, 5]:
        if n % 2 == 0:
            result.append("found")
            break
    else:
        result.append("not found")
    return result


def block8(x):
    # HOW IT WORKS: a function with an `if` and no `else`.
    # If the if condition is not met, the function runs to the end without
    # ever hitting a `return` - and in Python, a function that never returns
    # gives back a special value.
    # Predict: block8(2) - is 2 > 3 true or false? Then what does a function
    # return when it never reaches a return statement?
    if x > 3:
        return "big"


def block9():
    # HOW IT WORKS: this is about WHEN the variable inside a lambda is read.
    # The lambda does not store the VALUE of i at that moment; it stores a
    # REFERENCE to the variable i (the same variable, in the same scope).
    # The loop runs to completion first, and only afterwards are all the
    # lambdas called one by one in the list comprehension.
    # Predict: when the lambdas are CALLED, the loop is already finished - so
    # what is i at that point? All lambdas read the same i, so is the result
    # [0, 1, 2] or three identical values?
    makers = []
    for i in range(3):
        makers.append(lambda: i)
    return [f() for f in makers]


def block10():
    # HOW IT WORKS: the classic "find the LARGEST value" pattern with one
    # holder variable. The holder starts at 0, then each n is compared: if n
    # is GREATER than the holder, the holder becomes n. If not, it stays.
    # The trap: every number in this list is NEGATIVE and the holder starts
    # at 0.
    # Predict: is n, say -4, greater than 0? If nothing is ever greater than
    # 0, what does the holder end up holding? This is the "wrong initial
    # value" bug.
    largest = 0
    for n in [-4, -9, -2]:
        if n > largest:
            largest = n
    return largest


# ---- YOUR PREDICTIONS (fill in the 10 lines below) ----
# Write what print() would show for each block, e.g. "[1, 2]" or "None".
PREDICTION_1 = "0.30000000000000004"
PREDICTION_2 = "(3, 1, -4)"
PREDICTION_3 = "True"
PREDICTION_4 = "x"
PREDICTION_5 = "2"
PREDICTION_6 = "0"
PREDICTION_7 = "['not found']"
PREDICTION_8 = "None"
PREDICTION_9 = "[2, 2, 2]"
PREDICTION_10 = "0"


# ---- CHECKER (do not change) ----
def _norm(text):
    """Normalise: drop ALL spaces and quotes."""
    return "".join(text.split()).replace("'", "").replace('"', "")


def main():
    actual = [
        repr(block1()),
        repr(block2()),
        repr(block3()),
        repr(block4()),
        repr(block5()),
        repr(block6()),
        repr(block7()),
        repr(block8(2)),
        repr(block9()),
        repr(block10()),
    ]
    guesses = [
        PREDICTION_1, PREDICTION_2, PREDICTION_3, PREDICTION_4, PREDICTION_5,
        PREDICTION_6, PREDICTION_7, PREDICTION_8, PREDICTION_9, PREDICTION_10,
    ]

    blank = [i for i, g in enumerate(guesses, start=1) if not g.strip()]
    if blank:
        print(f"Not filled in yet: block {blank}.")
        return

    correct = 0
    for i, (guess, real) in enumerate(zip(guesses, actual), start=1):
        if _norm(guess) == _norm(real):
            correct += 1
            print(f"{i:2}. CORRECT -> {real}")
        else:
            print(f"{i:2}. WRONG   -> guess: {guess.strip()}")
            print(f"             real : {real}")

    print(f"\nScore: {correct}/10")


if __name__ == "__main__":
    main()
