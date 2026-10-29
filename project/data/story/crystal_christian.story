# DRAFT first story slice: Crystal Devroe versus Christian Devroe.
# Built only from project/docs/OMF20115_SIMPLE_LORE.md. The wording is placeholder dialogue for testing the
# runner and the flow of the slice, not final writing. Check it with:
#   build/omf_debug_z7/story_check.exe check project/data/story/crystal_christian.story
#
# Flags: tremors (told or hidden) is set before the match; result (won or lost, from Crystal's side) is set
# by the match; evidence (released, verified, or christian) is set by the choice after it.
# The result decides who WAR's Tier-2 offer goes to, which recovery scene plays, and how the story closes.
# The HARs come from the selection screen: {player_har} and {rival_har} are filled in, and the fight reads them
# with @player_har and @rival_har. The player is Crystal; the story recommends Jaguar but any pairing works.

player Crystal Jaguar
rival Christian
card Crystal: The Seeker. Composed and camera-ready, the pilot who handles pressure. She wants proof of her parents' fate.
card Christian: The Shield. Aggressive and outwardly confident. He wants revenge, and he wants Crystal kept alive.

# Presentation beats: flash (a quick white flash) and banner <text> (a big banner) do not wait; they sit just before
# the line they punctuate. Banner text is shown in capitals.
# The illustrated opening: four frames from project/build/art (built by export_story_assets.py) with captions.
# The faceoff frame is named after the player's HAR, so it shows the pairing that was chosen.
scene intro
art stadium_title fade
say : WAR presents the Ganymede tournament. Ten pilots, linked to giant HARs, in front of the cameras.
art crystal_card zoom
say : Crystal Devroe, 23. The Seeker.
art christian_card zoom
say : Christian Devroe, 23. The Shield.
flash
art faceoff_{player_har} fade
say : Tonight the draw puts one against the other.
art off
jump start

scene start
bg green room
say : Backstage at WAR's televised Ganymede tournament. The draw has set the Devroe siblings against each other.
say Christian: You are holding your wrist again.
say Crystal: It is nothing. Nerves.
say Christian: Five years I have watched you hide things well. This is not nerves.
choice Tell him about the tremors -> tremors_told set tremors=told
choice Keep the nerves excuse -> tremors_hidden set tremors=hidden

scene tremors_told
say Crystal: My hands shake after every link. I have been covering it.
say Christian: Then we do not ignore it. Whatever happens out there.
jump prefight

scene tremors_hidden
say Crystal: Nerves. I handle pressure. Everyone says so.
say Christian: Fine. But I am watching you.
jump prefight

scene prefight
bg stadium
say : The siblings take their HARs. Crystal in {player_har}. Christian in {rival_har}.
say Christian: Do not hold back on my account.
say Crystal: I never do.
fight Crystal @player_har vs Christian @rival_har win -> won lose -> lost

scene won
set result=won
say : {player_har} stands over a fallen {rival_har}. The crowd roars. Crystal's hands will not stop shaking.
say Christian: You did not hold back. Good.
jump recovery

scene lost
set result=lost
say : {rival_har} takes the match. Christian does not celebrate. He is looking at his sister's hands.
say Christian: Did you let me win? Or could you not hold the stick?
jump recovery

scene recovery
bg medical bay
banner TIER-2
if result=won -> recovery_won
say : In the corridor Dr. Varga finds Christian and calls his readings exceptional. A Tier-2 invitation follows, framed as a promotion.
say Christian: Exceptional. My head has been pounding all day.
say Crystal: Do not take it. Please.
jump evidence

scene recovery_won
bg medical bay
say : The winner's reward arrives on Crystal's datapad: an invitation to WAR's Tier-2 program, framed as a promotion.
say Crystal: A promotion. That is what they call it.
say Christian: You won. They will not take no easily.
jump evidence

scene evidence
flash
say : Later, a second message reaches Crystal's datapad: leaked Tier-2 medical telemetry, showing what the deep-link does to pilots.
say Crystal: This is proof. Or it is bait.
say Christian: Release it. Burn the whole thing down.
say Crystal: Unverified evidence can hurt the wrong people.
choice Release it to the broadcast now -> released set evidence=released
choice Verify it first -> verified set evidence=verified
choice Give it to Christian -> given set evidence=christian

scene released
say : The telemetry reaches the broadcast. Viewers demand public oversight of the tournament.
say Crystal: I should have checked every line first.
jump closing

scene verified
say : Crystal takes the files to be checked. It will take time, and WAR may notice.
say Christian: Time is what we do not have.
jump closing

scene given
say : Christian reads the files twice. His jaw sets.
say Christian: There is a WAR facility I could reach. Say the word.
say Crystal: No. Not civilians. Not like this.
jump closing

scene closing
if result=won -> closing_won
say : Christian keeps the Tier-2 invitation in his pocket. He has not decided what to do with it.
jump closing_end

scene closing_won
say : Crystal keeps the Tier-2 invitation on her datapad. WAR will expect an answer, and she has already tried the Nova code once.
jump closing_end

scene closing_end
if tremors=told -> closing_trust
say : They leave the building apart. Neither has said what they are afraid of.
jump ending

scene closing_trust
say : They leave the building together. For the first time in five years Christian does not walk ahead.
jump ending

# The endings: one for each sibling, shaped by the evidence choice, then a closing frame shaped by the tremors.
scene ending
banner CRYSTAL
art ending_crystal fade
if evidence=released -> ending_crystal_released
if evidence=verified -> ending_crystal_verified
say : Crystal kept her brother from the facility. The files are still unverified, and what to do with them is still hers to answer for.
jump ending_christian

scene ending_crystal_released
say : Crystal released the telemetry before she could check it. Public oversight of the tournament follows, and so does the weight of every line she never verified.
jump ending_christian

scene ending_crystal_verified
say : Crystal waited until the files checked out, then demanded independent reform. WAR knows her name now.
jump ending_christian

scene ending_christian
banner CHRISTIAN
art ending_christian fade
if evidence=christian -> ending_christian_given
say : Christian stopped trying to control the fight and started to trust his sister. It is a start.
jump ending_close

scene ending_christian_given
say : Christian put the facility out of his mind, for now. The anger has not gone, but he did not aim it at civilians.
jump ending_close

scene ending_close
if tremors=told -> ending_together
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
