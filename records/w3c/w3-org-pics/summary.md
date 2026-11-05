---
schema: "library-summary/v1"
id: w3-org-pics
record: w3-org-pics
type: summary
updated: "2026-11-05"
---

# W3C Platform for Internet Content Selection (PICS)

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | `historic`, from the page's own notice |
| **Authors** | none named |
| **Published** | undated |
| **Identifier** | https://www.w3.org/PICS/ |
| **Source** | https://www.w3.org/PICS/ |
| **Digest** | `sha256:bf09ac33…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

W3C's frozen landing page for PICS. A notice at the top says it is not maintained, that PICS has been superseded by POWDER, and that W3C encourages authors to refer to POWDER or its successor. The page describes PICS as a way to associate labels with Internet content, designed for parents and teachers but also useful for code signing and privacy. Otherwise it is an index of introductions, closed mailing lists, media coverage, specifications and product lists.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | None |
| Cryptography | `none` | None |
| This project | `adjacent` | A pointer into the PICS records and a dated statement of succession |

- **Bears on no decision itself, so `bears_on` is empty.** An earlier draft named DEC-007 "only as an index". A navigation page does not inform the decision; the argument is in `pics-1-1-services`, and this page adds only W3C's dated succession statement.

## Relations

- `see_also: pics-1-1-services`: the page lists it under Technical Specifications and links it. Authored only here; `pics-1-1-services` no longer repeats it.
- `see_also: pics-censorship-faq`: the page links that FAQ (PICS-FAQ-980126) in its introductory materials. That record does not author an edge back.
- `see_also: powder-description-resources`: the page's notice says PICS has been superseded by POWDER and links it. Authored only here; the POWDER record no longer repeats it.
- `pics-1-1-labels`, `pics-dsig-1-0` and `w3c-tag-obsolete-powder` author their edges to this record, so they are not repeated here.

## Implementations

The page links lists of PICS-compatible products and services. They were not followed, and no search was run for this record. See `pics-1-1-services`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar, and FX-1 does not apply to a `web` index page. No extraction is owed.

## Limits

- **It says nothing technical.** Cite the specifications instead.
- **Superseded in the page's words, and POWDER's own status is now in question.** `powder-description-resources` records the open obsolescence proposal, so the recommendation to use POWDER may be out of date.
- **Broken links.** The page itself warns that contact details and links may no longer be active, and marks several links as broken ("broken link as of July 2005" and similar).
- **Read scope.** The notice, description, table of contents, Introduction, Participating and the top of What's New. The rest of the page and its linked lists were not read.
