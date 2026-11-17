---
record: slsa-vsa-1-2
kind: examples
title: "slsa-vsa-1-2 — examples and test vectors"
extracted: "2026-11-17"
reviewed_by: ""
---

# Examples and test vectors

The source prints **one example VSA** (§4), the `predicateType` string, the schema
block, and two worked consumer checks (§5.1). It prints no digest that verifies, no
signature, no envelope. Two kinds of file:

- `*.verbatim.*` — cut out of the source **by script, by line range** (the skeleton's
  detector finds XML `sourcecode` only: it reported "code blocks: 0"). Byte-identical
  to the cached `.bin` (the original Markdown); the rendering `.txt` carries the same
  lines, a column-0 ordered-list item gaining one leading space.
- `*.derived.*`, `reproduce.py`, `build-messages.derived.py` — written by this library.
  Inputs the source does not give are **chosen here** and every expected value follows
  from the source's rules, nothing else.

## Run

```sh
python3 -I records/openssf/slsa-vsa-1-2/distilled/examples/reproduce.py          # check
python3 -I records/openssf/slsa-vsa-1-2/distilled/examples/reproduce.py --write  # rewrite fixtures, then check
```

Needs `.cache/slsa-vsa-1-2.bin` and `.txt` (never committed). It: re-runs
`../render-source.py` and requires the `.txt` byte for byte; finds every fence by
script and requires exactly L13-15, L64-104, L232-270; cuts and compares the verbatim
files; rebuilds the derived files; runs the consumer cases with a step-mutation test;
cross-checks field names (§3.2 headings and their required/optional words, the schema
block, the example, `../schema`, `../messages.yaml`) and the 19 backticked `SlsaResult`
tokens of the prose (the four in the §4 example are checked with the example); then runs `../schema/check-schemas.derived.py` and
`build-messages.derived.py --check`. Last line: `checks run: N, failed: 0`.

## Verbatim fixtures

| file | source | content | expected result |
|---|---|---|---|
| `predicate-type.verbatim.json` | Preamble L14 (inside the json fence L13-15) | the `predicateType` member | a JSON member, not a document; `predicate-type.derived.json` wraps it and it equals the `const` of `vsa-statement.derived.schema.json` |
| `../schema/vsa-schema.verbatim.jsonc` | §3 L65-103 (inside L64-104) | the schema block | not JSON (see `../schema/README.md`); its member names equal the predicate schema's properties (checked) |
| `example-vsa.verbatim.jsonc` | §4 L233-269 (inside L232-270) | the example VSA, jsonc, no enclosing braces, trailing comma at L266 | **not JSON as printed**; `example-vsa.derived.json` is accepted by `vsa-statement.derived.schema.json` |
| `verify-example-1.verbatim.txt` | §5.1 L322-343 | worked example 1: full delegation to verifier V, `verifiedLevels` contains `SLSA_BUILD_LEVEL_UNEVALUATED` | cases C-01 to C-10 of `consumer-verification.derived.json` |
| `verify-example-2.verbatim.txt` | §5.1 L345-367 | worked example 2: "Artifact A at resource R must have a passing VSA from verifier V showing it meets SLSA Build Level 2+" | cases C-11 to C-19 |

## Derived fixtures

| file | source | content | expected result |
|---|---|---|---|
| `predicate-type.derived.json` | L14 | `{"predicateType": ...}` | equals the constant in the Statement schema |
| `example-vsa.derived.json` | L233-269 | the §4 example with `//` comments removed, enclosing braces added, trailing commas removed (string-aware scanner in `reproduce.py`); values unchanged. Carries no header: a JSON file cannot hold a comment | ACCEPT by `vsa-statement.derived.schema.json` (all fields present, `verifiedLevels` has one level, `dependencyLevels` holds three levels of the Build track) |
| `consumer-verification.derived.json` | §5 L281-306, §5.1 L322-367 | 19 cases: a Statement, `signature_ok`, the consumer's expectation (artifact digest, `verifier.id`, `resourceUri`, acceptable levels), expected `accepted` and first `failed_step`, and the schema verdict | `consumer_verify()` in `reproduce.py` computes `expect` (steps 1-7 in order); `check-schemas.derived.py` asserts `schema_valid`. Disabling any one step flips at least one case (mutation test), and each step is the first failure of some case |
| `../schema/schema-tests.derived.json` | §3, §3.1, §3.2, §6 | 132 ACCEPT / REJECT instances | see `../schema/README.md` |

`consumer_verify` is §5 as §5.1 applies it. Step 1 (signature on the envelope) is a
boolean input: the envelope is outside the source. Step 6 tests `verificationResult`:
both §5.1 examples say `slsaResult` (L336, L360), source defect SD-15 (`../normative.md`). Example 1
expects the array to **contain** the value, example 2 that it **is** one of two values
(SD-14): the array reading "contains one of" is used for both.

## Case failures against the protocol model

`consumer-verification.derived.json` numbers the steps as §5 does (1 to 7). `../protocol.yaml` F04
has two more steps (delivery, F04 step 1; parsing, F04 step 3), so its numbers run higher. Joined by
script on the quoted source lines (7 of 7 agree), the error-path steps and the rejecting M01
transitions:

| §5 step | source lines | F04 step | error path | M01 transition | first failure of |
|---|---|---|---|---|---|
| 1 signature | L283-285 | 2 | E02 | T03 | C-02 |
| 2 subject | L287-288 | 4 | E03 | T07 | C-03 |
| 3 predicateType | L290-292 | 5 | E04 | T09 | C-04 |
| 4 verifier.id | L294-296 | 6 | E05 | T11 | C-05 |
| 5 resourceUri | L298-300 | 7 | E06 | T13 | C-06 |
| 6 verificationResult | L302-303 | 8 | E07 | T15 | C-07, C-18 |
| 7 verifiedLevels | L305-306 | 9 | E08 | T17 | C-08, C-13 to C-16 |

## What the examples found in the source

- **The jsonc is not JSON** (SD-4): no braces, one missing comma, trailing commas.
  A reader that feeds either block to a JSON parser fails; the derived example is what
  to parse.
- **`slsaResult` vs `verificationResult`** (SD-15): the 1.2 change history says the typo
  was fixed (L405-406); both §5.1 examples still carry it (L336, L360). Case C-18 pins that
  a VSA written with `slsaResult` fails step 6 and the schema.
- **C-19**: a VSA with two levels in one track passes a consumer's step 7 yet violates
  L199; the schema's semantic rule SEM-01 is what rejects it, not the consumer steps.
- **Empty `verifiedLevels`** (C-15) is schema-valid: the source does not forbid it, and it
  can never satisfy step 7.
- Source-defect ids are `../normative.md`'s canonical ones; its crosswalk maps the ids this
  lane used in pass 1 (SD-01 to SD-10).
