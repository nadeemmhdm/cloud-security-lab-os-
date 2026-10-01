# Admin Lab Server Model

Cloud Security Lab OS is one real self-hosted server shared by the administrator and explicitly allowed lab users.

## Administrator workflow
1. Install and start the server with the one-command installer.
2. Create the owner password.
3. Authenticate the host to the dedicated AWS training account and Azure training tenant/subscription.
4. Create Cloud Security Lab OS users.
5. Enable only the labs that are ready in the connected training environment.
6. Assign labs to specific users.
7. Monitor sessions, verification results and audit events.
8. Disable access when a course/lab is finished.

## Access model
- Owner: full server and lab administration.
- Admin: user/team management, lab enable/assignment, audit, terminal and lab access.
- Operator: terminal and assigned lab execution.
- Member: assigned lab execution plus normal file workspace.
- Viewer: assigned lab visibility only; no execution.

A disabled or unassigned lab cannot be started or verified by a normal user.

## Real lab lifecycle
Start performs a live AWS STS or Azure account authentication preflight and records a server-side session. The learner then performs the practical exercise through the real server terminal and connected official cloud tooling. Verify queries the real provider. Complete records completion. No fake AWS/Azure state is generated.

## Cloud isolation
Use dedicated training accounts/subscriptions rather than production. Admin is responsible for cloud IAM/RBAC, quotas, billing and resource cleanup. Never share the Cloud Security Lab OS owner account with students.

## Microsoft security services
Sentinel requires a real workspace and service configuration. KQL must execute against real available tables. Defender XDR requires an appropriately licensed tenant and API/role permissions. If those services are absent, the lab must remain unavailable rather than simulate data.
