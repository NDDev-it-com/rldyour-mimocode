<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.4 (no-fullrepo)
Scope: MiMoCode browser-provider routing
Area: BROWSER-->

# BROWSER-01-VALIDATION

## Scope
MiMoCode browser-provider routing.

## Current source of truth
- `path:config/browser-provider-policy.json`
- `path:.mimocode/skills/browser-review/SKILL.md`
- `path:.mimocode/agent/rldyour-browser-worker.md`
- `path:scripts/validate_mimocode_browser_provider_policy.py`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex rldyour-flow sync

## Facts
- Webwright is the high-level long-horizon browser workflow provider.
- Playwright CLI is the low-level screenshot, snapshot, trace, and visual
  evidence provider.
- Chrome DevTools MCP is the console, network, performance, memory,
  Lighthouse, and live-debug provider.
- MiMoCode built-in or future browser features are disabled as release
  providers until a separate provider model and validator are added.

## Evidence
- `path:config/browser-provider-policy.json`
- `path:.mimocode/skills/browser-review/SKILL.md`
- `path:.mimocode/agent/rldyour-browser-worker.md`
- `path:scripts/validate_mimocode_browser_provider_policy.py`

## Known pitfalls
- Do not treat a future MiMoCode built-in browser feature as approved just
  because the runtime exposes it.

## Update policy
Update after browser provider policy, browser skills, browser worker agents, or
browser validation commands change.

## Delete / merge policy
- Delete or merge only when MiMoCode no longer projects browser-provider
  routing and the replacement memory preserves the durable facts.

## Applies to
- `.mimocode/skills/browser-review/SKILL.md`
- `.mimocode/agent/rldyour-browser-worker.md`
- `config/browser-provider-policy.json`

## Source of truth
- The `Current source of truth` section above, plus current root browser
  provider policy and active provider inventory validators.

## Invariants
- Browser routing is positive-inventory-based.
- Unapproved browser providers must not be added without root policy updates.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer active provider approval from historical tool names or runtime
  availability alone.

## Update Triggers
- Update after browser provider policy, browser workflow, skill, agent, or
  validator changes.

## Validation Commands
- `python3 scripts/validate_mimocode_browser_provider_policy.py --strict`
- `python3 scripts/validate_fast.sh`

## Repair Procedure
- Re-read browser policy and native browser skill/agent files, update only
  verified facts, then rerun the validation commands.
