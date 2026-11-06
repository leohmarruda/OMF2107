#!/usr/bin/env python3
"""Dante playable campaign validator; fight choices independent of romances."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

CLUES = ('public_media_edit', 'maintenance_mirror_anomaly',
         'varga_independent_authentication', 'kreissack_biological_survival',
         'day12_genuine_rescue', 'day13_conditional_veto')

@dataclass(frozen=True)
class DanteChoices:
    public_response: str = 'playful'            # playful/pointed/measured
    lyra_response: str = 'accept'              # accept/lash_out/beg
    revenge_response: str = 'withdraw'         # needle/withdraw/threaten_public_scene
    evidence_policy: str = 'secure'            # secure/grandstand/decline
    witness_policy: str = 'protect_technician' # protect_technician/leak_too_soon/avoid_risk
    confrontation: str = 'clear'               # merciless/clear/vulnerable
    relationship_intent: str = 'solo'          # solo/lyra/steffan/mari/truce
    respect_response: str = 'professional'      # professional/curiosity (DV2.3)
    day11_contact: str = 'boundary'             # boundary/listen (DV5.2)
    later_approach: str = 'none'                # none/explore (DV6.4)
    # Global relationship history; the pilot's wish alone cannot edit any NPC's state.
    lyra_dante_prior_relationship: bool = True
    lyra_dante_current_relationship: bool = False
    lyra_available: bool = False
    lyra_independently_reciprocates: bool = False
    lyra_independent_repair: bool = False
    lyra_steffan_commitment_cleared: bool = True
    dante_available: bool = True
    dante_repaired_outburst: bool = False
    steffan_available: bool = False
    steffan_independently_recognizes_attraction: bool = False
    steffan_independently_reciprocates: bool = False
    steffan_treated_lyra_accountably: bool = False
    steffan_coercive_control_recorded: bool = False
    steffan_coercive_repair_complete: bool = False
    dante_independently_wants_steffan: bool = False
    steffan_lyra_commitment_cleared: bool = True
    mari_available: bool = False
    mari_independently_reciprocates: bool = False
    professional_conflict_resolved: bool = False
    future_interval_elapsed: bool = False


def simulate_dante(jean_paul_win: bool, angel_win: bool,
                   knockout_wins: tuple[bool, ...] = (False, False, False),
                   choices: DanteChoices = DanteChoices()) -> dict:
    """Screen order GD3 Jean-Paul, GD1 Angel; engine order GD1, GD3."""
    if type(jean_paul_win) is not bool or type(angel_win) is not bool:
        raise ValueError('Fight results must be booleans')
    return interpret(choices, simulate('Dante', (angel_win, jean_paul_win), knockout_wins))


def interpret(choices: DanteChoices, bracket: dict) -> dict:
    if bracket['selected_pilot'] != 'Dante':
        raise ValueError('Dante bracket required')
    options = {
        'public_response': ('playful', 'pointed', 'measured'),
        'lyra_response': ('accept', 'lash_out', 'beg'),
        'revenge_response': ('needle', 'withdraw', 'threaten_public_scene'),
        'evidence_policy': ('secure', 'grandstand', 'decline'),
        'witness_policy': ('protect_technician', 'leak_too_soon', 'avoid_risk'),
        'confrontation': ('merciless', 'clear', 'vulnerable'),
        'relationship_intent': ('solo', 'lyra', 'steffan', 'mari', 'truce'),
        'respect_response': ('professional', 'curiosity'),
        'day11_contact': ('boundary', 'listen'),
        'later_approach': ('none', 'explore'),
    }
    for k, allowed in options.items():
        if getattr(choices, k) not in allowed:
            raise ValueError('Invalid choice: ' + k)

    rank = bracket['group_standings']['D']['ranked'].index('Dante') + 1
    qualified = rank <= 2
    qf = 'Q4' if rank == 1 else 'Q3' if rank == 2 else None
    ids = set(bracket['player_match_ids'])
    if qualified != (qf in ids if qf else False):
        raise AssertionError('Quarterfinal bracket inconsistency')
    semifinal = 'S_CD' in ids
    final = 'FINAL' in ids
    if semifinal and not qualified or final and not semifinal:
        raise AssertionError('Impossible Dante progression')
    matches = {m['id']: m for m in bracket['matches']}
    def opponent(mid):
        if mid is None or mid not in ids:
            return None
        m = matches[mid]
        return m['right'] if m['left'] == 'Dante' else m['left']

    future = choices.future_interval_elapsed and choices.dante_available
    repaired_spite = (choices.lyra_response != 'lash_out' or choices.dante_repaired_outburst)
    private_noncoercion = choices.revenge_response != 'threaten_public_scene'
    eligible_lyra = all((
        choices.relationship_intent == 'lyra', future, repaired_spite,
        choices.lyra_dante_prior_relationship,
        choices.lyra_steffan_commitment_cleared,
        choices.lyra_available, choices.lyra_independently_reciprocates,
        choices.lyra_independent_repair, private_noncoercion,
    ))
    romance_path_developed = all((
        choices.respect_response == 'curiosity',
        choices.day11_contact == 'listen',
        choices.later_approach == 'explore',
        choices.confrontation != 'merciless',
        private_noncoercion,
    ))
    eligible_steffan = all((
        choices.relationship_intent == 'steffan', future, romance_path_developed,
        choices.dante_independently_wants_steffan,
        choices.steffan_available,
        choices.steffan_independently_recognizes_attraction,
        choices.steffan_independently_reciprocates,
        choices.steffan_treated_lyra_accountably,
        choices.steffan_lyra_commitment_cleared,
        not choices.steffan_coercive_control_recorded or choices.steffan_coercive_repair_complete,
        repaired_spite, private_noncoercion, choices.confrontation != 'merciless',
    ))
    eligible_mari = all((
        choices.relationship_intent == 'mari', future,
        choices.mari_available, choices.mari_independently_reciprocates,
        choices.professional_conflict_resolved, repaired_spite,
    ))
    if eligible_lyra:
        ending = 'lyra_future_proposal'
    elif eligible_steffan:
        ending = 'steffan_future_proposal'
    elif eligible_mari:
        ending = 'mari_future_proposal'
    elif choices.relationship_intent == 'truce':
        ending = 'professional_truce'
    elif choices.relationship_intent != 'solo':
        ending = 'relationship_not_available'
    elif choices.confrontation == 'merciless' and choices.revenge_response == 'threaten_public_scene':
        ending = 'vindictive_isolation'
    else:
        ending = 'solo_rebuild'
    scenes = ['DV1.1', 'DV1.3', 'DV2.1_GD3', 'DV2.2',
              'DV2.3_CURIOSITY' if choices.respect_response == 'curiosity' else 'DV2.3_PROFESSIONAL_DEFAULT',
              'DV3.1_GD1',
              'DV3.2_HISTORY_DEPENDENT', 'DV3.3', 'DV4.1_STANDINGS',
              'DV4.2_QF' if qualified else 'DV4.2_ELIMINATION',
              'DV4.3_KREISSACK_ALIVE', 'DV5.1_VARGA_DAY11',
              'DV5.2_CONFRONT_STEFFAN_DAY11',
              'DV5.2_LISTEN_OPTIONAL' if choices.day11_contact == 'listen' and choices.respect_response == 'curiosity' and choices.confrontation != 'merciless' else 'DV5.2_BOUNDARY_DEFAULT',
              'DV5.3_NOVA_RESCUE_DAY12',
              'DV5.4_SF' if semifinal else 'DV5.4_WATCH_REAL_SF',
              'DV6.1_FINAL' if final else 'DV6.1_WATCH_REAL_FINAL',
              'DV6.2_NOVA_VETO_AND_DESTRUCTION_DAY13', 'DV6.3_AFTER',
              'DV6.4_POSSIBLE_FUTURE_NOT_DEFAULT' if choices.relationship_intent in ('steffan','truce') else 'DV6.4_SKIPPED',
              'DV6.5_' + ending, 'DV6.6_E5_DAY30']
    if choices.revenge_response == 'threaten_public_scene':
        scenes.append('DV5.2b_PUBLIC_FALLOUT_NONDEFAULT')
    return {
        'selected_pilot': 'Dante', 'group_screen_order': ('GD3', 'GD1'),
        'group_engine_order': ('GD1', 'GD3'),
        'group_rank': rank, 'group_circular': bracket['group_standings']['D']['circular_1_1_1'],
        'qualified': qualified, 'quarterfinal_id': qf, 'quarterfinal_opponent': opponent(qf),
        'semifinal_played': semifinal, 'semifinal_opponent': opponent('S_CD'),
        'final_played': final, 'final_opponent': opponent('FINAL'),
        'official_champion': bracket['champion'], 'dante_champion': bracket['player_champion'],
        'eliminated_at': bracket['player_elimination_match'],
        'confrontation_inevitable': True, 'confrontation_has_possible_spite': True,
        'dante_knows_steffan_attraction': True, 'dante_default_nonromantic': True,
        'dante_steffan_romance_path_developed': romance_path_developed,
        'dante_reciprocity_not_canon': not eligible_steffan,
        'steffan_lyra_genuine_attraction': True, 'lyra_has_independent_agency': True,
        'lyra_evidence_independent': True, 'steffan_emotional_admission_not_forced': True,
        'relationship_ending': ending,
        'romance_achieved': ending in ('lyra_future_proposal', 'steffan_future_proposal','mari_future_proposal'),
        'clues': CLUES, 'scenes': tuple(scenes), 'timeline': {
          'DAY11_VARGA': 11, 'DAY11_CONFRONTATION': 11, 'DAY12_RESCUE': 12,
          'DAY12_SF': 12, 'DAY13_FINAL': 13, 'DAY13_NOVA':13, 'DAY30_E5':30},
        'day13_e5_known': False, 'day30_e5_authenticated': True,
        'nova_not_official_match': True, 'nova_default_survives': False,
        'kreissack_final_line': 'Apparently, I can still surprise you.',
        'tournament': bracket,
    }
