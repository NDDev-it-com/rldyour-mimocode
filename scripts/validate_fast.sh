#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validate_mimocode_config.py --strict
python3 scripts/validate_mimocode_runtime_baseline.py --strict
python3 scripts/validate_mimocode_mcp_inventory.py --strict
python3 scripts/validate_mimocode_commands.py --strict
python3 scripts/validate_mimocode_agents.py --strict
python3 scripts/validate_mimocode_skills.py --strict
python3 scripts/validate_mimocode_projection_parity.py --strict
python3 scripts/validate_mimocode_memory_boundary.py --strict
python3 scripts/validate_mimocode_browser_provider_policy.py --strict
python3 scripts/validate_mimocode_cmux_boundary.py --strict
python3 scripts/validate_mimocode_schema_url.py --strict
python3 scripts/validate_mimocode_config_filename_policy.py --strict
python3 scripts/validate_mimocode_security_boundary.py --strict
python3 scripts/validate_release_surfaces.py --strict
