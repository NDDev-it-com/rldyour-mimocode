<!-- Memory Metadata
Last updated: 2026-05-22
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: security posture and blocking/warning policy
Area: SECURITY
-->

# SECURITY-01-POSTURE

## Scope
security posture and blocking/warning policy

## Current source of truth
- `path:README.md`

## Last verified
- date: 2026-05-22
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex ry-start memory taxonomy sync

## Facts
- MiMoCode runtime permissions are UX controls, not a sandbox or security
  isolation boundary.
- The adapter repository is AGPL-3.0-or-later and does not vendor upstream
  Xiaomi MiMoCode source, binary assets, logos, or trademarked branding.
- Upstream MiMoCode is referenced as a separate runtime under upstream license
  and use restrictions.
- Secrets, OAuth state, API tokens, runtime databases, checkpoints, notes, and
  task progress artifacts must not be committed.

## Evidence
- `commit:c219a9beb8743a44add8d961733b2fac2d6a69ea`
- `path:README.md`

## Known pitfalls
- Treat this memory as derived context. Current code, configuration, runtime output, and GitHub state override stale memory text.

## Update policy
Update after verified changes to the referenced source-of-truth files.

## Delete / merge policy
- Delete or merge only when the referenced source-of-truth files no longer support this memory and the replacement memory preserves the durable facts.
