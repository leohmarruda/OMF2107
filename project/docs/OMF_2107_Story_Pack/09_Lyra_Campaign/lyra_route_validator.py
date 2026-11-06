#!/usr/bin/env python3
"""Lyra-specific screenplay dispatcher, first-pass v0.1, not a production engine.

Combines real tournament branch results with social flags. It never supplies or
changes official match winners. Only user-approved *direction* is canon;
individual new romantic options, NPC fallback results, and group circular ranking
remain proposals.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Literal

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate  # type: ignore

RelationshipChoice = Literal['stay_dante', 'steffan_clean', 'steffan_breach', 'single']
NeuralChoice = Literal['decline', 'monitor_only', 'enhanced']
Epilogue = Literal['dante', 'steffan', 'alex', 'solo']


@dataclass(frozen=True)
class LyraChoices:
    relationship: RelationshipChoice = 'steffan_breach'  # mirrors offplayer default
    neural: NeuralChoice = 'decline'
    # L5: A/B/C all separate Steffan, even if feelings persist.
    future_steffan: bool = False
    steffan_admitted: bool = True
    steffan_mutual_recommit: bool = False
    long_repair_interval: bool = False  # weeks/months later, not day 13
    dante_mutual_recommit: bool = False
    dante_accountability_repaired: bool = False
    alex_mutual_interest: bool = False
    alex_adult_verified: bool = False  # precision still unconfirmed in bible
    alex_assignment_finished: bool = False
    alex_recused_from_future_lyra_coverage: bool = False
    alex_editorial_independence: bool = False
    # Explicit post-Ch5 end of Dante relationship permits solo/Alex route.
    dante_amicable_separation: bool = False


def interpret(choices: LyraChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Lyra':
        raise ValueError('Lyra route needs selected_pilot=Lyra')
    if choices.relationship not in ('stay_dante','steffan_clean','steffan_breach','single'):
        raise ValueError('Unknown relationship route')
    if choices.neural not in ('decline','monitor_only','enhanced'):
        raise ValueError('Unknown neural route')
    if choices.future_steffan and choices.relationship not in ('steffan_clean','steffan_breach'):
        raise ValueError('Steffan future possibility requires prior Steffan relationship')

    matched_ids = set(tournament['player_match_ids'])
    qualified = tournament['selected_pilot_advances_from_group']
    participated_qf = any(x in matched_ids for x in ('Q3','Q4'))
    participated_sf = 'S_CD' in matched_ids
    participated_final = 'FINAL' in matched_ids
    if qualified != participated_qf:
        raise AssertionError('Qualification must match QF presence')
    if participated_final and not participated_sf:
        raise AssertionError('No final without a semifinal')
    if participated_sf and not participated_qf:
        raise AssertionError('No semifinal without a QF')

    match_by_id = {m['id']: m for m in tournament['matches']}
    group_c = tournament['group_standings']['C']['ranked']
    assert 'Lyra' in group_c
    rank = group_c.index('Lyra') + 1
    qf_match_id = ('Q3' if rank == 1 else 'Q4') if qualified else None
    if qualified and qf_match_id not in matched_ids:
        raise AssertionError('Wrong QF branch for Group C seeding')
    qf_opponent = None
    if qualified:
        qf = match_by_id[qf_match_id]
        qf_opponent = qf['right'] if qf['left'] == 'Lyra' else qf['left']
    sf_opponent = None
    if participated_sf:
        sf = match_by_id['S_CD']
        sf_opponent = sf['right'] if sf['left'] == 'Lyra' else sf['left']
    final_opponent = None
    if participated_final:
        f = match_by_id['FINAL']
        final_opponent = f['right'] if f['left'] == 'Lyra' else f['left']

    # The L5 Steffan conversation permanently ends the current relationship,
    # irrespective of future-repair eligibility. Staying with Dante does not.
    partner = 'Dante' if choices.relationship == 'stay_dante' and not choices.dante_amicable_separation else None
    if choices.dante_amicable_separation and choices.relationship != 'stay_dante':
        raise ValueError('Can only separate a current Dante relationship')

    endings = {'solo'} if partner is None else {'dante'}
    if partner is None:
        if (choices.dante_mutual_recommit and choices.dante_accountability_repaired
                and choices.long_repair_interval):
            endings.add('dante')
        if (choices.future_steffan and choices.steffan_admitted
                and choices.steffan_mutual_recommit and choices.long_repair_interval):
            endings.add('steffan')
        if (choices.alex_mutual_interest and choices.alex_adult_verified
                and choices.alex_assignment_finished
                and choices.alex_recused_from_future_lyra_coverage
                and choices.alex_editorial_independence):
            endings.add('alex')

    clue_variants = {
        'decline': 'offline_training_footage',
        'monitor_only': 'audit_timestamp_anomaly',
        'enhanced': 'subjective_anticipation_plus_record',
    }
    story = [
        'L1.1_gala', 'L1.2_rivals', 'L1.4_research_offer',
        'L2.1_milano_match', 'L2.2_publicity', 'L2.4_steffan_invitation',
        'L3.1_steffan_match', 'L3.2_romance_choice', 'L3.3_leak',
        'L3.4_neural_clue', 'L4.1_bracket',
        'L4.2_quarterfinal' if qualified else 'L4.2_eliminated_group_stage',
        'L4.3_technician_safety', 'L4.5_kreissack_alive',
        'L5.0_nova_rescue', 'L5.1_varga_evidence', 'L5.2_steffan_accountability' if choices.relationship.startswith('steffan_') else 'L5.2_nonsteffan_truth',
        'L5.4_semifinal' if participated_sf else 'L5.4_independent_safety_audit',
        'L5.5_independent_publication', 'L6.1_preparation',
        'L6.2_final_match' if participated_final else 'L6.2_final_broadcast',
        'L6.3_nova_reveal', 'L6.4_emergency_access', 'L6.5_nova_boss',
        'L6.6_public_aftermath', 'L6.7_eligible_personal_epilogue'
    ]
    return {
        'lyra_group_rank': rank, 'qualified': qualified,
        'qf_opponent': qf_opponent, 'sf_opponent': sf_opponent,
        'final_opponent': final_opponent, 'official_champion': tournament['champion'],
        'lyra_champion': tournament['player_champion'],
        'elimination': tournament['player_elimination_match'],
        'core_scenes': tuple(story),
        'core_clues': ('research_consent_addendum','edited_leak_provenance',
                       'neural_anomaly','relay_permission_violation',
                       'kreissack_biological_survival','nova_beneficial_rescue','varga_independent_audit',
                       'nova_conditional_executive_control'),
        'neural_clue_variant': clue_variants[choices.neural],
        'relationship_after_L5': partner,
        'possible_main_endings': tuple(sorted(endings)),
        'nova_access': 'accredited_technical_witness_and_electra_local_controls',
        'nova_is_official_match': False,
    }


def choose_ending(route: dict, desired: Epilogue) -> str:
    if desired not in route['possible_main_endings']:
        raise ValueError(f'Epilogue {desired} unavailable; available={route["possible_main_endings"]}')
    return f'L6.7_{desired}'


def simulate_lyra(group_wins: tuple[bool,bool], knockout_wins: tuple[bool,...],
                  choices: LyraChoices = LyraChoices()) -> dict:
    return interpret(choices, simulate('Lyra', group_wins, knockout_wins))


def simulate_lyra_screen(milano_win: bool, steffan_win: bool,
                         knockout_wins: tuple[bool,...] = (False,False,False),
                         choices: LyraChoices = LyraChoices()) -> dict:
    """UI-facing group fight order: L2 Milano, then L3 Steffan.

    The baseline engine uses the reverse order (Steffan, Milano). Do NOT
    call simulate_lyra(group_wins, ...) with screen-order input directly.
    """
    if type(milano_win) is not bool or type(steffan_win) is not bool:
        raise ValueError('Lyra screen fights must be Boolean')
    return simulate_lyra((steffan_win, milano_win), knockout_wins, choices)


if __name__ == '__main__':
    import json
    result = simulate_lyra((False, True), (True, True, False))
    print(json.dumps(result, indent=2))
