#!/usr/bin/env bash
set -euo pipefail
echo "Cloud Security Lab OS - one command setup"
command -v python3 >/dev/null || { echo "Python 3.10+ is required"; exit 1; }
python3 -c 'import sys; assert sys.version_info >= (3,10), "Python 3.10+ required"'
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m compileall -q cloud_os
python -m pytest -q
echo "Setup complete."
echo "First time: .venv/bin/cloud-os setup"
echo "Start:      .venv/bin/cloud-os start"
echo "Install AWS CLI/Azure CLI with your distro/vendor package instructions, then authenticate."
