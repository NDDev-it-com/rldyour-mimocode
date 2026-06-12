<!-- Memory Metadata
Last updated: 2026-06-13
Last verified: 2026-06-13
Last commit: 4e5482e1da7b648ccc7df61f88974e767587875e fix(ci): harden MiMoCode secret scan release metadata
Scope: MiMoCode native adapter surface
Area: MIMOCODE-->

# MIMOCODE-01-ADAPTER-SURFACE

## Scope
MiMoCode native adapter surface.

## Current source of truth
- `path:VERSION`
- `path:config/rldyour-contract.json`
- `path:config/mimocode-baseline.json`
- `path:.mimocode/mimocode.jsonc`
- `path:.mimocode/tui.json`
- `path:.mimocode/agent/`
- `path:.mimocode/command/`
- `path:.mimocode/skills/`

## Last verified
- date: 2026-06-13
- commit: `4e5482e1da7b648ccc7df61f88974e767587875e`
- checked by: Codex rldyour-flow sync

## Facts
- Adapter version is `1.0.7`.
- Runtime baseline is MiMoCode `0.1.0` with binary `mimo`.
- Primary runtime install channel is the official Xiaomi MiMo installer pinned
  to `0.1.0`; npm `@mimo-ai/cli@0.1.0` is secondary provenance.
- Native config surfaces are `.mimocode/mimocode.jsonc`, `.mimocode/tui.json`,
  `.mimocode/agent/*.md`, `.mimocode/command/*.md`, and
  `.mimocode/skills/*/SKILL.md`.
- MiMoCode is an active first-class adapter, not an OpenCode alias.

## Evidence
- `path:VERSION`
- `path:config/rldyour-contract.json`
- `path:config/mimocode-baseline.json`
- `path:.mimocode/mimocode.jsonc`
- `path:scripts/validate_mimocode_config.py`
- `path:scripts/validate_mimocode_projection_parity.py`

## Known pitfalls
- OpenCode-derived schema compatibility is not enough by itself. Runtime
  acceptance must be proven by installed `mimo` doctor checks when available.

## Update policy
Update after version, runtime baseline, native MiMoCode surface, or projection
policy changes.

## Delete / merge policy
- Delete or merge only when the adapter no longer owns native MiMoCode
  projection surfaces and the replacement memory preserves the durable facts.

## Applies to
- `.mimocode/mimocode.jsonc`
- `.mimocode/tui.json`
- `.mimocode/agent/`
- `.mimocode/command/`
- `.mimocode/skills/`

## Source of truth
- The `Current source of truth` section above, plus current code,
  configuration, tests, git state, and installed runtime output where runtime
  acceptance is claimed.

## Invariants
- Do not vendor upstream Xiaomi MiMoCode source code or binary assets.
- Do not model MiMoCode as an OpenCode alias.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer unsupported MiMoCode config keys or installed runtime behavior
  from upstream OpenCode compatibility alone.

## Update Triggers
- Update after MiMoCode adapter version changes, baseline refreshes, native
  directory layout changes, installer changes, or validator contract changes.

## Validation Commands
- `python3 scripts/validate_mimocode_config.py --strict`
- `python3 scripts/validate_mimocode_projection_parity.py --strict`
- `python3 scripts/validate_mimocode_runtime_baseline.py --strict`

## Repair Procedure
- Re-read native surface files and config policies, update only verified facts,
  then rerun the validation commands.
