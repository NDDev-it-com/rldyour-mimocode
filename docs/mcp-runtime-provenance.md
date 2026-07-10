# MCP Runtime Provenance

This release pins MiMoCode's local documentation and reasoning MCP servers to
immutable npm package versions while retaining `bunx` as the native local
stdio runner.

## Current Pins

| Server | Exact package | npm SHA-512 integrity | Upstream tag target |
| --- | --- | --- | --- |
| Sequential Thinking | `@modelcontextprotocol/server-sequential-thinking@2026.7.4` | `sha512-tmR/ieGaeweffLNBrDp1H1w4sn4M6TN5yWSbMS+YMfS+0GDyPjnNKzqCl2uqfdRiX3D44PJUhwiDGqtJp6tFhw==` | `2026.7.4` -> `6dd0a683e198783e30feabf7abaf42f925bd18b1` |
| Context7 | `@upstash/context7-mcp@3.2.3` | `sha512-9L/9ufypc6lvlmiGxMLw/O94c8UcTCIvBI+o1R+FHVTgRw2lzg9FPGwcrKWuIOsAXH0+6pWFWm4dJWHbCm92sw==` | `@upstash/context7-mcp@3.2.3` -> `98baa58d3625e2529e000f1c9f658fff25081bbb` |

The npm registry reported both versions as the stable `latest` dist-tag on
2026-07-10. The package binaries are `mcp-server-sequential-thinking` and
`context7-mcp`; `bunx` resolves those binaries from the exact package specs.

## Transport Compatibility

Each exact package was launched with the same command shape committed in
`.mimocode/mimocode.jsonc`. A credential-free MCP stdio probe completed this
sequence using protocol version `2025-11-25`:

1. `initialize`
2. `notifications/initialized`
3. `tools/list`

Sequential Thinking returned `sequentialthinking`. Context7 returned
`resolve-library-id` and `query-docs`. The probe removed `CONTEXT7_API_KEY`
from its environment and enabled `DISABLE_THOUGHT_LOGGING=true`; no credential
or thought content was captured.

## Supply-Chain Checks

- npm registry SHA-512 integrity and SHA-1 shasum values are recorded in
  `config/mcp-inventory.json` and validated structurally by
  `scripts/validate_mimocode_mcp_inventory.py`.
- The upstream annotated tags resolve to the commit targets shown above.
  GitHub reports both upstream tag objects as unsigned, so their target SHAs
  are evidence of source correspondence, not a cryptographic publisher
  identity guarantee.
- A temporary package-lock-only install with scripts disabled followed by
  `npm audit --omit=dev` reported zero info, low, moderate, high, or critical
  vulnerabilities across the production dependency graph.
- The release SPDX SBOM includes both exact MCP packages as adapter
  dependencies. Context7 declares MIT. Sequential Thinking's package metadata
  says `SEE LICENSE IN LICENSE`, while the published tarball omits that file;
  its upstream repository documents an Apache-2.0/MIT transition, so the SBOM
  conservatively uses `NOASSERTION` for the package's declared license.

Primary sources:

- `https://registry.npmjs.org/@modelcontextprotocol/server-sequential-thinking/2026.7.4`
- `https://github.com/modelcontextprotocol/servers/tree/2026.7.4/src/sequentialthinking`
- `https://registry.npmjs.org/@upstash/context7-mcp/3.2.3`
- `https://github.com/upstash/context7/tree/%40upstash/context7-mcp%403.2.3/packages/mcp`

## Update Policy

Change these pins only after checking current stable registry versions,
upstream tag provenance, local stdio initialization, tool discovery, production
dependency audit results, release SBOM output, and stale-pin regression tests.
