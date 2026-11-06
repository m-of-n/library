---
schema: "library-summary/v1"
id: iso-iec-19790
record: iso-iec-19790
type: summary
updated: "2026-11-03"
---

# ISO/IEC 19790:2012, Security requirements for cryptographic modules

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | historic: the ISO catalogue shows the 2012 edition Withdrawn, stage 95.99 (2025-02-26), revised by ISO/IEC 19790:2025 (capture of 2026-10-17) |
| **Authors** | ISO/IEC JTC 1/SC 27 (catalogue) |
| **Published** | 2012-08, Edition 2, 72 pages; corrected version 2015-11 (catalogue) |
| **Identifier** | ISO/IEC 19790:2012 |
| **Source** | https://www.iso.org/standard/52906.html (2025 edition: https://www.iso.org/standard/82423.html) |
| **Digest** | none. **Not fetched**: see `content.note` |

## Overview

**This record has not been read.** Neither the 2012 nor the 2025 edition was obtained, and the normative text of neither was read, so per `docs/scope.md` §1 the record stays unread (`status: queued`, because the 2025 edition is listed at CHF 0 and a person could obtain it). Everything below comes from the ISO catalogue page for the 2012 edition, seen through an Internet Archive capture dated 2026-10-17, and is labelled as such.

Per that catalogue abstract, the standard specifies security requirements for a cryptographic module used within a security system protecting sensitive information. It *"defines four security levels for cryptographic modules"* and *"specifies four security levels for each of 11 requirement areas with each security level increasing security over the preceding level"*. The abstract also states that compliance *"is not sufficient to ensure that a particular module is secure"*. The record is held because FIPS 140-3 adopts it as its security requirements (`fips-140-3`, which cites it).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Security requirements for cryptographic modules, per the abstract |
| Cryptography | `core` | Same: module requirements, not algorithms |
| This project | `adjacent` | Relevant only if mofn ever claims a validated module; no requirement says so |

**Bears on none yet.** ARCH-0001 §5 has no module-validation requirement, and NG3 lists freezing the algorithms as a non-goal. Earlier `bears_on: DEC-009` came from Threat-Radar's numbering and was removed (see `content.note`).

## Implementations

Not searched for this record: validated modules are tested against FIPS 140-3 through CMVP, so they are found from `fips-140-3`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with what was and was not seen in `content.note` |
| `summary.md` | this document |

**No authored relations and no `distilled/`.** The `see_also` edges from `iso-iec-24759`, `fips-140-3`, `nist-sp-800-140` and `nist-sp-800-140a` to `-140f` are authored on those records. No bytes were obtained. Obtaining the 2025 edition is a human decision (licence terms); a 2025 edition read in full would be a new record linked by `supersedes`, and as a `spec` it would owe FX-1.

## Limits

- **Unread.** Only the 2012 catalogue abstract was seen; the normative text of neither edition was read. The 11 requirement areas are not named in it, and nothing here says what the 2025 edition changed.
- **Id and title stay on 2012.** `fips-140-3` refers to this record, and ids are stable. The current edition is 2025, which this record does not describe.
- **Licence not checked.** Whether the 2025 edition's CHF 0 download carries the same AI-use clause that stopped `iso-iec-5962-2021` was not checked.
