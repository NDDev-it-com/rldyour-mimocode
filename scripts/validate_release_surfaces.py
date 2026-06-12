#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from mimocode_contract import CONTRACT, ROOT, Failure, load_json, require


VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def validate() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    contract = load_json(CONTRACT)
    require(VERSION_RE.fullmatch(version) is not None, "VERSION must be numeric semver")
    require(version == "1.0.0", "initial MiMoCode adapter release must be 1.0.0")
    require(contract.get("adapter", {}).get("version") == version, "contract version drift")
    require("GNU AFFERO GENERAL PUBLIC LICENSE" in (ROOT / "LICENSE").read_text(encoding="utf-8").splitlines()[0], "LICENSE must be canonical AGPL text")
    for rel_path in ("README.md", "CHANGELOG.md", "SECURITY.md", "NOTICE", "THIRD_PARTY_NOTICES.md", "pyproject.toml"):
        require((ROOT / rel_path).is_file(), f"{rel_path} missing")
        require(version in (ROOT / rel_path).read_text(encoding="utf-8"), f"{rel_path} must mention {version}")
    require("XiaomiMiMo/MiMo-Code" in (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8"), "third-party notices must identify upstream")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate release surfaces")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode release surfaces validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
