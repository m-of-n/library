---
schema: "library-summary/v1"
id: rfc-9529
record: rfc-9529
type: summary
updated: "2026-11-01"
---

# Traces of Ephemeral Diffie-Hellman Over COSE (EDHOC)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational`: Category Informational, confirmed in `rfc9529.json` 2026-11-01 |
| **Authors** | G. Selander, J. Preuß Mattsson, M. Serafin, M. Tiloca, M. Vučinić |
| **Published** | 2024-03 |
| **Identifier** | RFC 9529 · DOI 10.17487/RFC9529 · LAKE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc9529.txt |
| **Digest** | `sha256:e220e864…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 9529 is test material for `rfc-9528`: two complete annotated sessions (§2, signatures with X.509; §3, static DH with CCS, including a cipher suite negotiation), which §1 says were verified by two independent implementations. The positive traces matter only to someone building EDHOC.

§4 is the interesting part and was not reflected in the earlier verdict. It publishes invalid messages, each stating what is wrong and which clause it breaks: seven encoding errors (§4.1), six cryptographic errors (§4.2), and two cases of non-deterministic CBOR (§4.3). Those two are an integer in a longer form than necessary and an indefinite-length array. §4 opens by saying a compliant implementation will not compose these and *"must or may reject"* them, so the vectors state defects, not one required outcome. The hedge is the same one `rfc-9528` §9.8 makes.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4 is negative test material for a security protocol |
| Cryptography | `adjacent` | Keys and intermediate values, for a protocol we do not implement |
| This project | `adjacent` | §4.3 is prior art for rejection fixtures |

- **DEC-002** (accepted, `ADR-0004`): §4.3 is a published precedent for shipping non-canonical CBOR as negative vectors, which is what `spec/vectors/ksa-core/` does. It is thin as evidence. The set has two cases and neither is a map-order case, which is the condition `ARCH-0001` §7 singles out, and §4 says it is only a small set of examples.

**This reverses the verdict of 2026-09-22** (not-useful to marginal) for the reason above. A reviewer may reasonably prefer the old verdict: the record's value is one subsection.

## Implementations

**Searched 2026-11-01** alongside `rfc-9528`. The traces are consumed by the implementations listed in that record. No separate implementation exists for a document of examples. §1 does not name the two that verified them, in the text read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. §4 is fixture-shaped, so FX-1 would have `examples/` to fill. The bytes are not lifted here.

## Limits

- **The positive traces were not recomputed.** §2 and §3 were not re-derived, so the claim of two verifying implementations is §1's.
- **§4 is not complete.** It calls itself a small set of examples, and it does not cover map order.
- **§4 does not settle required behaviour.** That is *"must or may"*, resolved case by case against `rfc-9528` §9.8 and the documents §4 cites.
- **One check was run.** Every invalid message in §4 was counted against its stated byte length, and all 15 match. Their contents were read, not parsed.
- **The keys are public** and MUST NOT be used (§5).
- **Read scope.** §1, the opening of §2, the whole of §4, §5 and §6, from the `.txt` with page furniture stripped. §2.1 to §2.8 and §3.1 to §3.9 were not read line by line.
