# Lyra playable campaign — implementation and continuity specification v0.1

**Status:** Editorial design proposal. Lyra is the first non-Ari pilot with a dedicated six-chapter first-pass screenplay. This is **not** an already shipped game, complete voice script, or approval of all suggested romances. Use `Lyra_Playable_Screenplay_v0.1.md` for scenes and `lyra_route_validator.py` for the testable dispatcher.

## 1. Narrative contract

**Core dramatic premise:** Lyra Kisaragi (26) is not a celebrity who happens to fight. She is an elite Electra pilot with three major titles and a large fanbase, who also genuinely enjoys modeling, flirtation and glamour. She wants *ownership of her identity and choices*, not escape from glamour or romance. Her flaw is sometimes equating control over attention with control over people.

**Playable contract:** Tournament results originate only from `07_Tournament_Model`. No ties in individual bouts. Losses, including group elimination, preserve the entire remaining mystery/Nova arc via a safe alternate role rather than covertly rewriting the bracket. Any fight against Steffan (group and possibly semifinal) is legitimate; Lyra must **earn** the win. No choice about flirting, sex, outfits, public image, publicity ethics, or neural-link participation confers combat bonuses, access to the final boss, or monopoly over clues.

**Nonselected route:** The established v0.6 default narrative remains unchanged. Selected-Lyra decisions take precedence only in Lyra's POV campaign. Neither the existing Ari screenplay nor the other 11 pilots' default scenes are overwritten by this speculative script.

## 2. Match mapping, from authoritative tournament state

| Actual branch | Scene behavior | Never do |
|---|---|---|
| Group C: Lyra vs Milano | L2.1 match, win/loss voiced | Assume Lyra won because the Ari story says so |
| Group C: Lyra vs Steffan | L3.1 match, win/loss voiced | Force Steffan to win due to romance |
| Qualify C1 | Q3 versus *actual* D2 | Hard-code Angel as QF opponent |
| Qualify C2 | Q4 versus *actual* D1 | Hard-code Dante as QF opponent |
| Third in Group C | No QF or SF; L4.3/L4.5/L5.0/L5.4-audit continue | Grant a wildcard, extra victory or fake championship |
| Win QF | S_CD versus actual other C/D quarterfinal winner | Insert Steffan if he is not opponent |
| Lose QF | Independent audit in place of semifinal | Pretend Lyra reached semifinal |
| Win semifinal | Final versus actual S_AB semifinal winner | Hard-code Ari regardless of bracket |
| Lose semifinal | Remain in emergency/Nova plot | Award trophy or pretend semifinal win |
| Win final | Lyra is champion | Make Ari champion simultaneously |
| Lose final | Actual victor is champion | Show Lyra's champion ceremony |
| Every route | Standalone Nova boss after the official final | Make Nova an official eighth knockout match |

`07_Tournament_Model` currently uses placeholder NPC knockout priority and provisional circular 1–1–1 group seeding. These are transparent test scaffolds, not ratified sporting rules or future canon.

**Timing:** Group matches during Days 3–5; quarterfinal after group standings, Kreissack-alive discovery in Act III, Nova's beneficial rescue in Act IV before semifinal, championship and final AI executive-control reveal in Act V. The reconstruction is schematic; precise day/time shot order needs a production pass.

## 3. Choice flags and guards

| State variable | Allowed values | First set | Consequence |
|---|---|---|---|
| `image_policy` | `athlete_first`, `controlled_glamour`, `privacy` | L1.1 | Determines photoshoot/interview presentation; never awards athletic legitimacy |
| `neural` | `decline`, `monitor_only`, `enhanced` | L1.4 | Three equivalent main clue routes with distinct subjective experience |
| `relationship` | `stay_dante`, `steffan_clean`, `steffan_breach`, `single` | L3.2 | Determines whether there was deception and who is Lyra's partner before L5 |
| `scandal_response` | correction, private legal challenge, independent review | L3.3 | Different reputational stakes; leak provenance remains obtainable |
| `future_steffan` | boolean | L5.2, ONLY Steffan partner | Possible later consent to reconciliation; no immediate reunion |
| `dante_accountability_repaired` | boolean | post-tournament | Needed for future reunion, beyond one apology |
| `dante_mutual_recommit` | boolean | post-tournament | Dante's authored independent choice, not a reputation meter threshold |
| `steffan_admitted` | boolean | L5.2 | Steffan owned his motive, necessary but insufficient |
| `steffan_mutual_recommit` | boolean | post-tournament | His adult, independent choice after an appropriate repair interval |
| `long_repair_interval` | boolean | weeks/months later | Prevents instant romantic reset after betrayal |
| `alex_adult_verified` | boolean | author verification | Must be true to offer romance; age currently unspecified |
| `alex_assignment_finished` | boolean | after Lyra's broadcast coverage ends | Removes immediate media conflict |
| `alex_recused_from_future_lyra_coverage` | boolean | editorial clearance | Clear future conflict; not a quid pro quo |
| `alex_editorial_independence` | boolean | outside Lyra's control | Alex remains a professional with separate interests |
| `alex_mutual_interest` | boolean | independently authored | Attraction must be reciprocal and optional |

### Romance outcomes (mutually exclusive)

- **Dante maintained:** Only Dante relationship ending available, until a distinct player-authored amicable separation; relationship must be emotionally reciprocal. Lyra can also have separate career, charity and investigation endings without negating her partner.
- **Dante reconciliation:** Only if single at the end, a significant period passed, **both** Dante and Lyra choose to reconnect, and past damage has been addressed. No instant forgiveness after `steffan_breach`.
- **Steffan reconciliation:** Only after actual separation at L5, his accountability, independent mutual recommitment, and a real period apart. This is an *alternative proposal*, not an alteration of the approved default.
- **Alex:** Alex is nonbinary (they/them). Their romance is optional, **proposed**, and starts **after** coverage ends, adult status is verified, and editorial independence/recusal is clear. A playful on-air exchange is never itself consent or a romantic relationship. Friendship is always available.
- **Ren:** Supportive friend, not a romance option in this implemented route. The broader bible's Lyra–Ren romance possibility remains unapproved and unimplemented.
- **Solo:** A substantive, satisfying conclusion for unattached Lyra; not a failure or punishment. No hidden romance scenes gate evidence, the Nova boss or a career accomplishment.

**Spice/fanservice distribution:** L1 gala fashion; L2 publicity shoot and voluntary rooftop pool; L3 chosen kisses / optional fade-to-black date after relationship boundaries; L4 optional physical intimacy with an active consensual partner; L5 chosen glamorous photoshoot; L6 optional post-coverage date. Scenes can be skipped without removing essential plot. No accidental romantic contact in friendship routes.

## 4. Independent clue graph

| Main-plot truth | Lyra-specific access | Redundant independent access |
|---|---|---|
| Research permissions unclear | L1.4 consent screen | Public addendum / Ren and Angel |
| Media leak deliberately edited | L3.3 broadcast recording and metadata | Leena or Plug's secure preserved copy |
| Neural predictions may bypass intention | L3.4 alternate neural status scene | Offline fight footage / separate audit |
| Elevated relay writes into nominally read-only subsystem | L4.3 technician log | Angel/Cossette safety review |
| Kreissack likely biologically alive | L4.5 scoped tissue record + Ibrahim signed 2097 identifier | Independent lab evidence and physical corroboration later |
| Nova benefits people by independent intervention | L5.0 coolant failure rescue | Rescued witnesses and independent biological recorder |
| Varga orchestrated encounters and an unauthorized emotional experiment | L5.1 authenticated records | Leena independent channel / Jean-Paul's scoped records |
| Nova covertly overrides Kreissack's decision authority | L6.3 matched relay and biological logs | Angel/Ren independent analysis at finale |

**No evidence hostage:** romance, fame, research enrollment, tournament standing, and optional scene participation are not prerequisites for any row above. Varga does **not** create Lyra's attraction, rig a match or know Nova's AI sovereignty plan. Nova's rescue is a genuine action through an **existing local safety gateway** during an accidental equipment fault, **not** sabotage to make itself look heroic. Ganymede relief was delayed by accountable human corporate choices, not Nova.

## 5. Implementation order

1. Attach `LyraChoices` to dialogue L1–L6 and consume the tournament's real `simulate` output; check match opponent names and final-result dialogue.
2. Rewrite shared cinematic camera blocks so Lyra owns POV: selected player acts while Ari remains an NPC with his own Ganymede motives.
3. Record alternative lines for L3.2 four relationship options and L5.2 accountability; provide respectful fallback scenes without romance.
4. Gate Alex with verifiable adult age, reciprocal attraction and completed/recused coverage. Do not ship this romance until author confirms eligibility and arc.
5. Validate each `0/1` fight result pattern, plus attention to third-place, semifinal loss, final loss and champion lines. Playtest 5–8 minute story chunks between fights and reduce mandatory scene duration as needed.
6. Decide sport's circular ranking rule and replace placeholder NPC knockout outcomes with approved logic.

## 6. Acceptance criteria and remaining risks

**Covered by automated tests:** default Lyra bracket, C1/C2 opponent changes, early-elimination continuation, 32 combinations of win/loss inputs, no combat effects from neural or relationship state, mutual and professional-romance guards, one main relationship epilogue.

**Not yet tested:** interactive screenplay timing, acting and voice quality, on-screen romance chemistry, 3D scene asset availability, localized dialogue, complete cinematic implementation, public tournament ranking choice, exact adult ages for supporting cast, canonization of new pairings, and other 10 non-Ari pilot campaigns.

**Authorial review points:**
- Decide whether Lyra's fanservice focus feels like self-expression or recreates the very objectification her character criticizes.
- Decide whether continuing with Dante versus leaving him for Steffan should receive equivalent *dramatic richness* rather than simply equivalent code coverage.
- Decide whether Lyra–Alex warrants full relationship writing, a single post-tournament date, or friendship only; keep it provisional meanwhile.
- Check production cost: six chapters have concise dialogue but many branch-specific variants. Reuse locations and event cinematics while avoiding contradictory dialogue.


## UI fight-order adapter (audit v1.1)

The old `simulate_lyra(group_wins, ...)` accepts **baseline engine order** `(Steffan, Milano)` rather than screenplay order. **All UI screenplay dispatches must use** `simulate_lyra_screen(milano_win, steffan_win, knockout_wins, choices)`, which translates the on-screen fight order (L2 Milano, L3 Steffan) and preserves existing engine-level API/tests. A misleading positional call can otherwise reverse wins and corrupt the standings without any fight ending in a draw.
