---
record: rfc-9682
kind: schema
title: "rfc-9682 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

**For this record the schema directory *is* the extraction.** RFC 9682 is a
grammar-correcting document: it carries **zero** BCP 14 keyword occurrences in
28 KB, and everything it does it does by replacing ABNF. Its one normative
appendix says so in two sentences — "This appendix is normative." and "It
provides the full ABNF from [RFC8610] as updated by the present document." So
what a reader needs from this record is the replaced grammar held exactly, the
deltas held separately, and an honest statement of what a parser built from the
old grammar now gets wrong.

Four of the seven files here, this README aside, are the source's own bytes;
three are ours. The filename carries the distinction and `bin/validate`
enforces it: a `.derived.` infix is mandatory on anything this library wrote,
and an unmarked name asserts verbatim bytes (`docs/extraction.md`, "Derived vs
verbatim — the filename carries it"). Each file repeats the claim in its own
header.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `cddl-updated.abnf` | **verbatim** | **Appendix A (Figure 11) complete** — the grammar in force, all **55** rule definitions `cddl` … `CRLF`, with the RFC's three-column margin preserved, in one unbroken region (source lines 482–591) | **everything semantic**, exactly as RFC 8610's did: it still cannot tell a type rule from a group rule, still admits `0..10.0`, still cannot express PEG ordering, cut semantics, map matching or any control operator. It also no longer carries RFC 8610 Appendix B's two prose sentences — see `production-changes.derived.txt`, *Two things Appendix A drops* |
| `updates.abnf` | **verbatim** | the four figures that **state** the change — Figure 2 (SESC and the hexchar family), Figure 4 (SCHAR, BCHAR, PCHAR, NONASCII), Figure 8 (`cddl`), Figure 10 (`type2`, `head-number`) — each with its own caption quoted | it is the delta, not the grammar. Figures 8 and 10 are captioned for "Appendices B **and C** of RFC 8610"; **Appendix C is RFC 8610's matching rules and this document reproduces none of it**, so the Appendix C half of those two updates is stated in a caption and nowhere else |
| `rfc8610-originals.abnf` | **verbatim** | RFC 9682's own quotations of the text it replaces — Figures 1, 3, 7, 9, 12, 14. This is the left-hand column of the change table, sourced from **one** document and checkable against **one** digest | **nothing here is current.** It is the superseded text. Six fragments, not RFC 8610's whole Appendix B — that is at `../../../rfc-8610/distilled/schema/cddl.abnf` |
| `errata-6543-proposal.abnf` | **verbatim** | Figure 13 — the split of the byte-string rules that **Erratum ID 6543 proposed and this document declined**, with the reason | **never in force.** Kept because the reason it was declined is the finding: routing a prefixed byte string's content through `QCHAR → WS → NL → COMMENT → PCHAR` would admit an unescaped apostrophe inside a comment inside an `h''` literal |
| `cddl-updated-dedented.derived.abnf` | derived | `cddl-updated.abnf` with the three-column margin removed and **nothing else** | it is **not** the source's bytes. Cite `cddl-updated.abnf`. It exists only because RFC 5234 reads a leading-whitespace line as a continuation, so an indented grammar collapses into one rule. The transformation round-trips and the generator asserts it |
| `production-changes.derived.txt` | derived | **the central deliverable.** Production by production: RFC 8610's right-hand side, RFC 9682's replacement, a correction/relaxation/restriction verdict, and what an 8610-era parser gets wrong. 6 changed, 8 new, 41 carried, 0 dropped. Plus both aside blocks as exact line runs and the one source defect | the verdicts and every "gets wrong" line are **ours**. The two right-hand-side columns are the source's bytes |
| `grammar-gaps-status.derived.txt` | derived | the 44 side conditions this library enumerated against RFC 8610, each asked one question: does RFC 9682 change it? **2 closed, 1 half-closed, 1 amended, 2 restated, 38 standing**, plus 3 new conditions and 2 new observations | the G-nn framing is **the rfc-8610 record's and ours**, not RFC 8610's and not RFC 9682's. It asserts nothing about CDDL that a cited section does not say |
| `README.md` | — | this file | — |

## The grammar is closed, and that was checked

All 55 rules of Figure 11 are defined and **no rule reference is dangling** —
verified mechanically against `cddl-updated-dedented.derived.abnf`, not by eye.
The eight new rules (`head-number`, `hexchar`, `non-surrogate`,
`high-surrogate`, `low-surrogate`, `hexscalar`, `HEXDIG1`, `NONASCII`) are
reachable only from the six changed ones; no pre-existing rule references any
of them.

The dedented file round-trips: re-adding three spaces to every non-blank line
reproduces source lines 482–591 byte-for-byte, and that identity is asserted by
the generator rather than claimed here.

## There are no page frames in this document

Worth stating because the sibling record's equivalent capture needed three
regions. `rfc9682.txt` carries **no form feed, no running head and no
`[Page n]` footer** anywhere in its 699 lines, so Figure 11 is one unbroken
region and nothing is omitted between its first and last line. The RFC was
published in the rfc-editor's unpaginated plain-text format.

**But the document has two other quotation hazards, and both were found
mechanically:**

1. **Two aside blocks** (source lines 162–165 and 342–362) prefix every line
   with `      |`. Normalising whitespace across one interleaves `|` into the
   text, so **no sentence spanning two of its lines is a contiguous span of
   this document.** Both blocks are reproduced as exact line runs at the foot
   of `production-changes.derived.txt`; nothing in this record flows a sentence
   out of an aside.
2. **Two end-of-line word breaks in prose.** Line 329 ends `the head-` and line
   330 begins `number`, so `head-number` is severed at that one occurrence and
   the §3.2 sentence about `#7` cannot be quoted whole. Line 669 ends
   `copying-` and line 670 begins `and-pasting`. Both are quoted as halves with
   the cut named, in `../requirements.yaml`, `../normative.md` and the two
   derived files here. **Neither break is silently healed anywhere in this
   record.**

## What the ABNF alone does not capture

Three conditions are **new with this document** and live outside the grammar
(the full statement is in `grammar-gaps-status.derived.txt`):

1. **At least one rule, after directive processing** (§3.1). The grammar used
   to enforce it; now a tool must. The phase it names is defined in
   `[CDDL-MODULES]`, which this document cites as "Work in Progress".
2. **The three ranges of a `#7` head-number** (§3.2) — 0..23 and 32..255 mean
   the simple value, 24..31 means the additional information. And, *ours*: a
   `head-number` given as `<type>` whose type straddles 24..31 selects both
   readings at once, which the document does not address.
3. **Two-stage processing of a prefixed byte string** (Appendix B.2) — `BCHAR`
   syntax first, then the whitespace and comment rules over the *result*. This
   is what makes `h'43424F52 ; comment'` work, and it is stated **only** in an
   appendix whose opening line is "This appendix is informative."

## Source defects found

Reported, never repaired.

1. **`CRLF = %x0A / %x0D.0A` survives untouched** — a redefined RFC 5234 core
   rule admitting a bare LF, in a document titled *Updates to the CDDL Grammar*
   that lists RFC 5234 as a normative reference, rewrites `PCHAR` two lines
   above it in the same block, and says nothing. The new `HEXDIG1` makes the
   camouflage one rule thicker: the block now holds six rules that look like
   restatements of RFC 5234 core rules and one that is not.
2. **`hexscalar` reaches U+10FFFF while `NONASCII` stops at U+10FFFD.** So
   `\u{10FFFE}` and `\u{10FFFF}` are well-formed escapes for characters that
   cannot appear directly in any CDDL string. The inconsistency is new with
   this document and no sentence addresses it.
3. **The C1/DEL exclusion is lexical only.** §2.1.2 removes U+007F–U+009F from
   `SCHAR`, `BCHAR` and `PCHAR`, and `hexscalar`'s `1*3HEXDIG` branch puts all
   of them straight back as `\u{7F}` … `\u{9F}`, along with the whole C0 range.
   The document declines the semantic half in its own parenthetical, so this is
   a gap it chose rather than missed — but a tool that wants the exclusion to
   mean anything must check twice.
4. **One curly quotation mark, at source line 355**, inside the §3.2 aside:
   `not giving the CBOR "additional information”` opens with U+0022 and closes
   with U+201D. It is the only non-U+0022 quote in the file, and the *same
   phrase* at line 333 is correctly paired. A rendering defect in the exact
   bytes `content.sha256` pins, recorded because quoting line 355 reproduces
   it.
5. **A byte order mark at the head of line 1** (U+FEFF). Same character: a
   tool reading `rfc9682.txt` as ASCII sees three stray bytes before `Internet
   Engineering Task Force`.
6. **§2 narrows the language and never says so**, while §3 carries an explicit
   backward-compatibility claim scoped to itself. Six one-line CDDL files that
   are valid under RFC 8610 and invalid under RFC 9682 are listed in
   `grammar-gaps-status.derived.txt`, NEW-OBS-2.
7. **A second dead alternative in `type2`**, created here: `/ "#" DIGIT ["."
   uint]` is unreachable for `DIGIT = "7"` under prioritized choice, and under
   symmetrical ABNF `#7.n` now has two parses. Harmless in effect; the same
   species as RFC 8610's own `; preempted by above`.

## What this record settles for the rfc-8610 record

`rfc-8610`'s `distilled/README.md` and `summary.md` both carry a gate: that
record "is not the current state of CDDL" until `rfc-9165`, `rfc-9682`,
`rfc-9741` and `draft-ietf-cbor-cddl-modules` are read. This record discharges
the `rfc-9682` quarter of it, and **nothing found here invalidates any claim in
the `rfc-8610` artifacts** — its captured Appendix B is RFC 8610's grammar and
remains exactly that. What changes is the *currency* of six of its productions.

The one amendment the `rfc-8610` record needs is additive and is a pointer, not
a correction: its `cddl.abnf` header and its `grammar-gaps.derived.txt` should
say that `SCHAR`, `BCHAR`, `PCHAR`, `SESC`, `cddl` and `type2` are **superseded
by RFC 9682 Figure 11**, and that G-32 and G-33 are closed there. The precise
list is in `production-changes.derived.txt`. Making that edit is maintenance on
another record and is not done from here.
