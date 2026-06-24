# ry-repair System Install

Runtime install is intentionally separate from adapter config materialization.

Install the MiMoCode runtime with a version pin:

```bash
curl -fsSL https://mimo.xiaomi.com/install | bash -s -- --version 0.1.3 --no-modify-path
```

Then materialize rldyour system config:

```bash
bash scripts/install_system_mimocode.sh --apply
bash scripts/doctor_system_mimocode.sh --redact
```

`doctor_system_mimocode.sh` reports `NOT_PROVEN` when `mimo` is unavailable
instead of treating a missing runtime as success.
