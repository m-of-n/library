---
schema: "library-summary/v1"
id: rfc-7633
record: rfc-7633
type: summary
updated: "2026-11-01"
---

# X.509v3 TLS Feature Extension (OCSP Must-Staple)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | P. Hallam-Baker |
| **Published** | 2015-10 |
| **Identifier** | RFC 7633 · DOI 10.17487/RFC7633 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7633.txt |
| **Digest** | `sha256:7e69fff0…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 7633 defines an X.509 extension, `id-pe-tlsfeature`, listing TLS extensions a server promises to support. Its main use is OCSP stapling: a certificate marked this way tells the client that a missing staple is an immediate failure, which removes the soft-fail attack. §5.1 limits the claim. It is a post-issue control, so it helps with a certificate compromised after issue and not with an unmarked one obtained by fraud.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | closes the soft-fail gap |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: promises in the certificate shift the fail-closed decision, but `chung-2018-must-staple` shows the rest of the system was not ready.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, §4 and §4.1, §5 by section. §4.2 onward's CSR and use rules and Appendix A were not read.

- Its protection depends on every client enforcing it, which the RFC cannot require and `chung-2018-must-staple` measured as missing.
- Let's Encrypt, which `chung-2018-must-staple` calls the most popular CA, no longer serves OCSP, so this is largely historical for the Web PKI; we did not check other CAs.
- Errata exist per RFC metadata and were not read.
