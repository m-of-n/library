---
schema: "library-summary/v1"
id: iso-iec-19790
record: iso-iec-19790
type: summary
updated: "2026-11-05"
---

# ISO/IEC 19790:2012, Security requirements for cryptographic modules

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | historic: the ISO catalogue shows the 2012 edition Withdrawn, stage 95.99 (2025-02-26), revised by ISO/IEC 19790:2025 (capture of 2026-10-17) |
| **Committee** | ISO/IEC JTC 1/SC 27 (catalogue) |
| **Published** | 2012-08, Edition 2, 72 pages; corrected version 2015-11 (catalogue) |
| **Identifier** | ISO/IEC 19790:2012 |
| **Source** | https://www.iso.org/standard/52906.html (2025 edition: https://www.iso.org/standard/82423.html) |
| **Digest** | none. **Not fetched** (2026-11-05): ISO's free channel served no file to our client, and ISO's licence forbids AI processing (see Overview) |

## Overview

**This record has not been read, and it must not be read by an AI agent.** On 2026-11-05 the user accepted ISO's free-download licence on their behalf for the 2025 edition. That licence forbids AI processing. The CHF 0 download goes through the ISO End Customer Licence Agreement, and its clause 7(b) says the Licensee *"is not permitted to access, use, or process the ISO Publication for or related to any machine learning, artificial intelligence (AI), or analogous computational purposes"* without a separate licence (iso.org licence page, section B, clause 7(b), Internet Archive capture 20261023130946). It also names *"summarize"* among the barred uses. No bytes were obtained either: the Publicly Available Standards site says it is closed and returns only its licence page, also after "I accept", and the ISO webstore returned 403 to our client.

Only bibliographic facts are kept, from ISO catalogue pages seen through Internet Archive captures: the 2012 edition is Edition 2, 2012-08, corrected 2015-11, 72 pages, ISO/IEC JTC 1/SC 27, Withdrawn (stage 95.99, 2025-02-26), revised by ISO/IEC 19790:2025, Edition 3, 2025-02, 80 pages, Published, price CHF 0 (captures 20261017090619 and 20261017010159). The record is held because `fips-140-3` cites it; read that record for content. The abstract text from the catalogue page was removed on 2026-11-05: the iso.org footer says no ISO content may be used for machine learning or AI.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | From the title only: security requirements for cryptographic modules. Text unread |
| Cryptography | `core` | Same basis; `fips-140-3` carries the detail |
| This project | `adjacent` | Relevant only if mofn ever claims a validated module; no requirement says so |

**Bears on none yet.** ARCH-0001 §5 has no module-validation requirement, and NG3 lists freezing the algorithms as a non-goal. Earlier `bears_on: DEC-009` came from Threat-Radar's numbering and was removed (see `content.note`). **Restored 2026-11-09 as `tmodel:DEC-009` (library#133).** The removal misread a register collision as a stale id: these are tmodel's live ids (Threat-Radar `project/DECISIONS-0001.md` and `spec/ARCH-0001-threat-model-architecture.md`), where DEC-009 is generic-threat-to-product mapping and the mitigation lifecycle. They still bear on no mofn decision.

## Implementations

Not searched for this record: validated modules are tested against FIPS 140-3 through CMVP, so they are found from `fips-140-3`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | bibliographic facts; `content.note` quotes the licence clause and its locator |
| `summary.md` | this document |

**No authored relations.** The `see_also` edges from `iso-iec-24759`, `fips-140-3`, `nist-sp-800-140` and `nist-sp-800-140a` to `-140f` are authored on those records.

**No digest and no `distilled/`.** No bytes were obtained, and the licence bars an AI reading or extraction. A 2025 edition record would be a new record linked by `supersedes`; as a `spec` it would owe FX-1, which an agent cannot do under this licence.

## Limits

- **Unread, by licence.** Clause 7(b) of ISO's licence bars AI access and summarising. Nothing here describes the content of either edition.
- **Catalogue prose cut.** The iso.org footer forbids ML use of ISO content, so only bibliographic facts from the catalogue are kept.
- **Id and title stay on 2012.** `fips-140-3` refers to this record, and ids are stable. The current edition is 2025, which this record does not describe.
