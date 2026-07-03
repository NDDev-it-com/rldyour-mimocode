<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: Serena memory, fullrepo, and knowledge sync policy
Area: SERENA
-->

# SERENA-01-MEMORY-SYNC

## Scope
Serena memory, fullrepo, and knowledge sync policy

## Current source of truth
- `path:.serena/project.yml`
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- MiMoCode adapter Serena memories use the same strict template and
  source-of-truth policy as the root release validators.
- Required domains for MiMoCode are `CORE`, `MIMOCODE`, `RUNTIME`, `MCP`,
  `BROWSER`, `FLOW`, `SECURITY`, `RELEASE`, `SERENA`, and `MEMORY`.
- Serena memories are durable cross-tool facts; MiMoCode `MEMORY.md` is a
  runtime projection.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:.serena/project.yml`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
