---
schema: "library-summary/v1"
id: go-nameconstraint-cves
record: go-nameconstraint-cves
type: summary
updated: "2026-11-01"
---

# Go crypto/x509 name-constraint defects (five CVEs, 2025-2026)

|  |  |
|---|---|
| **Type** | dataset (five CVE records) |
| **Maturity** | `informational`: vulnerability records |
| **Authors** | Go Security Team |
| **Published** | 2026-04-08 |
| **Identifier** | CVE-2025-58187, -61727, CVE-2026-27137, -27138, -33810 |
| **Source** | https://cveawg.mitre.org/api/cve/ (one record each) |
| **Digest** | `sha256:bb5fc0c5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Five CVEs assigned by the Go project show `crypto/x509` getting name-constraint checking wrong in five ways. CVE-2025-58187 is non-linear processing time as certificates grow. CVE-2025-61727 lets a wildcard SAN escape an excluded subdomain. CVE-2026-27137 makes several email constraints collapse so that "only the last constraint will be considered". CVE-2026-27138 panics on an empty DNS name when another certificate has excluded constraints. CVE-2026-33810 misses excluded DNS constraints for wildcard SANs in a different case. Three of the five are incorrect allow decisions, one is denial of service by cost and one by crash.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | constraint checks failed open in a current verifier |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence about how hard this semantics is, not a dependency |

- **R-M-08** (intersection semantics defined for every tag profile): the wildcard, case and email defects are all set-membership errors in a constraint language. Our tag intersection is the same class of problem.
- **R-M-01**: this is part of the cost of carrying X.509 semantics natively.

## Implementations

Fixes are in Go's standard library. The records give fixed versions: 1.24.9 and 1.25.3 (58187), 1.24.11 and 1.25.5 (61727), 1.26.1 (27137, 27138), 1.26.2 (33810).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the five MITRE records whole: title, description, references, affected versions. The linked Go issues, CLs and advisories were not read, so root causes are as the CVE text states them.

- The publication dates run from 2025-10-29 to 2026-04-08, which is 161 days. R-001 §4.5 says "within eleven months": true, but it understates the clustering.
- Three of the affected ranges start at Go 1.26.0, so those look recent. CVE-2025-58187 and CVE-2025-61727 show ranges from version 0.
- Five CVEs in one implementation is not a rate, and no comparison with other verifiers was made.
- The records do not show whether other verifiers have the same faults; that was not examined.
