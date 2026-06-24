# rldyour-mimocode Runtime Memory Projection

Last commit: b2418f5d2661d677e12f4f1935fcfab039f3da7c

This file is the MiMoCode-native project memory projection for the
`rldyour-mimocode` adapter.

Current facts:

1. Adapter id: `mimocode`.
2. Adapter version: `1.6.0`.
3. Runtime baseline: MiMoCode `0.1.0`.
4. Runtime binary: `mimo`.
5. Upstream source: `https://github.com/XiaomiMiMo/MiMo-Code`.
6. Primary install channel: official Xiaomi MiMo installer / GitHub release
   assets pinned to `v0.1.0`.
7. This repository is AGPL-3.0-or-later and does not vendor upstream MiMoCode
   source, binaries, logos, QR codes, or trademarks.
8. MiMoCode compose, subagents, `/goal`, `/dream`, `/distill`, and background
   execution are native MiMoCode session features, not rldyour cmux
   orchestrator mode.
9. Serena memories are the cross-tool source of truth. MiMoCode runtime memory
   is a generated projection from verified facts.

Runtime-only files such as `checkpoint.md`, `notes.md`, SQLite databases, and
`tasks/<id>/progress.md` must remain ignored unless explicitly curated through a
source-backed review.
