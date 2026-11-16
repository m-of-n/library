---
record: fips-140-3
kind: schema
title: "fips-140-3 — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

FIPS 140-3 prescribes no document or message format, so there is nothing verbatim to copy: the two files below are derived from the area list and levels of paragraph 3 and the Approved security function test of paragraph 10.

## Derived (written by this library)

Every file here is **derived**: `fips-140-3` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:fips-140-3:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `SecurityLevelClaim.derived.schema.json` | ¶3 | one claim of a security level for one of the eleven security areas | L100-108 |
| `ApprovedSecurityFunctionBasis.derived.schema.json` | ¶10 | why a security function counts as Approved (paragraph 10, items a to d) | L169-185 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/fips-140-3/distilled/schema/build.derived.py
```

Last run: 2 structures, 23 cases (3 accept, 20 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Not modelled: Table 1 (which SP 800-140x modifies which ISO/IEC 19790 annex or 24759 clause) is a locating
aid, see the header of `../messages.yaml`.
