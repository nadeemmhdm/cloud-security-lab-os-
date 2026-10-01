# Cloud Security Lab OS

A self-hosted cloud-security learning workstation built directly on the original Cloud OS codebase.

## What is real
Cloud Security Lab OS runs real host commands and reads real AWS/Azure accounts through the official AWS CLI and Azure CLI already authenticated on the host. The application does not contain fake cloud-resource simulators and does not commit provider credentials.

## Included curriculum
- AWS IAM: users, roles, policies, least privilege, access keys and misconfiguration review
- AWS VPC: subnets, security groups, NACLs, exposure and monitoring
- AWS EC2: open ports, patching, metadata, containers and hardening
- AWS S3: public access, permissions, encryption, data protection and snapshots
- Microsoft Entra ID, Azure IAM, networking, storage, compute and monitoring
- Microsoft Sentinel: SIEM, ingestion, detection rules, alerts and incident investigation
- KQL security analysis
- Microsoft Defender XDR investigation topics

## Provider setup
Install AWS CLI and authenticate it using an appropriate lab account/role. Install Azure CLI and authenticate with `az login`. Use dedicated training subscriptions/accounts and least-privilege identities. Cloud provider charges and quotas remain the operator's responsibility.

The dashboard/server credentials are separate from cloud-provider credentials. Never commit AWS access keys, Azure tokens, service-principal secrets, private keys, or Cloudflare tokens.

## Run
Python 3.10+ is required.

```bash
python -m venv .venv
python -m pip install -e ".[test]"
cloud-os setup
cloud-os start
```

Then sign in to Cloud OS. `GET /api/cloud/status` reports whether the provider CLIs are installed/authenticated. `GET /api/labs` exposes the curriculum and `POST /api/labs/{lab_id}/verify` performs real read-only provider verification.

## Security boundary
The existing Cloud OS host terminal is powerful and executes with the privileges of the Cloud OS process. Only trusted users should receive terminal access. Lab verification is intentionally read-only; resource creation/deletion should be performed deliberately with official provider tools in a dedicated training account.

## Testing
```bash
python -m compileall -q cloud_os
pytest -q
```
