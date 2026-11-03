---
schema: "library-summary/v1"
id: nistir-8610
record: nistir-8610
type: summary
updated: "2026-11-03"
---

# NIST IR 8610: Status Report on the Second Round of the Additional Digital Signature Schemes

|  |  |
|---|---|
| **Type** | spec (NIST Internal Report, status report) |
| **Maturity** | `informational`: final per CSRC ("IR 8610 (Final)", 05/14/26), checked 2026-11-03. The enum value is our mapping, because the report standardizes nothing |
| **Authors** | G. Alagic, M. Bros, P. Ciadoux, Q. Dang, T. Dang, J. Kelsey, J. Lichtinger, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner, A. Robinson, H. Silberg, D. Smith-Tone, N. Waller (NIST) |
| **Published** | 2026-05-14 |
| **Identifier** | NIST IR 8610 · DOI 10.6028/NIST.IR.8610 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8610.pdf |
| **Digest** | `sha256:580b6f43…` (full value in `record.yaml`), fetched 2026-11-03 |

## Overview

NIST's "on-ramp" for signatures exists because two of its three general-purpose PQ signatures rest on structured lattices (§1). The 2022 call asked for non-lattice general-purpose schemes and for schemes with short signatures and fast verification. Lattice schemes had to beat both Dilithium and Falcon on some metric, and non-lattice schemes had to beat SPHINCS+ (§2.2). This report closes round 2. Of 14 candidates it advances **nine**: FAEST, MQOM and SDitH (MPC-in-the-head), HAWK (lattice), SQIsign (isogeny), and UOV, MAYO, QR-UOV and SNOVA (multivariate). CROSS, LESS, Mirath, PERK and RYDE are eliminated (§2.3, Table 3). Security ranks first, then cost and performance (§2.3). Its main claim about the multivariate schemes is a warning. Second-round attacks hit UOV, MAYO and SNOVA parameter sets (§2.2.1), and NIST *"anticipates a longer timeline for the potential standardization of any of these multivariate schemes and is unlikely to standardize them without a further round of evaluation"* (§2.3). Round-3 tweaks were due 14 Aug 2026, and the next conference is in the first half of 2027 (§4).

## Answer to the topic question

*Which attestation systems have a stated post-quantum path, and which have a gap?* This report contributes **the absence of a near-term second path**. As of this report, a system that wants a PQ signature with neither a structured-lattice assumption nor hash-based sizes has **nothing standardized to choose**. Round 3 has only just begun, and for multivariate schemes it is expected not to be the last round (§2.3, §4). For attestation the sizes are what make the track tempting, all at security category 1: SQIsign signatures *"as low as 148 bytes"* (§3.3), HAWK at 555 bytes (§3.4), UOV at 96 bytes against expanded public keys *"over 200 kilobytes"* (§3.11), and MQOM/RYDE/Mirath at 3–3.5 KB (§3.9). Each is a hedge, not a plan. The record is relevant to a format's PQ path only as a reason to keep the algorithm identifier open. **Post-publication:** NIST's round-3 page now says the HAWK team *"has withdrawn HAWK"* (checked 2026-11-03), which leaves eight candidates. NSA has separately said it does not expect to adopt on-ramp results into CNSA (`cnsa-2-0`, FAQ v2.2 p. 27).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Reports cryptanalysis outcomes (wedge attack, attacks on CROSS, LESS and SNOVA) by citation, not in detail (§2.2.1, §3) |
| Cryptography | `core` | The authoritative status of every non-FIPS PQ signature candidate as of May 2026 |
| This project | `none` | No candidate is usable within the project's horizon, and none is final |

**Bears on none yet.** This is an honest empty `bears_on`. A future suite slot for a compact signature would make it relevant to R-M-02 (a principal identified solely by key or key digest, where key size is the cost), as `fips-204`'s summary argues for ML-DSA. That slot does not exist, so no edge is set.

**Relations.** `see_also` is limited to `fips-204` and `fips-205`: §2.2 sets the bar every candidate had to beat against Dilithium/Falcon and SPHINCS+.

## Implementations

**Searched 2026-11-03.**

| Name | Kind | License | URL |
|---|---|---|---|
| liboqs (Open Quantum Safe) | open source, C library | MIT | https://github.com/open-quantum-safe/liboqs |

The liboqs README (2026-11-03) carries MAYO, MQOM, QR-UOV, SDitH, SNOVA and UOV at "Tier 3 (Community)". It also still lists **CROSS as "Under NIST consideration"**, which is stale: 8610 §2.3 eliminated it. Each candidate team also publishes a reference implementation. Those are linked from the CSRC round-3 page and were not individually checked. We found no commercial products and expected none for round-3 candidates.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest note (including the HAWK withdrawal), relations |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This is a `spec`-typed record at the summary bar. It is a status report with no requirements, schemas or vectors, so an FX-1 extraction would mostly be N/A pointers. If one is ever wanted, no issue owns it. The `.cache/nistir-8610.pdf` copy is local and gitignored.

## Limits

- **It is a snapshot.** It settles nothing about which candidate (if any) is standardized. HAWK's withdrawal after publication already makes Table 3 out of date.
- **No performance tables.** Sizes are quoted in prose per candidate and at category 1 only. Comparing the candidates needs the submission packages.
- **Attacks are cited, not described.** The wedge attack and the other second-round attacks ([6–11]) are only referenced. This record did not read them.
- **Read scope.** §1, §2 and §4 were read in full. In §3, the per-candidate summaries for SQIsign, HAWK, the MPCitH group and UOV were read; the rest were skimmed.
