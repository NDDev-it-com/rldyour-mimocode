# MIMOCODE-01-ADAPTER-SURFACE

## Purpose

Record native MiMoCode adapter surfaces.

## Current Facts

- Adapter version is `1.0.1`.
- Runtime baseline is MiMoCode `0.1.0` with binary `mimo`.
- Primary runtime install channel is the official Xiaomi MiMo installer pinned
  to `0.1.0`; npm `@mimo-ai/cli@0.1.0` is secondary provenance.
- Native config surfaces are `.mimocode/mimocode.jsonc`, `.mimocode/tui.json`,
  `.mimocode/agent/*.md`, `.mimocode/command/*.md`, and
  `.mimocode/skills/*/SKILL.md`.
- MiMoCode is an active first-class adapter, not an OpenCode alias.

## Evidence

- `VERSION`
- `config/rldyour-contract.json`
- `config/mimocode-baseline.json`
- `.mimocode/mimocode.jsonc`
- `scripts/validate_mimocode_config.py`
- `scripts/validate_mimocode_projection_parity.py`

## Operational Rules

- Do not vendor upstream Xiaomi MiMoCode source code or binary assets.
- Validate native surfaces through adapter validators before root pin updates.

## Last Verified

2026-06-13
