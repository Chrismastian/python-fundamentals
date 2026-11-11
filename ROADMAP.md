# Programming Fundamentals Map — 41 nodes, nothing left out

How to use it: every node has a **"PASS IF"** — one piece of evidence that
cannot be faked. A node may only be ticked once that evidence was produced by
hand, never because the code was "seen before".

Status: `[ ]` not checked yet · `[~]` being studied · `[x]` passed

**Progress: 12 / 41**

`PASSED` notes record the evidence, not the intention. `Drill:` points at the
file in this repo where that evidence gets produced.

---

## LAYER 0 — The machine under the code (5 nodes)

What actually happens while code runs. This is the root of nearly every bug
that feels "magical".

- [ ] **0.1 A program is a sequence of instructions**
  PASS IF: you can trace 10 lines of code on paper, write down the value of
  every variable after every line, and match the real output.
  Drill: `05_trace_by_hand.py`

- [x] **0.2 A name is a label, not a box**
  PASSED: 9/9 concepts correct in `01_mutability.py` (7/9 on exact format, the
  2 misses were `repr()` quoting, not the concept).
  Can explain shallow copy: "only the outermost container is copied".
  Still to sharpen: say explicitly that the INNER objects are the same object,
  not just "the outer container".
  Drill: `01_mutability.py`

- [x] **0.3 Mutable vs immutable**
  PASSED: `b = a[:]` vs `dict(a)` told apart correctly; `box=None` explained as
  "a new list per call, because the default is evaluated once at def time".
  Drill: `01_mutability.py` blocks 2, 3, 8, 9

- [x] **0.4 Types & representation**
  PASSED: knows `0.1 + 0.2` is not exactly 0.3, and the practical rule — never
  compare floats with `==`, use `abs(a - b) < 1e-9` or `decimal.Decimal`.
  Drill: `02_core_semantics.py` block 1

- [x] **0.5 Conversion & truthiness**
  PASSED: `bool("False")` -> True, `[] or "x"` -> `'x'`, `0 and 5` -> 0.
  Drill: `02_core_semantics.py` blocks 3-6

---

## LAYER 1 — Control flow (5 nodes)

- [ ] **1.1 Conditions & boolean logic**
  PASS IF: you can explain that `and`/`or` return a VALUE and not `True`/
  `False` (`2 or 3` -> `2`), and what short-circuit means: the left side is
  evaluated first, and if the answer is already decided the right side is never
  evaluated at all.
  Drill: `06_boolean_logic.py`

- [x] **1.2 Loops: `for` vs `while`**
  PASSED: wrote `for` loops from scratch in all three tasks and picked `for`
  over `while` for a known collection each time.
  Drill: `03_write_your_own.py`

- [x] **1.3 Recurring loop patterns**
  PASSED: wrote from scratch without googling: counter/accumulator (task 1),
  filter + build result (tasks 2 and 3).
  Drill: `03_write_your_own.py`

- [ ] **1.4 Boundaries & off-by-one**
  PASS IF: you can explain why `range(5)` stops at 4, and `range(len(x))` vs
  `enumerate(x)`.
  Drill: `07_boundaries.py`

- [ ] **1.5 `break` / `continue` / loop `else`**
  PASS IF: you can explain what `for...else` does and write one real case where
  it beats a boolean flag.
  Drill: `02_core_semantics.py` block 7

---

## LAYER 2 — Functions & data (6 nodes)

- [x] **2.1 Functions: parameters, arguments, `return`**
  PASSED: three functions written with `return` in the right place (not at the
  top) and parameters used correctly.
  Still to prove: the `print` vs `return` explanation, and why a function
  without `return` gives back `None`.
  Drill: `03_write_your_own.py`

- [ ] **2.2 Scope & lifetime**
  PASS IF: you can explain why a variable inside a function is invisible
  outside, why `global` is almost always wrong, and what a closure is (one
  example: a function that "remembers" a value).
  Drill: `02_core_semantics.py` block 9 (late binding is the visible symptom)

- [ ] **2.3 The default-argument trap**
  PASS IF: you can explain why `def f(x, box=[])` is dangerous and write the
  fix (`box=None` then `if box is None: box = []`).
  Drill: `01_mutability.py` block 3

- [x] **2.4 Data structures: which one**
  PASSED: chose `list`/`dict`/`set` by operation cost — dict for counting
  (O(1) key access), set for membership tests (O(1) vs O(n) for list).
  Drill: `03_write_your_own.py` tasks 2-3

- [x] **2.5 `dict` keys & hashability**
  PASSED: strings as dict keys, a set holding hashable values, and picking a
  set because of lookup cost.
  Drill: `03_write_your_own.py` task 3

- [ ] **2.6 Sorting & `key`**
  PASS IF: you can sort a list of dicts by two columns (first key, then
  second) and explain why `sort()` mutates the list while `sorted()` does not,
  and that both return `None`.
  Drill: not written yet (candidate for drill 08)

---

## LAYER 3 — Errors & debugging (5 nodes)

This is the layer that decides whether you are independent or always asking an
AI.

- [ ] **3.1 Reading a traceback**
  PASS IF: given a 6-line traceback, you can point at (a) your offending line,
  (b) the error type, (c) the value that caused the failure — within 30
  seconds.
  Drill: `04_traceback.py`

- [ ] **3.2 Exceptions: `try`/`except`/`finally`/`raise`**
  PASS IF: you can explain why `except Exception: pass` is dangerous, the
  hierarchy (`KeyError` -> `LookupError` -> `Exception`), and when NOT to use
  `try` at all.
  Drill: not written yet (candidate for drill 08)

- [ ] **3.3 Debugging: hypothesis, then proof**
  PASS IF: you have a written record of one real bug where you stated a guess
  first and then proved it with a single command/output — instead of changing
  code at random until it worked.
  Drill: `02b_trace.py` (print the state, do not guess it)

- [ ] **3.4 `assert` & basic tests**
  PASS IF: you can write 3 `assert`s that really fail when the logic is broken
  (not asserts that always pass).
  Drill: `02b_trace.py` (read the two asserts, then break one on purpose)

- [x] **3.5 Errors you cannot see**
  PASSED: found the `largest = 0` bug when the data was negative — the code
  runs, raises nothing, and is silently wrong. Fixed by seeding the holder from
  the data.
  Still to prove: name 3 such bugs, not 1.
  Drill: `02b_trace.py`, `02_core_semantics.py` block 10

---

## LAYER 4 — Data & files (4 nodes)

- [ ] **4.1 Text & encoding**
  PASS IF: you can explain why `open()` needs `encoding="utf-8"`, and why
  `len("é")` can be 1 or 2 depending on normalisation.
  Drill: not written yet

- [ ] **4.2 File I/O**
  PASS IF: you can read and write files with `with`, and explain why `with` is
  mandatory (the file is closed even when an error happens).
  Drill: not written yet

- [ ] **4.3 JSON & serialisation**
  PASS IF: you can explain why `json.dumps` exists (data in memory vs text),
  and why a `datetime` cannot be dumped directly.
  Drill: not written yet

- [x] **4.4 Parsing text into structures**
  PASSED: `text.split()` -> list -> counting dict, from scratch.
  Still to prove: broken input handled without crashing.
  Drill: `03_write_your_own.py` task 2

---

## LAYER 5 — Abstraction (4 nodes)

- [ ] **5.1 Classes: `__init__`, `self`, attributes**
  PASS IF: you can explain `self` in one correct sentence (not "it must be
  written"), and the difference between an instance attribute and a local
  variable.
  Drill: not written yet

- [ ] **5.2 Composition vs inheritance**
  PASS IF: you can explain why "has a" (`composition`) is more often right
  than "is a" (`inheritance`), with one example of inheritance used wrongly.
  Drill: not written yet

- [ ] **5.3 Modules, packages, `import`**
  PASS IF: you can create 2 files where one imports the other, and explain why
  a top-level import runs that file, plus what `if __name__ == "__main__":`
  is for.
  Drill: every drill in this repo uses `if __name__ == "__main__":` — the
  proof is writing one from an empty file, not reading this line.

- [ ] **5.4 Interface boundaries (duck typing)**
  PASS IF: you can explain why a function accepting "anything with `.read()`"
  is more flexible than one demanding a specific type.
  Drill: not written yet

---

## LAYER 6 — Scale (4 nodes)

- [x] **6.1 Basic complexity**
  PASSED: aware that `item in list` is O(n) and `item in set` is O(1), and
  chose the set for the dedupe task.
  Still to prove: guessing the cost from the shape of the code, and measuring
  n=1,000 vs n=10,000.
  Drill: `03_write_your_own.py` task 3

- [ ] **6.2 Recursion**
  PASS IF: you can write one recursive function with a correct base case, and
  explain what happens without one (RecursionError).
  Drill: `04_traceback.py` func_4

- [ ] **6.3 Generators / lazy iteration**
  PASS IF: you can explain why `range(10**9)` costs no memory but
  `list(range(10**9))` dies, and write one generator yourself (`yield`).
  Drill: not written yet

- [ ] **6.4 Basic concurrency**
  PASS IF: you can explain the difference between threads and async in one
  sentence about who waits, and when concurrency does NOT help (CPU work).
  Drill: not written yet

---

## LAYER 7 — Working tools (4 nodes)

- [ ] **7.1 Git mental model**
  PASS IF: you can explain a commit as a snapshot and a branch as a pointer,
  then use `status`/`diff`/`log` to know the state of a repo without guessing.
  Drill: this repo's own history

- [ ] **7.2 Terminal**
  PASS IF: you can change directory, create a file and view its contents
  without a GUI (and know the PowerShell vs Linux differences for the same
  command).
  Drill: this repo's own workflow

- [ ] **7.3 Environments & dependencies**
  PASS IF: you can explain why virtualenv exists, and what happens when two
  projects need different versions of a package.
  Drill: not written yet

- [ ] **7.4 Reading documentation**
  PASS IF: you can find a function signature in the official docs and use one
  optional parameter you have never used before, with no AI example.
  Drill: `07_boundaries.py` (`enumerate(..., start=1)` is exactly such a
  parameter)

---

## LAYER 8 — Ways of thinking (4 nodes)

This is what separates "can write code" from "can solve problems".

- [ ] **8.1 Decomposition**
  PASS IF: given a new problem, you can split it into 4-7 functions with one
  responsibility each, before writing any code.
  Drill: not written yet

- [ ] **8.2 Design the data first**
  PASS IF: you can explain why the shape of the data (list of dict vs dict of
  dict) decides how easy the algorithm is, with one example where changing the
  data shape removed a nested loop.
  Drill: not written yet

- [ ] **8.3 Pseudocode & edge cases**
  PASS IF: before coding, you can write pseudocode plus the list of odd cases
  (empty, single item, duplicates, very large, bad input).
  Drill: every `PART C` in drills 06 and 07 already lists the odd cases; the
  proof is writing them yourself first.

- [ ] **8.4 Reading someone else's code**
  PASS IF: given an 80-line file you have never seen, you can explain its flow
  in 5 minutes without running it.
  Drill: `05_trace_by_hand.py`, `04_traceback.py`

---

## Coverage summary

| Layer | Nodes | Passed | Content |
|---|---|---|---|
| 0 | 5 | 4 | the machine: names, types, mutability, conversion |
| 1 | 5 | 2 | control: conditions, loops, loop patterns, off-by-one |
| 2 | 6 | 3 | functions, scope, data structures, sorting |
| 3 | 5 | 1 | errors, traceback, debugging, assert |
| 4 | 4 | 1 | files, encoding, JSON, parsing |
| 5 | 4 | 0 | classes, composition, modules, duck typing |
| 6 | 4 | 1 | complexity, recursion, generators, concurrency |
| 7 | 4 | 0 | git, terminal, venv, documentation |
| 8 | 4 | 0 | decomposition, data design, pseudocode, reading code |
| **Total** | **41** | **12** | |

Order of work: **0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> 7**.
Layer 7 (tools) is deliberately last as a formality, since those are used
daily anyway. Layer 3 comes before 4 because debugging is the tool used by
every layer after it.

One node = one short session. 41 nodes at 2 hours a day is realistically 6-8
weeks if passing nodes are skipped and only the failures are dissected.

A ticked node without a `PASSED` line is a lie; `tests/test_roadmap.py` fails
the build if a node ID repeats or the count drifts from 41.
