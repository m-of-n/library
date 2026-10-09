# technical reference library

The bibliographic library with generated artifacts. Standalone by design:
independently cloneable, forkable, and citable by projects that are not this one.
Vendored as a submodule pinned to a commit, so a report's
bibliography is reproducible as `library@<commit>`.

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
records/<id>/     record.yaml · distilled.md · quotes.md · artifacts/
topics/<id>.yaml  the unit of parallel work (PROC-0001 §4)
schema/           normative record and topic schemas
exports/          GENERATED — CSL-JSON and BibTeX
bin/              ingest, validate, export, new-topic
```

## Federation, offline, and scale

A library is a git repo, so distribution and offline work are free. N libraries =
N repos. `MANIFEST.yaml` lists federation peers; cross-library references resolve
as `(library-id, record-id, content-digest)`, and a digest mismatch is
*detectable divergence* rather than silent corruption. We are not building a sync
engine — git is one.
