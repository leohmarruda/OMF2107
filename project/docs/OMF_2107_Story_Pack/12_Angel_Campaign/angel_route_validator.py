#!/usr/bin/env python3
"""Angel campaign branch dispatcher, first-pass editorial implementation.

Never changes a contest result from the shared tournament engine. Romance gates
protect adult age, mutuality, safety, free commitments and professional ethics.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

Identity = Literal['masked', 'controlled', 'public']
Archive = Literal['escrow', 'redacted_release', 'private_verify']
Witness = Literal['forensic', 'human', 'physical']
Release = Literal['audited_public', 'protected_hearing', 'limited_proof']
Partner = Literal['ren', 'crystal', 'leena', 'friendship', 'single']

CORE_CLUES = (
    'legacy_identifier_active',
    'legacy_permission_writes',
    'intention_timing_mismatch',
    'kreissack_biologically_alive',
    'nova_genuine_rescue',
    'varga_independent_ethics_breach',
    'nova_conditional_executive_veto',
    'ganymede_human_responsibility',
)

@dataclass(frozen=True)
class AngelChoices:
    identity_policy: Identity = 'controlled'
    archive_disposition: Archive = 'escrow'
    witness_method: Witness = 'forensic'
    release_policy: Release = 'audited_public'
    relationship_intent: Partner = 'friendship'
    angel_adult_verified: bool = False
    partner_adult_verified: bool = False
    partner_reciprocates: bool = False
    partner_free: bool = False
    ren_capacity_clear: bool = False
    ren_private_interface_isolated: bool = False
    ren_tessa_commitment_cleared: bool = False
    crystal_raven_commitment_cleared: bool = False
    leena_recused: bool = False
    leena_ari_commitment_cleared: bool = False


def simulate_angel(jean_paul_win: bool, dante_win: bool,
                   knockout_wins: tuple[bool, ...] = (False, False, False),
                   choices: AngelChoices = AngelChoices()) -> dict:
    """On-screen order JP GD2, Dante GD1; engine order Dante GD1, JP GD2."""
    if type(jean_paul_win) is not bool or type(dante_win) is not bool:
        raise ValueError('Angel group wins must be Boolean')
    return interpret(choices, simulate('Angel', (dante_win, jean_paul_win), knockout_wins))


def interpret(choices: AngelChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Angel':
        raise ValueError('Angel dispatcher requires selected_pilot=Angel')
    if choices.identity_policy not in ('masked', 'controlled', 'public'):
        raise ValueError('invalid identity policy')
    if choices.archive_disposition not in ('escrow', 'redacted_release', 'private_verify'):
        raise ValueError('invalid archive disposition')
    if choices.witness_method not in ('forensic', 'human', 'physical'):
        raise ValueError('invalid witness method')
    if choices.release_policy not in ('audited_public', 'protected_hearing', 'limited_proof'):
        raise ValueError('invalid release policy')
    if choices.relationship_intent not in ('ren', 'crystal', 'leena', 'friendship', 'single'):
        raise ValueError('invalid relationship intent')

    rank = tournament['group_standings']['D']['ranked'].index('Angel') + 1
    qualified = tournament['selected_pilot_advances_from_group']
    if qualified != (rank <= 2):
        raise AssertionError('invalid Angel group ranking')
    ids = set(tournament['player_match_ids'])
    by_id = {m['id']: m for m in tournament['matches']}
    if not {'GD1', 'GD2'} <= ids:
        raise AssertionError('missing mandatory Angel group fight')
    qf = ('Q4' if rank == 1 else 'Q3') if qualified else None
    if qualified != (qf in ids if qf else False):
        raise AssertionError('wrong quarterfinal dispatch')
    in_sf = 'S_CD' in ids
    in_final = 'FINAL' in ids
    if in_sf and not qualified or in_final and not in_sf:
        raise AssertionError('invalid Angel knockout sequence')

    def opponent(mid: str | None) -> str | None:
        if not mid or mid not in ids:
            return None
        match = by_id[mid]
        return match['right'] if match['left'] == 'Angel' else match['left']

    allowed = {'single', 'friendship'}
    intended = choices.relationship_intent
    adult_mutual = (choices.angel_adult_verified and choices.partner_adult_verified
                    and choices.partner_reciprocates and choices.partner_free)
    if intended == 'ren' and adult_mutual:
        if (choices.ren_capacity_clear and choices.ren_private_interface_isolated
                and choices.ren_tessa_commitment_cleared):
            allowed.add('ren')
    if intended == 'crystal' and adult_mutual and choices.crystal_raven_commitment_cleared:
        allowed.add('crystal')
    if (intended == 'leena' and adult_mutual and choices.leena_recused
            and choices.leena_ari_commitment_cleared):
        allowed.add('leena')

    evidence_contribution = {
        'forensic': 'independently_certified_historical_command_comparison',
        'human': 'consented_witness_and_medical_chain',
        'physical': 'independent_relay_provenance_and_isolation',
    }[choices.witness_method]
    archive_action = {
        'escrow': 'signed_sealed_third_party_copies',
        'redacted_release': 'privacy_preserving_public_discrepancy',
        'private_verify': 'independent_confirmation_then_reviewable_evidence',
    }[choices.archive_disposition]
    release_action = {
        'audited_public': 'redacted_verified_public_report',
        'protected_hearing': 'reviewable_protected_testimony_with_public_summary',
        'limited_proof': 'independently_preserved_minimal_proof_and_escalation',
    }[choices.release_policy]

    scenes = [
        'A1.1_gala_identity', 'A1.2_legacy_nova_identifier',
        'A2.1_jean_paul_GD2', 'A2.2_legacy_permission',
        'A3.1_dante_GD1', 'A3.2_ren_intention_timing',
        'A3.4_original_archive',
        'A4.1_quarterfinal_'+qf if qf else 'A4.1b_qualified_fighters_broadcast',
        'A4.2_kreissack_biological_survival', 'A4.3_witness_method',
        'A5.1_genuine_rescue', 'A5.2_varga_independent_study',
        'A5.3_semifinal' if in_sf else 'A5.3_relay_and_actual_semifinal_broadcast',
        'A5.5_unauthorized_signature_question',
        'A6.1_final' if in_final else 'A6.1_actual_finalist_broadcast',
        'A6.2_nova_control_revealed', 'A6.3_separate_nova_boss',
        'A6.4_disclosure_and_ganymede', 'A6.5_epilogue',
    ]
    return {
        'selected_pilot': 'Angel',
        'group_match_order_on_screen': ('GD2', 'GD1'),
        'angel_group_rank': rank,
        'qualified': qualified,
        'qf_id': qf,
        'qf_opponent': opponent(qf),
        'sf_opponent': opponent('S_CD'),
        'final_opponent': opponent('FINAL'),
        'played_semifinal': in_sf,
        'played_final': in_final,
        'official_champion': tournament['champion'],
        'angel_champion': tournament['player_champion'],
        'player_elimination_match': tournament['player_elimination_match'],
        'all_essential_clues': CORE_CLUES,
        'evidence_contribution': evidence_contribution,
        'archive_action': archive_action,
        'release_action': release_action,
        'identity_policy': choices.identity_policy,
        'romance_endings_available': tuple(sorted(allowed)),
        'main_scenes': tuple(scenes),
        'nova_is_official_match': False,
        'nova_access': 'archival_command_provenance_and_independent_relay_isolation',
        'dangerous_full_nova_blueprint_published': False,
        'neural_bonus_to_tournament': False,
        'privacy_is_always_forfeited': False,
        'secondary_characters_required_for_clues': False,
    }


def choose_ending(route: dict, desired: Partner) -> str:
    if desired not in route['romance_endings_available']:
        raise ValueError(f'unavailable Angel ending: {desired}')
    return desired
