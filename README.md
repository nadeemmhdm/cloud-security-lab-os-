# Cloud Security Lab OS

Cloud Security Lab OS turns a Windows 10/11 or Ubuntu computer into a self-hosted security lab server. The application runs on the owner's machine; Cloudflare Tunnel can provide worldwide access without requiring AWS/Azure hosting.

## Access model
Owner/Admin creates users, enables labs and assigns access. Users can see/run only enabled labs assigned to them. Lab workspaces and progress are separated per user. Host terminal privileges are not granted to student accounts by default.

## Curriculum
The lab catalog contains Modules 1–9: Cloud Security Fundamentals, AWS Identity & Access Security, AWS Network Security, AWS Compute Security, AWS Storage & Data Security, Microsoft Azure Security, Microsoft Sentinel & SIEM, KQL for Security Analysis and Microsoft Defender XDR.

AWS/Microsoft product names are retained to map the supplied curriculum. Without those external proprietary services, the self-hosted exercises are explicitly labelled local practical equivalents; the application does not claim to be AWS/Azure/Sentinel/Defender.

## Setup
Python 3.10+ is required.

Windows:
```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
.\.venv\Scripts\cloud-os.exe setup
.\.venv\Scripts\cloud-os.exe start
```

Ubuntu/Linux:
```bash
bash setup.sh
.venv/bin/cloud-os setup
.venv/bin/cloud-os start
```

No AWS CLI or Azure CLI is required for the self-hosted runtime.

## Lab guides
See [docs/labs/README.md](docs/labs/README.md) for all nine step-by-step solution guides, Windows/Ubuntu commands, expected results, verification and reset instructions.

## Worldwide access
See [docs/WORLDWIDE_ACCESS.md](docs/WORLDWIDE_ACCESS.md). Keep Cloud OS bound to loopback and publish approved services through authenticated Cloudflare routes. Tunnel credentials are deployment secrets and must never be committed.

## Testing
```bash
python -m compileall -q cloud_os
pytest -q
```

The test suite validates application behavior on Windows and Ubuntu GitHub runners. A passing CI run validates the implemented software checks; it does not certify proprietary cloud services that are not part of this self-hosted runtime.
