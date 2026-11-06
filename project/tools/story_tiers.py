#!/usr/bin/env python3
"""Report the story's pacing by tier: reading time of the spine, the optional episodes and the arcade cut.

Usage: python tools/story_tiers.py [--story data/story/ari.story] [--tiers data/story/ari.tiers] [--unassigned]

Reading time is words in `say` lines at 170 words per minute plus 1.5 s per line for timing, counted per scene (not per
route: a branch the player never takes still counts). Fight time is gameplay and is not counted. The audit's targets
(Critical_Story_Audit_v1.0.md 9.2) are 25 to 35 minutes of mandatory material and 5 to 8 minutes for an arcade run,
design targets and not measurements.
"""
import argparse
import fnmatch
import re
import sys
from pathlib import Path

WPM = 170.0
SECONDS_PER_LINE = 1.5


def read_scenes(path: Path) -> dict[str, tuple[int, int]]:
    """scene name -> (say lines, words)."""
    scenes: dict[str, list[int]] = {}
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"scene (\S+)", line)
        if m:
            cur = scenes.setdefault(m.group(1), [0, 0])
        elif cur is not None and line.startswith("say"):
            text = line.split(":", 1)[1] if ":" in line else ""
            cur[0] += 1
            cur[1] += len(text.split())
    return {k: (v[0], v[1]) for k, v in scenes.items()}


def read_tiers(path: Path) -> list[tuple[str, str, bool]]:
    rules = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2 or parts[1] not in ("spine", "optional") or parts[2:] not in ([], ["arcade"]):
            sys.exit(f"{path}:{n}: expected '<scene> <spine|optional> [arcade]', got {line!r}")
        rules.append((parts[0], parts[1], len(parts) == 3))
    return rules


def minutes(lines: int, words: int) -> float:
    return words / WPM + lines * SECONDS_PER_LINE / 60.0


def main() -> int:
    here = Path(__file__).resolve().parent.parent / "data" / "story"
    ap = argparse.ArgumentParser()
    ap.add_argument("--story", type=Path, default=here / "ari.story")
    ap.add_argument("--tiers", type=Path, default=here / "ari.tiers")
    ap.add_argument("--unassigned", action="store_true", help="list the scenes no rule matches")
    args = ap.parse_args()
    scenes, rules = read_scenes(args.story), read_tiers(args.tiers)
    totals = {"spine": [0, 0], "optional": [0, 0], "arcade": [0, 0], "unassigned": [0, 0]}
    counts = dict.fromkeys(totals, 0)
    unassigned = []
    for name, (lines, words) in scenes.items():
        hit = next(((t, a) for pat, t, a in rules if fnmatch.fnmatchcase(name, pat)), None)
        tier = hit[0] if hit else "unassigned"
        for key in (tier, "arcade" if hit and hit[1] else None):
            if key:
                totals[key][0] += lines
                totals[key][1] += words
                counts[key] += 1
        if not hit:
            unassigned.append((name, lines, words))
    for key, label, target in (("spine", "mandatory spine", "25-35 min"), ("arcade", "arcade cut", "5-8 min"),
                               ("optional", "optional episodes", ""), ("unassigned", "unassigned", "")):
        lines, words = totals[key]
        print(f"{label:18} {counts[key]:3} scenes {lines:5} lines {words:6} words  ~{minutes(lines, words):5.1f} min"
              + (f"   (audit target {target})" if target else ""))
    print("(all branches counted, so a single route is shorter; fights not counted)")
    if args.unassigned:
        for name, lines, words in sorted(unassigned, key=lambda x: -x[2]):
            print(f"  unassigned: {name} ({lines} lines, {words} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
