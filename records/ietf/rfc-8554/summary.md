---
schema: "library-summary/v1"
id: rfc-8554
record: rfc-8554
type: summary
updated: "2026-11-03"
---

# Leighton-Micali Hash-Based Signatures

|  |  |
|---|---|
| **Type** | rfc (IRTF CFRG, from `draft-mcgrew-hash-sigs-15`) |
| **Maturity** | `informational`: Category Informational on the title page; INFORMATIONAL in the RFC Editor metadata, checked 2026-11-03. An IRTF document |
| **Authors** | D. McGrew, M. Curcio, S. Fluhrer (Cisco Systems) |
| **Published** | 2019-04 |
| **Identifier** | RFC 8554 · DOI 10.17487/RFC8554 · no updates, updated_by or obsoleted_by |
| **Source** | https://www.rfc-editor.org/rfc/rfc8554.txt |
| **Digest** | `sha256:d5bfdbd4…` (full value in `record.yaml`), fetched 2026-11-03 |
| **Errata** | 3: 7409 Verified, 7994 Held for Document Update, 8907 Reported; checked 2026-11-03 |

## Overview

RFC 8554 specifies the Leighton–Micali one-time signature (LM-OTS, §4), the Merkle-tree many-time scheme built on it (LMS, §5), and the Hierarchical Signature System (HSS, §6). HSS is a chain of 1 to 8 LMS trees in which each tree signs the public key of the next and the bottom tree signs messages. Its argument matches RFC 8391's: hash-only signatures with small keys and post-quantum security (§1, §1.1), proven in the random-oracle model (§9, citing [Katz16] and [Fluhrer17]). It takes a more operational line. §2 defines the interface as stateful: signing returns the next private key, or an indication that none remains. §1.1 requires the API to let the signer update the secret-key state. §9.2 explains why that is hard: an updated key must actually reach physical media through file-system and drive caches. Then it gives the RFC's one structural mitigation: keep the second-level HSS private key in RAM only, so that a crash or restart simply generates a new lower tree (Implementations SHOULD do this, §9.2).

For the topic question, LMS/HSS is the **stateful post-quantum path that deployed systems actually took**. OpenSSL 3.6 verifies it, CNSA 2.0 allows LMS for firmware and software signing but not the multi-tree HSS (`cnsa-2-0`, pp. 7–8 and p. 11), and `rfc-8778` registers HSS/LMS as COSE `alg` -46. Like RFC 8391 it is an algorithm only, with no trust, rotation or hybrid machinery.

## What it says that matters for a post-quantum path, by locator

- **Parameters are SHA-256 only, m = n = 32** (LM-OTS Table 1, LMS Table 2). The only variables are the Winternitz parameter w ∈ {1, 2, 4, 8} and tree height h ∈ {5, 10, 15, 20, 25}. The SHA-256/192 and SHAKE sets that SP 800-208 and CNSA 2.0 prefer come from later work, RFC 9858, which is not held here and not read.
- **HSS is mandatory.** *"all implementations MUST support HSS in order to maximize interoperability"* (§6). With L = 1, HSS is LMS with a level count prepended. §6 allows different levels to use different parameter sets (plain prose, not a BCP 14 keyword), but the signer MUST NOT change the parameter sets for a specific level (§6).
- **Typecodes are checked.** A verifier MUST check each typecode, and a mismatch with the public key MUST return INVALID (§9).
- **Identifier `I`** is 16 random bytes per LMS tree. Uniqueness is not required, only the absence of many collisions (§7, §9.1).
- **Key lifetime is a stated table.** §6.4 Table 3 runs from 30 seconds to 34 years at 1000 signatures per second. Verified erratum 7409 says the two-level signature sizes there are all 48 bytes too large.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Total failure on state reuse (§1.1, §2), and the most concrete treatment of state persistence of any record in this topic (§9.2) |
| Cryptography | `core` | Defines LM-OTS, LMS and HSS, their formats (§3.3), registries (§8) and test vectors (Appendix F) |
| This project | `adjacent` | A candidate signature for long-lived roots under NG3's deferred suite choice. Not selected |

- **R-O-01**: as for `rfc-8391`, every signed object consumes a one-time key irreversibly (§2, §6). §9.2 adds a structural cost. Under the RAM-only mitigation each restart consumes a top-level leaf to sign the new lower tree. This is our derivation from §6 and §9.2; the RFC does not state it. So the budget of a key depends on how often the signer restarts, not only on how much it signs.
- **DEC-003**: §5.3 gives the LMS public key as `u32str(type) || u32str(otstype) || I || T[1]`, and §6.1 makes the HSS public key `u32str(L) || pub[0]`. These are the canonical key bytes DEC-003 asks for, with three IANA-registered or structural values ahead of the root hash. `rfc-8778`'s DEC-002/DEC-003 analysis depends on these lines. Its cross-check pass named three RFC 8554 facts as unverifiable from the stub: that `u32str` is four bytes (§3.1), that Appendix B gives p = 67 for w = 4 and p = 34 for w = 8, and that Appendix F prints LMS public keys. All three are confirmed against the fetched text.

## Implementations

**Searched 2026-11-03.**

| Name | Kind | License | URL |
|---|---|---|---|
| cisco/hash-sigs | open source, C (the §6.4 measurement code) | BSD-3-Clause (`license.txt`) | https://github.com/cisco/hash-sigs |
| OpenSSL 3.6+ | open source; **verify only**, `enable-lms` | Apache-2.0 | https://docs.openssl.org/3.6/man7/EVP_SIGNATURE-LMS/ |
| liboqs `sig_stfl` | open source; signing behind an experimental flag | MIT | https://openquantumsafe.org/ |
| wolfSSL / wolfCrypt, wolfBoot | open source / commercial | GPL-3.0 or commercial | https://www.wolfssl.com/ |
| Botan (`hss_lms`) | open source, C++ | BSD-2-Clause | https://botan.randombit.net/ |
| Bouncy Castle | open source, Java | MIT-style | https://www.bouncycastle.org/ |
| HSMs with stateful HBS firmware | commercial | — | vendor-specific |

The search result is itself a data point for the topic. OpenSSL's LMS man page says verification-only is an SP 800-208 requirement for FIPS software modules, and steers new deployments to ML-DSA or SLH-DSA. The page labels the link "RFC 8554" but points it at `datatracker.ietf.org/doc/html/rfc8854`, the wrong RFC (checked in the verify pass, 2026-11-03).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This record is at the summary bar for the `post-quantum-migration` topic (library#45). RFC 8554 is an `rfc` record, so FX-1 is owed when extraction is wanted. `rfc-8778`'s cross-check called these facts *"the strongest argument for extracting RFC 8554"*, but **no issue owns that extraction yet**. Fetching the `.txt` with a digest removes the blocker that record named, which was an empty `content.sha256` and an HTML URL. An extraction would cover the §3.3 XDR, Tables 1–2, Algorithms 0–8 (with 4a/4b and 6a), keyword reconciliation, the Appendix F test vectors, and the three errata. No keyword count is given here.

**Relations.** `see_also: sp-800-208`, the NIST profile that approves a subset of LMS/HSS and adds the hardware-module requirement. The `rfc-8391` and `rfc-8778` edges are authored on those records (`see_also` is symmetric and derived, `docs/references.md` §2). `cited_by` was emptied in the verify pass: it listed library records (`rfc-8778`, `sp-800-208`), and `cited_by` is for our own documents only. In `mofn`, `research/0001-signatures-and-attestation` cites RFC 8554.

## Limits

- **Algorithm only.** No private-key format, no state backup or replication, and nothing on trust anchors or on what happens when the top tree is exhausted. §9.2 calls attention to the persistence problem and explicitly declines to give complete guidance.
- **No migration or hybrid mode.** Nothing on pairing LMS with a classical signature or on moving a deployed key to it.
- **Parameter coverage is narrow and dated.** SHA-256/32 only. The truncated and SHAKE sets that later policy prefers are elsewhere, in RFC 9858, which is not held.
- **Source defects.**
  - Table 3 signature sizes for two-level HSS are wrong by 48 bytes (erratum 7409, Verified).
  - §3.3 names LMS sets `n32` where §5 and IANA use `m32` (7994, Held).
  - The Appendix F Test Case 1 comment reads `LM_SHA256_M32_H5` for `LMS_SHA256_M32_H5`.
- **We think erratum 8907 is mistaken.** It claims the §3.3 `lms_key_n32` struct omits the LMS type, so the encoding would not match §5.3. On our reading, `lms_public_key` is an XDR union switched on `lms_algorithm_type`, and XDR encodes the discriminant ahead of the arm. The encoding is therefore already `type || otstype || I || K`, which matches §5.3. Recorded as our reading; the erratum is still only Reported.
- **Read scope.** §1–§10 were read in full. The algorithm pseudocode in §4–§6 was read for structure. The Appendix F vectors were not executed.
