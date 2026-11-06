# Relationship continuity audit v4.9

**Basis:** v4.8 active scripts and cross-campaign event-ledger code. This is a targeted contract repair and source-linked candidate inventory, **not** an exhaustive editorial certification.

## Confirmed defect fixed

**R-01 (high; corrected):** `13_Cross_Campaign_Audit/world_state.py` required **both** members of a couple to record rejection before allowing separation. That gave a current partner an unintended veto over a breakup. This contradicted Lyra's independent right to leave Dante or Steffan (and any other pilot's autonomy). Now the initiating partner must independently record a negative relationship decision; the other's agreement is not required. Newly formed relationships continue to require affirmative independent decisions from both parties. Five new focused tests cover the rule, including no repeated separation and no automatic new relationship.

## Additional integration gaps (not silently corrected)

**R-02 (high):** `relationship_route_validator.py` currently recognizes only five ending pairs (`Ari:Mara`, `Ari:Leena`, `Mara:Plug`, `Crystal:Raven`, `Lyra:Alex`). Established Dante–Lyra, Lyra–Steffan, Dante–Steffan elective branch, Jean-Paul–Varga, Ren–Angel, Milano–Selene, and Cossette–Ibrahim/Milano are **not** all represented by its ending dispatcher. Thus passing tests cannot establish full romance availability or continuity for them. Distinguish eligible *main ending* routes from ordinary relationship-state tracks before expanding the dispatcher.

**R-03 (high):** `WorldState` starts with empty `bonds`; it does not initialize the existing Dante–Lyra and Cossette–Ibrahim couples, despite their established canon. A full game bootstrap must explicitly seed initial relationships with grounded events rather than infer that lack of a bond means singleness. Avoid auto-spawning Cossette–Milano as a commitment: it is casual and covered by CNM.

**R-04 (medium-high):** `cnm_agreement` currently verifies prior generic positive `decision` events for named partners. This is not proof of informed agreement about non-monogamy boundaries. A runtime consent record should be **agreement-specific**, not reused from ordinary attraction/relationship decisions. The canon still does not specify Cossette–Ibrahim's negotiated terms; do not invent them. This contract is documented as incomplete, rather than assuming the existing gate fully represents informed consent.

**R-05 (medium):** World decisions are latest-value lookups while chronological events remain preserved. Cross-POV projections must read state *as of the scene*, rather than querying the final world snapshot and leaking subsequent separations or discoveries into earlier scenes.

**R-06 (medium):** Crystal's subjective non-recognition and Raven's deliberate manipulation need distinct facts. Her later awareness cannot be inferred from Raven's knowledge, relationship dissolution, or player choice. Existing Crystal romance guard requires disclosure and independent review; its connection to actual scene evidence remains unimplemented.

**R-07 (medium):** Additional romance proposals (e.g. Raven–Varga, Dante–Alex) remain proposals. Do not treat `Secondary_Romance_Expansion_v0.2.md` as overriding the newer Cossette–Milano casual-fling canon.

## Source-linked review inventory

`RELATIONSHIP_SCENE_CANDIDATES_v4.9.csv` has **567** candidate line matches from latest active campaign files. Entries are search hits, not verified contradictions. The next editorial pass should use each source line and nearby context to verify **who is present, what they know, relationship status at that time, mutual choices, professional restrictions, and later callbacks**, then edit confirmed contradictions rather than broad rewrites.

## Recommended next implementation

1. Author an initial-state seeding plan for two established couples, with independent event provenance and no retroactive state leakage.
2. Add scene-time projections for separation, intimate status, and knowledge states; preserve optional branch autonomy.
3. Replace generic CNM gate with agreement-scoped consent when agreed terms are specified, while leaving Cossette–Milano casual and Ibrahim–Cossette steady.

No NPC tournament outcomes, competitive results, or Day-13 rules changed.
