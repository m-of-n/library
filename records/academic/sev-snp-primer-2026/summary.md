---
schema: "library-summary/v1"
id: sev-snp-primer-2026
record: sev-snp-primer-2026
type: summary
updated: "2026-11-03"
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

The primer builds SEV-SNP's guarantees from the hardware up against an adversarial hypervisor: memory encryption, the Reverse Map Table for integrity, and an attestation pipeline binding a signed measurement of initial state to AMD's certificate chain. §6.3.1 shows the VCEK is derived per chip and per TCB version, so identity is compound by construction. §6.7 separates what a report proves from what it does not. It proves genuine hardware, a TCB version, launched bytes and the guest's REPORT_DATA. It does not prove the code is correct, or uncompromised after launch: the measurement is an identity, not a behavioural assertion.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sets out what the hardware root does and where the boundary stops |
| Cryptography | `adjacent` | Describes key derivation and ECDSA P-384 report signatures. No new cryptography |
| This project | `adjacent` | Second-hand, but it states our topic's answer plainly |

- **R-I-02**: §6.8 (and step 4 of §6.4) says to pin the ARK as a known-good copy bundled with the verifier, not fetched from KDS at verification, because a network adversary could substitute a fake. The certificate chain that arrives with the evidence does not get to name its own root.
- Not R-M-02. §6.3.1 is about how the VCEK is derived, not about whether a principal may be named by key alone.

## Implementations

Taken from the paper's own §6.4 and checked on GitHub 2026-11-03.

- **virtee/sev-snp-measure** (Apache-2.0): computes the expected launch digest a verifier compares MEASUREMENT against ([26]).
- **confidential-dot-ai/attestation-rs** (MIT): generation and verification tooling from the authors' company ([27]), so not an independent implementation.

AMD's KDS ([25], §6.4 step 3) is the service a verifier fetches the VCEK, chain and CRL from.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites: rfc-9334`** is the paper's [6], named in §1.2 as the vendor-neutral framing of the verifier's role. **No `see_also`.** `aws-snp-attestation` already authors `see_also` to this record; the edge is symmetric, so it is not repeated here.

**No `distilled/`.** This is the summary bar. A `paper` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **The root has fallen before.** §6.3.1 reports a software-only extraction of the VCEK seed on Milan parts, enough to forge reports at arbitrary TCB versions, and concludes the VCEK's strength is exactly that of the surrounding hardware and firmware. This paper's citation [16] was not followed.
- **Initial state only.** Runtime compromise is not reflected (§6.7, §6.8).
- **Excluded by design.** Availability, side channels, guest software bugs, invasive physical attacks and trust-anchor compromise are outside the threat model (§2.5). §2.5 opens "Three categories of attack are explicitly outside the SEV-SNP threat model" and then describes five.
- **Secondary.** A vendor-neutral-looking primer by a company in this market, not AMD's own specification. No AMD SEV-SNP firmware ABI document is held, so details here are not checked against the primary.
- **Read scope.** Abstract, §1.2, §2.5, §4.7, §6.3 to §6.4, §6.7, §6.8 and the reference list were read. The rest was searched by keyword, not read. §6.7's two bullet lists lost their headings in text extraction, and the split into proved and not proved is taken from the section title and the bullets' wording.
