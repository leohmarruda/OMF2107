#!/usr/bin/env python3
"""Mara pilot-POV scene/epilogue dispatcher v0.1; no combat manipulation.

Uses selected-pilot tournament results; no fight draws. Other-pilot outcomes
and circular group standings still use explicitly provisional tournament rules.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Literal

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

Financial = Literal['itemized_plan', 'paid_work', 'transparent_sponsor']
Disclosure = Literal['private','trusted','public_with_consent']
Role = Literal['mechanical_audit','witness_network','worker_safety']
Intent = Literal['ari','plug','raven','solo']
Response = Literal['boundaries','disagreement','distance']
Epilogue = Literal['solo','friendship','ari','plug','raven']

@dataclass(frozen=True)
class MaraChoices:
    financial_strategy: Financial = 'itemized_plan'
    disclosure: Disclosure = 'private'
    investigation_role: Role = 'mechanical_audit'
    relationship_intent: Intent = 'ari'
    ari_neural_response: Response = 'boundaries'
    ari_mutual_interest: bool = True
    ari_concealed_nii: bool = False
    ari_repair_completed: bool = False
    plug_adult_verified: bool = False
    plug_mutual_interest: bool = False
    plug_professional_conflict_cleared: bool = False
    raven_crystal_commitment_cleared: bool = False
    raven_accountability_completed: bool = False
    raven_mutual_interest: bool = False
    mother_consented_to_publicity: bool = False


def interpret(choices: MaraChoices, tournament: dict) -> dict:
    if tournament['selected_pilot'] != 'Mara':
        raise ValueError('Requires selected pilot Mara')
    if choices.financial_strategy not in ('itemized_plan','paid_work','transparent_sponsor'):
        raise ValueError('Unknown financial strategy')
    if choices.disclosure not in ('private','trusted','public_with_consent'):
        raise ValueError('Unknown disclosure choice')
    if choices.investigation_role not in ('mechanical_audit','witness_network','worker_safety'):
        raise ValueError('Unknown investigation role')
    if choices.relationship_intent not in ('ari','plug','raven','solo'):
        raise ValueError('Unknown relationship intent')
    if choices.ari_neural_response not in ('boundaries','disagreement','distance'):
        raise ValueError('Unknown Ari neural response')
    # The mother's independent consent and Mara's chosen disclosure policy
    # are *both* needed for public medical publicity. A sponsor proposal is
    # likewise contingent on her consent, but can otherwise stay private.
    publicity_permitted = (choices.disclosure == 'public_with_consent'
                           and choices.mother_consented_to_publicity)
    sponsor_consent_cleared = (choices.financial_strategy != 'transparent_sponsor'
                               or choices.mother_consented_to_publicity)

    standings = tournament['group_standings']['B']['ranked']
    rank = standings.index('Mara')+1
    qualified = tournament['selected_pilot_advances_from_group']
    if qualified != (rank <= 2):
        raise AssertionError('Wrong group qualification')
    by_id = {m['id']: m for m in tournament['matches']}
    my_ids = set(tournament['player_match_ids'])
    assert {'GB1','GB2'} <= my_ids
    qf_id = ('Q2' if rank == 1 else 'Q1') if qualified else None
    if qualified != (qf_id in my_ids if qf_id else False):
        raise AssertionError('Wrong Mara QF mapping')
    sf = 'S_AB' in my_ids
    finalist = 'FINAL' in my_ids
    if sf and not qualified or finalist and not sf:
        raise AssertionError('Impossible knockout progression')

    def opponent(match_id: str | None) -> str | None:
        if match_id is None or match_id not in my_ids:
            return None
        m = by_id[match_id]
        return m['right'] if m['left'] == 'Mara' else m['left']

    eligible = {'solo','friendship'}
    if choices.relationship_intent == 'ari' and choices.ari_mutual_interest and (not choices.ari_concealed_nii or choices.ari_repair_completed):
        eligible.add('ari')
    if choices.relationship_intent == 'plug' and (choices.plug_adult_verified and choices.plug_mutual_interest and choices.plug_professional_conflict_cleared):
        eligible.add('plug')
    if choices.relationship_intent == 'raven' and (choices.raven_crystal_commitment_cleared and choices.raven_accountability_completed and choices.raven_mutual_interest):
        eligible.add('raven')

    clue_roles = {'mechanical_audit':'independent_physical_relay_isolation',
                  'witness_network':'distributed_human_and_signature_custody',
                  'worker_safety':'certified_perimeter_and_life_support_watch'}
    scenes = [
        'M1.1_care_call', 'M1.2_ari_gala', 'M1.4_raven_rivalry',
        'M2.1_raven_match', 'M2.2_ledger', 'M2.3_ren_match',
        'M2.5_remote_timestamp', 'M3.1_ari_training', 'M3.3_real_bracket',
        'M4.1_quarterfinal' if qualified else 'M4.1b_independent_audit',
        'M4.2_mother_agency','M4.3_remote_relay','M4.4_kreissack_alive',
        'M5.3_semifinal' if sf else 'M5.3_evidence_custody',
        'M5.0_accidental_rescue','M5.1_contingent_income',
        'M5.4_varga_audit',
        'M6.1_final_match' if finalist else 'M6.1_real_final_broadcast',
        'M6.2_nova_conditional_autonomy','M6.3_special_nova_boss',
        'M6.4_public_accountability','M6.5_personal_epilogue'
    ]
    return {
        'mara_group_rank':rank,
        'qualified':qualified,
        'group_match_order_on_screen':('GB2','GB1'),
        'qf_id':qf_id,'qf_opponent':opponent(qf_id),
        'sf_opponent':opponent('S_AB'),'final_opponent':opponent('FINAL'),
        'ari_is_official_opponent':any(opponent(i) == 'Ari' for i in (qf_id,'S_AB','FINAL')),
        'elimination':tournament['player_elimination_match'],
        'official_champion':tournament['champion'],
        'mara_champion':tournament['player_champion'],
        'prize_eligible':tournament['player_champion'],
        'prize_received':'not_assumed_until_settlement',
        'financial_strategy':choices.financial_strategy,
        'sponsor_consent_cleared':sponsor_consent_cleared,
        'financial_strategy_effective':(choices.financial_strategy if sponsor_consent_cleared else 'itemized_plan'),
        'care_plan':'independent_contingent_plan_always',
        'publicity_permitted':publicity_permitted,
        'evidence_role':clue_roles[choices.investigation_role],
        'core_clues':('remote_maintenance_write','neural_timing_anomaly',
                     'elevated_relay_permission','kreissack_biological_survival',
                     'nova_beneficial_safety_rescue','varga_unauthorized_experiment',
                     'ganymede_human_responsibility','nova_conditional_executive_veto'),
        'possible_main_endings':tuple(sorted(eligible)),
        'main_scenes':tuple(scenes),
        'nova_access':'independent_worker_safety_credential',
        'nova_is_official_match':False,
    }


def choose_ending(route: dict, desired: Epilogue) -> str:
    if desired not in route['possible_main_endings']:
        raise ValueError(f'Unavailable Mara ending: {desired}')
    return 'M6.5_'+desired


def simulate_mara(raven_win: bool, ren_win: bool, knockout_wins: tuple[bool,...],
                  choices: MaraChoices = MaraChoices()) -> dict:
    """Screenplay order (Raven then Ren), reversed for underlying engine."""
    return interpret(choices, simulate('Mara',(ren_win,raven_win),knockout_wins))

if __name__ == '__main__':
    import json
    print(json.dumps(simulate_mara(True,True,(False,)),indent=2))
