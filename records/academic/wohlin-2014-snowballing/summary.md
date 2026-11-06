---
schema: "library-summary/v1"
id: wohlin-2014-snowballing
record: wohlin-2014-snowballing
type: summary
updated: "2026-11-05"
---

# Guidelines for snowballing in systematic literature studies and a replication in software engineering

|  |  |
|---|---|
| **Type** | paper (peer-reviewed conference paper, EASE '14) |
| **Maturity** | unset: no value in the enum fits a conference paper |
| **Authors** | Claes Wohlin |
| **Published** | ACM, 2014-05-13, pp. 1-10 |
| **Identifier** | doi:10.1145/2601248.2601268 |
| **Source** | https://www.wohlin.eu/ease14.pdf (author's copy, ACM returns 403) |
| **Digest** | `b45773e4cb8fd006eb4df616418f696888cd35bf434ca183c7f1a62e797d5b76`, fetched 2026-11-01 |

## Overview

Wohlin turns snowballing from an outlined idea into a procedure and argues it can replace a database search as the first step of a literature study. Search strings are only as good as their terms, and inconsistent terminology defeats them (§2, §3.1), whereas citation links survive differences in vocabulary. The procedure takes a diverse start set of papers already judged as included, runs backward (reference lists) and forward (citing papers) one iteration at a time, and stops when no new paper appears (§3). The key rule is that a paper must be finally included, on the full text, before it is snowballed from, or the process has to be rolled back (§3.2, §3.2.3). A replication of MacDonell et al. reached the same papers with 294 candidates examined and 11 included, about the same detailed-review effort as the database reviews (§4.6, §4.10).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | A research method |
| Cryptography | `none` | Same |
| This project | `adjacent` | It governs how the library grows, not what mofn builds |

**It bears on no `DEC-*` or `R-*`, so `bears_on` is empty.** Its use is the method named in `docs/construction.md` *Method to follow*, under mofn backlog T-020.

- **`index/frontier.md` is only the backward half.** The old usefulness note called it this method "mechanised". `bin/reindex` lists `cites` entries with no record, which is backward snowballing. Forward snowballing needs citing-paper data, and nothing in `bin/` collects it. The note is corrected in `record.yaml`.
- **"Record each iteration's yield"** in `docs/construction.md` is lesson 7 of §4.9.1. It has a diagnostic use in lesson 8: if the rate of new papers does not fall, a cluster may have been missed.
- **Include before you snowball.** The frontier is fed by every `cites` entry of every record, whatever its verdict. That is broader than §3.2.3, which only follows included papers. Whether a `not-useful` record should feed the frontier is an open question for D1.
- **Independent clusters** (§3.1, §4.9.1 lessons 2 and 9) are the risk for the library: IETF, W3C and vendor literatures may not cite one another, so one start set per topic can close early.

## Implementations

**Searched 2026-11-01.** One web search for snowballing and citation-chasing tools. The repository was confirmed on GitHub and not run. The paper itself uses Google Scholar by hand for forward snowballing (§3.2.2).

| Name | Kind | License | URL |
|---|---|---|---|
| citationchaser | open source, R package and Shiny app | GPL-3.0-or-later (`DESCRIPTION`; no LICENSE file, so GitHub reports none) | https://github.com/nealhaddaway/citationchaser |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, usefulness verdict |
| `summary.md` | this document |

**Relations.** `kitchenham-charters-2007` is under `cites` (ref [7]), so it carries no `see_also`. The `see_also` to `prisma-2020` is authored on that record, with its reason there.

**No `distilled/`.** A `paper` is outside FX-1's type scope. No PDF is committed.

## Limits

- **One case, chosen because it suits the method.** Finding any one of the included papers leads to all the others (§4.8, §4.9.1), and the paper says the case was very suited to snowballing. It gives no basis for general claims.
- **The replicator had read the original.** The replicator remembered that the result lay between 10 and 19 papers (§4.9.2). The start set also shares one author across all three papers, which the paper concedes (§4.2), and authors were not contacted (§4.7).
- **Its strength varies by section.** The abstract calls snowballing a possible alternative to database search. §5 says it should not necessarily be seen as one and that approaches should be combined. The claim that it is better for extending a study is, by §5's own words, left to further research. This is a real tension with `kitchenham-charters-2007` §6.1, which treats reference lists as a supplement to database searches, but not a contradiction, so no `contradicts` edge is set.
- **Effort is not measured.** §4.10 notes the actual effort of the compared reviews is unavailable, and Table 2's comparison counts papers read in detail.
- **Bookkeeping slips in §4.** §4.5 says "the second iteration" of the third. §4.6 says 3 of 97 for backward Iteration 2, though §4.4.1 included none, and five of 12 included where the list gives 7 of 12. The headline 11 of 294 (3.7%) does reconcile.
- **Google Scholar results change** (§4.2), so forward snowballing is not exactly repeatable. Date every run.
- **Read scope.** The whole paper was read as text extracted from the author-hosted PDF, which is not the ACM version of record and was not compared with it. Figure 1 was not seen. Table 1 lost its layout, so its cells were not relied on.
