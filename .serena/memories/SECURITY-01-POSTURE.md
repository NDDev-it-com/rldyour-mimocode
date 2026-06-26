<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MiMoCode security posture
Area: SECURITY-->

# SECURITY-01-POSTURE

## Scope
MiMoCode security posture.

## Current source of truth
- `path:SECURITY.md`
- `path:THIRD_PARTY_NOTICES.md`
- `path:config/rldyour-contract.json`
- `path:.mimocode/mimocode.jsonc`
- `path:scripts/doctor_system_mimocode.sh`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex rldyour-flow sync

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
- `path:SECURITY.md`
- `path:THIRD_PARTY_NOTICES.md`
- `path:config/rldyour-contract.json`
- `path:.gitignore`
- `path:scripts/doctor_system_mimocode.sh`

## Known pitfalls
- Full-auto runtime posture is owner-approved workstation behavior, not a
  security boundary.

## Update policy
Update after permission model, secret-handling, license/notice, upstream
restriction, or doctor redaction changes.

## Delete / merge policy
- Delete or merge only when security posture tracking moves to another durable
  memory and the replacement preserves current facts.

## Applies to
- `SECURITY.md`
- `THIRD_PARTY_NOTICES.md`
- `.mimocode/mimocode.jsonc`
- `.gitignore`

## Source of truth
- The `Current source of truth` section above, plus current security validators
  and live upstream security documents where explicitly refreshed.

## Invariants
- Do not treat MiMoCode permissions as sandboxing.
- Do not commit secrets or runtime state.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer legal permission to use upstream assets from runtime install
  availability.

## Update Triggers
- Update after security posture, permission, secret-scan, license, notice,
  upstream restriction, or doctor redaction changes.

## Validation Commands
- `python3 scripts/validate_mimocode_config.py --strict`
- `python3 scripts/validate_fast.sh`

## Repair Procedure
- Re-read security and notice files, update only verified facts, then rerun the
  validation commands.
