---
record: nist-sp-800-140e
kind: schema
title: "nist-sp-800-140e — schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# Schemas

SP 800-140E has no formal notation. Its one table is Table 1; the rows are in `../examples/table-1.derived.json`, produced by `build.derived.py` from the source lines and validated against `AuthenticationLevelRow`.

## Derived (written by this library)

Every file here is **derived**: `nist-sp-800-140e` ships no CDDL, ASN.1 or JSON Schema of its own, so each is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:nist-sp-800-140e:<Name>`) written from the prose or tables the Source lines column names. Nothing here is verbatim.

| file | locator | what it validates | source lines |
|---|---|---|---|
| `AuthenticationLevelRow.derived.schema.json` | §6.2 | one row of Table 1: the authentication mechanisms permitted at one FIPS 140-3 security level | L292 |
| `AuthenticationMechanismClaim.derived.schema.json` | §6.2 | a vendor's claim that a module authenticates operators with one mechanism at one level | L282-285 |

## Rebuild and self-check

`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and `../examples/*.derived.json`. It resolves every `constrained_by` id from `../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every quotation from the cached source, then validates every case in `../examples/*-cases.derived.json` with the `jsonschema` package (`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has `jsonschema` installed, from the repository root:

```sh
python3 records/nist/nist-sp-800-140e/distilled/schema/build.derived.py
```

Last run: 2 structures, 49 cases (8 accept, 41 reject), 0 unexpected.

Every structure with a mandatory field is tested with the empty object and with each mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each field, and with an undefined extra field; a field the source makes a `shall` boolean is `const: true`, so `false` is rejected.

Source defects found while reading: (1) section 5.2 says the modifications follow the format of ISO/IEC
**24579**; every sibling document says 24759. (2) Table 1's Level 2 cell prints 'Memorized secret' before the
row label in the cleaned rendering (lines 299-302), and its mechanism names are capitalised differently from
the Level 3 bullets ('Memorized secret' against 'Memorized Secret'); the schema uses the Level 3 bullet
spelling. (3) 'Level 3 authentication mechanism' in the Level 2 cell is a reference, expanded here to the
nine Level 3 bullets; that expansion is this library's reading.
