# NPC-only tournament resolution — v4.1

**Author decision:** NPC-versus-NPC fights are never shown. They are resolved offscreen. Do not create playable fights, fight cinematics, fight choreography, fight asset cues, or required battle-performance scenes for these pairings.

## Runtime contract

1. The existing simulator supplies one decisive winner for every match. Player matches come from gameplay; NPC-only results use established exact-pair results first and separately approved deterministic overrides for other reachable pairs. The opt-in `npc_pair_proposals.py` table is NOT canon. The historical strength-priority fallback is NOT canon.
2. `offscreen_npc_results.project_board(...)` projects the authoritative result ledger into group standings, bracket lines, champion/loser dialogue bindings, and a list of offscreen NPC results. An NPC-only row always has `render_fight=false`.
3. Display only **actual recorded numeric scores**. Never synthesize a numerical score from the selected winner. A missing score becomes `null` and should be omitted or shown as 'not recorded', rather than `0–0`. The game's actual scoring semantics and normalization have not yet been specified in the pack.
4. In 1–1–1 circular group standings, use recorded cumulative scores across both group matches, with head-to-head resolving a *two-way* equal-total tie. An exact three-way total tie remains without an approved rule. Do not silently use the legacy seed.
5. Branch-dependent narrative must read champion, finalists, elimination status, and actual match outcomes from the result ledger. Optional commentary is allowed but must not invent an on-screen fight or tactics the player witnessed.
6. No three-way tie rule or 59 unapproved winner proposals are approved by this document. Production board generation fails closed on unapproved tournament state; explicitly labeled draft mode is available for QA.

## v4.0 dossier correction

The `NPC_PRIORITY_MATCHUP_DOSSIERS_v4.0.*` files remain historical **internal tactical hypotheses** only. Their fields `required_scene_evidence` and the phrases 'Stage...' or 'Show...' are **superseded**, not active writing requirements. Their tactical rationales may inform editorial winner decisions but need never be dramatized. An offscreen result may receive a bracket entry, optional one-line report, and downstream character reaction, with no portrayal of the fight.

## Still needed for release

- Approve individual NPC knockout winners for reachable pairings (the draft list is not approval).
- Supply actual score data/schema from the game, particularly for group-stage circular standings. Avoid inventing arbitrary numeric loser/winner margins.
- Determine behavior for all-three-equal cumulative group scores (preannounced tertiary rule).
- Integrate the board projection into the actual game runtime and revise fixed-winner screenplay references. This Python module is an integration contract, **not** proof of runtime wiring.
