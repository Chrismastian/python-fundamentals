"""
Gate for ROADMAP.md: the map is only useful if its count can be trusted.

Checks, in order of how likely they are to rot:
  1. 41 node IDs, no duplicates. (The original hand-written map listed 1.2,
     1.3, 2.1, 2.4, 2.5, 3.5, 4.4 and 6.1 TWICE - once inside LAYER 0 by
     accident. 48 bullet lines, 41 real nodes, and the summary table still said
     41. Nobody noticed for weeks.)
  2. Every ticked node carries a "PASSED" evidence line. A tick with no
     evidence is the one thing this file is supposed to prevent.
  3. The table's per-layer counts match the map, and the totals match 41.
  4. The headline "Progress: X / 41" matches the real number of ticks.

Run:  python tests/test_roadmap.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROADMAP = ROOT / "ROADMAP.md"

NODE = re.compile(r"^- \[(?P<mark>[ x~])\] \*\*(?P<id>\d+\.\d+) (?P<title>[^*]+)\*\*")
TABLE_ROW = re.compile(r"^\| (?P<layer>\d) \| (?P<nodes>\d+) \| \*{0,2}(?P<passed>\d+)\*{0,2} \|")
PROGRESS = re.compile(r"\*\*Progress: (\d+) / 41\*\*")
TOTAL_ROW = re.compile(r"^\| \*\*Total\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \|")

EXPECTED_TOTAL = 41
EXPECTED_PER_LAYER = {0: 5, 1: 5, 2: 6, 3: 5, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4}


def parse(text):
    """Return (nodes, table, progress) parsed straight out of the markdown."""
    nodes = {}
    table = {}
    progress = None
    current = None
    for line in text.splitlines():
        match = NODE.match(line)
        if match:
            current = match["id"]
            nodes[current] = {"mark": match["mark"], "title": match["title"].strip(), "body": []}
            continue
        if line.startswith("- ["):
            current = None  # a new bullet that is not a node ends the node body
            continue
        if current is not None:
            nodes[current]["body"].append(line)
        row = TABLE_ROW.match(line)
        if row:
            table[int(row["layer"])] = (int(row["nodes"]), int(row["passed"]))
        total = TOTAL_ROW.match(line)
        if total:
            table["total"] = (int(total[1]), int(total[2]))
        found = PROGRESS.search(line)
        if found:
            progress = int(found[1])
    return nodes, table, progress


def check():
    failures = []
    nodes, table, progress = parse(ROADMAP.read_text(encoding="utf-8"))

    # 1. count + duplicates
    if len(nodes) != EXPECTED_TOTAL:
        failures.append(f"expected {EXPECTED_TOTAL} unique node IDs, found {len(nodes)}")
    duplicated = {}
    for node_id in re.findall(r"^- \[[ x~]\] \*\*(\d+\.\d+)", ROADMAP.read_text(encoding="utf-8"), re.M):
        duplicated[node_id] = duplicated.get(node_id, 0) + 1
    for node_id, count in duplicated.items():
        if count > 1:
            failures.append(f"node {node_id} appears {count} times")

    # 2. a tick needs evidence
    for node_id, node in nodes.items():
        if node["mark"] == "x":
            body = " ".join(node["body"])
            if "PASSED" not in body:
                failures.append(f"node {node_id} is ticked but has no PASSED evidence line")

    # 3. per-layer counts and totals agree
    passed_total = sum(1 for n in nodes.values() if n["mark"] == "x")
    for layer, expected in EXPECTED_PER_LAYER.items():
        if layer not in table:
            failures.append(f"table is missing layer {layer}")
            continue
        count, passed = table[layer]
        real = sum(1 for node_id, n in nodes.items() if int(node_id.split(".")[0]) == layer)
        real_passed = sum(1 for node_id, n in nodes.items()
                          if int(node_id.split(".")[0]) == layer and n["mark"] == "x")
        if count != real:
            failures.append(f"layer {layer}: table says {count} nodes, map has {real}")
        if count != expected:
            failures.append(f"layer {layer}: expected {expected} nodes, table says {count}")
        if passed != real_passed:
            failures.append(f"layer {layer}: table says {passed} passed, map has {real_passed}")
    if "total" not in table:
        failures.append("table is missing the Total row")
    else:
        total_nodes, total_passed = table["total"]
        if total_nodes != EXPECTED_TOTAL:
            failures.append(f"Total row says {total_nodes} nodes, expected {EXPECTED_TOTAL}")
        if total_passed != passed_total:
            failures.append(f"Total row says {total_passed} passed, map has {passed_total}")

    # 4. the headline number
    if progress is None:
        failures.append('the "Progress: X / 41" line is missing')
    elif progress != passed_total:
        failures.append(f'headline says {progress}/41, map has {passed_total} ticks')

    return nodes, passed_total, failures


def main():
    nodes, passed_total, failures = check()
    print(f"{len(nodes)} unique nodes, {passed_total} ticked")
    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for failure in failures:
            print(f"  - {failure}")
        sys.exit(1)
    print("ROADMAP.md is consistent.")


if __name__ == "__main__":
    main()
