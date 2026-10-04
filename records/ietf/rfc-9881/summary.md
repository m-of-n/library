---
schema: "library-summary/v1"
id: rfc-9881
record: rfc-9881
type: summary
updated: "2026-10-03"
---

# Internet X.509 PKI — Algorithm Identifiers for ML-DSA

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track |
| **Authors** | J. Massimo, P. Kampanakis (AWS), S. Turner (sn3rd), B. E. Westerbaan (Cloudflare) |
| **Published** | 2025-10 |
| **Identifier** | RFC 9881 · DOI 10.17487/RFC9881 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9881.txt |
| **Digest** | `sha256:20ae3b519bc69e32989fa6e625ab8746453eddf457e20ddbfd79d841a44237a2` |

## Overview

Specifies how **FIPS 204 ML-DSA** is used in **X.509 certificates and CRLs** —
the algorithm identifiers, and the conventions for signatures, subject public
keys and private keys. It is the PKIX counterpart to `rfc-9964`, which does the
same job for COSE and JOSE.

The library holds it for one specific reason. `rfc-9964` §7.2 declines to
register HashML-DSA for COSE and **defers the actual argument to §8.3 of this
document**. That made the reason COSE excludes pre-hash signing a citation we
could not check. It is now checkable, and the argument turns out to be
**primarily about interoperability, not cryptography**:

> This restriction is primarily to increase interoperability.
>
> ML-DSA and HashML-DSA are incompatible algorithms that require different
> `Verify()` routines. … since the same OIDs are used to identify the ML-DSA
> public keys and ML-DSA signature algorithms, an implementation would need to
> commit a given public key to be either of type ML-DSA or HashML-DSA at the
> time of certificate creation.

There is a secondary, genuinely cryptographic argument: ML-DSA prepends `tr`,
the SHAKE256 hash of the **public key**, to the message before hashing
(FIPS 204 Algorithm 7, line 6). A collision attack against SHA-3 would
therefore have to be **public-key-specific** — the attacker needs
`H(tr ‖ m₁) = H(tr ‖ m₂)` for one particular key, not a generic collision.
Pure ML-DSA is strictly stronger than HashML-DSA here, and stronger than
conventional RSA or ECDSA.

The document also points at a **third mode** — External `μ`, in its
Appendix D — which it says avoids the operational concerns that motivate the
HashML-DSA ban.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Fixes how a post-quantum signature is identified in the PKI |
| Cryptography | `adjacent` | A binding and an OID allocation, not a primitive |
| This project | `adjacent` | X.509 is not our envelope, but this is where the COSE argument actually lives |

Bears on no `DEC-*`. ARCH-0001 is not an X.509 system. It is held as the
**source of an argument another record depends on** — the library's typed
`cited_by` edge from `rfc-9964` is the whole point of the record.

## Implementations

Searched **2026-10-03**. Certificate-side ML-DSA support is emerging; treat
any conformance claim as version-specific.

| Name | Kind | License | URL |
|---|---|---|---|
| BouncyCastle | open source | MIT | https://bouncycastle.org |
| OpenSSL 3.5+ | open source | Apache-2.0 | https://openssl.org |
| AWS-LC | open source | Apache-2.0 / ISC | https://github.com/aws/aws-lc |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Held to resolve `rfc-9964`'s citation; X.509 conformance is
not in scope for this project.

## Limits

- **It is an X.509 document, and the COSE world inherited its reasoning
  wholesale.** The argument that governs COSE's treatment of HashML-DSA was
  made for certificates, where a public key must be bound to one mode *at
  certificate-creation time*. COSE has no certificates and no such binding
  moment, so the premise does not straightforwardly transfer — yet `rfc-9964`
  adopts the conclusion by reference. Worth noticing before treating "COSE
  refuses pre-hash" as a reasoned COSE position rather than an inherited one.
- **"Primarily to increase interoperability" is the document's own
  characterisation.** The collision-resistance point is explicitly a *minor*
  security reason. Anyone citing the HashML-DSA exclusion as a security
  decision is overstating it.
- **External `μ` is a third mode and this lane holds nothing else on it.**
  Appendix D names it as the answer to the operational problem; the library
  has no other record covering it, and neither `fips-204` nor `rfc-9964`
  describes it.
- **OIDs, not COSE code points.** Nothing in this document is directly usable
  in a COSE context; `rfc-9964` is the record for that.
