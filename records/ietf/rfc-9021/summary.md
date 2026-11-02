---
schema: "library-summary/v1"
id: rfc-9021
record: rfc-9021
type: summary
updated: "2026-11-01"
---

# Use of the Walnut Digital Signature Algorithm with CBOR Object Signing and Encryption (COSE)

|  |  |
|---|---|
| **Type** | rfc (Independent Submission) |
| **Maturity** | `informational`: Category Informational, Independent Submission stream, confirmed in `rfc9021.json` 2026-11-01 |
| **Authors** | D. Atkins |
| **Published** | 2021-05 |
| **Identifier** | RFC 9021 · DOI 10.17487/RFC9021 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9021.txt |
| **Digest** | `sha256:177b3ea4…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9021 assigns COSE identifiers to WalnutDSA, a group-theoretic signature scheme pitched as quantum-resistant, stateless and very cheap to verify on small processors (§1, §3). It registers algorithm -260, key type 6 and six key parameters (§4, §6). It is an Independent Submission, and the abstract says the IETF has neither evaluated its security nor endorsed it. §5.2 summarises a run of published attacks and argues that current parameters defeat them.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Only as a record of a scheme with repeated cryptanalysis (§5.2) |
| Cryptography | `adjacent` | An unevaluated scheme. The document specifies the COSE binding, not the algorithm |
| This project | `none` | Bears on no `DEC-*` or `R-*`. NG3 defers the suite, and this would not be a candidate |

- It bears on none. `SPEC-0002` reserves post-quantum suites and provisions ML-DSA-65, not this.

## Implementations

**Searched 2026-11-01.** GitHub repository search for `WalnutDSA` only. No COSE binding was found. The search also returned `SimonMerz/Non-obfuscating-power-of-Garside-normal-forms`, code for the attack §5.2 credits to Merz and Petit.

| Name | Kind | License | URL |
|---|---|---|---|
| srseil/walnut-dsa-linux | open source, C, Linux kernel module | GPL-2.0 | https://github.com/srseil/walnut-dsa-linux |
| Veridify Security | commercial | n/a | https://www.rfc-editor.org/rfc/rfc9021 |

- **srseil/walnut-dsa-linux**: WalnutDSA itself, not its COSE binding; last pushed 2021-12-28.
- **Veridify Security**: Trademark holder and author's employer per the RFC; no product was checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Every security claim is the author's.** The author works for Veridify Security, which holds the trademark (§1.2). The claims of quantum resistance and of parameters defeating the attacks were not checked, and `[WalnutDSAAnalysis]` was not read.
- **The algorithm is not specified here.** §3 points to `[WALNUTDSA]` and `[WALNUTSPEC]`, neither held.
- **No test vectors.** Nor signature sizes, beyond the comparison in §1.
- **It cites RFC 8152.**
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the references.
