---
schema: "library-summary/v1"
id: nist-sp-800-140d
record: nist-sp-800-140d
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140D — CMVP Approved Sensitive Security Parameter Generation and Establishment Methods

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document); **withdrawn** 2022-05-20 |
| **Authors** | NIST (the cover page names Kim Schaffer) |
| **Published** | March 2020; withdrawn 2022-05-20 and superseded in its entirety by SP 800-140D Rev. 1, per the withdrawal notice the PDF opens with |
| **Identifier** | SP 800-140D |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140D.pdf (free) |
| **Digest** | `23a9f6798c641653ca999b5a19838204f6e61ea58b42b21303bdfc00d2c20f0b` |

## Overview

The CMVP's list of approved methods for generating and establishing sensitive security
parameters (keys and other SSPs), which supersedes ISO/IEC 19790 Annex D and ISO/IEC 24759
§6.16 (§1, §5.1) and precludes every method it does not list (§6.1). It defers transitions to
sections of SP 800-131A Rev. 2 (§6.2.1) and lists twelve numbered documents (§6.2.2): FIPS 186-4,
used only for domain parameters and key-pair generation (its Note); the SP 800-56A, 56B and 56C
key-establishment and key-derivation recommendations; SP 800-108, 800-132 and 800-135 key
derivation; SP 800-38F key wrapping; SP 800-133 key generation; and the SP 800-90A and 800-90B
random bit generation documents. No row carries a verbal form: each binds by being listed.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | What a validated module may use to make and exchange keys |
| Cryptography | core | A closed list of key generation, derivation, wrapping and establishment methods |
| This project | adjacent | Tests mofn's key derivation and exchange choices against the 2020 list |

`bears_on: tmodel:DEC-009`; `distilled/design-notes.md` compares the list with mofn's key
handling, and notes that neither its passphrase protection nor HPKE appears on it.

## Implementations

Nothing to list: a list of approved methods, not software (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** every citation, bullet and note of §6.2 as a stated row, the scope statements, inferred obligations flagged; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/` | the derived structure of one list row, its JSON Schema and the script that writes both |
| `distilled/examples/` | the finding that the source has no example; the list as one JSON row per citation, each naming the requirement entries it carries; derived accept and reject cases |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: a protocol model (no exchange is defined) and a state machine (no state is stated);
SP 800-140D Rev. 1 and the ISO/IEC annex it replaced.

## Limits

- **Withdrawn.** This is the 2020 list; Revision 1 replaced it in 2022, and the library does not
  hold Revision 1 (R-0031). Nothing here says what is approved today.
- **Closed, but by citation.** A method off the list is precluded, yet the list names documents,
  not parameter sets; what each permits is in the cited standard.
- **Transitions are by reference** to SP 800-131A Rev. 2, which the library does not hold.
