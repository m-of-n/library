---
schema: "library-summary/v1"
id: golang-61963
record: golang-61963
type: summary
updated: "2026-11-01"
---

# x/crypto/x509roots: TUBITAK Kamu SM SSL Kok Sertifikasi - Surum 1 should be constrained (golang/go#61963)

|  |  |
|---|---|
| **Type** | web (issue tracker) |
| **Maturity** | `informational`: issue thread |
| **Authors** | FiloSottile, rolandshoemaker |
| **Published** | 2023-08-11 |
| **Identifier** | golang/go#61963 |
| **Source** | https://github.com/golang/go/issues/61963 (via the GitHub API) |
| **Digest** | `sha256:945bd859…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Mozilla applies a `*.tr` constraint to one TUBITAK root, but only in CCADB, so Go's root bundle generated from `certdata.txt` carried the root unconstrained. A maintainer found that Mozilla's restrictions are not all encoded in `certdata.txt`, that this is the only additional name constraint, and that the "Mozilla Applied Constraints" field is not explicitly documented. Go's fallback lacked a way to enforce it anyway (issue 57178). The fix was CL 562475, "x509roots: manually exclude a confusingly constrained root".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a constraint lost in export widens trust silently |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | an example for mapping tables, not a design input by itself |

- **R-I-01** (publish what each foreign mapping preserves, drops or infers): a root store is a foreign format, and here the dropped field was the scope.

## Implementations

Not applicable. The bundle is `golang.org/x/crypto/x509roots`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the issue and all 3 comments, whole. CL 562475 itself was not read; its title is all we know of it.

- R-001 §4.5 says Go's bundle "does not carry" the constraint. The thread shows the outcome was excluding the root, so the scope is not lost: the root is gone. The portability point stands, but the summary sentence should say that.
- The thread is from 2023-2024 and does not show what Go does today.
