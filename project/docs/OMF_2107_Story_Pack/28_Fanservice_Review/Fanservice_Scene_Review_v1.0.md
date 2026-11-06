# OMF 2107 — Fanservice scene review anthology v1.0 (Story Pack v2.9)

**Source:** active v2.8 annotated scripts, copied verbatim except for newly inserted `[FANSERVICE: ...]` tag. The original lines, choices, BG references, MUSIC and PERF cues are preserved. Scene tags are **editorial classifications for review, not canon approval**. Earlier script revisions remain intact.

**Definition:** optional glamour, athletic display, light ensemble spectacle, flirtation staged for sensual appeal, a romantic kiss or private intimacy, or charged power dynamics. **Not every kiss is fanservice**, and dramatic scenes that only contain an optional intimate branch use `scope=OPTIONAL_BEAT`. `scope=FULL_SCENE` indicates the scene is primarily built for fanservice/spectacle, not that every choice involves romance.

**Important boundaries:** The catalog is not an instruction to display these scenes in every playthrough. Only independently authored, age-eligible, mutually chosen relationship paths may display physical intimacy. In Crystal–Raven / Steffan–Lyra encounters, manipulation is recorded as dramatic conflict; it never constitutes consent or qualifies for a romantic reward. Proposal-only routes and the legacy card bank do not become canon through tagging. Essential plot clues and tournament outcomes remain independent of these scenes.

**Review questions:** Does the moment suit the character? Is it optional, respectfully staged, appropriately placed in time, and distinct from nearby scenes? Does the text's romantic outcome agree with the global relationship state? Is the type of fanservice intentional rather than accidental?

**Inventory:** 65 active-script scene tags across 13 perspectives (Ari counted once), plus 12 proposed legacy scene cards.

| Perspective | Active tagged scenes |
|---|---:|
| Ari | 12 |
| Lyra | 6 |
| Mara | 5 |
| Ren | 5 |
| Angel | 5 |
| Crystal | 4 |
| Raven | 3 |
| Jean-Paul | 5 |
| Steffan | 3 |
| Dante | 4 |
| Selene | 6 |
| Milano | 5 |
| Christian | 2 |

## Part I — Active screenplay scenes (complete scene text)


---

### Ari


#### FS-ARI2-1B — SCENE 1B — OFF AIR (OPTIONAL: LYRA / ALEX)

**Source:** `04_Screenplay_Reconstructions/Chapter_02_Champions_Shadow_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `FLIRT` | **Review note:** optional spectacle; no relationship assumption

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 1B — OFF AIR (OPTIONAL: LYRA / ALEX)
**[FANSERVICE: FS-ARI2-1B | type=FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-SOC-BROADCAST@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED OPTIONAL INTERACTION — DAY 3, AFTER THE BROADCAST; 50–80 sec]**

**Gate:** playable Lyra; otherwise this can play as a brief noninteractive backstage exchange. Lyra is still dating Dante on the default route. Alex remains a professional broadcaster; no mutual romance flag is set here.

The interview lights go dark. Lyra, still wearing a shimmering sponsor jacket over training gear, sets her Electra gloves on a desk. Alex unclips a microphone.

**LYRA:** Everyone asked who I arrived with. Nobody asked how I improved my reaction time.

**ALEX:** Your third-round counter was the best part of the fight. The producer cut my analysis.

**LYRA:** You noticed?

**ALEX:** I was doing my job.

**[OPTIONAL CHOICE — LYRA]**

- **A — Ask for professional fairness:** “Put the counter on the next technical segment.” **ALEX:** “I can argue for analysis, not promise the edit.” `alex_respect=1`.
- **B — Admit exhaustion:** “Sometimes I don't know which smile is mine.” Alex puts away the microphone. **ALEX:** “Then you don't owe me one.” `alex_trust=1`.
- **C — Flirt playfully:** “You seem more interesting without a camera.” **ALEX:** “And you're still in an interview corridor. Talk to me when the tournament's over.” `alex_rapport=1`; no affair or recusal yet.

**Exit:** Alex continues objective commentary and Lyra returns to training. This interaction does not change the Lyra/Dante/Steffan arc or the match result.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI2-4B — SCENE 4B — NEON RESPITE (OPTIONAL PUBLIC FAN EVENT)

**Source:** `04_Screenplay_Reconstructions/Chapter_02_Champions_Shadow_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** optional spectacle; no relationship assumption

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 4B — NEON RESPITE (OPTIONAL PUBLIC FAN EVENT)
**[FANSERVICE: FS-ARI2-4B | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**[BG: BG-SOC-POOL@NIGHT | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED FAN SERVICE / COMEDY — DAY 3, NIGHT; 60–100 sec]**

**Gate:** any selected pilot can opt in. The segment plays *after* the day's matches and public obligations, not instead of them. Skip is always available. Lyra and Dante remain a couple on the default route; no public Steffan–Lyra romantic staging is assumed.

On a sponsor rooftop, reflected pool light scatters across a display of miniature HARs. Several adult pilots choose swimwear or tailored resort attire; staff ask permission before filming. Shirro poses extravagantly for a camera that has already found a better subject: Lyra demonstrating an impossible-looking dive for the cheering fans.

**LYRA:** [PERF: tone=excited | expression=EXP-BRIGHT | delivery=animated | intensity=3] That's what they call grace, Steffan. Your turn.

**STEFFAN:** I thought we were here to celebrate charisma.

He makes a spectacular splash. Dante rescues his soaked jacket with a look of absolute despair.

**DANTE:** I am going to win this tournament out of spite.

Mara laughs; Crystal offers Dante a dry towel without commenting. On the upper balcony, an uninvited WAR camera pans toward a restricted equipment access hatch; Plug closes the hatch and asks security to redirect it.

**[OPTIONAL CHOICE — ANY PILOT]**

- **A — Join the spectacle:** Pilot-specific pose or playful demonstration, no gameplay buff. `rooftop_joined=1`.
- **B — Have a private conversation:** Choose an *available* friend. A mutually eligible romantic partner can exchange a teasing line, but there is **no** automatic kiss, affair, or courtship progress. `rooftop_companion=chosen_id`.
- **C — Skip the event:** In the reading lounge, Cossette and Ibrahim discuss voluntary interface safeguards; the same research context and equipment anomaly can be learned without the spectacle. `rooftop_joined=0`.

**Exit:** The party stays lighthearted. Public outfits, poses and camera consent are unrelated to romantic interest or neural-interface consent. By morning every pilot is back on schedule for official fights.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI3-3B — SCENE 3B — THE VELVET PROBLEM (OPTIONAL: JEAN-PAUL)

**Source:** `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `SEDUCTION` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 3B — THE VELVET PROBLEM (OPTIONAL: JEAN-PAUL)
**[FANSERVICE: FS-ARI3-3B | type=SEDUCTION | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-SOC-FUND@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED OPTIONAL SIDE ROUTE — DAY 5, LATE EVENING; 60–90 sec]**

**Gate:** selected Jean-Paul; otherwise a distant shot of the reception establishes that Varga attends research-benefit events. This encounter precedes public discovery of her experiments and does **not** imply that the player has consented to being studied.

Jean-Paul stands near the doors of a small research-benefit reception, his tuxedo jacket slung over one shoulder. Varga emerges from the crowd in an elegant evening suit.

**JEAN-PAUL:** I thought this party was supposed to be boring.

**VARGA:** Only if you listen to the presentations.

**JEAN-PAUL:** Then save me with a dance.

**[OPTIONAL CHOICE — JEAN-PAUL]**

- **A — Offer his hand:** Varga joins him; they trade graceful steps and barbed compliments. An almost-kiss stops when she remarks, “You don't know what I'm asking.” **JEAN-PAUL:** “Then ask in words.” `varga_tension=1`, not commitment.
- **B — Ask about an unlikely coincidence:** “You scheduled a meeting before I requested it.” Varga deflects; Jean-Paul notices her tablet's prediction label. `varga_suspicion=1`.
- **C — Leave:** “I prefer dancing without a researcher taking notes.” Varga cannot prevent him from departing. `varga_distance=1`.

**Private sting, regardless of choice:** Varga's study log records the *predicted* encounter rather than an outcome. She cannot compel his genuine feelings. Her undisclosed orchestration will remain an ethical breach even if the attraction is mutual.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI3-5B — SCENE 5B — FIVE MORE SECONDS (OPTIONAL: ARI / MARA)

**Source:** `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `ATHLETIC_FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 5B — FIVE MORE SECONDS (OPTIONAL: ARI / MARA)
**[FANSERVICE: FS-ARI3-5B | type=ATHLETIC_FLIRT | scope=FULL_SCENE | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-ARE-TRAIN@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED SPARRING / FAN SERVICE — DAY 6, AFTERNOON; 45–70 sec]**

**Gate:** selected Ari or Mara and voluntary participation in Scene 5's safe sparring. **Continuity correction:** This *does not* include a first kiss; Chapter 3 Scene 11 is where the default first kiss can occur, after explicit reciprocal choice. No romance is inferred from sparring.

The training robots cool behind the glass. Mara, in ordinary practice clothing, catches Ari studying her left shoulder.

**MARA:** You keep watching that arm.

**ARI:** It telegraphs your hook.

**MARA:** Then why does it keep hitting you?

She offers a towel. Ari takes it; their fingers linger for an instant.

**[OPTIONAL CHOICE — SELECTED PILOT]**

- **A — Tease:** “Maybe I like the view from here.” Mara laughs. “Then keep your guard up.” `ari_mara_banter=1`, not intimacy.
- **B — Ask for another round:** “Five more seconds.” Mara steps into stance. “Finally, a reasonable request.” The HAR training clock flashes a new countdown. `ari_mara_spar_respect=1`.
- **C — End as friends:** “I trust you to tell me when I'm wrong.” **MARA:** [PERF: tone=amused | expression=EXP-SMILE | delivery=light, teasing | intensity=3] “I may need a larger schedule.” `ari_mara_friendship_rapport=1`.

**Exit:** They leave for separate obligations. No match is rigged, and the rapport flag does not override Chapter 3's independent romance/friendship choice.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI3-7 — SCENE 7 — AN UNFORTUNATE COINCIDENCE

**Source:** `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
# SCENE 7 — AN UNFORTUNATE COINCIDENCE
**[FANSERVICE: FS-ARI3-7 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**[CINEMATIC — DAY 6, NIGHT]**

**INT. BACKSTAGE SERVICE CORRIDOR**
**[BG: BG-TEC-SERVICE@BASE]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

Lyra leaves a late sponsor interview.

Her communicator shows a message from Dante.

**DANTE:** Still at the arena. Dinner?

She begins typing a reply.

A door opens.

Steffan emerges from a training room.

**STEFFAN**

You're still here.

**LYRA**

So are you.

**STEFFAN**

I couldn't sleep.

**LYRA**

You should try being less pleased with yourself.

**STEFFAN**

I've been told it's incurable.

She smiles.

**STEFFAN**

That was a good match yesterday.

**LYRA**

You already said that.

**STEFFAN**

I meant it both times.

They walk together toward the observation corridor.

**LYRA**

You know, you're much easier to tolerate when you're not performing for an audience.

**STEFFAN**

That's unfortunate. I rather enjoy audiences.

**LYRA**

I've noticed.

He stops beside a window.

Jupiter glows beyond the glass.

**STEFFAN**

Do you ever get tired of it?

**LYRA**

Of what?

**STEFFAN**

Being watched.

She looks at him.

**LYRA**

Sometimes.

**STEFFAN**

I thought you loved it.

**LYRA**

I love performing. That's not the same thing as wanting everyone to own a piece of me.

Steffan studies her.

For a moment, the usual joke doesn't come.

**STEFFAN**

I hadn't thought about it that way.

**LYRA**

There are lots of things you haven't thought about.

**STEFFAN**

You could educate me.

**LYRA**

That sounds like a full-time job.

They laugh.

The conversation becomes quieter.

**STEFFAN**

I wanted to win against you.

**LYRA**

Obviously.

**STEFFAN**

Not only because of Dante.

Lyra's expression changes.

**LYRA**

You understand how little that helps?

**STEFFAN**

Yes.

**LYRA**

Do you?

Steffan moves slightly closer but does not touch her.

**STEFFAN**

I like you, Lyra.

She looks at him for a long moment.

**LYRA**

You make it very difficult to do the sensible thing.

**STEFFAN**

I've heard that too.

This time she doesn't laugh.

Lyra closes the distance and kisses him.

Steffan responds.

The kiss is affectionate, impulsive, and clearly mutual.

Afterward, Lyra steps back.

**LYRA**
**[PERF: tone=regretful | expression=EXP-REMORSE | delivery=hushed | intensity=3]**

I shouldn't have done that.

**STEFFAN**

I'm not going to pretend I regret it.

**LYRA**

That isn't what I asked.

A pause.

**LYRA**

I need to talk to Dante.

Steffan nods.

**STEFFAN**

I know.

**LYRA**
**[PERF: tone=vulnerable | expression=EXP-VULNERABLE | delivery=exposed | intensity=2]**

And I need you not to make this into another victory.

That unsettles him.

**STEFFAN**

Lyra—

**LYRA**

I'm serious.

**STEFFAN**

So am I.

She studies his face, uncertain how much to believe.

**LYRA**

We'll see.

She leaves.

Steffan stays beside the window.

His excitement is genuine.

So is the satisfaction he feels at having defeated Dante in another arena.

He has not yet learned how to separate the two.

### A brief silent continuation

**INT. VARGA'S OFFICE**
**[BG: BG-LAB-RESTRICTED@BASE]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Varga studies a calendar of pilot interviews.

Earlier, she moved Steffan's training appointment and Lyra's sponsor interview into adjacent time slots.

She has no recording of the private kiss.

She does see that both entered the observation corridor within minutes of each other.

She adds a time stamp to her research notes.

**[TECHNICAL]** Varga created an opportunity for an encounter. She did not guarantee a romantic outcome or secretly induce the kiss.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI3-10B — SCENE 10B — TWO INVENTORS, ONE DANCE (OPTIONAL SUPPORTING CAST)

**Source:** `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `WARM_ROMANCE` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 10B — TWO INVENTORS, ONE DANCE (OPTIONAL SUPPORTING CAST)
**[FANSERVICE: FS-ARI3-10B | type=WARM_ROMANCE | scope=FULL_SCENE | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-SOC-DANCE@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED OPTIONAL RESPITE — DAY 7, LATE AFTERNOON; 40–70 sec]**

**Gate:** accessible to selected Ren, Angel or Ari, and as a short ensemble vignette to other routes. Cossette and Ibrahim are already an established adult couple. The player is a guest, never a voyeur.

A test-lighting fixture turns a workshop into an unexpected ballroom. Cossette inspects the circuit while Ibrahim offers a theatrical bow.

**IBRAHIM:** May I have this dance?

**COSSETTE:** If you remember who taught you.

They turn beneath the warm light. Cossette draws him close for a kiss. The test rig flashes an absurd victory animation.

**COSSETTE:** Was that deliberate?

**IBRAHIM:** I was hoping you wouldn't ask.

**[OPTIONAL CHOICE]**

- **A — Tease kindly:** “Should we applaud or send an invoice?” They laugh, then explain why opt-out control matters in neural systems. `workshop_trust=1`.
- **B — Give privacy:** The player withdraws; the same noninvasive safeguard information is available through the public workshop schematic. No hidden footage.
- **C — Ask about safeguards:** Cossette shows an isolated kill-switch design. Its usefulness is unrelated to the couple's private affection.

**Exit:** The light goes out. The technology remains testable whether or not the player attends.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI3-11 — SCENE 11 — SOMETHING WORTH WINNING FOR

**Source:** `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
# SCENE 11 — SOMETHING WORTH WINNING FOR
**[FANSERVICE: FS-ARI3-11 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**[CINEMATIC — DAY 7, EVENING]**

**INT. ANNIVERSARY COMPLEX — OBSERVATION GARDEN**
**[BG: BG-SOC-GARDEN@BASE]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

A quiet garden occupies a sheltered section of the orbital complex.

Small trees and flowering plants grow beneath carefully regulated artificial light.

Jupiter dominates the view beyond the glass.

Ari arrives to find Mara sitting beside a small ornamental pool.

**MARA**

You're late.

**ARI**

Two minutes.

**MARA**

I was beginning to think you'd escaped.

**ARI**

From dinner?

**MARA**

It's a perfectly reasonable response to the food here.

Ari sits beside her.

A small meal is laid out on the bench.

**ARI**

You found somewhere that doesn't serve commemorative coffee.

**MARA**

I have many talents.

They begin eating.

For a while, the conversation is light.

Mara tells an absurd story about a poorly maintained underground fighting venue.

Ari describes a childhood adventure on Ganymede involving a broken maintenance rover and an extremely unhappy security officer.

They laugh.

Eventually, the conversation becomes quieter.

**MARA**

You don't talk much about your family.

Ari looks at the pool.

**ARI**

There's not much left to say.

**MARA**

You don't have to say anything.

Ari considers that.

**ARI**

My sibling believed in WAR more than I did.

**MARA**

Really?

**ARI**

They thought the company would bring opportunities to the colonies. Jobs. Infrastructure. A future.

A pause.

**ARI**

I used to tease them for being so optimistic.

**MARA**

And then?

**ARI**

When the emergency happened, they kept saying the ships would come. That somebody would authorize them.

Mara listens.

**ARI**

They were right about the ships. The ships existed.

Ari looks away.

**ARI**

They just didn't come.

Silence.

Mara doesn't rush to fill it.

**MARA**
**[PERF: tone=regretful | expression=EXP-REMORSE | delivery=hushed | intensity=3]**

I'm sorry.

Ari nods.

**ARI**

Sometimes I think if I can prove what happened, something will finally make sense.

**MARA**

Maybe it will.

She looks toward Jupiter.

**MARA**

But you should get to have a life while you're doing it.

Ari turns.

**ARI**

That's something you sound very certain about.

**MARA**

I have a lot of opinions.

**ARI**

I've noticed.

They smile.

**MARA**

I spent most of my twenties moving from one contract to another. Repair bills, treatment bills, emergency jobs.

**ARI**

And now you're here.

**MARA**
**[PERF: tone=angry | expression=EXP-GLARE | delivery=hard edged | intensity=2]**

Now I'm trying to make enough money that I can stop pretending everything is temporary.

She glances at Ari.

**MARA**

Which probably sounds terribly romantic.

**ARI**

It sounds like you care about your mother.

**MARA**

I do.

Ari takes her hand.

Mara looks down, surprised by the gentleness of the gesture.

Then she closes her fingers around Ari's.

**MARA**

You've become rather difficult to make fun of.

**ARI**

That sounds serious.

**MARA**

It is. I may need professional help.

Ari laughs.

The atmosphere shifts.

For several seconds, neither looks away.

### [CHOICE 4 — ARI'S RESPONSE]

**A. Direct**

**ARI:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] I've wanted to kiss you since the gala.

**MARA:** [PERF: tone=proud | expression=EXP-PROUD | delivery=satisfied | intensity=1] You have excellent timing. It only took you a week to mention it.

**B. Playful**

**ARI:** Is this the part where you charge me for your company?

**MARA:** No. This one's on me.

**C. Vulnerable**

**ARI:** I wasn't expecting to feel this close to anyone here.

**MARA:** Neither was I.

**[Shared continuation]**

**[REVISION — ROMANCE CHOICE, Repair Pack R04]** Placed just before the first kiss.

**MARA**

> You know we're both still in the tournament.

**ARI**

> I know.

**MARA**

> And this may become complicated.

### [CHOICE 5 — RECIPROCATE OR REMAIN FRIENDS]

**A. Reciprocate** — `ari_mara = lovers`

**ARI:** I'd still like to find out where this goes.

**MARA:** Good. So would I.

*(Continues below.)*

**B. Remain friends** — `ari_mara = friends`

**ARI:** You're important to me. But I don't want to start a romance I may not be ready for.

**MARA:** I appreciate you telling me plainly.

They share a quiet, affectionate conversation under the Jupiter lights and walk back together. Mara is not hurt or vindictive; the quarterfinal stakes (friendship vs. prize money, fair fight vs. concern) stay serious. *(Skip to Scene 12; later Mara/Ari lines use the friendship variants.)*

**[Branch A continues]**

They kiss.

The moment is warm, unhurried, and mutual.

When they separate, Mara is smiling.

**MARA**

Well.

**ARI**

Well?

**MARA**

I was going to say something clever.

**ARI**

What happened?

**MARA**

You distracted me.

Ari kisses her again.

The camera shifts toward Jupiter and the lights of the garden.

**[TRANSITION — LATER]**

They walk together through a quiet residential corridor, still teasing each other.

At Mara's door, she turns.

**MARA**

You know we're both still in the tournament.

**ARI**

I know.

**MARA**

And I'm not going easy on you if we meet.

**ARI**

I wouldn't ask you to.

She studies Ari for a moment.

**MARA**

Good.

Mara opens the door and pauses, still holding Ari's hand.

**MARA**

Coming in? We can talk, or we can call it a night. Really.

### [OPTIONAL CHOICE 5B — PRIVATE FOLLOW-THROUGH; ONLY IF CHOICE 5A WAS RECIPROCATE]

**A. Spend a little time together.** Ari steps inside. Mara kisses Ari again; the camera stays in the corridor as the door closes. They have an unrecorded private evening. What happens offscreen is **not** used as a later assumption. `ari_mara_private_evening=1`.

**B. Say goodnight at the door.** Ari smiles. “I want tomorrow's conversation too.” Mara answers with a quick kiss and lets Ari leave. `ari_mara_private_evening=0`.

**C. Talk about the hard things.** They remain at the threshold discussing family, Ganymede and the risk of facing one another in the arena. The camera fades before either decides to go inside. `ari_mara_emotional_trust=1`.

**[CONTINUITY]** In all three alternatives, Ari is back in Ari's quarters for Scene 12's neural-program invitation later that night. This choice neither determines whether sex occurred nor overrides the subsequent tournament draw. If Choice 5 was friendship, omit this section entirely and continue to Scene 12.

**[RELATIONSHIP STATE]** Choice 5 sets `ari_mara` to `lovers` or `friends`. Earlier tone choices affect delivery only. `ari_mara_trust` is tracked separately.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI4-3B — SCENE 3B — COOLING SYSTEM (OPTIONAL: MARA / PLUG)

**Source:** `04_Screenplay_Reconstructions/Chapter_04_No_Holding_Back_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `WORKSHOP_FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 3B — COOLING SYSTEM (OPTIONAL: MARA / PLUG)
**[FANSERVICE: FS-ARI4-3B | type=WORKSHOP_FLIRT | scope=FULL_SCENE | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-TEC-HANGAR@NIGHT | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED MARA-PLAYER SIDE ROUTE — DAY 8, AFTERNOON; 65–95 sec]**

**Gate:** selected Mara; she must have previously arranged safe, invoiced repairs with Plug. Friendship/technical routes are always available. A romantic invitation appears **only** if both characters have been author-confirmed adults, a reciprocal compatible attraction route is enabled, the repair contract has ended, and Mara is not already exclusively committed to Ari or anyone else.

Plug kills the welding current and checks that the bench is safe. Mara removes her safety goggles, leaning over the repaired Flail actuator.

**PLUG:** The most expensive part of your machine now has a cheap scar.

**MARA:** It suits the pilot.

**PLUG:** The pilot is a walking invoice.

**[OPTIONAL CHOICE — MARA]**

- **A — Suggest dinner, off the clock:** “Now send the bill. Dinner is a separate conversation.” If `romance_ready(Mara,Plug)` is **independently established**, Plug may reciprocate and they agree to meet after the tournament. Otherwise Plug responds warmly but keeps it professional. `mara_plug_date_intent=1` only on reciprocal branch.
- **B — Enjoy the banter:** “Keep the invoice. I'll keep the scar.” They laugh; `mara_plug_friendship=1`.
- **C — Discuss the diagnostics:** Mara spots an anomalous feedback loop; Plug supplies the publicly inspectable testing log. `plug_hardware_clue=1`.

**Exit:** Flail's legitimate repairs, Mara's independent abilities, and the relevant technical anomaly are preserved on all branches. No kiss or tool access is exchanged for romantic interest.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI4-4B — SCENE 4B — THE BLUE HOUR (OPTIONAL: ARI / MARA)

**Source:** `04_Screenplay_Reconstructions/Chapter_04_No_Holding_Back_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PRIVATE_INTIMACY` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 4B — THE BLUE HOUR (OPTIONAL: ARI / MARA)
**[FANSERVICE: FS-ARI4-4B | type=PRIVATE_INTIMACY | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-SOC-GARDEN@NIGHT | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-CONFRONT | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED PRIVATE ROMANCE VARIANT — DAY 8, LATE EVENING; 55–90 sec]**

**Gate:** selected Ari or Mara; reciprocal Chapter 3 romance; neither committed elsewhere; both able to consent. If the neural-program argument has left them unwilling to be physically close, or if either prefers space, select the conversation/friendship fallback instead. This scene occurs **after** the argument, not as a substitute for resolving it. The quarterfinal is still ahead.

At Mara's doorway, the city bathes the hall in blue neon. She holds Ari's jacket across her shoulders after a short walk.

**MARA:** Tomorrow we might have to fight each other.

**ARI:** Can we schedule being enemies for after breakfast?

**MARA:** [PERF: tone=suspicious | expression=EXP-SKEPTICAL | delivery=guarded | intensity=1] You think you can distract me?

**ARI:** I think you still have my jacket.

They step closer only if both signal that the moment is welcome.

**[OPTIONAL CHOICE — SELECTED PILOT]**

- **A — Stay together tonight:** “Then let's have one night that's ours.” Mara's affirmative answer is explicit; they kiss, the hallway empties, the door closes, and the scene cuts to the next morning. Intimacy is implied offscreen, not presumed elsewhere. `ari_mara_private_night=1`.
- **B — Kiss and part:** They share a warm kiss and agree to meet in the arena with no favors. `ari_mara_private_night=0`.
- **C — Talk instead:** They sit beside the window, discussing Mara's mother and Ari's family. A difficult neural-program disagreement remains visible if present. `ari_mara_emotional_trust=1`.

**Fallback when `ari_mara=friends` or romance is strained:** Mara offers Ari the jacket and asks whether they are still prepared to fight honestly. They reaffirm mutual respect without a kiss or a private-night choice. If either wants distance, the scene is skipped with no penalty.

**Exit:** Tournament outcomes and medical risks are unaffected. Their competitive integrity and concerns about WAR continue into Scene 5.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI5-7B — SCENE 7B — OWN THE SPOTLIGHT (OPTIONAL: LYRA)

**Source:** `04_Screenplay_Reconstructions/Chapter_05_Fractures_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `GLAMOUR` | **Review note:** optional spectacle; no relationship assumption

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 7B — OWN THE SPOTLIGHT (OPTIONAL: LYRA)
**[FANSERVICE: FS-ARI5-7B | type=GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**[BG: BG-SOC-PRESS@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-CONFRONT | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED STAR POWER / FAN SERVICE — DAY 12, MORNING; 45–80 sec]**

**Gate:** selected Lyra; takes place after her press conference and established breakup, before her semifinal with Steffan. Steffan is **not** her public boyfriend in this beat. Appearance and posing are voluntary; fan support does not alter fight mechanics.

A sponsor offers Lyra a last-minute promotional portrait: two silhouettes, her Electra and Steffan's Pyros, posed like a romantic duel. Lyra surveys the lighting rig and a rack of dramatic, tailored outfits.

**LYRA:** I'm fighting him tonight. We're not selling a relationship.

**PHOTOGRAPHER:** The contrast would get attention.

**LYRA:** So would showing the move that got me here.

**[OPTIONAL CHOICE — LYRA]**

- **A — Choose an athletic solo shot:** In a metallic-jacketed Electra-inspired outfit, she performs a controlled vault beside her HAR. Fans applaud her mastery. `lyra_brand_autonomy=1`.
- **B — Agree to a *rivalry* double shot:** She and Steffan pose on opposite marks, no embrace or staged romance. She orders the caption **REMATCH**, not **REUNION**. `lyra_rivalry_promo=1`.
- **C — Cancel the shoot:** She goes straight to practice. The existing press conference remains her public statement. `lyra_brand_autonomy=1`.

**Exit:** Her public identity belongs to her; the semifinal is decided in the arena. The fans' loyalty is to the athlete, not the romance.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI6-15B — SCENE 15B — NO INTERVIEW TONIGHT (OPTIONAL: LYRA / ALEX)

**Source:** `04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PRIVATE_ROMANCE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 15B — NO INTERVIEW TONIGHT (OPTIONAL: LYRA / ALEX)
**[FANSERVICE: FS-ARI6-15B | type=PRIVATE_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-SOC-VIEW@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED OPTIONAL POST-TOURNAMENT ROMANCE — DAYS LATER; 75–110 sec]**

**Gate:** selected Lyra; the tournament and Alex's active coverage of her matches have ended; Lyra has ended the default Steffan relationship; Alex has transferred further reporting about Lyra to an independent colleague and disclosed the personal conflict. This is a *new proposed* mutual romance, not automatic canon. Both adults and romantic compatibility must be author-confirmed; otherwise use the friendship or solo variant. Never show this as occurring while Lyra is still exclusively committed elsewhere.

On a terrace after a charitable arena-repair event, Lyra looks at a huge holographic advertisement of her old smiling self. Alex joins her without a microphone.

**LYRA:** She looks perfect. She's very tired.

**ALEX:** It's a convincing performance.

**LYRA:** That sounds like a professional review.

**ALEX:** I'm off the assignment. You don't owe me a performance now.

**[OPTIONAL CHOICE — LYRA]**

- **A — Ask for something personal:** “Then stay when the cameras go.” **If** prior private trust, independent reciprocal attraction, adult eligibility and no exclusive commitments all pass, Alex says yes. Lyra invites a kiss; they share one and walk off together. `lyra_alex_date=1`. Otherwise Alex responds honestly that they aren't ready, with no penalty.
- **B — Keep the possibility open:** “Walk with me. No interview.” They leave as two friends with an unresolved spark. `lyra_alex_open=1`.
- **C — Choose solitude and freedom:** Lyra smiles at Alex and returns alone to the training deck. Her upcoming career plans remain intact. `lyra_alex_no_romance=1`.

**Exit:** This scene cannot alter Alex's prior commentary or Lyra's earned victories. Lyra keeps her athletic future and public fanbase in every variant.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-ARI6-16B — SCENE 16B — ALTERNATIVE RELATIONSHIP EPILOGUES (OPTIONAL)

**Source:** `04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SCENE 16B — ALTERNATIVE RELATIONSHIP EPILOGUES (OPTIONAL)
**[FANSERVICE: FS-ARI6-16B | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**[BG: BG-SOC-VIEW-PRIVATE@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-AFTERMATH | behavior=palette; continue_same_theme_unless_edited]**

**[INTEGRATED POST-TOURNAMENT ENDING DISPATCH — WEEKS LATER]**

This is an **exclusive display selector**, not a montage in which every romance happens. A protagonist's chosen primary route determines *one* main personal ending; other characters may receive a nonromantic status vignette. The core inquiry into the Ganymede authorization hold and Nova's victims continues independent of the romantic ending.

### E1 — Ari and Leena: Press Pass, Returned [proposed romance]

**Gate:** Ari selected; no Ari–Mara exclusive romance; Ari/Leena mutual interest independently authored; Leena's tournament assignment has ended; Ganymede evidence has been moved to an independent editor and archivist; Leena has disclosed her conflict and transferred coverage. Without these checks, show E1F friendship only.

Rain beads against the window of a transit-station noodle bar. Leena sets an obsolete press badge on the table, face down.

**LEENA:** I thought handing it in would make this simple.

**ARI:** Does it?

**LEENA:** It means I can ask you to dinner without pretending it's an interview.

**[OPTIONAL CHOICE — ARI]**

- **A — Accept a date:** “Dinner. No recorder.” She laughs, reaches across the table and takes Ari's hand. At the door they share a mutual kiss. `ari_leena_date=1`.
- **B — Keep it slow:** “The case is still open. Let's see what we want when the noise dies down.” They agree to meet again. `ari_leena_open=1`.
- **C — Remain friends:** “I trust you. I don't want to turn that into something else.” Leena accepts it. `ari_leena_friendship=1`.

**E1F fallback:** If the editorial recusal or reciprocal compatibility is unconfirmed, Leena and Ari exchange a warm professional farewell; the journalist's verified report is still published by the independent team.

### E2 — Mara and Plug: Parts and People [proposed romance]

**Gate:** selected Mara; not exclusively committed to Ari or Raven; Plug's adult eligibility and mutual interest confirmed; completed independent paid work; earlier Mara/Plug date intent reciprocated. Otherwise show E2F technical friendship.

In a public train-station café, Plug slides Mara a receipt: the Flail's last invoice, settled in full.

**PLUG:** I think this is the first time you've invited me somewhere without a broken machine.

**MARA:** I was considering breaking a toaster to make you comfortable.

**[OPTIONAL CHOICE — MARA]**

- **A — Ask about another evening:** Plug accepts only if the mutually authored attraction guard holds. They leave hand in hand, heading to a concert rather than back to the workshop. `mara_plug_dating=1`.
- **B — Celebrate professional partnership:** Plug raises a cup to the next contract. `mara_plug_partners=1`.
- **C — Spend the evening alone:** Mara returns to her independent engineering work, glad to have earned her own freedom. `mara_independent=1`.

**E2F fallback:** Mara and Plug exchange an affectionate but strictly professional thank-you. The legitimate repair contract and their respect remain unchanged.

### E3 — Crystal and Raven: Terms of Trust [established history, optional reconciliation]

**Gate:** playable Crystal or Raven; complete, verifiable disclosure and Christian's independent check; explicit reciprocal willingness. A breakup or respectful distance must remain possible.

They stand in a training room where only the sparring lamps are on.

**CRYSTAL:** I can remember wanting you without pretending the past was different.

**RAVEN:** I'm not asking you to forget it.

**[OPTIONAL CHOICE]**

- **A — Explore a future slowly:** After verbal confirmation from both, Crystal initiates a brief kiss. The ongoing inquiry stays open. `crystal_raven_repair=1`.
- **B — Remain allies:** Crystal takes the archival report rather than his offered hand. They agree to cooperate, not resume romance. `crystal_raven_allies=1`.
- **C — Part ways:** They exchange a respectful goodbye. `crystal_raven_closed=1`.

**E3F fallback:** If the disclosure is missing or inaccurate, there is no romantic option. Christian keeps custody of the documents; accountability is not erased by affection.

### E4 — Solo / friendship close (all playable pilots)

Any pilot whose romance route is absent, rejected or unavailable gets a complete short finale centered on their established personal stakes (career, technical safeguards, family, justice or rehabilitation). A warm friendship montage can replace a kiss, but **not** a victory, relevant investigation, or equal dignity. No unmatched NPC is assigned to a partner by a leftover flag.

**Epilogue priority:** Main closure for selected protagonist (`E1`, `E2`, `E3`, Ari–Mara restaurant, Lyra's `15B`, or `E4`) runs **once**. Global aftermath scenes still run independently and never silently restore a broken relationship.

---
<!-- END EXACT SOURCE SCENE -->


---

### Lyra


#### FS-LYRA-L1-3 — L1.3 — Off-script [OPTIONAL; ALEX, LEENA]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L1.3 — Off-script [OPTIONAL; ALEX, LEENA]
**[FANSERVICE: FS-LYRA-L1-3 | type=FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. CAMERA BALCONY**
**[BG: BG-SOC-VIEW@BASE]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

Alex, the broadcaster, adjusts a live feed while Leena checks records. Lyra slips in, avoiding a producer who wants her to confirm a dating rumor.

**ALEX:** "Our next interview is titled 'Lyra's Secret to Staying Beautiful Under Pressure.'"

**LYRA:** [PERF: tone=sarcastic | expression=EXP-DRY | delivery=dry | intensity=2] "My secret is refusing questions written by people who've never been hit by a seven-ton robot."

Alex switches the monitor to her championship footage.

**ALEX:** "How about 'What did the opponent misunderstand about your footwork?'"

**LYRA:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] "Now that's an indecently attractive question."

Alex laughs, but keeps professional distance. Leena points out a discrepancy between the promotional health certification and a technical addendum.

**LEENA:** [PERF: tone=amused | expression=EXP-SMILE | delivery=light, teasing | intensity=3] "I'm tracking a story about neural-interface monitoring. Your team may be offered extra testing. Check what you authorize."

**SAFE CLUE L1-K1:** The optional interaction provides context, not exclusive evidence. The same public addendum is available in Lyra's event briefing whether this scene is skipped.

**CHOICE L1-C3:** Invite a technical interview / decline politely / ask Leena for the public document. Alex responds professionally to all three. `alex_rapport` can increase; **no romance** while Alex covers Lyra.
<!-- END EXACT SOURCE SCENE -->


#### FS-LYRA-L2-3 — L2.3 — Neon Respite [OPTIONAL ENSEMBLE / FANSERVICE]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L2.3 — Neon Respite [OPTIONAL ENSEMBLE / FANSERVICE]
**[FANSERVICE: FS-LYRA-L2-3 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. ROOFTOP POOL AND TRAINING DECK — NIGHT**
**[BG: BG-SOC-POOL@NIGHT]**
**[MUSIC: MUS-RESCUE | behavior=palette; continue_same_theme_unless_edited]**

Athletes unwind by the pool. An affectionate older couple, Cossette and Ibrahim, exchange a private joke about their prototype's cooling system. Plug describes an exploded coolant line with the enthusiasm of an artist. Ren has brought a manual to a party.

**LYRA:** "You're reading hydraulic failures beside a swimming pool?"

**REN:** "It seemed thematically appropriate."

Lyra offers to race Ren down the deck—without pushing them into the water. Ren declines and watches her demonstrate a flawless handstand turn. Dante arrives with towels. Steffan arrives a minute later and tries to pretend it's a coincidence.

**CHOICE L2-C2:** affectionate flirting with Dante / light public teasing of Steffan without offering romance / make Ren laugh / talk craft with Plug / skip the event to rest. If Steffan is chosen for teasing, Lyra explicitly states it is not an invitation to intrude on her existing relationship. Their attraction may be established as plausible, but boundaries remain hers. **No intimacy check or scene unlock depends on swimwear.**

**COSSETTE (to Ibrahim):** "If you hand me an engineering specification on our date, I'll marry you twice just to divorce you twice."

**IBRAHIM:** "I've already removed the diagrams."
<!-- END EXACT SOURCE SCENE -->


#### FS-LYRA-L3-2 — L3.2 — Before the kiss [MANDATORY RELATIONSHIP DECISION]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L3.2 — Before the kiss [MANDATORY RELATIONSHIP DECISION]
**[FANSERVICE: FS-LYRA-L3-2 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. QUIET OBSERVATION GALLERY**
**[BG: BG-SOC-VIEW@BASE]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Steffan offers dinner without spectators. He has memorized one of Lyra's obscure early matches. She is disarmed by attention to her skill, and suspicious of how pleased he is that Dante sees them talking.

**LYRA:** "Do you like me, or the expression Dante makes when you stand beside me?"

**STEFFAN:** "Both would be an ugly answer."

**LYRA:** [PERF: tone=afraid | expression=EXP-FEAR | delivery=tremulous | intensity=3] "It's also the answer I'm afraid of."

**CHOICE L3-C1 — player chooses ONE:**
- **D — Stay with Dante.** Lyra tells Steffan she is attracted but unavailable, or not interested. She and Dante have a candid talk about publicity pressure and trust. `partner=dante`, `breach=false`. Optional affectionate kiss with Dante; implied intimacy only if mutual. **No forced Steffan affair or breakup.**
- **S — End things cleanly with Dante, then date Steffan.** Lyra speaks to Dante first, privately, without blaming him. He is hurt, not humiliated by a public show. After the breakup Steffan and Lyra share a deliberate kiss. `partner=steffan`, `breach=false`; attraction still genuine, his mixed motives unresolved.
- **B — Follow the default flawed path: kiss Steffan while still with Dante, then confess and break up.** The kiss is a choice, not manipulation by Varga; Lyra ends it, tells Dante herself, acknowledges betrayal without excusing it. `partner=steffan`, `breach=true`. Later Dante trust takes a hit, especially if she asks for immediate forgiveness. This route retains the default scandal without depicting infidelity as a free power-up.
- **N — Choose neither.** Lyra ends or pauses the relationship with Dante respectfully, declines Steffan, and explores solitude or friendship. `partner=none`, `breach=false`.

**DANTE (if told about S/N):** "I thought we were still planning the same future."

**LYRA:** "I should have told you earlier that I wasn't sure. I'm telling you now."

**DANTE (if told about B):** "You let me learn that the person who could hurt me most was standing right beside me."

**LYRA:** "I chose it. You don't have to make it easier for me."

No branch turns Dante into an abuser or Lyra into a villain. The romance with Steffan can include suggestive slow dancing, flirtatious close contact, and an optional private evening with fade-to-black **only if both are single and explicitly choose it**.
<!-- END EXACT SOURCE SCENE -->


#### FS-LYRA-L4-4 — L4.4 — Two versions of a rival [OPTIONAL; DANTE / STEFFAN]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PRIVATE_INTIMACY` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L4.4 — Two versions of a rival [OPTIONAL; DANTE / STEFFAN]
**[FANSERVICE: FS-LYRA-L4-4 | type=PRIVATE_INTIMACY | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. LATE-NIGHT COMPETITORS' LOUNGE**
**[BG: BG-ARE-LOUNGE@NIGHT]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

If Dante is still Lyra's partner, he asks if the public defense has cost her sponsorships. If separated, he asks only whether her equipment is safe. If Lyra crossed a boundary in Chapter 3, he does not grant immediate forgiveness; she can apologize once without demanding a response.

**DANTE:** "I always knew you could outfight me. I didn't realize I'd have to learn how to stop listening to strangers explain what you wanted."

**LYRA:** "Neither of us should have listened to them. I still own what I did."

If Steffan is her partner, he offers a private escape from the cameras. If Steffan is not her partner, the scene is a frank confrontation about treating competitors like prizes. He is allowed defensiveness and early partial growth, not absolution.

**[OPTIONAL STEFFAN ROMANCE VIGNETTE — only if current partner and mutual choice]**

He enters a quiet, softly lit rehearsal studio where she is stretching after training. Lyra has traded her camera-ready outfit for a loose warm-up shirt and shorts. He watches the difficult hold in respectful silence.

**STEFFAN:** "Is this where you practice making everyone look clumsy?"

**LYRA:** "No. That's in the arena. This is where I practice making you wait."

He offers his hand and lets her decide whether to take it. She does, pulls him into a slow dance, and almost trips him on purpose. Their laughter gives way to a kiss. When he tries to turn it into a grand romantic speech, she touches a finger to his lips.

**LYRA:** "Not everything between us needs an audience."

**STEFFAN:** "What would you prefer?"

**LYRA:** "Ask me without trying to win."

The player may choose **stay together privately** (their mutual invitation is clear; camera fades out as the studio door closes), **kiss and leave**, or **talk honestly instead**. There is no camera intrusion, concealed monitoring reveal, or mechanical reward from choosing intimacy. The scene does not replace later accountability for his initial rivalry motive.

**CHOICE L4-C1 — limited trust:** share an independent safety warning with either man / ask for privacy / refuse discussion. Evidence is not lost and neither man becomes a required informant.
<!-- END EXACT SOURCE SCENE -->


#### FS-LYRA-L5-3 — L5.3 — Own the Spotlight [OPTIONAL GLAMOUR / SECONDARY AGENCY]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `FULL_SCENE` | **Category:** `GLAMOUR` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L5.3 — Own the Spotlight [OPTIONAL GLAMOUR / SECONDARY AGENCY]
**[FANSERVICE: FS-LYRA-L5-3 | type=GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**INT. PHOTO STUDIO — EVENING**
**[BG: BG-SOC-PRESS@EVENING]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

Lyra agrees to one last controlled publicity session. Cameras alternate between a fashion portrait and unretouched footage of her hands taping her wrists. The staff are professionals, and she approves the poses and final use of images. If she previously selected privacy, the scene becomes a quiet training-film shoot or is skipped. She can choose a daring, beautiful outfit or ordinary training gear with equal narrative prestige.

**PHOTOGRAPHER:** "Which angle makes you look invincible?"

**LYRA:** "None. Show the bruises. Invincible is boring."

In an optional private exchange, Ren brings her a repaired training glove.

**REN:** "I didn't want you to think the investigation was all anyone noticed."

**LYRA:** "You're dangerously good at noticing the right things."

They share warmth; **friendship only in this version**. A Lyra–Ren romance has been proposed elsewhere, but is **not** implemented without approval and a reciprocal authored arc. Lyra may also thank Cossette and Ibrahim for helping the safety review.
<!-- END EXACT SOURCE SCENE -->


#### FS-LYRA-L6-7 — L6.7 — After the broadcast [OPTIONAL; ROMANTIC / FRIENDSHIP / SOLO EPILOGUE]

**Source:** `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### L6.7 — After the broadcast [OPTIONAL; ROMANTIC / FRIENDSHIP / SOLO EPILOGUE]
**[FANSERVICE: FS-LYRA-L6-7 | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**EXT. QUIET PROMENADE — EVENING**
**[BG: BG-SOC-TRANSIT@EVENING]**
**[MUSIC: MUS-AFTERMATH | behavior=palette; continue_same_theme_unless_edited]**

A screen plays highlights of Electra's fights. Lyra turns it down. No cameras are following her today.

**ROUTE D — Dante, only if current mutual relationship maintained:** He waits by a food stand with two drinks, asks if she wants company. She kisses him if she chooses; otherwise they share a relaxed conversation. If she separated from him earlier, the route can propose a *slow* reconnection only after individual accountability and Dante's reciprocal choice; it is **not** an instant reversal of a betrayal.

**ROUTE S — Steffan, only if not committed elsewhere, after the tournament and his demonstrated accountability:** He asks to speak rather than arriving with a gift or a public apology. Lyra may explicitly defer; mutual reconciliation is **proposed, not default**, and Steffan is free to decline it. They don't retcon why she left. A romantic fade-to-black is possible only after new consent, a credible period of repair, and both being free; it never occurs in the Chapter 5 breakup scene.

**ROUTE A — Alex, new optional romance, not yet approved:** Alex confirms **their Lyra-related tournament assignment has ended and they are recused from future coverage of her**, with an independent colleague responsible for any remaining coverage. Lyra and Alex are both verified adults and independently show mutual interest. Alex declines any special interview arrangement as the price of dating: "I won't stop being good at my job to be near you." Lyra smiles: "I'd like you less if you did." They arrange a private date. The camera stays outside; Alex need not become Lyra's partner. If the professional gate is absent, play a warm friendship scene instead—no kiss.

**ROUTE R — Ren, friendship (no romance implemented):** Lyra teaches Ren the footwork behind her famous feint. Ren teaches her a system diagnostic. Their trust has nothing to do with winning the tournament.

**ROUTE SOLO — independent Lyra:** She joins a friendly exhibition or walks home after telling her publicist to send the next training schedule, not a romantic press release. Optional glamorous afterparty fanservice is cheerful and public; no lover is implied or assigned by the engine.

**LAST IMAGE:** A young fan copies Lyra's step in the reflection of a dark screen. Lyra notices, makes the step more precise, and invites the child to try again. Above them, an advertisement says *ICON*. On the gym wall, someone has written *CHAMPION*. She looks happiest when they start practicing together.

---
<!-- END EXACT SOURCE SCENE -->


---

### Mara


#### FS-MARA-M2-4 — M2.4 — Rooftop: everybody gets one night [OPTIONAL FAN SERVICE / COMEDY]

**Source:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### M2.4 — Rooftop: everybody gets one night [OPTIONAL FAN SERVICE / COMEDY]
**[FANSERVICE: FS-MARA-M2-4 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. ROOFTOP POOL / OBSERVATION DECK — NIGHT**
**[BG: BG-SOC-POOL@NIGHT]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

A gala-adjacent pool has attracted fighters, technicians and people avoiding sponsors. Lyra is laughing at her own flashy publicity billboard; Dante watches a replay on a portable screen; Cossette and Ibrahim argue affectionately over a chessboard. There are designer swimwear, tank tops, tattoos, scarred shoulders and human bodies that have spent years in combat simulators. The camera is *playful and character-led*, not coerced exposure.

Mara arrives in a simple dark swimsuit, delighted that nobody expects her to speak to a shareholder. Plug has brought a ridiculous inflatable miniature Flail, whose chain is made of foam.

**MARA:** Is that supposed to be me?

**PLUG:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] No. It has fewer structural defects.

Ari asks whether she'd like to leave the crowd and watch Ganymede from the observation deck. Raven stays with his drink; their old rivalry can turn into unhurried conversation. `CHOICE`: talk with Ari / compare scars and repair stories with Plug / spar verbally with Raven / join Cossette and Ibrahim / retire alone for a long call with her mother. **Nothing here locks a romance or essential clue.**
<!-- END EXACT SOURCE SCENE -->


#### FS-MARA-M3-1 — M3.1 — Training with Ari [MANDATORY; optional intimacy]

**Source:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ATHLETIC_FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### M3.1 — Training with Ari [MANDATORY; optional intimacy]
**[FANSERVICE: FS-MARA-M3-1 | type=ATHLETIC_FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. PRACTICE HALL — LATE AFTERNOON**
**[BG: BG-ARE-TRAIN@DAY]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Ari asks Mara to teach a counter to a close-range hold. Mara demonstrates with a foam training chain; Ari adapts faster than she expected. The gym has gone quiet except for ventilation and their unsteady breathing after the last round.

**ARI:** You don't have to turn everything into a joke.

**MARA:** That's unfortunate. My second-best skill is deflection.

**ARI:** What's the first?

**MARA:** Chain management. Very romantic.

`CHOICE`: reveal how frightened she is about her mother; say only what she is comfortable saying; refuse to discuss the care account yet. Ari respects the boundary, including on the potential romance path.

`OPTIONAL, mutual attraction and clear intention = ari`: Ari looks at her, then asks, "Can I kiss you?" **MARA:** "If you stop looking so pleased with yourself first." They kiss. She breaks it to demand an honest fight if they meet. `CHOICE`: go on an optional private consensual date ending in a fade to black / share a kiss then say good night / keep the affection warm but unacted-upon. No romantic contact if Mara selects friendship, Raven, Plug or solo. The authorial default selected-Ari love story remains possible, not automatically binding for selected Mara.

`FRIENDSHIP`: Ari holds out a training towel. **ARI:** "Then five more seconds of practice." **MARA:** "Five more seconds of you losing." They leave laughing.
<!-- END EXACT SOURCE SCENE -->


#### FS-MARA-M3-2 — M3.2 — Two other kinds of chemistry [OPTIONAL; separate scenes]

**Source:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `WORKSHOP_FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### M3.2 — Two other kinds of chemistry [OPTIONAL; separate scenes]
**[FANSERVICE: FS-MARA-M3-2 | type=WORKSHOP_FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-TEC-HANGAR@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**
**A. WORKSHOP, IF PLUG INTENT, POST PROFESSIONAL REPAIR**

Mara returns to help calibrate a retired actuator rack under an **independently invoiced work arrangement**. Plug is meticulous; she is impatient. He shows her a trick for detecting load bearing fatigue with a cheap acoustic sensor.

**MARA:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] You're a terrible flirt.

**PLUG:** This is an industrial inspection.

**MARA:** [PERF: tone=contemptuous | expression=EXP-DISDAIN | delivery=cool | intensity=2] That's what makes it terrible.

He laughs, but does not trade affection for safety work. `CHOICE`: suggest coffee after all maintenance obligations and tournament equipment assignments end / make clear she wants only a good colleague. If professional boundaries remain active, their relationship stays potential, **not yet dating**; no kiss in the shop.

**B. OBSERVATION RAIL, IF RAVEN INTENT**

Raven knows Mara is considering whether a man who once worked for Kreissack and withheld records from Crystal deserves trust. She wants facts, not an alluring silence.

**MARA:** You're good at leaving before anyone asks a second question.

**RAVEN:** I used to be paid for it.

**MARA:** I'm not paying you to stay. I'm asking whether you can.

`CHOICE`: insist he disclose the missing record and resolve any actual commitment to Crystal before anything intimate / keep competitive friendship / withdraw. Romantic escalation is **not enabled** until he acts independently, acknowledges wrongdoing and is truly available. Mara does not become the reward for a man's redemption.
<!-- END EXACT SOURCE SCENE -->


#### FS-MARA-M5-2 — M5.2 — A confession is not a clearance [OPTIONAL RELATIONSHIP BRANCH]

**Source:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### M5.2 — A confession is not a clearance [OPTIONAL RELATIONSHIP BRANCH]
**[FANSERVICE: FS-MARA-M5-2 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**[BG: BG-TEC-SERVICE@EVENING | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**ARI PATH:** Ari meets Mara outside the service bay. If Ari participated in research, he tells her about any symptoms he knows—or, if he concealed them, the script treats that concealment as a substantial breach. If he refused, they instead discuss outsider evidence and the costs of resistance. Mara can keep romance with boundaries, remain close friends, request time apart or end an incompatible relationship. Her choice cannot retroactively pick Ari's neural history.

**MARA:** I can lose an argument with you. I can't build a future out of information you keep from me.

**PLUG PATH:** after outstanding safety repair duties have ended or been handed to a neutral shop, Plug meets Mara at an ordinary diner. He has his own plans, preferences and a paid job unrelated to her equipment. If both explicitly express interest, an **adult-verified** optional kiss is available; otherwise they laugh about foam Flail and remain friends. No technical access changes.

**RAVEN PATH:** Raven documents what he withheld from Crystal/Christian and obtains an independent review, admitting the harm without asserting that remorse absolves him. Any existing commitment with Crystal must have ended honestly before either person considers dating. If he is available and the project approves mutual interest, Mara can invite him to dinner **after** the tournament. Otherwise friendship, anger, or distance remain valid. A conditional romantic scene never disguises the missing record.

**SOLO PATH:** Mara walks the night market with her mother over video call, negotiating a ridiculous choice of gifts. Her emotional arc remains full; being single is neither punishment nor comic failure.
<!-- END EXACT SOURCE SCENE -->


#### FS-MARA-M6-5 — M6.5 — What we keep [OPTIONAL ENDINGS; eligibility guarded]

**Source:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### M6.5 — What we keep [OPTIONAL ENDINGS; eligibility guarded]
**[FANSERVICE: FS-MARA-M6-5 | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**[BG: BG-ARE-TRAIN@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**ARI, mutual and trustworthy:** They return to the training hall after the tournament. Ari does not offer to pay away the relationship's conflict; Mara does not ask Ari to abandon Ganymede. **MARA:** "We can help each other without keeping score." Ari offers a hand, and she takes it. A kiss may follow if both choose. **If truth was broken**, a separate accountable repair over time is required; otherwise the pair remain friends or separated. Their sporting result never decides whether they love each other.

**PLUG, adult verified, mutually interested, professional conflict cleared:** An independent workshop accepts Mara as a paid contractor. Plug meets her after the first shift, no longer responsible for inspecting her competition Flail. **PLUG:** "Still charging for advice?" **MARA:** "Only when it's bad." A private date, optional kiss, or fade-to-black is offered; the paid contract would have existed regardless.

**RAVEN, independent accountability and available:** On a modest station balcony, he shows Mara the public record of his testimony and explains his own plans. If she freely chooses to pursue him and the reciprocal route was authored, they make plans for a date. Crystal's separate life and valid grievances remain intact. If any guard fails, Mara refuses without being penalized.

**SOLO or FRIENDSHIP:** Mara and her mother go through a care plan with a coordinator and then discuss an ordinary trip together. She may pursue a licensed independent fighter/mechanic co-op, paid training, or a new tournament when ready. Ari, Plug, Raven and others remain people in her life, not collectible prizes. The finances are improved **only to the extent shown in the ledger**.

**Final image:** Flail's battered armor hangs beside a new, carefully stamped safety plate. Mara chooses to leave one old scratch visible. For once she does not need to hide what it cost to get here.

---

## First-pass scene budget and branch-production notes

- 6 chapters; `M1.1–M6.5` contain shared mandatory anchors, optional character interactions, and mutually exclusive variants. Standard combat replay scenes can use shared footage with different VO; never generate an official combat win from a romance choice.
- Reuse service bay, care-call room, practice hall, rooftop pool, safety archive and Nova hub. Mara's mother needs **at least two** distinctive non-financial personal interests and a final independently chosen care preference (to be decided by the author) rather than becoming a passive quest objective.
- Film all three investigation specializations as *different useful labor* with one shared truth, not as three different levels of proof. Keep Ren, Angel, Crystal, Leena and the technical team competent in their own roles.
- Keep the adult fanservice **optional and tasteful**: attractive adult fighters, intimate but nonexplicit staging, playful self-aware glamour, occasional kisses and fade-to-black; consent and actual relationship state apply. Camera behavior never assumes Mara wants to be objectified.
- The exact proposed debt amounts, payment schedule, awards, underlying illness, compatibility/preferences for Plug and Raven, Ari's off-player NII branch, while alternative *nondefault* Kreissack dispositions remain **unratified production questions**.
<!-- END EXACT SOURCE SCENE -->


---

### Ren


#### FS-REN-R1-3 — R1.3 — Somebody who can dance badly [OPTIONAL / NEW CIVILIAN]

**Source:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PLAYFUL_FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R1.3 — Somebody who can dance badly [OPTIONAL / NEW CIVILIAN]
**[FANSERVICE: FS-REN-R1-3 | type=PLAYFUL_FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**EXT. ZERO-G PERFORMANCE TERRACE — LATER**
**[BG: BG-SOC-VIEW@BASE]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

The event has hired an independent movement troupe. Its choreographer, **Tessa Kade**, 30, specializes in movement and accessibility for people who cannot use conventional exoskeleton controls. She is an exhibitor for a civilian cooperative, not a WAR researcher, clinician, or member of Ren's competition staff.

Ren watches a performer cross a low-gravity ribbon without making the small corrections that consume most pilots' attention.

**TESSA:** “I can tell you're calculating the trajectory.”

**REN:** “I can tell I'm doing it incorrectly.”

**TESSA:** “Good. It means you're watching the dancer instead of just the machine.”

She offers a hand toward the edge of the practice surface—not a demand. Ren can accept an improvised dance step, ask for a demonstration, or return later. Ren's attempt is exquisitely precise and completely lacking in rhythm.

**TESSA:** “Technically impeccable. Emotionally, you look like you've been subpoenaed.”

**REN:** “That's the nicest correction anyone has given me this week.”

The performance ends in applause. Tessa has an early rehearsal and refuses a sponsor's request to pose beside Helix. She has her own professional priorities.

**CHOICE R1-C3:** Dance / ask about her accessibility designs / decline with warmth. All three can begin a friendship; mutual romance requires later choices from *both* people.
<!-- END EXACT SOURCE SCENE -->


#### FS-REN-R2-4 — R2.4 — The rooftop experiment [OPTIONAL / FAN SERVICE / ANGEL OR TESSA FRIENDSHIP]

**Source:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R2.4 — The rooftop experiment [OPTIONAL / FAN SERVICE / ANGEL OR TESSA FRIENDSHIP]
**[FANSERVICE: FS-REN-R2-4 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. ROOFTOP POOL AND TRAINING DECK — NIGHT**
**[BG: BG-SOC-POOL@NIGHT]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

A party for the pilots turns the poolside into a fashion disaster of half-dried training clothes and improvised bathing outfits. Lyra demonstrates a spectacular dive. Shirro tries to copy her and lands with a cannonball that soaks a displeased Milano.

**LYRA:** [PERF: tone=excited | expression=EXP-BRIGHT | delivery=animated | intensity=1] “Ten points for commitment!”

**MILANO:** “I'll remember that when I negotiate your next endorsement.”

Angel is sitting at the quiet end of the deck in a practical dark swimsuit, calibrating a palm-sized recorder. Ren approaches in borrowed pool clothes that are a size too large.

**ANGEL:** “Did your machine choose the outfit?”

**REN:** “No. The machine would have checked the dimensions.”

She smiles despite herself. The recorder's private screen shows two drift lines, one controlled by WAR and the other by an independent oscillator.

**ANGEL:** “If they disagree, one clock is lying. That's not the same as knowing who lied.”

Ren can discuss timing, splash Angel playfully **only if she initiates that mood**, or leave her alone. The moment can build trust or attraction, but never yields a clue unavailable from the mandatory independent record.

At the opposite end, Tessa's troupe is rehearsing a floating ribbon routine. Ren may instead join a brief, mutually invited partner practice. Tessa catches them after an overcommitted turn; they laugh, close enough to notice one another's breath, then step apart on their own initiative.

**CHOICE R2-C2:** Spend time with Angel / Tessa / Lyra and the ensemble / take a private break. No choice establishes exclusivity yet.
<!-- END EXACT SOURCE SCENE -->


#### FS-REN-R3-4 — R3.4 — A quiet question [OPTIONAL / ANGEL]

**Source:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `QUIET_ROMANCE` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R3.4 — A quiet question [OPTIONAL / ANGEL]
**[FANSERVICE: FS-REN-R3-4 | type=QUIET_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. PRACTICE CORRIDOR — NIGHT**
**[BG: BG-ARE-PREPTUN@NIGHT]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Angel finds Ren holding a half-drunk cup of vending-machine tea beside an empty repair bay.

**ANGEL:** “You like the technology.”

**REN:** [PERF: tone=hopeful | expression=EXP-HOPE | delivery=quietly hopeful | intensity=1] “I love the idea of it.”

**ANGEL:** “Sometimes that's what makes it hard to read the terms.”

**REN:** “You think I should stop.”

**ANGEL:** “I think you should be allowed to stop. And be believed when you say stop.”

She hands them a small offline clock, with its write port physically removed. Their fingers brush. Neither pretends not to notice.

**CHOICE R3-C2:** Ask Angel whether the invitation is personal / thank her as a colleague / ask for space. **If personal:**

**REN:** “Is this because you need my help?”

**ANGEL:** “If I needed your help, I'd ask for it. This is something else. I haven't worked out what.”

A restrained, intriguing pause. No kiss while Ren is distressed and seeking support in the middle of an unverified neurological episode; a later mutual romantic choice remains possible.
<!-- END EXACT SOURCE SCENE -->


#### FS-REN-R4-4 — R4.4 — Unobserved [OPTIONAL / ROMANTIC TENSION]

**Source:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_TENSION` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R4.4 — Unobserved [OPTIONAL / ROMANTIC TENSION]
**[FANSERVICE: FS-REN-R4-4 | type=ROMANTIC_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. EMPTY GLASS CORRIDOR — LATER**
**[BG: BG-TEC-SERVICE@BASE]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Angel is exhausted. She and Ren stand near the quiet side of the habitat while Jupiter rotates beyond the glass.

**REN:** “If I ask you to stay, are you going to assume I need help with the data?”

**ANGEL:** “Do you?”

**REN:** “No.”

Angel considers the answer. She takes Ren's hand **only if the player has previously signaled personal interest and she has reciprocated**.

**ANGEL:** [PERF: tone=hopeful | expression=EXP-HOPE | delivery=quietly hopeful | intensity=1] “I need to be able to walk away from a question. Even a good one.”

**REN:** “So do I.”

They stay for a minute. On a friendship route, they exchange an affectionate joke about whether a sunset can be independently calibrated. If the relationship has been rejected or distance requested, Angel keeps it professional. No jealousy penalty for Ren's alternate civilian friendship.
<!-- END EXACT SOURCE SCENE -->


#### FS-REN-R5-5 — R5.5 — After the cameras [OPTIONAL / ROMANCE WITH CONSEQUENCES]

**Source:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PRIVATE_ROMANCE` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R5.5 — After the cameras [OPTIONAL / ROMANCE WITH CONSEQUENCES]
**[FANSERVICE: FS-REN-R5-5 | type=PRIVATE_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. QUIET HALLWAY / OBSERVATION GARDEN — NIGHT**
**[BG: BG-ARE-ENTRY@BASE -> BG-SOC-GARDEN@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Ren has time to invite *one* person for a private moment, or nobody. Romance is not unlocked by defeating an opponent or exposing Varga. Mutuality and consent must be established in earlier dialogue. **If Ren is experiencing an acute disorienting episode, or the advanced interface's executive write-path has not been physically isolated for the occasion, intimate escalation is deferred.** Ordinary companionship remains available.

**[ANGEL PATH, if mutually eligible]**

Angel meets Ren at the observation garden. Ren has left their recorder on the table, powered down; the suspicious connection is isolated by an independently confirmed switch.

**ANGEL:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] “I want to kiss you. That is a very inconvenient thing to know about myself.”

**REN:** “I could write it in the report.”

**ANGEL:** “You could try.”

They laugh. Angel asks, clearly, **“May I?”** Ren can say yes, not yet, or stay friends. If yes, they kiss, tentative and then assured. The camera turns toward Jupiter and the scene closes on their hands together. Angel does not promise to join Ren's research, reveal her past, or accept permanent proximity.

**[TESSA PATH, if mutually eligible]**

Tessa has stayed late to dismantle the troupe's set. Ren offers to help; she refuses because the venue contract requires trained riggers. Instead she invites Ren to the empty dance floor. A slow light travels across it.

**TESSA:** “No tracking marks. No score. You can even miss a step.”

**REN:** “That sounds radical.”

She takes Ren's hand after receiving an affirmative response. They move awkwardly, then beautifully, for reasons that have nothing to do with neural latency. She leans closer, then stops close enough to ask. Ren can kiss her or choose friendship without embarrassment. If they kiss, the next image is the empty floor after the music stops. Tessa makes no promise to move into the WAR world.

**[FRIENDSHIP OR SINGLE]** Ren shares a late meal with Lyra and Cossette, or spends a contented hour alone repairing a harmless toy HAR for a child from the exhibition. The emotional beat is complete, not a punishment for declining romance.

**CHAPTER OUT:** A projected diagram of the championship relay appears on Ren's independent recorder. The system's planned command route would place a **new executive layer** between pilot intention and network action. Ren understands that simply beating a mechanical opponent will not close it.

---

# CHAPTER 6 — WHO GETS THE FINAL SAY
*Championship day. Dramatic question: What does it mean to remain a person when something more capable offers to decide for you?*
<!-- END EXACT SOURCE SCENE -->


---

### Angel


#### FS-ANGEL-A2-3 — A2.3 — Photogenic anonymity [OPTIONAL / FANSERVICE]

**Source:** `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`  
**Scope:** `FULL_SCENE` | **Category:** `GLAMOUR` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### A2.3 — Photogenic anonymity [OPTIONAL / FANSERVICE]
**[FANSERVICE: FS-ANGEL-A2-3 | type=GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**INT. ATHLETE LOUNGE / COSTUME EXHIBITION — EVENING**
**[BG: BG-ARE-LOUNGE@EVENING]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

At a sponsor's retro-HAR fashion show, a stylist presents Angel with a dramatic chrome-and-violet coat designed to echo Chronos. Its sleeves are beautiful and wildly impractical.

**STYLIST:** “It's your public silhouette.”

**ANGEL:** [PERF: tone=amused | expression=EXP-SMILE | delivery=light, teasing | intensity=2] “My public silhouette has pockets.”

She can try the coat and make an unexpectedly elegant entrance; alter it with a pair of hidden pockets; or laugh and decline. The cameras are announced and opt-in. If she participates, **LYRA**, a professional athlete and model celebrity, graciously shares the stage without trying to unmask her.

**LYRA:** “You look like a secret that knows it's expensive.”

**ANGEL:** [PERF: tone=teasing | expression=EXP-SMIRK | delivery=playful | intensity=2] “You look like you have a better contract.”

**CHOICE A2-C2:** Pose / redesign the look / skip. Cosmetic dialogue and short comic crowd reactions only. No swimsuit ambush, unrequested body shots, stats, evidence, or romance flags.
<!-- END EXACT SOURCE SCENE -->


#### FS-ANGEL-A3-3 — A3.3 — The edges of trust [OPTIONAL / RELATIONSHIPS]

**Source:** `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_TENSION` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### A3.3 — The edges of trust [OPTIONAL / RELATIONSHIPS]
**[FANSERVICE: FS-ANGEL-A3-3 | type=ROMANTIC_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. QUIET OBSERVATION GREENHOUSE — EVENING**
**[BG: BG-SOC-GARDEN@EVENING]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Angel meets one of three people, depending on prior nonexclusive contact. The player may also decline the meeting and keep strong friendships.

**REN (if invited):** “You never ask questions you haven't already checked.”

**ANGEL:** “That's not true. I asked you to come.”

Ren smiles, then looks away. Their stillness may be nerves or side effects; Angel does **not** treat ambiguity as consent. They discuss trust, independence, and whether a future date with every sensor switched off might be welcome. A nonromantic reply is accepted with equal warmth.

**CRYSTAL (alternative):** “I can make them listen. You can make sure what they hear is real.”

**ANGEL:** “You could also make me the story.”

**CRYSTAL:** “Then tell me the limits before I do.”

An adult slow-burn attraction is *possible* but strictly proposed. Crystal's unresolved Raven relationship must first be honestly resolved, and public advocacy must never be traded for affection. She may instead become a lifelong friend.

**LEENA (alternative):** “I know the city without a map. You know where the missing pages should be.”

**ANGEL:** “Is this a professional pitch?”

**LEENA:** “Until I know it isn't.”

They agree on separate disclosure and source-custody roles, or end the conversation as two professionals. If later romantic, Leena must leave direct reporting/custody of Angel's case to an independent journalist; Ari's alternate relationship commitment must also be cleared. This is a proposal, not a default pairing.

**CHOICE A3-C1 — relationship intention:** `ren` / `crystal` / `leena` / `friendship` / `single`. A declared intention grants no kiss, exclusive record, or obligation. The other person independently chooses reciprocity later. Never show multiple simultaneous incompatible romantic endings.
<!-- END EXACT SOURCE SCENE -->


#### FS-ANGEL-A4-4 — A4.4 — Rooftop, no cameras [OPTIONAL / FAN SERVICE / FRIENDSHIP]

**Source:** `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### A4.4 — Rooftop, no cameras [OPTIONAL / FAN SERVICE / FRIENDSHIP]
**[FANSERVICE: FS-ANGEL-A4-4 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. HOTEL ROOFTOP POOL — NIGHT**
**[BG: BG-SOC-POOL@NIGHT]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

The pilots have been invited to a private after-hours social event. Shirro calls it a *low-visibility luxury experience*, which prompts Angel to count the cameras. The host voluntarily turns the remaining publicity drones away from a cordoned section.

Angel can swim in an understated black suit, keep her clothes on and play cards by the water, or leave. Ren arrives wearing a ridiculous oversized resort shirt; Lyra has precisely the amused expression of someone who knows it is ridiculous.

**LYRA:** “Is that shirt an engineering prototype?”

**REN:** “It has seven pockets.”

**ANGEL:** “Finally, responsible design.”

An optional playful dance, competitive diving joke, or mutual quiet conversation provides glamour and comedy with **no** unconsented voyeurism and no required romance. Crystal can sit beside Angel without asking about her case. Plug wins a poolside mechanical puzzle that nobody else knew was a competition.

---

# CHAPTER 5 — THE GOOD THING IT DID
*Days 11–12. Question: Can a good act make an illegitimate power legitimate?*
<!-- END EXACT SOURCE SCENE -->


#### FS-ANGEL-A5-4 — A5.4 — Unobserved [OPTIONAL / ROMANCE]

**Source:** `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `PRIVATE_ROMANCE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### A5.4 — Unobserved [OPTIONAL / ROMANCE]
**[FANSERVICE: FS-ANGEL-A5-4 | type=PRIVATE_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**EXT. OBSERVATION GARDEN / PRIVATE RESTAURANT — NIGHT**
**[BG: BG-SOC-GARDEN@BASE -> BG-SOC-RESTAURANT@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**REQUIRED BEFORE ANY ROMANTIC SCENE:** Both participants are verified adults and independently interested; neither is in an incompatible ongoing relationship; no professional access is exchanged for romance. Ren additionally must be fully alert and able to consent, with an independently verified disconnected high-bandwidth interface. An unfinished research session, medical uncertainty, or acute episode **suppresses romance, not friendship**. Leena must have handed the case to an independent reporter and be free of the Ari romance branch; Crystal must have resolved her Raven commitment. Ineligible routes use the friendship variant below.

**IF REN IS CHOSEN AND ELIGIBLE:** Ren waits outside the restaurant with two tickets to an event that has no screens and no measurements. Angel notices Ren has left the diagnostic device behind.

**REN:** “I asked them to turn the sensors off.”

**ANGEL:** “No sensors? That's almost a romantic gesture.”

**REN:** “It was intended as one.”

Angel can take Ren's hand, ask for a slow evening without a physical gesture, or say she'd rather remain friends. If both choose a kiss, it is brief, conscious, and unmistakably mutual. Later intimacy is private and fades to black. Ren's illness is neither cured nor romanticized.

**IF CRYSTAL IS CHOSEN AND ELIGIBLE:** After a long public hearing, Crystal arrives without her security retinue or a camera. Angel jokes about the surreal novelty of seeing the city's most visible woman alone.

**CRYSTAL:** “You're the only person I know who doesn't ask me to be a symbol.”

**ANGEL:** “You'd make a very inconvenient symbol. You move too much.”

Crystal leans toward Angel only after a direct, answered invitation. The scene ends at the balcony door or with both agreeing to take time. Their affection does not resolve the Devroe case or erase Crystal's history with Raven.

**IF LEENA IS CHOSEN AND ELIGIBLE:** Off assignment, Leena brings a battered book to an ordinary night café. She has transferred the case, not suppressed it, and tells Angel what she can discuss without breaking source protections.

**LEENA:** “I know we can't have the story between us.”

**ANGEL:** “That's the most attractive thing anyone has said to me this week.”

Angel proposes a genuine date without a notebook. Leena may agree or decline independently; the screenplay requires both choices to align. A kiss or warm parting follows. No private case information becomes romance currency.

**IF FRIENDSHIP, SINGLE, OR ANY GATE FAILS:** Ren, Crystal, Leena, or Plug can share a late meal and exchange jokes. There is no “friend-zone punishment” and no loss of plot clues. Angel may choose solitude gladly rather than as an automatic failure ending.
<!-- END EXACT SOURCE SCENE -->


#### FS-ANGEL-A6-5 — A6.5 — Optional human futures [EPILOGUE / RELATIONSHIP AND IDENTITY]

**Source:** `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### A6.5 — Optional human futures [EPILOGUE / RELATIONSHIP AND IDENTITY]
**[FANSERVICE: FS-ANGEL-A6-5 | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**EXT. CITY RIVERFRONT / SMALL WORKSHOP / OPEN-AIR CAFÉ — MONTHS LATER**
**[BG: BG-SOC-TRANSIT@BASE -> BG-INV-CONFERENCE@BASE -> BG-SOC-CAFE@AFTERMATH]**
**[MUSIC: MUS-AFTERMATH | behavior=palette; continue_same_theme_unless_edited]**

**IF `identity_policy=masked`:** Angel remains publicly pseudonymous under controlled witness protections, but no longer pretends the old archive was somebody else's responsibility. She takes a formal role with a narrowly scoped independent technical watchdog, or continues research privately while ensuring her findings can be verified.

**IF `identity_policy=controlled`:** She becomes a technically respected commentator who speaks at selected hearings and declines celebrity interviews with spectacular politeness.

**IF `identity_policy=public`:** She speaks on record about her responsibility and the error of mistaking isolation for safety. She keeps some parts of her life private even now. Public identity is not total access.

**IF ANGEL IS OFFICIAL CHAMPION:** She can fund an independent evidence-preservation initiative with part of her actual prize or support a regulator-independent safety standard. The championship is earned on the arena floor and cannot magically settle lawsuits.

**IF NOT CHAMPION:** Her evidence and work still matter. She pursues funding through an external technical coalition or continues a smaller archive. Losing a fight neither ruins her character nor erases her contribution.

**IF ROMANCE WITH REN ELIGIBLE AND MUTUALLY CHOSEN:** The two share breakfast at a small café where neither is taking data. Ren still needs careful medical follow-up and independently governed research. **REN:** “You promised not to read my logs.” **ANGEL:** “I am learning to survive the suspense.” A kiss or easy companionable touch is theirs to choose. No shared neural link becomes a metaphorical wedding ring.

**IF ROMANCE WITH CRYSTAL ELIGIBLE AND MUTUALLY CHOSEN:** At a quiet workshop, Crystal sets down a newspaper showing both their names, or Angel's chosen pseudonym. **CRYSTAL:** “Would you like me to tell them we met in a fight?” **ANGEL:** “We met arguing about who was allowed to know me.” They exchange a private smile and choose an ordinary evening, with Raven's unresolved history handled rather than erased.

**IF ROMANCE WITH LEENA ELIGIBLE AND MUTUALLY CHOSEN:** Leena waits with two coffees and no recorder. Her independent reporting beat continues with a separate journalist handling Angel's case. **LEENA:** “I brought no questions.” **ANGEL:** “That sounds suspicious.” Their intimacy is a choice between people, not a scoop.

**IF FRIENDSHIP:** Angel, Ren, Crystal, and Plug have learned how to work together without invading one another. She attends a small gathering voluntarily, and for once stays after everyone has stopped discussing the case.

**IF SINGLE:** She lives alone because she enjoys it, not because every choice led to loneliness. She accepts an invitation to repair a friend's ancient radio, then declines the invitation to become their public face. Anonymity and isolation are no longer synonyms.

**FINAL IMAGE:** An archival terminal boots in a modest workshop. Under the entry for **NOVA**, the phrase “destroyed, 2097” has been corrected with independently verified dates and a reference to the inquiry. Angel closes the record, switches off the monitor, and walks into the daylight. The last screen we see belongs to no machine at all.

---

## Authoring and production notes (not canonical developments)

1. **Historical involvement unresolved:** Angel's possession of a partial archival checksum is a *proposed* narrative device; don't invent direct culpability, a personal neural implant, or a hidden Kreissack family tie until approved. Her unique contribution is historical provenance and evidence accountability, not omniscient hacking.
2. **Definitive reveal timing:** active identifier (Ch1), legacy permission anomaly (Ch2), intention timing concern (Ch3), living Kreissack (Ch4), genuine rescue (Ch5), covert AI veto (Ch6). No prematurely correct omniscience in earlier scenes.
3. **Group match order:** screen shows Jean-Paul `GD2` before Dante `GD1`; engine sees Dante first. Route dispatcher MUST translate by match ID. If she wins both, Angel is D1 and faces Group C runner-up in Q4; as D2 she appears in Q3; as D3 she has no knockout match. Default Q4 loss to Lyra is not mandatory for the player.
4. **Secondary characters:** Plug supplies authorized hardware corroboration; Jean-Paul adds social/intelligence pressure without becoming exposition machinery; Ren offers intention timing; Crystal public witness protections; Leena a possible independent reporter/romance option only after recusal; Lyra/Dante are authentic rivals. None disappears because the player declines romance.
5. **Relationship exclusivity:** Angel–Ren, Angel–Crystal, Angel–Leena are **mutually exclusive alternate proposals**, with external Ren–Tessa, Crystal–Raven, and Ari–Leena commitments respected. Leena's exact adult age, preference, and independent career protections need approval. Angel's exact adult age remains provisional. Intimacy always adult, voluntary, and private; scenes fade to black.
6. **Disclosure is not dangerous source publication:** all routes keep personal medical data and actionable neural-integration implementation details under independent access controls. A publicly verifiable *finding* need not include a complete technical replication recipe. This route explores different credible accountability methods, not an option to conceal all evidence indefinitely.
7. **Cinematic budget:** every match branch needs winner/loser inserts; alternate opponents may require different fight banter. Several significant consent, law, professional-boundary and laboratory-safety questions remain for specialist editorial review. Any real-life legal or medical detail in this fiction is speculative and needs research before production.
<!-- END EXACT SOURCE SCENE -->


---

### Crystal


#### FS-CRYSTAL-C2-4 — C2.4 — Red carpet, unguarded [OPTIONAL GLAMOUR / FAN SERVICE]

**Source:** `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.9.md`  
**Scope:** `FULL_SCENE` | **Category:** `GLAMOUR` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### C2.4 — Red carpet, unguarded [OPTIONAL GLAMOUR / FAN SERVICE]
**[FANSERVICE: FS-CRYSTAL-C2-4 | type=GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**INT. POST-MATCH PUBLICITY STUDIO — NIGHT**
**[BG: BG-SOC-PRESS@NIGHT]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

A fashion house wants Crystal in an extravagant reinterpretation of Jaguar's scarlet armor. She chooses a silk evening suit, a sharply cut dress, or her original athletic jacket; the camera can appreciate her confidence without removing her control of what is photographed. LYRA is in the adjacent studio, spectacular in an illuminated outfit, cheerfully coaching Crystal in how to refuse an intrusive photographer.

**LYRA:** Tell them no. The good ones will ask what you want instead.

**CRYSTAL:** You're thirty years younger than my public image.

**LYRA:** And that's why we're fixing it.

Raven arrives with an urgent warning: the photographer's sponsor appears on the shuttle-log custody chain. Crystal wants to follow when he says “Come.” She deliberately asks **why** first. He tells her what he can substantiate, not “trust me.”

**Chapter end:** A second independent records source matches the timestamp gap. Someone altered custody metadata after the shuttle incident; the actor and purpose remain unknown.

---

# CHAPTER 3 — THE RIGHT KIND OF POWER
**Days 6–7 | Dramatic question: Can she admit what she wants without giving away what she is?**
<!-- END EXACT SOURCE SCENE -->


#### FS-CRYSTAL-C3-1 — C3.1 — Rooftop without armor [OPTIONAL ENSEMBLE FAN SERVICE / COMEDY]

**Source:** `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.9.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### C3.1 — Rooftop without armor [OPTIONAL ENSEMBLE FAN SERVICE / COMEDY]
**[FANSERVICE: FS-CRYSTAL-C3-1 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. OBSERVATION-DECK POOL — SUNSET**
**[BG: BG-SOC-POOL@SUNSET]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

Jupiter hangs over a rooftop pool. Elite athletes are unexpectedly ordinary in swimsuits, old scars and bad jokes. LYRA has organized an informal celebration, with designer swimwear, music and a miniature Jaguar pool float that appears to be stalking PLUG's inflatable Flail. COSSETTE and IBRAHIM calmly ignore the chaos.

Crystal wears a dark red swimsuit under a borrowed wrap, relishing anonymity for ten seconds. Raven is already there in a plain shirt, looking as though someone has threatened him with recreation.

**CRYSTAL:** [PERF: tone=grieving | expression=EXP-GRIEF | delivery=strained | intensity=2] You dressed for a funeral.

**RAVEN:** I saw the guest list.

They take turns challenging each other to keep a completely straight face through the others' dreadful poolside interviews. An optional private glance can be charged; a friendship branch becomes a rare unguarded laugh. No photographer gets a private image without consent.
<!-- END EXACT SOURCE SCENE -->


#### FS-CRYSTAL-C3-2 — C3.2 — The words neither has said [OPTIONAL RAVEN PATH; CHOICE IS NOT RECIPROCITY]

**Source:** `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.9.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `DARK_TENSION` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### C3.2 — The words neither has said [OPTIONAL RAVEN PATH; CHOICE IS NOT RECIPROCITY]
**[FANSERVICE: FS-CRYSTAL-C3-2 | type=DARK_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=attraction-not-consent; coercive options are NOT fanservice rewards]**
**INT. QUIET GALLERY, OFF THE POOL — NIGHT**
**[BG: BG-SOC-VIEW-PRIVATE@NIGHT]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Crystal comes because she wants an explanation for their unmistakable chemistry, not because Raven has summoned her. A translucent wall looks out over Jupiter. He stands at the far end, leaving her the door.

**CRYSTAL:** [PERF: tone=sad | expression=EXP-SAD | delivery=subdued | intensity=1] You speak and something in me moves before I've decided to move. I hate that you know.

**RAVEN:** I know you dislike it. I don't know what it means unless you tell me.

He enjoys how easily she watches for his reaction. In a **restrained NPC branch**, he refuses to treat that reaction as consent. In a **predatory NPC branch**, he tests whether her attraction can be traded for silence or separation from Christian; this is documented manipulation, and the private-romance gate closes regardless of how she initially responds.

**CRYSTAL:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=2] I think I want to be able to surrender control with you. Not to be controlled everywhere. Just—when I choose to stop holding everything up.

**RAVEN (restrained branch):** Then the choosing matters more than the surrender.

**RAVEN (predatory branch):** You could let me decide which questions hurt you.

**CRYSTAL (predatory branch, after reflection):** I postponed that witness call because you made me doubt my own judgment. The witness left. That's not an invitation. I'm leaving.

In the **predatory branch**, his manipulation can briefly succeed, costing an opportunity to interview a departing witness. The independently preserved shuttle evidence remains available. Once she recognizes the pressure, Crystal leaves, informs Christian or a trusted investigator, and refuses to let the delay become permanent silence. No D/s scene follows. In the **restrained branch**, Raven admits he likes having power over her and wishes to lead privately but, for this moment, does not demand the role; he does not receive intimacy as a reward for saying the right words.

`CHOICE — D/s intention`:

1. **Explore privately:** acknowledge desire for a consensual dominant/submissive dynamic, with negotiated limits, ongoing check-ins and a way to stop immediately. This is a **proposal**, not a commitment or blanket permission.
2. **Acknowledge desire, refuse the relationship:** she can feel submissive and still decide that Raven is too secretive to trust.
3. **Leave the subject open:** no enacted dynamic now; potential later reconsideration, if explicitly chosen.

Only on a reciprocal, **non-coercive restrained** exploration path do they agree that **“Stop” ends any scene immediately; “Slow” means pause and check in**. Consent is situation-specific; no orders concerning tournament outcomes, political statements, family investigation, access credentials, or whether she may leave. She will not accept demands that conceal evidence. Raven can also decline a scene at any time.

**CRYSTAL:** There's one thing you will not decide for me.

**RAVEN:** Name it.

**CRYSTAL:** The truth about my parents.

**RAVEN:** I should have told you sooner.

She moves toward him; he does not close the remaining distance.

**CRYSTAL:** Then tell me. Not tonight if you can't. But until you do, this goes no further.

Even on the exploration path there is no private intimacy that buys forgiveness. The moment can end with a consenting, restrained hand touch—if *both* choose—or with her leaving without it.
<!-- END EXACT SOURCE SCENE -->


#### FS-CRYSTAL-C6-5 — C6.5 — Private endings [EXCLUSIVE ELIGIBLE VARIANTS]

**Source:** `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.9.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `CONSENSUAL_DS` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### C6.5 — Private endings [EXCLUSIVE ELIGIBLE VARIANTS]
**[FANSERVICE: FS-CRYSTAL-C6-5 | type=CONSENSUAL_DS | scope=OPTIONAL_BEAT | status=REVIEW | note=consensual-post-accountability-only; no exploitation reward]**
**[BG: BG-SOC-VIEW-PRIVATE@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**A. Raven — The open hand (D/s romance, WEEKS AFTER HEARING):** Only if both are uncommitted, independently choose each other *with full knowledge* that Raven blocked the family's distress relay and ignored a chance to restore it, have an explicit boundaries agreement, Raven has given truthful testimony to an independent process, **and there is no active Raven coercion or evidence-for-intimacy incident**. This ending is possible, not guaranteed, and never discontinues the case. His guilt or innocence is not settled by intimacy. At her apartment, Crystal leaves the championship medal (if any) on a table. He asks, **“Would you like me to take the lead tonight?”** She answers yes. Later, standing beside him at the window, she announces she will testify again next week. He says, **“I know.”** Her private submission is a chosen space of trust, not her public role and not an unbreakable bond. Their next morning is ordinary, affectionate, teasing, and open to renegotiation.

**B. Raven — Attraction without reconciliation:** If he does not disclose, exploits her attraction, one of them withdraws consent, or Crystal refuses a relationship, her involuntary submissive response still exists. She decides not to act on it. In a corridor he says her name. She feels the familiar pull; she continues walking toward Christian and the hearing. The narration never frames this as failure to be true to herself.

**C. Angel — A different kind of closeness (proposal):** With independent adult confirmation, reciprocal interest, a clear prior Raven separation, and no conflict with Angel's other commitments, Crystal and Angel share an unhurried private supper and may choose a mutual kiss. Crystal does not have to extinguish all feelings for Raven to decide not to enact them. Angel has her own autonomy and may instead choose friendship.

**D. Friendship / solo:** Crystal meets Christian for a late dinner after a difficult hearing. They disagree about an investigative strategy and still enjoy each other's company. She spends some nights alone, grateful that no one asks her to perform the legend. A voluntary, private desire she never acts upon remains one true part of her, not the measure of her completeness.

**Final image:** The old victory statue remains in the museum. On its pedestal someone has added a smaller plaque with an independently maintained archive link. Crystal walks past it with no entourage. She doesn't need to look back.

---

## Scene-gating summary

| Scene | Show when | Fallback / nonromantic route |
|---|---|---|
| C1.2 instinctive Raven response | Always | She may refuse every subsequent invitation |
| C2.1 Selene | Always, `GA2` | Outcome recorded by fight engine |
| C2.2 Raven practice | Optional | Same training access through technician |
| C2.3 Ari | Always, `GA1` | Actual standings after both matches |
| C3.2 negotiated D/s | Only if Crystal initiates discussion | Decline or leave; no evidence lost |
| C4.1 QF | Only A1/A2 | Honest investigation if A3 |
| C4.3 Raven deposition | Always as an independent investigation | Legal records available without romance; Raven may resist |
| C4.4 Angel | Optional and adult/commitment gated | Strong professional friendship |
| C5.1 SF | Only QF win | Real broadcast and investigation |
| C5.2 rescue | Always Day 12 | Same true rescue under all routes |
| C5.3 romantic scene | Only explicit reciprocal consent and sufficient disclosure | Conversation, solo, or family scene |
| C6.1 official final | Only SF win | Actual other finalists and official trophy |
| C6.2 Nova reveal | Always after FINAL | No early hidden-veto knowledge |
| C6.3 special boss | All routes, separate | No title awarded |
| C6.5 romance ending | Exactly one eligible option | Friendship or solo |

## Authorship notes and deliberate open questions

1. **Settled by user:** Crystal's involuntary submissive attraction to Raven and the naturally D/s shape of a mutually chosen relationship. Not settled: the exact practices, whether they end together, whether Raven is cleared of historical wrongdoing, and how much prior sexual history they had.
2. **History resolved in working sequel canon v1.5:** Kreissack ordered the murder; Raven authorized the distress blackout, knowingly failed to restore it, then falsified the records; the contractor's separate lethal command directly caused the deaths. Judicial disposition, the contractor coder, and precise damages remain unresolved; **Kreissack is the senior assassination authorizer in sequel canon v1.7**. No completed acquittal may be assumed.
3. **Tournament policy pending:** 1–1–1 standings currently use provisional published seed; all nondefault NPC knockout outcomes are flagged provisional by engine.
4. **Angel alternative is optional and not canonized:** adult identity, reciprocal desire, exclusivity and shared-state resolution are required; Crystal's pull toward Raven need not disappear in an Angel or solo route.
5. **Tone:** glamorous and sensual without explicit sexual descriptions; D/s is an adult private relationship dynamic, not a combat mechanic, not a neural-implant consequence, and not a substitute for consent, testimony or responsibility.


**v1.4 cross-POV note:** Raven's enjoyment of exploitation is established in every route. The compassionate lines in this Crystal screenplay appear **only** when his independent NPC conduct permits them; the v1.4 Raven campaign includes genuinely predatory alternatives. The active `raven_coercion_recorded` state must suppress private romance even if Crystal is attracted to him.
<!-- END EXACT SOURCE SCENE -->


---

### Raven


#### FS-RAVEN-R3-2 — R3.2 — Crystal's reflex and Raven's choice [OPTIONAL; NOT A CONTRACT]

**Source:** `16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.8.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `DARK_TENSION` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R3.2 — Crystal's reflex and Raven's choice [OPTIONAL; NOT A CONTRACT]
**[FANSERVICE: FS-RAVEN-R3-2 | type=DARK_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=attraction-not-consent; coercive options are NOT fanservice rewards]**
**INT. QUIET CONSERVATORY — EVENING**
**[BG: BG-SOC-GARDEN@EVENING]**
**[MUSIC: MUS-CONFRONT | behavior=palette; continue_same_theme_unless_edited]**

Crystal enters freely. She has insisted the door remain unlocked. The distant music of the anniversary retrospective comes through the walls. She is dressed for a private reception, not a confrontation. Raven notices the open throat of her dress, the nervous adjustment of a glove, and her determination not to reveal the nerves.

**CRYSTAL:** I want to understand what happens around you. I don't want you to define it for me.

**RAVEN:** You know I like it when you listen.

**CRYSTAL:** I know you like it too much.

He tests the space with silence. Her eyes drop for a moment. The thrill he feels is real; he does not need to deny it to the player. He also recognizes an opening for a trick.

`CHOICE — the temptation:`

1. **EXPLOIT:** Tell her her judgment is clouded and she should postpone contacting Christian until Raven "decides" she is calm. This is a deliberate attempt to isolate her, **not consensual D/s**. For an awful moment it **works**: Crystal puts away her phone and postpones an interview with a departing security witness until morning. The witness departs and the opportunity is lost, though separately secured records preserve the central evidence. When she realizes what Raven engineered, she independently tells Christian and the investigator. Raven is privately exhilarated by the fact he could move her judgment, then confronted with the harm he caused. A manipulation incident is recorded and trust damaged. There is **no romantic reward scene** for obtaining compliance through pressure.
2. **BARGAIN:** Offer private truth only in exchange for a private relationship. Crystal refuses the condition. She may remain attracted, but evidence barter poisons any romance gate until Raven independently discloses and the incident is repaired in ways she accepts, if ever.
3. **DISCLOSE:** Admit, without asking for forgiveness, "I enjoy the part of you that answers me. I could use it against you. Sometimes I want to." Then step back and offer the evidence through her investigator. This is the only choice that preserves a credible possibility of *later* consensual intimacy, and **it does not guarantee one**.
4. **LEAVE:** End the conversation before he acts on the impulse. The attraction continues, but neither trust nor romance automatically advances.

**CRYSTAL (on EXPLOIT/BARGAIN):** You don't get to make a bargain out of my vulnerability.

**RAVEN:** I could have told you what you wanted to hear.

**CRYSTAL:** You still haven't told me what I need to know.

**CRYSTAL (on DISCLOSE):** You just made it sound worse.

**RAVEN:** It is worse.

**CRYSTAL:** [PERF: tone=angry | expression=EXP-GLARE | delivery=hard edged | intensity=2] Good. Then we can stop pretending it isn't.
<!-- END EXACT SOURCE SCENE -->


#### FS-RAVEN-R3-3 — R3.3 — A rooftop full of people who have nothing to hide [OPTIONAL ENSEMBLE / FAN SERVICE]

**Source:** `16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.8.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R3.3 — A rooftop full of people who have nothing to hide [OPTIONAL ENSEMBLE / FAN SERVICE]
**[FANSERVICE: FS-RAVEN-R3-3 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**EXT. JOVIAN VIEW-DECK POOL — SUNSET**
**[BG: BG-SOC-POOL@SUNSET]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

LYRA stages a publicity event that accidentally turns into a pool party. The champions and mechanics appear in bright swimwear, scars and all; several cameras are deliberately pointed away from the private terrace. Plug has constructed a miniature HAR racecourse that is rapidly becoming a public safety problem.

Raven arrives in black. Lyra surveys him with open disappointment.

**LYRA:** You made a swimming pool look like a hostage exchange.

**RAVEN:** I can leave.

**LYRA:** That's how I know it's your idea of a joke.

Mara, still wearing a racing jacket over a swimsuit, beats him at a miniature Katana game and refuses his rematch. Crystal may glance at him across the pool, drawn and wary. Any Raven/Crystal interaction depends on prior conduct; if he pressured her, she avoids private conversation and speaks with friends instead. The cinematography may enjoy glamorous bodies and physical confidence without equating privacy with a lack of attraction.

`CHOICE:` be an unexpectedly good sport / trade flirty banter with an available Mara / leave for the security archive. All are optional; no essential clue is lost. If Mara has a partner or rejects Raven, the scene is friendly or sarcastic only.
<!-- END EXACT SOURCE SCENE -->


#### FS-RAVEN-R6-5 — R6.5 — The ends he cannot choose alone [ENDING DISPATCH]

**Source:** `16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.8.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `CONSENSUAL_DS` | **Review note:** consensual-post-accountability-only; no exploitation reward

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### R6.5 — The ends he cannot choose alone [ENDING DISPATCH]
**[FANSERVICE: FS-RAVEN-R6-5 | type=CONSENSUAL_DS | scope=OPTIONAL_BEAT | status=REVIEW | note=consensual-post-accountability-only; no exploitation reward]**
**[BG: BG-SOC-VIEW-PRIVATE@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

**ENDING A — "A Hand Extended" [strictly gated, optional Raven–Crystal D/s romance].** Weeks after the hearing, Raven has fully admitted the blackout, ignored distress restoration and falsification, accepts independent scrutiny, has no open manipulation or obstruction incident, is free of other commitments, and is met by Crystal's **informed, independent, revocable** reciprocal decision. This possibility is **not** an early post-match reward. They negotiate private authority case by case, not over public reputation, investigations or her family. Crystal may choose to offer him her hand. The darkness in him does not vanish; the dramatic choice is whether he can go without using it against her. *Possible*, not automatically earned by choosing the courteous dialogue options.

**ENDING B — "The Portrait of a Victor" [dark solitude].** Raven may have won the championship and taken a wealthy buyer's money. He has also lost access to Crystal and faces inquiry. In a huge room he can control the lighting, every door, and every camera. No one stays because they want to. His last line: "I thought freedom would feel different." The ending does not imply Crystal secretly regrets leaving.

**ENDING C — "No Witnesses for Love" [exposure and estrangement].** The record of Raven's coercion or attempted evidence barter comes to light. Crystal and Christian pursue separate accounts of the past. Raven may accept responsibility or remain angry; he does not get an apology scene in which she restores him. His future, including legal proceedings, remains unsettled.

**ENDING D — "Professional Distance" [nonromantic alliance].** Raven cooperates with the Nova and Devroe inquiries but declines a relationship he cannot responsibly sustain, or Crystal declines him. He and Crystal may eventually exchange a brief professional acknowledgment. It is not a disguised romantic promise.

**ENDING E — "Two Fighters" [provisional Raven–Mara].** Only if Mara is demonstrably free, independently interested, and the Crystal relationship has been clearly closed. Neither a sponsor referral nor tournament victory is a courtship currency. Their banter becomes a mutual adult attraction built around candid challenge, not the assumption Mara shares Crystal's submissive response. If any condition fails, revert to friendship/solo. This is a **proposal**, not new canon.

**ENDING F — "The Unpaid Debt" [complicated attempt at repair].** Raven eventually supplies missing evidence and accepts that Crystal will not reconcile. He does useful, accountable work without receiving forgiveness as compensation. He still sometimes remembers the thrill of making her turn when he spoke. The memory is not a prophecy; it is a temptation he has learned to name.

**Final image:** Katana's blade hangs behind glass, not in a shrine but in a forensics room. The engraved plate describes the machine's victories and defeats accurately. It says nothing about the man who piloted it. That story remains contested by the people who survived him.

---

## Continuity / editorial constraints

1. Raven's **enjoyment of exploitation** is a stable dark character trait. Player choice changes *whether he acts on it and how far*, not whether it exists. Do not soften him into a reliable, universally considerate dominant; do not imply he becomes safe through attraction alone.
2. Crystal's involuntary submissive attraction remains authentic. It does not justify manipulation, isolation, secrecy, sexual pressure, or using her family as leverage. Being misled or pressured does not transfer responsibility to her. **Consent to a D/s scene is not consent to coercion outside it.** The script treats dark exploitation as a wrong act with repercussions, not as evidence she wanted harm.
3. A successful consensual D/s branch, if any, requires verifiable separate accountability, no active manipulation/obstruction, independent Crystal interest, clear revocable limits, and chronological consistency with her Crystal-POV route. Player Raven cannot directly choose Crystal's willingness.
4. Raven's liability and exact sentence remain **unadjudicated**. The fatal attack, Kreissack's prior authorization, Raven's relay suppression, ignored restoration request and postevent concealment are fixed sequel history; Raven did not personally install the fatal command.
5. The order of revelations, tournament bracket, Day 11/12 semifinal split, Nova's genuine rescue, final boss timing, Ganymede responsibility and Varga's separate unethical study are unchanged.
6. All Raven–Mara interactions are proposed. Mara's debt, mother, independent care choices and existing commitments cannot be overridden or bought; if she is in a relationship, no alternative is generated by a Raven flag.
7. Filmic tone: dark psychological noir, action, charged but non-explicit attraction, glamorous ensemble comedy, rare dry humor. Avoid presenting coerced sex or nonconsensual humiliation as an erotic reward; keep abusive manipulation legible as manipulation.
<!-- END EXACT SOURCE SCENE -->


---

### Jean-Paul


#### FS-JEANPAUL-JP-C1-3 — JP-C1.3 — The demonstration [OPTIONAL / FLIRTATION OR PROFESSIONAL]

**Source:** `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### JP-C1.3 — The demonstration [OPTIONAL / FLIRTATION OR PROFESSIONAL]
**[FANSERVICE: FS-JEANPAUL-JP-C1-3 | type=FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. HAR NEURAL-INTERFACE SHOWROOM — LATE NIGHT**
**[BG: BG-LAB-NEURAL-EXHIBIT@NIGHT]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

Varga's presentation is elegant: two mannequins, one with an ordinary reaction interface, the other with a neural overlay. She describes an experimental correlation between emotional arousal and motor timing. On the public screen, all participants have consented to their measurements. Behind the stage, a second window disappears when she notices Jean-Paul looking.

**VARGA:** “Don't tell me you're frightened of a reaction-time graph.”

**JEAN-PAUL:** “Only when the graph appears to be looking back.”

A camera catches their silhouettes across a mirrored wall. Varga steps near enough to adjust his crooked lapel; he looks at her hand, not her face. She gives him time to move away.

**CHOICE:** Flirt without surrendering his devices / ask for the ethical-review protocol / leave with the research sponsor's public name. The second window stays a suspicion, not a proof of a crime.
<!-- END EXACT SOURCE SCENE -->


#### FS-JEANPAUL-JP-C2-3 — JP-C2.3 — Velvet and steel [OPTIONAL / FAN SERVICE]

**Source:** `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`  
**Scope:** `FULL_SCENE` | **Category:** `DANCE_GLAMOUR` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### JP-C2.3 — Velvet and steel [OPTIONAL / FAN SERVICE]
**[FANSERVICE: FS-JEANPAUL-JP-C2-3 | type=DANCE_GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. FORMAL FUNDRAISER — EVENING**
**[BG: BG-SOC-GALA@EVENING]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

Shirro announces a charity exhibition in which the returning pilots model classic HAR-era formalwear. The mood is deliberately ridiculous. Crystal wears a sleek red suit and looks ready to interrogate its designer. Lyra turns the runway into a genuine athletic demonstration. Jean-Paul appears in an open-collar satin jacket that makes Raven mutter, “That coat costs more than my first weapon.”

Varga watches Jean-Paul from the edge of the light.

**VARGA:** “You know exactly what the room is thinking.”

**JEAN-PAUL:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] “No. I only know what the room thinks I know.”

**OPTIONAL:** Share a dance with Varga / make Selene laugh with a deliberately outrageous bow / spend the evening with Crystal and Raven trading insults / quietly leave. If Varga's dance is chosen, her hand rests at Jean-Paul's shoulder and neither uses the moment to demand data or allegiance. The scene ends with an almost-kiss interrupted by a security announcement. No kiss is imposed.
<!-- END EXACT SOURCE SCENE -->


#### FS-JEANPAUL-JP-C3-4 — JP-C3.4 — The room without mirrors [OPTIONAL / ROMANTIC TENSION]

**Source:** `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_TENSION` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### JP-C3.4 — The room without mirrors [OPTIONAL / ROMANTIC TENSION]
**[FANSERVICE: FS-JEANPAUL-JP-C3-4 | type=ROMANTIC_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. EMPTY DANCE STUDIO — NIGHT**
**[BG: BG-SOC-DANCE@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Varga has borrowed the room for a private event. Jean-Paul asks whether the audio sensors are off. She produces a signed facility notice showing the room is not used for study collection. Angel confirms the independently visible device status when asked; Jean-Paul keeps his own transmitter disabled.

**VARGA:** “You checked the exits.”

**JEAN-PAUL:** [PERF: tone=determined | expression=EXP-FOCUSED | delivery=steady and purposeful | intensity=2] “I intend to enjoy the entrance.”

She chooses an old recording of a waltz. They dance badly at first because both want to lead. Jean-Paul deliberately yields a step. Varga seems more startled by that than by any of his compliments.

**VARGA:** “Was that surrender?”

**JEAN-PAUL:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] “No. It was choreography.”

They nearly kiss. **OPTIONAL CHOICE:** kiss / stop and ask what the invitation means / dance in silence / leave. If a kiss occurs, it is mutual, noncontractual, and does not waive privacy rights or settle the investigation. Jean-Paul can later reject the relationship regardless.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-JEANPAUL-JP-C5-4 — JP-C5.4 — Selene, if invited [OPTIONAL / PROPOSED ALTERNATIVE ROMANCE]

**Source:** `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### JP-C5.4 — Selene, if invited [OPTIONAL / PROPOSED ALTERNATIVE ROMANCE]
**[FANSERVICE: FS-JEANPAUL-JP-C5-4 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. ORBITAL ROOFTOP RESTAURANT — EVENING**
**[BG: BG-SOC-RESTAURANT@EVENING]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Selene sits at a table from which one can see the maintenance wing and the stars. She has come because Jean-Paul asked without a trick. Her earlier complicated connection with Milano may or may not be over. The player cannot declare her available by wishing it so.

**SELENE:** [PERF: tone=proud | expression=EXP-PROUD | delivery=satisfied | intensity=1] “We could talk about money. We'd both be excellent at it.”

**JEAN-PAUL:** “I'd rather talk about what you do when nobody benefits.”

She considers the question carefully. If both are adults, genuinely unattached, interested, and no active professional coercion exists, they can agree to a date and an optional kiss. If any gate fails, the scene remains a friendly conversation or ends with her leaving on her own terms. A Selene route is **provisional**, not established canon.
<!-- END EXACT SOURCE SCENE -->


#### FS-JEANPAUL-JP-C5-5 — JP-C5.5 — Honesty is not rehabilitation [OPTIONAL / VARGA]

**Source:** `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### JP-C5.5 — Honesty is not rehabilitation [OPTIONAL / VARGA]
**[FANSERVICE: FS-JEANPAUL-JP-C5-5 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**
**INT. PRIVATE OBSERVATION SUITE — LATE NIGHT**
**[BG: BG-SOC-VIEW-PRIVATE@NIGHT]**
**[MUSIC: MUS-INVESTIGATION | behavior=palette; continue_same_theme_unless_edited]**

Varga meets Jean-Paul only if she has made a documented disclosure, ceased unauthorized collection, and accepted independent oversight. Nothing about the meeting cancels disciplinary consequences. They place their devices visibly on the table and agree that tonight will contain no research.

**VARGA:** “I know your face when you're lying.”

**JEAN-PAUL:** “Then I shall try something unfamiliar.”

**VARGA:** “What?”

**JEAN-PAUL:** [PERF: tone=affectionate | expression=EXP-TENDER | delivery=soft and warm | intensity=2] “I missed you.”

A long silence. She admits she missed him too. They may choose a kiss and a private night together—implied, not shown—or end the meeting without touching. If those accountability/availability/consent gates are not satisfied, this scene becomes a public conversation or does not occur. The ending can still be separation. This is neither a lab reward nor proof that Varga is forgiven.

---
<!-- END EXACT SOURCE SCENE -->


---

### Steffan


#### FS-STEFFAN-ST1-3 — ST1.3 — Control rehearsal [OPTIONAL; GLAMOUR / FANSERVICE]

**Source:** `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `GLAMOUR` | **Review note:** attraction-not-consent; coercive options are NOT fanservice rewards

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### ST1.3 — Control rehearsal [OPTIONAL; GLAMOUR / FANSERVICE]
**[FANSERVICE: FS-STEFFAN-ST1-3 | type=GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**

**INT. EQUIPMENT BAY — PHOTO SESSION**
**[BG: BG-TEC-HANGAR@BASE]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Steffan poses for a glamorous technical campaign: bare arms, scorched racing jacket, Pyros helmet on the floor. The camera crew has an elaborate lighting rig, but Steffan stops them to move the lamp thirty centimeters and eliminate reflection on the joint sensor. The resulting frame is spectacular.

Lyra arrives for an adjacent sportswear shoot. She notices what he did.

**LYRA:** [PERF: tone=resentful | expression=EXP-BITTER | delivery=clipped | intensity=1] “You always direct other people's cameras?”

**STEFFAN:** [PERF: tone=confident | expression=EXP-COMPOSED | delivery=firm | intensity=2] “Only when they're wrong.”

**LYRA:** “And if I don't want to be directed?”

Steffan has a practiced line ready. For once he tests whether it is wise to use it.

**CHOICE ST1-C2:** `respect_lyra` — “Then I ask what you want.” / `flirt_with_edge` — “Then I hope you're as stubborn as advertised.” / `make_her_a_prop` — he suggests a staged photo to unsettle Dante. Lyra refuses the third option and the publicity team records her objection. Attraction does **not** imply permission to manage her image.

---

# CHAPTER 2 — AN ENGINEER OF VICTORY

**Days 2–4.** Dramatic question: *What does Steffan do when winning is not the thing he wants most?*
<!-- END EXACT SOURCE SCENE -->


#### FS-STEFFAN-ST2-4 — ST2.4 — The afterparty [OPTIONAL; ENSEMBLE/FANSERVICE]

**Source:** `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** attraction-not-consent; coercive options are NOT fanservice rewards

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### ST2.4 — The afterparty [OPTIONAL; ENSEMBLE/FANSERVICE]
**[FANSERVICE: FS-STEFFAN-ST2-4 | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**
**[BG: BG-SOC-POOL@NIGHT | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

At a tasteful rooftop party, athletic pilots change out of competition armor; celebrities and technicians mingle. Steffan performs a choreographed demonstration with Ren, wins the crowd, then takes an unplanned, precariously close dance step with Dante. Both laugh before they realize who is watching.

**DANTE:** “Don't mistake my keeping pace for following.”

**STEFFAN:** [PERF: tone=sarcastic | expression=EXP-DRY | delivery=dry | intensity=2] “I wouldn't dare.”

He looks for Lyra's reaction. She is talking animatedly to Alex, oblivious. Steffan feels an irrational sting. The player may let the party end naturally, deliberately publicize a flirtation, or leave the cameras for a private conversation about competition. No privacy breach is a heroic shortcut.

---

# CHAPTER 3 — A BATTLE HE CAN'T NAME

**Days 5–7.** Dramatic question: *Can he distinguish wanting Lyra from wanting to defeat Dante?*
<!-- END EXACT SOURCE SCENE -->


#### FS-STEFFAN-ST3-2 — ST3.2 — The triangle, not the prize [MANDATORY PERSONAL CHOICE]

**Source:** `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `DARK_ROMANTIC_TENSION` | **Review note:** attraction-not-consent; coercive options are NOT fanservice rewards

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### ST3.2 — The triangle, not the prize [MANDATORY PERSONAL CHOICE]
**[FANSERVICE: FS-STEFFAN-ST3-2 | type=DARK_ROMANTIC_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=attraction-not-consent; coercive options are NOT fanservice rewards]**

**INT. OBSERVATION GARDEN — EVENING**
**[BG: BG-SOC-GARDEN@EVENING]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

If Steffan previously pursued her, Lyra meets him alone. She has made—or is considering—a decision about Dante; she is not asking permission.

**LYRA:** [PERF: tone=suspicious | expression=EXP-SKEPTICAL | delivery=guarded | intensity=2] “You have this habit of taking my hand just when he can see.”

**STEFFAN:** [PERF: tone=possessive | expression=EXP-INTENSE | delivery=insistent | intensity=2] “I like having your hand.”

**LYRA:** [PERF: tone=hurt | expression=EXP-HURT | delivery=unsteady | intensity=2] “I believe you. I also see when you look over my shoulder.”

He reaches toward her waist. She catches his wrist gently, firmly.

**LYRA:** “Ask.”

He freezes. It is almost easier to face a brutal tactical loss.

**STEFFAN:** [PERF: tone=vulnerable | expression=EXP-VULNERABLE | delivery=exposed | intensity=2] “May I?”

**LYRA:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=2] “Not when you're watching his face.”

The tension is real. So is her boundary. When the player selects `respect_and_wait`, he steps back, and Lyra can independently choose a kiss later if she has ended her existing commitment. When the player selects `press_for_control`, he tries to tell her what she *really* wants; she rejects the claim and may end the encounter. When selecting `keep_distance`, the route remains cordial or cool, without a required romance.

**[OPTIONAL PRIVATE TENSION — only after Lyra has freely ended her prior relationship and both reciprocate]** Away from cameras, Steffan says, “Come here.” Lyra crosses the room, drawn to his confident tone. He is thrilled—not only by her closeness, but by the fact that she moved when he asked. She puts a finger under his chin. **LYRA:** “I came because I wanted to. Don't confuse that with being yours to order.” **STEFFAN:** “Then tell me to stop.” **LYRA:** “I will.” She chooses whether they kiss or end the encounter with a laugh. The warmth is genuine. Steffan's private temptation to use that trust as proof of his power remains a problem, not a negotiated privilege.

**CHOICE ST3-C1:** `respect_and_wait` / `press_for_control` / `keep_distance`. **No romantic scene while Lyra remains committed to Dante without their established relationship decisions permitting it.** When she chooses Steffan in the default story, the attraction is real, but Steffan's initial manipulation remains true. Their relationship may include mutually chosen private teasing and a consensual preference for him taking the lead; his offstage attempts to isolate her, direct her public persona or use her as proof of victory are separate controlling behaviors, not consent.
<!-- END EXACT SOURCE SCENE -->


---

### Dante


#### FS-DANTE-DV1-2 — DV1.2 — Private laughter [OPTIONAL ROMANCE / WARM FANFARE]

**Source:** `22_Dante_Campaign/Dante_Playable_Screenplay_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `WARM_ROMANCE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### DV1.2 — Private laughter [OPTIONAL ROMANCE / WARM FANFARE]
**[FANSERVICE: FS-DANTE-DV1-2 | type=WARM_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. PILOT QUARTERS — GARDEN BALCONY — LATE NIGHT**
**[BG: BG-RES-GENERIC@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Lyra kicks off the shoes from the publicity event, revealing tape on a bruised ankle. Dante returns with two cups of water and a packet of ice. She tests his hand against her calf; he offers to stop, and she tells him where it actually hurts.

**LYRA:** “You looked like you wanted to punch him for looking at me.”

**DANTE:** [PERF: tone=resentful | expression=EXP-BITTER | delivery=clipped | intensity=2] “It wasn't the looking.”

**LYRA:** “He has been looking at you for years.”

Dante laughs despite himself. They are close enough to kiss, but neither needs to use the moment as proof of ownership. Lyra leans in if the active relationship state confirms mutual interest; otherwise she brushes his wrist and talks about tomorrow's training.

**DANTE:** [PERF: tone=affectionate | expression=EXP-TENDER | delivery=soft and warm | intensity=2] “I know you'll make your own choices.”

**LYRA:** “Knowing that is the easy part.”

**DANTE:** [PERF: tone=conflicted | expression=EXP-CONFLICTED | delivery=halting | intensity=2] “I didn't promise to be graceful.”

**CHOICE DV1-C2 — Dante's commitment:** `listen` (ask what she wants from the relationship), `deflect` (make a provocative joke), `cling` (ask for an exclusivity pledge she may freely refuse). The scene never locks Lyra into staying. If Dante and Lyra are already separated in an explicitly selected alternative world state, this is a memory, not a present-tense romance scene.
<!-- END EXACT SOURCE SCENE -->


#### FS-DANTE-DV2-2B — DV2.2b — The audience is not a relationship [OPTIONAL ENSEMBLE / FANFARE]

**Source:** `22_Dante_Campaign/Dante_Playable_Screenplay_v0.6.md`  
**Scope:** `FULL_SCENE` | **Category:** `ENSEMBLE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### DV2.2b — The audience is not a relationship [OPTIONAL ENSEMBLE / FANFARE]
**[FANSERVICE: FS-DANTE-DV2-2B | type=ENSEMBLE | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**

**INT. PROMOTIONAL ROOFTOP POOL — DAY**
**[BG: BG-SOC-POOL@DAY]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

Shirro organizes a publicity event full of athletic demonstrations, swimwear, staged dares and boastful sparring. Lyra dives cleanly from the high platform. Steffan critiques her entry angle, then offers to demonstrate. Dante calls him a coward unless he can do it without a camera.

**SHIRRO:** “I have been told the world's finest athletes are mature adults.”

**MARA:** “You were misinformed.”

Dante chooses whether to join the performance, leave with Mari to inspect a suspicious display cabinet, or step back when he notices Lyra's annoyance. A playful splash or consensual flirt can occur only where relationship state permits it. Mari's respect for him can deepen without becoming a romance; neither she nor Lyra is awarded as a prize for athletic showmanship.

---
<!-- END EXACT SOURCE SCENE -->


#### FS-DANTE-DV6-4 — DV6.4 — Optional Steffan reckoning [AFTER FINALE; ADULTS; ROMANCE NOT DEFAULT]

**Source:** `22_Dante_Campaign/Dante_Playable_Screenplay_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_DEVELOPMENT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### DV6.4 — Optional Steffan reckoning [AFTER FINALE; ADULTS; ROMANCE NOT DEFAULT]
**[FANSERVICE: FS-DANTE-DV6-4 | type=ROMANTIC_DEVELOPMENT | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**

**INT. EMPTY SPARRING ROOM — NIGHT**
**[BG: BG-ARE-TRAIN@NIGHT]**
**[MUSIC: MUS-FINALE | behavior=palette; continue_same_theme_unless_edited]**

Steffan waits without cameras or uniforms. The confrontation has changed what can be denied, not what can be forgiven.

**STEFFAN:** “When you said those things, you wanted to hurt me.”

**DANTE:** “Sometimes. Yes.”

**STEFFAN:** [PERF: tone=vulnerable | expression=EXP-VULNERABLE | delivery=exposed | intensity=2] “You were right about more than I wanted you to be.”

Dante recognizes the precision of that answer. It is the first time Steffan has refused to hide behind virtuosity.

On the **default nonromantic branch**, Dante accepts only a professional truce or chooses distance. Their intense rivalry has never amounted to romantic desire **for Dante**. Steffan may find this disappointing but cannot argue him out of it.

On the **estrangement branch**, Dante wants no further private relationship. On the **optional player-led path** (early `curiosity` and Day-11 `listen`), Dante can discover an unexpected change in his feelings after the crisis. He does not confess that he *always* loved Steffan. He weighs the new attraction against Steffan's treatment of Lyra and what he would need from an equal partner.

**CHOICE DV6-C4 — later direction:** `none` **(default)** / `explore` **(optional)**. Choosing `explore` means that Dante actively wants to investigate a new romantic possibility; it does not assign Steffan a relationship or settle what Lyra deserves. Any eventual romance requires a real post-tournament interval, mutual availability, documented accountability and repaired coercive behavior, and Steffan's independent consent.

**DANTE:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] “I won't spend my life being your mirror.”

**STEFFAN:** “Then what would you be?”

**DANTE:** “Ask me when you've learned to look at another person.”
<!-- END EXACT SOURCE SCENE -->


#### FS-DANTE-DV6-5 — DV6.5 — Alternate personal endings [AFTER FINALE]

**Source:** `22_Dante_Campaign/Dante_Playable_Screenplay_v0.6.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### DV6.5 — Alternate personal endings [AFTER FINALE]
**[FANSERVICE: FS-DANTE-DV6-5 | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**[BG: BG-ARE-TRAIN@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-FINALE | behavior=palette; continue_same_theme_unless_edited]**

- **`solo_rebuild` (default):** Dante returns to Shredder training, competing to be excellent rather than to make someone regret leaving. He remains passionate, capable of anger, and finally a little less governed by it.
- **`lyra_future_proposal`:** Following time, independent mutual decisions and a repaired relationship, Dante and Lyra can consider reconnecting. Her return is never his reward for unmasking Steffan; if she declines, he respects it.
- **`steffan_future_proposal` [PLAYER-ALTERED PATH ONLY]:** An optional quiet meeting months later: Dante returns to the training bay after Steffan has published a verifiable correction and respected Lyra's boundaries. **DANTE:** “I didn't come here wanting you. I came here wanting a fight. That changed, and I chose to find out why.” **STEFFAN:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] “I won't use that against you.” **DANTE:** “Then start by telling me when you're afraid.” Dante offers his hand; Steffan may take it. They may share a first kiss only after independently choosing to do so. It is a beginning, not proof of redemption. Missing any gate yields `relationship_not_available` or a nonromantic truce instead.
- **`mari_future_proposal`:** A modest adult romance with Mari is possible only if she is free, chooses it herself, and Dante's Shredder contracts do not give either party professional leverage over the other. Otherwise they remain colleagues and friends.
- **`vindictive_isolation`:** If he prefers humiliating Steffan and refuses repair, Dante may win matches and lose trust. He is not made a villain or secretly rewarded with another person's affection.
- **`professional_truce`:** Dante and Steffan keep the rivalry alive as athletes, stripped of the claim that one can possess the other's private world.

All paths leave Lyra's independent career and sporting achievements intact.
<!-- END EXACT SOURCE SCENE -->


---

### Selene


#### FS-SELENE-SV1-4 — SV1.4 — A dance with a balance sheet [OPTIONAL, ADULT FANFARE]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `FULL_SCENE` | **Category:** `DANCE_FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV1.4 — A dance with a balance sheet [OPTIONAL, ADULT FANFARE]
**[FANSERVICE: FS-SELENE-SV1-4 | type=DANCE_FLIRT | scope=FULL_SCENE | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. OBSERVATION LOUNGE — AFTER MIDNIGHT**
**[BG: BG-SOC-VIEW-PRIVATE@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

The music slows. Milano extends a hand.

**MILANO:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] “One dance. No nondisclosure agreement.”

**SELENE:** [PERF: tone=teasing | expression=EXP-SMIRK | delivery=playful | intensity=2] “You are a very poor negotiator.”

**MILANO:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] “I can afford one exception.”

The player may accept the dance, keep the encounter purely professional, or invite Jean-Paul to an improvised verbal duel about the art of forgery. In the dance branch Milano and Selene move with practiced ease, close enough to imply attraction, far enough apart to preserve uncertainty. A teasing remark about who leads is met with a confident physical turn from Selene; neither owes the other an intimate sequel.

**CHOICE SV1-C4 — after the dance:** `flirt`, `business_only`, `leave`. Optional chemistry changes dialogue, never hidden contractual obligations.

---

# CHAPTER 2 — THE COST OF A GOOD LIE

*Days 2–4. Theme: a result on the scoreboard is one fact no amount of charm can negotiate.*
<!-- END EXACT SOURCE SCENE -->


#### FS-SELENE-SV2-3 — SV2.3 — Jean-Paul and the locked cabinet [OPTIONAL SECONDARY / FLIRT]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `FLIRT` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV2.3 — Jean-Paul and the locked cabinet [OPTIONAL SECONDARY / FLIRT]
**[FANSERVICE: FS-SELENE-SV2-3 | type=FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. ARCHIVE-LINK CAFÉ — NIGHT**
**[BG: BG-SOC-CAFE@NIGHT]**
**[MUSIC: MUS-BANTER | behavior=palette; continue_same_theme_unless_edited]**

Jean-Paul recognizes that Selene has used exactly three decoy documents to see whether a WAR analyst would open a fourth. He places his cup beside the fourth—still sealed.

**JEAN-PAUL:** [PERF: tone=flirtatious | expression=EXP-FLIRT | delivery=soft, inviting | intensity=2] “It isn't a trap if you tell me where the wire is.”

**SELENE:** “And you aren't an investigator if you step over it.”

**JEAN-PAUL:** “I wasn't investigating the cabinet.”

**SELENE:** [PERF: tone=sarcastic | expression=EXP-DRY | delivery=dry | intensity=2] “How disappointing.”

An option to flirt can lead to a deliberately staged moment by the window, their reflections overlapping while neither admits which one is watching the other. An option to exchange professional methods produces a useful secure-communications practice. An option to mislead him costs trust. Jean-Paul's existing Varga entanglement is not magically cleared here: interest is not availability.

**CHOICE SV2-C2:** `flirt`, `trade_methods`, `misdirect`. A romance cannot become active until all existing commitments are resolved and both independently choose it.
<!-- END EXACT SOURCE SCENE -->


#### FS-SELENE-SV2-4 — SV2.4 — Mirage without the costume [OPTIONAL FANFARE / CHARACTER]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `FULL_SCENE` | **Category:** `ATHLETIC_GLAMOUR` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV2.4 — Mirage without the costume [OPTIONAL FANFARE / CHARACTER]
**[FANSERVICE: FS-SELENE-SV2-4 | type=ATHLETIC_GLAMOUR | scope=FULL_SCENE | status=REVIEW | note=optional spectacle; no relationship assumption]**

**INT. TRAINING DECK — SUNSET CYCLE**
**[BG: BG-ARE-TRAIN@SUNSET]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**

Selene practices barefoot in athletic training clothes, hair pulled up without the careful gala styling. Mirage's rehearsal drones paint harmless decoy shadows around her. She turns off the projection and tries the same movements without it, faster on the third attempt. Crystal watches from the doorway.

**CRYSTAL:** “You move better when there's nothing to hide behind.”

**SELENE:** [PERF: tone=teasing | expression=EXP-SMIRK | delivery=playful | intensity=2] “Don't tell my sponsors.”

**CRYSTAL:** “I thought you didn't have sponsors.”

A beat. They share a laugh that might grow into respect. Crystal notices Selene's defensive instinct and does not pry. The scene provides optional glamorous athletic presentation without romanticizing the tournament as a contest for anyone's body.

---

# CHAPTER 3 — THE HEIRESS UNDER THE MASK

*Days 5–7. Theme: privacy and deception are related, but not identical.*
<!-- END EXACT SOURCE SCENE -->


#### FS-SELENE-SV3-4 — SV3.4 — The rooftop almost-kiss [OPTIONAL, ADULT SUGGESTIVE]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV3.4 — The rooftop almost-kiss [OPTIONAL, ADULT SUGGESTIVE]
**[FANSERVICE: FS-SELENE-SV3-4 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**EXT. COMPETITOR ROOFTOP — NIGHT**
**[BG: BG-SOC-POOL@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Shirro's promotional pool gathering has become noisy enough to mask a serious conversation. Selene arrives in a dark swimsuit under a loosely tied cover-up, having escaped two corporate calls. Milano is alone near the railing, looking at Jupiter as though calculating its price.

**MILANO:** “I know your name. I still don't know what you want.”

**SELENE:** “Good. That means I've improved at something.”

Their teasing becomes quieter. He asks permission before drawing closer. If both express interest, she can let him kiss her, stop him inches away, or redirect the moment into a proposal for a clean, nonexclusive business partnership. A kiss is a flirtation beat, **not** agreement to give access to technology, to abandon a family relationship, or to start an exclusive romance. If Milano is committed elsewhere, the scene uses the professional version.

**CHOICE SV3-C2:** `kiss_if_mutual`, `stop_and_talk`, or `leave`. No clue or financial benefit depends on a kiss.
<!-- END EXACT SOURCE SCENE -->


#### FS-SELENE-SV5-4 — SV5.4 — An invitation not written as an invoice [OPTIONAL MILANO ROMANCE]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV5.4 — An invitation not written as an invoice [OPTIONAL MILANO ROMANCE]
**[FANSERVICE: FS-SELENE-SV5-4 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. GLASS GARDEN — NIGHT**
**[BG: BG-SOC-GARDEN@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Milano approaches without advisers. In other circumstances he would arrive with terms, counteroffers and a precise reason to be there. Tonight he is holding two ordinary drinks.

**MILANO:** “I thought about making you an offer.”

**SELENE:** [PERF: tone=resentful | expression=EXP-BITTER | delivery=clipped | intensity=1] “You always do.”

**MILANO:** “That's why I didn't.”

If there is mutual adult attraction and no conflicting commitments, Selene may draw him close by the lapel; if they kiss, the camera lingers on the cooling glasses and shifts away. Alternatively they can admit that attraction is not enough to make them compatible, or explicitly decide to keep the relationship professional. A romantic evening does not settle their future company ownership, give him access to protected data, or guarantee he will choose the same future.

**CHOICE SV5-C2:** `private_contact`, `professional_boundary`, or `postpone`. Romantic eligibility must be determined by *both* characters, not by a unilateral player flag.
<!-- END EXACT SOURCE SCENE -->


#### FS-SELENE-SV5-5 — SV5.5 — The honest deception [OPTIONAL JEAN-PAUL ROMANCE]

**Source:** `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_KISS` | **Review note:** only consensual/optional depiction where branch requires it

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## SV5.5 — The honest deception [OPTIONAL JEAN-PAUL ROMANCE]
**[FANSERVICE: FS-SELENE-SV5-5 | type=ROMANTIC_KISS | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. COMMUNICATIONS GALLERY — LATE NIGHT**
**[BG: BG-SOC-BROADCAST@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Jean-Paul has severed any romantic involvement with Varga *only if his independent route state confirms it*. He delivers an unglamorous update: the documentation of her study is secure and the affected people will have independent access. Selene can admire the competence without treating the victims as a flirtation pretext.

**JEAN-PAUL:** “I expected you to be impressed by the disguise.”

**SELENE:** “I am impressed that you finally decided to take it off.”

She reveals a private failure from her early career—not a melodramatic confession, but an occasion when her family paid to conceal her mistake and thereby made her achievements feel purchased. Jean-Paul does not offer to fix it. He listens.

If both choose it, a quiet kiss follows. Otherwise she invites him to collaborate on a legitimate public-interest investigation or leaves, professionally cordial. No romance occurs while he remains with Varga, while either is unavailable, or because he supplied evidence.

**CHOICE SV5-C3:** `invite_personally`, `collaborate`, `goodbye`.

---

# CHAPTER 6 — THE ONE THING SHE CAN'T BUY

*Days 13 and 30. Theme: the right to act freely matters more than getting to call yourself the winner.*
<!-- END EXACT SOURCE SCENE -->


---

### Milano


#### FS-MILANO-MA1-2 — MA1.2 — The woman who sees through the smile [OPTIONAL SELENE / PROFESSIONAL]

**Source:** `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## MA1.2 — The woman who sees through the smile [OPTIONAL SELENE / PROFESSIONAL]
**[FANSERVICE: FS-MILANO-MA1-2 | type=FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. OBSERVATION GALLERY — LATER**
**[BG: BG-SOC-VIEW@BASE]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

Selene Vale stands by the glass, watching a holographic mock-combat display. She wears a sharp silver evening gown. Milano comes to stand beside her, not quite invading her space.

**MILANO:** “You've been looking at our procurement presentations all evening.”

**SELENE:** “And you've been counting who watches them.”

**MILANO:** “An occupational hazard.”

**SELENE:** “Yours or theirs?”

His answer is a small laugh; hers is a half-smile. The choice of flirtation does not establish that Selene is romantically available. If the player chooses `professional`, they discuss opaque suppliers. If `flirt`, they trade barbs and dance at arm's length. If `recruit`, Selene refuses an offer without defined independence.

**SELENE:** “Don't mistake curiosity for a vote. Or a date.”

**MILANO:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=1] “I won't. Though I suspect you make both rather difficult to earn.”

**SELENE:** “Only for people accustomed to buying them.”

The camera lingers on their reflections, both immaculate; through the glass the working service docks are barely visible.
<!-- END EXACT SOURCE SCENE -->


#### FS-MILANO-MA2-4 — MA2.4 — Unscheduled attention [OPTIONAL ADULT FLIRT]

**Source:** `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `DANCE_FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## MA2.4 — Unscheduled attention [OPTIONAL ADULT FLIRT]
**[FANSERVICE: FS-MILANO-MA2-4 | type=DANCE_FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. GLASS-WALLED LOUNGE — NIGHT**
**[BG: BG-SOC-VIEW-PRIVATE@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Selene joins Milano at a table with a view of the rotating arena. A pair of younger pilots laughing nearby reminds him how rarely he has done anything without an agenda. He and Selene trade carefully pointed questions about their careers.

**SELENE:** “What would you do if you weren't someone's heir?”

**MILANO:** “Probably find a smaller company to disappoint.”

**SELENE:** “That's almost an honest answer.”

They share a dance or end the conversation as professional rivals, according to the player's choice. If Selene signals distance, there is no kiss. If both opt into flirtation, they almost kiss before a call interrupts. The camera cuts to the ballroom, not to an assumed relationship.

---

# CHAPTER 3 — THE COST OF THE SECOND SIGNATURE

*Days 5–7. Dramatic question: When the rules protect you, is obeying the rules enough?*
<!-- END EXACT SOURCE SCENE -->


#### FS-MILANO-MA3-4 — MA3.4 — The mask slips in the service lift [OPTIONAL SELENE OR FRIENDSHIP]

**Source:** `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `QUIET_FLIRT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## MA3.4 — The mask slips in the service lift [OPTIONAL SELENE OR FRIENDSHIP]
**[FANSERVICE: FS-MILANO-MA3-4 | type=QUIET_FLIRT | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. SERVICE LIFT — LATE NIGHT**
**[BG: BG-TEC-SERVICE@NIGHT]**
**[MUSIC: MUS-INVESTIGATION | behavior=palette; continue_same_theme_unless_edited]**

Milano and Selene share a ride between secured floors. It is the first space all week where neither has an audience.

**MILANO:** “You appear wherever I find a weak control.”

**SELENE:** “Then you should be more concerned about your controls.”

He admits he supported the original limited research. She admits she is looking into vendor anomalies, without disclosing her family identity or proof she has not obtained.

**SELENE:** “I don't date companies.”

**MILANO:** “I'm trying to become more interesting than one.”

If the relationship is professional, she responds with a genuinely useful public registry number; if flirtatious, she brushes his cuff while leaving and suggests a dinner *after* the relevant negotiations end. Neither option gives Milano access to her hidden data.

---

# CHAPTER 4 — A COMPANY IS NOT A PERSON

*Days 8–10. Dramatic question: Can Milano investigate himself and still be credible?*
<!-- END EXACT SOURCE SCENE -->


#### FS-MILANO-MA4-4 — MA4.4 — A conversation without a price [OPTIONAL SELENE ROMANCE / NEGOTIATION]

**Source:** `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_TENSION` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## MA4.4 — A conversation without a price [OPTIONAL SELENE ROMANCE / NEGOTIATION]
**[FANSERVICE: FS-MILANO-MA4-4 | type=ROMANTIC_TENSION | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. EMPTY ATRIUM — NIGHT**
**[BG: BG-ARE-WALK@NIGHT]**
**[MUSIC: MUS-ROMANCE | behavior=palette; continue_same_theme_unless_edited]**

Selene arrives with material she chooses to share: an openly verifiable supplier anomaly. She has her own investigation and may refuse to show him anything. Milano brings the board waiver trail—not a demand for loyalty.

**SELENE:** “You can call this a merger of interests.”

**MILANO:** “I would rather call it two people comparing notes.”

**SELENE:** “If I find that you've used what I told you as leverage against me, this ends.”

**MILANO:** “Then I will put the provenance in writing.”

A short pause. Their tension is genuine, but at this point any embrace is restrained and optional. The only kiss on this route is deferred until personal and corporate dependencies have been untangled and both characters actively want it. The scene remains complete with a professional handshake.

---

# CHAPTER 5 — THE EMERGENCY CLAUSE

*Days 11–12. Dramatic question: Is a reformer willing to surrender power when holding on would be easier?*
<!-- END EXACT SOURCE SCENE -->


#### FS-MILANO-MA5-4 — MA5.4 — The first honest terms [OPTIONAL POST-CONFLICT SELENE; ADULT]

**Source:** `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_DEVELOPMENT` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
## MA5.4 — The first honest terms [OPTIONAL POST-CONFLICT SELENE; ADULT]
**[FANSERVICE: FS-MILANO-MA5-4 | type=ROMANTIC_DEVELOPMENT | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**

**INT. OBSERVATION DECK — NIGHT**
**[BG: BG-SOC-VIEW@NIGHT]**
**[MUSIC: MUS-ARENA | behavior=palette; continue_same_theme_unless_edited]**

The glamour has drained out of the celebration. Milano has loosened his collar; Selene has exchanged her formal gown for a simple dark jacket. They watch crews sweep the empty arena.

**SELENE:** “You finally did something that may cost you your seat.”

**MILANO:** “I'm not sure that means it was noble.”

**SELENE:** “No. But it's a more interesting answer than your speeches.”

Milano has an optional choice: `invite_independent` (“Dinner, when this is over. No transaction.”), `respect_distance`, or `propose_alliance`. Romance remains unresolved here: an invitation is not Selene's consent, and her independent route may refuse it. If he has manipulated her corporation, traded access for intimacy, or concealed a relationship with someone else, the invitation does not become a romantic scene.

---

# CHAPTER 6 — THE POWER TO LET GO

*Days 13 and 30. Dramatic question: Can a man whose identity is built around command finally accept limits?*
<!-- END EXACT SOURCE SCENE -->


---

### Christian


#### FS-CHRISTIAN-CH4-3 — CH4.3 — An evening not about the case (optional)

**Source:** `18_Christian_Subplot/OMF_2107_Christian_Independent_Storyline_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `DANCE_ROMANCE` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### CH4.3 — An evening not about the case (optional)
**[FANSERVICE: FS-CHRISTIAN-CH4-3 | type=DANCE_ROMANCE | scope=OPTIONAL_BEAT | status=REVIEW | note=only consensual/optional depiction where branch requires it]**

**INT. NIGHT MARKET MUSIC VENUE — NIGHT**
**[BG: BG-SOC-DANCE@NIGHT]**
**[MUSIC: MUS-UNEASE | behavior=palette; continue_same_theme_unless_edited]**

Christian arrives to hear a low-key live set. He used to fix old percussion instruments as a teenager, but hasn't touched one in years. A friend has left a drum machine on a small table; he asks permission and helps reprogram a damaged rhythm loop. The venue owner offers a laugh, not a job.

Leena arrives only if independently uncommitted and inclined to maintain contact. The scene can also play with a platonic friend or alone. She has slipped out of a newsroom argument about headlines.

**LEENA:** You found a thing no one can cross-examine.

**CHRISTIAN:** Give it ten minutes.

She asks him to dance. Their movements are awkward enough to be human, close enough to make the room briefly disappear. If there is flirtation, it ends when she asks whether he would rather be kissed or left alone.

**CHRISTIAN:** I'd rather not make my parents the reason you said yes.

**LEENA:** Good. Because they aren't.

They may share a **mutually chosen brief kiss** only if Leena has already formally recused herself from covering the Devroe case, both are unattached, and both reciprocate; otherwise they may dance platonically or simply part as friends. The safer default is to leave romantic escalation for the later epilogue. Neither option advances the case, changes Leena's editorial duty, or establishes a romance by itself.

---

## CHAPTER FIVE — THE REQUEST (Days 9–12)
<!-- END EXACT SOURCE SCENE -->


#### FS-CHRISTIAN-CH6-3 — CH6.3 — Personal epilogues (mutually exclusive outcomes; weeks later)

**Source:** `18_Christian_Subplot/OMF_2107_Christian_Independent_Storyline_v0.5.md`  
**Scope:** `OPTIONAL_BEAT` | **Category:** `ROMANTIC_ENDING` | **Review note:** only eligible reciprocal romance branch; never the solo/friendship branch

<!-- BEGIN EXACT SOURCE SCENE (with added tag) -->
### CH6.3 — Personal epilogues (mutually exclusive outcomes; weeks later)
**[FANSERVICE: FS-CHRISTIAN-CH6-3 | type=ROMANTIC_ENDING | scope=OPTIONAL_BEAT | status=REVIEW | note=only eligible reciprocal romance branch; never the solo/friendship branch]**
**[BG: BG-EPI-CIVIL@AFTERMATH | STAGING PROVISIONAL — no source slugline]**
**[MUSIC: MUS-AFTERMATH | behavior=palette; continue_same_theme_unless_edited]**

**A — Open archive.** Christian helps create a victim-access records service with an independent civilian board. It preserves comparable cases beyond the Devroes' tragedy. He is not magically healed; he learns to ask different questions. Crystal may visit as a sibling rather than an exhibit.

**B — Responsible fieldwork.** Christian returns to independent investigations with a strict outside-custodian practice and a renewed interest in teaching younger investigators what *not* to assume. His first case after the shuttle is unremarkable and reassuring.

**C — The case is not his entire life.** Christian puts his investigative work aside for a period, calls the venue, and accepts a chance to play music badly in public. The hearing does not need him in the room every day for its findings to stand.

**D — Relationship with Leena (optional overlay on A/B/C, not a reward for testimony).** Only after both independently choose one another, both are adult and unattached, and Leena has fully stepped back from editorial or source handling concerning the Devroe case, Christian meets her at the music venue again. She has kept no secret copy; Christian has not asked her to manage the coverage. She asks whether they can have one evening with no work.

**CHRISTIAN:** We tried that once. It lasted eleven minutes.

**LEENA:** Twelve. You spent the first minute pretending you didn't see me.

He takes her hand if they both want it. A kiss can follow with explicit reciprocation, then the scene fades. If Leena has chosen Ari, Angel, or solitude, Christian does not wait for her or act cheated. Their journalism and friendship scenes remain; an independent solo or other-life ending is equally complete.

**E — Brother and sister, not one person.** Across A–D, if he respected Crystal's autonomy, they eat together and argue gently about the quality of the venue's sound system. If he tried to control her, they may be in limited contact; he writes an apology that names what he did instead of demanding closeness. Crystal accepts, refuses, or defers on her own terms. Her romantic outcome remains hers.
<!-- END EXACT SOURCE SCENE -->


---

## Part II — Historical / proposal-only scene cards (NOT automatically playable)

These 12 earlier concepts are preserved for comparison. Some have been integrated and revised elsewhere; do not treat them as extra simultaneous scenes or as approved relationship canon.


#### FS-BANK-S1 — ## S1. “Five More Seconds” — Ari / Mara [E, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S1. “Five More Seconds” — Ari / Mara [E, F]
**[FANSERVICE: FS-BANK-S1 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 3, after an optional safe sparring session; before the knockout bracket announcement. **Prereqs:** Ari or Mara player; mutual rapport; no incompatible commitment. **Versions:** attraction / friendship / alone. **Visual:** Steam rising from a training hall, harsh white lights, sweat-damp practice gear, the robots cooling down beyond the glass. This is physical *training* fanservice, not a surprise sexualized exposure.

The sparring clock goes dark. Mara has won the last exchange by a fraction of a second. She leans against the railing, catching her breath. Ari's gloves hit the bench.

**MARA:** You keep looking at my left shoulder.

**ARI:** It telegraphs your hook.

**MARA:** Funny. You never dodge it.

She tosses Ari a clean towel. Ari catches it without looking away.

**ARI:** Maybe I like seeing you pleased with yourself.

**MARA:** Dangerous hobby.

She steps close, takes Ari's wrist, and corrects the angle of a guard. Her fingers pause a moment longer than the demonstration requires. Ari does not close the distance for her.

**[PLAYER CHOICE]**

- **A — Return the flirt:** “Five more seconds of this lesson?” → On reciprocated interest, Mara grins: “You finally learn quickly.” They kiss, briefly and fiercely. She pulls back first to say: “Don't go soft when we fight for real.” Fade to them laughing, not to an invented tournament result. `ari_mara_heat=1`, no combat effect.
- **B — Keep the playful tension:** “Show me the move again. Without cheating.” → Mara laughs, re-demonstrates, and almost trips Ari. Mutual tension remains unresolved; no forced kiss. `ari_mara_banter=1`.
- **C — Keep it platonic:** “I trust you with my blind spots. That's enough.” → “Good,” Mara says, offering the towel properly this time. “Because your right side is terrible.” Warm friendship; no later kiss line. `ari_mara_friends=1`.

**End sting:** A public terminal starts printing the knockout draw. Both turn to read it; no romance status changes the official bracket.

---


#### FS-BANK-S2 — ## S2. “Own the Spotlight” — Lyra / Steffan, with Dante alternative [E, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S2. “Own the Spotlight” — Lyra / Steffan, with Dante alternative [E, F]
**[FANSERVICE: FS-BANK-S2 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 3 commercial shoot, only *after* the route has established Lyra's actual relationship status. **Visual:** Violet neon, metallic runway, two pilots in designer reinterpretations of their HAR armor; brief dazzling stage poses, confident body language, and cheering fans. The camera deliberately gives Lyra and Steffan equally glamorous coverage. Both approve the styling; neither is trapped into a reveal.

**PHOTOGRAPHER:** More chemistry. The sponsor needs a scandal it can fit on a billboard.

**LYRA:** Tell the sponsor a billboard costs extra.

Lyra walks past Steffan and steals the center mark. The audience screams. Steffan poses beside her, an inch away without touching.

**STEFFAN:** You know this is going to start rumors.

**LYRA:** I start rumors. You just have good hair.

**STEFFAN:** An expensive distinction.

Lyra glances at the live preview and deliberately changes the angle so the frame reads *two competitors*, not his arm around a trophy.

**[PLAYER CHOICE FOR LYRA]**

- **A — Turn up the chemistry:** “Try keeping up.” Lyra hooks one finger beneath the lapel of Steffan's jacket, pulling him into the light. He stops, searching her expression; she closes the remaining distance for a staged near-kiss and turns at the last instant toward the audience. The crowd erupts. Later, in private, Steffan may ask whether it was *only* performance. If they are mutually available and interested, Lyra can answer honestly; otherwise she reminds him it was a job. `lyra_public_flirt=1`, no relationship commitment.
- **B — Own the solo shot:** Lyra takes center stage alone with an athletic Electra-inspired flourish; the fanbase cheers louder. Steffan visibly admires her performance without claiming her. `lyra_brand_autonomy=1`.
- **C — Refuse the fabricated coupling:** “We can advertise the tournament without advertising my bed.” Lyra demands a revised brief. The sponsor complies or loses the star; a solo or team shot replaces the couple pose. `lyra_brand_autonomy=1`.

**Alternative if Lyra remains with Dante:** Steffan cannot play boyfriend. Dante joins only if she wants him there; their chemistry has teasing history rather than scandal. **DANTE:** “You're going to steal the whole spotlight.” **LYRA:** “You noticed. Excellent.” If Lyra is single, she takes the center alone. **Default path note:** Lyra's eventual discovery of Steffan's motives is not erased by this alluring scene. Fans can enjoy their attraction while the story interrogates it.

---


#### FS-BANK-S3 — ## S3. “The Velvet Problem” — Jean-Paul / Varga [E, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S3. “The Velvet Problem” — Jean-Paul / Varga [E, F]
**[FANSERVICE: FS-BANK-S3 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 3, formal research-benefit gala, *before* public exposure of Varga's experiments. **Visual:** Sharp black suit, bare shoulders beneath an elegant evening jacket, low gold light, a slow instrumental dance. Seduction occurs in dialogue, not anatomical description.

**JEAN-PAUL:** You're the only person here who looks bored by the money.

**VARGA:** And you're the only one who's pretending not to enjoy being watched.

She adjusts his crooked tie. He catches her hand gently and holds it at a polite distance.

**JEAN-PAUL:** Is this a diagnosis or an invitation?

**VARGA:** That depends. Would you prefer the truth?

**JEAN-PAUL:** I would prefer a dance.

**[PLAYER CHOICE FOR JEAN-PAUL]**

- **A — Dance:** He offers his hand. Varga accepts. Their exchange is elegant, suggestive and almost combative; she knows the steps before he leads. They pause at the edge of a kiss, but she says, “You're mistaking curiosity for a confession.” He answers: “Then ask a better question.” The tension remains; no automatic intimacy or forgiveness. `varga_attraction_tension=1`.
- **B — Challenge:** “How much did you know about tonight before I arrived?” She evades; he notices, storing an independent clue. No lost investigation access. `jean_paul_varga_suspicion=1`.
- **C — Withdraw:** Jean-Paul leaves with a bow and pursues his own leads. Varga remains dangerous and professionally accountable. `jean_paul_varga_distance=1`.

**Ethical sting:** After Jean-Paul leaves, Varga marks a private experiment note `encounter predicted` and hesitates before deleting a correction. The attraction can be real; the unauthorized orchestration remains an abuse. **Never use this gala as a romance-triggered amnesty:** when the study is revealed, Jean-Paul can end intimacy, seek accountability, and still admit that he felt something.

---


#### FS-BANK-S4 — ## S4. “Cooling System” — Mara / Plug [P, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S4. “Cooling System” — Mara / Plug [P, F]
**[FANSERVICE: FS-BANK-S4 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 4 in a *Mara player* alternative route, after the independent parts-and-labor arrangement of Scene B in `Optional_Relationship_Scene_Cards_v0.1.md`. **Eligibility:** Plug's adult age and mutual compatibility need explicit authoring; no intimacy until then. **Visual:** Sultry workshop light, sparks behind a safety screen, Mara in sleeveless workwear, Plug working with sleeves rolled up. Both are experienced adult technicians. Protective gear is worn whenever machinery is active.

The weld seals. Plug kills the current and flips up the protective visor.

**PLUG:** Congratulations. The most expensive part of your machine now has a cheap scar.

**MARA:** It suits the pilot.

**PLUG:** The pilot is a walking invoice.

Mara leans over the bench to inspect the seam. Plug wordlessly moves a hot tool away from her elbow, then lets her do the inspection herself.

**MARA:** Are you always this careful with the things you like?

**PLUG:** Only the ones that can knock me flat.

**[CHOICE]**

- **A — Make a genuine invitation:** “Then take me to dinner. Off the clock, after you send the bill.” If `romance_ready(Mara,Plug)` is authored and reciprocated, Plug responds, “You pick the place. I'm choosing the dessert.” A quick consensual kiss is possible **after** tools are safely put away. `mara_plug_date=1`.
- **B — Joke and continue work:** “Good. The Flail needs a new actuator.” Their banter continues without romance. `mara_plug_friendship=1`.
- **C — Keep the boundary:** “You're good at your job. Let's not make it complicated.” Plug accepts it without sulking; the invoice and repairs remain identical. `mara_plug_professional=1`.

**Scope:** Mara's mechanical ability is showcased; she is not helpless so a technician can seduce her. The scene cannot run when Mara is already committed to Ari without a separately negotiated, openly agreed arrangement.

---


#### FS-BANK-S5 — ## S5. “No Interview Tonight” — Lyra / Alex [P, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S5. “No Interview Tonight” — Lyra / Alex [P, F]
**[FANSERVICE: FS-BANK-S5 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Late Chapter 4 or Chapter 5, only *after* Alex's formal recusal from Lyra's coverage, their independently expressed reciprocal attraction, and confirmed adult eligibility. **Visual:** Quiet rooftop after a blinding media event; Lyra still wears a shimmering jacket over practical competition clothes; Alex has loosened their elegant collar. A faraway holographic ad loops Lyra's public smile.

**LYRA:** I look wonderful on a building three kilometers away.

**ALEX:** That one's clearly exhausted.

**LYRA:** The building?

**ALEX:** The woman smiling on it.

She looks away from her advertisement and toward Alex.

**LYRA:** You know, I could still give you the most exclusive interview of your career.

**ALEX:** I gave up covering you. Don't make it sound romantic.

**LYRA:** Why did you, then?

**ALEX:** Because if I asked to see you without a microphone, I wanted the answer to belong to you.

A beat. Lyra takes Alex's hand and searches their face. Alex waits.

**[PLAYER CHOICE FOR LYRA]**

- **A — Kiss Alex:** “Then here's my answer.” A slow, mutual kiss, broken when a distant rooftop drone flashes a harmless navigation light. Lyra laughs: “For once, not a camera.” They move inside together; the door closes, *fade out*. No explicit scene. `lyra_alex_intimate=1`.
- **B — Keep the electricity:** “Walk me home. We'll see what the night does with us.” They leave side by side; no assumed intimacy. `lyra_alex_flirt=1`.
- **C — Choose friendship:** “I'd rather have someone here who won't ask me to perform.” Alex squeezes her hand once and walks beside her. No relationship downgrade or withheld disclosure. `lyra_alex_friendship=1`.

**Branch guard:** The kiss cannot appear if Lyra is still dating Dante or Steffan under an exclusive commitment; no broadcaster influence on match outcomes or public reporting.

---


#### FS-BANK-S6 — ## S6. “Rules of Engagement” — Crystal / Raven [E, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S6. “Rules of Engagement” — Crystal / Raven [E, F]
**[FANSERVICE: FS-BANK-S6 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 5 *after* Raven discloses the verifiable Devroe evidence; only if Crystal actively chooses to explore renewed intimacy. **Visual:** Dim training room, Crystal's jacket draped on a chair; Raven wears a training shirt with old scars visible. Neither is ambushed in a private changing area.

**RAVEN:** You've been watching me for ten minutes.

**CRYSTAL:** I've spent ten years deciding whether I ever wanted to see you again.

**RAVEN:** Did you reach a verdict?

**CRYSTAL:** Several. None made the evidence disappear.

He offers her a practice weapon, handle first. She steps into range and disarms him in a single clean movement. Their faces stop close. He does not reach for her.

**[PLAYER CHOICE FOR CRYSTAL]**

- **A — Admit attraction, keep accountability:** “I remember what I wanted. I also remember why I stopped.” If Raven has been truthful and mutual interest is authored, she kisses him once, then steps back: “The investigation continues tomorrow.” `crystal_raven_tension=1`; `devroe_investigation` unchanged.
- **B — Leave a possibility:** “Earn trust. Don't ask me to call that forgiveness.” No kiss; Raven agrees. `crystal_raven_repair_open=1`.
- **C — Close the door:** “We were something. We're not going to be that again.” Raven lets her go, without romantic punishment. `crystal_raven_closed=1`.

**Branch guard:** Raven's truthfulness and Crystal's choice are necessary but not sufficient for any continued relationship. Christian's independent investigation remains intact.

---


#### FS-BANK-S7 — ## S7. “The Human Test” — Ren / Angel [E affinity, P romance]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S7. “The Human Test” — Ren / Angel [E affinity, P romance]
**[FANSERVICE: FS-BANK-S7 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 5 after a voluntary, *non-invasive* diagnostic session and after any acute neural symptoms have passed. **Eligibility:** Ren 25; Angel's age is provisional adult and must be confirmed, as must mutual attraction. **Visual:** Star-lit balcony outside the lab; two people in comfortable off-duty clothing, tension built from shared curiosity rather than exposed bodies.

**REN:** The machine responded before I decided. Everyone calls it an advantage.

**ANGEL:** You don't sound grateful.

**REN:** I want a machine that makes me faster. Not one that finishes my sentences.

Angel offers Ren a paper cup of warm tea. They touch fingertips for a moment. Ren makes the next move, if any.

**[PLAYER CHOICE FOR REN]**

- **A — Ask about a date:** “There's one experiment we haven't tried. Dinner, no sensors.” If both mutually interested and eligible, Angel smiles: “No controls, either. You decide where.” Their hands remain linked as they walk out. `ren_angel_date=1`.
- **B — Admit attraction without pressure:** “I like you. I don't need an answer tonight.” Angel acknowledges it honestly and asks for time. `ren_angel_open=1`; no kiss or forced declaration.
- **C — Choose friendship and work:** “You're the first person who believed me.” “Then let's make sure they listen.” They arrange to share evidence with an independent investigator. `ren_angel_friendship=1`.

**Critical:** No intimacy while Ren is cognitively compromised or under clinical duress; neither dating nor choosing friendship affects access to diagnostics or the Nova evidence.

---


#### FS-BANK-S8 — ## S8. “A Very Unprofessional Evening” — Cossette / Ibrahim [E, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S8. “A Very Unprofessional Evening” — Cossette / Ibrahim [E, F]
**[FANSERVICE: FS-BANK-S8 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 2 or 3, optional supporting-cast respite between serious plot beats. **Visual:** A home workshop turned into a miniature dance floor by a test lighting rig. Cossette and Ibrahim, established adult partners, both dress up for what was supposed to be a technical demo. The intimacy is playful, domestic, and not a joke at Cossette's expense.

**COSSETTE:** You promised one harmless adjustment to the apartment lighting.

**IBRAHIM:** It *is* harmless. It's also synchronized to the music.

A sweep of golden light follows Cossette's chair around the table. Ibrahim bows theatrically.

**IBRAHIM:** May I have this dance?

**COSSETTE:** Only if you remember who taught you how to lead.

He takes her hand. They circle the room together, finding their own rhythm. She draws him down for a warm kiss just as the lights flash a ridiculous victory animation.

**COSSETTE:** Is that supposed to happen?

**IBRAHIM:** In every successful experiment.

**COSSETTE:** Delete the logging function.

**[OPTIONAL OBSERVER CHOICE — REN/ANGEL/ARI]**

- **A — Tease them gently:** “Should we applaud, or invoice the lighting?” → comic reply and a short discussion of the difference between voluntary systems and invasive ones.
- **B — Give them privacy:** Exit quietly. No penalty; no recording.
- **C — Ask a technical question after the dance:** Ibrahim and Cossette independently explain an interface safeguard. Same information available in nonromantic workshop scenes.

**Production note:** This is relationship-positive fanservice without a new selectable romance. The camera treats the couple with warmth, not as an object of voyeurism; there is no hidden recording.

---


#### FS-BANK-S9 — ## S9. “Duel in the Dressing Room” — Dante / Steffan [P, F]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S9. “Duel in the Dressing Room” — Dante / Steffan [P, F]
**[FANSERVICE: FS-BANK-S9 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 5 or post-tournament, when both have become unattached and after any Lyra entanglements are acknowledged honestly. **Visual:** Two adult athletes in striking pre-event tailoring, mirror lights, deliberate flirtation framed as an extension of their rivalry—no accidental nudity or intruding cameras.

**DANTE:** Your jacket is loud.

**STEFFAN:** It's couture. Your jacket looks like you escaped a motorcycle crash.

Dante smooths an unfastened cuff on Steffan's sleeve. Steffan goes very still.

**DANTE:** There. Now you almost look respectable.

**STEFFAN:** Is that what this is about?

**DANTE:** I have no idea. For once, I'm asking instead of fighting.

**[CHOICE FOR SELECTED DANTE/STEFFAN]**

- **A — Explore the possibility:** “Do you ever wonder what we'd do if we stopped competing?” The counterpart may decline, hesitate or admit interest depending on separate authored reciprocity; if mutual, a hand remains on the other person's sleeve and the scene cuts before any assumption of a relationship. `dante_steffan_possibility=1`.
- **B — Keep the rivalry fun:** “Beat me fair and I'll consider complimenting your hair.” They laugh. `rivalry_friendly=1`.
- **C — Draw a boundary:** “It's just a jacket.” They reset their distance, still rivals. `rivalry_distance=1`.

**Branch guard:** This route is explicitly not canonized. Do not depict an affair while either is still exclusively dating Lyra; no romance is earned by defeating Lyra or Dante.

---


#### FS-BANK-S10 — ## S10. “Neon Respite” — ensemble spectacle [F, no romance requirement]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S10. “Neon Respite” — ensemble spectacle [F, no romance requirement]
**[FANSERVICE: FS-BANK-S10 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Mid-tournament optional sponsor-hosted rooftop pool / fashion event, with a quiet backstage alternative. **Visual:** Water reflections on chrome, swimsuits or summer resort attire chosen by the adult participants, playful sparring demonstrations, retro-futurist beach music and a deliberately *balanced* camera montage of multiple attractive competitors. The event is a voluntary public appearance, not a hidden-camera locker room. Nonparticipants stay elsewhere and lose nothing.

Lyra performs a flawless diving-platform spin for the fans, then points at Steffan.

**LYRA:** Your turn. The crowd demands grace.

**STEFFAN:** They demand charisma. I have plenty.

Steffan dives with a spectacular splash, soaking Dante's immaculate jacket. Dante stares at the dripping cuff.

**DANTE:** I am going to win this tournament out of spite.

Mara laughs from a lounge chair. Crystal lifts an eyebrow at the whole spectacle. Alex, off duty, declines the temptation to turn the moment into a broadcast segment. The pool lights briefly trace the silhouettes of the HARs above the roofline.

**[PLAYER CHOICE — ANY PILOT]**

- **A — Join the public fun:** Brief pilot-specific stylish outfit/camera flourish and a comic banter line. `event_participated=1`; *never* a strength buff or required social flag.
- **B — Spend time with an available companion:** If `romance_ready(player,companion)`, an existing date/attraction card may replace 15–30 seconds of montage. Otherwise, an equally warm friendship beat plays. No involuntary pairing.
- **C — Skip publicity:** Optional private workshop or reading-lounge encounter offers the same nonromantic information. `event_participated=0`; no penalty.

**Boundary:** Participants can veto a shot or costume. No minors, covert photography, public nonconsensual humiliation, or links between risqué participation and prize money. The location is a fun interlude, not a prerequisite for uncovering an AI conspiracy.

---


#### FS-BANK-S11 — ## S11. “Press Pass, Returned” — Ari / Leena [P]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S11. “Press Pass, Returned” — Ari / Leena [P]
**[FANSERVICE: FS-BANK-S11 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Late Chapter 5; only after Leena moves document custody/publication decisions to an independent colleague, discloses her conflict, and her romantic eligibility and reciprocal interest are confirmed. **Visual:** Rain against a tiny noodle bar window, Ari's damp jacket over the back of the chair, Leena finally without an on-air voice or a press badge.

**LEENA:** I handed in the access pass. I thought I would feel free.

**ARI:** What do you feel?

**LEENA:** Like I'm about to make a very unprofessional decision.

**ARI:** Ordering a second dessert?

**LEENA:** Worse. Asking you to stay when the rain stops.

**[PLAYER CHOICE FOR ARI]**

- **A — Reciprocate:** Ari takes Leena's hand across the table. “That sounds like a good decision.” When they reach the doorway, Ari waits for her signal; she kisses Ari first. The lights go down on them sharing one umbrella, with no implication of further events. `ari_leena_date=1`.
- **B — Keep possibility open:** “I don't want us confusing relief with trust.” They agree to meet again when the Ganymede story has been independently examined. `ari_leena_open=1`.
- **C — Remain allies:** “You're important to me. Not in that way.” Leena accepts the answer and laughs at the untouched second dessert. `ari_leena_friendship=1`.

**Guard:** Professional independence is a prerequisite to this date, never the *reward* for it. The Ganymede evidence/publication chain functions unchanged in the other branches.

---


#### FS-BANK-S12 — ## S12. “The Blue Hour” — Ari / Mara [E, heightened romantic version]

**Source:** `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md` | **Status:** `BANK_ONLY_NOT_INTEGRATED`

## S12. “The Blue Hour” — Ari / Mara [E, heightened romantic version]
**[FANSERVICE: FS-BANK-S12 | type=LEGACY_SCENE_CARD | scope=PROPOSAL_ONLY | status=REVIEW | note=may duplicate or conflict with active scenes; not automatically playable]**

**Window:** Chapter 4, after their *mutually chosen* Chapter 3 romance and before a scheduled official match. **Prereqs:** `ari_mara_committed=1`, both adults and free of other exclusive commitments, and neither is medically impaired. **Visual:** A private hotel doorway above the neon-lit city; Mara wears Ari's oversized jacket after a late-night walk. Their private room is not recorded by spectators, corporate security feeds, or a voyeuristic game camera.

**MARA:** You realize we're supposed to be enemies tomorrow.

**ARI:** Can we schedule that for after breakfast?

**MARA:** You think you can distract me.

**ARI:** I think you're the one who hasn't let go of my hand.

Mara looks at their joined hands. With her free hand, she slowly draws Ari closer by the jacket collar. Ari stops just short, letting her choose the rest. They kiss; the city's reflected lights stripe the wall behind them.

**MARA:** That doesn't mean I'm letting you win.

**ARI:** I'd be disappointed if you did.

**[PLAYER CHOICE]**

- **A — Stay the night:** “Then I want tonight to be ours.” Mara answers with a second kiss and an unambiguous “Stay.” She draws Ari inside, the door closes, and the scene fades to the blue sunrise. *Intimacy is implied, not shown.* `ari_mara_private_night=1`. Their match remains fully competitive and decisive.
- **B — One more kiss, then leave:** “I want you rested enough to beat me fairly.” Mara laughs at that, kisses Ari once more, and sends Ari back to the hallway. `ari_mara_private_night=0`; no relationship penalty.
- **C — Talk instead:** “I can't stop thinking about your mother, or my sibling.” They sit on the floor outside the door and speak quietly until sunrise. Intimacy is emotional; the scene does not imply sex. `ari_mara_emotional_trust=1`.

**Alternate suppression:** If Ari and Mara stayed friends, this scene **does not trigger**. Offer the existing quiet post-spar friendship exchange or a solo late-night call instead. No breakup or romantic ambiguity is fabricated.

---

## Integration and consistency checklist

1. **No forced romance / no unearned payoff:** Every heated scene has an explicitly nonromantic response or a route-suppression alternative. Endings never infer sex, commitment or reconciliation from a single flirt flag.
2. **No overlapping exclusivity:** Validate Lyra/Dante/Steffan/Alex/Ren, Ari/Mara/Leena, Mara/Plug/Raven, Angel/Ren, and other authored commitments before showing kisses or dates. Non-exclusivity is not implicit.
3. **Character agency:** Lyra chooses the public image, Mara retains independence, Crystal can withhold forgiveness, Ren can refuse interfaces, and secondary characters can decline advances without punishment.
4. **Professional and research ethics:** Leena/Alex recuse where needed; Varga's private study remains a violation; technicians' bills and medical oversight never hinge on intimacy. No contact under impairment or ambiguous consent.
5. **Tournament continuity:** Dialogue consults actual wins, losses and opponents; no match draw, romance-based power-up, illicit fight-fixing or fabricated semifinal.
6. **Rating / scene economy:** Spicy moments imply rather than anatomically depict sex. Typical scene 30–120 sec, optional and replayable, skip-able, with arcade-mode cutdowns or outfit-only nods.
7. **Production flag rule:** A *fanservice outfit* flag must not double as `mutual_interest`, `dating`, or `consent`. A suggestive photo pose is not an invitation to private touch.
8. **Age and attraction proof:** Confirm exact adult age/preferences for Leena, Alex, Plug and Angel before production. Never auto-assign attraction based on player gender, public persona, or intimate camera framing.
9. **Story balance:** At least one unambiguously *fun* scene per chapter's optional social menu; use intimate scenes to amplify trust conflicts, never to replace the AI mystery or fight pacing.
10. **Authoritative status:** Requested direction = accepted; each drafted scene/pairing/scene placement = proposal, until separately selected and rewritten into the main screenplays.

