---
record: rfc-9682
kind: examples
title: "rfc-9682 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` — **15 vectors, `rfc-9682#V-0001` … `rfc-9682#V-0015`, in source
order with no gaps.** 14 `valid`, 1 `invalid`, 0 `indeterminate`. **The single
negative is the source's own; no negative here is invented.**

RFC 9682 is a grammar-correcting document, so almost every example in it is
CDDL *text*. The exception is the one that matters most: **Figure 6 is the only
byte-level output the document prints**, and it is the document's own
acceptance criterion for §2 — three spellings of one 19-byte text string and
three of one 19-byte byte string, all resolving to
`446f6d696e6f277320f09f81b3202b20e28c98`.

## How a vector is built

- **`cddl`** — **always verbatim**, lifted from the cached source **by line
  range, by script, never retyped.** The only transformation is removal of the
  common left margin (which a YAML block scalar performs in any case) and
  re-indentation for YAML; relative indentation, the source's own comments, its
  blank lines and the alignment of its trailing comment column are the
  source's. 6 are multi-line blocks, 9 are single source lines, and 1
  (`V-0012`, `#7.25`) is a fragment quoted from running prose.
- **`instance`** — **mixed, and `vectors.yaml`'s own header declares which is
  which.** `V-0002`'s is Figure 6 entire, verbatim. **The six one-line
  `instance` values of `V-0003`…`V-0008` are OURS**: each composes Figure 6's
  two columns into one line, taking the CBOR head from the source's comment
  column (`# text(19)`, `# bytes(19)`) and the payload from its hex column.
  Every byte in them is the source's; the *line* is not. `V-0012`'s is a
  two-word fragment of §3.2's prose.
- **`matches`** — always **ours**: a reading, never a quotation.
- **`expect`** — against **the grammar in force**, Figure 11, i.e.
  `../schema/cddl-updated.abnf`. Where a vector's status under RFC 8610's
  grammar differs, its `notes` says so and marks the reading ours.
- **`notes`** — mixed inline: double-quoted spans are the source's own words
  and contiguous verbatim; anything marked OURS is this library's reading.

## No page frames, no joins, no repairs

`rfc9682.txt` carries **no form feed, no running head and no `[Page n]` footer**
anywhere in its 699 lines, so **every block below is a single unbroken source
line run.** None joins two non-adjacent ranges, none spans a page frame, and
none needed repair. `vectors.yaml` carries the complete audit trail under
`source_ranges` — 14 ranges, in the order the generator lifted them — and a
`counts` block that states all four zeros explicitly. An independent checker
re-derived all 6 multi-line blocks from the cache and confirmed each as a
dedented exact source line run.

## The two silent-divergence vectors are the point of this set

`V-0003` (rule `a`) and `V-0004` (rule `b`) are not merely examples of the new
escape syntax. **Both parse under RFC 8610's grammar as well, and mean something
else.** RFC 8610's `SESC = "\" (%x20-7E / %x80-10FFFD)` consumes `\u`, after
which `{`, `6`, `f`, `}` are each ordinary `SCHAR`s — U+007B and U+007D lie in
`%x5D-7E`, `6` in `%x23-5B`, `f` in `%x5D-7E` — so `"D\u{6f}mino"` is a nine-
character string beginning `D`, `u`, `{`, `6`, `f`, `}` under the old grammar
and `Domino` under the new one. **No diagnostic is produced on either side.**
`"🁳"` diverges the same way.

That is the concrete instance of the class §4 names and does not name:
"Attackers may want to exploit such potential confusion by crafting CDDL models
that are interpreted differently by different parts of a system." The worked
derivation is in `../schema/production-changes.derived.txt` under `SESC`.

## The one negative, and why it is `invalid` rather than `indeterminate`

`V-0013` is Appendix B.1's `foo = h'…'` fragment with **unescaped** apostrophes
inside its comments. The source's words are "This allows any non-C0 character in
a comment, so this fragment becomes possible" — and *becomes possible* is under
**Figure 13, the proposal this document declined**, where a prefixed byte
string's content runs `QCHAR → WS → NL → COMMENT → PCHAR` and `PCHAR` admits an
apostrophe.

`expect: invalid` is **ours**, and it is decidable rather than arguable: U+0027
appears in no `BCHAR` alternative — the ranges are `%x20-26` and `%x28-5B`,
which skip it — so the first bare apostrophe terminates the literal. It was
invalid under RFC 8610 for exactly the same reason. `V-0014`, the escaped form,
is valid under **both** grammars, and the source says so for the old one:
"... which would be supported by the existing ABNF in [RFC8610]."

**`V-0014` is also the only vector that exercises the two-stage model.** Its
comments are not comments at the syntax stage — every character is a `BCHAR`
and the newlines are `BCHAR`'s `CRLF` — and become comments only at the
semantic step Appendix B.2 describes. That appendix is informative.

## What is NOT in this set, and why

- **Figure 11 itself.** It is a grammar, not an example;
  `../schema/cddl-updated.abnf` holds it byte-exact.
- **Figures 1, 3, 7, 9, 12 and 14** — RFC 8610's superseded grammar, quoted by
  this document. Not examples of anything current;
  `../schema/rfc8610-originals.abnf`.
- **Figure 13** — the declined proposal's grammar;
  `../schema/errata-6543-proposal.abnf`. Its *consequence* is `V-0013`.
- **`QCHAR`.** Never in force. Deliberately absent, and `../messages.yaml`
  records the absence under `not_constructs` so that nobody reads it as CDDL.
- **Any vector we invented to probe the new grammar.** There are none. The
  nearest thing is `V-0015`, which is Figure 2's three `SESC` lines with the
  document's own comment column (`; \" \/ \\`, `; \b \f \n \r \t`, `; \uXXXX`)
  — the source's escape table, not ours. Probing cases that the document does
  not print — `\u{0}`, `\u{10FFFF}`, `\u{D800}`, `\u{110000}` — are argued in
  `../schema/grammar-gaps-status.derived.txt` with the branch of the grammar
  that decides each, and are **not** dressed up as vectors here.

## Running these against the grammar

Nothing in this record executes. The dedented companion
`../schema/cddl-updated-dedented.derived.abnf` exists so that a future pass can
load Figure 11 into an ABNF recognizer and run `V-0001`…`V-0015` against it, as
the `rfc-8610` record's cross-check pass did for RFC 8610's Appendix B. **That
has not been done here.** Pass 1 asserts the expectations from the grammar by
hand, branch by branch, and says so.
