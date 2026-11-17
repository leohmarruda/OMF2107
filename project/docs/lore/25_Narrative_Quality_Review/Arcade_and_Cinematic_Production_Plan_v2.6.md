# OMF 2107 — Narrative production plan: Cinematic and Arcade modes v2.6

**Status:** A scope and rehearsal plan, not promised runtime or a new canon choice. Assumes fights themselves remain the principal gameplay loop; actual cutscene durations require reads and animatic testing.

## Mode contracts

| Mode | Narrative footprint *proposed* | Mandatory content | Optional / skippable |
|---|---|---|---|
| **Arcade** | ~12–20 minutes *of non-combat narrative* per pilot, to validate against cost | 45–75 s opening; 1–2 rival scenes; 1 distinctive personal stake; 1 world revelation as short recap; ~2 min own ending | Long dossiers, romantic interludes, detailed Nova interrogation, most investigation and full ensemble cutaways |
| **Cinematic** | ~45–75 minutes *of non-combat narrative* per pilot before optional scenes, to validate | Three protagonist-specific decisions with visible later consequences; meaningful relationships or friendships; distinct action/access route to finale | Adult romantic/fanservice variants, extra evidence context, additional secondary-character bonds |

These are *targets to test*, not estimates measured from the current scripts. 12 fully bespoke movie-length paths would be prohibitively expensive; prefer cinematic shared assets + character-specific pivots.

## Three-gate development plan

**Gate A — consolidate narrative authority (P0):** approve circular ranking procedure, define 12-vs-12 fallback NPC outcome mapping (or authored matchup outcomes on demand), implement one save state, and register active script files. Add global graph invariants. **Acceptance:** simulated state replay deterministically yields one champion and no impossible NPC romance across *all protagonist selections*.

**Gate B — vertical slice for quality:** choose **Dante** (complex emotional branching), **Mara** (loss and financial consequences), and **Angel** (evidence/limited visibility) as complementary tests. For each, fully script: opening voice beat, two fights, group-eliminated path, one choice consequence, shared rescue cutaway, distinct boss access, one nonromantic ending, one eligible romance branch. **Acceptance:** blind readers identify speaker and stakes without character labels in ≥ most sampled exchanges; test-team reports no unearned knowledge or NPC behavior. Do not pretend this qualitative criterion is automated.

**Gate C — extend and compress:** after the slice, standardize scene cards / localization keys, use proven shared assets, compress all 12 into Arcade Mode, and produce 12 complete consequence matrices. **Acceptance:** 12 playable campaigns have unique character goal/reversal/ending; no mandatory scene implies an unearned opponent or romance, and the Nova finale has one consistent physical history.

## Scene-specific editing brief

- **Ari:** dramatize a cost to publishing Ganymede evidence; keep his ideological arc distinct from Crystal's reform arc.
- **Mara:** show an explicit invoice/plan variation after elimination instead of only an end-card declaration.
- **Lyra:** mandatory athletic celebration or humour unrelated to dating in Act I; maintain fans as characters with agency.
- **Ren:** distinct observable scene per neural choice rather than three explanations of the same clue.
- **Angel:** successful anonymity route must retain an emotionally satisfying personal ending, not a punishment for privacy.
- **Crystal:** include a public leadership decision independent of her confrontation with Raven; maintain consent distinctions.
- **Raven:** require a consequence of deliberate concealment even if Crystal later consents to private dominance.
- **Jean-Paul:** protect witnesses at a concrete cost to his cover; keep Varga's research abuse factual.
- **Steffan:** show Pyros engineering brilliance during a specific tactical problem, separate from romantic manipulation.
- **Dante:** support default nonromantic response with positive nonromantic final closure; do not require exploration to obtain emotional resolution.
- **Selene:** distinct supplier-focused choice effect; court filings, reputation or lost access actually change.
- **Milano:** a named independent observer loses/gains protection depending on board choices; physical proof does not evaporate.

## Minimal QA matrix to build

For each selected pilot: (1) group 0–2, circular 1–1–1 if possible, and 2–0; (2) first knockout loss and official championship win where earned; (3) no romance, reciprocal romance, romance rejected, and exclusive conflict; (4) one moral dark path; (5) early evidence refusal with fallback; (6) Day-11/12/13/30 knowledge consistency; (7) physical access to rescue and core; (8) one nonromantic emotional ending.

Do not multiply every condition into a brute-force storyboard. Pairwise coverage plus authored risk paths gives a tractable first playtest; reserve exhaustive simulations for pure finite-state rules.

**Do not begin a full Arcade cut until Gate A and at least one Gate B pilot read-through.** Compression before testing would preserve existing pacing and causality problems in smaller form.
