# rldyour-mimocode Runtime Memory Projection

Last commit: fc49d21e6a65f86b93c4a1baea6fc8e0c982409f feat(browser): enforce managed CloakBrowser skill boundary (other)

This file is the MiMoCode-native project memory projection for the
`rldyour-mimocode` adapter.

Current facts:

1. Adapter id: `mimocode`.
2. Adapter version: `1.7.31`.
3. Runtime baseline: MiMoCode `0.1.5`.
4. Runtime binary: `mimo`.
5. Upstream source: `https://github.com/XiaomiMiMo/MiMo-Code`.
6. Primary install channel: the parent bootstrap's frozen Bun lock, cross-checked
   against the official Xiaomi MiMo `v0.1.5` release.
7. This repository is AGPL-3.0-or-later and does not vendor upstream MiMoCode
   source, binaries, logos, QR codes, or trademarks.
8. MiMoCode compose, subagents, `/goal`, `/dream`, `/distill`, and background
   execution are native MiMoCode session features, not rldyour cmux
   orchestrator mode.
9. Serena memories are the cross-tool source of truth. MiMoCode runtime memory
   is a generated projection from verified facts.
10. Sequential Thinking is pinned to `2026.7.4`, Context7 is pinned to `3.2.3`,
    and both local MCP packages are validated as stdio transports.
11. Browser execution requires exact managed CloakBrowser health before every
    action and is limited to managed Playwright CLI and Chrome DevTools MCP;
    `webwright-task` is compatibility intent only and Webwright runtime is
    forbidden.

Runtime-only files such as `checkpoint.md`, `notes.md`, SQLite databases, and
`tasks/<id>/progress.md` must remain ignored unless explicitly curated through a
source-backed review.
