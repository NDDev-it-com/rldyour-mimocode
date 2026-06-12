---
description: Sync durable memory facts while preserving Serena as source of truth
mode: subagent
permission:
  edit: ask
  bash: ask
  task: ask
  skill: allow
---

Use this agent only when memory updates are requested or required by workflow.
Serena memories remain authoritative durable facts. MiMoCode `MEMORY.md` is a
projection and must be updated from code/config/tests, not speculation.
