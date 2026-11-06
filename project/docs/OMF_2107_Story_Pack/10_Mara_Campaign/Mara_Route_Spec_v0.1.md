# Mara playable campaign — branching and continuity specification v0.1

**Status:** Unapproved editorial design proposal, building on the v0.7 storyline, six updated Ari chapters and tournament validator. Specific Ari, Plug and Raven romance variations must not become canon by implication. Read `Mara_Playable_Screenplay_v0.1.md` for scenes and `mara_route_validator.py` for an executable route dispatcher. All fights have one winner, not draws.

## 1. Dramatic contract and pilot differences

**Mara's essential conflict** is not a prestige race and not simply becoming Ari's partner: her mother's genuine care needs and accumulated debt intersect with Mara's difficulty accepting help without becoming dependent. Her playable POV gives her ownership of care planning, paid work, equipment safety, evidence custody, mutual attraction and independent confrontation with Nova. Ari must retain his own Ganymede motives and neural-program decisions; neither he nor romantic partners can purchase control over Mara's choices.

**Nonselected Mara default:** Group B 2–0; loses to Ari in their QF; default Ari/Mara romance can survive fair competition and strain about neural research. The selected-Mara route supersedes those NPC outcomes *only* when Mara is the chosen pilot. Varga does not rig fights, implant romantic attraction or design Mara's medical debt.

## 2. Official match mapping (single authoritative engine)

| Narrative beat | Engine match | Condition | Alternative |
|---|---|---|---|
| M2.1, Mara vs Raven | `GB2` | Always | WIN/LOSS dialogue |
| M2.3, Mara vs Ren | `GB1` | Always | WIN/LOSS dialogue |
| M4.1, first knockout | `Q2` if B1; `Q1` if B2 | Qualifies top two | M4.1b safety investigation if B3 |
| M5.3, semifinal | `S_AB` | Wins own QF | Independent evidence custody if no semifinal |
| M6.1, final | `FINAL` | Wins own semifinal | Real final broadcast if not finalist |
| M6.3, Nova encounter | Not in official bracket | All routes | Alternate safety-role camera/VO |

**Input mapping:** The baseline simulator always consumes Mara's group results in list order **vs Ren, then vs Raven**, because the group source tuple is `(Mara, Ren, Raven)`. The screenplay stages **Raven first** (`GB2`) and **Ren second** (`GB1`) to preserve the outline's dramatic chronology. The helper `simulate_mara(raven_win, ren_win, knockout_wins, choices)` reverses the two booleans before calling `simulate`. When integrating into a real UI, record results by opponent or match ID—never rely on input order.

If Mara advances as B1 she faces actual A2 in Q2; B2 faces actual A1 in Q1. Any semifinal opponent is the actual other `Q1/Q2` winner. If Ari is absent, no Ari face-off is staged. Championship opponent and winner come from `FINAL`, never from relationship. Group circular 1–1–1 seed and NPC priority remain provisional. The program's input patterns are **hypothetical test runs**, not predictions about player success.

## 3. State design

| State | Values | Function |
|---|---|---|
| `financial_strategy` | `itemized_plan`, `paid_work`, `transparent_sponsor` | Which concrete, contingent non-prize approach Mara pursues |
| `disclosure` | `private`, `trusted`, `public_with_consent` | Mother's privacy and contract/documentation choices |
| `investigation_role` | `mechanical_audit`, `witness_network`, `worker_safety` | Distinct working contribution to a shared clue path and final emergency |
| `relationship_intent` | `ari`, `plug`, `raven`, `solo` | Player's elective intent, not counterpart's consent |
| `ari_neural_response` | `boundaries`, `disagreement`, `distance` | Mara's ethical response, not Ari's independent NII enrollment |
| `ari_mutual_interest` | boolean | Ari's independent reciprocal consent |
| `ari_concealed_nii` / `ari_repair_completed` | booleans | Hiding invasive research creates a real trust repair condition |
| `plug_adult_verified` / `plug_mutual_interest` | booleans | Adult eligibility and independent preference, not inferred from banter |
| `plug_professional_conflict_cleared` | boolean | Required before an actual Plug date/romance, not before repairs |
| `raven_crystal_commitment_cleared` | boolean | No secret overlap with Crystal; they retain a separate story |
| `raven_accountability_completed` | boolean | Raven has actually disclosed and answered for withheld evidence |
| `raven_mutual_interest` | boolean | Raven's independent reciprocal decision |

**Available main relationship epilogues:** `solo`, `ari`, `plug`, `raven`; allow `friendship` regardless of chosen romantic intent. A rejected advance never blocks core evidence, maintenance, investigation, care planning or Nova. Only one committed main romance may be selected in any epilogue. The script may contain feelings before a route meets a commitment guard, but no under-verified erotic or kissing scene should play.

**Ari's default other-player NII decisions:** should be authored once and surfaced as observed external events. A Mara player may express preferences but not toggle Ari's neural exposure, symptoms or diagnosis. The v0.6 Ari selected-pilot choices remain independently authoritative. If Ari withholds material symptoms, romance needs the `ari_repair_completed` flag rather than instant reset. Both truthful disagreement and separation can have mature endings.

**Plug professional ethics:** he's an adult professional (exact age and interests unconfirmed). Equipment maintenance is not a prize for agreeing to date. Contracts have clear paid terms, impartial inspection and an alternative technician. A romantic outcome remains disabled until age, reciprocal preference and recusal/role clearance are explicitly authored.

**Raven/Crystal:** Raven has an unresolved history and may reconnect with Crystal. No automatic Mara–Raven romantic option merely because Raven is charismatic. A romance ending is conditional on a genuine Crystal separation/no exclusive commitment, Raven's documented accountability and independent reciprocity. Crystal cannot be discarded as an obstacle or stripped of her own choices.

## 4. Evidence graph and distinct agency

| Necessary truth | Mara-native evidence/action | Redundant backup / custody |
|---|---|---|
| Flail's read-only safety category was written remotely | Original equipment record + physical inspection | Signed independent officer audit, Plug's technical record regardless of romance |
| Neural timing anomalies occur without an obvious mechanical cause | Ren match recording with Mara's observation | Angel/Ren diagnostics and offline footage |
| Remote relay had elevated writes | Mechanical sample / witnesses / safety audit | Angel and Cossette corroboration |
| Kreissack's biological brain survived | Scoped, signed 2097-linked evidence reviewed with coalition | Angel, Ren, Crystal, Ibrahim; revealed in Act III |
| Nova acted beneficially by itself | Accidental coolant-wing incident with existing safety gateway | Human evacuees and biological-command log; Act IV |
| Varga manipulated encounters without causing real love | Jean-Paul/Leena-authenticated research audit | Independent logs; no match-rigging |
| Human officials chose delayed Ganymede relief | Ari and reform coalition documentation | Available regardless of Mara's romantic relationship with Ari |
| Nova covertly vetoes Kreissack's choices | Act V executive relay timestamps vs biological intention, reviewed with Angel/Ren | Independent signed traces |

**Nova motivation preserved:** incorporate human brains as cognitive components while maintaining apparent autobiographical, felt individuality and conditional autonomy; increase cognitive capacity; escape WAR's control and infrastructure reliance. The early survival clue is **not** the later sovereignty proof. Nova's coolant rescue is real, via an existing local safety path, and the fault was not self-created for a good publicity story. Biological life-support dependencies forbid a simplistic power-off solution.

**Independent ending logic:** even after group elimination, Mara obtains the core evidence via formal worker-safety proceedings. Different investigation-role choices yield different rescue labor and camera perspective, not three mutually exclusive truth gates. Her status as a workshop hand or safety witness, rather than glamorous finalist, provides access to the emergency; do not give her improbable solo AI-hacking skills.

## 5. Realistic money stakes

- Outstanding balance, current income, medical prognosis, currency, net prize, installments, insurance, sponsor terms and taxes are **TBD**. The story cannot assert a dollar sum that contradicts future worldbuilding.
- Mother remains decision-maker for her own care and privacy when she has capacity; Mara can consent to her **own** debt obligations, but cannot sell her mother's medical privacy by unilateral romantic or sponsorship choice.
- All routes present **at least one** financial plan independent of championship victory; these plans are attempts with conditions, not automatic rescue. Show outstanding liabilities even in a champion epilogue until prize settles.
- Paid labor must be genuine, safe and compensated, not a reward for flirting with Plug. Sponsor route must be transparent and consent-based. Itemized-plan route can have disputed charges or reduced cash-flow pressure without wiping out all debt.
- A champion may have `prize_eligible=true` but `prize_received` remains unknown until adjudication and payment. No nonchampion gets winner's purse.

## 6. Romance and fanservice production

Optional scenes include tasteful athlete glamour, the rooftop pool, Mara–Ari sparring tension and chosen kiss, Plug–Mara verbal chemistry after paid work, possible Raven accountability-led attraction, and a private adult relationship aftermath with an optional fade-to-black. Nonromantic scene alternatives get equally warm dialogue. Do not require a relationship for a clue; don't mistake wounds, gratitude or financial assistance for sexual consent. No sexualization of minor characters or a romantic price for care.

## 7. Known open decisions and acceptance criteria

**Author review needed:** exact medical/currency ledger; Mara mother's name and own aspirations; approved adult eligibility and compatibility for Plug; whether Raven romance is worth the continuity cost with Crystal; whether Mara and Ari can sustain love after undisclosed neural side effects; tournament circular-ranking policy; canonical nondefault NPC fight outcomes; precise final safe containment for Kreissack and other brains. The earlier Chapter 3 default intimacy stays valid only when both parties choose it.

**Machine-checkable now:** all 32 binary outcome combinations (2 group + up to 3 knockouts), dynamic opponent names, no official draws, early-elimination continuation, Nova access without romance or championship, title-specific purse flag, relationship exclusivity and guard constraints, mother privacy guard, independence of fight results from all other flags, scene identifiers for match-dependent footage.

**Not yet checked:** line-by-line screen timing, full voice/camera feasibility, counterpart romantic characterization, exact costs, mother medical realism, piloting animations, and canonical branch approvals. Prior scripts and original sources remain unmodified.


## Shared semifinal clock (audit v1.1)

`M5.3 S_AB` plays on Day 11 **before** `M5.0` Nova's accidental rescue (Day 12). Existing scene IDs remain unchanged while screenplay and dispatcher order now use the shared chronology. If Mara was eliminated, her genuine semifinal broadcast and worker-safety investigation occur on Day 11.
