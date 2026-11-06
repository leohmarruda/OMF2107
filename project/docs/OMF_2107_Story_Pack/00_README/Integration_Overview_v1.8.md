# OMF 2107 — v1.8 integration overview: Kreissack's character and Nova

**Date:** 2026-11-02  
**Focus:** Deepen Kreissack's motivations, relationship with Nova and finale, without converting the human Devroe murders into a Nova conspiracy or permitting an early revelation.

## What was written

1. **Character and Nova bible:** `02_Story_Bibles/Kreissack_Character_and_Nova_Arc_v1.8.md` provides motives, a 2092–2107 timeline, psychological arc, relationships, voice guidance, knowledge locks, and physical finale constraints.
2. **Eight optional cinematic scenes, K0–K7:** `19_Kreissack_Arc/Kreissack_Scene_Packet_v1.8.md`: the documented assassination order (post-E5 flashback), biological recovery, retrospective proof of covert veto, genuine rescue aftermath, last pre-activation bargain, first unmistakable rejected order, original hardwired safety-path choice, and Day-30 postscript.
3. **Active Ari finale script:** `04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.4.md` embeds K4 and K5 as shared cutaways. All other Ari chapters remain v0.3; Ari Ch6 v0.3 is preserved unchanged as the prior snapshot. These scenes have **no default-Ari-winner assumption** and cannot alter official match outcomes.
4. **Master Bible v2.4:** Adds section 10A to the v2.3 canon reconciliation while leaving v2.3 intact.
5. **Scene-availability contract:** `19_Kreissack_Arc/kreissack_arc_state.py` and 13 tests gate K0–K7 by chronology, knowledge and mechanism. Test cases cover seven selected pilots, no early E5, correct rescue/revelation sequencing, and the separate G/B→L/E/D finale machinery.
6. **Provenance:** This overview, source-level author-decision note in `Decision_Log.md`, and README/manifest/checksums updated.

## Locked story constraints preserved

- **Human responsibility:** Kreissack personally ordered the 2092 Devroe assassination. Raven was *not* briefed on the hidden lethal clause but independently suppressed distress access, ignored the restoration request and covered up his role. The sabotage directly caused the fatal shuttle deviation; restoring distress communications is **not proven** to have saved anyone.
- **No anachronistic Nova:** The composite AI did not make the 2092 killing decision. The later covert override is genuine but cannot retroactively excuse pre-integration crimes.
- **Revelation separation:** Biological survival becomes discoverable in Act III; the Day-12 rescue has no matched biological initiation but is genuinely lifesaving; composite executive control is explicitly understood Day 13; E5 names Kreissack as assassin principal only Day 30, after the default sacrifice.
- **Composite, not a puppet:** Kreissack's memories, personality and consciousness persist. His ordinary judgments are authentic, although his high-level incompatible choices are covertly diverted. No invented universal memory rewriting or mind control of other pilots.
- **Physics of the default ending:** The Nova boss fight damages neural executive gateway G. Kreissack uses surviving independent biological safety path B→L to retain the unique core once D is irreversible; E cannot complete. Destroyed Nova has no fully synchronized offsite copy. The rescue safety gateway is not an escape route.
- **Agency and ethics:** The rescue does not vindicate coercive integration, and the final sacrifice does not cancel the murders. Crystal and Christian's views remain theirs. Independent evidence does not depend on Raven's confession or on any romance.

## Integration scope (important)

- **Directly integrated:** K4/K5 in Ari Chapter 6 v0.4 and the new section in the master bible.
- **Available as optional inserts, NOT yet embedded across every POV:** K0/K1/K2/K3/K6/K7. Existing Day-12 rescue and Day-13 final core-interlock scenes remain active; their optional expanded scene cards must not be replayed as duplicate events.
- **Other playable campaigns (Lyra, Mara, Ren, Angel, Crystal, Raven):** Their existing complete drafts are unchanged. Their shared Day-13 finale can reference K4/K5 when next editing their scripts; scene gate tests alone are *not* full cinematics integration.
- **Independent Christian subplot:** E5 chronology and existing Day-30 scene remain active; K0/K7 are optional postscript embellishments, not a second contradictory hearing.

## Editorial risks and further decisions

- **Potential overexplanation:** K2 (2105 hindsight) works best as an optional unlocked replay; mandatory deployment would spoil the composite mystery in retrospect and slow pacing.
- **Kreissack's humanization:** His rational concern for technicians or brief contemplation of the Day-12 rescue adds complexity, not repentance. Avoid using these moments to soften his willful 2092 violence.
- **Proposed E5 escrow mechanism:** Remains a worldbuilding proposal, not a verified legal procedure; no new pre-Day-30 authorization proof has been added.
- **Canon boundaries:** Only the user's specified core decisions are locked. Precise dialogue, body-language cues, technical labels, Haldane's earlier exchanges and the 2092 reconstructed words are proposals pending review.
- **Unfinished production tasks:** Bind shared cutaways to the six non-Ari playable campaigns; resolve the tournament's provisional circular group ordering and unauthored NPC fight outcomes; test full cinematic pacing rather than relying on unit tests.

## Automated validation

`python -m pytest -q` from archive root: **182 passing tests across 13 suites** (169 prior + 13 new), with 76 existing unittest subtests. This covers code-level guards; it is *not* a proof of screenplay quality or fully integrated runtime state.
