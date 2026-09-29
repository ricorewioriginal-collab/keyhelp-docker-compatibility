# KeyHelp Docker Compatibility

[Deutsch](#deutsch) · [English](#english)

> **Inoffizielles Community-Projekt / Unofficial community project**  
> Dieses Projekt ist kein offizielles Produkt von KeyHelp/Keyweb AG und steht nicht mit KeyHelp/Keyweb AG in Verbindung.  
> This project is not an official KeyHelp/Keyweb AG product and is not affiliated with KeyHelp/Keyweb AG.

---

# Deutsch

## Über das Projekt

**KeyHelp Docker Compatibility** erweitert die KeyHelp-Administratoroberfläche um eine integrierte Docker-Verwaltung. Ziel ist, häufig benötigte Docker-Funktionen direkt innerhalb von KeyHelp erreichbar zu machen, ohne für jede alltägliche Aktion auf die Shell wechseln zu müssen.

Das Projekt entstand aus einer produktiv eingesetzten KeyHelp-/Docker-Installation und wurde anschließend für eine öffentliche Community-Version bereinigt und verallgemeinert.

## Funktionen

- Docker-Übersicht und Container-Verwaltung
- Container starten, stoppen und neu starten
- Container-Logs und Inspect
- Docker-Installationsansicht
- Docker Compose Projekte / Stacks
- Git-basierte Projektbereitstellung
- Image-Verwaltung einschließlich Pull und Bereinigung
- Volume-/Storage-Verwaltung einschließlich Inspect
- Docker-Netzwerkverwaltung
- Registry Login, Test und Logout
- Update-Prüfungen
- Backup-Funktionen
- Systeminformationen
- Integration in die KeyHelp-Seitennavigation
- Request-Token und Same-Origin-Prüfungen
- Audit-Logging
- eingeschränkte sudo-Helper statt uneingeschränktem Docker-Zugriff aus der Weboberfläche

## Getestete Ausgangsbasis

Die ursprüngliche Installation bestand den abschließenden technischen Audit mit:

- **71 erfolgreichen Prüfungen**
- **0 kritischen Fehlern**

Getestete Umgebung:

- KeyHelp **26.1.1 (Build 3698)**
- Ubuntu **22.04 LTS, 64 Bit**
- Docker Engine **29.1.3**
- Docker Compose **v5.5.1**

Diese Angaben beschreiben die getestete Ausgangsbasis. Sie sind **keine Garantie**, dass jede andere oder zukünftige Version von KeyHelp, Ubuntu oder Docker ohne Anpassungen funktioniert.

## Voraussetzungen

- bestehende KeyHelp-Installation
- Linux-System mit Root-Zugriff
- Git
- Bash
- Python 3
- Apache/KeyHelp-Webserverumgebung

Docker kann abhängig vom vorhandenen System über die Erweiterung bzw. die vorgesehenen Installationsfunktionen eingerichtet werden.

## Installation

Vor der Installation auf einem produktiven Server sollte ein vollständiges Backup oder ein Server-Snapshot erstellt werden.

Repository klonen:

```bash
git clone https://github.com/ricorewioriginal-collab/keyhelp-docker-compatibility.git
cd keyhelp-docker-compatibility
```

Installer als Root ausführen:

```bash
sudo bash ./install.sh
```

Der Installer erstellt vor Änderungen an der KeyHelp-Navigation ein Backup und richtet die benötigten Komponenten ein.

Anschließend die KeyHelp-Administratoroberfläche mit **Strg+F5** vollständig neu laden.

## Aktualisieren

Im Repository-Verzeichnis:

```bash
git pull --ff-only
sudo bash ./update.sh
```

`update.sh` installiert die aktuell ausgecheckte Repository-Version erneut. Deshalb zuerst `git pull --ff-only` ausführen, wenn auf den neuesten Stand aktualisiert werden soll.

Vor größeren Updates empfiehlt sich erneut ein Snapshot oder Backup.

## Deinstallation

```bash
sudo bash ./uninstall.sh
```

## Sicherheit

Die öffentliche Version verwendet unter anderem:

- ein installationsspezifisches Secret
- Same-Origin-Prüfungen
- Request-Authentifizierung
- Audit-Logging
- gezielt eingeschränkte sudo-Helper

Vor dem Einsatz auf einem öffentlich erreichbaren Produktivserver bitte **`SECURITY.md`** lesen.

Docker-Verwaltung besitzt naturgemäß weitreichende Rechte auf einem Server. Installiere diese Erweiterung daher nur auf Systemen, die du administrierst und deren Sicherheitsmodell du kontrollierst.

## Dokumentation

Weitere Informationen befinden sich in:

- `docs/INSTALLATION.md`
- `SECURITY.md`
- `CHANGELOG.md`

## Fehler und Beiträge

Fehlerberichte, Verbesserungsvorschläge und Beiträge aus der Community sind willkommen. Bei Fehlerberichten sollten nach Möglichkeit KeyHelp-Version, Betriebssystem, Docker-Version und die konkrete Fehlermeldung angegeben werden. Zugangsdaten, Tokens, Passwörter und andere Secrets dürfen nicht in Issues veröffentlicht werden.

## Lizenz und Marken

Der Quellcode dieses Projekts steht unter der **MIT-Lizenz**. Siehe `LICENSE`.

KeyHelp und Docker sind Marken ihrer jeweiligen Rechteinhaber. Die Verwendung der Namen dient ausschließlich der Beschreibung der Kompatibilität bzw. Integration.

---

# English

## About the project

**KeyHelp Docker Compatibility** extends the KeyHelp administrator interface with integrated Docker management. Its goal is to make frequently used Docker operations available directly inside KeyHelp without requiring administrators to switch to the shell for every routine action.

The project originated from a production KeyHelp/Docker installation and was subsequently cleaned up and generalized for a public community release.

## Features

- Docker overview and container management
- Start, stop and restart containers
- Container logs and inspect
- Docker installation view
- Docker Compose projects / stacks
- Git-based project deployment
- Image management including pull and cleanup
- Volume/storage management including inspect
- Docker network management
- Registry login, test and logout
- Update checks
- Backup functions
- System information
- KeyHelp sidebar integration
- Request-token and same-origin checks
- Audit logging
- restricted sudo helpers instead of unrestricted Docker access from the web interface

## Tested baseline

The original installation passed the final technical audit with:

- **71 successful checks**
- **0 critical errors**

Tested environment:

- KeyHelp **26.1.1 (Build 3698)**
- Ubuntu **22.04 LTS, 64-bit**
- Docker Engine **29.1.3**
- Docker Compose **v5.5.1**

This describes the tested baseline. It is **not a guarantee** that every other or future KeyHelp, Ubuntu or Docker version will work without adjustments.

## Requirements

- an existing KeyHelp installation
- Linux system with root access
- Git
- Bash
- Python 3
- Apache/KeyHelp web-server environment

Depending on the existing system, Docker can be installed using the extension or its provided installation functions.

## Installation

Create a complete backup or server snapshot before installing the extension on a production server.

Clone the repository:

```bash
git clone https://github.com/ricorewioriginal-collab/keyhelp-docker-compatibility.git
cd keyhelp-docker-compatibility
```

Run the installer as root:

```bash
sudo bash ./install.sh
```

The installer creates a backup before modifying the KeyHelp navigation and installs the required components.

After installation, perform a full reload of the KeyHelp administrator interface using **Ctrl+F5**.

## Updating

From the repository directory:

```bash
git pull --ff-only
sudo bash ./update.sh
```

`update.sh` reinstalls the currently checked-out repository version. Run `git pull --ff-only` first when you want to update to the latest revision.

Creating another snapshot or backup before major updates is recommended.

## Uninstalling

```bash
sudo bash ./uninstall.sh
```

## Security

The public version uses, among other measures:

- a per-installation secret
- same-origin validation
- request authentication
- audit logging
- purpose-specific restricted sudo helpers

Please read **`SECURITY.md`** before deploying the extension on a publicly reachable production server.

Docker management inherently provides extensive control over a server. Only install this extension on systems you administer and whose security model you control.

## Documentation

Additional information is available in:

- `docs/INSTALLATION.md`
- `SECURITY.md`
- `CHANGELOG.md`

## Issues and contributions

Bug reports, improvements and community contributions are welcome. When reporting a problem, please include the KeyHelp version, operating system, Docker version and the exact error message whenever possible. Never publish credentials, tokens, passwords or other secrets in an issue.

## License and trademarks

The source code of this project is licensed under the **MIT License**. See `LICENSE`.

KeyHelp and Docker are trademarks of their respective owners. Their names are used solely to describe compatibility and integration.
