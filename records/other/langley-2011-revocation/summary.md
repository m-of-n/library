---
schema: "library-summary/v1"
id: langley-2011-revocation
record: langley-2011-revocation
type: summary
updated: "2026-11-01"
---

# Revocation doesn't work

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: personal blog by a Chrome engineer |
| **Authors** | Adam Langley |
| **Published** | 2011-03-18 |
| **Identifier** | ImperialViolet, 2011-03-18 |
| **Source** | https://www.imperialviolet.org/2011/03/18/revocation.html |
| **Digest** | `sha256:369f7b9d…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Langley ran a proxy that failed every revocation check, then tried browsers. IE 8, Firefox and Safari showed no real sign of a problem, and Chrome's indication was easy to miss. An attacker close to the user can therefore defeat revocation, and browsers cannot be strict because a CA outage would take down the web. His alternative: certificates valid for a few days, so "If you want to “revoke” a certificate, just stop renewing it".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | shows the attack on soft-fail |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | source of R-O-02's reasoning |

- **R-O-02**: this post is the design argument in its original form.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole.

- An informal test of browser versions from 2011, and screenshots were not read. `liu-2015-revocation` is the systematic version.
- The attacker model is scoped to one close to the user; for one close to the site, the post notes revocation can still work.
- The renewal channel it assumes is itself a dependency, which it passes over.
