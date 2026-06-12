#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import PROJECTION_POLICY, ROOT, Failure, frontmatter, load_json, require, rel


def validate() -> None:
    policy = load_json(PROJECTION_POLICY)
    base = ROOT / ".mimocode" / "agent"
    require(base.is_dir(), ".mimocode/agent missing")
    for name in policy.get("required_agents") or []:
        path = base / f"{name}.md"
        require(path.is_file(), f"{rel(path)} missing")
        meta = frontmatter(path)
        require(meta.get("mode") == "subagent", f"{rel(path)} must be a MiMoCode subagent definition")
        require(meta.get("description"), f"{rel(path)} description missing")
    compose_text = (base / "rldyour-compose.md").read_text(encoding="utf-8").lower()
    require("not rldyour cmux orchestrator" in compose_text, "compose agent must reject cmux orchestrator equivalence")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode agents")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode agents validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
