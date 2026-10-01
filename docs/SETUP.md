# Setup and verification

## Windows — single command

Open PowerShell in the cloned repository and run:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

This creates the virtual environment, installs Cloud Security Lab OS, optionally installs AWS CLI and Azure CLI through WinGet when missing, compiles the Python package, and runs the test suite.

## Linux/macOS — single command

```bash
bash setup.sh
```

The script installs the Python application and runs compilation/tests. Install AWS CLI and Azure CLI using the official packages for your OS before cloud labs.

## Real terminal checks

PowerShell:
```powershell
Get-Location
Get-ChildItem
python --version
aws sts get-caller-identity
az account show
```

Bash:
```bash
pwd
ls -la
python3 --version
aws sts get-caller-identity
az account show
```

Cloud OS uses the native host shell. PowerShell commands require a Windows host with PowerShell; Bash commands require Bash installed on the host. Privileged Windows commands still obey UAC. Linux privileged execution uses non-interactive sudo and therefore requires the host administrator to configure allowed sudo privileges deliberately.

## Cloud authentication

AWS: use an isolated training account or role and authenticate using AWS SSO or the AWS credential chain. Azure: use a training subscription and `az login`. Do not put secrets in the repository.

## Verify

After starting Cloud OS, open Labs. Provider status must show authenticated before real verification succeeds. Run each lab's Verify action to query the connected account.
