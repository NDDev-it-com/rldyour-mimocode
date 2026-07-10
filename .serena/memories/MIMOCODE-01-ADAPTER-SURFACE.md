<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: fc49d21e6a65f86b93c4a1baea6fc8e0c982409f feat(browser): enforce managed CloakBrowser skill boundary (other)
Scope: MIMOCODE repository knowledge
Area: MIMOCODE
-->

# MIMOCODE-01-ADAPTER-SURFACE

## Scope
MIMOCODE repository knowledge

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-07-10
- commit: `fc49d21e6a65f86b93c4a1baea6fc8e0c982409f`
- checked by: MiMoCode adapter surface validation

## Facts
- Adapter version is `1.7.30`.
- Runtime baseline is MiMoCode `0.1.5` with binary `mimo`.
- Primary runtime install channel is the parent bootstrap's frozen Bun lock;
  `@mimo-ai/cli@0.1.5` is cross-checked against the official `v0.1.5` release.
- Native config surfaces are `.mimocode/mimocode.jsonc`, `.mimocode/tui.json`,
  `.mimocode/agent/*.md`, `.mimocode/command/*.md`, and
  `.mimocode/skills/*/SKILL.md`.
- Local MCP runtime pins are Sequential Thinking `2026.7.4` and Context7
  `3.2.3`; both use exact `bunx` package specs over stdio.
- MiMoCode is an active first-class adapter, not an OpenCode alias.

## Evidence
- `commit:fc49d21e6a65f86b93c4a1baea6fc8e0c982409f`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.

## Applies to

- The scope and source-of-truth paths declared in this memory.

## Source of truth

- The `Current source of truth` entries above, plus current code, configuration, tests, git state, and live GitHub state where this memory references live release or repository surfaces.

## Invariants

- Current code, configuration, tests, validators, git state, and live GitHub state override this memory whenever they disagree.

## Current State

- Treat the `Facts` section as the current durable state. Do not treat historical evidence, superseded notes, or previous release entries as current.

## Do Not Infer

- Do not infer runtime versions, product versions, commits, permissions, release state, security posture, or tool behavior from this memory without checking the source of truth.

## Update Triggers

- Update after verified changes to the source-of-truth files, runtime baselines, release tuple, validation gates, live release state, or durable agent-workflow contracts.

## Validation Commands

- Run the rldyour control-plane Serena memory validators in strict mode: `validate_serena_memory_schema` (`--strict-mode strict-all`) and `validate_serena_memory_semantics` (`--strict-current-facts --strict-metadata-dates --strict-evidence-commits`).

## Repair Procedure

1. Re-read the source-of-truth files listed above.
2. Update only verified current facts; move stale facts into historical evidence.
3. Rerun the validation commands until green.
