---
record: rfc-8610
kind: index
title: "rfc-8610 — distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: passes 1 and 2 of 3 complete.** Pass 1: two agents in parallel at
effort max, each reading only `.cache/rfc-8610.txt`. Pass 2 (verify, effort max,
2026-10-19): an independent agent that did not extract, re-deriving every
mechanical claim from the cache with checkers written from scratch. **The
cross-check pass has NOT run** and no `reviewed_by` is signed, so this record
carries no `profile`. Readable; nothing may be built on it. library#39 owns
finishing it.

Source: RFC 8610, *Concise Data Definition Language (CDDL)*.

**Read this before using anything here.** RFC 8610 carries exactly **two**
all-capitals BCP 14 occurrences in 125 KB, and neither is an obligation on a
CDDL implementer: one is a `SHOULD` binding *a downstream specification
author* (§3.8.3.1), and the other is RFC 8610 **quoting RFC 7071 in order to
call it ambiguous**, inside an appendix its own opening line declares "for
information only". That is not a thin document — **CDDL's normativity is
carried by its grammar and its matching rules**, which is why six of its eight
appendices open "This appendix is normative." and why 137 of the 139
requirements here are `kind: inferred`, each naming the phrase or matching rule
that carries the force.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 344 verbatim statements and 4 reproduced blocks (the §3.3 primitive-keyword list, §3.11 Table 1, the §6.1 registry table, Appendix A's CDDL→PEG map) across 56 distinct locators. All 344 and all 4 confirmed contiguous substrings of the whitespace-normalised source; every locator verified by section range, not merely document-wide |
| requirements | `requirements.yaml` | 139 entries, `R-0001`–`R-0139`, source order, no gaps: **2 stated, 137 inferred**. `source_keyword_count` and `extracted_keyword_count` both 2, with a 2560-character `reconciliation` stating what was counted instead — every type- and group-matching rule, every occurrence semantic, every control-operator definition, socket/plug, the prelude's fixity, every explicit *disclaimer of capability*, and the lower-case force words the document actually uses (`must`, `needs to`, `ought not`, `urged`, `strongly encouraged`). §1.1's boilerplate is deliberately never quoted: `bin/validate` counts texts with stripping off, so quoting it would add 11 phantom keywords |
| schema | `schema/` | **8 verbatim, 3 derived.** The two that matter most are Appendix B's complete ABNF (47 productions, three regions spanning two page breaks) and Appendix D's standard prelude (40 rules) — both byte-identical to the cache with the RFC's margin intact, independently re-verified. See `schema/README.md` |
| messages | `messages.yaml` | 39 constructs, 142 fields (33 CDDL-text, 6 EDN-text from the normative Appendix G). **`constrained_by` is omitted throughout, deliberately and stated in the file header**: with two keyword occurrences there is no honest way to tie a construct to a requirement id, and inventing one is the failure FX-1 exists to prevent |
| examples | `examples/` | 98 vectors covering every example the document prints: 92 valid, 5 invalid, **1 `indeterminate`**. All five negatives are the source's own, none invented. **109 block scalars verified against the cache: 103 a single unbroken source run, 1 spanning a page frame, 5 joining two non-adjacent ranges across an omitted line and declaring it in their own `notes`** — so 104 are dedented contiguous slices and 5 are the declared compositions. 9 further `instance` values are one-line prose-quoted scalars, each confirmed present in the source. (Pass 1 reported the single-range count as the total; corrected in pass 2.) |
| design-notes | `design-notes.md` | a verdict on CDDL for D4's encoding-neutral types; six things we need that CDDL cannot express, each with the source's own statement of the absence; and five named cuts against MD-3 |

## Not applicable

- **protocol** — §5 says it outright: "This document presents a content rules
  language for expressing CBOR data structures. As such, it does not bring any
  security issues on itself". Appendix C makes the whole semantics a *matching
  relation between one specification and one instance* — "an instance (data
  item) "matches" a CDDL specification if it is allowed by the CDDL
  specification". No roles, no messages, no error paths. §4's three uses are
  all single-party tool uses. The only procedural content is §6.1's IANA
  registration policy, which is an IANA process, not a protocol.
- **state-machine** — no states and no transitions, for the same reason:
  matching is a predicate, not a lifecycle.

## The `indeterminate` vector is deliberate

`V-0037` (§3.5.3's `do-not-do-this` against `{3: 5, 4: 6}`) carries
`expect: indeterminate` rather than valid or invalid, because the source
refuses to decide it — "the specification writer is simply urged to not write
pathologically non-deterministic specifications" — in the same sentence that
says tools cannot detect the condition. Forcing a verdict either way would
assert something RFC 8610 does not.

## What CDDL cannot express that we need

Stated here because it changes a deliverable, not merely a schema. In each
case the source states the absence itself:

1. **Cross-field constraints — `Threshold` is inexpressible.** `1 ≤ k ≤ n` and
   `n = len(members)` have no construct: `.lt/.le/.gt/.ge` compare against "a
   value given as a right-hand-side type" (§3.8.6), occurrence indicators take
   literal integers (§3.2), and Appendix A confirms CDDL has neither PEG's NOT
   nor AND, so it cannot be smuggled in as an exclusion. The same hole takes
   `Validity`'s `not_before ≤ not_after`.
2. **Algorithm-dependent widths** — only by hand-enumerating `(alg, size)`
   pairs as a type choice.
3. **Sets.** CDDL has no set type, cannot require an array be duplicate-free,
   and §3.5 states it has no ordering vocabulary at all.
4. **Unicode normalisation of labels** — §3.1: "Processing of CDDL does not
   involve Unicode normalization processes"; §3.8.6 compares text "bytewise
   identical".
5. **A semantic layer.** Comments are whitespace (§3.1) and annotations do not
   exist. **So D4's deliverable is not "a CDDL file" but a container that
   carries one** — a scope statement D4 does not currently make.
6. **Type-versus-group identity is not locally decidable** — Appendix C says
   the determination "isn't always determined by syntax alone" and "may need to
   span several levels of rule definitions". Related: prioritized choice makes
   `Principal = Key / KeyId / …` order-dependent when both are byte-string
   shaped, and because a `/=` choice "is populated in the order the rules are
   given", **plug-file concatenation order is semantic**.

**And on encoding:** four independent statements forbid reading a CDDL schema
as a byte constraint (§2.2.3, §3.2, §3.8.1, Appendix E). **A CDDL schema alone
cannot make an encoding deterministic.**

## Source defects found

Reported, never repaired. The first is concrete for our test vectors:

1. **Appendix G.2 names four EDN byte-string prefixes; §3.1 and the Appendix B
   ABNF admit two.** G.2 (normative) gives `h`/`b32`/`h32`/`b64`; §3.1
   (normative) says "may be prefixed by "h" or "b64"", and `bsqual = "h" /
   "b64"`. Both normative, never reconciled. **#39 assigns EDN the test-vector
   role, so a vector written `b32'…'` is valid EDN and will not parse as a CDDL
   literal.**
2. The plain-text rendering of Appendix G.2 is corrupt — `>h<`, `>b32<`,
   `>h32<`, `>b64<` are untranslated markup. A rendering defect in the exact
   bytes `content.sha256` pins, not a spec defect, recorded because our
   verbatim quotes necessarily reproduce it.
3. **§3.8.1's only pointer at "format constraints outside of CDDL" is stale** —
   it cites "Section 3.9 of [RFC7049]", obsoleted by RFC 8949 where §3.9 became
   §4.2 with materially different content. That parenthetical is the hinge
   between CDDL and any determinism profile, so the staleness is load-bearing.
4. **The prelude's tag set is frozen at RFC 7049** and the prelude "is deemed to
   be fixed", so every tag registered since 2013 must be redeclared per file.
5. Appendix E Figure 15 admits `float16/32/64` while the same appendix says NaN
   and the infinities "cannot be represented in JSON".
6. §3.5.3's drafting obligation has no decision procedure, in the same sentence
   that says tools cannot detect the condition. Any CI check we write is our
   own invention and under `R-O-03` must be cited as ours.
7. **`CRLF` is redefined as `%x0A / %x0D.0A`**, admitting a bare LF where
   RFC 5234's core rule is `%x0D %x0A` — and it hides in plain sight, because
   `ALPHA`, `DIGIT`, `HEXDIG` and `SP` are redefined *identically* in the same
   block, so the whole thing reads as a restatement.
8. Surrogates U+D800–DFFF are admitted by `SCHAR`/`BCHAR`/`PCHAR`/`SESC`
   although §3.1 mandates UTF-8; `SCHAR` and `BCHAR` are not parallel and
   nothing says so; and **no horizontal tab exists anywhere in CDDL**, not even
   inside a text string, which no sentence states.
9. Table 1 disagrees with the grammar three times, including omitting the cut
   `^` that §3.5.4 makes load-bearing.
10. Appendix H's own generated instance does not satisfy its own schema on a
    strict reading — and in **every** place it could fail, not one. Three members
    are typed `float16` (`rating`, `confidence`, `normal-rating`) and the
    instance carries six floating-point values across them; pass 2 round-tripped
    all six through binary16 and **none is representable** (`0.34133473256800795`
    rounds to `0.34130859375`), nor is any representable in binary32.

## This record is not the current state of CDDL

`rfc-9165`, `rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` are all
still `status: fetched`, and `rfc-9682`'s own record note says "both remain
current, so an implementation must read them together". **Nothing here may be
treated as the current state of CDDL until those four are read.** They are
library#39 Tier 2.
