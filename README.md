# rldyour-mimocode

`rldyour-mimocode` is the native MiMoCode configuration adapter for the
rldyour AI CLI control plane. It is a public AGPL-3.0-or-later configuration
repository that projects rldyour lifecycle, memory, MCP, browser-provider, and
cmux-worker policies into MiMoCode's native `.mimocode` surfaces.

Current release:

| Surface | Value |
| --- | --- |
| Adapter version | `1.0.1` |
| Runtime baseline | MiMoCode `0.1.0` |
| Runtime binary | `mimo` |
| Primary install channel | official Xiaomi MiMo installer / GitHub release assets |
| Secondary install channel | `npm install -g @mimo-ai/cli@0.1.0` after registry provenance validation |
| License for this repo | `AGPL-3.0-or-later` |

## Native Boundaries

MiMoCode is OpenCode-derived, but this adapter is not an OpenCode alias. The
adapter owns MiMoCode-native project configuration:

- `.mimocode/mimocode.jsonc`
- `.mimocode/tui.json`
- `.mimocode/agent/*.md`
- `.mimocode/command/*.md`
- `.mimocode/skills/*/SKILL.md`
- `.mimocode/glossary/`
- `.mimocode/plugins/`
- `.mimocode/themes/`
- `MEMORY.md`

MiMoCode compose, subagents, background work, `/goal`, `/dream`, and `/distill`
are MiMoCode-native session features. They are not rldyour cmux orchestrator
mode and must not be described as hidden daemon orchestration.

## Russian-First Operation

The owner normally works in Russian. Command and skill descriptions therefore
start with Russian trigger wording and include English trigger suffixes. Code,
metadata, and durable documentation stay English and ASCII-stable.

## Memory Boundary

Serena memories are the cross-tool source-of-truth project memory. MiMoCode
`MEMORY.md` is a native runtime projection from verified repository facts.
MiMoCode runtime files such as `checkpoint.md`, `notes.md`, SQLite databases,
and `tasks/<id>/progress.md` are session artifacts and are ignored by default.
`/dream` and `/distill` output must enter normal reviewable source changes
before it becomes release memory or adapter code.

## Security Boundary

MiMoCode permissions are runtime UX controls, not a security sandbox. This
adapter documents owner-approved automation posture, but true isolation still
requires a container, VM, or another operating-system boundary. No OAuth token,
API key, auth file, provider credential, or MiMo Auto session state is committed.

## Validation

```bash
python3 -m pytest -q
python3 scripts/validate_mimocode_config.py --strict
python3 scripts/validate_mimocode_runtime_baseline.py --strict
python3 scripts/validate_mimocode_mcp_inventory.py --strict
python3 scripts/validate_mimocode_commands.py --strict
python3 scripts/validate_mimocode_agents.py --strict
python3 scripts/validate_mimocode_skills.py --strict
python3 scripts/validate_mimocode_projection_parity.py --strict
python3 scripts/validate_mimocode_memory_boundary.py --strict
python3 scripts/validate_mimocode_browser_provider_policy.py --strict
python3 scripts/validate_mimocode_cmux_boundary.py --strict
```

Runtime doctor:

```bash
bash scripts/doctor_system_mimocode.sh --redact
```

If `mimo` is not installed, the doctor reports `NOT_PROVEN` instead of faking a
pass.
