# research/

**Where external research about *how to run the library* is archived.**

Distinct from `records/`, which holds references about the project's *subject
matter*. This directory holds our own research **reports** on method — library
construction, bibliography practice, ingestion workflow — and the evidence
behind them.

The gap this fills: `docs/construction.md` states conclusions (CSL-JSON over
BibTeX, Kitchenham/Wohlin/PRISMA method, typed relations) with **no archived
sources**. The searches were run and thrown away. That is exactly the failure
this library exists to prevent, and it happened in our own methodology.

```
research/
  NNNN-question/
    report.md        YAML front matter; the finding and its basis
    sources.md       every source consulted, with retrieval dates
    searches.md      the queries run, verbatim, and their yield
```

Every source that mattered also gets a `records/` entry with
`tags: [bibliography-method]` and `role: method`, so it is citable like
anything else.

Reports on the project's *subject* — context, mechanism, uptake (D3) — live in
`mofn/research/`, not here.
