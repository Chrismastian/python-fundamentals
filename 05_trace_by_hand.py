"""Drill 05 - trace by hand, then let Python grade the trace.

ROADMAP node 0.1 "A program is a sequence of instructions".
PASS IF: you can trace 10 lines of code on paper, write down the value of every
variable after every line, and match the real output.

HOW TO USE:
  1. Do NOT run this file yet. Read `target()` below.
  2. Fill in TRACE at the bottom: one row per EXECUTED line, in execution order.
     A row is (line number that just finished, {variable: value}).
     Write the state AFTER that line has run.
  3. Save, then:  python 05_trace_by_hand.py
  4. The checker replays target() under sys.settrace and compares your rows with
     what really happened. The first divergence is reported with detail.

Things that trip people up:
  - The loop body appears ONCE PER ITERATION: the same line number shows up
    several times, in order.
  - The `for` line itself executes once per iteration, before the body.
  - A line inside an `if` that is not taken is still executed (the condition
    line runs; the body line does not).
  - Only the variables in WATCH are compared. Other names are ignored.
  - Lines are counted from the top of this file, so the loop body's line
    numbers are the ones in `target()`, not 1, 2, 3.
"""

import sys
from itertools import zip_longest

NUMBERS = [4, 9]
WATCH = ("total", "largest")


def target(numbers):
    total = 0
    largest = None
    for n in numbers:
        total = total + n
        if largest is None or n > largest:
            largest = n
    doubled = total * 2
    return total, largest, doubled


# ---- YOUR TRACE (fill in) ----
# One row per executed line, in order: (line number, {variable: value}).
# Row shape, with made-up numbers just to show the format:
#   (100, {"total": 0, "largest": None}),
TRACE = [
]


# ---- CHECKER (do not change) ----
def snapshot(frame):
    """The watched variables, read from inside the running frame."""
    return {name: frame.f_locals.get(name) for name in WATCH}


def real_trace(fn, *args):
    """Replay fn under sys.settrace: rows of (line that just finished, state).

    sys.settrace hands us the frame every time Python is about to run a line.
    So when we arrive at the NEXT line, the variables already show the result of
    the previous one: that is exactly "the state after that line ran".
    """
    rows = []
    pending = None

    def local_tracer(frame, event, arg):
        nonlocal pending
        if event == "line":
            if pending is not None:
                rows.append((pending, snapshot(frame)))
            pending = frame.f_lineno
        elif event == "return":
            if pending is not None:
                rows.append((pending, snapshot(frame)))
            pending = None
        return local_tracer

    def global_tracer(frame, event, arg):
        if event == "call" and frame.f_code is fn.__code__:
            return local_tracer
        return None

    sys.settrace(global_tracer)
    try:
        fn(*args)
    finally:
        sys.settrace(None)
    return rows


def main():
    print(f"NUMBERS = {NUMBERS}   watching: {', '.join(WATCH)}\n")
    actual = real_trace(target, NUMBERS)

    if not TRACE:
        print("TRACE is empty. Trace it on paper first, then fill it in.")
        print(f"For reference: target() executes {len(actual)} lines.")
        return

    correct = 0
    first_bad = None
    for i, (mine, real) in enumerate(zip_longest(TRACE, actual), start=1):
        if mine == real:
            correct += 1
            print(f"{i:2}. OK      line {real[0]:<3} {real[1]}")
            continue
        first_bad = first_bad or i
        if mine is None:
            print(f"{i:2}. MISSING -> you stopped early; actual: line {real[0]} {real[1]}")
        elif real is None:
            print(f"{i:2}. EXTRA   -> you traced past the end: {mine}")
        else:
            print(f"{i:2}. WRONG")
            print(f"        you wrote: line {mine[0]} {mine[1]}")
            print(f"        actual   : line {real[0]} {real[1]}")

    print(f"\nScore: {correct}/{len(actual)} executed lines traced correctly")
    if first_bad:
        print(f"First divergence at row {first_bad}. Fix that row first: everything")
        print("after it is usually wrong for the same reason.")
        print("Tip: if the divergence is in a value, ask 'which line wrote that")
        print("variable last?' If it is a line number, you skipped or repeated a line.")


if __name__ == "__main__":
    main()