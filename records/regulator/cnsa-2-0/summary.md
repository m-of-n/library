---
schema: "library-summary/v1"
id: cnsa-2-0
record: cnsa-2-0
type: summary
updated: "2026-11-03"
---

# Commercial National Security Algorithm Suite 2.0 and Quantum Computing FAQ

|  |  |
|---|---|
| **Type** | spec (NSA Cybersecurity Information Sheet, FAQ) |
| **Maturity** | _unset_. Verified as NSA CSI **Ver. 2.2, October 2026** from the cover. No enum value fits an FAQ that explains binding NSS policy (CNSSP 15) without being it |
| **Authors** | National Security Agency |
| **Published** | October 2026 (v2.2). Earlier: Sept 2022 original, Dec 2024 v2.1 (seen), with other revisions between them that were not checked |
| **Identifier** | U/OO/6072712-26 · PP-26-3194 |
| **Source** | https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF (403 to direct fetch. Bytes taken from the Internet Archive capture of 2026-10-23, see `record.yaml`) |
| **Digest** | `sha256:bc430341…` (full value in `record.yaml`), fetched 2026-11-03 |

## Overview

CNSA 2.0 is the algorithm set NSA requires for National Security Systems. The FAQ explains it and, through CNSSP 15, its deadlines (p. 1, p. 6: NSA *"does not mandate requirements on any other entity outside of NSS"*). The suite is narrow on purpose. It has AES-256, ML-KEM-1024, **ML-DSA-87 "in any use case, including signing firmware and software"**, and SHA-384/512. LMS and XMSS are allowed for firmware and software signing, and SHA3-384/512 only for internal hardware integrity (table, pp. 7–8). Everything else is excluded explicitly. SLH-DSA is *"not approved for any use in NSS"*. HSS and XMSS^MT are not allowed (p. 11). HashML-DSA is not allowed *"at the present time"* (p. 15). FN-DSA is not expected to be added (p. 15), nor are any on-ramp results (p. 27) or any future NIST PQ standard (p. 16), because *"adding more algorithms generally makes interoperability more complex"*. The schedule (pp. 17–18) has three dates. From **1 Jan 2027**, CNSA 2.0 is required in new NSS acquisitions. By **31 Dec 2030**, equipment that cannot support it is phased out. By **31 Dec 2031**, CNSA 2.0 is mandated for full QR. p. 24 adds that from 2027 *"no new product for NSS should have a burned-in root of trust relying on a non-QR primitive"*.

## Answer to the topic question

*Which attestation systems have a stated post-quantum path, and which have a gap?* CNSA 2.0 is the **strictest stated path** in the library, and three of its positions cut against common attestation practice.

1. **Roots of trust first.** Firmware signing is urgent because *"the validation algorithm is not easily updated"*, and a QR root may be needed *"years before the rest of the system"* (p. 13). The guidance is to start now with LMS/XMSS. ML-DSA-87 is reasonable where one stateful key cannot cover the signature volume or where signing is distributed (p. 15). NSS signers must use CMVP-validated hardware with no waivers. Backup flows *"must prevent state re-use"* (pp. 11–12). For an attestation system, the verifier embedded in a device is what has to be QR at purchase (p. 18).
2. **No composites in PKI.** The FAQ's answer to "do I need a composite signature?" is no. NSA's answer is a **parallel PKI**, with old, new, or dual credentials per device until the transition ends, and *"NSS systems using PKI should not use novel mechanisms to support multiple algorithms within a single certificate"* (pp. 29–30). Hybrids are not required for security. Where NSA has approved one (the IKEv2 ML-KEM case, p. 29), only that one counts (p. 28). This is a direct policy disagreement with `draft-ietf-lamps-pq-composite-sigs`. We record it as a tension, not `contradicts`, because one document is a format and the other is a deployment policy.
3. **Threshold signatures have no approved solution.** The FAQ lists threshold signatures, group and ring signatures, distributed ledgers and others as having *"no generally approved solutions"*, and NSS owners must consult NSA first (p. 26). A threshold *signature scheme* is therefore outside CNSA 2.0. Independent ML-DSA-87 signatures combined by policy are not threshold signatures, and are not excluded.

**Gap it leaves:** there is no post-break evidence story. Like `nistir-8547`, the FAQ says nothing about how a signature made before a CRQC stays verifiable afterwards.

## What changed from v2.1 (December 2024)

We compared v2.2 against a 2025-12-23 capture of the same URL (v2.1, digest in `record.yaml`) by term search, not a full diff. New in v2.2: the "full QR" framing of the **31 Dec 2031** date (v2.1 already had the date, as CNSA 2.0 "mandated for use"), the "well ahead of the 2035 goal" wording (v2.1: "by 2035"), three EO 14412 questions (pp. 21–22), the parallel-PKI / composite question (pp. 29–30), the 2027 burned-in-root sentence (p. 24), the on-ramp question (p. 27), and "Department of War" for DoD. Unchanged: the algorithm table, including ML-DSA for firmware.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Threat framing and validation policy (CAVP for verifiers, CMVP for signers), not analysis |
| Cryptography | `core` | A closed algorithm and parameter list with explicit exclusions |
| This project | `adjacent` | Constrains how a threshold principal can be realised for anyone who must interoperate with NSS |

- **R-M-06** (threshold principals representable without a CA hierarchy). p. 26 places threshold *signatures* outside approval. Our reading: an m-of-n principal that is satisfied by m independent CNSA-approved signatures, each verifiable alone, stays inside CNSA 2.0, and a threshold-signature realisation would not. That argues for keeping R-M-06's principal at the policy layer and not making it a primitive. The inference is ours, not NSA's.
- **It bears on no `DEC-*`.** The parallel-PKI stance (pp. 29–30) is relevant to how R-I-05 imports X.509, but nothing in R-I-05 turns on algorithm choice, so no edge is set.

**Relations.** `see_also` edges are the specifications the FAQ's algorithm table and answers name (FIPS 197, 203, 204, 180-4, 202; SP 800-208, with RFC 8554/8391 as the LMS/XMSS specs behind it; SP 800-53r5, p. 21), FIPS 205 as the one it excludes (p. 11), `nistir-8547` (the miscited "NISTIR 8647", p. 22), `nistir-8610` (the on-ramp it will not adopt, p. 27), and the composite-signature draft (the policy tension above).

## Implementations

**Searched 2026-11-03.** The FAQ makes compliance a property of validated products (NIAP, CMVP, CAVP; pp. 9–10, 25), not of libraries.

| Name | Kind | License | URL |
|---|---|---|---|
| liboqs | open source, C | MIT | https://github.com/open-quantum-safe/liboqs |
| Bouncy Castle | open source, Java/C# | MIT-style | https://www.bouncycastle.org/ |
| wolfSSL / wolfCrypt | open source / commercial, C | GPL-3.0 or commercial | https://www.wolfssl.com/ |
| NIAP Product Compliant List | commercial (the compliance gate) | — | https://www.niap-ccevs.org/product-compliant-list |

None of these is CNSA-compliant merely by implementing the algorithms. We did not check validation status.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata. The digest note covers the 403, the Wayback provenance, and v2.1 vs v2.2 |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec`-typed record at the summary bar. An FAQ has no BCP 14 keywords, but it has mandate-like sentences ("must", "will not be granted"). An FX-1 pass would be owed if the project ever needs CNSA conformance. **No issue owns it.** **No `versions/`**: v2.1 was only spot-checked, and folding it in is cheap if wanted. The `.cache/cnsa-2-0.pdf` copy is local and gitignored.

## Limits

- **NSS only.** By its own terms (p. 6) it binds nobody else. Its civilian counterpart is `nistir-8547`.
- **Not the policy itself.** CNSSP 15, which actually mandates the dates, is not held. The FAQ paraphrases it.
- **Source defects.** p. 22 cites *"NISTIR 8647"* for NIST's 2035 disallowance. The document meant is NIST IR 8547 (`nistir-8547`). The FAQ also disagrees with itself on CNSSP 15's date: p. 20 calls it *"the 2024 update to CNSSP 15"*, and p. 24 says *"With the signing of CNSSP 15 in 2025"*. p. 24's *"By the end of 2030, all available devices should fully support QR algorithms"* sits uneasily beside p. 17's 31 Dec 2031 date for full QR. Support and use differ, but the FAQ does not say so. p. 18 is plainer: it speaks of *"the 2030 deadline for full QR"*, which contradicts p. 17 outright.
- **No per-category chart.** The 2022 announcement's per-use-case "support/prefer by … exclusively by …" chart, which mofn `research/0001-signatures-and-attestation/mini-reports/H-post-quantum.md` §6 quotes, is not in this FAQ and is not held. Those dates should not be cited to this record.
- **Provenance.** The bytes come from an archive capture, because the canonical host refused us. The capture is of the canonical URL and the cover version matches, but NSA revises this file in place.
- **Read scope.** v2.2 was read in full.
