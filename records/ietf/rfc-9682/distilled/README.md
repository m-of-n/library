---
record: rfc-9682
kind: index
title: "rfc-9682 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: passes 1 and 2 of 3 complete. `distillation.standard: FX-1` and NO
`profile`** — an unfinished extraction is neither `full` nor `partial` and the
gate says so. Pass 1 (extract, effort max, 2026-10-19): one agent reading only
`.cache/rfc-9682.txt`. Pass 2 (verify, effort max, 2026-10-20): an independent
agent that did not extract, which re-derived the change table from both sources
and **built the ABNF recognizer pass 1 said it had not built** — an RFC 5234
engine with ABNF's symmetric alternation, loaded with Figure 11 and with
RFC 8610's Appendix B. It confirmed the table, the three code-point counts, the
silent-disagreement claim, the three-way behaviour split, all four `hexscalar`
branches and the new dead alternative, and it **falsified five claims, each now
corrected and marked** (`record.yaml`, `distillation.passes`, the `verify`
entry). **Cross-check has not run**; nothing here has yet been read against the
sibling records by an agent that had not already read this one. No
`reviewed_by` is signed.

Source: RFC 9682, *Updates to the Concise Data Definition Language (CDDL)
Grammar*, Standards Track, November 2024, Updates: 8610. sha256
`d35602e7f784e509a5984283ea8d998adfee23f086ad0d77bd22f98c6cdea89c`,
699 lines, 28 KB.

**Read this before using anything here.** RFC 9682 carries **zero** BCP 14
keyword occurrences in 28 KB, with stripping both on and off. That is not a
thin document — it is a **grammar-correcting document**, so its normativity is
carried by **the ABNF it replaces** and by **the prose that says what it
replaces**. Its one normative appendix is two sentences of prose plus a figure,
and its force comes from one sentence in §1: "the updated collected ABNF syntax
in Figure 11 in Appendix A replaces the collected ABNF syntax in Appendix B of
[RFC8610]." All 87 requirements here are `kind: inferred`, each naming the
phrase, figure or production that carries the force.

## The headline

**RFC 9682 replaces RFC 8610 Appendix B in whole: 8 new productions, 6 with a
changed right-hand side, 41 carried over unchanged, 0 dropped.**

It **fixes** the surrogate admission in `SCHAR`/`BCHAR`/`PCHAR`/`SESC` and the
unrestricted backslash escape. It **leaves** the bare-LF `CRLF`, the two-prefix
`bsqual`, and all three of RFC 8610 Table 1's disagreements with the grammar
exactly where they were.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 77 verbatim bullets across 18 distinct locators, plus 18 reproduced blocks — every figure in the document and both aside blocks. All 75 plain bullets confirmed contiguous substrings of the whitespace-normalised source **and** confirmed by section range (both ends of every span inside the locator's own line range); all 18 blocks confirmed exact source line runs. The 2 remaining bullets are the declared-severed quotes, whose halves pass the same two checks |
| requirements | `requirements.yaml` | 87 entries, `R-0001`–`R-0087`, source order, no gaps: **0 stated, 87 inferred**, because the document has no BCP 14 keyword to state one with. `source_keyword_count` and `extracted_keyword_count` both **0**, with an 8350-character `reconciliation` giving the full **thirteen**-occurrence census of BCP-14-shaped words in the source (all lower case, each inspected — pass 2 corrected this from eight, which had omitted the five lower-case `may`) and stating what was counted instead. Every one of the 33 requirement ids the reconciliation cites was re-checked against the entry it names |
| schema | `schema/` | **4 verbatim, 3 derived.** Figure 11 entire — 55 productions, one unbroken region, source lines 482–591, per-region sha256, the RFC's three-column margin intact; the four delta figures; this document's own six quotations of the RFC 8610 text it replaces; and the declined Erratum 6543 proposal. Derived: a dedented tool-readable companion that round-trips, **the production-by-production change table**, and the status of RFC 8610's 44 side conditions. See `schema/README.md` |
| messages | `messages.yaml` | 18 constructs — 6 changed, 8 new, 4 unchanged-but-load-bearing — with parts, concrete syntax, and an `old_parser_behaviour` line for each. **`constrained_by` is omitted throughout, deliberately and stated in the file header**: with zero keyword occurrences there is no honest way to tie a construct to a requirement id, and inventing one is the failure FX-1 exists to prevent. The honest join is by section and is in `locator_join` |
| examples | `examples/` | 15 vectors `V-0001`–`V-0015`: 14 valid, 1 invalid, 0 indeterminate. **The one negative is the source's own.** Every `cddl` field verbatim by line range; all 6 multi-line blocks independently re-derived as exact source line runs; **0 span a page frame and 0 join non-adjacent ranges**, because this document has no page frames. The 6 one-line `instance` values are declared **ours** in the file's own header |
| design-notes | `design-notes.md` | what we adopt, adapt and reject for `D4`; **five named cuts against MD-3**, three of them option-neutral, one favouring option 2 and one putting option 1 on the right side of condition (6) of `DECISIONS-0001`'s standing note; and five open questions |

## Not applicable

- **protocol** — this document defines no exchange and no roles. §5 is one
  sentence, "This document has no IANA actions."; §4 says "The grammar fixes
  and updates in this document are not believed to create additional security
  considerations." and incorporates RFC 8610 §5, which the `rfc-8610` record
  cites for the same conclusion. The whole document is a grammar replacement
  plus the prose that states it. Nothing is sent, received, requested or
  answered. The **one** place a reviewer would look for a protocol is §4's
  transition paragraph, and it is answered under *state-machine* below.
- **state-machine** — no states and no transitions. §4 does say "There will be
  a period of transition from the details that the grammar in [RFC8610] handled
  in a less well-defined way, to the updated grammar defined in the present
  document", and §2 does deny forward compatibility for `\u{hex}`. **That is a
  deployment transition in the population of installed tools, not a lifecycle
  of any object this document defines.** There is no trigger, no guard and no
  transition an implementation performs: a tool is either built from Figure 11
  or it is not, and nothing in the document moves it from one to the other.
  Writing a two-state machine over "updated" and "not updated" would be
  inventing a model the source does not have. **The information is not lost**:
  the four-way compatibility matrix it would have held is in
  `schema/production-changes.derived.txt` as the `old_parser_behaviour` of each
  changed production, in `messages.yaml` under the same key, and in
  `design-notes.md` where it bears on us.

## The two quotation hazards, and what was done about them

Both were found **mechanically**, not by eye, and **neither is healed anywhere
in this record.** This document has no page frames at all — no form feed, no
running head, no `[Page n]` footer in 699 lines — so the hazards are different
from the sibling records':

1. **Two aside blocks**, source lines 162–165 and 342–362, prefix every line
   with `      |`. Normalising whitespace across one interleaves `|` into the
   text, so **no sentence spanning two of its lines is a contiguous span of
   this document.** Three requirements quote an aside, and all three
   **reproduce the `|` prefixes** in their `text` and say so in their `field`.
   `normative.md` and `schema/production-changes.derived.txt` reproduce both
   blocks as exact line runs rather than flowing them.
2. **Two end-of-line word breaks in prose.** Line 329 ends `the head-` and line
   330 begins `number`, so §3.2's sentence about `#7` cannot be quoted whole.
   Line 669 ends `copying-` and line 670 begins `and-pasting`. The two
   requirements affected (`R-0052`, `R-0084`) carry the **obligation-bearing
   half** as `text`, open their `field` with "SEVERED QUOTE." and quote the
   severed half there. A third and fourth break fall inside reference entries
   (lines 430, 432) and are declared wherever `[EDN-LITERALS]` is cited.

Nine quotations written in pass 1 failed one of these checks and were replaced
with spans that pass. They are recorded here because the failure mode is the
one this library has been bitten by: a sibling record once healed 15 such
breaks silently.

## Source defects found

Reported, never repaired. The full statements are in
`schema/README.md` and `schema/grammar-gaps-status.derived.txt`.

1. **`CRLF = %x0A / %x0D.0A` survives untouched** — a redefined RFC 5234 core
   rule admitting a bare LF, in a document titled *Updates to the CDDL Grammar*
   that lists RFC 5234 as a **normative** reference, says in §1.1 that the
   grammar "is based on ABNF, which is defined in [STD68] and [RFC7405]",
   rewrites `PCHAR` two lines above it in the same block of Figure 11 — and
   says nothing. The new `HEXDIG1` makes the camouflage one rule thicker.
2. **`hexscalar` reaches U+10FFFF while `NONASCII` stops at U+10FFFD**, so
   `\u{10FFFE}` and `\u{10FFFF}` are well-formed escapes for characters that
   cannot appear directly in any CDDL string. New with this document.
3. **The C1/DEL exclusion is lexical only.** §2.1.2 removes U+007F–U+009F from
   three rules and `hexscalar`'s `1*3HEXDIG` branch puts all of them back as
   escapes, along with the whole C0 range. The document declines the semantic
   half in its own parenthetical, so this one it chose.
4. **A `#7.<type>` whose type straddles 24..31 selects both readings of
   `head-number` at once.** The grammar permits it; §3.2 is silent.
5. **One curly quotation mark, source line 355**, inside the §3.2 aside:
   `not giving the CBOR "additional information”` opens with U+0022 and closes
   with U+201D. The only non-U+0022 quote in the file, and the *same phrase* at
   line 333 is correctly paired. A rendering defect in the exact bytes
   `content.sha256` pins, reproduced unrepaired inside `R-0057`.
6. **A byte order mark at the head of line 1** (U+FEFF, three bytes).
7. **§2 narrows the language and never says so**, while §3 carries an explicit
   backward-compatibility claim scoped to itself by its own opening words. Six
   one-line CDDL files valid under RFC 8610 and invalid under RFC 9682 are
   listed in `schema/grammar-gaps-status.derived.txt`, NEW-OBS-2.
8. **A second dead alternative in `type2`**, created here: `/ "#" DIGIT ["."
   uint]` is unreachable for `DIGIT = "7"` under prioritized choice, and under
   symmetrical ABNF `#7.n` now has two parses. The same species as RFC 8610's
   own `; preempted by above`, which this document carries forward verbatim.
9. **Appendix A drops two sentences of RFC 8610 Appendix B** rather than
   changing them — the case-sensitivity preamble and the closing note on
   prefixed byte strings — and the replacement clause's word "syntax" is the
   only thing deciding whether they survive. The second one's substance
   reappears in Appendix B.2, which declares itself **informative**, so a
   normative caveat became informative prose.

## What this record settles for `rfc-8610` — and what it does not invalidate

`rfc-8610` is at `profile: full` and both its `distilled/README.md` and its
`summary.md` carry a gate: that record "is not the current state of CDDL" until
`rfc-9165`, `rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` are read.
**This record discharges the `rfc-9682` quarter.**

**Nothing found here invalidates any claim in the `rfc-8610` artifacts.** Its
captured Appendix B is RFC 8610's own grammar and remains exactly that; this
document quotes six fragments of it, holding sixteen rule statements, and
**fifteen of the sixteen are byte-identical** to the sibling record's capture
after dedenting and stripping trailing ABNF comments. The sixteenth is Figure
9, which is an **extract and says so** — "; extracted from the ABNF in
RFC 8610:" — printing one `type2` alternative with ABNF's incremental `=/`
where RFC 8610 defines `type2` with `=` and eleven alternatives. That
alternative is present verbatim in RFC 8610; the one-alternative *statement* is
RFC 9682's framing. `schema/rfc8610-originals.abnf`'s header says so, because
pass 1's first draft of that header overclaimed and the mechanical cross-check
caught it. What changes is the **currency** of
six of its productions, and the **status** of four of its 44 side conditions:

- **G-32 (surrogates) and G-33 (unrestricted escapes) are CLOSED.**
- **G-31 is HALF-CLOSED** — the DEL asymmetry is fixed and stated; the
  CRLF/line-spanning asymmetry stands and is still unstated anywhere.
- **G-04 is AMENDED** — "at least one rule" moves from the grammar to a
  semantic constraint on a phase defined in a Work-in-Progress draft.
- **G-12 and G-28 are RESTATED or made harder to find, not closed.**
- **38 stand untouched**, including G-02, G-06, G-29, G-30, G-34 and all three
  Table 1 items (G-42, G-43, G-44).

The amendment `rfc-8610` needs is therefore **additive and a pointer, not a
correction**: its `schema/cddl.abnf` header and its
`schema/grammar-gaps.derived.txt` should say that `cddl`, `type2`, `SCHAR`,
`SESC`, `BCHAR` and `PCHAR` are superseded by RFC 9682 Figure 11, and that
G-32 and G-33 are closed there. Making that edit is maintenance on another
record and was not done from here.

## This record is still not the current state of CDDL

`rfc-9165`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` remain unread, and
this document depends on the last of them: §3.1's new semantic constraint is to
be fulfilled "after processing of all directives", a phase RFC 9682 does not
define and cites to `[CDDL-MODULES]` as "Work in Progress". **The full picture
of current CDDL needs all four Tier 2 records.** `library#39`.
