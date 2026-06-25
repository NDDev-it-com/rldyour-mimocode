# rldyour-mimocode

`rldyour-mimocode` is the native MiMoCode configuration adapter for the
rldyour AI CLI control plane. It projects rldyour lifecycle, memory, MCP,
browser-provider, and cmux-worker policies into MiMoCode's native `.mimocode`
surfaces. It is a public AGPL-3.0-or-later configuration repository and does
not vendor Xiaomi MiMoCode source, binaries, logos, QR codes, or trademarks.

rldyour AI CLI configuration for MiMoCode: native .mimocode config, build/plan/compose agents, persistent memory projection, commands, skills, MCP, browser routing, and runtime validation.

## Current Baseline

| Surface | Value |
| --- | --- |
| Adapter version | `1.7.4` |
| Runtime baseline | MiMoCode `0.1.3` |
| GitHub release tag | `1.7.4` |

## What This Repository Provides

This repository is a configuration package for Xiaomi MiMoCode, an
OpenCode-derived AI CLI. It projects rldyour skill, command, agent, MCP,
browser-provider, memory-boundary, and permission policies into MiMoCode's
native `.mimocode` directory layout. It does not vendor or modify MiMoCode
source code or binary assets. All implementation changes to MiMoCode itself
belong in the upstream `XiaomiMiMo/MiMo-Code` repository.

## Native Boundaries

MiMoCode project configuration is stored under `.mimocode/`. The adapter owns
the following MiMoCode-native surfaces:

- `.mimocode/mimocode.jsonc` - primary project config (JSONC officially
  supported; `.mimocode/mimocode.json` is also accepted). The runtime resolves
  `.jsonc` first via `jsonc-parser` (comments and trailing commas allowed), so
  no `.json` projection is needed.
- `.mimocode/tui.json` - TUI layout config.
- `.mimocode/command/*.md` - slash command definitions.
- `.mimocode/skills/*/SKILL.md` - skill definitions with `name` and
  `description` frontmatter.
- `.mimocode/agent/*.md` - agent definitions with `description`, `mode`, and
  optional permission fields.

Config schema points to `https://opencode.ai/config.json` because MiMoCode is
an OpenCode fork and its project config is OpenCode-config compatible. That URL
resolves. MiMoCode-native keys (for example `checkpoint` and `maxMode`) extend
the OpenCode schema and may surface as editor schema warnings; runtime config
correctness is enforced by `scripts/validate_mimocode_config.py`.

`build`, `plan`, and `compose` are native MiMoCode agent modes. MiMoCode
compose, subagents, background work, `/goal`, `/dream`, and `/distill` are
MiMoCode-native session features. They are not rldyour cmux orchestrator mode
and must not be described as hidden daemon orchestration.

## Install / Update / ry-repair

Install the MiMoCode runtime with a version pin:

```bash
curl -fsSL https://mimo.xiaomi.com/install | bash -s -- --version 0.1.3 --no-modify-path
```

The binary installs to `$HOME/.mimocode/bin/mimo`. As a secondary channel,
after registry provenance validation:

```bash
npm install -g @mimo-ai/cli@0.1.3
```

Materialize rldyour system config and verify the runtime:

```bash
bash scripts/install_system_mimocode.sh --apply
bash scripts/doctor_system_mimocode.sh --redact
```

The doctor reports `NOT_PROVEN` when `mimo` is unavailable instead of treating
a missing runtime as success. For full `ry-repair` convergence, see
`docs/ry-repair-system-install.md`.

## Active Catalog

**Skills** (`.mimocode/skills/`): `browser-review`, `cmux-worker`,
`design-review`, `flow-post-task-sync`, `ry-repair`, `ry-start`,
`security-review`, `serena-memory-sync`.

**Commands** (`.mimocode/command/`): `browser-review`, `design-review`,
`rules-review`, `ry-deploy`, `ry-init`, `ry-newp`, `ry-repair`, `ry-review`,
`ry-start`, `ry-sync`, `security-review`.

**Agents** (`.mimocode/agent/`): `rldyour-browser-worker`, `rldyour-build`,
`rldyour-compose`, `rldyour-design-worker`, `rldyour-memory-sync`,
`rldyour-plan`, `rldyour-quality-review`, `rldyour-review`,
`rldyour-security-review`.

**MCP servers** (`.mimocode/mimocode.jsonc`):

| Server | Transport | Package / URL |
| --- | --- | --- |
| serena | local | `serena-agent==1.5.3` via `uvx` |
| chrome-devtools | local | `chrome-devtools-mcp@1.4.0` via `bunx` |
| sequential-thinking | local | `@modelcontextprotocol/server-sequential-thinking@2025.12.18` via `bunx` |
| shadcn | local | `shadcn@4.11.0` via `bunx` |
| dart-flutter | local | `dart mcp-server` |
| context7 | local | `@upstash/context7-mcp@3.2.2` via `bunx` |
| github | remote | `https://api.githubcopilot.com/mcp/` |
| deepwiki | remote | `https://mcp.deepwiki.com/mcp` |
| grep | remote | `https://mcp.grep.app` |
| figma | remote | `https://mcp.figma.com/mcp` |
| openai-docs | remote | `https://developers.openai.com/mcp` |

Permission policy: `allow` for all keys except `*.env` and `*.env.*` reads,
which are `deny`. The `plan` agent sets `edit: deny` as its read-only mode.

## Browser / Design / DevTools Routing

MiMoCode uses the same positive browser-provider inventory as the root control
plane:

- **Webwright** - long-horizon web workflows and reusable evidence scripts.
- **Playwright CLI** - deterministic screenshots, snapshots, traces, and visual
  evidence.
- **Chrome DevTools MCP** (`chrome-devtools-mcp@1.4.0`) - console, network,
  performance, memory, Lighthouse, and live Chrome debugging.

MiMoCode built-in or future browser features are disabled as release providers
until a separate provider model, policy, and validator are added.

## Repository Context / Serena Memory

Serena memories are the cross-tool source-of-truth project memory for release
facts, contracts, invariants, entry points, and validation commands.

`MEMORY.md` is a tracked projection generated from verified repository facts.
It is the MiMoCode-native project memory surface. Runtime-only files -
`checkpoint.md`, `notes.md`, SQLite databases, and `tasks/<id>/progress.md` -
are session artifacts and remain ignored by default.

`/dream` may suggest durable memory updates but cannot directly overwrite
Serena memories. `/distill` may suggest new skills, agents, or commands, but
the output must become normal reviewable source changes before it becomes
release memory or adapter code.

Serena context (`.serena/project.yml`, `.serena/memories/`) is tracked directly on
`main` as part of durable project facts.

## Security Boundary

Committed `.mimocode/mimocode.jsonc` sets the OpenCode permission ruleset to
`allow` for every key - `read`, `glob`, `grep`, `skill`, `bash`, `edit`,
`task`, `external_directory`, `doom_loop`, `webfetch`, `websearch`,
`codesearch`, `lsp`, and `question` - enabling full-auto, no-prompt operation.
`build` and `compose` agents inherit `bash: allow` and `edit: allow`. The
`*.env` and `*.env.*` read guard stays `deny`, and `plan` keeps `edit: deny`
as its read-only mode.

The `mm` launcher injects allow-all `MIMOCODE_CONFIG_CONTENT` at runtime.

MiMoCode permissions are runtime UX controls, not a security sandbox. Configured
MCP servers run outside the trust boundary and execute as trusted code. True
isolation still requires a container, VM, or another operating-system boundary.

No OAuth token, API key, auth file, provider credential, `MIMOCODE_AUTH_CONTENT`,
`MIMOCODE_CONFIG_CONTENT`, or MiMoCode runtime session state is committed.

## Validation

Fast static validation:

```bash
bash scripts/validate_fast.sh
```

Adapter-deep validation:

```bash
python3 -m pytest -q
python3 scripts/validate_mimocode_config.py --strict
python3 scripts/validate_mimocode_runtime_baseline.py --strict
python3 scripts/validate_mimocode_mcp_inventory.py --strict
python3 scripts/validate_mimocode_commands.py --strict
python3 scripts/validate_mimocode_agents.py --strict
python3 scripts/validate_mimocode_skills.py --strict
python3 scripts/validate_mimocode_projection_parity.py --strict
python3 scripts/validate_mimocode_memory_boundary.py --strict
python3 scripts/validate_mimocode_browser_provider_policy.py --strict
python3 scripts/validate_mimocode_cmux_boundary.py --strict
python3 scripts/validate_mimocode_security_boundary.py --strict
python3 scripts/validate_release_surfaces.py --strict
```

Installed-runtime doctor:

```bash
bash scripts/doctor_system_mimocode.sh --redact
```

If `mimo` is not installed, the doctor reports `NOT_PROVEN` instead of faking a
pass. Live-network lanes (MCP endpoint reachability, npm registry provenance)
require `mimo` to be installed and a live network connection; they are not
required to pass the static release gate.

## Release / Rollback

Adapter releases are numeric-tag-driven. Each supported product version must
have a matching GitHub Release at `NDDev-it-com/rldyour-mimocode`. The
`VERSION` file, `CHANGELOG.md`, and `SECURITY.md` are the three required public
surfaces. The default version movement is patch (`+0.0.1`); minor and major
bumps are owner-directed only.

To roll back, pin the submodule in the control plane to the previous numeric
commit and verify with `python3 scripts/validate_control_plane.py` at root.
Older tags are not supported unless re-released as the current exact tag (see
`SECURITY.md` for the supported-version policy).

## Support / License

License: `AGPL-3.0-or-later`. See `LICENSE`.

Author: Danil Silantyev (github:rldyourmnd), CEO NDDev.

Report security issues through **GitHub Security Advisories** for this
repository (`NDDev-it-com/rldyour-mimocode`). For MiMoCode runtime
vulnerabilities, also follow `XiaomiMiMo/MiMo-Code` upstream security
reporting guidance.

Use of Xiaomi MiMoCode is subject to upstream MiMoCode use restrictions in
addition to this repository's `AGPL-3.0-or-later` license.
