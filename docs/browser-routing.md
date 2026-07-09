# Browser Routing

MiMoCode uses the same positive browser-provider inventory as the root control
plane:

- Webwright: long-horizon web workflows and reusable evidence scripts.
- Playwright CLI: deterministic screenshots, snapshots, traces, and visual
  evidence.
- Chrome DevTools MCP: console, network, performance, memory, Lighthouse, and
  live Chrome debugging. MiMoCode invokes the exact managed
  `~/.local/bin/chrome-devtools-mcp` wrapper; endpoint ownership and the
  CloakBrowser health gate belong to bootstrap, with no stock-browser fallback.

MiMoCode built-in or future browser features are disabled as release providers
until a separate provider model, policy, and validator are added.
