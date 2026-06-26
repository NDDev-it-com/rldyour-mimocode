<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MiMoCode adapter memory index
Area: CORE-->

# CORE-01-INDEX

## Scope
MiMoCode adapter memory index.

## Current source of truth
- `path:VERSION`
- `path:config/rldyour-contract.json`
- `path:config/mimocode-baseline.json`
- `path:.mimocode/mimocode.jsonc`
- `path:MEMORY.md`
- `path:.serena/memories/MIMOCODE-01-ADAPTER-SURFACE.md`
- `path:.serena/memories/MEMORY-01-MIMOCODE-SERENA-BOUNDARY.md`
- `path:.serena/memories/BROWSER-01-VALIDATION.md`
- `path:.serena/memories/RELEASE-01-VALIDATION.md`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: ry-start no-fullrepo MiMoCode migration

## Facts
- `rldyour-mimocode` is the MiMoCode-native adapter repository.
- The current adapter release is `1.7.7`.
- The runtime baseline is MiMoCode `0.1.3` with binary `mimo`.
- The adapter owns `.mimocode` config, agent, command, skill, MCP, browser,
  cmux-worker, and runtime memory projection surfaces.
- Serena memories are durable cross-tool facts. MiMoCode `MEMORY.md` is a
  tracked MiMoCode runtime projection generated from verified facts.

## Evidence
- `path:VERSION`
- `path:README.md`
- `path:config/rldyour-contract.json`
- `path:config/mimocode-baseline.json`
- `path:.mimocode/mimocode.jsonc`
- `path:MEMORY.md`

## Known pitfalls
- Do not infer installed runtime state from this memory. `mimo --version` and
  `scripts/doctor_system_mimocode.sh --redact` are the runtime evidence.

## Update policy
Update after verified changes to adapter version, runtime baseline, native
surface layout, MCP/browser policy, memory boundary, or release gates.

## Delete / merge policy
- Delete or merge only when the source-of-truth files no longer support this
  memory and the replacement memory preserves the durable facts.

## Applies to
- `rldyour-mimocode`
- `modules/rldyour-mimocode`

## Source of truth
- The `Current source of truth` section above, plus current code,
  configuration, tests, git state, and live GitHub release state where this
  memory explicitly references release surfaces.

## Invariants
- MiMoCode is a first-class native adapter, not an OpenCode alias.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer product versions, runtime versions, permissions, release state,
  security posture, or tool behavior from this memory without checking the
  source of truth.

## Update Triggers
- Update after verified changes to source-of-truth files, runtime baselines,
  release tuple, validation gates, live release state, or durable agent
  workflow contracts.

## Validation Commands
- `python3 scripts/validate_fast.sh`
- `python3 -m pytest -q`
- `python3 scripts/validate_mimocode_memory_boundary.py --strict`

## Repair Procedure
- Re-read source-of-truth files, update only verified current facts, move stale
  facts to historical evidence, then rerun the validation commands.
