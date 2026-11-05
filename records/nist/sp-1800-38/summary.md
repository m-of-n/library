---
schema: "library-summary/v1"
id: sp-1800-38
record: sp-1800-38
type: summary
updated: "2026-11-03"
---

# SP 1800-38: Migration to Post-Quantum Cryptography

|  |  |
|---|---|
| **Type** | spec (NIST SP 1800-series practice guide, NCCoE), multi-volume |
| **Maturity** | `draft`: every volume is a "Preliminary Draft" (CSRC, checked 2026-11-03). No final exists |
| **Authors** | W. Newhouse, M. Souppaya (NIST), W. Barker (Dakota Consulting), C. Brown (MITRE). Vols B and C add consortium authors |
| **Published** | Vol A 2023-04-24 (updated 2023-05-02). Vols B and C December 2023 (comments closed 2024-02-20) |
| **Identifier** | NIST SP 1800-38A, 1800-38B, 1800-38C (preliminary drafts) |
| **Source** | https://www.nccoe.nist.gov/sites/default/files/2023-04/pqc-migration-nist-sp-1800-38a-preliminary-draft.pdf |
| **Digest** | `sha256:b0654d3a…` (Volume A. Full value, plus the B and C digests, in `record.yaml`), fetched 2026-11-03 |

## What was read, exactly

The record URL is CSRC `…/sp/1800/38/iprd`, the April 2023 landing page for **Volume A: Executive Summary** (5 pp.). CSRC says that page was *"Obsoleted on December 19, 2023"* by `…/iprd-(1)`, which carries three PDFs: the **same** Volume A file, **Volume B** *"Quantum Readiness: Cryptographic Discovery"* (Approach, Architecture, and Security Characteristics of Public Key Application Discovery Tools, 68 pp.), and **Volume C** *"Quantum Readiness: Testing Draft Standards"* (Quantum-Resistant Cryptography Technology Interoperability and Performance Report). The digest is of Volume A. Volume A was read in full. Volume C was read at §3, §8, §10 and Appendix C. Volume B was read only to the TOC and front matter. No later version was found (see `record.yaml` note). A 2025 NCCoE slide deck surfaced by search speaks of consolidating the volumes into one SP 1800-38 on pages.nist.gov. We could not confirm that this happened.

## Overview

The guide does not set policy. It is an NCCoE consortium project of about 20 vendors plus NSA (Vol A, "Collaborators"), with two workstreams. The first is **discovery**: tools that find where quantum-vulnerable public-key cryptography is used, in CI/CD pipelines, network traffic and end-host libraries, and feed that into risk-based prioritisation (Vol A "Solution", Vol B). The second is **interoperability and performance testing** of the then-draft algorithms in TLS 1.3, SSH, QUIC, X.509 and HSMs (Vol A "Outcome", Vol C). The argument is that migration is bottlenecked on inventory and interoperability, not on algorithms. The new algorithms *"will likely not be drop-in replacements"* (Vol A "Challenge"). Vol C's headline is that core TLS/SSH integration was largely unproblematic: it gives *"confidence that migrating to the new PQC standards will be straightforward for most implementations"* (Vol C §10).

## Answer to the topic question

*Which attestation systems have a stated post-quantum path, and which have a gap?* The guide contributes three things.

1. **X.509 has many candidate paths and no settled one** (Vol C §8). It tested pure-PQC certificates and several hybrid formats (§8.1.2). Its lessons list interest in composite keys and signatures, Chameleon delta certificates, RelatedCertificate, Catalyst alt-signature extensions, and SIA discovery (§8.4). That is evidence of plurality, not of a path.
2. **Firmware and code signing, where attestation roots live, was out of scope.** Vol C §3.3: *"The participants also chose to exclude firmware signing and IoT uses"*. The volume that tests interoperability is silent on the attestation-heavy cases.
3. **Signing whole messages versus pre-hashing** (Vol C Appendix C). Dilithium, Falcon and SPHINCS+ (the pre-FIPS forms Vol C tested) bind the digest step to the key operation, so the hash-then-sign split of RSA/ECDSA no longer exists. The appendix finds that *"most use-cases can leverage post-quantum signatures as they are without pre-digesting"*, and that pre-digesting remains possible *"for uses which can offer a protocol-level signature envelope"*. It also notes PKCS#11 streaming problems for Falcon and SPHINCS+ (C.5.1) and the large-message case for firmware and documents (C.5.2). This is directly relevant to statement formats, which already sign an envelope containing a content digest.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Inventory methodology and interop findings, with no threat analysis beyond HNDL framing |
| Cryptography | `adjacent` | Tests draft-era algorithms (CRYSTALS-Dilithium, Falcon, SPHINCS+, Kyber; Vol C §3.1), not the FIPS versions |
| This project | `adjacent` | Appendix C bears on what our signer feeds to the signature primitive |

- **R-O-05**, proposed in mofn `spec/ARCH-0001-PROPOSAL-v0.2.0.md` §6, not yet in ARCH-0001 (signed payload is the canonical encoding verbatim, with an authenticated type indicator). Vol C Appendix C's finding, that PQ signatures should take the whole message and pre-hashing belongs in a protocol envelope, is consistent with signing canonical bytes directly. It is also a caution: if a native statement is large (an embedded SBOM, say), R-O-05 plus ML-DSA means the signer must stream the whole payload. That is fine for ML-DSA, where tr is known up front, and harder for SLH-DSA (two passes; C.5.1). Our reading, not the guide's.
- It bears on no `DEC-*`.

**Relations.** `see_also` edges are named by the source: FIPS 203/204/205 and SP 800-208 (Vol C §3.1), the composite-signature draft (one of the X.509 formats tested, Vol C §8.1.2.4), and `nistir-8547` as the source of the dates this guide does not set.

## Implementations

**Searched 2026-11-03.** The guide is itself the record of implementations tested. Vol C §4 lists the collaborators' products. They were 2023 draft-algorithm builds, and NIST disclaims endorsement.

| Name | Kind | License | URL |
|---|---|---|---|
| liboqs / oqs-provider | open source, C | MIT | https://github.com/open-quantum-safe/liboqs |
| wolfSSL | open source / commercial, C | GPL-3.0 or commercial | https://www.wolfssl.com/ |
| Vol C HSM and toolkit collaborators (Crypto4A, CryptoNext, Entrust, Thales, Utimaco, …) | commercial | — | https://csrc.nist.gov/pubs/sp/1800/38/iprd-(1) |

Vol B's discovery tools are commercial collaborator products. Vol B was not read far enough to list them.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata. The digest note says which volumes and versions were fetched, with all three digests |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec`-typed record at the summary bar. It is a practice guide with no BCP 14 requirements. An FX-1 pass would mostly be N/A pointers plus Vol C's test matrices, and should wait for a final volume set. No issue owns it. **One record for three volumes** is deliberate, because CSRC publishes them under one SP number and one landing page. If a final is issued per volume, splitting is a judgement for then. The `.cache/` copies (`sp-1800-38.pdf` = Vol A, `sp-1800-38b.pdf`, `sp-1800-38c.pdf`) are local and gitignored.

## Limits

- **Preliminary and dated.** Every result predates FIPS 203/204/205 (August 2024). Vol C §3.1 tests the *submissions*, which `cnsa-2-0` (FAQ v2.2 p. 11) explicitly says are not the same as the standards.
- **Vol B was not read** beyond its front matter. Any claim about discovery tooling here comes from Vol A's description.
- **Mislabel in the source (minor).** Vol C §3.2 says *"the collaborators explored the topic of stateful hash-based signatures in Appendix C"*, but Appendix C is "Hash and Sign Analysis" and is about pre-hashing. Stateful HBS appear there only in a note that the analysis also applies to them (C.1, citing RFC 8554 and RFC 8391). The sentence that follows in §3.2 describes the actual content.
- **No firmware, IoT, TLS 1.2 or IKEv2 testing** (Vol C §3.3), so it says nothing about the slowest-to-migrate verifiers.
- **Not a mandate.** NCCoE practice guides carry no statutory authority. Dates and requirements come from `nistir-8547` and `cnsa-2-0`.
