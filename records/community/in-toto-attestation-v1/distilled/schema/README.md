---
record: in-toto-attestation-v1
kind: schema
title: "in-toto-attestation-v1 — schemas"
extracted: "2026-11-09"
reviewed_by: ""
---

# Schemas

**The source ships no JSON Schema.** It prints templates (JSON blocks with
`<PLACEHOLDER>` values and `...`) and prose. The reference repository also has
`protos/in_toto_attestation/v1/*.proto`, whose own comment says "Validation of
all fields is left to the users of this proto." So there are two kinds of file
here, and the name says which:

- **verbatim** — `*.verbatim.*` and `*.schema-block.verbatim.jsonc`: the
  source's bytes, with a header giving the locator and a sha256 of the body.
- **derived** — `*.derived.*`: the library's rendering of the prose. Every
  derived JSON Schema carries `$id: urn:library:in-toto-attestation-v1:<name>.derived`
  and says `DERIVED - not verbatim` in its description.

Rendering = `.cache/in-toto-attestation-v1.txt`, made by `../render-source.py`.
Archive = in-toto/attestation @ df02077bf97218a8860a5c534eff1f1381f56984.

## Verbatim (6 files + an index)

| file | source | locator |
|---|---|---|
| `statement.schema-block.verbatim.jsonc` | statement.md §3.1 | rendering 164-175 |
| `resource-descriptor.schema-block.verbatim.jsonc` | resource_descriptor.md §4.1 | rendering 241-253 |
| `digest-set.schema-block.verbatim.jsonc` | digest_set.md §5.1 | rendering 421-425 |
| `predicate.schema-block.verbatim.jsonc` | predicate.md §7.1 | rendering 713-716 |
| `statement.verbatim.proto` | archive `protos/in_toto_attestation/v1/statement.proto` | whole file, sha256 8d508fd0… |
| `resource-descriptor.verbatim.proto` | archive `protos/in_toto_attestation/v1/resource_descriptor.proto` | whole file, sha256 246a5cf0… |

No schema block exists in `envelope.md` or `bundle.md`: their "Schema" text is
prose (envelope §8.1 names DSSE v1.0, which is not in the source; the bundle
has only a JSON-Lines description and examples). Those two are derived only.
`verbatim-sources.derived.json` indexes the six files (md file sha256, line
ranges, body sha256); `../examples/reproduce.py` re-cuts each from the
rendering and, with `--archive DIR`, from the Markdown and `.proto` bytes.

The jsonc blocks are templates, not valid JSON (`...`, `<ALGORITHM_1>`, `//`
comments), so they are kept as `.jsonc` and never fed to a JSON parser.

## Derived JSON Schemas (7)

| file | covers | basis in the source |
|---|---|---|
| `statement.derived.schema.json` | Statement | statement.md §3.2 (rendering 180-221) |
| `resource-descriptor.derived.schema.json` | ResourceDescriptor | resource_descriptor.md §4.2 (256-329) |
| `digest-set.derived.schema.json` | DigestSet | digest_set.md §5.2 (428-565) |
| `digest-set-lengths.derived.schema.json` | DigestSet + output length per fixed-size algorithm | **not in the source**: lengths come from the algorithm definitions (the Go and Rust bindings check 12 of the 14, not ripemd160 or sm3) |
| `envelope.derived.schema.json` | Envelope, DSSE as used | envelope.md §8.1-8.2 (748-798), validation.md (1137-1141) for `keyid`/`sig` |
| `bundle-line.derived.schema.json` | one Bundle line = a recognized Envelope | bundle.md §9.1 (876-885) |
| `field-types.derived.schema.json` | `$defs` ResourceURI, TypeURI, Timestamp | field_types.md §6 (637-690) |

Choices a reader would otherwise have to guess (each is argued in the schema's
`description` or in `gen-schemas.derived.py`):

- `additionalProperties: true` on every object but one: v1 README §2.2
  "Consumers MUST ignore unrecognized fields". A Statement is valid with extra
  members. The exception is DigestSet, whose extra keys are custom algorithms:
  `additionalProperties: {"type": "string"}`, so any key is allowed and its
  value must be a string (R-0157, R-0207). (Pass 2: this line said "everywhere".)
- **Statement.subject[]** requires `digest` (R-0090); `predicate` is optional
  and `{}` is valid ("Unset is treated the same as set-but-empty").
- **ResourceDescriptor** needs at least one of `uri`, `digest`, `content`
  (`anyOf`) — not `name`.
- **DigestSet** keys: the 19 algorithms of §5.2.1.1, spelled as its heading
  spells them (R-0205; the stated NIST-name rule gives only 6 of the 19,
  normative SD-25), take lowercase hex of even length (two digits per byte);
  the four `git*` take 40 or 64 lowercase hex; `dirHash` takes 64; any other key
  is a custom algorithm and takes any string. `dirHash1` (the source's own example
  key) is therefore a custom key, which is a source defect, not a feature.
- **TypeURI/ResourceURI**: has a scheme; scheme lowercase; authority (if `//`
  follows) has no uppercase. Percent-triplet case is not enforced: the source's
  "meaning" clause names only scheme and authority.
- **Envelope.payloadType** accepts `application/vnd.in-toto+json` and
  `application/vnd.in-toto.<predicate>+json`. It rejects
  `application/vnd.in-toto.<predicate>+dsse` (a storage media type, §8.4).
  The general MUST at §8.2 (`application/vnd.in-toto+<encoding>`) is **not**
  encoded: it contradicts the DSSE-specific bullet the source gives next, and
  the schema follows the DSSE bullet (see messages.yaml SD-04).
- **base64** (`content`, `payload`, `sig`): the source never names the
  alphabet or padding; the pattern accepts the standard or the URL-safe
  alphabet (one per value), padding optional but correct where present, and
  rejects a length no byte string encodes to (`A`, `AAAAA`, `AA=`).
- The Bundle-line schema deliberately does **not** fix `payloadType`: a line
  that fails it is an *unrecognized line*, to be ignored, never an error
  (R-0075).

## `check-schemas.derived.py` — does it bind?

A schema that parses is not a schema that binds (hazards §7), so the checker
holds the instances each schema MUST reject as well as MUST accept, and
mutation-tests that the reject cases are doing the work.

```
python3 -I check-schemas.derived.py              # every case, exit 1 on a failure
python3 -I check-schemas.derived.py --mutate     # + mutation test
python3 -I check-schemas.derived.py --basis ../requirements.yaml   # + cited R-ids exist and contain the cited words
python3 -I check-schemas.derived.py --list       # print every case
```

The validator inside is a deliberately small JSON Schema 2020-12 subset that
**raises on any keyword it does not implement**, so nothing is silently
ignored. It reports how many cases it examined.

Measured on this tree (2026-11-09):

| | must accept | must reject |
|---|---|---|
| statement | 86 | 317 |
| resource-descriptor | 77 | 308 |
| digest-set | 43 | 230 |
| digest-set-lengths | 37 | 172 |
| envelope | 8 | 29 |
| bundle-line | 4 | 14 |
| field-types | 19 | 50 |
| **total** | **274** | **1120** |

1403 cases examined (those 1394, plus 5 deep cases — a Statement inside an
Envelope payload — and 4 whole Bundle files). 641 requirement citations in
the cases were checked against `requirements.yaml` (218 entries); each cites
the statement its verdict rests on (pass 2 replaced 584 citations made against
the skeleton's 87, among them `R-0029` for every DigestSet case and four split
parents).

**Mutation test:** 846 mutants of the seven schemas (drop a `required`, a
`pattern`, an `anyOf` branch, a property, a `const`, a `type`; relax a pattern
to any-case hex, to a variable length, to hex of any length, to base64 of any
length with mixed alphabets, to drop an anchor, to allow an uppercase
authority, month 13, hour 24, any zone; make `additionalProperties` true). 841
killed by at least one case, 5 equivalent and reasoned (they drop the
ResourceDescriptor `anyOf` under `statement`, where `subject[]` already requires
`digest`; no instance can tell them apart), **0 survived**. One reject case per
rule is therefore load-bearing; there is no wildcard that swallows a rule.

## `refimpl-compare.derived.py` — the schemas against the reference code

Read, not run: `go/v1/statement.go`, `go/v1/resource_descriptor.go`,
`python/in_toto_attestation/v1/statement.py`, `resource_descriptor.py`
(archive @ df02077). The script is a hand port of their `Validate`/`validate`
rules, run over the 1061 schema cases that have an analogue, to list where the
verdicts differ. The port is the library's reading and has not been executed
against the bindings; two assumed behaviours (protobuf JSON parsing rejects an
unknown member by default) are marked in its docstring, with a third unverified
modelling choice (bytes content decoded strictly for both; Python's
`json_format` decodes it leniently). Pass 2 fixed one port bug: Go's hex check
was modelled with `bytes.fromhex`, which skips whitespace, so 51 verdicts (a
digest value with a trailing newline, 17 algorithms, direct and lifted) had Go
accepting what `hex.DecodeString` rejects.

The Rust binding (`rust/src/lib.rs`, `hash_algorithm.rs`) was read by pass 2 for
this note only and is not ported: it has the same name/uri/digest minimum, the
same 17-name length table (20 bytes for every `git*` key), requires a non-empty
subject and accepts only `Statement/v1`, and does not check `predicate` (its
comment: an unset predicate is set-but-empty).

Disagreements between the spec as written (our schemas) and the bindings:

1. **ResourceDescriptor minimum.** Spec §4.2: one of `uri`, `digest`,
   `content` (R-0013). Go and Python: one of `name`, `uri`, `digest`. So
   `{"name": "only"}` passes the code and fails the spec, and `{"content":
   "Ynl0ZXNjb250ZW50"}` (valid per spec) is rejected by the code.
2. **Statement.predicate.** Spec §3.2: optional, and unset is treated the same
   as set-but-empty (R-0012, R-0142). Go rejects a nil predicate
   (`ErrPredicateRequired`) and accepts an empty one, since protobuf JSON
   parsing yields a non-nil empty Struct for `{}`; Python rejects an unset *or
   empty* one (`len(predicate) == 0`). A Statement with no predicate is valid
   per spec and rejected by both; `"predicate": {}` is rejected by Python only.
   (Pass 2: this item said `{}` was rejected by both, which the port's own
   output contradicts.)
3. **Statement._type.** Spec: exactly `https://in-toto.io/Statement/v1`. Go also
   accepts `https://in-toto.io/Statement/v0.1` (`statementTypeUriLegacy`).
4. **Subject count.** Go and Python require at least one subject; no sentence in
   the source says so.
5. **Digest value check.** Spec: lowercase hex (R-0158, R-0159; §5.2, §5.2.1.1). Go checks hex
   decoding (`hex.DecodeString`, which also accepts upper case) and an exact
   byte length for 17 names: md5, sha1, sha224, sha256, sha384, sha512,
   sha512_224, sha512_256, sha3_224/256/384/512, gitBlob/Commit/Tag/Tree and
   dirHash. It does **not** look at shake128, shake256, blake2b, blake2s,
   ripemd160, sm3 or gost, which the spec lists. Python checks no digest.
6. **git* digests.** Spec §5.2.1.3: SHA-1 (40 hex) **or** SHA-256 (64 hex). Go
   fixes 20 bytes, so a SHA-256 git object id is rejected.
7. **Unknown members.** Spec: ignore them. protobuf's JSON parsers reject them
   unless told to ignore (assumed, not run), so 4 instances the spec accepts
   are rejected by the strict parse, in Go and in Python alike.
8. **Nothing in either binding checks** TypeURI or ResourceURI lowercase,
   `mediaType`, `content` size (<1KB) or `name`/`uri` uniqueness within
   `subject`. The archive has no Envelope or Bundle code at all (the Java tree
   is generated protobuf; the Go and Python `validate` functions cover only
   Statement and ResourceDescriptor).

Counts, hand port, 1061 cases: Go agrees with the schema on 760 and Python on
444 with unknown members tolerated (756 and 440 when they are rejected, as
protobuf's default parse does). The large "schema rejects, code accepts" numbers
(Go 64+108+103, Python 175+220+216 over digest-set, resource-descriptor and
statement) are the bindings checking less than the schema, as points 5 and 8
say (the port was not run; the classes, not the counts, are the finding).

## Regenerating

`gen-schemas.derived.py [outdir]` writes the seven schemas (one file, so the
shared `$defs` are written once; `$ref` across files would need a resolver the
checker does not have). The `.derived.schema.json` files are generated; fix
the generator, not the JSON.
