# OMF 2107 — NPC-only knockout outcome audit v3.9

**Authority:** Editorial diagnosis and workflow only. **No previously unapproved winner is canonized.** In particular, the author's approval of deterministic authored match results is NOT approval of the proposed match winner table.

## Actual findings

The current `npc_pair_proposals.py` enumerates 66 unordered pairs of 12 pilots. Comparison to the historical fallback `NPC_KNOCKOUT_PRIORITY` shows:

- **7** established exact-pair cinematic outcomes, already canonical as **default bracket** results. None contradicts the proposal table.
- **51** additional proposed winners obtained by simply choosing the higher fighter in the old global priority ordering. This is the *opposite* of genuine independent matchup authorship. Their individual results should not be approved just to make strict simulations pass.
- **8** proposed winners that *depart* from that priority ordering. These are potentially interesting specific upsets, but no justification is attached to the existing proposal data. The eight review questions below describe plausible issues to investigate, **not factual fight outcomes**.

| Proposed winner | Opponent | Editorial question, not established tactical justification |
|---|---|---|
| Crystal | Lyra | Does Jaguar have a credible answer to Electra's mobility and control? |
| Mara | Steffan | Can Flail defeat Pyros through an established tactical interaction? |
| Raven | Steffan | Can Katana overcome Steffan's exceptional engineering and adaptation? |
| Selene | Mara | Can Mirage create a credible opening against Flail? |
| Ren | Angel | Does Helix have an established defense or counter to Chronos? |
| Milano | Angel | What lets Gargoyle beat Chronos without an arbitrary immunity? |
| Dante | Ren | Can Shredder exploit a recognizable Helix limitation? |
| Jean-Paul | Selene | How can Shadow outmaneuver Mirage when both exploit deception? |

### Simulation coverage is not reachability proof

The 384 raw tuples from v3.6 encode one selectable fighter's two group results and at most three knockout results. They do **not** enumerate every NPC group-stage upset, nor actual score-based group rankings. When sampled with the existing provisional seeds and proposed outcomes, only **21** unordered pairs occur as NPC-only knockout fights; **45** are unobserved in this particular test space. Do not interpret that as 45 unreachable pairs. The CSV marks these as conditional observations; raw sample counts are *not probabilities*.

### Relevant source references

- `02_Story_Bibles/Character_Bible_v1.0.md` — pilot archetypes and signature HARs.
- `02_Story_Bibles/Steffan_Character_Addendum_v2.3.md` — Steffan's engineering talent and character constraints.
- `07_Tournament_Model/tournament_validator.py` — canonical exact-pair default fights and provisional priority.
- `07_Tournament_Model/npc_pair_proposals.py` — unapproved suggestions.
- Individual active campaign scripts — must supply any actual matchup-specific combat evidence and outcome-dependent consequences.

## Decision and integration workflow

1. **Preserve the seven default exact-pair winners.** They are reference-cinematic facts, not universal fixtures for player-controlled fights.
2. **For each newly reachable NPC-only matchup**, author an explicit tactical setup, battle outcome and plausible cinematic consequence; cite the source or record a new author decision. Favor character- and machine-specific reasons over the old global rank.
3. Record approval **per pairing**, not per entire 66-row table. A proposed result without an approved rationale stays pending.
4. Add only approved pairings to the validator's `npc_knockout_winners` input (or to a future approved-only registry). Strict mode should continue to reject gaps; never enable `use_proposed_npc` as a production shortcut.
5. After score semantics and a three-way equality procedure are settled, resimulate a **wider group-result/score space** before claiming all reachable pairings covered. Test side assignment, player overrides, and nondefault dialogue/epilogues together.

## Production blockers unchanged

The 166 tournament-keyword references still lack exhaustive human scene-by-scene verification; opponent-specific dialogue remains incomplete; the runtime does not yet consume all bracket bindings. **This release does not claim to fix those issues.**
