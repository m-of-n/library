---
schema: "library-summary/v1"
id: fips-205
record: fips-205
type: summary
updated: "2026-10-08"
---

# Stateless Hash-Based Digital Signature Standard

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, issued under 40 U.S.C. 11331 |
| **Authors** | NIST |
| **Published** | 2024-08-13 |
| **Identifier** | FIPS 205 · DOI 10.6028/NIST.FIPS.205 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf |
| **Digest** | `sha256:8ef34228276f3386d23cb0da8c14592b8cfb0db3358016bba64df7a004f8d13d` |

## Overview

Specifies **SLH-DSA**, a stateless hash-based signature scheme derived from
SPHINCS+. Its distinguishing claim is **what it does not assume**: security
rests on the properties of the underlying hash function alone — no lattice,
no discrete log, no factoring. It is the conservative hedge in NIST's
post-quantum portfolio, and the one whose security argument would survive a
break of ML-DSA.

The construction stacks three hash-based primitives: **WOTS+** one-time
signatures, **XMSS** Merkle trees, assembled into a **hypertree** of total
height *h* across *d* layers, with **FORS** few-time signatures at the bottom
signing the actual message digest (§§5–8). "Stateless" is the contrast with
`sp-800-208` (HSS/LMS), where the signer **must** track which one-time keys
are spent; SLH-DSA removes that obligation, and removes with it the
catastrophic failure mode of state reuse.

Twelve parameter sets: **SHA2** and **SHAKE** families × 128/192/256 ×
`s` (small signature) / `f` (fast signing).

| Parameter set | Category | Public key | Signature |
|---|---|---|---|
| SLH-DSA-{SHA2,SHAKE}-128s | 1 | 32 B | **7 856 B** |
| SLH-DSA-{SHA2,SHAKE}-128f | 1 | 32 B | **17 088 B** |
| SLH-DSA-{SHA2,SHAKE}-192s | 3 | 48 B | **16 224 B** |
| SLH-DSA-{SHA2,SHAKE}-192f | 3 | 48 B | **35 664 B** |
| SLH-DSA-{SHA2,SHAKE}-256s | 5 | 64 B | **29 792 B** |
| SLH-DSA-{SHA2,SHAKE}-256f | 5 | 64 B | **49 856 B** |

Like ML-DSA it takes a **context string of at most 255 bytes**, empty by
default, and defines a domain-separated pre-hash variant, `HashSLH-DSA`
(§10.2.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A signature standard, and the conservative post-quantum option |
| Cryptography | `core` | Normative for the primitive |
| This project | `adjacent` | ARCH-0001 NG3 defers the suite; held as the hedge, not the default |

Bears on **R-M-02** — *a principal MAY be identified solely by key or key
digest*. SLH-DSA inverts ML-DSA's trade: the **public key is tiny** (32–64
bytes, comparable to Ed25519), so naming a principal by key is cheap here.
The cost moves entirely into the signature.

It bears on no open `DEC-*`. The suite is deferred under NG3, and SLH-DSA
would in any case be a fallback rather than a default.

## Implementations

Searched **2026-10-03**. Thinner than ML-DSA's — SLH-DSA is implemented where
post-quantum coverage is a goal in itself, and is not yet a routine default.

| Name | Kind | License | URL |
|---|---|---|---|
| `sphincs/sphincsplus` | open source | CC0 | https://github.com/sphincs/sphincsplus — reference from the submission team |
| liboqs (Open Quantum Safe) | open source | MIT | https://openquantumsafe.org |
| BouncyCastle | open source | MIT | https://bouncycastle.org |
| AWS-LC | open source | Apache-2.0 / ISC | https://github.com/aws/aws-lc |

Notably **absent**: Go's standard library and libsodium carry no SLH-DSA, and
OpenSSL's support lags its ML-DSA support. **We use a vetted library. We do
not implement these** — the hypertree construction is long, parameter-heavy,
and unforgiving of an indexing error.

## Test vectors — the PROC-0002 stage 8 hook

NIST's **ACVP** server publishes validation vectors for SLH-DSA under three
registered algorithm/mode/revision triples:

| Registration | Revision |
|---|---|
| `SLH-DSA / keyGen / FIPS205` | `FIPS205` |
| `SLH-DSA / sigGen / FIPS205` | `FIPS205` |
| `SLH-DSA / sigVer / FIPS205` | `FIPS205` |

The schema is defined by **`draft-livelsberger-acvp-slh-dsa-01`** (2 October
2026) — a different sub-specification and a different editor from ML-DSA's.
There is one revision only; unlike ML-DSA there is no `-tr1` seed-format
revision. All three were enabled on ACVTS **production on 2024-08-13**, the day
FIPS 205 was published, alongside ML-DSA's.

This is the **publisher source** that PROC-0002 stage 8 requires: vectors come
from the source or its publisher and are **never generated**. A self-generated
vector proves only that the code agrees with itself. If a stage 8
implementation of SLH-DSA ships without ACVP vectors, that is a **stage 10
failure**.

**Retrievable without a CMVP account — yes, for the published sets.** Each
registration has a directory under `gen-val/json-files/` in the public
`usnistgov/ACVP-Server` repository holding `registration.json`, `prompt.json`,
`expectedResults.json` and `internalProjection.json`. Verified anonymous HTTPS
retrieval on **2026-10-08**; no certificate, account or CMVP relationship is
needed. A *live* ACVTS session is gated — `demo.acvts.nist.gov` and the
production server require a NIST-issued TLS client certificate and a TOTP
seed — so **freshly generated** per-session vectors need a NIST relationship
and the published sample sets do not.

**The signature size shows up here too, and it is a stage 8 logistics
problem.** `SLH-DSA-sigGen-FIPS205/expectedResults.json` is ≈32 MB and its
`internalProjection.json` ≈38 MB — a direct consequence of signatures up to
49 856 bytes. These are **third-party bytes we must not commit** (`CLAUDE.md`);
a stage 8 harness fetches them by URL and pins the digest, exactly as this
record pins the FIPS 205 PDF.

**What the vectors cover.** `sigVer` is the interesting one: the server takes a
valid signature and mutates it, with at least two tests per disposition —
unmodified (must verify), modified message, modified **R**, modified
**SIGFORS**, modified **SIGHT**, signature too long, signature too short. So
component-level rejection across the hypertree construction is tested, which is
worth having given how unforgiving that construction is of an indexing error.
`sigGen`/`sigVer` also register `signatureInterfaces`, `preHash`
(`pure`/`preHash` — SLH-DSA versus HashSLH-DSA) and `contextLength`, whose
domain runs 0–2040 **bits**: the 255-byte context ceiling, expressed in the
registration.

**What they do not cover.** `draft-livelsberger-acvp-slh-dsa-01` §6.2.2
excludes FIPS 205 §3.1 *Additional Requirements*: an ACVP server "will not
test that fresh seed values are used for fresh invocations of key generation,
that approved deterministic random bit generators (DRBGs) are used with the
correct security strengths, that sensitive data is destroyed, that key
validation is performed, and that floating point arithmetic is not used."
Every item in that list is one the fourth bullet under Limits identifies as
load-bearing — the freshness of PK.seed/SK.seed/SK.prf, the 8*n*-bit RBG floor,
and the destruction of verification intermediates. **The vectors test the
arithmetic and none of the §3.1 obligations.** A green ACVP run is not evidence
on any of them.

- `usnistgov/ACVP` — protocol specification; algorithm sub-specifications at https://pages.nist.gov/ACVP/
- `usnistgov/ACVP-Server` — the server, its releases and the published vector sets
- https://pages.nist.gov/ACVP/draft-livelsberger-acvp-slh-dsa.html — the SLH-DSA schema

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`, for the same reason as `fips-204`: we hold and cite the
post-quantum base, and extract only where we intend to conform.

## Limits

- **The signature size is the whole story, and it is disqualifying for some
  designs.** The *smallest* SLH-DSA signature is **7 856 bytes**; the largest
  is **49 856**. Against Ed25519's 64 bytes that is a factor of 123 to 779.
  For a statement model where many small statements are each independently
  signed — which is the shape of a key-centric assertion system — this is not
  a tuning parameter, it is an architectural constraint. Any envelope or
  encoding decision that assumes signatures are "small" is silently assuming
  SLH-DSA is out of scope. **This is the single most useful fact in the
  record.**
- **`s` versus `f` is a real trade and the document does not choose for you.**
  The `s` sets roughly halve the signature at the cost of much slower signing;
  `f` inverts it. A system signing rarely and verifying often wants `s`; the
  reverse wants `f`. Both are approved, so conformance does not settle it.
- **EUF-CMA, not SUF-CMA, and bounded at 2⁶⁴ messages per key pair.** §11
  states the categories hold "when each key pair is used to sign at most 2⁶⁴
  messages." NIST notes in a footnote that 2⁶⁴ is unreachable in practice —
  over 58 years at 10 billion signatures per second — so the bound is not an
  operational concern. The weaker *existential* rather than *strong*
  unforgeability target is the more meaningful difference from `fips-204`.
- **Stateless removes a failure mode; it does not remove all of them.** The
  contrast with `sp-800-208` is the point of the scheme, but **§3.1**
  (*Additional Requirements*) still imposes a floor on the RBG under
  "Randomness generation": PK.seed, SK.seed and SK.prf must each be fresh, and
  the RBG "shall have a security strength of at least 8𝑛 bits". Under
  "Destruction of sensitive data" the same section makes an unusual point for
  a signature standard — intermediate values of the **verification** algorithm
  may reveal information about the message, signature and public key, which
  matters where signatures are used as bearer tokens or sit on plaintext
  intended to stay confidential — and requires that such data be destroyed.
- **It inherits the fate of whichever hash family you pick.** The SHA2 sets
  depend on `fips-180-4`, the SHAKE sets on `fips-202`. The scheme's selling
  point is that this is its *only* assumption — which also means the choice
  of family is the entire security surface, and the two families are not
  interchangeable once a key exists.
- **The IETF binding is not held.** `draft-ietf-cose-sphincs-plus` would
  register SLH-DSA for COSE/JOSE and give these parameter sets concrete
  algorithm identifiers. The library does not hold it, so this record cannot
  yet say what an SLH-DSA signature looks like on the wire. Named here rather
  than recorded as a dangling relation.
