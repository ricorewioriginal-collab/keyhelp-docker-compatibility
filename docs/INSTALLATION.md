# Installation

## Requirements

- KeyHelp installation using the Bulma theme path used by current KeyHelp 26.x
- Ubuntu/Debian-like host with Apache, systemd, Python 3, sudo and OpenSSL
- root access

`install.sh` backs up the sidebar template, installs the manager/API/helpers, generates `/etc/keyhelp-docker-manager.secret`, installs sudoers/systemd/Apache integration, patches the sidebar between dedicated markers, and validates syntax.

KeyHelp is third-party software; template paths can change between releases. If the installer cannot find the expected sidebar file, it stops rather than guessing.
