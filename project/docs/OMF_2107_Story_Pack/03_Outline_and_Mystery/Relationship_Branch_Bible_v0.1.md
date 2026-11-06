# ONE MUST FALL 2107 — Relationship and Secondary-Character Branch Bible v0.1

**Status:** DESIGN PROPOSAL — not automatically established canon. 2026-11-01.
**Applies to:** cinematic story mode for each of the 12 selectable pilots; arcade mode gets a short route-specific introduction, mid-route encounter, and epilogue.
**Source baseline:** `Character_Bible_v1.0.md`, `Five_Act_Outline_v2.0.md`, `Story_Repair_Pack_v0.2.md`, `Decision_Log.md`, and the executable tournament model.

## 0. Canon firewall and creative targets

### Already decided — preserve

- Twelve playable pilots, each with a meaningful point of view; no forced romance. Ari is partly customizable; Mara is Ari's *default* slow-burn relationship, but friendship is an explicit, respected alternative.
- Lyra **starts** with Dante in the default continuity; she autonomously leaves him for Steffan, later learns of Steffan's initial ulterior motive and Varga's inappropriate intervention, ends that relationship, and **defeats Steffan in the default semifinal**. She is an elite athlete and celebrity in her own right. Player-controlled alternatives may change events without negating her agency.
- Steffan and Dante's fascination is intentionally ambiguous, not an established mutual romance. A route exploring reciprocity must be elective, not retroactively imposed.
- Crystal/Raven, Jean-Paul/Varga, Milano/Selene, Angel/Ren, and Ren/Lyra have the previously established histories or affinities shown in the Character Bible. Cossette/Ibrahim are an existing mature couple.
- Varga's unauthorized emotional research is a violation, even if Jean-Paul has genuine feelings. Her interference engineers opportunities and media leaks; it **does not create authentic attraction**, compel relationships, or rig fights.
- All matches are decisive. Group standings may have circular one-win records but no drawn *fights*. The tournament winner and match pairings are read from actual match outcomes, never the romance state.
- The Ganymede relief tragedy is a human political decision, not Nova's doing. Nova's brain incorporation preserves subjective personality/memories but covertly redirects incompatible choices. Neither romance nor match-winning is required to learn core evidence.

### Proposed design principles

1. **Autonomous counterpart:** Choosing flirtation expresses the player's interest; it never guarantees reciprocation. Each counterpart has commitments, attraction, preferences, boundaries, and a possible rejection.
2. **Several valid outcomes:** Romance, friendship, professional alliance, respectful distance, breakup, and reconciliation can all be satisfying and useful; a refused advance is not a game-over or secret penalty.
3. **No relationship as combat buff:** Romantic affiliation cannot alter hitboxes, controls, a required victory, tournament ranking, or access to the final boss. It may change support conversations, who volunteers, optional information paths, or epilogues.
4. **Chemistry through action:** Make choices consequential through disclosure, confidentiality, care under pressure, professional boundaries, honesty and sacrifice—not merely a number of flattering dialogue clicks.
5. **Professional ethics:** Leena's reporter/source relationship, Alex's broadcaster/subject relationship, Varga's researcher/participant relationship, and Haldane's authority over experimental subjects must be treated as actual conflicts. Romance may require recusal, an independent evidence custodian, or refusal; authority cannot be used to extract intimacy.
6. **Competent adults only:** All romantic characters must be established as adults before writing or shipping those scenes. Alex, Leena, Plug, and Christian are written as adult professionals; precise ages are unconfirmed. No assumptions about a partly customizable Ari's gender or everyone else's orientations/preferences; attraction compatibility needs authored character-specific decisions before implementation.
7. **Don't maximize pairings:** Not everyone is a romance candidate for everyone. A few carefully characterized secondary connections are better than a universal dating menu. Default ensemble events continue when another pilot is player-controlled, but adapt coherently to their choices.
8. **Explicit consent and communication:** Affairs or ethically compromised conduct may occur in the story, but should not be sold as a reward for deception. If exploring non-exclusivity, it requires transparent agreement and an authored route, not a hidden exploit.

## 1. Two independent branching layers

**Layer A — tournament:** groups, playoff opponents, winner, prize and fame, Nova access. Read only from real match results and investigation state.

**Layer B — social/political:** affinities, romantic intentions, consent, established relationship commitments, trust, disclosure, voluntary support, secondary-character careers. Read from choices and events. Cross-layer scenes may acknowledge a victory/loss, but the plot cannot substitute a predetermined champion for the actual winner.

Suggested minimal state, deliberately separate from the Repair Pack's older, Ari-centered romance enums:

```yaml
player_pilot: Ari                      # selected from 12 pilots
matches: {}                           # authoritative tournament validator result
social:
  ties:                              # each unordered pair stored once
    ari:mara: {bond: close, mutual_interest: true, status: dating, trust: 2}
    ari:leena: {bond: respectful, mutual_interest: false, status: none, trust: 1}
  chosen_primary_route: ari:mara      # optional; can remain null
  commitments:                       # existing couples; may change via own scenes
    lyra:dante: separated
    lyra:steffan: separated
  public_knowledge: {scandal: true, relationship_revealed: false}
  conflict_flags: {reporter_recused: false, research_boundary_violation: false}
  support_flags: {plug_warned: true, christian_shared_records: false}
investigation: {}                     # evidence independently obtainable
```

`bond`, `interest`, `trust`, `status`, `professional_boundary` and `public_knowledge` are conceptually separate. **The sample values above illustrate structure, not the default scripted ending.** A relationship may be intimate but untrusting; a committed friend can be deeply trusted without romance.

### Relationship lifecycle

`acquainted -> rapport -> optional interest -> mutual interest -> explicit commitment -> stable | strained | separated | repaired`.

Parallel transitions from `rapport` to `friendship`, `work partnership`, or `respectful distance`. Attraction and commitment cannot be inferred from charm alone. The other party must have an authored positive response. A reconciliation requires accountability and a renewed choice, not sufficient points.

### Playable-route exclusivity and global coherence

The selected pilot owns their own dialogue and decisions. Nonselected pilots have the **default** route unless directly and credibly changed by witnessed actions. For instance, Ari choosing Leena must not cause Lyra and Dante to reconcile magically; Angel choosing Ren must not automatically erase the established default Lyra/Steffan confrontation. A relationship is stored once globally; do not allow the same NPC to be simultaneously in mutually exclusive commitments unless all participants knowingly agreed to another structure.

## 2. Pilot-specific relationship menu

Entries marked **E** follow an established relationship/history (not necessarily its outcome). **P** are proposed, needing approval and characterization. A menu entry is an *opportunity to author a route*, not proof of attraction or guaranteed access.

| Player pilot | Existing / default emotional center | Proposed optional connection(s) | Important non-romantic / secondary interactions | Unique branch tension |
|---|---|---|---|---|
| **Ari** | **E:** Mara romance or friendship | **P:** Leena (reporter; only after clean editorial separation); Selene (ambitious political attraction) | Plug, Christian, Cossette, Imani | Personal intimacy versus the integrity of Ganymede evidence; Mara's independence; neural-link boundaries |
| **Mara** | **E:** Ari romance or friendship | **P:** Raven (trusted equal with secrets); Plug (technical rapport, contingent on reciprocal attraction and adult characterization) | Her mother, Dante, Cossette | Romantic solidarity cannot be used to buy her compliance or solve her debt offscreen |
| **Lyra** | **E:** Dante then Steffan, followed by autonomy in default | **P:** Alex (public/private-life tension; anchor recusal); possible Ren romance only if both characters' established friendship is deliberately developed | Shirro, Leena, fans, Cossette | Choosing her own image, career, desire and match strategy |
| **Dante** | **E:** Lyra, complicated fascination with Steffan | **P:** Steffan *if mutual choice after accountability*; a solo/healing route equally rich | Mara, Shirro, Leena | Distinguish love from competition, public humiliation from private hurt |
| **Steffan** | **E:** Lyra courtship; unresolved Dante fixation | **P:** Dante reciprocity as a hard-earned alternative to rivalry | Shirro, Alex, Ren | Being honest without treating apologies as tickets to someone's affection |
| **Crystal** | **E:** unfinished Raven romance | **P:** Angel slow, private mutual interest (investigation must still stand without it) | Christian, Leena, Milano | Trusting allies while facing her own failed reform history |
| **Raven** | **E:** attraction/conflict with Crystal | **P:** Mara mutual respect moving into attraction, *only after neither has an incompatible commitment* | Christian, Plug, Kreissack | Secrets, historical culpability and truthful confession |
| **Jean-Paul** | **E:** Varga mutual attraction and ethical catastrophe | **P:** Selene rivals-to-allies-to-lovers, without using her as an informant | Alex, Leena, Milano | Seduction versus evidence ethics; refusing to excuse Varga |
| **Selene** | **E:** political/flirtatious affinity with Milano | **P:** Jean-Paul; Ari (independent political romance) | Imani, Christian, Leena | Whether a sincere connection survives transparent disclosure of her identity |
| **Milano** | **E:** Selene rivalry/attraction | **P:** No second primary romance needed in first implementation | Imani, Haldane, Crystal, Alex | Reforms versus personal power; no insider access via romance |
| **Angel** | **E:** intellectual connection with Ren | **P:** Ren mutual romance; alternatively a close friendship with equal narrative payoff | Plug, Cossette, Christian, Leena | Trust without giving up anonymity or the right to refuse neural testing |
| **Ren** | **E:** Angel, Lyra friendship | **P:** Angel mutual romance; *possible* Lyra romance on a mutually authored route | Cossette, Ibrahim, Varga, Alex | Consent and autonomy, not romantic attachment as a cure for side effects |

**Caution — competing proposals:** An Angel–Ren romance may coexist in the design with Lyra–Ren *as alternative branches*, but not as simultaneous secret promises. Crystal–Angel and Angel–Ren similarly require one coherent chosen route rather than wish-fulfillment for every selectable pilot. The same is true for Mara–Ari, Mara–Raven and Mara–Plug. No relationship is canonized by this table.

## 3. Secondary cast: interaction agency, including romance

| Character | Agency and independent plot | Interaction gameplay | Proposed relationship use |
|---|---|---|---|
| **Leena Sato** | Pursues document authentication, public accountability and the ethics of protecting sources; can refuse being used as someone's publicity machine | Optional interview → independent archive request → evidence publication choice | **P:** Ari romance only with independent editorial recusal; **P:** Christian–Leena mutual off-player relationship after evidence-handling boundaries are clear. Both alternatives cannot be predetermined by player wishes. |
| **Alex** | Balances honest broadcasting, employer pressure, and their own personal/public identity | Pre-/post-match interview, off-camera media access, choice whether to broadcast damaging leaks | **P:** Lyra romance *after* broadcaster recusal from her coverage; player may instead forge a strong friendship. Alex is nonbinary and has their own preferences. |
| **Plug McEllis** | Warns of unsafe HAR service modifications; decides whether to risk a job to preserve a machine's local logs | Optional workshop time, equipment fault report, credible clue for Ari's refusal path | **P:** Potential Mara relationship arising through competence and mutual humor; don't reduce Plug to a “nice mechanic reward.” |
| **Christian Devroe** | Investigates family history and confronts Raven about what he knew; can protect Crystal without controlling her | Collaborative inquiry, diplomatic choice about Raven's testimony, evacuation support | **P:** An independent, low-key Christian–Leena connection in some routes; no requirement to pair them. |
| **Cossette + Ibrahim** | Existing mature couple, genuinely affectionate but disagree over neural integration | Private dinner, workshop debate, shared protective decision under emergency | **E:** Show their ongoing intimacy, tenderness and productive disagreement. **Do not manufacture a breakup to make them player romance prizes.** |
| **Shirro** | Must choose between sensationalism and broadcasting the truth; has a meaningful, sometimes harmful mentorship of Steffan | Media rehearsal, an awkward apology to Lyra, optional cover-up confession | Romance not required; use charisma, history and humorous/reflective social scenes instead. |
| **Imani Sorell** | Protects WAR's board legitimacy; can support oversight or block accountability | Negotiation, testimony conditions, public defense-contract announcement | No romance proposal in first pass; avoid conflating executive authority with intimacy. |
| **Dr. Haldane** | Has independent technocratic beliefs and complicity; should face oversight | Research meeting, oversight refusal, legal conflict | No romance proposal with experimental subjects; workplace power asymmetry is central. |
| **Dr. Varga** | Conducts unauthorized emotional experiments; must face independent investigation | Jean-Paul can test trust, confront evidence, withdraw; survivors can reject her framing | Established dangerous chemistry with Jean-Paul; **not** a romantic success condition. Romantic reconciliation is not an escape from accountability. |
| **Mara's mother** | Person with preferences, humor, judgment and independence—not a plot invoice | Optional meaningful conversation, treatment decisions with Mara, later rehabilitation plans | Family connection only. Her view of any partner can be favorable or skeptical; never a voting mechanic. |

### Secondary-to-secondary relationships

- **Cossette/Ibrahim (existing):** a warm, durable baseline; their disagreements make the neural-integration debate human rather than purely abstract.
- **Christian/Leena (proposed):** mutually earned professional trust could turn romantic off the player's route, **if** neither reporting nor source protection is compromised; both can remain single.
- **Shirro/Steffan (existing mentor relationship):** pseudo-familial show-business loyalty, public damage and genuine remorse; no need to sexualize every connection.
- **Alex/Leena (professional partnership):** occasional disagreement about protecting sources versus immediate public disclosure; not a default romance.

## 4. Priority route A — Mara, Ari, Raven, Plug (expanded)

**Core question:** Can Mara accept intimacy and assistance without relinquishing her independence? The prize and her mother's needs remain real even when she loses. Her arc never depends on whether Ari wins the championship.

| Chapter | Shared beat | Ari player option | Mara player option / suggested branches |
|---|---|---|---|
| 1 Gala | Mara teases newcomers and speaks bluntly about elite sponsorship | Respond with humor, curiosity, flirtation or guarded respect; none is a romance lock | Bond with Ari, seek Raven's respect, or spend time with Plug repairing Flail |
| 2 Champions | Mara reveals a small, concrete piece of her family burden | Respect her privacy, offer practical solidarity without taking charge, or press too hard | Speak frankly to Ari, keep distance, confide in Raven about tournament rules, or ask Plug for work rather than favors |
| 3 Attraction | **Existing explicit Ari choice:** lovers or friendship | Mutual consent for romance; friendship remains warm and not punished | May reciprocate Ari, choose friendship, or pursue her own connection if player-directed; **nonplayer Mara follows default unless Ari's choices change it** |
| 4 Quarterfinal | If paired, their fight is fully competitive, always decisive | After winning or losing, don't patronize or promise instant rescue; NII choice triggers ideological conflict | As selected pilot, she can beat Ari legitimately; alternative partners must not induce thrown fights |
| 5 Fractures | Mara sees the consequences of neural research and material debt | Tell the truth about symptoms/observed opponent anomalies; respect her autonomy | Choose coalition work, independent contracts, family care or a relationship conversation; she isn't obligated to forgive concealment |
| 6 Epilogue | Distinct independence + relationship resolutions | Partner/friend/separated, independent of trophy; financial plan is concrete, not magically paid | Romance with Ari/Raven/Plug or single; closeness does not erase an unresolved invoice or dictate care |

**Concrete optional scene: Flail workshop (Ch. 2)** — Plug shows Mara a cracked load bearing bracket. She refuses free equipment; he offers paid repair work and shows the legitimate cost breakdown. Choosing to stay and help opens camaraderie and potentially attraction later; choosing to handle it alone makes Plug a professional ally rather than a resentful rejected suitor. If the player is Ari, this is a brief witnessed scene, not a prompt to control Mara's reaction.

**Concrete optional scene: Locker-room corridor (Ch. 4)** — Raven privately admits to Mara that he withheld information from Crystal. A player-controlled Mara can insist on disclosure before any further intimacy, turn him down without losing evidence, or remain a respectful peer. **A Raven romance cannot excuse his historical conduct.**

**Provisional Mara endpoints:** (i) Ari partnership with maintained independence; (ii) close Ari friendship; (iii) Raven relationship after honesty; (iv) Plug relationship grounded in reciprocal competence; (v) self-directed career and family focus; (vi) relationship ends over concealment, with continued mutual respect. Where needed, meet care costs through negotiated payments, contracts and earned sponsorship with Mara's consent; tournament money helps only if she actually receives it.

## 5. Priority route B — Lyra's autonomy, public image and possible loves

**Core question:** Can Lyra choose desire, sporting excellence and her own public narrative when other people keep writing stories around her?

| Chapter | Default Lyra trajectory (NPC) | Playable Lyra: allowed agency | Secondary cast and nonromantic choices |
|---|---|---|---|
| 1 Gala | Established Dante relationship; provocative Steffan interest | Set boundaries, encourage Steffan, or recognize early manipulation; honest discussion with Dante | Alex interviews her as an elite champion, not ornament; Shirro pitches manufactured scandal |
| 2 Champion's Shadow | Wins legitimately; public idol pressures build | Share career ambitions with Dante; reject Steffan or pursue him **after** ending Dante relationship | Ren offers genuine friendship; Leena asks about contracts and privacy |
| 3 Attraction | Leaves Dante, begins Steffan involvement; scandal weaponized | Stay with Dante **if player-chosen** and mutually repaired; leave and date Steffan; leave both; no Varga-imposed romance | Alex may refuse invasive questions; Leena investigates source of selectively leaked footage |
| 4 Ghost | Qualifying loss to Steffan is a tactical clue in the **default** route | Her match result stands whatever the player achieves; she can study opponent tactics without need for romantic revenge | Optional off-camera Alex conversation; broadcaster conflict flagged if romantic interest is mutual |
| 5 Fractures | Receives evidence of Varga's intervention and Steffan's initial motive; ends relationship; **defeats Steffan only if actual bracket and result warrant it** | Confront with evidence, refuse to be a trophy, forgive without dating, or consider reconciliation only after sincere new choice; **not required to take him back** | Alex must recuse from covering Lyra if relationship develops; Shirro owns sensational edit |
| 6 Championship | Default faces Ari, loses; maintains career and fandom | If Lyra wins any route, she is *actual* champion and remains autonomous; if eliminated, her public declaration still belongs to her | Fanbase reactions range across support, anger and debate; Alex's professional role independently resolved |

**Proposed Alex option:** This is not a backstage flirt-to-prize. Alex and Lyra first share an unusually honest off-camera exchange about pressures of performance. Lyra can initiate a later conversation; Alex can refuse or reciprocate based on their own authored preferences. If reciprocal, Alex must stop independently presenting Lyra's tournament coverage (another commentator takes those segments) and both choose privacy or disclosure. A friendship route gets equivalent support, without implying Alex exists to validate Lyra.

**Proposed Ren option:** Start from the established supportive friendship; develop only in an authored alternate continuity after they both consider what their relationship means. Ren must not be turned into a rescue-from-technology romantic trope. Keep Angel/Ren branch mutually exclusive unless specifically expanded with transparent mutual agreement.

**Provisional Lyra endpoints:** self-chosen single celebrity/athlete; independent reunion with Dante after an earned relationship repair; no-reunion cordiality; mutually chosen Steffan reconciliation **only if he fully owns his conduct**, not the default; Alex romance with clear media boundaries; deep Alex friendship; possible Ren romance (requires approval). Her independence and ability to beat Steffan do **not** depend on dating decisions.

## 6. Priority route C — Ren and Angel

Both seek reliable truth about neural synchronization. A relationship can be romantic or deeply platonic; **neither grants free informed consent to an invasive procedure**.

- **Ch. 1–2:** Ren is fascinated by Angel's unconventional debugging methods; Angel respects intellectual honesty but is suspicious of research confidentiality. The player can share a non-sensitive observation, remain guarded or propose an independently logged test.
- **Ch. 3–4:** Ren notices anomalies and may conceal symptoms; Angel can request documentation rather than ask for blind trust. A selected Ren can agree to medical review, stop, or continue with recorded safeguards. Angel's friendship or love does not override her objections.
- **Ch. 5:** Angel discovers the high-bandwidth interface concerns independently or with Ren; both can present evidence even if their personal bond broke down. The official experiment, Varga's emotional manipulation and Nova's coercive integration must not be conflated.
- **Ch. 6:** Ren/Angel may agree to pursue ethical independent research, separate with mutual respect, stay friends or consciously choose romance. No romantic ending implies Ren's neurological symptoms have disappeared. Their technical cooperation can assist Nova containment regardless of dating state.

## 7. Priority route D — Crystal/Raven and Jean-Paul/Varga

**Crystal/Raven:** Forgiveness has a factual prerequisite: Raven must disclose what he actually knows about the Devroe tragedy, with uncertainty marked. He cannot unlock romance by winning fights or presenting an invented exonerating document. A Crystal-controlled route may support, distance, reject, or later reconsider. An honest-but-unforgiven route is valid. Christian's reaction is his own, not a morality-meter punishment.

**Jean-Paul/Varga:** Keep the seduction clever and mutual while making its asymmetry explicit when he discovers her unauthorized experimentation. Separate three questions: *Is attraction real?* *Can he continue the relationship?* *Must she face accountability?* The answer to the third remains yes regardless of the first two. He can report and sever ties, cooperate with investigators while conflicted, or distance himself from both; he cannot romance-away the evidence. A Selene option needs independent intimacy, not espionage leverage.

## 8. Flexible story beats — secondary character availability

Give each selected pilot **one or two optional interactions per act**, selected by story context instead of presenting a map of dozens of heart icons. Each supplies at least one tangible payoff unrelated to sex/dating: a clue, moral debate, comic relief, reputation information, equipment context, or meaningful friendship.

| Window | Suggested encounter | Nonromantic payoff | Romantic path only if earned |
|---|---|---|---|
| Ch. 1 gala | Leena interviews Ari/Crystal/Selene | What records the press can independently verify | Ari–Leena: only curiosity, not an instant invitation |
| Ch. 1 gala | Alex with Lyra/Steffan/Dante | Public image versus private speech | Lyra–Alex: first mutual respect |
| Ch. 2 workshop | Plug with Mara/Angel/Ren | Equipment diagnostics; credible Nova precursor | Mara–Plug: workshop camaraderie |
| Ch. 2 investigation | Christian with Crystal/Raven/Leena | Devroe shuttle document trail | Christian–Leena: possible secondary spark, not a quid pro quo |
| Ch. 3 tech dinner | Cossette and Ibrahim with Ren/Angel/Ari | Real benefits and risks of voluntary neural research | Existing committed warmth, not a selectable couple |
| Ch. 3 media control | Shirro with Lyra/Steffan/Alex | Why scandal clips travel; later culpability | No default romance |
| Ch. 4 mediation | Raven with Mara/Crystal/Christian | Truth about past cover-up; credible alliance | Raven–Mara/Crystal conditional and exclusive |
| Ch. 5 documents | Leena/Alex independently review disclosures | Safer leak custody; on-air correction | Reporter or broadcaster recusal required if romantic |
| Ch. 6 aftermath | Plug, Cossette, Ibrahim and Mara | Repairs, paid work, independent medical-support logistics | Partner status reflected only if previously established |

## 9. Low-cost ending architecture

Compose endings in **three independent passes**:

1. **Tournament:** champion, runner-up, eliminated, purse owed/received, fame.
2. **Investigation/world:** Ganymede accountability, WAR oversight, Varga review, Nova fate and research safeguards.
3. **Relationship:** who is close, dating, separated or distant; specific trust-dependent dialogue; secondary character's autonomous career conclusion.

Do not write one enormous ending per mathematical combination. Instead, use a fixed core scene plus 1–2 insertable companion/support snippets and a short independent supporting-cast montage. The companion can be absent, and the scene still works. All romance endings should acknowledge a past choice rather than assert a connection based on the player's tournament victory.

### Acceptance tests for narrative design

- Play Ari with Mara as **friends**, win against her: she fights seriously, does not resent being refused, her mother still needs care, and they remain close by choice.
- Play Ari with **Leena**, lose QF: Ari is not champion; Leena can publish evidence through independent verification without treating dating as a source privilege. Mara does not become a jealous caricature.
- Play Mara, beat Ari, and remain single: Mara can be champion without receiving a romance or a magical debt erasure.
- Play Lyra and **never date Steffan**: no scene may claim he is her ex; Varga's experiment can still target her public image, but cannot cause her to choose him.
- Play Lyra and **beat Steffan**: the win is authentic, from gameplay, even if she chose to remain with Dante, date Alex, or stay single. If Steffan does not reach her bracket, she does not fictionally beat him.
- Play Steffan and **win against Lyra**: no default speech may overwrite the victor; her decision to leave can remain authentic independent of losing.
- Play Ren and pursue **Angel friendship**: identical access to essential technical evidence as Ren/Angel romance.
- Play Jean-Paul and end relationship with Varga: her abuses can still be exposed; if he remains involved, she still faces review.
- Show Cossette and Ibrahim affectionate and disagreeing: neither the disagreement nor their intimacy exists only as a payoff for player actions.
- For every playable pilot: each match has one winner and one loser; romance flags never change official results or guarantee Nova access.
- Run a global exclusivity audit for routes involving Ari/Mara/Raven/Plug, Lyra/Dante/Steffan/Alex/Ren, Ren/Angel and Selene/Milano/Jean-Paul/Ari.

## 10. Scope and sequence proposal

**First playable slice:** the existing Ari story plus (1) fully playable Mara romance/friendship, (2) optional Ari–Leena relationship with journalism safeguards, (3) independent Mara/Plug friendship, (4) Lyra–Alex media friendship as observed subplot, (5) Cossette/Ibrahim dinner. This tests secondary-character agency without multiplying full endings.

**Second slice:** Lyra as selectable pilot, with stay-with-Dante / pursue-Steffan / single / possible Alex bond; alternate match outcomes preserve her athletic agency. **Third:** Mara as selected pilot and Ren/Angel friendship-or-romance routes. **Fourth:** rest of roster after systems/pacing are tested.

### Decisions needed from project owner before calling options canon

1. Which *proposed* romantic pairs should become supported routes at all? Prioritize 2–3 beyond established romances to avoid scope explosion.
2. Confirm each relevant character's adult age, romantic preferences and whether gender-customizable Ari can pursue them; do not default to universal eligibility.
3. Should the design permit negotiated non-exclusive arrangements, or use exclusive primary romances for this first installment? Neither is implied by the current canon.
4. How many optional conversation slots should cinematic mode provide, so a full romance does not overwhelm the fighting game?

**Status:** All above new pairings, character-specific romance eligibility, scene inserts, recusal mechanisms and endings are design options pending approval. None replaces the existing default six-chapter screenplay.


## 11. Addendum — spicy scenes and fanservice (2026-11-01)

**User-approved direction:** Add playful, glamorous, sensual and occasionally heated optional scenes; romance and fanservice should be visible components of the fighting-game tone, including interactions with secondary characters. This direction does **not** canonize specific new couples.

**Companion proposals:** `../04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.1.md` (12 complete optional scene cards), alongside `Optional_Relationship_Scene_Cards_v0.1.md`.

**New scene selection model:** An optional social slot can resolve as (1) generic spectacle/comedy; (2) character-specific fanservice/banter; (3) romantic escalation only with `romance_ready`; (4) friendship or independent non-romantic content. Explicitly separate `public_flirt`, `outfit_unlocked`, `attraction`, `mutual_interest`, `commitment`, and `intimacy`. Do not treat a swimsuit, dance, posed photo, banter, camera angle, or playful line as consent or a relationship commitment.

**Pacing:** Prefer one 30–120-second spectacle in a chapter where it relieves tension; romantic route inserts can replace a social slot rather than accumulate infinitely. Arcade gets a brief pre/post-fight banter or outfit variant, not a mandatory dating subplot.

**Safety/continuity gates:** All scenes are adult and consensual; Leena, Alex and Plug require age/eligibility finalization before implementing romance. Preserve Ari customization and Ren/Alex pronouns, the canonical default sequence, real match winners, Ganymede accountability, and meaningful professional research boundaries. Do not force pairings.

**Status:** approved *content direction*; scene text, optional pairings, outfit designs and precise placements remain design proposals.


## 12. Active screenplay integration status — v0.6 (2026-11-01)

The user instructed that selected romance, fanservice and secondary encounters be integrated into the screenplay. **Chapter v0.2** now contains option modules for Ari/Mara, Ari/Leena, Lyra/Alex, Mara/Plug, Crystal/Raven, Jean-Paul/Varga, Cossette/Ibrahim, Lyra's solo image control, and ensemble spectacle. Read `08_Relationship_Model/README.md` and the six active chapters rather than using the v0.1 cards as play instructions.

This is an **editorial implementation of proposals**, not approval of every possible romance. Specific new pairings require author decisions on reciprocal attraction, adult eligibility and exclusions; the current scene branches must not silently act as canon when the guards fail. Dante/Steffan, Angel/Ren and other pilot- or secondary-person routes are not yet integrated in the full screenplay.
