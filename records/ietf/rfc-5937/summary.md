---
schema: "library-summary/v1"
id: rfc-5937
record: rfc-5937
type: summary
updated: "2026-11-04"
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
| **Digest** | `sha256:6424a9b1…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | none: `errata_url` is null in rfc5937.json, checked 2026-11-04 |

## Overview

RFC 5280 permits an implementation to use extra trust anchor data but leaves the processing unspecified (§1, pointing to RFC 5280 §6.2). RFC 5937 fills that in with one added input, `enforceTrustAnchorConstraints` (§3.1), and initialisation steps that (or equivalent ones) MUST run before RFC 5280's (§3.2). Name constraints on the anchor intersect with the user's `initial-permitted-subtrees` and union with `initial-excluded-subtrees`, and post-initialisation processing is not affected (§1). So name and policy scoping on an anchor reduce to existing path-validation inputs; path length does not, since RFC 5280 has no input for it and §4 says a wrapper cannot enforce it by pre-processing.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | defines enforcement of anchor scope |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | worked example for R-I-02 |

- **R-I-02** (import SHALL NOT require the foreign object to become a native trust anchor): this is the operation a local policy would perform to scope a foreign key, and it is plain set arithmetic over subtrees. It still works on a trust anchor, so it is a technique to borrow, not a model of R-I-02 itself.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-5280` and `rfc-5914` are references [RFC5280] and [RFC5914], under `cites`; `rfc-5280` also authors its own `see_also` here. `rfc-6818` cites this RFC, so that edge sits under its `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1 to §5 and the reference list, by section. Re-checked against the text 2026-11-04.

- Category Informational: this is one way to do it, not a requirement on RFC 5280 implementations.
- §5 notes the failure case: paths rejected by an enforcing implementation may be accepted by one that does not enforce. Support was not surveyed.
