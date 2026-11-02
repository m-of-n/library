---
schema: "library-summary/v1"
id: rfc-5937
record: rfc-5937
type: summary
updated: "2026-11-01"
---

# Using Trust Anchor Constraints during Certification Path Processing

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational`: Category Informational |
| **Authors** | S. Ashmore, C. Wallace |
| **Published** | 2010-08 |
| **Identifier** | RFC 5937 · DOI 10.17487/RFC5937 |
| **Source** | https://www.rfc-editor.org/rfc/rfc5937.txt |
| **Digest** | `sha256:6424a9b1…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | no errata link in RFC metadata, 2026-11-01 |

## Overview

RFC 5280 lets an implementation use extra trust anchor data but leaves the processing unspecified. RFC 5937 fills that in with one added input, `enforceTrustAnchorConstraints`, and initialisation steps that run before RFC 5280's. Name constraints on the anchor intersect with the user's `initial-permitted-subtrees` and union with `initial-excluded-subtrees`, and later processing does not change. So anchor scoping reduces to existing path-validation inputs.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | defines enforcement of anchor scope |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | worked example for R-I-02 |

- **R-I-02**: this is the operation our local policy would perform on an imported anchor, and it is plain set arithmetic over subtrees.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, §2, §3.1 and the name-constraint steps of §3.2, §5 by section. The remaining §3.2 steps and §4 were not read.

- Category Informational: this is one way to do it, not a requirement.
- §5 notes the failure case: paths rejected by an enforcing implementation may be accepted by one that does not enforce. Support was not surveyed.
