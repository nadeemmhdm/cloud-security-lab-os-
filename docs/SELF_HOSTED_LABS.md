# Self-hosted Lab Architecture

Cloud Security Lab OS turns the user's own Windows or Ubuntu computer into the lab server. It does not require an AWS account, Azure subscription, or another cloud server.

## Supported host model
The application detects the host at runtime. Windows hosts use real PowerShell when available. Ubuntu/Linux hosts use real Bash. If both shells are installed, both can be exposed by the terminal.

The server records OS family/version, architecture, logical CPU count, available shells, Docker/Podman availability and WSL detection. Unsupported hosts are reported rather than silently treated as supported.

## Curriculum mapping
The nine syllabus modules remain named after their curriculum subjects. Modules that describe proprietary AWS or Microsoft services are marked **Local Practical Equivalent**, **Local SIEM Practical**, **Local Query Practical**, or **Local XDR Concept Practical**. They are not presented as genuine AWS/Azure/Sentinel/Defender cloud services.

The local labs teach and exercise the corresponding identity, permissions, networking, compute, storage, logging, querying and investigation concepts on the user's own server.

## User model
Owner/Admin enables labs and assigns them to users. Instructor can manage labs without owner privileges. Student can run only enabled labs assigned to that account. Lab workspaces are stored separately by username and lab ID.

## Lifecycle
- Start: creates/prepares the user's real local lab workspace.
- Terminal: executes the installed host PowerShell/Bash.
- Verify: inspects real host/workspace state.
- Complete: records completion.
- Reset: removes that user's lab workspace/session so it can be rebuilt.

## Important terminology
A self-hosted local equivalent is not AWS EC2, AWS IAM, Microsoft Entra ID, Sentinel, or Defender XDR. Those names are retained because they are syllabus modules; the UI mode label states when the practical environment is a local equivalent.
