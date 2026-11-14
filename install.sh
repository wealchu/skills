#!/usr/bin/env bash
# ChatGPT Office Skills: export reviewed source to a Codex workspace.
set -euo pipefail
OFFICE_SOURCE_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$OFFICE_SOURCE_ROOT/scripts/export_skills.py" "$@"
