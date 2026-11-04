#!/usr/bin/env bash
# scripts/install.sh - Install DevSpec Kit locally
set -e

DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Installing DevSpec Kit from $DIR..."

pip install -e "$DIR"

echo "Done! You can now use the 'devspec' command anywhere."
