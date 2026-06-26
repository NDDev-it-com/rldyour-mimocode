<!-- Memory Metadata
Last updated: 2026-06-26
Last verified: 2026-06-26
Last commit: c219a9beb8743a44add8d961733b2fac2d6a69ea chore(release): prepare mimocode 1.7.7 (no-fullrepo)
Scope: MiMoCode release validation
Area: RELEASE-->

# RELEASE-01-VALIDATION

## Scope
MiMoCode release validation.

## Current source of truth
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:SECURITY.md`
- `path:.github/branch-protection/main.json`
- `path:.github/workflows/validate.yml`
- `path:.github/workflows/secret-scan.yml`
- `path:scripts/validate_fast.sh`
- `path:scripts/doctor_system_mimocode.sh`

## Last verified
- date: 2026-06-26
- commit: `c219a9beb8743a44add8d961733b2fac2d6a69ea`
- checked by: Codex rldyour-flow sync

## Facts
- Current adapter release is `1.7.7`.
- Initial adapter release was `1.0.0`.
- Runtime baseline is MiMoCode `0.1.3`.
- Public CI must use GitHub-hosted runners and SHA-pinned actions.
- Required status checks must be emitted on `pull_request` and
  protected-branch `push`.
- Runtime doctor reports `NOT_PROVEN` when `mimo` is unavailable.

## Evidence
- `path:VERSION`
- `path:CHANGELOG.md`
- `path:SECURITY.md`
- `path:.github/branch-protection/main.json`
- `path:.github/workflows/validate.yml`
- `path:.github/workflows/secret-scan.yml`
- `path:scripts/validate_fast.sh`
- `path:scripts/doctor_system_mimocode.sh`

## Known pitfalls
- A `VERSION` file is not enough for release certification. GitHub Release,
  local validators, pytest, and clean artifact hygiene are all required.

## Update policy
Update after release version changes, CI policy changes, branch protection
changes, release workflow changes, or runtime doctor contract changes.

## Delete / merge policy
- Delete or merge only when MiMoCode release validation is replaced by another
  durable memory and the replacement preserves current release facts.

## Applies to
- `VERSION`
- `CHANGELOG.md`
- `SECURITY.md`
- `.github/`
- `scripts/validate_fast.sh`
- `scripts/doctor_system_mimocode.sh`

## Source of truth
- The `Current source of truth` section above, plus current code,
  configuration, tests, git state, and live GitHub release state.

## Invariants
- Do not certify a MiMoCode release without local validators, pytest, GitHub
  Release evidence, and clean artifact hygiene.
- Code, configuration, tests, validators, git state, and live GitHub state
  override this memory when they disagree.

## Current State
- See `Facts` for current durable facts.

## Do Not Infer
- Do not infer CI success from UI impressions or branch names. Use machine
  evidence where available and mark unavailable evidence as `NOT_PROVEN`.

## Update Triggers
- Update after release version changes, CI/governance changes, release evidence
  changes, or runtime doctor behavior changes.

## Validation Commands
- `python3 scripts/validate_fast.sh`
- `python3 -m pytest -q`
- `python3 scripts/doctor_system_mimocode.sh --redact`

## Repair Procedure
- Re-read release surfaces and CI policy, update only verified current facts,
  then rerun the validation commands.
