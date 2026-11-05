---
schema: "library-summary/v1"
id: nistir-8547
record: nistir-8547
type: summary
updated: "2026-11-03"
---

# NIST IR 8547 ipd: Transition to Post-Quantum Cryptography Standards

|  |  |
|---|---|
| **Type** | spec (NIST Internal Report, Initial Public Draft) |
| **Maturity** | `draft`: Initial Public Draft per the CSRC page, checked 2026-11-03. **Withdrawn 27 Oct 2026**, followed by the final NIST IR 8547 (October 2026) |
| **Authors** | D. Moody, R. Perlner, A. Regenscheid, A. Robinson, D. Cooper (NIST CSD) |
| **Published** | 2024-11-12. Comments closed 2025-01-10 |
| **Identifier** | NIST IR 8547 ipd · DOI 10.6028/NIST.IR.8547.ipd |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf |
| **Digest** | `sha256:bed27fff…` (full value in `record.yaml`). Note: this is the PDF with the 2026 withdrawal notice prepended. Fetched 2026-11-03 |
| **Successor** | NIST IR 8547 final, October 2026, DOI 10.6028/NIST.IR.8547. Fetched and compared on the points below, not read in full |

## Overview

The draft is NIST's plan for retiring quantum-vulnerable public-key algorithms. It lists the vulnerable ones (§2.1: RSA, ECDSA and EdDSA under FIPS 186, and DH/MQV and RSA key establishment under SP 800-56A/B) and the replacements (FIPS 203/204/205 and SP 800-208). It anchors the schedule to NSM-10's 2035 goal (§4), and then sets a deprecation clock in §4.1. Under that clock, 112-bit-strength classical signatures and key establishment are **"Deprecated after 2030"**, and every classical public-key scheme at every strength is **"Disallowed after 2035"** (Tables 2 and 4). The draft's view of signatures is relaxed. §3.1.2 says authentication *"remains secure as long as the cryptographic algorithms and keys used to perform the authentication are secure when the authentication is performed"*, so signatures can migrate later than key establishment. The exception is code signing on devices whose verifier cannot be updated, which §3.1.1 says should require quantum-resistant signatures from the start. On hybrids, §3.2.2 defines a "dual signature" as two or more signatures that must all verify, and says existing guidance already accommodates them if at least one component is NIST-approved.

## The final (October 2026) moved the clock: this record's dates are stale

The draft is withdrawn, and the final differs on exactly the points the topic depends on. We compared these points directly in the final PDF:

- **Deprecation now covers every strength.** Final §4.1.1 and Table 2: NIST *"will instead deprecate all quantum-vulnerable digital signature algorithms after 2030 and disallow their use … after 2035"*. ECDSA and RSA at ≥112 bits and EdDSA at ≥128 bits are all "Deprecated after 2030, Disallowed after 2035". In the draft, ≥128-bit ECDSA, EdDSA and RSA had no deprecation step at all, only "Disallowed after 2035". Key establishment changed the same way (final §4.1.2).
- **Federal deadlines arrived on top of the clock.** Final §1 and §4 cite EO 14412 and OMB M-26-15. High value assets and high impact systems must use PQC for key establishment by **31 Dec 2030** and for digital signatures by **31 Dec 2031**. The final says the 2030–2035 window *"does not alter the earlier deadlines"* (§4).
- **Signatures are no longer treated as relaxed.** Final §3 adds: *"While signatures are not vulnerable to HNDL attacks, transitioning to post-quantum signatures is also urgent"*.
- **Smaller changes.** The final selects HQC as the alternative KEM, with a FIPS under development (§2.1.2), and recommends ML-KEM-768 as the default (§4.1.2). It notes that stateful HBS *"may be useful for applications like software and firmware signing"* (§2.1.1). It adds an AEAD table (Ascon, SP 800-232) and says SHA-1 is disallowed in FIPS modules after 2030 (Table 8, note 4).

**This matters for the parent project.** mofn `research/0001-signatures-and-attestation/report.md` §10.3 cites this record for *"deprecates 112-bit ECDSA and RSA after 2030 and disallows … after 2035"*. The report names the ipd explicitly, so it is accurate to what it cites, but it is stale: in the final, deprecation covers every strength. The report should move to the final.

## Answer to the topic question

*Which attestation systems have a stated post-quantum path, and which have a gap?* This document is the **yardstick, not a system**. It defines the dates that every attestation format's PQ path has to meet in the US civilian space. It also defines what NIST counts as a legitimate hybrid: a dual signature in which all components must verify and at least one is approved (§3.2.2, unchanged in the final). In SP 800-131A terms (§4.1), "legacy use" means a disallowed algorithm *"may only be used … to verify a digital signature"* on already-protected information. **For a long-lived attestation, that is the gap the document leaves open.** It permits verification after 2035 but says nothing about how a verifier then distinguishes a pre-2035 signature from a forgery. That needs timestamping or transparency evidence, which the document does not mention.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A migration policy. §3.1 has threat-model reasoning (HNDL, non-updatable verifiers) but no attacks |
| Cryptography | `core` | The authoritative list of what is vulnerable, what replaces it, and when each step happens (§4.1, Tables 2–7) |
| This project | `adjacent` | Constrains what algorithms a suite may carry and for how long. The suite memo has no requirement ID |

- **No `bears_on`.** §3.2.2's dual signature (all components must verify, one must be approved) reads to us as a 2-of-2 conjunction a threshold principal could express, but that is our inference and says nothing about R-M-06's actual subject (representing threshold principals without a CA hierarchy), so it is not recorded as bearing on it.
- The record would bear more on the parent's cipher-suite memo (`research/0003-cipher-suite/report.md`: what a suite is, and agility) than on any ARCH-0001 requirement, but that memo defines no `R-*`/`DEC-*` about algorithm lifetime. **It bears on no `DEC-*` yet.**

**Relations.** `see_also` edges are the documents this one names: the replacements (FIPS 203/204/205, SP 800-208, §2.1), the vulnerable baselines (FIPS 186-5, SP 800-56A r3, §2.1 and Tables 2/4), SP 800-57 Part 1's 2031 projection that §4.1.1 overrides, the composite-signature draft as the IETF form of §3.2.2's "composite signature", and CNSA 2.0 as the parallel National Security Systems clock.

## Implementations

**Searched 2026-11-03.** A transition plan has no implementations of its own. These are the libraries that implement its target algorithms:

| Name | Kind | License | URL |
|---|---|---|---|
| liboqs (Open Quantum Safe) | open source, C library | MIT | https://github.com/open-quantum-safe/liboqs |
| OpenSSL 3.5+ | open source, C library | Apache-2.0 | https://www.openssl.org/ |
| Bouncy Castle | open source, Java/C# | MIT-style | https://www.bouncycastle.org/ |

Validated (CMVP) modules are what the plan actually gates on. We did not survey them.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, successor identifiers, digest note, relations, `bears_on` |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec` record at the summary bar. It holds no BCP 14 requirements, but its Tables 2–7 are the normative-ish content an extraction would carry. **No issue owns an extraction.** One should be done against the final, not the withdrawn draft. **No `versions/`.** Under `schema/record.schema.yaml` §versions this line should arguably track the final, with the ipd folded into `versions/ipd/`. That would retarget what the id cites, so it was left for the record owner to decide. The `.cache/` copies (`nistir-8547.pdf` for the ipd, `nistir-8547-final.pdf`) are local and gitignored.

## Limits

- **The draft is superseded in substance.** Its deprecation dates are not the current NIST position. Cite the final for any date.
- **Source defects in the ipd, fixed in the final.** Table 5 lists ML-KEM's parameter sets as "ML-KEM-512, **ML-DSA-768**, **ML-DSA-1024**". Table 4 has "Elliptic Curve DH and **MQC**" for MQV. Final Table 5 reads ML-KEM-768/1024.
- **It does not set application deadlines.** §4.2 defers them to future revisions of application-specific guidance (it names FIPS 201-3/PIV credentials and SP 800-52r2 for TLS, and mentions IKE); §4.1 separately promises an SP 800-131A revision. None of that is held here.
- **Hybrid security is asserted, not analysed.** The ipd's only caveat sits in §3.2.1 (key establishment): security properties *"can be complex"*. Its §3.2.2 on signatures has none. The final adds one to §3.2.2 (*"need to be carefully analyzed"*). Neither version says how to bind the components of a dual signature against stripping.
- **Read scope.** The ipd was read in full. The final was compared on §1, §2.1, §3, §3.2.2, §4 and §4.1.1–4.1.3 only.
