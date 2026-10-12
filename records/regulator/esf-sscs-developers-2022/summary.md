---
schema: "library-summary/v1"
id: esf-sscs-developers-2022
record: esf-sscs-developers-2022
type: summary
updated: "2026-10-02"
---

# Securing the Software Supply Chain: Recommended Practices Guide for Developers (ESF, 2022)

|  |  |
|---|---|
| **Type** | spec (joint government guidance) |
| **Maturity** | best-practice (advisory) |
| **Authors** | Enduring Security Framework Software Supply Chain Working Panel; issued by NSA, CISA, ODNI |
| **Published** | August 2022 (released 2022-09-01) |
| **Identifier** | ESF Part 1 of 3 (Developers) |
| **Source** | https://media.defense.gov/2022/Sep/01/2003068942/-1/-1/0/ESF_SECURING_THE_SOFTWARE_SUPPLY_CHAIN_DEVELOPERS.PDF (also mirrored on cisa.gov) |
| **Digest** | `72f5bb1f9d5c57066b8149cc1ecb1aa79433c086561c95e786b9b4ef4b0834bf` (64 pp, retrieved 2026-10-02) |

**Currency (checked 2026-10-02 by web search).** No revision of the developer guide found. The
series continues with Part 2 *Suppliers* (2022-10-31) and Part 3 *Customers* (Nov 2022), and was
followed by ESF reports *Recommended Practices for Software Bill of Materials Consumption*
(2023-11) and *Recommended Practices for Managing Open Source Software and SBOM* (2023-12) — none
held yet.

## Overview

A compendium of developer practices organised by lifecycle area — secure product criteria and
management (2.1), develop secure code (2.2), verify third-party components (2.3), harden the build
environment (2.4), deliver code (2.5) — each pairing **threat scenarios** (e.g. insider code
modification in five variants, vulnerable third-party binaries, a four-step build-chain exploit,
signing-server compromise, distribution-system compromise) with **recommended mitigations**
(threat models with two independent approvers and annual refresh, security test plans, release
criteria, authenticated check-in with MFA and peer review, protected production branches, nightly
security builds, compiler hardening flags, OSRB-approved component repositories, SBOM validation,
segregated build networks, hermetic and reproducible builds, isolated signing, signed packages,
TLS distribution). Mitigations are aligned to SSDF tasks (Table 1, Appendix A); Appendix C quotes
SLSA (alpha) build requirements; Appendix D lists attesting artifacts and a 60-question checklist
mapped to SSDF tasks.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the most concrete US-government SDL/supply-chain practice catalogue for developers |
| Cryptography | adjacent | signing, key protection, crypto standards (SP 800-175B), TLS (SP 800-52r2) |
| This project | core | its scenario→mitigation→phase structure is tmodel's own; threat-model governance rules (R-043), release criteria (R-041/R-042), checklist verdicts (R-042), SSDF crosswalk (R-044), mitigation kinds (R-040), DEC-009 |

## Implementations

Searched 2026-10-02: none specific to the guide. Practices are implemented by common tooling
(SAST/DAST/SCA, Sigstore-style signing, hermetic build systems such as Bazel, SLSA provenance
generators) — not assessed here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites, distillation |
| `distilled/README.md` | index |
| `distilled/normative.md` | all extracted statements verbatim + threat scenarios |
| `distilled/requirements.yaml` | 490 typed entries (463 pass 1 + 27 added in pass 2) incl. 60 SSDF-mapped checklist questions |
| `distilled/crosswalk.yaml` | Table 1, Appendix A, Appendix B transcribed |
| `distilled/object-model.*` | object-model pass (27 objects, 22 edges) |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/esf-sscs-developers-2022.{pdf,txt,raw.txt}`.

## Limits

Advisory, long and repetitive; most statements are "should" without pass/fail thresholds (a few
exceptions: pen test at least yearly, threat-model refresh at least annually, ≥2 reviewers).
Written against the SSDF 1.1 *draft* (cites PW.3) and SLSA *alpha*. Requirement extraction is
semi-automated (sentence selection by normative markers + all items under "Recommended
mitigations"); derived fields (actor, phase, deliverables) are heuristics pending human review.
Section sub-numbering cited by its own appendices (2.2.1.4 etc.) does not match the body.
