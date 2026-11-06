# OMF 2107 — Lyra playable-campaign addition (v0.7)

**Date:** 2026-11-01 · **Status:** Working narrative-design proposal.

## Scope of this pass

For the first time, Lyra has a **dedicated six-chapter POV campaign**, not just optional scenes inserted into Ari's story. Added a 6,000+ word first-pass script, a detailed route/evidence spec, an executable story dispatcher, and thirteen automated tests under `09_Lyra_Campaign/`. The six existing Ari-focused Chapters v0.2 are unchanged; all original sources are retained.

| Chapter | Principal dramatic arc | Fights / branches |
|---|---|---|
| 1 — Someone Else's Spotlight | Gala celebrity vs athletic achievement; Dante and Steffan; Alex/Leena; neural consent | Choose public image and neural involvement |
| 2 — The Real Thing | Milano group fight; self-directed glamour photos; optional rooftop fanservice; secondary interactions | **Lyra vs Milano** actually playable |
| 3 — The Bad Question | Steffan qualifying fight; honest/complicated romance options; edited media leak; neural clue | **Lyra vs Steffan** actually playable; four relationship choices |
| 4 — More Than a Headline | Dynamic quarterfinal; independent machine logs; investigation; Kreissack-alive midpoint | **Q3 or Q4**, or third-place investigation route |
| 5 — The Name They Gave Her | Accidental coolant-wing emergency and Nova rescue; Varga exposure; Steffan accountability; authentic semifinal; voluntary publicity | **S_CD vs actual opponent**, or independent safety audit |
| 6 — No One's Trophy | Actual championship final if earned; Nova control reveal and independent boss; safety, consent and career choices; possible personal endings | **Final vs actual opponent** when qualified; Nova boss for all |

### Relationship routes and fanservice

- Dante: remain together, or (with future authoring and genuine mutual reconciliation) rebuild later.
- Steffan: clean breakup from Dante first or flawed early kiss/affair with accountability; **default separation after motive revealed**, not a mandatory reunion.
- Alex: possible *post-coverage* date only if adult/reciprocity/independent editorial recusal requirements are established; **proposal, not canon**.
- Solo: complete career, personal and mystery outcomes without romance.
- Ren, Plug, Leena, Cossette/Ibrahim, Shirro, fans: substantive friendly/professional secondary interactions, not merely dating targets.
- Glamour, photoshoots, dancing, kisses and optional implied intimacy are voluntary, adult, and never unlock main evidence, safety actions or victory.

### Verified by automated tests

- **13 new Lyra tests** including 32 simulated binary input sets.
- **7 existing tournament** and **15 existing relationship** tests retained; total **35 checks** when all suites run.
- Romance and neural flags cannot choose official match winners. Third-place and other lost-match paths still reach Nova legitimately.

### Outstanding decisions

1. **Canon authorization:** The user approved exploring romances and fanservice generally, not all individual new couples. Confirm whether Alex is an eventual mutual romance option and if either former partner deserves an alternate post-tournament reunion.
2. **Tournament:** Resolve three-way 1–1–1 group standings; replace placeholder NPC knockout winners with approved matchup logic.
3. **Production:** Flesh out optional interactive dialogue variants, confirm cast adult ages, stage coherent camera transitions and time the lengthy cinematic route; automated tests cannot validate character chemistry or final lore quality.
4. **Broader expansion:** Mara, Ren and Angel still need similarly complete pilot-POV campaigns. Preserve Lyra's selected-player-only deviations when building those routes.

**Reading order:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.1.md` → `Lyra_Route_Spec_v0.1.md` → validator/tests.
