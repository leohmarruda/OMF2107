# Plays the story mode with the Meshy robots in the matches (the Robot Mascot for Jaguar, the Rocket Jester for Shadow)
# instead of the blockout models. Same story, same saves; only the look of the fighters in the match window differs.
#   run-story-meshy.ps1              # resumes the saved story
#   run-story-meshy.ps1 -New         # starts over
# Every other option of run-story.ps1 is passed through (-DebugFights, -Scene, -Script, -SaveFile).
# The Meshy meshes are compiled into the viewer; this only switches them on for the viewer and for the matches it starts.
param(
    [string]$Script,
    [string]$Scene,
    [switch]$New,
    [switch]$DebugFights,
    [string]$SaveFile
)

$ErrorActionPreference = 'Stop'
$env:OMF3K_MESHY = '1'   # read by omf3d_prototype.exe; the match window inherits it from the story window
$passThrough = @{}
foreach ($name in $PSBoundParameters.Keys) { $passThrough[$name] = $PSBoundParameters[$name] }
& (Join-Path $PSScriptRoot 'run-story.ps1') @passThrough
exit $LASTEXITCODE
