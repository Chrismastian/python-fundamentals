# Python Fundamentals — Prediction Drills

Self-scoring drills for Python fundamentals. The rule is always the same:
**write your answer down before you run the code.** A script that prints the
answer teaches you nothing; a script that scores your prediction tells you
exactly which concept is still missing.

Every drill ends with a score. Wrong answers are the useful output.

## How to use

```
python 01_mutability.py
```

1. Read each block. Do not run it first.
2. Fill in the `PREDICTION_n` strings at the bottom of the file.
3. Save, run the file, read the score.
4. For every wrong answer, go back to the mechanism — do not just read the
   real value and move on.

No dependencies, no framework, no install: standard library only.

## Drills

| File | What it drills | Scoring |
|---|---|---|
| `01_mutability.py` | names are labels, aliasing, mutable vs immutable, copy depth, default arguments | exact match, 9 blocks |
| `02_core_semantics.py` | float representation, `//` and `%`, truthiness, `and`/`or` returning operands, `for...else`, missing `return`, late binding in closures, wrong initial value | whitespace and quotes ignored, 10 blocks |
| `02b_trace.py` | printing state per loop iteration to find a logic bug (no debugger) | `assert` against `max()` |
| `03_write_your_own.py` | writing the loop yourself instead of predicting: max, word count, dedupe keeping order | 10 test cases |
| `04_traceback.py` | predicting the exception type and line from reading the code, then fixing each bug | 5 functions |

## Roadmap

`ROADMAP.md` is the checklist this repo is built against: 41 fundamental nodes,
each with one falsifiable pass criterion ("PASS IF ..."). A node is only ticked
after the evidence was produced here, never after merely reading about it.

## Honest scope

These are practice files, not a library. Nothing here is meant to be imported.
The value is in the drill format: predict, run, compare, fix the concept.
