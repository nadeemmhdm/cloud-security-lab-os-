# Worldwide Access and Boot Recovery

Cloud Security Lab OS runs on the owner's Windows 10/11 or Ubuntu computer. Cloudflare Tunnel provides the worldwide transport; the computer remains the origin server.

## Exposure model

- Web UI: publish only the Cloud OS loopback HTTP service through a Cloudflare Tunnel hostname.
- SSH: publish the host SSH service through a separate authenticated Cloudflare Access/Cloudflare One route. SSH is intended for administrators, not students.
- Other TCP services: add explicit allowlisted routes only when a lab actually needs them. Do not expose every host port.
- Students use the HTTPS Cloud OS application and can only authenticate with an account created by an Owner/Admin. Lab assignment is checked again server-side before start, verify, complete or reset.
- Host terminal and privileged commands remain Owner/Admin capabilities. A student lab must not inherit host administrator access.

Non-HTTP SSH/TCP clients may require cloudflared or the Cloudflare One Client on the remote client, depending on the selected Cloudflare access model.

## Reboot recovery

Both processes must be operating-system services:
1. Cloud Security Lab OS starts after networking and restarts on failure.
2. cloudflared starts at boot and reconnects the named tunnel automatically.

If the physical PC is powered off, the server is offline. Cloudflare cannot run the origin while that PC has no power. When the PC boots again, the OS services reconnect automatically and the same configured hostnames become reachable again.

For true availability while the PC is powered off, a second always-on origin/replica is required; this project does not pretend otherwise.

## Power configuration

The server machine should be configured not to sleep while acting as a server. Where supported by firmware, the owner can also enable restore-on-AC-power after a power failure. Cloud OS must not silently change BIOS/firmware power settings.

## Cloudflare secrets

Tunnel credentials/tokens are deployment secrets. Never commit them to this repository, expose them in the browser, include them in audit logs, or store them in ordinary application configuration.

## Lab lifecycle

Admin enables a lab and assigns it to a user. Start creates the user's isolated workspace. Verify checks actual host/workspace state. Complete records completion. Reset removes only that user's lab workspace/session. Curriculum modules referring to proprietary AWS/Microsoft products remain clearly labelled as local practical equivalents when no real provider is used.
