---
schema: "library-summary/v1"
id: fda-premarket-cybersecurity-guidance
record: fda-premarket-cybersecurity-guidance
type: summary
updated: "2026-10-02"
---

# FDA: Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions

|  |  |
|---|---|
| **Type** | spec (final guidance for industry and FDA staff; contains nonbinding recommendations) |
| **Maturity** | best-practice. Agency guidance under 21 CFR 10.115; its restatements of FD&C Act 524B and 21 CFR 820 are binding law. |
| **Authors** | U.S. FDA: Center for Devices and Radiological Health (CDRH), Center for Biologics Evaluation and Research (CBER) |
| **Published** | 2026-02-03 (Level 2 revision; supersedes the 2025-06-27 final) |
| **Identifier** | Docket FDA-2021-D-1158; document number GUI00001825 |
| **Source** | https://www.fda.gov/media/119933/download (PDF, 64 pp., `Premarket-Cybersecurity-Guidance-2026.pdf`, Last-Modified 2026-02-03) |
| **Digest** | `d046fa836048933e1a8795bcf2f8224bcfa08789c2f3ef6f46ae53c2eb096c54` (re-fetched and re-hashed 2026-10-02: identical) |

## Overview

FDA treats cybersecurity as part of device safety and effectiveness and as part of the Quality Management System
Regulation (21 CFR 820, which incorporates ISO 13485:2016 since 2 February 2026). It recommends a **Secure Product
Development Framework (SPDF)** as one way to satisfy the QMSR.

The guidance then specifies what a premarket submission should contain to show that the SPDF worked:
- a security risk management report built around a threat model, an exploitability-based cybersecurity risk
  assessment, an SBOM with component support status, and vulnerability and unresolved-anomaly assessments, with
  **traceability** across all of them;
- security requirements and the eight control categories of Appendix 1;
- four kinds of security architecture view;
- layered security testing, including penetration testing with independence;
- user-facing labeling;
- a postmarket cybersecurity management plan.

For **cyber devices** (FD&C Act 524B, added by FDORA 2022), three items are statutory: the postmarket plan with CVD,
the processes giving reasonable assurance of cybersecurity, and the SBOM.

## Version and currency (checked 2026-10-02)

- The cached PDF is the **February 3, 2026** document. Its cover says: "This document supersedes ... issued June 27,
  2025". The download URL still serves byte-identical bytes, with Last-Modified 2026-02-03.
- Guidance History table (in the document):
  - Sept 2023: final;
  - March 2024: reissued as a Level 1 draft;
  - June 2025: Level 1 final;
  - Feb 2026: Level 2 revisions to align with the amended QMSR.
- The FDA guidance landing page URL we tried returned 404, so currency rests on the PDF's own statements and the live
  download.
- Older versions are not separate records (one record per document line). Their history is noted here.
- The FDA Recognized Consensus Standards status of IEC 81001-5-1 and ANSI/ISA 62443-4-1 is recorded in those records.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A regulator's detailed expectations for secure development evidence, with the threat model at the centre. |
| Cryptography | adjacent | App. 1 C and App. 2.B ask for algorithm, key length, mode, key management and PKI details, and expert analysis of proprietary crypto. No algorithms are mandated. |
| This project | core | It bears on **R-042**: a threats → risks → controls → requirements → tests traceability chain is the review expectation. It also bears on **R-040** (technical, documentation and process mitigations, plus compensating controls and risk transfer), **R-041** (the premarket submission as a gate; Table 1 as exit criteria; SPDF metrics), **R-043** (architecture views and reports are governed views), **R-044** (it names 62443-4-1, IEC 81001-5-1, JSP2, AAMI TIR57/SW96) and **DEC-009** (the vulnerability disposition lifecycle). |

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| MDIC/MITRE Playbook for Threat Modeling Medical Devices | Method guide cited at fn 34 | free | (MITRE site returned 403 on 2026-10-02; URL not verified) |
| MDS2 form (NEMA/HIMSS) | Manufacturer disclosure statement cited in §VI.A | free | (NEMA; URL not verified) |
| SPDX / CycloneDX | SBOM formats ("industry-accepted formats") | open | records `spdx-3-0-1`, `cyclonedx-1-7` |

Commercial premarket-cybersecurity tooling exists; none was evaluated (searched 2026-10-02).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, FX-1 distillation block |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | verbatim normative paragraphs in source order |
| `distilled/requirements.yaml` | 426 entries, library-requirements/v2, with reconciled own-form counts |
| `distilled/messages.yaml` | 18 documentation structures, 157 fields |
| `distilled/schema/` | 4 derived JSON Schemas |
| `distilled/examples/` | fixtures for every illustrative example |
| `distilled/state-machine.yaml` | vulnerability disposition; device support lifecycle |
| `distilled/design-notes.md` | adopt / adapt / reject; open questions |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (46 objects, 42 edges) |

## Limits

- It is premarket only. Postmarket handling (controlled vs uncontrolled risk examples, CVD timelines, 21 CFR 806) is
  in the 2016 Postmarket Cybersecurity Guidance, which is not yet in the library.
- The recommendations are non-binding and "expected to scale" with cybersecurity risk. No numeric thresholds are given
  apart from the "e.g., annually" testing interval.
- There is no data format: every schema here is derived.
- Medical-device specific. Its "security risk vs safety risk" split is valuable but tied to ISO 14971.
- Verify and cross-check passes done 2026-10-02 by an independent verifier; defects and residual issues in `distilled/verification.md`.
