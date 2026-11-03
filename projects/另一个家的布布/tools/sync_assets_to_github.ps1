param(
    [Parameter(Mandatory = $true)]
    [string]$RepoPath,
    [Parameter(Mandatory = $true)]
    [string]$PackagePath
)

$ErrorActionPreference = 'Stop'
$RepoPath = (Resolve-Path $RepoPath).Path
$PackagePath = (Resolve-Path $PackagePath).Path

if (-not (Test-Path (Join-Path $RepoPath '.git'))) {
    throw "RepoPath 不是 Git 仓库：$RepoPath"
}

# This helper copies only the eight image binaries. It deliberately does not overwrite
# the Markdown documents already synchronized through the GitHub connector.
$mapping = @(
    @{ Source = 'assets/PLAN-001_彩平图_20261025_阳台家具删除版.png'; Dest = 'projects/另一个家的布布/assets/space/PLAN-001_彩平图_20261025_阳台家具删除版.png' },
    @{ Source = 'assets/PLAN-002_AB世界交汇区标注_V2.2.png'; Dest = 'projects/另一个家的布布/assets/space/PLAN-002_AB世界交汇区标注_V2.2.png' },
    @{ Source = 'assets/VIEW-01_朝阳台.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-01_朝阳台.png' },
    @{ Source = 'assets/VIEW-02_朝厨房.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-02_朝厨房.jpg' },
    @{ Source = 'assets/VIEW-03_朝沙发.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-03_朝沙发.png' },
    @{ Source = 'assets/VIEW-04_朝电视.png'; Dest = 'projects/另一个家的布布/assets/views/VIEW-04_朝电视.png' },
    @{ Source = 'assets/VIEW-05_朝入户门.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-05_朝入户门.jpg' },
    @{ Source = 'assets/VIEW-06_朝卫生间.jpg'; Dest = 'projects/另一个家的布布/assets/views/VIEW-06_朝卫生间.jpg' }
)

$gitPaths = @()
foreach ($item in $mapping) {
    $sourcePath = Join-Path $PackagePath $item.Source
    if (-not (Test-Path $sourcePath)) { throw "同步包缺少文件：$sourcePath" }
    $destPath = Join-Path $RepoPath ($item.Dest -replace '/', '\')
    $destDir = Split-Path $destPath -Parent
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    Copy-Item -LiteralPath $sourcePath -Destination $destPath -Force
    $gitPaths += $item.Dest
}

Write-Host "已复制 8 张图片到：$RepoPath" -ForegroundColor Green
git -C $RepoPath add -- $gitPaths
git -C $RepoPath status --short
$confirm = Read-Host '确认上方仅为这 8 张图片的变更后，是否提交并推送到 GitHub？输入 Y 确认'
if ($confirm -match '^(Y|YES)$') {
    git -C $RepoPath commit -m 'Add confirmed 另一个家的布布 space assets'
    git -C $RepoPath push
    Write-Host '图片提交并推送完成。请再按 manifest.json 校验远程 SHA-256。' -ForegroundColor Green
} else {
    Write-Host '已保留图片暂存状态，未提交、未推送。' -ForegroundColor Yellow
}
