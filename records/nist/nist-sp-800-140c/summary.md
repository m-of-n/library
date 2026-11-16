---
schema: "library-summary/v1"
id: nist-sp-800-140c
record: nist-sp-800-140c
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140C — CMVP Approved Security Functions

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document); **withdrawn** 2022-05-20 |
| **Authors** | NIST (the cover page names Kim Schaffer) |
| **Published** | March 2020; withdrawn 2022-05-20 and superseded in its entirety by SP 800-140C Rev. 1 (May 2022), per the withdrawal notice the PDF opens with |
| **Identifier** | SP 800-140C |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140C.pdf (free) |
| **Digest** | `8edf4f1f64bbdf62660f7b1b19f10e95a2d9a5671533530b2eb1dfb9e10dd0f4` |

## Overview

The CMVP's list of approved security functions, which takes the place of ISO/IEC 19790 Annex C
and ISO/IEC 24759 §6.15 (§1, §5.1, §6.1). The list is a set of citations under six headings
(§6.2): transitions, deferring to sections of SP 800-131A Rev. 2; symmetric encryption (AES and
its modes, TDEA, and SKIPJACK for decryption only); digital signatures by FIPS 186-4; the
SHA-2 and SHA-3 families with the SHA-3 derived functions; and message authentication by CMAC,
CCM, GCM/GMAC and HMAC. No row carries a verbal form: each binds by being listed.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | What a validated module may use in its approved mode |
| Cryptography | core | A list of approved algorithms and the documents specifying them |
| This project | adjacent | Tests mofn's suites against the 2020 list; tmodel models the list as a RequirementSource |

`bears_on: tmodel:DEC-009`; `distilled/design-notes.md` compares the list with mofn's
cipher-suite and key-identifier decisions.

## Implementations

Nothing to list: a list of approved functions, not software (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** every heading, citation, bullet and NOTE of §6.2 as a stated row, the scope statements, inferred obligations flagged; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/` | the derived structure of one list row, its JSON Schema and the script that writes both |
| `distilled/examples/` | the finding that the source has no example; the list as one JSON row per citation, each naming the requirement entries it carries; derived accept and reject cases |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: a protocol model (no exchange is defined) and a state machine (no state is stated);
SP 800-140C Rev. 1 and the ISO/IEC annex it replaced.

## Limits

- **Withdrawn.** This is the 2020 list; Revision 1 replaced it in 2022, and the library does not
  hold Revision 1 (R-0058). Nothing here says what is approved today.
- **SKIPJACK.** Decryption stays approved while the NOTE calls its only cited specification,
  FIPS 185, obsolete and withdrawn (SD-5).
- **Transitions are by reference.** What the transition rules allow depends on SP 800-131A
  Rev. 2, which the library does not hold.
- **By citation only.** The list names documents, not parameters: key sizes and modes come from
  each cited standard.
