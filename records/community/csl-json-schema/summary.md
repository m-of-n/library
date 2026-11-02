---
schema: "library-summary/v1"
id: csl-json-schema
record: csl-json-schema
type: summary
updated: "2026-11-01"
---

# Citation Style Language — schemas (CSL-JSON)

|  |  |
|---|---|
| **Type** | repo (JSON Schema draft-07 for data, RELAX NG for styles) |
| **Maturity** | `unofficial`: the README says the CSL-JSON schema is not yet fully normative |
| **Authors** | Citation Style Language contributors |
| **Published** | Commit of 2023-01-25, after tag v1.0.2 (2021-10-22). Still master's head on 2026-11-01 |
| **Identifier** | `citation-style-language/schema` @ `e3ce254a` · MIT |
| **Source** | https://codeload.github.com/citation-style-language/schema/tar.gz/e3ce254a72c4470a5ed3b9d23b428017d25674e9 |
| **Digest** | `594ae2f930c8d824b67bc3ae4eefa1238cbbed0529c34e31ffd69a0e910f63d4`, of the archive, re-fetched 2026-11-01 unchanged |

## Overview

The repository holds the schemas for the Citation Style Language: RELAX NG for style and locale XML, and JSON Schema for CSL-JSON. The format began as citeproc-js's input and was codified afterwards, so the schema follows practice rather than leading it (README). `csl-data.json` defines an array of items, each requiring `type` and `id`, with a closed property set (`additionalProperties: false`) and a 45-value `type` enum. `csl-citation.json` wraps items with citation context such as locators and prefixes. The `custom` object exists for key-value data with no designated field.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | A bibliographic data format |
| Cryptography | `none` | Same |
| This project | `adjacent` | The library's interchange format, not a mofn design input |

**It bears on no `DEC-*` or `R-*`, so `bears_on` is empty.** Its use is `docs/construction.md` decision 1, under mofn backlog T-020.

**Checked 2026-11-01 against the schema at this commit.** `bin/export` on this branch produced 442 items, and all validated against `csl-data.json` with 0 errors under `jsonschema` Draft-07. Three things that validation does not show:

- **`bin/export` emits no `author`.** The keys it writes are `id`, `type`, `title`, `URL`, `issued`, `DOI`, `ISBN`, `publisher` and `number`. A citation built from `exports/references.json` has no authors, and the schema cannot catch that because only `type` and `id` are required. `bin/export` was not changed here.
- **Types are coarse.** `paper` maps to `article-journal`, so a conference paper or technical report is mistyped, though the enum has `paper-conference` and `report`.
- **`custom` is an answer to decision 1's open question.** Typed relations are lost today. `custom` could carry them inside the schema, though whether Zotero, Citation.js or pandoc keep it on a round trip was not tested.

## Implementations

**Searched 2026-11-01.** Named from the README and `docs/construction.md`, and confirmed on GitHub. None was run.

| Name | Kind | License | URL |
|---|---|---|---|
| citeproc-js | open source, CSL processor | not checked: GitHub reports NOASSERTION | https://github.com/Juris-M/citeproc-js |
| citeproc | open source, Haskell, CSL processor | BSD-2-Clause | https://github.com/jgm/citeproc |
| Citation.js | open source, converter | MIT | https://github.com/citation-js/citation-js |
| Zotero | open source, reference manager | not checked: GitHub reports NOASSERTION | https://github.com/zotero/zotero |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, pinned commit, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A `repo` is outside FX-1's type scope. The schema files stay in the upstream archive, and none is committed here.

## Limits

- **It is not a standard, and the old usefulness note overstated it.** That note called this repo the format's "normative schema". The README says in bold that the schema is not yet fully normative and warns about compatibility with other tools. So 0 validation errors is necessary, not sufficient, for interoperability. The note is corrected in `record.yaml`.
- **The schema disagrees with its own description.** `date-variable` says EDTF strings are preferred, yet its `anyOf` allows only the object form. A test item with `"issued": "2007-07"` failed validation here, and `date-parts` passed. `bin/export` writes `date-parts`, so we are on the side that validates.
- **It does not define semantics.** Field meaning, name particles and how processors use each variable are not in these files. The CSL specification is not held here.
- **Versioning is loose.** `csl-data.json` has a `v1.0` `$id` and `csl-citation.json` a `latest` one, and the commit is ahead of any tag. The changelog was generated from commits and has no entry for this commit.
- **Read scope.** `README.md`, `csl-data.json`, `csl-citation.json`, `LICENSE.txt` and the head of `CHANGELOG.md` were read whole, plus the start of `tests/schemas/input/test_json.py`. The RELAX NG style schemas under `schemas/styles/` were not read, as they describe styles, which we do not use.
