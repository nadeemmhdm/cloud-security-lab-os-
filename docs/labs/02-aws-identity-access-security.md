# Module 2 — AWS Identity & Access Security

**Lab ID:** `aws-iam`

## Syllabus scope
- AWS IAM
- Users, Roles & Policies
- Least Privilege
- Access Keys
- Permission Management
- IAM Misconfigurations

## Environment
Start this lab from Cloud Security Lab OS after an Owner/Admin enables it and assigns it to your account. The workspace is per-user. Commands below are host-specific observation/training commands. Commands requiring administrator/root rights may fail for a student by design.

## Practical steps
This self-hosted exercise maps IAM concepts to host identities and permissions; it is not AWS IAM.

PowerShell:
```powershell
whoami
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember -Group Users
whoami /priv
```
Ubuntu:
```bash
whoami
id
getent passwd
getent group
sudo -l
```
Review the output for excessive group membership or privileges. Do not change system accounts unless the administrator explicitly authorizes it.

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
