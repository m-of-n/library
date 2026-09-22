# Skills that act on the library

**Canonical here, because they operate on these records.** Claude Code loads
skills from the **project root only** — not transitively through a submodule.
So these load when `library/` is opened as the project, and `mofn/` carries
only the skills that act on `mofn/`.

| skill | for |
|---|---|
| `ingest-reference` | creating a record: type, body, `bears_on`, stub-or-not |
| `summarize` | `summary.md` — the document a human reviews |
| `distill` | `distilled.md` — compaction for requirements extraction |

Open the repo you are working in. See `CLAUDE.md` §Skills.
