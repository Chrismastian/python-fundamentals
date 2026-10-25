# Programming Fundamentals Map — the complete list, nothing left out

How to use it: every node has a **"PASS IF"** — one piece of evidence that
cannot be faked. A node may only be ticked once that evidence was produced by
hand, never because the code was "seen before".

Status: `[ ]` not checked yet · `[~]` being studied · `[x]` passed

---

## LAYER 0 — The machine under the code (5 nodes)

What actually happens while code runs. This is the root of nearly every bug
that feels "magical".

- [ ] **0.1 A program is a sequence of instructions**
  PASS IF: you can trace 10 lines of code on paper, write down the value of
  every variable after every line, and match the real output.

- [x] **0.2 A name is a label, not a box**
  PASSED 15 Nov: 9/9 concepts correct in `01_mutability.py` (7/9 on format, 2
  wrong only because of `repr()`). Can explain shallow copy: "only the
  outermost container is copied". Still to sharpen: state explicitly that the
  INNER objects are the same object, not just "the outer container".

- [x] **0.3 Mutable vs immutable**
  PASSED 15 Nov: `b = a[:]` vs `dict(a)` told apart correctly; `box=None`
  explained as "a new list per call because the default is evaluated once at
  def time".

- [x] **0.4 Types & representation**
  PASSED 24 Nov: knows `0.1 + 0.2` is not exactly 0.3; practical rule — never
  compare floats with `==`, use `abs(a - b) < 1e-9` or `decimal.Decimal`.

- [x] **0.5 Conversion & truthiness**
  PASSED 24 Nov: `bool("False")` -> True, `[] or "x"` -> 'x', `0 and 5` -> 0.

- [x] **1.2 Loops: `for` vs `while`**
  PASSED 24 Nov: wrote `for` loops from scratch in tasks 1-3, chose the right
  one.

- [x] **1.3 Recurring loop patterns**
  PASSED 24 Nov: wrote from scratch without googling: counter/accumulator
  (task 1), filter + build result (tasks 2, 3).

- [x] **2.1 Functions: parameters, arguments, `return`**
  PASSED 24 Nov: three functions with `return` in the right place (not at the
  top), parameters used correctly.

- [x] **2.4 Data structures: which one**
  PASSED 24 Nov: chose `list`/`dict`/`set` by operation cost: dict for counting
  (O(1) key access), set for membership tests (O(1) vs O(n) for list).

- [x] **2.5 `dict` keys & hashability**
  PASSED 24 Nov: strings as dict keys, a set holding hashable values.

- [x] **3.5 Errors you cannot see**
  PASSED 24 Nov: found the `largest = 0` bug when the data was negative — the
  code runs, raises nothing, and is silently wrong. Fixed by seeding the holder
  from the data.

- [x] **4.4 Parsing text into structures**
  PASSED 24 Nov: `text.split()` -> list -> counting dict.

- [x] **6.1 Basic complexity**
  PASSED 24 Nov: aware that `item in list` is O(n) and `item in set` is O(1),
  chose the set for task 3.

---

## LAYER 1 — Control flow (5 nodes)

- [ ] **1.1 Conditions & boolean logic**
  PASS IF: you can explain that `and`/`or` return a VALUE and not `True`/
  `False` (`2 or 3` -> `2`), and what short-circuit means: the left side is
  evaluated first, and if the answer is already decided the right side is never
  evaluated at all.

- [ ] **1.2 Loops: `for` vs `while`**
  PASS IF: you can pick the right one for 3 cases (iterating a collection,
  repeating until a condition, repeating forever with `break`) and say when
  `while` turns into an infinite loop.

- [ ] **1.3 Recurring loop patterns**
  PASS IF: you can write from scratch without googling: counting, summing
  (accumulator), maximum, filtering, and "find the first match".

- [ ] **1.4 Boundaries & off-by-one**
  PASS IF: you can explain why `range(5)` stops at 4, and `range(len(x))` vs
  `enumerate(x)`.

- [ ] **1.5 `break` / `continue` / loop `else`**
  PASS IF: you can explain what `for...else` does and write one real case where
  it beats a boolean flag.

---

## LAYER 2 — Functions & data (6 nodes)

- [ ] **2.1 Functions: parameters, arguments, `return`**
  PASS IF: you can explain `print` vs `return` with one example where `print`
  causes a bug, and why a function without `return` gives back `None`.

- [ ] **2.2 Scope & lifetime**
  PASS IF: you can explain why a variable inside a function is invisible
  outside, why `global` is almost always wrong, and what a closure is (one
  example: a function that "remembers" a value).

- [ ] **2.3 The default-argument trap**
  PASS IF: you can explain why `def f(x, box=[])` is dangerous and write the
  fix (`box=None` then `if box is None: box = []`).

- [ ] **2.4 Data structures: which one**
  PASS IF: given 5 cases, you pick `list`/`dict`/`set`/`tuple` by operation
  cost rather than taste. You must be able to say: lookup in a `list` is O(n),
  in a `dict`/`set` O(1) on average.

- [ ] **2.5 `dict` keys & hashability**
  PASS IF: you can explain why `[1,2]` cannot be a dict key but `(1,2)` can,
  and why a set can remove duplicates fast.

- [ ] **2.6 Sorting & `key`**
  PASS IF: you can sort a list of dicts by two columns (first key, then
  second) and explain why `sort()` mutates the list while `sorted()` does not,
  and that both return `None`.

---

## LAYER 3 — Errors & debugging (5 nodes)

This is the layer that decides whether you are independent or always asking an
AI.

- [ ] **3.1 Reading a traceback**
  PASS IF: given a 6-line traceback, you can point at (a) your offending line,
  (b) the error type, (c) the value that caused the failure — within 30
  seconds.

- [ ] **3.2 Exceptions: `try`/`except`/`finally`/`raise`**
  PASS IF: you can explain why `except Exception: pass` is dangerous, the
  hierarchy (`KeyError` -> `LookupError` -> `Exception`), and when NOT to use
  `try` at all.

- [ ] **3.3 Debugging: hypothesis, then proof**
  PASS IF: you have a written record of one real bug where you stated a guess
  first and then proved it with a single command/output — instead of changing
  code at random until it worked.

- [ ] **3.4 `assert` & basic tests**
  PASS IF: you can write 3 `assert`s that really fail when the logic is broken
  (not asserts that always pass).

- [ ] **3.5 Errors you cannot see**
  PASS IF: you can name 3 bugs that raise no error at all (silently wrong
  results) and how to detect them.

---

## LAYER 4 — Data & files (4 nodes)

- [ ] **4.1 Text & encoding**
  PASS IF: you can explain why `open()` needs `encoding="utf-8"`, and why
  `len("é")` can be 1 or 2 depending on normalisation.

- [ ] **4.2 File I/O**
  PASS IF: you can read and write files with `with`, and explain why `with` is
  mandatory (the file is closed even when an error happens).

- [ ] **4.3 JSON & serialisation**
  PASS IF: you can explain why `json.dumps` exists (data in memory vs text),
  and why a `datetime` cannot be dumped directly.

- [ ] **4.4 Parsing text into structures**
  PASS IF: given CSV text or `key=value` lines, you can turn it into
  `list[dict]` and survive broken lines without crashing.

---

## LAYER 5 — Abstraction (4 nodes)

- [ ] **5.1 Classes: `__init__`, `self`, attributes**
  PASS IF: you can explain `self` in one correct sentence (not "it must be
  written"), and the difference between an instance attribute and a local
  variable.

- [ ] **5.2 Composition vs inheritance**
  PASS IF: you can explain why "has a" (`composition`) is more often right
  than "is a" (`inheritance`), with one example of inheritance used wrongly.

- [ ] **5.3 Modules, packages, `import`**
  PASS IF: you can create 2 files where one imports the other, and explain why
  a top-level import runs that file, plus what `if __name__ == "__main__":`
  is for.

- [ ] **5.4 Interface boundaries (duck typing)**
  PASS IF: you can explain why a function accepting "anything with `.read()`"
  is more flexible than one demanding a specific type.

---

## LAYER 6 — Scale (4 nodes)

- [ ] **6.1 Basic complexity**
  PASS IF: you can guess the cost (`n`, `n log n`, `n2`) from the shape of the
  code before running it, and prove it by timing n=1,000 vs n=10,000.

- [ ] **6.2 Recursion**
  PASS IF: you can write one recursive function with a correct base case, and
  explain what happens without one (RecursionError).

- [ ] **6.3 Generators / lazy iteration**
  PASS IF: you can explain why `range(10**9)` costs no memory but
  `list(range(10**9))` dies, and write one generator yourself (`yield`).

- [ ] **6.4 Basic concurrency**
  PASS IF: you can explain the difference between threads and async in one
  sentence about who waits, and when concurrency does NOT help (CPU work).

---

## LAYER 7 — Working tools (4 nodes)

- [ ] **7.1 Git mental model**
  PASS IF: you can explain a commit as a snapshot and a branch as a pointer,
  then use `status`/`diff`/`log` to know the state of a repo without guessing.

- [ ] **7.2 Terminal**
  PASS IF: you can change directory, create a file and view its contents
  without a GUI (and know the PowerShell vs Linux differences for the same
  command).

- [ ] **7.3 Environments & dependencies**
  PASS IF: you can explain why virtualenv exists, and what happens when two
  projects need different versions of a package.

- [ ] **7.4 Reading documentation**
  PASS IF: you can find a function signature in the official docs and use one
  optional parameter you have never used before, with no AI example.

---

## LAYER 8 — Ways of thinking (4 nodes)

This is what separates "can write code" from "can solve problems".

- [ ] **8.1 Decomposition**
  PASS IF: given a new problem, you can split it into 4-7 functions with one
  responsibility each, before writing any code.

- [ ] **8.2 Design the data first**
  PASS IF: you can explain why the shape of the data (list of dict vs dict of
  dict) decides how easy the algorithm is, with one example where changing the
  data shape removed a nested loop.

- [ ] **8.3 Pseudocode & edge cases**
  PASS IF: before coding, you can write pseudocode plus the list of odd cases
  (empty, single item, duplicates, very large, bad input).

- [ ] **8.4 Reading someone else's code**
  PASS IF: given an 80-line file you have never seen, you can explain its flow
  in 5 minutes without running it.

---

## Coverage summary

| Layer | Nodes | Content |
|---|---|---|
| 0 | 5 | the machine: names, types, mutability, conversion |
| 1 | 5 | control: conditions, loops, loop patterns, off-by-one |
| 2 | 6 | functions, scope, data structures, sorting |
| 3 | 5 | errors, traceback, debugging, assert |
| 4 | 4 | files, encoding, JSON, parsing |
| 5 | 4 | classes, composition, modules, duck typing |
| 6 | 4 | complexity, recursion, generators, concurrency |
| 7 | 4 | git, terminal, venv, documentation |
| 8 | 4 | decomposition, data design, pseudocode, reading code |
| **Total** | **41** | |

Order of work: **0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> 7**.
Layer 7 (tools) is deliberately last as a formality, since those are used
daily anyway. Layer 3 comes before 4 because debugging is the tool used by
every layer after it.

One node = one short session. 41 nodes at 2 hours a day is realistically 6-8
weeks if passing nodes are skipped and only the failures are dissected.
