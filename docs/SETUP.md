# One-command setup

## Linux / Ubuntu / WSL
```bash
bash install.sh
```

## Windows PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The installer creates an isolated `.venv`, installs Cloud Security Lab OS, and runs the secure first-time setup.

## Real terminal support
Cloud Security Lab OS does not emulate a shell. On Windows it discovers and runs the host PowerShell executable. On Linux it discovers and runs the host Bash executable. Commands execute with `shell=False` inside the configured storage root. Privileged Linux commands use non-interactive `sudo -n`; Windows privileged commands require the Cloud OS process itself to already be elevated.

After installation:
```powershell
.\.venv\Scripts\cloud-os.exe doctor
.\.venv\Scripts\cloud-os.exe start
```
or:
```bash
. .venv/bin/activate
cloud-os doctor
cloud-os start
```

## AWS / Azure
Cloud labs use the real official provider CLIs on this same host. Authenticate AWS with your dedicated training account/role and Azure with your dedicated training subscription. Provider credentials are not stored by Cloud Security Lab OS.
