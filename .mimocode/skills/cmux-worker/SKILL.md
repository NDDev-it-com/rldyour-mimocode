---
name: cmux-worker
description: Используй для visible cmux worker reports only. EN: cmux worker.
---

# cmux-worker

MiMoCode may run as a visible cmux worker terminal. It must return scoped
reports and must not:

- Push branches or tags.
- Publish fullrepo.
- Delete branches.
- Mutate root policy.
- Run system install.
- Perform final sync.

MiMoCode compose/subagents/background execution do not replace rldyour cmux
orchestrator mode.
