---
record: slsa-provenance-1-2
kind: examples
title: "slsa-provenance-1-2 — examples and test vectors"
extracted: "2026-11-16"
reviewed_by: ""
---

# Examples and test vectors

The source prints no complete provenance. It has three fenced examples and two
prose examples; all five are fixtures here. A fixture is the rendering's lines
joined by a newline plus one final newline, cut by script, never retyped.
`reproduce.py` re-cuts each one, compares bytes, and runs the expectation.
Everything else in this directory is derived, and its filename says so.

## Run

```sh
python3 -I distilled/examples/reproduce.py            # check
python3 -I distilled/examples/reproduce.py --write    # rewrite the verbatim fixtures and migration-v1-output, then check
```

Stdlib only; it imports the validator in `../schema/check-schemas.derived.py`.
Last run: 49 checks, 0 failed. Besides the fixtures it re-runs
`../render-source.py` over the `.bin` and the two includes and requires the
output to equal the `.txt` byte for byte, requires the set of fence lines in the
rendering to equal the fences the manifest accounts for, and checks that the cue
and proto in `../schema/` equal the include files.

## Verbatim fixtures

| file | source | content | expected result |
|---|---|---|---|
| `ex-01.verbatim.txt` | preamble L17 (json fence L16-18) | the `predicateType` member | not a document: wrapped in braces it parses, and `predicateType` is accepted by the schema's `PredicateType` |
| `ex-02.verbatim.txt` | §4.3 L343-350 (json fence L342-351) | `externalParameters` and `resolvedDependencies` for a git repository | wrapped in braces it parses; each member is accepted by the `BuildDefinition` property of that name; the fragment alone is rejected as a `BuildDefinition` (no `buildType`, L272); with a `buildType` and a builder added it is a valid predicate |
| `ex-03.verbatim.txt` | §7 L580-616 (javascript fence L579-617) | the v0.2 to v1 mapping pseudocode | **not JSON** (comments, `old.*` references, the `+` operator); implemented as `migrate_v02` and checked against `migration-v1-output.derived.json` |
| `ex-04.verbatim.txt` | §4.3 L287 | the example `buildType` URI, a prose line | accepted as `TypeURI` and as `buildType` |
| `ex-05.verbatim.txt` | §4.7 L543-544 | the extension-field naming rule and its example name | the one code-quoted `vendor_fieldname` name is accepted as an extra member at four object levels |

The rendering has five fenced blocks, ten fence lines: three are the fixtures
above and two (cue L124-173, proto L188-239) are kept as
`../schema/provenance.verbatim.cue` and `.proto`; the manifest lists all five
under `fences_accounted_for` and `reproduce.py` requires the list to equal the
fence lines found. No other inline JSON occurs; inline code spans such as `externalParameters["config"]`
(L624) are names, not examples.

## Derived fixtures

Marked derived because every value was chosen here, not taken from the source.

| file | what | expected result |
|---|---|---|
| `provenance-minimal.derived.json` | only the members REQUIRED for SLSA Build L1 | accepted at the schema root |
| `provenance-full.derived.json` | every documented member, ex-02's dependency included | accepted at the root |
| `statement-full.derived.json` | the full predicate in the cue summary's outer object | accepted as `Statement` |
| `migration-v02-input.derived.json` | a v0.2 object shaped only as the pseudocode reads it | input to `migrate_v02` |
| `migration-v1-output.derived.json` | the pseudocode applied to the input; `buildType` chosen here | equals `migrate_v02(input)`; accepted at the root; its key set minus the input's own data keys equals the quoted keys of ex-03 |
| `manifest.derived.json` | the table above as data: file, source lines, fence, check, expectation | read by `reproduce.py` |

Two further derived checks live in `reproduce.py`. A v0.2 object with no
`configSource`, `environment`, `materials` or `metadata` migrates to a predicate
the derived schema accepts, under this library's reading that an expression over
an absent member yields nothing and the member is omitted (JavaScript itself
would throw on `old.invocation.configSource.uri`; the source leaves the case
undefined, SD-12). The appended dependency is then an empty descriptor, `{}`,
which the schema accepts only because in-toto's descriptor rules are outside
this source. A v0.2 object with no parameters at all migrates to an empty
`externalParameters`, which the schema rejects (source defect SD-7).

## What the fixtures do not cover

The source has no signature, no envelope and no wire bytes; DSSE wrapping and
the Statement's `subject` rules are in-toto's. No test vector exists for a
digest or a timestamp, and the two real build-type documents the source indexes
(L569-570) are linked, not reproduced.
