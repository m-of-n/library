---
schema: "library-summary/v1"
id: fips-140-2
record: fips-140-2
type: summary
updated: "2026-11-04"
---

# FIPS 140-2, Security Requirements for Cryptographic Modules (superseded by FIPS 140-3)

|  |  |
|---|---|
| **Type** | spec (Federal Information Processing Standard) |
| **Maturity** | `historic`: superseded by FIPS 140-3 per the CSRC page |
| **Authors** | NIST |
| **Published** | 2001-05-25, change notices to 2002-12-03 |
| **Identifier** | FIPS PUB 140-2 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-2.pdf |
| **Digest** | `sha256:0df0fdd676df…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

FIPS 140-2 sets security requirements for a cryptographic module, across 11 requirement areas and four increasing qualitative levels (§1), so a procurer can match protection to the data and the environment. The levels run from production-grade equipment at Level 1, to a complete tamper detection and response envelope at Level 4 (§4, Table 1). The module's boundary, roles, services, finite state model and key management are specified and validated under the CMVP. The standard limits its own claim: §1 says conformance is not sufficient to make a module secure, and a validated module does not make the surrounding system secure. Mitigation of other attacks, such as DPA and TEMPEST, must be documented but is not tested (§4, §4.11).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Long the reference requirement set for cryptographic modules |
| Cryptography | `core` | Key management, approved functions and self-tests are its subject |
| This project | `none` | ARCH-0001 specifies objects and verification, not modules holding keys |

`bears_on` is empty. The scaffold carried `DEC-009`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), `DEC-009` asks what the contract form is, and this document has nothing to say on that. Those ids are removed rather than kept as a false edge.

**Near miss.** §4.7.4's split knowledge rules for key entry and output require at least two components, and documentation that any n-1 of n reveal nothing beyond key length. That is n-of-n custody of a key inside one module. It is not a threshold principal in the sense of R-M-06 or G4, so no edge is set.

## Implementations

Not searched. The CMVP validation list is the natural place to look, and `fips-140-3` is the record to search from.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**Relations.** None authored here. `fips-140-3` authors `supersedes: fips-140-2`, and `superseded_by` on this record is derived from it by `bin/reindex`, not written by hand.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. `fips-140-3` is the record that carries an extraction, so this one is unlikely to need its own.

## Limits

- **Superseded.** Testing ended in 2021 per the CSRC page. Do not cite it as a current requirement.
- **Read scope.** Front matter, §1 and Levels 1 to 4, §2 in part, §3, §4's introduction and Table 1, and §4.7.4. Change Notice titles 3 and 4 were read, not their bodies. §4.1 to §4.6, the other §4.7 subsections, and §4.8 to §4.11 were not read line by line, and neither were the appendices.
- **Approved lists are elsewhere.** Annexes A to D are separate documents and were not fetched, so this record says nothing about which algorithms were approved.
- **PDF text extraction.** The PDF's text layer has irregular spacing, so no passage is quoted here. Check the PDF for exact wording.
