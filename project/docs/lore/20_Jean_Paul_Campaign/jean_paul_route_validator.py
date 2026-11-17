#!/usr/bin/env python3
"""Jean-Paul selected-pilot branch dispatcher. Uses shared v1.9 tournament.

Proposed dialogue/relationship scene routing; not a source of canonical NPC outcomes.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

ESSENTIAL_CLUES = (
    'jp_legacy_funding_discrepancy',
    'jp_legacy_authorization_trace',
    'jp_unauthorized_study_pointer',
    'jp_varga_authenticated_misconduct',
    'kreissack_biological_survival',
    'nova_genuine_rescue',
    'nova_attribution_anomaly',
    'nova_conditional_executive_veto',
)

@dataclass(frozen=True)
class JeanPaulChoices:
    approach: str = 'investigate'
    client_policy: str = 'independent_audit'
    evidence_policy: str = 'protected_release'
    varga_boundary: str = 'distance'
    final_evidence_action: str = 'audited_disclosure'
    public_stance: str = 'accountable_testimony'
    relationship_intent: str = 'single'
    jp_adult: bool = True
    jp_available: bool = True
    varga_adult: bool = True
    varga_available: bool = False
    varga_reciprocates: bool = False
    varga_active_consent: bool = False
    jp_active_consent: bool = False
    varga_stopped_collection: bool = False
    varga_disclosed: bool = False
    varga_accepts_oversight: bool = False
    selene_adult: bool = True
    selene_available: bool = False
    selene_reciprocates: bool = False
    selene_active_consent: bool = False
    selene_milano_cleared: bool = False
    no_professional_coercion: bool = True


def simulate_jean_paul(angel_win: bool, dante_win: bool,
                       knockout_wins: tuple[bool, ...] = (False, False, False),
                       choices: JeanPaulChoices = JeanPaulChoices()) -> dict:
    """On-screen and engine input orders are identical: GD2, GD3."""
    if type(angel_win) is not bool or type(dante_win) is not bool:
        raise ValueError('Group outcomes must be booleans')
    bracket = simulate('Jean-Paul', (angel_win, dante_win), knockout_wins)
    return interpret(choices, bracket)


def interpret(choices: JeanPaulChoices, bracket: dict) -> dict:
    if bracket['selected_pilot'] != 'Jean-Paul':
        raise ValueError('Expected Jean-Paul bracket')
    allowed = {
        'approach': {'investigate', 'court', 'keep_distance'},
        'client_policy': {'independent_audit', 'sell_to_bidder', 'war_inside_channel'},
        'evidence_policy': {'protected_release', 'escrow_negotiation', 'brokerage'},
        'varga_boundary': {'distance', 'accountability_only', 'conditional_contact'},
        'final_evidence_action': {'audited_disclosure', 'compromised_bargain', 'illicit_sale'},
        'public_stance': {'accountable_testimony', 'protected_cooperation', 'self_serving_spin'},
        'relationship_intent': {'varga', 'selene', 'friendship', 'single'},
    }
    for field, accepted in allowed.items():
        if getattr(choices, field) not in accepted:
            raise ValueError(f'Invalid {field}')
    ranks = bracket['group_standings']['D']['ranked']
    rank = ranks.index('Jean-Paul') + 1
    qf = ('Q4' if rank == 1 else 'Q3' if rank == 2 else None)
    mine = set(bracket['player_match_ids'])
    if qf is not None and qf not in mine:
        raise AssertionError('Qualified pilot missing QF')
    if qf is None and ('Q4' in mine or 'Q3' in mine):
        raise AssertionError('Eliminated pilot assigned QF')
    sf = 'S_CD' in mine
    final = 'FINAL' in mine
    if sf and not qf or final and not sf:
        raise AssertionError('Knockout progression gap')
    matches = {m['id']: m for m in bracket['matches']}
    def opponent(match_id: str | None) -> str | None:
        if match_id not in mine:
            return None
        m = matches[match_id]
        return m['right'] if m['left'] == 'Jean-Paul' else m['left']

    varga_eligible = all((
        choices.varga_boundary == 'conditional_contact',
        choices.jp_adult, choices.jp_available, choices.varga_adult,
        choices.varga_available, choices.varga_reciprocates,
        choices.jp_active_consent, choices.varga_active_consent,
        choices.varga_stopped_collection, choices.varga_disclosed,
        choices.varga_accepts_oversight, choices.no_professional_coercion,
    ))
    selene_eligible = all((
        choices.jp_adult, choices.jp_available, choices.selene_adult,
        choices.selene_available, choices.selene_reciprocates,
        choices.jp_active_consent, choices.selene_active_consent,
        choices.selene_milano_cleared, choices.no_professional_coercion,
    ))
    if choices.relationship_intent == 'varga':
        ending = 'varga_conditional_romance' if varga_eligible else 'varga_unresolved_or_separated'
    elif choices.relationship_intent == 'selene':
        ending = 'selene_proposed_romance' if selene_eligible else 'selene_friendship_or_distance'
    else:
        ending = choices.relationship_intent

    scenes = ['JP-C1.1', 'JP-C1.2', 'JP-C1.4',
              'JP-C2.1_GD2', 'JP-C2.2',
              'JP-C3.1_GD3', 'JP-C3.2_QUALIFIED' if qf else 'JP-C3.2_ELIMINATED',
              'JP-C3.3',
              'JP-C4.1_QF' if qf else 'JP-C4.1_NO_QF', 'JP-C4.2',
              'JP-C4.3', 'JP-C4.4',
              'JP-C5.0_DAY11_CONFRONT_NOTICE', 'JP-C5.1_DAY12_RESCUE',
              'JP-C5.2_SF' if sf else 'JP-C5.2_SPECTATOR',
              'JP-C5.3',
              'JP-C6.1_FINAL' if final else 'JP-C6.1_SPECTATOR',
              'JP-C6.2_K4_K5_PRIVATE', 'JP-C6.3_SPECIAL_NOVA',
              'JP-C6.4', 'JP-C6.5_DAY30_E5']
    if ending == 'varga_conditional_romance':
        scenes.append('JP-C5.5_CONSENT_ELIGIBLE')
    if ending == 'selene_proposed_romance':
        scenes.append('JP-C5.4_SELENE_ELIGIBLE')

    return {
        'selected_pilot': 'Jean-Paul',
        'group_order': ('GD2', 'GD3'),
        'group_rank': rank,
        'qualified': bool(qf),
        'qf_id': qf,
        'qf_opponent': opponent(qf),
        'semifinal_played': sf,
        'semifinal_opponent': opponent('S_CD'),
        'final_played': final,
        'final_opponent': opponent('FINAL'),
        'official_champion': bracket['champion'],
        'player_champion': bracket['champion'] == 'Jean-Paul',
        'player_elimination_match': bracket['player_elimination_match'],
        'group_circular': bracket['group_standings']['D']['circular_1_1_1'],
        'relationship_ending': ending,
        'romance_committed': ending in {'varga_conditional_romance', 'selene_proposed_romance'},
        'varga_ethics_breach': True,
        'evidence_delivered_independently': True,
        'varga_no_match_fixing': True,
        'lyra_notice_reachable': True,
        'essential_clues': ESSENTIAL_CLUES,
        'day_30_e5_authenticated': True,
        'day_13_e5_authenticated': False,
        'shared_kreissack_last_line': 'Apparently, I can still surprise you.',
        'nova_encounter': 'SPECIAL_NOVA_AFTER_OFFICIAL_FINAL',
        'nova_survives_default': False,
        'timeline': {'BIOLOGICAL_SURVIVAL': 9, 'QF': 9,
                     'RESCUE': 12, 'S_CD': 12, 'FINAL': 13,
                     'NOVA': 13, 'DEVROE_E5': 30},
        'scenes': tuple(scenes),
        'tournament': bracket,
    }
