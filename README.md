# KeyHelp Docker Compatibility

Community extension that integrates Docker management into the KeyHelp administrator interface.

> **Unofficial:** This project is not an official KeyHelp product and is not affiliated with KeyHelp/Keyweb AG. KeyHelp updates may change internal templates and require compatibility updates.

## Features

- Docker overview and container controls
- Docker installation view
- Compose projects / stacks
- Images, volumes and networks
- Update checks and backups
- Registry login/test/logout
- System information
- KeyHelp sidebar integration
- Request token, same-origin checks, audit logging and restricted sudo helpers

## Tested baseline

The original installation passed a 71-check final audit on KeyHelp 26.1.1 / Ubuntu 22.04 with Docker Engine 29.1.3 and Docker Compose v5.5.1. This is a tested baseline, not a guarantee for every KeyHelp/Docker version.

## Install

Run as root on a KeyHelp server:

```bash
git clone https://github.com/ricorewioriginal-collab/keyhelp-docker-compatibility.git
cd keyhelp-docker-compatibility
sudo ./install.sh
```

The installer creates a backup before modifying the KeyHelp sidebar. Reload KeyHelp with Ctrl+F5 after installation.

## Update / uninstall

```bash
sudo ./update.sh
sudo ./uninstall.sh
```

See `docs/INSTALLATION.md` and `SECURITY.md` before using this on a production server.

## License

MIT. KeyHelp and Docker are trademarks of their respective owners.
