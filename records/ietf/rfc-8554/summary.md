---
schema: "library-summary/v1"
id: rfc-8554
record: rfc-8554
type: summary
updated: "2026-11-01"
---

# Leighton-Micali Hash-Based Signatures

|  |  |
|---|---|
| **Type** | rfc (IRTF CFRG) |
| **Maturity** | `informational`: Category Informational, confirmed in `rfc8554.json` 2026-11-01 |
| **Authors** | D. McGrew, M. Curcio, S. Fluhrer |
| **Published** | 2019-04 |
| **Identifier** | RFC 8554 · DOI 10.17487/RFC8554 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8554.txt |
| **Digest** | `sha256:d5bfdbd4…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | not checked (see Limits) |

## Overview

RFC 8554 specifies LM-OTS one-time signatures, LMS (a Merkle tree of them) and HSS, a hierarchy in which each LMS tree signs the next tree's public key and the last signs the message (§4 to §6). The tree split is a time trade: only active trees need generating, at the cost of larger signatures (§1, §6.4). It carries the same CFRG warning as `rfc-8391`, that a reused state voids all guarantees (§1.1). §9.2 is unusually practical about why that is hard, covering caches between the application and the disk, and it gives a mitigation: keep the second-level HSS key in RAM only and regenerate on restart. §10 argues for HSS over XMSS: roughly four times faster and simpler with SHA-256, at slightly larger signatures.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | State reuse is total failure. §9 also has hard verifier rules on typecodes |
| Cryptography | `core` | A complete hash-based signature specification with test cases (Appendix F) |
| This project | `adjacent` | NG3 defers the suite. The state model and the bounded key life still bear on the key model |

- **R-M-02**: as with `rfc-8391`, a key has a finite signature budget. §6.4 expresses this directly as KeyLifetime, from 30 seconds at height 15 to 34 years at 25/15, assuming 1000 signatures per second. A key-only principal has that lifetime unless something rotates it. `rfc-8778`, already held, maps HSS into COSE and carries the fuller analysis.

## Implementations

**Searched 2026-11-01.** Only the implementation named by §6.4 was confirmed; no wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| cisco/hash-sigs | open source, C | none detected by GitHub | https://github.com/cisco/hash-sigs |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **NSA's preferred parameters are not in this RFC.** `cnsa-2-0` recommends LMS with SHA-256/192. This RFC defines only SHA-256 with n = 32 and m = 32 (§4.1, §5.1). The 192-bit form comes from `sp-800-208`. Whether the IANA registry has since gained it was not checked.
- **It does not solve state.** §9.2 calls out the issues and says it does not attempt complete guidance.
- **HSS is out for NSS.** `cnsa-2-0` allows LMS only, not the multi-tree HSS this RFC also defines, while `nistir-8547` Table 3 lists both as post-quantum.
- **The performance table is one machine.** §6.4's numbers are from a 3.3 GHz Xeon without SHA extensions, and it says your mileage may vary.
- **Errata not checked.** The errata lookup gave no usable result.
- **Read scope.** §1, §6, §6.4, §7, §9 and §10, plus the parameter tables in §4.1 and §5.1, were read. The rest of §3 to §6 and Appendices A to F were not read line by line.
