from __future__ import annotations

import copy

import pytest

from scripts import validate_mimocode_browser_provider_policy as policy


def test_live_repository_browser_policy_passes() -> None:
    policy.validate()


@pytest.mark.parametrize("surface", sorted(policy.SURFACES))
def test_every_browser_surface_has_exact_boundary(surface: str) -> None:
    text = policy.SURFACES[surface].read_text(encoding="utf-8")
    assert text.count(policy.MANDATORY_SKILL_BOUNDARY) == 1


def test_webwright_cannot_become_an_active_provider() -> None:
    mutated = copy.deepcopy(policy.EXPECTED_POLICY)
    mutated["active_providers"].append("webwright")
    with pytest.raises(policy.Failure, match="exactly match"):
        policy.validate_policy(mutated)


def test_missing_boundary_fails_closed() -> None:
    with pytest.raises(policy.Failure, match="must appear exactly once"):
        policy.validate_surface("skill", "# Browser Review\nwebwright-task compatibility intent\n")


@pytest.mark.parametrize(
    "alternate",
    [
        "/tmp/playwright-cli",
        "/tmp/chrome-devtools-mcp",
        "/tmp/$HOME/.local/bin/playwright-cli",
    ],
)
def test_alternate_provider_path_is_rejected(alternate: str) -> None:
    text = (
        policy.MANDATORY_SKILL_BOUNDARY
        + f"\n\nwebwright-task compatibility intent\n{alternate}\n"
    )
    with pytest.raises(policy.Failure, match="must use exact"):
        policy.validate_surface("skill", text)


def test_action_without_immediate_health_gate_is_rejected() -> None:
    text = (
        policy.MANDATORY_SKILL_BOUNDARY
        + "\n\nwebwright-task compatibility intent\n```bash\n"
        + "$HOME/.local/bin/playwright-cli open https://example.test\n"
        + "```\n"
    )
    with pytest.raises(policy.Failure, match="immediately health-gated"):
        policy.validate_surface("skill", text)


@pytest.mark.parametrize(
    "command",
    [
        "npx playwright test",
        "bunx @playwright/test",
        "python3 -m webwright run workflow.py",
        "playwright test",
    ],
)
def test_unapproved_browser_shell_execution_is_rejected(command: str) -> None:
    text = (
        policy.MANDATORY_SKILL_BOUNDARY
        + f"\n\nwebwright-task compatibility intent\n```bash\n{command}\n```\n"
    )
    with pytest.raises(policy.Failure, match="unapproved browser shell execution"):
        policy.validate_surface("skill", text)


def test_browser_agent_cannot_delegate_or_use_webfetch() -> None:
    text = policy.SURFACES["agent"].read_text(encoding="utf-8").replace(
        "  webfetch: deny", "  webfetch: allow"
    )
    with pytest.raises(policy.Failure, match="required permission missing"):
        policy.validate_surface("agent", text)
