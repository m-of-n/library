---
schema: "library-summary/v1"
id: rfc-1952
record: rfc-1952
type: summary
updated: "2026-11-04"
---

# GZIP file format specification version 4.3

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational`: Category Informational, confirmed in `rfc1952.json` 2026-11-01 |
| **Authors** | P. Deutsch |
| **Published** | 1996-05 |
| **Identifier** | RFC 1952 · DOI 10.17487/RFC1952 |
| **Source** | https://www.rfc-editor.org/rfc/rfc1952.txt |
| **Digest** | `sha256:164ef089…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 1952 defines the gzip file format: a series of members, each a header, DEFLATE-compressed data, a CRC-32 of the uncompressed data and the input size modulo 2^32 (§2.2, §2.3). It documents a format already in wide use and aims at interchange without being tied to a CPU, file system or character set (§1.1). The compressor has real freedom: only ID1, ID2, CM, CRC32 and ISIZE must be correct, and the other fixed header fields may take defaults (§2.3.1.2). The reader's obligations are also few: it must check ID1, ID2 and CM, parse the flags far enough to skip the optional fields, and give an error if any reserved bit is non-zero, because such a bit could signal a new field (§2.3.1.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | §4 is about corruption only; a CRC-32 detects accidental damage, not tampering (our reading) |
| Cryptography | `none` | No cryptographic content |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*` yet.** It is held because `draft-ietf-vcon-vcon-core-04` §5.2 allows the signed payload to be the gzipped form of the vCon.

One point for anyone reading that draft. Because §2.3.1.2 lets the compressor default MTIME, XFL and OS, and the FLG bits decide which optional fields appear, two compliant compressors can produce different bytes for one input. So a signature or digest over a gzipped payload binds those particular bytes, not the uncompressed vCon. That is our inference from §2.3.1.2, not a statement in either document.

## Relations

- `see_also: draft-ietf-vcon-vcon-core-04`: that draft cites this RFC as `[GZIP]` for the gzipped signed payload (§5.2) and the `application/vcon+gzip` form (§6.2). The edge is authored only here.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| zlib | open source, C | Zlib (the zlib licence, per the repo `LICENSE`; GitHub's detector reports `NOASSERTION`) | https://github.com/madler/zlib |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It is not a security format.** §4 recommends that systems provide some means of validating integrity, giving setting and checking the CRC-32 as the example. That detects corruption only, and nothing in the format authenticates anything.
- **DEFLATE is defined elsewhere.** §2.3.1 calls it documented elsewhere and §3 cites it in reference [4], not RFC 1951.
- **The subfield registry is informal.** §2.3.1.1 names a person, not a registry operator, and whether that still works was not checked.
- **Errata.** `errata.json` retrieved 2026-11-01, recounted 2026-11-04, lists 1 verified (Editorial). Its text was not reviewed.
- **Read scope.** Whole document, from the RFC Editor `.txt`, including both appendices.
