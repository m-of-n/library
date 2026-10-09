# m-of-n technical reference library

The bibliographic library for the [m-of-n](../) project. Standalone by design:
independently cloneable, forkable, and citable by projects that are not this one.
Vendored into `mofn/` as a submodule pinned to a commit, so a report's
bibliography is reproducible as `library@<commit>`.

## What this is for

This library is a **component of the m-of-n project harness**, not a reading
list. Its job is to be the evidence layer the specification cites: a claim
ARCH-0001 makes about what a standard requires should resolve to a record here,
and that record should carry enough extracted detail that nobody has to
re-read the source to check it.

That is why a record has three layers.

| layer | file | answers |
|---|---|---|
| **bibliographic** | `record.yaml` | what this is, where it lives, what it `bears_on` |
| **human** | `summary.md` | what it says and why we hold it — enough to decide whether to read it |
| **machine** | `distilled/` | every normative statement, schema, message, state machine and test vector, in a form a program can consume |

`distilled/` is the layer that makes the library **citable at requirement
granularity**. A statement extracted into `distilled/requirements.yaml` gets a
stable id — `<record>#R-NNNN` — so the specification can cite *a requirement*
rather than *a document*. `docs/extraction.md` (FX-1) is the standard.

**FX-1 is triggered by the intent to extract, not by contact with a record**
(amended 2026-10-03). It fires on an in-scope `rfc` / `draft` / `spec` /
`ietf` record when the record is `status: distilled`, already declares a
`distillation` block, or the pull request changes its `distilled/`.
Summarising a record is *ingestion*, and is held to the **summary bar**
instead. `bin/check-pr-extraction` prints which bar each touched record was
held to, so a reviewer can see what was waived.

**So distillation is opt-in, and deliberately rare.** Most records are stubs,
and a stub is a legitimate resting state: it costs one directory and preserves
a source we can find again. Filling a scaffold into a real `summary.md` does
**not** pull a record into FX-1. Full extraction is claimed deliberately, for
the documents we build against — it is the expensive layer, and spending it
on a document nothing depends on is how a library turns into a reading list.

## Rules

- **`record.yaml` is authored. `exports/` is generated.** Never edit `exports/`.
- **We never commit third-party documents.** Record the digest and the locator;
  `.cache/` is gitignored. Keeps the repo small, the licensing clean, and the
  integrity intact.
- **IDs are stable and never reused.** An id means the same thing forever.
- **Cross-references are typed**, not tags: `supersedes`, `cited_by`,
  `implements_concept`, `contradicts`, `part_of`. Typed edges make the library
  queryable — *"every normative reference bearing on DEC-002"* is a real query.
- **Every record names what it bears on** (`bears_on: [DEC-002, R-M-12]`).
  A reference that informs no decision is a reference we did not need.

## Tools

```sh
bin/ingest --list                      # supported source types
bin/ingest rfc 9943 --topic foo        # RFC by number
bin/ingest draft draft-ietf-cose-...   # IETF draft
bin/ingest pdf ~/papers/x.pdf          # local PDF (hashes it, reads pdfinfo)
bin/ingest repo https://github.com/... # open source project (pins HEAD)
bin/ingest consortium https://w3.org/  # standards org; specs use part_of
bin/ingest spreadsheet data.xlsx       # tabular source
bin/ingest url https://...   --fetch   # web page; --fetch hashes the bytes

bin/new-topic <id> "<question>" <owner>
bin/validate                           # CI gate
bin/export                             # → exports/references.{json,bib}
```

Adding a source type is a **data** change: drop a template in `bin/adapters/`.
Only touch `bin/ingest` if the type needs real metadata extraction.

## Layout

```
MANIFEST.yaml     library id, federation peers, schema version
records/<id>/     record.yaml · summary.md · distilled/  (FX-1, when built against)
topics/<id>.yaml  the unit of parallel work (PROC-0001 §4)
schema/           normative record and topic schemas
exports/          GENERATED, untracked — CSL-JSON and BibTeX
index/            GENERATED, untracked — bibliography, crosswalk, frontier
bin/              ingest, validate, export, new-topic
```

## Federation, offline, and scale

A library is a git repo, so distribution and offline work are free. N libraries =
N repos. `MANIFEST.yaml` lists federation peers; cross-library references resolve
as `(library-id, record-id, content-digest)`, and a digest mismatch is
*detectable divergence* rather than silent corruption. We are not building a sync
engine — git is one.

**Shelfmark:** no merger of record data. Convergence of *requirements* first,
then *schema*. Tracked as `T-023` in the m-of-n backlog.
