---
schema: "library-summary/v1"
id: tcg-tpm-2-0-library-185
record: tcg-tpm-2-0-library-185
type: summary
updated: "2026-11-03"
---

# Trusted Platform Module 2.0 Library, Version 185

|  |  |
|---|---|
| **Type** | spec (TCG TPM Work Group; Part 0 Introduction, Part 1 Architecture, Part 2 Structures, Part 3 Commands, and Errata v1) |
| **Maturity** | `standard`. Every part's cover reads "TCG Published", dated March 12, 2026, which is TCG's final ratified state. It is not an ISO/IEC 11889 edition (`iso-iec-11889-2015` is the ISO track) |
| **Authors** | Trusted Computing Group, TPM Work Group. Per the press release, Chris Fenner co-chairs the Work Group, and Part 0's acknowledgements list contributors to the 185 reference code |
| **Published** | 2026-03-12 (covers). The press release is dated 2026-03-22. Errata v1 change history: "2026/02/10 Initial version", published 2026/03/12 |
| **Identifier** | `TPM_SPEC_VERSION` 185, family "2.0", level 00 (Errata §2.1). Supersedes Version 184 |
| **Source** | https://trustedcomputinggroup.org/resources/documents/tpm-library-specification (PDF links for each part are listed there) |
| **Digest** | Part 1 `sha256:c2604f79…` (`content`). Parts 0, 2, 3 and Errata digests are in `record.yaml` `content.note`. All fetched 2026-11-03 |

**What this record's URL used to be.** The stub pointed at TCG's press release, *"New spec implements PQC measures to mitigate quantum attacks"* (2026-03-22). That is an announcement, not the specification. The specification PDFs turned out to be openly downloadable from TCG's library-specification page, so they were fetched and this record now cites them. The press release was also fetched and is cited only where it adds something.

## Overview

Version 185 is the release that puts NIST's post-quantum algorithms into the TPM. Part 0's change history (§2, "Version 185") lists the additions:

- ML-DSA, HashML-DSA and ML-KEM
- EdDSA, HashEdDSA and DHKEM
- four sequenced signing commands (`TPM2_SignSequenceStart/Complete`, `TPM2_VerifySequenceStart/Complete`) for messages of arbitrary size
- two digest-signing commands (`TPM2_SignDigest`, `TPM2_VerifyDigestSignature`) that replace the now-deprecated `TPM2_Sign` and `TPM2_VerifySignature`
- KEM commands (`TPM2_Encapsulate`, `TPM2_Decapsulate`)

It also reframes the restricted-decryption "secret sharing" used by credential activation, duplication and salted sessions as a **Labeled KEM**, with RSA, ECC and ML-KEM instances (Part 1 §47.4, Figure 24). Part 0 §3.1.3.5 states the reason for the command redesign: the new commands "were introduced in order to accommodate post-quantum algorithms". Pure ML-DSA signs a message, not a caller-supplied digest, and the old digest-in, signature-out command shape could not carry it.

**What it contributes to the post-quantum question** ("which attestation systems have a stated post-quantum path, and which have a gap"): the TPM now has a **stated, specified PQ path for its core attestation chain**, with named gaps.

*Path.*
- An ML-KEM key is a first-class object (Part 1 §47; Part 2 Table 205: ML-KEM-512, ML-KEM-768 and ML-KEM-1024). It can act as the restricted decryption key behind the `"IDENTITY"` label (Part 1 §47.4), which is the credential-activation step a privacy CA uses to bind an attestation key to an endorsement key.
- An ML-DSA key is a first-class signing object (Part 1 §46; Part 2 Table 208: ML-DSA-44/65/87). Errata §2.6–§2.8 fix how `TPM2_Quote` and `TPM2_NV_Certify` behave when the signing key's scheme has no hash. So restricted ML-DSA attestation keys signing `TPMS_ATTEST` are an intended use.
- Keys are stored and exported as seeds: 32 bytes for ML-DSA, 64 bytes (*d*‖*z*) for ML-KEM (Part 1 §46.2, §47.2).
- Pure ML-DSA, with the optional external-μ mode, and HashML-DSA are both available. Support is advertised through `TPM_PT_ML_PARAMETER_SETS` (Part 2 §8.13, Table 47).

*Gaps.* These are listed under Limits: no PQ anonymous attestation, no hybrid or composite scheme, the EK certificate profile not shown to cover ML-KEM, no public reference code, and several text defects in the new v185 clauses (PQ and sequenced-signing).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines the hardware root of trust for reporting, and what an attestation signature covers (Part 1 §28; Part 3 §18) |
| Cryptography | `core` | Specifies key representation, parameter sets, signing modes and the Labeled KEM construction for ML-DSA and ML-KEM (Part 1 §46–§47; Part 2 §11.2.6–§11.2.7, §12.2.3.6–§12.2.3.8) |
| This project | `none` | ARCH-0001 has no device-attestation requirement. This record is held for the PQ-migration survey, not a decision |

**Bears on no `DEC-*` or `R-*` yet.** The nearest miss is R-O-01, *issuer key specifiable as `KeyId`*. A TPM names every key by a digest of its public area, and `TPMS_ATTEST.qualifiedSigner` carries that Qualified Name (Part 1 §28.2, Table 38). That is prior art for issuer-by-key-digest. But a TPM attestation is not a signed object of ours, so it informs no requirement and is not claimed. If m-of-n ever accepts TPM quotes as `ArtifactStatement` evidence (an R-I-01 mapping), this record becomes relevant.

**Relations.** `supersedes: tcg-tpm-2-0-library-184` (v185 replaces v184 on the same line). `see_also: iso-iec-11889-2015`, the ISO/IEC track of the same library at an older version. FIPS 203, FIPS 204, FIPS 186-5 and RFC 8032 are recorded under `cites` (Part 1 references), not repeated as relations.

## Implementations

**Searched 2026-11-03** (web search; GitHub API for tags, PRs, licences).

| Name | Kind | License | URL |
|---|---|---|---|
| wolfTPM (client and fwTPM) | open source | dual GPL/commercial per wolfSSL (not checked against LICENSE) | https://github.com/wolfSSL/wolfTPM |
| TCG TPM 2.0 reference implementation | open source (reference) | TCG reference-code licence | https://github.com/TrustedComputingGroup/TPM |
| libtpms / swtpm | open source | BSD-style | https://github.com/stefanberger/libtpms |
| tpm2-tss | open source (TSS) | BSD-2-Clause | https://github.com/tpm2-software/tpm2-tss |

- **wolfTPM is the only v185 PQC implementation we could confirm.** PR #445, "Add TPM 2.0 v1.85 PQC (ML-DSA and ML-KEM) and fwTPM PQC Support", was merged 2026-04-29, and releases 4.1.0 and 4.2.0 followed. We did not build or test it.
- **TCG's public reference code has no v185.** Its GitHub tags on 2026-11-03 are `V183` and `V184` only. wolfSSL says the same; we confirmed only the tag list.
- **Not determined:** whether libtpms or tpm2-tss carry v185 PQC types.
- **No hardware.** The search found no shipping TPM silicon with ML-DSA or ML-KEM. Vendors were not individually checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, all five PDF digests, relations (`supersedes: tcg-tpm-2-0-library-184`), implementations survey |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec` record at the summary bar for issue #45's PQ calibration batch. A full FX-1 extraction of a roughly 1,000-page, four-part library specification is a large job of its own. It would be owed when one is wanted, and **it needs its own issue**. None owns it yet. The `.cache/` copies of the PDFs and press release are local and gitignored.

## Limits

**Read scope: partial, and this is the honest boundary.** Read in full: Part 0 (41 pp) and the Errata (10 pp). Read in Part 1: §11.2, §24.5.3.6–§24.5.3.7, §28, §29.4.5, §45.2.2.3–§45.2.2.5, §46, §47 and the references. Read in Part 2: §8.13, §11.2.6–§11.2.7, §12.2.3.6–§12.2.3.8, and the algorithm-ID rows. Read in Part 3: §18.1, §20.1, §20.7.1, and the existence and numbering of §17.5–§17.6. Text was extracted from the PDFs, which loses spacing but not content. Nothing else in Parts 1–3 was read. Any claim here outside those clauses is not made.

**Gaps for the PQ question.**
- **No post-quantum anonymous attestation.** The only anonymous scheme named for attestation is `TPM_ALG_ECDAA` (Part 1 §28.5). It is pairing-based and has no PQ counterpart in v185. A PQ attestation from a v185 TPM therefore discloses the signing key's Qualified Name.
- **No hybrid or composite signature or KEM.** Algorithm agility is by separate keys per algorithm from the same primary seed (Part 1 §11.2). A classical and a PQ attestation are two keys and two signatures, and the spec offers no binding between them. Contrast `draft-ietf-lamps-pq-composite-sigs`.
- **EK certificates are out of this document.** Part 1 cites the EK Credential Profile as ref [12], the December 2024 edition, which predates v185. We did not read it, and do not know whether an ML-KEM EK template or certificate profile exists there. The press release's "ML-KEM (including Endorsement Keys)" is a claim about the library primitives. A relying party also needs a manufacturer-issued EK certificate, and the trust in that certificate is a separate PQ question.
- **Restricted ML-DSA keys cannot sign external digests.** Part 3 §20.7.1 notes there is "currently no way to produce a TPMT_TK_HASHCHECK for ML-DSA". Restricted-key signing of non-attestation data, such as a CSR, goes through the sequence commands instead. Errata §2.5 adds that an external-μ verification ticket is not useful to `TPM2_PolicyAuthorize`, and that returning a NULL ticket is preferable.
- **No public reference code, and no shipping hardware found** (see Implementations).

**Source defects found while reading.** None of these is corrected in Errata v1.
1. **External μ is "64-byte" in one part and "512-byte" in another.** Part 1 §46.3 says the digest is interpreted as "the 64-byte external Mu (𝜇) value". Part 2 §12.2.3.6, Table 230 (`allowExternalMu`), says "the 512-byte external Mu (𝜇) value". FIPS 204's μ is 64 bytes (512 bits), so Part 2 is wrong: bits written as bytes.
2. **A command that does not exist.** Part 1 §45.2.2.3 (sequenced signing with SM2), step 1, calls `TPM2_SignVerifySequenceStart()`. The press release also names "SignVerifySequenceStart". Part 2's command codes and Part 3 §17.5–§17.6 define two separate commands, `TPM2_SignSequenceStart` and `TPM2_VerifySequenceStart`.
3. **Verification sequences.** Part 1 §45.2.2.3 (the same SM2 clause) has `TPM2_SequenceUpdate()` called "zero or more times" (step 2), and step 3 says `TPM2_VerifySequenceComplete()` "is called with remainder of the message data M". Part 1 §29.4.5.2 says that command "does not allow passing additional data into the sequence", so `TPM2_SequenceUpdate` must be used at least once. The two clauses disagree, and §29.4.5.2 is consistent with Part 3.
4. **Attestation signing is described as hash-then-sign.** Part 1 §28.1 says the attestation block "is then hashed and signed". For pure ML-DSA and EdDSA keys this is at best loose. Errata §2.6–§2.8 had to patch the Quote and NV_Certify digest rules for schemes with no hash, and §28.1 itself was not updated.
5. **`TPMU_SIG_SCHEME` omits the ML-DSA cases.** Errata §2.3 records this (interpret as `TPMS_EMPTY`). It is listed here because the errata is explicitly non-normative (Errata §1) until a later version adopts it.

These are inconsistencies inside one release. They are not set as `contradicts`, which is for incompatible claims between records.

**Parameter tables checked.** The ML-KEM and ML-DSA key, ciphertext and signature sizes in Part 2 Tables 205 and 208 agree with FIPS 203 and FIPS 204. ML-KEM-512: encapsulation key 800, ciphertext 768. ML-DSA-44/65/87: public key 1312/1952/2592 and signature 2420/3309/4627.
