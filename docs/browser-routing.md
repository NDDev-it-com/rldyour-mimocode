# Fail-Closed Browser Routing

MiMoCode inherits the bootstrap-owned CloakBrowser trust boundary. Every
browser action starts with exact `$HOME/.local/bin/cloakbrowser-cdp-health`.
Missing or nonzero health produces `NOT_PROVEN` and stops the workflow; no
fallback is allowed.

Exactly two execution providers are active:

- `$HOME/.local/bin/playwright-cli` `0.1.17` handles flows, screenshots,
  snapshots, traces, responsive evidence, and long-horizon stepwise workflows.
  `run-code`, `--filename`, raw Playwright, alternate executables/configs, and
  package-runner invocation are forbidden.
- Chrome DevTools MCP `1.5.0` handles console, network, runtime, DOM/layout,
  performance, Lighthouse, and memory through the exact managed transport in
  `.mimocode/mimocode.jsonc`.

`webwright-task` remains a compatibility intent only. It routes through
`browser-review` to the providers above and never installs, imports, or runs
Webwright. Stock/raw/in-app Browser, MiMoCode built-in browser execution,
`browser_agent`, `node_repl`, computer-use, Playwright MCP, raw Playwright,
direct browser packages, alternate CDP endpoints, browser executables/configs,
and every fallback remain forbidden.

The authoritative machine-readable contract is
`config/browser-provider-policy.json`; its validator also enforces the exact
boundary in the MiMoCode skill, agent, and command surfaces.
