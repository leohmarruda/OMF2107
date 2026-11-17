# ONE MUST FALL 2107
## Chapter 2 — The Champion's Shadow

**Screenplay:** v0.3 (Ari branch repair: outcome-driven gate and replacement scenes; default dramatic spine retained)  
**Timeline:** Tournament Days 3–4  
**Primary playable fight:** Ari vs. Crystal  
**Main characters:** Ari, Crystal, Mara, Lyra, Steffan, Dante  
**Secondary appearances:** Jean-Paul, Varga, Raven, Ren, Angel, Milano, Shirro

### Chapter objectives

- Establish Lyra's independence, athletic skill, and celebrity appeal.
- Develop the Steffan–Lyra attraction while retaining Dante's dignity and competitiveness.
- Advance Ari and Mara from playful acquaintances toward personal trust.
- Confront Ari with Crystal's imperfect but sincere legacy.
- Introduce further hints of neural-interface irregularities.
- Demonstrate that player victories genuinely change tournament outcomes.

**AUTHORITATIVE BRANCH CONTRACT (v0.3):** This chapter is rendered only through `14_Ari_Campaign/ari_route_validator.py`. A fight's recorded winner determines the scene, and `14_Ari_Campaign/Ari_Alternate_Scenes_v0.1.md` supplies longer replacement/dialogue cards. All default prose is gated: when it contradicts the actual bracket, hide it. The optional cards are not new canon.

---

# SCENE 1 — ELECTRIC CELEBRITY

**[CINEMATIC — DAY 3, AFTERNOON]**

**INT. CHAMPIONSHIP ARENA**

A deafening crowd chants Lyra's name.

Holographic projections display Electra's silhouette above thousands of spectators.

Lyra's modeling campaigns, sponsorships, and athletic achievements appear across the broadcast montage.

**ALEX (BROADCAST)**

And here comes the face of a dozen international campaigns—and the pilot who made last year's exhibition circuit look easy!

**LEENA (BROADCAST)**

Three major championships, Alex. She didn't get here by being photogenic.

**ALEX**

Though I imagine it hasn't hurt.

**LEENA**

Neither has being extremely good at fighting.

Lyra's Electra faces Milano's Gargoyle.

A short montage shows an intense exchange. Milano uses heavy defensive positioning, but Lyra anticipates his counterattack.

Electra lands a precise finishing sequence.

**SHIRRO**

LYRA KISARAGI TAKES THE MATCH!

The crowd erupts.

Lyra raises both hands, victorious.

A sea of illuminated Electra symbols ripples through the stadium.

She spots a group of young fans near the front row and points toward them.

They scream with excitement.

**[CUT TO BACKSTAGE]**

Lyra is drying her hair when Steffan appears beside the dressing-room entrance.

**STEFFAN**

That final counter. Beautiful.

**LYRA**

You actually watched the fight?

**STEFFAN**

Every second.

**LYRA**

That's unusual. Most people just watch the entrance.

**STEFFAN**

The entrance was excellent too.

Lyra smiles despite herself.

**LYRA**

Careful. I might think you're trying to flatter me.

**STEFFAN**

I wouldn't insult your intelligence.

**LYRA**

That's encouraging.

**STEFFAN**

I'd rather challenge your confidence.

**LYRA**

You'd need an appointment. My confidence has a very busy schedule.

Steffan laughs.

**STEFFAN**

You know, when you and I meet, I intend to win.

**LYRA**

That's adorable.

**STEFFAN**

Adorable?

**LYRA**

Most men at least pretend to be intimidated.

**STEFFAN**

Maybe I should buy you dinner and practice.

Lyra considers the invitation.

**LYRA**

I'm having dinner with Dante.

Steffan's expression barely changes.

**STEFFAN**

Of course.

**LYRA**

And I'm not sure you'd survive the conversation.

**STEFFAN**

I'll take that as an invitation to improve my conversational skills.

She turns toward her fans.

**LYRA**

Then start by learning when someone has to leave.

She walks away, smiling.

Steffan watches her go.

Dante steps out from behind a nearby equipment display.

**DANTE**

Enjoying yourself?

**STEFFAN**

Enormously.

**DANTE**

Stay away from her.

**STEFFAN**

Why? Afraid she might decide I'm more entertaining?

**DANTE**

Afraid you'll make an idiot of yourself in public.

Steffan steps closer.

**STEFFAN**

That concern almost sounds affectionate.

**DANTE**

Don't flatter yourself.

**STEFFAN**

You make that difficult.

Dante stares at him.

**DANTE**

You'll get your chance against me.

**STEFFAN**

Good.

A pause.

**STEFFAN**

I'd hate to think you were avoiding me.

Steffan walks away.

Dante remains tense, then notices a broadcast replay of Lyra's victory.

His expression softens into genuine pride.

---

## SCENE 1B — OFF AIR (OPTIONAL: LYRA / ALEX)

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

# SCENE 2 — BREAKFAST WITH THE ENEMY

**[CINEMATIC — DAY 3, MORNING]**

**INT. COMPETITORS' CAFETERIA**

Ari studies the tournament schedule on a handheld screen.

Mara places a breakfast tray opposite Ari without asking permission.

**MARA**

You're going to get wrinkles.

**ARI**

What?

**MARA**

That expression. You've been making it for three consecutive minutes.

**ARI**

I'm reviewing the match schedule.

**MARA**

That's what the expression says.

Ari looks up.

**ARI**

Good morning to you too.

**MARA**

See? Better already.

She takes a seat.

The screen shows the remaining Group A match:

**ARI SOLANO vs. CRYSTAL DEVROE**

**MARA**

Ah. The living legend.

**ARI**

You sound impressed.

**MARA**

I am impressed. She's very good.

**ARI**

I know.

**MARA**

That doesn't sound like you're impressed.

**ARI**

She won the championship ten years ago. WAR still uses her victory to advertise itself.

**MARA**

And she doesn't work for them anymore.

**ARI**

That doesn't mean she has nothing to answer for.

Mara considers this.

**MARA**

Maybe not. But you're fighting the woman, not the advertising department.

Ari pauses.

**ARI**

You think I'm being unfair?

**MARA**

I think you sometimes enter an argument before anyone has started one.

Ari smiles reluctantly.

**ARI**

You're unusually perceptive for someone who steals pastries.

**MARA**

The pastries are how I maintain my powers.

Her communicator vibrates.

She glances at it.

**MEDICAL BILLING — PAYMENT REMINDER**

She dismisses the notification.

Ari notices the change in her expression but not the message itself.

**ARI**

Everything okay?

**MARA**

Of course. I just remembered the universe expects me to pay for things.

**ARI**

Inconvenient.

**MARA**

Deeply.

She reaches for Ari's untouched toast.

**ARI**

Excuse me?

**MARA**

You weren't eating it.

**ARI**

I was considering it.

**MARA**

Consider faster.

Ari laughs.

Mara looks at the match schedule again.

**MARA**

For what it's worth, I think you've got a chance.

**ARI**

Against Crystal?

**MARA**

No, against the toast. Yes, against Crystal.

**ARI**

Any advice?

**MARA**

Don't try to beat her at being Crystal Devroe.

**ARI**

Meaning?

**MARA**

She's had ten years to perfect that particular skill.

For once, Ari has no immediate reply.

Mara smiles.

**MARA**

See? My professional advice is improving.

---

# SCENE 3 — THE PRICE OF A LEGEND

**[CINEMATIC — DAY 3, LATE AFTERNOON]**

**INT. HALL OF CHAMPIONS**

Crystal stands before a display commemorating the 2097 tournament.

An interviewer finishes a segment.

**INTERVIEWER**

Ten years later, do you still consider that victory the proudest moment of your life?

**CRYSTAL**

One of them.

**INTERVIEWER**

Would you change anything?

Crystal looks at the archival image of herself standing over Nova.

**CRYSTAL**

Quite a few things that happened afterward.

**INTERVIEWER**

Such as?

**CRYSTAL**

That's a longer interview.

The interviewer smiles, thanks her, and departs.

Ari approaches.

**ARI**

You didn't answer the question.

**CRYSTAL**

I answered the part I could in thirty seconds.

**ARI**

You helped make WAR look like it had changed.

**CRYSTAL**

I believed it could.

**ARI**

People believed you.

**CRYSTAL**

Some still do.

**ARI**

My sibling did.

Crystal's expression changes.

**CRYSTAL**

You're from the settlement affected by the evacuation crisis.

**ARI**

You know about it?

**CRYSTAL**

I know the official account.

**ARI**

Then you don't know very much.

Crystal doesn't respond defensively.

**CRYSTAL**

What do you know that I don't?

**ARI**

I know relief was requested before WAR claims it was. I know the transport capacity wasn't exhausted. And I know someone changed the timeline afterward.

**CRYSTAL**

Do you have evidence?

**ARI**

Some.

**CRYSTAL**

Then we should look at it.

Ari seems momentarily surprised.

**ARI**

Just like that?

**CRYSTAL**

Do you want me to refuse?

**ARI**

I want you to understand what happened.

**CRYSTAL**

So do I.

A pause.

**ARI**

You could have done more after 2097.

**CRYSTAL**

Yes.

Ari studies her.

**CRYSTAL**

I don't know whether I could have prevented what happened to your family. I wasn't running WAR, and I'd left its Ganymede position before the crisis.

**ARI**

But you knew what the company was.

**CRYSTAL**

I knew some of it. I learned more. Eventually I realized I couldn't change the rest from the position they'd given me.

**ARI**

And you walked away.

**CRYSTAL**

I did.

**ARI**

People who lived there couldn't.

Crystal absorbs that.

**CRYSTAL**

No. They couldn't.

Silence.

Then she glances toward the arena schedule.

**CRYSTAL**

We fight tomorrow.

**ARI**

I haven't forgotten.

**CRYSTAL**

Good. Don't expect me to go easy on you.

**ARI**

I wouldn't want you to.

**CRYSTAL**

Then we understand each other.

Ari leaves.

Raven emerges from a side corridor.

**RAVEN**

That looked unpleasant.

**CRYSTAL**

It was useful.

**RAVEN**

You seem to have a talent for collecting angry young people.

**CRYSTAL**

And you seem to have a talent for avoiding questions.

Raven says nothing.

**CRYSTAL**

You heard what Ari said?

**RAVEN**

Enough.

**CRYSTAL**

If you know anything about those records—

**RAVEN**

Not everything WAR did passed through me.

**CRYSTAL**

That's not what I asked.

Raven looks at the archival display.

**RAVEN**

No. It isn't.

He leaves before she can continue.

---

# SCENE 4 — A MATTER OF COMPATIBILITY

**[OPTIONAL CINEMATIC]**

**INT. NEURAL RESEARCH WING — DAY 3, EVENING**

Ren is reviewing a simulation while Varga records synchronization data.

Jean-Paul arrives carrying a medical consent form.

**JEAN-PAUL**

Doctor. I was told you needed me.

**VARGA**

For a routine screening.

**JEAN-PAUL**

How disappointing.

**VARGA**

You haven't seen the questionnaire.

Ren looks up.

**REN**

Some of the questions are very unusual.

**VARGA**

Only if you answer honestly.

Jean-Paul smiles.

**JEAN-PAUL**

That seems rather unfair.

Varga gestures toward a chair.

**VARGA**

Sit.

He does.

**JEAN-PAUL**

You have an authoritative manner.

**VARGA**

And you have an inconvenient tendency to talk when someone is trying to measure your attention.

**JEAN-PAUL**

Perhaps you should measure how much attention I'm paying to you.

Varga studies the readout.

**VARGA**

Elevated.

Ren looks between them.

**REN**

Is that an actual result?

**VARGA**

Not one we're publishing.

Ren returns to the simulator, slightly embarrassed.

Jean-Paul leans toward Varga.

**JEAN-PAUL**

You enjoy making people uncomfortable.

**VARGA**

Not particularly.

**JEAN-PAUL**

No?

**VARGA**

I enjoy seeing what they do when they're uncomfortable.

Their eyes meet.

**JEAN-PAUL**

That's worse.

**VARGA**

Scientifically, it's much more useful.

The interaction remains playful, but Jean-Paul notices an encrypted research folder on her console.

**PRIVATE STUDY — AFFECTIVE VARIABILITY**

He says nothing.

Varga notices where he looked.

She closes the window.

**VARGA**

Curiosity is a useful trait.

**JEAN-PAUL**

I thought you'd approve.

**VARGA**

Only when appropriately supervised.

---

## SCENE 4B — NEON RESPITE (OPTIONAL PUBLIC FAN EVENT)

**[INTEGRATED FAN SERVICE / COMEDY — DAY 3, NIGHT; 60–100 sec]**

**Gate:** any selected pilot can opt in. The segment plays *after* the day's matches and public obligations, not instead of them. Skip is always available. Lyra and Dante remain a couple on the default route; no public Steffan–Lyra romantic staging is assumed.

On a sponsor rooftop, reflected pool light scatters across a display of miniature HARs. Several adult pilots choose swimwear or tailored resort attire; staff ask permission before filming. Shirro poses extravagantly for a camera that has already found a better subject: Lyra demonstrating an impossible-looking dive for the cheering fans.

**LYRA:** That's what they call grace, Steffan. Your turn.

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

# SCENE 5 — THE WRONG WAY TO BEAT A CHAMPION

**[CINEMATIC — DAY 4, BEFORE ARI'S MATCH]**

**INT. PRACTICE FACILITY**

Ari practices against a simulated opponent using archived footage of Crystal's 2097 fighting style.

The simulation repeatedly anticipates Ari's approach.

Ari mutters in frustration.

Mara watches from the doorway.

**MARA**

You're doing it again.

**ARI**

Doing what?

**MARA**

Trying to prove something to a machine that can't appreciate the effort.

**ARI**

I'm studying her reactions.

**MARA**

You're studying how to make the same mistake with increasing precision.

Ari shuts down the simulation.

**ARI**

You have a better idea?

**MARA**

Several. Most of them involve not attacking her where she expects you.

She approaches the controls.

**MARA**

Look at this.

Mara replays Crystal's counterattack.

**MARA**

You see how she shifts her weight before the strike?

**ARI**

Yes.

**MARA**

That's not the important part.

She pauses the image one moment earlier.

**MARA**

Here. She's already decided what you're going to do.

**ARI**

So?

**MARA**

Make her decide wrong.

Ari considers the demonstration.

**ARI**

That's useful.

**MARA**

I know. It's very inconvenient for my reputation.

Ari turns to face her.

**ARI**

Why are you helping me?

Mara considers the question.

**MARA**

Maybe I want to fight someone interesting in the final.

**ARI**

Maybe?

**MARA**

Maybe I like your company.

A small pause.

Ari smiles.

**ARI**

That sounds dangerously close to a compliment.

**MARA**

Don't tell anyone.

### [CHOICE 2 — RESPONSE]

**A. Competitive**

**ARI:** If we meet in the final, I won't hold back.

**MARA:** Good. Neither will I.

**B. Warm**

**ARI:** For what it's worth, I like your company too.

**MARA:** I had a suspicion. You're getting easier to read.

**C. Teasing**

**ARI:** So all this advice is an elaborate attempt to impress me?

**MARA:** It's working, isn't it?

**[All responses converge.]**

An announcement calls Ari to the preparation area.

**MARA**

Go on. Make her work for it.

**ARI**

You coming to watch?

**MARA**

I wouldn't miss it.

---

# SCENE 6 — ARI VS. CRYSTAL

**[MANDATORY FIGHT — DAY 4]**

**INT. MAIN ARENA**

The crowd is enormous.

Crystal's image appears beside archival footage from 2097.

Ari's image appears beside a news report describing the Ganymede dissident movement.

**ALEX (BROADCAST)**

A veteran legend against one of the tournament's most determined newcomers.

**LEENA**

Crystal Devroe has spent ten years hearing people tell her she's unbeatable. Ari Solano may be the first person this week who genuinely doesn't care.

**ALEX**

You think Solano can win?

**LEENA**

I think Crystal's going to have to earn it.

### Pre-fight cinematic

Ari's HAR enters the arena.

Crystal's HAR steps forward.

**CRYSTAL**

You looked at the footage.

**ARI**

I did.

**CRYSTAL**

Then you know what you're getting into.

**ARI**

I know what you used to do.

Crystal smiles faintly.

**CRYSTAL**

Good answer.

The arena lights intensify.

**SHIRRO**

FIGHT!

### [FIGHT 2 — ARI VS. CRYSTAL]

This is an ordinary, fair championship fight.

Crystal is a technically skilled opponent who uses well-timed counters, strong defense, and punishing responses to predictable attacks.

The fight tests what Ari learned from Mara without making that training mandatory for success.

**Default fictional outcome:** Crystal wins.

**Playable outcome:** The actual player result determines the story branch.

---

# SCENE 7A — IF CRYSTAL WINS

**[BRANCH: Crystal won the current fight. The group standings below are shown ONLY if Ari previously beat Selene. Otherwise branch to `GA_OUT` after the post-match conversation.]**

Ari's HAR falls to one knee.

Crystal steps back rather than delivering an unnecessary final strike.

**SHIRRO**

CRYSTAL DEVROE TAKES THE MATCH!

**ALEX**

The legend remains undefeated in Group A!

Ari exits the cockpit, disappointed and frustrated.

Crystal approaches.

**CRYSTAL**

You nearly caught me with that second counter.

**ARI**

Nearly doesn't count.

**CRYSTAL**

In the standings? No.

Ari looks away.

**CRYSTAL**

You fought well.

**ARI**

I wanted to win.

**CRYSTAL**

I noticed.

She pauses.

**CRYSTAL**

Send me those Ganymede records.

Ari looks back.

**ARI**

You're still willing to help?

**CRYSTAL**

I said I would.

**ARI**

Even after all that?

**CRYSTAL**

Ari, I've been insulted by people far more important than you.

Ari almost laughs.

**CRYSTAL**

And some far less interesting.

Her expression softens.

**CRYSTAL**

Winning against me wasn't a condition.

She walks away.

### Default Group A standings — only if Ari beat Selene

1. Crystal — 2 wins.
2. Ari — 1 win.
3. Selene — 0 wins.

Both Crystal and Ari qualify for the knockout stage.

Under the tournament's published seeding, Ari will face Group B's winner in the quarterfinals.

If Mara wins Group B as expected, that opponent will be Mara.

---

# SCENE 7B — IF ARI WINS

**[ALTERNATE STORY ROUTE. The group standings below assume Ari also beat Selene; if he lost to Selene, run 7C after the shared Crystal-loss post-fight conversation.]**

Crystal's HAR crashes against the arena floor.

The crowd erupts.

For a moment, the commentators are speechless.

**SHIRRO**

ARI SOLANO HAS DEFEATED CRYSTAL DEVROE!

**ALEX**

THE 2097 CHAMPION HAS FALLEN!

**LEENA**

That changes the entire Group A bracket.

Ari emerges from the HAR, exhilarated.

Crystal approaches.

**CRYSTAL**

Well fought.

**ARI**

I wasn't sure I'd catch you.

**CRYSTAL**

Neither was I.

She smiles.

**CRYSTAL**

You found a weakness I should have corrected years ago.

**ARI**

I had help.

**CRYSTAL**

Then you know the value of listening.

Ari glances toward the competitors' section, where Mara is cheering.

**CRYSTAL**

Don't let winning convince you that you've answered every question.

**ARI**

I won't.

**CRYSTAL**

Good. Now send me those Ganymede records.

Ari looks surprised.

**ARI**

You're still interested?

**CRYSTAL**

More than ever.

She offers a handshake.

Ari accepts.

### Alternate Group A standings — only if Ari also beat Selene

1. Ari — 2 wins.
2. Crystal — 1 win.
3. Selene — 0 wins.

Ari now faces Group B's runner-up in the quarterfinals.

If Group B's default results remain unchanged, this means:

- Ari vs. Ren.
- Crystal vs. Mara.

Ari and Mara will not face each other in the quarterfinals, although they may still meet later if both advance.

**Important:** The scene must not later pretend that Crystal won or that Ari was automatically assigned to fight Mara.

---

## SCENE 7C — ARI BEATS CRYSTAL AFTER LOSING TO SELENE (`GA_CYCLE`)

Three decisive fights, three fighters with exactly one victory. **This is a standings circle, not a drawn fight.** Crystal beat Selene, Selene beat Ari, Ari beat Crystal. Under the current provisional pre-published circular seed the ranking is **Crystal / Ari / Selene**.

**ALEX:** Ari wins! Is he the group champion?

**LEENA:** Not under the provisional circular-record rule. Crystal ranks first on published seed; Ari still qualifies, second. He faces Mara.

**ARI:** I beat Crystal, but she's seeded above me?

**CRYSTAL:** You beat me today. No one can take that from you. The ranking rule isn't a second fight.

**SELENE:** What an irritatingly elegant way to go home with a win.

Ari offers to share his Ganymede source documents with Crystal. The exchange is based on trust, not whether Crystal won or lost.

## SCENE 7D — ARI LOSES BOTH QUALIFYING MATCHES (`GA_OUT`)

Crystal's name appears first, Selene's second, Ari's third. **2–0 / 1–1 / 0–2**. There will be no Ari quarterfinal.

**SHIRRO:** GROUP A QUALIFIERS: CRYSTAL DEVROE AND SELENE VALE!

**ARI:** No knockout for me.

**CRYSTAL:** No. But Ganymede's records are still worth reading. Send them.

**ARI:** Even after I lost?

**CRYSTAL:** I didn't offer because you might win a trophy.

Ari may work with Christian, Angel or an independent journalist/archivist. This changes the investigation texture, not the authenticity of the documented abuse or the reality of his losses. His playable path continues in **Ch3 Scene 13C / Ch4 Scene 5C**, not into a fictitious match against Mara.

# SCENE 8 — THE PERSON WAITING OUTSIDE

**[CINEMATIC — AFTER THE FIGHT]**

**INT. COMPETITORS' MEDICAL CORRIDOR**

Ari exits a routine post-match examination.

Mara is waiting beside a vending machine.

She holds two drinks.

**MARA**

I got you something.

Ari examines the cup.

**ARI**

What is it?

**MARA**

No idea. The machine called it victory-flavored electrolyte recovery.

**ARI**

That sounds terrible.

**MARA**

It was either that or commemorative Shirro coffee.

She holds up the alternative cup.

**MARA**

Apparently it comes with a speech.

Ari laughs.

### If Ari lost

**MARA**

You gave her a hell of a fight.

**ARI**

I lost.

**MARA**

Yes. I was there.

**ARI**

Then why do you sound so pleased?

**MARA**

Because you made Crystal Devroe change her entire approach halfway through a match.

**ARI**

It wasn't enough.

**MARA**

Today.

Ari looks at her.

**MARA**

You're still in the tournament, you know.

### If Ari won

**MARA**

You actually did it.

**ARI**

You sound surprised.

**MARA**

I was surprised. Crystal's frightening.

**ARI**

Should I be offended?

**MARA**

Only if you think I'm easily impressed.

She hands Ari the drink.

**MARA**

Besides, I told you to make her decide wrong. You listened.

**ARI**

I do that occasionally.

**MARA**

Let's not make a habit of it.

### Shared continuation

Ari takes a sip.

**ARI**

This is awful.

**MARA**

I know. I tried mine first.

**ARI**

You still gave it to me?

**MARA**

I wanted to see your face.

They both laugh.

Then Ari notices that Mara's expression has become thoughtful.

**ARI**

What?

**MARA**

Nothing.

**ARI**

Mara.

She considers saying something more personal, then chooses a lighter answer.

**MARA**

Just wondering whether you're always this stubborn.

**ARI**

Usually.

**MARA**

That could be a problem.

**ARI**

For you?

Mara holds Ari's gaze for a moment.

**MARA**

Possibly.

The announcement system calls the remaining Group B competitors for tomorrow's matches.

Mara looks toward the arena.

**MARA**

I've got Ren tomorrow.

**ARI**

Good luck.

**MARA**

I prefer skill.

**ARI**

Then use both.

She smiles.

**MARA**

I'll consider it.

Mara turns to leave.

**ARI**

Dinner sometime?

She stops.

**MARA**

Is that a request for tactical consultation?

**ARI**

No.

Mara's smile becomes noticeably warmer.

**MARA**

Then ask me again after tomorrow.

She leaves.

Ari watches her go.

The moment is hopeful, but it establishes no guarantee about the tournament or the relationship.

---

# SCENE 9 — THE THINGS THE COMPUTER DIDN'T SAY

**[SHORT MYSTERY SCENE — DAY 4, NIGHT]**

**INT. NEURAL DIAGNOSTICS LAB**

Ren reviews footage from a recent enhanced-link test.

Angel stands at an independent monitoring console.

On the screen, a HAR executes a difficult defensive maneuver.

**REN**

That response was faster than my conscious correction.

**ANGEL**

Predictive assistance?

**REN**

Probably. That's what the system is designed to do.

Ren replays the sequence.

**REN**

Except I don't remember intending the adjustment.

**ANGEL**

You don't necessarily remember every motor intention.

**REN**

I know.

Ren looks again.

**REN**

It still feels strange.

Angel compares the neural trace with the executed movement.

A small discrepancy appears.

**ANGEL**

Do you have an independent recording?

**REN**

Yes.

**ANGEL**

Good. Keep it.

**REN**

Why?

Angel displays a record associated with the obsolete Nova identifier.

**ANGEL**

Because the central system has already corrected its copy.

Ren looks concerned.

**REN**

Corrected what?

**ANGEL**

That's what I'd like to know.

CUT TO:

**INT. PRIVATE RESEARCH OFFICE**

Varga watches a short recording of Steffan talking to Lyra.

She adds a time-stamped note to her private observations.

Her eyes linger on a separate interview schedule.

She moves one appointment by twenty minutes.

The change places Steffan and Lyra in the same backstage corridor the next afternoon.

Varga closes the schedule.

Her office becomes quiet again.

The act is small, nearly mundane.

Its eventual consequences will not be.

---

# SCENE 10 — THE EMPTY PLACE

**[OPTIONAL ARI EPILOGUE — NIGHT]**

**INT. OBSERVATION DECK**

Ari stands alone, looking out toward Ganymede.

A news display shows footage of the championship and Crystal's public statements.

Ari opens an old personal message thread.

The most recent entry is several years old.

A photograph shows Ari with the sibling who died during the crisis.

No sentimental speech is necessary.

Ari starts recording a voice message, then stops.

After a moment, Ari closes the conversation.

A new message appears.

**MARA:** The machine's coffee was worse. In case you're wondering.

Ari smiles.

### [CHOICE 3 — REPLY]

**A.** That's reassuring. I was beginning to question your judgment.

**B.** I'm glad you were there today.

**C.** We should find somewhere that serves actual food.

Mara responds appropriately, with humor or a hint of affection.

Ari puts the communicator away.

The camera pulls back to reveal the vast darkness beyond the observation windows and Ganymede hanging beneath Jupiter.

**END OF CHAPTER 2**

---

# ARCADE MODE — COMPRESSED VERSION

## Opening transition

A broadcast montage shows Lyra defeating Milano.

**ALEX:** Another spectacular victory for Lyra Kisaragi!

**LEENA:** And tomorrow, Crystal Devroe faces the Ganymede newcomer Ari Solano.

Mara approaches Ari in the competitors' corridor.

**MARA:** You're going up against a legend.

**ARI:** I know.

**MARA:** Good. Then try not to look so impressed.

## Pre-fight

**CRYSTAL:** You've seen the footage. You know what I'm capable of.

**ARI:** I've seen what you used to do.

**CRYSTAL:** Then let's see what you've learned.

**[FIGHT — ARI VS. CRYSTAL]**

## Post-fight, Crystal victory

**CRYSTAL:** Well fought. And send me those Ganymede records.

**ARI:** Even after I lost?

**CRYSTAL:** They weren't part of the wager.

## Post-fight, Ari victory

**CRYSTAL:** You earned that victory. Send me the records.

**ARI:** You still want to help?

**CRYSTAL:** More than ever.

## Closing transition

Mara watches the result.

**MARA:** Not bad, Solano.

Ren notices an unusual response in a neural-interface recording.

**REN:** I don't remember making that adjustment.

Angel studies the log.

**ANGEL:** Then why does the system say you did?

The screen flickers.

**NVA-97 — RECORD UPDATED**

---

# IMPLEMENTATION NOTES

## Match state

`GROUP_A_RESULT` alone is insufficient. Use both official match IDs and actual results: `G_Ari_Selene` (screen first) and `G_Ari_Crystal` (screen second), with engine IDs bound to their participants. The four combinations are:

| Ari–Selene | Ari–Crystal | Group A rank for Ari | Next scene |
|---|---|---|---|
| Win | Lose | 2 | Ari–Mara Q2 |
| Win | Win | 1 | Ari–Ren Q1 |
| Lose | Win | 2 (1–1–1 provisional seed) | Ari–Mara Q2 |
| Lose | Lose | 3, eliminated | Archive investigation; Selene–Mara Q2 |

No match ends in a draw; only the group standings may be tied on one win each. The seed remains a provisional public rule rather than finalized canon.

## Relationship state

`MARA_RAPPORT` accumulates small differences in dialogue tone without making early flirting mandatory for romance.

`MARA_TRUST` is tracked separately and becomes important when Ari receives WAR's advanced neural-program invitation.

The romance must not depend solely on selecting flirtatious dialogue.

## Narrative information

`GANYMEDE_EVIDENCE_STAGE` remains preliminary.

Ari has contradictions and incomplete records, not yet definitive evidence of corporate responsibility.

`NOVA_ANOMALY_STAGE` advances through Angel and Ren's independent investigation.

The player has not yet discovered Kreissack's survival.

`VARGA_OBSERVATION_STAGE` now includes social scheduling interference, but no major public manipulation is revealed.

## Character continuity

Lyra has not yet cheated on or broken up with Dante.

Steffan's attraction is partly sincere and partly driven by rivalry.

Dante's anger must remain understandable without reducing him to a stereotypical jealous boyfriend.

Crystal is not responsible for the Ganymede crisis merely because she once represented WAR's interests.

Mara's medical-debt problem is hinted at, not fully disclosed.

## Scene priority

**Mandatory cinematic content:**

- Lyra's victory and Steffan's pursuit.
- Ari–Mara cafeteria interaction.
- Ari–Crystal confrontation.
- Ari–Crystal match.
- Ari–Mara post-match encounter.
- Brief neural-anomaly scene.

**Optional expanded content:**

- Jean-Paul–Varga screening.
- Full pre-match practice conversation.
- Ari's late-night observation-deck scene.

**Player-controlled content:**

- Ari vs. Crystal.
- Optional training drill.
- Dialogue choices that influence relationship tone.

## Success criteria

By the chapter's end:

1. The player respects Crystal as a formidable opponent and a complicated person.
2. Ari's political grievance feels specific rather than purely rhetorical.
3. Ari and Mara have developed credible mutual attraction.
4. Lyra is firmly established as a skilled athlete with an identity beyond her romantic relationships.
5. Steffan's pursuit is attractive but contains visible competitive motives.
6. Neural enhancement appears exciting and slightly unsettling, not obviously evil.
7. Both outcomes of Ari–Crystal remain narratively valid.

---

# NEXT CHAPTER — THE TROUBLE WITH ATTRACTION

Chapter 3 should cover Days 5–7 and the conclusion of qualification.

**Principal developments:**

- Mara defeats Ren and wins Group B.
- Steffan defeats Lyra, securing Group C's top position.
- Angel defeats Dante, winning Group D.
- Lyra's interest in Steffan becomes harder to dismiss.
- Ari and Mara have a more personal conversation about family, money, and the future.
- Jean-Paul deepens his involvement with Varga.
- Ari receives stronger evidence about Ganymede.
- The advanced neural-program invitation is introduced.
- Ari and Mara may choose romance **or** close friendship before the knockout bracket is announced; neither outcome changes the bracket.

The ending diverges according to **both** of Ari's group fights: a first-place Ari faces Ren; a second-place Ari faces Mara; a third-place Ari continues the investigation outside the official bracket. The circular-standing case ranks Ari second on the provisional seed.

The romantic stakes remain significant in both routes, but their immediate competitive consequences differ.
