#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import BASELINE, CONTRACT, ROOT, Failure, load_json, require


def validate() -> None:
    baseline = load_json(BASELINE)
    contract = load_json(CONTRACT)
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    adapter = contract.get("adapter") or {}
    require(adapter.get("id") == "mimocode", "contract adapter id must be mimocode")
    require(adapter.get("version") == version, "contract adapter version must match VERSION")
    require(adapter.get("runtime_version") == "0.1.5", "contract runtime version must be 0.1.5")
    require(baseline.get("upstream_release") == "v0.1.5", "baseline upstream release must be v0.1.5")
    require(baseline.get("binary") == "mimo", "runtime binary must be mimo")
    require((baseline.get("npm") or {}).get("package") == "@mimo-ai/cli", "npm package metadata must name @mimo-ai/cli")
    install = baseline.get("install") or {}
    require(baseline.get("target_channel") == "rldyour-bootstrap-frozen-bun-lock", "runtime channel must be the bootstrap-owned frozen lock")
    require(install.get("lock_source") == "templates/ai-cli/bun.lock", "runtime lock source must be explicit")
    require(install.get("managed_wrapper") == "$HOME/.local/bin/mimo", "managed wrapper path must be explicit")
    require(install.get("remote_script_execution") is False, "remote installer scripts must remain disabled")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode runtime baseline")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode runtime baseline validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
