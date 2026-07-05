#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/skills/devbuddy"

if [[ ! -f "$ROOT/skill/SKILL.md" ]]; then
  echo "Missing skill/SKILL.md under $ROOT" >&2
  exit 1
fi

mkdir -p "$DEST"
rsync -a --delete --exclude ".DS_Store" "$ROOT/skill/" "$DEST/"

echo "Installed DevBuddy Codex skill to $DEST"
echo "Start a fresh Codex thread for the skill list to refresh."
