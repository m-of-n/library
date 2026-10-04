---
record: rfc-8785
kind: schema
artifact: sorting
provenance: derived
title: "rfc-8785 — property-name sorting, as an implementable algorithm"
derived_from: "RFC 8785 Section 3.2.3 (in full), with Section 3.1 and Appendix A"
extracted: "2026-10-03"
reviewed_by: ""
---

# Sorting of object properties — RFC 8785 §3.2.3

**DERIVED — not verbatim.** RFC 8785 ships no ABNF, no CDDL and no JSON
Schema; its only formal artifact is the ECMAScript sample canonicalizer of
Appendix A, held verbatim in this directory as `canonicalizer.ecmascript.js`.
§3.2.3 states the sorting rule in prose. Everything below that is not inside a
blockquote was written for this record and **must not be quoted as RFC 8785's
own text**. Source quotations are blockquoted and attributed to their section.

This file exists because sorting is the one JCS rule that **no grammar can
express**. `canonical-output.abnf` admits any member order (its gap item 1);
`i-json-input.schema.json` does not reach the output at all. A harness that
checks only those two has not checked canonicalization. This is the missing
decision procedure.

Derived from: §3.2.3 in full (including its worked example, its rationale
paragraph, its test data, and its closing Note), §3.1 (duplicate property
names), §3.2.2.2 (what "raw form" means), and Appendix A (the reference
implementation of the rule).

---

## 1. What is sorted, and what is not

> *  JSON object properties MUST be sorted recursively, which means that JSON
>    child Objects MUST have their properties sorted as well.
>
> *  JSON array data MUST also be scanned for the presence of JSON objects (if
>    an object is found, then its properties MUST be sorted), but array element
>    order MUST NOT be changed.
>
> — RFC 8785 §3.2.3

Three separate obligations, worth separating because implementations get the
third wrong:

| | obligation | scope |
|---|---|---|
| S-1 | every object's members are emitted in sorted name order | **every** object, at every depth |
| S-2 | the recursion descends through objects **and through arrays** | arrays are traversed, not skipped |
| S-3 | array element order is **preserved exactly** | arrays are never reordered, never deduplicated |

S-2 is the one that is easy to miss: an array is not itself sorted, but it is
not a leaf either. An object nested inside an array inside an object must have
its own members sorted. Appendix A implements exactly this — the array branch
recurses into `serialize(element)` while maintaining element order, and only
the object branch calls `.sort()`.

Only **names** participate. A member's value travels with its name; values are
never compared, never reordered among themselves, and never consulted to break
a tie (there are no ties — see §5).

---

## 2. The comparison, stated as an algorithm

> *  The sorting process is applied to property name strings in their "raw"
>    (unescaped) form.  That is, a newline character is treated as U+000A.
>
> *  Property name strings to be sorted are formatted as arrays of UTF-16
>    [UNICODE] code units.  The sorting is based on pure value comparisons,
>    where code units are treated as unsigned integers, independent of locale
>    settings.
>
> *  Property name strings either have different values at some index that is a
>    valid index for both strings, or their lengths are different, or both.  If
>    they have different values at one or more index positions, let k be the
>    smallest such index; then, the string whose value at position k has the
>    smaller value, as determined by using the "<" operator, lexicographically
>    precedes the other string.  If there is no index position at which they
>    differ, then the shorter string lexicographically precedes the longer
>    string.
>
> — RFC 8785 §3.2.3

Rendered as a procedure:

```
KEY(name):
    1. Take the name in its RAW form: the sequence of Unicode code points the
       name denotes, AFTER JSON escape sequences have been resolved and
       BEFORE JCS output escaping is applied.  (§3.2.3 bullet 1, §4 below.)
    2. Encode that sequence as UTF-16: each code point below U+10000 becomes
       one code unit equal to its value; each code point U+10000..U+10FFFF
       becomes the surrogate pair
           lead  = 0xD800 + ((cp - 0x10000) >> 10)
           trail = 0xDC00 + ((cp - 0x10000) & 0x3FF)
       in that order.  (§3.2.3 bullet 2.)
    3. Return the resulting array of 16-bit UNSIGNED integers.

PRECEDES(a, b):            # true iff name a sorts strictly before name b
    A = KEY(a); B = KEY(b)
    for i in 0 .. min(len(A), len(B)) - 1:
        if A[i] != B[i]:
            return A[i] < B[i]          # unsigned 16-bit comparison
    return len(A) < len(B)              # the shorter-string rule
```

Four properties of `PRECEDES` that an implementer must not relax:

- **Unsigned.** Code units are 16-bit unsigned values, `0x0000..0xFFFF`. A
  language whose 16-bit type is signed (Java's `char` is unsigned, but its
  `short` is not; C's `wchar_t` is implementation-defined) will order
  `0x8000..0xFFFF` **before** `0x0000..0x7FFF` if the comparison is signed.
  Every name containing a character at or above U+8000 — including the whole
  CJK compatibility and presentation-form area, and every lead surrogate —
  would then sort wrongly.
- **Locale-independent.** "independent of locale settings". No collation, no
  `strcoll`, no ICU, no case folding, no accent folding, no `localeCompare`.
  A locale-aware collator will order `"a"` before `"B"` and will treat `"ö"`
  as adjacent to `"o"`; JCS orders by raw code unit, so `"B"` (0x0042) precedes
  `"a"` (0x0061) and `"ö"` (0x00F6) sorts after both.
- **No normalization.** §3.1's Note — "all components involved in a scheme
  depending on JCS MUST preserve Unicode string data 'as is'" — applies to the
  sort key as much as to the output. `"é"` (NFC) and `"é"` (NFD) are
  two different names that sort to two different places and are **not**
  duplicates of one another.
- **The shorter-string rule is a tiebreak on a prefix, not a length-first
  order.** `"aa"` precedes `"ab"` because they differ at index 1, not because
  of any length consideration. Length is consulted **only** when one name is a
  proper prefix of the other. This differs from CBOR's length-first map
  ordering of RFC 8949 §4.2.3, and it is worth being explicit about the
  difference when comparing JCS against a CBOR deterministic profile.

The source gives the intended shape in plain English:

> In plain English, this means that property names are sorted in ascending
> order like the following:
>
>         ""
>         "a"
>         "aa"
>         "ab"
>
> — RFC 8785 §3.2.3

The empty string, when present, always sorts first: it is a prefix of
everything and differs from nothing.

---

## 3. Why UTF-16, and the incompatibility that follows

> The rationale for basing the sorting algorithm on UTF-16 code units is that
> it maps directly to the string type in ECMAScript (featured in web browsers
> and Node.js), Java, and .NET.  In addition, JSON only supports escape
> sequences expressed as UTF-16 code units, making knowledge and handling of
> such data a necessity anyway.  Systems using another internal representation
> of string data will need to convert JSON property name strings into arrays of
> UTF-16 code units before sorting.  The conversion from UTF-8 or UTF-32 to
> UTF-16 is defined by the Unicode [UNICODE] standard.
>
> — RFC 8785 §3.2.3

And the consequence, which the source states as a Note and which is the single
most important portability fact in the document:

> Note: For the purpose of obtaining a deterministic property order, sorting of
> data encoded in UTF-8 or UTF-32 would also work, but the outcome for JSON
> data like above would differ and thus be incompatible with this
> specification.  However, in practice, property names are rarely defined
> outside of 7-bit ASCII, making it possible to sort string data in UTF-8 or
> UTF-32 format without conversion to UTF-16 and still be compatible with JCS.
> Whether or not this is a viable option depends on the environment JCS is used
> in.
>
> — RFC 8785 §3.2.3

**Derived — the exact condition.** UTF-8 byte order and UTF-32 code-unit order
are both identical to Unicode code-point order. UTF-16 code-unit order is not,
because a supplementary-plane character sorts under its **lead surrogate**,
which lies in `0xD800..0xDBFF` — *below* every BMP character in
`U+E000..U+FFFF`, even though its code point is far above them. So:

> The two orders **coincide** for all property names drawn entirely from the
> Basic Multilingual Plane (`U+0000..U+FFFF`), which includes all of 7-bit
> ASCII. They **diverge** exactly when the deciding comparison is between a
> supplementary-plane character (`U+10000..U+10FFFF`) and a BMP character in
> `U+E000..U+FFFF`; in that case UTF-16 puts the supplementary character first
> and code-point order puts it last.

Verified for this record by exhaustively comparing both orders over 275,145,156
single-character name pairs sampled across the whole scalar range, densely
through `U+D000..U+E100`: every disagreeing pair had a supplementary character
on one side and a character in `U+E000..U+FFFF` on the other, and **no**
BMP-only pair disagreed. This is a derived result, not a statement of the
source's.

Practical reading: emoji, historic scripts, musical notation, and most
mathematical alphanumerics are supplementary; private-use-area characters,
CJK compatibility ideographs, Arabic and Hebrew presentation forms, halfwidth
forms, and `U+FFFD` are the BMP side. A system whose property names stay inside
the BMP may sort UTF-8 bytes directly and remain JCS-compatible. **One
supplementary character in one property name is enough to break that**, and it
breaks it silently — the output is still well-formed JSON, still deterministic,
and verifies against a different digest.

---

## 4. "Raw (unescaped) form" — and the bug it is there to prevent

> The sorting process is applied to property name strings in their "raw"
> (unescaped) form.  That is, a newline character is treated as U+000A.
>
> — RFC 8785 §3.2.3

**Derived.** There are three candidate spellings of a name and only one is the
sort key:

| spelling | example for a carriage return | sort key? |
|---|---|---|
| the input's JSON escape | `\u000d` or `\r` as written in the source document | no |
| the **raw** code points | `U+000D` | **yes** |
| the JCS output escape (§3.2.2.2) | `\r` (two characters, `U+005C U+0072`) | no |

Sorting is on the middle row — the decoded characters — even though the output
will re-escape them. A canonicalizer that sorts the serialized, re-escaped
names gets a different answer whenever an escaped character is involved,
because the escape introduces a leading `U+005C` (`0x5C`) that dominates the
comparison.

This is not hypothetical, and §3.2.3's test data is built to catch it: sorting
the **escaped** forms of that data puts `"One"` first instead of
`"Carriage Return"`, because `"1"` is `0x0031` while the escaped `\r` begins
`0x005C`. The divergence appears at position 0 of the result.

---

## 5. There are no ties

**Derived.** §3.1 requires that "JSON objects MUST NOT exhibit duplicate
property names". Two names that compare equal under §2 are byte-identical
sequences of code units and therefore the same name — which §3.1 forbids within
one object. So within a single object the ordering is a **strict total order**
and:

- sort **stability is irrelevant**: no comparator call can return "equal" for
  two distinct members, so an unstable sort (C's `qsort`, Java's
  `Arrays.sort` on primitives, V8's pre-2018 `Array.prototype.sort`) is as
  correct here as a stable one;
- the canonical form is **unique**, which is the whole point;
- conversely, if an implementation ever observes two equal keys while sorting,
  the input violated §3.1 and the §3.1 check was skipped upstream. That is a
  useful place to assert, because — see `i-json-input.schema.json` — the
  duplicate-name rule is unenforceable by schema and most parsers have already
  collapsed the duplicate before the canonicalizer is reached.

---

## 6. Conformance vector — §3.2.3's own test data

> The following JSON test data can be used for verifying the correctness of the
> sorting scheme in a JCS implementation:
>
>     {
>       "\u20ac": "Euro Sign",
>       "\r": "Carriage Return",
>       "\ufb33": "Hebrew Letter Dalet With Dagesh",
>       "1": "One",
>       "\ud83d\ude00": "Emoji: Grinning Face",
>       "\u0080": "Control",
>       "\u00f6": "Latin Small Letter O With Diaeresis"
>     }
>
> Expected argument order after sorting property strings:
>
>     "Carriage Return"
>     "One"
>     "Control"
>     "Latin Small Letter O With Diaeresis"
>     "Euro Sign"
>     "Emoji: Grinning Face"
>     "Hebrew Letter Dalet With Dagesh"
>
> — RFC 8785 §3.2.3

**Derived — the sort keys, and what each wrong answer looks like.**

| expected position | value | name | `KEY(name)` |
|---|---|---|---|
| 1 | Carriage Return | `U+000D` | `000D` |
| 2 | One | `U+0031` | `0031` |
| 3 | Control | `U+0080` | `0080` |
| 4 | Latin Small Letter O With Diaeresis | `U+00F6` | `00F6` |
| 5 | Euro Sign | `U+20AC` | `20AC` |
| 6 | Emoji: Grinning Face | `U+1F600` | `D83D DE00` |
| 7 | Hebrew Letter Dalet With Dagesh | `U+FB33` | `FB33` |

Seven names, each one character, chosen so that a single comparison exposes
each of the three classic implementation errors. Computed for this record:

| sorted by | result | first divergence |
|---|---|---|
| **UTF-16 code units (JCS)** | matches the expected order | — |
| code point / UTF-32 | wrong | position 6: Hebrew Dalet, not Emoji |
| UTF-8 bytes | wrong | position 6: Hebrew Dalet, not Emoji |
| escaped output form | wrong | position 1: One, not Carriage Return |

So rows 6 and 7 are the UTF-16-vs-code-point probe (`D83D` < `FB33` in UTF-16;
`U+FB33` < `U+1F600` by code point), and row 1 against row 2 is the
raw-vs-escaped probe. Row 3 (`U+0080`) additionally confirms the §3.2.2.2
escaping boundary — it is a control character that JCS does **not** escape,
since the `\uhhhh` rule stops at `U+001F`, so it appears in canonical output as
the raw UTF-8 bytes `c2 80`.

The sample canonicalizer of Appendix A was run against this vector for this
record and reproduced the expected order exactly, emitting:

```
{"\r":"Carriage Return","1":"One","<U+0080>":"Control","ö":"Latin Small Letter O With Diaeresis","€":"Euro Sign","😀":"Emoji: Grinning Face","דּ":"Hebrew Letter Dalet With Dagesh"}
```

(`<U+0080>` stands for the raw unescaped `U+0080` character, which is not
printable here.) The same run reproduced the §3.2.3 worked example and the
§3.2.4 byte dump byte-for-byte. Fixtures belong in `../examples/`, not here;
this section is the algorithm's acceptance criterion, not the vector file.

---

## 7. Two traps in the reference implementation's host language

**Derived**, from running Appendix A for this record. Neither is a defect in
the sample; both are ECMAScript behaviours that an implementer transcribing it
will meet.

1. **`Object.keys()` does not return insertion order for integer-like names.**
   ECMAScript hoists array-index-like property names to the front in ascending
   numeric order. For §3.2.3's test data, `Object.keys()` returns `"1"` first,
   ahead of `"\r"`. Appendix A is correct because `.sort()` immediately
   repairs it — `Object.keys(object).sort()` — but an implementation that
   relies on `Object.keys()` order anywhere, or that uses a map type with its
   own ordering, inherits a bug that only shows up on numeric property names.

2. **Canonical order does not survive a round trip through an object.**
   Parsing canonical JCS output back into an ECMAScript object and re-reading
   its keys re-applies the hoisting above, so the canonical order is lost.
   Canonical order is a property of the **octet string** (§3.2.4), not of any
   in-memory value. Anything that re-parses canonical output and re-serializes
   it must re-run the full canonicalization; it must not assume the order came
   back.

A third point, from the sample's own banner rather than from running it: the
Appendix A code states that "error handling and UTF-8 generation were not
implemented", so it does not enforce the lone-surrogate rule (§3.2.2.2), the
NaN/Infinity rule (§3.2.2.3), or the UTF-8 output encoding (§3.2.4). It is a
specification aid, not a conformant implementation.

---

## 8. What is still not decidable from this file alone

- **S-3, "array element order MUST NOT be changed", is a relation between input
  and output.** Nothing examining the output alone can verify it; only a
  differential test against the input can. Same gap as
  `canonical-output.abnf` item 3.
- **Whether the sort key was built from the raw form** is likewise invisible in
  the output for names containing no escapable character — which is most names.
  §3.2.3's test vector is the check; there is no structural one.
- **This file states the order; it does not state the serialization.** The
  escaping, number and whitespace rules are in `canonical-output.abnf`. A
  correct order with incorrect escaping is still a wrong digest.
