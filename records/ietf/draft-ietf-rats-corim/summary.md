---
schema: "library-summary/v1"
id: draft-ietf-rats-corim
record: draft-ietf-rats-corim
type: summary
updated: "2026-11-04"
---

# Concise Reference Integrity Manifest

|  |  |
|---|---|
| **Type** | draft (IETF, RATS WG, intended Proposed Standard) |
| **Maturity** | `draft`: active working-group Internet-Draft, not an RFC |
| **Authors** | H. Birkholz, T. Fossati, Y. Deshpande, N. Smith, W. Pan |
| **Published** | 2026-11-01 (revision -12) |
| **Identifier** | draft-ietf-rats-corim-12 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-rats-corim-12.txt |
| **Digest** | `sha256:f4e33b7e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CoRIM carries what a Verifier compares Evidence against. Endorsers and Reference Value Providers issue signed CBOR manifests describing expected Attester state, in the RATS terms of `rfc-9334` (§1). A CoRIM is a tagged map, signed by COSE_Sign1 or COSE_Sign (§4.1, §4.2), wrapping CoMID, CoSWID and CoTL tags (§4, §5, §6). §8 goes further than a format and gives a reference Verifier with four appraisal phases (§1, §8.2). The point of the design is that several supply-chain actors each supply part of the picture (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Without Reference Values a measurement is an unappraisable number. This supplies them |
| Cryptography | `adjacent` | Signs with COSE. No new primitives |
| This project | `adjacent` | Signed, digest-bearing supply-chain statements in CBOR, near our ArtifactStatement |

- **R-M-07**: reference measurements are digests of artifacts asserted by a supply-chain actor, the same shape as an artifact statement.
- **R-O-03 and DEC-002**: §4.1.4 says a CoRIM profile "should also specify whether CBOR deterministic encoding is required", so the wire question is delegated. The reference Verifier still leans on it: §8.3.4.4.1 says the processor SHOULD convert environments to CBOR core deterministic encoding before binary comparison, and §8.3.4.4.2 compares crypto keys by their deterministic encoding. Encoding is profile-defined but comparison assumes a canonical form, which is the citation R-O-03 asks for.

## Implementations

§9.1 names four Veraison repositories; each was followed and its licence read from GitHub on 2026-11-04. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| veraison/corim | Go CoRIM/CoMID library | Apache-2.0 | https://github.com/veraison/corim |
| veraison/corim-rs | Rust CoRIM library | MIT | https://github.com/veraison/corim-rs |
| veraison/cover | CoRIM processor (§8.3 appraisal) | Apache-2.0 | https://github.com/veraison/cover |
| veraison/cocli | CLI over the Go library | Apache-2.0 | https://github.com/veraison/cocli |

§9.1 gives their maturity as alpha and their compatibility as draft -06, six revisions behind this one.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists the held records among §12's references: RFC 9334, RFC 9711, STD 94 (`rfc-8949`), STD 96 (`rfc-9052`), RFC 8392, RFC 8610, RFC 5280, RFC 9090, RFC 9164, RFC 9597, RFC 9995, [DICE.cert] v1.1 (`tcg-dice-cert-profiles`) and [DICE.Layer] r0.19 (`tcg-dice-layering`). [TPM2.Part1] is revision 1.83, which the library does not hold. **No `see_also`.** `rfc-9334` and `rfc-9711` duplicated `cites`; `tcg-integrity-event-log` had no stated reason and the draft does not mention event logs.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not stable.** Revision -12 appeared the day it was fetched, and grew from 147 to 163 pages since -11.
- **It moves trust; it does not create it.** §10 calls the Verifier effectively part of the Attesters' and Relying Parties' trusted computing base.
- **Encoding is deferred to profiles** (§4.1.4).
- **Implementations lag.** The only implementations named track -06 (§9.1).
- **Read scope.** §1, §4 opening, §4.1 including §4.1.4, §4.2 in part, §8.2's opening, §8.3.4.4.1 and §8.3.4.4.2, §9.1, the opening of §10 and the §12 reference list were read. §5, §6, §7, §8.3 and the CDDL were not read. At 163 pages it is the largest IETF text in this batch. No keyword count is given.
