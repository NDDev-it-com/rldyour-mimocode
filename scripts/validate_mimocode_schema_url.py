#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys

from mimocode_contract import BASELINE, CONFIG, Failure, load_json, load_jsonc, rel, require

EXPECTED_SCHEMA = "https://opencode.ai/config.json"
_DOUBLE_SLASH = re.compile(r"https?://[^/]+//")


def _no_double_slash(url: str) -> bool:
    return _DOUBLE_SLASH.search(url) is None


def validate() -> None:
    config = load_jsonc(CONFIG)
    schema = config.get("$schema", "")
    require(isinstance(schema, str) and bool(schema), f"{rel(CONFIG)} must declare a string $schema")
    require(_no_double_slash(schema), f"{rel(CONFIG)} $schema must not contain a doubled slash: {schema!r}")
    require(schema == EXPECTED_SCHEMA, f"{rel(CONFIG)} $schema must be {EXPECTED_SCHEMA!r}, got {schema!r}")

    baseline = load_json(BASELINE)
    config_schema = baseline.get("config_schema", {})
    require(isinstance(config_schema, dict), f"{rel(BASELINE)} must declare a config_schema object")
    for key in ("current_docs_schema", "upstream_repo_example_schema", "selected_project_schema"):
        value = config_schema.get(key, "")
        require(isinstance(value, str) and bool(value), f"{rel(BASELINE)} config_schema.{key} must be a non-empty string")
        require(_no_double_slash(value), f"{rel(BASELINE)} config_schema.{key} must not contain a doubled slash: {value!r}")
    require(
        config_schema.get("selected_project_schema") == EXPECTED_SCHEMA,
        f"{rel(BASELINE)} config_schema.selected_project_schema must be {EXPECTED_SCHEMA!r}",
    )
    require(
        config_schema.get("selected_project_schema") == schema,
        f"{rel(BASELINE)} selected_project_schema must match {rel(CONFIG)} $schema",
    )
    require(
        bool(config_schema.get("selected_schema_reason")),
        f"{rel(BASELINE)} config_schema.selected_schema_reason must document why the schema was selected",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MiMoCode config $schema URL hygiene")
    parser.add_argument("--strict", action="store_true")
    parser.parse_args()
    try:
        validate()
    except Failure as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("ok: MiMoCode schema URL validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
