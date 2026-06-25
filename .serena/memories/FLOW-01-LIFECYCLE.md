<!-- Memory Metadata
Last updated: 2026-06-25
Last verified: 2026-06-25
Last commit: 6ecb87450652175d25efc42128884b7fa2b2fc2f chore(release): mimocode 1.7.0
Scope: MiMoCode rldyour lifecycle projection
Area: FLOW-->

# FLOW-01-LIFECYCLE

## Scope
MiMoCode rldyour lifecycle projection.

## Current source of truth
- `path:.mimocode/command/`
- `path:.mimocode/skills/`
- `path:.mimocode/agent/`
- `path:scripts/validate_mimocode_commands.py`
- `path:scripts/validate_mimocode_skills.py`
- `path:scripts/validate_mimocode_agents.py`

## Last verified
- date: 2026-06-25
- commit: `6ecb87450652175d25efc42128884b7fa2b2fc2f`
- checked by: Codex rldyour-flow sync

## Facts
- MiMoCode exposes native command projections for `ry-init`, `ry-start`,
  `ry-newp`, `ry-review`, `ry-repair`, `ry-deploy`, and `ry-sync`.
- MiMoCode skills include `ry-start`, `ry-repair`, `flow-post-task-sync`,
  browser/design/security review, Serena memory sync, and cmux worker support.
- MiMoCode compose/subagent/background runtime features are native session
  features, not rldyour cmux orchestrator mode.

## Evidence
- `path:.mimocode/command/ry-start.md`
- `path:.mimocode/skills/ry-start/SKILL.md`
- `path:.mimocode/skills/flow-post-task-sync/SKILL.md`
- `path:.mimocode/agent/rldyour-compose.md`
- `path:scripts/validate_mimocode_commands.py`
- `path:scripts/validate_mimocode_skills.py`
- `path:scripts/validate_mimocode_agents.py`

## Known pitfalls
- Do not describe MiMoCode compose or background work as a hidden rldyour
  orchestrator.

## Update policy
Update after command, skill, agent, flow parity, or cmux worker policy changes.

## Delete / merge policy
- Delete or merge only when lifecycle projection moves to another durable
  memory and the replacement preserves current facts.

## Applies to
- `.mimocode/command/`
- `.mimocode/skills/`
- `.mimocode/agent/`

## Source of truth
- The `Current source of truth` section above, plus root flow parity policy.

## Invariants
- All canonical rldyour flows must stay present as MiMoCode-native surfaces.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer that native MiMoCode subagents may push, publish durable context, or
  perform final sync unless explicitly delegated by the visible orchestrator.

## Update Triggers
- Update after lifecycle command, skill, subagent, flow parity, or cmux worker
  protocol changes.

## Validation Commands
- `python3 scripts/validate_mimocode_commands.py --strict`
- `python3 scripts/validate_mimocode_skills.py --strict`
- `python3 scripts/validate_mimocode_agents.py --strict`

## Repair Procedure
- Re-read native flow surfaces, update only verified facts, then rerun the
  validation commands.
