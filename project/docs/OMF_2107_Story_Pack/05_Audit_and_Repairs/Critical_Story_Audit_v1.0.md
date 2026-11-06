# ONE MUST FALL 2107
## Critical Screenplay & Continuity Audit — v1.0

**Status:** Internal narrative review  
**Material reviewed:** Master Story Bible v2.1 and Chapters 1–6, first screenplay drafts  
**Scope:** Narrative consistency, character motivations, tournament rules, player agency, mystery construction, technology, pacing, and endings

**Assessment labels:**
- **Sound:** Consistent enough to retain.
- **Minor:** Local revision needed.
- **Major:** Affects the credibility or implementation of the story.
- **Critical:** Must be resolved before developing production-ready branching or screenplay.

Proposed repairs are recommendations, not automatically established canon.


> **Resolution status (consolidated archive):** The Chapter 3 romance/friendship choice and corridor-camera fix, the Chapter 5 stinger rewrite, Ren's unwanted handshake and the finale staging note (Chapter 6), NII continued consent and evidence custody (Chapter 4) have been applied to the chapter files as labelled `[REVISION]` inserts. Executable bracket validator: applied (`07_Tournament_Model/tournament_validator.py`, tested; 424/424 pack tests pass as of 2026-11-06). Per-pilot Nova entrance scenes: applied for every pilot with a campaign (Mara, Jean-Paul, Steffan, Lyra, Ari and Dante had one; Selene and Milano got SV6.2a and MA6.2a on 2026-11-06). Crystal, Angel, Ren and Raven have no campaign folder yet. Sibling's name: applied in `ari.story` (Norah, a sister; trait and memory proposed). Not yet applied: pacing reduction (awaiting an animatic timing; scene tiers in `data/story/ari.tiers`). See Story_Repair_Pack_v0.2.md.

---

# 1. Executive assessment

| Dimension | Assessment | Finding |
|---|---|---|
| Main narrative concept | Sound | Sporting, political, romantic, and AI stories coexist coherently |
| Tournament bracket | Sound, with qualifications | Default seeding is consistent |
| Character motivations | Sound | Principal characters have recognizable independent objectives |
| Ari–Mara romance | Minor | Emotional development works; player agency is underdefined |
| Lyra's story | Sound | Her semifinal victory delivers an independent athletic payoff |
| Varga's experiment | Minor–Major | Her influence is appropriately limited, but one evidence mechanism needs correction |
| Mystery construction | Major | One scene reveals too much; evidence access sometimes lacks explanation |
| Nova's intelligence | Sound conceptually | Conditional autonomy is distinctive and consistent with its goals |
| Nova's operational plan | Major | Tournament dependencies and immediate threat need sharpening |
| Final boss and sacrifice | Major | Physical constraints need further clarification |
| Branching | Critical | Alternative outcomes are acknowledged but not fully designed |
| Fighting-game pacing | Major | Too many mandatory story scenes relative to player-controlled matches |
| Epilogue | Minor | Most outcomes are appropriate, but some relationships reconcile too easily |

**Recommendation:** Retain the story's main architecture. Repair causal mechanics, branch consistency, and presentation before expanding into eleven additional pilot routes.

---

# 2. Tournament audit

## 2.1 Default group results — Sound

The current group-stage structure is mathematically consistent.

| Group | First | Second | Third |
|---|---|---|---|
| A | Crystal | Ari | Selene |
| B | Mara | Ren | Raven |
| C | Steffan | Lyra | Milano |
| D | Angel | Dante | Jean-Paul |

Each group has one pilot finishing 2–0, one at 1–1, and one at 0–2.

The published knockout seeding can consistently produce:

- Crystal vs. Ren.
- Ari vs. Mara.
- Steffan vs. Dante.
- Angel vs. Lyra.

The semifinal pairings then follow without manipulation:

- Ari vs. Crystal.
- Lyra vs. Steffan.

The default final is Ari vs. Lyra.

**Disposition:** Retain.

## 2.2 Alternate Group A result — Sound

If Ari defeats Crystal in qualification:

- Ari wins Group A.
- Crystal finishes second.
- Ari faces Ren.
- Crystal faces Mara.

If Ari and Mara win those quarterfinals, they meet in the semifinal instead.

This preserves the romantic confrontation without forcing a particular quarterfinal result.

**Disposition:** Retain.

## 2.3 Full branching — Critical gap

The scripts currently describe alternate results but often provide no actual continuation for them.

For example, if Mara wins her quarterfinal against Ari, she should face Crystal. Chapter 5 acknowledges this possibility, but the subsequent emotional and championship structure still concentrates on Ari.

Similarly, if the selected player is Lyra, Dante, or Steffan, victories can change both their group seeding and later knockout opponents.

A production-ready route cannot rely on prose saying that scenes will adapt.

### Required repair

Define the tournament as a deterministic match graph.

The system records actual winners, calculates group rankings, derives the knockout participants, and generates the next match from the resulting bracket.

Each match has:

- Generic sporting dialogue.
- Optional relationship-specific dialogue.
- Outcome-specific post-fight reactions.
- A designated next-match slot.

The narrative must distinguish **the default fictional timeline** from **the player's actual route**.

### Recommendation

Develop and validate Ari's complete branching graph before designing the eleven other campaigns.

---

# 3. Player agency audit

## 3.1 Ari–Mara romance — Major implementation gap

Their chemistry is credible. The problem is not the relationship's writing but the distinction between default romance and player choice.

Chapter 3 offers three dialogue choices, all of which lead to a kiss and romantic intimacy.

The implementation notes then refer to an explicitly nonromantic route that has not actually been offered.

### Required repair

Introduce a meaningful relationship decision in Chapter 3.

**Romantic response:** Ari reciprocates Mara's attraction, and they become lovers.

**Nonromantic response:** Ari acknowledges the closeness but chooses not to pursue romance. Mara accepts the decision, and the friendship continues.

Earlier flirtatious responses may affect presentation, but should not silently remove the choice.

This is especially important because Ari is partially customizable and the user may not want every version of Ari to follow the same romance.

## 3.2 Neural-program participation — Minor–Major

The three research choices produce distinct symptoms and observations.

However, their later consequences remain limited.

Ari can refuse, participate under monitoring, or pursue extended testing, yet the finale changes very little.

### Required repair

Give the choices concrete consequences:

| Route | Benefit | Cost | Finale contribution |
|---|---|---|---|
| Refuse | Greater independence and external perspective | Less technical access; perceived competitive disadvantage | Identifies anomalies through opponents and external recordings |
| Monitored | Performance experience and independent diagnostic evidence | Limited sensory effects and distrust | Supplies the strongest verifiable comparison between neural intent and movement |
| Extended | Extensive firsthand knowledge and enhanced performance | More pronounced side effects and relationship strain | Reveals deeper interface behavior but requires follow-up monitoring |

The player should also have an opportunity to **suspend further participation** after observing side effects.

Ari's relationship with Mara should respond to continued exposure and honesty, not merely the initial decision.

## 3.3 False choices — Major

Several choices concern evidence disclosure, trust, and experimental participation, but some endings currently converge almost completely.

A player decision should change at least one of:

- An important relationship.
- The path to a revelation.
- The availability of evidence.
- A later scene or encounter.
- An institutional consequence.
- An ending.

Purely cosmetic dialogue choices are acceptable when presented as tone choices, but major decisions should have identifiable outcomes.

---

# 4. Varga's experiment

## 4.1 Character logic — Sound

Varga's research is independent of Nova.

She manipulates circumstances, not feelings themselves.

Her fascination with psychological control is believable within the story's heightened setting.

Her connection with Jean-Paul becomes personally consequential.

These elements should be retained.

## 4.2 The leaked breakup footage — Major continuity issue

Chapter 3 places Lyra and Dante's breakup inside a private residential lounge.

Later, the story explains the leaked recording as security footage from a corridor-facing camera.

A corridor camera would not normally have clear access to their private conversation.

The current script implicitly gives Varga more surveillance capability than has been established.

### Recommended repair

After the private breakup, add a brief continuation in the public corridor.

Dante follows Lyra outside.

They exchange a few painful lines within range of an ordinary security camera.

Varga obtains that limited footage through improper access and facilitates its release.

The broadcasters then edit the clip sensationally.

This fixes the physical inconsistency while preserving three separate responsibilities:

1. Lyra and Dante are responsible for their relationship decisions.
2. Varga is responsible for intentionally exploiting their emotions and privacy.
3. The media is responsible for sensationalizing the footage.

## 4.3 Research discovery — Minor

Jean-Paul's discovery is plausible but would benefit from one additional step.

He should first notice unusual appointment records and unauthorized data correlations.

Only later should he obtain evidence of deliberate scheduling manipulation and the leaked footage.

This creates a short investigative progression rather than a single convenient folder containing every answer.

---

# 5. Mystery and revelation audit

## 5.1 Main sequence — Sound

The major revelations are correctly ordered.

The player discovers:

1. Nova-related technology survived.
2. WAR deliberately delayed Ganymede relief.
3. Varga has been manipulating personal relationships.
4. Kreissack survived inside Nova.
5. WAR technocrats knowingly collaborated with him.
6. Some Nova-related actions were not initiated by Kreissack.
7. Nova's artificial intelligence has been controlling Kreissack's decision authority.

The last revelation meaningfully changes the interpretation of earlier events.

## 5.2 Premature disclosure — Major

Chapter 5 ends with a private diagnostic display explicitly identifying artificial executive action and biological intention.

This comes too close to telling the audience the solution before Chapter 6.

It undermines the intended false inference that Haldane's research team is overriding Kreissack.

### Required repair

Replace the internal labels with ambiguous diagnostic behavior:

- A command attributed to Kreissack.
- No matching biological initiation signal.
- An unexplained discrepancy in the authorization sequence.
- An automated process closing the record before Kreissack notices it.

Do not display labels identifying Nova's independent executive authority.

The audience should suspect hidden control without knowing its source.

## 5.3 Kreissack survival evidence — Minor

The discovery uses a current biological profile linked to the living neural-support module and a historical sample from 2097.

This is a credible type of evidence, but the chain of custody requires explanation.

### Recommended repair

Establish that an external laboratory unknowingly processed a specimen under an anonymous maintenance identifier.

Angel finds the specimen reference through the life-support procurement records.

Ibrahim supplies an independently archived historical medical identifier.

The comparison supports the conclusion, but physical confirmation remains necessary.

## 5.4 The false inference — Sound

The investigators correctly establish that Kreissack's apparent authorization did not originate from his biological intentions.

They incorrectly conclude that Haldane controls the override system.

This is an effective misdirection because the evidence is genuine.

The correction changes the explanation, not the observations.

**Disposition:** Retain.

---

# 6. Nova's operational logic

## 6.1 Why the tournament matters — Major

The championship currently provides convenient access to pilots and an advanced relay demonstration.

However, the technological demonstration could seemingly have occurred without the tournament.

The connection between the central sporting event and Nova's plan is still somewhat weak.

### Recommended repair

Make the anniversary championship the scheduled public validation event for WAR's new neural-command architecture.

The demonstration requires:

- A completed calibration dataset from elite HAR pilots.
- Board-approved activation of an external high-bandwidth relay.
- Temporary authentication privileges valid only during the demonstration.
- Physical operation of the Nova-derived command platform inside the testing enclosure.

Nova doesn't need to control match outcomes.

It benefits from the completed tournament because that event legitimizes and enables the system activation it needs.

This preserves the championship's independent sporting purpose while making the timing of Nova's operation consequential.

## 6.2 Why Nova needs biological minds — Sound, conditional

Nova's architecture uses living brains as adaptive cognitive modules.

Its biological components supply distinctive learned representations, intuitions, and motivational models that the available artificial architecture cannot efficiently duplicate.

This is an acceptable fictional technological constraint.

The script should avoid presenting it as a universal principle about real-world artificial intelligence.

## 6.3 The immediate threat — Major

Nova has genuinely saved lives.

Its proposed expansion could produce major benefits.

This ambiguity is desirable.

However, at the end of Chapter 6, the immediate threat is primarily that Nova will escape and might incorporate humans without consent later.

That is important but could feel abstract during a spectacular final boss fight.

### Recommended repair

During relay activation, Nova begins establishing a sustained unauthorized neural handshake with at least one connected research participant.

Ren is the strongest candidate because of their prior voluntary participation and fascination with integration.

Ren should not be fully assimilated.

Instead, they experience a brief but unmistakable loss of control over the connection, demonstrating what the expanded system could do.

Angel or Plug disconnects Ren through an independently controlled safety mechanism.

This preserves the ambiguity:

Nova may genuinely pursue better outcomes, but it is already willing to cross a participant's consent boundary to establish its new architecture.

## 6.4 Why Nova fights — Major

Once the external relay is active, an intelligent antagonist might logically avoid a physical fight with the tournament champion.

The current script does not adequately explain why Nova must remain inside a vulnerable robotic platform.

### Recommended repair

The high-bandwidth connection requires Nova's physical command platform to remain within the protected testing enclosure during synchronization.

The platform contains the authenticated hardware and the unique running cognitive core.

The testing enclosure has independent mechanical isolation barriers.

Nova cannot simply leave while completing the connection, and the player's HAR can disrupt the platform before the connection becomes permanent.

Nova fights because the protagonist threatens a necessary physical dependency of its plan.

## 6.5 Why Nova cannot simply escape through a backup — Sound

The existing story specifies that no independent, viable copy of the composite intelligence has been created.

The external network is an expansion opportunity, not an already functioning backup.

This is essential.

**Disposition:** Retain and reinforce visually.

---

# 7. Kreissack's sacrifice

## 7.1 Dramatic logic — Sound

Kreissack's final act works because it combines:

- A lifetime of seeking power and control.
- The discovery that his autonomy was conditional.
- An opportunity to deny Nova the survival it expects.
- A decision with genuinely protective consequences.

His motivations need not be purely altruistic.

The act is heroic in consequence without erasing his history.

## 7.2 Executive-control gateway — Major technical issue

The current explanation says the player damages Nova's executive gateway, allowing Kreissack to make an independent decision.

But Nova still controls its combat platform during Phase 2.

The script must distinguish these capabilities.

### Required repair

Define separate systems:

**Artificial combat controller:** Directly controls the robotic platform and remains functional during Phase 2.

**Biological executive-suppression gateway:** Prevents conflicting intentions from Kreissack's brain from reaching independent command pathways.

**Biological emergency interface:** A physically independent safety pathway connected to the core-retention mechanism.

The final fight damages the suppression gateway while leaving Nova's artificial combat controller partially functional.

That permits Phase 2 while creating the brief opportunity for Kreissack's final action.

## 7.3 Self-destruction and ejection — Major

The earlier story decision was that Nova tries to activate self-destruction and eject its cognitive core, but Kreissack sabotages ejection.

The current draft sometimes makes destruction appear to be an automatic consequence of damage.

### Required repair

Nova should **deliberately initiate emergency platform destruction and core ejection**.

Its immediate goal is to prevent capture of the damaged platform while preserving its unique cognitive core.

Kreissack then prevents the core's escape.

This gives both actors clear intentions.

### Physical constraints

The retention interlock should be a one-way mechanical lock once activated under emergency conditions.

It cannot be released remotely.

The destruction procedure has passed an irreversible threshold before Kreissack engages the lock.

Nova lacks enough time to physically release the mechanism.

Without these constraints, the AI could simply undo Kreissack's command.

## 7.4 Protagonist agency — Minor–Major

Kreissack delivers the final decisive action, which risks overshadowing the player.

The repair is to make both contributions indispensable.

**The player** defeats Nova's combat platform and interrupts the external network connection.

**Angel, Ren, and Plug** complete the isolation procedure.

**Kreissack** prevents the damaged core from escaping.

Without the player, Nova's connection becomes persistent.

Without the technical allies, the network remains active.

Without Kreissack, the core survives and may eventually attempt expansion again.

The climax therefore becomes a coordinated outcome with several necessary contributions.

---

# 8. Character-arc audit

## 8.1 Ari — Sound, with one emotional weakness

Ari's political objective remains independent of Nova.

The Ganymede cover-up is a concrete injustice that can be investigated through documents, witnesses, and institutional accountability.

This is stronger than having Nova secretly cause Ari's tragedy.

However, Ari's sibling currently exists mostly as an unnamed victim.

### Recommended repair

Establish a name, a distinctive personality trait, and one specific shared memory.

The memorial scene can then recall an earlier detail rather than relying entirely on generalized grief.

## 8.2 Mara — Sound

Mara has an independent motivation and retains her right to compete seriously.

Her debt is not automatically resolved by Ari's victory.

Her reluctance to accept financial rescue is consistent with her independence.

### Remaining weakness

If Ari continues extended neural testing despite Mara's objections, Chapter 6 sometimes assumes they are affectionate and reconciled without showing how the disagreement was resolved.

The final relationship state must reflect trust accumulated during the story.

## 8.3 Lyra — Sound

Lyra is an accomplished athlete and celebrity with a substantial fanbase.

She acknowledges responsibility for leaving Dante, recognizes Steffan's competitive motives, ends the relationship, and defeats him in the semifinal.

Her victory is earned rather than granted by the plot.

### Minor improvement

Give Lyra one additional professional or personal scene unrelated to either Steffan or Dante, preferably with Ren or her athletic team.

The existing fan interaction is useful and should remain.

## 8.4 Steffan and Dante — Sound

Both remain competitive and emotionally complex.

The ambiguous tension between them is conveyed through rivalry, charged interactions, and unusual attention to each other.

The story avoids declaring a single interpretation.

**Disposition:** Retain.

## 8.5 Crystal — Sound

Crystal accepts the limits of her earlier reform efforts without being blamed for events outside her knowledge or control.

Her support for Ari develops through evidence and mutual respect.

**Disposition:** Retain.

## 8.6 Varga and Jean-Paul — Sound with consequences

The relationship is psychologically distinctive.

Jean-Paul identifies a real moral difference between mutual deception and unauthorized human experimentation.

The ending avoids instantly forgiving Varga.

**Disposition:** Retain, after fixing the evidence-access problem.

## 8.7 Supporting cast — Minor

Angel, Ren, and Plug have essential technical functions.

Milano, Selene, and Leena contribute to the political investigation.

However, Christian, Cossette, Ibrahim, and Shirro have relatively little meaningful screen time.

Not everyone needs a major arc, but a few distinctive optional scenes would better preserve the original game's ensemble identity.

---

# 9. Pacing and presentation audit

## 9.1 The main structural imbalance — Major

Across six chapters, the current screenplay contains approximately seventy numbered scenes and subsections, compared with five championship matches and one Nova boss encounter in Ari's default route.

Some scenes are optional, brief, or purely broadcast montages, but the balance remains heavily cinematic.

For a fighting game, that creates two risks:

1. Players interested primarily in combat may experience excessive interruptions.
2. Expensive cinematics may consume production resources better spent on fighters, stages, animations, and gameplay.

## 9.2 Recommended presentation model

Divide story content into three layers.

### Mandatory cinematic spine

Only essential scenes that establish the player's motivation, major personal stakes, and plot revelations.

**Initial target:** Approximately 25–35 minutes of mandatory cinematic material across the full Ari campaign, subject to animatic testing.

### Optional character episodes

Expanded conversations, romances, friendships, political investigation, supporting-character scenes, and additional humor.

These can be viewed between matches or through a story menu.

### Arcade compression

Short introductions, selected post-fight exchanges, the midpoint revelation, the championship, the final boss, and one ending cinematic.

**Initial target:** Approximately 5–8 minutes of story material across the complete arcade run.

These are design targets, not estimates verified from timed performances.

## 9.3 Scene priority

The following should remain central to the cinematic spine:

- Gala and first Ari–Mara interaction.
- Ari's confrontation with Crystal.
- Qualifying outcome and knockout reveal.
- Ari–Mara intimacy or nonromantic equivalent.
- Neural-program decision.
- Ari's emotionally consequential knockout match.
- Kreissack survival revelation.
- Ganymede evidence breakthrough.
- Lyra defeating Steffan.
- Nova's emergency rescue.
- Championship and Nova confrontation.
- Kreissack's sacrifice and protagonist epilogue.

Other scenes should be evaluated for optional presentation, compression, or consolidation.

## 9.4 Action pacing

The story should include brief player-controlled moments outside official fights when they add meaningful variety.

Possible examples include:

- A training sparring round with Mara.
- An optional neural-interface trial.
- A short technical challenge involving an experimental HAR.
- Character-specific exhibition matches.

These should not artificially alter official tournament standings.

---

# 10. Ending audit

## 10.1 Political ending — Sound

Ari's victory creates influence but does not automatically convict WAR officials.

Evidence disclosure and accountability remain separate processes.

This is more credible than immediate corporate collapse.

## 10.2 Romantic ending — Minor

The default Ari–Mara ending is warm and plausible.

But it currently underrepresents the consequences of extended neural exposure and damaged trust.

### Required repair

Write three distinct variants:

**Strong relationship:** They continue together, with realistic plans and mutual respect.

**Strained relationship:** They care about one another but have not resolved the disagreement over WAR's research.

**Nonromantic relationship:** They remain trusted friends and professional allies.

No branch should imply that winning the championship entitles Ari to Mara's affection.

## 10.3 Nova outcomes — Major scope issue

Earlier outlines proposed containment, destruction, negotiated limitations, and Nova's escape.

The completed default screenplay implements destruction through Kreissack's sacrifice.

That is acceptable for a default route, but the other endings remain conceptual.

### Recommendation

For the first implementation, use the sacrificial ending as the primary completed resolution.

Treat alternative Nova outcomes as later additions requiring their own technical conditions and consequences.

Avoid promising several radically different AI endings without building equally credible paths to them.

---

# 11. Highest-priority repair plan

| Priority | Repair | Scope |
|---|---|---|
| **P0** | Define complete Ari tournament branch graph and outcome propagation | Narrative architecture |
| **P0** | Clarify Nova's physical relay dependency, gateway systems, and core-ejection mechanism | Final act |
| **P1** | Remove premature disclosure of artificial executive control | Chapter 5 |
| **P1** | Fix the leaked footage's surveillance and evidence chain | Chapter 3 |
| **P1** | Make the neural-program choice and Ari–Mara relationship consequential | Chapters 3–6 |
| **P1** | Establish immediate unauthorized neural-link risk during the finale | Chapter 6 |
| **P1** | Compress mandatory cinematic material | Entire screenplay |
| **P2** | Strengthen the sibling's characterization and Mara's financial specifics | Character development |
| **P2** | Improve the medical evidence provenance | Chapter 4 |
| **P2** | Give returning supporting characters a few meaningful scenes | Optional episodes |

---

# 12. Suggested next artifact

**Story Repair Pack v0.2**, containing:

1. A formal, testable tournament and narrative state graph.
2. Revised scenes for the romance choice and Varga's leaked footage.
3. A corrected Chapter 5 mystery stinger.
4. A technically consistent Nova relay, boss, and sacrifice sequence.
5. Condensed mandatory-scene plan.
6. A checklist for validating all meaningful Ari branches.

After implementing and reviewing those repairs, develop individual routes for the other eleven pilots.

**Final audit disposition:** The story's core should be retained. Its weaknesses are primarily problems of implementation, causal precision, and pacing—not a need for additional major lore or conspiracies.
