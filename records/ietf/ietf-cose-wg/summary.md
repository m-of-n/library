---
schema: "library-summary/v1"
id: ietf-cose-wg
record: ietf-cose-wg
type: summary
updated: "2026-11-01"
---

# IETF CBOR Object Signing and Encryption (COSE) Working Group

|  |  |
|---|---|
| **Type** | consortium (IETF working group, Security Area) |
| **Maturity** | unset: a charter has no RFC 2026 standing |
| **Authors** | IETF working group charter. Chairs Ivaylo Petrov, Michael B. Jones. AD Christopher Inacio, as listed 2026-11-01 |
| **Published** | charter-ietf-cose-05, datatracker last updated 2026-03-18 |
| **Identifier** | charter-ietf-cose-05 |
| **Source** | https://www.ietf.org/charter/charter-ietf-cose-05.txt |
| **Digest** | `sha256:890efc09…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | not applicable |

## Overview

The COSE charter narrows the group to four kinds of Standards Track document: algorithm use, additional attributes, header parameters, and key representations, plus a CBOR encoding of the RFC 5280 certificate profile that is required to be invertible. The two exclusions matter more to us than the list. *"Key management and binding of keys to identities are out of scope"*, and *"The COSE WG will not innovate in terms of cryptography"*: algorithms must come from RFCs, active IRTF CFRG or IETF WG documents, or positive CFRG review.

So COSE is an envelope and registry maintainer. It does not compete with anything m-of-n says about who a key is. The documents page shows the live output: RFC 9942 (receipts), RFC 9995 (hash envelope) and RFC 9921 (timestamps) have all shipped against their milestones, and post-quantum algorithm work is in progress.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Owns the signed envelope most of the ecosystem uses |
| Cryptography | `core` | Algorithm admission is a chartered policy |
| This project | `adjacent` | An export envelope candidate, excluded from the native model |

- **DEC-005** (open, `ADR-0004` leaves it open): COSE_Sign1 is one of the two candidates, and this group is who would change it underneath us. Every milestone date on the page has passed, some with the documents still in progress, so a timeline should not be inferred from them.
- **R-I-03**: export to COSE_Sign1 plus CWT claims. The charter's header parameter and algorithm tracks are where the registry values such an export would carry come from. The native model excludes those registries (`ADR-0004` item 3).
- **The scope exclusion** cuts in our favour and bears on no decision on its own: identity binding is the part of the problem COSE declines.

## Implementations

**Not applicable, 2026-11-01.** A working group is not software. Implementations belong to `rfc-9052` and the algorithm records.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A working group charter is not an `rfc`, `draft`, `spec` or `ietf` type record, so FX-1 does not reach it. No `maturity` is set: a charter has no RFC 2026 standing and no value in the schema's enum fits it. The digest is of the charter text, because the about page cannot hold one.

## Limits

- **It does not specify anything.** The format is in `rfc-9052` and `rfc-9053`, the algorithms in their own records.
- **The charter names no IANA policy**, though the group's work fills IANA registries. Registry policy is in the RFCs.
- **Membership is not exact.** The documents page lists 16 RFCs. Records marked `part_of` this group do not all appear there: `rfc-8230` was a non-WG document, `rfc-8392` and `rfc-8747` came from ACE, and `rfc-9021` was an Independent Stream submission. All four are reported in the PR, not changed.
- **Read scope.** The whole charter text. The about page and the documents page, as text. The history page was checked only for milestone events. Mailing list, wiki and issue tracker not read.
