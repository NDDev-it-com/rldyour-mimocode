# BROWSER-01-VALIDATION

## Purpose

Record browser-provider routing for the MiMoCode adapter.

## Current Facts

- Webwright is the high-level long-horizon browser workflow provider.
- Playwright CLI is the low-level screenshot, snapshot, trace, and visual
  evidence provider.
- Chrome DevTools MCP is the console, network, performance, memory, Lighthouse,
  and live-debug provider.
- MiMoCode built-in/future browser features are disabled as release providers
  until a separate provider model and validator are added.

## Evidence

- `config/browser-provider-policy.json`
- `.mimocode/skills/browser-review/SKILL.md`
- `.mimocode/agent/rldyour-browser-worker.md`
- `scripts/validate_mimocode_browser_provider_policy.py`

## Operational Rules

- Keep browser routing positive-inventory-based.
- Do not add unapproved browser providers without root policy update.

## Last Verified

2026-06-13
