# OMF 2107 — Ari campaign branch repair (Story Pack v1.2)

**Date:** November 1, 2026. **Editorial status:** Integrated draft and testable dispatcher; no new romance or public tournament rule automatically canonized.

## Main accomplishment

The existing Ari Chapters 1–6 now have revised **v0.3 active screenplay files** with honest qualifying losses, 0–2 elimination, 1–1–1 circular standings, dynamic QF/SF scenes and winner-exclusive championship/trophy scenes. The previous **v0.2 chapter files are preserved byte-for-byte** for comparison; earlier bibles, Lyra/Mara/Ren/Angel campaigns and archived audits remain intact.

New folder `14_Ari_Campaign/` contains an alternate scene bank, route specification, a script-level dispatcher and tests. Ari may be eliminated and continue to investigate WAR, learn about Kreissack, and enter the separate, consent/safety-gated Nova emergency without magically reentering the sports bracket.

## The four group outcomes

| Ari vs Selene | Ari vs Crystal | Outcome |
|---|---|---|
| W | L | 2nd, vs Mara in QF |
| W | W | 1st, vs Ren in QF |
| L | W | 2nd on provisional circular seed; vs Mara in QF |
| L | L | 3rd, no QF; playable archive investigation |

**No fights end in a draw.** Three-way equal win totals still need a public ranking rule; the simulator's seed is provisional and prominently marked as such.

## Finale and romance changes

- If Ari reaches the final: an actual playable match against the real other semifinalist; win and loss have different cinematic outcomes.
- If Ari has been eliminated: two NPC finalists fight; the championship and trophy go only to the verified winner, using a provisional outcome if the NPC pairing is not yet authored.
- Ari's possible romance with Mara, future Leena romance, or solo/friendship route remains independent of tournament outcome, with genuine reciprocal choice, journalistic recusal and adult eligibility requirements.
- The Nova boss follows the real final, and its emergency equipment/access rationale is explicitly independent of official tournament qualification.

## Validation and residual gaps

**117/117 project tests pass** (107 prior plus 10 Ari dispatcher tests), including all 32 Ari fight-input combinations. Static editing and model tests are not a complete five-POV animatic or full global save-state implementation.

Remaining decisions: final public circular group-ranking rule; explicitly authored NPC knockout upsets and final winner scenarios; master hourly scene/availability ledger; global NPC consent and relationship graph hookup; detailed alternate opponent dialogue/personal endings and emergency access logistics. Exact revised dialogue remains subject to creative review.

**Reading order:** `14_Ari_Campaign/Ari_Route_Spec_v0.1.md` → `14_Ari_Campaign/Ari_Alternate_Scenes_v0.1.md` → six `04_Screenplay_Reconstructions/Chapter_*_v0.3.md`.
