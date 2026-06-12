#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import CONFIG, CONTRACT, PROJECTION_POLICY, ROOT, Failure, load_json, load_jsonc, require


def validate() -> None:
    config = load_jsonc(CONFIG)
    contract = load_json(CONTRACT)
    policy = load_json(PROJECTION_POLICY)
    for surface in ("mimocode_jsonc", "mimocode_tui_json", "mimocode_agents", "mimocode_commands", "mimocode_skills", "mimocode_memory_projection"):
        require(surface in contract.get("native_surfaces", []), f"contract missing native surface {surface}")
    require(policy.get("native_root") == ".mimocode", "projection native root must be .mimocode")
    require(policy.get("commands_directory") == ".mimocode/command", "projection policy must use upstream command directory")
    require((ROOT / "MEMORY.md").is_file(), "top-level MEMORY.md projection missing")
    require(config.get("instructions") == ["README.md", "MEMORY.md", "THIRD_PARTY_NOTICES.md"], "instructions projection drift")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode projection parity")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode projection parity validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
