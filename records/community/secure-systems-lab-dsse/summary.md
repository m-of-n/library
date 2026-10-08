---
schema: "library-summary/v1"
id: secure-systems-lab-dsse
record: secure-systems-lab-dsse
type: summary
updated: "2026-10-08"
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
| **Digest** | archive sha256 `88fc65fd…3ac1`, re-verified 2026-10-08 |

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

Bears on **DEC-002**, **DEC-003**, **DEC-005**, **R-I-03**, **R-M-02**,
**R-M-06**, **R-M-12** and **R-O-05**.

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
- **An authenticated type indicator, defended by a worked attack.** `PAYLOAD_TYPE`
  is inside the signed bytes (`protocol.md` §Parameters marks it
  `Authenticated: Yes`), and `hypothetical_signature_attack.ipynb` is the
  proof-of-concept that motivated it — a payload crafted to parse as one message
  under CBOR and a different one under protobuf, with the type flipped after
  signing. That notebook is the citation behind R-O-05's type-indicator clause.

**Retracted (2026-10-08).** An earlier version of this summary claimed the
`(t, n)` envelope already carried threshold semantics, and that R-I-03's export
target therefore gave R-M-06 a cheaper interchange story than expected. It does
not. The sentence continues *"where `t` is application-specific"* — `t` is a
verifier-side parameter supplied out of band, not an envelope field — and
`envelope.md` adds that multiple signatures are *"equivalent to separate
envelopes with individual signatures"*. A DSSE envelope carries `n` and cannot
carry `k`. See `distilled/design-notes.md` §1.

## Limits

- **`KEYID` is unauthenticated and `MUST NOT` be used for security decisions** —
  it is only a hint to narrow key selection. This is the opposite of our
  `KeyId`, which under R-M-02 *is* the principal's name. The collision of terms
  is a documentation hazard for any mapping table written under R-I-01.
- **`PAYLOAD_TYPE` is *recommended* to be a globally allocated string** — a media
  type or a URI. Under R-M-12 (accepted as ARCH-0002 P1 via ADR-0001) that is
  exactly the centrally allocated extension point the native model excludes. But
  the recommendation is a **SHOULD**, and `envelope.md` §Other data structures
  licenses the escape — *"code `payloadType` as a shorter string or enum"* —
  which PAE authenticates just as well. So DSSE does not force a global
  identifier; its default recommends one, and the cost of declining is ecosystem
  divergence rather than non-conformance. This corrects a stronger claim made
  here earlier; see `distilled/design-notes.md` §2.
- **`envelope.md` requires consumers to `MUST ignore unrecognized fields`**,
  which is the opposite default to ARCH-0002 **P5**'s reject-unknown — at the
  envelope layer only, since unsupported *payload types* are rejected. A
  conforming DSSE export boundary therefore cannot enforce P5 on the envelope
  exterior. See `distilled/design-notes.md` §3.
- **No canonical form at all**, which is the point — but it means DSSE cannot
  express R-M-11's description-mode `ArtifactId` or ARCH-0002 P4's domain hash,
  both of which require canonicalising a structure to derive its identity.
- **Signature algorithm and key management are out of scope**, agreed out of
  band, so DSSE settles none of DEC-003.
- **Read scope:** all specification text at the pinned commit —
  `background.md` and `protocol.md` (2026-10-03), `envelope.md`,
  `envelope.proto` and `hypothetical_signature_attack.ipynb` (2026-10-08). The
  `implementation/` and `governance/` sub-trees are not specification text and
  are not read. Reading the last three changed two conclusions recorded here;
  both retractions are above and in `distilled/design-notes.md`.
- This record is type `repo`, so FX-1 full extraction does not apply to it. If
  DSSE becomes a selected envelope under DEC-005 rather than an export target,
  that exemption should be revisited.
