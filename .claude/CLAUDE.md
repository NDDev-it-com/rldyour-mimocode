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
python3 scripts/validate_mimocode_browser_provider_policy.py --strict
scripts/validate_fast.sh
```

## Boundaries

Use MiMoCode-native CLI/project surfaces only.
Before every browser action, require exact managed CloakBrowser health. Execute
only exact managed Playwright CLI or the configured managed Chrome DevTools MCP
transport. `webwright-task` is compatibility intent only; the Webwright runtime
and every fallback are forbidden.

## CI runner selection

This repository is public, so `pull_request` executes untrusted fork code.
Every caller of a `NDDev-OpenNetwork/ci-workflows` reusable that exposes a `runner`
input passes `runner: ubuntu-latest` explicitly, and must keep it. Several of
those reusables default `runner` to the estate's self-hosted `amsterdam`
label, and a default is a property of the **pinned commit**, not of this
repository — so dropping the explicit value would let a routine pin bump route
fork PRs onto trusted private infrastructure with no diff here to review. On
any ci-workflows pin bump, diff `inputs.runner.default` between the old and
new commit before merging.
