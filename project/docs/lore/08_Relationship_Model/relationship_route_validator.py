"""OMF 2107 optional romance route gate / ending dispatcher, draft v0.1.

This is a *design* validator for screenplay v0.2, not a production quest engine.
It never writes match outcomes and assumes independent official combat results.
New pairings remain pending owner approval and the authoring of reciprocal attraction.
"""
from dataclasses import dataclass, field
from typing import FrozenSet, Mapping, Optional

# Playable pilots confirmed adult in current bible (precise Angel age still provisional).
KNOWN_ADULT_PILOTS = frozenset({
    'Ari','Mara','Lyra','Dante','Steffan','Crystal','Raven',
    'Jean-Paul','Milano','Selene','Ren',
})
CANON_RELATION = 'Ari:Mara'  # The default romance is choice-dependent, never compulsory.
ENDINGS = {
    'Ari:Mara': '16_ari_mara_restaurant',
    'Ari:Leena': '16B_E1_ari_leena',
    'Mara:Plug': '16B_E2_mara_plug',
    'Crystal:Raven': '16B_E3_crystal_raven',
    'Lyra:Alex': '15B_lyra_alex',
}
PAIRS = {
    'Ari:Mara': ('Ari','Mara'),
    'Ari:Leena': ('Ari','Leena'),
    'Mara:Plug': ('Mara','Plug'),
    'Crystal:Raven': ('Crystal','Raven'),
    'Lyra:Alex': ('Lyra','Alex'),
}
PROFESSIONAL_REQUIRED = {
    'Ari:Leena': 'leena_independent_publication',
    'Lyra:Alex': 'alex_recused',
    'Mara:Plug': 'plug_repair_contract_closed',
}
SUPPORTED_PLAYER_ROUTES = {key for key, pair in PAIRS.items()}


@dataclass(frozen=True)
class StoryState:
    player: str
    # Independent of combat result; the tournament system is source of truth for wins.
    primary_route: Optional[str] = None
    adult_verified: FrozenSet[str] = KNOWN_ADULT_PILOTS
    mutual_attraction: FrozenSet[str] = frozenset()
    # exclusive partner identities, including default offscreen partners.
    commitments: Mapping[str, str] = field(default_factory=dict)
    professional_cleared: FrozenSet[str] = frozenset()
    bonds: Mapping[str, str] = field(default_factory=dict)  # friends, romance, distant
    disclosure_complete: bool = False
    independent_evidence_review: bool = False
    trust_strained: bool = False
    chapter: int = 6


def relationship_ready(state: StoryState, pair: str) -> bool:
    """Opt-in mutual-romance eligibility; a flirt alone can never satisfy it."""
    if pair not in PAIRS:
        return False
    a, b = PAIRS[pair]
    if state.player not in (a, b):
        return False
    if pair not in state.mutual_attraction:
        return False
    if a not in state.adult_verified or b not in state.adult_verified:
        return False
    if a in state.commitments and state.commitments[a] != b:
        return False
    if b in state.commitments and state.commitments[b] != a:
        return False
    required = PROFESSIONAL_REQUIRED.get(pair)
    if required and required not in state.professional_cleared:
        return False
    if pair == 'Crystal:Raven' and not (
        state.disclosure_complete and state.independent_evidence_review
    ):
        return False
    if pair == 'Ari:Mara' and state.trust_strained:
        return False
    return True


def main_ending(state: StoryState) -> str:
    """Exactly one main relationship or solo ending per selected pilot.

    Global investigation/aftermath scenes are *not* changed by this selector.
    """
    if state.primary_route in ENDINGS and relationship_ready(state, state.primary_route):
        # Any optional romance is still only an eligible branch; the scene's own
        # affirmative dialogue choice is required for an on-screen kiss/date.
        return ENDINGS[state.primary_route]
    if state.player == 'Ari' and state.bonds.get('Ari:Mara') == 'friends':
        return '16_ari_mara_friendship_restaurant'
    return '16B_E4_solo_friendship'


def available_scene_slots(state: StoryState) -> tuple[str, ...]:
    """Slots are accessible for their non-romantic alternatives by design."""
    available = {
        1: {'Ari': ('2E_proper_question',)},
        2: {'Lyra': ('1B_off_air',)},
        3: {
            'Ari': ('5B_five_seconds','10B_inventors'),
            'Mara': ('5B_five_seconds',),
            'Jean-Paul': ('3B_velvet_problem',),
            'Ren': ('10B_inventors',),
            'Angel': ('10B_inventors',),
        },
        4: {
            'Ari': ('4B_blue_hour',),
            'Mara': ('3B_cooling_system','4B_blue_hour'),
        },
        5: {
            'Ari': ('2B_clean_custody',),
            'Crystal': ('5B_devroe_document',),
            'Raven': ('5B_devroe_document',),
            'Lyra': ('7B_spotlight',),
        },
        6: {
            'Lyra': ('15B_no_interview',),
        },
    }
    slots = list(available.get(state.chapter, {}).get(state.player, ()))
    if state.chapter == 2:
        slots.append('4B_neon_respite')  # All twelve pilots may skip or attend.
    return tuple(slots)


def blue_hour_choices(state: StoryState) -> tuple[str, ...]:
    if state.chapter != 4 or state.player not in {'Ari','Mara'}:
        return ()
    if relationship_ready(state, 'Ari:Mara') and state.bonds.get('Ari:Mara') == 'romance':
        return ('stay','kiss_and_leave','talk','skip')
    return ('quiet_nonromantic_talk','skip')
