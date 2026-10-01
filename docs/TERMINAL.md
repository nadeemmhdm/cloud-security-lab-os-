# Terminal Guide

The Terminal page executes real host commands; it is not a simulated terminal.

## PowerShell
Windows hosts expose PowerShell when installed/discovered. Examples: `Get-Location`, `Get-ChildItem`, `Get-Process`, `Get-Service`, `aws sts get-caller-identity`, and `az account show`.

## Bash
Linux hosts expose Bash when installed/discovered. Examples: `pwd`, `ls -la`, `ps aux`, `systemctl status cloud-os`, `aws sts get-caller-identity`, and `az account show`.

Commands execute under the OS account running Cloud Security Lab OS and inside its configured storage root. Owner/Admin authorization is required for privileged terminal mode. On Linux, privileged mode uses `sudo -n`; configure sudo policy deliberately. On Windows, the application cannot bypass UAC; start the service/process elevated only when administrative host operations are genuinely required.
