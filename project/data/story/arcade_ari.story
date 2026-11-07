# ARCADE LADDER (vertical slice): Ari's arcade-mode run. Five opponents in a RANDOM order, then the Nova boss (two fights).
# After every win comes a NEWS REPORT (Alex and Leena on the result) and then HANGAR MAINTENANCE (Plug and the crew
# repair the HAR; the player picks a tune-up). Both are required parts of the arcade loop, not optional scenes.
# PLACEHOLDER dialogue (Plug and Ari show with their portraits in the hangar): a few lines per beat, to prove the ladder mechanics. The real arcade cut waits for the
# Gate A / Gate B read-through (Arcade_and_Cinematic_Production_Plan_v2.6.md) and will be driven by ari.tiers.
# Opponent dialogue must not depend on the order (any opponent can be met first, second, and so on).
#
# Flags the viewer sets when the run starts (project/prototype/main.c, story_begin; the `arcade` line below turns this on):
#   shuffled=yes        the run was started by the viewer; if it is missing (story_check) the intro sets defaults
#   at_<opponent>=N     the position (1 to 5) of selene, crystal, mara, ren and lyra in this run's order
#   mode=easy|normal|hard, lives=unlimited|3|0   the difficulty mode picked on the selection screen
# Flags the script keeps:
#   rung                the fight being fought: 1 to 5 for the shuffled opponents, 6 and 7 for Nova's two rounds. The viewer
#                       sets the rival's AI level from it (rung 1 to 5 is level 1 to 5, Nova is 5 then 6), not from the opponent.
#   lives               continues left. A loss with lives left spends one and offers a rematch; at 0 a loss ends the run.
#                       "unlimited" never runs out.
#   tn_armor, tn_power, tn_speed   how many times each hangar tune-up was picked. Repeat picks of one stat give half the
#                       gain of the previous pick (armor +25%, +12.5%, ...; power +20%; speed +15%), see story_match_start in main.c.
#   beaten, beaten_har, next_opponent feed the news report (art: news_<player har>_<beaten har>, then Leena in the pit lane);
#   the hangar shows the player's HAR (art: maintenance_<har>, both from project/tools/build_story_art.py).
# Check it with:  build/omf_debug_z7/story_check.exe check project/data/story/arcade_ari.story

player Ari Jaguar
rival Selene
card Ari: The Ganymede rebel, fighting his way up the 2107 tournament ladder.
card Selene: The private entrant and first obstacle.
blurb Five opponents in a random order, then the champion's machine. After each win: the news report, then the hangar.
opponents Selene, Crystal, Mara, Ren, Lyra, Nova
arcade

scene intro
music menu
say : ARCADE. Five opponents, then Nova. Between Ari and the truth about Ganymede, nobody waits in line.
if shuffled=yes -> start
set mode=easy
set lives=unlimited
set at_selene=1
set at_crystal=2
set at_mara=3
set at_ren=4
set at_lyra=5
jump start

scene start
set rung=0
set tn_armor=0
set tn_power=0
set tn_speed=0
jump pick1

# Which opponent stands at position N: one scene per position, one line per opponent.
scene pick1
set rung=1
if at_selene=1 -> selene
if at_crystal=1 -> crystal
if at_mara=1 -> mara
if at_ren=1 -> ren
if at_lyra=1 -> lyra
jump gameover

scene pick2
set rung=2
if at_selene=2 -> selene
if at_crystal=2 -> crystal
if at_mara=2 -> mara
if at_ren=2 -> ren
if at_lyra=2 -> lyra
jump gameover

scene pick3
set rung=3
if at_selene=3 -> selene
if at_crystal=3 -> crystal
if at_mara=3 -> mara
if at_ren=3 -> ren
if at_lyra=3 -> lyra
jump gameover

scene pick4
set rung=4
if at_selene=4 -> selene
if at_crystal=4 -> crystal
if at_mara=4 -> mara
if at_ren=4 -> ren
if at_lyra=4 -> lyra
jump gameover

scene pick5
set rung=5
if at_selene=5 -> selene
if at_crystal=5 -> crystal
if at_mara=5 -> mara
if at_ren=5 -> ren
if at_lyra=5 -> lyra
jump gameover

scene selene
music arena0
art ari_ch1_arena_main fade
say : Round {rung}. Selene Vale.
present ari left Ari Solano
present selene right Selene Vale
say Selene: Ari Solano. I expected someone taller.
say Ari: I expected someone less interested in appearances.
say Selene: Appearances are rather important in this business.
say Ari: I'm here to win.
say Selene: Of course. Let's see what you're made of.
fight Ari @player_har vs Selene Shadow win -> won_selene lose -> retry difficulty 1

scene won_selene
set beaten=Selene Vale
set beaten_har=Shadow
jump preview

scene crystal
music arena1
art ari_ch1_arena_main fade
say : Round {rung}. Crystal Devroe, the Nova-slayer.
present ari left Ari Solano
present crystal right Crystal Devroe
say Crystal: I've been watching the ladder. You don't waste movement.
say Ari: You're the one who brought Nova down. I need to know what you saw in that arena.
say Crystal: More than I ever told anyone.
say Ari: Then win, and maybe you'll tell me.
say Crystal: Show me what Ganymede taught you.
fight Ari @player_har vs Crystal Katana win -> won_crystal lose -> retry difficulty 2

scene won_crystal
set beaten=Crystal Devroe
set beaten_har=Katana
jump preview

scene mara
music arena2
art ari_ch1_arena_main fade
say : Round {rung}. Mara.
present ari left Ari Solano
present mara right Mara Voss
say Mara: You fixed your own actuators last night. Plug told me.
say Ari: Somebody has to. Not all of us have a pit crew that likes us.
say Mara: Don't confuse liking you with going easy on you.
say Ari: Wouldn't dream of it.
say Mara: No hard feelings. Not yet.
fight Ari @player_har vs Mara Jaguar win -> won_mara lose -> retry difficulty 3

scene won_mara
set beaten=Mara Voss
set beaten_har=Jaguar
jump preview

scene ren
music arena3
art ari_ch1_arena_main fade
say : Round {rung}. Ren.
present ari left Ari Solano
present ren right Ren Akiyama
say Ren: The league is starting to say your name.
say Ari: I'd rather they said what happened on Ganymede.
say Ren: Perhaps they will, if you earn the right to be heard.
say Ari: That's what these fights are for.
say Ren: Then I will not hold back.
fight Ari @player_har vs Ren Shadow win -> won_ren lose -> retry difficulty 4

scene won_ren
set beaten=Ren Akiyama
set beaten_har=Shadow
jump preview

scene lyra
music arena4
art ari_ch1_arena_main fade
say : Round {rung}. Lyra.
present ari left Ari Solano
present lyra right Lyra Kisaragi
say Lyra: Everyone has a story about you now. The rebel from Ganymede.
say Ari: Everyone has a story. I just have the evidence.
say Lyra: Evidence doesn't fill a stadium. A good fight does.
say Ari: Then let's give them one.
say Lyra: The crowd wants a finale. I intend to give them one.
fight Ari @player_har vs Lyra Katana win -> won_lyra lose -> retry difficulty 5

scene won_lyra
set beaten=Lyra
set beaten_har=Katana
jump preview

scene nova1
set rung=6
music arena4
art ari_ch1_arena_main fade
say : The champion's machine. Nova, round one.
present ari left Ari Solano
present kreissack right Major Kreissack
say Kreissack: Ten years, and you walk into my arena as if you'd earned it.
say Ari: Major. You were supposed to be dead.
say Kreissack: Supposed. A fine word. Nova doesn't care what anyone supposed.
say Ari: Then I'll end it where it started.
fight Ari @player_har vs Nova Jaguar win -> won_nova1 lose -> retry difficulty 5

scene won_nova1
set beaten=Nova's first form
set beaten_har=Jaguar
jump preview

scene nova2
set rung=7
art ari_ch1_arena_main fade
flash
say : Nova's capsule hisses. The machine rises again.
present ari left Ari Solano
present kreissack right Major Kreissack
say Kreissack: You've damaged it. Good. It learns from damage.
say Ari: Not this time.
say Kreissack: Then show me.
fight Ari @player_har vs Nova Shadow win -> victory lose -> retry difficulty 6

# Who comes after the fight just won (rung is that fight): the opponent at the next position, or Nova.
scene preview
if rung=1 -> look2
if rung=2 -> look3
if rung=3 -> look4
if rung=4 -> look5
if rung=5 -> look_nova
if rung=6 -> look_nova2
jump news

scene look2
if at_selene=2 -> next_selene
if at_crystal=2 -> next_crystal
if at_mara=2 -> next_mara
if at_ren=2 -> next_ren
if at_lyra=2 -> next_lyra
jump news

scene look3
if at_selene=3 -> next_selene
if at_crystal=3 -> next_crystal
if at_mara=3 -> next_mara
if at_ren=3 -> next_ren
if at_lyra=3 -> next_lyra
jump news

scene look4
if at_selene=4 -> next_selene
if at_crystal=4 -> next_crystal
if at_mara=4 -> next_mara
if at_ren=4 -> next_ren
if at_lyra=4 -> next_lyra
jump news

scene look5
if at_selene=5 -> next_selene
if at_crystal=5 -> next_crystal
if at_mara=5 -> next_mara
if at_ren=5 -> next_ren
if at_lyra=5 -> next_lyra
jump news

scene next_selene
set next_opponent=Selene Vale
jump news

scene next_crystal
set next_opponent=Crystal Devroe, the Nova-slayer
jump news

scene next_mara
set next_opponent=Mara Voss
jump news

scene next_ren
set next_opponent=Ren Akiyama
jump news

scene next_lyra
set next_opponent=Lyra
jump news

scene look_nova
set next_opponent=Nova, the champion's machine
jump news

scene look_nova2
set next_opponent=Nova's second form
jump news

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

# Hangar maintenance after the news: the crew repairs the HAR, then the player picks a tune-up. Picks stack, with
# half the gain each time the same stat is picked again.
scene hangar
bg hangar workshop
art maintenance_{player_har} fade
say : The hangar. Steam, sparks and the smell of hot metal. {player_har} stands in the repair cradle, plating scorched.
present plug left Plug McEllis
say Plug: Welding the arm now. Hold still, big guy. Not you, Ari. The HAR.
say Ari: How bad is it?
say Plug: Nothing I can't fix before the next match. Pick what to tune while I have it open.
choice Reinforce the armor -> tune_armor
choice Boost the power output -> tune_power
choice Tighten the actuators for speed -> tune_speed

scene tune_armor
add tn_armor 1
jump next

scene tune_power
add tn_power 1
jump next

scene tune_speed
add tn_speed 1
jump next

# After the hangar, on to the next fight.
scene next
say Plug: Done. Go and win.
present off
art off
if rung=1 -> pick2
if rung=2 -> pick3
if rung=3 -> pick4
if rung=4 -> pick5
if rung=5 -> nova1
if rung=6 -> nova2
jump gameover

# A loss: with lives left it spends one and offers a rematch of the same fight; at 0 lives the run ends.
scene retry
music menu
present off
if lives=unlimited -> retry_ok
if lives=0 -> retry_over
add lives -1
jump retry_ok

scene retry_ok
say : Ari goes down. The ladder holds your place.
choice Rematch -> rematch
choice Give up -> gameover

scene retry_over
say : Ari goes down, and there are no continues left.
jump gameover

scene rematch
if rung=1 -> pick1
if rung=2 -> pick2
if rung=3 -> pick3
if rung=4 -> pick4
if rung=5 -> pick5
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
say : The run ends here. Shift+R starts a new run with a new order.
end
