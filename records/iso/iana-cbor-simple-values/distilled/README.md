---
schema: "library-doc/v1"
id: iana-cbor-simple-values-distilled-index
record: iana-cbor-simple-values
type: index
updated: "2026-10-16"
---

# Distilled artifacts — IANA CBOR Simple Values registry

**Not an FX-1 extraction, and not an unfinished one.** This record is a
`type: dataset` held to the **summary bar** — `summarized`, valid typed
relations, `bin/validate` clean — and carries **no `distillation` block** and
no `profile`. library#39 scoped it that way in terms:

> "iana-cbor-tags, iana-cbor-simple-values — registries, not FX-1 types;
> extract the tables as data, because option 5 is defined by what it excludes."

FX-1 fires on `rfc` / `draft` / `spec` / `ietf` records, and its artifact set
has no subject here: a registry states no BCP 14 requirements, defines no
protocol and carries no test vectors. It allocates code points. The table is
the only thing an extraction could get wrong, so the table is what this
directory holds, complete and row-for-row.

| file | what it is | coverage |
|---|---|---|
| `tables.yaml` | every row of the registry, in page order, under the page's own column headings | **complete** — 9 rows |
| `README.md` | this index | — |

`reviewed_by` is empty in `tables.yaml`. An unreviewed artifact may be read;
nothing may be built on it (`docs/requirements.md`).

## What `tables.yaml` covers

| key in `tables.yaml` | table | columns (the page's own) | rows |
|---|---|---|---|
| `rows` (top level) | **CBOR Simple Values** | Value · Semantics · Reference | **9** |
| `registration_procedure_ranges` | the page's Range / Registration Procedures / Note table | Range · Registration Procedures · Note | 2 |

Nine rows is the whole registry. The simple-value space is one byte wide
(0–255) and almost all of it is unassigned, so most rows are ranges, kept
exactly as the page expresses them.

**The page is internally inconsistent, and the snapshot preserves that
rather than repairing it.** In page order the Value column reads
`0-19`, `20`, `21`, `22`, `23`, `24-31`, `58-255`, `59`, `60-255`. Two things
are wrong with that and neither is ours to fix:

- **Values 32–57 appear in no row at all.** The registration-procedures table
  governs `32-255` ("Specification Required"), so the space exists; the value
  table simply omits it.
- **`58-255 Unassigned` overlaps the two rows that follow it.** IANA's usual
  rendering splits an unassigned range around a new assignment; here the split
  left a range that still swallows the assigned value 59 and the `60-255`
  tail. The row that was presumably meant is `58`.

Both are recorded verbatim in `tables.yaml`, which is why the artifact is
worth having: a hand-written restatement would have quietly tidied them away.

## This is a point-in-time snapshot of a LIVE registry

The registry changes. The digest in `record.yaml` and in `tables.yaml`
(`d1733d66…`) identifies **a snapshot taken 2026-10-16**, not a work. The page
reports itself created 2013-09-19 and last updated **2026-01-15**.

The previous digest recorded on this record (`bcd0848a…`, retrieved
2026-09-22) **no longer matched the live page** when this pass fetched it.
Any count or absence stated here or in `summary.md` is true as of 2026-10-16
and must be re-checked rather than cited as settled — in particular the single
assigned value in the Specification Required range, **value 59**, which is a
`TEMPORARY` registration from `draft-ietf-spice-sd-cwt-06` that expires
2026-12-16 and will then disappear, taking the registry back to RFC 8949's
original four.

Because the bytes are not committed (`library/CLAUDE.md`: never commit a
third-party document), `tables.yaml` is the only durable record we hold of what
the registry said on this date.

## Provenance

Generated from the cached XHTML at `.cache/iana-cbor-simple-values.txt`
(gitignored), then checked by hand against the source markup. Cell text is the
page's rendered text: markup stripped, HTML entities decoded, whitespace
collapsed, link text kept.
