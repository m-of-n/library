---
schema: "library-summary/v1"
id: draft-ietf-cbor-packed
record: draft-ietf-cbor-packed
type: summary
updated: "2026-11-01"
---

# Packed CBOR

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | `draft`: **expired** 2026-08-06, Datatracker state Expired, read 2026-11-01 |
| **Authors** | C. Bormann, M. Gütschow |
| **Published** | 2026-02-02, expired 2026-08-06 |
| **Identifier** | draft-ietf-cbor-packed-19 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cbor-packed-19.txt |
| **Digest** | `sha256:fa660259…` (full value in `record.yaml`), verified on fetch 2026-11-01 |

## Overview

Packed CBOR replaces repeated substructure with references into a shared-item table and an argument table, so a recipient can often use the data without a separate decompression step (§1, §2). The draft defines only the reconstruction, not a packer (§1). Tables come from tags 113 and 1113 or from the application environment, such as a media type (§3). Its broadest claim is in §7: a tag or simple value may declare that it stands in for a structure, and §7.1 says existing protocols that never mention this implicitly gain a variant allowing it. Because unpacking is recursive, a crafted item can contain a reference loop, and §2.5 makes protecting against that mandatory.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Reference loops and blow-up during unpacking (§2.5, §9). Table evolution can change what old references mean (§9) |
| Cryptography | `none` | No cryptography. §9 touches signing inputs only |
| This project | `adjacent` | Shows what `ADR-0004` keeps out, and nothing we would adopt |

- **DEC-002**: closed by `ADR-0004`, whose profile forbids tags and simple values, so tag 6, tags 113 and 1113, and `simple(0..15)` are all rejected by a conforming KSA-CBOR decoder. The record's value is the argument against: §9 allows packed forms as signing inputs when deterministically encoded, but concedes that external dictionaries need more consideration. Our reading: the meaning of signed bytes would then depend on a table outside them.
- It bears on no `R-*` directly. `ARCH-0002` P1 would apply only if tags were native, and they are not.

## Implementations

**Searched 2026-11-01.** GitHub code search for `Packed CBOR tag 113` returned nothing. cbor-x comes from mofn's 2026-09-22 survey, not from this search.

| Name | Kind | License | URL |
|---|---|---|---|
| cbor-x | open source, JS | MIT | https://github.com/kriszyp/cbor-x |
| cbor-wg/cbor-packed | specification repository, not a library | not identified by GitHub | https://github.com/cbor-wg/cbor-packed |

- **cbor-x**: Named as the one real implementation by mofn research/0001-cbor/report.md; not re-checked here.
- **cbor-wg/cbor-packed**: Source and issue tracker named by the draft.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A draft owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **It has no standing.** An expired Internet-Draft, usable only as work in progress. Nothing here should be cited as a CBOR rule.
- **The numbers are requests, not allocations.** On 2026-11-01 the IANA tags CSV had none of 6, 105, 106, 113, 114, 128, 1112, 1113 or 1115, and the simple values CSV showed 0-19 as unassigned. The abstract's editor note says -19 chose numbers in preparation for continuing early allocation.
- **Two conforming unpackers can differ.** §2.1 lets an unpacker either abort on an unpopulated index or hand the application a tag 1112 value.
- **No efficiency evidence was assessed.** Appendix A's examples were not read, so no size claim is made here.
- **Read scope.** -19 from the cached `.txt`: abstract and §1 to §9 read in full, the start of the references, not Appendix A or the rest of the references.
