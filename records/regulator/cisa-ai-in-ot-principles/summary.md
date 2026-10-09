---
schema: "library-summary/v1"
id: cisa-ai-in-ot-principles
record: cisa-ai-in-ot-principles
type: summary
updated: "2026-10-01"
---

# Principles for the Secure Integration of Artificial Intelligence in Operational Technology

|  |  |
|---|---|
| **Type** | spec (joint guidance) |
| **Maturity** | `best-practice` — joint agency guidance; no conformance claim |
| **Authors** | CISA, ASD's ACSC, NSA AISC, FBI, Canadian Centre for Cyber Security, BSI, NCSC-NL, NCSC-NZ, NCSC-UK |
| **Published** | 2025-12-03; PDF revision 508cV2, January 2026 |
| **Identifier** | CISA joint guidance |
| **Source** | https://www.cisa.gov/sites/default/files/2026-01/joint-guidance-principles-for-the-secure-integration-of-artificial-intelligence-in-operational-technology-508cV2.pdf |
| **Digest** | `sha256:1fde3cbaadf9f75411158a144595631f8dd4029e52b11545c49811d29f531560` |

## Overview

Guidance from nine agencies for critical-infrastructure operators putting AI into
operational technology, as four principles in twelve subsections: **understand AI** (a
risk table including prompt injection, drift, explainability and reliability — LLMs
"almost certainly should not be used to make safety decisions for OT environments",
§1.1); **consider AI use in the OT domain** (decide first whether AI is the right tool,
protect OT data, demand vendor transparency including an SBOM covering AI, keep a failsafe
fallback, §2); **governance and assurance** (roles, audits, integrate AI into existing
security frameworks, test on non-production first, §3); and **oversight and failsafes**
(inventory AI components, log inputs and outputs, human-in-the-loop decisions, anomaly
detection, AI red teaming, §4). It is written as recommendations ("should", "may"), not
requirements.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Security guidance for AI systems |
| Cryptography | `none` | Encryption is mentioned only generically |
| This project | `adjacent` | Its threat-modeling and oversight recommendations bear on tmodel directly |

`bears_on: DEC-001` — threat models should include AI-specific attack vectors such as
adversarial inputs and data poisoning (§4.1) and use **MITRE ATLAS** alongside ATT&CK
(§3.2). `bears_on: R-018` — human-in-the-loop decision-making and an audit trail of AI
inputs and outputs, with the AI's identity logged separately from users and machines
(§4.1).

## Implementations

Nothing to list. This document is a set of recommended practices, not a file format or protocol, so no software "implements" it. Tools that support individual recommendations (for example, MITRE ATLAS for AI threat modeling) belong in their own records.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **OT-specific.** Much of it (latency, safety certification, push-based architectures)
  assumes industrial control systems; the general AI-security recommendations have to be
  picked out.
- **No conformance.** Recommendations only; nothing defines how compliance is checked.
- **Points elsewhere for requirements.** It names ETSI TR 104 128, TS 104 223 and TR 104 048
  as the top AI technical standards (§3.4); those, not this guidance, carry testable
  requirements. TS 104 223 is now EN 304 223.
