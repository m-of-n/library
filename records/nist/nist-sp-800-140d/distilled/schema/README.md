---
record: nist-sp-800-140d
kind: schema
title: "nist-sp-800-140d — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140D has no formal notation: its section 6.2 is a numbered list of citations. The one schema describes a row of that list.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140d` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140d:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `ApprovedSspMethodReference.derived.schema.json` | §6.2 | one row of the CMVP approved sensitive security parameter generation and establishment methods list: the document that specifies a method | L303-305 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140d/distilled/schema/build.derived.py
```

Last run: 1 structures, 37 cases (2 accept, 35 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Row cut: `build.derived.py` cuts section 6.2 into rows by script. A row ends at its URL (a URL split after a
hyphen across a page ends one token later, as for SP 800-56B Rev. 2, lines 343-349); the bullets and the note
under row 1 are attached by the document's own order (the layout table at the top of the spec). Coverage is
checked: the number of `https://` tokens in lines 309-393 equals the number of rows (13 each).

Rendering: row 3 prints its URL across a page break (lines 343-349); the reader joins it at the line-end
hyphen. Source: row 12's first author is printed Sonmez (line 390) and row 5's Sönmez (line 355); both are kept as printed.

Join: each row's `requirements` lists the requirements.yaml entries it is the machine form of (its citation, and
its bullets or note), resolved by script from the row's lines; the build refuses a row entry of section 6.2 that
no row carries, or one that two rows carry.
