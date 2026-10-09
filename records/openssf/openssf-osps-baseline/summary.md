---
schema: "library-summary/v1"
id: openssf-osps-baseline
record: openssf-osps-baseline
type: summary
updated: "2026-10-02"
---

# Open Source Project Security Baseline (OSPS Baseline) v2026.08.28

|  |  |
|---|---|
| **Type** | spec (control catalog, Gemara Layer 2) |
| **Maturity** | best-practice (OpenSSF SIG publication; the catalog metadata still says `draft: true`) |
| **Authors** | "OSPS Baseline Authors" — OpenSSF Security Baseline SIG (under the ORBIT WG); created with OpenJS, OpenSSF, CNCF and FINOS community leaders (page Acknowledgments) |
| **Published** | 2026-08-28 (calendar version `v2026.08.28`) |
| **Identifier** | OSPS Baseline v2026.08.28; git tag `v2026.08.28` (commit `a26a7963f6fd098c1e82829322ec9e1196a4f294`) |
| **Source** | https://baseline.openssf.org/versions/2026-08-28 · authoritative YAML: https://github.com/ossf/security-baseline/tree/v2026.08.28/baseline |
| **Digest** | `406dca03e1e1d01fcfee489bf5465938498686fa5e8701698b22d492281661b8` (release tarball `archive/refs/tags/v2026.08.28.tar.gz`); live page HTML `d1d603880f2948f8465d5334af55e3235291493ab002898cd9519c70963e176c` |

## Version check (2026-10-02)

- https://baseline.openssf.org/ — "Current version: v2026.08.28"; previous v2026.02.19, v2025.10.10,
  v2025.02.25; an in-development version exists.
- https://api.github.com/repos/ossf/security-baseline/releases/latest — tag `v2026.08.28`,
  published 2026-08-28T23:28:53Z.
- `main` already carries post-release changes (OSPS-AC-03.02 clarified, #558; OSPS-VM-05.01 split,
  #554). They belong to the next version and are **not** extracted here.
- The authoritative source is the Gemara YAML at the tag; all 65 assessment-requirement texts and
  all recommendations were checked identical to the live page. The rendered
  `docs/versions/2026-08-28.md` committed *at* the tag is stale (still shows a "While active,"
  qualifier removed by #544) and was regenerated on `main` later — see design-notes Q4.
- Publisher identity: README/index say the Baseline "is maintained by the OpenSSF Security Baseline
  SIG"; that the SIG sits under the OpenSSF ORBIT Working Group comes from OpenSSF's working-group
  structure, not from the tagged repo itself.

## Overview

The OSPS Baseline is a minimum set of security requirements for an open source project, scaled to
its maturity: Level 1 for any project, Level 2 for code projects with at least two maintainers and
consistent users, Level 3 for widely used projects. It contains **only MUST requirements** — 41
controls in 8 families (Access Control, Build and Release, Documentation, Governance, Legal,
Quality, Security Assessment, Vulnerability Management) with **64 active assessment requirements**
(24 at L1, 41 at L2, 62 at L3). Each one is a single testable condition, usually triggered by an
event ("When the project has made a release, … MUST …"). It is published as machine-readable
Gemara YAML with a CUE schema, and its maintainers publish `relates-to` crosswalks from every
control to 14 external frameworks, including the CRA, SSDF, SP 800-161, SLSA, SAMM, Scorecard,
PSSCRM, the UK Software Security Code of Practice and BSI TR-03185-2. Its argument is that a
baseline is useful only if it is **assessable and automatable**. Most of its requirements are
platform-configuration facts or the presence of named documents, and tools can check both.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Minimum secure-development and supply-chain controls for OSS projects; the requirements mapped to the CRA for open source stewards and manufacturers. |
| Cryptography | adjacent | Requires MFA, encrypted and authenticated channels, and signed releases or manifests. It does not specify algorithms. |
| This project | core | It is the best template for the R-042 automatable conformance check and the R-044 crosswalk. It has two requirement grains, a requirement lifecycle and typed graded mapping edges, all available as data. OSPS-SA-03.02 requires a threat model, which is what tmodel produces. |

Bears on **R-042** (conformance check), **R-044** (requirements crosswalk), **R-040** (mitigation
kind: documentation / process / configuration), **R-041** (gates; release-triggered requirements),
**R-043** (documents as governed views), **DEC-009** (generic mitigation to product instance).

## How it relates to the other SDL references

- It is **narrower than SSDF** (`sp-800-218`): it is project-level, has OSS-specific controls (license, DCO) and contains no organisation practices. It is **more testable** than SSDF: SSDF tasks are outcomes, while OSPS ARs are checks. 35 OSPS controls are mapped to SSDF tasks.
- It **complements SLSA** (`slsa-1-2`). OSPS asks for signed releases, provenance-verification instructions and CI least privilege, but not for a SLSA level. Its SLSA mappings target SLSA 1.0 prose names, not ids.
- **Scorecard** (`openssf-scorecard-checks`) is the heuristic scorer, and OSPS is the pass/fail requirement set. 13 OSPS controls map to Scorecard checks.
- For the **EU CRA** (`eu-cra-2024-2847`), 35 controls are mapped to Annex I items (e.g. `1.2d/e/f`).
- The SP 800-161r1, PSSCRM (`psscrm-v1`), UK CoP and BSI TR-03185 records are mapped targets.

## Implementations

Searched 2026-10-02.

| Name | Kind | License | URL |
|---|---|---|---|
| pvtr-github-repo-scanner (Privateer plugin) | automated assessor; consumes the Gemara L2 catalog and emits L4 evaluation results; bundles several catalog versions; feeds LFX Insights | Apache-2.0 | https://github.com/ossf/pvtr-github-repo-scanner |
| osps-baseline-action | GitHub Action wrapper for OSPS assessments | not checked | https://github.com/revanite-io/osps-baseline-action |
| Minder rules and profiles (`security-baseline/`) | policy-as-code rules for OSPS controls | Apache-2.0 | https://github.com/mindersec/minder-rules-and-profiles |
| Gemara | schema and model the catalog is written in | Apache-2.0 | https://github.com/gemaraproj/gemara |
| baseline-compiler (`cmd/` in the source repo) | validates YAML, renders Markdown and checklists, exports OSCAL JSON and Gemara | Apache-2.0 | https://github.com/ossf/security-baseline/tree/v2026.08.28/cmd |
| Security Insights spec | machine-readable project metadata that many assessments read | not checked | https://github.com/ossf/security-insights |
| LFX Insights | hosted dashboard showing OSPS results per repo | proprietary service | https://insights.linuxfoundation.org/docs/metrics/security/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, distillation block |
| `distilled/README.md` | artifact index and coverage |
| `distilled/normative.md` | every control, objective, AR text, recommendation, applicability and control-level mapping, verbatim; metadata, frameworks, full lexicon, maintenance rules on ids |
| `distilled/requirements.yaml` | 67 entries: 64 active ARs, 1 retired tombstone, and 2 recommendation-level MAY permissions. Each has audit typing and the `maps_to` crosswalk. Counts are reconciled: 66 = 66. |
| `distilled/schema/` | `osps.cue` and the Gemara v1.2.0 CUE files it imports, verbatim |
| `distilled/messages.yaml` | the catalog and mapping-document data structures, field by field |
| `distilled/state-machine.yaml` | project maturity progression, Control/AR lifecycle, and baseline release states |
| `distilled/examples/` | 5 verbatim YAML excerpts with expected validation results |
| `distilled/design-notes.md` | adopt / adapt / reject against R-040…R-044 and DEC-009, plus 7 open questions |
| `distilled/object-model.yaml`, `object-model.md` | 45 objects and 48 edges (verify pass added 1 object + 9 edges), gaps, and Mermaid diagrams |

## Limits

- It **does not define an assessment procedure or result format**: no evidence rules, no evaluator qualification and no attestation. Gemara Layer 4/5 and Privateer fill that gap outside the spec.
- It is **only for open source projects**. It has no organisation-level SDL practices and no training, metrics, or risk-acceptance process. It is a baseline, not a maturity model of the program.
- Its crosswalks are `relates-to` only, with strength, confidence and rationale unset. The source disclaims them as "not a functional connection".
- Threats are implicit: they are named in objectives, but the Gemara `threats` field is unused.
- Applicability anomaly: BR-07.01 and VM-02.01 apply at L1 only. Two MUST texts embed a lowercase "should" (BR-07.02, QA-06.03).
- The released catalog still carries `draft: true`, and `metadata.version`/`date` are unset. The version identity is the git tag and the docs path only.
