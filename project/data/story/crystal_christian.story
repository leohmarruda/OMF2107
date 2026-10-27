# DRAFT first story slice: Crystal Devroe versus Christian Devroe.
# Built only from project/docs/OMF20115_SIMPLE_LORE.md. The wording is placeholder dialogue for testing the
# runner and the flow of the slice, not final writing. Check it with:
#   build/omf_debug_z7/story_check.exe check project/data/story/crystal_christian.story

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
say : The siblings take their HARs. Crystal in Jaguar. Christian in Shadow.
say Christian: Do not hold back on my account.
say Crystal: I never do.
fight Crystal Jaguar vs Christian Shadow win -> won lose -> lost

scene won
set result=won
say : Jaguar stands over a fallen Shadow. Crystal's hands will not stop shaking.
jump recovery

scene lost
set result=lost
say : Shadow takes the match. Christian does not celebrate. He is looking at his sister's hands.
jump recovery

scene recovery
bg medical bay
say : In the corridor a message waits on Crystal's datapad: leaked Tier-2 medical telemetry, showing what the deep-link does to pilots.
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
if tremors=told -> closing_trust
say : They leave the building apart. Neither has said what they are afraid of.
end

scene closing_trust
say : They leave the building together. For the first time in five years Christian does not walk ahead.
end
