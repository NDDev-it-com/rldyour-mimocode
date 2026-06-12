<!-- Memory Metadata
Last updated: 2026-06-13
Last verified: 2026-06-13
Last commit: 5ff1946483f51519450a1f6e95b7313df52af185 fix(release): restore MiMoCode changelog unreleased section
Scope: MiMoCode MCP inventory
Area: MCP-->

# MCP-01-INVENTORY

## Scope
MiMoCode MCP inventory.

## Current source of truth
- `path:config/mcp-inventory.json`
- `path:.mimocode/mimocode.jsonc`
- `path:scripts/validate_mimocode_mcp_inventory.py`

## Last verified
- date: 2026-06-13
- commit: `5ff1946483f51519450a1f6e95b7313df52af185`
- checked by: Codex rldyour-flow sync

## Facts
- MiMoCode projects only the approved active MCP inventory from root policy.
- Chrome DevTools MCP remains the DevTools, performance, network, console,
  memory, and Lighthouse provider.
- MiMoCode MCP configuration is stored in `.mimocode/mimocode.jsonc`.
- Removed or historical MCP tools are not active inventory.

## Evidence
- `path:config/mcp-inventory.json`
- `path:.mimocode/mimocode.jsonc`
- `path:scripts/validate_mimocode_mcp_inventory.py`

## Known pitfalls
- OpenCode-derived MCP compatibility does not waive MiMoCode inventory
  validation.

## Update policy
Update after MCP inventory, aliases, transport, env policy, or runtime config
format changes.

## Delete / merge policy
- Delete or merge only when MCP inventory tracking moves to another durable
  memory and the replacement preserves current facts.

## Applies to
- `.mimocode/mimocode.jsonc`
- `config/mcp-inventory.json`

## Source of truth
- The `Current source of truth` section above, plus root MCP inventory policy.

## Invariants
- Use positive active inventories, not tool-specific tombstone validators.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer approval for extra MCP servers from runtime support alone.

## Update Triggers
- Update after approved active MCP inventory changes, alias changes, transport
  changes, or root parity policy changes.

## Validation Commands
- `python3 scripts/validate_mimocode_mcp_inventory.py --strict`
- `python3 scripts/validate_fast.sh`

## Repair Procedure
- Re-read MCP policy and `.mimocode/mimocode.jsonc`, update only verified
  facts, then rerun the validation commands.
