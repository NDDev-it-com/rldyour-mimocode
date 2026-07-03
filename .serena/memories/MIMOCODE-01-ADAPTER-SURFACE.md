<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MIMOCODE repository knowledge
Area: MIMOCODE
-->

# MIMOCODE-01-ADAPTER-SURFACE

## Scope
MIMOCODE repository knowledge

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Adapter version is `1.7.7`.
- Runtime baseline is MiMoCode `0.1.4` with binary `mimo`.
- Primary runtime install channel is the official Xiaomi MiMo installer pinned
  to `0.1.4`; npm `@mimo-ai/cli@0.1.4` is secondary provenance.
- Native config surfaces are `.mimocode/mimocode.jsonc`, `.mimocode/tui.json`,
  `.mimocode/agent/*.md`, `.mimocode/command/*.md`, and
  `.mimocode/skills/*/SKILL.md`.
- MiMoCode is an active first-class adapter, not an OpenCode alias.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
