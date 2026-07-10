---
description: Проверить browser evidence через управляемый CloakBrowser boundary; EN: managed browser workflow review
agent: rldyour-browser-worker
subtask: true
---

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

Review the requested browser workflow through the managed Playwright CLI and
use the managed Chrome DevTools MCP transport only for diagnostics. Rerun health
before every action. A `webwright-task` request is compatibility intent, not
permission to execute Webwright. Return exact evidence or `NOT_PROVEN`.

Scope:

$ARGUMENTS
