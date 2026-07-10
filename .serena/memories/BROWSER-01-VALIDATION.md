<!-- Memory Metadata
Last updated: 2026-07-10
Last verified: 2026-07-10
Last commit: fc49d21e6a65f86b93c4a1baea6fc8e0c982409f feat(browser): enforce managed CloakBrowser skill boundary (other)
Scope: browser-visible validation and debugging workflows
Area: BROWSER
-->

# BROWSER-01-VALIDATION

## Scope
browser-visible validation and debugging workflows

## Current source of truth
- `path:README.md`
- `path:config/browser-provider-policy.json`
- `path:.mimocode/skills/browser-review/SKILL.md`
- `path:.mimocode/agent/rldyour-browser-worker.md`
- `path:.mimocode/command/browser-review.md`
- `path:scripts/validate_mimocode_browser_provider_policy.py`

## Last verified
- date: 2026-07-10
- commit: `fc49d21e6a65f86b93c4a1baea6fc8e0c982409f`
- checked by: MiMoCode fail-closed browser policy validation

## Facts
- Every browser action first runs exact
  `$HOME/.local/bin/cloakbrowser-cdp-health`; missing or nonzero health stops as
  `NOT_PROVEN` with no fallback.
- Active browser execution is limited to exact managed Playwright CLI and the
  exact managed Chrome DevTools MCP transport. `run-code` and `--filename` are
  forbidden.
- `webwright-task` is compatibility intent routed through `browser-review`.
  Webwright runtime, MiMoCode built-in/raw browser surfaces, direct packages,
  alternate CDP/executable/config paths, and fallbacks are forbidden.
- The browser skill, agent, and command each carry the exact mandatory boundary;
  the agent also denies webfetch and task delegation.

## Evidence
- `commit:fc49d21e6a65f86b93c4a1baea6fc8e0c982409f`
- `path:README.md`
- `path:config/browser-provider-policy.json`
- `path:scripts/validate_mimocode_browser_provider_policy.py`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.

## Applies to

- The scope and source-of-truth paths declared in this memory.

## Source of truth

- The `Current source of truth` entries above, plus current code, configuration, tests, git state, and live GitHub state where this memory references live release or repository surfaces.

## Invariants

- Current code, configuration, tests, validators, git state, and live GitHub state override this memory whenever they disagree.

## Current State

- Treat the `Facts` section as the current durable state. Do not treat historical evidence, superseded notes, or previous release entries as current.

## Do Not Infer

- Do not infer runtime versions, product versions, commits, permissions, release state, security posture, or tool behavior from this memory without checking the source of truth.

## Update Triggers

- Update after verified changes to the source-of-truth files, runtime baselines, release tuple, validation gates, live release state, or durable agent-workflow contracts.

## Validation Commands

- Run `python3 scripts/validate_mimocode_browser_provider_policy.py --strict`.
- Run `python3 -m pytest -q tests/test_mimocode_browser_policy.py`.
- Run the rldyour control-plane Serena memory validators in strict mode: `validate_serena_memory_schema` (`--strict-mode strict-all`) and `validate_serena_memory_semantics` (`--strict-current-facts --strict-metadata-dates --strict-evidence-commits`).

## Repair Procedure

1. Re-read the source-of-truth files listed above.
2. Update only verified current facts; move stale facts into historical evidence.
3. Rerun the validation commands until green.
