---
schema: "library-summary/v1"
id: iso-26262-3-2018
record: iso-26262-3-2018
type: summary
updated: "2026-11-03"
---

# ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard: ISO catalogue shows Published, stage 90.92 (capture of 2026-07-14) |
| **Authors** | ISO/TC 22/SC 32 (catalogue) |
| **Published** | 2018-12, Edition 2, 28 pages (catalogue) |
| **Identifier** | ISO 26262-3:2018 |
| **Source** | https://www.iso.org/standard/68385.html |
| **Digest** | none. **Not fetched**: sold by ISO, and www.iso.org returned 403 to our client |

## Overview

**This record has not been read.** The standard is sold by ISO and was not obtained, and its normative text was not read. Per `docs/scope.md` §1 it stays a `stub`. Everything below comes from the ISO catalogue page, seen through an Internet Archive capture dated 2026-07-14, and is labelled as such.

Per the catalogue abstract, Part 3 of ISO 26262 *"specifies the requirements for the concept phase for automotive applications"*, naming item definition, hazard analysis and risk assessment, and the functional safety concept. The abstract says the document applies to safety-related systems that include one or more electrical and/or electronic (E/E) systems installed in series production road vehicles, excluding mopeds, and addresses hazards caused by malfunctioning behaviour of safety-related E/E systems. It is held here because `iso-sae-21434-2021` cites it; that record's `cites` entry marks it as a Clause 2 normative reference.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Functional safety, not security; relevant as the safety counterpart that ISO/SAE 21434 references |
| Cryptography | `none` | Nothing in the abstract concerns cryptography |
| This project | `none` | No mofn requirement touches vehicle functional safety |

**Bears on none.** ARCH-0001 §5 and the design log have no automotive or functional-safety requirement. Earlier `bears_on: DEC-003` came from Threat-Radar's numbering and was removed (see `content.note`).

## Implementations

Not searched: this is a process standard for an engineering organisation, not something we would build on.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with what was and was not seen in `content.note` |
| `summary.md` | this document |

**No relations and no `distilled/`.** No typed edge is authored here: `iso-sae-21434-2021` points at this record through `cites`. No bytes were obtained. A legitimate copy would move this record past `stub`; an extraction would then be owed under FX-1, since this is a `spec`.

## Limits

- **Unread.** Only the catalogue abstract was seen; the normative text was not read. How the concept-phase work products relate to ISO/SAE 21434's TARA was not checked.
- **Status may move.** The capture shows stage 90.92 (to be revised) and ISO/WD 26262-3.2 under development; a third edition would be a new record linked by `supersedes`.
