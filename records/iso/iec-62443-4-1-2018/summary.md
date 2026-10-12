---
schema: "library-summary/v1"
id: iec-62443-4-1-2018
record: iec-62443-4-1-2018
type: summary
updated: "2026-10-02"
---

# IEC 62443-4-1:2018 — Secure product development lifecycle requirements

|  |  |
|---|---|
| **Type** | spec (International Standard) |
| **Maturity** | standard |
| **Authors** | IEC TC 65 (text based on 65/685/FDIS, RVD 65/688/RVD); developed largely from ISCI SDLA certification requirements |
| **Published** | 2018-01-15, Edition 1.0; identical ANSI/ISA-62443-4-1-2018; EN IEC 62443-4-1:2018 |
| **Identifier** | IEC 62443-4-1:2018 (ISBN 978-2-8322-5239-0 on preview) |
| **Source** | https://webstore.iec.ch/en/publication/33615 (paywalled; 54 pp) |
| **Digest** | `eb2f67981f03f944f8fe0044c6ac176b8f2422cb0473cc08c28d477cb3c52d03` — IEC webstore preview EN (11 pp), retrieved 2026-10-02 |

**Version check (2026-10-02).** IEC webstore publication 33615: Edition 1.0, status *valid*,
stability date 2027, no amendment listed. CEN-CENELEC webinar "CRA Standards Unlocked: From EN IEC 62443
to CRA" (2025-09-09, cencenelec.eu PDF, sha256 `7ccbe82337e35cbe509cf4e65423178d218a3661104878e2668f7866d8021b9d`)
lists work item 81487 **EN IEC 62443-4-1:2018/prAA** (→ A11:2026) under CEN-CLC/JTC 13 WG 9 to add
"intended use"/"security context" documentation and expected development artefacts, and states EN IEC
62443-4-1 "Covers EU CRA Annex I Part I (1) and Part II Essential Cybersecurity Requirements". IEC
Edition 2 (TC 65/WG 10) is in revision; a secondary report gives a 2027 CDV — not confirmed from an IEC
page. ISASecure SDLA-102 v4.3 (July 2025) baselines SDLA-312 at v6.4 (editorial logo change vs the v6.3
used here).

**CRA amendment, re-checked 2026-10-02.** **EN IEC 62443-4-1:2018/prAA:2026** is the European amendment that
adapts this standard for presumption of conformity under the CRA (Regulation (EU) 2024/2847, record `eu-cra-2024-2847`).
The enquiry draft is dated 2026-03-13 and voting closed 2026-06-05 (stage 40.60). Committee CLC/TC 65X; the
related legislation listed is 2024/2847. Sources: genorma.com and the national mirrors evs.ee and iss.rs (secondary
catalogue pages, read 2026-10-02). It is **not yet ratified and not cited in the OJ**, and its text was not read.
Once ratified, cited and readable, it will be a new record linked to this one by `updated_by`.

## Overview

The product-supplier part of IEC 62443: a secure development lifecycle expressed as 47 numbered
**process** requirements in eight practices — security management (SM-1..13), specification of security
requirements (SR-1..5), secure by design (SD-1..4), secure implementation (SI-1..2), security
verification and validation testing (SVV-1..5), management of security-related issues (DM-1..6),
security update management (SUM-1..5) and security guidelines (SG-1..7) — with each practice graded on a
four-level maturity model (Clause 4.2). It binds the developer and maintainer of a product, not the
integrator or asset owner. It is the most prescriptive SDL standard on the threat model's content (SR-2's
DFD-shaped list), tester independence (Table 3), release gating (SM-11/SM-12) and user-facing security
documentation (Practice 8), and the EU is amending its EN to serve CRA Annex I.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | reference SDL process standard for OT/IACS; parent of IEC 81001-5-1; CRA harmonisation basis |
| Cryptography | adjacent | only code-signing key protection (SM-8), file integrity (SM-6), update authenticity (SUM-4) |
| This project | core | R-041 (SM-11/SM-12 release gate), R-042 (SR-2 k + SVV-2 = threats-mitigated check), R-044 (MAP-0001 column), R-040 (Practice 8 = documentation mitigations), DEC-009 (DM-4 dispositions), DEC-003 (CVSS severity, residual-risk threshold) |

## Implementations

Searched 2026-10-02.

| Name | Kind | License | URL |
|---|---|---|---|
| ISASecure SDLA (ISCI/ASCI) | certification scheme; SDLA-312 maps each requirement to validation activities | spec PDFs: non-commercial use | https://isasecure.org/certification/iec-62443-sdla-certification |
| IECEE scheme for IEC 62443-4-1 | certification scheme | — | https://www.iecee.org/certification/iec-standards/iec-62443-4-12018 |
| open-source 62443-4-1 conformance tooling | searched: none found 2026-10-02 | — | — |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, every free source consulted with digest, relations |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | everything normative legitimately readable, with locators |
| `distilled/requirements.yaml` | 8 practices; 84 statements covering all 47 requirement ids (library-requirements/v2) |
| `distilled/state-machine.yaml` | security-related-issue lifecycle, ML1–ML4, ISASecure SDLA certification |
| `distilled/object-model.yaml`, `distilled/object-model.md` | object-model pass: 54 objects, 38 edges, 10 gaps; Mermaid |
| `distilled/design-notes.md` | bearing on R-040..R-044 / DEC-003 / DEC-009; MAP-0001 corrections; open questions; licensing |

## Limits

- **The IEC normative body was not read** (paywalled). Requirement text is ISCI's reproduction in
  SDLA-312 v6.3; SR-2 is restructured there, and SUM-1's "should" sentence may be an ISCI addition.
  Not covered: rationale and supplemental guidance subclauses, Clause 4 (concepts, maturity model,
  Table 1), Table 2, Annex A (metrics), Annex B. ML1–ML4 labels come from secondary slide decks.
- Process-only: it requires that a threat model, reviews and tests exist, not how good they are.
  Product technical requirements are in 62443-4-2 / 3-3 (not held).
- Severity is delegated to "a vulnerability scoring system (for example, CVSS)"; no risk method of its own.
- Operational incident response is outside its scope (integrator/asset owner, 62443-2-1/2-4).
