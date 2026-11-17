"""Conservative cross-campaign event ledger. Not an endorsement of proposed canon.

Events are validated and applied atomically. Multiple campaign playthroughs are
alternative histories; never merge their ledgers into one save.
"""
from dataclasses import dataclass, field
from typing import Optional

PILOTS = frozenset(('Ari','Lyra','Mara','Ren','Angel','Crystal','Raven','Jean-Paul','Steffan','Dante','Selene','Milano'))
PHASES = ('day0_1','group_stage','quarterfinals','day9_reveal','day11_ab_semifinal',
          'day11_protected_disclosure','day12_rescue','day12_cd_semifinal',
          'day13_final','day13_nova_reveal','day13_special_nova',
          'day30_devroe_authentication','epilogue')
PHASE_INDEX = {p:i for i,p in enumerate(PHASES)}

# Established pre-game statuses; these are not evidence of any particular
# negotiation, exclusivity rule, or subsequent branch outcome.
BASELINE_BONDS = frozenset((frozenset(('Dante','Lyra')), frozenset(('Cossette','Ibrahim'))))
BASELINE_CASUAL = frozenset((frozenset(('Cossette','Milano')),))
BASELINE_SOURCE = 'author_relationship_canon_v4.7_v4.8'


class StateConflict(ValueError):
    pass

@dataclass(frozen=True)
class Event:
    event_id: str
    kind: str
    phase: str
    actor: str = ''
    target: str = ''
    payload: tuple = ()

@dataclass
class WorldState:
    pilot: str
    events: list[Event] = field(default_factory=list)
    matches: dict = field(default_factory=dict)
    knowledge: dict = field(default_factory=dict)  # (person, clue) -> (phase, source)
    bonds: set = field(default_factory=set)
    casual_connections: set = field(default_factory=set)  # noncommittal ties, separate from committed bonds
    agreements: dict = field(default_factory=dict)  # person -> set of explicitly consenting active partners
    decisions: dict = field(default_factory=dict)  # (person, partner) -> (phase, yes/no)

    def __post_init__(self):
        if self.pilot not in PILOTS:
            raise StateConflict('unsupported selected pilot')

    def apply(self, e: Event):
        if not e.event_id or any(x.event_id == e.event_id for x in self.events):
            raise StateConflict('empty or duplicate event ID')
        if e.phase not in PHASE_INDEX:
            raise StateConflict('unknown phase')
        if self.events and PHASE_INDEX[e.phase] < PHASE_INDEX[self.events[-1].phase]:
            raise StateConflict('events must be chronological')
        if e.kind in ('baseline_bond', 'baseline_casual'):
            pair = frozenset((e.actor,e.target))
            permitted = BASELINE_BONDS if e.kind == 'baseline_bond' else BASELINE_CASUAL
            if (e.phase != 'day0_1' or len(pair) != 2 or pair not in permitted
                    or e.payload != (BASELINE_SOURCE,) or self.events):
                # Baseline events must be added by bootstrap at the start of
                # a save; the bootstrap function uses a private initialization
                # window below to allow more than one baseline event.
                if not (e.phase == 'day0_1' and len(pair)==2 and pair in permitted
                        and e.payload == (BASELINE_SOURCE,)
                        and all(x.kind.startswith('baseline_') for x in self.events)):
                    raise StateConflict('invalid or late canonical baseline')
            coll = self.bonds if e.kind == 'baseline_bond' else self.casual_connections
            if pair in coll: raise StateConflict('duplicate baseline relationship')
            coll.add(pair)
        elif e.kind == 'match':
            if len(e.payload) != 3: raise StateConflict('match needs left, right, winner')
            left,right,winner = e.payload
            if left == right or winner not in (left,right) or e.target in self.matches or not e.target:
                raise StateConflict('invalid or duplicate decisive match')
            if e.target == 'FINAL' and e.phase != 'day13_final':
                raise StateConflict('official final must occur day 13')
            if e.target == 'SPECIAL_NOVA':
                raise StateConflict('special Nova boss cannot be an official match')
            self.matches[e.target] = e.payload
        elif e.kind == 'clue':
            if not e.actor or not e.target or not e.payload or not e.payload[0]:
                raise StateConflict('clue requires knower, clue and source')
            key = (e.actor,e.target)
            if key in self.knowledge: raise StateConflict('knowledge already acquired')
            minimum = {'kreissack_alive':'day9_reveal', 'nova_rescue':'day12_rescue',
                       'nova_executive_veto':'day13_nova_reveal',
                       'devroe_e5_order':'day30_devroe_authentication'}
            if e.target in minimum and PHASE_INDEX[e.phase] < PHASE_INDEX[minimum[e.target]]:
                raise StateConflict('clue learned before earliest permitted phase')
            self.knowledge[key] = (e.phase,e.payload[0])
        elif e.kind == 'decision':
            if not e.actor or not e.target or type(e.payload[0] if e.payload else None) is not bool:
                raise StateConflict('requires an independently recorded yes/no decision')
            self.decisions[(e.actor,e.target)] = (e.phase,e.payload[0])
        elif e.kind == 'cnm_agreement':
            # Explicit, person-specific consent: this does not itself create a relationship.
            if not e.actor or not e.payload or not isinstance(e.payload[0],tuple):
                raise StateConflict('CNM requires explicit partner coverage')
            partners = set(e.payload[0])
            if not partners or e.actor in partners or not all(self.decisions.get((p,e.actor),(None,False))[1] for p in partners):
                raise StateConflict('CNM requires partner independent agreement')
            self.agreements[e.actor] = partners
        elif e.kind == 'casual_connection':
            # An established casual involvement is not a second commitment.
            if not e.actor or not e.target or e.actor == e.target:
                raise StateConflict('invalid casual connection')
            pair = frozenset((e.actor,e.target))
            if pair in self.casual_connections:
                raise StateConflict('duplicate casual connection')
            if not all(self.decisions.get((p,q),(None,False))[1] for p,q in ((e.actor,e.target),(e.target,e.actor))):
                raise StateConflict('casual connection requires independently recorded mutual decisions')
            for p,q in ((e.actor,e.target),(e.target,e.actor)):
                existing = {next(iter(b-{p})) for b in self.bonds if p in b and q not in b}
                if existing and (p not in self.agreements or not existing.union({q}) <= self.agreements[p]):
                    raise StateConflict('existing committed bond requires partner-covered CNM agreement')
            self.casual_connections.add(pair)
        elif e.kind == 'end_casual_connection':
            pair = frozenset((e.actor,e.target))
            if pair not in self.casual_connections:
                raise StateConflict('casual connection not active')
            self.casual_connections.remove(pair)
        elif e.kind == 'commit':
            if not e.actor or not e.target or e.actor == e.target:
                raise StateConflict('invalid relationship')
            pair = frozenset((e.actor,e.target))
            if pair in self.bonds: raise StateConflict('already committed')
            if not all(self.decisions.get((p,q),(None,False))[1] for p,q in ((e.actor,e.target),(e.target,e.actor))):
                raise StateConflict('mutual affirmative decisions required')
            for p,q in ((e.actor,e.target),(e.target,e.actor)):
                existing = {next(iter(b-{p})) for b in self.bonds if p in b}
                if existing and (p not in self.agreements or not existing.union({q}) <= self.agreements[p]):
                    raise StateConflict('existing commitment requires explicitly negotiated CNM')
            self.bonds.add(pair)
        elif e.kind == 'separate':
            pair = frozenset((e.actor,e.target))
            # Ending a relationship is a unilateral right; the other partner need
            # not agree. Only the initiating person's decision must be recorded.
            # This is distinct from beginning or expanding a relationship, which
            # requires independently affirmative choices and applicable agreements.
            if pair not in self.bonds or not e.actor or not e.target or e.actor == e.target:
                raise StateConflict('separation requires an existing committed relationship')
            if self.decisions.get((e.actor,e.target),(None,None))[1] is not False:
                raise StateConflict('separation requires initiating partner recorded no')
            self.bonds.remove(pair)
        elif e.kind == 'story':
            if e.target == 'nova_rescue' and e.phase != 'day12_rescue':
                raise StateConflict('Nova rescue must precede CD semifinal')
            if e.target == 'nova_boss' and (e.phase != 'day13_special_nova' or 'FINAL' not in self.matches):
                raise StateConflict('Nova boss follows completed official final')
        else:
            raise StateConflict('unrecognized event kind')
        self.events.append(e)

    def as_of(self, phase: str, *, through_event_id: Optional[str] = None) -> 'WorldState':
        """Reconstruct a nonmutating snapshot, without future-event leakage.

        `through_event_id` is inclusive and useful for scenes in the same phase.
        If omitted, all events of that phase are included; scene-level callers
        must supply the last completed event ID for precise ordering.
        """
        if phase not in PHASE_INDEX: raise StateConflict('unknown phase')
        if through_event_id is not None and not any(e.event_id == through_event_id for e in self.events):
            raise StateConflict('unknown scene event boundary')
        cutoff = PHASE_INDEX[phase]
        snapshot = WorldState(self.pilot)
        reached = False
        for e in self.events:
            if PHASE_INDEX[e.phase] > cutoff: break
            snapshot.apply(e)
            if e.event_id == through_event_id:
                reached = True
                break
        if through_event_id is not None and not reached:
            raise StateConflict('event boundary later than requested phase')
        return snapshot

    def knows(self, person: str, clue: str, at_phase: str) -> bool:
        if at_phase not in PHASE_INDEX: raise StateConflict('unknown phase')
        recorded = self.knowledge.get((person,clue))
        return bool(recorded and PHASE_INDEX[recorded[0]] <= PHASE_INDEX[at_phase])
