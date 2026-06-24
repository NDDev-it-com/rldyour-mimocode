from __future__ import annotations

import json
from pathlib import Path

from scripts import mimocode_contract
from scripts.validate_mimocode_config import validate as validate_config
from scripts.validate_mimocode_mcp_inventory import validate as validate_mcp
from scripts.validate_mimocode_runtime_baseline import validate as validate_runtime

ROOT = Path(__file__).resolve().parents[1]


def test_config_is_valid_jsonc_and_credential_free() -> None:
    validate_config()
    config = mimocode_contract.load_jsonc(ROOT / ".mimocode" / "mimocode.jsonc")
    assert config["provider"] == {}
    assert config["share"] == "disabled"
    assert config["autoupdate"] is False


def test_checkpoint_reserved_is_positive_int() -> None:
    validate_config()
    config = mimocode_contract.load_jsonc(ROOT / ".mimocode" / "mimocode.jsonc")
    reserved = config["checkpoint"]["reserved"]
    assert isinstance(reserved, int) and not isinstance(reserved, bool) and reserved > 0


def test_mcp_inventory_contains_required_positive_set() -> None:
    validate_mcp()
    config = mimocode_contract.load_jsonc(ROOT / ".mimocode" / "mimocode.jsonc")
    required = set(json.loads((ROOT / "config" / "mcp-inventory.json").read_text())["required_servers"])
    assert required <= set(config["mcp"])


def test_runtime_baseline_is_initial_mimocode_target() -> None:
    validate_runtime()
    baseline = json.loads((ROOT / "config" / "mimocode-baseline.json").read_text())
    assert baseline["runtime"] == "mimocode"
    assert baseline["upstream_release"] == "v0.1.3"
    assert baseline["npm"]["package"] == "@mimo-ai/cli"
