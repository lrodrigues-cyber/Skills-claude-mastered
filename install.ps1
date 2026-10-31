# Usage: .\install.ps1 -Pack 02-motion-design [-Target $HOME\.claude\skills]
param([Parameter(Mandatory)][string]$Pack, [string]$Target = "$HOME\.claude\skills")
New-Item -ItemType Directory -Force $Target | Out-Null
$n = 0
Get-ChildItem $Pack -Recurse -Filter SKILL.md | ForEach-Object {
  $d = $_.Directory; $dst = Join-Path $Target $d.Name
  if (Test-Path $dst) { Write-Host "skip (exists): $($d.Name)"; return }
  Copy-Item $d.FullName $dst -Recurse; $n++
}
Write-Host "$n skills installed in $Target"
