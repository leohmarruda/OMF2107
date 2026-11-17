#!/usr/bin/env python3
"""Steffan six-chapter POV dispatcher. Decisive matches only; no outcome rigging."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

CLUES = (
    'spectator_analytics_public_fingerprint',
    'varga_independent_authentication',
    'kreissack_biological_survival',
    'day12_genuine_rescue',
    'nova_attribution_anomaly',
    'day13_conditional_veto',
)

@dataclass(frozen=True)
class SteffanChoices:
    public_persona: str = 'showman'              # showman/precision/needle_dante
    lyra_approach: str = 'strategic_seduction'  # truthful_interest/strategic_seduction/leave_her_alone
    private_behavior: str = 'press_for_control' # respect_and_wait/press_for_control/keep_distance
    evidence_policy: str = 'secure_source'      # secure_source/exploit_scandal/decline_comment
    technical_role: str = 'independent_media_audit' # independent_media_audit/private_technical_review/self_serving_broadcast
    day11_response: str = 'full_admission'       # full_admission/minimize/blame_varga
    dante_truth: str = 'deny'                   # deny/name_attachment/name_attraction
    relationship_intent: str = 'solo'           # solo/friendship/dante/lyra
    lyra_chose_steffan_earlier: bool = False
    lyra_was_in_dante_relationship_at_start: bool = True
    lyra_dante_commitment_cleared: bool = False
    lyra_reciprocal_future_choice: bool = False
    lyra_post_tournament_repair: bool = False
    lyra_available: bool = False
    steffan_available: bool = True
    coercive_control_recorded: bool = False
    dante_adult: bool = True
    dante_available: bool = False
    dante_reciprocates: bool = False
    dante_independent_consent: bool = False
    dante_harm_addressed: bool = False
    steffan_adult: bool = True
    future_time_elapsed: bool = False


def simulate_steffan(milano_win: bool, lyra_win: bool,
                     knockout_wins: tuple[bool, ...] = (False, False, False),
                     choices: SteffanChoices = SteffanChoices()) -> dict:
    """Screenplay GC2 Milano then GC1 Lyra; engine GC1 Lyra then GC2 Milano."""
    if type(milano_win) is not bool or type(lyra_win) is not bool:
        raise ValueError('Group results must be booleans')
    return interpret(choices, simulate('Steffan', (lyra_win, milano_win), knockout_wins))


def interpret(choices: SteffanChoices, bracket: dict) -> dict:
    if bracket['selected_pilot'] != 'Steffan':
        raise ValueError('Steffan bracket required')
    options = {
        'public_persona': ('showman', 'precision', 'needle_dante'),
        'lyra_approach': ('truthful_interest', 'strategic_seduction', 'leave_her_alone'),
        'private_behavior': ('respect_and_wait', 'press_for_control', 'keep_distance'),
        'evidence_policy': ('secure_source', 'exploit_scandal', 'decline_comment'),
        'technical_role': ('independent_media_audit', 'private_technical_review', 'self_serving_broadcast'),
        'day11_response': ('full_admission', 'minimize', 'blame_varga'),
        'dante_truth': ('deny', 'name_attachment', 'name_attraction'),
        'relationship_intent': ('solo', 'friendship', 'dante', 'lyra'),
    }
    for key, values in options.items():
        if getattr(choices, key) not in values:
            raise ValueError('Invalid ' + key)
    rank = bracket['group_standings']['C']['ranked'].index('Steffan') + 1
    qualified = rank <= 2
    qf = ('Q3' if rank == 1 else 'Q4' if rank == 2 else None)
    mine = set(bracket['player_match_ids'])
    if (qf in mine if qf else False) != qualified:
        raise AssertionError('Quarterfinal mismatch')
    sf = 'S_CD' in mine
    final = 'FINAL' in mine
    if (sf and not qualified) or (final and not sf):
        raise AssertionError('Impossible advancement')
    matches = {m['id']: m for m in bracket['matches']}
    def other(mid):
        if mid is None or mid not in mine:
            return None
        m = matches[mid]
        return m['left'] if m['right'] == 'Steffan' else m['right']

    # Both potential romance endings are proposals, not commitments manufactured by the dispatcher.
    no_control = not choices.coercive_control_recorded and choices.private_behavior != 'press_for_control'
    lyra_future = all((
        choices.relationship_intent == 'lyra', choices.lyra_chose_steffan_earlier,
        choices.lyra_dante_commitment_cleared, choices.lyra_reciprocal_future_choice,
        choices.lyra_post_tournament_repair, choices.lyra_available,
        choices.steffan_available, choices.steffan_adult,
        choices.future_time_elapsed, no_control,
        choices.day11_response == 'full_admission',
    ))
    dante_future = all((
        choices.relationship_intent == 'dante', choices.dante_truth == 'name_attraction',
        choices.dante_adult, choices.steffan_adult,
        choices.dante_available, choices.steffan_available,
        choices.dante_reciprocates, choices.dante_independent_consent,
        choices.dante_harm_addressed, choices.future_time_elapsed,
        not choices.lyra_chose_steffan_earlier or choices.lyra_dante_commitment_cleared,
        no_control,
    ))
    if lyra_future:
        ending = 'lyra_future_proposal'
    elif dante_future:
        ending = 'dante_future_proposal'
    elif choices.relationship_intent == 'friendship':
        ending = 'friendship'
    elif choices.relationship_intent in ('lyra', 'dante'):
        ending = 'unreciprocated_or_not_eligible'
    else:
        ending = 'solo'
    scenes = [
        'ST1.1', 'ST1.2', 'ST2.1_GC2', 'ST2.2',
        'ST3.1_GC1', 'ST3.2', 'ST3.3',
        'ST4.1_GROUP_RANK', 'ST4.2_QF' if qualified else 'ST4.1_NO_QF',
        'ST4.3_KREISSACK_ALIVE',
        'ST5.1_DAY11_VARGA_AND_LYRA_NOTICE', 'ST5.2_DAY12_RESCUE',
        'ST5.3_SF' if sf else 'ST5.3_WATCH_REAL_SF',
        'ST6.1_FINAL' if final else 'ST6.1_WATCH_REAL_FINAL',
        'ST6.2_DAY13_ATTRIBUTION', 'ST6.3_SPECIAL_NOVA',
        'ST6.4_AFTER', 'ST6.5_' + ending, 'ST6.6_DAY30_E5',
    ]
    if choices.lyra_approach != 'leave_her_alone':
        scenes.append('ST3.2_POSSIBLE_TENSION')
    if choices.dante_truth != 'deny':
        scenes.append('ST5.4_POSSIBLE_CONFESSION')
    return {
        'selected_pilot': 'Steffan', 'group_order_screenplay': ('GC2', 'GC1'),
        'group_order_engine': ('GC1', 'GC2'),
        'group_rank': rank, 'group_circular': bracket['group_standings']['C']['circular_1_1_1'],
        'qualified': qualified, 'qf_id': qf, 'qf_opponent': other(qf),
        'semifinal_played': sf, 'semifinal_opponent': other('S_CD'),
        'final_played': final, 'final_opponent': other('FINAL'),
        'official_champion': bracket['champion'],
        'steffan_champion': bracket['player_champion'],
        'eliminated_at': bracket['player_elimination_match'],
        'romance_ending': ending, 'romance_achieved': ending in ('lyra_future_proposal','dante_future_proposal'),
        'lyra_chooses_independently': True, 'dante_chooses_independently': True,
        'private_dominance_is_not_consent': True,
        'varga_study_not_match_rigging': True,
        'lyra_protected_notice_independent': True,
        'core_clues': CLUES,
        'scenes': tuple(scenes),
        'timeline': {'VARGA_NOTICE':11,'RESCUE':12,'SF':12,'OFFICIAL_FINAL':13,'NOVA':13,'E5':30},
        'day13_e5_known': False, 'day30_e5_authenticated': True,
        'nova_after_official_final': True, 'nova_not_official_match': True,
        'nova_default_survives': False,
        'kreissack_final_line': 'Apparently, I can still surprise you.',
        'tournament': bracket,
    }


if __name__ == '__main__':
    import json
    print(json.dumps(simulate_steffan(True,True,(True,False)), indent=2))
