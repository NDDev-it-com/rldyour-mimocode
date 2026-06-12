from __future__ import annotations

from pathlib import Path

from scripts.validate_mimocode_memory_boundary import validate

ROOT = Path(__file__).resolve().parents[1]


def test_memory_boundary_rejects_runtime_artifacts() -> None:
    validate()
    assert not (ROOT / "checkpoint.md").exists()
    assert not (ROOT / "notes.md").exists()
    assert not (ROOT / "tasks").exists()
