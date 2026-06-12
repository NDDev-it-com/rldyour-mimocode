<!-- Memory Metadata
Last updated: 2026-06-13
Last verified: 2026-06-13
Last commit: 578c1265f6439d0d83866b03d2d4462068b61726 fix(release): empty MiMoCode unreleased changelog section
Scope: MiMoCode Serena memory maintenance
Area: SERENA-->

# SERENA-01-MEMORY-SYNC

## Scope
MiMoCode Serena memory maintenance.

## Current source of truth
- `path:.serena/project.yml`
- `path:.serena/memories/`
- `path:config/memory-boundary-policy.json`
- `path:scripts/validate_mimocode_memory_boundary.py`

## Last verified
- date: 2026-06-13
- commit: `578c1265f6439d0d83866b03d2d4462068b61726`
- checked by: Codex rldyour-flow sync

## Facts
- MiMoCode adapter Serena memories use the same strict template and
  source-of-truth policy as the root release validators.
- Required domains for MiMoCode are `CORE`, `MIMOCODE`, `RUNTIME`, `MCP`,
  `BROWSER`, `FLOW`, `SECURITY`, `RELEASE`, `SERENA`, and `MEMORY`.
- Serena memories are durable cross-tool facts; MiMoCode `MEMORY.md` is a
  runtime projection.

## Evidence
- `path:.serena/project.yml`
- `path:.serena/memories/CORE-01-INDEX.md`
- `path:.serena/memories/MEMORY-01-MIMOCODE-SERENA-BOUNDARY.md`
- `path:scripts/validate_mimocode_memory_boundary.py`

## Known pitfalls
- Do not allow MiMoCode `/dream` or `/distill` output to silently mutate Serena
  memories.

## Update policy
Update after required memory domains, Serena project config, memory boundary, or
MiMoCode memory projection changes.

## Delete / merge policy
- Delete or merge only when Serena memory maintenance moves to another durable
  memory and the replacement preserves current facts.

## Applies to
- `.serena/project.yml`
- `.serena/memories/`
- `MEMORY.md`

## Source of truth
- The `Current source of truth` section above, plus root memory schema and
  memory evidence validators.

## Invariants
- Serena memories must remain fact-only and source-backed.
- MiMoCode runtime memory must not overwrite Serena memories.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer current release facts from generated or runtime MiMoCode memory
  unless source files and validators confirm them.

## Update Triggers
- Update after memory taxonomy, memory boundary, Serena project, or adapter
  release facts change.

## Validation Commands
- `python3 scripts/validate_mimocode_memory_boundary.py --strict`
- `python3 scripts/validate_fast.sh`

## Repair Procedure
- Re-read memory policy and current memory files, update only verified facts,
  then rerun the validation commands.
