# Changelog

## [Unreleased]

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
