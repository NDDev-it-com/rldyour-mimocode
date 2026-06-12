# Contributing

Keep this repository focused on MiMoCode configuration, installer, doctor,
policy, validation, documentation, and release metadata.

rldyour AI CLI configuration for MiMoCode: native .mimocode config, build/plan/compose agents, persistent memory projection, commands, skills, MCP, browser routing, and runtime validation.

Do not vendor Xiaomi MiMoCode source code, binaries, logos, QR codes, or
trademarked assets. Runtime facts must come from source-backed upstream evidence
or a locally installed `mimo` binary.

Before opening a change:

```bash
python3 -m pytest -q
scripts/validate_fast.sh
```

Repository artifacts are English. Invocation metadata that helps the Russian
owner trigger commands or skills should be Russian-first with an English suffix.
