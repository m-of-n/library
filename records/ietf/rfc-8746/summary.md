---
schema: "library-summary/v1"
id: rfc-8746
record: rfc-8746
type: summary
updated: "2026-11-05"
---

# Concise Binary Object Representation (CBOR) Tags for Typed Arrays

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc8746.json` 2026-11-01 |
| **Authors** | C. Bormann, Ed. |
| **Published** | 2020-02 |
| **Identifier** | RFC 8746 · DOI 10.17487/RFC8746 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8746.txt |
| **Digest** | `sha256:26d0f7d0…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 8746 ships numeric arrays as one byte string under a tag whose bits give integer or float, sign, endianness and element length, so that memory buffers can move without converting each element (§1, §2). Tags 64 to 87 cover 24 variants, and tags 40, 1040 and 41 add multi-dimensional and homogeneous arrays (§3). Little-endian forms are admitted on purpose, against CBOR's otherwise big-endian habit (§4). §1 is the part that matters to us: no variant is preferred, so a protocol wanting determinism has to choose one for each case.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §7: tag 41's promise may be false, and clamped and plain uint8 arrays can be swapped by an attacker |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Evidence for a decided point: we do not use these tags |

- **DEC-002**: `ADR-0004` forbids tags, and this RFC shows the cost of allowing them. One array has many valid encodings, and §1 names none as preferred and leaves the choice to the protocol. Our reading: RFC 8949 §4.2.1 alone therefore cannot pick one.
- **R-M-12**: now `ARCH-0002` P1, accepted by `ADR-0001`. These are registry numbers, a block of the one-byte tag space that §4 itself calls sizable.

## Implementations

**Searched 2026-11-01.** GitHub code search for `RFC8746 cbor typed array` returned nothing. A narrow query: mofn's `research/0001-cbor/dimensions/open-source.md` already names cbor-x as implementing RFC 8746, and its README, read 2026-11-05, says so.

| Name | Kind | License | URL |
|---|---|---|---|
| cbor-x | open source, JS | MIT | https://github.com/kriszyp/cbor-x |

- **cbor-x**: README claims RFC 8746; which tags it supports was not tested.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **The data-item text disagrees with itself.** §3.1.1 allows a Homogeneous Array as tag 40's element array. The note under Table 3 lists only a major type 4 array or a Typed Array. `draft-ietf-cbor-packed` §7 quotes that note.
- **A byte string that is not a whole number of elements is not addressed.** §2 only derives the count by shifting.
- **It cites RFC 7049,** so its security reference points to `rfc-7049` §8.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the references.
