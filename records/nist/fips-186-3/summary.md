---
schema: "library-summary/v1"
id: fips-186-3
record: fips-186-3
type: summary
updated: "2026-11-01"
---

# FIPS 186-3: Digital Signature Standard (DSS), 2009

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: withdrawn or superseded (CSRC) |
| **Authors** | National Institute of Standards and Technology |
| **Published** | 2009-06. Withdrawn 2013-07-19 (CSRC) |
| **Identifier** | FIPS PUB 186-3 |
| **Source** | https://csrc.nist.gov/files/pubs/fips/186-3/final/docs/fips_186-3.pdf |
| **Digest** | `sha256:d8dad7b8…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

FIPS 186-3 rewrites the standard around what a verifier can conclude. §3 separates *verification*, the mathematics, from *validation*, which also needs assurance of domain parameters, public key validity, possession of the private key, and the claimed signatory's identity, and explains what goes wrong without each. Without identity assurance, it says, a verifier has integrity but not source authentication. Algorithmically it raises DSA to pairs (L, N) up to (3072, 256) with SHA-2 (§4.2), admits RSA through both X9.31 and PKCS #1 with added requirements (§5), and approves ECDSA under X9.62-2005 with key-use limits (§6). Key pairs for signatures shall not be used for any other purpose (§3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | States what verification does not establish |
| Cryptography | `core` | Parameter and hash rules for all three algorithms, now superseded |
| This project | `adjacent` | §3's structure bears on how a key-named principal changes the assurances needed |

`bears_on` is empty on purpose: this version is withdrawn, and `fips-186-5` already carries R-M-02 and R-O-05. For the record, §3's identity assurance is the check that R-M-02 changes. A principal identified solely by its key has no separate claimed identity to assure, so that assurance becomes a statement about names (R-M-03). We have not shown that the other three assurances carry over unchanged.

## Implementations

Not searched: this standard is withdrawn. See `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `spec` is inside FX-1's type scope, and extraction would owe the full artifact set, but this withdrawn version was not extracted and no issue owns it. The PDF stays in `.cache/` and is not committed.

## Limits

- **Softer than its predecessors, and on purpose or not, it does not say.** `fips-186` says signatures cannot be forged and the signatory cannot repudiate. Here §3 says *"signatures are designed so that they cannot be forged"* and the Abstract says *"the signatory cannot easily repudiate the signature at a later time"*. The document gives no reason for the change.
- **Assurances are delegated.** Methods live in SP 800-89, timeliness in SP 800-102, and neither is held in the library.
- **RSA and ECDSA still lean on external standards.** X9.31, X9.62-2005 and PKCS #1 were not read.
- **No `supersedes` from `fips-186-4` is assumed here.** That edge belongs on `fips-186-4`, and it is being added by another PR. This record authors only its own edge to `fips-186-2`; `superseded_by` is derived.
- **Read by section.** Read: front matter, §1, §3, §4.1, §4.2, §4.4.2, §5 and §6 openings, the Appendix E opening. The glossary was sampled. The appendices on generation, primality and curves (A to D, F) were not read beyond their contents and one page, and no example was run.
