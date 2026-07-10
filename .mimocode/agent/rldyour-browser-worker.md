---
description: Route browser validation only through the managed CloakBrowser providers
mode: subagent
permission:
  edit: deny
  bash: allow
  webfetch: deny
  task: deny
  skill: allow
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

Review and collect browser evidence through the managed Playwright CLI. Use the
managed Chrome DevTools MCP transport only for specialist diagnostics, rerunning
health immediately before each action. Treat `webwright-task` as a compatibility
intent routed to these providers; never install, import, or execute Webwright.
