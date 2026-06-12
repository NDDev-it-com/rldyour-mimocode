# Security Policy

## Supported Versions

| Version | Supported |
| --- | --- |
| Current exact tag `1.0.1` | yes |
| `1.0.x` latest released patch | yes |

## Boundary

This repository contains rldyour configuration, policy, installer, doctor, and
validation files for MiMoCode. It does not vendor Xiaomi MiMoCode source code or
binary assets.

MiMoCode itself runs locally with shell, file, MCP, provider, and session
capabilities. Its permission prompts are not a security sandbox. Treat any
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
