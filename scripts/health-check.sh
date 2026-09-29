#!/usr/bin/env bash
set -u
fail=0
check(){ if eval "$2" >/dev/null 2>&1; then echo "[OK] $1"; else echo "[FAIL] $1"; fail=1; fi; }
check "Docker" "docker info"
check "CGI syntax" "python3 -m py_compile /home/keyhelp/www/keyhelp/docker-api/action.cgi"
check "Apache" "apache2ctl configtest"
check "Secret" "test -s /etc/keyhelp-docker-manager.secret"
check "Manager UI" "test -s /var/lib/keyhelp/docker-monitor/manager/index.html"
exit "$fail"
