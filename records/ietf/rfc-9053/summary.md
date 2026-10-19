---
schema: "library-summary/v1"
id: rfc-9053
record: rfc-9053
type: summary
updated: "2026-10-19"
---

# CBOR Object Signing and Encryption (COSE): Initial Algorithms

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational` — explicitly *not* a Standards Track specification |
| **Authors** | J. Schaad (August Cellars) |
| **Published** | 2022-08 |
| **Identifier** | RFC 9053 · DOI 10.17487/RFC9053 · obsoletes RFC 8152 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9053.txt |
| **Digest** | `sha256:3d470615875620375f8453ba25b8dce7e4d0271e76b0b79a46df34ccb2d56ab0` |

## Overview

The **algorithm half of COSE**. RFC 9052 defines the message structures;
this document defines the initial set of algorithms that populate them, and
together the two obsolete RFC 8152. It is the document that assigns the
integer code points a COSE `alg` header actually carries.

The signature algorithms are the part this project cares about:

| Name | `alg` | Notes |
|---|---|---|
| ES256 | **-7** | ECDSA w/ SHA-256 |
| ES384 | **-35** | ECDSA w/ SHA-384 |
| ES512 | **-36** | ECDSA w/ SHA-512 |
| EdDSA | **-8** | pure EdDSA only |

Beyond signatures it covers MACs (HMAC 4–7, AES-CBC-MAC), content encryption
(A128/192/256GCM = 1/2/3, eight AES-CCM variants, ChaCha20/Poly1305 = **24**),
HKDF, and the key distribution methods — direct, AES key wrap, and ECDH
variants. §7 defines the key object parameters for EC2, OKP and symmetric
keys; §8 adds COSE capabilities; §9 states the CBOR encoding restrictions.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The algorithm identifiers a COSE verifier dispatches on |
| Cryptography | `adjacent` | Bindings and code points, not primitives |
| This project | `adjacent` | Bears on DEC-005; NG3 defers the suite itself |

Bears on **DEC-005**, which is open. This document is one of the concrete
answers available to it — if COSE is selected, these are the algorithm
identifiers that come with it, and `rfc-9964` is how that set extends to
post-quantum. No decision is made here, and this record does not make one.

## Implementations

Searched **2026-10-03**. COSE's initial algorithms are the best-supported part
of the ecosystem — essentially every COSE library implements ES256 and EdDSA.

| Name | Kind | License | URL |
|---|---|---|---|
| `cose-wg` reference implementations | open source | varies | https://github.com/cose-wg |
| python-cose | open source | BSD-3-Clause | https://github.com/TimothyClaeys/pycose |
| `go-cose` | open source | MPL-2.0 | https://github.com/veraison/go-cose |
| COSE-JS | open source | Apache-2.0 | https://github.com/erdtman/cose-js |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |
| `distilled/normative.md` | 323 verbatim statements, 31 fences, **all 23 tables** |
| `distilled/requirements.yaml` | 222 entries — 101 stated, 121 inferred |
| `distilled/schema/` | 1 verbatim (§5.2's CDDL) + 4 derived |
| `distilled/messages.yaml` | 56 structures, 300 fields, all 43 code points |
| `distilled/examples/` | 6 vectors — see *Limits* |
| `distilled/state-machine.yaml` | two machines, both `derived: true` |
| `distilled/design-notes.md` | the export path under MD-3, and five named cuts |

**FX-1 under #39 (Tier 1): passes 1 and 2 of 3 complete**; cross-check has not
run, so nothing here carries a profile and nothing may be built on it.
`distilled/README.md` states the artifact set and which passes have run.

*(This paragraph has now been wrong in both directions. #42 wrote "No
`distilled/`", true then and false the moment the record was scaffolded — the
stale-absence defect library#70 fixed on three other records. The replacement
said the directory held only TODO templates, which went stale the moment pass 1
landed. The fix for a line that keeps going stale is to state what is there and
date it, which is what the table above does.)*

## Limits

*The first four come from the FX-1 extraction rather than from reading.*

- **It prints no cryptographic test vectors at all.** Not one key, signature,
  MAC, ciphertext, nonce, derived key, `COSE_Key` or `COSE_KDF_Context`, for
  any of its **43 algorithm code points**. Verified hard across all 2444
  lines: four `0x` literals in total, zero `h''` byte strings, zero base64,
  zero runs of eight or more hex characters, zero PEM. §1.5 points instead at
  `github.com/cose-wg/Examples` **commit 3221310 of 3 June 2020** —
  informative, pinned 26 months before publication, digest unrecorded.
- **A conformance checker built from the BCP 14 keywords misses the hardest
  rules.** The ECDSA curve restriction ("working only with"), the EC2
  key-type requirement ("requires"), the AES-GCM 96-bit nonce ("fixes") and
  128-bit tag ("is fixed at"), the AES-CBC-MAC all-zero IV ("is fixed to"),
  the `COSE_KDF_Context` AlgorithmID ("required to be present") and the
  fresh-IV rule ("must") are **every one of them lowercase prose**. They are
  held as `inferred` requirements naming the phrase that carries the force.
- **It allocated exactly one code point.** §10 re-points the registries from
  RFC 8152; §10.2 adds a single row — `IV-GENERATION` = 34, Recommended No. So
  42 pre-existing plus 1 is the 43. This document is the citation of record
  for 42 code points it did not allocate: cite the registry for the number and
  §2.1/§2.2 for the constraint.
- **A `MUST NOT` rests on an informative reference.** §4.1.1's "MUST NOT
  exceed 2^32 [SP800-38D]" cites a tag listed in §12.2 **Informative**
  References, while the identical NIST SP 800-38D also appears as `[AES-GCM]`
  in §12.1 Normative under a different URL — and only the normative listing
  carries the DOI. Separately, §12.2's `[SP800-56A]` is cited as "Revision 3"
  with a Revision 3 DOI but a URL pointing at **r2**, and §5.2 bases the whole
  context structure on it.
- **It is Informational, and that is genuinely odd.** RFC 9052 — the structures
  — is Standards Track; RFC 9053 — the algorithms you must implement to
  interoperate — is not. A reader inferring standing from the companion
  document will get this wrong, which is precisely the mistake
  `library/CLAUDE.md` warns about: an RFC being an RFC does not make it a
  standard. `maturity` here is `informational` on the document's own say-so.
- **Read it with RFC 9864 or implement under-specified identifiers.** RFC 9053
  is **updated by RFC 9864**, which the library holds. Neither document is
  complete alone.
- **`EdDSA` is a single code point for two curves.** `alg` -8 covers both
  edwards25519 and edwards448; the curve is carried in the key's `crv`
  parameter, not the algorithm identifier. A verifier that dispatches on `alg`
  alone does not know which curve it is about to use — contrast `rfc-9964`,
  where ML-DSA-44/65/87 each get their own code point. The newer design is the
  better one, and anything naming a principal by `alg`-inclusive thumbprint
  inherits this ambiguity for EdDSA keys.
- **Pure EdDSA only.** §2.2 admits only pure EdDSA, excluding HashEdDSA, on the
  grounds that COSE does not expect extremely large contents and the whole
  message must be held in memory anyway. The same refusal recurs for
  HashML-DSA in `rfc-9964` §7.2 — **COSE consistently excludes pre-hash
  variants**, and a design that assumes a pre-hash path exists will not find
  one.
- **The symmetric half is held here and nowhere else.** AES-GCM, AES-CCM and
  ChaCha20/Poly1305 get their COSE code points in §4, but the library holds
  **none** of the underlying specifications — no FIPS 197, no SP 800-38C/D, no
  RFC 8439. This record names the algorithms; nothing in the library yet says
  what they are. That gap is the symmetric/AEAD section of #8.
- **It predates post-quantum entirely.** August 2022. Nothing here is
  quantum-resistant, and the extension point is `rfc-9964`, not this document.
