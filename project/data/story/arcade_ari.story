# ARCADE LADDER (vertical slice): Ari's arcade-mode run as a ladder of six rungs, each a short beat then a match.
# After every win comes a NEWS REPORT (Alex and Leena on the result) and then HANGAR MAINTENANCE (Plug and the crew
# repair the HAR; the player picks a tune-up). Both are required parts of the arcade loop, not optional scenes.
# PLACEHOLDER dialogue (Plug and Ari show with their portraits in the hangar): a few lines per beat, to prove the ladder mechanics. The real arcade cut waits for the
# Gate A / Gate B read-through (Arcade_and_Cinematic_Production_Plan_v2.6.md) and will be driven by ari.tiers.
# Rules: a loss offers a rematch of the same rung (flag `rung`); the Nova boss is two fights (flag `nova_round`);
# winning the second Nova fight ends the run. `lives` is reserved for counting rematches (not used yet).
# Flags: rung is the rung being fought; beaten, beaten_har and next_opponent feed the news report (art: news_<player har>_<beaten har>, then Leena in the pit lane);
# the hangar shows the player's HAR (art: maintenance_<har>, both from project/tools/build_story_art.py);
# tune is the hangar pick (armor, power or speed) and changes the player's HAR in the fights that follow, until the next
# pick: armor +25% health, power +20% damage dealt, speed +15% walking speed (see story_match_start in main.c).
# Check it with:  build/omf_debug_z7/story_check.exe check project/data/story/arcade_ari.story

player Ari Jaguar
rival Selene
card Ari: The Ganymede rebel, fighting his way up the 2107 tournament ladder.
card Selene: The private entrant and first obstacle.
blurb Six fights from the opening round to the champion's machine. After each win: the news report, then the hangar.
opponents Selene, Crystal, Mara, Ren, Lyra, Nova

scene intro
music menu
say : ARCADE. Six opponents stand between Ari and the truth about Ganymede.
set rung=0
set lives=0
set tune=none
jump rung1

scene rung1
set rung=1
music arena0
art ari_ch1_arena_main fade
say : Round 1. Selene Vale.
present ari left Ari Solano
present selene right Selene Vale
say Selene: Ari Solano. I expected someone taller.
say Ari: I expected someone less interested in appearances.
say Selene: Appearances are rather important in this business.
say Ari: I'm here to win.
say Selene: Of course. Let's see what you're made of.
fight Ari @player_har vs Selene Shadow win -> won1 lose -> retry difficulty 1

scene won1
set beaten=Selene Vale
set beaten_har=Shadow
set next_opponent=Crystal Devroe, the Nova-slayer
jump news

scene rung2
set rung=2
music arena1
art ari_ch1_arena_main fade
say : Round 2. Crystal Devroe, the Nova-slayer.
present ari left Ari Solano
present crystal right Crystal Devroe
say Crystal: You beat Selene cleanly. I was watching.
say Ari: You're the one who brought Nova down. I need to know what you saw in that arena.
say Crystal: More than I ever told anyone.
say Ari: Then win, and maybe you'll tell me.
say Crystal: Show me what Ganymede taught you.
fight Ari @player_har vs Crystal Katana win -> won2 lose -> retry difficulty 2

scene won2
set beaten=Crystal Devroe
set beaten_har=Katana
set next_opponent=Mara Voss
jump news

scene rung3
set rung=3
music arena2
art ari_ch1_arena_main fade
say : Round 3. Mara.
present ari left Ari Solano
present mara right Mara Voss
say Mara: You fixed your own actuators last night. Plug told me.
say Ari: Somebody has to. Not all of us have a pit crew that likes us.
say Mara: Don't confuse liking you with going easy on you.
say Ari: Wouldn't dream of it.
say Mara: No hard feelings. Not yet.
fight Ari @player_har vs Mara Jaguar win -> won3 lose -> retry difficulty 3

scene won3
set beaten=Mara Voss
set beaten_har=Jaguar
set next_opponent=Ren Akiyama
jump news

scene rung4
set rung=4
music arena3
art ari_ch1_arena_main fade
say : Round 4. Ren.
present ari left Ari Solano
present ren right Ren Akiyama
say Ren: Three wins in a row. The league is starting to say your name.
say Ari: I'd rather they said what happened on Ganymede.
say Ren: Perhaps they will, if you earn the right to be heard.
say Ari: That's what these fights are for.
say Ren: Then I will not hold back.
fight Ari @player_har vs Ren Shadow win -> won4 lose -> retry difficulty 4

scene won4
set beaten=Ren Akiyama
set beaten_har=Shadow
set next_opponent=Lyra
jump news

scene rung5
set rung=5
music arena4
art ari_ch1_arena_main fade
say : Round 5. Lyra.
present ari left Ari Solano
present lyra right Lyra Kisaragi
say Lyra: Everyone has a story about you now. The rebel from Ganymede.
say Ari: Everyone has a story. I just have the evidence.
say Lyra: Evidence doesn't fill a stadium. A good fight does.
say Ari: Then let's give them one.
say Lyra: The crowd wants a finale. I intend to give them one.
fight Ari @player_har vs Lyra Katana win -> won5 lose -> retry difficulty 5

scene won5
set beaten=Lyra
set beaten_har=Katana
set next_opponent=Nova, the champion's machine
jump news

scene nova1
set rung=6
set nova_round=1
music arena4
art ari_ch1_arena_main fade
say : The champion's machine. Nova, round one.
present ari left Ari Solano
present kreissack right Major Kreissack
say Kreissack: Ten years, and you walk into my arena as if you'd earned it.
say Ari: Major. You were supposed to be dead.
say Kreissack: Supposed. A fine word. Nova doesn't care what anyone supposed.
say Ari: Then I'll end it where it started.
fight Ari @player_har vs Nova Jaguar win -> won6 lose -> retry difficulty 5

scene won6
set beaten=Nova's first form
set beaten_har=Jaguar
set next_opponent=Nova's second form
jump news

scene nova2
set rung=7
set nova_round=2
art ari_ch1_arena_main fade
flash
say : Nova's capsule hisses. The machine rises again.
present ari left Ari Solano
present kreissack right Major Kreissack
say Kreissack: You've damaged it. Good. It learns from damage.
say Ari: Not this time.
say Kreissack: Then show me.
fight Ari @player_har vs Nova Shadow win -> victory lose -> retry difficulty 6

# The news report after every win. {beaten} is the pilot just defeated.
scene news
music menu
present off
art news_{player_har}_{beaten_har} fade
banner WRDE NEWS
say Alex: Good evening from the tournament. Ari Solano's {player_har} defeated {beaten} in the Stadium tonight.
say Alex: The replay says it all. Solano advances, and the ladder grows steeper.
say Alex: Next up, Solano meets {next_opponent}. Let's go to the pit lane, where Leena Sato has caught up with him.
art ari_ch1_arena_main fade
present ari left Ari Solano
present leena right Leena Sato
say Leena: Ari, you've just beaten {beaten}. Was that the fight you planned?
say Ari: There's no plan. There's the next match.
say Leena: And the next one is {next_opponent}. Nervous?
say Ari: Ask me after the hangar crew has finished with my machine.
say Leena: Back to you in the studio, Alex.
present off
art off
jump hangar

# Hangar maintenance after the news: the crew repairs the HAR, then the player picks a tune-up.
scene hangar
bg hangar workshop
art maintenance_{player_har} fade
say : The hangar. Steam, sparks and the smell of hot metal. {player_har} stands in the repair cradle, plating scorched.
present plug left Plug McEllis
say Plug: Welding the arm now. Hold still, big guy. Not you, Ari. The HAR.
say Ari: How bad is it?
say Plug: Nothing I can't fix before the next match. Pick what to tune while I have it open.
choice Reinforce the armor -> next set tune=armor
choice Boost the power output -> next set tune=power
choice Tighten the actuators for speed -> next set tune=speed

# After the hangar, on to the next rung.
scene next
say Plug: Done. Go and win.
present off
art off
if rung=1 -> rung2
if rung=2 -> rung3
if rung=3 -> rung4
if rung=4 -> rung5
if rung=5 -> nova1
if rung=6 -> nova2
jump gameover

scene retry
music menu
present off
say : Ari goes down. The ladder holds your place.
choice Rematch -> rematch
choice Give up -> gameover

scene rematch
if rung=1 -> rung1
if rung=2 -> rung2
if rung=3 -> rung3
if rung=4 -> rung4
if rung=5 -> rung5
if rung=6 -> nova1
if rung=7 -> nova2
jump gameover

scene victory
music end
present off
banner CHAMPION
say : Nova falls. The arena is silent, then it is not.
say : Ari raises his head. Ganymede will get its answer.
end

scene gameover
music end
say : The run ends here.
end
