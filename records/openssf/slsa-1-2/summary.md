---
schema: "library-summary/v1"
id: slsa-1-2
record: slsa-1-2
type: summary
updated: "2026-10-02"
---

# SLSA Specification v1.2

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard. "Status: Approved" on the spec index; this is OpenSSF community consensus, not de jure |
| **Authors** | SLSA project contributors (OpenSSF SLSA working group / slsa-framework) |
| **Published** | 2025-11-24 ("content: Release SLSA 1.2", slsa-framework/slsa#1516) |
| **Identifier** | SLSA v1.2. Predicate types `https://slsa.dev/provenance/v1` and `https://slsa.dev/verification_summary/v1` |
| **Source** | https://slsa.dev/spec/v1.2/ (single page https://slsa.dev/spec/v1.2/zonepage); Markdown at slsa-framework/slsa `releases/v1.2` @ `ae7fc762` |
| **Digest** | `d9e2a942ecfece89b28da9463b18e5aa9c1a549d969cab93b37ec5610be1d052` (rendered single page, retrieved 2026-10-02) |

**Version verified 2026-10-02:**

- https://slsa.dev/spec/ reads "Status: Approved … This is Version 1.2 of the SLSA specification"
  and lists v1.1 as the previous version.
- The repo history shows 1.2 released 2025-11-24 (#1516), after RC1 and RC2. The what's-new page
  lists "No changes" since RC2.
- The Working Draft (https://slsa.dev/spec/draft/) adds a **Build Environment Track** and a
  **Dependency Track**. They are not part of 1.2.

So the existing stub id `slsa-1-2` is correct and the record was upgraded in place. The library
holds no record for v1.1, so no `supersedes` link was added. The record keeps its original topic,
`supply-chain-attestation`, and also serves the `sdl` topic.

## Overview

SLSA describes supply-chain integrity as **tracks of cumulative levels**.

- **Build track (L0–L3):**
  - L1: provenance exists.
  - L2: hosted build platform, signed and authentic provenance.
  - L3: provenance unforgeable by tenants, builds isolated, ephemeral environments, no cache
    poisoning.
- **Source track (L1–L4), new in 1.2.** It covers version-controlled source, change history and
  source provenance, continuous enforcement of technical controls on protected refs, and two-party
  review.

Each level is a set of MUST/SHOULD requirements on the **producer**, the **build platform**, the
**source control system** or the **organization**. Conformance is shown through attestations: in-toto
Statements carrying **Provenance** or a **Verification Summary Attestation (VSA)**. A **verifier**
checks them against **expectations** and **roots of trust**.

The spec also defines a threat model of nine threats, **A–I**, at the source, build and usage
stages, plus dependency, availability and verification threats, with example attacks and
mitigations. It defines how build platforms and source control systems are assessed. In the
author's words, SLSA is "a way to measure your efforts toward compliance with the Secure Software
Development Framework (SSDF)".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the de facto supply-chain integrity standard; SSDF PS/PW, the OSPS Baseline, Scorecard and CNCF all point to it |
| Cryptography | adjacent | signatures and roots of trust are required, but no algorithms are specified (DSSE/in-toto carry the bytes) |
| This project | core | the VSA and expectations are the template for the R-042 conformance result; Level/Track vs Gate settles part of R-041; threats A–I give phase-scoped threat categories (R-037). Build provenance itself stays on the radar side (ADR-0001) |

Bears on **R-042**, **R-041**, **R-044** (SSDF link, OSPS mapping), **R-040** (source controls
and attestations as mitigation kinds), **R-037**, **R-036** (party roles) and **DEC-009** (control
continuity as a mitigation lifecycle).

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| slsa-github-generator | Build L3 provenance generator for GitHub Actions | Apache-2.0 | https://github.com/slsa-framework/slsa-github-generator |
| slsa-verifier | provenance and VSA verifier | Apache-2.0 | https://github.com/slsa-framework/slsa-verifier |
| slsa-source-poc | Source track proof of concept (source VSAs on GitHub) | Apache-2.0 | https://github.com/slsa-framework/slsa-source-poc |
| gittuf | source-side policy and RSL (cited by the source track) | Apache-2.0 | https://github.com/gittuf/gittuf |
| Tekton Chains | provenance for Tekton pipelines | Apache-2.0 | https://tekton.dev/ |
| GitHub artifact attestations | hosted build-provenance service | commercial service | https://github.blog/changelog/2024-06-25-artifact-attestations-is-generally-available/ |
| Sigstore (cosign, Rekor) | signing and transparency for attestations | Apache-2.0 | https://github.com/sigstore |

Searched 2026-10-02.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, FX-1 distillation block |
| `distilled/README.md` | index with per-artifact coverage |
| `distilled/normative.md` | all 16 normative/technical pages verbatim |
| `distilled/requirements.yaml` | 243 keyword-bearing statements (268 BCP 14 keywords, reconciled), typed by actor, track, level, phase, nature, deliverables and verification |
| `distilled/schema/` | verbatim provenance cue and proto, the VSA jsonc sketch, and 3 derived JSON Schemas |
| `distilled/messages.yaml` | 18 structures (DSSE, Statement, Provenance tree, ResourceDescriptor, VSA, Source VSA, roots of trust, expectations) |
| `distilled/protocol.yaml`, `protocol.md` | 9 flows with Mermaid sequence diagrams |
| `distilled/state-machine.yaml` | 9 machines (level ladders, continuity, review, verification) |
| `distilled/examples/` | 21 fixtures with expected results, 54 threat scenarios and 2 VSA verification cases |
| `distilled/design-notes.md` | adopt, adapt or reject against ARCH-0001 / DL-0009 / ADR-0001 |
| `distilled/verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass: 80 objects, 81 edges (25 added by the verify pass), 8 gaps |

Informative pages are summarised here and not reproduced in `normative.md`: what's new, about,
threats overview, use cases, guiding principles, FAQ and future directions.

## Limits

- **Integrity, not quality.** SLSA says nothing about vulnerabilities, secure design or code
  review content. Two-party review is about consent, not depth: "Reviews SHOULD cover, at least,
  security relevant properties of the code". An SDL needs SSDF, ASVS or SAMM alongside it.
- **No transitive levels.** `dependencyLevels` only *reports* dependency levels. The Dependency
  track exists only in the working draft.
- **Weak self-attestation at low source levels.** Source L1 VSAs "MAY" be issued from the SCS's
  own understanding of the system (R-0098), and platform assessment may be self-attested. R-0098 is
  internally overlapping at Level 2: it grants the MAY "At Source Levels 1 and 2" and in the same
  sentence requires "at Level 2+" that the SCS MUST use SCS-issued source provenance; the MUST
  governs (verify pass, 2026-10-02).
- **Schemas are informative.** The cue and proto sketches are explicitly non-authoritative; the
  field text governs. Our JSON Schemas are derived, and some MUSTs (e.g. R-0236) cannot be checked
  by a schema.
- **Packaging, not deployment.** SLSA covers publication; it does not cover runtime admission
  (compare the CNCF deployment gate in `cncf-supply-chain-best-practices-v2`).
