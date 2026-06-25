<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.2 (no-fullrepo)
Scope: MiMoCode runtime baseline and install proof
Area: RUNTIME-->

# RUNTIME-01-BASELINE

## Scope
MiMoCode runtime baseline and install proof.

## Current source of truth
- `path:config/mimocode-baseline.json`
- `path:config/rldyour-contract.json`
- `path:scripts/validate_mimocode_runtime_baseline.py`
- `path:scripts/install_system_mimocode.sh`
- `path:scripts/doctor_system_mimocode.sh`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: ry-start no-fullrepo MiMoCode migration

## Facts
- Runtime baseline is MiMoCode `0.1.3`.
- Runtime binary is `mimo`.
- Primary install channel is the official Xiaomi MiMo installer pinned to
  `0.1.3` with `--no-modify-path`.
- npm `@mimo-ai/cli@0.1.3` is secondary provenance and must not replace the
  primary installer channel without explicit validation.
- The runtime doctor must report `NOT_PROVEN` when `mimo` is unavailable.

## Evidence
- `path:config/mimocode-baseline.json`
- `path:scripts/validate_mimocode_runtime_baseline.py`
- `path:scripts/install_system_mimocode.sh`
- `path:scripts/doctor_system_mimocode.sh`

## Known pitfalls
- Installed runtime state is not proven by repository files alone.

## Update policy
Update after runtime baseline, install channel, binary path, doctor behavior, or
runtime validation changes.

## Delete / merge policy
- Delete or merge only when runtime baseline tracking moves to another durable
  memory and the replacement preserves current facts.

## Applies to
- `mimo`
- `config/mimocode-baseline.json`
- `scripts/install_system_mimocode.sh`
- `scripts/doctor_system_mimocode.sh`

## Source of truth
- The `Current source of truth` section above, plus installed `mimo --version`
  output when runtime presence is claimed.

## Invariants
- Do not mark runtime checks passing when the binary is absent.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer npm registry availability or installed auth state from upstream
  README text.

## Update Triggers
- Update after runtime baseline refresh, installer changes, doctor changes, or
  live runtime provenance changes.

## Validation Commands
- `python3 scripts/validate_mimocode_runtime_baseline.py --strict`
- `python3 scripts/doctor_system_mimocode.sh --redact`

## Repair Procedure
- Re-read runtime baseline and installer files, update only verified facts, then
  rerun the validation commands.
