# Replay a recorded OpenOMF match (.REC) headlessly to produce a source trace CSV,
# verify it, then show it in the 3D viewer with --source-replay. Use it to compare
# a recorded move, such as a throw, against the 3D presentation.
#   replay-rec.ps1                                  # JAG-CORNER-THROW in the viewer
#   replay-rec.ps1 -Rec THROW-RANGE -CaptureTick 198
#   replay-rec.ps1 -Rec JAG-THROW-LAND -TraceOnly   # just write the CSV
# -Rec is a name in rectests/ (with or without .REC) or a path to a .REC file.
# -CaptureTick saves project/build/mesh-match-ticks/<name>-<tick>.bmp instead of
# opening the viewer; give several ticks with -CaptureTick 191,198,210.
param(
    [string]$Rec = 'JAG-CORNER-THROW',
    [int[]]$CaptureTick = @(),
    [switch]$TraceOnly,
    [switch]$SkipTrace
)

$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
$sourceDir = Join-Path $projectRoot 'build\omf_trace_z7'
$sourceExe = Join-Path $sourceDir 'openomf.exe'
$viewerExe = Join-Path $projectRoot 'build\omf_debug_z7\omf3d_prototype.exe'
$captureDir = Join-Path $projectRoot 'project\build'
$tickDir = Join-Path $captureDir 'mesh-match-ticks'

if (Test-Path -LiteralPath $Rec) {
    $recPath = (Resolve-Path -LiteralPath $Rec).Path
} else {
    $recName = if ($Rec -like '*.REC') { $Rec } else { "$Rec.REC" }
    $recPath = Join-Path $projectRoot "rectests\$recName"
}
if (-not (Test-Path -LiteralPath $recPath)) { throw "Recording not found: $recPath" }
$name = [System.IO.Path]::GetFileNameWithoutExtension($recPath).ToLower()
$tracePath = Join-Path $sourceDir "$name-trace.csv"

if (-not $SkipTrace) {
    if (-not (Test-Path -LiteralPath $sourceExe)) { throw "Build the trace OpenOMF first: $sourceExe" }
    # The trace build writes one CSV row per fighter per completed tick to OMF3K_TRACE_PATH.
    $env:OMF3K_TRACE_PATH = $tracePath
    $logPath = Join-Path $sourceDir "$name-run.log"
    Push-Location $sourceDir
    try {
        # cmd does the redirect: openomf logs to stderr, which PowerShell would treat as an error.
        cmd /c "`"$sourceExe`" --force-audio-backend=NULL --force-renderer=NULL --speed=10 -P `"$recPath`" > `"$logPath`" 2>&1"
        if ($LASTEXITCODE -ne 0) { throw "openomf replay failed (exit $LASTEXITCODE); see $logPath" }
    } finally {
        Pop-Location
        Remove-Item Env:\OMF3K_TRACE_PATH -ErrorAction SilentlyContinue
    }
}
if (-not (Test-Path -LiteralPath $tracePath)) { throw "No trace was written: $tracePath" }
Write-Host "Trace: $tracePath"
if ($TraceOnly) { exit 0 }

if (-not (Test-Path -LiteralPath $viewerExe)) { throw "Build omf3d_prototype first: $viewerExe" }
Push-Location $projectRoot
try {
    & $viewerExe --source-replay-check $tracePath
    if ($LASTEXITCODE -ne 0) { throw 'Source replay check failed.' }

    if ($CaptureTick.Count -eq 0) {
        & $viewerExe --source-replay $tracePath
        exit $LASTEXITCODE
    }

    New-Item -ItemType Directory -Force $tickDir | Out-Null
    foreach ($tick in $CaptureTick) {
        $last = (Get-Content -LiteralPath $tracePath -Tail 1).Split(',')[0]
        cmd /c "`"$viewerExe`" --source-replay `"$tracePath`" --capture-tick $tick >nul 2>&1"
        if ($LASTEXITCODE -ne 0) { throw "Capture failed at tick $tick (trace ends at tick $last)." }
        $out = Join-Path $tickDir "$name-$tick.bmp"
        Copy-Item -LiteralPath (Join-Path $captureDir 'omf3d_source_replay_capture.bmp') -Destination $out -Force
        Write-Host "Captured: $out"
    }
} finally {
    Pop-Location
}
