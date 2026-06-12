#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import BROWSER_POLICY, Failure, load_json, require


def validate() -> None:
    policy = load_json(BROWSER_POLICY)
    providers = policy.get("providers") or {}
    for provider in ("webwright", "playwright-cli", "chrome-devtools-mcp"):
        require(provider in providers, f"browser provider {provider} missing")
    require(providers["webwright"].get("mcp") is False, "Webwright must not be MCP")
    require(providers["playwright-cli"].get("mcp") is False, "Playwright must remain CLI, not MCP")
    require(providers["chrome-devtools-mcp"].get("mcp") is True, "Chrome DevTools MCP must remain MCP provider")
    require(policy.get("mimocode_builtin_browser", {}).get("enabled") is False, "MiMoCode built-in browser provider must remain disabled until modeled")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode browser provider policy")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode browser provider policy validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
