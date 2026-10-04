---
schema: "library-summary/v1"
id: draft-ietf-cose-sphincs-plus
record: draft-ietf-cose-sphincs-plus
type: summary
updated: "2026-10-03"
---

# SLH-DSA for JOSE and COSE

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | `draft` — IETF COSE WG, intended status Standards Track; expires 2027-01-29 |
| **Authors** | M. Prorock (mesur.io), O. Steele (Tradeverifyd), H. Tschofenig (UniBw M.) |
| **Published** | 2026-07-28 (**revision -10**) |
| **Identifier** | draft-ietf-cose-sphincs-plus-10 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cose-sphincs-plus-10.txt |
| **Digest** | `sha256:f6b882a07aec9834e02e5bd8b0576a0474e70874582ea120b8aa47c0f82758a5` |

## Overview

The wire binding for **FIPS 205 SLH-DSA** in JOSE and COSE — algorithm
identifiers, signatures, public keys and private keys. It is the SLH-DSA
counterpart to `rfc-9964`, and it is the document `fips-205`'s Limits section
named as missing.

The headline finding is **how little of FIPS 205 it binds**. FIPS 205 defines
twelve parameter sets; this draft registers **two**:

| Name | JOSE `alg` | COSE `alg` |
|---|---|---|
| SLH-DSA-SHA2-128s | `SLH-DSA-SHA2-128s` | **TBD1 (-51)** |
| SLH-DSA-SHAKE-128s | `SLH-DSA-SHAKE-128s` | **TBD2 (-52)** |

The draft states its own reasoning plainly: both are NIST **Category 1**,
both are the **"small"** variant, one per hash family, and

> Limiting the initial registration to a small, symmetric set is intended to
> maximize interoperability among early implementations and to keep the JOSE
> and COSE registries focused.

It is also candid about the expected constituency — deployments that
specifically need a stateless hash-based scheme or want algorithmic diversity
as a fallback, with **firmware signing** named as the primary use case — and
adds that registration "does not imply that every general-purpose JOSE or COSE
implementation is expected to support them."

As with `rfc-9964` and `rfc-9053`, the registered algorithms identify **pure**
SLH-DSA (`slh_sign` / `slh_verify`, FIPS 205 §§10.2.1 and 10.3). No pre-hash
variant is registered.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The only way to carry a hash-based post-quantum signature in COSE |
| Cryptography | `adjacent` | A binding, not a primitive — the primitive is FIPS 205 |
| This project | `adjacent` | NG3 defers the suite; this is the hedge's only wire form |

Bears on no `DEC-*`. It closes a gap this lane recorded rather than opening a
decision: `fips-205` could not say what an SLH-DSA signature looks like on the
wire, and now it can.

## Implementations

Searched **2026-10-03**. **None found.** The FIPS 205 primitives exist
(liboqs, BouncyCastle, the SPHINCS+ reference implementation), but no COSE or
JOSE library was found implementing *this binding* — unsurprising for a draft
whose code points are still TBD. That is a result, not an omission.

| Name | Kind | License | URL |
|---|---|---|---|
| — | — | — | none found on 2026-10-03 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. It is a draft with unassigned code points; extracting
requirements from text that will change is work we would redo.

## Limits

- **Two parameter sets out of twelve, and both are Category 1.** There is no
  registered way to carry SLH-DSA at Category 3 or 5 in COSE, and no `f`
  (fast-signing) variant at all. A deployment wanting category-5 hash-based
  signatures — the conservative choice, for the most conservative reason —
  cannot express it. Read with `fips-205`, which specifies all twelve.
- **The suggested code points are already taken.** The draft proposes
  `TBD1 (-51)` and `TBD2 (-52)`, but in the live IANA COSE Algorithms registry
  (snapshot 2026-10-03, `iana-cose-algorithms`) **-51 is ESP384 and -52 is
  ESP512**, both assigned by **RFC 9864 §2.1** and both `Recommended: Yes`.
  RFC 9864 is held in this library. So the draft's parenthetical values are
  stale and must change before publication — they are suggestions, not
  assignments, and nothing should be implemented against them. Checked against
  the registry rather than assumed.
- **`128s` means the 7 856-byte signature.** The smallest SLH-DSA signature is
  still roughly 123× an Ed25519 signature. Registering only the `s` variants
  means COSE's SLH-DSA is the slow-signing, smaller-signature corner of
  FIPS 205 — a reasonable choice for firmware, and a poor fit for a system
  signing many small statements. The constraint recorded in `fips-205`'s
  Limits is not relieved by this binding; it is fixed in place.
- **It is a draft and expires 2027-01-29.** Revision `-10` is recorded in
  `version` and `identifiers.draft`; a new revision is a re-ingest, not an
  edit in place.
- **No implementations exist to check it against.** Everything above is read
  from the draft text, not verified against running code.
