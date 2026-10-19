---
record: rfc-8610
kind: schema
title: "rfc-8610 — schemas"
extracted: "2026-10-18"
reviewed_by: ""
---

# Schemas

**For this record the schema directory is the extraction, not a side artifact.**
RFC 8610 carries **two** BCP 14 keyword occurrences in 125 KB, and one of those
is a quotation of RFC 7071. Its normative content is a **grammar and a type
system**, so what a reader needs from this record is the grammar held exactly
and the type system's side conditions held honestly. Eight of the eleven files
here, this README aside, are the source's own bytes; three are ours.

The filename carries the distinction and `bin/validate` enforces it: a
`.derived.` infix is mandatory on anything this library wrote, and an unmarked
name asserts verbatim bytes (`docs/extraction.md`, "Derived vs verbatim — the
filename carries it"). Each file repeats the claim in its own header.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `cddl.abnf` | **verbatim** | **Appendix B (Figure 13) complete** — the formal definition of CDDL's syntax, all 47 productions `cddl` … `CRLF`, with the RFC's five-column page margin preserved, in three BEGIN/END regions split at the two page frames | **everything semantic.** It cannot tell a type rule from a group rule, admits `0..10.0` (which §2.2.2.1 calls NOT DEFINED), cannot express PEG ordering, cut semantics, map matching, or any control operator's target/controller rules. Also, per the appendix's own closing note, it "does not attempt to reflect the detailed rules of what can be in a prefixed byte string" |
| `prelude.cddl` | **verbatim** | **Appendix D (Figure 14) complete** — all 40 rules of the standard prelude, `any` … `undefined`, in two regions split at the page frame | nothing is added or resolved. The prelude is **fixed**: tags registered after RFC 7049 must be defined in each file that uses them, and there is deliberately no `string` |
| `prelude-json-subset.cddl` | **verbatim** | Appendix E (Figure 15) — the 18 prelude rules that survive in the JSON data model | it is a **subset statement**, not a replacement prelude; the major-type notation it keeps "do[es] not have a direct meaning in JSON" |
| `ijson-types.cddl` | **verbatim** | Appendix E (Figure 16) — the three I-JSON-safe integer range types | **not part of the prelude** (the source says so outright); they must be copied into any specification that wants them |
| `reputon-verbose.cddl` | **verbatim** | Appendix H — the worked RFC 7071 reputon schema, 15 rules, in two regions split at the page frame | **informative.** Appendix H declares itself "for information only"; it describes an RFC 7071 JSON structure, nothing of ours |
| `reputon-compact.cddl` | **verbatim** | Appendix H — the equivalent compact form, 2 rules | informative; redefines the same rule names as the verbose form, which is why the two are separate files |
| `operator-precedence.txt` | **verbatim** | §3.11 Table 1 — 17 operator rows with arity and precedence 1–8 | it is explicitly a **summary**; §3.11 says precedence is "defined in Appendix B and summarized in Table 1". Three places where it disagrees with the grammar are recorded below |
| `peg-mapping.txt` | **verbatim** | Appendix A — the CDDL → PEG construct mapping, 8 rows | it maps notation, not semantics; the literal notation, brackets, braces, tildes, ampersands and hash marks "are specific to CDDL and unrelated to the conventional PEG notation" |
| `cddl-dedented.derived.abnf` | derived | `cddl.abnf` with the five-column margin removed and the two page frames replaced by one blank line each — **nothing else** | it is **not** the source's bytes. Cite `cddl.abnf`. It exists only because an indented ABNF file collapses into a single rule under RFC 5234 and no tool can read it |
| `control-operators.derived.yaml` | derived | all **14** control operators as data: target, controller, matching predicate, IANA registry status and policy, per-operator gaps. Every `quote:` field is the source's own wording | the predicates are **our rendering of prose**. RFC 8610 ships no formal semantics for any operator and no machine-readable operator table |
| `grammar-gaps.derived.txt` | derived | **44 enumerated side conditions** (G-01…G-44) a conforming tool must carry beyond the grammar, each with a locator and a static/instance/not-checkable verdict | it is a list, not an implementation; and the verdicts are ours. It asserts nothing about CDDL that the cited section does not say |
| `README.md` | — | this file | — |

## What the ABNF alone does not capture

`cddl.abnf` is the complete formal definition of CDDL's **syntax**. It is not a
definition of CDDL, and the document is candid about it: Appendices A, C and D
are each marked "This appendix is normative", and together they carry as much
of the language as Appendix B does. **The grammar accepts strings the type
system rejects.** The canonical case is the source's own:

```
BAD-range1 = 0..10.0 ; NOT DEFINED
BAD-range2 = 0.0..10 ; NOT DEFINED
```

Both parse against `type1 = type2 [S (rangeop / ctlop) S type2]`. §2.2.2.1
nonetheless states that ranges exist only "between integers … or between
floating-point values", and the document says nothing about what a tool should
do when it meets one. The full enumeration is `grammar-gaps.derived.txt`; the
six classes are:

1. **Type versus group is not a syntactic question.** `a = b` defines a type if
   `b` is a type and a group if `b` is a group, and the determination "may need
   to span several levels of rule definitions". The grammar's own `grpent`
   carries the comment `; preempted by above`, conceding that one of its three
   alternatives is unreachable.
2. **Per-operator side conditions.** `ctlop = "." id` would accept `.nonsense`;
   `~` is admitted before any typename though it requires a map, array or tag;
   `&` before any group though it requires one whose entries have values;
   `.lt`/`.le`/`.gt`/`.ge` are numeric-only. None of this is in the grammar.
3. **PEG, not BNF.** `/` and `//` are *prioritized*. ABNF notation cannot say
   so; Appendix A explains that this grammar was *written* so both readings
   coincide — a property of the authoring, not of the notation. Occurrence
   indicators are greedy, so `*a a` can never match.
4. **Maps are not matched by the PEG algorithm at all.** "For each candidate
   name/value pair that the PEG algorithm would try, a matching member is
   picked out of the entire map." Which member gets picked can be
   indeterminate, and the document resolves its one real ambiguity by *urging
   authors not to trigger it*: "the specification writer is simply urged to not
   write pathologically non-deterministic specifications."
5. **Conventions that read as rules.** Socket/plug (`$`, `$$`), the rule that
   plugs "must be augmentations", naming style, and the advice to parenthesise
   rather than rely on precedence are all explicitly conventions. `id` treats
   `$` like any other character.
6. **CDDL constrains the data model, never the encoding.** `#7.25` "specifies
   the set of values that can be represented as half-precision floats; it does
   not mandate that these values also do have to be serialized as
   half-precision floats: CDDL does not provide any language means to restrict
   the choice of serialization variants." Nor does it say anything about
   definite versus indefinite length, or about key order.

## Defects and internal inconsistencies, recorded not repaired

Reported here because `docs/extraction.md` forbids repairing them in a verbatim
file. Full detail and locators in `grammar-gaps.derived.txt`.

- **`CRLF` is redefined.** `CRLF = %x0A / %x0D.0A` admits a bare LF; RFC 5234's
  own `CRLF` is `%x0D %x0A`. `ALPHA`, `DIGIT`, `HEXDIG` and `SP` are redefined
  *identically* to RFC 5234, so a reader may reasonably take the whole block as
  a restatement of the core rules — and then get `CRLF` wrong. (G-29)
- **The surrogate range is admitted.** `SCHAR`, `BCHAR`, `PCHAR` and `SESC` all
  span `%x80-10FFFD`, which includes U+D800–U+DFFF — not Unicode scalar values,
  and not encodable in the UTF-8 that §3.1 mandates. (G-32)
- **`SCHAR` and `BCHAR` are not parallel.** U+007F is excluded from text strings
  and admitted in byte strings; `BCHAR` includes `CRLF` and `SCHAR` does not, so
  a byte string literal may span lines and a text string literal may not. We
  found neither stated anywhere in the document. (G-31)
- **There is no horizontal tab in CDDL,** anywhere, including inside text
  strings — `SP = %x20` and `SCHAR` begins at `%x20`. No sentence says so. (G-30)
- **`COMMENT` requires a line terminator,** so a comment on the final line of a
  file with no trailing newline does not parse. (G-34)
- **`SESC` is wider than RFC 8259 §7,** which §3.1 nonetheless invokes: a
  backslash before any printable character is grammatical, and `\u` is not
  required to carry four hex digits. (G-33)
- **Table 1 disagrees with the grammar three times:** it lists `,` as a binary
  operator although `optcom` makes it decoration (Appendix A: "comma is
  decoration only"); it omits the cut `^` entirely; and it gives `..`, `...`
  and `.ctrl` a precedence although `type1` admits at most one of them, so they
  cannot compose — which is why §3.8.6 must write `(number .gt 0) .default 1`.
  (G-42, G-43, G-44)
- **"Additional information" is used loosely for tags.** §2.2.3 and Appendix C
  both describe the number after the dot as additional information, which is
  right for `#7.25` and wrong for `#6.55799`, where it is a tag number.
- **Appendix H's generated instance does not satisfy its own schema** on a
  strict reading: `rating: float16` against `"rating": 0.34133473256800795`,
  which is not representable in binary16. Recorded as `rfc-8610#V-0098`.

## Not held here

The §6.1 IANA "CDDL Control Operators" registry table is captured as data in
`control-operators.derived.yaml` (`iana_initial_entry` plus the registration
policy) rather than copied verbatim. The library has records for the IANA CBOR
tags and simple-values registries (`records/iso/iana-cbor-tags`,
`records/iso/iana-cbor-simple-values`) but none for this one; if that record is
ever created, the verbatim table belongs there, not here.

## State

**Pass 1 (extract) only.** Every verbatim region in this directory was verified
byte-for-byte against the cached source by line range, by script, twice — once
by the generator and once by an independent `sed`-based re-extraction and
`diff`. The four derived files have **not** been adversarially re-derived, and
nothing here has been run through a real RFC 8610 parser; none is installed in
this environment.
