# Azure, Sentinel, KQL and Defender XDR Practical Labs — Complete Solve Guide

Use only a Microsoft tenant/subscription you own or are authorized to administer. Licensing and permissions determine which Sentinel and Defender XDR exercises are available.

## Module 6 — Microsoft Azure Security
Authenticate: `az login`; confirm subscription: `az account show`. Use a dedicated resource group: `az group create --name cslab-rg --location centralindia`. Review role assignments with `az role assignment list --all`. Review NSGs with `az network nsg list -g cslab-rg`, storage accounts with `az storage account list -g cslab-rg`, VMs with `az vm list -g cslab-rg -d`, and monitoring configuration with Azure Monitor commands appropriate to your workspace. Apply least privilege and avoid public management ports. Delete the dedicated resource group after all exercises if it contains only disposable lab resources: `az group delete --name cslab-rg --yes --no-wait`.

## Module 7 — Microsoft Sentinel & SIEM
Use an authorized Log Analytics workspace with Microsoft Sentinel enabled. Connect approved data sources, confirm ingestion in the workspace, create detection/analytics rules for your own test telemetry, review generated alerts, and investigate incidents in Sentinel. Do not manufacture production incidents or connect data you are not authorized to process. Cloud Security Lab OS verifies Azure connectivity; Sentinel availability still depends on workspace configuration, RBAC and licensing.

## Module 8 — KQL for Security Analysis
Run KQL against the real Log Analytics/Sentinel workspace. Start with `SecurityEvent | take 20` where that table exists. Filtering: `SecurityEvent | where TimeGenerated > ago(1h) | take 50`. Sorting: `SecurityEvent | sort by TimeGenerated desc | take 50`. Aggregation: `SecurityEvent | summarize Events=count() by EventID | sort by Events desc`. If your workspace does not ingest `SecurityEvent`, use a table that your connected data source actually provides rather than treating an empty/nonexistent table as a lab failure.

## Module 9 — Microsoft Defender XDR
In an appropriately licensed and authorized Defender XDR tenant, review incidents/alerts and use Advanced Hunting against your own tenant telemetry. Map observed events to the syllabus topics: Threat Detection, Defense Evasion, Execution, Credential Access, Privilege Escalation and Lateral Movement. Investigation is defensive: validate device/user/timestamp/process evidence, scope affected assets, document findings, and follow your organization's containment procedure. Availability of specific hunting tables varies with products, licensing and onboarded data.

## Verification
Cloud Security Lab OS uses the real Azure CLI account context. A successful Azure verification confirms the CLI is installed, authenticated and can query the selected subscription. Sentinel/KQL/Defender exercises additionally require the corresponding Microsoft services and permissions.
