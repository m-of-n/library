# Generated views are not tracked

`index/` and `exports/` are **pure functions** of `records/` and `topics/`.
They are not committed. Regenerate them at any time:

```sh
bin/export && bin/reindex
```

## Why

They were tracked until 2026-09-28. On that date three open pull requests —
`topic/scitt` (#30), `topic/nist-cryptography-lane` (#22) and
`topic/survey-seed` (#20) — were all reported `CONFLICTING` by GitHub.

Every conflict was in a generated file:

```
exports/references.bib   exports/references.json
index/bibliography.md    index/crosswalk.md      index/records.md
```

**Not one conflict was in `records/`, `topics/` or `docs/`.** Three people had
ingested different records in parallel, which is exactly what the library is
for, and git had no way to know that two regenerated bibliographies are not a
disagreement — they are the same function applied to two different inputs.

This is structural, not bad luck. Any two branches that add a record will
always conflict in the bibliography, because both rewrite the same sorted list.
The more the library is used the way it is meant to be used, the worse it gets.

A `.gitattributes` merge driver would not have helped: GitHub computes
mergeability server-side and does not run custom drivers, so the pull requests
would still have shown as conflicting and still have blocked review.

Untracking also retires a second failure mode. The old CI had a
"derived views are current" gate, which existed only because a contributor
could commit a record and forget to regenerate. If the files are never
committed, they can never be stale.

## Where to read the bibliography

The human-readable bibliography is published, not browsed in the repo tree:

- **Site:** the mofn Pages build copies it to `docs/library/bibliography.md`.
  `mofn/bin/build-site` regenerates it from the pinned submodule first.
- **Any pull request:** CI uploads `library-views` as a build artifact, so a
  reviewer can download the bibliography, crosswalk and CSL-JSON for that
  branch without checking it out.

## Per-record HTML lives beside its source

`bin/render-html` writes `records/<body>/<id>/summary.html` next to the
`record.yaml` and `summary.md` it is built from. It is the human-readable
page for one record (identity, applicability, tags, links, summary prose).
It sits beside the source because it is an extraction artifact of that
record, not a site page. It is untracked (`.gitignore`) for the same reason
as `index/`: it is a pure function of the record.

Publishers do not re-template it. They import `bin/_record_html.py`, render,
and copy the page into their site, keeping the `records/<body>/<id>/` layout
so links between records still resolve. The page has two hooks for a
publisher:

- The top chrome is a **replaceable region** between `<!-- site-nav -->` and
  `<!-- /site-nav -->`. Standalone library pages render a default banner (a link
  to the repo README) inside it; a publisher replaces the **whole region**
  (both markers inclusive) with its own nav — so no library-relative link leaks
  and there is no double chrome. Replace the region, not just the opening comment.
- `<a class="rec" data-id="…">` marks a link to another record, so a site
  can turn a link to a record it does not publish into plain text.

A publisher's bibliography index, topic pages, and tables belong to that
publisher's manifest, not to this repo. For tmodel, see
`docs/publishing/bibliography.yaml` there.

`bin/_record_yaml.py` is the faithful YAML reader these pages use.
`bin/_yaml.py` stays the validator's reader. It drops flow collections, so
do not render from it.

## What CI still guarantees

Generating them is now the *first* step of CI, so every downstream gate runs
against freshly built views:

- `bin/validate` — records and topics are well-formed
- every record appears in the bibliography (catches a record that generates no
  entry — the check a diff could never make)
- no dangling relations
- no third-party document bytes committed

## If you have a stale checkout

`git pull` will not delete files git has stopped tracking. Remove them once:

```sh
rm -rf index exports && bin/export && bin/reindex
```
