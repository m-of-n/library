---
schema: "library-summary/v1"
id: chung-2018-must-staple
record: chung-2018-must-staple
type: summary
updated: "2026-11-04"
---

# Is the Web Ready for OCSP Must-Staple?

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IMC '18) |
| **Maturity** | unset: a conference paper; no body assigns it a standing |
| **Authors** | Taejoong Chung, Jay Lok, Balakrishnan Chandrasekaran, David Choffnes, Dave Levin, Bruce M. Maggs, Alan Mislove, John Rula, Nick Sullivan, Christo Wilson |
| **Published** | 2018-10 |
| **Identifier** | DOI 10.1145/3278532.3278543 |
| **Source** | author-hosted PDF |
| **Digest** | `sha256:de000fb8…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |

## Overview

OCSP Must-Staple can only work if CAs, web servers and browsers all act correctly, so the paper tests each. Only 29,709 certificates (0.02%) used it (§4), and over four months responders showed outages and returned invalid responses. Of the major browsers only Firefox enforced it, and not on iOS. Apache and Nginx do not prefetch responses, and Apache had two further faults (§7, Table 3). The conclusion is that "the web is not ready for OCSP Must-Staple" (§8), though the paper thinks few parties need to act.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | an end-to-end test of hard-fail revocation |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02** (short-lived validity preferred over revocation-heavy design): every party had to change for this revocation design to work, and they had not. The paper draws the opposite lesson, that the fix is within reach; preferring short validity is our reading.

## Implementations

Apache 2.4.18 and Nginx 1.13.12 were tested (§7). The paper says its code and data would be published (§8); that release was not located or checked.

## Relations

No `see_also` edges. Every library record this paper relates to is one it cites, so the edges are under `cites` in `record.yaml`, with reference numbers: `rfc-5280`, `rfc-7633`, `langley-2014-revchecking`, `rfc-6962`, `larisch-2017-crlite`, `liu-2015-revocation`, `rfc-6960`, `zhang-2014-heartbleed`. Only references the library holds are listed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction and contributions, §7's web-server results, the concluding section (§8) with recommendations, and the reference list, from the author copy. Methods and per-CA results were not read through, only searched for the figures above. Figures and quotes re-checked against the PDF 2026-11-04.

- 2018 snapshot. `letsencrypt-ocsp-eol` shows the largest CA has since turned OCSP off, so the paper's optimism was overtaken.
- The abstract's claim that wider deployment is "realistic and achievable" is the paper's forecast, and it did not come true.
