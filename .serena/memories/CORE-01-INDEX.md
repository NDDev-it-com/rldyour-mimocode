# CORE-01-INDEX

## Purpose

Index the MiMoCode adapter durable memory set.

## Current Facts

- `rldyour-mimocode` is the MiMoCode-native adapter repository.
- The adapter owns `.mimocode` config, agent, command, skill, MCP, browser,
  cmux-worker, and runtime memory projection surfaces.
- Serena memories are durable cross-tool facts; MiMoCode `MEMORY.md` is a
  runtime projection.

## Evidence

- `config/rldyour-contract.json`
- `config/mimocode-baseline.json`
- `.mimocode/mimocode.jsonc`
- `MEMORY.md`
- `.serena/memories/MIMOCODE-01-ADAPTER-SURFACE.md`
- `.serena/memories/MEMORY-01-MIMOCODE-SERENA-BOUNDARY.md`
- `.serena/memories/BROWSER-01-VALIDATION.md`
- `.serena/memories/RELEASE-01-VALIDATION.md`

## Operational Rules

- Keep memories short and evidence-backed.
- Mark runtime facts `NOT_PROVEN` when the installed `mimo` binary is absent.

## Last Verified

2026-06-13
