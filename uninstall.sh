#!/usr/bin/env bash
set -Eeuo pipefail
[ "$(id -u)" -eq 0 ] || { echo "Run as root." >&2; exit 1; }
NAV="/home/keyhelp/www/keyhelp/theme/bulma/templates/components/nav/nav_sidebar.twig"
if [ -f "$NAV" ]; then python3 - "$NAV" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); s=p.read_text(); a='{# ricorewi-docker-navigation #}'; b='{# /ricorewi-docker-navigation #}'
if a in s and b in s:
 i=s.index(a); j=s.index(b,i)+len(b); p.write_text(s[:i]+s[j:])
PY
fi
for t in ricorewi-docker-status.timer ricorewi-docker-update-check.timer ricorewi-docker-backup.timer ricorewi-docker-project-status.timer; do systemctl disable --now "$t" 2>/dev/null || true; done
rm -f /etc/systemd/system/ricorewi-docker-{status,update-check,backup,project-status}.{service,timer}
rm -rf /etc/systemd/system/ricorewi-docker-status.service.d
rm -f /etc/sudoers.d/keyhelp-docker-{manager,network,registry}
rm -f /usr/local/sbin/ricorewi-docker-*
a2disconf keyhelp-docker-manager >/dev/null 2>&1 || true
rm -f /etc/apache2/conf-available/keyhelp-docker-manager.conf
rm -rf /var/lib/keyhelp/docker-monitor/manager /home/keyhelp/www/keyhelp/docker-api
systemctl daemon-reload; apache2ctl configtest; systemctl reload apache2
echo "Uninstalled. /etc/keyhelp-docker-manager.secret was intentionally retained; delete it manually if no longer needed."
