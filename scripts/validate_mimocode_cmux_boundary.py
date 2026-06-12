#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import CONTRACT, ROOT, Failure, load_json, require


def validate() -> None:
    contract = load_json(CONTRACT)
    boundary = contract.get("orchestration_boundary") or {}
    require(boundary.get("mimocode_compose_is_cmux_orchestrator") is False, "compose must not be cmux orchestrator")
    require(boundary.get("mimocode_background_execution_is_cmux_orchestrator") is False, "background execution must not be cmux orchestrator")
    require(boundary.get("cmux_orchestrator_requires_visible_terminal_session") is True, "cmux must require visible terminal session")
    active_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in [
            ROOT / "README.md",
            ROOT / ".mimocode" / "agent" / "rldyour-compose.md",
            ROOT / ".mimocode" / "skills" / "cmux-worker" / "SKILL.md",
        ]
    ).lower()
    for forbidden in ("hidden daemon orchestrator", "background orchestrator", "headless orchestrator"):
        require(forbidden not in active_text, f"forbidden orchestrator wording present: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode cmux boundary")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode cmux boundary validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
