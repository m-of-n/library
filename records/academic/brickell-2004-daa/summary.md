---
schema: "library-summary/v1"
id: brickell-2004-daa
record: brickell-2004-daa
type: summary
updated: "2026-11-03"
---

# Direct Anonymous Attestation

|  |  |
|---|---|
| **Type** | paper (full version of ACM CCS 2004 paper) |
| **Maturity** | _unset_: an ePrint full version of a peer-reviewed conference paper, so no standards-track level applies |
| **Authors** | E. Brickell, J. Camenisch, L. Chen |
| **Published** | 2004-02-11 on the paper; received by ePrint 2004-08-21 |
| **Identifier** | IACR ePrint 2004/205 |
| **Source** | https://eprint.iacr.org/2004/205 |
| **Digest** | `sha256:013b1bbd…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DAA lets a TPM prove it is a valid TPM without revealing which one. It is a group signature with no opening: anonymity cannot be revoked (abstract, §1). For each signature the user, in agreement with the verifier, decides whether it should be linkable to others, through a per-basename pseudonym (abstract, §1; the basename model is §2), and a TPM whose secret was extracted and published can be detected (abstract, §1). It replaces the Privacy CA, which had to be online for every transaction and could identify a TPM by colluding with a verifier (§1). Security is proved in the random oracle model under strong RSA and DDH (abstract, §1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Solves linkability of attestation while keeping rogue detection |
| Cryptography | `core` | A full scheme and proof built on Camenisch-Lysyanskaya signatures |
| This project | `adjacent` | We name principals by key, the opposite posture, so this marks what that gives up |

- **R-M-02**: identifying a principal solely by key makes every use linkable. DAA is what a design has to adopt if that is unacceptable, and the price is a group-wide issuer.
- Not R-O-02. Rogue tagging (§2, §4) is detection of extracted keys by a verifier-held list, not a validity-period or revocation design choice, so it does not inform the short-lived-versus-revocation preference.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites: tcg-tpm-1-2-main`** is the paper's [34], the TPM 1.2 main specification that adopted DAA (§1); the record held is a later revision (rev 116) of the same line. **No `see_also`.** `tcg-tpm-2-0-library-184` already authors `see_also` to this record; the edge is symmetric, so it is not repeated here. The TPM 1.2 link is the `cites` edge above.

**No `distilled/`.** This is the summary bar. A `paper` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Anonymity needs an honest host.** A corrupted host can always add an identifier (§1), and the model only guarantees anonymity if both host and TPM are honest (§2).
- **The basename policy is not settled.** A fixed ζ gives almost no privacy, and how often to change it is left to risk management (§1).
- **Parameters are of their time.** The proposal uses a 2048-bit modulus and a 160-bit hash (§4). Nothing here is post-quantum.
- **Proofs assume corrupted TPMs sit in corrupted hosts** (§2).
- **Read scope.** Abstract, §1, §2, §3 to §3.3, the high-level description and security parameters in §4, the theorem statement in §5, and the §6 conclusion were read, from the Archive capture, by text extraction. The protocol steps in §4 and the proofs in §5 were not checked. Mathematical notation extracted imperfectly.
