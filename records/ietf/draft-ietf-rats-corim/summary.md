---
schema: "library-summary/v1"
id: draft-ietf-rats-corim
record: draft-ietf-rats-corim
type: summary
updated: "2026-11-01"
---

# Concise Reference Integrity Manifest

|  |  |
|---|---|
| **Type** | draft (IETF, RATS WG, intended Standards Track) |
| **Maturity** | `draft`: active working-group Internet-Draft, not an RFC |
| **Authors** | H. Birkholz, T. Fossati, Y. Deshpande, N. Smith, W. Pan |
| **Published** | 2026-11-01 (revision -12) |
| **Identifier** | draft-ietf-rats-corim-12 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-rats-corim-12.txt |
| **Digest** | `sha256:f4e33b7e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CoRIM carries what a Verifier compares Evidence against. Endorsers and Reference Value Providers issue signed CBOR manifests describing expected Attester state, in the RATS terms of `rfc-9334` (§1). A CoRIM is a tagged map, signed by COSE_Sign1 or COSE_Sign (§4.1, §4.2), wrapping CoMID modules and CoTL lists (§5, §6). §8 goes further than a format and gives a reference Verifier with logical appraisal phases. The point of the design is that several supply-chain actors each supply part of the picture (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Without Reference Values a measurement is an unappraisable number. This supplies them |
| Cryptography | `adjacent` | Signs with COSE. No new primitives |
| This project | `adjacent` | Signed, digest-bearing supply-chain statements in CBOR, near our ArtifactStatement |

- **R-M-07**: reference measurements are digests of artifacts asserted by a supply-chain actor, the same shape as an artifact statement.
- **R-O-03 and DEC-002**: §4.1 says a CoRIM profile should state whether CBOR deterministic encoding is required, so the question is delegated, not answered.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| Veraison | open source, named in §9.1 | Apache-2.0 | https://github.com/veraison/veraison |

The veraison/veraison repository is archived on GitHub; §9.1 still names the project. Current code location not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not stable.** Revision -12 appeared the day it was fetched, and grew from 147 to 163 pages since -11.
- **It moves trust; it does not create it.** §10 calls the Verifier effectively part of the Attesters' and Relying Parties' trusted computing base.
- **Encoding is deferred to profiles** (§4.1).
- **Read scope.** §1, §4.1 in part, §4.2 in part, §8.2's opening, §9.1 and the opening of §10 were read. §5, §6, §7, §8.3 and the CDDL were not read. At 163 pages it is the largest IETF text in this batch. No keyword count is given.
