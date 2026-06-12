from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_install_plan_is_json_event_and_does_not_require_runtime() -> None:
    proc = subprocess.run(
        ["bash", "scripts/install_system_mimocode.sh", "--plan"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    event = json.loads(proc.stdout)
    assert event["event"] == "mimocode-install-plan"
    assert event["mode"] == "plan"


def test_doctor_reports_not_proven_when_runtime_missing_or_reports_version() -> None:
    proc = subprocess.run(
        ["bash", "scripts/doctor_system_mimocode.sh", "--redact"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    event = json.loads(proc.stdout)
    assert event["status"] in {"OK", "NOT_PROVEN"}
    assert event["runtime"] == "mimocode"
