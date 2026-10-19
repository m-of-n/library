---
record: draft-ietf-cbor-serialization
kind: schema
title: "draft-ietf-cbor-serialization — schemas"
extracted: "2026-10-18"
pass: 1
reviewed_by: ""
---

# CBOR Serialization and Determinism — schemas

## The document ships three formal artifacts, and they are small

Unusually for this library, **draft-ietf-cbor-serialization-08 does ship formal
material of its own** — three pieces, all held here verbatim:

- **CDDL in Appendix F**, twelve lines, for big numbers.
- **CDDL in Section 8**, five lines across two examples, for the `.serial`
  control operator it defines.
- **C in Appendix D**, 133 lines, "Figure 1: Example C Code for Preferred-Plus
  Floating-Point Encoding".

It ships **no ABNF**, no JSON Schema, no pseudocode, and no CDDL profile of
either serialization it defines. The four derived files below are this
library's and must never be cited as the document's own grammar.

| file | claim | covers | deliberately does **not** constrain |
|---|---|---|---|
| `bignums.cddl` | **verbatim** (App. F, src 1811-1822) | the shape of tags 2 and 3 and their byte-string content; the `#0 / #6.2(bstr)` type choice that expresses the unified integer space | leading zeros (§4.1 item 5 b1); the integer/big-number *choice* itself, since a CDDL type choice matches in both arms; any real upper bound — `bnmax = 1000` is a fiction the source's own comment admits |
| `serial-control-operator.cddl` | **verbatim** (§8, src 967-969 and 974-975) | the two worked usages of `.serial`: on a root rule, and on a type wrapped in tag 24 | everything the serializations *are*. `.serial` is a hook for a validator to call out to a codec; a CDDL tool that does not implement this draft checks the left-hand side and ignores the controller |
| `pref-plus-float.c` | **verbatim** (App. D, src 1588-1744) | the float-width decision procedure, double→single→half, and the −1 "cannot narrow" signal; the only executable artifact in the document | it is labelled "Example … Code" and is not normative — §4.1 item 4 is the requirement. It decides width and NaN rejection only; nothing else in §4.1 |
| `prefp-head.derived.abnf` | **derived** | the data item *head* under preferred-plus: the shortest-form argument (§4.1 item 1) **decided by construction**, definite lengths only (items 2 and 3), the one permitted NaN and the always-reducible float patterns (item 4), and both bullets of the big-number rule (item 5) | the float width rule in general — see below; **map key ordering**, which no grammar can express; duplicate keys; UTF-8 well-formedness; string content |
| `prefp-encode.derived.pseudocode.txt` | **derived** | the encoder, §4.1 and §5.1 as one procedure: head emission, the unified integer space, string/array/map emission, the map sort, float narrowing via Appendix D, and `BYTEWISE_LT` spelled out byte by byte | nothing in §4.1/§5.1 is omitted. It is a *reading*, not the document's text — in particular the 8-byte argument step, which the document never states |
| `serialization-check.derived.pseudocode.txt` | **derived** | the two decoder jobs kept apart: ACCEPT (§4.2, §5.2 — what any decoder must take) and CHECK (App. H — the optional conformance pass), plus the four test procedures of App. L.1 | it cannot check what the document does not require: duplicate keys, Unicode form, or anything about general serialization, which by definition rejects nothing |

`.derived.` is mandatory on anything this library wrote and an unmarked
filename asserts the source's own bytes — `docs/extraction.md`, *Derived vs
verbatim*. Every file also carries its claim in its own header, and the two
agree. No derived JSON Schema exists here, so no `urn:library:` `$id` applies.

## What CDDL cannot say about this document, and why that is the whole story

The document's subject is **serialization**, and RFC 8949 §2 makes
serialization variants *invisible* in the generic data model on purpose. CDDL
describes that data model. So a CDDL profile of preferred-plus or deterministic
serialization would be silent on precisely the rules that define them:

- **The shortest-head predicate.** "0 to 23 … MUST be encoded in the same byte
  as the major type" is a statement about which of five encodings of the same
  data-model value is permitted. CDDL has no way to say it. *ABNF can*, because
  a value range over a fixed-width big-endian argument is a byte-range
  constraint — which is why `prefp-head.derived.abnf` exists and is the only
  artifact here that decides §4.1 item 1 mechanically.
- **Definite versus indefinite length.** Same reason: the two encode the same
  data-model value. CDDL cannot distinguish `[1, 2]` from `[_ 1, 2]`.
- **Sibling ordering.** §5.1 item 2 constrains the *relation between* a map's
  entries, which is not a property of any entry. No grammar — CDDL or ABNF —
  expresses a sibling-ordering constraint, and in a model where maps are
  unordered (RFC 8949 §5.6) there is nothing for it to constrain. This is why
  the one difference between the document's two serializations is invisible in
  every file in this directory except the two pseudocode procedures.
- **The NaN restriction**, at the data-model level. CDDL has no NaN literal,
  and App. C.4 makes equivalent NaNs at different widths the *same* value, so
  there is nothing to exclude. At the *byte* level the restriction is exactly
  expressible, and `prefp-head.derived.abnf` does exclude it.
- **The float width choice.** "the shortest of double, single or half-precision
  that preserves precision" is arithmetic over the value, not a pattern.
  Partially decidable: ±0, ±Infinity and every NaN are fixed bit patterns and
  are excluded by construction in the ABNF. `h'fa477fe000'` — 65504.0, exactly
  representable in half — is the case that needs Appendix D's code and nothing
  else.

The source says much of this about itself. Appendix F: the prelude's
`bigint`/`biguint` "do NOT describe the big numbers described in this document
… The types integer and unsigned can be used, but note that they do not fully
express the rules that govern the choice between major types 0 and 1 and the
big number tags", and so protocols SHOULD use those and state the rest **in
prose**. §8's answer to the same problem is to add a control operator rather
than a grammar — which is the admission that CDDL cannot express the thing, and
is correct.

## The division of labour, stated as a count

Of the document's **13 numbered encoder and decoder rules** (§4.1 items 1-5,
§4.2 items 1-5, §5.1 items 1-2, §5.2 item 1, plus their sub-bullets):

- `prefp-head.derived.abnf` decides **§4.1 items 1, 2, 3 and 5 in full**, and
  the fixed-pattern part of item 4. Verified exhaustively: of RFC 8949's 229
  well-formed initial bytes it admits 224, 28 for each of the eight major
  types, excluding exactly `5f`, `7f`, `9f`, `bf` and `ff`. Every float
  byte-range predicate in it was checked against IEEE 754 over all 65536 half
  patterns and all 65536 leading-two-byte patterns of single and of double.
- `prefp-encode.derived.pseudocode.txt` adds the value-dependent half of item 4
  and all of §5.1.
- `serialization-check.derived.pseudocode.txt` covers §4.2 and §5.2, which are
  about *acceptance* and have no grammatical content at all.

The split against the neighbouring record is worth noting, because the two
drafts pull in opposite directions. `draft-mcnally-deterministic-cbor`'s ABNF
here narrows the *initial byte* hard — 27 bytes removed — and says in its own
header that it "cannot require the shortest [argument] form". This document is
the mirror image: it removes 5 initial bytes and states the shortest-form rule
as four explicit value ranges, so the rule the other grammar had to defer is
decided here by construction.

## Defects and gaps found in the source's own formal material

Recorded, never repaired — the verbatim files hold the source's bytes unaltered
and each carries the finding in its header.

1. **`bnbstr = bstr .size (8..bnmax)` is one byte too loose** (Appendix F). No
   8-byte big-number content can occur in preferred-plus: without leading zeros
   its value is at most 2^64−1, which major type 0 carries, so §4.1 item 5
   bullet 2 forbids it; with leading zeros bullet 1 forbids it. The floor is 9,
   which the document's own vector `h'c349010000000000000000'`
   (negative_bignum.edn, annotated "the value closest that can be represented
   as a big number, not a type 1 integer") demonstrates. The bound should read
   `(9..bnmax)`. Two independent derivations agree — the arithmetic above and
   the ABNF's `bignum-bstr-head`.
2. **§4.1 item 1 never states the 8-byte case.** The enumeration stops at
   "65536 to 4294967295 … (ai = 0x1a)" and says nothing about an argument of
   2^32 or more, although §9.1 enumerates all five widths and Appendix L.2
   treats `1b`-headed arguments as general-only throughout. Both derived
   procedures supply the missing step and both label it as ours.
3. **§4.1 item 1 collides with RFC 8949 §3.3 in major type 7.** Read literally
   — it is stated "for all major types" — its second bullet puts arguments 24
   to 255 in the one-additional-byte form, which would admit `0xf8 0x18`
   through `0xf8 0x1f`, simple values 24 to 31, that RFC 8949 declares not
   well-formed. The document never mentions the exception. The derived files
   follow RFC 8949 and start at `0x20`, justified by the document's own frame:
   general serialization is "the complete set of all encodings standardized in
   Section 3 of [STD94]", and ill-formed encodings are not in it.
4. **Appendix D's `pref_plus_single_to_half()` will not narrow a negative
   trivial NaN** — it tests `sign == 0`. That is consistent rather than wrong,
   since Appendix C.1 counts a NaN with the sign bit set as *non-trivial*, but
   it means the code's "trivial NaN" comment covers a narrower set than the
   phrase suggests. Noted in the file's header.
5. **No duplicate-key rule anywhere.** §4.1, §4.2, §5.1 and §5.2 are silent,
   and RFC 8949 §4.2.1's prohibition is not restated. The document's only
   sentence about duplicates is App. C.4's float case, which says *when* two
   keys are duplicates without saying what to do. `CHECK_MAP` in the checking
   pseudocode flags where an implementation must decide for itself, and notes
   that a strict ordering comparison catches byte-identical keys as a side
   effect while a non-strict one does not.
6. **A tension between two scope claims, reported as a tension.** §4.4 lists
   three differences between preferred-plus and RFC 8949 preferred
   serialization (definite lengths as requirement not preference; the NaN
   restriction; the big-number leading-zero and empty-string decoder rules),
   while App. C.5 calls the NaN restriction "the sole difference" from RFC 8949
   §4.2.1. The two reconcile — §4.2.1 already requires definite lengths, and
   the big-number items are decoder-acceptance rules — but the document never
   does the reconciling, and a reader comparing this draft against CDE or dCBOR
   on the strength of C.5 alone will miss the big-number half.

## Tooling notes

- `bignums.cddl` and `serial-control-operator.cddl` retain the draft's
  three-space page margin, so the verbatim regions stay byte-identical. CDDL
  tolerates the indentation.
- **Do not concatenate the two CDDL files** and feed them to a validator
  expecting a working schema: `serial-control-operator.cddl` contains the
  draft's `...` ellipses, which are not CDDL, and `.serial` is unknown to
  every current tool.
- `pref-plus-float.c` compiles as-is apart from its last line, the Figure 1
  caption, which is part of the verbatim region and is not C. Strip it or
  comment it out. The three page-break blocks the draft's pagination inserted
  into the code are deleted in full; the file's header gives the source line
  numbers and the reasoning.
- The ABNF is RFC 5234 and uses the core rule `OCTET` without redefining it.
  It is a head grammar: every alternative consumes exactly one head except
  `bignum-opening`, which consumes the tag head, the byte-string head and the
  first content byte, because that is where §4.1 item 5 is decided.
