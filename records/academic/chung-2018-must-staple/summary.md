---
schema: "library-summary/v1"
id: chung-2018-must-staple
record: chung-2018-must-staple
type: summary
updated: "2026-11-01"
---

# Is the Web Ready for OCSP Must-Staple?

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IMC '18) |
| **Maturity** | `informational`: research paper |
| **Authors** | Taejoong Chung, Jay Lok, Balakrishnan Chandrasekaran, David Choffnes, Dave Levin, Bruce M. Maggs, Alan Mislove, John Rula, Nick Sullivan, Christo Wilson |
| **Published** | 2018-10 |
| **Identifier** | DOI 10.1145/3278532.3278543 |
| **Source** | author-hosted PDF |
| **Digest** | `sha256:de000fb8…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

OCSP Must-Staple can only work if CAs, web servers and browsers all act correctly, so the paper tests each. Only 29,709 certificates (0.02%) used it, and over four months responders showed outages and returned invalid responses. Of the major browsers only Firefox enforced it, and not on iOS. Apache and Nginx do not prefetch responses, and Apache had two further faults. The conclusion is that "the web is not ready for OCSP Must-Staple", though the paper thinks few parties need to act.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | an end-to-end test of hard-fail revocation |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02** (short-lived validity preferred over revocation-heavy design): every party had to change for this revocation design to work, and they had not.

## Implementations

Apache and Nginx were tested. The paper says its code and data would be published; that release was not located or checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction and contributions, and the concluding section with recommendations, from the author copy. Methods and per-CA results were not read through, only searched for the figures above.

- 2018 snapshot. `letsencrypt-ocsp-eol` shows the largest CA has since turned OCSP off, so the paper's optimism was overtaken.
- The paper's recommendation that deployment is "realistic and achievable" is its own forecast, and it did not come true.
