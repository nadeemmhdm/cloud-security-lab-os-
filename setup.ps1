param([switch]$SkipTests)
$ErrorActionPreference="Stop"
Write-Host "Cloud Security Lab OS - Windows setup"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python 3.10+ is required." }
python -c "import sys; assert sys.version_info >= (3,10), 'Python 3.10+ required'"
if (-not (Test-Path ".venv")) { python -m venv .venv }
$py=Join-Path $PWD ".venv\Scripts\python.exe"
& $py -m pip install --upgrade pip
& $py -m pip install -e ".[test]"
& $py -m compileall -q cloud_os
if (-not $SkipTests) { & $py -m pytest -q }
Write-Host "Setup complete. No AWS/Azure CLI is required."
Write-Host "Run .\.venv\Scripts\cloud-os.exe setup, then install Cloud OS + cloudflared as boot services."
