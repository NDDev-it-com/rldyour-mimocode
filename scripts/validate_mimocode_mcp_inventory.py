#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import (
    CONFIG,
    CONTRACT,
    MCP_INVENTORY,
    Failure,
    load_json,
    load_jsonc,
    require,
)


EXPECTED_MCP_RUNTIME_PINS = {
    "sequential-thinking": "@modelcontextprotocol/server-sequential-thinking@2026.7.4",
    "context7": "@upstash/context7-mcp@3.2.3",
}


def validate_mcp_runtime_pins(
    mcp: dict[str, object], inventory: dict[str, object], contract: dict[str, object]
) -> None:
    require(
        inventory.get("runtime_pins") == EXPECTED_MCP_RUNTIME_PINS,
        "MCP inventory runtime pins must match the current exact package set",
    )
    require(
        contract.get("mcp_runtime_pins") == EXPECTED_MCP_RUNTIME_PINS,
        "contract MCP runtime pins must match the current exact package set",
    )
    for alias, package_spec in EXPECTED_MCP_RUNTIME_PINS.items():
        server = mcp.get(alias)
        require(
            isinstance(server, dict), f"{alias} MCP configuration must be an object"
        )
        require(
            server.get("type") == "local",
            f"{alias} MCP must use the local stdio transport",
        )
        require(server.get("enabled") is True, f"{alias} MCP must remain enabled")
        require(
            server.get("command") == ["bunx", package_spec],
            f"{alias} MCP must pin {package_spec} via bunx",
        )

    provenance = inventory.get("registry_provenance")
    require(isinstance(provenance, dict), "MCP registry provenance must be recorded")
    packages = provenance.get("packages")
    require(
        isinstance(packages, dict), "MCP registry package provenance must be an object"
    )
    for alias in EXPECTED_MCP_RUNTIME_PINS:
        package = packages.get(alias)
        require(isinstance(package, dict), f"registry provenance missing for {alias}")
        require(
            str(package.get("dist_integrity", "")).startswith("sha512-"),
            f"{alias} npm integrity must be sha512",
        )
        require(
            len(str(package.get("dist_shasum", ""))) == 40,
            f"{alias} npm shasum must be a 40-character SHA-1 registry digest",
        )
        require(
            len(str(package.get("upstream_commit", ""))) == 40,
            f"{alias} upstream commit must be pinned",
        )
    require(
        provenance.get("stdio_probe")
        == "initialize+notifications/initialized+tools/list",
        "MCP stdio compatibility probe evidence is missing",
    )
    require(
        provenance.get("protocol_version") == "2025-11-25",
        "MCP protocol probe version drift",
    )
    require(
        provenance.get("production_audit_vulnerabilities") == 0,
        "MCP production dependency audit must be clean",
    )


def validate() -> None:
    config = load_jsonc(CONFIG)
    inventory = load_json(MCP_INVENTORY)
    contract = load_json(CONTRACT)
    mcp = config.get("mcp") or {}
    required = set(inventory.get("required_servers") or [])
    actual = set(mcp)
    missing = sorted(required - actual)
    require(not missing, f"missing MCP servers: {missing}")
    require(
        inventory.get("positive_inventory_only") is True,
        "MCP policy must be positive-inventory-only",
    )
    github = mcp.get("github") or {}
    header = (github.get("headers") or {}).get("X-MCP-Toolsets", "")
    for toolset in inventory.get("github_toolsets") or []:
        require(toolset in header, f"github MCP missing toolset {toolset}")
    require(
        inventory.get("openai_docs_alias") in mcp,
        "OpenAI Docs alias missing from MiMoCode MCP inventory",
    )
    validate_mcp_runtime_pins(mcp, inventory, contract)


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
