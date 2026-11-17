"""Conservative read-only bridge: shared commitments -> optional route eligibility.
Does not infer attraction, forgive misconduct, or authorize proposed pairings.
"""
from dataclasses import replace
from relationship_route_validator import StoryState, relationship_ready, PAIRS

def relationship_conflicts(world, pair: str) -> tuple[str, ...]:
    if pair not in PAIRS:
        return ('unsupported_ending_pair',)
    a,b=PAIRS[pair]
    blockers=[]
    for person,partner in ((a,b),(b,a)):
        active={next(iter(bond-{person})) for bond in world.bonds if person in bond and partner not in bond}
        if active and (person not in world.agreements or not active.union({partner}) <= world.agreements[person]):
            blockers.append(f'{person}:existing_commitment_without_cnm')
        if world.decisions.get((person,partner),(None,False))[1] is not True:
            blockers.append(f'{person}:no_independent_yes')
    return tuple(blockers)

def eligible_with_world(world, route_state: StoryState, pair: str) -> bool:
    """Both independent world decisions AND local narrative guards must pass.

    A world commitment is not required in advance (an eligible route may lead to it).
    """
    if world.pilot != route_state.player:
        return False
    return not relationship_conflicts(world,pair) and relationship_ready(route_state,pair)


def eligible_with_world_at(world, route_state: StoryState, pair: str, *, phase: str,
                           through_event_id: str | None = None) -> bool:
    """Evaluate existing local guards against *scene-time* global state.

    No future breakup, consent decision, or knowledge can affect this scene.
    Route-specific guard fields must themselves be captured at the scene time;
    this wrapper cannot guarantee that independently.
    """
    snapshot = world.as_of(phase, through_event_id=through_event_id)
    return eligible_with_world(snapshot, route_state, pair)
