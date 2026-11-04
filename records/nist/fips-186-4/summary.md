---
schema: "library-summary/v1"
id: fips-186-4
record: fips-186-4
type: summary
updated: "2026-11-03"
---

# Digital Signature Standard (DSS), FIPS 186-4

|  |  |
|---|---|
| **Type** | spec (Federal Information Processing Standard) |
| **Maturity** | `historic`: **withdrawn 2024-02-03**, superseded in its entirety by FIPS 186-5. Verified on the CSRC landing page and the PDF's withdrawal notice, 2026-11-03. The schema has no `withdrawn` value |
| **Authors** | National Institute of Standards and Technology (Information Technology Laboratory) |
| **Published** | 2013-07-19 (withdrawal notice). Title page: "Issued July 2013" |
| **Identifier** | FIPS 186-4 · DOI 10.6028/NIST.FIPS.186-4 · supersedes FIPS 186-3 (2009-06-25) |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf |
| **Digest** | `sha256:081dcccb…` (full value in `record.yaml`), fetched 2026-11-03. These are the bytes NIST serves today, **with the 2024 withdrawal page prepended** |

## Overview

FIPS 186-4 approves three signature techniques for US federal use (§1). It specifies **DSA** itself, in §4 and Appendices A–B. It approves **RSA** as specified in ANS X9.31 and PKCS #1, with extra requirements (§5). It approves **ECDSA** as specified in ANS X9.62-2005, with extra requirements and the NIST recommended curves P-, K- and B- of Appendix D (§6). Its argument is that a signature only proves something once the verifier also has *assurances*. These are domain-parameter validity, public-key validity, the signatory's possession of the private key, and a binding of the owner's identity to the public key (§3, §3.1–§3.3, delegated in method to SP 800-89). Without them, §3 says, forgery *"is reduced to the problem of falsely claiming an identity"*. Sizes are fixed lists. DSA (L, N) is one of 1024/160, 2048/224, 2048/256 or 3072/256 (§4.2). The RSA modulus is 1024, 2048 or 3072 bits (§5.1). ECDSA uses five ranges of *n* with maximum cofactors (§6.1.1, Table 1). Hashes come from FIPS 180.

The standard is withdrawn. FIPS 186-5 (2023-02-03) superseded it, with a one-year transition under 186-5's Implementation Schedule clause 12, and the withdrawal took effect 2024-02-03. Per `fips-186-5`, the material change was dropping DSA for signature generation (kept for verification only) and adding EdDSA.

## What it contributes to "which attestation systems have a stated post-quantum path?"

**A clean negative, from the base layer.** Every technique it approves rests on factoring (RSA) or discrete logarithms (DSA, ECDSA). `shor-1997` §5–§6 breaks both families directly, and its cited generalisation breaks the elliptic-curve case. The word "quantum" does not occur in the 2013 text. The threat model, where one is stated, is classical. Appendix F.3, on generating primes for RSA signatures, says that *"For an adversary with overwhelming resources, the best all-purpose factoring algorithm is assumed to be the General Number Field Sieve"*. The only future-proofing is procedural. Item 15 of the announcement says the standard *"will be reviewed every five years"*. The post-quantum path for this line did not come as a 186 revision: `fips-186-5` is also classical only. It came as separate standards, `fips-204` (ML-DSA) and `fips-205` (SLH-DSA), with `sp-800-208` for stateful hash-based signatures. The deprecation and disallowance dates for the 186 algorithms are in `nistir-8547`. Any attestation system whose signature suite is exactly "FIPS 186-4 algorithms" therefore has a gap by construction.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §3's assurance model (identity binding, possession, key validity) is the security argument. The rest is algorithm specification |
| Cryptography | `core` | Normative for DSA, and for the approved profiles of RSA and ECDSA, until 2024 |
| This project | `none` | Withdrawn. Anything we adopt from this line comes from `fips-186-5` |

**Bears on none.** Any requirement this line informs is carried by the current version: `fips-186-5` records R-M-02 and R-O-05. Citing the withdrawn version against a live requirement would point the reader at superseded text. One tension is worth recording for whoever writes the R-M-02 rationale. §3 says *"A binding of an owner's identity and the owner's public key shall be effected"* to obtain assurance of the signatory. ARCH-0001 R-M-02 lets a principal be the key alone. Whether 186-5 keeps that sentence was not checked here.

## Implementations

**Searched 2026-11-03.** Every mainstream library implements the 186-4 algorithms, because 186-5 kept RSA and ECDSA. What sets an implementation apart is whether it still offers **DSA generation**.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org (DSA, RSA incl. X9.31 padding, ECDSA) |
| Go `crypto/ecdsa`, `crypto/rsa`, `crypto/dsa` | open source | BSD-3-Clause | https://pkg.go.dev/crypto (`crypto/dsa` deprecated, no binary curves) |
| python-cryptography | open source | Apache-2.0 / BSD-3-Clause | https://cryptography.io |
| CMVP-validated modules (historic 186-4 validations) | commercial | — | https://csrc.nist.gov/projects/cryptographic-module-validation-program |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, withdrawal evidence in `content.note`, `supersedes: fips-186-3`, implementations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec` record at the summary bar for m-of-n/library#45. No issue owns an FX-1 extraction of it, and none should be opened. A withdrawn standard superseded in its entirety is the wrong target, and the extraction belongs on `fips-186-5`. The trigger for reconsidering is a need to verify legacy DSA or B-/K-curve signatures against the exact 2013 requirements. The `superseded_by` edge to `fips-186-5` is not authored here: `fips-186-5` holds `supersedes: fips-186-4`, and `bin/reindex` derives the inverse (`docs/references.md` §2). The PDF is in `.cache/` and is not committed.

## Limits

- **Withdrawn.** Nothing here is approved for new federal signature generation. Use `fips-186-5`, and `fips-204`/`fips-205` for post-quantum.
- **Normative content is mostly elsewhere.** RSA lives in ANS X9.31 and PKCS #1, ECDSA in ANS X9.62-2005, and the assurance methods in SP 800-89. This record holds none of those (`sp-800-57pt1r5` is held, for security strengths).
- **The digest is of today's bytes, not 2013's.** The prepended withdrawal page means this digest will not match a 2013 copy.
- **Source defects, minor.** §4.2 reads *"shall generate digital signatures using use one or more of these choices"*, with a doubled verb. Appendix D.1.1.2 says *"Table E-1 provides the bit lengths of the various underlying fields"*, but the table that follows is Table D-1. §6.1.1 footnote 2 concedes that the recommended curves were generated with SHA-1, and keeps them approved because SHA-1 *"will only be used to validate those curves"*.
- **Read scope.** The announcement, §1–§6 and the openings of Appendices D and F, plus D.1.1.2 and F.3, were read. The algorithmic Appendices A–C and D.2–D.10 (prime generation, primality tests, curve arithmetic) were checked for structure only. No count of shall statements was reconciled. Roughly 200 occurrences of "shall" appear in the extracted text (202 or 212, depending on the PDF extractor), and that is not a requirement count.
