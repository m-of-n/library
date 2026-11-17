---
record: slsa-vsa-1-2
kind: schema
title: "slsa-vsa-1-2 — schemas"
extracted: "2026-11-17"
reviewed_by: ""
---

# Schemas

SLSA VSA v1.2 ships **no JSON Schema**. Its formal content is one `jsonc` block
(§3, L64-104) that shows member names with placeholders, the §3.2 field list
(`required` / `optional`), the §3.1 parsing rules and the §6 `SlsaResult`
grammar. The filename says which files are the source's and which are ours.

## Verbatim (cut from the source by script)

| file | source | content |
|---|---|---|
| `vsa-schema.verbatim.jsonc` | §3 L65-103 (the inside of the jsonc fence L64-104) | the schema block, byte-identical to the cached `.bin`; **not JSON**: no enclosing braces, a missing comma after the `policy` object (L87-88), a trailing comma after `slsaVersion` (L102), `...` ellipses, bare placeholders (`<NAME>`, `<TIMESTAMP>`, `<Int>`) |

Cut and re-checked by `../examples/reproduce.py` (the same script cuts every fence).

## Derived (written by this library from §3, §3.1, §3.2, §6)

`$id: urn:library:slsa-vsa-1-2:<name>.derived`, JSON Schema 2020-12.

| file | instance | source |
|---|---|---|
| `vsa-statement.derived.schema.json` | the VSA in-toto Statement: `_type`, `subject`, `predicateType`, `predicate` | §3 block L66-74, §2 L43, §5 step 3 |
| `vsa-predicate.derived.schema.json` | the `predicate` object | §3.2 L123-226, §3.1 |
| `slsa-result.derived.schema.json` | one `SlsaResult` string | §6 L375-397 |
| `schema-tests.derived.json` | 132 instances (55 ACCEPT of which 14 SILENT, 77 REJECT), each with the source lines that license the verdict | |
| `check-schemas.derived.py` | stdlib validator and runner | |

```sh
python3 -I records/openssf/slsa-vsa-1-2/distilled/schema/check-schemas.derived.py
```

The runner (a) runs every case, requiring the REJECT cases to be rejected **by the
channel they name** (`schema` or `semantic`); (b) validates the §4 example and the
consumer-verification VSAs from `../examples/`; (c) **mutates** every keyword, and every
element of `required` and `enum`, one at a time, and fails if no case changes verdict —
a keyword that binds nothing is reported (it caught a planted `minimum` on a string
during development); (d) checks the member names of the verbatim jsonc against the
schema: the predicate's properties, the members of `verifier` and `policy`, and those of
an `inputAttestations` entry. The validator raises on any keyword it does not
implement. Last line: `checks run: N, failed: 0`.

**Which validator.** JSON Schema patterns are ECMA-262 regular expressions, where `$`
matches only at the end of the input; the in-tree validator rewrites `$` as `\Z`.
Measured by pass 2 with python-jsonschema 4.26, which uses Python's `re`: it agrees on
every case but the three trailing-newline ones (T-054, T-071, T-101), which it accepts,
because Python's `$` also matches before a final newline. A consumer validating with it
gets those three verdicts wrong. `integer` follows 2020-12, so `5.0` is one (pass 1's
validator required a Python `int`; no case had turned on it).

### SlsaResult, exactly

A string **in the level form**, one that starts with `SLSA_` and has `_LEVEL` either at
its end or followed by an underscore (`if`: `^SLSA_.*_LEVEL(_|$)`), must match

    ^SLSA_[A-Z][A-Z0-9_]*_LEVEL_(UNEVALUATED|[0-9]+)$

and any other string is accepted: `FAILED` (R-0078), the verified properties
`verifiedLevels` may carry (R-0053, L196) and other SLSA-endorsed values (L402-404), and
custom values (R-0080). Custom values may not start with `SLSA_` (R-0081), but a `SLSA_`
string outside the level form may equally be an endorsed value: v1.2's verified
properties are `SLSA_SOURCE_TWO_PARTY_REVIEWED` and `SLSA_BUILD_REPRODUCED` (SLSA's
verified-properties page at `ae7fc76`, outside this source). Only SLSA's own list tells
the two apart, so those strings are accepted (`SILENT` cases) and R-0081 is checkable
here only in the level form. Written as `if`/`then`, so there is no redundant `FAILED`
branch to bind nothing.

**Corrected by pass 2.** Pass 1's `if` was `^SLSA_`: it held every `SLSA_` string to the
level grammar and so rejected both v1.2 verified properties, values the source admits in
`verifiedLevels`. Six REJECT cases became `SILENT` (T-050, T-066, T-092, T-093, T-103,
T-104), T-130 and T-131 pin the two properties, and T-132 replaces T-066 as the case that
binds `dependencyLevels`' `propertyNames`, which the mutation test then reported unbound.

Ambiguities, none repaired:

- the source writes the placeholder `<TRACK_NAME>` (L379) and `<TRACK NAME>` (L380);
  underscores are taken, so `SLSA_MY_TRACK_LEVEL_1` and `SLSA_BUILD_LEVEL_LEVEL_3` match;
- the range of `<LEVEL_NUMBER>` is not stated: decimal digits, any length, leading
  zeros admitted (`SILENT` test);
- lower-case `slsa_build_level_1` does not start with `SLSA_`, so it is a custom value;
- `SHOULD be` (L376) makes the grammar a recommendation: only the `SLSA_` prefix is exclusive.

### What JSON Schema cannot say (semantic rule in the checker, or not checkable)

- **SEM-01** one level per SLSA track in `verifiedLevels` (R-0054, L199):
  implemented in `check-schemas.derived.py`, with its own REJECT cases (`via: semantic`)
  and its own mutation test. The track of `SLSA_<T>_LEVEL_<n>` is `<T>`;
  `UNEVALUATED` counts as a level of its track; `FAILED`, verified properties and custom
  values count for none.
- `inputAttestations` contains **all** attestations used (L181-182) and each dependency
  is counted once at its highest level (L216-219): not checkable from the document.
- how `verificationResult` relates to a `FAILED` element of `verifiedLevels`: not
  stated (SD-8); the schema accepts both combinations (SILENT test).

### Readings (marked in each schema's `$comment`)

- `dependencyLevels` admits `null` (L213-214 give it a meaning) though L205 types it
  `object`; counts are integers `>= 0` (`<Int>` at L98, "a count" at L207; the minimum
  is inferred).
- `subject` has `minItems: 1` from "one or more software artifacts" (L43); no
  `additionalProperties: false` anywhere: unknown fields MUST be ignored (L110), URI-named
  extensions are allowed (L115). Tests pin both.
- SHOULD members (`policy.digest`, entry `uri`) are not required.

### Outside this source

The in-toto `Statement`, `ResourceDescriptor` (so which of `name`/`digest` a subject
needs, and the other descriptor members), `DigestSet`, `TypeURI`, `Timestamp`
(so no format check on `timeVerified`, `verifier.id`, `resourceUri`), the signed
envelope of §5 step 1, and the SLSA track and level definitions (so which tracks
exist and what each level means). The link footers (L423-432) name them.
