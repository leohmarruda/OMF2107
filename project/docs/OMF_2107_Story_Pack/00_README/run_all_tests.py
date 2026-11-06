#!/usr/bin/env python3
"""Reproduce the number of discovered OMF 2107 test cases per folder.

Usage: python 00_README/run_all_tests.py
Requires `pytest` (third-party; see note below). No network use.

v5.3 fix: the previous version of this runner used
`python -m unittest discover` per folder. `unittest discover` only
collects `unittest.TestCase` subclasses, so it silently collects ZERO
tests (and exits 0 / "OK") from any file written in bare pytest idiom
(plain functions, `@pytest.mark.parametrize`). That is exactly the
shape of `19_Kreissack_Arc/test_pov_integration_v19.py`, whose 27 test
cases -- covering the six-POV Kreissack finale integration -- were
never actually executed by any "official" run of this script, even
though two README files describe that file as actively enforcing
finale integration. `pytest` collects both `unittest.TestCase` classes
and bare pytest-style tests, so switching the runner to `pytest`
recovers those 27 tests with no changes to any test file, and removes
the main source of false confidence in previously reported counts
(e.g. "394 methods" / "276 methods" in older audit docs never included
them). If `pytest` is not installed in your environment, install it
(`pip install pytest`) rather than reverting to `unittest discover`.
"""
from pathlib import Path
import subprocess
import sys
import re

root = Path(__file__).resolve().parents[1]
folders = sorted({p.parent for p in root.rglob('test_*.py')})
total = 0
failures = []
for folder in folders:
    args = [sys.executable, '-m', 'pytest', str(folder), '-q']
    outcome = subprocess.run(args, cwd=root, text=True, capture_output=True)
    combined = outcome.stdout + '\n' + outcome.stderr
    # pytest's short summary line looks like "12 passed, 3 subtests passed in 0.04s"
    passed = sum(int(m) for m in re.findall(r'(\d+) passed', combined))
    n = passed
    total += n
    print(f'{folder.relative_to(root)}: {n} tests; {"PASS" if outcome.returncode == 0 else "FAIL"}')
    if outcome.returncode:
        failures.append(str(folder.relative_to(root)))
        print(combined)
print(f'TOTAL: {total} tests in {len(folders)} directories')
if failures:
    print('FAILED: ' + ', '.join(failures), file=sys.stderr)
    sys.exit(1)
