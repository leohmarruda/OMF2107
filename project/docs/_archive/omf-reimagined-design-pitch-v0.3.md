# One Must Fall: Reimagined — Design Pitch (Draft v0.3)

> **ARCHIVED 2026-11-09. Not a source of decisions.** OMF2107 adopted parts of this pitch on 2026-11-07 and 2026-11-09.
> Current rules live in `DEVPLAN.md` (plan, rulesets, feature tiers) and `OMF2107_GAME_SPEC.md` (AI §4.4, readability
> §5, economy, sponsors, rivals and reputation §7, accessibility §8). Kept only to explain where ideas came from; the
> proposal numbers (#n) are still used for traceability.
>
> | Pitch idea | Status in OMF2107 |
> | --- | --- |
> | Classic combat on a 2.5D plane, fixed HAR signatures, fidelity baseline (#11) | Adopted: parity foundation on `classic` |
> | Localized damage (#1), damage visuals (#22) | Adopted, changed: four regions (no specials region), numeric stun-centred effects, **no move removal**, carried between rounds and matches; Tournament only |
> | Repair, preparation and insurance economy (#2) | Adopted, changed: repair ladder is full repair, patch, fight damaged |
> | Tournament-scoped reset of money and damage | **Rejected:** persistent career (Model A); insolvency is game over after two consecutive negative matches |
> | Fail-forward (#3) | Adopted in Tournament (lower bracket); Story has its own fail-forward or game-over endings |
> | Rivals remember (#4), sponsors (#10), contracts (#16), rankings (#17) | Adopted (minimal sponsors at M3, full at M6) |
> | Personality AI and bounded adaptation (#5) | Adopted: one profile per opponent at M4, adaptation at M6 |
> | Limb targeting (#13) | Adopted through height-based region mapping |
> | Heat and overclock (#7), desperation (#27), overdrive (#29) | **Rejected:** stun is the only combat resource |
> | Jury-rigged repair (#24c) | **Rejected** |
> | Emergency power rerouting (#14) | **Rejected** |
> | Learned Shadow AI (#25), neural stress (#30), injury roster (#31) | **Rejected** |
> | Hybrid tournament simulation (#6), three-axis relationships (#8), arena engineering (#15), illicit tech (#19), modular parts (#20), native affinity (#24b) | Deferred |
> | Broadcast and reputation (#24), spectator hype (#24a) | Decide after the M3 playtest |
> | Accessibility (§4) | Moved to spec §8 as a proposal; decision due by M4 |


> Working concept: a **single-player fighting RPG / mech-pilot career game** with classic, execution-heavy 2D fighting at its core, self-contained tournament runs, and persistent narrative choices. Inspired by *One Must Fall 2097* (1994).
>
> **Status:** concept draft, not a production commitment. Rights to the OMF name, setting, and characters are unverified. All OMF-specific material presumes licensed use; otherwise this is an original spiritual successor. Feature tiers below rank *design value*, not a promise that everything in Tier 1 ships at launch.
>
> **Revision note:** v0.3 builds on v0.2 by adding spectator hype/underground funding, manufacturer calibration/native pilot affinity, and field-expedient jury-rigged repair. Existing #1–#32 rankings are preserved; three additions use #24a–#24c. An original-idea crosswalk follows the ranking.

---

## 1. Vision

You pilot a giant robot (HAR) in corporate-run gladiator tournaments. Between fights, you manage repairs, sponsors, and relationships. Every hit you take costs money, every relationship has stakes, and sometimes the person you care about is your next opponent in the bracket.

**One-line pitch:** *Classic 2D fighting, where damage has a price and rivals have a heart.*

**Distinctive fantasy:** becoming the best fighter, advancing your career, and protecting your personal commitments are related but **not identical goals**. You can win a match while losing money, protect someone by forfeiting, or become a champion at the cost of a sponsor or friendship.

**Genre positioning:** a **single-player fighting RPG and tournament-career simulator**, with *roguelite elements within tournaments* rather than an assumed fully procedural roguelite campaign. The differentiator is the interaction of **mech damage, repair strategy, evolving rivals, relationships, and corporate pressure**—not merely a run-based fighter.

**System-level design rule:** every major feature should create choices **before, during, or after** a match, and those choices should meaningfully affect at least one other system. Don't add parallel subsystems that never intersect.

## 2. Design pillars

1. **Classic combat, no compromise.** Execution-heavy, readable, frame-precise. Accessibility is layered on top; the default combat remains fully expressive.
2. **Damage has consequences—but not arbitrary frustration.** Hits translate into readable part failures, repair bills, and tactical tradeoffs, without making a comeback impossible.
3. **Pilots are people.** Every fight sits inside a relationship: rival, mentor, sponsor, partner. Narrative stakes have gameplay consequences, without compulsory romance.
4. **Gameplay expresses character.** AI behavior follows personality and observable information, and evolving rivals respond to prior encounters.
5. **The circuit is a world, not a ladder.** Opponents progress, contracts change, and tournament outcomes reshape future choices; pivotal authored story beats remain legible.
6. **Consequences with tolerance.** Losses branch forward; persistent narrative history matters, while tournament-specific financial and mechanical setbacks reset to avoid debt spirals.

## 3. Core loop

```text
Story / career hub ──► Tournament run ──► Tournament resolution ──► Career hub
  │                    │                  │                          │
  │  relationships     │ evolving bracket │ run funds/damage reset   │ future rivals,
  │  sponsors, HARs     │ fights, repairs   │ records, story flags     │ contracts, routes
  │  and intel         │ and tactics       │ and unlocks persist      │ and stakes
  └─────────────────────────────────────────────────────────────────┘
```

- **Story/career hub:** conversations, sponsors and corporate offers, relationship choices, HAR/limited module selection, intel, and optional training.
- **Tournament run:** bracket competition with fights, repair/insurance/temporary preparation decisions, sponsor conditions, and consequential rival meetings.
- **Tournament resolution:** tournament-scoped damage, money, temporary equipment and patches reset; narrative flags, relationship states, learned techniques, rival history, unlocks and reputation persist.
- **Career evolution:** tournament results influence invitations, sponsor interest, rival loadouts, and the next authored story beats. Failure may lead to a qualifier, lower-tier invitation, or alternate chapter rather than an immediate game over.
- **Cross-system example:** winning with a damaged leg generates a large repair bill and a reputation for recklessness; a future opponent studies that tendency, while a sponsor offers a risky reactor as a solution.

## 4. Combat

- **Perspective:** 2.5D: 3D models constrained to a strict 2D gameplay plane.
- **Feel:** preserve the identifiable OMF physics identity: wall slams, juggles, interactive arenas, distinctive movement arcs, and impactful metal-on-metal combat.
- **Execution:** classic motion inputs, tight timing, and combos that reward practice.
- **HAR identity:** each HAR keeps a clear base moveset, signature capabilities, movement identity, weaknesses, and recognizable silhouette, regardless of pilot. Pilot training changes general-purpose techniques rather than replacing HAR signature attacks.
- **Standard tooling:** training mode with frame data, hitbox/hurtbox and input display, dummy recording/playback, and a consistent documented input buffer.
- **Readability rules for 3D:** strong silhouettes, clear startup tells, and visible part damage that never conceals collision behavior.
- **Faithfulness gate:** before changing the formula, build a small comparison study of original OMF movement, juggle rhythm, wall interactions, special-move identity and arena hazard pacing. Document preserved vs intentionally changed behavior; do not assume a 2.5D rendering alone preserves the feel.

### 4.1 Heat and reactor load (core candidate; prototype before lock-in)

Heat is the proposed **mech-specific combat resource**, replacing or significantly modifying a generic super meter:

- Special attacks, sustained offense, overclocking, and certain modules build heat; defensive maneuvering or venting may cool it.
- **Controlled heat** offers reliable action. **Elevated heat** increases risk but can enable limited performance advantages. **Overclock range** unlocks powerful options in exchange for exposing the reactor. **Critical heat** causes a telegraphed shutdown/stagger or forced cooldown.
- Heat thresholds, cooling, and burst profiles differ by HAR. A heat-focused build should not become universally optimal.
- The core decision is *whether the extra power justifies a future vulnerability*, not simply avoiding a punishment for pressing specials.
- Avoid stacking an independent rage meter and transformation gauge on top of this by default. The existing **desperation window** proposal can be subsumed into overclocking if tests support it.

### 4.2 Emergency power rerouting (strong candidate)

When a subsystem is damaged, a player may divert power from one function to another for a limited period: e.g., sacrifice mobility for stronger remaining-arm attacks, or reduce offensive output to stabilize damaged actuators. Tradeoffs must be visible, deterministic and constrained; rerouting is not a free full repair. Prototype only after core localized damage proves enjoyable.

### 4.3 Environmental engineering (strong candidate)

Arena mechanics should be deliberate, readable positional tools: magnets, hydraulic lifts, electrical conduits, destructible barriers, wall rebounds and hazard-triggered stage transitions. Favor predictable timing and clear counterplay over random damage. A small number of distinctive arenas is better than many interchangeable effects.

### 4.4 Manufacturer calibration and native pilot–HAR affinity (Tier 2 candidate)

Each pilot has a **native chassis profile** representing prior experience, cockpit ergonomics, and manufacturer calibration. **Any pilot may still operate any HAR**, and a pilot's skills and HAR's signature moves remain available regardless of pairing.

- Native combinations start with familiar handling; non-native combinations may have **small, documented, deterministic friction**, such as modestly higher reactor heat for a specific maneuver or a published dash-recovery adjustment. The effects must never silently change input interpretation, invalidate practiced combos without warning, or create severe tier gaps.
- Calibration or training can mitigate the friction over time; familiarity mainly widens **tactical options** rather than delivering escalating raw damage/health bonuses. A native chassis is a starting preference, not a mandatory endgame choice.
- Display the exact effect in pilot/HAR selection, loadout screens, and training frame data. Balance all pilot–HAR combinations; assess whether minor heat costs preserve more control consistency than dash-frame changes.
- **Prototype gate:** adopt only if test players recognize pilot identity without reporting loss of control or being compelled to use native pairings. Consider cosmetics, dialogue, or sponsor access instead of combat penalties if the mechanical version fails.

### Accessibility (required, not optional)

The single-player audience will include story/RPG players. Provide:

- Difficulty tiers that improve AI decisions, timing and predictability rather than merely increasing stats.
- Optional assist inputs (e.g., one-button specials) configurable per profile.
- A Story difficulty that preserves the repair and relationship decisions while softening execution requirements.
- Accessible alternatives to any time-sensitive ejection or critical-event sequence; normal defeats must not demand a reflex-based quick-time event.
- Readable damage indicators and alternative UI to flashing/noisy sensor penalties, preserving player control and input consistency.
- Default classic rules untouched by assist settings chosen for Story mode.

## 5. Damage and tournament economy

### 5.1 Localized damage: tactical and readable

- **Regions:** arms, legs, torso, head/sensors, and special systems.
- **Three qualitative states:** *Operational* (normal); *Damaged* (specific predictable penalty); *Critical* (major but telegraphed impairment, possibly with compensating tactical options). Thresholds and effects must be testable and explainable.
- **Counterplay:** deliberate pressure on a part can be viable without making attrition the only strategy. Part damage should create a choice between changing tactics, accepting risk, rerouting power, or spending on repair—not an irreversible control failure.

| Region | Damaged | Critical (illustrative, to test) | Fairness constraint |
|---|---|---|---|
| Arm | Weaker punches, reduced access to a subset of moves | Some arm-specific moves unavailable; alternative attacks remain | Never remove all meaningful offense |
| Leg | Reduced dash/walk performance | Dangerous mobility maneuver disabled or restricted | Avoid unannounced changes to input timing |
| Torso | Less effective protection | Lower available armor/health for a later round or fight | Avoid instantaneous unavoidable defeat |
| Sensors | Reduced sensor assistance / tactical intel | In-world targeting feedback deteriorates | No unreadable HUD or mandatory visual noise |
| Specials/reactor | Higher heat or reduced efficiency | Signature subsystem offline until patched/rerouted | Preserve a functional base toolkit |

- Show dents, sparks, damaged armor and missing plating on the HAR model; effects must not obscure hurtboxes/hitboxes. Communicate state through both visuals and clean HUD indicators.
- **Separation:** match health and persistent-within-tournament subsystem condition need distinct rules. Specify exactly when damage carries into subsequent rounds/fights, and when a repaired state clears. This remains a balancing decision for the prototype.

### 5.2 Economy rules: opportunity costs, not a flat repair tax

- **Run-scoped:** damage, tournament money, and temporary patches reset at the end of each tournament. Sponsor/corporate relationships may persist, but not spendable tournament debt.
- **Three spending categories:**
  1. **Repair:** full restoration, a guaranteed cheap patch, a higher-function jury-rig with disclosed risk, or knowingly fight damaged.
  2. **Adaptation:** opponent-specific temporary tuning or limited legal modules.
  3. **Risk management:** insurance, guaranteed salvage, or emergency service.
- **Repair ladder:**
  - **Full repair:** highest cost; restores normal performance reliably.
  - **Standard patch:** lowest-cost dependable fix; restores minimum functionality with a known limitation or reduced efficiency.
  - **Jury-rigged scrap repair (Tier 2):** somewhat more expensive than a standard patch but cheaper than a full repair; restores **more** of a critical system for the current bout using reclaimed parts. Its tradeoff is a **telegraphed reliability or heat risk**, not an invisible arbitrary failure.
  - **Fight damaged:** no repair expense; accept tactical risk and potentially earn a disclosed spectacle reward.
- **Jury-rig fairness rule:** prefer a visible heat-spike threshold, escalating strain indicator, or predictable deterioration condition over a hidden mid-match random roll. If a randomized reliability check is retained after testing, disclose the odds/risk class in advance, telegraph danger, and preserve counterplay; it must never cause an unavoidable sudden loss.
- **Other between-fight actions:** strategically forfeit a round/match where rules allow; salvage scrap parts; take an optional low-stakes bout when available; accept a sponsor contract; or save funds for a more difficult future opponent.
- **Purse accounting:** prize payout and bonuses minus repair, temporary equipment and consumable costs. Money is meaningful *within* a tournament; it does not transfer as campaign debt.
- **Baseline solvency target:** `E[winnings per fight] - E[repair and prep cost per fight] > 0` for a representative player on default difficulty. This expectation alone is **not enough**: test loss tails, the probability of becoming unable to continue after one bad fight, and recoverability without mandatory grinding.
- **Anti-spiral tools:** purchasable insurance, inexpensive partial fixes or jury-rigs, limited emergency functionality, scrap markets, spectacle-earned community assistance (if implemented), alternate brackets and fallback options; avoid systems that punish failing players by also stripping their ability to fight competently.
- **Anti-turtling:** bonuses for entertaining or challenging play, but include multiple viable styles (defensive precision should not be automatically penalized). Contract objectives should be explicit, feasible and optional.
- **Repair decision example:** a damaged arm versus a coming aerial opponent. Spend on arm restoration, buy an anti-air module, or retain funds and accept both weaknesses. All three should sometimes be rational.

### 5.3 Persistence and progression

| Resets per tournament | Persists across campaign |
|---|---|
| Damage, tournament purse, insurance, patches, temporary modules | Relationships (trust/respect/affection), story flags, rival memories, learned pilot techniques, unlocks, reputation and sponsorship history |

**Rule:** persistent progress is primarily what you *learn, unlock, or change in the world*, not what you spend. A bad tournament can change the story or delay advancement without leaving a debt balance or compounding stat penalty.

**Pilot progression:** favor *horizontal* growth—techniques, tactical options, knowledge, HAR access, and modest calibration proficiency—over endlessly increasing attack/health stats. Skillful fighting must stay central. Any pilot can operate any HAR; native manufacturer affinity may offer a small initial ergonomic advantage, while training can reduce non-native friction without making a first-time combination unusable (see §4.4).

### 5.4 Sponsors, contracts and corporate politics

Sponsors are actors with competing agendas, not merely bonus multipliers. Offers may include cash, special equipment, intelligence, repair access, invitations or protection. Demands might include an aggressive play style, testing an unstable component, withholding a secret, throwing a match, or taking sides in a corporate feud.

- **Every questionable offer has a legible refusal path**, even if refusal costs an advantage.
- Contract consequences should cross systems: money, reputation, relationships, access, rival behavior and main-plot evidence.
- Ethical choices should not be reduced to obvious “good/evil” bonuses; allow credible tradeoffs, including principled choices that are costly in the short term.
- Sponsors may act on a pilot's prior conduct or public reputation; major offers can be authored while smaller contracts are reusable templates.

### 5.4a Spectator hype and underground odds (Tier 2 candidate)

A distinct **spectacle channel** gives pilots ways to secure emergency support **without depending exclusively on corporate sponsors**. Entertaining play, daring but intentional risk-taking, successful clutch comebacks, or visible sporting integrity can earn **spectator hype**. The underground scene reacts through fictional support networks, informal odds, salvage tips, or fan-organized emergency repairs.

- **Gameplay payoff:** a capped hype reward can enable an emergency fan-funded repair, a scrap lead, a small one-time tournament cash infusion, or an underground contact. This creates a recovery path without making damage farming or reckless play profitable by default.
- **Separate concepts:** *hype* is performance-driven, short-horizon audience attention; *public reputation* is longer-term social perception. Hype may influence reputation, but does not replace trust/respect/affection or create an independent reputation-grid minigame.
- **Underground odds are fictional world feedback**, not a player-facing real-money wagering system. If odds appear, they can estimate perceived chances and affect story offers; do not require betting, purchasable gambling currency, or monetized wagers to obtain core resources.
- **Balance:** reward varied skill expression, including impressive defensive play; cap per-fight gains, prohibit intentional self-damage exploits, and make the support contingent on comprehensible achievements. Emergency repairs must not trivialize the purse and sponsor tradeoffs.

### 5.5 Experimental and illicit technology (strong candidate)

Include a restrained set of *optional* modules with benefits and risks: unstable overclockers, deliberately shedding armor, sensor interference and unapproved neural interfaces. Legality varies by tournament; detection, reliability, safety and reputation effects should be transparent. Technologies can provide story evidence about the corporate conspiracy.

**Important constraint:** no unlimited mix-and-match of signature moves. Most HAR identity remains fixed; any modular options should be limited in number and comprehensible to opponents.

### 5.6 Normal defeat, ejection and persistent stakes

A defeated HAR normally performs **automatic safe ejection**: the player loses the match and faces the usual tournament consequences. Death or lasting injury is **not a default failed-reflex punishment**. Dangerous ejection, injury or lethal stakes are reserved for clearly flagged exceptional matches and must have accessible resolution alternatives. Whether exceptional persistent injury exists at all is a **Tier 3 decision**, not an adopted mandatory mechanic.

**Single-carrier constraint:** do not stack multiple cross-tournament *mechanical penalties* (injury, stress, neural trauma and financial debt). Persistent **narrative** consequences—relationships, rivals, story flags—are intended and do not violate this constraint. If lasting mechanical injury is eventually adopted, cap it strictly, prevent irreversible death spirals, and test it against fail-forward.

## 6. Campaign and tournament structure

- **Pilot selection:** choose from an authored roster, with limited customization:
  - **Background trait:** ex-corporate, indebted, veteran, wildcard, etc., influencing initial resources, dialogue and sponsor approaches.
  - **Cosmetics:** pilot outfits, HAR paint and decals. Native HAR familiarity is a soft, transparent initial calibration profile, not a pilot–HAR restriction (§4.4).
- **Shared main plot:** a corporate conspiracy behind the tournaments, experienced from each pilot's point of view. Shared scenes are reused, but pilots have distinctive key scenes, rivals and endings.
- **Depth tiers:** **Tier A** has 3–4 pilots with full routes at intended launch; **Tier B** appears as rivals/relationship options and can later get shorter or expanded routes. These are targets, not validated budgets.
- **Hybrid tournament ecosystem (core direction):** ordinary bracket positions and offscreen NPC results can be simulated; pivotal plot encounters and meaningful constraints are authored. Rival careers can advance, stall or change after losses, while the story protects the beats that must occur.
- **Rival continuity:** competitors remember important matches, adjust HAR choices and preparation, change sponsors, develop alliances or grudges, and reference what happened. Use bounded state tags and reusable events rather than bespoke writing for every history combination.
- **Failure tolerance:** tournament defeat can lead to a qualifier, lower-tier invitation, detour or alternate outcome. The route may end after repeated failures or an explicitly marked lethal story event, not because of a single routine loss. Distinguish **route failure** from **save deletion**.
- **Sporting integrity choices:** a player may refuse to throw a match, deliberately lose, expose a rigged bracket, or seek an alternative solution. No choice should silently override fixed authored match outcomes in content that requires them.
- **Career reputation:** track how a player fights and behaves—sportsmanship, spectacle, perceived ruthlessness, reliability, corporate alignment—rather than just win/loss. Use broad interpretable profiles instead of dozens of opaque gauges.
- **Media layer (candidate):** broadcasts, commentators and public narratives make reputation legible, alter sponsor opportunities, and help give the circuit a history. A separate, short-term **spectator hype** signal may unlock limited underground or fan-funded assistance; it should not duplicate the long-term reputation system (§5.4a).

### 6.1 Example integrated tournament (illustrative, not canon)

1. **Qualifier:** victory with damaged leg actuators forces a repair-versus-preparation decision.
2. **Quarterfinal:** a sponsor offers an experimental reactor with significant heat and contractual risk.
3. **Semifinal:** a close relationship and a suspicious offer make winning, losing or exposing manipulation consequential.
4. **Final:** a recurring rival has studied the player's habits and changed their legal loadout within clear bounds.
5. **Resolution:** a win may reveal corporate wrongdoing; career advancement, public reputation and personal loyalties point in different directions.

## 7. Relationships, mentorship and romance

- **Scope:** romance available with all or most adult pilots; friendship, rivalry, mentoring and sponsor dynamics remain fully meaningful without romance. Romance is optional and never required for completion or combat power.
- **Three relationship dimensions, not one affinity bar:**

| Dimension | Measures | Potential consequences |
|---|---|---|
| **Trust** | Reliability, honesty, willingness to take risks together | Shared intel, secrets, support and cooperation |
| **Respect** | Skill, principles, conduct in competition | Mentorship, sparring, rival recognition |
| **Affection** | Emotional attachment, including optional romance | Personal events, closeness, conflicting loyalties |

These can diverge: someone can admire a pilot's skill while distrusting them, or love someone without approving of their choices. Use a few meaningful state thresholds and authored reactions rather than large combinatorial dialogue trees.

- **Training unlocks pilot techniques:** earned through mentorship, shared training, sparring or observation—not purchased with affection. They teach broadly applicable capabilities (defensive timing, counters, aerial control or reactor use) while each HAR retains its unique signature moveset. Non-romantic routes provide equivalent opportunities.
- **Mechanical hooks:** allies can offer parts, intel or discounted repairs; rivals can challenge contracts or adapt; personal arcs can reveal conspiracy clues.
- **Bracket tension:** you may face a friend, mentor, rival or partner. Winning, losing honestly, intentionally throwing a match, or revealing coercion can change trust, respect, affection and the outside world—not just the next cutscene.
- **Consequences need agency:** do not force the player into a harmful act to maintain a relationship, and do not turn characters into rewards for choosing agreeable dialogue.
- **Writing scope control:** character-centric arcs with route-specific framing; shared scenes, reusable interaction structures and a limited number of high-impact branching decisions. Romance with most pilots × multiple routes remains a major production risk.

## 8. Opponent AI and rivals

AI is a core part of a single-player fighting game, but complexity should be earned through player-visible results.

### 8.1 Two-layer AI architecture (recommended baseline)

1. **Stable personality:** aggression, preferred range, risk tolerance, tactical preferences, adaptation speed, willingness to exploit damage; defined independently of difficulty.
2. **Bounded tactical adaptation:** track a small, interpretable set of *observed* habits (jump rate, approach patterns, throw/strike mix, repeated punish options, retreats under damage). Opponents respond only after plausible observation and within reaction limits.

- **No input reading or impossible foreknowledge.** Difficulty comes from decision quality and the capacity to punish predictable habits, not perfect reactions or secretly reading button presses.
- **Legible counterplay:** the player should be able to identify what an opponent learned and vary tactics to beat it. Expose this through believable dialogue, reports, or behavior rather than an intrusive analytics UI.
- **Story-reactive modes:** fight-to-win, hesitant or desperate variations may reflect relationships without making the AI intentionally incompetent or contradicting important narrative stakes.
- **Career memory:** persistent bounded facts (who won, decisive tactics, humiliation, help, grudges) affect preparation and commentary. This is distinct from real-time adaptation.
- **Boss design:** asymmetric opponents, overpowered HARs, handicap matches, recognizable attack patterns and readable tells are allowed if they produce fair learning and counterplay.
- **Advanced Shadow AI:** training on full recorded player fights remains an optional research/prototype track. Do **not** require ML for launch; validate whether simple authored counters already deliver the intended experience.

### 8.2 Verification tests

Test whether distinct AI profiles are recognizable without dialogue; whether adaptation defeats repetitive habits without cheating; whether players can counter-adapt; and whether multiple difficulty settings remain fair. Collect decision traces in test builds, not just win rates.

## 9. Scope tiers, gates and production plan

| Stage | Contents | Gate to progress |
|---|---|---|
| **Combat/economy microprototype** | 2 HARs, 1 arena, 2 AI profiles, basic 3-state damage, a small repair purse and one meaningful between-fight decision; temporary UI acceptable | Fighting feels good **and** repair stakes improve decisions rather than just cause passivity |
| **Vertical slice** | 1 partial pilot route, 4 HARs (target), 1 short hybrid tournament, heat experiment, usable damage/repair system, foundational training, one remembered rival, one consequential relationship/sponsor choice | Core systems reinforce one another; failure remains recoverable; AI styles readable |
| **Launch target** | 3–4 full pilot routes, 8–10 HARs, Tier B pilots as rivals and relationship options, approximately 5 tournaments per route, bounded persistent rival memory, core sponsors and accessibility | Only after writing, balancing and production budgets are validated |
| **Post-launch / optional** | Expanded Tier B routes, extra HARs and arenas, experimental technology, deeper circuit simulation, local versus and possibly online versus | Depends on demand, technical feasibility and IP status |

**Scope principles:**

- The vertical slice is **not** the first prototype. Validate combat + repair economy before building extensive narrative or expensive AI.
- Target the smallest connected example: one pilot, one rival, one sponsor, one repair dilemma, and a consequential match outcome.
- Prefer fixed HAR signatures, a few meaningful modules, transparent native-chassis calibration, and data-driven authoring over unlimited modular combat systems.
- Tier 1 in section 12 means **high design priority**, not automatic inclusion in the microprototype or launch build.
- A slice passes only if players choose different rational repairs/preparations, AI behavior is distinguishable, and matches remain enjoyable under damage. If repair incentives cause passive play, redesign them before expanding content.

## 10. Key risks and mitigations

1. **Audience mismatch:** execution-heavy fighting vs. story/RPG appeal. Offer transparent difficulty and assist controls, playable training, and accessible consequential-event resolution.
2. **Writing combinatorics:** pilots × routes × relationships × dynamic brackets. Use reusable character arcs, authored anchor encounters, bounded tags and explicit branching budgets.
3. **AI quality/cheating perception:** weak or unfair AI undermines single-player value. Prototype personality and observable rule-based adaptation first, instrument decisions and cap reactions.
4. **Economy death spiral or passive play:** average positive net winnings are insufficient. Test bad-loss tails, recovery, and incentives across skill levels, not only expert play.
5. **Identity loss:** story weight, excessive modules and 3D presentation can dilute OMF's feel. Keep HAR signature movesets and a documented movement/physics fidelity baseline.
6. **System overload:** independent gauges (heat, rage, overdrive, injury), reputation/hype meters and prep screens can overwhelm the player. Consolidate overlapping mechanics; make spectator hype primarily event-driven and legible rather than a second full economy.
7. **Emergent narrative incoherence:** procedural brackets may eliminate a required story rival. Use a hybrid simulation with authored anchors and transparent eligibility constraints.
8. **Persistent punishment conflict:** ejection injuries, neural feedback and stress can defeat fail-forward. Default to safe ejection; defer lasting mechanical penalties and never stack them.
9. **Production/scope:** the original vertical-slice specification combined too many features. Build the two-HAR combat/economy microprototype first, with go/no-go testing.
10. **IP and legal:** verify OMF rights; treat the broad 'Nemesis patent' concern as unverified and obtain legal review if designing a mechanically similar protected system. Do not assume any specific patent coverage without current legal analysis.
11. **Jury-rig unfairness:** random mid-match part failures may feel like the game overrides execution skill. Favor forecastable heat/strain costs; cap severity and validate both success and failure cases.
12. **Native-affinity lock-in:** pilot-dependent frame changes may undermine practiced timing or make non-native HAR combinations unattractive. Keep friction modest, clearly documented and reversible; drop mechanical penalties if they fail usability tests.
13. **Hype farming and odds confusion:** rewarding spectacle may favor unsafe play styles or imply a gambling progression loop. Support skillful defense, cap awards, prevent damage farming, and keep odds fictional and non-monetized.

## 11. Open questions and decisions

### Open

1. **Tone:** grim corporate dystopia, pulpy melodrama, or a mix?
2. **Primary player fantasy:** mastery of robot combat, navigating a corrupt sports industry, or pilot relationships? All three matter, but one should guide spending.
3. **Tournament simulation depth:** how far should offscreen competitor progression go, and which encounters must remain authored?
4. **Run length:** how many bouts/tournaments per route, and how long is an intended full playthrough? Current ~5 tournaments is only a target.
5. **HAR customization limit:** how many legal temporary modules are compatible with clear fixed HAR identities?
6. **Versus mode:** local versus at launch or post-launch? Online versus remains optional.
7. **Exceptional lethality:** can marked lethal matches truly end a route or kill a pilot? If so, what are the fairness, content and save rules?
8. **Long-horizon AI:** are simple scripts sufficient, or is advanced learned Shadow AI valuable enough to justify cost?
9. **Spectator hype:** should it produce a small emergency aid token, a capped cash/repair credit, or story-only favors? How much support avoids undermining sponsors?
10. **Native calibration:** are tiny heat modifiers sufficient, or would clearly disclosed movement changes add enough pilot identity to justify the execution costs?
11. **Jury-rig risk:** is forecastable strain/thermal exposure more fun than a disclosed reliability roll? Which repair tier creates distinct decisions?

### Working design decisions (subject to prototype validation)

- Any pilot can use any HAR; HAR signature identity stays fixed. Native calibration is a **soft Tier 2 experiment**, not a lockout or required penalty.
- Routes can fail for real but ordinarily fail forward; routine losses do not erase a save.
- Tournament-scoped money/damage reset; no cross-tournament debt or stacking injuries.
- Relationships use trust, respect and affection; combat unlocks are not gated on romance.
- Hybrid brackets and rule-based opponent adaptation are baseline proposals; full ML Shadow AI is not required.
- Automatic safe ejection in ordinary bouts; lethal mechanical consequences remain an explicit open question.
- Spectator hype and underground support are optional, capped **in-game** mechanics; underground odds are not a real-money gambling feature.
- Jury-rigged repairs are a candidate distinct from guaranteed patches and full restoration; no untelegraphed mid-match failure is assumed.
- Genre label: single-player fighting RPG / career simulator with tournament-scoped roguelite elements.

## 12. Ranked proposals and disposition (v0.3)

**Ranking objective:** strengthen the distinct *mech damage → economic strategy → adaptive rivals → personal/corporate stakes* loop while controlling technical, balance and content risk. Ratings: **H / M / L** for fit, differentiation, and estimated implementation cost. All cost/differentiation scores are design judgments, not verified market data. **Tier 1 is a design priority, not a launch guarantee.**

### Tier 1 — Core design directions (adopt; implement in stages)

| # | Proposal | Origin / precedent | Fit | Diff. | Cost | Scope / rationale |
|---|---|---|---|---|---|---|
| 1 | **Three-stage localized damage with fairness guardrails** | New; extends v0.1 §5.1 | H | H | M | Operational/damaged/critical; predictable effects and counterplay before complex part targeting. |
| 2 | **Strategic repair/preparation/insurance economy** | Expands old #8; *Armored Core* | H | H | M | Real opportunity costs, purse-minus-expenses, loss-tail tests, recovery without grinding. |
| 3 | **Fail-forward tournament losses** | Old #1; *Hades*, *Disco Elysium* | H | M | M | Alternate qualifiers, fallback brackets or story branches; real failure remains possible. |
| 4 | **Rivals remember and evolve** | Old #4; *Shadow of Mordor* conceptual comparator | H | H | M | Bounded rival history changes dialogue, loadout, sponsor and rematches; legal scope unverified. |
| 5 | **Rule-based, personality-first opponent adaptation** | Practical subset of old #3; *Killer Instinct* Shadows, *Tekken* Ghosts | H | H | M | Observable habits, capped reactions and clear counter-adaptation; no ML dependency. |
| 6 | **Hybrid dynamic tournament ecosystem** | New; builds on old #10 | H | H | M–H | Simulate ordinary brackets/offscreen progression with authored narrative anchors. |
| 7 | **Heat and risky overclocking** | Old #5; *MechWarrior* | H | H | M | Power-vulnerability tradeoffs; consolidate rage/desperation if used. |
| 8 | **Multidimensional relationships** | New; expands v0.1 §7 | H | H | M | Separate trust, respect, affection; optional romance and real conflicting loyalties. |
| 9 | **Mentorship teaches pilot techniques** | Old #2; *SF6* World Tour | H | H | M | Training/sparring, not affection purchases; works with any HAR without copying signatures. |
| 10 | **Sponsors with competing agendas** | New; expands v0.1 §§5,7 | H | H | M | Contracts alter resources, access, reputation, relationships and story; refusal possible. |
| 11 | **Fixed signature HAR identities and physics-fidelity baseline** | New clarification; original *OMF 2097* | H | H | M | Protect individual robot movesets, physical feel and readable combat despite modules/3D. |
| 12 | **Consequential relationship-versus-bracket dilemmas** | New; expands v0.1 §7 | H | H | M–H | Honest win, throw, expose manipulation or protect someone; authored outcomes constrain complexity. |

### Tier 2 — Strong additions (selective implementation)

| # | Proposal | Origin / precedent | Fit | Diff. | Cost | Scope / rationale |
|---|---|---|---|---|---|---|
| 13 | **Deliberate limb-targeting tactics** | Old #7; *Bushido Blade* | H | M | M | Makes damaged regions strategically targetable; avoid runaway attrition. |
| 14 | **Emergency power rerouting** | New | H | H | M | Temporary transfer of strength/mobility/cooling from one subsystem to another; fairness-first prototype. |
| 15 | **Environmental engineering** | New; extends original arenas | H | H | M | Magnetic, electrical and destructible positional tools with reliable counterplay. |
| 16 | **Fight modifiers and sponsor conditions** | Old #9; *MK11* Towers of Time | H | M | L | Reusable contract objectives and arena conditions; easy variety if not arbitrary. |
| 17 | **AI circuit, rankings and reputations** | Old #10; *Virtua Fighter 4* Quest | H | M | M | Named competitor ladder, linked to hybrid tournament simulation, not a second progression mode. |
| 18 | **Horizontal pilot progression** | New | H | M | L–M | More moves/options/knowledge, little permanent raw stat inflation. |
| 19 | **Experimental / illicit technology** | New | H | H | M | Limited risky modules, variable legality, conspiracy clues; preserves HAR identities. |
| 20 | **Limited modular HAR parts** | Old #18; *Custom Robo* | M | M | H | Few universal or HAR-compatible slots; forbid wholesale signature-move substitution. |
| 21 | **Readable pattern bosses** | Old #11; *Punch-Out!!* | M | M | M | Asymmetric HARs with learnable cues and non-cheating counterplay. |
| 22 | **Armor-break visuals** | Old #13; *Soulcalibur* | H | M | L–M | Readable mechanical damage if asset pipeline allows; do not alter hitbox visibility. |
| 23 | **Stage transitions and escalating hazards** | Old #12; *GG Strive*, *DOA* | H | M | M | Can extend environmental engineering without overloading every stage. |
| 24 | **Broadcast, public reputation and corporate PR** | Expands old #17; *WWE 2K* MyRise | H | M | M | Commentary and offers react to fighting style and career choices; avoid opaque reputation grids. |
| **24a** | **Spectator Hype and Underground Odds** | New addition | **H** | **H** | **M** | Public spectacle builds capped hype from stylistic play, risk-taking and clutch comebacks; may unlock fictional underground support or emergency fan repairs without corporate reliance. Prevent farming and real-money wagering (§5.4a). |
| **24b** | **Manufacturer Calibration & Native Affinity** | New addition | **H** | **M** | **L–M** | Native chassis profiles preserve pilot identity without lock-out; non-native HARs may incur mild, visible ergonomic costs (e.g., heat or documented dash recovery), reducible through calibration (§4.4). |
| **24c** | **Field-Expedient “Jury-Rigged” Scrap Repair** | New addition | **H** | **H** | **L–M** | Intermediate scrap-based repair tier restores more function than cheap patches at less than full-repair cost, trading predictable heat/strain exposure or a clearly disclosed reliability risk; avoid surprise failures (§5.2). |

### Tier 3 — Prototype / conditional / defer until justified

| # | Proposal | Origin / precedent | Fit | Diff. | Cost | Scope / rationale |
|---|---|---|---|---|---|---|
| 25 | **Advanced full-fight Shadow AI** | Advanced version of old #3; *Killer Instinct*, *Tekken* | H | M | H | Experiment only if bounded scripted adaptation proves inadequate; distinguish from #5. |
| 26 | **Safe ejection with exceptional lethal-match consequences** | Revised old #6; *Titanfall 2* | M | H | M | Automatic safe ejection by default; marked exceptional stakes only; no compulsory QTE. |
| 27 | **Desperation overclock window** | Old #14; *Garou* TOP | M | L–M | L | Merge into heat #7 if beneficial; do not add independent rage resource. |
| 28 | **Viewpoint-switching chapters** | Old #15; NetherRealm story modes | M | L | M | Author-costly; may be valuable for key shared-plot moments after core route works. |

### Tier 4 — Park or decide as production format

| # | Proposal | Origin / precedent | Reason to park |
|---|---|---|---|
| 29 | **Separate overdrive / transformation mode** | Old #16; *Bloody Roar* | Conflicts with focused heat/overclock resource; reconsider only if unique HAR demands it. |
| 30 | **Persistent neural feedback/stress penalties** | Old #19; OMF lore connection unverified | Overlaps with mechanical injuries; risks stacking punishments across tournaments. Narrative neural themes may remain. |
| 31 | **Persistent injury/stress roster** | Old #20; *Darkest Dungeon*, *XCOM* | Death-spiral risk, high UI/balance burden, conflicts with run resets. |
| 32 | **Visual-novel story layer** | Old #21; *BlazBlue*, *Persona 4 Arena* | Delivery/production format rather than a core design choice; decide after dialogue and scene needs are established. |

### Traceability to the original 21 proposals

The original list was **re-ranked, not silently discarded**. Old IDs map as follows; **#24a–#24c are new additions to v0.3, not reassignments of any original proposal**:

| Old v0.1 IDs | New v0.2 IDs | Decision |
|---|---|---|
| 1, 2, 4, 5 | 3, 9, 4, 7 | Retained as core, with targeted revisions |
| 3 | 5 + 25 | Split affordable rule-based adaptation from advanced learned Shadow AI |
| 6 | 26 | Moved to conditional; ordinary defeat uses safe ejection |
| 7, 8, 9, 10 | 13, 2, 16, 6 + 17 | Retained/merged into refined systems |
| 11, 12, 13 | 21, 23, 22 | Retained as strong additions |
| 14, 15, 16 | 27, 28, 29 | Conditional or parked |
| 17, 18 | 24, 20 | Expanded / constrained |
| 19, 20, 21 | 30, 31, 32 | Parked or format-only |

### Constraints and sequencing

1. **One carrier of persistent mechanical penalties at most.** Narrative flags, reputation and relationships persist by design; debt, injuries and stress do not accumulate together. The current default has **none**.
2. **Rival memory ≠ adaptive combat AI.** Career history and round-by-round habit detection can function independently; advanced ML is strictly optional.
3. **One primary risk meter.** Heat/overclock is the favored prototype; do not automatically add separate rage, desperation and transformation meters.
4. **One clear HAR signature.** Modules, training and rerouting should not make robots indistinguishable.
5. **Do not interpret priority as implementation order.** Before pursuing most items, validate two robots, enjoyable classic combat, and a consequential repair decision.
6. **Hype ≠ reputation, and fictional odds ≠ wagering.** Cap emergency support and keep it separate from cash-out or monetized bets; make skilled defensive performance eligible.
7. **Native is not exclusive.** All pilot–HAR combinations remain available, input-consistent and viable; disclose and tune any ergonomic modifiers.
8. **Jury-rigging is a meaningful third repair option.** It must differ from both a guaranteed degraded patch and a full repair, with legible risk and no arbitrary forced defeat.

## 13. References (design precedents; not an independent verification review)

- *One Must Fall 2097*: pilot × HAR split, tournament economy, arena physics.
- *Street Fighter IV–6*: 2.5D presentation, optional modern controls.
- *MechWarrior / Armored Core*: localized mech damage, heat, repair/preparation economics.
- *Fire Emblem: Three Houses*: shared plot and route-specific perspectives.
- *Hades*: relationships integrated with replayable action; fail-forward structure.
- *Virtua Fighter 4* Quest: a ranked circuit with individual competitor profiles.
- *Killer Instinct* Shadows / *Tekken* Ghosts: precedents for player-habit-responsive opponents.
- *Punch-Out!!*: readable, personality-driven asymmetric bosses.
- *OpenOMF*: [openomf.org](https://www.openomf.org/), an open-source OMF engine remake; evaluate as a technical reference after checking its current status and licensing.

---

### Revision summary (v0.1 → v0.3)

- Preserved the original concept, 2.5D classic combat, authored pilot routes, all-HAR pilot compatibility, optional romance, and tournament-scoped economic resets.
- Made **localized damage** predictable and strategically recoverable; added three damage states and limited emergency power rerouting.
- Turned the economy into **repair vs preparation vs insurance**, with recovery tests beyond the positive expected-value target.
- Defined **heat/overclock** as the preferred mech-specific resource; reduced competing gauges.
- Added **hybrid evolving tournaments**, **sponsor politics**, **corporate reputation**, **experimental technology**, and **environmental engineering**.
- Replaced one-dimensional affinity with **trust/respect/affection** and framed learned pilot techniques around training rather than romance.
- Split AI into **personality + bounded rule-based adaptation**; deferred expensive full-match learning.
- Defaulted routine losses to **safe ejection** while preserving explicitly marked high-stakes match possibilities as a decision.
- Added a **two-HAR microprototype** and clear validation gates before the originally proposed vertical slice.
- Renumbered all **21 original ranked ideas**, retained or merged them explicitly, and included a traceability table.

### v0.3 addition log (relative to v0.2)

- Added **#24a Spectator Hype and Underground Odds** with capped, fictional, non-monetized underground/fan support; distinguished momentary hype from lasting public reputation (§5.4a; §6).
- Added **#24b Manufacturer Calibration & Native Affinity** while retaining universal pilot–HAR compatibility; limited ergonomic friction and required transparent frame/heat reporting (§4.4; §5.3).
- Added **#24c Field-Expedient “Jury-Rigged” Scrap Repair** as a separate repair tier; recommended forecastable heat/strain instead of unpredictable mid-fight component failure (§5.2).
- Updated open questions, risks, explicit constraints, and the Tier 2 matrix without changing the original #1–#32 identities.
