---
schema: "library-summary/v1"
id: rfc-9741
record: rfc-9741
type: summary
updated: "2026-10-19"
---

# CDDL: Additional Control Operators for the Conversion and Processing of Text

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Proposed Standard |
| **Authors** | C. Bormann |
| **Published** | March 2025 |
| **Identifier** | RFC 9741 · DOI 10.17487/RFC9741 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9741.txt |
| **Digest** | `3234aeea39d01b7c1c8e9c70d4d7dc8745852e0b6edbea167a3e55b91e7a9ee3` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

Fourteen new CDDL control operators, all of them about text. Ten relate a text
string to a byte string through a base encoding — `.b64u`, `.b64c`, `.b45`,
`.b32`, `.h32`, `.hex`, `.hexlc`, `.hexuc` and the two `-sloppy` variants — one
relates text to an integer (`.base10`), one to a printf format and arguments
(`.printf`), one to a JSON text (`.json`), and one concatenates strings
(`.join`).

**It adds no grammar.** RFC 8610's ABNF is untouched, so a CDDL parser needs no
change; what it needs is fourteen more semantic cases. That is why this record
holds the document's CDDL and tables verbatim rather than a grammar.

The genuinely new expressive power is one sentence, §2.3: *"The data items in
the controller array do not need to be literals"*. A text field's content can
now be tied to a CDDL **type** rather than to a constant — before this, text
could only be constrained by `.regexp` against a literal pattern.

All 14 are **type** controls. CDDL has no group controls at all, which the
document never says.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | supporting | Pins an injective text form for a digest or an integer, which is what a hex-valued field in our schema needs. |
| Naming | **core** | This is the document best placed to give CDDL a text-identity constraint, and it declines. See below. |

**The answer this record exists to give is no.** library#39's reading of CDDL's
text handling turned on whether a schema can state a normalisation or
text-identity constraint. It cannot, after this document, and the evidence is
stronger than absence:

- `normaliz`, `normalis`, `NFC`, `NFD`, `NFKC`, `NFKD` occur **zero** times in
  the source. So do `canonical`, `identity`, `hash` and `digest` — a document
  defining eight injective text forms never calls one canonical.
- None of the 14 takes a text target and imposes a predicate about the text's
  own form *as text*. The only text-identity property any of them imposes is
  UTF-8 validity, in §3.1.
- §2.4 names the missing operator class and defers it: restrictions on
  serialisation variants "could be defined in future control operators".

**So the `canonical-encoding` topic's condition (6) is not a schema-layer
question at all.** `rfc-8610` recorded CDDL's silence as of 2019, from a
document not about text; this one is 2025, is *titled* for the conversion and
processing of text, had the occasion, and declined. Condition (6) is answerable
only in the encoding layer (dCBOR §2.7), by absence (RFC 9804), or by an
application rule under `R-O-05`. That also removes an argument DEC-002 option 2
could have made: **option 2 pays CDDL's costs without buying the answer.**

**What it does give us.** Eight of the fourteen pin an *injective* text form —
one text per value — but only for text that transcodes a byte string or an
integer: `.b64u`, `.b64c`, `.b45`, `.b32`, `.h32`, `.hexlc`, `.hexuc`,
`.base10`. So condition (6) is now citably answerable **for a hex digest** and
still unanswerable **for a label**. Adopted: `.hexlc` or `.hexuc` for
`ArtifactId.digest`, `.base10` for integer-valued text, and `.b64u` + `.cbor`
for the export envelope — which is §2.1's own first example and is MD-3's
"COSE as export only" written as CDDL by the CBOR WG.

**Two findings with teeth beyond the yes/no:**

- **`.join` makes text identity non-compositional.** §3.1: "The concatenation
  is performed on the sequences of bytes in the strings", and "there is no need
  for all individual byte sequences going into the concatenation to constitute
  valid text strings." An element may end mid-UTF-8 sequence, so a fortiori
  mid-combining-sequence. NFC is not closed under concatenation, so **even a
  future `.nfc` operator could not be checked element-by-element across a
  `.join`.** Our name chains are exactly that shape, so the rule we owe the ADR
  is one line: *a name chain must be normalised after joining, never per
  label.* No document of ours states it.
- **`.base10` forbids leading zeros**, so it cannot model an RFC 3339
  timestamp. After this document `Validity` has no usable text form in CDDL —
  the only other route is `.printf`, which the Limits below rule out.

## Implementations

The RFC names none. Its own validator model is §1.1's "tools along the lines of
that described in Appendix F of [RFC8610]", and §3.1's implementation note
describes a single-pass scanner with marker elements. *Searched on 2026-10-19;
no named implementation in the document.*

## Limits

- **`.printf`'s matching relation is locale-dependent, and no locale is
  fixed.** §2.3 defines matching as "the textual output of an equivalent
  C-language printf function call". C takes the decimal-point character from
  the locale, so `1.5` and `1,5` are both conforming output of one format
  string, and two conforming validators can disagree. This is the sharpest
  defect because it is *silent* — a format string looks deterministic.
- **The ban on length modifiers caps `.printf`'s integer range with no overflow
  rule.** The document's only two `MUST NOT`s forbid length modifiers, so each
  conversion carries C's default argument type. §2.2's own example reaches
  `9223372036854775807`, and a 256-bit digest has no conversion at all.
  **That rules `.printf` out for exactly our use case.**
- **`%c` is redefined away from C and the deviation is not labelled.** In C
  `%c` writes one byte and the wide form needs `%lc` — a length modifier the
  same paragraph forbids, so the redefinition is forced. A reader who knows C
  and skims takes the opposite meaning.
- **Three names are traps.** `.hex` admits **either case**, so it is *not*
  injective — 2ⁿ texts per value. Both `-sloppy` operators are non-injective by
  definition. Pick `.hexlc` or `.hexuc` by name and never `.hex`.
- **A normative dependency we cannot freely read.** The `[C]` reference is
  ISO/IEC 9899:2024, and the one free route printed in the source is **broken
  across lines 485/486 with a space in the URL as rendered**. Under `R-O-03` a
  citation we cannot read is barely better than an invention.
- **The 14 names appear in three different orders** across Tables 1, 2 and 7;
  "Table 1" is ambiguous across two documents in the sentence defining
  "sloppy"; `COSE_Sign1` is used and never defined; and the document's single
  `RECOMMENDED` sits inside an RFC v3 aside and concedes false negatives in the
  same sentence.
- **It closes none of the 44 side conditions** `rfc-8610`'s extraction
  enumerated, and adds ten more (`N-01`–`N-10`). A grammar extension that adds
  operators cannot close a grammar or type-system gap; it widens it.
- The extraction is at **pass 1 of 3** — verify and cross-check have not run,
  and nothing carries a human sign-off, so these artifacts are readable but not
  buildable-on.

## What this corrected in a completed record

`rfc-8610` is at `profile: full`, and its extraction wrote a gate saying it is
not the current state of CDDL until this record and three others are read. That
gate earned itself immediately: `rfc-8610`'s own
`schema/control-operators.derived.yaml` asserted *"All names other than the
fourteen below are Unassigned."* That sentence was **ours, not RFC 8610's**,
and it is false — RFC 9741 §1 states that RFCs had already added to the
extension point "in both an application-specific [RFC9090] and a more general
[RFC9165] way", and §4 then registers 14 more. **The registry holds at least 28
and strictly more.** The claim has been corrected in place, with the
falsification recorded rather than overwritten.

Nothing else in `rfc-8610` moved: no syntax changed, all six items of its
"What CDDL cannot express that we need" stand, and item 4 — Unicode
normalisation of labels — is *strengthened* from "absent" to "declined by the
document best placed to add it".
