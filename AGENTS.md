# AGENTS.md - rldyour-mimocode

rldyour AI CLI configuration for MiMoCode: native .mimocode config, build/plan/compose agents, persistent memory projection, commands, skills, MCP, browser routing, and runtime validation.
This is the MiMoCode adapter package for the rldyour AI CLI control plane.
It owns MiMoCode-native project configuration under `.mimocode/`, runtime
validation rules, and command/agent/skill projection.

## Source of Truth

- `config/mimocode-baseline.json`
- `.mimocode/mimocode.jsonc`
- `.mimocode/command/*.md`
- `.mimocode/agent/*.md`
- `.mimocode/skills/*/SKILL.md`
- `scripts/*.sh`, `scripts/*.py`
- `config/rldyour-contract.json`

## Native Boundaries

Use MiMoCode-native surfaces only:

- `.mimocode/`
- `mimocode` binary config layout and command handlers
- runtime validation scripts in this repo

Do not introduce Claude/Antigravity/Codex native config formats as runtime controls.

## Runtime Baseline

- MiMoCode runtime version is `0.1.5` (from `config/mimocode-baseline.json`).
- `curl` installer path and optional npm secondary channel are validated via
  dedicated runtime checks.

## Validation Commands

```bash
scripts/validate_fast.sh
python3 scripts/validate_mimocode_runtime_baseline.py
python3 scripts/validate_mimocode_config.py
python3 scripts/validate_mimocode_memory_boundary.py
python3 scripts/validate_mimocode_projection_parity.py
python3 scripts/validate_mimocode_browser_provider_policy.py --strict
python3 scripts/validate_release_assets.py
```

## Browser Boundary

- Run exact `$HOME/.local/bin/cloakbrowser-cdp-health` before every browser
  action; missing or nonzero health stops as `NOT_PROVEN`.
- Execute only exact `$HOME/.local/bin/playwright-cli` or the exact managed
  Chrome DevTools MCP transport in `.mimocode/mimocode.jsonc`.
- `webwright-task` is compatibility intent routed through `browser-review`.
  Webwright runtime execution, built-in/raw browser surfaces, direct packages,
  alternate CDP/executables/configs, and fallbacks are forbidden.

## Security Policy

- Secrets, API tokens, and local browser artifacts are never committed.
- Keep `.serena/` durable state updated while runtime artifacts stay gitignored.
- Any permission model change requires accompanying validation evidence.
