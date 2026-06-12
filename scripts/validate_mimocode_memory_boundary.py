#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import MEMORY_POLICY, ROOT, Failure, load_json, require


def validate() -> None:
    policy = load_json(MEMORY_POLICY)
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    memory = (ROOT / "MEMORY.md").read_text(encoding="utf-8")
    require(f"Adapter version: `{version}`" in memory, "MEMORY.md must record current adapter version")
    require("Runtime baseline: MiMoCode `0.1.0`" in memory, "MEMORY.md must record current runtime baseline")
    require("Serena memories are the cross-tool source of truth" in memory, "MEMORY.md must preserve Serena source-of-truth boundary")
    for rel_path in ("checkpoint.md", "notes.md"):
        require(not (ROOT / rel_path).exists(), f"{rel_path} must not be committed runtime state")
    require(not (ROOT / "tasks").exists(), "tasks/ must remain runtime-only by default")
    require(policy.get("dream_policy", {}).get("may_write_serena_directly") is False, "dream must not write Serena directly")
    require(policy.get("distill_policy", {}).get("must_be_reviewable_source_change") is True, "distill output must be reviewable")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode memory boundary")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode memory boundary validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
