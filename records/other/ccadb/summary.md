---
schema: "library-summary/v1"
id: ccadb
record: ccadb
type: summary
updated: "2026-11-04"
---

# Common CA Database (CCADB) public reports

|  |  |
|---|---|
| **Type** | dataset (index of public reports) |
| **Maturity** | unset: an operational data service, no standing to verify |
| **Authors** | Common CA Database |
| **Published** | 2026 |
| **Identifier** | https://www.ccadb.org/resources |
| **Source** | https://www.ccadb.org/resources |
| **Digest** | `sha256:92273cd0…` (full value in `record.yaml`), fetched 2026-11-04; the 2026-11-01 digest is superseded by a page edit, see `content.note` |

## Overview

CCADB is the shared database in which root store operators and CAs record certificates, audits and policies. The Resources page indexes per-program reports for Apple, Google Chrome, Microsoft and Mozilla, plus Cisco's bundles, along with use-case and all-certificate reports. It warns that re-purposing a root store for applications that do not perfectly align with its intended products, communities or policies "can introduce significant risks to security and interoperability" and says it is in most cases "far more appropriate and secure to curate a purpose-built root store". So the data that tells you what a browser trusts is published with a warning against inheriting it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | data about the trust system, not a control |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a data source for analysis, not a dependency |

- **R-I-02** (import must not require the foreign object to become a native trust anchor): CCADB's warning against adopting another program's root store wholesale is an operator-side caution in the same direction. It is an analogy, not the same rule: CCADB speaks of choosing anchors, R-I-02 of what import may require.

## Relations

- `golang-61963` authors the `see_also` edge to this record (the Go issue turns on Mozilla's `*.tr` constraint existing only in CCADB's "Mozilla Applied Constraints" field); it is not duplicated here.
- The edge from `survey-2026-nameconstraints-measurement`, whose CSVs come from these reports, is authored on that record.

## Implementations

Not applicable. A hosted data service; the page states the CCADB Data Usage Terms apply to all data it hosts.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the Resources page whole, 2026-11-01, and again 2026-11-04 after its digest changed. The reports were sampled, not surveyed: only the two Mozilla CSVs behind `survey-2026-nameconstraints-measurement` were downloaded, and the CCADB Policy was not read.

- The page describes the "Mozilla Constrained" style fields of the use-case reports as booleans. That is coarser than the "Mozilla Applied Constraints" text field, which `golang-61963` found undocumented.
- Disclosure is not enforcement: the database records what CAs and programs report.
