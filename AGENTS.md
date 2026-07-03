# AGENTS.md - rldyour-mimocode

This is the MiMoCode adapter package for the rldyour AI CLI control plane.
It owns MiMoCode-native project configuration under `.mimocode/`, runtime
validation rules, and command/agent/skill projection.

## Source of Truth

- `config/mimocode-baseline.json`
- `references/mimocode-baseline.json`
- `.mimocode/mimocode.jsonc`
- `.mimocode/command/*.md`
- `.mimocode/agent/*.md`
- `.mimocode/skill/*/SKILL.md`
- `scripts/*.sh`, `scripts/*.py`
- `config/rldyour-contract.json`

## Native Boundaries

Use MiMoCode-native surfaces only:

- `.mimocode/`
- `mimocode` binary config layout and command handlers
- runtime validation scripts in this repo

Do not introduce Claude/Antigravity/Codex native config formats as runtime controls.

## Runtime Baseline

- MiMoCode runtime version is `0.1.4` (from `config/mimocode-baseline.json`).
- `curl` installer path and optional npm secondary channel are validated via
  dedicated runtime checks.

## Validation Commands

```bash
bash scripts/install_system_mimocode.sh --apply
bash scripts/doctor_system_mimocode.sh --redact
python3 scripts/validate_contract.py
python3 scripts/validate_mimocode_runtime_baseline.py
python3 scripts/validate_mimocode_config.py
python3 scripts/validate_mimocode_memory_boundary.py
python3 scripts/validate_mimocode_projection_parity.py
python3 scripts/validate_instruction_docs.py
python3 scripts/validate_release_assets.py
```

## Security Policy

- Secrets, API tokens, and local browser artifacts are never committed.
- Keep `.serena/` durable state updated while runtime artifacts stay gitignored.
- Any permission model change requires accompanying validation evidence.
