# MEMORY-01-MIMOCODE-SERENA-BOUNDARY

## Purpose

Record the boundary between Serena memories and MiMoCode native memory.

## Current Facts

- Serena memories are release-grade cross-tool durable facts.
- MiMoCode `MEMORY.md` is a tracked runtime projection from verified facts.
- `checkpoint.md`, `notes.md`, SQLite memory stores, and `tasks/<id>/progress.md`
  are runtime/session artifacts and ignored by default.
- MiMoCode `/dream` and `/distill` output must enter reviewable source changes
  before it becomes durable memory or adapter surface.

## Evidence

- `config/memory-boundary-policy.json`
- `MEMORY.md`
- `.gitignore`
- `scripts/validate_mimocode_memory_boundary.py`

## Operational Rules

- Do not overwrite Serena memories from MiMoCode runtime memory.
- Do not commit runtime memory artifacts unless the owner explicitly curates
  them as source-backed documentation.

## Last Verified

2026-06-13
