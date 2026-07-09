#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import BROWSER_POLICY, CONFIG, Failure, load_json, load_jsonc, require

EXPECTED_TRANSPORT = [
    "/bin/sh",
    "-c",
    'exec "$HOME/.local/bin/chrome-devtools-mcp" --headless --isolated '
    "--no-usage-statistics --no-performance-crux",
]


def validate() -> None:
    policy = load_json(BROWSER_POLICY)
    require(policy.get("schema_version") == 2, "browser provider policy schema must be 2")
    require(policy.get("required_backend") == "cloakbrowser", "CloakBrowser must be the required backend")
    require(policy.get("fallback_allowed") is False, "browser fallback must remain disabled")
    providers = policy.get("providers") or {}
    for provider in ("webwright", "playwright-cli", "chrome-devtools-mcp"):
        require(provider in providers, f"browser provider {provider} missing")
    require(providers["webwright"].get("mcp") is False, "Webwright must not be MCP")
    require(providers["playwright-cli"].get("mcp") is False, "Playwright must remain CLI, not MCP")
    require(providers["chrome-devtools-mcp"].get("mcp") is True, "Chrome DevTools MCP must remain MCP provider")
    require(providers["playwright-cli"].get("version") == "0.1.17", "Playwright CLI pin must be 0.1.17")
    require(providers["chrome-devtools-mcp"].get("version") == "1.5.0", "Chrome DevTools MCP pin must be 1.5.0")
    require(providers["chrome-devtools-mcp"].get("transport") == EXPECTED_TRANSPORT, "browser policy transport must use the exact managed wrapper")
    config = load_jsonc(CONFIG)
    chrome = ((config.get("mcp") or {}).get("chrome-devtools") or {})
    require(chrome.get("command") == EXPECTED_TRANSPORT, "MiMoCode config must use the exact managed CloakBrowser wrapper")
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
