---
schema: "library-summary/v1"
id: rfc-8949
record: rfc-8949
type: summary
updated: "2026-09-22"
---

# Concise Binary Object Representation (CBOR)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Internet Standard, **STD 94** |
| **Authors** | C. Bormann, P. Hoffman |
| **Published** | December 2020 |
| **Identifier** | RFC 8949 · DOI 10.17487/RFC8949 · STD 94 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8949.txt |
| **Digest** | `f1164a5b31a3…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

CBOR defines a binary serialisation whose data model is deliberately close to
JSON's — maps, arrays, text and byte strings, numbers, simple values — but
encoded in a self-describing binary form built on a 3-bit major type plus an
argument. Its argument is that a format can be small on the wire, cheap to
encode and decode on a constrained device, and extensible *without* requiring
a schema to be present at decode time. Extensibility is delegated to a tag
mechanism whose code points are allocated by IANA, which is the design choice
with the most consequence for this project. §4.2 additionally defines
**deterministic encoding** — the property that semantically equivalent data
items produce identical bytes — but defines it as an option a protocol must
select and further constrain, not as a property of CBOR itself. RFC 8949
obsoletes RFC 7049 and is STD 94.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | §4.2 determinism is the precondition for signing a structured object at all; §7 enumerates the decoder resource-exhaustion classes that produced real CVEs in shipped libraries. |
| Cryptography | adjacent | Defines no primitives. It is the substrate COSE (RFC 9052) signs over. |
| This project | core | Named directly in **DEC-002** option 2 ("CBOR + CDDL as canonical; COSE for signed form"), and the 2026-09-22 direction records "start with a reduced CBOR profile". |

Bears on **DEC-002** (concrete native encoding) and **R-M-12** (native
extension points must be key-relative, not registry-dependent). The R-M-12
tension is native to this document: CBOR's own extension point is the IANA tag
registry (`iana-cbor-tags`), so adopting CBOR's tags wholesale would make the
native model registry-dependent in exactly the way ADR-0001 rejects. Note this
is a constraint on the *profile*, not an argument against the encoding — the
data model can be used with tags excluded, which is what "reduced CBOR
profile" means.

## Implementations

Surveyed 2026-09-22. Full list with licences and per-project notes is in
`record.yaml` under `implementations`. The load-bearing findings:

| Name | Kind | License | URL |
|---|---|---|---|
| fxamacker/cbor (Go) | open source | MIT | https://github.com/fxamacker/cbor |
| agronholm/cbor2 (Python) | open source | MIT | https://github.com/agronholm/cbor2 |
| ciborium (Rust) | open source | Apache-2.0 | https://crates.io/crates/ciborium |
| QCBOR (C, constrained) | open source | permissive | https://github.com/laurencelundblade/QCBOR |
| zcbor (CDDL→C codegen) | open source | Apache-2.0 | https://github.com/NordicSemiconductor/zcbor |

Three points a build-on-it decision turns on:

- **Deterministic encoding is not a default.** QCBOR v1.x does not sort map
  keys on encode; kotlinx-serialization-cbor defaults to indefinite-length
  encoding. A library being "RFC 8949 compliant" says nothing about whether it
  can produce the §4.2 form you need to sign.
- **Rust's former default, `serde_cbor`, is deprecated and unpatched**
  (RUSTSEC-2021-0127); `ciborium` and `minicbor` are the advisory's own
  recommended replacements.
- **CDDL tooling is the ecosystem's weakest link.** `zcbor` is the most
  production-grade CDDL consumer found and it targets embedded C only; the
  most-used Rust CDDL validator self-describes as a personal learning
  exercise. WP1 ("CDDL for logical types") should not assume mature tooling.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, typed relations, and the 2026-09-22 implementations survey |
| `summary.md` | this document |

No `distilled/` artifacts yet. If DEC-002 selects CBOR, this record is the
first candidate for `distilled/normative.md` — §3 (major types), §4.2
(determinism) and Appendix F (non-well-formedness) are the sections a
conforming implementation is mined from.

## Limits

- **It does not settle determinism.** §4.2 offers *two* orderings — core
  bytewise-lexicographic (§4.2.1) and length-first (§4.2.3) — and leaves tag
  presence, NaN payloads and float shortening to the protocol. Four mutually
  incompatible profiles have grown in that gap (see the CBOR research report):
  RFC 8949 §4.2.1, CTAP2 canonical, DAG-CBOR, and dCBOR. "Deterministic CBOR"
  is not one thing, and a spec that says only "use deterministic CBOR" has not
  specified an encoding.
- **It does not settle extension governance.** Tag allocation is IANA's, which
  is the whole of the R-M-12 problem.
- **It does not define a schema language.** That is RFC 8610 (CDDL), a separate
  record, itself modified by RFC 9682 and extended by RFC 9165 and RFC 9741.
- **Read scope:** this summary was written from §1–§5, §7 and §8 plus the
  verified cross-spec analysis in the research report. Appendix F's
  non-well-formedness taxonomy has *not* been read line by line and is the
  first thing to check before any conformance claim.
