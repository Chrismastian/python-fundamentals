"""
CI for a drill repository: run every drill file and fail if any of them stops
working. The drills are scripts with their own built-in checkers, so a plain
run of each file is the test: a crash, a non-zero exit code, or an assertion
failure breaks the build.

The scoring output is meant to be low (predictions are guesses, and a wrong
guess is data) - what must never happen is a drill file failing to run.
"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRILL = re.compile(r"^\d+[a-z]?_.*\.py$")

drills = sorted(p for p in ROOT.glob("*.py") if DRILL.match(p.name))

if not drills:
    print("No drill files found - the glob is wrong, not the drills.")
    sys.exit(1)

failed = []
for path in drills:
    print(f"--- {path.name} ---")
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
    if result.returncode != 0:
        failed.append(path.name)

print(f"\nRan {len(drills)} drill files, {len(failed)} failed.")
if failed:
    print("Failed:", ", ".join(failed))
    sys.exit(1)
print("All drills run cleanly.")
