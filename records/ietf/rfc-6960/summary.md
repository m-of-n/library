---
schema: "library-summary/v1"
id: rfc-6960
record: rfc-6960
type: summary
updated: "2026-11-01"
---

# X.509 Internet PKI Online Certificate Status Protocol (OCSP)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | S. Santesson, M. Myers, R. Ankney, A. Malpani, S. Galperin, C. Adams |
| **Published** | 2013-06 |
| **Identifier** | RFC 6960 · DOI 10.17487/RFC6960 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6960.txt |
| **Digest** | `sha256:7e63ffa1…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

OCSP lets a client ask for one certificate's status without fetching a CRL. Definitive responses are signed by the issuing CA, a trusted responder, or a delegate holding a certificate issued directly by that CA with `id-kp-OCSPSigning` (§2.2, §4.2.2.2). §5 is candid: the service is only effective if the client can connect, signing makes query floods expensive, and precomputed responses allow replay until they expire. The protocol's design is sound; what the other records in this topic show is that its operational dependency is the problem.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | a live revocation channel |
| Cryptography | `adjacent` | signed status statements |
| This project | `adjacent` | what R-O-02 prefers not to depend on |

- **R-O-02** and **R-M-09** (validity intersection, time window with optional online checks): OCSP is the canonical optional online check. If we keep one, §5's three warnings are the requirements.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §2.2, §4.2.2.2, §5 by section. The ASN.1, extensions and the §4.1 request syntax were not read.

- It does not say what a client should do when a response cannot be obtained, except that CRL fallback is possible; soft-fail is deployment behaviour (`langley-2014-revchecking`).
- RFC 8954 and RFC 9654 update it and were not read. Errata exist per RFC metadata and were not read.
- `cabforum-sc063` and `letsencrypt-ocsp-eol` show it being retired from the Web PKI.
