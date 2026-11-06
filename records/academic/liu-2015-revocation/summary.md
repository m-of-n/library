---
schema: "library-summary/v1"
id: liu-2015-revocation
record: liu-2015-revocation
type: summary
updated: "2026-11-04"
---

# An End-to-End Measurement of Certificate Revocation in the Web's PKI

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IMC '15) |
| **Maturity** | unset: a conference paper; no body assigns it a standing |
| **Authors** | Yabing Liu, Will Tome, Liang Zhang, David Choffnes, Dave Levin, Bruce Maggs, Alan Mislove, Aaron Schulman, Christo Wilson |
| **Published** | 2015-10 |
| **Identifier** | DOI 10.1145/2815675.2815685 |
| **Source** | author-hosted PDF |
| **Digest** | `sha256:6c676ed7…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |

## Overview

Using 74 full IPv4 HTTPS scans, the paper measures who does their part in revocation. Over 8% of fresh certificates are revoked, and fetching revocation information is often expensive. Across 30 browser and OS combinations, it finds that "no browser in its default configuration correctly checks all revocations and rejects certificates if revocation information is unavailable" (§6.3), and mobile browsers never check. Chrome's CRLSet covers 0.35% of all revocations (§7.2). The paper still concludes that revocation "ought not be given up on" (§9), and proposes smaller CRLs, wider OCSP stapling and a modified CRLSet.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | measures the failure of a security control |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02** (short-lived validity preferred over revocation-heavy design): the measured result is inaction at every party. Taking that as the case for short validity is our reading; the paper argues for repairing revocation instead.

## Implementations

None: a measurement study. The paper says its data and browser test suite are at http://www.sslresearch.org (§9); not checked.

## Relations

No `see_also` edges. `zhang-2014-heartbleed`, `langley-2014-revchecking`, `rfc-5280`, `rfc-6960` and `rfc-6962` are references of this paper, under `cites` in `record.yaml`. `larisch-2017-crlite` and `chung-2018-must-staple` cite this paper, and the edge is under their `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction, §4's revocation figures, the browser results (§6.3, §6.5), and the concluding discussion (§9). The scan methodology and per-CA tables were not read through. Figures and the quote re-checked against the PDF 2026-11-04.

- 2015 snapshot of browsers; `chung-2018-must-staple` re-tested them three years later.
- Most of the 8% of *fresh* certificates comes from Heartbleed, per the paper, with over 1% revoked before it. The paper's figure for alive certificates is almost 1%. The three should not be interchanged.
- It does not settle whether strict checking would be deployable.
