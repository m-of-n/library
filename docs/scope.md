---
schema: "library-doc/v1"
id: scope
title: "Ingestion scope — what belongs in this library"
type: policy
status: draft
version: "0.3.0"
updated: "2026-10-01"
needs_review: true
reviewed: false
backlog: L-018
source: "library#1 item 10; sponsor review of library#4; library#27"
---

# Ingestion scope

**Status: draft, revision 3.** Sponsor review answered the four original open
questions and §4 now answers a fifth (library#27). They are rules. What remains
open is marked **[?]**.

The library is **for collecting as well as deciding.** Breadth is allowed. What
is not allowed is silent loss: a reference judged unhelpful is *recorded as
unhelpful*, never dropped, or the same document gets re-evaluated every few
weeks and the judgement evaporates.

---

## 1. In scope

| Kind | Type | Example |
|---|---|---|
| Standards | `rfc` `spec` | RFC 9943, ISO/IEC 19566-5 |
| Specifications, not ratified | `draft` `spec` | draft-ietf-cose-merkle-tree-proofs |
| Recommendations, best practice | `spec` `rfc` | IETF BCP, NIST SP 800-57 |
| White papers, technical reports | `paper` | NIST IR, vendor architecture papers |
| Academic publications | `paper` `article` | Wohlin snowballing, arXiv preprints |
| Open source projects | `repo` | sigstore/rekor, in-toto/attestation |
| Standards bodies and consortia | `consortium` | IETF COSE WG, C2PA, W3C |
| Document families | `hierarchy` | the SLSA release line, C2PA 2.x |
| Websites with durable technical content | `web` | a spec landing page, a registry |
| Registries and datasets | `dataset` | IANA COSE Header Parameters |
| Regulation | `spec` | EU CRA, EU AI Act Art. 50 |

**Cryptographic standards are in scope and summarised, not stubbed.** We
implement cryptography; NIST is core. FIPS 186-5, 180-4, 202 and SP 800-57 are
first-class records even though ARCH-0001 NG3 defers the algorithm suite and
they bear on no open DEC. *Do not apply the "bears on a decision" test
literally* — it is a prompt for judgement, not a gate.

**Paywalled work is recorded.** Digest the abstract or landing page, set the
locator, `status: stub`. We may get access later, and a record we cannot read
today is still a record we can find tomorrow. We never store bytes we may not
redistribute.

## 2. Out of scope — a short list, applied with judgement

- **Marketing material.** A vendor architecture paper is in; a product page is
  an `implementations` entry, not a record.
- **Secondary summaries of primary sources we already hold** — unless they
  *disagree*, in which case ingest and set `contradicts`.
- **Anything without a stable locator.** If it cannot be cited and
  re-retrieved, it cannot be evidence. A screenshot is not a source.

News and blog posts are not excluded outright: if a post is the primary source
for a claim we make, it is a record with `role: evidence`.

When in doubt, **ingest as a stub.** A stub costs one directory. A missed
source costs a decision.

## 3. The rule that does most of the work

> **An implementation of a spec we already hold is not a new record. It is an
> `implementations` entry on that spec's record.**

`sigstore/cosign` does not get a record because it implements things we already
track. It appears under `implementations.open_source` on the relevant spec.

A repo earns its own record only when **the repo is the primary source** — the
specification lives there and nowhere else. `in-toto/attestation` qualifies;
`sigstore/cosign` does not.

This is the difference between a library of ~60 useful records and one of ~400
that nobody reads.

## 4. Higher-level organisation — `body` is a shelf, not a byline

Records live at **`records/<body>/<id>/`**: `records/ietf/`, `records/nist/`,
`records/w3c/`, `records/academic/`.

**`body` is a storage key and a coarse grouping. It is not a claim about who
published the document.** Decided 2026-10-01, library#27, where it had been
quietly doing three jobs and only the first of them honestly. Each question now
has exactly one field that answers it:

| the question | the field |
|---|---|
| where is the file | `body` — the directory, and the section heading in `index/` |
| who published it | `publisher` — free text, and it MAY name two |
| what is its standing | `maturity` — `standard` means ratified |

`body` is **single-valued**, so it cannot represent a document with two
affiliations, and it is no longer asked to. CycloneDX 1.7 is authored by the
OWASP Foundation and ratified by Ecma International as ECMA-424 2nd edition.
Both are load-bearing for a reader deciding whether to rely on it, and nothing
is lost: `publisher` names both, `identifiers.ecma` carries the number and is
rendered in the bibliography, `maturity: standard` carries the standing. What
`body` records is that the file sits on the `community` shelf.

So: **never reach for a new `body` value in order to assert an affiliation.** A
value earns a directory by making records easier to find, not by a new legal
entity appearing. `other` and `community` are legitimate shelves, not failures
to classify, and `regulator` collapsing EU and US sources is a shelving choice
— not a claim that CISA and the European Commission are one body. *That closes
what revision 2 listed as open question 2.*

Two corollaries:

- **A re-publication of the same text under another body is an `identifiers`
  entry, not a second record.** A different *version* is a different record
  (§5). This is the rule library#25 wrote into `cyclonedx-1-7`, and
  `records/other/ecma-424/` already breaks it — tracked separately, because
  retiring a record is not a reshelving.
- **Reshelving is cheap and ids do not move.** `body` is a directory, so
  changing it is a `git mv` plus `bin/reindex`. Ids stay globally unique and an
  id cannot be reused under a different body — `bin/ingest` checks across all
  shelves before creating anything — so no citation silently retargets. Cheap
  reversal is why this was worth deciding rather than deferring a third time.

Values come from **`schema/record.schema.yaml:fields.body`** — the single
declaration, parsed at run time by `bin/validate` and `bin/ingest`. They are
deliberately *not* in `schema/tags.yaml`: `body` is not a tag, and the copy
that lived there had already drifted out of agreement with the schema. Adding a
shelf is still a PR, and it is cheap.

### What was rejected, and why

- **Split the field** — keep `body` as the directory, add a multi-valued
  `publishers` or `standardized_by`. This is the honest model of dual
  affiliation and the only option with real query power. Rejected *for now*:
  `publisher` plus `identifiers` already answers the reader's question, while a
  schema bump and a 280-record migration buy a field nothing queries yet.
  Revisit the moment something does — when a report needs *"every record
  ratified by a body other than its author"*, this becomes the right answer,
  and the migration is mechanical.
- **Grow the enum as needed** — add `owasp`, `ecma`, `linux-foundation`, …
  Cheapest per case and worst at scale, and it does not even solve the case
  that raised it: one record still gets one `body`, so dual affiliation still
  picks a winner. It also produces single-record directories and splits SPDX
  from CycloneDX across bibliography sections, where a reader wants them
  adjacent.

## 5. Versions fold into the record

**One record per document *line*, tracking the current version.** Superseded
versions go in **`versions/<version>/`** inside that same record, not as
sibling records.

Per-version sibling records explode the library, and we are largely interested
in the latest. `draft-…-11` through `-18` is one record; C2PA 2.2 → 2.4 is one
record with `version: "2.4"`.

The exception is obsolescence across document lines: **an RFC that OBSOLETES
another is a different line** and keeps its own record, linked by `supersedes`.
RFC 9943 does not fold into the draft it came from.

Other granularity rules:

- **Do not ingest a whole working group.** One `consortium` record, then the
  documents that matter, each with `part_of`.
- **Families get a `hierarchy` parent.** Forty sibling records with no parent is
  a failure, not thoroughness.
- **Registries are one record**, not one per entry. The IANA COSE Header
  Parameters registry is a single `dataset` record even though it bears heavily
  on R-M-12.

## 6. No caps — but no silent discards

There is **no record cap.** Collecting is a legitimate mode and breadth is
allowed.

What replaces the cap is an explicit verdict. Every record carries
`usefulness`:

```yaml
usefulness:
  verdict: useful | marginal | not-useful | unassessed
  reason: "one line — required for not-useful and marginal"
  assessed: 2026-09-22
```

**Recording that something is not useful is the deliverable**, not a failure.
An unexplained negative verdict gets re-litigated; `bin/validate` requires the
reason.

Two rules survive the removal of caps:

- **Never invent relevance.** A fabricated `bears_on` corrupts the one query
  the library exists to answer. A stub is the honest alternative.
- **A topic with 40 records has probably become two topics.** That is a signal
  to split, not a limit to enforce.

---

## 7. Open questions **[?]**

1. **Does `versions/` hold the full record or just the metadata?** Keeping a
   `summary.md` per superseded version preserves what changed; keeping only
   `record.yaml` is cheaper. Proposed: metadata plus a one-line delta note.
2. **Does `usefulness` need review dating?** A verdict of `not-useful` from
   before a decision was reopened may be stale. `assessed` records when, but
   nothing forces re-assessment.
