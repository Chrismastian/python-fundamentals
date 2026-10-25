"""Drill 03 - WRITING from scratch, not guessing.

Different from 01 and 02: there is no finished code to read here. You get
EMPTY functions and test cases. Your job is to fill the functions in.

HOW TO USE:
  1. Do not run this file yet. Read the three tasks below.
  2. Fill in the three functions. Ugly is fine, wrong is fine - it has to run.
  3. Save, then:  python 03_write_your_own.py
  4. Failing cases are listed. Fix them one by one until everything is OK.
  5. If you get stuck, do NOT ask an AI yet. Print the variables with print()
     inside the function, exactly as in 02b_trace.py.

RULE: do not use max(), min(), sum() or sorted() for tasks 1-3. The point is
to write the logic yourself. Once the tests pass, compare with the builtin.
"""


def task_1_max(numbers):
    """Return the LARGEST number in the list `numbers`.

    The data may be all negative, or empty.
    If the list is empty, return None (do not raise).

    Things to think about:
      - what should the holder variable start at? what is the holder for?
      - if the list is empty the loop never runs once, so what comes back?
    """

    if not numbers:
        return None
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def task_2_word_count(text):
    """Return a dict with the number of occurrences of each word.

    `text` is split on spaces. Example: "a b a" -> {"a": 2, "b": 1}

    Things to think about:
      - how do you add 1 to a value that ALREADY exists? `count[word] += 1`
        works only because the key is already there.
      - how do you handle a word that is NOT in the dict yet? Doing `+= 1`
        on a missing key raises KeyError, because there is no value to add to.
        The two usual fixes: an `if word in count:` branch, or
        `count[word] = count.get(word, 0) + 1`.
      - why is the check `word in count` O(1) here?
    """
    # 1. Prepare an empty dict to hold the counts
    count = {}

    # 2. Split the text into a list of words (use .split())
    words = text.split()

    # 3. Loop over every word
    for word in words:
        # FILL IN HERE: if the word is already in count, add 1
        if word in count:
            count[word] += 1
        #              if it is not there yet, start from 1
        else:
            count[word] = 1
        # Hint: count.get(word, 0) + 1 does both branches in one line

    # 4. Return the resulting dict
    return count


def task_3_dedupe(items):
    """Return a NEW list without duplicates, keeping the original order.

    [3, 1, 3, 2, 1] -> [3, 1, 2]

    Things to think about:
      - how do you know a value has been seen before? Seen-from-the-left is
        what keeps the original order: the first 3 is kept, the second 3 is
        dropped, so the result is not sorted just unique.
      - why is a list a bad choice for "have I seen this?" but a set a good
        one? (hint: lookup cost - list is O(n), set is O(1) on average)
    """
    # 1. Prepare a set to record what has been seen (O(1) lookup)
    seen = set()

    # 2. Prepare an empty list for the result
    result = []

    # 3. Loop over every item
    for item in items:
        # FILL IN HERE: if the item is NOT in `seen` yet,
        #               add it to `seen` AND to `result`
        # Hint: use 'if item not in seen:'
        if item not in seen:
            seen.add(item)
            result.append(item)

    # 4. Return the result
    return result


# ---------- CHECKER (do not change) ----------
FAILED = []


def check(name, got, expected):
    if got == expected:
        print(f"  OK    {name:<28} -> {got!r}")
    else:
        print(f"  FAIL  {name:<28} -> got {got!r}, expected {expected!r}")
        FAILED.append(name)


def main():
    print("Task 1 - find the largest")
    check("positive numbers", task_1_max([3, 9, 2]), 9)
    check("all negative", task_1_max([-4, -9, -2]), -2)
    check("single item", task_1_max([7]), 7)
    check("empty list", task_1_max([]), None)

    print("\nTask 2 - word count")
    check("repeated word", task_2_word_count("a b a"), {"a": 2, "b": 1})
    check("single word", task_2_word_count("hello"), {"hello": 1})
    check("empty text", task_2_word_count(""), {})

    print("\nTask 3 - remove duplicates")
    check("with duplicates", task_3_dedupe([3, 1, 3, 2, 1]), [3, 1, 2])
    check("no duplicates", task_3_dedupe([1, 2, 3]), [1, 2, 3])
    check("empty list", task_3_dedupe([]), [])

    print()
    if FAILED:
        print(f"Not passing yet: {len(FAILED)} cases. Fix those before moving on.")
    else:
        print("ALL PASSING. Only now are you allowed to bring in max()/set() and")
        print("compare: does your version produce the same thing?")


if __name__ == "__main__":
    main()
