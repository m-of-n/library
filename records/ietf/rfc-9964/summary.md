---
schema: "library-summary/v1"
id: rfc-9964
record: rfc-9964
type: summary
updated: "2026-10-03"
---

# ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track, IESG-approved |
| **Authors** | M. Prorock, O. Steele (Tradeverifyd) |
| **Published** | 2026-05 |
| **Identifier** | RFC 9964 · DOI 10.17487/RFC9964 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9964.txt |
| **Digest** | `sha256:8c42035b948301b197d431de8b3f40019bdaa3bb40150dc523306923948f34cf` |

## Overview

Binds **FIPS 204 ML-DSA** to the COSE and JOSE wire formats. This is the
document that turns "NIST standardised a post-quantum signature" into
something with a concrete algorithm identifier a verifier can dispatch on.

It does two separable things. First it registers the **algorithms**:

| Name | COSE `alg` | Recommended |
|---|---|---|
| ML-DSA-44 | **-48** | Yes |
| ML-DSA-65 | **-49** | Yes |
| ML-DSA-87 | **-50** | Yes |

Second — and more consequentially — it introduces the **AKP (Algorithm Key
Pair) key type**, COSE `kty` value **7**. AKP is deliberately generic: §3 says
it "specifies a generic cryptographic key structure for use with algorithms
not limited to those registered in this document." A key carries `alg`
(REQUIRED), `pub` (REQUIRED) and `priv` (MUST NOT appear in a public key),
with the byte-string format determined by `alg` rather than by the key type.
This is a different shape from `EC2`/`OKP`, where the key type implies the
structure.

§6 then defines **AKP thumbprints**: computing a COSE Key Thumbprint per
RFC 9679 over an AKP key requires exactly `kty` (1, int, 7), `alg` (3, int)
and `pub` (-1, bstr); the JWK Thumbprint per RFC 7638 uses `alg`, `kty`, `pub`
in that lexicographic order.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines how a post-quantum signature is carried and identified |
| Cryptography | `adjacent` | A binding, not a primitive — the primitive is FIPS 204 |
| This project | `adjacent` | NG3 defers the suite, but this is the first document a suite decision would need |

Bears on **R-M-02** — *a principal MAY be identified solely by key or key
digest*. §6 is the concrete mechanism: it specifies exactly which parameters
enter the digest when a principal is named by the thumbprint of a
post-quantum key. The library holds `rfc-9679`, so this chain is complete and
checkable — R-M-02 → COSE Key Thumbprint → the three required AKP parameters.
This is the most directly load-bearing document in the post-quantum lane.

Note what the thumbprint includes: **`alg` is part of the digest**. A
principal's identity under R-M-02 is therefore bound to the parameter set, not
just to the key material. Moving a principal from ML-DSA-44 to ML-DSA-65 makes
it a different principal.

## Implementations

Searched **2026-10-03**. The RFC is five months old and implementations are
early; expect the key type to lag the algorithms.

| Name | Kind | License | URL |
|---|---|---|---|
| `cose-lib` / COSE-JS ecosystem | open source | varies | https://github.com/cose-wg — tracking AKP support |
| liboqs (Open Quantum Safe) | open source | MIT | https://openquantumsafe.org — supplies ML-DSA; COSE binding is separate |
| BouncyCastle | open source | MIT | https://bouncycastle.org — ML-DSA primitives present |

**No implementation verified against this RFC on 2026-10-03.** That is a
result, not an omission: the primitives are widely available, the *AKP key
type and thumbprint rules* are what would need checking, and this record does
not claim they have been.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. **FX-1 extraction for this record is owned by #39** (Tier 2),
not by the NIST lane — this issue owns ingest, summary and the relation graph
only, and the `distillation` block is deliberately untouched.

## Limits

- **It deliberately does not support HashML-DSA, and says so.** §7.2 states
  that no algorithms are specified for the pre-hash variant of FIPS 204 §5.4,
  because "the verify routines are different" and future support would need
  *additional* registrations. This matches COSE's treatment of EdDSA in
  `rfc-9053` §2.2, which admits only pure EdDSA and excludes HashEdDSA.
  **COSE consistently refuses pre-hash variants** — a pattern worth carrying
  into any encoding decision rather than rediscovering.
- **The rationale lives in a document the library does not hold.** §7.2 defers
  the actual argument to §8.3 of **RFC 9881**, which is not in the library. The
  reason COSE excludes HashML-DSA is therefore currently a citation, not
  something we can check. Named here rather than recorded as a dangling
  relation; it is an ingest candidate.
- **AKP's generality is a loaded gun.** Because `pub` and `priv` are opaque
  byte strings whose format is determined by `alg`, a verifier that dispatches
  on `kty` alone learns nothing about the key's structure. §7.4 flags
  mismatched AKP parameters as a security consideration for exactly this
  reason. The key type cannot be validated independently of the algorithm.
- **It binds ML-DSA only.** SLH-DSA (FIPS 205) has no COSE binding here, and
  the library holds no draft for one. A system that wanted the hash-based
  hedge could not express it in COSE today.
- **Standards Track does not mean deployed.** Published May 2026. The
  algorithm code points are stable; the ecosystem is not yet.
