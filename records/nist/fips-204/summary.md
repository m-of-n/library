---
schema: "library-summary/v1"
id: fips-204
record: fips-204
type: summary
updated: "2026-10-08"
---

# Module-Lattice-Based Digital Signature Standard

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, issued under 40 U.S.C. 11331 |
| **Authors** | NIST |
| **Published** | 2024-08-13 (effective the same day) |
| **Identifier** | FIPS 204 · DOI 10.6028/NIST.FIPS.204 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf |
| **Digest** | `sha256:57239b9f84c03227eda3ca0991204dc7764c79af9ce2e6824eda774918d46b6b` |

## Overview

Specifies **ML-DSA**, a lattice-based digital signature scheme derived from
CRYSTALS-Dilithium, in three parameter sets. Security rests on the **Module
Learning With Errors** and **Module Short Integer Solution** problems, and the
construction is **Fiat-Shamir with Aborts** (§3). The design target is
**SUF-CMA** — strong existential unforgeability under chosen-message attack,
meaning an adversary cannot produce even a *new signature on an
already-signed message* (§3.1).

| Parameter set | Claimed category | Private key | Public key | Signature |
|---|---|---|---|---|
| ML-DSA-44 | 2 | 2560 B | 1312 B | 2420 B |
| ML-DSA-65 | 3 | 4032 B | 1952 B | 3309 B |
| ML-DSA-87 | 5 | 4896 B | 2592 B | 4627 B |

Two details matter more to this project than the lattice mathematics:

**It is built on FIPS 202.** §3.7 states the standard "makes use of the
functions SHAKE256 and SHAKE128, as defined in FIPS 202," and additionally
uses the incremental absorb/squeeze API from **SP 800-185**. The post-quantum
signature standard inherits the SHA-3 permutation exactly as ML-KEM does.

**Signing takes a context string.** `ML-DSA.Sign` takes `(sk, M, ctx)` where
`ctx` is a byte string of **255 or fewer bytes**, empty by default, and signing
returns ⊥ if it is longer (§5.2, Algorithm 2 line 2). A separate,
**domain-separated** scheme `HashML-DSA` (§5.4) adds a pre-hashing step for
signing a digest rather than the message.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A signature standard, and the likely post-quantum default |
| Cryptography | `core` | Normative for the primitive |
| This project | `adjacent` | ARCH-0001 NG3 defers the suite, but this is the strongest candidate for it |

Bears on **R-M-02** — *a principal MAY be identified solely by key or key
digest*. ML-DSA is where that requirement gets expensive: a public key is
**1312–2592 bytes**, against 32 for Ed25519. Naming a principal *by key*
rather than by key digest is a design option under R-M-02, and at these sizes
it stops being a free one. Naming by digest is unaffected.

This is the record in the lane that comes closest to bearing on a real
decision. It bears on no open `DEC-*` **today** only because NG3 defers the
suite; if that defer is ever lifted, ML-DSA is the first thing a suite ADR
would have to rule on.

## Implementations

Searched **2026-10-03**. Coverage is markedly better than for SLH-DSA — ML-DSA
is the one post-quantum signature scheme with mainstream library support.

| Name | Kind | License | URL |
|---|---|---|---|
| `pq-crystals/dilithium` | open source | CC0 / Apache-2.0 | https://github.com/pq-crystals/dilithium — reference from the submission team |
| liboqs (Open Quantum Safe) | open source | MIT | https://openquantumsafe.org |
| OpenSSL 3.5+ | open source | Apache-2.0 | https://openssl.org |
| AWS-LC | open source | Apache-2.0 / ISC | https://github.com/aws/aws-lc |
| BouncyCastle | open source | MIT | https://bouncycastle.org |

**We use a vetted library. We do not implement these.**

## Test vectors — the PROC-0002 stage 8 hook

NIST's **ACVP** server publishes validation vectors for ML-DSA under four
registered algorithm/mode/revision triples:

| Registration | Revision | Notes |
|---|---|---|
| `ML-DSA / keyGen / FIPS204` | `FIPS204` | ≥25 tests per parameter set |
| `ML-DSA / sigGen / FIPS204` | `FIPS204` | |
| `ML-DSA / sigVer / FIPS204` | `FIPS204` | negative tests from server-modified signatures |
| `ML-DSA / sigGen / FIPS204-tr1` | `FIPS204-tr1` | a **new test revision against the same standard** — adds `keyFormats`, so sigGen may receive the private key as a 32-byte seed rather than expanded |

The schema is defined by **`draft-celi-acvp-ml-dsa-01`** (2 October 2026), the
CAVP's own sub-specification; there is no `keyVer` mode for ML-DSA, unlike
ECDSA. All three `FIPS204` revisions were enabled on ACVTS **production on
2024-08-13** — the day FIPS 204 was published. `FIPS204-tr1` arrived with
ACVP-Server **v1.1.0.43** (2026-08-12).

This is the **publisher source** that PROC-0002 stage 8 requires: vectors come
from the source or its publisher and are **never generated**. A self-generated
vector proves only that the code agrees with itself. If a stage 8
implementation of ML-DSA ships without ACVP vectors, that is a **stage 10
failure**.

**Retrievable without a CMVP account — yes, for the published sets.** Each
registration has a directory under `gen-val/json-files/` in the public
`usnistgov/ACVP-Server` repository holding `registration.json`, `prompt.json`,
`expectedResults.json` and `internalProjection.json`. Verified anonymous
HTTPS retrieval on **2026-10-08**; no certificate, account or CMVP
relationship is needed. A *live* ACVTS session is different: `demo.acvts.nist.gov`
and the production server require a NIST-issued TLS client certificate and a
TOTP seed, so **freshly generated** per-session vectors are gated even though
the published sample sets are not. Stage 8 needs the published sets.

**What the vectors cover that this record cares about.** The sigGen and sigVer
registrations carry `signatureInterfaces` (`internal`/`external`), `preHash`
(`pure`/`preHash` — ML-DSA versus HashML-DSA), `externalMu`, and
`contextLength`. The domain separation flagged under Limits below is therefore
a **registered, tested distinction**, not an informal one: a conformance claim
names which interface and which of the two schemes it covers.

**What they do not cover.** `draft-celi-acvp-ml-dsa-01` §6.2.2 excludes FIPS
204 §3.5 *Additional Requirements* — an ACVP server "will not test the
zeroization of intermediate values, security strength of the deterministic
random bit generators (DRBGs), or incorrect length signatures or public keys."
Read that against the first bullet under Limits: whether ML-DSA-44 actually
reaches category 2 depends on the RBG's security strength, and **that is
precisely what the vectors do not check**. Passing ACVP is a correctness
assertion, not a strength assertion.

**Vector sets have a shelf life.** ACVP-Server **v1.1.0.38** (2025-02-21) added
external-interface testing and changed the sigGen/sigVer registration format;
vectors generated before it cannot be submitted against a later release. A
pinned vector set must record the server release it came from.

CAVP/ACVP coverage for ML-DSA is newer than the classical suites; treat a FIPS
204 conformance claim as something to check against CMVP, not to infer from a
library's release notes.

- `usnistgov/ACVP` — protocol specification; algorithm sub-specifications at https://pages.nist.gov/ACVP/
- `usnistgov/ACVP-Server` — the server, its releases and the published vector sets
- https://pages.nist.gov/ACVP/draft-celi-acvp-ml-dsa.html — the ML-DSA schema

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. FX-1 extraction is warranted where we intend to conform or
map; the suite is deferred, so we hold and cite rather than extract. If NG3 is
ever lifted, this record is a candidate for promotion.

## Limits

- **Category 2 is not a typo, and ML-DSA-44 is conditional.** ML-DSA-44 is
  claimed at category **2** — the only parameter set in this lane below
  category 3. §3.6.1 adds a condition most summaries drop: the RBG used
  "should have a security strength of at least 192 bits and **shall** have a
  security strength of at least 128 bits," and at 128 the **claimed strength
  of ML-DSA-44 is reduced from category 2 to category 1**. The headline
  category depends on the entropy source, not on the scheme alone.
- **The context string is a domain-separation hook with a hard ceiling.** 255
  bytes is enough for a short label and not enough for a URI-shaped domain
  identifier of any length. P4 holds that domains of discourse are
  *hash-identified* — which fits a fixed-width digest comfortably inside 255
  bytes, but only if the domain is named by its digest rather than spelled out.
  Worth noting before any encoding decision assumes room here.
- **Deterministic signing is permitted and is not the recommended default.**
  §3.4 allows a fully deterministic variant for signers without reliable
  randomness, then states that determinism "makes the risk of side-channel
  attacks (particularly fault attacks) more difficult to manage," and that
  implementing the hedged variant alone is sufficient for interoperability.
  A verifier cannot tell which was used.
- **Two schemes, not one, and a key should not cross between them.** ML-DSA and
  HashML-DSA are domain-separated. Treating "ML-DSA" as a single algorithm
  identifier is an error that an encoding or COSE binding must not make — see
  `rfc-9964`, which registers the algorithm identifiers, and which this library
  holds only at `fetched`.
- **Its security is conditional on FIPS 202, exactly as ML-KEM's is.** H, the
  PRFs and the expansion functions are SHAKE. Any future weakening of
  `KECCAK-p` is an ML-DSA problem too; `fips-202` and this record are not
  independent.
- **Category claims are claims.** **§4** (*Parameter Sets*) presents
  categories 2/3/5 as *claimed*, benchmarked against the cost of breaking a
  generic block cipher or hash function under "any realistic model of
  computation" — and notes that different models give more or less accurate
  estimates. Lattice
  cryptanalysis is young relative to factoring, and the document does not
  pretend otherwise.
