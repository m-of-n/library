---
schema: "library-summary/v1"
id: ietf-spki-wg
record: ietf-spki-wg
type: summary
updated: "2026-11-01"
---

# IETF SPKI Working Group charter and documents

|  |  |
|---|---|
| **Type** | web (Datatracker working group page) |
| **Maturity** | `historic`: Datatracker state Concluded |
| **Authors** | Chairs: Perry E. Metzger, Steven M. Bellovin |
| **Published** | Charter milestones dated February to May 1997 |
| **Identifier** | https://datatracker.ietf.org/wg/spki/about/ |
| **Source** | https://datatracker.ietf.org/wg/spki/about/ |
| **Digest** | `sha256:c4105cf4…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The charter (charter-ietf-spki-01) asked for Internet standards for a public key certificate format, signature formats and key acquisition protocols, "simple to understand, implement, and use", supporting a range of trust models. Its milestones expected specifications to go to the IESG by May 1997. What the Datatracker records as output is two Experimental RFCs of September 1999, `rfc-2692` (requirements) and `rfc-2693` (theory), with state Concluded. The gap between that charter and that list is the point of this record: a certificate format was the charge, and the group's RFCs are titled requirements and theory (the format draft is `draft-ietf-spki-cert-structure`).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Scope of a trust-model effort, not a mechanism |
| Cryptography | `none` | The page carries no technical content |
| This project | `core` | The record of how the direct ancestor ended without a wire format |

`DEC-002`: mofn R-0004 §5(a) reads the missing format as the one failure a specification can fix, and ties it to closing this decision. This page supplies only the bare record; `draft-ietf-spki-cert-structure` holds the format itself.

## Implementations

None applicable: an organisational page. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, not an extraction. This record has no normative content to extract, and no issue owns one.

## Limits

Read whole: the about page and documents page, live. The Datatracker warns its data for concluded groups is occasionally incorrect. It lists only the two RFCs, not the expired drafts, and gives no date or reason for conclusion, so this record does not say why the group stopped. The mailing list (spki@c2.net) was not read. The reading that the group abandoned the format is R-001 §5.5's inference, not something the page states.
