---
record: sigstore-bundle-0-3
kind: schema
title: "sigstore-bundle-0-3 — schemas"
extracted: "2026-11-20"
reviewed_by: ""
---

# sigstore-bundle-0-3 — schemas

**The source ships a schema, in Protobuf.** The four `*.verbatim.proto` files are the
source's own bytes. Everything else here is the library's and carries `.derived.`;
do not cite a `.derived.` file as the Sigstore project's.

| file | kind | what it is |
|---|---|---|
| `sigstore_bundle.verbatim.proto` | verbatim | `.cache/sigstore-bundle-0-3.bin`, byte for byte (sha256 `bf8d01cc...`) |
| `envelope.verbatim.proto`, `sigstore_common.verbatim.proto`, `sigstore_rekor.verbatim.proto` | verbatim | the three imports, from `.cache/sigstore-bundle-0-3.include/`. No header was added; `bin/validate` reads the first 12 lines (a licence header) and finds no marker word |
| `protoc-descriptor.derived.json` | derived | what protoc reports: 4 files, 23 messages, 53 fields (25 with `field_behavior` REQUIRED), 3 enums; json_name, numbers, oneofs, reserved ranges, declaration lines |
| `check-protoc.derived.py` | derived | compiles the four files with protoc and compares the dump with the committed one |
| `bundle.derived.schema.json` | derived | JSON Schema 2020-12, `$id` `urn:library:sigstore-bundle-0-3:bundle.derived`: the proto3 canonical JSON of a v0.3 Bundle |
| `build-schema.derived.py` | derived | writes the schema and `../examples/cases.derived.json` from the descriptor and `requirements.yaml` |
| `check-schemas.derived.py` | derived | stdlib validator, the cases, the mutation run, optional cross-runs |
| `build-messages.derived.py`, `_ids.derived.py` | derived | write `../messages.yaml`; resolve requirement ids from selectors (raise on 0 or more than 1 match) |

## protoc

Compiled with libprotoc 35.1 (grpcio-tools 1.85.3, a scratch venv). The only file not
in the source is `google/api/field_behavior.proto`, fetched from `googleapis/googleapis`
at commit `a6f4580d494b12461aa1b9190cac8eefe8a3fd22` (the newest commit touching that path
on 2026-11-20), sha256 `e2a1ac88c49909d4579bacbb18519085e82da32c2c7bb15c31037f3be19f667f`.
Only the number of the extension (1052) and `REQUIRED = 2` are used. The compile succeeds (protoc exit 0). 25 REQUIRED annotations plus the four `REQUIRED` words in
the DSSE envelope's comments (R-0028, R-0029, R-0030's `REQUIRED (length >= 1)` and R-0031) are the 29 of `bin/bcp14-count`.

```sh
python3 -m venv V && V/bin/pip install grpcio-tools
V/bin/python -I schema/check-protoc.derived.py --googleapis DIR [--write]   # DIR/google/api/field_behavior.proto
```

## The derived schema

Names. Each of the 24 fields whose json_name differs from its field name is spelled twice: the
lowerCamelCase json_name (what the §5 examples use) and the original field name; the other 16 fields of the
schema's messages have one name for both (`payload`, `payloadType`, `signatures`, `sig`, `keyid`, `algorithm`,
`digest`, `signature`, `hint`, `certificates`, `kind`, `version`, `envelope`, `hashes`, `checkpoint`,
`certificate`; counted from the descriptor). Proto3 JSON parsers accept both; that is **not** in the
pinned source, it is the protobuf JSON mapping (an external basis, marked `proto3-json` on
the cases), and python protobuf accepts both (cross-run). Both spellings of one field at
once are rejected, as is a oneof member spelled twice.

Types. bytes: standard **or** URL-safe base64 (not mixed), padding optional but exact.
int64: a decimal **string** in the int64 range (a regex built by script; no leading zero,
no `-0`). Enums: names. The examples print standard-alphabet base64; the values with no `=` (3 in the first bundle, 2 in the second) are exactly those whose byte length is a multiple of 3, which needs no padding (measured in `../examples/*.expected.derived.json`, `base64_fields`).

Oneofs: `VerificationMaterial.content` (publicKey | x509CertificateChain | certificate) and
`Bundle.content` (messageSignature | dsseEnvelope) are exactly-one, which is also what
REQUIRED on each member means.

Required members. The 25 `field_behavior` REQUIRED fields, plus: `mediaType` (R-0001, MUST be versioned
by populating it), `X509CertificateChain.certificates` with at least one item (the oneof comment's "one or more", in R-0005),
and the DSSE members whose REQUIRED is a comment, `payload`, `payloadType`, `signatures`, `sig` (R-0028 to R-0031).
Each constraint carries its id in `x-constrained-by`.

Media types. `Bundle` accepts all four strings (the v0.3 form and the three legacy
`+json;version=` forms): the proto says clients must be able to accept them. `BundleV03`
accepts only `application/vnd.dev.sigstore.bundle.v0.3+json` (R-0021, MUST). The two example
bundles are checked against both. Version 0.3 therefore has two spellings (SD-S-8, unified as SD-3 in `../normative.md`).

DSSE. `Bundle.dsseEnvelope` has exactly one signature (R-0025, R-0026); the generic
`Envelope` has at least one (R-0030). `payloadType` is any string, because the proto says
a DSSE envelope can carry arbitrary payloads (SD-S-7, unified as SD-11); `DsseEnvelopeInToto` pins the docs
page's `application/vnd.in-toto+json` and is not reached from `Bundle`.

Closed: unknown members are rejected. The source is silent on unknown members (it reserves
numbers 5 to 50 on Bundle), so this is a derived choice, pinned among the 24 `source-silent` cases;
a v0.4 bundle with new members would be rejected.

### REQUIRED at the default value: both readings

proto3 JSON emitters omit a member whose value is the proto default (`0`, empty bytes,
empty array) unless told to print defaults. REQUIRED then means one of:

- **Reading A, presence (enforced here):** the member must be in the JSON. A canonical emitter that omits
  `inclusionProof.logIndex` `"0"` or an empty `hashes` produces a document this schema rejects (case
  A-242 for `logIndex`). Why: it is what the source's words say ("REQUIRED"), it is what the
  §5.1.3.2 example prints (`"logIndex": "0"`, `"hashes": []`, tree size 1), it is checkable
  by a schema, and a verifier cannot tell a missing member from a default after parsing,
  so a document that always prints them is the safe thing to emit. Python protobuf accepts
  the omission (cross-run).
- **Reading B, non-default value:** a REQUIRED scalar must also be non-zero or non-empty.
  Rejected here: logIndex 0 is legitimate (the example), and an empty `hashes` is what a
  one-leaf tree needs.

The source states neither (SD-8 in `../normative.md`; `messages.yaml` source_silences). Cases pin A. A reader
that wants B-tolerant input should relax `required` for default-able members.

### What the schema cannot encode (listed in its `x-not-encodable`)

The v0.3 keyless rule (R-0014: a v0.3 bundle used with the Public Good Instance for keyless
signing must use the single-certificate form) needs to know who issued the certificate, so it
is **not** encoded; likewise signature-time-in-validity (R-0022), the key-hint equality
between `publicKey.hint` and the DSSE `keyid` (R-0004, R-0022), `canonicalizedBody` matching
the content signature (R-0067), certificate order and no root (R-0005 to R-0007), and the RFC 3161
imprint (R-0003). `../examples/reproduce.py` checks the last three on the two example bundles.
Not modelled either: parser leniencies (null, int64 as a JSON number, an enum as an integer)
and the messages not reachable from a Bundle (PublicKey, TimeRange, ObjectIdentifier*,
DistinguishedName, SubjectAlternativeName): `messages.yaml` covers them.

## Cases and the mutation run

`../examples/cases.derived.json`: **251 cases, 66 accept, 185 reject**, each with a reason, a basis
(`source` 78, `proto3-json` 149, `source-silent` 24) and, where a requirement says it, cites
resolved by script (a REQUIRED field's id is found by its declaration's line in the rendering;
`int64 log_index = 1` occurs twice). Every reject, 185 of 185, names the error it must produce
(`error_contains`), so a reject for the wrong reason fails. Cases edit one of three base
instances (the two §5.1.3 bundles and a minimal publicKey bundle) by JSON-pointer ops.

Instances the schema must reject and does (hazards.md section 7), among others: a field of
the wrong JSON type, each required member removed, both members of a oneof, none of them, a member spelled
both ways, zero or two DSSE signatures, an empty chain, mixed-alphabet base64, a space or trailing newline in
base64, wrong padding, int64 at max+1 and min-1, `-0`, leading zeros, `+1`, `1e3`, `0x10`, JSON number and null int64,
an enum number, a legacy media type under `BundleV03`, an unknown version, an unknown member in every message.
No wildcard or open member exists in the schema: `additionalProperties` is false on every definition that declares
`properties`, and the three `allOf` fragments that narrow a closed definition (`BundleV03`, `BundleDsseEnvelope`,
`DsseEnvelopeInToto`) add no member to it, so nothing can swallow a constraint.

**Mutation.** 337 mutants (each `type`, `pattern`, `const`, `minItems`, `maxItems`, `additionalProperties`,
`items`, `not`, `$ref`; each `required` name, `enum` value, `oneOf`/`anyOf`/`allOf` branch; each property
schema relaxed to `{}`): **324 killed, 13 survive, 13 explained, 0 unexplained**. A kill is a flipped accept/reject
verdict. The 13 survivors are all `drop type` on a definition and are equivalent mutants by two named rules,
which the checker classifies by shape and prints: (1) an enum or const whose values are all strings implies the type
(3: HashAlgorithm, MediaTypeV03, MediaTypeAccepted); (2) in a definition whose `allOf` holds an exactly-one `oneOf` over
`required` branches or a `not` over a `required` pair, a non-object already fails, because `required` holds vacuously for
non-objects and so every branch matches / the `not` fails (10: Bundle, InclusionPromise, InclusionProof,
LogId, MessageSignature, RFC3161SignedTimestamp, TimestampVerificationData, TransparencyLogEntry, VerificationMaterial,
X509Certificate). Deleting `type` there does not bind anything the instance did not already meet.

## Cross-runs (scratch venv; not part of the library's toolchain)

```sh
V/bin/python -I schema/check-schemas.derived.py --cross     # PB_GEN=DIR for the protobuf run (below); exits 1 on the 2 known jsonschema disagreements
```

- **python-jsonschema 4.26.0** (Draft 2020-12): agrees with the stdlib validator on 249 of 251 cases. The two
  that differ are the trailing-newline cases (A-222 base64, A-239 int64): python's `$` matches before a final
  newline, so jsonschema **accepts** `"AAAA\n"` where ECMA-262 anchoring (what the checker implements, and what
  JSON Schema specifies for `pattern`) rejects it. Reproduce with the cases named.
- **python-protobuf 7.36.2** (`json_format.Parse` on a Bundle compiled from the same four files with the field_behavior import
  and annotations stripped in a scratch copy; they change nothing for parsing): over the 246 Bundle-level cases there are
  **89 where the schema rejects and protobuf accepts and 0 the other way**. The 89 are, by kind: REQUIRED and oneof
  presence (protobuf does not enforce field_behavior, and an empty `{}`, even `[]`, parses); both spellings
  of a field at once; the media-type rules (protobuf stores any string); one-signature and empty-chain rules;
  malformed base64 (mixed alphabets, spaces, bad padding: python's decoder is lenient); int64 forms (`-0`, `007`,
  `+1`, `1e3`), a JSON number or null; an enum as an integer. Unknown members are rejected by both. Of the 73
Bundle-level rejects for a wrong JSON type, protobuf rejects 60; the other 13 are proto3 JSON's own alternatives
(a JSON number or null for an int64, a number for an enum) and a top-level `[]`, which it parses as an empty Bundle.
  So the schema is a **stricter** reading of the mapping than the reference parser; a bundle the schema rejects is not
  necessarily one a Sigstore client cannot read.

## Checks

```sh
python3 -I distilled/schema/build-schema.derived.py        # schema and cases equal the builders' output
python3 -I distilled/schema/check-schemas.derived.py       # cases + mutation
python3 -I distilled/examples/reproduce.py                 # also needs .cache; runs the above
```
