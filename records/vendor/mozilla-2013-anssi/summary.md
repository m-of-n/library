---
schema: "library-summary/v1"
id: mozilla-2013-anssi
record: mozilla-2013-anssi
type: summary
updated: "2026-11-01"
---

# Revoking Trust in one ANSSI Certificate

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: vendor announcement |
| **Authors** | Kathleen Wilson |
| **Published** | 2013-12-09 |
| **Identifier** | Mozilla Security Blog, 2013-12-09 |
| **Source** | https://blog.mozilla.org/security/2013/12/09/revoking-trust-in-one-anssi-certificate/ |
| **Digest** | `sha256:369e88e3…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A subordinate CA of ANSSI, a French government agency operating the IGC/A root, issued an intermediate that was loaded into a man-in-the-middle traffic device and used to generate certificates for domains its owner did not control. Mozilla revoked trust in the subordinate certificate through a certificate store update. ANSSI's root issues certificates for French government sites, yet the intermediate could sign for anyone, and the fix reached users only through a browser update. Google reported it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | unscoped delegation misused |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-M-03 |

- **R-M-03**: a CA whose legitimate scope was one government's sites held power over every name.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** post whole, not the comments.

- Mozilla believed the use was confined to the subordinate CA's internal network; the post states this as belief, not a finding.
- It does not say whether a name constraint existed or would have helped.
