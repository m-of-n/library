---
schema: "library-summary/v1"
id: rfc-5914
record: rfc-5914
type: summary
updated: "2026-11-04"
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
| **Digest** | `sha256:0ad7784e…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

§1 notes there was no standard format for trust anchor information. RFC 5914 defines `TrustAnchorInfo`, which wraps a public key with a title and `CertPathControls` (policies, policy flags, `nameConstr`, `pathLenConstraint`), and §1 says it provides "a means of associating additional or alternative constraints with certificates without breaking the signature on the certificate". Whoever holds the anchor store can thus scope an anchor without the issuer re-signing it; that reading is ours. §4 draws the security consequence: where TA-based constraints are enforced, an unauthorised holder of a compromised anchor key is limited by those controls.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a containment mechanism for anchors |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a precedent, partly a counterpoint, for R-I-02 |

- **R-I-02** (import SHALL NOT require the foreign object to become a native trust anchor): TAF shows a relying party attaching its own constraints to a foreign key without changing the foreign object. It is also a counterpoint: TAF still makes that key a trust anchor, which R-I-02 says import must not require.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-5280` is reference [RFC5280], under `cites`, and also authors its own `see_also` here. `rfc-5937` and `rfc-6818` each cite this RFC, so those edges sit under their `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, the §2 syntax, §4 and the reference list, by section. §3 and the ASN.1 modules were not read. Quotes re-checked against the text 2026-11-04.

- Whether any mainstream verifier consumes this format was not checked; the source does not say.
- Enforcement is specified in `rfc-5937`. There the `enforceTrustAnchorConstraints` input is optional, but `CertPathControls` in a `TrustAnchorInfo` "MUST be processed" in all cases (RFC 5937 §2), and an implementation without the input MUST behave as if it were TRUE (§3.1).
- Errata exist per RFC metadata and were not read.
