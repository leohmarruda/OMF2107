param(
    [int]$CaptureTick = -1,
    [int]$WarmupSeconds = 4,
    [ValidateSet('Jaguar', 'Shadow', 'Katana')]
    [string]$Player = 'Jaguar',
    # Story matches: the rival's HAR. Left out, it is the other of Jaguar and Shadow; it is never the player's own HAR.
    [ValidateSet('', 'Jaguar', 'Shadow', 'Katana')]
    [string]$RivalHar = '',
    [ValidateSet('Crystal', 'Steffan', 'Milano', 'Christian', 'Shirro', 'JeanPaul', 'Ibrahim', 'Angel', 'Cossette', 'Raven', 'Ari', 'Selene', 'Mara', 'Ren', 'Lyra', 'Nova')]
    [string]$Pilot = '',
    # Original Tournament upgrade level for Shadow (0-3). Shadow's shadow attacks,
    # such as Shadow Punch, only exist in the original data at level 3.
    [ValidateRange(0, 3)]
    [int]$ShadowEnhancement = 0,
    # Story matches: the AI rival's pilot, and a file the viewer writes the winner to before it exits
    # (without the retry prompt). The rival always fights in the HAR the player did not pick.
    [ValidateSet('', 'Crystal', 'Steffan', 'Milano', 'Christian', 'Shirro', 'JeanPaul', 'Ibrahim', 'Angel', 'Cossette', 'Raven', 'Ari', 'Selene', 'Mara', 'Ren', 'Lyra', 'Nova')]
    [string]$RivalPilot = '',
    [string]$ResultFile = '',
    # Let OpenOMF play its own sound effects and music in the match. Off by default, as before.
    [switch]$Sound
)

$ErrorActionPreference = 'Stop'
if ($CaptureTick -lt -1) { throw 'CaptureTick must be zero or greater.' }
if ($WarmupSeconds -lt 0 -or $WarmupSeconds -gt 8) { throw 'WarmupSeconds must be between zero and eight.' }
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
New-Item -ItemType Directory -Force (Join-Path $projectRoot 'project\build') | Out-Null   # where the viewer writes its captures
$sourceDir = Join-Path $projectRoot 'build\omf_trace_z7'
$viewerExe = Join-Path $projectRoot 'build\omf_debug_z7\omf3d_prototype.exe'
# A playtest package (package-playtest.ps1) has both programs together in bin\ instead.
$binDir = Join-Path $projectRoot 'bin'
if (Test-Path -LiteralPath (Join-Path $binDir 'openomf.exe')) {
    $sourceDir = $binDir
    $viewerExe = Join-Path $binDir 'omf3d_prototype.exe'
}
$sourceExe = Join-Path $sourceDir 'openomf.exe'
$tracePath = Join-Path $sourceDir 'omf3k-live.csv'

if (-not (Test-Path -LiteralPath $sourceExe)) { throw "Build OpenOMF with OMF3K_SOURCE_TRACE=ON first: $sourceExe" }
if (-not (Test-Path -LiteralPath $viewerExe)) { throw "Build omf3d_prototype first: $viewerExe" }
if (-not (Test-Path -LiteralPath (Join-Path $sourceDir 'resources\ARENA0.BK'))) {
    throw "OpenOMF resources are missing in $sourceDir"
}

$env:OMF3K_TRACE_PATH = $null
$env:OMF3K_INPUT_PATH = $null
$env:OMF3K_LIVE_PLAYER = $Player
$env:OMF3K_LIVE_RIVAL_HAR = if ($RivalHar -ne '') { $RivalHar } else { $null }
$pilotNames = @('Crystal', 'Steffan', 'Milano', 'Christian', 'Shirro', 'JeanPaul', 'Ibrahim', 'Angel', 'Cossette', 'Raven')
# Story pilots that have no original-game pilot: they fight with the stats, sex and colours of a stand-in, under their own name.
$standIns = @{ Ari = 'Christian'; Selene = 'Cossette'; Mara = 'Milano'; Ren = 'Ibrahim'; Lyra = 'Steffan'; Nova = 'Shirro' }
if ($Pilot -eq '') { $Pilot = if ($Player -eq 'Shadow') { 'Shirro' } else { 'Crystal' } }
$pilotLabel = $Pilot
if ($standIns.ContainsKey($Pilot)) { $Pilot = $standIns[$Pilot] }
$Pilot = $pilotNames | Where-Object { $_ -ieq $Pilot } | Select-Object -First 1
$env:OMF3K_LIVE_PILOT_ID = [string][array]::IndexOf($pilotNames, $Pilot)
$env:OMF3K_LIVE_PILOT_NAME = $pilotLabel.ToUpperInvariant()
$env:OMF3K_LIVE_RIVAL_NAME = if ($Player -eq 'Shadow') { 'CRYSTAL' } else { 'SHIRRO' }
$env:OMF3K_LIVE_RIVAL_PILOT_ID = $null
if ($RivalPilot -ne '') {
    $rivalLabel = $RivalPilot
    if ($standIns.ContainsKey($RivalPilot)) { $RivalPilot = $standIns[$RivalPilot] }
    $RivalPilot = $pilotNames | Where-Object { $_ -ieq $RivalPilot } | Select-Object -First 1
    $env:OMF3K_LIVE_RIVAL_PILOT_ID = [string][array]::IndexOf($pilotNames, $RivalPilot)
    $env:OMF3K_LIVE_RIVAL_NAME = $rivalLabel.ToUpperInvariant()
}
$env:OMF3K_SHADOW_ENHANCEMENT = [string]$ShadowEnhancement
Write-Host "Starting $Pilot / $Player in Stadium"
$env:OMF3K_INPUT_MAP = 'Local\OMF3KInput_' + [Guid]::NewGuid().ToString('N')
$env:OMF3K_STATE_MAP = 'Local\OMF3KState_' + [Guid]::NewGuid().ToString('N')
$viewerArgs = @('--source-live', $tracePath)
if ($CaptureTick -ge 0) { $viewerArgs += @('--capture-tick', [string]$CaptureTick) }
if ($ResultFile -ne '') { $viewerArgs += @('--result-file', $ResultFile) }
$viewerOut = Join-Path $sourceDir 'omf3k-live-viewer-out.txt'
$viewerErr = Join-Path $sourceDir 'omf3k-live-viewer-err.txt'
$sourceOut = Join-Path $sourceDir 'omf3k-live-source-out.txt'
$sourceErr = Join-Path $sourceDir 'omf3k-live-source-err.txt'
$sourceArgs = @('--omf3k-live', '--force-renderer=NULL', '--speed=5', '--log-level=WARN')
if (-not $Sound) { $sourceArgs += '--force-audio-backend=NULL' }
$source = $null
$viewer = $null
$viewerExit = 1
try {
    if ($WarmupSeconds -gt 0) {
        $viewer = Start-Process -FilePath $viewerExe -ArgumentList $viewerArgs `
            -WorkingDirectory $projectRoot `
            -RedirectStandardOutput $viewerOut `
            -RedirectStandardError $viewerErr `
            -PassThru
        Start-Sleep -Seconds $WarmupSeconds
        $viewer.Refresh()
        if ($viewer.HasExited) { throw "3D viewer exited during startup (code $($viewer.ExitCode))." }
    }
    $source = Start-Process -FilePath $sourceExe `
        -ArgumentList $sourceArgs `
        -WorkingDirectory $sourceDir `
        -RedirectStandardOutput $sourceOut `
        -RedirectStandardError $sourceErr `
        -WindowStyle Hidden -PassThru
    Start-Sleep -Milliseconds 500
    $source.Refresh()
    if ($source.HasExited) { throw "OpenOMF exited during startup (code $($source.ExitCode)). Check omf3k-live-source-err.txt." }

    if ($viewer) {
        $viewer.WaitForExit()
        $viewerExit = $viewer.ExitCode
        Get-Content -LiteralPath $viewerOut
        if ($viewerExit -ne 0) { Get-Content -LiteralPath $viewerErr }
    } else {
        Push-Location $projectRoot
        try {
            & $viewerExe @viewerArgs
            $viewerExit = $LASTEXITCODE
        } finally {
            Pop-Location
        }
    }
} finally {
    if ($viewer) {
        $viewer.Refresh()
        if (-not $viewer.HasExited) { Stop-Process -Id $viewer.Id }
    }
    if ($source) {
        $source.Refresh()
        if (-not $source.HasExited) { Stop-Process -Id $source.Id }
    }
}
exit $viewerExit
