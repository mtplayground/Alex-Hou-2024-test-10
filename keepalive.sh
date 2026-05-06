#!/bin/bash
set -e

while true; do
  curl --silent --show-error --fail --max-time 5 http://127.0.0.1:8080/ >/dev/null 2>&1 || true
  sleep 20
done
