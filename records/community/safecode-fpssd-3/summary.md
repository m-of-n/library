---
schema: "library-summary/v1"
id: safecode-fpssd-3
record: safecode-fpssd-3
type: summary
updated: "2026-10-02"
---

# SAFECode — Fundamental Practices for Secure Software Development, 3rd edition

|  |  |
|---|---|
| **Type** | spec (industry practice guide, 38 pp. PDF) |
| **Maturity** | white-paper (industry consortium guidance) |
| **Authors** | Tony Rice (Microsoft), Nazira Carlage (Dell EMC), Josh Brown-White (Microsoft), Wendy Poland (Adobe), Tania Skinner (Intel), Eric Heitzman (Security Compass), Nick Ozmore (Veracode), Danny Dhillon (Dell EMC); contributors incl. Steve Lipner (SAFECode) |
| **Published** | March 2018 |
| **Identifier** | "Essential Elements of a Secure Development Lifecycle Program, Third Edition" |
| **Source** | https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf |
| **Digest** | `9a9a07b5fab1727c5d2e96cec38747e2c1c8508fe1e84a3971618714ecd733ae` |
| **Licence** | "© 2018 SAFECode – All Rights Reserved." (no open licence stated) |

**Version verified 2026-10-02.** safecode.org's resource page for the
publication and its "Secure Development Practices" archive list the 3rd edition
(March 2018) as current; a web search found no 4th edition. Earlier editions:
1st (2008), 2nd (2011), per the executive summary.

## Overview

SAFECode's members (Adobe, Microsoft, Intel, Dell EMC, Siemens, CA, Symantec,
…) describe the secure development practices they actually use ("practiced
practices"): define and track application security controls; secure design
(principles, threat modeling, encryption strategy, identity and access
management, logging); secure coding (standards, safe functions, toolchain,
code analysis, data handling, error handling); third-party component risk;
automated and manual testing; managing security findings (severity, risk
acceptance); vulnerability response and disclosure; and how to plan an SDL
rollout. It is methodology-agnostic and has no phases or gates.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | widely cited practice baseline (cited by NIST SSDF) |
| Cryptography | adjacent | full encryption-strategy section (standards, key lifecycle, agility) |
| This project | core | finding dispositions and TSRV risk acceptance (R-042, DEC-009), "controls as structured data" (R-043), documentation-kind mitigation example (R-040), CWE links per practice (R-044) |

## How it relates to the others

- NIST SSDF cites SAFECode in its references; Microsoft's SDL Resources page
  links SAFECode's third-party-components paper.
- No published mapping to SAMM/BSIMM; MAP-0001 column "SAFECode 2018" uses
  its chapter names.

## Implementations

Searched 2026-10-02: none — SAFECode publishes guidance, not tools.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/normative.md` | eight practice chapters verbatim with statement ids |
| `distilled/requirements.yaml` | 198 entries (195 extract pass + 3 added by the verify pass) |
| `distilled/schema/` | derived records |
| `distilled/protocol.yaml`, `protocol.md` | vulnerability response exchange |
| `distilled/state-machine.yaml` | finding, risk acceptance, reported vulnerability |
| `distilled/examples/` | worked examples |
| `distilled/design-notes.md` | bearing on our design |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- Guidance in lowercase modals; no conformance criteria, phases or gates.
- Dated 2018 (pre-SBOM mandates, pre-AI); third-party guidance defers to a
  separate SAFECode paper; vulnerability handling defers to ISO/IEC 29147/30111.
- The ISO standards table on the Vulnerability Response page is a two-column
  layout that the text capture partly scrambles.
