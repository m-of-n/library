---
schema: "library-summary/v1"
id: fips-186-5
record: fips-186-5
type: summary
updated: "2026-09-22"
---

# Digital Signature Standard (DSS)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, approved by the Secretary of Commerce |
| **Authors** | NIST |
| **Published** | 2023-02-03 |
| **Identifier** | FIPS 186-5 · DOI 10.6028/NIST.FIPS.186-5 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf |
| **Digest** | `sha256:fbb9c7c2ba442f03c57b63b43c888311903c9d0f29f89b06efdebd9b619140c5` |

## Overview

Specifies the three digital signature schemes approved for US federal use:
**RSA**, **ECDSA**, and — new in this revision — **EdDSA** (Ed25519 and Ed448).
It defines key generation, signature generation and signature verification for
each, and delegates elliptic curve domain parameters to SP 800-186.

The consequential change from 186-4 is the retirement of **DSA**: it is retained
**only to verify existing signatures** and is no longer approved for generating
new ones. EdDSA's addition is the practical counterpart — it brings
deterministic, misuse-resistant Edwards-curve signatures into federal scope for
the first time.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines the signature schemes any key-centric model actually runs on |
| Cryptography | `core` | Normative for the primitives; we implement none of them ourselves |
| This project | `adjacent` | **Bears on no open `DEC-*`.** ARCH-0001 NG3 defers the algorithm suite |

`bears_on: R-M-02` — a principal may be identified solely by key or key digest,
which requires a defined key encoding. `R-O-05` — sign the canonical bytes; the
scheme determines what "signing" means at the bottom of that stack.

**Read this as the sponsor's rule in `docs/scope.md` §1:** the "bears on a
decision" test is a prompt for judgement, not a gate. We implement
cryptography, so this is core even though it settles no open decision.

## Implementations

Searched **2026-09-22**.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| libsodium | open source | ISC | https://libsodium.org — Ed25519 |
| python-cryptography | open source | Apache-2.0 / BSD | https://cryptography.io |
| acvp-assay | open source | — | https://github.com/Govardhan527/acvp-assay — runs ACVP vectors against an implementation you cannot link against |
| CAVP/CMVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these.** `CLAUDE.md`: no
generated cryptographic primitives.

## Test vectors — the PROC-0002 stage 8 hook

NIST's **ACVP** server publishes validation vectors covering `ECDSA sigGen
FIPS186-5`, `DetECDSA sigGen FIPS186-5`, `ECDSA sigVer FIPS186-5` and `EdDSA
sigGen 1.0`, spanning domain-parameter generation, key generation, signature
generation and verification.

This is the **publisher source** that PROC-0002 stage 8 requires: vectors come
from the source or its publisher and are **never generated**. A self-generated
vector proves only that the code agrees with itself. If a stage 8 implementation
of FIPS 186-5 ships without ACVP vectors, that is a **stage 10 failure**.

- `usnistgov/ACVP` — protocol specification
- `usnistgov/ACVP-Server` — the server and its releases

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. One is warranted only if we extract requirements from it —
we currently do not, because we conform to no clause here. See
`docs/requirements.md` §5.1.

## Limits

- **It settles nothing in our architecture.** It tells us which signature
  schemes exist and are approved, not which we should use — ARCH-0001 NG3
  explicitly defers that, and this record must not be cited as having decided it.
- **Classical only.** Post-quantum signatures are FIPS 204 (ML-DSA) and FIPS 205
  (SLH-DSA), separate records. FIPS 186-5 predates them and does not reference
  them; **treating it as "the signature standard" in 2026 would be wrong.**
- **Curve parameters are elsewhere** — SP 800-186. Reading 186-5 alone will not
  tell you which curves are approved.
- **Approval is jurisdictional, not a security argument.** "FIPS-approved"
  describes US federal procurement scope, not a claim that these are the best
  available schemes.
