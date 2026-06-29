#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import PROJECTION_POLICY, ROOT, Failure, frontmatter, load_json, rel, require


def validate() -> None:
    policy = load_json(PROJECTION_POLICY)
    base = ROOT / ".mimocode" / "skills"
    require(base.is_dir(), ".mimocode/skills missing")
    seen: set[str] = set()
    for name in policy.get("required_skills") or []:
        path = base / name / "SKILL.md"
        require(path.is_file(), f"{rel(path)} missing")
        meta = frontmatter(path)
        require(meta.get("name") == name, f"{rel(path)} frontmatter name mismatch")
        description = meta.get("description", "")
        require("EN:" in description, f"{rel(path)} description must include English trigger suffix")
        require(any(ord(char) > 127 for char in description), f"{rel(path)} description must be Russian-first")
        require(name not in seen, f"duplicate skill {name}")
        seen.add(name)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode skills")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
