# Relationship-state integration — first pass v4.6

The historical `relationship_route_validator.py` and `13_Cross_Campaign_Audit/world_state.py` are **separate partial validators**. `relationship_world_bridge.py` adds an opt-in conservative bridge: even when a local route declares attraction, both parties must have independently recorded affirmative choices; existing commitments require an explicit CNM agreement before additional bonds. The bridge does **not** assert any romance in canon or make previously unsupported pairings playable.

Important open issues for next pass:
1. The bridge is read-only and is not wired into screenplay runtime.
2. Supporting relationships (Cossette–Ibrahim, potential Cossette–Milano) are not defined by `PAIRS` and must not be coerced into player ending slots.
3. Existing `world_state` has no fully modeled relationship breakup/reconciliation and consent-revocation lifecycle; run state-transition tests before claiming complete CNM handling.
4. Event-level relationship changes still need shared-POV scene and timestamp binding, especially Dante–Steffan–Lyra, Crystal–Raven, and Cossette–Ibrahim.
5. The existing route model assumes exclusive `commitments`, unlike conditional CNM world state. Do not merge the two commitment representations naively.

Immediate next editorial pass: reconcile named relationship events and scene prerequisites against the unified ledger; retain author-established defaults and optionality.
