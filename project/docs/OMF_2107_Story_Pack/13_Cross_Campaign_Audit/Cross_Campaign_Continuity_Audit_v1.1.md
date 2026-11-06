# One Must Fall 2107 — Cross-campaign continuity audit v1.1

**Date:** 2026-11-01  
**Baseline:** Story Pack v1.0 (Ari v0.2; Lyra, Mara, Ren, Angel v0.1).  
**Scope:** Five selected-pilot campaigns; tournament results, shared calendar, knowledge progression, NPC agency, romance and optional fanservice, finale and ending validity.  
**Status:** Partial repairs incorporated in v1.1; unresolved items explicitly not claimed fixed. No new romantic pairing or character backstory is thereby made canon.

## Executive finding

**Overall: conditional pass for a draft multi-POV project; not yet production-ready.** The tournament engine itself is deterministic and decisive; the five POVs can describe alternative histories of **one save file per selected fighter**. The biggest remaining risk is the gap between executable route models and actual prose/scene flags, particularly in Ari's legacy screenplay. Narrative clues remain accessible in nonromantic and early-elimination playthroughs in the current dispatcher models. Automated checks are necessary but cannot establish screenplay coherence or NPC consent at runtime.

## Findings by priority

| ID | Severity | Evidence (source / scene) | Diagnosis | v1.1 disposition |
|---|---|---|---|---|
| C01 | **Major** | `12_Angel_Campaign/Angel_Playable_Screenplay_v0.1.md` Ch2–6 originally labeled Days 2–6; `04_Screenplay_Reconstructions/Chapter_05_Fractures_v0.2.md` first semifinal Day 11, rescue Day 12, second semifinal Day 12; Ch6 final Day 13 | Angel's QF, rescue and final cannot occur days before the same shared events in other campaigns | **Repaired in Angel Ch2–6 headings**: Days 3–4, Day 5, Days 8–10, Days 11–12, Day 13; scene-specific rescue/SF date added |
| C02 | **Major** | Ren `R5.1` rescue preceded `R5.3` `S_AB`; Mara `M5.0` rescue preceded `M5.3` `S_AB`. Original Ari Ch5 has `S_AB` Day 11 before the rescue Day 12 | Both campaigns reversed the first semifinal relative to the Nova rescue | **Repaired:** moved Day-11 S_AB (or honest elimination broadcast) before Day-12 rescue in Mara/Ren prose and scene dispatchers; stable scene IDs intentionally remain nonnumerical in display order |
| C03 | **Major** | `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.1.md` L2 Milano, L3 Steffan; engine's `simulate('Lyra',...)` inputs vs Steffan, then Milano; `lyra_route_validator.py` previous API consumed engine order | Game UI could attribute a win against Milano to a win against Steffan, producing wrong rank and bracket while all bouts remain decisive | **Repaired at entry boundary:** added `simulate_lyra_screen(milano_win, steffan_win, ...)` while retaining original engine API for compatibility. Added specific tests |
| C04 | **Major / still open** | `04_Screenplay_Reconstructions/Chapter_01_Anniversary_v0.2.md` Fight Ari–Selene default win; `Chapter_03_Trouble_With_Attraction_v0.2.md` draws bracket chiefly from Ari wins Selene; `07_Tournament_Model` permits Ari group 0–2 | Ari's possible loss to Selene / third-place group finish has insufficient mandatory narration and early-elimination gameplay despite engine support | **Open.** Author C1 loss and 0–2/1–1 standing scenes and a no-QF investigation route. The new cross-run adapter correctly interprets screen order, but cannot write the missing scenes |
| C05 | **Major / still open** | Ari Ch6 Scene 3 assumes Ari–Lyra final and Ari winner; Scene 4 assumes Ari trophy. The v0.2 branch notes warn to vary this, but default narration remains unconditional text | If Ari loses a prior knockout, loses the final, or faces a different finalist, the cinematic would announce a false winner unless production suppresses/replaces Scenes 3–4 | **Open.** Convert Scene 3/4 into explicit bracket-driven variants and champion-dependent award scene before shipping |
| C06 | **Major / model added, integration open** | `11_Ren_Campaign` Ren–Angel/Tessa, `12_Angel_Campaign` Angel–Ren/Crystal/Leena, `10_Mara_Campaign` Mara–Ari/Plug/Raven, `09_Lyra_Campaign` Lyra–Dante/Steffan/Alex; each local code uses separate permissive Boolean flags | Different POVs can potentially contradict an NPC's existing exclusive commitment, date/recusal, or romantic decision if global current state is not consulted | **Partially addressed:** new *single graph* checker `resolve_ending` rejects conflicting active pairings and requires an independently **verified** separation to free one. Production still must connect real scene-choice evidence and NPC approvals; a Boolean naming `*_commitment_cleared` alone is not proof |
| C07 | **Moderate / still open** | Ari Ch5 first semifinal Day 11; other campaigns write a compressed 6-chapter, 13-day outline; matches `GB1` etc. are numbered by engine not by screen order | No unified per-hour schedule or source-of-truth event dispatcher for simultaneous NPC scenes; cross-campaign scene ID ordering is now repaired only for known hard contradictions | **Open:** author a master scene clock/availability ledger before full screenplay merge. `World_Event_and_Relationship_State_v1.1.md` establishes minimum fixed anchors |
| C08 | **Moderate / still open** | `07_Tournament_Model` uses `CYCLE_SEED` when 1–1–1 and `NPC_KNOCKOUT_PRIORITY` for unauthored alternate NPC pairings | Rules are coherent but were intentionally only test scaffolds. Publishing results as canon would be unjustified | **Open:** select public group ranking rule and authored NPC upset/simulation design. This is **not a draw-fight issue** |
| C09 | **Moderate / still open** | Angel archive provenance and precise age; Lyra–Alex, Angel–Leena/Crystal, Mara–Plug/Raven, Ren–Tessa options | Unapproved new romance or biography may accidentally be presented as established canon; adult eligibility and professional boundaries unresolved for some NPCs | **Open editorial decisions**. Preserve friendship/solo and non-intimate variants; do not infer reciprocity from character chemistry or a selected player's intentions |
| C10 | **Moderate / still open** | All routes' finale leads to `SPECIAL_NOVA` after a real final, sometimes via technical/safety work when the pilot was eliminated | The **technical** reason each early-eliminated fighter can directly fight Nova is drafted, but the shared security access, rig readiness and evacuation window are not yet one jointly staged logistical incident | **Open for animatic:** common final-base entry condition plus protagonist-specific task/equipment and a plausible handoff from nonselected NPCs |
| C11 | **Minor / monitored** | Ari/Alex/Leena relationship insert cards, Lyra and Angel publicity scenes, Jean-Paul/Varga, Crystal/Raven | Risk of overwriting a deliberately nonromantic branch with a default kiss, or letting intimacy gate evidence | In existing model, core clues do not depend on intimacy; cross-graph check adds conflict detection. Full playthrough and scene-script implementation still needed |
| C12 | **Minor / managed** | Shared clue bibles and all new POV scripts | The Kreissack-alive midpoint, genuine accidental Nova rescue, and *later* covert executive veto can be blurred by suggestive dialogue | Currently separation is maintained in the authored drafts. Keep three evidence levels distinct: biological survival (Act III), unexplained beneficial authority (Act IV), conclusive concealed override (Act V) |

## Shared world-event ordering (nonoptional)

1. Day 0–1: anniversary / gala / first anomalies.
2. Days 3–5: all twelve decisive group matches; on-screen order may differ from engine ID order.
3. Days 8–10: four quarterfinals, investigation of Kreissack biological survival.
4. **Day 11: `S_AB` first semifinal** (from Q1/Q2); no Nova coolant-wing rescue yet.
5. **Day 12, midday: accidental coolant-wing emergency and Nova's beneficial intervention** through an existing safety gateway; no evidence Nova sabotaged the accident.
6. **Day 12, evening: `S_CD` second semifinal** (from Q3/Q4).
7. **Day 13: official final, real champion and ceremony**, then Nova's independent concealed-control reveal and separate boss (not a sanctioned tournament match).
8. Weeks later: independent legal/technical fallout and relationship epilogues; prize payouts and medical/career outcomes remain contingent.

Only the **selected protagonist's** official matches take player results. The nonselected fighters have their existing default stories unless the selected pilot's verified actions plausibly change their outcomes or choices. **These five campaigns are alternatives, not five simultaneously selected players.** Each official fight has exactly one winner and loser, never a draw. Three-way group standings may still require a rule.

## Reciprocal relationship design

A player's interest in an NPC does not establish the NPC's interest. Every proposed romance requires (a) adult eligibility; (b) authored reciprocal preference and capacity to consent; (c) no conflicting current exclusive commitment or a *specific* independently witnessed separation; (d) professional safety/recusal where warranted; (e) later scene continuity. The `cross_campaign_validator` catches conflicts **only in the active-pair list it receives**: it cannot discover an offscreen relationship that a production save file failed to record. A cleared Boolean is not a substitute for authoring the counterpart's decision.

Examples tested: Ren–Tessa conflicts with Angel–Ren; Crystal–Raven conflicts with Angel–Crystal; Ari–Leena conflicts with Angel–Leena; Ari–Mara conflicts with Mara–Plug or Ari–Leena. These are *conditional* conflicting choices, not statements that all the pairs are canonical.

## Shared mystery: minimum invariant across paths

- WAR managers, not Nova, remain responsible for the Ganymede policy disaster.
- Varga's unauthorized emotional research remains a separate **human** violation, not a secret AI matchmaking engine or a reason to throw fights.
- Kreissack biologically lives and retains experiences/personality, but Nova can covertly block directives opposed to its own goals; the **confirmation** of that veto is finale-only.
- Nova seeks more biological processing capacity and independence from WAR; an authentic rescue does not erase its coercive actions.
- Romance, fanservice, neural participation and champion status never gate the minimum clue path or the Nova encounter.

## Validation and limitations

Ran 7 tournament + 15 shared romance + 13 Lyra + 16 Mara + 24 Ren + 24 Angel = **99 existing tests**, plus **8 cross-campaign tests** in v1.1: **107 passing**. The cross-campaign exhaustive loop evaluates **five pilots × four group-result patterns × eight knockout-input patterns = 160 input tuples**, including cases where unused knockout booleans are ignored after elimination. It verifies consistent match winners, tournament champion, no fight draws, known semifinal/rescue order and local clue/boss availability in the existing dispatchers; the new graph tests conflict and explicit release behavior. Existing group seeds and nondefault NPC results are still unapproved placeholders.

This is neither a formal proof of narrative coherence nor a test of every script line: relationship gate tests use synthetic input states, not the game's actual runtime and cinematics. The Ari screenplay still needs true alternative branch scenes and a production dispatcher. Production playthrough QA and dialogue review remain essential.

## Priority next sequence

1. **Ari repair sprint:** write (i) Ari loss to Selene + group third, (ii) earlier elimination, (iii) final vs real opponent, loss/champion ceremony variants, then connect Ari to the same screen-order adapter.
2. **Single state store:** record tournament results, shared event clock, NPC commitments and verified separations, journalist conflicts, neuro-interface choices, clue acquisition; scene rendering queries *one* state. Do not maintain redundant independent relationship flags.
3. **Authorial decisions:** approve/decline pairings and Tessa, verify NPC ages/interests, settle group ranking and alternate NPC outcome principles.
4. **Human review:** trace at least five full save-file playthroughs (including one early group elimination) and time Arcade versus Story modes before the Crystal campaign.
