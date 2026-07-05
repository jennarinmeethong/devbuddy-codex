#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"
ZIP="$DIST/devbuddy-codex-skill.zip"

if [[ ! -f "$ROOT/skill/SKILL.md" ]]; then
  echo "Missing skill/SKILL.md under $ROOT" >&2
  exit 1
fi

mkdir -p "$DIST"
rm -f "$ZIP"

TEMP_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEMP_ROOT"' EXIT
mkdir -p "$TEMP_ROOT/devbuddy"
rsync -a --exclude ".DS_Store" "$ROOT/skill/" "$TEMP_ROOT/devbuddy/"

if command -v zip >/dev/null 2>&1; then
  (cd "$TEMP_ROOT" && zip -qr "$ZIP" devbuddy -x "*/.DS_Store" "__MACOSX/*")
else
  echo "zip is required to create $ZIP" >&2
  exit 1
fi

echo "Created $ZIP"
