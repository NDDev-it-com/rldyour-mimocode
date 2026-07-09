#!/usr/bin/env bash
set -euo pipefail

redact=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --redact)
      redact=true
      shift
      ;;
    --help|-h)
      echo "Usage: scripts/doctor_system_mimocode.sh [--redact]"
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$repo_root/scripts/validate_mimocode_config.py" --strict >/dev/null
python3 "$repo_root/scripts/validate_mimocode_runtime_baseline.py" --strict >/dev/null
python3 "$repo_root/scripts/validate_mimocode_mcp_inventory.py" --strict >/dev/null

if ! command -v mimo >/dev/null 2>&1; then
  echo '{"status":"NOT_PROVEN","runtime":"mimocode","binary":"mimo","reason":"mimo binary is not installed or not on PATH"}'
  exit 0
fi

version="$(mimo --version 2>&1 || true)"
if [[ "$redact" == "true" ]]; then
  version="$(printf '%s' "$version" | sed -E 's/(token|key|secret|password)=([^[:space:]]+)/\\1=REDACTED/Ig')"
fi
if [[ "$version" == *"0.1.5"* ]]; then
  printf '{"status":"OK","runtime":"mimocode","binary":"mimo","version":%s}\n' "$(python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))' <<<"$version")"
else
  printf '{"status":"NOT_PROVEN","runtime":"mimocode","binary":"mimo","reason":"version output does not contain 0.1.5","version":%s}\n' "$(python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))' <<<"$version")"
fi
