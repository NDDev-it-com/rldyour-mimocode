# Claude Code Project Memory - rldyour-mimocode

MiMoCode adapter memory for `rldyour-mimocode`.

## Source of Truth

- `.mimocode/mimocode.jsonc`
- `config/mimocode-baseline.json`
- `references/mimocode-baseline.json`
- `scripts/*.py`, `scripts/*.sh`
- `config/rldyour-contract.json`

## Runtime Baseline

- Runtime package: `@mimo-ai/cli@0.1.5` (secondary/npm channel).
- Primary install is GitHub release pin in runtime baseline file.

## Workflow

```bash
bash scripts/install_system_mimocode.sh --dry-run
bash scripts/install_system_mimocode.sh --apply
bash scripts/doctor_system_mimocode.sh --redact
```

Checks:

```bash
python3 scripts/validate_mimocode_config.py
python3 scripts/validate_mimocode_runtime_baseline.py
python3 scripts/validate_mimocode_projection_parity.py
python3 scripts/validate_mimocode_schema_url.py
python3 scripts/validate_instruction_docs.py
```

## Boundaries

Use MiMoCode-native CLI/project surfaces only.
Keep browser policy aligned with global rldyour routing (Webwright / Playwright CLI /
Chrome DevTools MCP).
