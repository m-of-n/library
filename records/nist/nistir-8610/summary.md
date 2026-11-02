---
schema: "library-summary/v1"
id: nistir-8610
record: nistir-8610
type: summary
updated: "2026-11-01"
---

# NIST IR 8610: Status Report on the Second Round of the Additional Digital Signature Schemes

|  |  |
|---|---|
| **Type** | spec (NIST Internal Report, final) |
| **Maturity** | `informational`: a status report |
| **Authors** | G. Alagic, M. Bros, P. Ciadoux, Q. Dang, T. Dang, J. Kelsey, J. Lichtinger, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner, A. Robinson, H. Silberg, D. Smith-Tone, N. Waller |
| **Published** | May 2026 |
| **Identifier** | NIST IR 8610 · DOI 10.6028/NIST.IR.8610 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8610.pdf |
| **Digest** | `sha256:580b6f43…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

NIST's standards so far lean on structured lattices, so it opened a second competition for non-lattice general-purpose signatures, and for short signatures with fast verification (§1). This report cuts 14 second-round candidates to nine: FAEST, HAWK, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign and UOV (§2.3). CROSS, LESS, Mirath, PERK and RYDE are out. The main story is that cryptanalysis moved: wedge-style attacks hit UOV, MAYO and SNOVA parameter sets, and NIST kept all the multivariate schemes anyway because each still has unbroken parameters, while expecting a longer timeline and probably another evaluation round for them (§2.2.1, §2.3). MPC-in-the-Head schemes improved sharply in performance, but their designs and proofs need verification. HAWK and SQIsign rest on newer assumptions.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Shows how fast candidate assumptions can move, not a basis for any choice today |
| Cryptography | `core` | The state of non-lattice and compact signatures, by family |
| This project | `none` | NG3 defers the suite, and no candidate is available |

It bears on no open `DEC-*` or `R-*`. It matters only as a sign of direction: nothing here should be designed against yet. If a compact candidate does arrive, the size pressure described in `tuf-tap-21` would ease. `cnsa-2-0` already says it does not expect to adopt these results.

## Implementations

Not searched. Candidates have submission packages (§1) but no standard exists to implement.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A status report has no normative content to extract, so FX-1 would have little to work on, and this record stays at the summary bar. No issue owns further work on it.

## Limits

- **Not a recommendation.** Selection is for further evaluation only, and §4 says modifications were due by August 14, 2026, so third-round specifications may already differ from what is described.
- **Performance figures are second-round.** The numbers quoted in §3 will move.
- **No timeline for a standard.** §4 gives a conference in the first half of 2027 and nothing further.
- **Security is NIST's judgement at the time.** This record does not evaluate any candidate.
- **Read scope.** §1 to §3 and §4 were read. In §3, paragraph openings were read for each candidate, not every paragraph in full. The references were not read.
