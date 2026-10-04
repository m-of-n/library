# Contributing to library/

Workflow, branches, worktrees and PR discipline live in the **m-of-n** repo's
`CONTRIBUTING.md`. They apply here identically.

> **Work in this repo — never in `mofn/library/`.** That directory is a
> submodule checkout on a **detached HEAD**: commits made there belong to no
> branch and are orphaned by the next `git checkout`, `git submodule update` or
> `bin/lib-sync`. A 49-record CBOR/COSE sweep was nearly lost this way (#12,
> rescued as #13). Clone `m-of-n/library` and open *that* as your project —
> which is also the only way this repo's skills load.

Library-specific:

1. `bin/ingest <type> <source> --body <org>` — never hand-create a record
   directory. Records live at `records/<body>/<id>/`.
2. Fill `summary.md` before setting `status: summarized`. It is the document a
   human reviews. `distilled.md` is a separate, optional job.
3. **Validate before every PR:**
   ```sh
   bin/validate
   ```
   **Do not commit `index/` or `exports/` — they are generated and ignored.**
   CI builds them and then gates: **every record appears in the bibliography**,
   and no relation dangles. Reviewers can download the built views from the
   `library-views` artifact on the PR.

   Regenerate them locally whenever you want to read them:
   ```sh
   bin/export && bin/reindex
   ```

   **The published bibliography lags by two steps**, deliberately: merge here,
   then the pin moves in `mofn`, then the site rebuilds. A report cites
   `library@<commit>`, so the pin is a decision. `notify-mofn` opens the
   pin-bump PR automatically once `MOFN_DISPATCH_TOKEN` is set.
4. **Protocol and format documents are fully extracted before merge (FX-1).**
   Any `rfc`, `draft`, `spec` or `ietf` record your PR **extracts** needs the
   complete artifact set — requirements, schemas, messages, protocol model,
   state machines, test vectors, design notes — from multi-agent passes at
   maximum effort. See `docs/extraction.md`; start with
   `bin/extract-scaffold <record-dir>`.

   A PR that only **summarises** such a record is held to the summary bar
   instead (`summarized`, valid relations, `bin/validate` clean) — FX-1 fires
   on `status: distilled`, an existing `distillation` block, or a change under
   `distilled/`. Say which bar you are claiming in the PR body.
5. One topic per branch. Topics are sized so branches do not collide.
6. Never commit a PDF, spreadsheet or ebook. CI rejects it.

## What regeneration owes you

`bin/reindex` rebuilds `records`, `versions` (folded documents), `crosswalk`,
`bibliography`, `frontier` and `by-decision`, and derives every inverse
relation, so the two sides of an edge cannot drift.

`index/` and `exports/` are **generated and untracked. Never edit them, never
commit them, regenerate them.** They were tracked until 2026-09-28; every merge
conflict the library had ever seen was in them, and none was a real
disagreement — two branches that each add a record always rewrite the same
sorted bibliography. See `docs/generated-views.md`.

Untracking them also retired the "stale derived view" failure: a file that is
never committed cannot be stale.

## Bumping the pin in mofn/

Merging here changes nothing in `mofn/` until the submodule pin moves:

```sh
cd ../mofn && bin/lib-sync --update
```

Deliberate: a report cites `library@<commit>`, so the bibliography it was
written against cannot shift underneath it.
