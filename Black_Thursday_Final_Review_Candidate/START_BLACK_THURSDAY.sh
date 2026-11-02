#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  exec python3 launch_presentation.py
elif command -v python >/dev/null 2>&1; then
  exec python launch_presentation.py
else
  echo 'Python 3.11+ required for interactive mode.' >&2
  exit 1
fi
