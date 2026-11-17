#!/usr/bin/env python3
"""Crystal selected-pilot branch dispatcher. Draft, stdlib; no narrative authoring by algorithm."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '17_Devroe_Case'))
from devroe_case_state import case_for_route

CORE_CLUES = (
    'nova_legacy_identifier',
    'devroe_independent_custody_gap',
    'legacy_permission_discrepancy',
    'kreissack_biological_survival',
    'nova_genuine_rescue',
    'nova_attribution_discrepancy',
    'nova_conditional_executive_veto',
    'nova_biological_expansion_motive',
    'ganymede_human_responsibility',
    'varga_separate_unethical_study',
)

@dataclass(frozen=True)
class CrystalChoices:
    shuttle_method: str = 'independent_archive'
    reform_policy: str = 'outside_watchdog'
    relationship_intent: str = 'single'
    chooses_private_ds: bool = False
    raven_reciprocates: bool = False
    raven_free: bool = False
    crystal_free: bool = True
    raven_disclosure_verified: bool = False
    limits_agreed: bool = False
    crystal_active_consent: bool = False
    raven_active_consent: bool = False
    angel_adult_verified: bool = False
    angel_reciprocates: bool = False
    angel_free: bool = False
    raven_relationship_cleared: bool = False
    raven_coercion_recorded: bool = False  # v1.4: no romance following documented exploitation


def simulate_crystal_screen(selene_win: bool, ari_win: bool,
                            knockout_wins: tuple[bool, ...] = (False, False, False),
                            choices: CrystalChoices = CrystalChoices()) -> dict:
    """Input order is screen order, Selene GA2 then Ari GA1; engine is inverse."""
    if type(selene_win) is not bool or type(ari_win) is not bool:
        raise ValueError('group screen outcomes must be booleans')
    return interpret(choices, simulate('Crystal', (ari_win, selene_win), knockout_wins))


def interpret(choices: CrystalChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Crystal':
        raise ValueError('wrong pilot for Crystal dispatcher')
    if choices.shuttle_method not in {'independent_archive', 'protected_deposition', 'victim_family_inquiry'}:
        raise ValueError('unknown shuttle method')
    if choices.reform_policy not in {'conditional_council', 'outside_watchdog', 'public_witness'}:
        raise ValueError('unknown reform policy')
    if choices.relationship_intent not in {'raven', 'angel', 'friendship', 'single'}:
        raise ValueError('unknown romantic intent')

    all_matches = {m['id']: m for m in tournament['matches']}
    pilot_matches = set(tournament['player_match_ids'])
    if not {'GA1', 'GA2'} <= pilot_matches:
        raise AssertionError('selected Crystal must fight both group opponents')
    rank = tournament['group_standings']['A']['ranked'].index('Crystal') + 1
    expected_qf = ('Q1' if rank == 1 else 'Q2') if rank <= 2 else None
    qf = expected_qf if expected_qf in pilot_matches else None
    if rank <= 2 and not qf or rank == 3 and ('Q1' in pilot_matches or 'Q2' in pilot_matches):
        raise AssertionError('bad Crystal QF mapping')
    semifinal = 'S_AB' in pilot_matches
    final = 'FINAL' in pilot_matches
    if semifinal and not qf or final and not semifinal:
        raise AssertionError('non-contiguous Crystal knockout')

    def opponent(match_id: str | None) -> str | None:
        if match_id not in pilot_matches:
            return None
        match = all_matches[match_id]
        return match['right'] if match['left'] == 'Crystal' else match['left']

    raven_gates = (
        choices.chooses_private_ds, choices.raven_reciprocates,
        choices.raven_free, choices.crystal_free,
        choices.raven_disclosure_verified, choices.limits_agreed,
        choices.crystal_active_consent, choices.raven_active_consent,
        not choices.raven_coercion_recorded,
    )
    angel_gates = (
        choices.angel_adult_verified, choices.angel_reciprocates,
        choices.angel_free, choices.crystal_free,
        choices.raven_relationship_cleared,
    )
    intent = choices.relationship_intent
    if intent == 'raven':
        ending = 'raven_consensual_ds' if all(raven_gates) else 'raven_unresolved'
    elif intent == 'angel':
        ending = 'angel_romance' if all(angel_gates) else 'angel_friendship_only'
    else:
        ending = intent
    romance_committed = ending in ('raven_consensual_ds', 'angel_romance')
    # Actual chronological scene dispatch; optional affinity/fanservice scenes are
    # deliberately kept out of this mandatory proof-of-reachability list.
    scenes = ['C1.2', 'C2.1', 'C2.3', 'C3.3', 'C3.4']
    scenes += ['C4.1_QF' if qf else 'C4.1_NO_QF', 'C4.2', 'C4.3']
    scenes += ['C5.1_SF' if semifinal else 'C5.1_BROADCAST', 'C5.1B_E4_RESTORATION_RECORD', 'C5.2']
    scenes += ['C5.3_INFORMED_NO_INTIMACY', 'C5.4']
    scenes += ['C6.1_FINAL' if final else 'C6.1_SPECTATE', 'C6.2', 'C6.3', 'C6.4', 'C6.5']
    scenes += ['C6.5_POSTHEARING_CONSENSUAL_DS' if ending == 'raven_consensual_ds' else 'C6.5_NO_PRIVATE_ROMANCE']

    result = {
        'selected_pilot': 'Crystal',
        'group_rank': rank,
        'qualified': rank <= 2,
        'qf_id': qf,
        'qf_opponent': opponent(qf),
        'sf_reached': semifinal,
        'sf_opponent': opponent('S_AB'),
        'final_reached': final,
        'final_opponent': opponent('FINAL'),
        'champion': tournament['champion'],
        'crystal_champion': tournament['champion'] == 'Crystal',
        'official_trophy': tournament['champion'] == 'Crystal',
        'group_match_order': ('GA2', 'GA1'),
        'match_ids': tuple(tournament['player_match_ids']),
        'involuntary_pull_to_raven': True,
        'raven_coercion_recorded': choices.raven_coercion_recorded,
        'consensual_private_ds': ending == 'raven_consensual_ds',
        'romance_committed': romance_committed,
        'relationship_ending': ending,
        'independent_shuttle_inquiry': True,
        'devroe_case': case_for_route(False),
        'crystal_truth_independent_of_raven': True,
        'prehearing_private_intimacy': False,
        'shuttle_method': choices.shuttle_method,
        'reform_policy': choices.reform_policy,
        'core_clues': CORE_CLUES,
        'scene_ids': tuple(scenes),
        'nova_encounter': 'SPECIAL_NOVA_AFTER_ACTUAL_FINAL',
        'timeline': {'S_AB': 11, 'RESCUE': 12, 'S_CD': 12, 'FINAL': 13, 'NOVA': 13},
        'tournament': tournament,
    }
    if result['consensual_private_ds'] and not all(raven_gates):
        raise AssertionError('enacted D/s missing specific consent or independent disclosure')
    if final and not semifinal:
        raise AssertionError('false final')
    return result
