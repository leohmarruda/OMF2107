"""Exhaustive structural knockout-pair reachability, independent of draft winners.

Enumerates all 6^4 possible two-qualifier group orders. For each bracket,
knockout winners may be either participant. The calculation does NOT assume
that any particular score or NPC upset has occurred; it proves structural
possibility, not probability or current narrative reachability.
"""
from __future__ import annotations

import csv
import itertools
from collections import defaultdict
from pathlib import Path
from tournament_validator import GROUPS, DEFAULT_KNOCKOUT_WINNERS

STAGES = ('quarterfinal', 'semifinal', 'final')


def reachability():
    possible = defaultdict(set)
    brackets = 0
    for a,b,c,d in itertools.product(*(itertools.permutations(g) for g in GROUPS.values())):
        brackets += 1
        quarters = ((a[0],b[1]),(a[1],b[0]),(c[0],d[1]),(d[0],c[1]))
        for pair in quarters:
            possible[frozenset(pair)].add('quarterfinal')
        for p,q in itertools.product(quarters[0], quarters[1]):
            possible[frozenset((p,q))].add('semifinal')
        for p,q in itertools.product(quarters[2], quarters[3]):
            possible[frozenset((p,q))].add('semifinal')
        ab = set(quarters[0] + quarters[1])
        cd = set(quarters[2] + quarters[3])
        for p,q in itertools.product(ab,cd):
            possible[frozenset((p,q))].add('final')
    assert brackets == 1296
    return possible


def review_rows():
    possibilities = reachability()
    players = sorted(p for ps in GROUPS.values() for p in ps)
    rows = []
    for a,b in itertools.combinations(players,2):
        pair = frozenset((a,b))
        stages = possibilities.get(pair, set())
        rows.append({'fighter_a': a, 'fighter_b': b,
                     'quarterfinal_possible': 'yes' if 'quarterfinal' in stages else 'no',
                     'semifinal_possible': 'yes' if 'semifinal' in stages else 'no',
                     'final_possible': 'yes' if 'final' in stages else 'no',
                     'structurally_reachable': 'yes' if stages else 'no',
                     'canon_default_winner': DEFAULT_KNOCKOUT_WINNERS.get(pair, ''),
                     'needs_individual_approval': 'no' if pair in DEFAULT_KNOCKOUT_WINNERS else 'yes'})
    return rows


def write_csv(path):
    rows = review_rows()
    with Path(path).open('w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows

if __name__ == '__main__':
    out = Path(__file__).with_name('NPC_STRUCTURAL_REACHABILITY_v4.2.csv')
    rows = write_csv(out)
    print(f'{len(rows)} pairs, {sum(x["needs_individual_approval"]=="yes" for x in rows)} unapproved; {out}')
