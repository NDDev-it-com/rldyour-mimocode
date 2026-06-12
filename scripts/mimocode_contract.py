from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".mimocode" / "mimocode.jsonc"
TUI = ROOT / ".mimocode" / "tui.json"
CONTRACT = ROOT / "config" / "rldyour-contract.json"
BASELINE = ROOT / "config" / "mimocode-baseline.json"
MCP_INVENTORY = ROOT / "config" / "mcp-inventory.json"
BROWSER_POLICY = ROOT / "config" / "browser-provider-policy.json"
MEMORY_POLICY = ROOT / "config" / "memory-boundary-policy.json"
PROJECTION_POLICY = ROOT / "config" / "projection-policy.json"


class Failure(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Failure(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise Failure(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def strip_jsonc(text: str) -> str:
    output: list[str] = []
    i = 0
    in_string = False
    escaped = False
    while i < len(text):
        char = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if in_string:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            i += 1
            continue
        if char == '"':
            in_string = True
            output.append(char)
            i += 1
            continue
        if char == "/" and nxt == "/":
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        if char == "/" and nxt == "*":
            i += 2
            while i + 1 < len(text) and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        output.append(char)
        i += 1
    stripped = "".join(output)
    return re.sub(r",\s*([}\]])", r"\1", stripped)


def load_jsonc(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(strip_jsonc(path.read_text(encoding="utf-8")))
    except json.JSONDecodeError as exc:
        raise Failure(f"{path.relative_to(ROOT)} is not valid JSONC: {exc}") from exc
    if not isinstance(data, dict):
        raise Failure(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise Failure(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise Failure(f"{path.relative_to(ROOT)} frontmatter is not closed")
    fields: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith("  "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))
