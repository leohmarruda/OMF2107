# DRAFT first story slice, Christian's route: Christian Devroe versus Crystal Devroe.
# The same evening as crystal_christian.story, told from the other sibling's side. Built only from
# project/docs/OMF2107_SIMPLE_LORE.md. The wording is placeholder dialogue for testing the runner and the flow of the
# slice, not final writing. Check it with:
#   build/omf_debug_z7/story_check.exe check project/data/story/christian_crystal.story
#
# Flags: symptoms (told or hidden) is set before the match; result (won or lost, from Christian's side) is set by the
# match; evidence (fixer, released, or crystal) is set by the choice after it.
# The result decides who WAR's Tier-2 offer goes to, which recovery scene plays, and how the story closes.
# The HARs come from the selection screen: {player_har} and {rival_har} are filled in, and the fight reads them
# with @player_har and @rival_har. The player is Christian; the story recommends Shadow but any pairing works.
# The route line lets the selection screen switch to Crystal's script and back.

player Christian Shadow
rival Crystal
route Crystal crystal_christian.story
card Crystal: The Seeker. Composed and camera-ready, the pilot who handles pressure. She wants proof of her parents' fate.
card Christian: The Shield. Aggressive and outwardly confident. He wants revenge, and he wants Crystal kept alive.

# The illustrated opening: four frames from project/build/art with captions. The faceoff frame is named after the
# player's HAR, so it shows the pairing that was chosen.
scene intro
music menu
art stadium_title fade
say : WAR presents the Ganymede tournament. Ten pilots, linked to giant HARs, in front of the cameras.
art christian_card zoom
say : Christian Devroe, 23. The Shield.
art crystal_card zoom
say : Crystal Devroe, 23. The Seeker.
flash
art faceoff_{player_har} fade
say : Tonight the draw puts one against the other.
art off
jump start

scene start
bg green room
say : Backstage at WAR's televised Ganymede tournament. The draw has set the Devroe siblings against each other.
say Crystal: Your hands are cold. And you have not blinked in a minute.
say Christian: Pre-match nerves. Everyone has them.
say Crystal: You do not have nerves. You have bravado, and something in your pocket.
say : For five years Christian has kept his suspicions about their parents to himself. His head has been pounding since morning.
choice Admit the headaches and the stimulants -> symptoms_told set symptoms=told
choice Wave it off with a joke -> symptoms_hidden set symptoms=hidden

scene symptoms_told
say Christian: Headaches since the last link. I take something to get through them.
say Crystal: Then we stop pretending, you and I. Whatever happens out there.
jump hangar

scene symptoms_hidden
say Christian: I am the Shield. Nothing gets past me, remember?
say Crystal: That is exactly what worries me.
jump hangar

# The hangar bay before the match: the original VS-screen hangar with the two chosen HARs, named after the pilot and HAR.
scene hangar
art bay_{player_pilot}_{player_har} fade
say : In the hangar bay the crews run the last checks. {player_har} waits on the left and {rival_har} on the right, and the deep-link cradles are warming.
jump prefight

scene prefight
music arena0
bg stadium
say : The siblings take their HARs. Christian in {player_har}. Crystal in {rival_har}.
say Crystal: Do not hold back on my account.
say Christian: I never do.
fight Christian @player_har vs Crystal @rival_har win -> won lose -> lost

scene won
set result=won
art off
say : {player_har} stands over a fallen {rival_har}. The crowd roars. Christian's head is pounding, and he counts it as proof that he won.
say Crystal: You won. Now tell me you can still feel your hands.
jump news_won

scene lost
set result=lost
art off
say : {rival_har} takes the match. Crystal does not smile. She is watching the pulse in her brother's neck.
say Crystal: You were slow on the last exchange. Why?
jump news_lost

# The newscast after the match: the original newsroom frame with the winner on the news screen.
scene news_won
music menu
art news_christian fade
banner WRDE NEWS
say Alex: Good evening from the Ganymede tournament. Christian Devroe takes the Stadium bout against his sister Crystal.
say Alex: Fierce as ever, say the commentators. WAR reports that both pilots' readings were within tournament limits.
art wreck_{player_har}_{result} fade
say : In the repair bay the crews haul the battered machines in. Scorched plating, cracked ribs, a smell of burnt coolant. Neither HAR fights again without an overhaul.
art off
jump recovery

scene news_lost
music menu
art news_crystal fade
banner WRDE NEWS
say Alex: Good evening from the Ganymede tournament. Crystal Devroe takes the Stadium bout against her brother Christian.
say Alex: A measured performance, say the commentators. WAR reports that both pilots' readings were within tournament limits.
art wreck_{player_har}_{result} fade
say : In the repair bay the crews haul the battered machines in. Scorched plating, cracked ribs, a smell of burnt coolant. Neither HAR fights again without an overhaul.
art off
jump recovery

scene recovery
music menu
bg medical bay
banner TIER-2
if result=won -> recovery_won
say : The winner's reward arrives on Crystal's datapad: an invitation to WAR's Tier-2 program, framed as a promotion.
say Christian: A promotion. That is what they call it.
say Crystal: I did not ask for it. And I am not sure I can say no.
jump evidence

scene recovery_won
bg medical bay
say : In the corridor Dr. Varga finds Christian and calls his readings exceptional. A Tier-2 invitation follows, framed as a promotion.
say Christian: Exceptional. My head has been pounding all day.
say Crystal: Do not take it. Please.
jump evidence

scene evidence
flash
say : Later, two messages reach Christian's datapad. The first is leaked Tier-2 medical telemetry, showing what the deep-link does to pilots. The second is from his fixer: a name, a place, a time.
say Christian: Five years. And now I have a place to put it.
say Crystal: Whatever you are thinking, say it to me first.
choice Take it to the fixer -> fixer set evidence=fixer
choice Release it to the broadcast now -> released set evidence=released
choice Hand it to Crystal to verify -> crystal_verifies set evidence=crystal

scene fixer
say : Christian meets the fixer and asks about the facility. The fixer already knows when Crystal's next match is, down to the hour.
say Christian: How do you know that?
say : Every answer Christian paid for was a piece of his sister's schedule going out the other way.
say Christian: This ends tonight.
jump closing

scene released
say : The telemetry reaches the broadcast. Viewers demand public oversight of the tournament.
say Christian: Better the whole world sees it than I carry it alone.
say Crystal: I would have checked every line first. But I understand.
jump closing

scene crystal_verifies
say : Christian hands the files to Crystal. She starts checking them line by line. It will take time, and WAR may notice.
say Christian: Time is what we do not have.
say Crystal: Then we use it carefully. Together.
jump closing

scene closing
if result=won -> closing_won
say : Crystal keeps the Tier-2 invitation on her datapad. WAR will expect an answer.
jump closing_end

scene closing_won
say : Christian keeps the Tier-2 invitation in his pocket. He has not decided what to do with it, and the headaches have not stopped.
jump closing_end

scene closing_end
if symptoms=told -> closing_trust
say : They leave the building apart. Neither has said what they are afraid of.
jump ending

scene closing_trust
say : They leave the building together. For the first time in five years Christian does not walk ahead.
jump ending

# The endings: one for each sibling, shaped by the evidence choice, then a closing frame shaped by the symptoms.
scene ending
music end
banner CHRISTIAN
art ending_christian fade
if evidence=released -> ending_christian_released
if evidence=crystal -> ending_christian_crystal
say : Christian cut the fixer off. The facility is out of his hands, but he has to answer for every piece of his sister's schedule he gave away.
jump ending_crystal

scene ending_christian_released
say : Christian released the telemetry before anyone could verify it. Public oversight of the tournament follows, and so does the question of whether he shared it to help or to hurt.
jump ending_crystal

scene ending_christian_crystal
say : Christian handed the evidence to his sister instead of acting on it. Learning to wait is harder than any match.
jump ending_crystal

scene ending_crystal
banner CRYSTAL
art ending_crystal fade
if evidence=released -> ending_crystal_released
if evidence=crystal -> ending_crystal_verified
say : Crystal learned that her schedule had been leaking for months. She forgave her brother slowly, and the files are still unverified.
jump ending_close

scene ending_crystal_released
say : Crystal found the telemetry already public. She checks it line by line anyway, and most of it holds.
jump ending_close

scene ending_crystal_verified
say : Crystal checked every line and demanded independent reform. WAR knows her name now, and her brother stood beside her.
jump ending_close

scene ending_close
if symptoms=told -> ending_together
art ending_apart fade
say : The siblings face what comes next apart, each holding a secret.
jump ending_last

scene ending_together
art ending_together fade
say : The siblings face what comes next together.
jump ending_last

scene ending_last
flash
art ending_title fade
say : End of the first slice.
end
