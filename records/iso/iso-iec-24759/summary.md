---
schema: "library-summary/v1"
id: iso-iec-24759
record: iso-iec-24759
type: summary
updated: "2026-11-03"
---

# ISO/IEC 24759:2017, Test requirements for cryptographic modules

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | historic: the ISO catalogue shows the 2017 edition Withdrawn, stage 95.99, with ISO/IEC 24759:2025 as the new version |
| **Authors** | ISO/IEC JTC 1/SC 27 (catalogue) |
| **Published** | 2017-03, Edition 3, 135 pages (catalogue) |
| **Identifier** | ISO/IEC 24759:2017 |
| **Source** | https://www.iso.org/standard/72515.html (2025 edition: https://www.iso.org/standard/82424.html) |
| **Digest** | none. **Not fetched**: see `content.note` |

## Overview

**This record has not been read.** Neither the 2017 nor the 2025 edition was obtained, so per `docs/scope.md` §1 the record stays unread (`status: queued`, because the 2025 edition is listed at CHF 0 and a person could obtain it). Everything below comes from the ISO catalogue page for the 2017 edition, seen through Internet Archive captures, and is labelled as such.

Per that catalogue abstract, the 2017 edition *"specifies the methods to be used by testing laboratories to test whether the cryptographic module conforms to the requirements specified in ISO/IEC 19790:2012"*. It also specifies what information vendors provide to laboratories as evidence of conformity, and vendors can use it to check a module before applying for testing. It is the test-method companion of `iso-iec-19790`, and FIPS 140-3 adopts it as its test requirements (`fips-140-3`, which cites it).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Conformance-test methods, not security requirements, per the abstract |
| Cryptography | `adjacent` | Same: testing of modules, not algorithms |
| This project | `none` | mofn tests no cryptographic module for validation; no requirement says it will |

**Bears on none.** ARCH-0001 §5 has no module-validation requirement. Earlier `bears_on: DEC-009` came from Threat-Radar's numbering and was removed (see `content.note`).

## Implementations

Not searched: the users of this standard are accredited testing laboratories, not software we would build on.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with what was and was not seen in `content.note` |
| `summary.md` | this document |

**Relations.** `see_also: iso-iec-19790`, because the abstract defines this standard's test methods against ISO/IEC 19790:2012's requirements. A more precise typed relation does not fit: the abstract describes a companion, not a part or an update. The edges from `fips-140-3` and `nist-sp-800-140` are authored on those records.

**No digest and no `distilled/`.** No bytes were obtained. Obtaining the 2025 edition is a human decision (licence terms); a 2025 edition read in full would be a new record linked by `supersedes`, and as a `spec` it would owe FX-1.

## Limits

- **Unread.** Only the 2017 catalogue abstract was seen. What the 2025 edition changed is unknown.
- **Id and title stay on 2017.** `fips-140-3` refers to this record, and ids are stable. The current edition is 2025, which this record does not describe.
- **Licence not checked.** Whether the 2025 edition's CHF 0 download carries the same AI-use clause that stopped `iso-iec-5962-2021` was not checked.
