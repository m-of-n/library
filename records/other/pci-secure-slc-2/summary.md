---
schema: "library-summary/v1"
id: pci-secure-slc-2
record: pci-secure-slc-2
type: summary
updated: "2026-10-03"
---

# PCI Secure Software Lifecycle (Secure SLC) Standard v2.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard (PCI SSC published standard) |
| **Authors** | PCI Security Standards Council |
| **Published** | 2026-09-28 (per the PCI SSC blog announcement) |
| **Identifier** | https://www.pcisecuritystandards.org/standards/secure-software-lifecycle/ |
| **Source** | https://blog.pcisecuritystandards.org/pci-ssc-releases-version-2.0-of-the-secure-software-lifecycle-standard |
| **Digest** | public blog HTML only (see `record.yaml`); the standard itself was **not** downloaded |

**Coverage warning.** The standard sits behind the PCI SSC document-library licence
agreement, which we did not accept on the project's behalf. Everything below comes from
public PCI SSC pages and the release announcement. No requirement text has been read or
extracted; this record must not be cited for requirement content.

## Overview

The Secure SLC Standard is the PCI Software Security Framework's process standard: it
assesses a **software vendor's secure development lifecycle**, while its sibling, the PCI
Secure Software Standard v2.0 (January 2026), assesses the payment software product
itself. Version 2.0 is described by PCI SSC as "refocused solely on a software vendor's
Secure SLC", with "objective" requirements. It introduces the concept of **sensitive
assets**, documented in a Sensitive Asset Identification Document (SAID), and extends
scope to "digital tools", including AI used in development. It is assessed by qualified
assessors, with Report on Validation / Attestation of Validation templates and a public
listing of validated vendors. A 12-month transition from v1.1 starts once assessor training
is available (announced for Q4 2026).

## Why it matters for an SDL

It is one of the few SDL standards with an **independent assessment and public listing
programme**, alongside IEC 62443-4-1 (ISASecure SDLA). The SSDF 1.1 References column and
ETSI TS 104 219 Annex B.2 map to its v1.x predecessor (`[PCISSLC]`).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | assessed SDL process standard |
| Cryptography | adjacent | payment-software context |
| This project | adjacent | precedent for gate/assessment objects (R-041, R-042); content not usable until licensed |

## Implementations

Assessment programme run by PCI SSC (Secure Software Assessors). No open-source tooling
searched (2026-10-03).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/object-model.yaml`, `object-model.md` | objects/edges from **public programme material only** (16 objects, 9 edges, 2 inferred) |

## Limits

No requirement, control objective or test procedure has been read. Re-ingest from a
licensed copy before using it in MAP-0001 or the conformance model.
