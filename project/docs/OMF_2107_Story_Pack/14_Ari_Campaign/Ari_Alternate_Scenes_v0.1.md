# One Must Fall 2107 — Ari Solano: Alternate Scene Bank v0.1

**Editorial status:** Draft replacement/conditional scenes, not a separate parallel canon. This document is a complete authoring reference for branch coverage of Ari's selected-pilot campaign. The Ari v0.3 chapter files embed condensed versions or call out these scenes by key. When a player result and old default narration disagree, the result wins and the default narration is suppressed. The actual fight is always decisive; standings may be tied on wins.

**Shared invariant:** Official tournament matches are fair. WAR is accountable for Ganymede's policies; Nova's later secret control of Kreissack is a separate plot. The evidence of Kreissack's biological survival appears by the midpoint; the coolant-wing rescue is genuinely beneficial on Day 12; Nova's covert executive veto becomes conclusive after the Day-13 final. Romantic choices neither unlock essential clues nor decide fights.

## A1. Day 3: Selene wins Ari's opening group match (`ARI_SELENE_LOSS`)

**[REPLACE Ch1 Scene 5B only when Ari loses; keep pre-fight and player bout.]**

Selene's Mirage reverses Ari's last attack, circles past Thorn's guard, and ends the bout decisively. Ari's cockpit display shows a loss, with no interference diagnostics. The broadcast erupts.

**SHIRRO:** SELENE VALE WINS THE OPENING MATCH!

**ALEX:** Solano came in to make a political statement. Selene has just reminded everyone this is also a fighting tournament.

**LEENA:** That should not make his allegations more or less credible. His fighting and his evidence are separate questions.

In the service corridor Ari peels the safety tape from his wrist. Selene stops at a respectful distance.

**SELENE:** I suspect you expected me to be a corporate mascot.

**ARI:** I expected to win.

**SELENE:** People are allowed to be wrong twice in one evening.

**ARI:** Are you going to sell me a sponsorship now?

**SELENE:** No. You would be a terrible client. You would read the contract.

Ari looks at her despite himself.

**SELENE:** You found something on Ganymede. Don't let losing a fight persuade you that nobody will listen. And don't mistake a press opportunity for a favor.

She leaves before he can ask whether it was advice or a warning. Mara finds him outside the medical bay, offering a hot drink without consolation speeches.

**MARA:** Want to complain?

**ARI:** Yes.

**MARA:** Excellent. You have four minutes. Then we review the third-round counter you missed.

**ARI:** Four minutes?

**MARA:** I only have three.

Ari laughs once, reluctantly. **[CHOICE]** Ask for technical analysis, take a quiet walk, or politely request space. All maintain Ari's standing as a fighter and access to the investigation; no romance is implied.

**Arcade cut:** `SHIRRO: SELENE WINS.` `ARI: Fair enough. Crystal's next.` No false victory montage.

## A2. Day 5: Group A's four possible conclusions (`ARI_GROUP_RECAP`)

The on-screen match order is Selene, then Crystal; the engine's data order is Crystal, then Selene. The 2097 champion Crystal defeats Selene in all current Ari-selected simulations. Fight results and the provisional public ranking rule determine the scenes:

| Ari v Selene | Ari v Crystal | Group A ranks | Ari's next step | Scene key |
|---|---|---|---|---|
| Win | Lose | Crystal 2–0, Ari 1–1, Selene 0–2 | Q2 vs Mara | `GA_DEFAULT` |
| Win | Win | Ari 2–0, Crystal 1–1, Selene 0–2 | Q1 vs Ren | `GA_ARI_WINNER` |
| Lose | Win | Crystal / Ari / Selene all 1–1; **provisional seed ranks Crystal, Ari, Selene** | Q2 vs Mara | `GA_CYCLE` |
| Lose | Lose | Crystal 2–0, Selene 1–1, Ari 0–2 | Eliminated; Selene Q2 vs Mara | `GA_OUT` |

**[GA_CYCLE — replace Ch2 post-Crystal-win standings and Ch3 draw.]**

Crystal's Jaguar strikes the ground. Ari's Thorn is still standing. For a moment Ari can only hear his own breathing.

**SHIRRO:** SOLANO BEATS CRYSTAL DEVROE!

**ALEX:** Then Ari wins Group A?

**LEENA:** No. Selene beat Ari; Crystal beat Selene. That's one victory each. By the provisional published circular-record seed, Crystal is first, Ari second, Selene third.

The result appears on screen, with a visible **PROVISIONAL RANKING POLICY** caption. Ari looks at Crystal.

**ARI:** I beat you. And you're above me.

**CRYSTAL:** You beat me in a fight. That happened. The table tells a different story.

**ARI:** You like the rule?

**CRYSTAL:** I like it being announced before anyone loses. I don't like pretending it measures more than it does.

Selene arrives at the exit, disappointed but composed.

**SELENE:** I beat the man who beat the champion. I still go home.

**ARI:** It isn't much of a consolation.

**SELENE:** No. But it makes a good headline.

Ari and Crystal exchange the Ganymede-records contact details as in the default branch, without treating Crystal's defeat as a bar to her cooperation.

**[GA_OUT — replace Ch2 post-fight and the qualifying announcement.]**

Crystal wins cleanly. Ari does not argue with the result. He stares at the screen: **CRYSTAL 2–0 / SELENE 1–1 / ARI 0–2**.

**SHIRRO:** GROUP A'S QUALIFIERS ARE CRYSTAL DEVROE AND SELENE VALE!

**ARI:** No quarterfinal. No trophy. Not even a chance to fight Mara.

Crystal meets him in the corridor.

**CRYSTAL:** Your counter was better this time.

**ARI:** Still lost.

**CRYSTAL:** Yes. I'm not going to tell you that doesn't matter.

**ARI:** I came here so somebody would hear Ganymede's story. I thought they would only listen if I won.

**CRYSTAL:** Then make them listen to the records. You know where to find me.

**[CHOICE]** Ari accepts help from Crystal and Christian, gives Leena an independently authenticated document, or requests a technical briefing from Angel. Every option leads to real corroborating evidence; none uses intimacy as currency. He remains a registered pilot and an investigation witness even if he cannot enter knockout matches.

**[GA_ARI_WINNER]** Existing Crystal-loss dialogue and the Ari–Ren draw apply, but retain only if Ari beat **both** Selene and Crystal. **[GA_DEFAULT]** Existing default qualifying recap applies only to Ari-win Selene / Ari-loss Crystal.

## A3. Day 8: Draw broadcast and relational aftermath (`ARI_DRAW_DISPATCH`)

Four broadcast plates, never an invented fight: 

- `GA_DEFAULT`: Crystal–Ren (`Q1`), Ari–Mara (`Q2`).
- `GA_ARI_WINNER`: Ari–Ren (`Q1`), Crystal–Mara (`Q2`).
- `GA_CYCLE`: Crystal–Ren (`Q1`), Ari–Mara (`Q2`); comment that seed, **not** Ari's loss to Crystal, set this order.
- `GA_OUT`: Crystal–Ren (`Q1`), Selene–Mara (`Q2`); Ari is **not** a quarterfinalist.

**[GA_OUT — INT. MARA'S QUARTERS]**

The draw graphic darkens and resolves into two brackets. Mara is looking at Selene's portrait when Ari enters.

**MARA:** You still want to come to my corner?

**ARI:** I'd rather be on the other side of the arena.

**MARA:** I know.

**ARI:** I'm disappointed. I'm not going to make you apologize for advancing.

**MARA:** Good. Because I didn't ask to be spared.

She sets down her training notes.

**MARA:** What are you doing tomorrow?

**ARI:** Checking the procurement ledger Christian found. There's an old hazard waiver with my colony's name on it. I need a second copy before WAR notices.

**MARA:** Then we both have work.

**[IF reciprocal Ari–Mara romance]** Mara kisses Ari, then moves away to finish her training. **[IF friendship]** She squeezes his shoulder. **[IF distant or committed to Leena later]** They trade a respectful goodbye. No path makes Mara responsible for fixing Ari's defeat, and her financial pressures do not disappear.

## A4. Days 8–10: Ari eliminated in group, still playable (`ARI_GROUP_OUT_INVESTIGATION`)

**[NEW Ch4 Scene 5C; replaces a playable quarterfinal when `GA_OUT`.]**

**INT. ANNIVERSARY COMPLEX — INDEPENDENT ARCHIVE ROOM — DAY 9**

The official announcer introduces **Crystal versus Ren**; the next screen lists **Selene versus Mara**. Ari watches the verified names, then turns away before the broadcast cuts to the fight. The result feeds from the authoritative match ledger and is never attributed to him.

Christian arrives carrying a sealed evidence cartridge.

**CHRISTIAN:** You missed an excellent first round.

**ARI:** I noticed the part where I wasn't in it.

**CHRISTIAN:** Good. Then you'll notice this. The same Ganymede hold order was copied into three different departmental systems. Each carries a different approval timestamp.

**ARI:** That's impossible without an override.

**CHRISTIAN:** Or somebody laundering the same instruction through departments. I don't know which yet.

**[INVESTIGATION CHOICE — player selects one action; all available without romance]**

1. **Independent chain of custody.** Ari works with Leena's editor to hash and split the evidence among independent holders; his public-facing comments remain separated from her report.
2. **Technical verification.** Ari asks Plug to compare revision histories while Angel examines a legacy security token. Plug's professional cooperation does not imply dating Mara or Ari.
3. **Witness protection.** Ari contacts a Ganymede worker before publication and obtains informed permission to use a redacted statement. No involuntary public identification.

Each choice gives one texture and one corroborating source. The common investigation later finds a current anonymous biological sample that Ibrahim can link to Kreissack; it **does not yet reveal** Nova's hidden veto. Ari remains a credentialed former competitor, able to help the safety team during a later emergency, but never gains a post-elimination official fight.

**EXT. ARENA VIEWING TERRACE — NIGHT**

Ari watches Mara's match replay only if the player chooses. She may have won or lost; use the recorded result. He records a private message.

**ARI:** I don't know whether anyone will care about the files. I know I was wrong about the easiest way to make them care.

He deletes a self-pitying second sentence and sends the evidence confirmation instead. The arc advances without a trophy.

## A5. Days 8–10: Quarterfinal loss branch (`ARI_QF_LOSS`)

**[IF Ari qualified but loses Q1 vs Ren or Q2 vs Mara.]**

Ari's HAR powers down inside the arena; his opponent receives an unambiguous victory announcement. If Ren won, Ren asks for access to Ari's interface logs; if Mara won, their existing no-thrown-fight dialogue plays with correct romantic/friendship variant. Neither decision changes the result. Ari makes an independent choice about whether to secure evidence, take a medical evaluation, or spend the afternoon verifying worker testimony. The same nonromantic investigative hub is available as in A4, with a shorter setup because Ari already met Crystal and Angel.

**Optional reflective encounter — Selene:**

**SELENE:** I see you're now a retired quarterfinalist.

**ARI:** Temporarily unemployed, more like.

**SELENE:** I could recommend a sponsor. You wouldn't like the conditions.

**ARI:** Then why mention it?

**SELENE:** To see whether you're still reading the small print.

**ARI:** Every line.

She nods once. It is ambiguous whether she approves or is looking for leverage. The exchange may increase mutual respect; it does not make a romance or deal automatically available.

## A6. Day 11: Legitimate first semifinal (`ARI_SEMIFINAL_DISPATCH`)

`S_AB` is held **before** the Day-12 coolant-wing accident. Its combatants come from actual `Q1` and `Q2` winners—not a screenplay-expected rematch.

- **If Ari is in `S_AB` against Crystal:** Keep the existing rematch only if they actually fought in the group. Crystal's line about beating Ari in qualification is **suppressed** if Ari beat her; replace with: **CRYSTAL:** We each know what it means to lose to the other. **ARI:** Today only one of us has to.
- **If Ari is in `S_AB` against Mara:** Play their rivalry scene, including a fair result and separately gated romance/friendship gestures.
- **If Ari is in `S_AB` against Ren or another ledger-verified survivor:** Open with Ren comparing diagnostic timing with Ari. **REN:** I want this test to have an answer. **ARI:** I'm here for a fight, not an experiment. **REN:** It can be both, if we keep the consent separate. No hidden motor-control penalties.
- **If Ari has been eliminated:** `S_AB` plays as an NPC fight with its *actual* finalists and winner. Ari is in the broadcast room or archive, not inside a semifinal HAR. The winning finalist proceeds to Day 13 regardless of the player's romantic state.

**[IF ARI LOSES S_AB]**

The winner waves from the platform. Ari watches the victory screen without flinching this time.

**ARI:** I wanted to win more than I knew.

**CHRISTIAN:** And now?

**ARI:** Now I have less reason to hold the evidence until after the prize ceremony.

Christian looks uneasy.

**CHRISTIAN:** Don't publish it until the source is protected.

**ARI:** Then protect the source. I'll do the rest.

**[IF ARI WINS S_AB]** Ari's victory is played, then he receives a properly populated invitation to the *actual* final (normally against Lyra). He is not declared champion yet.

## A7. Day 12–13: Championship independent of Ari (`ARI_FINAL_DISPATCH`)

**[REPLACE Ch6 Scenes 3–4 entirely with the conditional championship text in the revised chapter.]**

The opening broadcast shows **the two real finalists**, sourced from `S_AB` and `S_CD`. The final is a playable Ari fight *only if Ari actually reached it*; otherwise the match is an NPC broadcast, using an independently resolved winner from the same tournament ledger. The default opponent on the C/D side is Lyra, but another C/D finalist can be supplied by explicitly authored future NPC results. The current fallback priority is a noncanonical test placeholder.

**[ARI REACHES FINAL; ARI WINS]** Ari receives the trophy and may choose a public Ganymede statement, a brief statement with documentation, or to defer comment until witnesses are safe. Crystal's previous-champion presentation is permissible; Mara's celebration depends on her relationship state, not a forced embrace.

**[ARI REACHES FINAL; ARI LOSES]**

The other finalist's HAR holds the field. Ari lowers Thorn's damaged arms and accepts the result.

**SHIRRO:** THE CHAMPION OF ONE MUST FALL 2107 IS **[FINAL_WINNER]**!

The other pilot approaches during the awards setup.

**ARI:** Good fight.

**[FINAL_WINNER]:** It was. You made me earn it.

Ari watches the trophy go to someone else. Mara may congratulate him on reaching the final, or give him space; Leena does not become his consolation prize. The independent Ganymede evidence remains available, and Ari can still speak publicly without claiming the champion's podium.

**[ARI ELIMINATED BEFORE FINAL]**

**INT. BROADCAST GALLERY**

Ari and Christian watch the matchup announcement. The presenters announce two competitors who are **not** Ari. Ari acknowledges the sport as separate from his politics.

**ARI:** I thought I had to win to make anything change.

**CHRISTIAN:** You still have to make people believe you. Winning would've helped. It would never have been enough.

The official champion receives the prize. Ari may watch the ceremony, continue in the archive, or speak with Mara, depending on the available scene clock. He receives no trophy, no prize money, and no winner's interview.

## A8. Day 13: Crisis access for a former competitor (`ARI_NOVA_ACCESS`)

**[Shared route independent of bracket result; after actual official final only.]**

An evacuation order seals the public arena. The demonstration wing has an adjacent maintenance passage cleared by facility safety officers. Ari has already helped preserve the Ganymede documentation and, by choice or fallback, is known to Crystal and Angel as a competent former contestant. Angel holds a validated emergency safety-access token; Plug has a inspected, powered-down HAR service cradle. The site commander authorizes one trained pilot to enter the shielded test arena because the existing defensive platform is misidentifying automated responders. The **player's Ari** is selected only after he affirms consent, passes a quick medical/safety check (extra restrictions for neurological symptoms), and a trained technician confirms the HAR is operational. This is an emergency defensive action against Nova, *not* a fresh tournament bracket match.

**ANGEL:** We don't need you to win another tournament. We need somebody who can keep that platform away from the evacuation corridor for ninety seconds.

**ARI:** You're asking me to go back in after what happened?

**PLUG:** No. We're asking whether you can. There's a difference.

**[OPTIONAL CHOICE]** Ari accepts immediately, demands independent safety oversight first, or requests a safer alternate HAR configuration. The crisis persists but the cutscene accounts for the decision; the game cannot quietly force a medically unsafe interface. If Ari is temporarily unfit for neural commands, he uses standard manual control with safety supervision, not a miraculous recovery or coercive brain connection.

The Nova boss fight and Kreissack containment intervention retain the existing story's order. No player victory over Nova retroactively creates a championship title.

## A9. Weeks later: Consequence-responsive epilogue (`ARI_EPILOGUE_DISPATCH`)

Four illustrative closures with the shared Ganymede and Nova fallout intact:

**Champion + romance:** In a transit-station café, Mara examines the giant championship trophy's shipping label and insists she will not move her mother's treatment funds into Ari's trophy tour. Ari promises only what he can actually deliver. Their trust score, not his championship, determines whether the relationship is stable.

**Runner-up or earlier eliminated + romance:** Ari and Mara compare the cost of transit tickets and a more modest investigative schedule. Ari confesses he thought Mara would respect him less for losing. **MARA:** I respect how you fight and what you do when people are watching. Not a number on a screen. No financial rescue is guaranteed.

**Leena route (post-recusal only):** Ari meets Leena after her coverage transfer and after reciprocal intentions have been established, with a clear choice to date or remain friends. His bracket result is a conversation topic, not a gate. There is no on-duty journalist intimacy bargain for evidence.

**Friendship/solo:** Ari leads a workers' testimony review while Crystal and Christian coordinate verification. Mara may visit as a friend or professional ally. He sees an archival Ganymede photo beside a tournament poster. **ARI:** Losing was information. Giving up would have been a choice.

The legal inquiry is ongoing; the villain's defeat is not automatic corporate reform, total medical recovery, or universal compensation.
