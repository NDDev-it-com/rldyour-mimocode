#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import CONFIG, ROOT, Failure, require

NATIVE_SURFACES_DOC = ROOT / "docs" / "native-surfaces.md"


def validate() -> None:
    require(CONFIG.exists(), "project config .mimocode/mimocode.jsonc must exist")
    json_variant = CONFIG.with_suffix(".json")
    require(
        not json_variant.exists(),
        "ambiguous .mimocode/mimocode.json must not coexist with .mimocode/mimocode.jsonc",
    )
    require(NATIVE_SURFACES_DOC.exists(), "docs/native-surfaces.md must exist")
    doc = NATIVE_SURFACES_DOC.read_text(encoding="utf-8")
    require(
        "`.mimocode/mimocode.jsonc`" in doc,
        "docs/native-surfaces.md must reference `.mimocode/mimocode.jsonc`",
    )
    require(
        "`.mimocode/mimocode.json`" in doc,
        "docs/native-surfaces.md must document the upstream `.mimocode/mimocode.json` name for contrast",
    )
    require(
        "JSONC" in doc and "comments" in doc.lower(),
        "docs/native-surfaces.md must explain the .jsonc rationale (JSONC comments/trailing commas)",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode config filename policy")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode config filename policy validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
