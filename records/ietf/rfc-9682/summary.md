---
schema: "library-summary/v1"
id: rfc-9682
record: rfc-9682
type: summary
updated: "2026-10-20"
---

# Updates to the Concise Data Definition Language (CDDL) Grammar

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track, **Updates: 8610** |
| **Authors** | C. Bormann (Universität Bremen TZI) |
| **Published** | November 2024 |
| **Identifier** | RFC 9682 · DOI 10.17487/RFC9682 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9682.txt |
| **Digest** | `d35602e7f784e509a5984283ea8d998adfee23f086ad0d77bd22f98c6cdea89c` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

RFC 9682 replaces RFC 8610's Appendix B grammar. It is the reason this
library's `rfc-8610` record, though at `profile: full`, is **not** the current
state of CDDL — and reading it is what lifts that gate for the grammar.

The change, derived production by production: **47 rule definitions become 55 —
8 new, 6 with a changed right-hand side, 41 carried over unchanged, none
dropped.** The six that changed:

| production | RFC 8610 | RFC 9682 | verdict |
|---|---|---|---|
| `cddl` | `S 1*(rule S)` | `S *(rule S)` | relaxation — an empty or comment-only file is now CDDL |
| `type2` | `#6 ["." uint]` | `["." head-number]`, plus a new `#7 ["." head-number]` | relaxation |
| `SCHAR` | `… %x80-10FFFD` | `… NONASCII` | restriction + correction |
| `SESC` | `"\" (%x20-7E / %x80-10FFFD)` | eight named escapes plus `\u{hex}` | **restriction *and* relaxation** |
| `BCHAR` | `… %x5D-10FFFD` | `… %x5D-7E / NONASCII / "\'"` | restriction + correction |
| `PCHAR` | `%x20-7E / %x80-10FFFD` | `%x20-7E / NONASCII` | restriction + correction |

The eight new rules — `head-number`, `hexchar`, `non-surrogate`,
`high-surrogate`, `low-surrogate`, `hexscalar`, `HEXDIG1`, `NONASCII` — are all
reachable only from those six. Closure checked: all 55 defined, no dangling
reference.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | It supersedes the grammar every CDDL-writing record in this library leans on. |
| Naming | supporting | The new escape syntax multiplies the spellings of a text label, which lands on the text-identity question. |

**The hazard is that one change disagrees silently rather than failing.**
`"D\u{6f}mino"` **parses under both grammars, with different meanings, and
produces no diagnostic on either side**: RFC 8610's `SESC` consumes a backslash
plus one character, after which `{`, `6`, `f` and `}` are each ordinary
`SCHAR`s. RFC 9682 reads the same text as the escape for U+006F. Verified
mechanically against both productions, and held as vectors in this record. The
document names this class of problem in §4 and never names an instance.

The other two directions are safe by comparison. An 8610-era parser
**over-rejects** — loudly — on empty files, `#6.<n>(t)` and `#7.<n>`; and it
**over-accepts** raw C1 controls and surrogates in text strings, byte strings
and *comments*, DEL in byte strings, and every escape outside the eight.

**Two of the 44 side conditions `rfc-8610`'s extraction enumerated are closed
here.** G-32: surrogates are excluded from all four character rules via
`NONASCII = %xA0-D7FF / %xE000-10FFFD`, stated deliberately and credited in the
Acknowledgments — **and the escape path is closed too**, since a lone surrogate
is unreachable through `hexscalar`. G-33: escapes are now an exhaustive set.
G-31 is half-closed, G-04 amended rather than fixed, and the other 38 stand.

## Implementations

The RFC names none. Its own evidence of practice is §2's claim to "mirror the
way existing implementations have dealt with the errata reports" — a claim
about tools, not about the language, and one this record flags as doing work §3
does not. *Searched on 2026-10-19; no named implementation in the document.*

## Limits

- **The bare-LF `CRLF` survives untouched.** `CRLF = %x0A / %x0D.0A` is carried
  into the normative appendix **byte-identical**, in a document titled *Updates
  to the CDDL Grammar* which lists RFC 5234 as a normative reference and
  **rewrites `PCHAR` two lines above it in the same block**. It says nothing.
  The new `HEXDIG1` makes the camouflage one rule thicker. **The charge is that
  the relaxation is *undeclared*, not that it is wrong.** RFC 9165 §3 makes the
  identical redefinition and declares and scopes it — [PROVENANCE: RFC 9165's
  sentence, not RFC 9682's] "As is customary for ABNF, the syntax of ABNF itself
  (_not_ the syntax expressed in ABNF!) is relaxed to allow a single line feed
  as a newline" — so the substance is deliberate community practice and that
  instance is no defect. Counting **undeclared** instances, the current ones are
  **two**: this document's own normative Appendix A, which supersedes RFC 8610's
  copy, and `draft-ietf-cbor-cddl-modules`, whose directive grammar reproduces
  the rule with no declaration anywhere in the draft. *(Adjudicated by pass 2
  from the three sources; an earlier draft of this line said "three current CDDL
  documents", which counted the superseded copy and did not separate the
  declared instance from the undeclared ones.)*
- **`bsqual = "h" / "b64"` is unchanged at two prefixes.** Appendix B.2 says
  only that "the approach taken lends support to extending bsqual in CDDL
  similar to the way this is done for CBOR diagnostic notation in
  [EDN-LITERALS]". **Support lent, not taken** — which is what
  `draft-ietf-cbor-edn-literals`'s record independently reported.
- **None of RFC 8610 Table 1's three disagreements with the grammar is
  resolved, and this document cannot resolve them**: its scope is Appendix B,
  and Table 1 is in §3.11. The cut `^` survives in `memberkey`.
- **A new inconsistency, created here:** `hexscalar` reaches U+10FFFF while
  `NONASCII` stops at U+10FFFD, so `\u{10FFFE}` and `\u{10FFFF}` escape
  characters that cannot appear directly.
- **The C1/DEL exclusion is lexical only**, and the document chose that:
  `hexscalar`'s `1*3HEXDIG` puts `\u{0}`…`\u{1F}` and `\u{7F}`…`\u{9F}` straight
  back, and `\u{9}` makes a tab expressible in a text string for the first time.
- **A second dead alternative is introduced.** Figure 11 places
  `/ "#" "7" ["." head-number]` before `/ "#" DIGIT ["." uint]`, so under
  prioritized choice the older alternative is unreachable for `DIGIT = "7"`;
  read as plain ABNF, `#7.n` now has two parses.
- **§2 narrows the language and never says so.** §3's backward-compatibility
  claim is scoped to §3 by its own opening words, and §2 claims only to mirror
  implementations. Six one-line CDDL files valid under RFC 8610 and invalid
  under RFC 9682 are listed in
  `distilled/schema/grammar-gaps-status.derived.txt`, NEW-OBS-2.
- **Appendix A *drops* two sentences of RFC 8610 Appendix B** rather than
  changing them, and the second's substance reappears in Appendix B.2 — which
  declares itself informative. A normative caveat became informative prose.
- Smaller: one curly closing quotation mark at line 355 where the same phrase
  is correctly paired at line 333; a byte order mark at the head of line 1.
- The extraction is at **passes 1 and 2 of 3**; cross-check has not run. Pass 2
  **built the recognizer pass 1 lacked** — an RFC 5234 engine with ABNF's
  symmetric alternation, loaded with Figure 11 and with RFC 8610's Appendix B —
  and re-derived the change table from both sources independently. It confirmed
  the table, the three code-point counts, the silent disagreement, the
  behaviour split, all four `hexscalar` branches and the dead alternative, and
  every one of the 15 vectors' `expect` verdicts. It **falsified five claims**, each now
  corrected and marked in place; the sharpest was that four artifacts stated
  this record's own central hazard with the escape `\uD83C\uDC73` silently
  resolved into the character it denotes, which is the very failure the hazard
  describes. Readable and now checked; still not cross-checked against the
  sibling records.

## What this changed in `rfc-8610`

Nothing was invalidated. All 16 rule statements RFC 9682 quotes from RFC 8610
were cross-checked against that record's verbatim capture: **15 byte-identical,
and the 16th correctly not**, because RFC 9682's Figure 9 is an extract of one
`type2` alternative written with ABNF's incremental `=/`.

What changed is **currency, not correctness** — so `rfc-8610`'s
`schema/cddl.abnf` has gained an additive header pointer naming the six
superseded productions, the two closed gaps, and the silent-disagreement
hazard. Its three verbatim regions remain byte-exact and its own defect list is
unchanged on `CRLF`, `bsqual` and Table 1, because RFC 9682 fixes none of them.
Pass 2 re-derived that header against both sources and **corrected its
arithmetic**: it had said "2 closed, 1 half-closed, 1 amended, the other 38
stand", which omits the **2 restated** (G-12, G-28) and sums to 42 rather than
44. It also now carries the three code-point counts and the `"\'"` alternative
`BCHAR` gains back, which the first version of the table elided.

## Where it cuts against MD-3

Five cuts are recorded in `distilled/design-notes.md`. The two sharpest:

- **Cut 1 favours DEC-002 option 2 outright.** §3.2 — this document's principal
  new capability, ranging over tag numbers via `head-number` — exists to serve
  **registered** tags, with RFC 9277's range as the motivating case. Option 5's
  registry abstention makes it dead weight; option 2 would use it. A cost
  option 5 pays that option 2 does not.
- **Cut 5 puts option 1 on the right side of condition (6).** The new escape
  syntax multiplies the spellings of an ARCH-0002 P1 local label — `"café"`,
  `"caf\u{e9}"`, and `"cafe\u{301}"` as a fourth spelling of *different* bytes
  that renders identically — while RFC 8610 §3.1's "Processing of CDDL does not
  involve Unicode normalization processes" is untouched. Option 1's native
  identifiers are byte strings, which sidesteps it.

And one absence recorded so it stays visible: §5 is "This document has no IANA
actions", so this document neither helps nor hurts option 5's registry
objection. Reporting it as evidence *for* option 5 would be reading the
narrowing into the source.
