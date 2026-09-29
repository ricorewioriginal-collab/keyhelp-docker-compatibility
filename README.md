# KeyHelp Docker Compatibility

[Deutsch](#deutsch) · [English](#english)

> **Inoffizielles Community-Projekt / Unofficial community project**  
> Dieses Projekt ist kein offizielles Produkt von KeyHelp/Keyweb AG und steht nicht mit KeyHelp/Keyweb AG in Verbindung.  
> This project is not an official KeyHelp/Keyweb AG product and is not affiliated with KeyHelp/Keyweb AG.

---

# Deutsch

## Über das Projekt

**KeyHelp Docker Compatibility** erweitert die KeyHelp-Administratoroberfläche um eine integrierte Docker-Verwaltung. Die Erweiterung fügt Docker als eigenen Bereich in KeyHelp ein und stellt die wichtigsten Verwaltungsfunktionen über eine grafische Oberfläche bereit.

Das Projekt entstand aus einer produktiv eingesetzten KeyHelp-/Docker-Installation und wurde anschließend für eine öffentliche Community-Version bereinigt und verallgemeinert.

## Funktionen im Detail

### Übersicht

Die Übersichtsseite fasst den aktuellen Docker-Zustand zusammen. Sie dient als Einstiegspunkt, um laufende Container und den allgemeinen Zustand der Docker-Umgebung schnell zu überblicken.

### Container

Vorhandene Docker-Container werden innerhalb von KeyHelp angezeigt. Je nach Zustand stehen Verwaltungsaktionen zur Verfügung:

- **Start** – startet einen gestoppten Container.
- **Stop** – beendet einen laufenden Container.
- **Neustart** – startet einen laufenden Container neu.
- **Logs** – zeigt die Container-Ausgabe bzw. Docker-Logs an.
- **Inspect** – zeigt die von Docker gelieferten technischen Detailinformationen an.
- **Details** – zeigt aufbereitete Informationen wie CPU-/RAM-Nutzung, PIDs, Netzwerk-I/O, Block-I/O, Restart-Policy, Startzeit, Ports, Netzwerke und Mounts.
- **Update** – führt die für die Erweiterung vorgesehene Container-/Image-Aktualisierung aus.
- **Entfernen** – entfernt einen gestoppten Container, sofern die Aktion angeboten wird.

### Docker installieren

Der Bereich **Installieren** ist für die Einrichtung von Docker bzw. für unterstützte Installationswege vorgesehen. Damit kann die Docker-Integration auch auf einem KeyHelp-System vorbereitet werden, auf dem Docker noch nicht vollständig eingerichtet ist.

### Projekte / Stacks

Dieser Bereich verwaltet Docker-Compose-Projekte als zusammengehörige Stacks. Unterstützt werden im Backend unter anderem:

- Projekt starten
- Projekt stoppen
- Projekt neu starten
- Images eines Projekts abrufen (`pull`)
- Projekt bauen (`build`)
- Projekt bereitstellen (`deploy`)
- Git-basierte Bereitstellung
- Projekt-Logs anzeigen
- Projekt-Konfiguration anzeigen
- Compose-Projekt herunterfahren (`down`)
- Git-/Compose-basierte Projekte einrichten

Die Projekterkennung wird über einen eigenen Status-Collector aktualisiert.

### Images

Installierte Docker-Images werden mit Repository, Tag, Größe und Erstellungsinformationen dargestellt.

Mögliche Aktionen:

- **Pull** – lädt die aktuelle Version einer angegebenen Image-Referenz herunter.
- **Löschen** – entfernt ein Image, sofern Docker dies zulässt.
- **Ungenutzte bereinigen** – entfernt nicht mehr benötigte Images über die vorgesehene Bereinigungsfunktion.

Docker-Image-Referenzen wie `nginx:latest`, `library/nginx:latest` oder Registry-Pfade werden vom Backend gesondert validiert.

### Volumes / Storage

Docker-Volumes werden mit technischen Informationen angezeigt. Der Bereich unterstützt unter anderem:

- vorhandene Volumes auflisten
- neues Volume erstellen
- Volume untersuchen (**Inspect**)
- Mountpoint und Treiber anzeigen
- Verwendung eines Volumes nachvollziehen
- nicht verwendete Volumes löschen

Löschaktionen sollten besonders auf Produktivsystemen nur durchgeführt werden, wenn sicher ist, dass die enthaltenen persistenten Daten nicht mehr benötigt werden.

### Netzwerke

Docker-Netzwerke können direkt in KeyHelp verwaltet werden. Der Manager unterstützt:

- Netzwerke auflisten
- neues Netzwerk erstellen
- Netzwerk untersuchen (**Inspect**)
- Treiber, Scope und IPAM-Informationen anzeigen
- Subnetz, Gateway und IP-Range anzeigen
- interne Netzwerke erkennen
- Container mit einem Netzwerk verbinden
- Container von einem Netzwerk trennen
- unbenutzte Netzwerke entfernen

Docker-Systemnetzwerke wie `bridge`, `host` und `none` werden in der Oberfläche besonders berücksichtigt und sollen nicht wie normale benutzerdefinierte Netzwerke behandelt werden.

### Ports / Endpoints

Der Bereich **Ports / Endpoints** bereitet veröffentlichte und interne Container-Ports übersichtlich auf. Dadurch lässt sich leichter erkennen, welche Dienste nach außen gebunden sind und welche Ports nur intern oder lokal verwendet werden.

### Updates

Der Update-Bereich prüft Container bzw. verwendete Images auf den von der Erweiterung ermittelten Aktualisierungsstatus. Für erkannte Aktualisierungen kann die vorgesehene Update-Aktion gestartet werden. Die Oberfläche zeigt außerdem den Zeitpunkt der letzten Prüfung an.

### Backups

Der Backup-Bereich bindet die vorgesehenen Docker-Backup-Funktionen ein. Ziel ist, relevante Container-/Compose-Konfigurationen und persistente Docker-Daten vor kritischen Änderungen sichern zu können.

Ein Docker-Backup ersetzt kein vollständiges Server- oder VM-Backup. Vor größeren Änderungen an einem Produktivserver wird zusätzlich ein Snapshot bzw. vollständiges Systembackup empfohlen.

### Registry

Private oder öffentliche Docker-Registries können über den Manager verwaltet werden. Unterstützt werden:

- Registry-Anmeldungen auflisten
- Registry-Login
- Benutzername und Passwort/Token übergeben
- Registry-Verbindung testen
- Registry-Logout

Passwörter bzw. Tokens sollen nicht in Audit-Ausgaben protokolliert werden. Registry-Ziele werden vor der Übergabe an die Helper validiert.

### System

Der System-Bereich stellt Docker- und Hostinformationen bereit, die für Diagnose und Administration relevant sind. Dazu gehören die vom installierten Monitoring/Status-System gelieferten Systemdaten.

### Hilfe

Der Hilfe-Bereich erklärt Bedienung und sicherheitsrelevante Hinweise direkt innerhalb des Docker Managers.

## Integration in KeyHelp

Die Erweiterung ergänzt die KeyHelp-Seitennavigation und öffnet die einzelnen Docker-Bereiche innerhalb der Administratoroberfläche. Unterstützte Views sind:

`Übersicht`, `Container`, `Installieren`, `Projekte / Stacks`, `Images`, `Volumes`, `Netzwerke`, `Ports / Endpoints`, `Updates`, `Backups`, `Registry`, `System` und `Hilfe`.

## Sicherheitskonzept

Die Weboberfläche führt Docker-Befehle nicht beliebig direkt als Root aus. Die öffentliche Version verwendet mehrere Schutzschichten:

- installationsspezifisches Secret
- Request-Authentifizierung zwischen KeyHelp-Integration und Docker-API
- Same-Origin-Prüfungen
- Eingabevalidierung für Ziele und Aktionen
- Allowlist unterstützter Aktionen
- gezielt eingeschränkte sudo-Helper
- getrennte Helper für allgemeine Docker-, Projekt- und Registry-Aktionen
- Audit-Logging
- Zeitlimits für Backend-Aktionen
- keine beabsichtigte Protokollierung von Registry-Passwörtern oder Tokens

Docker-Verwaltung besitzt trotzdem weitreichende Serverrechte. Die Erweiterung sollte deshalb nur auf Systemen eingesetzt werden, die vom jeweiligen Administrator kontrolliert werden.

## Getestete Ausgangsbasis

Die ursprüngliche Installation bestand den abschließenden technischen Audit mit:

- **71 erfolgreichen Prüfungen**
- **0 kritischen Fehlern**

Getestete Umgebung:

- KeyHelp **26.1.1 (Build 3698)**
- Ubuntu **22.04 LTS, 64 Bit**
- Docker Engine **29.1.3**
- Docker Compose **v5.5.1**

Dies ist die getestete Ausgangsbasis und keine Garantie für jede andere oder zukünftige KeyHelp-, Ubuntu- oder Docker-Version.

## Installation

Vor der Installation auf einem Produktivserver unbedingt ein vollständiges Backup oder einen Server-Snapshot erstellen.

```bash
git clone https://github.com/ricorewioriginal-collab/keyhelp-docker-compatibility.git
cd keyhelp-docker-compatibility
sudo bash ./install.sh
```

Der Installer sichert die betroffene KeyHelp-Navigation vor der Änderung und richtet die benötigten Komponenten ein. Danach KeyHelp mit **Strg+F5** vollständig neu laden.

## Aktualisieren

```bash
cd keyhelp-docker-compatibility
git pull --ff-only
sudo bash ./update.sh
```

`update.sh` installiert die aktuell ausgecheckte Repository-Version erneut.

## Deinstallation

```bash
sudo bash ./uninstall.sh
```

## Dokumentation

Siehe zusätzlich:

- `docs/INSTALLATION.md`
- `SECURITY.md`
- `CHANGELOG.md`

## Fehler und Beiträge

Fehlerberichte und Beiträge aus der Community sind willkommen. Bitte nach Möglichkeit KeyHelp-Version, Betriebssystem, Docker-Version und die konkrete Fehlermeldung angeben. **Keine Passwörter, Tokens, Zugangsdaten oder sonstigen Secrets in Issues veröffentlichen.**

## Lizenz und Marken

MIT-Lizenz – siehe `LICENSE`.

KeyHelp und Docker sind Marken ihrer jeweiligen Rechteinhaber. Die Namen werden ausschließlich zur Beschreibung der Kompatibilität und Integration verwendet.

---

# English

## About the project

**KeyHelp Docker Compatibility** extends the KeyHelp administrator interface with integrated Docker management. It adds Docker as a dedicated KeyHelp area and exposes common administration tasks through a graphical interface.

The project originated from a production KeyHelp/Docker installation and was subsequently cleaned up and generalized for a public community release.

## Features in detail

### Overview

The overview summarizes the current Docker state and provides a quick entry point for checking running containers and the general Docker environment.

### Containers

Existing Docker containers are displayed inside KeyHelp. Depending on their state, the manager provides actions including:

- **Start** – start a stopped container.
- **Stop** – stop a running container.
- **Restart** – restart a running container.
- **Logs** – display Docker/container logs.
- **Inspect** – display technical information returned by Docker inspect.
- **Details** – show prepared information such as CPU/RAM usage, PIDs, network I/O, block I/O, restart policy, start time, ports, networks and mounts.
- **Update** – run the container/image update operation provided by the extension.
- **Remove** – remove a stopped container when the action is available.

### Install Docker

The **Install** area provides the supported setup paths for Docker and the Docker integration. It is intended to help prepare KeyHelp systems where Docker has not yet been fully configured.

### Projects / Stacks

Docker Compose projects are managed as related stacks. Backend operations include:

- start project
- stop project
- restart project
- pull project images
- build project
- deploy project
- Git-based deployment
- display project logs
- display project configuration
- bring a Compose project down
- set up Git-/Compose-based projects

A dedicated project status collector refreshes detected project information.

### Images

Installed Docker images are displayed with repository, tag, size and creation information.

Available operations include:

- **Pull** – download the current version of an image reference.
- **Delete** – remove an image when Docker permits it.
- **Prune unused images** – invoke the provided cleanup operation for unused images.

Docker image references such as `nginx:latest`, `library/nginx:latest` and registry paths are validated separately by the backend.

### Volumes / Storage

Docker volumes are displayed together with technical information. The manager supports:

- listing existing volumes
- creating a new volume
- inspecting a volume
- displaying mountpoint and driver
- identifying volume usage
- deleting unused volumes

Be especially careful with deletion on production systems because volumes commonly contain persistent application data.

### Networks

Docker networks can be managed directly from KeyHelp. Supported functions include:

- list networks
- create a network
- inspect a network
- display driver, scope and IPAM information
- display subnet, gateway and IP range
- identify internal networks
- connect a container to a network
- disconnect a container from a network
- remove unused networks

Docker system networks such as `bridge`, `host` and `none` are treated specially by the interface and should not be handled like ordinary user-created networks.

### Ports / Endpoints

The **Ports / Endpoints** view summarizes published and internal container ports. It helps administrators identify services exposed externally and distinguish them from locally bound or internal endpoints.

### Updates

The update view checks containers and their images for the update state determined by the extension. When an update is detected, the provided update operation can be started. The interface also displays the time of the most recent check.

### Backups

The backup area integrates the project's Docker backup functions. It is intended to preserve relevant container/Compose configuration and persistent Docker data before critical changes.

A Docker-level backup is not a replacement for a complete server or VM backup. A full snapshot or system backup is recommended before major production changes.

### Registry

Private and public Docker registries can be managed through the interface. Supported operations include:

- list configured/authenticated registries
- registry login
- pass username and password/token to the login helper
- test registry access
- registry logout

Passwords and tokens are not intended to be written to audit output. Registry targets are validated before being passed to backend helpers.

### System

The System view displays Docker and host information relevant to diagnostics and administration, based on the installed monitoring/status components.

### Help

The Help view provides operating and security guidance directly inside Docker Manager.

## KeyHelp integration

The extension adds Docker entries to the KeyHelp sidebar and opens the individual Docker views within the administrator interface. Available views include:

`Overview`, `Containers`, `Install`, `Projects / Stacks`, `Images`, `Volumes`, `Networks`, `Ports / Endpoints`, `Updates`, `Backups`, `Registry`, `System` and `Help`.

## Security model

The web interface does not intentionally expose arbitrary root shell execution. The public version uses several layers of protection:

- per-installation secret
- request authentication between the KeyHelp integration and Docker API
- same-origin validation
- input validation for targets and operations
- allowlisted backend actions
- purpose-specific restricted sudo helpers
- separate helpers for general Docker, project and registry operations
- audit logging
- backend operation timeouts
- registry passwords/tokens are not intended to be written to audit logs

Docker administration still provides extensive control over a server. Deploy the extension only on systems administered and controlled by you.

## Tested baseline

The original installation passed its final technical audit with:

- **71 successful checks**
- **0 critical errors**

Tested environment:

- KeyHelp **26.1.1 (Build 3698)**
- Ubuntu **22.04 LTS, 64-bit**
- Docker Engine **29.1.3**
- Docker Compose **v5.5.1**

This is a tested baseline, not a guarantee for every other or future KeyHelp, Ubuntu or Docker version.

## Installation

Create a full backup or server snapshot before installing on a production system.

```bash
git clone https://github.com/ricorewioriginal-collab/keyhelp-docker-compatibility.git
cd keyhelp-docker-compatibility
sudo bash ./install.sh
```

The installer backs up the affected KeyHelp navigation before modifying it and installs the required components. Afterwards, fully reload KeyHelp with **Ctrl+F5**.

## Updating

```bash
cd keyhelp-docker-compatibility
git pull --ff-only
sudo bash ./update.sh
```

`update.sh` reinstalls the currently checked-out repository version.

## Uninstalling

```bash
sudo bash ./uninstall.sh
```

## Documentation

See also:

- `docs/INSTALLATION.md`
- `SECURITY.md`
- `CHANGELOG.md`

## Issues and contributions

Bug reports and community contributions are welcome. Whenever possible, include the KeyHelp version, operating system, Docker version and exact error message. **Never publish passwords, tokens, credentials or other secrets in issues.**

## License and trademarks

MIT License – see `LICENSE`.

KeyHelp and Docker are trademarks of their respective owners. Their names are used solely to describe compatibility and integration.
