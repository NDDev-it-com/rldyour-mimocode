# Third-Party Notices

This notice applies to `rldyour-mimocode` adapter release `1.7.31`.

## XiaomiMiMo/MiMo-Code

MiMoCode is developed upstream at `https://github.com/XiaomiMiMo/MiMo-Code` and
is licensed under MIT by its upstream authors. Upstream use of MiMoCode is also
subject to the Xiaomi MiMoCode use restrictions and any service terms for
Xiaomi-hosted MiMo services.

This repository does not include upstream MiMoCode source code, binaries, logos,
QR codes, or trademarked branding.

## OpenCode-Derived Formats

MiMoCode is OpenCode-derived and uses OpenCode-like configuration semantics in
some surfaces. This adapter validates the MiMoCode-facing projection explicitly
and does not treat OpenCode compatibility as a substitute for MiMoCode runtime
validation.

## MCP Runtime Packages

This adapter executes, but does not vendor, these exact npm packages:

- `@modelcontextprotocol/server-sequential-thinking@2026.7.4`, from
  `modelcontextprotocol/servers` tag `2026.7.4`. Its npm metadata delegates the
  license declaration to the upstream repository license, which documents an
  Apache-2.0/MIT licensing transition; the release SBOM therefore records its
  declared license as `NOASSERTION`.
- `@upstash/context7-mcp@3.2.3`, from `upstash/context7` tag
  `@upstash/context7-mcp@3.2.3`, licensed MIT by its package metadata.

Registry digests and transport verification are recorded in
`config/mcp-inventory.json` and `docs/mcp-runtime-provenance.md`.
