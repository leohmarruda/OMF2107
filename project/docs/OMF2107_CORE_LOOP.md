# OMF2107 Core Loop

One-page summary of how a session plays. Source of truth is `OMF2097_3D_GAME_SPEC.md` (§3 core flow, §7 career loop); this page restates it so it can be read in one sitting.

## Moment to moment (a match)

- Fixed side-on fight plane. Camera and stage geometry add depth; they never change left/right inputs (spec §3, §4.1).
- Hits come from authored shapes, not mesh overlap. Stun, knockdowns, air hits, combos and the original-style finish are in scope (spec §4.1).
- Simulation runs at a 60 Hz fixed tick (initial target, spec line 98); presentation targets 60 fps.
- AI obeys the same rules as the player. Difficulty changes decision quality and reaction allowance, never hidden damage bonuses (spec §4.2).
- All modes use the same match rules and move definitions. A mode may change pre-match conditions only if shown clearly before the fight.

## One session (all modes)

1. Choose a mode.
2. Pick a pilot, then a HAR. Story may recommend a pairing but does not force it. Tournament uses the custom pilot and owned HARs.
3. Short opponent introduction (skippable).
4. Fight.
5. Result, reward, and a character beat suited to the mode.
6. Mode-specific next step:
   - **Story:** choose a response or alliance at selected moments; advance through the Ganymede bracket.
   - **Tournament:** repair, train, buy, enter the next event.
   - **Arcade:** newscast, hangar, tune-up, next rung (see `OMF2107_ARCADE_MODE.md`).

## Career loop (Tournament, spec §7)

1. Create a pilot and spend a fixed budget on starting strengths.
2. Enter a ranked event or a contract with known prize, arena, opponent class and repair risk.
3. Fight; receive transparent payouts for result and optional objectives.
4. Spend on repairs, training or legal HAR parts. Projected effect is shown before buying.
5. Build rivalries and sponsor reputation, climb brackets, work toward the top title.

Design rules: upgrades stay bounded (a well-played base HAR can beat an upgraded one); no invisible injury rolls; autosave. Tournament is separate and replayable; story choices do not gate it.

## Open questions for discussion

- Arcade's tune-up (armor/power/speed pick between fights) gives diminishing gains per repeat pick (decided). Should it live in the shared match rules, or stay a documented pre-match condition?
- First slice is decided: Ari's route (spec §6, development plan). Crystal vs Christian is deferred to Phase 3. See `OMF2107_FEATURES.md`.
