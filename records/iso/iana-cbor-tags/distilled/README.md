---
schema: "library-doc/v1"
id: iana-cbor-tags-distilled-index
record: iana-cbor-tags
type: index
updated: "2026-10-16"
---

# Distilled artifacts — IANA CBOR Tags registry

**Not an FX-1 extraction, and not an unfinished one.** This record is a
`type: dataset` held to the **summary bar** — `summarized`, valid typed
relations, `bin/validate` clean — and carries **no `distillation` block** and
no `profile`. library#39 scoped it that way in terms:

> "iana-cbor-tags, iana-cbor-simple-values — registries, not FX-1 types;
> extract the tables as data, because option 5 is defined by what it excludes."

FX-1 fires on `rfc` / `draft` / `spec` / `ietf` records, and its artifact set
(normative text, BCP 14 requirements with reconciled counts, protocol model,
state machines, test vectors) has no subject here. A registry states no
requirements and specifies no protocol; it allocates code points. The one
thing it has that an extraction could get wrong is **the table**, so the table
is what this directory holds, complete and row-for-row.

| file | what it is | coverage |
|---|---|---|
| `tables.yaml` | every row of all three sub-registries on the page, in page order, under the page's own column headings | **complete** — 358 / 3 / 29 rows, see below |
| `README.md` | this index | — |

`reviewed_by` is empty in `tables.yaml`. An unreviewed artifact may be read;
nothing may be built on it (`docs/requirements.md`).

## What `tables.yaml` covers

One IANA page carries three separate sub-registries. All three are captured:

| key in `tables.yaml` | sub-registry | columns (the page's own) | rows |
|---|---|---|---|
| `rows` (top level) | **CBOR Tags** — the tag number space itself | Tag · Data Item · Semantics · Reference · Template | **358** |
| `subregistries.timescales` | **Timescales** (RFC 9581) | Timescale · Value · Semantics · Reference | 3 |
| `subregistries.time_tag_map_keys` | **Time Tag Map Keys** (RFC 9581) | Value · Semantics · Reference | 29 |

Plus `registration_procedure_ranges` (the page's Range / Registration
Procedures table, 3 rows) and `footnotes` (footnote [1], with the two rows that
cite it — tags 40 and 1040).

Row counts reconcile against the source bytes: the `table-tags` element holds
359 `<tr>` (1 header + 358 data rows) and 1790 `<td>` = 358 × 5 columns, so no
row and no cell was dropped. Ranges the page itself expresses as ranges
(`121-127`, `32768-18446744073709551615`, `-18446744073709551616..-19`) are
kept exactly as given and are **not** expanded; `Unassigned` and `Reserved`
range rows are kept rather than elided, because the shape of the unassigned
space is part of what the registry says.

**Deliberately not captured,** recorded in `tables.yaml` under `not_captured`:
the page's **Contact Information** table — a directory of registrant names and
obfuscated e-mail addresses. It is not a registry assignment and is personal
contact data we have no reason to republish.

## This is a point-in-time snapshot of a LIVE registry

The registry changes. The digest in `record.yaml` and in `tables.yaml`
(`5f3570cf…`) identifies **a snapshot taken 2026-10-16**, not a work. The page
reports itself created 2013-09-19 and last updated **2026-10-08**, eight days
before this snapshot.

The previous digest recorded on this record (`0d338a17…`, retrieved
2026-09-22) **no longer matched the live page** when this pass fetched it;
the registry had moved under it in three weeks. Expect the same again. Any
count or absence stated here or in `summary.md` is true as of 2026-10-16 and
must be re-checked rather than cited as settled — including the three
`TEMPORARY` registrations (tags 58, 60, 62), which expire in 2026 and 2027 and
will simply vanish.

Because the bytes are not committed (`library/CLAUDE.md`: never commit a
third-party document), `tables.yaml` is the only durable record we hold of what
the registry said on this date. That is its point: it makes the snapshot
citable and diffable against the next one.

## Provenance

Generated from the cached XHTML at `.cache/iana-cbor-tags.txt` (gitignored),
then checked by hand against the source markup. Cell text is the page's
rendered text: markup stripped, HTML entities decoded, whitespace collapsed,
link text kept (so a Reference cell reads `RFC 8949`, and a privately-specified
one reads `<url>; <registrant name>` exactly as the page prints it).
