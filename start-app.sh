#!/bin/bash
set -e

[ -f /opt/app/.env.production ] && set -a && . /opt/app/.env.production && set +a
export PORT="${PORT:-8080}"

cd /opt/app
exec /opt/app/.venv/bin/gunicorn --bind "0.0.0.0:${PORT}" app:app
