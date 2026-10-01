# Azure, Sentinel, KQL and Defender XDR Practical Labs

Use only a tenant/subscription/workspace you own or are authorized to administer. Licensing and permissions determine which Sentinel and Defender XDR features are available.

## Module 6 — Microsoft Azure Security
1. Authenticate: `az login`.
2. Confirm subscription: `az account show`; select the dedicated training subscription if needed.
3. Inventory resource groups: `az group list`.
4. Review Entra identities and Azure RBAC assignments used by the lab.
5. Inspect VNets/NSGs and remove unnecessary broad inbound exposure.
6. Review the lab storage account for network access, encryption and access configuration.
7. Review lab VM networking, identity, disk/security configuration and monitoring.
8. Run Azure Security Verify.

## Module 7 — Microsoft Sentinel & SIEM
1. Use an authorized Log Analytics workspace with Microsoft Sentinel enabled.
2. Confirm required data connectors are configured for the course exercise.
3. Verify log ingestion in the workspace.
4. Review analytics/detection rules and resulting alerts.
5. Open a lab incident, inspect entities/evidence/timeline, document findings and close/update it according to the exercise.
6. Do not manufacture incident results in Cloud Security Lab OS; the workspace is the source of truth.

## Module 8 — KQL for Security Analysis
Run queries against the authorized Log Analytics/Sentinel workspace. Start with a table available in your workspace, then practice:
```text
<TableName>
| take 20
```
Filtering:
```text
<TableName>
| where TimeGenerated > ago(1h)
| take 50
```
Aggregation:
```text
<TableName>
| where TimeGenerated > ago(24h)
| summarize Events=count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```
Replace `<TableName>` with a table actually present in your workspace. The syllabus does not specify a mandatory table/schema, so the lab must not invent one.

## Module 9 — Microsoft Defender XDR
1. Open the authorized Defender XDR tenant.
2. Review alerts/incidents relevant to the training dataset/environment.
3. Use Advanced Hunting where licensed/authorized.
4. Investigate evidence associated with Threat Detection, Defense Evasion, Execution, Credential Access, Privilege Escalation and Lateral Movement exercises.
5. Record evidence and remediation; do not run offensive activity against systems outside the dedicated lab.

## Cleanup
Remove only resources created for the training environment and preserve logs/evidence required by the course before cleanup.
