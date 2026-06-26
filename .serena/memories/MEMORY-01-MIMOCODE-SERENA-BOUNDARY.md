<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: Serena and MiMoCode memory boundary
Area: MEMORY-->

# MEMORY-01-MIMOCODE-SERENA-BOUNDARY

## Scope
Serena and MiMoCode memory boundary.

## Current source of truth
- `path:config/memory-boundary-policy.json`
- `path:MEMORY.md`
- `path:.gitignore`
- `path:scripts/validate_mimocode_memory_boundary.py`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex rldyour-flow sync

## Facts
- Serena memories are release-grade cross-tool durable facts.
- MiMoCode `MEMORY.md` is a tracked runtime projection from verified facts.
- `checkpoint.md`, `notes.md`, SQLite memory stores, and
  `tasks/<id>/progress.md` are runtime/session artifacts and ignored by
  default.
- MiMoCode `/dream` and `/distill` output must enter reviewable source changes
  before it becomes durable memory or adapter surface.

## Evidence
- `path:config/memory-boundary-policy.json`
- `path:MEMORY.md`
- `path:.gitignore`
- `path:scripts/validate_mimocode_memory_boundary.py`

## Known pitfalls
- MiMoCode native memory can be useful runtime context, but it is not the
  cross-tool source of truth for release facts.

## Update policy
Update after memory boundary policy, ignored runtime artifact list, MiMoCode
memory projection, or dream/distill review-gate changes.

## Delete / merge policy
- Delete or merge only when the MiMoCode adapter no longer includes native
  memory projection and the replacement memory preserves the boundary facts.

## Applies to
- `.serena/memories/`
- `MEMORY.md`
- `checkpoint.md`
- `notes.md`
- `tasks/<id>/progress.md`

## Source of truth
- The `Current source of truth` section above, plus current code,
  configuration, tests, git state, and runtime artifact hygiene validators.

## Invariants
- MiMoCode runtime memory must not overwrite Serena memories.
- Runtime/session memory artifacts stay untracked unless the owner explicitly
  curates them as source-backed documentation.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer that `/dream` or `/distill` output is release-grade until it has
  gone through reviewable source changes and validation.

## Update Triggers
- Update after memory policy changes, ignored runtime artifact changes, memory
  projection changes, or dream/distill workflow changes.

## Validation Commands
- `python3 scripts/validate_mimocode_memory_boundary.py --strict`
- `python3 scripts/validate_fast.sh`

## Repair Procedure
- Re-read memory policy and ignored runtime artifact rules, update only
  verified facts, then rerun the validation commands.
