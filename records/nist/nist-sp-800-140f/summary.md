---
schema: "library-summary/v1"
id: nist-sp-800-140f
record: nist-sp-800-140f
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140F — CMVP Approved Non-Invasive Attack Mitigation Test Metrics

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST (the cover page names Kim Schaffer) |
| **Published** | March 2020 (cover page); the PDF as retrieved carries no withdrawal notice |
| **Identifier** | SP 800-140F |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140F.pdf (free) |
| **Digest** | `7772ec5af1909a87b7e724afeef77bb3206174c321aa59f80e32500df7fc48ed` |

## Overview

The CMVP's replacement for ISO/IEC 19790 Annex F's approved non-invasive attack mitigation
test metrics and their tests in ISO/IEC 24759 §6.18 (§5.1, Abstract). It replaces
them with nothing yet: §6.2, where the approved metrics would be, says there are no additional
requirements at this time. §1 meanwhile keeps ISO/IEC 24759 §6.18 as the test requirements
unless this SP says otherwise, so whether Annex F's own metrics still apply, or none does, the
text does not settle (`distilled/normative.md` SD-1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Side-channel mitigation testing for validated modules, if any applies |
| Cryptography | core | Specific to cryptographic-module validation |
| This project | adjacent | A compliance input tmodel models; no mofn specification addresses side channels |

`bears_on: tmodel:DEC-009`; `distilled/design-notes.md` records what tmodel would need to carry a
list that changes, and why nothing here rests on a mofn decision.

## Implementations

Nothing to list: there is no metric to implement (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** the one keyword sentence, the keyword-less binding sentences and the inferred obligation, verbatim with source lines; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/README.md`, `distilled/examples/README.md` | the finding that there is nothing to model, written by `distilled/schema/build.derived.py` |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: messages, schemas, examples, a protocol model and a state machine, all not
applicable (`record.yaml` gives the reason); ISO/IEC 19790 Annex F, which is paywalled.

## Limits

- **An empty list.** §6.1 promises the approved metrics and §6.2 identifies none (SD-2).
- **Unsettled precedence.** Read with §1, Annex F's metrics still apply and this SP adds none;
  read with §5.1 and the Abstract, they are replaced and no approved metric exists (SD-1).
- **Marks the rendering cannot show.** Additions are underlined (§5.2) and the text rendering
  carries neither underline nor strikethrough (SD-4); §6 prints no marked-up text.
