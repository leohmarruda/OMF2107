"""Day-13 integration contract. Provisional gameplay staging, not approved facility canon."""
from dataclasses import dataclass

PILOTS = frozenset(('Ari','Lyra','Mara','Ren','Angel','Crystal','Raven','Jean-Paul','Steffan','Dante','Selene','Milano'))
class FinaleConflict(ValueError): pass

@dataclass(frozen=True)
class FinaleRoute:
    pilot: str
    cleared: bool
    mode: str
    player_action: str
    gateway_actor: str
    access_path: tuple[str, ...]
    evacuation_path: tuple[str, ...]
    life_support_protected: bool = True

def route(pilot: str, *, final_complete: bool, cleared: bool, map_verified: bool=False, map_transmitted: bool=False) -> FinaleRoute:
    if pilot not in PILOTS: raise FinaleConflict('unrecognized pilot')
    if type(final_complete) is not bool or not final_complete: raise FinaleConflict('official FINAL must conclude first')
    if type(cleared) is not bool: raise FinaleConflict('clearance decision must be explicit')
    if pilot != 'Raven' and (map_verified or map_transmitted):
        raise FinaleConflict('map branch belongs to Raven only')
    if cleared:
        return FinaleRoute(pilot, True, 'player_boss', 'player_damages_G', pilot, ('Z0','Z2'), ('Z2','Z0','Z4'))
    if pilot != 'Raven':
        raise FinaleConflict('non-Raven denied-clearance branch not authored')
    if map_transmitted and not map_verified:
        raise FinaleConflict('unsafe/unverified map cannot be transmitted as verified')
    action = 'verify_extract_transmit_map' if map_verified and map_transmitted else 'independent_survey_fallback'
    return FinaleRoute(pilot, False, 'player_containment', action, 'independently_cleared_NPC', ('Z0','Z1'), ('Z1','Z0','Z4'))

def validate_event_sequence(events: tuple[str, ...], scenario: FinaleRoute) -> None:
    mandatory=('FINAL_COMPLETE','EMERGENCY_AUTHORIZED','G_DAMAGED','R_ISOLATED','D_IRREVERSIBLE','E_EJECTION_STARTED','B_L_ENGAGED','CORE_DESTROYED','EVACUATED')
    if len(events)!=len(set(events)): raise FinaleConflict('duplicate finale event')
    if any(x not in events for x in mandatory): raise FinaleConflict('missing mandatory finale event')
    idx={x:events.index(x) for x in events}
    edges=(('FINAL_COMPLETE','EMERGENCY_AUTHORIZED'),('EMERGENCY_AUTHORIZED','G_DAMAGED'),('G_DAMAGED','B_L_ENGAGED'),('R_ISOLATED','B_L_ENGAGED'),('D_IRREVERSIBLE','E_EJECTION_STARTED'),('E_EJECTION_STARTED','B_L_ENGAGED'),('B_L_ENGAGED','CORE_DESTROYED'),('CORE_DESTROYED','EVACUATED'))
    if any(idx[a]>=idx[b] for a,b in edges): raise FinaleConflict('invalid physical event order')
    if scenario.mode=='player_containment' and scenario.gateway_actor==scenario.pilot: raise FinaleConflict('noncombat pilot credited with G')
