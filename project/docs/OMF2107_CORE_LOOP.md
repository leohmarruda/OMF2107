# OMF2107 Core Loop

One-page summary of how a session plays. Sources of truth: `DEVPLAN.md` (direction change of 2026-11-07, rulesets) and `OMF2107_GAME_SPEC.md` (§3 core flow, §7 career loop); this page restates them so they can be read in one sitting. The career layer's rules (economy, sponsors, rivals) are in spec §7.

## Moment to moment (a match)

- Fixed side-on fight plane. Camera and stage geometry add depth; they never change left/right inputs (spec §3, §4.1).
- Hits come from authored shapes, not mesh overlap. Stun, knockdowns, air hits, combos and the original-style finish are in scope (spec §4.1).
- **Stun is the only combat resource.** No heat, overclock, rage or desperation meter.
- Simulation runs at a 60 Hz fixed tick; presentation targets 60 fps, including damage effects.
- AI obeys the same rules as the player. Difficulty changes decision quality and reaction allowance, never hidden damage bonuses (spec §4.2).
- All modes share move definitions. Match rules come from a named ruleset, shown before the fight:
  - `classic` (Story, Arcade): OpenOMF-parity rules. Arcade adds its tune-up multipliers as disclosed pre-match conditions.
  - `career` (Tournament): `classic` plus region damage in four regions (arms, legs, torso, head) and three states (Operational, Damaged, Critical), with numeric effects shown in the HUD and no move ever removed. Low hits damage legs, mid hits the torso, high hits head and arms. Damage carries between rounds and between matches until repaired; the pre-match screen shows the opponent's regions.
- Destruction finishers only in the last round, and only when the finishing HAR is in good condition (no Critical region in `career`; in `classic`, every round won without losing one, each ended with at least 50% health). The AI follows the same rule, and its destructions play in full.

## One session (all modes)

1. Choose a mode.
2. Pick a pilot, then a HAR. Story may recommend a pairing but does not force it. Tournament uses the custom pilot and owned HARs.
3. Short opponent introduction (skippable).
4. Fight.
5. Result, reward, and a character beat suited to the mode.
6. Mode-specific next step:
   - **Story:** choose a response or alliance at selected moments; advance through the Ganymede bracket. No economy, upgrades or damage. A loss either changes the route or ends in a game-over ending, depending on chapter and state.
   - **Tournament:** repair, buy, train, consider sponsor offers, enter the next event.
   - **Arcade:** newscast, hangar, tune-up, next rung (see `OMF2107_ARCADE_MODE.md`).

## Career loop (Tournament)

1. Create a pilot and spend a fixed budget on starting strengths.
2. Enter a ranked event or a contract with known prize, arena, opponent class and repair risk.
3. Fight; receive transparent payouts for result and optional objectives.
4. Choose how to repair each damaged region: full repair (restores the region), standard patch (cheaper, restores it to Damaged with a known limitation), or fight damaged. Insurance and legal HAR upgrades are also on sale. Projected effect is shown before buying.
5. Build rivalries, sponsor relationships and reputation, climb brackets, work toward the top title.

Design rules:

- **Persistent career (Model A).** Money, owned HARs, upgrades and unrepaired damage carry between events.
- **Insolvency is game over.** Before that point the game offers ways out (sponsor advance, conditioned contract, salvage sale, insurance) and warns before any match that could end the career. The trigger is the original rule: money still negative after two consecutive matches. The first negative match is the warning.
- A routine loss never ends the career on its own; it can drop the pilot to a lower bracket or a qualifier.
- Upgrades stay bounded: a well-played base HAR can beat an upgraded one.
- No invisible rolls; every risk is disclosed. Autosave after matches and purchases.
- Tournament is separate and replayable; story choices do not gate it.

## Open questions for discussion

- Size and frequency of sponsor rescues (decide at M3, after the economy simulation).
- Upgrade model under Model A: the original's bounded vertical upgrades, or horizontal options.
- Whether the `career` finisher also needs the `classic` rule (no round lost, 50% or more).
