# Lab Solution Guides

These guides follow the nine-module curriculum order used by Cloud Security Lab OS.

| Module | Guide | Runtime label |
|---|---|---|
| 1 | [Cloud Security Fundamentals](01-cloud-security-fundamentals.md) | Local Practical Lab |
| 2 | [AWS Identity & Access Security](02-aws-identity-access-security.md) | Local Practical Equivalent |
| 3 | [AWS Network Security](03-aws-network-security.md) | Local Practical Equivalent |
| 4 | [AWS Compute Security](04-aws-compute-security.md) | Local Practical Equivalent |
| 5 | [AWS Storage & Data Security](05-aws-storage-data-security.md) | Local Practical Equivalent |
| 6 | [Microsoft Azure Security](06-microsoft-azure-security.md) | Local Practical Equivalent |
| 7 | [Microsoft Sentinel & SIEM](07-microsoft-sentinel-siem.md) | Local SIEM Practical |
| 8 | [KQL for Security Analysis](08-kql-security-analysis.md) | Local Query Practical |
| 9 | [Microsoft Defender XDR](09-microsoft-defender-xdr.md) | Local XDR Concept Practical |

## Accuracy boundary
The server is self-hosted on Windows/Ubuntu and can be made worldwide-accessible through Cloudflare Tunnel. It does not become AWS, Azure, Microsoft Sentinel, the Microsoft KQL service, or Microsoft Defender XDR. Guides preserve those syllabus subjects while explicitly identifying the self-hosted equivalents.

## Access
Owner/Admin enables labs and assigns users. Students see only enabled labs assigned to them. Start/Verify/Complete/Reset are server-side permission checked.

## Verification status
Automated CI verifies cross-platform Python behavior, access isolation and the implemented local lab verifier. CI cannot prove that every command shown here is available on every Windows/Ubuntu edition because OS packages/features vary. Commands that require elevated rights are identified by the operating system through normal permission errors.
