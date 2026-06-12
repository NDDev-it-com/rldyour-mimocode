#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import BASELINE, CONTRACT, Failure, load_json, require


def validate() -> None:
    baseline = load_json(BASELINE)
    contract = load_json(CONTRACT)
    adapter = contract.get("adapter") or {}
    require(adapter.get("id") == "mimocode", "contract adapter id must be mimocode")
    require(adapter.get("version") == "1.0.0", "adapter version must be 1.0.0")
    require(adapter.get("runtime_version") == "0.1.0", "contract runtime version must be 0.1.0")
    require(baseline.get("upstream_release") == "v0.1.0", "baseline upstream release must be v0.1.0")
    require(baseline.get("binary") == "mimo", "runtime binary must be mimo")
    require((baseline.get("npm") or {}).get("package") == "@mimo-ai/cli", "npm package metadata must name @mimo-ai/cli")
    require((baseline.get("install") or {}).get("primary_command", "").endswith("--version 0.1.0 --no-modify-path"), "primary install command must be version-pinned and avoid PATH mutation")


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
