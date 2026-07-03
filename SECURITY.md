# Security Policy

## Supported Versions

Only the current exact numeric product release tag receives security fixes. The
`1.7.x` line label tracks only the latest released patch, not every historical
patch in the line. Development snapshots and older tags are not supported unless
re-released as the current exact tag.

| Version | Supported |
| --- | --- |
| Current exact tag `1.7.16` | yes |
| Older minor / major lines | no |

## Boundary

This repository contains rldyour configuration, policy, installer, doctor, and
validation files for MiMoCode. It does not vendor Xiaomi MiMoCode source code or
binary assets.

MiMoCode itself runs locally with shell, file, MCP, provider, and session
capabilities. Its permission prompts are not a security sandbox, and configured
MCP servers run outside the trust boundary and execute as trusted code. Treat any
full-auto/yolo posture as owner-approved local automation only. Use a container
or VM when a true isolation boundary is required.

## Secrets

Do not commit:

- API keys, OAuth tokens, auth files, cookies, or provider credentials.
- `MIMOCODE_AUTH_CONTENT`, `MIMOCODE_CONFIG_CONTENT`, or logs that include them.
- MiMoCode runtime databases, checkpoints, notes, or task progress artifacts.

## Upstream Use Restrictions

Use of Xiaomi MiMoCode is subject to upstream MiMoCode use restrictions in
addition to this repository's AGPL-3.0-or-later license.

## Reporting

Report security issues through GitHub Security Advisories for this repository.
For MiMoCode runtime vulnerabilities, also follow XiaomiMiMo/MiMo-Code upstream
security reporting guidance.
