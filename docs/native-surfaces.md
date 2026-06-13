# Native Surfaces

MiMoCode project configuration is stored under `.mimocode/`.

This adapter follows the upstream repository layout for custom command files:
`.mimocode/command/*.md`. Current public docs also describe `commands/` in
places, so installer/runtime validation must be revisited when a future MiMoCode
release changes discovery rules.

Skills use `SKILL.md` files with `name` and `description` frontmatter. Agent
definitions use Markdown frontmatter with `description`, `mode`, and optional
permission fields.

Russian owner triggers are encoded in command and skill descriptions. The body
text remains English for stable repo artifacts and validator matching.

## Config File Naming

This adapter uses `.mimocode/mimocode.jsonc` for project configuration. JSONC is
JSON with comments and trailing commas. Upstream MiMo-Code documentation
sometimes names this file `.mimocode/mimocode.json`, while the upstream
repository example ships `.mimocode/mimocode.jsonc`. The adapter intentionally
uses `.jsonc` because comments and trailing commas are part of the
OpenCode-derived config style and match the upstream repository example. Do not
rename `.mimocode/mimocode.jsonc` to `.mimocode/mimocode.json` without verifying
the MiMoCode runtime's accepted file names; the installer materializes runtime
config according to MiMoCode's accepted names.
`scripts/validate_mimocode_config_filename_policy.py` enforces this policy.

## Config Schema Selection

The config `$schema` points at `https://opencode.ai/config.json` because
MiMoCode is an OpenCode fork and its project config is OpenCode-config
compatible, and that URL resolves. The previous
`https://mimo.xiaomi.com//config.json` value had a doubled slash and returned
HTTP 404. MiMoCode-native keys (for example `checkpoint` and `maxMode`) extend
the OpenCode schema and may surface as editor schema warnings; runtime config
correctness is enforced by `scripts/validate_mimocode_config.py`, and schema-URL
hygiene by `scripts/validate_mimocode_schema_url.py`.
