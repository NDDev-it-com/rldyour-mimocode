---
name: ry-repair
description: Используй для ремонта repo/config/runtime/release drift. EN: repair convergence.
---

# ry-repair

Use this skill for release-wrapper, adapter, install, validation, docs, or memory
drift.

Rules:

- Code/config/tests are source of truth.
- Never fake a green check; report `NOT_PROVEN` when runtime evidence is absent.
- Repair root/adapters through native surfaces, not copied foreign commands.
- Keep MiMoCode runtime artifacts ignored unless explicitly curated.
- Run adapter validators before claiming convergence.
