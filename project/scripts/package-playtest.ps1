# Assembles a Windows playtest package of the story slice and zips it.
#   project/scripts/package-playtest.ps1            # -> dist/OMF2107-playtest.zip
# Needs a Release build (project/scripts/build.ps1 -Config Release) and the exported story assets
# (python project/tools/export_story_assets.py).
# The package contains the original game's data, art and music for a PRIVATE playtest. The asset
# ledger marks them as not distributable: send the zip only to the tester, never publish it.
param(
    [string]$Name = 'OMF2107-playtest'
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
$build = Join-Path $root 'build\omf_release_z7'
$dist = Join-Path $root 'dist'
$out = Join-Path $dist $Name
$zip = Join-Path $dist "$Name.zip"

foreach ($f in 'openomf.exe', 'omf3d_prototype.exe') {
    if (-not (Test-Path -LiteralPath (Join-Path $build $f))) { throw "Missing ${f}: run project/scripts/build.ps1 -Config Release first." }
}
foreach ($d in 'portraits', 'backdrops', 'sounds', 'art') {
    if (-not (Test-Path -LiteralPath (Join-Path $root "project\build\$d"))) { throw "Missing project\build\${d}: run python project/tools/export_story_assets.py first." }
}
if (-not (Test-Path -LiteralPath (Join-Path $root 'OMF2097\ARENA0.BK'))) { throw 'OMF2097 game data not found.' }

if (Test-Path -LiteralPath $out) { Remove-Item -LiteralPath $out -Recurse -Force }
New-Item -ItemType Directory -Force (Join-Path $out 'bin'), (Join-Path $out 'project\scripts'), (Join-Path $out 'project\data\story'), (Join-Path $out 'project\build') | Out-Null

# Programs and libraries (the launcher and viewer find them in bin\).
Copy-Item -Path (Join-Path $build '*.dll') -Destination (Join-Path $out 'bin')
Copy-Item -LiteralPath (Join-Path $build 'openomf.exe'), (Join-Path $build 'omf3d_prototype.exe') -Destination (Join-Path $out 'bin')
Copy-Item -LiteralPath (Join-Path $build 'resources') -Destination (Join-Path $out 'bin\resources') -Recurse
Copy-Item -LiteralPath (Join-Path $build 'shaders') -Destination (Join-Path $out 'bin\shaders') -Recurse
# The C runtime, beside the programs, so the tester does not need Visual Studio installed.
foreach ($dll in 'vcruntime140.dll', 'vcruntime140_1.dll', 'msvcp140.dll') {
    $src = Join-Path $env:SystemRoot "System32\$dll"
    if (Test-Path -LiteralPath $src) { Copy-Item -LiteralPath $src -Destination (Join-Path $out 'bin') }
}

# Game data (the viewer plays the music straight from OMF2097\) and the exported story art and sounds.
Copy-Item -LiteralPath (Join-Path $root 'OMF2097') -Destination (Join-Path $out 'OMF2097') -Recurse
foreach ($d in 'portraits', 'backdrops', 'sounds', 'art') {
    New-Item -ItemType Directory -Force (Join-Path $out "project\build\$d") | Out-Null
    Copy-Item -Path (Join-Path $root "project\build\$d\*.bmp"), (Join-Path $root "project\build\$d\*.wav") `
        -Destination (Join-Path $out "project\build\$d") -ErrorAction SilentlyContinue
}

Copy-Item -LiteralPath (Join-Path $root 'project\scripts\run-story.ps1'), (Join-Path $root 'project\scripts\run-story-meshy.ps1'), `
    (Join-Path $root 'project\scripts\run-blockout-jaguar.ps1') `
    -Destination (Join-Path $out 'project\scripts')
Copy-Item -LiteralPath (Join-Path $root 'project\data\story\crystal_christian.story'), (Join-Path $root 'project\data\story\christian_crystal.story') -Destination (Join-Path $out 'project\data\story')
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'playtest\Play.bat'), (Join-Path $PSScriptRoot 'playtest\Play-NewGame.bat'), `
    (Join-Path $PSScriptRoot 'playtest\Play-Meshy.bat'), (Join-Path $PSScriptRoot 'playtest\Play-Meshy-NewGame.bat'), `
    (Join-Path $PSScriptRoot 'playtest\README-TESTER.txt') -Destination $out

if (Test-Path -LiteralPath $zip) { Remove-Item -LiteralPath $zip -Force }
Compress-Archive -Path $out -DestinationPath $zip -CompressionLevel Optimal
"{0}  ({1:N0} MB)" -f $zip, ((Get-Item -LiteralPath $zip).Length / 1MB)
