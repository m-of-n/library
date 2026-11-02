---
schema: "library-summary/v1"
id: ccadb
record: ccadb
type: summary
updated: "2026-11-01"
---

# Common CA Database (CCADB) public reports

|  |  |
|---|---|
| **Type** | dataset (index of public reports) |
| **Maturity** | `informational`: operational data service |
| **Authors** | Common CA Database |
| **Published** | 2026 |
| **Identifier** | https://www.ccadb.org/resources |
| **Source** | https://www.ccadb.org/resources |
| **Digest** | `sha256:ef0c8207…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CCADB is the shared database in which root store operators and CAs record certificates, audits and policies. The Resources page indexes per-program reports for Apple, Google Chrome, Microsoft and Mozilla, plus Cisco's bundles, along with use-case and all-certificate reports. It warns that repurposing a root store for applications that do not match its intended community "can introduce significant risks" and recommends curating a purpose-built store instead. So the data that tells you what a browser trusts is explicitly not offered as something to inherit.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | data about the trust system, not a control |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a data source for analysis, not a dependency |

- **R-I-02** (import must not require the foreign object to become a native trust anchor): CCADB's warning against inheriting a root store is the operators' own form of this rule.

## Implementations

Not applicable. A hosted data service, under the CCADB Data Usage Terms.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the Resources page whole, 2026-11-01. The reports were sampled, not surveyed: only the two Mozilla CSVs behind `survey-2026-nameconstraints-measurement` were downloaded, and the CCADB Policy was not read.

- The page describes the "Mozilla Constrained" style fields as booleans. That is coarser than the "Mozilla Applied Constraints" text field, which `golang-61963` found undocumented.
- Disclosure is not enforcement: the database records what CAs and programs report.
