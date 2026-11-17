#!/usr/bin/env python3
"""Raven selected-pilot branch dispatcher; draft narrative gate, not a production save engine."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '17_Devroe_Case'))
from devroe_case_state import case_for_route

CORE_CLUES = (
    'devroe_independent_custody_gap',
    'nova_legacy_identifier',
    'kreissack_biological_survival',
    'nova_genuine_rescue',
    'nova_attribution_discrepancy',
    'nova_conditional_executive_veto',
    'nova_biological_brain_expansion_motive',
    'ganymede_human_responsibility',
    'varga_separate_unethical_study',
)

@dataclass(frozen=True)
class RavenChoices:
    gala_behavior: str = 'admit'
    money_choice: str = 'refuse'
    shuttle_statement: str = 'full'
    crystal_pressure: str = 'leave'
    hearing_response: str = 'testify'
    final_offer: str = 'refuse'
    relationship_intent: str = 'single'
    nova_attitude: str = 'oppose'
    independently_verified_disclosure: bool = False
    raven_free: bool = True
    crystal_free: bool = False
    crystal_reciprocates: bool = False
    chooses_ds: bool = False
    limits_agreed: bool = False
    crystal_active_consent: bool = False
    raven_active_consent: bool = False
    mara_adult_verified: bool = False
    mara_free: bool = False
    mara_reciprocates: bool = False
    crystal_relationship_closed: bool = False

CHOICE_SETS = {
    'gala_behavior': {'probe', 'withhold', 'admit'},
    'money_choice': {'refuse', 'take_advance', 'counsel_copy'},
    'shuttle_statement': {'full', 'selective', 'false_denial'},
    'crystal_pressure': {'exploit', 'bargain', 'disclose', 'leave'},
    'hearing_response': {'testify', 'limited', 'obstruct'},
    'final_offer': {'refuse', 'accept_trace', 'obstruct'},
    'relationship_intent': {'crystal', 'mara', 'friendship', 'single'},
    'nova_attitude': {'oppose', 'envy_but_oppose', 'try_bargain'},
}


def simulate_raven_screen(mara_win: bool, ren_win: bool,
                          knockout_wins: tuple[bool, ...] = (False, False, False),
                          choices: RavenChoices = RavenChoices()) -> dict:
    """Screen order GB2 Mara, GB3 Ren; engine happens to use that order."""
    if type(mara_win) is not bool or type(ren_win) is not bool:
        raise ValueError('fight results must be boolean')
    return interpret(choices, simulate('Raven', (mara_win, ren_win), knockout_wins))


def interpret(choices: RavenChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Raven':
        raise ValueError('Raven validator received another pilot')
    for field, allowed in CHOICE_SETS.items():
        if getattr(choices, field) not in allowed:
            raise ValueError(f'invalid {field}')

    selected = set(tournament['player_match_ids'])
    if not {'GB2', 'GB3'} <= selected:
        raise AssertionError('missing Raven group fight')
    rank = tournament['group_standings']['B']['ranked'].index('Raven') + 1
    qf_id = ('Q2' if rank == 1 else 'Q1') if rank <= 2 else None
    if (qf_id is not None) != ('Q1' in selected or 'Q2' in selected):
        raise AssertionError('Raven qualifier stage mismatch')
    sf = 'S_AB' in selected
    final = 'FINAL' in selected
    if (sf and not qf_id) or (final and not sf):
        raise AssertionError('noncontiguous Raven bracket')
    matches = {m['id']: m for m in tournament['matches']}

    def opp(mid):
        if mid is None or mid not in selected:
            return None
        m = matches[mid]
        return m['right'] if m['left'] == 'Raven' else m['left']

    incidents = []
    if choices.gala_behavior in {'probe', 'withhold'}:
        incidents.append('boundary_testing' if choices.gala_behavior == 'probe' else 'deliberate_ambiguity')
    if choices.money_choice == 'take_advance':
        incidents.append('corrupt_advance')
    if choices.shuttle_statement == 'false_denial':
        incidents.append('shuttle_deceit')
    if choices.crystal_pressure in {'exploit', 'bargain'}:
        incidents.append('isolation_attempt' if choices.crystal_pressure == 'exploit' else 'intimacy_evidence_barter')
    if choices.hearing_response == 'obstruct':
        incidents.append('hearing_obstruction')
    if choices.final_offer in {'accept_trace', 'obstruct'}:
        incidents.append('postrescue_corrupt_payment' if choices.final_offer == 'accept_trace' else 'postrescue_obstruction')

    clean_for_crystal = (
        not incidents and choices.shuttle_statement == 'full'
        and choices.hearing_response == 'testify'
        and choices.independently_verified_disclosure
    )
    all_crystal_gates = (
        clean_for_crystal, choices.raven_free, choices.crystal_free,
        choices.crystal_reciprocates, choices.chooses_ds, choices.limits_agreed,
        choices.crystal_active_consent, choices.raven_active_consent,
    )
    mara_gates = (
        choices.raven_free, choices.mara_adult_verified, choices.mara_free,
        choices.mara_reciprocates, choices.crystal_relationship_closed,
    )
    if incidents and choices.relationship_intent == 'crystal':
        ending = 'dark_exposed'
    elif choices.relationship_intent == 'crystal':
        ending = 'crystal_consensual_ds' if all(all_crystal_gates) else 'crystal_refuses_or_unavailable'
    elif choices.relationship_intent == 'mara':
        ending = 'mara_romance' if all(mara_gates) else 'mara_friendship_only'
    else:
        ending = choices.relationship_intent

    scenes = ['R1.1', 'R1.2', 'R1.3', 'R2.1', 'R2.2', 'R2.3', 'R2.4', 'R3.1', 'R3.2', 'R3.4']
    scenes += ['R4.1_QF' if qf_id else 'R4.1_NO_QF', 'R4.2', 'R4.3']
    scenes += ['R5.1_SF' if sf else 'R5.1_NO_SF', 'R5.1B_E4_RESTORATION_RECORD', 'R5.2']
    scenes += ['R5.3_INFORMED_NO_INTIMACY', 'R5.4']
    scenes += ['R6.1_FINAL' if final else 'R6.1_SPECTATE', 'R6.2', 'R6.3', 'R6.4', 'R6.5']
    scenes += ['R6.5_POSTHEARING_CONSENSUAL_DS' if ending == 'crystal_consensual_ds' else 'R6.5_NO_PRIVATE_ROMANCE']

    result = {
        'selected_pilot': 'Raven',
        'group_rank': rank, 'qualified': rank <= 2, 'qf_id': qf_id,
        'qf_opponent': opp(qf_id), 'sf_reached': sf, 'sf_opponent': opp('S_AB'),
        'final_reached': final, 'final_opponent': opp('FINAL'),
        'champion': tournament['champion'],
        'raven_champion': tournament['champion'] == 'Raven',
        'official_trophy': tournament['champion'] == 'Raven',
        'group_match_order': ('GB2', 'GB3'),
        'match_ids': tuple(tournament['player_match_ids']),
        'raven_enjoys_exploiting_crystal': True,
        'crystal_involuntary_pull_to_raven': True,
        'misconduct_incidents': tuple(incidents),
        'crystal_romance_eligible': all(all_crystal_gates),
        'consensual_private_ds': ending == 'crystal_consensual_ds',
        'relationship_ending': ending,
        'independent_shuttle_inquiry': True,
        'devroe_case': case_for_route(choices.shuttle_statement == 'full' and choices.hearing_response == 'testify'),
        'crystal_truth_independent_of_raven': True,
        'prehearing_private_intimacy': False,
        'core_clues': CORE_CLUES,
        'scene_ids': tuple(scenes),
        'nova_encounter': 'SPECIAL_NOVA_AFTER_ACTUAL_FINAL',
        'timeline': {'S_AB': 11, 'RESCUE': 12, 'S_CD': 12, 'FINAL': 13, 'NOVA': 13},
        'tournament': tournament,
    }
    if result['consensual_private_ds'] and (incidents or not all(all_crystal_gates)):
        raise AssertionError('coercion incorrectly treated as consent')
    if final and not sf:
        raise AssertionError('Raven false final')
    return result
