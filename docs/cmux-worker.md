# cmux Worker Mode

This document is generated from root `config/cmux-adapter-projections.json`. Do not edit manually.

## Native Adapter Notes

- MiMoCode is worker-only for rldyour cmux mode.
- MiMoCode compose, subagents, background tasks, dream, goal, and memory behavior remain native MiMoCode features, not rldyour cmux workers.

## Current Implementation Status

- `typed-task-report-protocol`: `IMPLEMENTED`.
- `live-start-fail-closed`: `IMPLEMENTED`.
- `compact-template`: `IMPLEMENTED`.
- `workspace-group-topology`: `PLANNED`.
- `delegation-command`: `PLANNED`.
- `worktree-scheduler`: `PLANNED`.
- `adapter-native-projections`: `IMPLEMENTED`.
- `stop-finalization-receipt`: `PLANNED`.

Treat `PLANNED` and `NOT_PROVEN` entries as unavailable in production.

MiMoCode may participate as a visible worker terminal only. Its native compose, subagent, background, goal, dream, and memory features remain MiMoCode-native and do not replace the rldyour visible head terminal.

Worker completion requires a root schema-valid report; notifications are UI signals only.
