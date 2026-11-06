"""OMF 2107 v1.1 audit layer: fight-order adapters, scene chronology, romance graph.

One selected pilot per save. Stories are mutually exclusive world histories, not
five simultaneous protagonists winning contradictory fights. This module checks
only specified invariants, not NPC romance consent or artistic quality.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import sys

ROOT=Path(__file__).resolve().parents[1]
for folder in ('07_Tournament_Model','09_Lyra_Campaign','10_Mara_Campaign','11_Ren_Campaign','12_Angel_Campaign'):
    sys.path.insert(0, str(ROOT/folder))
from tournament_validator import simulate
from lyra_route_validator import simulate_lyra_screen
from mara_route_validator import simulate_mara
from ren_route_validator import simulate_ren
from angel_route_validator import simulate_angel

# These are opponent-order labels on the *player's screen*, NOT engine tuples.
FIGHTS_ON_SCREEN={
 'Ari':('Selene','Crystal'),
 'Lyra':('Milano','Steffan'),
 'Mara':('Raven','Ren'),
 'Ren':('Raven','Mara'),
 'Angel':('Jean-Paul','Dante'),
}
DEFAULT_SCREEN_WINS={
 'Ari':(True,False), 'Lyra':(True,False),
 'Mara':(True,True), 'Ren':(True,False), 'Angel':(True,True)
}
DEFAULT_KNOCKOUT_WINS={
 'Ari':(True,True,True), 'Lyra':(True,True,False),
 'Mara':(False,), 'Ren':(False,), 'Angel':(False,)
}
STORY_EVENTS=(
 'group_stage','quarterfinals','AB_semifinal_day11',
 'nova_rescue_day12_midday','CD_semifinal_day12_evening',
 'official_final_day13','nova_executive_veto_reveal','special_nova_boss'
)


def simulate_screen(protagonist: str, first_win:bool, second_win:bool,
                    knockout_wins:tuple[bool,...]) -> tuple[dict, dict|None]:
    """Return shared tournament and optional campaign dispatch, from UI order."""
    if protagonist not in FIGHTS_ON_SCREEN: raise ValueError('Unsupported protagonist')
    if type(first_win) is not bool or type(second_win) is not bool:
        raise ValueError('screen match results must be booleans')
    if protagonist=='Ari':
        tour=simulate('Ari',(second_win,first_win),knockout_wins)
        route=None # Ari cinematic still lacks a full screenplay dispatcher.
    elif protagonist=='Lyra':
        route=simulate_lyra_screen(first_win,second_win,knockout_wins)
        tour=simulate('Lyra',(second_win,first_win),knockout_wins)
    elif protagonist=='Mara':
        route=simulate_mara(first_win,second_win,knockout_wins)
        tour=simulate('Mara',(second_win,first_win),knockout_wins)
    elif protagonist=='Ren':
        route=simulate_ren(first_win,second_win,knockout_wins)
        tour=simulate('Ren',(second_win,first_win),knockout_wins)
    else:
        route=simulate_angel(first_win,second_win,knockout_wins)
        tour=simulate('Angel',(second_win,first_win),knockout_wins)
    if route is not None:
        name_field={'Lyra':'lyra_champion','Mara':'mara_champion','Ren':'ren_champion','Angel':'angel_champion'}[protagonist]
        assert route['official_champion']==tour['champion']
        assert route[name_field]==tour['player_champion']
    return tour,route


# Active romantic commitments are one single global graph. No automatic
# overwriting a nonselected character's prior partners just because a new route
# was asked for. Optional friendship/solo paths never remove commitments.
PARTNER_ID={
 'Lyra':{'dante':'Dante','steffan':'Steffan','alex':'Alex'},
 'Mara':{'ari':'Ari','plug':'Plug','raven':'Raven'},
 'Ren':{'angel':'Angel','tessa':'Tessa'},
 'Angel':{'ren':'Ren','crystal':'Crystal','leena':'Leena'},
}
ENDINGS_KEY={'Lyra':'possible_main_endings', 'Mara':'possible_main_endings',
             'Ren':'romance_endings_available', 'Angel':'romance_endings_available'}

class RelationshipConflict(ValueError): pass


def normalized_pairs(pairs:Iterable[tuple[str,str]]) -> frozenset[frozenset[str]]:
    normalized=set()
    occupied={}
    for a,b in pairs:
        if not a or not b or a==b: raise RelationshipConflict('invalid pair')
        for person,other in ((a,b),(b,a)):
            if person in occupied and occupied[person]!=other:
                raise RelationshipConflict(f'{person} already committed to {occupied[person]}')
            occupied[person]=other
        normalized.add(frozenset((a,b)))
    return frozenset(normalized)


def resolve_ending(protagonist:str,route:dict,ending:str,
                   current_pairs:Iterable[tuple[str,str]]=(),
                   verified_separations:Iterable[tuple[str,str]]=()) -> frozenset[frozenset[str]]:
    """Reject exclusivity conflicts. Verification of separations comes from
    *independent authored scenes*, not this validator or user-intent flags.
    Caller must check that the partner's own choice and eligibility are real.
    """
    if protagonist not in ENDINGS_KEY: raise ValueError('Ari route not implemented here')
    if ending not in route[ENDINGS_KEY[protagonist]]:
        raise RelationshipConflict('romantic ending not eligible in local route')
    current=normalized_pairs(current_pairs)
    released=normalized_pairs(verified_separations)
    if not released <= current:
        raise RelationshipConflict('cannot release a nonexistent bond')
    after=current-released
    choice=PARTNER_ID[protagonist].get(ending)
    if choice:
        return normalized_pairs([tuple(p) for p in after]+[(protagonist,choice)])
    return after


def chronology_check(protagonist:str,route:dict|None):
    """Checks known shared mandatory-scene ordering, not production scheduling."""
    if protagonist=='Ari': return True # Ari Day 11/12 prose; no executable dispatcher.
    scenes=route['core_scenes'] if protagonist=='Lyra' else route['main_scenes']
    anchors={
        'Lyra':('L5.0_nova_rescue','L5.4_'),
        'Mara':('M5.3_','M5.0_accidental_rescue'),
        'Ren':('R5.3_','R5.1_accidental_rescue'),
        'Angel':('A5.1_genuine_rescue','A5.3_'),
    }
    first,second=anchors[protagonist]
    first_index=next(i for i,s in enumerate(scenes) if s.startswith(first))
    second_index=next(i for i,s in enumerate(scenes) if s.startswith(second))
    if first_index>=second_index:
        raise AssertionError(f'{protagonist} has noncanonical semifinal/rescue clock')
    return True
