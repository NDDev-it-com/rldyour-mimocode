<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MEMORY repository knowledge
Area: MEMORY
-->

# MEMORY-01-MIMOCODE-SERENA-BOUNDARY

## Scope
MEMORY repository knowledge

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Serena memories are release-grade cross-tool durable facts.
- MiMoCode `MEMORY.md` is a tracked runtime projection from verified facts.
- `checkpoint.md`, `notes.md`, SQLite memory stores, and
  `tasks/<id>/progress.md` are runtime/session artifacts and ignored by
  default.
- MiMoCode `/dream` and `/distill` output must enter reviewable source changes
  before it becomes durable memory or adapter surface.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
