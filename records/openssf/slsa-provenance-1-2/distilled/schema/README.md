---
record: slsa-provenance-1-2
kind: schema
title: "slsa-provenance-1-2 — schemas"
extracted: "2026-11-16"
reviewed_by: ""
---

# Schemas

The source ships two machine-readable summaries of the predicate, both
informative: the text is authoritative where they disagree (source L116-117
for the cue file, L178-179 for the proto). It ships **no JSON Schema**, so the
JSON Schema here is derived. Line numbers are those of
`.cache/slsa-provenance-1-2.txt`, the rendering built by `../render-source.py`.

| file | kind | what it is |
|---|---|---|
| `provenance.verbatim.cue` | verbatim | the cue summary, rendering L125-172 (inside the fence at L124-173); byte-identical to the Jekyll include `spec/schema/provenance.cue`, sha256 `0ddd00372622d1c04f71d1fb2666579af089eb733c9c5d838d158489b2ea6145` |
| `provenance.verbatim.proto` | verbatim | the protobuf summary, rendering L189-238 (fence L188-239); byte-identical to `spec/schema/provenance.proto`, sha256 `ea548207a78bd81b809a449edd5ed36a011a665ca7d15831d1133fe674fc41de` |
| `provenance-v1.derived.schema.json` | derived | JSON Schema 2020-12 for the predicate, `$id` `urn:library:slsa-provenance-1-2:provenance-v1.derived`; `$defs` for Statement, PredicateType, Provenance, BuildDefinition, RunDetails, Builder, BuildMetadata, ResourceDescriptor, TypeURI, Timestamp, OptionalTimestamp |
| `schema-tests.derived.json` | derived | 143 instances: 62 the schema must ACCEPT, 81 it must REJECT, each with the source lines it rests on and a basis |
| `check-schemas.derived.py` | derived | stdlib validator, case runner, keyword-mutation test, cue/proto comparison, optional protoc run, one lint |

Both verbatim files were cut by script from the rendering by line range and
compared with the include files and with the `.bin`'s include directives
(`../examples/reproduce.py` does it again on every run). Their first twelve
lines carry no marker word, so the derived/verbatim header check reads the
filename alone.

## Run

```sh
python3 -I distilled/schema/check-schemas.derived.py            # exit 0 only if every check holds
python3 -I distilled/schema/check-schemas.derived.py --verbose  # every case and mutant
python3 -I distilled/examples/reproduce.py                       # fixtures, rendering, migration
```

Last run (pass 2): 143 cases, 0 mismatched; 144 mutants, 0 survivors; 15 structure
comparisons (6 proto messages, 22 proto fields, 22 cue fields), 0 differences;
lint R-0023 flags the one instance it should and none of the two it should not.

## What the derived schema decides

It is the **SLSA Build L1 profile**: a member the tables label REQUIRED for SLSA
Build L1 (L250, L272, L407, L441, L511) is `required`; every other member is
optional by omission from those lists. (Only `internalParameters` is called
OPTIONAL in words, L78.) Three reading rules are fixed in the schema's
`$comment` and tested:

1. **L110, unset, null and empty are equivalent.** An optional member accepts
   null and its empty value (`""`, `[]`, `{}`). A REQUIRED member rejects both,
   because an empty value is as good as absent. The literal consequence, an
   empty `externalParameters` is invalid, is source defect SD-7 and is tagged
   `ambiguous` in the tests.
2. **L105, unrecognized fields are ignored.** No object closes
   `additionalProperties`; extension fields (L540-553) are accepted at every
   level. The mutation test closes each object in turn and requires an accept
   case to notice, so the tolerance is tested, not just left unsaid.
3. **Member names are lowerCamelCase** (L196-198). A snake_case spelling is an
   unrecognized field.

`required` and `type` keep their JSON Schema meaning only on objects; the
checker applies each keyword only to the instance types it governs.

### Where the text overrides the summaries

- The cue file draws every member without an optional marker. The text names
  which are required, so the schema follows the text (SD-9).
- The proto has no presence rules at all (proto3), and its Timestamp type
  admits nanoseconds where the cue comment draws whole seconds (SD-10).
- The cue lists `sha256`, `sha512` and `gitCommit` in `digest` and then a
  string-to-string wildcard; the wildcard covers every key, so the schema
  states one rule, `additionalProperties` of type string.

### Outside this source, not modelled or modelled from the summaries only

- The in-toto **Statement**: only the four members the cue summary draws
  (`_type`, `subject`, `predicateType`, `predicate`); their required-ness and the
  items of `subject` are in-toto's. Cases tagged `outside-source`. That `subject` holds
  at least one item is this page's (the build outputs one or more artifacts, L96-97,
  R-0068), so an empty `subject` is rejected.
- **ResourceDescriptor**: the member list and types are the summaries'; which
  members a descriptor must carry is in-toto's, so an empty descriptor is
  accepted here. The `content` pattern is standard base64 with optional padding, and
  rejects a string that cannot decode (a lone character, padding alone).
- **TypeURI** and **Timestamp** are in-toto field types (L278, L447, L525). The
  schema requires a URI scheme (inferred from the text calling the value a URI)
  and accepts the RFC 3339 shape with optional fraction and offset (SD-10).
  A scheme alone is a URI (RFC 3986 lets the rest be empty), so `example:` is accepted.
- Rules the schema cannot hold: completeness at SLSA Build L3 (L293-295),
  verifiers rejecting unrecognized `externalParameters` (L302-303), consumers
  accepting only specific signer-builder pairs (L496), a unique `invocationId`
  (L522). The checker lints one SHOULD NOT that is expressible, R-0023 (L333-334).

## Test basis

| basis | count | meaning |
|---|---|---|
| `text` | 103 | the source's prose or tables state it; `source_lines` names where |
| `outside-source` | 33 | in-toto decides it; modelled from the informative cue and protobuf summaries (L124-239) or left open |
| `inferred` | 4 | a reading this library chose (URI scheme; a scheme alone is a URI) |
| `ambiguous` | 3 | the source does not settle it (empty `externalParameters`, timestamp fraction, timestamp offset) |

## Does it bind

A schema that parses is not a schema that binds (`hazards.md` section 7). The
checker deletes, one at a time, every constraint keyword, every `required`
member, every property, every `type` member and every `anyOf` branch, and
closes every object, and asks whether any case changes its verdict. 144 mutants
are tried now (143 in pass 1; pass 2's `minItems` on `subject` adds one); the first run left four alive (a missing `type` reject case for
Statement and Provenance, no accept case with an extra Statement member, and a
`minLength` the pattern already implied). Cases were added for the first three
and the redundant `minLength` was removed, so none survives now.

## Tools, and what was and was not available

- **protoc**: not installed. `check-schemas.derived.py` runs `grpc_tools.protoc`
  when it can import it and otherwise prints SKIPPED. With `grpcio-tools`
  1.85.1 installed in a scratch directory the verbatim proto compiles (exit 0;
  replayed in pass 2, as were the four parser results below).
  Protobuf's own JSON parser then accepted `startedOn` with a fraction and an
  offset, rejected a date-only value, accepted snake_case member names, and
  rejected unknown members unless told to ignore them: a stock protobuf
  consumer does not implement L105 by default.
- **cue**: not installed and not run. The cue file is read by the small parser
  in the checker, which compares its member sets and types with the schema; it
  is not checked against cue's own grammar.
- **jsonschema**: not a library dependency. As a one-off, `jsonschema` 4.26 in a
  scratch directory validated all 139 cases (Draft 2020-12) and agreed with this
  checker on every one; pass 2 re-ran it on all 143 with the same result. Python's `re` lets `$` match before a final newline where
  ECMA 262 does not; the stdlib checker converts a trailing `$` to `\Z`, and a
  Python-`re` validator would accept a trailing newline the schema means to reject.
