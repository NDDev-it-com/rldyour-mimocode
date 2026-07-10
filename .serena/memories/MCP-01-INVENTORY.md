<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MCP runtime transport and pin policy
Area: MCP
-->

# MCP-01-INVENTORY

## Scope
MCP runtime transport and pin policy

## Current source of truth
- `path:.mimocode/mimocode.jsonc`
- `path:config/mcp-inventory.json`
- `path:config/rldyour-contract.json`
- `path:docs/mcp-runtime-provenance.md`

## Last verified
- date: 2026-07-10
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- MiMoCode projects only the approved active MCP inventory from root policy.
- Chrome DevTools MCP remains the DevTools, performance, network, console,
  memory, and Lighthouse provider.
- MiMoCode MCP configuration is stored in `.mimocode/mimocode.jsonc`.
- Sequential Thinking is exact-pinned to
  `@modelcontextprotocol/server-sequential-thinking@2026.7.4` via `bunx`.
- Context7 is exact-pinned to `@upstash/context7-mcp@3.2.3` via `bunx`.
- Both exact packages completed credential-free MCP stdio `initialize` and
  `tools/list` probes using protocol `2025-11-25`.
- Registry SHA-512 integrity, upstream annotated-tag commit targets, and the
  zero-vulnerability production dependency audit are recorded in
  `config/mcp-inventory.json`; the release SBOM lists both packages.
- Removed or historical MCP tools are not active inventory.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:.mimocode/mimocode.jsonc`
- `path:config/mcp-inventory.json`
- `path:config/rldyour-contract.json`
- `path:docs/mcp-runtime-provenance.md`

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
