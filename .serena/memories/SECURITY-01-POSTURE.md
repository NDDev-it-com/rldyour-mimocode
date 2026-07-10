<!-- Memory Metadata
Last updated: 2026-05-22
Last verified: 2026-05-22
Last commit: 943ce4031fc4d87b2108cc19a009f4d89ec3be18 chore(release): mimocode 1.7.31 (other)
Scope: security posture and blocking/warning policy
Area: SECURITY
-->

# SECURITY-01-POSTURE

## Scope
security posture and blocking/warning policy

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `943ce4031fc4d87b2108cc19a009f4d89ec3be18`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- MiMoCode runtime permissions are UX controls, not a sandbox or security
  isolation boundary.
- The adapter repository is AGPL-3.0-or-later and does not vendor upstream
  Xiaomi MiMoCode source, binary assets, logos, or trademarked branding.
- Upstream MiMoCode is referenced as a separate runtime under upstream license
  and use restrictions.
- Secrets, OAuth state, API tokens, runtime databases, checkpoints, notes, and
  task progress artifacts must not be committed.

## Evidence
- `commit:943ce4031fc4d87b2108cc19a009f4d89ec3be18`
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
