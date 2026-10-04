---
schema: "library-summary/v1"
id: sp-800-186
record: sp-800-186
type: summary
updated: "2026-10-03"
---

# Recommendations for Discrete Logarithm-based Cryptography: Elliptic Curve Domain Parameters

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication issued under FISMA 2014, 44 U.S.C. §3551. Guidance for federal systems, not a FIPS |
| **Authors** | Lily Chen, Dustin Moody, Andrew Regenscheid, Angela Robinson (NIST Computer Security Division); Karen Randall (Randall Consulting) |
| **Published** | 2023-02 (NIST publishes no day for this document) |
| **Identifier** | SP 800-186 · DOI 10.6028/NIST.SP.800-186 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-186.pdf |
| **Digest** | `sha256:53c7cf3340528aaa0a7bbeaef947f2099568192367d4341a7d4abceb55f78432` |

## Overview

Specifies the **elliptic curve domain parameters** approved for U.S. federal
government use — the concrete `(p, h, n, Type, a, b, G, {Seed, c})` tuples, not
the algorithms that consume them. §1.1 is explicit that it is to be read
alongside FIPS 186-5 (signatures) and SP 800-56A (key establishment), and that
keys from these curves are for "digital signature generation and verification
or key agreement only."

The substantive change from the curve set it replaces is the admission of
**Edwards and Montgomery curves** — edwards25519, edwards448, Curve25519,
Curve448, E448 — alongside the legacy NIST prime curves, with NIST stating the
new curves are **interoperable with those specified by the IETF CFRG**
(RFC 7748, RFC 8032). The second change is a demotion: the binary-field curves
are **deprecated**, and the document says "it is strongly recommended to use
the other prime curves."

Table 2, *Allowed Usage of the Specified Curves*, is the operative page:

| Curves | Allowed usage |
|---|---|
| K-233/283/409/571, B-233/283/409/571 | **Deprecated** |
| P-224, P-256, P-384, P-521 | ECDSA, EC key establishment (SP 800-56A) |
| edwards25519, edwards448 | EdDSA |
| Curve25519, W-25519, Curve448, E448, W-448 | Alternative representations for implementation flexibility — **not to be used for ECDSA or EdDSA directly** |

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Curve choice is a security decision, and this is the document that bounds it for federal-facing work |
| Cryptography | `core` | Normative for the domain parameters themselves |
| This project | `adjacent` | Bounds which keys can name a principal, but ARCH-0001 NG3 defers the suite |

Bears on **R-M-02** — *a principal MAY be identified solely by key or key
digest*. If a principal is named by a key, this document fixes which curves
that key may lie on, exactly as `fips-180-4` fixes which digest functions may
compute a key digest. It is a bound on the naming space, not a requirement
discharged.

It bears on **no open `DEC-*`**. ARCH-0001 NG3 defers the algorithm suite, so
there is no decision here to inform yet; the record exists so that a future
suite ADR is not a cold start. Per `docs/scope.md` §1 the "bears on a decision"
test is a prompt for judgement, not a gate.

## Implementations

Searched **2026-10-03**. Coverage is uneven in a way that matters: the prime
curves and Ed25519 are near-universal, Ed448 much less so, and the deprecated
binary curves are being actively removed from libraries rather than maintained.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org — P-224/256/384/521, Ed25519, Ed448 |
| libsodium | open source | ISC | https://libsodium.org — Ed25519 and X25519 only; no NIST prime curves |
| Go `crypto/elliptic`, `crypto/ed25519`, `crypto/ecdh` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/elliptic — no Ed448 |
| RustCrypto `elliptic-curves` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/elliptic-curves |
| BoringSSL | open source | ISC / OpenSSL | https://boringssl.googlesource.com |
| CAVP/CMVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these.** Curve arithmetic is
precisely the category where a hand-rolled implementation is a defect.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. FX-1 extraction is warranted only where we intend to conform
or map, and the suite is deferred — the domain parameters are reference data we
would cite, not requirements we would discharge.

## Limits

- **It specifies parameters, not algorithms, and settles nothing on its own.**
  ECDSA and EdDSA are in FIPS 186-5; key establishment is in SP 800-56A. Citing
  SP 800-186 for "how we sign" would be a category error.
- **The library does not hold its two most load-bearing companions.**
  **SP 800-56A** (key establishment, named in Table 2 as the authority for the
  allowed usage of P-224/256/384/521) and **RFC 7748** (the CFRG source for
  Curve25519/Curve448, and the basis for the interoperability claim) are both
  absent. `rfc-8032` is held, so the EdDSA side is covered; the key-agreement
  and Montgomery-curve side is not. Relations to the two missing documents are
  deliberately **not** recorded rather than left dangling — they are named here
  instead, and are ingest candidates.
- **P-192 is specified but has no allowed usage.** §3.2.1 lists it among the
  pseudorandom Weierstrass curves, and Table 2 then omits it entirely — as it
  omits K-163/B-163. The document never states in one place that P-192 is
  disallowed; it simply never grants it a use. An implementer reading §3 alone
  and not Table 2 would get this wrong.
- **The pseudorandom curves are generated from unexplained seeds via SHA-1.**
  §3.2.1 records a 160-bit `Seed` fed to SHA-1 (Appendix C.3) to derive the
  coefficients. The procedure is *verifiable* — given the seed you can confirm
  the coefficients — but the provenance of the seeds themselves is not
  explained here, which is the long-standing objection to the NIST prime
  curves. NIST neither restates nor answers that objection in this document.
  Note the asymmetry worth recording: the newer special curves W-25519 and
  W-448 use **no seed at all**, which is the stronger position.
- **"Deprecated" is not "disallowed," and the document does not say what
  deprecation obliges.** The binary curves remain fully specified, with no
  sunset date and no migration requirement stated here. Whatever force
  deprecation has comes from elsewhere — SP 800-57 Part 1 and the CMVP
  transition schedule — not from this text.
- **It is entirely classical.** Every curve here is broken by a
  cryptographically relevant quantum computer. SP 800-186 makes no post-quantum
  claim and should never be read as the current answer; the post-quantum
  signature standards are FIPS 204 and FIPS 205, held separately in this lane.
