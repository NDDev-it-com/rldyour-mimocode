#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import PROJECTION_POLICY, ROOT, Failure, frontmatter, load_json, require, rel


def validate() -> None:
    policy = load_json(PROJECTION_POLICY)
    base = ROOT / ".mimocode" / "command"
    require(base.is_dir(), ".mimocode/command missing")
    for name in policy.get("required_commands") or []:
        path = base / f"{name}.md"
        require(path.is_file(), f"{rel(path)} missing")
        meta = frontmatter(path)
        description = meta.get("description", "")
        require("EN:" in description, f"{rel(path)} description must include English trigger suffix")
        require(any(ord(char) > 127 for char in description), f"{rel(path)} description must be Russian-first")
        require(path.read_text(encoding="utf-8").strip().count("\n") >= 5, f"{rel(path)} must contain a usable prompt template")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode commands")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode commands validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
