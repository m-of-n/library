---
schema: "library-summary/v1"
id: brickell-2004-daa
record: brickell-2004-daa
type: summary
updated: "2026-11-01"
---

# Direct Anonymous Attestation

|  |  |
|---|---|
| **Type** | paper (full version of ACM CCS 2004 paper) |
| **Maturity** | `white-paper`: an ePrint preprint |
| **Authors** | E. Brickell, J. Camenisch, L. Chen |
| **Published** | 2004-02-11 on the paper; received by ePrint 2004-08-21 |
| **Identifier** | IACR ePrint 2004/205 |
| **Source** | https://eprint.iacr.org/2004/205 |
| **Digest** | `sha256:013b1bbd…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DAA lets a TPM prove it is a valid TPM without revealing which one. It is a group signature with no opening: anonymity cannot be revoked (§1). Pseudonyms are chosen per signature, so a user can decide with the verifier whether signatures link, and a TPM whose secret was extracted and published can be detected (abstract, §1). It replaces the Privacy CA, which had to be online for every transaction and could identify a TPM by colluding with a verifier (§1). Security is proved in the random oracle model under strong RSA and DDH (abstract, §1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Solves linkability of attestation while keeping rogue detection |
| Cryptography | `core` | A full scheme and proof built on Camenisch-Lysyanskaya signatures |
| This project | `adjacent` | We name principals by key, the opposite posture, so this marks what that gives up |

- **R-M-02**: identifying a principal solely by key makes every use linkable. DAA is what a design has to adopt if that is unacceptable, and the price is a group-wide issuer.
- **R-O-02**: rogue tagging here affects only messages signed after a tag in the model (§2), which is a concrete example of the limits of revocation.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `paper` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Anonymity needs an honest host.** A corrupted host can always add an identifier (§1), and the model only guarantees anonymity if both host and TPM are honest (§2).
- **The basename policy is not settled.** A fixed ζ gives almost no privacy, and how often to change it is left to risk management (§1).
- **Parameters are of their time.** The proposal uses a 2048-bit modulus and a 160-bit hash (§4). Nothing here is post-quantum.
- **Proofs assume corrupted TPMs sit in corrupted hosts** (§2).
- **Read scope.** Abstract, §1, §2, §3 to §3.3, the security parameters in §4 and §6 were read, from the Archive capture, by text extraction. The protocol steps in §4 and the proofs in §5 were not checked. Mathematical notation extracted imperfectly.
