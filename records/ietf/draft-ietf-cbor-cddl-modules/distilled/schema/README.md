---
record: draft-ietf-cbor-cddl-modules
kind: schema
title: "draft-ietf-cbor-cddl-modules — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

**For this record the grammar *is* the specification.** `bin/bcp14-count`
reports **0** BCP 14 keyword occurrences in 26 KB. Appendix A's ten ABNF
productions and a handful of definitional sentences in §2.1–§2.6 are the whole
of the normative content, so what a reader needs from this directory is the
grammar held exactly, and the side conditions it cannot express held honestly.

**One** of the five files here is the source's own bytes; **four** are ours. The
filename carries the distinction and `bin/validate` enforces it: a `.derived.`
infix is mandatory on anything this library wrote, and an unmarked name asserts
verbatim bytes (`docs/extraction.md`, *Derived vs verbatim — the filename
carries it*). Each file repeats the claim in its own header.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `module-directives.abnf` | **verbatim** | **Appendix A complete** — all ten productions `directive` … `CRLF`, source lines 677–688, one unbroken region with the Internet-Draft's three-column margin preserved. Region sha256 `43c17148af31265a171f2e722b24d2e0063d0ab253d8b681cc1c223d5df696ab` | **everything semantic, and more besides.** It is a grammar of the **directive line only** — it says nothing about what `include` and `import` *draw in*, nothing about prefixing, nothing about the prelude exemption, nothing about emission order, and nothing about CDDL itself (the CDDL in a module file is basic CDDL and is RFC 8610's grammar's business). Three of its ten productions do not hold as written: see `grammar-gaps.derived.txt` G-01, G-02, G-03 |
| `module-directives-dedented.derived.abnf` | derived | the same ten productions with the three-column margin removed and **nothing else** changed — round-trip checked in both directions | it is **not** the source's bytes. Cite `module-directives.abnf`. It exists only because RFC 5234 reads an indented line as a continuation, so the margin-bearing capture collapses into one `directive` rule and no ABNF tool can read it. Same reason as `rfc-8610`'s `cddl-dedented.derived.abnf` |
| `grammar-gaps.derived.txt` | derived | **21 enumerated items G-01…G-21** — the side conditions, under-specifications and internal disagreements a conforming implementation must carry beyond the grammar, each with a locator, a requirement id and a static / instance / not-checkable verdict. Tally: **S 10, I 1, N 8**, plus 2 recorded as *not* defects so nobody "fixes" them | it is a list, not an implementation, and the verdicts are ours. It asserts nothing about the document that the cited requirement does not say |
| `name-resolution.derived.yaml` | derived | how a module is **named** and how the name is **resolved**, as data: the `filename` character set, the absence of a path separator, the absence of principal / version / digest / URI, the explicit refusal of URIs, the `CDDL_INCLUDE_PATH` mechanism and its `.:` default, the `as`-clause prefixing model, and the producer-side / consumer-side selection table | every `quote` is the document's; every `ours_note` is this library's reading and says so. The whole file is scoped to §2.2, §2.4, §4 and Appendix A; it is not a resolution algorithm and the document does not contain one |
| `cose-closure-unfolded.derived.cddl` | derived | the **two** composed outputs that carry an RFC 8792 `\` wrap (§2.6, source lines 420–435 and 455–471), with the wrap undone so they are usable CDDL | not the document's text — `examples/vectors.yaml` V-0011 and V-0013 carry the source's own folded bytes. And **not a COSE schema**: these are the document's illustrations of what `import … from rfc9052 as cose` emits, drawn from the `cddlc` tool's bundled extract of RFC 9052 rather than from RFC 9052 itself |
| `README.md` | — | this file | — |

## What the grammar alone does not capture

`module-directives.abnf` is the complete formal definition of the **directive
line**. It is not a definition of the module structure, and the gap is wider
here than the corresponding gap in RFC 8610. Everything that makes the
mechanism *do* something is prose:

- **what `include` draws in** — `R-0046`, and it is transitive *through* the
  module into what that module itself imported;
- **what `import` draws in** — `R-0047`, `R-0060`, reachability from the
  consumer plus transitive closure;
- **that an explicit `include … from` is *not* transitive** — `R-0056`, so one
  keyword has two closure behaviours depending on whether a `from` clause is
  present;
- **what the `as` clause does to a name** — `R-0028`, textual prefixing;
- **that the RFC 8610 prelude is exempt from prefixing** — `R-0053`, a side
  condition requiring 40 names from another document as data;
- **that writing a selector without its prefix also emits an unprefixed
  alias** — `R-0064`, and that one is shown by example rather than stated
  (`grammar-gaps.derived.txt` G-21).

`grammar-gaps.derived.txt` holds all 21 of these and the eleven questions the
document leaves open.

## Defects in the grammar, reported and not repaired

All three are recorded in `../README.md`'s defect list as well, because they
are the ones a reader is most likely to trip over.

1. **`id` cannot match the document's own dotted selectors.** `id` admits
   neither `-` nor `.`, where RFC 8610's `id` admits both. Two of the seven
   directive instances the document prints — source lines 388 and 414, carrying
   three dotted selectors — are therefore not derivable from `directive`.
   G-01.
2. **`CRLF` is redefined against its own metalanguage, and the redefinition is
   undeclared.** Appendix A declares STD 68, whose core rule is `CRLF = CR LF`;
   the appendix redefines it as `%x0A / %x0D.0A`, admitting a bare LF. **The
   substance of that is not an error** — RFC 9165 §3 makes the byte-identical
   redefinition, *declares* it and calls it "customary for ABNF"
   (`rfc-9165#R-0053`), so relaxing ABNF's own newline is deliberate community
   practice. What is defective here is only that it is **undeclared**: a
   documentation gap, not a grammar one. The same gap as `rfc-8610` defect 7 as
   that record now frames it — camouflaged there by four core rules redefined
   *identically* in the same block, whereas here `SP` is the only other core
   rule touched and it keeps its value, so the one conflicting redefinition
   stands alone and still unremarked. G-02.
3. **The prose and the grammar disagree on what makes a line a directive.**
   §2.3 requires only that the line "start with the prefix ;#"; `directive`
   requires whitespace after it. A line beginning `;#` that is *not* a
   grammatical directive — a section banner, another convention's annotation —
   is a directive under the prose and ungrammatical under the appendix, and
   nothing says whether a processor then errors or falls back to reading the
   comment it also is. G-03.

## What the composed outputs show that the prose does not

Checked against the document alone: **not one of the seven composed outputs it
prints contains a single `;` character.** Across the display-block span that
holds every example — source lines **309–519** — the only semicolons are the
`;#` of the seven *input* directives. (That line range is given because it is
exact: §2.5's prose carries one more semicolon at line 296, outside any
example.) Because directives
*are* comments (`R-0023`, `R-0032`), that means the transformation is
**one-way** — a composed model cannot be read back as the module structure that
produced it — and that every comment in every input module is discarded.

The cross-document half of this rests on another record, and is attributed
rather than asserted from this source: the RFC 9052 fragments those outputs are
drawn from *do* carry per-field comments (`; kty`, `; kid`, `; alg`,
`; criticality`, `; content type`, `; key identifier`, `; IV`, `; Partial IV`),
per this library's verbatim capture at
`records/ietf/rfc-9052/distilled/schema/cose.cddl` — in its `COSE_Key` and
`Generic_Headers` fragments, found under that file's own markers
`; §7 Key Objects -- COSE_Key` and
`; §3.1 Common COSE Header Parameters -- Generic_Headers`. *[correction
2026-10-20, cross-check pass: this cited "lines 60–67 and 168–175" of that
file. The ranges are still right, but a cross-record citation by line number is
the drift pass 2 had to repair in `grammar-gaps.derived.txt` G-01; productions
are stable and line numbers are not.]* The
document's rendering also drops the redundant inner parentheses of RFC 9052's
`? 4 => [+ (tstr / int) ]`, normalises the indentation from four columns to two
and adds a trailing comma after the last member. **None of those changes the
language** — under RFC 8610 an occurrence indicator binds the whole following
`type`, so `[+ tstr / int]` and `[+ (tstr / int)]` denote the same thing, and a
trailing comma is admitted by `optcom`. What is lost is the documentation, and
for `rfc-8610`'s finding that four of `ARCH-0002` P3's five rows have nowhere
to live but comments, losing the documentation is the cost. See
`../design-notes.md`.
