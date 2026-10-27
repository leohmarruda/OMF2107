# Replay Shadow's Shadow Grab (AF animation 16) recordings in the 3D viewer.
# Wraps replay-rec.ps1; the thrown fighter enters throw state 7 / animation 9.
#   replay-shadow-grab.ps1                          # SHADOW-GRAB in the viewer
#   replay-shadow-grab.ps1 -Interrupt               # grab interrupted by a hit
#   replay-shadow-grab.ps1 -Capture                 # screenshots at the key ticks
#   replay-shadow-grab.ps1 -CaptureTick 105,155     # screenshots at chosen ticks
# SHADOW-GRAB.REC holds two grabs: Shadow starts animation 16 at ticks 105 and 386.
# SHADOW-GRAB-INTERRUPT-HIT.REC: animation 16 at tick 189, the opponent hits at 205.
param(
    [switch]$Interrupt,
    [switch]$Capture,
    [int[]]$CaptureTick = @(),
    [switch]$TraceOnly,
    [switch]$SkipTrace
)

$ErrorActionPreference = 'Stop'
if ($Interrupt) {
    $rec = 'SHADOW-GRAB-INTERRUPT-HIT'
    $keyTicks = @(189, 195, 205, 207, 215)
} else {
    $rec = 'SHADOW-GRAB'
    $keyTicks = @(105, 107, 155, 159, 386, 436)
}
if ($Capture -and $CaptureTick.Count -eq 0) { $CaptureTick = $keyTicks }

$replay = @{ Rec = $rec }
if ($CaptureTick.Count -gt 0) { $replay.CaptureTick = $CaptureTick }
if ($TraceOnly) { $replay.TraceOnly = $true }
if ($SkipTrace) { $replay.SkipTrace = $true }
& (Join-Path $PSScriptRoot 'replay-rec.ps1') @replay
exit $LASTEXITCODE
