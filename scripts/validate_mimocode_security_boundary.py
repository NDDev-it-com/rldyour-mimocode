#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from mimocode_contract import ROOT, Failure, require

SECURITY = ROOT / "SECURITY.md"

# Source-tracked security-facing surfaces. Session artifacts and runtime state are
# intentionally excluded because they may be absent in a source-only CI checkout.
SCAN_FILES = (
    ROOT / "SECURITY.md",
    ROOT / "README.md",
    ROOT / "docs" / "rldyour-security-review.md",
    ROOT / ".mimocode" / "agent" / "rldyour-security-review.md",
)

FORBIDDEN = (
    "permissions are a sandbox",
    "permission system is a sandbox",
    "permission prompts are a sandbox",
    "permissions provide sandbox isolation",
    "sandboxed by permissions",
    "mcp servers are inside the trust boundary",
    "mcp servers are within the trust boundary",
)


def validate() -> None:
    require(SECURITY.exists(), "SECURITY.md must exist")
    security_text = SECURITY.read_text(encoding="utf-8").lower()
    require(
        "not a security sandbox" in security_text,
        "SECURITY.md must state MiMoCode permissions are not a security sandbox",
    )
    require(
        "outside the trust boundary" in security_text,
        "SECURITY.md must state MCP servers run outside the trust boundary",
    )
    for path in SCAN_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8").lower()
        for phrase in FORBIDDEN:
            require(
                phrase not in text,
                f"{path.relative_to(ROOT)} must not claim permissions/MCP provide a security sandbox: found {phrase!r}",
            )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode security boundary documentation")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode security boundary validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
