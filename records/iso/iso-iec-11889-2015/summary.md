---
schema: "library-summary/v1"
id: iso-iec-11889-2015
record: iso-iec-11889-2015
type: summary
updated: "2026-11-03"
---

# ISO/IEC 11889:2015 Trusted Platform Module Library

|  |  |
|---|---|
| **Type** | spec (four-part International Standard) |
| **Maturity** | standard: ISO catalogue shows Part 1 as Published (capture of 2026-10-20) |
| **Authors** | ISO/IEC JTC 1 (catalogue, Part 1) |
| **Published** | 2015-08, Edition 2; English corrected version 2016-03 (catalogue, Part 1) |
| **Identifier** | ISO/IEC 11889-1:2015 to 11889-4:2015 |
| **Source** | https://www.iso.org/standard/66510.html (Part 1 catalogue page) |
| **Digest** | none. **Not fetched**: listed at CHF 0, but the download goes through ISO's licence (see Limits), and www.iso.org returned 403 to our client |

## Overview

**This record has not been read.** No part of the standard was obtained, and the normative text was not read. It is not paywalled: the catalogue lists Part 1 at CHF 0, so the record is `status: queued`, not `stub`, as for `iso-iec-19790`. Everything below comes from the ISO catalogue page for Part 1, seen through an Internet Archive capture dated 2026-10-20, or from the TCG library page, and is labelled as such.

Per that catalogue abstract, Part 1 *"defines the architectural elements of the Trusted Platform Module (TPM), a device which enables trust in computing platforms in general"*. The abstract limits the standard's scope to TPM requirements, puts cryptographic analysis and algorithm-applicability guidance out of scope, and says that defining a specific strength of function or assurance level is out of scope too. The TCG library page (fetched 2026-11-05), not the ISO catalogue, says JTC 1 approved the TCG TPM Library Specification 2.0 as ISO/IEC 11889:2015, Parts 1-4; which TCG revision it matches was not established.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Hardware root of trust for platform attestation, per the catalogue abstract |
| Cryptography | `adjacent` | The abstract says it defines how a TPM implements cryptographic techniques, without analysing them |
| This project | `adjacent` | Device evidence is a possible input to attestation; ARCH-0001 has no hardware-evidence requirement |

**Bears on none yet.** ARCH-0001 §5 has no requirement for hardware or device evidence (the `device-attestation` topic says the same). Nothing in the abstract supports a `DEC-*` or `R-*` link.

## Implementations

Not searched for this record: implementations target the TCG text, not the ISO edition. See `tcg-tpm-2-0-library-185`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with what was and was not seen in `content.note` |
| `summary.md` | this document |

**Relations.** `see_also: tcg-tpm-2-0-library-184`, a readable TCG TPM 2.0 Library text: the TCG line this standard transposes, though which revision the 2015 edition matches is not established. `see_also: tcg-tpm-1-2-main`, because TCG's page (as recorded in that record's `content.note`, checked 2026-11-04) says TPM 1.2 was published as ISO/IEC 11889:2009, the edition before this one; it is not `supersedes`, since that record is the TCG text, not the ISO 2009 edition. The edge to `tcg-tpm-2-0-library-185`, the current TCG text, is authored on that record and not repeated here.

**No digest and no `distilled/`.** No bytes were obtained. A legitimate copy would move this record past `queued`; an extraction would then be owed under FX-1 (`docs/extraction.md`), since this is a `spec`.

## Limits

- **Unread.** Only the Part 1 catalogue abstract was seen; the normative text of no part was read. Parts 2 to 4 were not looked at individually.
- **Licence not checked.** Whether the CHF 0 download carries the same AI-use clause that stopped `iso-iec-5962-2021` was not checked. Obtaining it is a human decision.
- **Revision mapping unknown.** Which TCG Library revision the 2015 edition transposes was not established, so the TCG records cannot be assumed to match it clause for clause.
- **Status may move.** The capture shows Part 1 at stage 90.92 (to be revised); a new edition would be a new record linked by `supersedes`.
