#!/usr/bin/env bash
# scripts/devspec.sh - Direct runner for DevSpec CLI
set -e

DIR="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="$DIR:$PYTHONPATH"

python3 -m devspec.cli "$@"
