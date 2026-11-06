"""Reproducible editorial review export; proposals are NEVER promoted to canon.

Run `python npc_pair_review.py` from any cwd to regenerate two review artifacts.
"""
from __future__ import annotations
import csv
import itertools
import json
from collections import Counter
from pathlib import Path
from npc_pair_proposals import PROPOSED_PAIR_WINNERS
from tournament_validator import (GROUPS, DEFAULT_KNOCKOUT_WINNERS,
                                  NPC_KNOCKOUT_PRIORITY, simulate)

HERE = Path(__file__).resolve().parent
PILOTS = tuple(p for group in GROUPS.values() for p in group)

# These are proposed *review questions*, NOT substantiated tactical claims.
UPSET_QUESTIONS = {
    frozenset(('Lyra','Crystal')): 'Can Jaguar neutralize Electra positioning without contrived advantage?',
    frozenset(('Mara','Steffan')): 'What concrete Flail-vs-Pyros interaction permits a Mara upset?',
    frozenset(('Raven','Steffan')): 'Can Katana overcome Pyros technical ingenuity in this match?',
    frozenset(('Selene','Mara')): 'Can Mirage create a legitimate tactical opening against Flail?',
    frozenset(('Ren','Angel')): 'What Helix-vs-Chronos interaction supports Ren winning?',
    frozenset(('Milano','Angel')): 'Can Gargoyle resist Chronos tricks without arbitrary immunity?',
    frozenset(('Dante','Ren')): 'What Shredder-vs-Helix tactic supports Dante winning?',
    frozenset(('Jean-Paul','Selene')): 'How does Shadow defeat Mirage given both favor deception?',
}

def build_review():
    priority = {p: i for i, p in enumerate(NPC_KNOCKOUT_PRIORITY)}
    pair_encounters = Counter()
    # These paths are reachability witnesses under proposed NPC results and
    # historical provisional seeding. NOT an exhaustive proof of all score outcomes.
    for pilot in PILOTS:
        for bits in itertools.product((False, True), repeat=5):
            route = simulate(pilot, bits[:2], bits[2:], use_proposed_npc=True)
            for match in route['matches']:
                if match['id'].startswith('G') or pilot in (match['left'], match['right']):
                    continue
                pair_encounters[frozenset((match['left'], match['right']))] += 1
    rows = []
    for pair in sorted(PROPOSED_PAIR_WINNERS, key=lambda pair: tuple(sorted(pair))):
        a,b = sorted(pair)
        proposed = PROPOSED_PAIR_WINNERS[pair]
        canon = DEFAULT_KNOCKOUT_WINNERS.get(pair)
        shortcut = min(pair, key=lambda p: priority[p])
        if canon is not None:
            kind = 'established_exact_pair'
            status = 'canonical_default_only'
        elif proposed != shortcut:
            kind = 'ranking_exception'
            status = 'pending_individual_approval'
        else:
            kind = 'ranking_inherited'
            status = 'pending_individual_approval'
        rows.append({
            'fighter_a': a, 'fighter_b': b,
            'proposed_winner': proposed,
            'established_default_winner': canon or '',
            'old_priority_winner': shortcut,
            'proposal_type': kind,
            'approval_status': status,
            'observed_npc_occurrences_in_384_test_inputs': pair_encounters[pair],
            'observation_scope': 'provisional seed and proposed winners; not exhaustive',
            'matchup_review_question': UPSET_QUESTIONS.get(pair, 'Specify HAR matchup mechanism, evidence, and branch consequences.'),
            'source_needed': '' if canon else 'Active route fight scenes or explicit author decision',
            'editorial_rationale': 'Established cinematic exact-pair result' if canon else 'NOT YET SUBSTANTIATED',
        })
    return rows


def write_review():
    rows = build_review()
    path = HERE / 'NPC_PAIR_EDITORIAL_REVIEW_v3.9.csv'
    with path.open('w', encoding='utf-8', newline='') as handle:
        out = csv.DictWriter(handle, fieldnames=list(rows[0])); out.writeheader(); out.writerows(rows)
    counts = Counter(row['proposal_type'] for row in rows)
    summary = {
        'total_unordered_pairs': len(rows), 'type_counts': dict(counts),
        'unique_test_input_pairs_observed': sum(bool(row['observed_npc_occurrences_in_384_test_inputs']) for row in rows),
        'unobserved_test_input_pairs': [[r['fighter_a'],r['fighter_b']] for r in rows if not r['observed_npc_occurrences_in_384_test_inputs']],
        'new_approved_pair_winners': 0,
        'method': '384 raw simulated input tuples; provisional seeded circular groups; proposed NPC outcomes. Reachability is not a proof of canonical production reachability.',
    }
    (HERE / 'NPC_PAIR_REVIEW_SUMMARY_v3.9.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    return summary

if __name__ == '__main__':
    print(json.dumps(write_review(), indent=2))
