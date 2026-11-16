---
record: nist-sp-800-140a
kind: schema
title: "nist-sp-800-140a — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140A has no formal notation at all. Its whole content is one modified vendor-evidence item; the schema below is the thinnest honest rendering of it.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140a` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140a:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `MinimumDocumentation.derived.schema.json` | §6.1 | the documentation a vendor provides a testing laboratory for one cryptographic module (ASA.01, VEA.01.02, TEA.01.02) | L266-268 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140a/distilled/schema/build.derived.py
```

Last run: 1 structures, 16 cases (2 accept, 14 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Source defect: VEA.01.02 and TEA.01.02 (R-0004, R-0005) measure the documentation against the validation
authority's requirement and management documentation, which SP 800-140A neither names nor cites
(normative.md SD-2), so `minimum_requirements_specified_in` is a free string.
