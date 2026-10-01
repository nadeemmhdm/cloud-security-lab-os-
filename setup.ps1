param([switch]$NoCloudCLIs)
$ErrorActionPreference="Stop"
Write-Host "Cloud Security Lab OS - one command setup"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python 3.10+ is required." }
python -c "import sys; assert sys.version_info >= (3,10), 'Python 3.10+ required'"
if (-not (Test-Path ".venv")) { python -m venv .venv }
$py = Join-Path $PWD ".venv\Scripts\python.exe"
& $py -m pip install --upgrade pip
& $py -m pip install -e ".[test]"
if (-not $NoCloudCLIs) {
 if (-not (Get-Command aws -ErrorAction SilentlyContinue) -and (Get-Command winget -ErrorAction SilentlyContinue)) { winget install -e --id Amazon.AWSCLI --accept-package-agreements --accept-source-agreements }
 if (-not (Get-Command az -ErrorAction SilentlyContinue) -and (Get-Command winget -ErrorAction SilentlyContinue)) { winget install -e --id Microsoft.AzureCLI --accept-package-agreements --accept-source-agreements }
}
& $py -m compileall -q cloud_os
& $py -m pytest -q
Write-Host ""
Write-Host "Setup complete."
Write-Host "First time: .\.venv\Scripts\cloud-os.exe setup"
Write-Host "Start:      .\.venv\Scripts\cloud-os.exe start"
Write-Host "AWS login:  aws configure / aws sso login"
Write-Host "Azure login: az login"
