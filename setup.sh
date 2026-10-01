#!/usr/bin/env bash
set -euo pipefail
echo "Cloud Security Lab OS - Ubuntu/Linux setup"
command -v python3 >/dev/null || { echo "Python 3.10+ is required"; exit 1; }
python3 -c 'import sys; assert sys.version_info >= (3,10), "Python 3.10+ required"'
[ -d .venv ] || python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m compileall -q cloud_os
python -m pytest -q
echo "Setup complete. No AWS/Azure CLI is required."
echo "Run .venv/bin/cloud-os setup, then install Cloud OS + cloudflared as boot services."
