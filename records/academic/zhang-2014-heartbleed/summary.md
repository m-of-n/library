---
schema: "library-summary/v1"
id: zhang-2014-heartbleed
record: zhang-2014-heartbleed
type: summary
updated: "2026-11-01"
---

# Analysis of SSL Certificate Reissues and Revocations in the Wake of Heartbleed

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IMC '14) |
| **Maturity** | `informational`: research paper |
| **Authors** | Liang Zhang, David Choffnes, Dave Levin, Tudor Dumitraș, Alan Mislove, Aaron Schulman, Christo Wilson |
| **Published** | 2014-11 |
| **Identifier** | DOI 10.1145/2663716.2663758 |
| **Source** | author-hosted PDF |
| **Digest** | `sha256:5d1e0a43…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Heartbleed gave administrators a clear moment when they should have revoked, so the paper uses it as a natural experiment over all certificates advertised by the Alexa Top 1 Million for six months. Three weeks after disclosure, over 73% of vulnerable certificates had not been reissued and over 87% had not been revoked. Of domains that reissued, 60% did not revoke the old certificate. Revocations also dropped sharply on weekends. The argument is that revocation is a manual process and behaves like one.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | quantifies the human dependency in revocation |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: expiry needs nobody to act, and this measures what happens when revocation does.

## Implementations

None: a measurement study.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction and concluding discussion, with results searched for the figures above.

- Alexa Top 1M only, so not the whole Web PKI.
- It measures operators' behaviour, and says nothing about whether clients would have honoured the revocations (`liu-2015-revocation` covers that).
