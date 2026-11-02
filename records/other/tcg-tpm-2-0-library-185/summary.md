---
schema: "library-summary/v1"
id: tcg-tpm-2-0-library-185
record: tcg-tpm-2-0-library-185
type: summary
updated: "2026-11-01"
---

# TPM 2.0 Library Specification v1.85 (PQC: ML-KEM, ML-DSA)

|  |  |
|---|---|
| **Type** | spec (four-part consortium specification, with errata) |
| **Maturity** | `standard`: each part is marked TCG Published. ISO/IEC status not examined |
| **Authors** | Trusted Computing Group, no individuals named |
| **Published** | 2026-03-12 (Version 185) |
| **Identifier** | TPM 2.0 Library, Version 185, Parts 0 to 3 |
| **Source** | https://trustedcomputinggroup.org/resources/documents/tpm-library-specification |
| **Digest** | `sha256:d8b43afb…` for Part 0. Others in `content.note`. Fetched 2026-11-01 |
| **Errata** | Errata v1 for v185, 2026-03-12, read |

## Overview

Version 185 adds ML-DSA, HashML-DSA and ML-KEM to the TPM (Part 0 change list). Pure ML-DSA signs messages, not digests, and the TPM's signing model was digest-based. So v185 deprecates TPM2_Sign() and TPM2_VerifySignature(), and adds sequenced signing commands for messages of arbitrary size, and new digest commands for algorithms that can use them (Part 0 §3.1.3.5). ML-KEM arrives with TPM2_Encapsulate() and TPM2_Decapsulate(), and with a Labeled KEM. Private keys are seeds only: 32 bytes for ML-DSA, 64 for ML-KEM (Part 1 §46.2, §47.2). TCG's news item says Attestation Keys can be ML-DSA and Endorsement Keys ML-KEM, so hardware attestation itself gains a path, which answers the topic's question for this layer.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The hardware root that platform attestation rests on |
| Cryptography | `adjacent` | Profiles FIPS 203 and 204 for a device, and defines a Labeled KEM on top |
| This project | `adjacent` | A foreign attestation source, not a target. There is no import rule for TPM evidence yet |

- **R-M-02**: Part 3 §28.5 (TPM2_EvictControl) says a TPM may have room for an ML-DSA private seed but not a public-only key of at least 1312 bytes, and that for such keys there may never be enough NV space. Device-held principals therefore lean towards identification by digest, not by raw key.

Three details an attestation design should expect. Restricted ML-DSA keys cannot use TPM2_SignDigest() at all, because no ticket can be produced for mu (Part 3 §20.7). Errata 2.6 fixes how TPM2_Quote() picks a hash for keys with no scheme hash, such as pure ML-DSA. Errata 2.8 lets a TPM refuse large TPM2_NV_Certify() responses with ML-DSA, leaving digest-based certification only.

## Implementations

**Searched 2026-11-01.** Results were almost entirely from one vendor.

| Name | Kind | License | URL |
|---|---|---|---|
| wolfTPM | open source, client and firmware TPM | not checked | https://github.com/wolfSSL/wolfTPM |

wolfSSL claims v1.85 support for ML-DSA and ML-KEM, and claims other simulators do not yet expose it. Neither claim was verified. No discrete TPM product with v185 PQC was found, and that search was shallow.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. At roughly 980 pages it would be a large extraction, scoped to PQC at most. No keyword count is given because none has been reconciled.

## Limits

- **A library specification is not a shipped device.** Part 3 §28.5 leaves minimum NV to platform-specific specifications, which we did not read. Availability in shipped TPMs is not settled here.
- **Size pressure is unresolved.** See the NV note above and errata 2.8.
- **SLH-DSA, LMS and XMSS were not looked for**, and `cnsa-2-0`'s firmware-signing choices are not mapped to this specification.
- **The record's old URL was a news item.** The spec was read directly; the "Attestation Keys" and "Endorsement Keys" framing is from the news item, not confirmed clause by clause.
- **Read scope.** Part 0 change list and deprecations, Part 1 §46 and §47, Part 2's algorithm constants, Part 3's ML-DSA notes and the errata entries on ML-DSA were read, using text search over the parts. The rest of the specification was not read.
