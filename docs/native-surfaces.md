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
