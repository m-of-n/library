---
schema: "library-summary/v1"
id: draft-ietf-cbor-serialization
record: draft-ietf-cbor-serialization
type: summary
updated: "2026-10-19"
---

# CBOR Serialization and Determinism

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft — IETF CBOR WG, intended status **Standards Track** |
| **Authors** | L. Lundblade (Security Theory LLC) |
| **Published** | 29 July 2026 (revision -08); expires 30 January 2027 |
| **Identifier** | draft-ietf-cbor-serialization-08 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cbor-serialization-08.txt |
| **Digest** | `5e5f2e9c0ec3…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

This draft names three CBOR serializations and fixes the relation between
them: **general** (anything well-formed), **preferred-plus** (shortest head,
definite lengths, preferred float widths — but maps unsorted), and
**deterministic** (preferred-plus plus sorted map keys). They nest:
deterministic ⊂ preferred-plus ⊂ general. The one rule deterministic adds over
preferred-plus is map ordering, and §5.1 item 2 states it precisely — items
"MUST be sorted in the bytewise lexicographic order of their deterministic
encodings of the map keys", which it notes is RFC 8949 §4.2.1's sorting and
explicitly *not* RFC 7049 §3.9 / RFC 8949 §4.2.3's length-first sorting.

Preferred-plus exists as a separate mode "solely because map sorting can be
too expensive in some constrained environments". The draft also adds a CDDL
control operator and ships a worked corpus of 25 example files in Appendix L.2.

This is the CBOR working group's **live** determinism work. `draft-ietf-cbor-cde`
is parked and expired; see *A contradiction in our own repo* below.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | library#39 lists this as the serialization and determinism rules a signing profile must target; it is the live WG document. |
| Security | supporting | Determinism is the precondition for signing a structured object; this draft is the candidate cited algorithm under R-O-03. |

**The finding that matters most, and it is about the document's own test
corpus.** Appendix L.2 is the most attractive thing here — 25 files with
general, preferred-plus and deterministic encodings enumerated, which looks
like a ready-made conformance suite. It cannot test the one rule that
distinguishes the two modes we care about.

The document contains **16 map encodings in total**, all in Appendix L.2
(`map.edn` and `map_strings.edn`, eight each). Because §5.1 item 2 sorts on the
*deterministic encoding* of each key, every key in every one of those maps
normalises to equal length within its map — one-byte integer keys, or
four-byte text keys. Equal lengths collapse length-first sorting onto its
bytewise tiebreak, so **bytewise order and the rejected RFC 7049 length-first
order agree on all sixteen: zero disagreements.** A library implementing the
sort this draft explicitly rejects passes the entire suite.

This was re-derived twice and the second derivation corrected the first: an
earlier reading found one disagreement by sorting keys *as printed* (where
indefinite-length string keys are 7/7/6 bytes), which is neither what §5.1 item
2 says nor what RFC 7049 §3.9 means, since §3.9 is part of Canonical CBOR and
already requires shortest-form keys. The corrected result is cleaner: the gap
is total, not contingent on one vector being rejected for other reasons.

For our purposes that means the corpus is a good test of *encoding* and no test
at all of *ordering*, and the ordering rule is precisely what a signing profile
buys from deterministic serialization.

## Implementations

The draft names no implementations and has no implementation-status section.
Its only running code is Appendix D's 133-line C function for preferred float
encoding, held verbatim at `distilled/schema/pref-plus-float.c`. *Searched on
2026-10-19; no named implementation in the document.* The extraction's own
decoder reproduced all 105 vectors and independently agreed with the author's
Appendix L.2 lists across all 25 files, 34 preferred-plus and 24 deterministic
encodings, with zero mismatches.

## Limits

- **An expiring draft.** Revision -08 expires 30 January 2027, so citing it
  means citing a moving target — the same R-O-03 standing problem as dCBOR and
  CDE.
- **§3 states a wrong value.** It says `0xc34100` encodes 0; it encodes **−1**.
  `0xc3` is tag 3, the *negative* big number (value −1−n), so with content
  `0x00` the value is −1 — and the corpus's own `zero.edn` lists `h'c2420000'`
  and `h'c240'`, with tag **2**, never `c34100`. Verified by decoding.
- **No duplicate-key rule anywhere.** §4.1, §4.2, §5.1 and §5.2 are silent, and
  RFC 8949 §4.2.1's prohibition is not restated. Within those sections the word
  "key" occurs exactly once, in §5.1 item 2's sorting note. Appendix C.4 says
  *when* two float keys are duplicates without saying what to do about it.
- **§4.1 item 1 is incomplete and, read literally, admits ill-formed
  encodings.** Its enumeration of argument widths stops at `ai = 0x1a` and
  never states the 8-byte case, although §9.1 enumerates all five and
  Appendix L.2 treats `1b`-headed arguments as general-only throughout. And
  because it is stated "for all major types", it admits `0xf8 0x18`–`0xf8 0x1f`
  — simple values 24–31, which RFC 8949 §3.3 declares not well-formed. The
  exception is never mentioned; the derived artifacts follow RFC 8949.
- **Appendix F's bignum size floor is one byte too loose** — `bstr .size
  (8..bnmax)` where no 8-byte content can occur in preferred-plus, so the floor
  is 9, as the document's own `h'c349010000000000000000'` demonstrates.
- **Two scope claims in tension**: §4.4 lists three differences from RFC 8949
  preferred serialization while Appendix C.5 calls the NaN restriction "the
  sole difference" from §4.2.1. They reconcile, but the document never does it,
  and anyone comparing this draft against CDE or dCBOR on C.5 alone misses the
  big-number half.
- `COSE_Sign1` and `Sig_structure` are referenced but never defined, and
  Appendix C.5's escape hatch ("A new CBOR tag can be defined in the future")
  names no tag number and no content model.
- The extraction is at **passes 1 and 2 of 3**; cross-check has not run and no
  human has signed anything off, so these artifacts are readable but not
  buildable-on.

## A contradiction in our own repo

`topics/deterministic-cbor-profiles.yaml` says "the CBOR WG is now writing CDE
to close it [the §4.2 gap]". This record and `draft-ietf-cbor-cde`'s both say
CDE expired 2026-04-17, is parked, and that the live work is *this* document.
Both are ours, both are cited, and the topic is `status: open` with no owner. A
reviewer reading only the topic will believe CDE is the working group's live
determinism effort. Recorded because an extraction can report it but not fix
it.

## One finding for the COSE export lane

Appendix K.2 says **this COSE requirement** is "also effectively equivalent to
preferred-plus serialization as defined in Section 4, because the Sig_structure
contains no maps." The `Sig_structure` is an array of a text string and byte
strings — protected headers enter as a byte string *wrapping* an encoded map,
not as a map — so deterministic serialization's one added rule has nothing to
bite on, and the document confirms it two paragraphs later: "determinism
requirements do not extend into CBOR inside of byte strings." A preferred-plus
encoder suffices for signing. Note the subject is the COSE requirement, not the
structure; do not restate this as "the `Sig_structure` is equivalent to a
serialization", which compares a structure to a mode.
