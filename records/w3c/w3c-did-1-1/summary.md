---
schema: "library-summary/v1"
id: w3c-did-1-1
record: w3c-did-1-1
type: summary
updated: "2026-11-01"
---

# Decentralized Identifiers (DIDs) v1.1

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `draft`: W3C Candidate Recommendation Snapshot; not a Recommendation (see Limits) |
| **Authors** | Manu Sporny, Dmitri Zagidulin |
| **Published** | 2026-03-05 |
| **Identifier** | W3C CR-did-1.1-20260305 |
| **Source** | https://www.w3.org/TR/did-1.1/ |
| **Digest** | `sha256:4a48022d…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DID v1.1 defines a URI scheme, `did:<method>:<id>`, plus a document data model that lists verification material. Its design goal in the abstract is that a controller can prove control "without requiring permission from any other party", decoupled from central registries, providers and CAs. The core specification does not define trust: that lies in each method, and resolution is out of scope here, in a separate specification. So it standardises a shape around identifiers, and the governance question is delegated to methods.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | control proofs depend on each method |
| Cryptography | `adjacent` | carries verification material |
| This project | `adjacent` | one DEC-003 option |

- **DEC-003**: gives a uniform identifier syntax, but the security comes from the method.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, status section, and keyword-located parts; the security and privacy considerations and the data model were not read through.

- **Standing:** a Candidate Recommendation that asks for experimental implementations and warns of change. We set `draft`, not `recommendation`, because the schema's `recommendation` would read as a finished Recommendation. `w3c-did-core` is the 1.0 record, still a stub; the line between the two was not checked.
- Says nothing about any method's security.
