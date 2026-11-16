---
schema: "library-summary/v1"
id: nist-sp-800-140a
record: nist-sp-800-140a
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140A — CMVP Documentation Requirements

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST (the cover page names Kim Schaffer, Computer Security Division) |
| **Published** | March 2020 (cover page); the PDF as retrieved carries no withdrawal notice |
| **Identifier** | SP 800-140A |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140A.pdf (free) |
| **Digest** | `0fc31c5fdb7bd4a33a2490897d509da1fdedba59e10c46729ce11831fb611fd1` |

## Overview

The CMVP's change, as validation authority, to the vendor documentation that ISO/IEC 19790
Annex A requires and that ISO/IEC 24759 §6.13 tests (§1, §5.1). The whole change is one
ISO/IEC 24759 assertion, ASA.01, with one vendor-evidence item (VEA.01.02) and one test
procedure (TEA.01.02), both numbered as additions (§5.2, §6.1). Those two items set the
documentation floor by a validation-authority document this SP never names. Everything else in
ISO/IEC 24759 applies as printed (§1), against ISO/IEC 19790:2012 with its 2015 corrections and
ISO/IEC 24759:2017 (§2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A CMVP validation requirement for cryptographic modules |
| Cryptography | core | Specific to cryptographic-module validation |
| This project | adjacent | A compliance input tmodel models; no mofn decision rests on it |

`bears_on: tmodel:DEC-009`: a documentation floor is a tmodel Requirement of kind
documentation, discharged through a Mitigation or a practice, with the vendor's documents as
Evidence (`distilled/design-notes.md`).

## Implementations

Nothing to list. This is a validation authority's requirements document, which no software
implements (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** every keyword sentence, the keyword-less binding sentences and the inferred obligations, verbatim with source lines; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/` | one derived structure for the documentation a vendor provides, its JSON Schema and the script that writes both |
| `distilled/examples/` | the finding that the source has no example, and derived accept and reject cases |
| `distilled/protocol.yaml`, `distilled/protocol.md` | the vendor-to-laboratory hand-off VEA.01.02 and TEA.01.02 describe |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: a state machine (no lifecycle is stated), and the ISO/IEC 19790 Annex A and ISO/IEC
24759 text this SP modifies, which are paywalled; `iso-iec-19790` is held unread under its
licence.

## Limits

- **The floor is unnamed.** VEA.01.02 and TEA.01.02 measure documentation against the validation
  authority's requirement and management documentation, which the SP neither names nor cites
  (`normative.md` SD-2). Neither item is fully testable from this record.
- **Marks the rendering cannot show.** Additions are underlined and deletions struck through
  (§5.2), and the text rendering carries neither (SD-3). Which words of ASA.01 the CMVP added,
  and whether anything was deleted, needs the PDF.
- **A garbled lead-in.** §6.1's lead-in names ISO/IEC 24759 twice and no ISO/IEC 19790 annex
  (SD-1).
- **Which paragraph grants the CMVP's authority** is cited differently here (ISO/IEC 19790 §5.2)
  and in SP 800-140 (ISO/IEC 24759 §5.2); the library cannot check which is right.
