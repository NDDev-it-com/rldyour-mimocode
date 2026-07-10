from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from scripts import mimocode_contract
from scripts import validate_mimocode_mcp_inventory as mcp_validator
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
    required = set(
        json.loads((ROOT / "config" / "mcp-inventory.json").read_text())[
            "required_servers"
        ]
    )
    assert required <= set(config["mcp"])


def test_mcp_runtime_pins_are_exact_and_provenanced() -> None:
    config = mimocode_contract.load_jsonc(ROOT / ".mimocode" / "mimocode.jsonc")
    inventory = json.loads((ROOT / "config" / "mcp-inventory.json").read_text())
    contract = json.loads((ROOT / "config" / "rldyour-contract.json").read_text())

    mcp_validator.validate_mcp_runtime_pins(config["mcp"], inventory, contract)


@pytest.mark.parametrize(
    ("alias", "stale_spec"),
    [
        (
            "sequential-thinking",
            "@modelcontextprotocol/server-sequential-thinking@2025.12.18",
        ),
        ("context7", "@upstash/context7-mcp@3.2.2"),
    ],
)
def test_stale_mcp_runtime_pins_are_rejected(alias: str, stale_spec: str) -> None:
    config = mimocode_contract.load_jsonc(ROOT / ".mimocode" / "mimocode.jsonc")
    inventory = json.loads((ROOT / "config" / "mcp-inventory.json").read_text())
    contract = json.loads((ROOT / "config" / "rldyour-contract.json").read_text())
    stale_config = copy.deepcopy(config)
    stale_config["mcp"][alias]["command"] = ["bunx", stale_spec]

    with pytest.raises(mcp_validator.Failure, match=f"{alias} MCP must pin"):
        mcp_validator.validate_mcp_runtime_pins(
            stale_config["mcp"], inventory, contract
        )


def test_runtime_baseline_is_initial_mimocode_target() -> None:
    validate_runtime()
    baseline = json.loads((ROOT / "config" / "mimocode-baseline.json").read_text())
    assert baseline["runtime"] == "mimocode"
    assert baseline["upstream_release"] == "v0.1.5"
    assert baseline["npm"]["package"] == "@mimo-ai/cli"
