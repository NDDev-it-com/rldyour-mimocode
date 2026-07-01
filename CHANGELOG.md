# Changelog

## [1.7.10] - 2026-06-29

### Fixed

- Harden Ruff and Pyright baseline across adapter configs.

## [1.7.7] - 2026-06-27

### Changed

- Refresh shadcn MCP runtime pin to the latest published 4.12.0 release.

## [1.7.6] - 2026-06-26

### Changed

- Sync Serena release memories after runtime and MCP refresh.

## [1.7.5] - 2026-06-26

### Changed

- Refresh CLI runtime and MCP pins to latest stable versions.

## [1.7.4] - 2026-06-26

### Fixed

- Publish a clean follow-up release with a valid Conventional Commit head subject after the 1.7.3 release commit subject included literal quotes.

## [1.7.3] - 2026-06-26

### Fixed

- State that the `1.7.x` support label tracks only the latest released patch in the security policy.

## [1.7.2] - 2026-06-26

### Fixed

- Align README memory heading with the shared tracked-context adapter template.

## [1.7.1] - 2026-06-26

### Fixed

- Sync generated cmux worker/orchestrator skill projections with the tracked-context branch model.

## [Unreleased]


## [1.7.15] - 2026-07-01

### Changed

- Refresh Codex CLI 0.142.5 and Playwright CLI 0.1.15 adapter baselines.
- Align Playwright CLI browser provider pin to 0.1.15.

## [1.7.14] - 2026-06-29

### Changed

- Refresh MiMoCode runtime baseline to 0.1.4.

## [1.7.13] - 2026-06-29

### Fixed

- Install pytest dependencies in required CI validation workflows.

## [1.7.12] - 2026-06-29

### Fixed

- Enforce five-adapter validation parity and structured release evidence

## [1.7.11] - 2026-06-29

### Fixed

- Enforce five-adapter validation parity and structured release evidence

## [1.7.9] - 2026-06-27

### Fixed

- Refresh MiMoCode Serena release memory.

## [1.7.8] - 2026-06-27

### Fixed

- Refresh setup-python action pin.

## [1.7.0] - 2026-06-26

### Changed

- Remove fullrepo-boundary from MiMoCode configuration: agent context (.serena/project.yml and .serena/memories) is tracked on `main`; remove fullrepo branch machinery and branch-protection settings.
- `scripts/validate_mimocode_security_boundary.py` and runtime docs now state durable context policy directly on main branch.
- Remove managed fullrepo publish lifecycle (`publish_fullrepo`, bootstrap, and restore steps) from MiMoCode sync scripts and instructions.

## [1.6.1] - 2026-06-25

### Changed

- Refresh CLI runtime baselines to latest (Claude Code 2.1.190, Codex 0.142.0, OpenCode 1.17.9, Antigravity CLI 1.0.11, MiMoCode 0.1.3); resolve adapter instruction-doc and surface-adoption drift.

## [1.6.0] - 2026-06-24

### Changed

- cmux worker v3 projections and latest MCP runtime pins (chrome-devtools-mcp 1.4.0, context7 3.2.2)

## [1.5.1] - 2026-06-15

### Changed

- Align SECURITY.md line label, adapter README baseline, and tracked uv.lock self-version to the 1.5.x line for the public governance gate.

## [1.5.0] - 2026-06-15

### Changed

- Owner-directed unified 1.5.0 release: perfect-sync quality wave (README baseline, ASCII hygiene, agy binary canonicalization, validator coverage).

## [1.0.13] - 2026-06-14

### Fixed

- Five-adapter wave (codex/opencode/gemini/mimocode): owner autonomous standard (Gemini auto_edit+launcher YOLO, MiMoCode allow-all), ry-repair canonical flags, five-adapter contract matrix, SECURITY parity, MiMoCode runtime proof, unified ASCII public README template; root cmux worker-only, coverage policies, launchers gm/mm, enforcement validators.

## [1.0.12] - 2026-06-14

### Changed

- Pin Context7 MCP to latest 3.2.1

## [1.0.11] - 2026-06-13

### Changed

- Harden MiMoCode native config schema (resolvable OpenCode schema), document .json vs .jsonc naming, and enforce permission/MCP security-boundary docs with new validators.

## [1.0.10] - 2026-06-13

### Fixed

- Re-pinned Actionlint and CodeQL workflow actions to live, resolvable upstream
  commit SHAs so required public CI checks can start reliably.

## [1.0.9] - 2026-06-13

### Fixed

- Kept the standard `[Unreleased]` changelog section present and empty for
  release-ready root policy validation.

## [1.0.8] - 2026-06-13

### Fixed

- Restored the standard `[Unreleased]` changelog section required by the
  root release-version policy.

## [1.0.7] - 2026-06-13

### Fixed

- Moved Serena project knowledge out of the normal branch so MiMoCode follows
  the same agent-only/fullrepo boundary as the other fullrepo-managed adapters.

## [1.0.6] - 2026-06-13

### Fixed

- Normalized all MiMoCode Serena memories to the strict metadata and
  source-of-truth template used by the root release validators.

## [1.0.5] - 2026-06-13

### Fixed

- Hardened the public secret-scan workflow with scheduled coverage,
  full-history checkout, and explicit gitleaks-compatible provenance markers.
- Updated release memory facts so adapter health checks can prove the current
  supported release from agent-only knowledge.

## [1.0.4] - 2026-06-13

### Fixed

- Added the canonical GitHub repository description to README and
  CONTRIBUTING so public metadata surface validation can prove exact parity.

## [1.0.3] - 2026-06-13

### Fixed

- Normalized the `NOTICE` author additional-grant sentence onto one line so the
  root AGPL metadata validator can prove the exact policy wording.

## [1.0.2] - 2026-06-13

### Fixed

- Added Windows to the public cross-platform smoke matrix so MiMoCode matches
  the root public-adapter runner coverage policy from its first supported line.

## [1.0.1] - 2026-06-13

### Fixed

- Added complete public-repository governance and release supply-chain surfaces
  for root policy validation.
- Kept `1.0.0` as the initial public tag and advanced the active supported
  adapter patch after follow-up release-wrapper hardening.

## [1.0.0] - 2026-06-13

### Added

- Initial public rldyour MiMoCode adapter.
- Native `.mimocode` project config, TUI config, agents, commands, skills,
  glossary, plugin, theme, and `MEMORY.md` projection surfaces.
- MiMoCode runtime baseline for upstream `v0.1.0`.
- Explicit Serena/MiMoCode memory boundary and `/dream`/`/distill` review gate.
- MCP and browser-provider policies matching the rldyour active inventories.
- cmux worker-only boundary: MiMoCode is a visible worker/direct CLI, not a
  background orchestrator.
