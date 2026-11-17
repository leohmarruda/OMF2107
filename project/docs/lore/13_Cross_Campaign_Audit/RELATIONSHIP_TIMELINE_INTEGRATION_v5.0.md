# Relationship-state timeline integration — v5.0

## Implemented and tested

- `new_canonical_world(pilot)` creates a **separate save state for each of the twelve playable campaigns** with three author-established starting statuses: Dante–Lyra committed, Cossette–Ibrahim committed, and Cossette–Milano casual. The casual connection is **not** added to the committed-bond set.
- Baselines are provenance-tagged and loaded at the start of the story, not re-created as fictional on-screen consent decisions. They encode existing statuses, **not** an account of the underlying CNM negotiations.
- `WorldState.as_of(phase, through_event_id=...)` replays events into a fresh state through an inclusive event boundary. Use an event boundary for two scenes sharing a phase; querying by phase alone includes every event in that phase.
- `relationship_view(...)` reports committed/casual statuses and Crystal's knowledge independently. Crystal does **not** recognize Raven's manipulation by default; her later awareness requires a recorded `clue` acquired by Crystal from a source.
- `eligible_with_world_at` allows the existing optional ending validator to consult scene-time world state, rather than the save's final state. Its local `route_state` must itself be time-correct.
- Unilateral separation, mutual formation, non-exclusive casual connections, and the two different campaign histories are preserved.

## Incomplete boundaries

- **Do not represent the precise Cossette–Ibrahim CNM agreement terms as known.** Their existence as an established consensual non-monogamous relationship is canon; the exact terms, consent history, and limits have not been authored. The pre-existing `cnm_agreement` event is a **legacy, coarse validator** and cannot by itself establish that detailed boundaries were negotiated. `cnm_terms_specified` remains false in the scene view pending an agreement-scoped contract.
- This is a world-state/bootstrap/projection integration, **not** a sweep that has edited 567 candidate scene references. Do not claim the active scripts already consume these APIs. Production game bootstrap and dialogue dispatch must call them.
- A baseline records current relationship status, not guaranteed exclusivity, a legal status, an intimacy scene, or knowledge by unrelated characters.
- The `raven_manipulation` clue indicates *Crystal's evidenced awareness*, not a claim that Raven's exploitation began at the exact instant the clue was recorded. Existing romance gates requiring accountability still apply.
- Same-phase boundaries use an event ID; a production scene layer must define and save the appropriate last event for the viewpoint.
- Historical source versions remain for provenance; the v4.7/v4.8 author canon overrides conflicting older proposals.

## Next steps

1. Define structured agreement-scoped permissions and revocations for CNM instead of using generic romantic `decision` events.
2. Wire `new_canonical_world` into the runtime per pilot and use as-of snapshots for specific cross-POV scenes.
3. Review the highest-confidence of 567 relationship candidate references and edit actual contradictions in active scripts; regenerate scene indices after any screenplay edits.
