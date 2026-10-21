---
record: rfc-9277
kind: schema
title: "rfc-9277 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 9277 defines three envelopes in prose and supplies CDDL for none of them.**
Its four CDDL snippets are *content-format tag assertions*, and only two of the
four carry an outer tag at all. So the verbatim captures here are the document's
snippets, its three registry entries and the TN formula; everything that
describes an **envelope** is derived and carries `.derived.` in its name.

**Four verbatim files, three derived.** `docs/extraction.md`, *Derived vs
verbatim*: an unmarked filename asserts the source's own bytes.

| file | claim | what it is |
|---|---|---|
| `cddl-snippets.cddl` | **verbatim** | all four CDDL snippets the document prints (Appendix B.1 ×2, Appendix D.1 ×2), lifted by line range with the RFC's six-space left margin intact. Four regions, each with its source line range and its own sha256. **Not one of them is an envelope** |
| `registrations.txt` | **verbatim** | everything this document asks of IANA — the §4.1, §4.2 and §4.3 entries, complete. Three regions with per-region digests. **Every IANA action in this document is a CBOR tag action**, in its own words |
| `tn-formula.txt` | **verbatim** | the Appendix B allocation, the TN formula, its C-arithmetic clause and its aside — 27 lines that are the normative content of **65,279 registry entries**. The aside's `\|` bars, its two U+2264 characters and the trailing spaces on its blank lines are all preserved |
| `cddl-snippets-dedented.derived.cddl` | **derived** | the same four regions with the margin removed so a CDDL tool can read them. The removal round-trips, and unlike `rfc-8742`'s the four regions may be concatenated: the rule names are distinct |
| `envelopes.derived.cddl` | **derived** | the three envelopes as CDDL — **and the file's value is the four things CDDL cannot say about them**: the inner tag number is a parameter where CDDL requires a literal; the top-level rule for a labelled sequence is an array rule standing in for a sequence rule; a schema cannot distinguish the 12-byte label from its 29 other spellings; and after byte 12 of an Appendix D file there is no CBOR left to describe |
| `content-format-tag.derived.yaml` | **derived** | **the central artifact.** The TN function as data: domain, image, injectivity, the exact shape of the image, the 254 allocated-and-unreachable code points, all four worked values recomputed, the `TN(63)` value for `application/cbor-seq` that the document does not print, and the registry-dependence claim with what it does to `R-M-12` |
| `prefix-spellings.derived.txt` | **derived** | the enumeration that **refutes the document's central claim**. §2 says the two methods give "a deterministic first 8 to 12 bytes"; this file lists **all 30 well-formed definite-length spellings** of the 12-byte label and all 6 of the 8-byte prefix, and counts how many a `file(1)` rule would match |

## Mechanically checked, not asserted

The per-region digest convention is the library's: **`sha256` of the region's
lines joined by `\n`, with no trailing newline** — the convention
`records/ietf/rfc-9741/distilled/schema/README.md` states.

Eight regions, all verified at pass 1:

| region | locator | source lines | sha256 |
|---|---|---|---|
| `C01` | Appendix B.1 | 810 | `4b58e806faccce8abd47678b4a26f4519c41917a9a1055edf93550825aae8a21` |
| `C02` | Appendix B.1 | 825 | `82b9e6793cae5e0a671ca56ebb9856ff8db7e76e4048b63debf51644363dafe6` |
| `C03` | Appendix D.1 | 923 | `bba455f2eadb41e5d9ad801a958148d9ea7a03e6645efe80c232c575ff416960` |
| `C04` | Appendix D.1 | 934 | `2453a98e20afdea71a06ca5e2ddc6f969a19f6ae3d4ef94ded10fd429fc16db5` |
| `R01` | §4.1 | 412–443 | `01fd032c5b072bccb466e2504862d073b2132fd7d1e5049293a4386d9e615139` |
| `R02` | §4.2 | 445–477 | `043f7e11dfb8e15b98cbd8c37ffc4cbdd0c00c77db91746e6ba2c3d9eda40de2` |
| `R03` | §4.3 | 479–496 | `f608633c6488a9f85f632affd5640a7ee2c7aa58b30ca435c75baa2cd09768e5` |
| `F01` | Appendix B | 751–777 | `28959c781267d14b14b03b1db5d8f6db763bed97636c56ff707b843dee7b1920` |

- each region is **byte-identical** to its declared source line range, and each
  declared digest verifies under exactly that convention and under **none** of
  the alternatives;
- a **completeness sweep** over every source line outside the claimed regions
  finds **no CDDL rule and no registration field left uncaptured**;
- the dedented derived file **round-trips**: re-indenting every non-blank line
  by six spaces reproduces the verbatim regions exactly;
- the source carries **no form feeds and no page footers**. Exactly **four**
  lines carry trailing whitespace — 724, 767, 770, 772 — and all four are blank
  **aside** lines; `F01` contains three of them and preserves them. `F01` also
  contains the only two non-ASCII characters in the technical body of the
  document (two U+2264 on line 771), preserved as they are;
- all four worked `TN` values and both 8-byte fingerprints were **recomputed**
  and all six agree with the document.

## Three things the source gets wrong, recorded and not repaired

1. **The document's own CDDL does not match the document's own example.**
   `C01` is `senml-cbor = #6.1668546929(bstr)`, justified in B.1 by "Note that a
   byte string is used as the type of the tag content because a media type
   representation in general can be any byte string." But Appendix B adds, in two
   spans quoted separately rather than elided into one, "Exceptionally, when
   used immediately as tag content of one of the tags 55799, 55800, or 55801,
   the tag content is as follows:" and then, under *Tag 55799 (Section 2.2)*,
   "The CBOR data item within the representation (without byte-" /
   "string wrapping)." §2.2.1's
   envelope is therefore `55799(1668546929([{…}]))` — tag content an **array** —
   and `C01` does not match it. B.1 is introduced by a cross-reference *to*
   §2.2.1 ("As discussed in Section 2.2.1"), so a reader is actively invited to
   apply the rule to the example it does not fit.
2. **The TN formula's arithmetic is defined only in an appendix, and only by
   reference to a paywalled standard.** Appendix B: "(where +, *, / and % stand
   for integer addition, multiplication, division, and remainder as in the
   programming language C [C].)" `[C]` is ISO/IEC 9899:2018 and is a
   **normative** reference of this document, used nowhere outside an appendix.
   The §4.3 registry entry — the text IANA publishes — carries the formula and
   **not** the citation. `tn-formula.txt`'s header says so.
3. **The registry text and the RFC text are not identical.** The in-library copy
   of the IANA row (`records/iso/iana-cbor-tags/distilled/tables.yaml`, checked
   at this pass) reads "byte string or any CBOR data item (see Appendix B of
   RFC 9277)" where §4.3 reads "(see Appendix B)". IANA qualified the dangling
   cross-reference; the RFC did not. Two smaller ones: §4.1 says "IANA has updated this tag
   registration to point to this document." and §4.2 says "IANA updated this
   tag registration to point to this document." — *has* in one and not the
   other, for two otherwise word-for-word parallel entries, and §4.3
   writes the block's upper bound `0x6374ffff` where Appendix B writes
   `0x6374FFFF`.

## The one thing to know about `prefix-spellings.derived.txt`

**It refutes §2's central claim, and the refutation is arithmetic rather than
argument.** "Both use CBOR tags in a way that results in a deterministic first 8
to 12 bytes." That holds only under **preferred serialization**, and this
document requires nothing at all — it has **zero** BCP 14 keywords. RFC 8949
§3.1 admits a wider head for the same argument value, and §4.1's preferred rule
is an encoder-side recommendation a conforming decoder does not enforce.

Of the **30** definite-length spellings of the 12-byte label:

- **1** is 12 bytes long;
- **5** match the 8-byte fingerprint §2.3.1 states;
- **20** put a **zero byte inside the first eight**, defeating §2.1's own advice
  to avoid values that "may confuse implementations that treat the magic number
  as a C string."

And **30 is a floor, not a count**: RFC 8949 §3.2.3 also admits an
indefinite-length byte string for the 3-byte content, which the enumeration
excludes. §2.1 pins the tag **value** into `0x01000000..0xFFFFFFFF` and that is
exactly as far as it goes — it makes `da` the *shortest* head and does not
forbid `db`, and it does not reach the outer tag at all, whose value is
`55800 = 0xD9F8`.

## Why there is no `*.schema.json` and no ABNF

Nothing in RFC 9277 is JSON Schema shaped. An ABNF would be the natural language
for a fixed byte prefix, and it is not written here for one reason:
`prefix-spellings.derived.txt` is strictly better for this document, because an
ABNF rule for the preferred spelling alone would **assert the determinism the
document only claims**. The enumeration states the real admissible set, and a
`file(1)` rule author can read it directly.
