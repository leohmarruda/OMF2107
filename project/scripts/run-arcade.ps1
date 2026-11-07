# Plays the arcade ladder (Ari's six rungs and the Nova boss, with a news report and hangar maintenance after each win)
# in the 3D prototype's story mode.
#   run-arcade.ps1                    # resume the save if there is one
#   run-arcade.ps1 -New               # ignore the save and start over
#   run-arcade.ps1 -DebugFights       # matches can be skipped by choosing the result (Y win, N loss)
#   run-arcade.ps1 -Scene rung3       # start at a scene (rung1 to rung5, nova1, nova2, news, hangar, victory)
# Wraps run-story.ps1 with project/data/story/arcade_ari.story. Progress is saved to project/build/story/arcade_ari.save,
# separate from the Ari route's save. Each match raises the rival's AI level (the `difficulty` on its fight line).
# This does not build: after editing main.c, story.c, or story.h run project/scripts/build.ps1 -Config Debug first,
# and real matches need the trace build (build.ps1 -Config All).
param(
    [string]$Scene,
    [switch]$New,
    [switch]$DebugFights,
    [string]$SaveFile
)

$runner = Join-Path $PSScriptRoot 'run-story.ps1'
$splat = @{ Script = 'project/data/story/arcade_ari.story' }
if ($Scene) { $splat.Scene = $Scene }
if ($New) { $splat.New = $true }
if ($DebugFights) { $splat.DebugFights = $true }
if ($SaveFile) { $splat.SaveFile = $SaveFile }
& $runner @splat
exit $LASTEXITCODE
