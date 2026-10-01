# Module 4 — AWS Compute Security

**Lab ID:** `aws-compute`

## Syllabus scope
- EC2 Security
- Open Ports
- Patch Management
- Instance Metadata
- Container Security
- Compute Hardening

## Environment
Start this lab from Cloud Security Lab OS after an Owner/Admin enables it and assigns it to your account. The workspace is per-user. Commands below are host-specific observation/training commands. Commands requiring administrator/root rights may fail for a student by design.

## Practical steps
This maps EC2/compute controls to the self-hosted machine; it is not EC2.

PowerShell:
```powershell
Get-ComputerInfo | Select-Object OsName,OsVersion,OsArchitecture
Get-NetTCPConnection -State Listen
Get-Service | Where-Object Status -eq Running | Select-Object -First 20
Get-Command docker -ErrorAction SilentlyContinue
```
Ubuntu:
```bash
uname -a
ss -lntup
systemctl --type=service --state=running --no-pager | head -30
command -v docker || command -v podman || true
```
Document open services, patch status and container runtime availability.

## Cloud Security Lab OS workflow
1. Sign in with the account created by Owner/Admin.
2. Open Labs and select this assigned lab.
3. Select **Start** to create/restore the per-user workspace.
4. Perform the applicable Windows or Ubuntu observations above in an authorized terminal/session.
5. Select **Verify**. The current verifier checks host/workspace readiness and the module-specific checks implemented by the server.
6. Select **Complete** to record the session as completed.
7. Use **Reset** only when you want the lab workspace/session rebuilt.

## Expected result
The Cloud Security Lab OS verifier must return `passed: true` for its implemented checks. This does not certify every proprietary cloud-product behavior named by the syllabus.

## Troubleshooting
- `AUTH-003`: sign in again.
- `PERM-001`: the account lacks permission or the lab is not enabled/assigned.
- `LAB-001`: unknown/missing lab session; Start the lab first.
- Missing PowerShell/Bash command: use the commands for the actual host OS and ensure required OS components are installed.
