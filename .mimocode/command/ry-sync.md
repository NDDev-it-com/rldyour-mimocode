---
description: Синхронизировать финальное состояние rldyour; EN: post-task sync
agent: build
---

Finalize after meaningful changes: verify git status, run required validators,
update Serena/MiMoCode memory projections when current facts changed, prepare
atomic commits, push only when the workflow requires it, and publish fullrepo
when agent-only files changed.
