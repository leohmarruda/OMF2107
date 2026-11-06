# Cross-campaign audit module — v1.1

Read `Cross_Campaign_Continuity_Audit_v1.1.md` for findings, repairs, limitations and the priority list; `World_Event_and_Relationship_State_v1.1.md` for the proposed single-run state contract. Both separate approved story decisions from new editorial recommendations.

**Execute tests from project root:** `python -m unittest discover -s 13_Cross_Campaign_Audit -p 'test_*.py' -v`. Eight tests check 160 binary tournament inputs for five campaigns plus chronology, input adapters and active-romance exclusivity examples. Existing six suites must also pass.

**Honest boundary:** This is a partial integration audit, not a finished cross-campaign runtime. It does *not* establish that every romance has been independently consented to or that Ari's alternate screenplay scenes exist; unresolved items are recorded as open.

## v3.2 integration increment (new, not canonical tournament decisions)

`world_state.py` is an event-ledger prototype for **all twelve** selectable pilots. `test_world_state.py` validates ordering, decisive matches, relative clue-knowledge, mutual decisions, existing commitments, explicitly negotiated non-monogamy, and Nova finale placement. It does not replace campaign scripts or certify their continuity. The `World_Event_and_Relationship_State_v1.1.md` five-pilot list is superseded **for pilot scope only** by this implementation; its tournament and narrative caveats remain.

Critical limits: the ledger is in-memory, does not yet import route scenes or actual bracket outputs, does not enforce ages/capacity/professional recusals, and does not establish genuine consent merely because a Boolean was stored. Approved Cossette–Ibrahim CNM direction does not constitute approval of any particular Cossette–Milano outcome. Do not wire production saves to this prototype without a proper story scene/event authority layer.

## v4.8 casual connections

`WorldState` separately records casual connections and committed bonds; consensual non-monogamy coverage and independently recorded mutual decisions remain requirements for new casual event activation. The Cossette–Milano fling is author-established, while the precise negotiation events remain un-authored. See `test_cossette_relationship_v48.py`.
