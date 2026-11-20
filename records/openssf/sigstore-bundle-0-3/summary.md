---
schema: "library-summary/v1"
id: sigstore-bundle-0-3
record: sigstore-bundle-0-3
type: summary
updated: "2026-11-20"
---

# Sigstore Bundle format v0.3

|  |  |
|---|---|
| **Type** | spec: a protobuf schema whose comments carry the normative text (`protos/sigstore_bundle.proto`), the three Sigstore files it imports, and the project's prose page on the format |
| **Maturity** | _unset._ A versioned project specification with no ratification step that maps to RFC 2026 |
| **Authors** | No byline. "The Sigstore Authors" (licence header); sigstore/protobuf-specs maintainers |
| **Published** | 2025-01-15 (last commit touching `sigstore_bundle.proto`, `134d573`); pinned at release tag `v0.5.2` (`0342fe5`, 2026-08-21). Bundle media type version 0.3; the docs page says "Version 0.3.2", last updated 2025-01-14 |
| **Identifier** | media type `application/vnd.dev.sigstore.bundle.v0.3+json`; protobuf package `dev.sigstore.bundle.v1` |
| **Source** | https://raw.githubusercontent.com/sigstore/protobuf-specs/0342fe5797edd558c58098033220fb27a2542a28/protos/sigstore_bundle.proto |
| **Digest** | `sha256:bf8d01cc…` (full value in `record.yaml`), fetched 2026-11-20; the four spliced files are pinned by digest in `content.note` |

## Overview

A Sigstore bundle is the unit a Sigstore verifier is handed: **one** signature
over an artifact plus everything needed to check it offline except the trust
root. The `Bundle` message (§1.3 of our rendering) is a media type, a
`VerificationMaterial`, and a `content` that is exactly one of a bare
`MessageSignature` over an artifact digest or a DSSE envelope, which in a
bundle must hold exactly one signature. `VerificationMaterial` (§1.2) carries
the key as one of three forms — a public-key hint, an X.509 chain, or (new in
0.3, and required for public-instance keyless signing) a single leaf
certificate — plus zero or more Rekor transparency-log entries (inclusion
proof with checkpoint, and optionally a signed entry timestamp) and zero or
more RFC 3161 timestamps. The versioning note (§1) and the media-type comment
(§1.3) give the version history: 0.1, 0.2 and 0.3 media types, in two
spellings. The point of the design is that a short-lived Fulcio certificate is
verifiable after it expires, because the log or a TSA proves *when* the
signature was made.

The docs page (§5) restates the structure for humans and prints two real
bundles — a `hashedrekord` message signature from Maven Central and a DSSE
SLSA-provenance bundle from the Sigstore conformance suite — which are the
record's test vectors.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Fixes what a verifier must check — chain to an independently trusted CA, signing time inside certificate validity, the log's promise or proof, the single DSSE signature (§1.2, §1.3, §4.5) |
| Cryptography | `adjacent` | No primitive of its own; algorithms are named in `sigstore_common.proto` (§3.2) and, for a key hint, must come out of band (§3.4) |
| This project | `core` | The container real SLSA provenance arrives in, including mofn's wallet releases |

- **R-I-02, R-I-03.** An import or export at the in-toto/DSSE boundary meets
  this format first: the DSSE envelope sits inside a bundle, with the
  verification material beside it rather than inside it.
- **R-O-05.** DSSE signs the payload bytes verbatim under PAE (§2.1); the
  bundle adds no canonicalization of its own. The log entry's
  `canonicalized_body` (§4.5) is a different object — the log's record of the
  entry — and is where a byte-faithfulness question lives.
- **DEC-005.** A bundle permits only one DSSE signature (§1.3; docs §5.1.2.2),
  so a bundle is not an ITE-5-compliant multi-signature envelope — the point
  `in-toto-envelope-v1` records from the other side.
- **T-052 context** (byte-faithful round trip of a real release's provenance):
  the provenance is the base64 `payload` of the bundle's DSSE envelope; keeping
  it byte-faithful means keeping that envelope, not re-serializing the bundle's
  JSON.

## Implementations

**Searched 2026-11-20** (GitHub API for licence and language).

| Name | Kind | License | URL |
|---|---|---|---|
| protobuf-specs generated bindings | open source, several languages | Apache-2.0 | https://github.com/sigstore/protobuf-specs |
| sigstore-go | open source, Go | Apache-2.0 | https://github.com/sigstore/sigstore-go |
| sigstore-python | open source, Python | API reports NOASSERTION | https://github.com/sigstore/sigstore-python |
| sigstore-js | open source, TypeScript | Apache-2.0 | https://github.com/sigstore/sigstore-js |
| sigstore-java | open source, Java | Apache-2.0 | https://github.com/sigstore/sigstore-java |
| sigstore-rs | open source, Rust | Apache-2.0 | https://github.com/sigstore/sigstore-rs |
| cosign | open source, Go | Apache-2.0 | https://github.com/sigstore/cosign |
| sigstore-conformance | open source, Python | none reported by the API | https://github.com/sigstore/sigstore-conformance |
| actions/attest-build-provenance | open source, Action | MIT | https://github.com/actions/attest-build-provenance |
| GitHub artifact attestations | commercial service | — | https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, the five pinned inputs (`content.note`), relations, `bears_on`, the FX-1 `distillation` block |
| `summary.md` | this document |
| `distilled/` | the FX-1 artifact set; `distilled/README.md` lists every file and its coverage |
| `distilled/render-source.py` | builds `.cache/sigstore-bundle-0-3.txt`, the one text every locator and quotation refers to: §1 `sigstore_bundle.proto`, §2 `envelope.proto`, §3 `sigstore_common.proto`, §4 `sigstore_rekor.proto`, §5 the docs page |

**Absences.** No source bytes are committed (`.cache/` is gitignored).
`protos/sigstore_bundle_v2.proto`, a draft on main since 2026-10-26 and marked
unstable on 2026-11-18, is not this record; if it stabilises it is a new
record linked by `supersedes`. The trusted-root and verification-options
protos (`sigstore_trustroot.proto`, `sigstore_verification.proto`) are not
imported by the bundle and are not read here, though a verifier needs the
trust root they describe. The Sigstore client specification the bundle defers
to for time-of-signing checks is a Google Doc, cited, not held.

## Limits

- **The normative text is protobuf comments.** Binding force rests on comment
  prose and `field_behavior` annotations; nothing says which wins when they
  disagree, and the JSON encoding is whatever the protobuf JSON mapping
  produces.
- **The verification algorithm is elsewhere.** "Verify that the signature was
  computed at the time the certificate was valid" points at the client spec
  (§1.3), which is not part of this source.
- **The docs page and the proto disagree in places** — the page is a
  restatement with lowercase "must"s and its own version number, and it is
  silent on rules the proto states (chain contents, the v0.1 promise). The
  extraction treats the proto as authoritative and records each divergence.
- **Single signature, single key.** By design; a bundle cannot carry a
  classical and a post-quantum signature side by side.
