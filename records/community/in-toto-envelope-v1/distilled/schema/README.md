---
record: in-toto-envelope-v1
kind: schema
title: "in-toto-envelope-v1 — schemas"
extracted: "2026-11-16"
reviewed_by: ""
---

# in-toto-envelope-v1 — schemas

**The source ships no schema.** `spec/v1/envelope.md` has no code block, no
CDDL, no JSON Schema, no grammar (skeleton report: 0 schema blocks). It states
field requirements in prose (§2), two media-type templates (§2, §4) and three
file-name templates (§3). So **nothing here is verbatim**; everything formal is
the library's own and carries `.derived.` (`docs/extraction.md`, *Derived vs
verbatim*). Do not cite either file as the in-toto specification's schema.

| file | derived | what it covers | what it deliberately does **not** constrain |
|---|---|---|---|
| `envelope.derived.schema.json` | yes. `$id: urn:library:in-toto-envelope-v1:envelope.derived` | JSON Schema 2020-12. `GenericEnvelope` (§2 general requirements), `DsseEnvelope` (the root; §2 DSSE-specific requirements), `DsseSignature`, `GenericSignature`, `Statement` (only `_type`), `PayloadTypeGeneric` (`application/vnd.in-toto+<encoding>`), `PayloadTypeDsse` (`…+json` and `…<predicate>+json`), `StorageMediaType` (`…<predicate>+dsse`, §4), `EnvelopeFileName` and `EnvelopeFileNameWithKeyid` (§3), `Base64Text`, and `RN` (the assumed token class) | the encoding of signature bytes; keyid nesting (both accepted) and a top-level `keyid`'s type (a list, one per signing key, is accepted); DSSE members defined outside this source (`sig` is typed, not required); the base64 alphabet, and padding beyond requiring that present padding be what the length calls for; the character set of `<encoding>`, `<predicate>`, `<step-name>`; empty `signatures`; unknown members; media-type case and parameters. Listed in the file's own `x-open`. Not wire-observable, so not bound at all: that `payloadType` is signed with the payload, no payload parse before verifying, canonicalization independence, algorithm hints, consumers' reliance on `predicateType` |
| `check-envelope.derived.py` | yes | `python3 -I check-envelope.derived.py`. A stdlib validator that implements exactly the keywords the schema uses and **exits on any other keyword**, plus `contentEncoding`/`contentMediaType`/`contentSchema` asserted (standard validators only annotate them). Runs every case in `../examples/cases.derived.json` and a **mutation pass**: every asserting keyword in the schema is removed in turn (44 of them; 43 removals, the one equivalent mutant, `GenericSignature`'s `if` type test, skipped with its reason), and each removal must flip at least one case, so a keyword that binds nothing fails the run. Every definition but the three reached only through a parent must have a reject case | |

## Accept and reject

`../examples/cases.derived.json` holds 93 instances: 32 the schema must
accept, 61 it must reject, each reject naming the error it must produce
(`error_contains`), so a reject for the wrong reason fails. Every case has a
`basis`: `source` (a cited line says so), `derived-assumption` (a reading or
assumption of ours, named in the schema), or `source-silent` (the source says
nothing; the schema's behaviour is pinned so a change is deliberate; 11 cases).
Cited requirement ids are resolved by script from `../requirements.yaml` and read
back beside their texts: a split half by its child (R-0035, R-0036), and an
inferred entry where a case rests on one (R-0043, R-0045, R-0049).

Rejects that matter: missing or non-array `signatures`; a `payload` that is not
base64 (including padding the length does not call for), is base64 of non-JSON, of a JSON array, of an object without `_type`,
or is carried unencoded; `payloadType` of the storage form (`+dsse`) or of
another encoding in the DSSE profile; a trailing newline on any pattern-bound
string (the checker uses ECMA-262 anchoring, not Python's `$`). A standard
validator disagrees on exactly those two classes: it only annotates the
`content*` keywords, and python-jsonschema's `$` accepts a trailing newline (10
of the 93 cases, measured with jsonschema 4.26).

## Source tension the schema cannot hide

`PayloadTypeDsse` is **not** a subset of `PayloadTypeGeneric`: the
predicate-specific form of §2 line 45 does not match the §2 line 39-40 form
(source defect SD-1, `../normative.md`). `GEN-R05` pins it. The DSSE root schema uses
`PayloadTypeDsse` alone.

## Checks

```sh
python3 -I distilled/schema/check-envelope.derived.py
python3 -I distilled/examples/reproduce.py        # also re-extracts the fixtures; needs .cache/in-toto-envelope-v1.bin
```
