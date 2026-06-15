#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import CONFIG, TUI, Failure, load_json, load_jsonc, require


def validate() -> None:
    config = load_jsonc(CONFIG)
    require(config.get("$schema") == "https://opencode.ai/config.json", "MiMoCode config must use the resolvable OpenCode-compatible schema URL (see scripts/validate_mimocode_schema_url.py)")
    require(config.get("provider") == {}, "committed provider config must not contain credentials or provider defaults")
    require(config.get("share") == "disabled", "committed config must disable auto-sharing")
    require(config.get("autoupdate") is False, "committed config must disable unpinned runtime auto-update")
    max_mode = config.get("experimental", {}).get("maxMode")
    require(
        max_mode is False or (isinstance(max_mode, dict) and isinstance(max_mode.get("candidates"), int)),
        "experimental.maxMode must be false or an object with integer candidates (best-of-N reasoning)",
    )
    permission = config.get("permission")
    require(isinstance(permission, dict), "permission must be an object")
    for key in ("read", "glob", "grep", "bash", "edit", "task", "skill", "external_directory", "doom_loop", "list", "todowrite"):
        require(key in permission, f"permission.{key} missing")
    mcp = config.get("mcp")
    require(isinstance(mcp, dict) and mcp, "mcp inventory must be present")
    tui = load_json(TUI)
    require(tui.get("$schema") == "https://opencode.ai/tui.json", "tui.json must use MiMoCode/OpenCode-compatible TUI schema")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode native config")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode config validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
