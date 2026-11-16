---
schema: "library-summary/v1"
id: nist-sp-800-140b
record: nist-sp-800-140b
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140B — CMVP Security Policy Requirements

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document); **withdrawn** 2023-11-17 |
| **Authors** | NIST (the cover page names Kim Schaffer) |
| **Published** | March 2020; withdrawn 2023-11-17 and superseded in its entirety by SP 800-140B Rev. 1 (November 2023), per the withdrawal notice the PDF opens with |
| **Identifier** | SP 800-140B |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140B.pdf (free) |
| **Digest** | `60bc7223fa81f21724d0d4cd74e5a7e5df52cba928c8187803290ccaa398424c` |

## Overview

The CMVP's rules for the non-proprietary security policy, the public document a FIPS 140-3
validation publishes (§1, §5.1, §6.1). The policy follows ISO/IEC 19790 Annex B's order, from
B.2.1 General to B.2.12 Mitigation of other attacks, and marks a section that does not apply
(§6.1). For each section the SP reprints Annex B's bulleted items for reference and adds table
templates, figure placeholders and footnotes saying what goes in them: tested and
vendor-affirmed environments, approved and non-approved algorithms, ports, roles, services and
their SSP access rights, physical security, and the SSP and entropy tables (B.2.1 to B.2.9).
Six sections, and ISO/IEC 24759 §6.14 itself, are marked No change.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The deliverable that states what a validated module does in its approved mode |
| Cryptography | core | Its tables list a module's algorithms, keys and entropy sources |
| This project | adjacent | A compliance input tmodel models; no mofn decision rests on it |

`bears_on: tmodel:DEC-009`; `distilled/design-notes.md` maps the policy's structures onto
tmodel's Requirement, Evidence and identity slots and names the decisions it touches.

## Implementations

Nothing to list: a document format for a validation deliverable, with no software implementing
it (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** every keyword sentence, bullet, table header and pre-filled row, figure caption, applicability label and footnote, verbatim with source lines; inferred obligations flagged; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/` | the security policy spine and one derived structure per table or figure template, their JSON Schemas and the script that writes them |
| `distilled/examples/` | the finding that the source has no example, and derived accept and reject cases |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: a protocol model (no exchange is defined) and a state machine (no states or
transitions of its own); ISO/IEC 19790 Annex B and ISO/IEC 24759 §6.14, which are paywalled.

## Limits

- **Withdrawn.** Revision 1 supersedes this edition in its entirety, and the library does not
  hold it. Read this record as what modules validated against the 2020 edition followed
  (`requirements.yaml` R-0176).
- **Templates, not data.** Every table is captioned Table x and every figure Figure x (SD-2), so
  none can be cited by number; the records name them by clause and position.
- **Marks the rendering cannot show.** Which words or sub-items of a bullet the CMVP added is
  carried by underline (§5.2), which the text rendering loses (SD-6).
- **Small source defects:** B.2.9's heading and the Security Levels table spell the area
  differently (SD-5), a sub-item cites B 2.2 for B.2.2 (SD-4), and footnote 14 runs across a page
  and past B.2.12 (SD-3).
