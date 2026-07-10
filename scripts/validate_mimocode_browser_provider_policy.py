#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any

from mimocode_contract import (
    BROWSER_POLICY,
    CONFIG,
    CONTRACT,
    ROOT,
    Failure,
    load_json,
    load_jsonc,
    require,
)

HEALTH_COMMAND = "$HOME/.local/bin/cloakbrowser-cdp-health"
PLAYWRIGHT_CLI = "$HOME/.local/bin/playwright-cli"
CHROME_WRAPPER = "$HOME/.local/bin/chrome-devtools-mcp"
EXPECTED_TRANSPORT = [
    "/bin/sh",
    "-c",
    'exec "$HOME/.local/bin/chrome-devtools-mcp" --headless --isolated '
    +
    "--no-usage-statistics --no-performance-crux",
]
EXPECTED_POLICY: dict[str, Any] = {
    "schema_version": 3,
    "required_backend": "cloakbrowser",
    "fallback_allowed": False,
    "health_gate": {
        "command": HEALTH_COMMAND,
        "required_before_every_action": True,
        "failure_result": "NOT_PROVEN",
    },
    "active_providers": ["playwright-cli", "chrome-devtools-mcp"],
    "providers": {
        "playwright-cli": {
            "kind": "browser-automation",
            "mcp": False,
            "version": "0.1.17",
            "executable": PLAYWRIGHT_CLI,
            "forbidden_arguments": ["run-code", "--filename"],
        },
        "chrome-devtools-mcp": {
            "kind": "devtools-debugging",
            "mcp": True,
            "version": "1.5.0",
            "transport": EXPECTED_TRANSPORT,
        },
    },
    "routing": {
        "long_horizon_web_task": "playwright-cli",
        "screenshots_snapshots_traces": "playwright-cli",
        "console_network_runtime_layout_performance_memory_lighthouse": "chrome-devtools-mcp",
    },
    "compatibility_workflows": {
        "webwright-task": {
            "route": "browser-review",
            "runtime_provider": "webwright",
            "runtime_execution_allowed": False,
            "failure_result": "NOT_PROVEN",
        }
    },
    "forbidden_runtime_providers": [
        "webwright",
        "stock-browser",
        "raw-browser",
        "in-app-browser",
        "browser_agent",
        "node_repl",
        "computer-use",
        "playwright-mcp",
        "raw-playwright",
        "direct-package-browser-provider",
        "alternate-cdp",
        "alternate-browser-executable",
        "alternate-browser-config",
    ],
    "mimocode_builtin_browser": {
        "enabled": False,
        "reason": "MiMoCode built-in browser execution is outside the bootstrap-owned CloakBrowser trust boundary.",
        "requires_explicit_provider_model_before_enablement": True,
    },
}
EXPECTED_CONTRACT_MODEL = {
    "required_backend": "cloakbrowser",
    "health_gate": "$HOME/.local/bin/cloakbrowser-cdp-health before every browser action",
    "active_providers": ["playwright-cli", "chrome-devtools-mcp"],
    "playwright-cli": "exact managed executable for flows, screenshots, snapshots, traces, visual evidence, and long-horizon stepwise workflows",
    "chrome-devtools-mcp": "exact managed transport for console, network, runtime, layout, performance, Lighthouse, memory, and live debugging",
    "webwright-task": "compatibility intent routed through browser-review; Webwright runtime execution forbidden",
    "fallback_allowed": False,
    "mimocode_builtin_browser": "disabled until separately modeled as an approved provider",
}
SURFACES = {
    "skill": ROOT / ".mimocode" / "skills" / "browser-review" / "SKILL.md",
    "agent": ROOT / ".mimocode" / "agent" / "rldyour-browser-worker.md",
    "command": ROOT / ".mimocode" / "command" / "browser-review.md",
}
MANDATORY_SKILL_BOUNDARY = """## Mandatory CloakBrowser Boundary

This boundary applies before every browser action:

1. Run exactly:

   ```bash
   $HOME/.local/bin/cloakbrowser-cdp-health
   ```

   If the command is missing or exits nonzero, stop immediately and report `NOT_PROVEN`.
2. Browser execution is permitted only through:
   - the exact `$HOME/.local/bin/playwright-cli` executable; `run-code` and `--filename` are forbidden;
   - the approved Chrome DevTools MCP transport, exactly `/bin/sh -c 'exec "$HOME/.local/bin/chrome-devtools-mcp" --headless --isolated --no-usage-statistics --no-performance-crux'`.
3. Never execute the Webwright Python runtime, stock/raw/in-app Browser, `browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright, `bunx`, `npx`, direct package invocations, alternate CDP endpoints, alternate browser executables, alternate browser configs, or any fallback. No fallback is allowed."""
FORBIDDEN_SHELL_PATTERNS = (
    re.compile(r"(^|[;&|]\s*)(?:bunx|npx)\b"),
    re.compile(
        r"(^|[;&|]\s*)(?:python(?:3)?|uv\s+run\s+python(?:3)?)\b.*\bwebwright\b",
        re.IGNORECASE,
    ),
    re.compile(r"(^|[;&|]\s*)playwright\b"),
)


def bash_blocks(text: str) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in text.splitlines():
        if line.strip() == "```bash":
            current = []
            continue
        if line.strip() == "```" and current is not None:
            blocks.append(current)
            current = None
            continue
        if current is not None:
            current.append(line)
    return blocks


def require_exact_provider_mentions(text: str, surface: str) -> None:
    for token, exact in (
        ("playwright-cli", PLAYWRIGHT_CLI),
        ("chrome-devtools-mcp", CHROME_WRAPPER),
    ):
        pattern = re.compile(rf"(?<![\w-]){re.escape(token)}(?![\w-])")
        prefix = exact[: -len(token)]
        for match in pattern.finditer(text):
            exact_start = match.start() - len(prefix)
            actual_prefix = text[max(0, exact_start) : match.start()]
            prior = text[exact_start - 1] if exact_start > 0 else ""
            require(
                actual_prefix == prefix and (not prior or prior not in "/~$._-"),
                f"{surface}: {token} must use exact {exact}",
            )


def validate_surface(surface: str, text: str) -> None:
    require(
        text.count(MANDATORY_SKILL_BOUNDARY) == 1,
        f"{surface}: mandatory CloakBrowser boundary must appear exactly once",
    )
    remainder = text.replace(MANDATORY_SKILL_BOUNDARY, "", 1)
    require(
        "run-code" not in remainder,
        f"{surface}: run-code is forbidden outside the boundary declaration",
    )
    require(
        "--filename" not in remainder,
        f"{surface}: --filename is forbidden outside the boundary declaration",
    )
    require_exact_provider_mentions(remainder, surface)

    for block in bash_blocks(remainder):
        previous_command = ""
        for raw_line in block:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            for pattern in FORBIDDEN_SHELL_PATTERNS:
                require(
                    pattern.search(line) is None,
                    f"{surface}: unapproved browser shell execution is forbidden: {line}",
                )
            if PLAYWRIGHT_CLI in line:
                require(
                    previous_command == HEALTH_COMMAND,
                    f"{surface}: every Playwright CLI action must be immediately health-gated",
                )
            previous_command = line

    require(
        "webwright-task" in remainder,
        f"{surface}: webwright-task compatibility intent must be explicit",
    )

    if surface == "agent":
        for permission in (
            "  edit: deny",
            "  bash: allow",
            "  webfetch: deny",
            "  task: deny",
            "  skill: allow",
        ):
            require(permission in text, f"agent: required permission missing: {permission.strip()}")


def validate_policy(policy: dict[str, Any]) -> None:
    require(
        policy == EXPECTED_POLICY,
        "browser provider policy must exactly match the fail-closed CloakBrowser contract",
    )


def validate() -> None:
    policy = load_json(BROWSER_POLICY)
    validate_policy(policy)

    config = load_jsonc(CONFIG)
    mcp = config.get("mcp") or {}
    for alias in ("webwright", "playwright", "browser", "browser-agent"):
        require(alias not in mcp, f"unapproved browser MCP alias is active: {alias}")
    chrome = mcp.get("chrome-devtools") or {}
    require(
        chrome.get("command") == EXPECTED_TRANSPORT,
        "MiMoCode config must use the exact managed CloakBrowser wrapper",
    )

    contract = load_json(CONTRACT)
    require(
        contract.get("browser_provider_model") == EXPECTED_CONTRACT_MODEL,
        "contract browser provider model drift",
    )

    for surface, path in SURFACES.items():
        require(path.is_file(), f"missing browser {surface}: {path.relative_to(ROOT)}")
        validate_surface(surface, path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode browser provider policy")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except (Failure, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode fail-closed CloakBrowser provider policy validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
