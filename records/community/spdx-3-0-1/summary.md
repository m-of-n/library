---
schema: "library-summary/v1"
id: spdx-3-0-1
record: spdx-3-0-1
type: summary
updated: "2026-11-01"
---

# System Package Data Exchange (SPDX) Specification Version 3.0.1

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — OMG formal/24-11-01 (March 2025), labelled Version 3.0 and self-identifying as 3.0.1 in its body. ISO/IEC DIS 5962 is a separate, unfinished track. See Limits |
| **Authors** | The Linux Foundation and its Contributors |
| **Published** | 2024-12-17 |
| **Identifier** | SPDX 3.0.1 · git tag `3.0.1` · OMG formal/24-11-01 |
| **Source** | https://spdx.github.io/spdx-spec/v3.0.1/ (read as source at the tag; see Limits) |
| **Digest** | `e3c04d121e56bb5355bf666da0d2226365c6d78a6d4421329cdac001915e6e9e` — archive of `spdx/spdx-spec` at the tag's commit. The model is a second repository; its digest is in `content.note` |

## Overview

SPDX 3 rebuilds the format as an RDF data model: everything is an `Element`
with a mandatory `spdxId` and `creationInfo`, relationships are themselves Elements,
and JSON-LD, Turtle, N-Triples and RDF/XML are all serialisations of that one graph
(`serializations.md`). The scope widens with the name, from Software to System
Package Data Exchange, covering build, AI, dataset, security and licensing data
through nine conformance profiles, of which only Core is mandatory
(`conformance.md`). The Core minimum is deliberately low: the required fields "are
rather minimal". Integrity is a per-Element `verifiedUsing` list of hash-like
`IntegrityMethod`s, optional throughout. **There is no signature anywhere in the
specification.** SPDX does not delegate signing to an envelope; it does not mention
signing at all.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Describes composition and vulnerability data; defines no verification beyond hash comparison |
| Cryptography | adjacent | Enumerates hash algorithms and defines no signing, keys or trust |
| This project | adjacent | Prior art for artifact subjects and a canonical serialisation, with no adoption path into the native format |

**R-M-07** (*"Artifact statements SHALL bind at least one content digest."*, ARCH-0001
§5). Not met by the format. `verifiedUsing` on `Element` has no `minCount` and
`contentIdentifier` on `SoftwareArtifact` is `minCount: 0`. Even the Lite annex lists
`verifiedUsing` as recommended, not mandatory. `HashAlgorithm` admits `adler32`, a
checksum, plus `md2`, `md4`, `md5` and `other`, so a value's presence does not make it
a content digest in R-M-07's sense. A profile would have to require one and restrict
the algorithm, the same fix `cyclonedx-1-7` needs.

**R-M-11** (proposed in `ARCH-0001-PROPOSAL-v0.2.0` §7, not in ARCH-0001 v0.1.5). The
closest match among the sbom records to the `digest` and `description` modes.
`ContentIdentifier` carries `gitoid` or `swhid`, intrinsic identifiers of content,
alongside `Hash`. SPDX models the bytes of a serialisation as a separate `Artifact`
linked to the logical `SpdxDocument` by `serializedInArtifact` (`serializations.md`),
which is the logical-versus-physical split `description` mode needs. No equivalent
was found in the parts of ECMA-424 read.

**DEC-002** (mofn native encoding, accepted 2026-10-25, option 5 by `ADR-0004`). A
comparison point only, and a change of meaning for this `bears_on`: the entry was
inherited as *tmodel's* DEC-002, a different decision, and it is kept for a different
reason. `serializations.md` defines a canonical JSON form, which is a real rival data
point for "which bytes do we hash". It is weak by mofn's standard; see Limits.

## Implementations

Searched 2026-11-01. Licences come from the GitHub API, and capability notes from
each project's README. None of these were run. 3.x support is uneven, so the version
column of each tool matters.

| Name | Kind | License | URL |
|---|---|---|---|
| spdx/tools-java | reference tooling; README documents SPDX 2 to 3.0.1 conversion | Apache-2.0 | https://github.com/spdx/tools-java |
| spdx/tools-python | library; README says SPDX 3.0 support is experimental and write-only | Apache-2.0 | https://github.com/spdx/tools-python |
| protobom | format-neutral library; table lists SPDX 3.0.1 JSON-LD | Apache-2.0 | https://github.com/protobom/protobom |
| cdxgen | generator; SPDX 3.0.1 JSON-LD output alongside CycloneDX | Apache-2.0 | https://github.com/cdxgen/cdxgen |
| Syft | generator, SPDX and CycloneDX output; signed attestations via in-toto. SPDX 3 support not checked | Apache-2.0 | https://github.com/anchore/syft |
| sigstore/cosign | external signing: `cosign attest --predicate <file>` wraps a file as an in-toto attestation. Generic, not SPDX-specific | Apache-2.0 | https://github.com/sigstore/cosign |
| Anchore Enterprise | commercial SBOM management, from web search results only | commercial | https://anchore.com/ |
| Sonatype SBOM Manager | commercial SBOM management, from vendor pages in web search only | commercial | https://www.sonatype.com/products/sbom-manager |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

No `distilled/`: this record is at the summary bar. FX-1 extraction of SPDX 3.0.1 is
owned by no issue yet. It would have to span both repositories, since the normative
model is 271 Markdown files outside `spdx/spdx-spec`.

## Limits

**What was read.** Source Markdown at the release tag, not the rendered site, which
was only confirmed live (HTTP 200). From `spdx/spdx-spec` at
`61a649da8ca27924ac1ca8d2a061cb228839b24c`: `scope`, `conformance`, `serializations`,
`front/introduction`, `front/copyright`, `annexes/rdf-model`, `CHANGELOG`, the
headings of `references`, and the Lite annex in part. From `spdx/spdx-3-model` at
`a745f63e8643d5ae0f0851fcfa6836085308f80b`: Core's `Element`, `Artifact`,
`IntegrityMethod`, `Hash`, `PackageVerificationCode`, `ExternalMap`, `Relationship`,
`SpdxDocument`, `CreationInfo`, `Agent`, `Bom`, `Bundle`, `ExternalIdentifier`,
`verifiedUsing`, `HashAlgorithm` and `RelationshipCompleteness`; Software's `Sbom`,
`SoftwareArtifact`, `ContentIdentifier` and its two vocabularies; the Lite and Build
profile pages. **Not read:** most of the 271 model files, including all of Security,
AI, Dataset, and the licensing profiles, and the licence-matching and purl annexes.
Multi-part PDFs were not used.

**"No signature" rests on a search.** A case-insensitive search for sign, signed,
signing, signature, signer, envelope, DSSE, cosign, JWS and Sigstore across the
whole model, its docs, and the spec pages listed above returned only a `falcon-sign`
URL and a "minus sign". The unread annexes were searched too, and hit only
punctuation names such as "at-sign" and the word "designed". The OMG PDF also has no occurrence of "signature".
A reference to SLSA Provenance v0.2 exists in `references`; its use in the model was
not traced.

**The canonical form is underspecified.** `serializations.md` orders pairs "by name"
without a collation, and leaves strings "without specific canonicalisation". Its
escaping sentence says "the two characters" and then lists three things. It cites no
RFC 8785 or RDF dataset canonicalisation, and does not say what the form is for, so
nothing establishes that two implementations produce equal bytes. Since an RDF graph
has many JSON-LD framings, the form's premise, that it is "exactly the same as the
JSON-LD serialization", does not itself fix one. That is a judgement from reading, not
something tested.

**Negative assertion is richer here than in CycloneDX, and still only asserted.**
`Relationship.md` provides `NoneElement` to state that no such relationship exists and
`NoAssertionElement` to decline to state, and `RelationshipCompleteness` adds
`complete`, `incomplete` and `noAssertion`. These let an author say the negative. They
cannot make it true, and with nothing to sign them they carry no key at all.

**Identity of the creator is not a key.** `createdBy` is an `Agent`, an Element with a
name and optional external identifiers. Nothing binds an Agent to a key.

**Standing.** The September note said ratification was still in progress. That was
stale for OMG: `omg.org/spec/SPDX/3.0/PDF` is Formal/24-11-01, released March 2025. It
is labelled Version 3.0, but its text says "SPDX Specification 3.0.1" and references
the 3.0.1 context. Only those markers were compared, not the full text, so whether
the two are identical is unverified; `maturity: standard` rests on this and should
be reviewed. ISO is not done: an Internet Archive capture of 2026-03-23 shows ISO/IEC
DIS 5962 ("SPDX® Specification V3.0") at stage 40.20, replacing the 2021 edition. Its
state after that capture is unknown, because iso.org refuses scripted clients.

**Currency.** `v3.1-RC1` was tagged 2026-01-24 as a pre-release, so 3.0.1 is still the
latest full release. 3.1 was not read and could change the absence of signing.

## Note — RDF/graph-native serialization (tmodel)

SPDX 3.0.1 defines an **RDF/OWL model with a SHACL profile** ([RDF-model annex](https://spdx.github.io/spdx-spec/v3.0.1/annexes/rdf-model/)) — the most graph-native SBOM standard, a first-class fit if tmodel uses a triple store. (Consolidated here from the former `other/spdx-3-rdf`. This bore on tmodel's DEC-002, a different decision from the mofn DEC-002 named under Applicability.) The annex itself is marked Informative. `serializations.md` makes the OWL ontology and its SHACL restrictions part of JSON-LD validation.
