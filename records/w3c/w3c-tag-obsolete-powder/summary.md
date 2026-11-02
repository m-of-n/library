---
schema: "library-summary/v1"
id: w3c-tag-obsolete-powder
record: w3c-tag-obsolete-powder
type: summary
updated: "2026-11-01"
---

# W3C TAG proposal to obsolete CC/PP and POWDER (issue 86)

|  |  |
|---|---|
| **Type** | web (GitHub issue in w3c/transitions) |
| **Maturity** | `informational`: a process issue, still open |
| **Authors** | plehegar (issue); comments by svgeesus, rigow, philarcher and others |
| **Published** | Opened 31 August 2018; latest comment 20 February 2026 |
| **Identifier** | w3c/transitions#86 |
| **Source** | https://api.github.com/repos/w3c/transitions/issues/86 |
| **Digest** | `sha256:e35d8b8c…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

W3C's Technical Architecture Group asked to mark the PICS, CC/PP and POWDER specifications obsolete. The rationale is that PICS lacks market relevance, and POWDER's main goal, labelling, "did not take off as expected" and suffers the same problem as PICS. The issue then sat for years. PICS was finished separately by marking it superseded and removing it from /TR, and on 20 February 2026 a staff comment reads "Approved. Next step is to organize the AC vote", for POWDER and CC/PP. philarcher, who worked on it in the working group, adds the strongest evidence: the software built to implement it "was never actually used in any production system by anyone ever".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Standards housekeeping |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | First-hand evidence that a better successor inherited non-adoption |

It bears on no open `DEC-*` or `R-*`. It is evidence for mofn R-0004 §6. rigow's dissent is worth noting: reducing POWDER to PICS and harmful content "seems unfair".

## Implementations

None: philarcher reports no production use. Not searched further.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `web` record is outside FX-1 scope.

## Limits

Read whole: the issue and all comments, from the GitHub API, 2026-11-01. The linked TAG minutes and www-tag messages were not read, so the rationale is as quoted in the issue. Still open, labelled `Awaiting AC Vote`: nothing here says POWDER has been obsoleted. philarcher's statement is one participant's recollection ("AFAIK"). The title understates scope: as filed it covers PICS as well.
