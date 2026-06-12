# RELEASE-01-VALIDATION

## Purpose

Record release validation requirements for the current MiMoCode adapter release.

## Current Facts

- Current adapter release is `1.0.0`.
- Runtime baseline is MiMoCode `0.1.0`.
- Public CI must use GitHub-hosted runners and SHA-pinned actions.
- Required status checks must be emitted on `pull_request` and protected-branch
  `push`.
- Runtime doctor reports `NOT_PROVEN` when `mimo` is unavailable.

## Evidence

- `VERSION`
- `CHANGELOG.md`
- `SECURITY.md`
- `.github/branch-protection/main.json`
- `.github/workflows/validate.yml`
- `scripts/validate_fast.sh`
- `scripts/doctor_system_mimocode.sh`

## Operational Rules

- Do not certify release without local validators, pytest, GitHub Release
  evidence, and clean artifact hygiene.

## Last Verified

2026-06-13
