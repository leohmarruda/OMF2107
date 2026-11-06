#!/usr/bin/env python3
"""Ren pilot campaign branch dispatcher (first-pass prototype, stdlib).

Every fight outcome comes from the established tournament model. Both the
1-1-1 group tiebreak and unauthored NPC pairs remain provisional.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

Research = Literal['withdraw', 'audited', 'persist_safeguarded']
Disclosure = Literal['full', 'limited', 'concealed']
Evidence = Literal['offline_record', 'witness_protocol', 'hardware_isolation']
Intent = Literal['angel', 'tessa', 'friendship', 'single']
Ending = Literal['angel', 'tessa', 'friendship', 'single']

CORE_CLUES = (
    'executive_write_field_missing',
    'unexplained_permission_escalation',
    'intention_command_mismatch',
    'kreissack_biological_survival',
    'nova_beneficial_rescue',
    'varga_emotional_experiment',
    'ganymede_human_responsibility',
    'nova_conditional_override',
)

@dataclass(frozen=True)
class RenChoices:
    research_path: Research = 'audited'
    symptom_disclosure: Disclosure = 'full'
    corrected_disclosure: bool = False
    evidence_method: Evidence = 'offline_record'
    relationship_intent: Intent = 'friendship'
    angel_reciprocates: bool = False
    tessa_reciprocates: bool = False
    angel_current_commitment_cleared: bool = False
    consent_capacity_clear: bool = True
    private_interface_isolated: bool = False


def simulate_ren(raven_win: bool, mara_win: bool,
                 knockout_wins: tuple[bool, ...] = (False, False, False),
                 choices: RenChoices = RenChoices()) -> dict:
    """Inputs by on-screen opponent order: Raven GB3 then Mara GB1."""
    if any(type(v) is not bool for v in (raven_win, mara_win)):
        raise ValueError('ren group wins must be Boolean')
    tournament = simulate('Ren', (mara_win, raven_win), knockout_wins)
    return interpret(choices, tournament)


def interpret(choices: RenChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Ren':
        raise ValueError('Ren dispatcher needs selected_pilot=Ren')
    if choices.research_path not in ('withdraw','audited','persist_safeguarded'):
        raise ValueError('unknown research path')
    if choices.symptom_disclosure not in ('full','limited','concealed'):
        raise ValueError('unknown disclosure')
    if choices.evidence_method not in ('offline_record','witness_protocol','hardware_isolation'):
        raise ValueError('unknown evidence path')
    if choices.relationship_intent not in ('angel','tessa','friendship','single'):
        raise ValueError('unknown relationship intent')

    rank = tournament['group_standings']['B']['ranked'].index('Ren')+1
    qualified = tournament['selected_pilot_advances_from_group']
    if qualified != (rank <= 2):
        raise AssertionError('group qualification mismatch')
    by_id = {m['id']:m for m in tournament['matches']}
    ids = set(tournament['player_match_ids'])
    if not {'GB1','GB3'} <= ids:
        raise AssertionError('Ren must play both qualifying bouts')
    qf = ('Q2' if rank == 1 else 'Q1') if qualified else None
    if qualified != (qf in ids if qf else False):
        raise AssertionError('wrong group B QF mapping')
    in_sf = 'S_AB' in ids
    in_final = 'FINAL' in ids
    if in_sf and not qualified or in_final and not in_sf:
        raise AssertionError('invalid knockout sequence')

    def opponent(mid: str | None) -> str | None:
        if not mid or mid not in ids:
            return None
        m = by_id[mid]
        return m['right'] if m['left'] == 'Ren' else m['left']

    ready = choices.consent_capacity_clear and choices.private_interface_isolated
    allowed = {'single','friendship'}
    if choices.relationship_intent == 'angel' and ready and choices.angel_reciprocates and choices.angel_current_commitment_cleared:
        allowed.add('angel')
    if choices.relationship_intent == 'tessa' and ready and choices.tessa_reciprocates:
        allowed.add('tessa')

    research_can_resume = (choices.research_path != 'withdraw'
                           and (choices.symptom_disclosure != 'concealed' or choices.corrected_disclosure))
    # Resumption is never automatic: clinical, independent safety and
    # disconnection requirements must additionally be satisfied in-story.

    research_payoff = {
        'withdraw':'independent_civilian_research_or_rest',
        'audited':'external_verifiability_and_revocable_access',
        'persist_safeguarded':'future_independent_review_before_deep_test',
    }[choices.research_path]
    evidence_contribution = {
        'offline_record':'signed_intention_and_authorization_trace',
        'witness_protocol':'human_credential_and_order_chain',
        'hardware_isolation':'physical_second_write_path',
    }[choices.evidence_method]

    scenes = [
        'R1.1_gala', 'R1.2_authority_field', 'R2.1_raven_GB3',
        'R2.2_symptoms_and_trace', 'R2.5_independent_clock',
        'R3.1_mara_GB1', 'R3.2_research_decision',
        'R3.3_lyra_friendship', 'R3.6_group_standings',
        'R4.1_qf_'+qf if qf else 'R4.1b_bench_evidence',
        'R4.2_independent_metrology', 'R4.3_kreissack_alive',
        'R5.3_semifinal' if in_sf else 'R5.3_service_relay',
        'R5.1_accidental_rescue', 'R5.2_research_path',
        'R5.4_varga_separate_study',
        'R6.1_final' if in_final else 'R6.1_actual_broadcast',
        'R6.2_nova_veto_revealed', 'R6.3_special_nova',
        'R6.4_independent_hearing', 'R6.5_epilogue'
    ]
    return {
        'selected_pilot':'Ren', 'ren_group_rank':rank, 'qualified':qualified,
        'group_match_order_on_screen':('GB3','GB1'),
        'qf_id':qf, 'qf_opponent':opponent(qf),
        'sf_opponent':opponent('S_AB'), 'final_opponent':opponent('FINAL'),
        'played_semifinal':in_sf,'played_final':in_final,
        'official_champion':tournament['champion'],
        'ren_champion':tournament['player_champion'],
        'player_elimination_match':tournament['player_elimination_match'],
        'all_essential_clues':CORE_CLUES,
        'evidence_contribution':evidence_contribution,
        'research_path':choices.research_path,
        'research_payoff':research_payoff,
        'research_resumption_may_be_reviewed':research_can_resume,
        'research_resumption_is_automatic':False,
        'romance_endings_available':tuple(sorted(allowed)),
        'main_scenes':tuple(scenes),
        'nova_is_official_match':False,
        'special_nova_access':'independent_timing_and_physical_relay_work',
        'symptoms_magically_cured':False,
        'neural_bonus_to_tournament':False,
    }


def choose_ending(route: dict, desired: Ending) -> str:
    if desired not in route['romance_endings_available']:
        raise ValueError(f'unavailable Ren ending {desired}')
    return desired
