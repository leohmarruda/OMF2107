param(
    [ValidateSet('Debug', 'Trace', 'All')]
    [string]$Config = 'All',
    [string]$VcpkgRoot = $(if ($env:VCPKG_ROOT) { $env:VCPKG_ROOT } else { Join-Path $env:USERPROFILE 'vcpkg' })
)

# Builds the dirs the run-blockout*.ps1 scripts expect:
#   build\omf_debug_z7  openomf + omf3d_prototype
#   build\omf_trace_z7  openomf with OMF3K_SOURCE_TRACE=ON
# Sets up the MSVC environment by hand because vcvars64.bat/VsDevCmd.bat need
# vswhere.exe, which is missing when the Visual Studio Installer is not present.

$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path

$vs = 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools'
$kits = 'C:\Program Files (x86)\Windows Kits\10'
$cmakeDir = Join-Path $vs 'Common7\IDE\CommonExtensions\Microsoft\CMake'
$toolchain = Join-Path $VcpkgRoot 'scripts\buildsystems\vcpkg.cmake'

if (-not (Test-Path -LiteralPath $toolchain)) { throw "vcpkg toolchain not found: $toolchain (pass -VcpkgRoot or set VCPKG_ROOT)" }
$msvc = Get-ChildItem (Join-Path $vs 'VC\Tools\MSVC') -Directory | Sort-Object Name | Select-Object -Last 1
if (-not $msvc) { throw "MSVC toolset not found under $vs" }
$sdk = Get-ChildItem (Join-Path $kits 'Include') -Directory | Sort-Object Name | Select-Object -Last 1
if (-not $sdk) { throw "Windows SDK not found under $kits" }

$env:PATH = (@(
    (Join-Path $msvc.FullName 'bin\Hostx64\x64'),
    (Join-Path $kits "bin\$($sdk.Name)\x64"),
    (Join-Path $cmakeDir 'CMake\bin'),
    (Join-Path $cmakeDir 'Ninja'),
    $env:PATH) -join ';')
$env:INCLUDE = (Join-Path $msvc.FullName 'include')
foreach ($d in 'ucrt', 'um', 'shared') { $env:INCLUDE += ';' + (Join-Path $kits "Include\$($sdk.Name)\$d") }
$env:LIB = (Join-Path $msvc.FullName 'lib\x64')
foreach ($d in 'ucrt\x64', 'um\x64') { $env:LIB += ';' + (Join-Path $kits "Lib\$($sdk.Name)\$d") }

function Invoke-Build([string]$Name, [string[]]$ExtraArgs) {
    $dir = Join-Path $projectRoot "build\$Name"
    Write-Host "== $Name"
    # cmd merges stderr into stdout: CMake prints warnings to stderr, which Windows PowerShell 5.1
    # would otherwise turn into a terminating error under $ErrorActionPreference = 'Stop'.
    $configure = (@('cmake', '-S', $projectRoot, '-B', $dir, '-G', 'Ninja', '-DCMAKE_BUILD_TYPE=Debug', '--toolchain', $toolchain) + $ExtraArgs |
        ForEach-Object { "`"$_`"" }) -join ' '
    cmd /c "$configure 2>&1"
    if ($LASTEXITCODE -ne 0) { throw "Configure failed for $Name" }
    cmd /c "cmake --build `"$dir`" 2>&1"
    if ($LASTEXITCODE -ne 0) { throw "Build failed for $Name" }

    # OpenOMF and the run-blockout scripts need the original game data next to the exe.
    $gameData = Join-Path $projectRoot 'OMF2097'
    if (Test-Path -LiteralPath $gameData) {
        $resources = Join-Path $dir 'resources'
        New-Item -ItemType Directory -Force $resources | Out-Null
        Copy-Item -Path (Join-Path $gameData '*') -Destination $resources -Force
    } else {
        Write-Warning "OMF2097 game data not found at $gameData; run-blockout*.ps1 will fail until it is copied into $dir\resources"
    }
}

if ($Config -in 'Debug', 'All') { Invoke-Build 'omf_debug_z7' @('-DUSE_TOOLS=ON') }
if ($Config -in 'Trace', 'All') { Invoke-Build 'omf_trace_z7' @('-DOMF3K_SOURCE_TRACE=ON') }
