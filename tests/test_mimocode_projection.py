from __future__ import annotations

from scripts.validate_mimocode_agents import validate as validate_agents
from scripts.validate_mimocode_browser_provider_policy import validate as validate_browser
from scripts.validate_mimocode_cmux_boundary import validate as validate_cmux
from scripts.validate_mimocode_commands import validate as validate_commands
from scripts.validate_mimocode_projection_parity import validate as validate_projection
from scripts.validate_mimocode_skills import validate as validate_skills


def test_native_projection_surfaces_are_complete() -> None:
    validate_agents()
    validate_commands()
    validate_skills()
    validate_projection()


def test_browser_and_cmux_boundaries_are_explicit() -> None:
    validate_browser()
    validate_cmux()
