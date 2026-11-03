---
schema: "library-summary/v1"
id: rfc-8391
record: rfc-8391
type: summary
updated: "2026-11-03"
---

# XMSS: eXtended Merkle Signature Scheme

|  |  |
|---|---|
| **Type** | rfc (IRTF CFRG, from `draft-irtf-cfrg-xmss-hash-based-signatures-12`) |
| **Maturity** | `informational`: Category Informational on the title page; INFORMATIONAL in the RFC Editor metadata, checked 2026-11-03. An IRTF document, so not a candidate for any Internet Standard level (Status of This Memo) |
| **Authors** | A. Huelsing (TU Eindhoven), D. Butin (TU Darmstadt), S. Gazdag (genua), J. Rijneveld (Radboud), A. Mohaisen (UCF) |
| **Published** | 2018-05 |
| **Identifier** | RFC 8391 · DOI 10.17487/RFC8391 · no updates, updated_by or obsoleted_by |
| **Source** | https://www.rfc-editor.org/rfc/rfc8391.txt |
| **Digest** | `sha256:1c9af7d6…` (full value in `record.yaml`), fetched 2026-11-03 |
| **Errata** | 13 reports: 9 Verified, 3 Held for Document Update, 1 Rejected, checked 2026-11-03 |

## Overview

RFC 8391 specifies three hash-based signature schemes: the one-time scheme WOTS+ (§3.1), the single-tree many-time scheme XMSS (§4.1), and the multi-tree XMSS^MT (§4.2). Its argument is that a signature can be made secure against quantum adversaries with no assumption beyond properties of a hash function. §9.2 calls the assumptions "minimal" because any signature over arbitrary-length messages already needs a hash, and §9.1 says collision resistance is not even required. The price is **state**. Each XMSS key is a Merkle tree over 2^h one-time keys, and the private key carries an index that moves forward on every signature (§4.1). §1.1 carries the CFRG warning that if a state is used twice, "no cryptographic security guarantees remain". It also says the signing API must be able to return an updated secret-key state, so classical signature APIs cannot be used unmodified. §4.1.9 requires that the private key be updated before the signature is output.

For the topic question this is the **supply side of the stateful post-quantum path**. It is a complete, interoperable algorithm with an IANA registry (§8) and a 32-bit type code at the head of every key and signature (§6). It contains no deployment, trust or migration machinery of its own: no private-key format (§4.1.7 says so explicitly), no state-management protocol, and no hybrid or transition mode. Systems that cite XMSS as their post-quantum path inherit the state problem and have to solve it themselves.

## What it says about post-quantum security, by locator

- **§1.1, CFRG note.** The schemes are ready "for experimentation and further engineering development". CFRG is "confident in the cryptographic security … against quantum computers", conditional on developers preventing state reuse.
- **§5 and §6, security levels.** REQUIRED parameter sets are SHA2-256 only: h ∈ {10, 16, 20} for XMSS (Table 2), and total heights of 20, 40 and 60 split across d layers for XMSS^MT (§5.4). Implementations are only required to *verify* the REQUIRED sets (§5). §6 justifies SHA2-256 as giving 128 bits of security against quantum-computer-aided attacks.
- **Verified erratum 6024 corrects §5.** As printed, §5 claims that n = 32 gives 256-bit classical and 128-bit post-quantum security for every set. The erratum (Verified 2020-06-23) restricts that claim to SHA2. It says the SHAKE sets give 128 classical / **86** post-quantum bits at n = 32, and 256 / 170 at n = 64. A reader who takes §5 at face value credits the n = 32 SHAKE sets with 128 post-quantum bits where the erratum gives 86.
- **§9.3.** For post-quantum security, n must be twice the classical size because of Grover's algorithm. The hash should be retired as soon as a dedicated quantum attack beats the generic one.
- **§4.1.12, partial keys.** Applications MAY split or copy private keys, for example for load balancing or "delegation of signing rights", using their own formats, but MUST guarantee that each index signs only one message. This is the only place the RFC touches distribution, and it pushes the whole problem to the application.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The security model is total failure on state reuse (§1.1), and §4.1.9 orders the state commit before the signature is released |
| Cryptography | `core` | Defines the primitives, parameter sets, security estimates (§5, §9) and wire formats (Appendices A–C) |
| This project | `adjacent` | A candidate post-quantum signature for long-lived roots. ARCH-0001 NG3 defers the algorithm-suite freeze, so this is evidence for that choice, not a selection |

- **R-O-01** ("Every signed object SHALL have an issuer key that can be specified as `KeyId`"): under XMSS each signed object consumes one leaf of a finite tree, and Table 3 gives 2^10 to 2^20 signatures per key. An issuer key is therefore a counted resource. A crash between signing and committing the state is a forgery risk, not a retry (§1.1, §4.1.9). `rfc-8778` records the same finding for HSS/LMS.
- **DEC-003** ("Must specify: canonical key bytes before hashing"): Algorithm 10 in §4.1.7 gives the public key as `OID || root || SEED`. That is a fixed-width string with the IANA type code first, so a `KeyId` digest over it carries a registry allocation inside the key material. The Appendix B.3 XDR does not quite agree; see Limits.

It bears on no `DEC-*` that selects an algorithm, because ARCH-0001 §7 has none open. The cipher-suite memo (`mofn` research R-0003) has not named a post-quantum candidate.

## Implementations

**Searched 2026-11-03** (web search, plus the `sp-800-208` record's survey of 2026-09-26).

| Name | Kind | License | URL |
|---|---|---|---|
| xmss-reference | open source, reference C (§7) | CC0-1.0 | https://github.com/XMSS/xmss-reference |
| liboqs `sig_stfl` | open source, C library; signing behind a "hazardous experimental" flag | MIT | https://openquantumsafe.org/liboqs/api/doxygen/sig__stfl_8h.html |
| wolfSSL / wolfCrypt, wolfBoot | open source / commercial; verify-only build option | GPL-3.0 or commercial | https://www.wolfssl.com/ |
| Bouncy Castle | open source, Java | MIT-style | https://www.bouncycastle.org/ |
| HSMs with stateful HBS firmware | commercial | — | vendor-specific |

The pattern in these results answers part of the topic question. Libraries ship **verification** freely and gate **signing** behind flags or hardware. That matches SP 800-208's requirement, recorded in `sp-800-208`, that keys be generated and used for signing only inside hardware modules. We did not test any implementation.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This record is at the summary bar, written for the `post-quantum-migration` topic (library#45 calibration batch). RFC 8391 is an `rfc` record, so a full FX-1 extraction would be owed when one is wanted, and **it needs its own issue**. No issue owns it yet. That extraction would cover:

- the WOTS+, XMSS and XMSS^MT algorithms (Algorithms 1–16)
- BCP 14 keyword reconciliation
- the XDR of Appendices A–C, which erratum 6352 says is not machine-readable as XDR
- the IANA tables
- the errata, applied

No keyword count is given here because none has been reconciled. The `.cache/` copies of the RFC and its metadata are local and gitignored. The errata page was read live (https://www.rfc-editor.org/errata/rfc8391) and is not cached.

**Relations.** `see_also` edges, each with its reason: `rfc-8554` is the other standardised stateful hash-based family (LMS/HSS); `sp-800-208` is the NIST profile that approves a subset of these parameter sets (see Limits); `fips-205` (SLH-DSA) is the stateless scheme that §6 says this modular description was written to support (SPHINCS [BHH15]); `merkle-1979-thesis` is the origin of the hash tree XMSS builds on. `cited_by` was emptied in the verify pass: it listed `rfc-8554`, `rfc-9162` and `sp-800-208`, which are library records, and `cited_by` is for our own documents only (`docs/references.md` §2). In `mofn`, `research/0001-signatures-and-attestation` (`report.md` and `mini-reports/H-post-quantum.md`) cites RFC 8391. No id convention for those as relation targets is settled, so they are noted here, not authored as an edge.

## Limits

- **It settles the algorithm, not the deployment.** It defines no private-key format (§4.1.7) and no method for synchronising, backing up or replicating state. It says nothing about trust anchors, or about rotation when a tree is exhausted. §4.1.12 hands distribution entirely to applications.
- **No migration story.** There is nothing here on hybrids, dual signatures, or moving an existing classical key to XMSS. For the topic, a system "on XMSS" has a primitive, not a path.
- **The errata are substantial.** Four verified errata fix argument-order mismatches between function definitions and their call sites (5572, 8382, 8383, 8396). Another, 6821, fixes a wrong checksum bound: the printed `* 2^8` would have overflowed the checksum field. An implementer working from the printed text alone would hit these.
- **Source defects we found beyond the errata.**
  - §6 lists the OPTIONAL hashes as "SHA2-512, SHAKE-256, and SHAKE-512". Table 2 actually uses SHAKE128 and SHAKE256, and SHAKE-512 appears nowhere else in the document.
  - §5 and §8 spell the default as `XMSS_SHA2_20_256`, while Table 2 and the registry name it `XMSS-SHA2_20_256`.
  - On our reading, Appendix B.3's `xmss_public_key` is a struct of two XDR unions, each discriminated on the algorithm type, so it would serialise the type twice. The §4.1.7 figure and Algorithm 10 carry the OID once.

  None of these is set as `contradicts`, since each is internal to one document. They are recorded for whoever extracts it.
- **SP 800-208 approves only a subset.** According to the `sp-800-208` record, not every RFC 8391 parameter set is approved, so "we implement RFC 8391" does not mean "we conform to SP 800-208".
- **Read scope.** §1–§9 were read in full. The algorithm pseudocode (§3–§4) and Appendices A–C were read for structure, not checked line by line. All 13 errata entries were read. The signature counts and runtimes in §5 were not re-derived.
