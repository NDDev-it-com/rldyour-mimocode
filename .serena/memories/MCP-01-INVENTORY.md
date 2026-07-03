<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MCP runtime transport and pin policy
Area: MCP
-->

# MCP-01-INVENTORY

## Scope
MCP runtime transport and pin policy

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- MiMoCode projects only the approved active MCP inventory from root policy.
- Chrome DevTools MCP remains the DevTools, performance, network, console,
  memory, and Lighthouse provider.
- MiMoCode MCP configuration is stored in `.mimocode/mimocode.jsonc`.
- Removed or historical MCP tools are not active inventory.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
