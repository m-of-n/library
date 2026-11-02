---
schema: "library-summary/v1"
id: ipld-dag-cbor
record: ipld-dag-cbor
type: summary
updated: "2026-11-01"
---

# IPLD DAG-CBOR Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `draft` — the document labels itself *Descriptive - Draft*. It carries no version number |
| **Authors** | IPLD specification contributors; none are named in the document |
| **Published** | Undated. Last change to the source file 2026-07-23 (`0f0ea9c`) |
| **Identifier** | https://ipld.io/specs/codecs/dag-cbor/spec/ · ipld/ipld `specs/codecs/dag-cbor/spec.md` @ `0f0ea9c` |
| **Source** | https://raw.githubusercontent.com/ipld/ipld/0f0ea9c9a9b95e2e37168ac9fc887470f7f8ba58/specs/codecs/dag-cbor/spec.md |
| **Digest** | `sha256:82f6b5263e23cd468f3f4e5c00c01731f8d305379db7aadb2afc85a86b01534a` (the pinned Markdown, retrieved 2026-11-01) |

## Overview

DAG-CBOR restricts CBOR so that a value has one encoding, which is what a
content-addressed system needs when the bytes are the name. Compared with RFC
8949 it keeps only tag 42 (a CID link), only string map keys, and only definite
lengths. It applies the §4.2 rules of RFC 8949 to integers, lengths, the tag and
map order, then departs from them on floats: every float is 64-bit, and NaN, the
infinities and -0.0 are excluded (*Strictness*). A block must also decode to
exactly one top-level object with no trailing bytes.

The same document then takes much of that back. *Decode strictness* lets decoders
relax key order, integer and length minimality, tag form and float width by
default, for historical data and non-conforming encoders. So the guarantee is one
about conforming encoders, not about what a decoder accepted.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Non-canonical acceptance decides whether two byte strings can name one value |
| Cryptography | `none` | No primitive. The hash lives in the CID, outside this document |
| This project | `core` | One of the profiles DEC-002 would have to cite or reject |

- **DEC-002** (concrete native encoding). Evidence for how a CBOR profile behaves
  once deployed, and in particular that strict decoding is not the default.
- **R-O-03** (cite the canonicalisation algorithm, do not invent one). Citing
  "RFC 8949 §4.2" would not describe this profile: the float rule differs. A
  profile must be cited by name.

Against `rfc-8949`: this is not a contradiction, so no `contradicts` edge is set.
§4.2.2 of that RFC lists all-64-bit floats as an example rule and disallowing
negative zero as an option, and it leaves those to the application. But such an
encoding is not §4.2.1 core deterministic, because §4.2.1 requires shortest-form
floats. For text-string keys the sort order agrees with §4.2.1.

## Implementations

The spec's own *Implementations* section records caveats per library, and those
caveats are the finding. Searched 2026-11-01; licenses read from GitHub.

| Name | Kind | License | URL |
|---|---|---|---|
| @ipld/dag-cbor | open source | Apache-2.0 | https://github.com/ipld/js-dag-cbor |
| go-ipld-prime | open source | MIT | https://github.com/ipld/go-ipld-prime |
| go-ipld-cbor | open source | MIT | https://github.com/ipfs/go-ipld-cbor |
| cbor-gen | open source | MIT | https://github.com/whyrusleeping/cbor-gen |
| Peergos Java IPLD | open source | AGPL-3.0 | https://github.com/Peergos/Peergos |
| serde_ipld_dagcbor | open source | not detected | https://github.com/ipld/serde_ipld_dagcbor |
| dag-cbor (Python) | open source | MIT | https://github.com/hashberg-io/dag-cbor |

The legacy `ipld-dag-cbor` JS library is archived on GitHub. Commercial: searched,
none found on 2026-11-01. Fixtures are at
https://ipld.io/specs/codecs/dag-cbor/fixtures/.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and typed relations |
| `summary.md` | this document |

No `distilled/`. This PR claims the summary bar. Any FX-1 extraction belongs with
the topic's convergence work, and no issue owns it yet. Verbatim normative text
lives under FX-1, so this summary cites sections only.

## Limits

- **Decoding does not prove canonical form.** By the spec's own caveats,
  `@ipld/dag-cbor` does not enforce map order or float width on decode, and
  `go-ipld-prime`, `go-ipld-cbor`, `cbor-gen` and the Java library do not enforce
  strictness on decode. Two different encodings of a value can both be accepted,
  and they hash differently. A verifier wanting canonical bytes has to re-encode
  and compare, or use a strict mode, which the spec says only *may* be offered.
- **Listed libraries deviate on encode too.** `cbor-gen` sorts map keys with
  `sort.Strings()`, which is not the required length-first order. `go-ipld-cbor`
  and `go-ipld-prime` accept NaN and the infinities, which the spec excludes.
- **Its normative strength is unstable.** The list opens with "must" but the rules
  inherit "should" (a valid encoder "should produce", a decoder "should reject"),
  and the words are not defined by reference to BCP 14. It calls itself
  descriptive, so where code and text differ the document does not say which wins.
- **Coverage of the -0.0 rule is new.** It arrived 2026-07-23 (#380), after
  implementations shipped, and the caveats do not say which ones enforce it.
- **JavaScript cannot carry the data model faithfully.** Whole-number floats are
  indistinguishable from integers, and values past the safe-integer range need
  BigInt (*Limitations*). A value may not round-trip to the same bytes.
- **The CID is out of scope.** Tag 42 and the multibase prefix are defined here,
  but hash choice and CID validity are not.
- **Digest note.** The earlier digest `4a35ffac…` (2026-10-05) was of the rendered
  page. Today's page hashes differently with identical visible text, so that
  digest changes on site rebuilds. The record now pins the source Markdown; a word
  comparison with the rendered page differed only in markup.
- **Read scope:** the complete spec, the IPLD *About the Specifications* page, and
  RFC 8949 §4.2.1 and §4.2.2. The `cid-cbor` document and the fixtures were not read.
