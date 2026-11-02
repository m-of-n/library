---
schema: "library-summary/v1"
id: kitchenham-charters-2007
record: kitchenham-charters-2007
type: summary
updated: "2026-11-01"
---

# Guidelines for performing Systematic Literature Reviews in Software Engineering

|  |  |
|---|---|
| **Type** | paper (technical report, Version 2.3) |
| **Maturity** | `white-paper`: a self-published technical report with named external reviewers (§0.3), not a journal article |
| **Authors** | Barbara Kitchenham, Stuart Charters |
| **Published** | July 2007. The cover says 9 July, the version table says 20 July for 2.3 |
| **Identifier** | EBSE Technical Report EBSE-2007-01 (Keele University and University of Durham) |
| **Source** | https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf |
| **Digest** | `ea531e4515a8ed61cdffe06233c37714df1efae14da2801ba348ae0bda158cc4`, fetched 2026-11-01 |

## Overview

The report adapts systematic review practice from medicine to software engineering, and leans on social science because software engineering cannot randomise or blind as medicine does (§3, §9). It organises a review into three phases, planning, conducting and reporting, broken into stages that are mostly mandatory (§4). The argument is about bias: a review protocol is fixed in advance so that study selection and analysis are not driven by what the researchers expect (§5.4), and the search is documented so a reader can assess how thorough it was (§6.1.4). The research question is called the most important part of a review, because the search, extraction and analysis all follow from it (§5.3). §9 lists a reduced set of steps for a lone researcher.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | A research method, with nothing on security |
| Cryptography | `none` | Same |
| This project | `adjacent` | It governs how the library is built, not what mofn builds |

**It bears on no `DEC-*` or `R-*`, so `bears_on` is empty.** Its use is the method: `docs/construction.md` *Method to follow* names it, and that work is mofn backlog T-020 (D1, construction best practice). The parts that map most directly:

- **§5.4 protocol components.** `docs/construction.md` says the protocol is a committed artifact. Whether `topics/*.yaml` carries §5.4's components was not assessed here.
- **§6.1.4 search documentation** and Table 2. This is the rule behind our dated `searched` field: database, search strategy, date and years covered, with changes noted and justified.
- **§6.2.2 excluded studies.** The report keeps a list of exclusions with reasons once the totally irrelevant hits are gone. Our `usefulness: not-useful` verdict does the same job.
- **§6.2.3, §6.4.3 reliability.** One extractor plus one checker, or test-retest for a single researcher. This is the same shape as the FX-1 extract and verify passes.

**`docs/construction.md` says "three-stage", and the source says three phases.** The protocol is a stage inside planning (§4), not a phase of its own, so "protocol → conduct → report" is a slight compression.

## Implementations

**Searched 2026-11-01.** One web search for SLR support tools. Repositories and licences were confirmed on GitHub. None was run. No commercial product was evaluated.

| Name | Kind | License | URL |
|---|---|---|---|
| Parsifal | open source, SLR management | MIT | https://github.com/vitorfs/parsifal |
| ASReview | open source, screening | Apache-2.0 | https://github.com/asreview/asreview |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A `paper` is outside FX-1's `rfc` / `draft` / `spec` / `ietf` scope and nothing here is built against it, so extraction would only be triggered by someone deciding to add a file there. No PDF is committed.

## Limits

- **No meta-analysis detail, and the report says so.** §0.4 and §1 exclude the mechanics of meta-analysis and how question type changes the procedures. Readers with detailed methodological queries are told they are unlikely to find answers here (§1.4).
- **Written for reviews of empirical studies.** The quality checklists (Tables 5 and 6) grade experiments, surveys and qualitative studies. A library of standards has no such primary studies, so §6.3 to §6.5 transfer poorly. This is our reading, not the report's.
- **The search guidance is dated.** §6.1.5 lists 2007 sources, and the authors note digital library searches are almost impossible to replicate (§2.4). The search is database-first, which `wohlin-2014-snowballing` §2 challenges.
- **Terminology has moved on.** The report grades study "quality", and `prisma-2020` records the field's shift to "certainty" of the body of evidence.
- **Internal slips.** §1.4 calls the reporting structure Table 7, and it is Table 8. §6.5.8 and §7.4 both say "during data extraction" of their synthesis and reporting lessons. §5.2 cites the CRD guidelines as [12], and they are [19]. None changes the guidance.
- **Read scope.** The whole 65-page PDF was read as extracted text, Elsevier-hosted copy. Tables 5, 7 and 9 and Appendix 2 lost their layout in extraction, so column placement in them was not relied on. Figures 1 and 2 were not seen. No Keele copy was compared.
