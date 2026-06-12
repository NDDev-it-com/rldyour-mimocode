# Memory Boundary

Serena memories are the cross-tool source-of-truth project memory for release
facts, contracts, invariants, entry points, and validation commands.

MiMoCode memory is runtime-native:

- `MEMORY.md` is a tracked projection generated from verified facts.
- `checkpoint.md` is runtime/session state.
- `notes.md` is runtime scratch state.
- `tasks/<id>/progress.md` is task progress state.
- SQLite databases and indexes are runtime state.

`/dream` may suggest durable memory updates, but it cannot directly overwrite
Serena memories. `/distill` may suggest new skills, agents, or commands, but
the output must become normal reviewable source changes.
