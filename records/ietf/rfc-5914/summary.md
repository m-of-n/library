---
schema: "library-summary/v1"
id: rfc-5914
record: rfc-5914
type: summary
updated: "2026-11-01"
---

# Trust Anchor Format

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | R. Housley, S. Ashmore, C. Wallace |
| **Published** | 2010-06 |
| **Identifier** | RFC 5914 · DOI 10.17487/RFC5914 |
| **Source** | https://www.rfc-editor.org/rfc/rfc5914.txt |
| **Digest** | `sha256:0ad7784e…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

There was no standard format for trust anchor information, and a self-signed certificate cannot gain constraints without breaking its signature. RFC 5914 defines `TrustAnchorInfo`, which wraps a public key with a title and `CertPathControls`, including policies, `nameConstr` and path length. The relying party can thus scope an anchor. §4 draws the conclusion: a stolen anchor key is still limited by those controls, where they are enforced.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a containment mechanism for anchors |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a precedent for R-I-02 |

- **R-I-02** (import must not make the foreign object a native trust anchor) and **R-I-05**: a local wrapper that holds the foreign key plus our constraints is the structure these requirements describe.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, the §2 syntax, §4 by section. §3 and the ASN.1 modules were not read.

- Whether any mainstream verifier consumes this format was not checked; the source does not say.
- Enforcement is `rfc-5937`'s business and is optional there.
- Errata exist per RFC metadata and were not read.
