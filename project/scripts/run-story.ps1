# Plays a story script in the 3D prototype's story mode.
#   run-story.ps1                    # the draft Crystal versus Christian slice, resuming a save if there is one
#   run-story.ps1 -New               # ignore the save and start over (it is replaced as you play)
#   run-story.ps1 -DebugFights       # matches can be skipped by choosing the result (Y win, N loss)
#   run-story.ps1 -Scene recovery    # start at a scene
# Progress is saved to project/build/story/<script name>.save. This does not build: after editing
# main.c, story.c, or story.h run project/scripts/build.ps1 -Config Debug first.
param(
    [string]$Script = 'project/data/story/crystal_christian.story',
    [string]$Scene,
    [switch]$New,
    [switch]$DebugFights,
    [string]$SaveFile
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
$exe = Join-Path $root 'build\omf_debug_z7\omf3d_prototype.exe'
if (-not (Test-Path -LiteralPath $exe)) { throw "Build omf3d_prototype first (project/scripts/build.ps1): $exe" }
$scriptPath = if ([System.IO.Path]::IsPathRooted($Script)) { $Script } else { Join-Path $root $Script }
if (-not (Test-Path -LiteralPath $scriptPath)) { throw "Story script not found: $scriptPath" }

# The viewer is not rebuilt by the run scripts, so say so when it is older than its sources.
$exeTime = (Get-Item -LiteralPath $exe).LastWriteTime
$stale = Get-ChildItem -LiteralPath (Join-Path $root 'project\prototype') -Include '*.c', '*.h' -File |
    Where-Object { $_.LastWriteTime -gt $exeTime } | Select-Object -ExpandProperty Name
if ($stale) {
    Write-Warning ("omf3d_prototype.exe is older than: " + ($stale -join ', ') +
                   ". Rebuild with project/scripts/build.ps1 -Config Debug to see those changes.")
}

$viewerArgs = @('--story', $scriptPath)
if ($Scene) { $viewerArgs += @('--scene', $Scene) }
if ($New) { $viewerArgs += '--new' }
if ($DebugFights) { $viewerArgs += '--debug-fights' }
if ($SaveFile) { $viewerArgs += @('--save-file', $SaveFile) }

Push-Location $root   # the viewer writes its save to project/build/story relative to here
try {
    & $exe @viewerArgs
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
