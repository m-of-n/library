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
