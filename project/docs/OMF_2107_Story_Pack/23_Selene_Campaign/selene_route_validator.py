#!/usr/bin/env python3
"""Selene POV route dispatcher; mirrors the global decisive-fight simulator.

Screen group order is GA3 (vs Ari), GA2 (vs Crystal). The shared engine
iterates GA2 then GA3, so translate the inputs. Branch rules below are
editorial proposals, not authority to change shared world canon.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

EVIDENCE = (
    'selene_public_procurement_identifiers',
    'selene_supplier_support_discrepancy',
    'independent_ganymede_ledger',
    'independent_varga_unauthorized_study',
    'angel_ren_kreissack_biologically_alive',
    'nova_real_day12_safety_rescue',
    'nova_day12_false_biological_command_attribution',
    'nova_day13_conditional_executive_veto',
    'christian_day30_authenticated_devroe_e5',
)

@dataclass(frozen=True)
class SeleneChoices:
    identity_strategy: str = 'limited_disclosure'
    investigation: str = 'independent_audit'
    family_mandate: str = 'decline_illicit_access'
    business_strategy: str = 'independent_competitor'
    personal_ending: str = 'solo'
    relationship_intent: str = 'solo'
    selene_adult: bool = True
    selene_available: bool = True
    selene_active_consent: bool = False
    milano_adult: bool = True
    milano_available: bool = False
    milano_reciprocates: bool = False
    milano_active_consent: bool = False
    milano_business_power_separated: bool = False
    jean_paul_adult: bool = True
    jean_paul_available: bool = False
    jean_paul_reciprocates: bool = False
    jean_paul_active_consent: bool = False
    jean_paul_varga_ended: bool = False
    no_leverage_for_intimacy: bool = True
    no_exclusive_external_commitment: bool = True
    meaningful_time_elapsed: bool = False


def simulate_selene(ari_win: bool, crystal_win: bool,
                    knockout_wins: tuple[bool, ...] = (False, False, False),
                    choices: SeleneChoices = SeleneChoices()) -> dict:
    if type(ari_win) is not bool or type(crystal_win) is not bool:
        raise ValueError('Every match requires a decisive boolean result')
    bracket = simulate('Selene', (crystal_win, ari_win), knockout_wins)
    return interpret(choices, bracket)


def interpret(choices: SeleneChoices, bracket: dict) -> dict:
    if bracket['selected_pilot'] != 'Selene':
        raise ValueError('Expected Selene bracket')
    allowed = {
        'identity_strategy': {'own_identity', 'limited_disclosure', 'deny_then_correct'},
        'investigation': {'independent_audit', 'commercial_leverage', 'withhold_for_now'},
        'family_mandate': {'decline_illicit_access', 'negotiate_clean_license', 'seek_illicit_edge'},
        'business_strategy': {'independent_competitor', 'conditional_reform', 'opportunistic_acquisition'},
        'personal_ending': {'solo', 'independent', 'professional_alliance', 'compromised'},
        'relationship_intent': {'solo', 'milano', 'jean_paul', 'friendship'},
    }
    for key, options in allowed.items():
        if getattr(choices, key) not in options:
            raise ValueError(f'Unrecognized {key}: {getattr(choices, key)!r}')
    rank = bracket['group_standings']['A']['ranked'].index('Selene') + 1
    qf_id = 'Q1' if rank == 1 else 'Q2' if rank == 2 else None
    mine = set(bracket['player_match_ids'])
    if bool(qf_id) != bool('Q1' in mine or 'Q2' in mine):
        raise AssertionError('Inconsistent quarterfinal gate')
    if 'S_AB' in mine and not qf_id or 'FINAL' in mine and 'S_AB' not in mine:
        raise AssertionError('Invalid knockout advance')
    matches = {m['id']: m for m in bracket['matches']}

    def foe(mid: str | None):
        if mid not in mine:
            return None
        match = matches[mid]
        return match['right'] if match['left'] == 'Selene' else match['left']

    common_eligibility = all((
        choices.selene_adult, choices.selene_available,
        choices.selene_active_consent, choices.no_leverage_for_intimacy,
        choices.no_exclusive_external_commitment, choices.meaningful_time_elapsed,
    ))
    milano_eligible = common_eligibility and all((
        choices.milano_adult, choices.milano_available,
        choices.milano_reciprocates, choices.milano_active_consent,
        choices.milano_business_power_separated,
    ))
    jp_eligible = common_eligibility and all((
        choices.jean_paul_adult, choices.jean_paul_available,
        choices.jean_paul_reciprocates, choices.jean_paul_active_consent,
        choices.jean_paul_varga_ended,
    ))
    if choices.relationship_intent == 'milano':
        relationship = 'milano_mutual_future' if milano_eligible else 'milano_unresolved'
    elif choices.relationship_intent == 'jean_paul':
        relationship = 'jean_paul_mutual_future' if jp_eligible else 'jean_paul_unresolved'
    else:
        relationship = choices.relationship_intent

    scenes = [
        'SV1.1', 'SV1.2', 'SV1.3', 'SV2.1_GA3', 'SV2.2',
        'SV3.1_GA2', 'SV3.2_QUALIFIED' if qf_id else 'SV3.2_ELIMINATED',
        'SV3.3_IDENTITY', 'SV3.5_FAMILY', 'SV4.1_FINANCIAL',
        'SV4.2_QF' if qf_id else 'SV4.2_NONPLAYER', 'SV4.3_DAY9_SURVIVAL',
        'SV5.1_STRATEGY',
        'SV5.3_SF' if 'S_AB' in mine else 'SV5.3_SPECTATOR',
        'SV5.2_DAY12_RESCUE',
        'SV6.1_FINAL' if 'FINAL' in mine else 'SV6.1_SPECTATOR',
        'SV6.2_DAY13_NOVA', 'SV6.3_ENDING', 'SV6.5_DAY30_AUTHENTICATION',
    ]
    if relationship == 'milano_mutual_future':
        scenes.extend(('SV5.4_MILANO_ELIGIBLE', 'SV6.4_MILANO_ENDING'))
    elif relationship == 'jean_paul_mutual_future':
        scenes.extend(('SV5.5_JP_ELIGIBLE', 'SV6.4_JP_ENDING'))
    if choices.personal_ending == 'compromised' or choices.family_mandate == 'seek_illicit_edge':
        scenes.append('SV6.4_COMPROMISED_CONSEQUENCES')
    if choices.investigation == 'commercial_leverage':
        scenes.append('SV4.1_CREDIBILITY_RISK')

    return {
        'pilot': 'Selene',
        'screen_group_order': ('GA3', 'GA2'),
        'engine_group_order': ('GA2', 'GA3'),
        'group_rank': rank,
        'group_circular': bracket['group_standings']['A']['circular_1_1_1'],
        'qualified': bool(qf_id),
        'qf_id': qf_id, 'qf_opponent': foe(qf_id),
        'semifinal_played': 'S_AB' in mine, 'semifinal_opponent': foe('S_AB'),
        'final_played': 'FINAL' in mine, 'final_opponent': foe('FINAL'),
        'champion': bracket['champion'],
        'player_champion': bracket['player_champion'],
        'player_elimination_match': bracket['player_elimination_match'],
        'relationship_ending': relationship,
        'romance_committed': relationship in ('milano_mutual_future', 'jean_paul_mutual_future'),
        'identity_truth_unchanged': True,
        'varga_cannot_fix_matches': True,
        'essential_evidence': EVIDENCE,
        'essential_evidence_independent_of_romance': True,
        'kreissack_bio_discovery_day': 9,
        'semifinal_day': 11,
        'genuine_rescue_day': 12,
        'nova_veto_reveal_day': 13,
        'devroe_e5_authentication_day': 30,
        'devroe_e5_authenticated_day13': False,
        'nova_core_survives_default': False,
        'shared_kreissack_final_line': 'Apparently, I can still surprise you.',
        'nova_boss_separate_from_tournament': True,
        'scenes': tuple(scenes),
        'tournament': bracket,
    }
