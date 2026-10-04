---
schema: "library-summary/v1"
id: secure-systems-lab-dsse
record: secure-systems-lab-dsse
type: summary
updated: "2026-10-03"
---

# Dead Simple Signing Envelope (DSSE)

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | unofficial — a Secure Systems Lab specification, protocol v1.0.2 (10 May 2024); no standards-body status |
| **Authors** | Secure Systems Lab (secure-systems-lab/dsse) |
| **Published** | protocol.md v1.0.2, 2024-05-10 |
| **Identifier** | git: https://github.com/secure-systems-lab/dsse |
| **Source** | pinned at commit `1d3370f62565bca041e97c8310b873ac340edc2e` |
| **Digest** | per-file; `background.md` and `protocol.md` read at that commit, 2026-10-03 |

## Overview

DSSE is a minimal signature envelope whose central design claim is that
**canonicalisation should be avoided rather than perfected**. Instead of
normalising a payload before signing, it signs the received byte sequence
verbatim, binding an authenticated type string alongside it through a
Pre-Authentication Encoding:

```
SIGNATURE = Sign(PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY))
PAE(type, body) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body
```

where `LEN` is ASCII decimal with no leading zeros and `SP` is `0x20`. The
length prefixes make the serialisation of the (type, body) pair unambiguous
without escaping, and `PAYLOAD_TYPE` — a media type or URI identifying *both*
encoding and schema — is inside the signed bytes, which is what defeats
cross-encoding confusion. The idea and the name are taken from PASETO; the
authors replaced PASETO's binary PAE with an ASCII one, fixed the input count,
and added the `"DSSEv1"` version string.

It was built for TUF and in-toto, which previously signed Canonical JSON.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Its critique of canonicalisation is the argument R-O-05 has to survive, and its verify-then-parse ordering is the discipline R-O-05 adopts. |
| Cryptography | adjacent | Deliberately algorithm-agnostic — `Sign()` is "an arbitrary digital signature format" agreed out of band. |
| This project | core | Named in **DEC-005** (envelope for ArtifactStatement), **R-I-03** (export target), and **DEC-002 option 3** pairs it with JCS. Its `(t, n)` envelope bears on **R-M-06**. |

Bears on **DEC-002**, **DEC-005**, **R-I-03**, **R-M-06** and **R-O-05**.

## The critique, in its own terms

`background.md` lists one practical and two theoretical problems with the
Canonical JSON scheme TUF and in-toto used:

1. **Practical** — it requires the payload to be JSON or convertible to JSON,
   whereas a generic signature layer should handle arbitrary payloads.
2. **Theoretical 1** — *"Two semantically different payloads could have the same
   canonical encoding."* This is a non-injectivity claim, and it is the same
   property a canonical form must have to be safe to sign. They note no known
   attack on Canonical JSON but cite past breaks of other canonicalisation
   schemes, concluding *"It is safer to avoid canonicalization altogether."*
3. **Theoretical 2** — it *"requires the verifier to parse the payload before
   verifying, which is both error-prone—too easy to forget to verify—and an
   unnecessarily increased attack surface."*

Separately, the old scheme carried no authenticated context indicator, so a
signer could obtain a CBOR message meaning X and have a verifier read it as a
protobuf message meaning Y.

**Worth noting precisely:** in DSSE's own design-requirements list these are
**SHOULD**, not MUST — *"SHOULD avoid depending on canonicalization for
security"* and *"SHOULD NOT require the verifier to parse the payload before
verifying."* DSSE recommends against canonicalisation; it does not forbid it.
That matters for R-O-05, which keeps a canonical form while honouring the
ordering, and is therefore consistent with DSSE's requirements as written rather
than in tension with them.

## Two rules worth importing

- **Verified bytes are the bytes the application sees.** *"Implementations MUST
  ensure that the same SERIALIZED_BODY that is verified is the same sent to the
  application layer. In particular, implementations MUST NOT re-parse the
  envelope after verification to pull out the payload."* R-O-05 as proposed does
  not say this, and it closes a real gap between "verify before decoding" and
  what the application finally acts on.
- **`(t, n)` multi-signature is already in the envelope.** *"A `(t, n)`-ENVELOPE
  is valid if the enclosed signatures pass the verification against at least `t`
  of `n` unique trusted public keys."* The export target named in R-I-03
  therefore already carries threshold semantics, which bears directly on R-M-06
  and is a cheaper interchange story for threshold subjects than expected.

## Limits

- **`KEYID` is unauthenticated and `MUST NOT` be used for security decisions** —
  it is only a hint to narrow key selection. This is the opposite of our
  `KeyId`, which under R-M-02 *is* the principal's name. The collision of terms
  is a documentation hazard for any mapping table written under R-I-01.
- **`PAYLOAD_TYPE` is a globally allocated string** — a media type or a URI.
  Under R-M-12 (accepted as ARCH-0002 P1 via ADR-0001) that is exactly the
  centrally allocated extension point the native model excludes, so DSSE's type
  indicator is usable at the interchange boundary and not natively.
- **No canonical form at all**, which is the point — but it means DSSE cannot
  express R-M-11's description-mode `ArtifactId` or ARCH-0002 P4's domain hash,
  both of which require canonicalising a structure to derive its identity.
- **Signature algorithm and key management are out of scope**, agreed out of
  band, so DSSE settles none of DEC-003.
- **Read scope:** `background.md` and `protocol.md` in full at the pinned
  commit. `envelope.md`, `hypothetical_signature_attack.ipynb` and the
  implementation sub-trees have **not** been read; the notebook is the authors'
  worked cross-encoding attack and is the first thing to read next.
- This record is type `repo`, so FX-1 full extraction does not apply to it. If
  DSSE becomes a selected envelope under DEC-005 rather than an export target,
  that exemption should be revisited.
