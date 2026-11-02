---
schema: "library-summary/v1"
id: first-cvss
record: first-cvss
type: summary
updated: "2026-11-01"
---

# FIRST, Common Vulnerability Scoring System (CVSS)

|  |  |
|---|---|
| **Type** | spec on the record; the source is a programme page |
| **Maturity** | _unset_: the pages read do not state a ratification standing |
| **Authors** | FIRST CVSS SIG |
| **Published** | undated page; v4.0 initial release November 2023, as the page states |
| **Identifier** | https://www.first.org/cvss/ |
| **Source** | https://www.first.org/cvss/ |
| **Digest** | `sha256:207702046407…` (full value in `record.yaml`), fetched 2026-11-01; live page |

## Overview

CVSS is a way to record the principal technical characteristics of a vulnerability and turn them into a numerical severity score, which can be mapped to a qualitative rating to help prioritise vulnerability management. The argument for it is comparability: the v4.0 Introduction describes a vendor- and platform-agnostic, open framework in which each score's inputs are visible. v4.0 separates four metric groups (Base, Threat, Environmental, Supplemental). Base and optionally Supplemental come from the maintainer of the vulnerable system, and Threat and Environmental information is available only to the end consumer. So a published Base score is not a statement of risk to any one deployment. This record is the family entry; the normative texts are `first-cvss-v3-1` and `first-cvss-v4-0`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A widely referenced vulnerability severity scale, cited by several records here |
| Cryptography | `none` | Scores vulnerabilities in general and has no cryptographic content |
| This project | `none` | ARCH-0001 has no vulnerability-scoring requirement |

`bears_on` is empty. The scaffold carried `DEC-003` and `R-011`, which come from the numbering of the Threat-Radar library folded in by #62, not from mofn. On mofn `origin/main` (`bec50fd`), `DEC-003` is issuer and subject identifiers on the wire, accepted by `ADR-0005`, and `R-011` does not exist. ARCH-0001 §5 numbers its requirements `R-M-*`, `R-I-*`, `R-O-*` and `R-D-*`. Those ids are removed rather than kept as a false edge.

## Implementations

Not applicable and not searched: this is a scoring scheme. The page links FIRST's own calculators and a CVSS Adopters list, neither of which was evaluated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled. Extraction belongs on the versioned records, and this one has no specification text of its own to extract.

## Limits

- **Read scope.** The whole programme page was read, plus the Introduction and the opening of the Metrics section of the v4.0 HTML specification. The rest of v4.0, all of v3.1, and the User Guide and Implementation Guide were not read for this record.
- **It is a page, not a standard.** Nothing normative should be cited to this record.
- **`type: spec` is inherited.** The source is a programme page, and the type was left alone. If it is reclassified, the id does not change.
- **`maturity` is unset on purpose.** Neither page states what ratification, if any, stands behind CVSS, and the two versioned records leave it unset too.
- **Severity is not risk.** The v4.0 Introduction puts factors such as regulation and business impact outside CVSS.
