<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: e239f9df6caa67bb408f763b478ea1f2ce49e9f3 chore(release): mimocode 1.7.16 (other)
Scope: release readiness, versioning, and artifact hygiene
Area: RELEASE
-->

# RELEASE-01-VALIDATION

## Scope
release readiness, versioning, and artifact hygiene

## Current source of truth
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`

## Last verified
- date: 2026-05-22
- commit: `e239f9df6caa67bb408f763b478ea1f2ce49e9f3`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- Current adapter release is `1.7.17`.
- Initial adapter release was `1.0.0`.
- Runtime baseline is MiMoCode `0.1.4`.
- Public CI must use GitHub-hosted runners and SHA-pinned actions.
- Required status checks must be emitted on `pull_request` and
  protected-branch `push`.
- Runtime doctor reports `NOT_PROVEN` when `mimo` is unavailable.

## Evidence
- `commit:e239f9df6caa67bb408f763b478ea1f2ce49e9f3`
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:.github/workflows/release.yml`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
