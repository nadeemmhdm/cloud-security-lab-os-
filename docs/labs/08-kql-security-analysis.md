# Module 8 — KQL for Security Analysis

**Lab ID:** `kql`

## Syllabus scope
- KQL Fundamentals
- Basic Queries
- Filtering & Searching
- Sorting
- Aggregation
- Advanced Security Queries
- Log Investigation

## Environment
Start this lab from Cloud Security Lab OS after an Owner/Admin enables it and assigns it to your account. The workspace is per-user. Commands below are host-specific observation/training commands. Commands requiring administrator/root rights may fail for a student by design.

## Practical steps
The syllabus names KQL. The self-hosted engine currently supplies JSONL telemetry; it does **not** implement Microsoft's KQL engine. Use these host commands only as local filtering exercises.

PowerShell:
```powershell
Get-Content .\events.jsonl | ForEach-Object { $_ | ConvertFrom-Json } | Where-Object severity -eq warning
Get-Content .\events.jsonl | ForEach-Object { $_ | ConvertFrom-Json } | Group-Object source
```
Ubuntu:
```bash
python -c "import json;print(*[x for x in map(json.loads,open('events.jsonl')) if x['severity']=='warning'],sep='\\n')"
python -c "import json,collections;print(collections.Counter(x['source'] for x in map(json.loads,open('events.jsonl'))))"
```
These are not KQL commands.

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
