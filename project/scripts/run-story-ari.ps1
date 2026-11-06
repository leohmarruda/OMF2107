# Plays Ari Solano's story (the whole route, Chapters 1 to 6) in the 3D prototype's story mode.
#   run-story-ari.ps1                    # resume the save if there is one
#   run-story-ari.ps1 -New               # ignore the save and start over
#   run-story-ari.ps1 -DebugFights       # matches can be skipped by choosing the result (Y win, N loss)
#   run-story-ari.ps1 -Scene prefight    # start at a scene (for example arena, prefight, ch2_breakfast, ch6_start, ch6_boss1)
# Wraps run-story.ps1 with project/data/story/ari.story. Progress is saved to project/build/story/ari.save.
param(
    [string]$Scene,
    [switch]$New,
    [switch]$DebugFights,
    [string]$SaveFile
)

$runner = Join-Path $PSScriptRoot 'run-story.ps1'
$splat = @{ Script = 'project/data/story/ari.story' }
if ($Scene) { $splat.Scene = $Scene }
if ($New) { $splat.New = $true }
if ($DebugFights) { $splat.DebugFights = $true }
if ($SaveFile) { $splat.SaveFile = $SaveFile }
& $runner @splat
exit $LASTEXITCODE
