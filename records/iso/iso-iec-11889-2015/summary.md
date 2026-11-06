---
schema: "library-summary/v1"
id: iso-iec-11889-2015
record: iso-iec-11889-2015
type: summary
updated: "2026-11-05"
---

# ISO/IEC 11889:2015 Trusted Platform Module Library

|  |  |
|---|---|
| **Type** | spec (four-part International Standard) |
| **Maturity** | standard: ISO catalogue shows Part 1 as Published (capture of 2026-10-20) |
| **Committee** | ISO/IEC JTC 1 (catalogue, Part 1) |
| **Published** | 2015-08, Edition 2; English corrected version 2016-03 (catalogue, Part 1) |
| **Identifier** | ISO/IEC 11889-1:2015 to 11889-4:2015 |
| **Source** | https://www.iso.org/standard/66510.html (Part 1 catalogue page) |
| **Digest** | none. **Not fetched** (2026-11-05): ISO's free channel served no file to our client, and ISO's licence forbids AI processing (see Overview) |

## Overview

**This record has not been read, and it must not be read by an AI agent.** On 2026-11-05 the user accepted ISO's free-download licence on their behalf. That licence forbids AI processing. The CHF 0 download goes through the ISO End Customer Licence Agreement, and its clause 7(b) says the Licensee *"is not permitted to access, use, or process the ISO Publication for or related to any machine learning, artificial intelligence (AI), or analogous computational purposes"* without a separate licence (iso.org licence page, section B, clause 7(b), Internet Archive capture 20261023130946). It also names *"summarize"* among the barred uses. No bytes were obtained either: the Publicly Available Standards site says it is closed and returns only its licence page, also after "I accept", and the ISO webstore returned 403 to our client.

Only bibliographic facts are kept. They come from the Part 1 catalogue page, seen through an Internet Archive capture dated 2026-10-20: Edition 2, 2015-08, English corrected version 2016-03, 257 pages, ISO/IEC JTC 1, Published, confirmed 2021, stage 90.92 (to be revised) since 2026-05-29, to be replaced by ISO/IEC DIS 11889-1, price CHF 0. The abstract text from that page was removed on 2026-11-05: the iso.org footer says no ISO content may be used for machine learning or AI. The TCG library page, not ISO, says JTC 1 approved the TCG TPM Library Specification 2.0 as ISO/IEC 11889:2015, Parts 1-4. Read `tcg-tpm-2-0-library-184` or `-185` for the content.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | From the title and the TCG transposition only: a TPM library standard. ISO text unread |
| Cryptography | `adjacent` | Same basis; the TCG records carry the detail |
| This project | `adjacent` | Device evidence is a possible input to attestation; ARCH-0001 has no hardware-evidence requirement |

**Bears on none yet.** ARCH-0001 §5 has no requirement for hardware or device evidence (the `device-attestation` topic says the same).

## Implementations

Not searched for this record: implementations target the TCG text, not the ISO edition. See `tcg-tpm-2-0-library-185`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | bibliographic facts; `content.note` quotes the licence clause and its locator |
| `summary.md` | this document |

**Relations.** `see_also: tcg-tpm-2-0-library-184`, a readable TCG TPM 2.0 Library text: the TCG line this standard transposes, though which revision the 2015 edition matches is not established. `see_also: tcg-tpm-1-2-main`, because TCG's page (as recorded in that record's `content.note`, checked 2026-11-04) says TPM 1.2 was published as ISO/IEC 11889:2009, the edition before this one; it is not `supersedes`, since that record is the TCG text, not the ISO 2009 edition. The edge to `tcg-tpm-2-0-library-185` is authored on that record.

**No digest and no `distilled/`.** No bytes were obtained, and the licence bars an AI reading or extraction. FX-1 extraction cannot be done by an agent under this licence.

## Limits

- **Unread, by licence.** Clause 7(b) of ISO's licence bars AI access and summarising. Nothing here describes the content.
- **Catalogue prose cut.** The iso.org footer forbids ML use of ISO content, so only bibliographic facts from the catalogue are kept.
- **Parts 2-4 not checked.** Whether they are also CHF 0 was not seen; only the Part 1 catalogue page was captured.
- **Revision mapping unknown.** Which TCG Library revision the 2015 edition transposes was not established.
- **Status may move.** Part 1 is at stage 90.92 (to be revised); a new edition would be a new record linked by `supersedes`.
