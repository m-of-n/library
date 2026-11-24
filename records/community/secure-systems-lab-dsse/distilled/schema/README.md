---
record: secure-systems-lab-dsse
kind: schema
title: "secure-systems-lab-dsse — schemas"
extracted: "2026-11-20"
reviewed_by: ""
---

# secure-systems-lab-dsse — schemas

The source ships **one** formal artifact, `envelope.proto`, and no JSON Schema,
no grammar for the PAE and no CDDL. So one file here is verbatim and the rest is
the library's own and carries `.derived.` (`docs/extraction.md`, *Derived vs
verbatim*). Do not cite a derived file as the DSSE specification's schema.

| file | verbatim / derived | what it is | what it must reject |
|---|---|---|---|
| `envelope.verbatim.proto` | **verbatim**: the bytes of `envelope.proto` at commit 1d3370f (sha256 `2f689071…a0cbfb`, 1017 bytes), no header added, cut by script from the archive (`examples/reproduce.py` re-extracts and compares) | proto3 `Envelope` (payload 1, payloadType 2, signatures 3) and `Signature` (sig 1, keyid 2); rendering lines 283-317 | not a checkable schema here (no protoc on the toolchain); its comments are requirements R-0018..R-0022 |
| `envelope.derived.schema.json` | derived, `$id: urn:library:secure-systems-lab-dsse:envelope.derived` | JSON Schema 2020-12 for the JSON envelope of envelope.md 2.1, 2.1.1, 2.1.2 with the proto's types. Definitions: `Base64Text`, `Signature`, `Envelope` (root), `EnvelopeStrict` | a missing `payload`, `payloadType`, `signatures` or `sig`; wrong member types (including JSON null); text that is not base64 in either alphabet, a mix of both alphabets, an impossible length, padding that does not complete a multiple of 4; the singular `signature` member name; for `EnvelopeStrict` also an empty `signatures` |
| `check-envelope.derived.py` | derived | stdlib validator that implements exactly the keywords the schema uses (and refuses any other), asserts `contentEncoding`, runs `../examples/cases.derived.json`, then a removal-mutation pass and an insertion-mutation pass | a schema keyword that binds nothing; a permission the source grants that no case pins |
| `pae.derived.abnf` | derived | the PAE byte format as ABNF, plus the one length-bound rule ABNF cannot say | n/a (a grammar) |
| `check-pae.derived.py` | derived | stdlib builder and strict parser for that grammar; runs `../examples/pae-vectors.derived.json`, a 20000-case round-trip/injectivity property and an exhaustive injectivity pass | a byte string with a wrong version, a leading-zero or non-ASCII LEN, a type or body not matching its LEN, trailing bytes |

## How the JSON envelope is encoded (decisions, each a reading)

- **Presence.** R-0011: `payload`, `payloadType`, `signatures`, and `sig` in each element are `required`, and an empty value still counts as set: the empty string for `payload`, `payloadType` and `sig`; for `signatures` the empty array, which `Envelope` accepts and `EnvelopeStrict` rejects (SD-2). `keyid` is optional; any string, the empty string included, an unset field being treated the same as a set-but-empty one (R-0013).
- **Unknown members.** Allowed at both levels (`additionalProperties` unset): producers MAY add, consumers MUST ignore. The insertion mutants prove that adding `additionalProperties: false` is caught by an accept case.
- **Base64.** Either alphabet (protocol 1.2, envelope 2.1). **Padding is a source silence**: padded and unpadded are both accepted; padding that is present must complete a multiple of 4 (our reading of "RFC 4648"). A mix of `+/` with `-_` is rejected (neither alphabet; also silent in the source). Trailing bits are not checked.
- **Tension, recorded not resolved.** `envelope.md` says `signatures` must be set "even if empty"; `envelope.proto` says `REQUIRED (length >= 1)`. `Envelope` follows the first (accepts `[]`), `EnvelopeStrict` follows the second (cases ENV-A14 and STR-R01 pin both).
- **Source defect.** envelope.md 2.1.2 names `signature` and `signature.sig`; the template and the proto use `signatures` and `sig`. The schema follows the template (case ENV-R05).
- **Not bound** (not wire-observable): that the verified bytes are the bytes handed to the application (R-0008, R-0009), that payloadType is authenticated, that a signature verifies. The full list is the schema's own `x-open`.

## Accept and reject

`../examples/cases.derived.json`: 61 instances (25 accept, 36 reject). Every
reject names `error_contains`, so a reject for the wrong reason fails. Every
case has a `basis` (`source`, `source-conflict`, `derived-assumption`,
`source-silent`) and `cites` (R-ids resolved by script).

## Mutation testing (hazards.md §7: a schema that parses is not a schema that binds)

- **Removal**: each of the 19 asserting-keyword sites in the schema is removed in turn; each removal must make some case miss its stated outcome (accept becomes reject, or a reject loses its stated reason). 19 of 19 do; none skipped as equivalent.
- **Insertion**: 12 constraints the source does **not** make (`additionalProperties: false` at both levels, a required `keyid`, `minLength: 1` on keyid, sig, payload, payloadType, `minItems: 1`, three narrower base64 patterns) are added in turn; each must make some accept case fail. 12 of 12 do.
- The checker also fails if a keyword in the schema is exercised by no case, or a definition lacks an accept or a reject case.

## Checks

A second, real validator (pass 2): python-jsonschema 4.23.0, Draft 2020-12, installed into a scratch directory and not part of the toolchain, checks the schema itself and runs the 61 cases. 54 agree; the 7 that differ (ENV-R15, ENV-R16, ENV-R17, ENV-R26, B64-R01, B64-R02, B64-R05) are exactly the rejects that rest on the content check, since a standard validator only annotates `contentEncoding`. A pattern ending in `$` had made it 53: Python's `$` matches before a trailing newline, so ENV-R24 passed; the pattern now ends in an end-of-input lookahead, which ECMA-262 and Python read alike.

```sh
python3 -I -B distilled/schema/check-envelope.derived.py
python3 -I -B distilled/schema/check-pae.derived.py
python3 -I -B distilled/examples/reproduce.py     # also re-extracts fixtures; needs .cache/secure-systems-lab-dsse.tar.gz
```
