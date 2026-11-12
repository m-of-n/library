---
schema: "library-summary/v1"
id: sae-j3061
record: sae-j3061
type: summary
updated: "2026-11-03"
---

# SAE J3061, Cybersecurity Guidebook for Cyber-Physical Vehicle Systems (superseded by ISO/SAE 21434)

|  |  |
|---|---|
| **Type** | spec (SAE Recommended Practice) |
| **Maturity** | historic: SAE lists J3061_201601 as "Historical", replaced by J3061_202112 "Stabilized" (catalogue capture of 2022-01-21) |
| **Authors** | SAE Vehicle Cybersecurity Systems Engineering Committee (catalogue) |
| **Published** | 2016-01-14 (J3061_201601); 129 pages per the catalogue capture, which shows the 202112 revision |
| **Identifier** | SAE J3061_201601 |
| **Source** | https://www.sae.org/standards/content/j3061/ |
| **Digest** | none. **Not fetched**: sold by SAE (USD 87 in the 2022 capture) |

## Overview

**This record has not been read.** The document is sold by SAE and was not obtained, and its normative text was not read. Per `docs/scope.md` §1 it stays a `stub`. Everything below comes from SAE catalogue pages seen through Internet Archive captures dated 2021-10-28 and 2022-01-21 (the latter redirected to the J3061_202112 page), and is labelled as such.

Per the catalogue abstract, J3061 is a recommended practice that provides a lifecycle process framework for building cybersecurity into cyber-physical vehicle systems *"from concept phase through production, operation, service, and decommissioning"*, plus guiding principles and an overview of existing tools and methods. The abstract lists appendices on threat analysis and risk assessment, threat modelling and vulnerability analysis, such as attack trees (A–C), sample controls derived from NIST SP 800-53 (D), and vulnerability databases, vehicle-level design practice, related standards, research projects and test tools (E–I). The 2022 capture gives the rationale for stabilisation: *"SAE J3061 is being superseded by ISO/SAE 21434."* `iso-sae-21434-2021` carries the matching `supersedes: sae-j3061` edge.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The predecessor of ISO/SAE 21434's automotive cybersecurity engineering process |
| Cryptography | `none` | Nothing in the abstract concerns cryptography |
| This project | `none` | Historical; read `iso-sae-21434-2021` instead |

**Bears on none.** ARCH-0001 §5 and the design log have no automotive requirement. Earlier `bears_on: DEC-005` came from Threat-Radar's numbering and was removed (see `content.note`). **Restored 2026-11-09 as `tmodel:DEC-005` (library#133).** The removal misread a register collision as a stale id: these are tmodel's live ids (Threat-Radar `project/DECISIONS-0001.md` and `spec/ARCH-0001-threat-model-architecture.md`), where DEC-005 is MVP scope. They still bear on no mofn decision.

## Implementations

Not searched: a superseded process guidebook.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with what was and was not seen in `content.note` |
| `summary.md` | this document |

**No authored relations and no `distilled/`.** The `supersedes` edge lives on `iso-sae-21434-2021`; this record's `superseded_by` is derived from it and left empty here. No bytes were obtained. A legitimate copy would move this record past `stub`.

## Limits

- **Unread.** Only catalogue abstracts were seen; the normative text was not read. What changed between J3061_201601 and the stabilized J3061_202112, if anything, is unknown. A stabilized J3061_202112 would be a new record linked by `supersedes`, not this one.
- **Conflicting catalogue states.** The 2021-10-28 capture described the document as being cancelled with a J3061A shown as work in progress; the 2022-01-21 capture shows it stabilized instead. The live sae.org page returned only an application shell, so the current state was not seen.
