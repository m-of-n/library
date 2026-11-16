---
record: nist-sp-800-140c
kind: schema
title: "nist-sp-800-140c — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140C has no formal notation: its section 6.2 is a list of citations under sub-headings. The one schema describes a row of that list.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140c` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140c:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `ApprovedSecurityFunctionReference.derived.schema.json` | §6.2 | one row of the CMVP approved security functions list: a function group and the document that specifies it | L306-307 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140c/distilled/schema/build.derived.py
```

Last run: 1 structures, 39 cases (3 accept, 36 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Row cut: `build.derived.py` cuts section 6.2 into rows by script. A row ends at its URL (a URL split after a
hyphen across a page ends one token later); headings, bullets and the SKIPJACK NOTE are placed by the
document's own order (the layout table at the top of the spec). Coverage is checked: the number of `https://`
tokens in lines 309-491 equals the number of rows that carry a citation (24 each).

Join: each row's `requirements` lists the requirements.yaml entries it is the machine form of (its function
sub-heading, its citation, its bullets or NOTE), resolved by script from the row's lines; the build refuses a
row entry of section 6.2 that no row carries, or one that two rows carry (a sub-heading is shared by its rows).
`designation` is parsed from the series: the SP 800-38A Addendum is `SP 800-38A Addendum`, a document of its own.
