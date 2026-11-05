---
schema: "library-summary/v1"
id: rfc-7633
record: rfc-7633
type: summary
updated: "2026-11-04"
---

# X.509v3 Transport Layer Security (TLS) Feature Extension

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | P. Hallam-Baker |
| **Published** | 2015-10 |
| **Identifier** | RFC 7633 · DOI 10.17487/RFC7633 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7633.txt |
| **Digest** | `sha256:7e69fff0…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 7633 defines an X.509 extension, `id-pe-tlsfeature` (§4), listing TLS features a server's certificate commits it to support; used with `status_request` it is commonly called OCSP Must-Staple, a name the RFC does not use. Per §3, a certificate marked this way lets the client fail immediately when the staple is missing, which removes the need to query the responder and prevents a denial-of-service attack made by blocking the OCSP response or the responder. §5.1 limits the claim. It is a post-issue control, so it helps with a certificate compromised after issue and not with an unmarked one obtained by fraud.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | closes the soft-fail gap, where enforced |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02** (short-lived validity preferred over revocation-heavy design): promises in the certificate shift the fail-closed decision, but `chung-2018-must-staple` shows the rest of the system was not ready.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also: rfc-6960`: this extension exists to make OCSP stapling mandatory. The RFC itself cites the stapling extensions (RFC 6066, RFC 6961), not RFC 6960, so this is our edge, not a citation.
- `rfc-5280` is reference [RFC5280], under `cites`. `chung-2018-must-staple` and `larisch-2017-crlite` cite this RFC, and `langley-2014-revchecking` authors its own edge here; none is repeated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1 to §5 and the reference list, by section. Appendix A was not read. Re-checked against the text 2026-11-04.

- §4.3.3 requires a conforming client to treat the certificate as invalid when a requested feature is missing, but §4.2.3.1 lets a client accept the configuration if validity is established another way, and nothing reaches clients that never implemented the RFC. `chung-2018-must-staple` measured that enforcement as largely missing.
- Let's Encrypt no longer serves OCSP (`letsencrypt-ocsp-eol`), so for its certificates this extension has nothing to staple; other CAs were not checked.
- Errata exist per RFC metadata and were not read.
