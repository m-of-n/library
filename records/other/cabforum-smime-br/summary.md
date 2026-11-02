---
schema: "library-summary/v1"
id: cabforum-smime-br
record: cabforum-smime-br
type: summary
updated: "2026-11-01"
---

# CA/Browser Forum Baseline Requirements for S/MIME Certificates

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: adopted CA/Browser Forum requirements, not an IETF or ISO standard |
| **Authors** | CA/Browser Forum |
| **Published** | 2026-09-28 |
| **Identifier** | S/MIME BR v1.0.16 |
| **Source** | https://github.com/cabforum/smime/blob/main/SBR.md (raw) |
| **Digest** | `sha256:fa30ec6c…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

These requirements govern publicly trusted S/MIME certificates. The clause that matters here is the name-constraints footnote in the certificate profile: non-critical constraints are allowed as an exception to RFC 5280 "until the `nameConstraints` extension is supported by Application Software Suppliers whose software is used by a substantial portion of Relying Parties worldwide". A Subordinate CA with `id-kp-emailProtection` is technically constrained only if it carries `nameConstraints` (§7.1.5). So the mechanism is required for the status and admitted to be incompletely supported.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | rules for a real email-identity PKI |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | what an S/MIME import inherits |

- **R-I-05**: a certificate imported under these rules may carry a constraint some clients do not enforce, so an importer must not treat constraint presence as proof of scope.

The `contradicts: rfc-5280` edge records the deliberate exception on criticality.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** front matter, revision table lines, and name-constraint passages by keyword. This long document was not read through; identity validation and audit clauses were not read.

- The footnote's condition has no measurable test.
- The ballot history was not traced, so R-001 §4.4's "2023" dating was not checked.
