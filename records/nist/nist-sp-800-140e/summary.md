---
schema: "library-summary/v1"
id: nist-sp-800-140e
record: nist-sp-800-140e
type: summary
updated: "2026-11-15"
---

# NIST SP 800-140E — CMVP Approved Authentication Mechanisms

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST (the cover page names Kim Schaffer) |
| **Published** | March 2020 (cover page); the PDF as retrieved carries no withdrawal notice |
| **Identifier** | SP 800-140E |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140E.pdf (free) |
| **Digest** | `26616caa396fc292dd1d726309e34287683c8089ea401f3dc7f55ccb671aa28e` |

## Overview

The CMVP's replacement for ISO/IEC 19790 Annex E's approved authentication mechanisms and
their tests in ISO/IEC 24759 §6.17 (§5.1). Despite the title it approves none: §6.2 says there are
currently no approved mechanisms and lists, in Table 1, the mechanisms allowed at each FIPS
140-3 security level, from none required at level 1 to two multi-factor cryptographic
mechanisms at level 4. Above level 1 the module or its operating environment performs the
authentication (§6.2). Vendors are pointed to SP 800-63B as the framework, with its sections 5
to 7 named normative and sections 8 and 10 to be assessed, and testers are to review and affirm
the vendor's documentation (§6.2). A mechanism that also sets up a protected communication
service is held to the strength requirements of SP 800-140C and SP 800-140D (§6.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Operator authentication at each FIPS 140-3 level |
| Cryptography | core | Ties cryptographic authenticators to the approved-function lists |
| This project | adjacent | Maps onto mofn's passphrase handling and tmodel's requirement sources |

`bears_on: tmodel:DEC-009`; `distilled/design-notes.md` maps Table 1 and the SP 800-63B
pointer onto tmodel and mofn.

## Implementations

Nothing to list: a requirements document, not software (searched 2026-09-26).

## Artifacts in this record

FX-1 extraction, `profile: full`; coverage figures and the reason for each artifact that does
not apply are in `record.yaml` `distillation`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and the `distillation` block |
| `distilled/README.md` | index of the extraction and of the pinned source rendering |
| `distilled/requirements.yaml` | **machine source:** every keyword sentence, every Table 1 row and mechanism, the SP 800-63B section lists, the scope statements and the inferred obligations, verbatim with source lines; keyword counts reconciled |
| `distilled/inferred-candidates.yaml` | every sentence that might bind, with a verdict |
| `distilled/normative.md` | the normative text by section, and the source defects |
| `distilled/messages.yaml`, `distilled/schema/` | two derived structures (a Table 1 row, and a vendor's mechanism claim checked against it), their JSON Schemas and the script that writes them |
| `distilled/examples/` | the finding that the source has no example; Table 1 as JSON rows; derived accept and reject cases |
| `distilled/protocol.yaml`, `distilled/protocol.md` | the two stated exchanges: the vendor's documentation and its review, and operator authentication |
| `distilled/design-notes.md` | how the record bears on tmodel and mofn |
| `distilled/skeleton-report.txt` | the skeleton run's counts |

Not here: a state machine (the authenticator lifecycle and session management are SP 800-63B's,
named and not stated); SP 800-63B itself, which the library does not hold.

## Limits

- **No approved mechanism.** The title promises approved mechanisms and §6.2 lists allowed ones
  (SD-5).
- **SP 800-63B's standing is inconsistent:** an informative reference in §5.1, a framework with
  normative sections in §6.2, and absent from §2 (SD-3).
- **Copy errors:** §1's scope names SSP generation and establishment methods, SP 800-140D's
  subject (SD-1), and ISO/IEC 24579 is printed for ISO/IEC 24759 (SD-2).
- **A strength rule with no home:** §6.1 cites strength requirements of SP 800-140C and
  SP 800-140D, which list approved functions and methods and state none of their own (SD-4).
