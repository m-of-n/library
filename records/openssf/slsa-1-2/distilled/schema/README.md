---
record: slsa-1-2
kind: schema
title: "slsa-1-2 — schemas"
extracted: "2026-10-02"
reviewed_by: ""
---

# SLSA v1.2 schemas

SLSA publishes no normative JSON Schema. `build-provenance.md` gives the predicate as a cue-like
sketch and a protobuf summary, and says the field text is authoritative. The `verbatim` files are
those code blocks, byte-for-byte (dedented), from the release-branch Markdown
(`slsa-framework/slsa` `releases/v1.2` @ `ae7fc762`). The `derived` files are machine-checkable
JSON Schemas (Draft 2020-12) that the library wrote from the field tables. Each one's `$comment`
names its source section and the requirement ids it encodes.

| file | status | source | what it covers |
|---|---|---|---|
| `provenance-v1.verbatim.cue` | verbatim | build-provenance.md § Schema (cue-like) | in-toto Statement v1 + `https://slsa.dev/provenance/v1` predicate (buildDefinition, runDetails) |
| `provenance-v1.verbatim.proto` | verbatim | build-provenance.md § Schema (protobuf) | Provenance, BuildDefinition, RunDetails, Builder, BuildMetadata, ResourceDescriptor messages |
| `vsa-v1.verbatim.jsonc` | verbatim | verification_summary.md § Schema | VSA predicate `https://slsa.dev/verification_summary/v1` sketch |
| `provenance-v1.derived.schema.json` | derived | build-provenance.md field tables | REQUIRED fields per Build level, types, ResourceDescriptor "at least one of uri/digest/content" |
| `vsa-v1.derived.schema.json` | derived | verification_summary.md § Fields | required/optional VSA fields, `verificationResult` enum, SlsaResult pattern |
| `source-vsa-v1.derived.schema.json` | derived | source-requirements.md § Source VSA items 1–6 (R-0118..R-0132) | Source-track profile applied on top of the VSA schema |

Validated 2026-10-02 with python `jsonschema` 4.19 against the fixtures in `../examples/`. The results are in `../examples/vectors.yaml`.
Some MUSTs cannot be detected by a schema, for example R-0236, and the vectors say so.
