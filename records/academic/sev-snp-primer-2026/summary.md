---
schema: "library-summary/v1"
id: sev-snp-primer-2026
record: sev-snp-primer-2026
type: summary
updated: "2026-11-01"
---

# AMD SEV-SNP: A Confidential Computing Primer

|  |  |
|---|---|
| **Type** | paper (arXiv preprint, company-authored primer) |
| **Maturity** | `white-paper`: preprint |
| **Authors** | A. Asad, P. McClurg, P. Woodhead |
| **Published** | June 2026 on the paper; arXiv 2026-08-03 |
| **Identifier** | arXiv:2608.04039 |
| **Source** | https://arxiv.org/abs/2608.04039 |
| **Digest** | `sha256:c8fc5c13…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The primer builds SEV-SNP's guarantees from the hardware up against an adversarial hypervisor: memory encryption, the Reverse Map Table for integrity, and an attestation pipeline binding a signed measurement of initial state to AMD's certificate chain. §6.3 shows the VCEK is derived per chip and per TCB version, so identity is compound by construction. §6.7 separates what a report proves from what it does not. It proves genuine hardware, a TCB version, launched bytes and the guest's REPORT_DATA. It does not prove the code is correct, or uncompromised after launch: the measurement is an identity, not a behavioural assertion.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sets out what the hardware root does and where the boundary stops |
| Cryptography | `adjacent` | Describes key derivation and ECDSA P-384 report signatures. No new cryptography |
| This project | `adjacent` | Second-hand, but it states our topic's answer plainly |

- **R-M-02**: a key alone proves possession. Here the key is derived so that its identity also says which chip and firmware hold it (§6.3.1). §6.7 shows how little more that buys.
- **R-I-02**: §6.8 says to pin the ARK and not fetch it at verification, and to enforce a minimum TCB. The root is chosen by the verifier, and policy does the rest.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `paper` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **The root has fallen before.** §6.3.1 reports a software-only extraction of the VCEK seed on Milan parts, enough to forge reports at arbitrary TCB versions, and concludes the VCEK's strength is exactly that of the surrounding hardware and firmware. This paper's citation [16] was not followed.
- **Initial state only.** Runtime compromise is not reflected (§6.7, §6.8).
- **Excluded by design.** Availability, side channels, guest software bugs and invasive physical attacks are out of scope (§2.5).
- **Secondary.** A vendor-neutral-looking primer by a company in this market, not AMD's own specification. No AMD SEV-SNP firmware ABI document is held, so details here are not checked against the primary.
- **Read scope.** Abstract, section list, §2.5, §4.7, §6.3 to §6.3.1, §6.7 and §6.8 were read. The rest was searched by keyword, not read. §6.7's two bullet lists lost their headings in text extraction, and the split into proved and not proved is taken from the section title and the bullets' wording.
