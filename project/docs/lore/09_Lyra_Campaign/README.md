# Lyra Playable Campaign — v0.7 addition

First non-Ari playable POV expansion. **Status: editorial proposal, not automatically canon**. Does not replace six Ari POV screenplays in `04_Screenplay_Reconstructions`.

- `Lyra_Playable_Screenplay_v0.1.md` — six drafted chapters, conditional dialogue, match blocks, optional romance and fanservice, climax and epilogues.
- `Lyra_Route_Spec_v0.1.md` — canonical boundaries, branch table, evidence graph, ethics, remaining decisions and implementation steps.
- `lyra_route_validator.py` — story-scene selection driven by existing tournament model; romance guard independent of match outcomes.
- `test_lyra_route_validator.py` — 13 route tests (32 fight-input patterns plus focused guards).

**Run:** `python -m unittest discover -s 09_Lyra_Campaign -v` from archive root. Also run the earlier `07_Tournament_Model` and `08_Relationship_Model` suites. The tests are only logic checks, not an enacted game or scene-by-scene quality evaluation.

**Source precedence:** Selected-Lyra route is an overlay on global events; the earlier selected-Ari default screenplays and already approved lore stay controlling on common events. Exact proposed alternative outcomes involving Dante, Steffan and Alex require user review. Circular group rankings and nondefault NPC winners still use provisional tournament fallbacks.
