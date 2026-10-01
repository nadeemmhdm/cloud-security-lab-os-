# Complete Setup Guide

Cloud Security Lab OS uses the user's Windows 10/11 or Ubuntu/Linux computer as the origin server. No AWS account, Azure subscription, AWS CLI or Azure CLI is required for the self-hosted runtime.

## 1. Requirements
- Windows 10/11 or Ubuntu/Linux
- Python 3.10+
- Internet during installation
- Administrator/root access for installing OS services and Cloudflare components
- Git if cloning the repository

## 2. Windows
Open PowerShell in the repository:
```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
.\.venv\Scripts\cloud-os.exe setup
.\.venv\Scripts\cloud-os.exe start
```
The setup command creates the owner credential/configuration. Do not share the owner password.

To install the supplied Cloud OS boot task, review and run the Windows service helper from an elevated PowerShell session:
```powershell
powershell -ExecutionPolicy Bypass -File .\packaging\install-windows-service.ps1 -InstallDir "$PWD"
```

## 3. Ubuntu/Linux
```bash
bash setup.sh
.venv/bin/cloud-os setup
.venv/bin/cloud-os start
```
For an always-on installation, adapt `packaging/cloud-os.service` to the final installation path/user, install it under systemd, then enable/start it with the normal systemd administrator workflow.

## 4. First login and users
Sign in as Owner. Create only the users who need access. Use `student` for lab users and `instructor` for delegated lab management. Owner/Admin enables each lab and assigns it to the intended account. A student cannot run an unassigned/disabled lab.

## 5. Lab workflow
1. Owner/Admin enables and assigns the lab.
2. Student signs in.
3. Start creates the per-user workspace/session.
4. Perform the Windows or Ubuntu steps in `docs/labs/`.
5. Verify runs the implemented server checks.
6. Complete records completion.
7. Reset removes that user's lab workspace/session and allows a clean restart.

## 6. Worldwide access
Cloudflare Tunnel is the transport layer; the physical PC remains the origin. Publish the Cloud OS loopback web service through an authenticated HTTPS route. SSH and other TCP services should use separate explicit authenticated routes. Never expose every host port.

Install/configure `cloudflared` using Cloudflare's current official instructions for the host OS. Store tunnel credentials as deployment secrets, never in Git or browser-visible configuration. Configure cloudflared as an OS service so it reconnects after reboot.

## 7. Reboot behavior
Cloud OS and cloudflared should both be configured as startup services. If the PC loses power, the origin is offline. When the PC boots again and networking returns, the services can start/reconnect automatically. Prevent sleep while the machine is acting as a server. Firmware restore-on-AC-power is optional and must be configured by the machine owner where supported.

## 8. Verification
```bash
python -m compileall -q cloud_os
pytest -q
```
CI also runs the application test suite on Windows and Ubuntu GitHub runners.

## 9. Security
- Never commit Cloudflare tokens, passwords, SSH private keys or other secrets.
- Do not grant student accounts host-admin terminal access.
- Keep the application origin bound to loopback when using a tunnel.
- Publish only required services.
- Operating-system UAC/sudo/firewall controls remain authoritative.

## 10. Product-boundary note
The curriculum contains AWS and Microsoft product subjects. In this self-hosted mode they are explicitly local practical equivalents. This PC does not become AWS IAM/VPC/EC2/S3, Microsoft Entra ID/Azure, Sentinel, Microsoft's KQL service or Defender XDR.
