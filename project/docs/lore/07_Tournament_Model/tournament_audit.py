#!/usr/bin/env python3
"""Exhaustive reachable outcome audit, never interprets provisional outcomes as canon."""
import csv
import itertools
import json
from collections import Counter
from pathlib import Path
from tournament_validator import GROUPS, simulate


def enumerate_routes():
    rows = []
    for pilot in (p for group in GROUPS.values() for p in group):
        for bits in itertools.product((False, True), repeat=5):
            result = simulate(pilot, bits[:2], bits[2:])
            audit = result['audit']
            rows.append({
                'pilot': pilot,
                'group_bits': ''.join(str(int(x)) for x in bits[:2]),
                'knockout_input_bits': ''.join(str(int(x)) for x in bits[2:]),
                'knockout_bits_consumed': result['used_knockout_results'],
                'champion': result['champion'],
                'player_champion': result['player_champion'],
                'elimination': result['player_elimination_match'] or '',
                'circular_groups': ','.join(result['circular_groups']),
                'unapproved_cycle_groups': ','.join(audit['unapproved_cycle_seed_groups']),
                'provisional_npc_match_ids': ','.join(audit['provisional_npc_match_ids']),
                'canon_ready': audit['canon_ready'],
            })
    return rows


def summarize(rows):
    return {
        'total_input_tuples': len(rows),
        'canonical_input_paths_after_ignored_bits': len(set((r['pilot'], r['group_bits'], r['knockout_input_bits'][:r['knockout_bits_consumed']]) for r in rows)),
        'routes_using_unapproved_seed': sum(bool(r['unapproved_cycle_groups']) for r in rows),
        'routes_using_provisional_npc_result': sum(bool(r['provisional_npc_match_ids']) for r in rows),
        'canon_ready_input_tuples': sum(r['canon_ready'] for r in rows),
        'provisional_match_frequency': dict(sorted(Counter(m for r in rows for m in r['provisional_npc_match_ids'].split(',') if m).items())),
        'circular_group_frequency': dict(sorted(Counter(g for r in rows for g in r['circular_groups'].split(',') if g).items())),
    }


def main():
    output = Path(__file__).resolve().parent / 'audit_outputs'
    output.mkdir(exist_ok=True)
    rows = enumerate_routes()
    with (output / 'route_matrix.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0]); writer.writeheader(); writer.writerows(rows)
    summary = summarize(rows)
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
