# Security

This extension can perform privileged Docker operations. Treat access to the KeyHelp administrator area as privileged server access.

- Do not commit `/etc/keyhelp-docker-manager.secret`.
- The installer generates a random installation-specific token.
- Registry passwords/tokens are passed to `docker login --password-stdin`; do not paste credentials into issues.
- Review sudoers files before deployment.
- Keep KeyHelp, Docker and the host OS patched.
- Report suspected vulnerabilities privately to the repository owner rather than publishing secrets in an issue.
