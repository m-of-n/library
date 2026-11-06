---
schema: "library-summary/v1"
id: rfc-6960
record: rfc-6960
type: summary
updated: "2026-11-04"
---

# X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | S. Santesson, M. Myers, R. Ankney, A. Malpani, S. Galperin, C. Adams |
| **Published** | 2013-06 |
| **Identifier** | RFC 6960 · DOI 10.17487/RFC6960 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6960.txt |
| **Digest** | `sha256:7e63ffa1…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

OCSP lets a client ask for one certificate's status without fetching a CRL. Definitive responses are signed by the issuing CA, a trusted responder, or a delegate holding a certificate issued directly by that CA with `id-kp-OCSPSigning` (§2.2, §4.2.2.2). §5 is candid: the service is only effective if the client can connect, signing makes query floods worse, and precomputed responses allow replay until they expire. Our reading, from the other records in this topic, is that the operational dependency, not the message design, is what failed.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | a live revocation channel |
| Cryptography | `adjacent` | signed status statements |
| This project | `adjacent` | what R-O-02 prefers not to depend on |

- **R-O-02** (short-lived validity preferred over revocation-heavy design; revocation still representable) and **R-M-09** (validity intersection, time window ∩ optional online checks): OCSP is the canonical optional online check. If we keep one, §5's warnings are the requirements.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also: letsencrypt-ocsp-eol`: Let's Encrypt turned its OCSP service off on 2025-08-06 and publishes revocation only through CRLs: a large CA retiring this protocol.
- `see_also: cabforum-sc063`: the ballot that made OCSP optional for CAs under the TLS Baseline Requirements.
- `rfc-5280` is reference [RFC5280], under `cites`; it also authors its own `see_also` here. `rfc-7633` authors the edge from TLS Feature to this RFC, and `rfc-9608` cites it; neither is repeated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §2.2, §4.2.2.2, §5 and the reference list, by section. The ASN.1, extensions and the §4.1 request syntax were not read. Re-checked against the text 2026-11-04.

- It does not say what a client should do when a response cannot be obtained, except that CRL fallback is possible (§5); soft-fail is deployment behaviour (`langley-2014-revchecking`).
- RFC 8954 and RFC 9654 update it and were not read. Errata exist per RFC metadata and were not read.
