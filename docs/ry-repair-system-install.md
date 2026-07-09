# ry-repair System Install

Runtime install is intentionally separate from adapter config materialization.

Install the runtime through `rldyour-new-mac-or-ubuntu`'s frozen AI CLI bundle:

```bash
bash scripts/bootstrap.sh --platform <macos|ubuntu> --profile <desktop|server> --apply
```

That bootstrap publishes the exact managed `~/.local/bin/mimo` wrapper without
executing a remote installer stream. Then materialize rldyour system config:

```bash
bash scripts/install_system_mimocode.sh --apply
bash scripts/doctor_system_mimocode.sh --redact
```

`doctor_system_mimocode.sh` reports `NOT_PROVEN` when `mimo` is unavailable
instead of treating a missing runtime as success.
