# Mara's playable POV campaign (v0.8)

A first-pass six-chapter screenplay for Mara Voss, set against the same tournament and conspiracy as the v0.7 Lyra route and v0.6 Ari script. Her story is built around independent family-care decision-making, contractual/financial independence, physical safety investigation, honest fighting, and elective Ari/Plug/Raven/solo personal outcomes. No prior Ari/Lyra manuscript is overwritten.

1. `Mara_Playable_Screenplay_v0.1.md` — full narrative, branching scene IDs, dialogue, optional adult fanservice.
2. `Mara_Route_Spec_v0.1.md` — integration contract and unresolved questions.
3. `mara_route_validator.py` — testable narrator dispatcher that reads existing tournament results, does not edit them.
4. `test_mara_route_validator.py` — 16 test cases including all 32 binary fight-result patterns.

`simulate_mara(raven_win, ren_win, knockout_wins, choices)` accepts the order **Raven then Ren** as shown on screen; the underlying tournament engine accepts `Ren then Raven`. Always bind your UI to match IDs `GB2` and `GB1` to avoid an inverted win result.

**Status:** All romantic options other than the existing default Ari/Mara relationship are design proposals, not approved canon. Plug's adult eligibility and reciprocal preference must be verified before romantic scenes are enabled. Raven's existing history with Crystal is protected by guards. Financial numbers and medical circumstances remain intentionally unquantified. Neither the prose nor tests verify production implementation.
