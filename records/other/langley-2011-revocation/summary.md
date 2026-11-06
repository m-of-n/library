---
schema: "library-summary/v1"
id: langley-2011-revocation
record: langley-2011-revocation
type: summary
updated: "2026-11-04"
---

# Revocation doesn't work

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: personal blog by a Chrome engineer, no standing to verify |
| **Authors** | Adam Langley |
| **Published** | 2011-03-18 |
| **Identifier** | ImperialViolet, 2011-03-18 |
| **Source** | https://www.imperialviolet.org/2011/03/18/revocation.html |
| **Digest** | `sha256:369f7b9d…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

Langley ran a proxy that returned errors for every revocation check, then tried browsers. IE 8, Firefox 3.6 (beyond dropping the EV indication, per an update) and Safari showed nothing wrong, and Chrome's indication was the mixed-content one, easy to ignore, though for HSTS sites it treated revocation failure as fatal, a behaviour the post's own update says Langley later changed. An attacker close to the user can therefore defeat revocation, and browsers cannot simply be strict because a CA outage would take down large parts of the web. His alternative: certificates valid for a few days, so "If you want to “revoke” a certificate, just stop renewing it".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | shows the attack on soft-fail |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | an early statement of R-O-02's reasoning |

- **R-O-02**: the post argues for short validity in place of revocation checking, which is the preference R-O-02 states.

## Relations

None authored. `langley-2014-revchecking` carries the edge between the two posts.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole text; the screenshots were not read.

- An informal test of browser versions from 2011. `liu-2015-revocation` is the systematic version.
- The attacker model is scoped to one close to the user; for one close to the site, the post notes revocation can still work.
- It considers the renewal channel's availability (a CA down for hours does not matter, down for days does) but not its integrity.
