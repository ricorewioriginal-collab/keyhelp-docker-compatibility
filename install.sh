#!/usr/bin/env bash
set -Eeuo pipefail
[ "$(id -u)" -eq 0 ] || { echo "Run as root." >&2; exit 1; }
ROOT="$(cd "$(dirname "$0")" && pwd)"
NAV="/home/keyhelp/www/keyhelp/theme/bulma/templates/components/nav/nav_sidebar.twig"
[ -f "$NAV" ] || { echo "KeyHelp sidebar not found: $NAV" >&2; exit 1; }
for c in python3 openssl sudo apache2ctl install visudo; do command -v "$c" >/dev/null || { echo "Missing: $c" >&2; exit 1; }; done
STAMP="$(date +%Y%m%d-%H%M%S)"; BACKUP="/root/keyhelp-docker-compatibility-$STAMP"; mkdir -p "$BACKUP"
cp -a "$NAV" "$BACKUP/nav_sidebar.twig"
[ -f /etc/keyhelp-docker-manager.secret ] && cp -a /etc/keyhelp-docker-manager.secret "$BACKUP/" || true
install -d -m 0755 /var/lib/keyhelp/docker-monitor/manager /home/keyhelp/www/keyhelp/docker-api
install -m 0644 "$ROOT/manager/index.html" /var/lib/keyhelp/docker-monitor/manager/index.html
install -m 0755 "$ROOT/api/action.cgi" /home/keyhelp/www/keyhelp/docker-api/action.cgi
for f in "$ROOT"/helpers/*; do install -m 0755 "$f" "/usr/local/sbin/$(basename "$f")"; done
if [ ! -s /etc/keyhelp-docker-manager.secret ]; then openssl rand -hex 32 > /etc/keyhelp-docker-manager.secret; fi
chown root:keyhelp /etc/keyhelp-docker-manager.secret; chmod 0640 /etc/keyhelp-docker-manager.secret
TOKEN="$(cat /etc/keyhelp-docker-manager.secret)"
python3 - "$NAV" "$ROOT/keyhelp/nav_sidebar.twig" "$TOKEN" <<'PY'
from pathlib import Path
import sys
nav=Path(sys.argv[1]); template=Path(sys.argv[2]).read_text(); token=sys.argv[3]
start='{# ricorewi-docker-navigation #}'; end='{# /ricorewi-docker-navigation #}'; s=nav.read_text()
block=template[template.index(start):template.index(end)+len(end)].replace('__KEYHELP_DOCKER_TOKEN__',token)
if start in s and end in s:
 a=s.index(start); b=s.index(end,a)+len(end); s=s[:a]+block+s[b:]
else:
 pos=s.find('>')
 if pos < 0: raise SystemExit('Could not locate opening nav tag')
 s=s[:pos+1]+'\n\n    '+block+'\n'+s[pos+1:]
nav.write_text(s)
PY
for f in "$ROOT"/sudoers/*; do install -m 0440 "$f" "/etc/sudoers.d/$(basename "$f")"; done
visudo -cf /etc/sudoers >/dev/null
for f in "$ROOT"/systemd/*; do [ -f "$f" ] && install -m 0644 "$f" "/etc/systemd/system/$(basename "$f")"; done
if [ -d "$ROOT/systemd/ricorewi-docker-status.service.d" ]; then install -d /etc/systemd/system/ricorewi-docker-status.service.d; install -m 0644 "$ROOT/systemd/ricorewi-docker-status.service.d/"* /etc/systemd/system/ricorewi-docker-status.service.d/; fi
install -m 0644 "$ROOT/apache/keyhelp-docker-manager.conf" /etc/apache2/conf-available/keyhelp-docker-manager.conf
a2enmod cgi >/dev/null; a2enconf keyhelp-docker-manager >/dev/null
python3 -m py_compile /home/keyhelp/www/keyhelp/docker-api/action.cgi
apache2ctl configtest
systemctl daemon-reload
for t in ricorewi-docker-status.timer ricorewi-docker-update-check.timer ricorewi-docker-backup.timer ricorewi-docker-project-status.timer; do [ -f "/etc/systemd/system/$t" ] && systemctl enable --now "$t"; done
/usr/local/sbin/ricorewi-docker-status || true
/usr/local/sbin/ricorewi-docker-project-status || true
systemctl reload apache2
echo "Installed. Backup: $BACKUP"
