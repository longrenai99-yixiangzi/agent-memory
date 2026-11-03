param(
    [Parameter(Mandatory = $true)][string]$RepoPath,
    [Parameter(Mandatory = $true)][string]$PackagePath
)
$ErrorActionPreference = 'Stop'
$RepoPath = (Resolve-Path -LiteralPath $RepoPath).Path
$PackagePath = (Resolve-Path -LiteralPath $PackagePath).Path
if (-not (Test-Path -LiteralPath (Join-Path $RepoPath '.git'))) { throw "RepoPath is not a Git repository: $RepoPath" }
$manifestPath = Join-Path $PackagePath 'manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath)) { throw "manifest.json not found in PackagePath: $PackagePath" }
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
$mapping = @(
    @{ Source = 'assets/PLAN-001.png'; Dest = 'projects/另一个家的布布/assets/space/PLAN-001_彩平图_20261025_阳台家具删除版.png' },
    @{ Source = 'assets/PLAN-002.png'; Dest = 'projects/另一个家的布布/assets/space/PLAN-002_AB世界交汇区标注_V2.2.png' },
    @{ Source = 'assets/VIEW-01.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-01_朝阳台.png' },
    @{ Source = 'assets/VIEW-02.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-02_朝厨房.jpg' },
    @{ Source = 'assets/VIEW-03.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-03_朝沙发.png' },
    @{ Source = 'assets/VIEW-04.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-04_朝电视.png' },
    @{ Source = 'assets/VIEW-05.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-05_朝入户门.jpg' },
    @{ Source = 'assets/VIEW-06.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-06_朝卫生间.jpg' }
)
$gitPaths = @()
foreach ($item in $mapping) {
    $src = Join-Path $PackagePath ($item.Source -replace '/', '\')
    if (-not (Test-Path -LiteralPath $src)) { throw "Missing image in package: $src" }
    $asset = $manifest.assets | Where-Object { $_.archive_path -eq $item.Source } | Select-Object -First 1
    if ($null -eq $asset) { throw "Manifest entry missing: $($item.Source)" }
    $sourceHash = (Get-FileHash -LiteralPath $src -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($sourceHash -ne $asset.sha256 -or (Get-Item -LiteralPath $src).Length -ne [int64]$asset.size_bytes) { throw "Source image SHA256/size mismatch: $($item.Source)" }
    $dest = Join-Path $RepoPath ($item.Dest -replace '/', '\')
    $dir = Split-Path -Parent $dest
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    Copy-Item -LiteralPath $src -Destination $dest -Force
    $destHash = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($destHash -ne $asset.sha256) { throw "Copied image SHA256 mismatch: $($item.Dest)" }
    $gitPaths += $item.Dest
    Write-Host ("OK SHA256  " + $item.Source) -ForegroundColor Green
}
Write-Host "All 8 images copied and SHA256-verified. Repository: $RepoPath" -ForegroundColor Green
git -C $RepoPath add -- $gitPaths
git -C $RepoPath status --short
$confirm = Read-Host 'Review that only the 8 image files are staged. Type Y to commit and push; any other input leaves them staged'
if ($confirm -match '^(Y|YES)$') {
    git -C $RepoPath commit -m 'Add confirmed 另一个家的布布 space assets'
    git -C $RepoPath push
    Write-Host 'Push command completed. Verify remote image SHA256 before updating the asset registry.' -ForegroundColor Green
} else {
    Write-Host 'Images remain staged; no commit or push was run.' -ForegroundColor Yellow
}
