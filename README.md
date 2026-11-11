# Python Fundamentals — Prediction Drills

[![CI](https://github.com/Chrismastian/python-fundamentals/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-fundamentals/actions/workflows/ci.yml)

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
| `05_trace_by_hand.py` | tracing a function by hand: what each watched variable holds after every executed line | row-by-row compare against the real trace (`sys.settrace`), 13 rows |
| `06_boolean_logic.py` | `and`/`or` return an operand, short-circuit proven by a call log, plus writing "first truthy" by hand | 12 predictions + 5 written-loop cases |
| `07_boundaries.py` | half-open `range`/slice rule: where a loop stops, negative steps, `range(len(x))` vs `enumerate(x, start=1)` | 10 predictions + 6 written-loop cases |

## Roadmap

`ROADMAP.md` is the checklist this repo is built against: 41 fundamental nodes,
each with one falsifiable pass criterion ("PASS IF ..."). A node is only ticked
after the evidence was produced here, never after merely reading about it.
Every ticked node carries a `PASSED` line, and a `Drill:` pointer to the file
where that evidence was produced.

Progress is a real number, not a vibe: **12 / 41**. `tests/test_roadmap.py`
fails the build if the count, the duplicates, or an evidence-free tick ever
drifts.

## Checks

```
python tests/test_roadmap.py     # 41 unique nodes, no evidence-free tick, counts match
python tests/test_drills_run.py  # every drill file runs; a crash fails the build
```

Both run in CI on every push. The drills' own scores are allowed to be low —
a wrong prediction is the point — but a drill that stops running is a bug.

## Honest scope

These are practice files, not a library. Nothing here is meant to be imported.
The value is in the drill format: predict, run, compare, fix the concept.

The drills are written by an AI; the answers are supposed to be filled in by a
human. Until the `PREDICTION_n` lines are filled in and the `PART C` functions
are written, a drill file is a lesson, not evidence. That is why the roadmap
only ticks a node when its `PASSED` line says what was actually done.
