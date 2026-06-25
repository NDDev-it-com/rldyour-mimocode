---
description: Синхронизировать финальное состояние rldyour; EN: post-task sync
agent: build
---

Finalize after meaningful changes: verify git status, run required validators,
update Serena/MiMoCode memory projections when current facts changed, prepare
atomic commits, and push only when the workflow requires it. Agent context files
are part of tracked `main` and do not require a separate publish step.
