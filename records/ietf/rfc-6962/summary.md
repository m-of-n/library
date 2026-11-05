---
schema: "library-summary/v1"
id: rfc-6962
record: rfc-6962
type: summary
updated: "2026-11-04"
---

# Certificate Transparency

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `experimental`: Category Experimental, obsoleted by RFC 9162 |
| **Authors** | B. Laurie, A. Langley, E. Kasper |
| **Published** | 2013-06 |
| **Identifier** | RFC 6962 · DOI 10.17487/RFC6962 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6962.txt |
| **Digest** | `sha256:08fdf31c…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

Certificate Transparency adds public, append-only, auditable logs built on Merkle trees, and a signed timestamp a server can show as evidence of logging. It does not stop misissuance. In its own words the logs "do not themselves prevent misissue" (§1), and §7.2 adds that they do not detect it either: they rely on interested parties, such as domain owners, to monitor them. The hope stated in the abstract is that clients will eventually refuse certificates that do not appear in a log, effectively forcing CAs to log everything they issue.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | detection control for misissuance |
| Cryptography | `adjacent` | Merkle tree proofs |
| This project | `adjacent` | R-O-04 is a Could |

- **R-O-04** (optional registration of statements with a SCITT-like transparency service): CT is the deployed precedent, and §7.2 sets the limit of what such a service can claim.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-9162` carries `supersedes: rfc-6962`, and `larisch-2017-crlite` and `chung-2018-must-staple` list this RFC under their `cites`; none is repeated. `rfc-5280` is reference [RFC5280], under `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, §7 to §7.2, the section list and the reference list. §2 to §5, the tree and client details, were not read here; `rfc-9162` has the algorithms. Quotes re-checked against the text 2026-11-04.

- R-0001 §4.7's claim that RFC 9162 has essentially no deployment was not checked here.
- `superseded_by` is left empty because `rfc-9162` carries the edge. Errata exist per RFC metadata and were not read.
