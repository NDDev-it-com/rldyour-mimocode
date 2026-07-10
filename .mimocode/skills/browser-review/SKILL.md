---
name: browser-review
description: Используй для browser QA только через управляемые Playwright CLI и Chrome DevTools MCP. EN: managed CloakBrowser evidence review.
---

# browser-review

## Mandatory CloakBrowser Boundary

This boundary applies before every browser action:

1. Run exactly:

   ```bash
   $HOME/.local/bin/cloakbrowser-cdp-health
   ```

   If the command is missing or exits nonzero, stop immediately and report `NOT_PROVEN`.
2. Browser execution is permitted only through:
   - the exact `$HOME/.local/bin/playwright-cli` executable; `run-code` and `--filename` are forbidden;
   - the approved Chrome DevTools MCP transport, exactly `/bin/sh -c 'exec "$HOME/.local/bin/chrome-devtools-mcp" --headless --isolated --no-usage-statistics --no-performance-crux'`.
3. Never execute the Webwright Python runtime, stock/raw/in-app Browser, `browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright, `bunx`, `npx`, direct package invocations, alternate CDP endpoints, alternate browser executables, alternate browser configs, or any fallback. No fallback is allowed.

Use the managed Playwright CLI for browser flows, screenshots, snapshots, traces,
responsive checks, and long-horizon stepwise workflows. Use the managed Chrome
DevTools MCP transport for console, network, runtime, DOM/layout, performance,
Lighthouse, and memory diagnosis. `webwright-task` is a compatibility intent
only; it routes here and never authorizes Webwright runtime execution.

Run health again immediately before every browser action:

```bash
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" open "$URL"
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" snapshot
$HOME/.local/bin/cloakbrowser-cdp-health
$HOME/.local/bin/playwright-cli -s="${RY_PROJECT_SLUG:-rldyour}" screenshot
```

Report exact evidence paths and `NOT_PROVEN` for anything this boundary cannot
verify.
