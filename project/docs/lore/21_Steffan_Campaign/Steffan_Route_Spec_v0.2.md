# OMF 2107 — Steffan Thomas playable route specification v0.2

**Canonical character direction:** `02_Story_Bibles/Steffan_Character_Addendum_v2.1.md`. **Screenplay:** `Steffan_Playable_Screenplay_v0.3.md`. **Executable:** `steffan_route_validator.py`; `test_steffan_route_validator.py`. All new dialogue, optional Steffan–Dante romance and Lyra long-term reconciliation are **editorial proposals**. Steffan's baseline intelligence, emotional immaturity, envy, denied attraction and domination are user-established.

## Official fight routing

Steffan appears in Group C with Lyra and Milano. The scene order is **GC2 (Milano) then GC1 (Lyra)**; the tournament engine consumes **GC1 (Lyra) then GC2 (Milano)**. The adapter maps input values accordingly. GC3 is the NPC match Lyra–Milano, default Lyra wins. Every match has one winner and one loser. Circular equal *records* are resolved by public provisional seeding (Steffan, Lyra, Milano), not by drawn fights.

| Standing | Official quarterfinal | Default opponent if unchanged | Possible next stages |
|---|---|---|---|
| C1 | Q3 | Dante (D2) | S_CD → FINAL, only if actual wins |
| C2 | Q4 | Angel (D1) | S_CD → FINAL, only if actual wins |
| C3 | none | none | investigation, real Nova emergency only |

Default selected results: Steffan beats Milano and Lyra, beats Dante at Q3, loses semifinal to Lyra. Ari then wins default final against Lyra. All real alternative opponents derive from the simulator; no one creates or cancels a fight to satisfy a romantic scene. NPC knockout priority and circular seeding remain provisional; they must be tagged as such until authored.

## State and eligibility

`SteffanChoices` has explicit allowed values for persona, Lyra approach, private behavior, evidence policy, technical role, Day-11 admission, Dante emotional truth, and future relationship intent. Ending intent can be solo, friendship, Lyra or Dante but not simultaneously both romances.

**Default:** `showman`, `strategic_seduction`, `press_for_control`, `full_admission`, `deny`, `solo`; these are route demonstration defaults, not proof of each unshown moment. Since the default is Lyra's Day-11 breakup, there is no same-night permanent Lyra ending. Nor is Dante automatically available.

**Lyra future proposal gates:** Lyra's actual choice to date him earlier (or authored mutual relationship history), prior Dante commitment cleared, her independent future reciprocal choice, a substantial post-tournament interval, meaningful accountability and repair, both single and consenting, no recorded coercive control, Steffan having acknowledged his responsibility. If any gate is absent, continue as separated/unresolved. Her career and achievements do not change.

**Dante future proposal gates:** Steffan explicitly acknowledges attraction; Dante is an adult, free of incompatible commitments, voluntarily reciprocates, expresses active consent, and Steffan has addressed relevant harms. A later interval is required and Lyra's relationship, if it existed, has formally ended. Steffan's recorded coercive control is disqualifying pending an authored repair path (not provided in this version). Any missing gate → no romance.

**Control distinction:** Consensual private assertive flirting may be written if the scene explicitly establishes mutual choice. A controlling approach (`press_for_control`) or recorded coercion cannot be re-labeled consent and is not eligible for either romantic ending in this first-pass model. This is a conservative guard pending a more nuanced repair system, not a claim that every controlling act makes reconciliation logically impossible.

## Investigation and scene clocks

| Clock | Scene / fact | What can be known |
|---|---|---|
| D0–1 | ST1.1–ST1.3 | Persona, envy and emotional dissonance; public footage |
| D2–4 | ST2.1–ST2.4 | GC2; public biometric-analytics fingerprint without illegal data access |
| D5–7 | ST3.1–ST3.4 | GC1, relationship decisions, leak; no fixed-match theory |
| D8–10 | ST4.1–ST4.4 | Official QF if qualified; Angel/Ren corroborate Kreissack alive |
| Day 11 | ST5.1 | Independent Varga custody and protected Lyra notice, optional Steffan admission, breakup if default couple |
| Day 12 | ST5.2, then ST5.3 | Real autonomous rescue then actual S_CD if qualified |
| Day 13 | ST6.1–ST6.5 | Actual official final first; then Nova conditional veto and unique core destruction |
| Day 30 | ST6.6 | Independent authenticated E5 Kreissack Devroe order, never a Day-13 clue |

- Steffan's evidence contribution consists of *media timing and public procurement anomalies*, supplementary to Angel/Ren's independent neural proof and Christian's independent Devroe records. Self-serving choices compromise Steffan's credibility but cannot erase others' custody.
- Varga may manipulate schedules/encounters and record private emotion without permission; neither she nor Steffan gains control of authentic desire or match results.
- Shared physical finale is official final → Kreissack failed control → executive gateway damaged → relay isolated → destruction initiated → attempted ejection → regained latch control → unique Nova/Kreissack core destroyed. Kreissack's final line is **“Apparently, I can still surprise you.”**
- No route has a guaranteed romantic payoff, false official champion, Nova fight counted as a championship round, miraculous replay of eliminated fights, or a premature Day-30 revelation.

## Outstanding author decisions

1. Whether the proposed Steffan–Dante mutual romance is approved canon *as a possible branch*; Dante's reciprocity is currently unestablished.
2. Exactly what forms of domination Lyra enjoys by choice and which specific coercive choices Steffan might make in the darker path.
3. Whether some future Steffan–Lyra reconciliation route should exist, and what independently observable repair would make it narratively credible.
4. Real-world story implementation still needs a single cross-campaign relationship store. This validator is local and cannot by itself prove Dante and Lyra made compatible decisions in their separate playable campaigns.
5. Official final NPC pairings and provisional public seeding still require nonplaceholder narrative authoring.


## v2.3 — Dante romantic defaults and elective path (author-approved direction)

Dante's default feelings toward Steffan are **nonromantic**. This does not alter Steffan's denied attraction, his actual ability as a fighter, his troubled Lyra history or his Day-11 confrontation. The player may alter Dante's course through an authored progression (`curiosity` → `listen` → `explore`), with newly developing attraction rather than a secret predestined romance.

The local Steffan dispatcher accepts external booleans `dante_reciprocates` and `dante_independent_consent`; **these must only be true when the canonical cross-POV world state confirms player-developed mutuality**, not merely because Steffan admits his feelings. A unified relationship-event store is not yet implemented. New active Steffan screenplay: `Steffan_Playable_Screenplay_v0.3.md`.
