# library

The bibliographic library for m-of-n. Standalone by design: independently
cloneable, forkable, and citable by projects that are not this one.

`schema/record.schema.yaml` is normative. `docs/construction.md` is the method.

## Never

- **Never commit a third-party document.** PDF, spreadsheet, ebook, epub:
  record `content.sha256` and `content.url`. `.cache/` is gitignored. CI rejects
  the bytes.
- **Never set `content.local: true`.**
- **Never edit or commit `exports/` or `index/`.** Generated and gitignored.
  CSL-JSON is the interchange format; BibTeX is generated, never authored.
- **Never hand-create a record directory.** `bin/ingest <type> <source>`.
- **Never reuse an id.** Ids are stable forever — a citation must not silently
  retarget. A new version of a spec is a new record linked by `supersedes`.
- **Never set `status: distilled` with TODOs in `distilled.md`.** CI rejects it.

## Full extraction — FX-1

Every `rfc` / `draft` / `spec` / `ietf` record a PR **extracts** must reach
`distillation.profile: full`: normative text, **all** requirements with keyword
counts reconciled, schemas, message formats, protocol model, state machines,
test vectors, and design notes mapped to our decisions. Multi-agent passes
(extract → verify → cross-check), **every pass at maximum effort**. A summary
is a started record, not a finished one. `docs/extraction.md` is normative;
`.claude/skills/extract` is the procedure; CI enforces it.

**Extracting, not touching** (amended 2026-10-03). FX-1 fires when the record
has `status: distilled`, already declares `distillation`, or the PR changes its
`distilled/`. Summarising a record is ingestion and is held to the summary bar
instead — `summarized`, valid relations, `bin/validate` clean. It is a ratchet:
an extracted record can never regress to a summary. Say in the PR body which
bar you are claiming, and name the issue that owns the eventual extraction.

## Shape

```
MANIFEST.yaml     library id, federation peers, schema version
records/<id>/     record.yaml · distilled.md · quotes.md · artifacts/
topics/<id>.yaml  the unit of parallel work
exports/          GENERATED, untracked — CSL-JSON and BibTeX
index/            GENERATED, untracked — bibliography, crosswalk, frontier
bin/              ingest, validate, export, new-topic
```

Cross-references are **typed** — `supersedes`, `updates`, `cited_by`,
`see_also`, `implements_concept`, `contradicts`, `part_of` — not tags. Typed
edges are what make *"every normative reference bearing on DEC-002"* a real
query.

Every record names what it `bears_on`. A reference that informs no decision is
one we did not need yet.

## Skills — open this repo as the project

Claude Code loads skills from the **project root only**, never transitively
through a submodule. Opening `mofn/` does **not** load these.

**Working on records? Open `library/` as the project.**

`.claude/skills/` — `ingest-reference`, `summarize`, `extract` (FX-1), `distill`. They carry the
judgement the tools do not.

## Before any PR

```sh
bin/validate
```

**Do not commit `index/` or `exports/`.** They are generated and untracked —
regenerate locally with `bin/export && bin/reindex` whenever you want to read
them. Every merge conflict this library has ever had was in those files, and
none was a real disagreement: two branches that each add a record always
rewrite the same sorted bibliography. See `docs/generated-views.md`.

CI generates them and gates against the fresh output, including the check that
every record produces a bibliography entry. Reviewers can download the built
views from the `library-views` artifact on any PR.

**Shelfmark:** no merger of record data. Convergence of *requirements* first,
then *schema*. Backlog T-023.
