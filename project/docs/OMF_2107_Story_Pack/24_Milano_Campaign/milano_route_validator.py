#!/usr/bin/env python3
"""Milano single-player route adapter, preserving common decisive tournament.

Authorial distinction: a possible Selene romance requires Selene's own agency,
reciprocity, availability and non-coercive corporate separation. Choice flags are
contract inputs, NOT an implemented cross-campaign romance-state engine.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

EVIDENCE = (
    'milano_original_limited_authorization',
    'milano_missing_independent_safety_observer',
    'milano_subsequent_waiver_and_incident_record',
    'selene_independent_supplier_anomaly',
    'ari_independent_ganymede_evidence',
    'jean_paul_varga_unauthorized_emotional_study',
    'angel_ren_day9_kreissack_biologically_alive',
    'nova_day12_genuine_safety_rescue',
    'nova_day12_false_command_attribution',
    'nova_day13_covert_executive_veto',
    'christian_day30_authenticated_devroe_order',
)

@dataclass(frozen=True)
class MilanoChoices:
    public_stance: str = 'private_first'
    authorization_position: str = 'own_vote'
    investigation: str = 'independent_hold'
    review: str = 'recuse_and_disclose'
    board_strategy: str = 'external_oversight'
    institutional_ending: str = 'independent_reform'
    relationship_intent: str = 'solo'
    milano_adult: bool = True
    milano_available: bool = True
    milano_active_consent: bool = False
    selene_adult: bool = True
    selene_available: bool = False
    selene_reciprocates: bool = False
    selene_chooses_milano: bool = False  # external POV / independently scripted choice
    selene_active_consent: bool = False
    meaningful_time_elapsed: bool = False
    separated_corporate_leverage: bool = False
    no_coercive_bargain: bool = True
    no_other_exclusive_commitments: bool = True


def simulate_milano(lyra_win: bool, steffan_win: bool,
                    knockout_wins: tuple[bool, ...] = (False, False, False),
                    choices: MilanoChoices = MilanoChoices()) -> dict:
    """Screen order GC3 vs Lyra, then GC2 vs Steffan; engine GC2 then GC3."""
    if type(lyra_win) is not bool or type(steffan_win) is not bool:
        raise ValueError('Fight outcomes must be decisive bools')
    bracket = simulate('Milano', (steffan_win, lyra_win), knockout_wins)
    return interpret_milano(choices, bracket)


def interpret_milano(choices: MilanoChoices, bracket: dict) -> dict:
    if bracket['selected_pilot'] != 'Milano':
        raise ValueError('Expected Milano bracket')
    domains = {
        'public_stance': {'assure_investors','announce_audit','private_first'},
        'authorization_position': {'own_vote','minimize','contain'},
        'investigation': {'independent_hold','internal_probe','political_trade'},
        'review': {'recuse_and_disclose','lead_internal_review','bury_waiver'},
        'board_strategy': {'external_oversight','controlled_reform','emergency_takeover'},
        'institutional_ending': {'independent_reform','managed_reform','consolidate'},
        'relationship_intent': {'solo','selene','friendship'},
    }
    for name, options in domains.items():
        if getattr(choices, name) not in options:
            raise ValueError(f'Invalid {name}: {getattr(choices,name)!r}')
    rank = bracket['group_standings']['C']['ranked'].index('Milano') + 1
    qf = 'Q3' if rank == 1 else 'Q4' if rank == 2 else None
    matches = {m['id']:m for m in bracket['matches']}
    mine = set(bracket['player_match_ids'])

    def opponent(match_id: str | None):
        if match_id not in mine:
            return None
        match = matches[match_id]
        return match['right'] if match['left']=='Milano' else match['left']

    if bool(qf) != bool('Q3' in mine or 'Q4' in mine):
        raise AssertionError('Illegal C group qualification')
    if ('S_CD' in mine and qf is None) or ('FINAL' in mine and 'S_CD' not in mine):
        raise AssertionError('Illegal knockout gating')
    consent_ready = all((
        choices.milano_adult, choices.milano_available, choices.milano_active_consent,
        choices.selene_adult, choices.selene_available, choices.selene_reciprocates,
        choices.selene_chooses_milano, choices.selene_active_consent,
        choices.meaningful_time_elapsed, choices.separated_corporate_leverage,
        choices.no_coercive_bargain, choices.no_other_exclusive_commitments,
    ))
    if choices.relationship_intent == 'selene':
        relationship = 'selene_mutual_future' if consent_ready else 'selene_unresolved'
    else:
        relationship = choices.relationship_intent

    scenes = [
        'MA1.1', 'MA1.3', 'MA2.1_GC3', 'MA2.2',
        'MA3.1_GC2', 'MA3.2_QUALIFIED' if qf else 'MA3.2_ELIMINATED',
        'MA3.3', 'MA4.1_QF' if qf else 'MA4.1_HEARING',
        'MA4.2', 'MA4.3_DAY9_SURVIVAL', 'MA5.1_DAY11_VARGA',
        'MA5.2_DAY12_RESCUE',
        'MA5.3_DAY12_SF' if 'S_CD' in mine else 'MA5.3_DAY12_NOT_PLAYING',
        'MA6.1_FINAL' if 'FINAL' in mine else 'MA6.1_SPECTATOR',
        'MA6.2_DAY13_NOVA', 'MA6.3_GOVERNANCE', 'MA6.4_ENDING',
        'MA6.5_DAY30_E5_AUTHENTICATION',
    ]
    if choices.relationship_intent == 'selene':
        scenes.extend(('MA1.2_SELENE', 'MA2.4_SELENE', 'MA3.4_SELENE', 'MA4.4_SELENE', 'MA5.4_SELENE'))
    if relationship == 'selene_mutual_future':
        scenes.append('MA6.4_SELENE_MUTUAL')
    if choices.institutional_ending == 'consolidate':
        scenes.append('MA6.4_DARK_CONSOLIDATION')
    if choices.investigation == 'political_trade' or choices.review == 'bury_waiver':
        scenes.append('MA6.4_HISTORICAL_CULPABILITY')

    return {
        'pilot': 'Milano',
        'screen_group_order': ('GC3','GC2'),
        'engine_group_order': ('GC2','GC3'),
        'group_rank': rank,
        'group_circular': bracket['group_standings']['C']['circular_1_1_1'],
        'qualified': qf is not None,
        'qf_id': qf, 'qf_opponent': opponent(qf),
        'semifinal_played': 'S_CD' in mine,
        'semifinal_opponent': opponent('S_CD'),
        'final_played': 'FINAL' in mine,
        'final_opponent': opponent('FINAL'),
        'champion': bracket['champion'],
        'player_champion': bracket['player_champion'],
        'elimination_match': bracket['player_elimination_match'],
        'relationship_ending': relationship,
        'romance_committed': relationship == 'selene_mutual_future',
        'institutional_ending': choices.institutional_ending,
        'milano_prior_vote_history_fixed': True,
        'evidence_independent_of_romance_and_rank': True,
        'essential_evidence': EVIDENCE,
        'qf_day_range': (8,10),
        'semifinal_day': 12,
        'nova_rescue_day': 12,
        'final_day': 13,
        'nova_veto_reveal_day': 13,
        'devroe_order_authentication_day': 30,
        'devroe_order_authenticated_by_day13': False,
        'nova_core_survives_default': False,
        'shared_kreissack_final_line': 'Apparently, I can still surprise you.',
        'nova_boss_separate_from_official_tournament': True,
        'scenes': tuple(scenes),
        'tournament': bracket,
    }
