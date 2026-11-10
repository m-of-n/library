---
schema: "library-summary/v1"
id: iso-26262-3-2018
record: iso-26262-3-2018
type: summary
updated: "2026-11-05"
---

# ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard: ISO catalogue shows Published, stage 90.92 (capture of 2026-07-14) |
| **Committee** | ISO/TC 22/SC 32 (catalogue) |
| **Published** | 2018-12, Edition 2, 28 pages (catalogue) |
| **Identifier** | ISO 26262-3:2018 |
| **Source** | https://www.iso.org/standard/68385.html |
| **Digest** | none. **Not fetched**: sold by ISO, and www.iso.org returned 403 to our client |

## Overview

**This record has not been read.** The standard is sold by ISO (CHF 179) and was not obtained, and its normative text was not read. Per `docs/scope.md` §1 it stays a `stub`.

Only bibliographic facts are kept, from the ISO catalogue page seen through an Internet Archive capture dated 2026-07-14: Edition 2, 2018-12, 28 pages, ISO/TC 22/SC 32, Published, stage 90.92 (to be revised) since 2024-07-08, replacing the withdrawn ISO 26262-3:2011, to be replaced by ISO/WD 26262-3.2. The abstract paraphrase and quote were removed on 2026-11-05: the iso.org footer says *"no ISO content may be used for any machine learning and/or artificial intelligence and/or similar technologies"*. It is held here because `iso-sae-21434-2021` cites it; that record's `cites` entry marks it as a Clause 2 normative reference.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | From the title only: functional safety, not security; relevant as the safety counterpart that ISO/SAE 21434 references |
| Cryptography | `none` | From the title only: functional safety, not cryptography |
| This project | `none` | No mofn requirement touches vehicle functional safety |

**Bears on none.** ARCH-0001 §5 and the design log have no automotive or functional-safety requirement. Earlier `bears_on: DEC-003` came from Threat-Radar's numbering and was removed (see `content.note`). **Restored 2026-11-09 as `tmodel:DEC-003` (library#133).** The removal misread a register collision as a stale id: these are tmodel's live ids (Threat-Radar `project/DECISIONS-0001.md` and `spec/ARCH-0001-threat-model-architecture.md`), where DEC-003 is the risk-metric scheme. They still bear on no mofn decision.

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

- **Unread.** The normative text was not read, and the catalogue abstract is no longer used (iso.org footer forbids ML use of ISO content). How the concept-phase work products relate to ISO/SAE 21434's TARA was not checked.
- **Status may move.** The capture shows stage 90.92 (to be revised) and ISO/WD 26262-3.2 under development; a third edition would be a new record linked by `supersedes`.
