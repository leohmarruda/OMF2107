"""Explicit pre-existing statuses and scene-time, branch-local projections.

Baseline events assert status only. They do NOT assert that particular CNM
terms, conversations, or legal/ethical permissions occurred on-screen.
"""
from dataclasses import dataclass
from world_state import Event, WorldState, StateConflict, BASELINE_SOURCE

_BASELINE = (
    ('baseline_dante_lyra','baseline_bond','Dante','Lyra'),
    ('baseline_cossette_ibrahim','baseline_bond','Cossette','Ibrahim'),
    ('baseline_cossette_milano','baseline_casual','Cossette','Milano'),
)

def new_canonical_world(pilot: str) -> WorldState:
    world = WorldState(pilot)
    for eid,kind,a,b in _BASELINE:
        world.apply(Event(eid,kind,'day0_1',a,b,(BASELINE_SOURCE,)))
    return world

@dataclass(frozen=True)
class RelationshipView:
    phase: str
    event_boundary: str | None
    committed: frozenset[frozenset[str]]
    casual: frozenset[frozenset[str]]
    crystal_knows_raven_manipulation: bool
    # The known casual connection is established canon, but the precise
    # Cossette/Ibrahim CNM agreement terms have not been authored.
    cnm_terms_specified: bool

def relationship_view(world: WorldState, phase: str, *, through_event_id: str | None = None) -> RelationshipView:
    snapshot = world.as_of(phase, through_event_id=through_event_id)
    return RelationshipView(
        phase=phase,
        event_boundary=through_event_id,
        committed=frozenset(snapshot.bonds),
        casual=frozenset(snapshot.casual_connections),
        crystal_knows_raven_manipulation=snapshot.knows('Crystal','raven_manipulation',phase),
        cnm_terms_specified=False,  # contract gap; never infer from generic 'yes'
    )
