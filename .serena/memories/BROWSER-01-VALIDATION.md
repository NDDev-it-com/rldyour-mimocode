<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: browser-visible validation and debugging workflows
Area: BROWSER
-->

# BROWSER-01-VALIDATION

## Scope
browser-visible validation and debugging workflows

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Webwright is the high-level long-horizon browser workflow provider.
- Playwright CLI is the low-level screenshot, snapshot, trace, and visual
  evidence provider.
- Chrome DevTools MCP is the console, network, performance, memory,
  Lighthouse, and live-debug provider.
- MiMoCode built-in or future browser features are disabled as release
  providers until a separate provider model and validator are added.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
