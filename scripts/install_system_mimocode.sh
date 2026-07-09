#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/install_system_mimocode.sh [--plan|--apply] [--mimocode-home PATH]

Materializes rldyour-mimocode into the local MiMoCode global config directory.
This does not install the MiMoCode runtime binary. The parent workstation
bootstrap installs @mimo-ai/cli@0.1.5 from its frozen Bun lock and publishes
the managed $HOME/.local/bin/mimo wrapper. Remote scripts are not executed.
USAGE
}

mode="plan"
mimocode_home="${MIMOCODE_HOME:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --plan)
      mode="plan"
      shift
      ;;
    --apply)
      mode="apply"
      shift
      ;;
    --mimocode-home)
      mimocode_home="${2:?--mimocode-home requires a path}"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -n "$mimocode_home" ]]; then
  if [[ "$mimocode_home" != /* ]]; then
    echo "ERROR: MIMOCODE_HOME must be an absolute path" >&2
    exit 2
  fi
  config_dir="$mimocode_home/config"
else
  config_dir="${XDG_CONFIG_HOME:-$HOME/.config}/mimocode"
fi

echo "{\"event\":\"mimocode-install-plan\",\"mode\":\"$mode\",\"config_dir\":\"$config_dir\"}"

if [[ "$mode" == "plan" ]]; then
  exit 0
fi

mkdir -p "$config_dir"

python3 - "$repo_root/.mimocode/mimocode.jsonc" "$config_dir/mimocode.json" <<'PY'
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv[1]).resolve().parents[1] / "scripts"))
from mimocode_contract import load_jsonc  # noqa: E402

source = Path(sys.argv[1])
target = Path(sys.argv[2])
data = load_jsonc(source)
target.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
PY

for name in agent command skills glossary plugins themes; do
  src="$repo_root/.mimocode/$name"
  dst="$config_dir/$name"
  if [[ -d "$src" ]]; then
    rm -rf "$dst"
    mkdir -p "$(dirname "$dst")"
    cp -R "$src" "$dst"
  fi
done

cp "$repo_root/MEMORY.md" "$config_dir/MEMORY.md"

echo "{\"event\":\"mimocode-install-complete\",\"config\":\"$config_dir/mimocode.json\"}"
