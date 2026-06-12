# Architecture

`rldyour-mimocode` is a first-party configuration adapter for MiMoCode. It
projects rldyour lifecycle policy into MiMoCode-native surfaces rather than
copying OpenCode, Claude Code, Codex, or Gemini formats.

Primary surfaces:

- `.mimocode/mimocode.jsonc`
- `.mimocode/tui.json`
- `.mimocode/agent/*.md`
- `.mimocode/command/*.md`
- `.mimocode/skills/*/SKILL.md`
- `MEMORY.md`
- `config/*.json`
- `scripts/validate_*.py`
- `scripts/install_system_mimocode.sh`
- `scripts/doctor_system_mimocode.sh`

MiMoCode is OpenCode-derived upstream, but this adapter treats compatibility as
a hint only. Runtime behavior must be validated with MiMoCode facts and, when
available, the installed `mimo` binary.
