---
schema: "library-summary/v1"
id: in-toto-envelope-v1
record: in-toto-envelope-v1
type: summary
updated: "2026-11-01"
---

# in-toto Attestation Framework: Envelope

|  |  |
|---|---|
| **Type** | spec (in-toto Attestation Framework v1, Envelope layer) |
| **Maturity** | unset: the file states no standing |
| **Authors** | none named |
| **Published** | 2026-03-11 (last commit to the file) |
| **Identifier** | `spec/v1/envelope.md` @ `7bfb269c` |
| **Source** | https://raw.githubusercontent.com/in-toto/attestation/7bfb269c6eb5fe8ca56edf5e1cc17776a294457a/spec/v1/envelope.md |
| **Digest** | `sha256:c02c6588…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The Envelope is the outer layer of an in-toto attestation, handling serialization and signing. It recommends DSSE v1.0, and permits any format meeting ITE-5's list: multiple signatures are a MUST, while an authenticated payload type, avoiding canonicalization and verifying before parsing are SHOULDs. It also says a format SHOULD NOT require the signing key algorithm in the signature. Under that test it calls `COSE_Sign` compliant and `COSE_Sign1` not, because `COSE_Sign1` carries one signer. The Sigstore Bundle is also non-compliant, because it requires a single signature.

**On the topic's question: the file never mentions quantum or names any algorithm.** It has no stated post-quantum path. What it has is the means for one. The multi-signature MUST allows a classical and a PQ signature side by side, and DSSE's protocol places no restriction on the signature algorithm (`protocol.md` v1.0.2, checked 2026-11-01). The cost is unaddressed here, and an algorithm hint is at most an unauthenticated KEYID.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines what is signed and what a consumer may rely on before verifying |
| Cryptography | `adjacent` | Algorithm-free by construction |
| This project | `core` | The envelope we must export to under R-I-03, and one option in DEC-005 |

- **DEC-005**: this cuts the COSE_Sign1 option. A COSE_Sign1 envelope is not an in-toto envelope by ITE-5 (*Alternative Envelope schemas*). "Both" in DEC-005 means two formats that differ in signer count, and that difference is also the dual-signature path.
- **R-I-03**: the export target. An export that must carry two signatures can do so in DSSE, but not in COSE_Sign1.
- **R-O-01**: `keyid` is a SHOULD and only a hint, weaker than our MUST.
- **R-O-05**: `payloadType` MUST be signed along with `payload`, and consumers must verify before relying on the content. This agrees with R-O-05.

## Implementations

**Searched 2026-11-01.** GitHub code search for ML-DSA in `in-toto/in-toto` and `in-toto/attestation` returned nothing. `securesystemslib` 1.5.0 has ML-DSA per `tuf-tap-21`, but whether in-toto can use it was not tested.

| Name | Kind | License | URL |
|---|---|---|---|
| DSSE | open source, spec and libraries | Apache-2.0 | https://github.com/secure-systems-lab/dsse |
| in-toto | open source, reference implementation | see repository | https://github.com/in-toto/in-toto |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **No PQ commitment.** Absence from this file is not proof that in-toto has no plan elsewhere. Only this file, `in-toto/attestation` and `in-toto/in-toto` code were searched.
- **Dual signatures have no semantics here.** The file does not say whether a verifier needs one signature or all. That is policy outside the envelope.
- **Size is not addressed.** `tuf-tap-21`'s Appendix shows ML-DSA growth for TUF metadata. Nothing comparable exists for attestations.
- **ITE-5 and DSSE were not read in full.** The ITE-5 list is taken as this file restates it. Of DSSE, only the v1.0.2 `envelope.md` and `protocol.md` lines used above were checked.
