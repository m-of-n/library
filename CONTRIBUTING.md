# Contributing to library/

Workflow, branches, worktrees and PR discipline live in the **m-of-n** repo's
`CONTRIBUTING.md`. They apply here identically.

Library-specific:

1. `bin/ingest <type> <source> --body <org>` — never hand-create a record
   directory. Records live at `records/<body>/<id>/`.
2. Fill `summary.md` before setting `status: summarized`. It is the document a
   human reviews. `distilled.md` is a separate, optional job.
3. **Regenerate derived views before every PR:**
   ```sh
   bin/validate && bin/export && bin/reindex
   ```
   Commit `exports/` **and** `index/`. CI enforces three things: the views are
   not stale, **every record appears in the bibliography**, and no relation
   dangles. Adding a record without regenerating leaves the bibliography wrong,
   which is the most visible way this library can be untrustworthy.

   **The published bibliography lags by two steps**, deliberately: merge here,
   then the pin moves in `mofn`, then the site rebuilds. A report cites
   `library@<commit>`, so the pin is a decision. `notify-mofn` opens the
   pin-bump PR automatically once `MOFN_DISPATCH_TOKEN` is set.
4. One topic per branch. Topics are sized so branches do not collide.
5. Never commit a PDF, spreadsheet or ebook. CI rejects it.

## What regeneration owes you

After ingesting anything, or editing any relation, **`index/` is stale**:
`records`, `versions` (folded documents), `crosswalk`, `bibliography`,
`frontier`, `by-decision`. `bin/reindex` rebuilds all of them and derives every
inverse relation, so the two sides of an edge cannot drift.

`index/` is **generated. Never edit it; regenerate it.**

A human-visible bibliography going stale after ingestion is the normal failure
here — the gate exists because it is easy to forget.

## Bumping the pin in mofn/

Merging here changes nothing in `mofn/` until the submodule pin moves:

```sh
cd ../mofn && bin/lib-sync --update
```

Deliberate: a report cites `library@<commit>`, so the bibliography it was
written against cannot shift underneath it.
