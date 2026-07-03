<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: CLI runtime and package baselines
Area: RUNTIME
-->

# RUNTIME-01-BASELINE

## Scope
CLI runtime and package baselines

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Runtime baseline is MiMoCode `0.1.4`.
- Runtime binary is `mimo`.
- Primary install channel is the official Xiaomi MiMo installer pinned to
  `0.1.4` with `--no-modify-path`.
- npm `@mimo-ai/cli@0.1.4` is secondary provenance and must not replace the
  primary installer channel without explicit validation.
- The runtime doctor must report `NOT_PROVEN` when `mimo` is unavailable.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
