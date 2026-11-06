---
schema: "library-summary/v1"
id: prisma-2020
record: prisma-2020
type: summary
updated: "2026-11-05"
---

# The PRISMA 2020 statement: an updated guideline for reporting systematic reviews

|  |  |
|---|---|
| **Type** | paper (reporting guideline) |
| **Maturity** | _unset_: a consensus reporting guideline published as a journal article. The BMJ page was not read, and the enum's `best-practice` is for BCP- or NIST-SP-style standing, which was not verified |
| **Authors** | Matthew J Page and 25 others, David Moher last (full list in `record.yaml`) |
| **Published** | BMJ 2021;372:n71, 2021-03-29. The id says 2020 after the guideline's name |
| **Identifier** | doi:10.1136/bmj.n71 · PMID 33782057 · PMC8005924 |
| **Source** | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8005924/fullTextXML (mirror, BMJ returns 403) |
| **Digest** | `c5e3b4a1892f0cb97ea0360d5e5b4b51ab4ea8b4e8ddabe7b441b5d464f18758`, of the XML, fetched 2026-11-01 |

## Overview

PRISMA 2020 replaces the 2009 statement, which it says should no longer be used (*How to use PRISMA 2020*). It is a guideline for reporting, not for doing: a 27-item checklist in seven sections, a 12-item abstract checklist, and flow diagram templates, so a reader can see why a review was done, what was done and what was found. Its changes from 2009 push on search transparency: full strategies for every database, register and website rather than one (item 7), how many reviewers screened and whether independently (item 8), and citing near-miss studies with the reason each was excluded (item 16b). It was built from a review of 60 guidance documents, a survey with 110 of 220 invitees responding, and a 21-member meeting (*Development of PRISMA 2020*).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | A reporting guideline |
| Cryptography | `none` | Same |
| This project | `adjacent` | It governs how the library reports its own searches, not what mofn builds |

**It bears on no `DEC-*` or `R-*`, so `bears_on` is empty.** Its use is the method named in `docs/construction.md` *Method to follow*, under mofn backlog T-020. The items that map onto the library:

- **Items 6, 7 and 16a:** sources searched with dates, and counts from records identified to studies included. These are the checks our dated `searched` field and a topic's reading list should pass.
- **Item 16b:** near misses cited with reasons, which is the `usefulness: not-useful` rule. This is the exact sense of "excluded — and why" in `docs/construction.md`.
- **Item 24:** registration, protocol and amendments. Amendments need a home if the protocol is a committed artifact, as `docs/construction.md` says.
- **Item 27:** data, code and materials stated as public or not. The library is public by design.

**The word `record` differs, and it will mislead.** In Box 1 a PRISMA "record" is a title or abstract indexed in a database, and a "report" is the document. Our `record.yaml` describes what PRISMA calls a report. A PRISMA-style count of "records" must not be read as the library's record count.

## Implementations

**Searched 2026-11-01.** One web search for PRISMA flow diagram tools. The statement itself names a checklist web app, which answered HTTP 200 on 2026-11-01, as did the statement website.

| Name | Kind | License | URL |
|---|---|---|---|
| PRISMA checklist web app | web app, named by the statement | not checked | https://prisma.shinyapps.io/checklist/ |
| PRISMA2020 | open source, R package and Shiny app | MIT (`DESCRIPTION`: "MIT + file LICENSE"; the GitHub API reports NOASSERTION) | https://github.com/prisma-flowdiagram/PRISMA2020 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**Relations.** Neither `see_also` target cites PRISMA 2020 or is cited by it, so the edges are ours. They are authored on this record only. The three are the methods `docs/construction.md` *Method to follow* names, and each covers a different part of the work:
- `see_also: kitchenham-charters-2007`: the conduct half that PRISMA rules out of its scope (*Scope of the guideline*).
- `see_also: wohlin-2014-snowballing`: the search method whose iterations item 6 (reference lists as a source) and item 16a (counts from records identified to studies included) would have to report.

**No `distilled/`.** A `paper` is outside FX-1's type scope, and the checklist is short enough that nothing has needed it. No source bytes are committed.

## Limits

- **It does not tell you how to do a review.** The statement rules out guiding conduct, and rules out being used to assess conduct or methodological quality (*Scope of the guideline*). So "PRISMA-compliant" says the report is complete, not that the search was good. `kitchenham-charters-2007` is the conduct half.
- **Scoped to health.** It is designed primarily for reviews of health interventions, and says items apply to other interventions and many to other objectives. Nothing tests it on a library of standards, and items 11 to 15 and 18 to 22 (risk of bias, effect measures, synthesis, certainty) have no equivalent for us. That last judgement is ours.
- **Protocols are out of scope.** PRISMA-P 2015 covers them, and it is not held here.
- **How to get adherence is unsettled.** Of 31 interventions proposed to raise adherence to reporting guidelines, 11 were evaluated, mostly in observational studies at high risk of bias (*Discussion*), so the statement says it is unclear which strategies to use. Our own adherence is untested.
- **Read scope.** The whole article body, both checklists and Box 1 and Box 2 were read from the Europe PMC JATS XML, a mirror, not the BMJ page. The reference list was only searched by name. Figure 1, the flow diagram, is an image and only its caption was read. The expanded checklist and the explanation and elaboration paper (ref 41) were not read, and they hold the detail behind each item. Co-publications elsewhere were not compared.
