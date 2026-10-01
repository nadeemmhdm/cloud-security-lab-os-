param(
 [Parameter(Mandatory=$true)][string]$InstallDir,
 [string]$PythonExe=""
)
$ErrorActionPreference="Stop"
$task="CloudSecurityLabOS"
$exe=Join-Path $InstallDir ".venv\Scripts\cloud-os.exe"
if (-not (Test-Path $exe)) { throw "cloud-os.exe not found at $exe" }
$action=New-ScheduledTaskAction -Execute $exe -Argument "start" -WorkingDirectory $InstallDir
$trigger=New-ScheduledTaskTrigger -AtStartup
$settings=New-ScheduledTaskSettingsSet -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Days 3650)
$principal=New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
Register-ScheduledTask -TaskName $task -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
Write-Host "Cloud Security Lab OS boot task installed."
Write-Host "Configure cloudflared separately as its official Windows service."
