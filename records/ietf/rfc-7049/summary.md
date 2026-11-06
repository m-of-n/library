---
schema: "library-summary/v1"
id: rfc-7049
record: rfc-7049
type: summary
updated: "2026-11-01"
---

# Concise Binary Object Representation (CBOR)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, **obsoleted by RFC 8949**, confirmed in `rfc7049.json` 2026-11-01 |
| **Authors** | C. Bormann, P. Hoffman |
| **Published** | 2013-10 |
| **Identifier** | RFC 7049 · DOI 10.17487/RFC7049 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7049.txt |
| **Digest** | `sha256:2b65264a…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | 2 verified, 4 held, 3 rejected (see Limits) |

## Overview

The original CBOR specification: a self-describing binary format, starting from the JSON data model, that puts small code size ahead of compactness (§1.1). Objective 1 accepts that one value can have several encodings, so determinism was never a property of the format here. §3.9 offers canonical form only as suggestions a protocol may adopt, and §3.10 makes strict decoding optional because of its cost. §8 already names the gatekeeper problem: duplicate keys and number precision can make two decoders see different data.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §3.10 and §8 are the earliest statement of differential decoding, restated by `rfc-8949` |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Superseded, but its old rule is still a live hazard for DEC-002 and R-O-03 |

- **DEC-002**: `ADR-0004` chose bytewise lexicographic map order (RFC 8949 §4.2.1). §3.9 here sorts shorter keys first, the rule `rfc-8949` §4.2.3 keeps under the name length-first. Example of ours: keys 24 (`0x1818`) and -1 (`0x20`) sort -1 first here, and 24 first under §4.2.1.
- **R-O-03**: the canonicalisation algorithm has to be cited. Citing this RFC's canonical form would cite a different algorithm, and §3.9 is a list of suggestions, not one fixed algorithm.

## Implementations

**Not searched for this record.** It is obsolete, so what to build on belongs to `rfc-8949`. mofn's `research/0001-cbor/dimensions/open-source.md` surveys the libraries. A library's claim to implement this RFC should be read as a warning about its canonical mode.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Obsolete.** Cite `rfc-8949`, not this. The maturity field keeps the status the RFC was published with.
- **Errata.** 2 verified, both wrong encodings in the text (§2.4.2, §3.6). 4 held, including Appendix A example EID 5917. 3 rejected, all against §3.9, and EID 4964 proposed the plain binary comparison that RFC 8949 §4.2.1 now uses.
- **§3.9 leaves float, tag and NaN handling to the protocol.** It suggests rules only.
- **Whether a given library still uses this order was not tested.**
- **Read scope.** §1, §1.1, §1.2, the §2 opening and the first major types in §2.1, §3.9, §3.10, §5, §7.2 and §8 of the cached `.txt`. The rest of §2 and §3, §4, §6 and the appendices were not read. The RFC 8949 §4.2.3 comparison was checked against `records/ietf/rfc-8949/distilled/normative.md`.
