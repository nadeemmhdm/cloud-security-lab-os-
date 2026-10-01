#!/usr/bin/env bash
set -euo pipefail
PY="${PYTHON:-python3}"
command -v "$PY" >/dev/null 2>&1 || { echo "Python 3.10+ is required"; exit 1; }
"$PY" -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
cloud-os setup
echo "Installed. Start with: . .venv/bin/activate && cloud-os start"
