#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import CONFIG, MCP_INVENTORY, Failure, load_json, load_jsonc, require


def validate() -> None:
    config = load_jsonc(CONFIG)
    inventory = load_json(MCP_INVENTORY)
    mcp = config.get("mcp") or {}
    required = set(inventory.get("required_servers") or [])
    actual = set(mcp)
    missing = sorted(required - actual)
    require(not missing, f"missing MCP servers: {missing}")
    require(inventory.get("positive_inventory_only") is True, "MCP policy must be positive-inventory-only")
    github = mcp.get("github") or {}
    header = (github.get("headers") or {}).get("X-MCP-Toolsets", "")
    for toolset in inventory.get("github_toolsets") or []:
        require(toolset in header, f"github MCP missing toolset {toolset}")
    require(inventory.get("openai_docs_alias") in mcp, "OpenAI Docs alias missing from MiMoCode MCP inventory")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode MCP inventory")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode MCP inventory validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
