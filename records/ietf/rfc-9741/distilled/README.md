---
record: rfc-9741
kind: index
title: "rfc-9741 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: pass 1 (extract) complete. No `profile` is declared.** One agent at
effort max, reading only `.cache/rfc-9741.txt`. Pass 2 (verify) and pass 3
(cross-check) have not run, and **no `reviewed_by` is signed**. The artifact set
is complete; the claim that it is *correct* is one pass short.

Source: RFC 9741, *Concise Data Definition Language (CDDL): Additional Control
Operators for the Conversion and Processing of Text*, Standards Track, March
2025. sha256 `3234aeea39d01b7c1c8e9c70d4d7dc8745852e0b6edbea167a3e55b91e7a9ee3`,
602 lines, 28550 bytes.

## The answer this record was extracted for

**Can a CDDL schema state a Unicode normalisation or text-identity constraint
after this document? No.** The strings `normaliz`, `normalis`, `NFC`, `NFD`,
`NFKC` and `NFKD` do not occur in the source; `Unicode` occurs once, defining
`%c`. The only text-identity property any of the fourteen new operators imposes
on a text result is **validity as UTF-8** (§3.1), and §2.4 says in the
document's own words that it *"provides no way to constrain the use of blank
space or other serialization variants"*, deferring that class to *"future
control operators"*.

**What it can do:** eight of the fourteen pin an *injective* text form — one
text per value — but only for text that is a transcoding of a **byte string**
or of an **integer**. So `canonical-encoding`'s **condition (6)** is answerable
for a hex digest and unanswerable for a label, in every DEC-002 option.
`design-notes.md` §1 carries the argument; `schema/control-operators.derived.yaml`
→ `text_identity_summary` carries the table.

## Read this before using anything here

RFC 9741 carries exactly **three** all-capitals BCP 14 occurrences in 28 KB, and
none of them is about an operator. Two are `MUST NOT`s forbidding three C
`printf` features *inside a format string*; the third is a `RECOMMENDED`, inside
an RFC v3 **aside**, asking a validator to cover at least the marker-based
subset of `.join` — in the same sentence that concedes **false negatives**. That
is expected and correct: a control operator is normative by its **definition and
its matching rule**, not by an obligation on an actor. 58 of the 61 requirements
here are `kind: inferred`, each naming the phrase or matching rule that carries
the force. The precedents are `rfc-8610` (2 keywords in 125 KB, 137 of 139
inferred) and `draft-ietf-cbor-edn-literals`.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 74 verbatim spans across 10 locators, plus all 7 tables, the 1 figure and all 6 CDDL fragments reproduced in fenced blocks with their source line ranges. All 74 confirmed contiguous substrings of the whitespace-normalised source inside their locator's section, 0 failures. **Two declared exceptions, neither healed:** one hyphenation break (`left-hand-side`, source lines 133/134) quoted as two halves, and §3.1's aside (lines 416–428) quoted with its leading `\|` bar removed and nothing else |
| requirements | `requirements.yaml` | 61 entries, `R-0001`–`R-0061`, source order, no gaps: **3 stated, 58 inferred**. `source_keyword_count` and `extracted_keyword_count` both **3**, agreeing, with a 3217-character `reconciliation` that states the real normative baseline and what was counted instead — every operator definition, every matching rule, every explicit absence or disclaimer of capability, the registry facts, and the lower-case force words the document does use (`need to be`, `needs to be reflected`, `recommended`, `should not be confused`, `cannot`, `may be useful`, `will use`, `apply`). §1.1's boilerplate is deliberately never quoted here: `bin/validate` counts texts with stripping off, so quoting it would add 11 phantom keywords and make the extraction read 14 against a source of 3 |
| schema | `schema/` | **3 verbatim, 3 derived.** Verbatim: all 6 CDDL fragments and all 7 tables, margin intact, each region with its own sha256; and the one I-Regexp the document prints. Derived: a dedented, tool-readable CDDL companion that round-trips; **all 14 operators as data** — target, controller, predicate, IANA entry, injectivity, and the effect on rfc-8610's 44 side conditions; and the exact C `printf` profile §2.3 adopts. 52 mechanical checks, all passing. See `schema/README.md` |
| messages | `messages.yaml` | 5 constructs covering all 14 operators (the ten base encodings differ only in four per-operator field values), 29 fields, with `constrained_by` **used** — 50 of the 61 requirements are cited by a field, and the 11 that are not are listed with a reason each in `locator_join`. Unlike rfc-8610, the join is honest here: 61 entries at 10 locators and one construct per section |
| examples | `examples/` | 8 vectors, `V-0001`–`V-0008`, source order, no gaps: every example the document prints — 6 CDDL fragments and 4 instances (3 valid, 1 invalid). The one negative is the source's own. Every `cddl` block re-verified as a dedented contiguous slice of the cache at its declared line range, and every instance confirmed present in the source. **The document prints not one instance of any base encoding it defines** — see `examples/README.md` |
| design-notes | `design-notes.md` | the normalisation answer with its four pieces of evidence; the `.join` non-compositionality finding and the one-line rule it produces for SDSI name chains; an operator-to-field mapping over all of `ARCH-0001` §4.1; **six named cuts against MD-3**, five of them naming the DEC-002 option they favour and one stated in option 5's favour; 9 source defects; and the correction `rfc-8610` is owed |

## Not applicable

- **protocol** — RFC 9741 defines no exchange, no role and no message. It
  defines fourteen *predicates over a data item*. Its entire §5 is two
  sentences, both incorporations by reference: "The security considerations in
  Section 5 of [RFC8610] apply." and "In addition, for the control operators
  defined in Section 2.1, the security considerations in Section 12 of
  [RFC4648] apply." Neither names a party. The only procedural content in the
  document is §4, and it is a **completed** registration in the past tense —
  "IANA has registered the contents of Table 7" — not even a policy: RFC 8610
  §6.1 governs and is not restated.
- **state-machine** — no states and no transitions, for the same reason.
  Matching is a predicate over a specification and an instance. Nothing in the
  document registers, issues, rotates, revokes or expires anything, and no
  sentence in it describes a sequence of events.

## What this does to `rfc-8610`

`rfc-8610` is at `profile: full` and carries a gate: *nothing there may be
treated as the current state of CDDL until `rfc-9165`, `rfc-9682`, `rfc-9741`
and `draft-ietf-cbor-cddl-modules` are read.* This is one of the four. What it
settles:

- **No syntax changed.** RFC 9741 adds no grammar. `rfc-8610`'s `cddl.abnf` is
  still the whole of CDDL's syntax; a tool that parses CDDL needs no parser
  change for these fourteen operators, only fourteen semantic cases.
- **None of the 44 side conditions is closed.** G-11 is *extended*, G-12
  *confirmed by a newer normative source*, G-35 *partially relieved*, G-44
  *refined*, G-36 and G-38 *reinforced*, G-39 *worsened*. Ten new side
  conditions (`N-01`–`N-10`) are added in
  `schema/control-operators.derived.yaml`.
- **[correction] One claim in an `rfc-8610` artifact of ours is now false.**
  Its `control-operators.derived.yaml` says "All names other than the fourteen
  below are Unassigned" — our wording, not RFC 8610's. This document registers
  fourteen more and names RFC 9090 and RFC 9165 as having registered others, so
  the registry holds **at least 28**. `design-notes.md` §9 states the fix.
- **All six items of `rfc-8610`'s "What CDDL cannot express that we need"
  stand.** Item 4, Unicode normalisation of labels, is *strengthened*: not
  merely absent, but declined by the document that was best placed to add it.

## Source defects found

Nine, in `design-notes.md` §8. The three that matter: `.printf`'s matching
relation is **locale-dependent with no locale fixed**, so two conforming
validators can disagree about the same instance; the ban on length modifiers
**caps `.printf`'s integer range** with no overflow rule, which rules it out
for a 64-bit SID let alone a 256-bit digest; and `%c` is **redefined away from
C** without the deviation being labelled. All are reported, none repaired.
