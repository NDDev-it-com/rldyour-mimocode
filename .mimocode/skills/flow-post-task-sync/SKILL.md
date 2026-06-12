---
name: flow-post-task-sync
description: Используй для финальной синхронизации rldyour после задачи. EN: post-task sync.
---

# flow-post-task-sync

Finish work by verifying:

- Git status and submodule status.
- Targeted adapter validators.
- Root control-plane validators when root pins/contracts changed.
- Serena memories and MiMoCode `MEMORY.md` if durable facts changed.
- Fullrepo publish when agent-only context changed.

Workers must not push, publish fullrepo, or perform final sync unless that exact
action was explicitly delegated by the visible orchestrator/owner.
