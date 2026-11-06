"""Christian's non-playable secondary arc: evidence chronology, agency and romance gates.

Not a production save-state implementation; inputs such as global commitments and editor
recusal must come from independently recorded world events, not a player-controlled flag.
"""
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '17_Devroe_Case'))
from devroe_case_state import case_for_route, HISTORICAL_FACTS, INDEPENDENT_EVIDENCE

EVIDENCE_DAYS = {'E1': 5, 'E2': 8, 'E3': 10, 'E4': 11, 'E5': 30}
EVIDENCE_IDS = dict(zip(EVIDENCE_DAYS, INDEPENDENT_EVIDENCE))

@dataclass(frozen=True)
class ChristianChoices:
    family_dynamic: str = 'parallel'  # collaborate | parallel | private | intrusive
    records_approach: str = 'methodical'  # methodical | public_pressure
    raven_meeting: str = 'formal'  # formal | demand_meeting | avoid_face_to_face
    after_hearing: str = 'records_service'  # records_service | fieldwork | music_break
    romance_intent: str = 'none'  # none | leena
    both_adults_confirmed: bool = False
    leena_independently_reciprocates: bool = False
    christian_reciprocates: bool = False
    leena_editor_recusal_accepted: bool = False
    leena_recusal_day: int | None = None
    leena_has_partner: bool = False
    christian_has_partner: bool = False
    leena_other_route_reserved: bool = False  # Ari/Angel/etc global exclusive pair
    dance_kiss_intent: bool = False


def evidence_known_by_christian(day: int):
    """Only independently authenticated case evidence, never speculation or rumors."""
    if day < 0:
        raise ValueError('day must be nonnegative')
    return tuple(EVIDENCE_IDS[k] for k, earliest in EVIDENCE_DAYS.items() if earliest <= day)


def christian_secondary_arc(choices: ChristianChoices = ChristianChoices(), *,
                             selected_pilot: str = 'Crystal',
                             raven_disclosure: str = 'false_denial',
                             pilot_eliminated: bool = False):
    allowed = {
        'family_dynamic': {'collaborate','parallel','private','intrusive'},
        'records_approach': {'methodical','public_pressure'},
        'raven_meeting': {'formal','demand_meeting','avoid_face_to_face'},
        'after_hearing': {'records_service','fieldwork','music_break'},
        'romance_intent': {'none','leena'},
    }
    for key, values in allowed.items():
        if getattr(choices, key) not in values:
            raise ValueError(f'invalid {key}')
    if selected_pilot not in {'Ari','Lyra','Mara','Ren','Angel','Crystal','Raven'}:
        raise ValueError('unknown selected pilot')
    if raven_disclosure not in {'full','selective','false_denial'}:
        raise ValueError('invalid Raven statement')
    if choices.leena_recusal_day is not None and choices.leena_recusal_day < 0:
        raise ValueError('invalid recusal day')

    global_free = not (choices.leena_has_partner or choices.christian_has_partner
                       or choices.leena_other_route_reserved)
    valid_recusal = (choices.leena_editor_recusal_accepted and
                     choices.leena_recusal_day is not None)
    mutual = (choices.both_adults_confirmed and choices.christian_reciprocates and
              choices.leena_independently_reciprocates)
    romance = (choices.romance_intent == 'leena' and global_free and mutual and
               valid_recusal and choices.leena_recusal_day <= 30)
    day10_kiss = (choices.dance_kiss_intent and global_free and mutual and valid_recusal
                  and choices.leena_recusal_day <= 10)

    scenes = [
        ('CH1.1_PUBLIC_INDEX',0),('CH1.2_LEENA_MEETING',0),('CH1.3_PRIVATE_MEMORY',1),
        ('CH2.1_CERTIFIED_REQUEST',4),('CH2.2_SIBLING_BOUNDARY',4),
        ('CH2.3_E1_CUSTODY_GAP',5),('CH3.1_E2_SIGNED_RELAY_HOLD',8),
        ('CH3.2_INDEPENDENT_JOURNALISM',8),('CH3.3_BROKER_REFUSED',8),
        ('CH4.1_E3_LETHAL_COMMAND_FORENSIC',10),('CH4.2_AUTONOMY_CONFLICT',10),
        ('CH4.3_NIGHT_MARKET',10),('CH5.1_E4_RESTORE_REQUEST',11),
        ('CH5.2_GENUINE_NOVA_RESCUE',12),('CH5.3_PRIVACY_NOT_PUBLICITY',12),
        ('CH6.1_POST_FINAL_NOVA_VETO',13),('CH6.1B_E5_KREISSACK_ORDER',30),('CH6.2_INDEPENDENT_HEARING',30),
        ('CH6.3_PERSONAL_EPILOGUE',30),('CH6.4_TRANSIT_PLATFORM',30)
    ]
    if day10_kiss:
        scenes.insert(next(i for i,s in enumerate(scenes) if s[0]=='CH5.1_E4_RESTORE_REQUEST'),
                      ('CH4.3_OPTIONAL_MUTUAL_KISS',10))
    if choices.family_dynamic == 'intrusive':
        scenes.insert(next(i for i,s in enumerate(scenes) if s[0]=='CH6.2_INDEPENDENT_HEARING'),
                      ('CH5.3_FAMILY_TRUST_REPAIR_OR_DISTANCE',12))
    if romance:
        scenes.insert(next(i for i,s in enumerate(scenes) if s[0]=='CH6.4_TRANSIT_PLATFORM'),
                      ('CH6.3_LEENA_RECIPROCAL_ROMANCE',30))
    case = case_for_route(raven_disclosure == 'full')
    return {
        'selected_pilot': selected_pilot,
        'nonplayable': True,
        'pilot_eliminated': pilot_eliminated,
        'evidence_by_day': {day: evidence_known_by_christian(day) for day in [0,4,5,8,10,11,12,13,30]},
        'evidence_immutable': case.independent_evidence,
        'historical_facts': case.historical_facts,
        'unproven_but_for_rescue': not case.rescue_if_restored_proven,
        'kill_order_signer_unknown': not case.kill_order_signer_identified, # at campaign end (Day 30)
        'kill_order_signer_known_by_day': {day: (day >= 30 and case.kill_order_signer_identified) for day in [0,4,5,8,10,11,12,13,30]},
        'legal_outcome_unresolved': not case.criminal_verdict_final,
        'new_nova_veto_proven_day': 13,  # strictly after the official final
        'scene_ids': tuple(s for s,day in scenes),
        'scene_days': dict(scenes),
        'family_trust_cost': choices.family_dynamic == 'intrusive',
        'christian_ending': choices.after_hearing,
        'leena_romance': romance,
        'day10_kiss': day10_kiss,
        'leena_has_independent_editorial_recusal': valid_recusal,
        'raven_statement': raven_disclosure,
        'tournament_modified': False,
        'crystal_romance_determined_by_christian': False,
    }
