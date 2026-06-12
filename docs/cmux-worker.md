# cmux Worker Mode

MiMoCode can be launched as a visible cmux worker terminal.

It must not be modeled as:

- a background orchestrator;
- a headless orchestrator;
- a daemon orchestrator;
- a replacement for the visible cmux orchestrator terminal.

In rldyour cmux orchestrator mode, one visible terminal session is the
orchestrator and worker sessions return scoped reports. Worker agents do not
push, publish fullrepo, run system install, delete branches, mutate policy, or
perform final sync unless the visible orchestrator explicitly delegates that
exact action.
