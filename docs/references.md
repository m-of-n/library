---
schema: "library-doc/v1"
id: references
title: "Reference semantics — what each relation means"
type: policy
status: draft
version: "0.1.0"
updated: "2026-09-22"
needs_review: true
reviewed: false
source: "sponsor question 2026-09-22: what are the semantics of references?"
---

# Reference semantics

**Status: draft. Open for review.**

## 1. The distinction that matters most

Two different things are called "references" and conflating them makes the
crosswalk unreadable:

| | `cites` | `relations` |
|---|---|---|
| **What it is** | what the document *itself* references | what **we** assert about how documents relate |
| **Warrant** | fact — it is in the reference section | judgement — revisable, and ours to defend |
| **Source** | extracted from the document | written by a person or proposed by an agent and reviewed |
| **Wrong how** | extraction error | we were mistaken |

*"RFC 9943 cites RFC 9052"* and *"we judge RFC 9804 to be historical prior art
for DEC-002"* are different claims with different warrants. They live in
different fields and are rendered differently in the crosswalk.

**`cites` is also the ingestion frontier.** A cited document we do not hold is a
gap: `{title, locator}` with no record id. That is the queue for the next
snowballing pass.

## 2. Relation semantics

Each relation, its meaning, its inverse, and the test for using it.

| Relation | Means | Inverse | Use it when |
|---|---|---|---|
| `supersedes` | replaces, same document line or successor line | `superseded_by` | the target should no longer be relied on. RFC 9943 supersedes its draft line |
| `updates` | modifies without replacing | `updated_by` | RFC 9682 updates RFC 8610; both remain current |
| `part_of` | member of a family or body | `has_part` | a spec within a consortium or hierarchy record |
| `implements_concept` | realises an idea a topic names | — | links a record to a `topics/<id>` question |
| `contradicts` | asserts something incompatible | `contradicts` (symmetric) | two sources cannot both be right. **The most valuable and least used** |
| `see_also` | related, no stronger claim | `see_also` (symmetric) | last resort. If a precise relation fits, use it |
| `cited_by` | *our own documents* cite this | — | ARCH-0001, a report, an ADR. Not other library records |

Rules:

- **`see_also` is the weakest and most overused.** If you can name why two
  records relate, name it. A crosswalk of `see_also` edges carries no
  information.
- **Inverses are derived, never authored.** Write `supersedes` on one record;
  `bin/reindex` computes `superseded_by` on the other. Authoring both sides
  guarantees they drift.
- **`contradicts` needs a reason** in `summary.md`. An unexplained contradiction
  is an unresolved one.
- **Relations point at record ids**, never URLs. A relation to something we do
  not hold is a `cites` gap instead.

## 3. Versions are not relations

A superseded *version of the same document line* folds into
`versions/<version>/` inside its record (scope §5). It does **not** get a
`supersedes` edge — there is only one record, so there is nothing to point at.

`supersedes` is for **across** document lines: RFC 9943 supersedes the
`draft-ietf-scitt-architecture` line because those are different records.

Getting this wrong produces a crosswalk full of self-edges.

## 4. What regeneration owes you

After any ingestion or relation edit, **derived views are stale** until
`bin/reindex` runs. It regenerates:

- `index/records.md` — everything, including folded versions
- `index/versions.md` — the folded-version index, so a superseded version is
  still findable
- `index/crosswalk.md` — the relation graph, plus **dangling relations**
  (pointing at nothing) and **orphans** (nothing points at them)
- `index/bibliography.md` — the human-readable bibliography
- `index/frontier.md` — `cites` entries with no record: the ingestion queue
- `exports/` — CSL-JSON and BibTeX

`index/` is **generated. Never edit it; regenerate it.** CI fails if it is
stale, the same way it fails on stale `exports/`.

## 5. Open questions

1. Should `cites` be extracted automatically from a converted PDF, or always
   reviewed? Automatic extraction is noisy; manual is slow at volume.
2. Does `cited_by` belong on the record at all, given it points *out* of the
   library into our own documents? It may belong in `index/` only.
3. Do we need `derived_from` for records whose content is generated (extracted
   grammars, generated code) rather than retrieved?
