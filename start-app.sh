#!/bin/bash
set -e

[ -f /opt/app/.env.production ] && set -a && . /opt/app/.env.production && set +a
export PORT="${PORT:-8080}"

cd /opt/app
: > /.sprite/logs/services/app.log 2>/dev/null || true
exec /opt/app/.venv/bin/gunicorn --bind "0.0.0.0:${PORT}" app:app
