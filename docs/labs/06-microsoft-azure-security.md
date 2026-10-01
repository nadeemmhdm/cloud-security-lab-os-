# Module 6 — Microsoft Azure Security

**Lab ID:** `azure-security`

## Syllabus scope
- Microsoft Entra ID
- Azure IAM & Permissions
- Azure Networking
- Azure Storage Security
- Azure Compute Security
- Azure Security Monitoring

## Environment
Start this lab from Cloud Security Lab OS after an Owner/Admin enables it and assigns it to your account. The workspace is per-user. Commands below are host-specific observation/training commands. Commands requiring administrator/root rights may fail for a student by design.

## Practical steps
This is a local practical equivalent and is not Microsoft Entra ID or Azure.

PowerShell:
```powershell
whoami /all
Get-LocalUser
Get-NetIPConfiguration
Get-NetFirewallProfile
Get-Volume
Get-WinEvent -LogName System -MaxEvents 10
```
Ubuntu:
```bash
id
getent passwd
ip -4 addr
sudo nft list ruleset
findmnt
journalctl -n 20 --no-pager
```
Map identity, network, storage, compute and monitoring observations to the syllabus control categories.

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
