---
record: rfc-8785
kind: index
title: "rfc-8785 — distilled artifact set"
extracted: "2026-10-03"
reviewed_by: ""
---

# rfc-8785 — distilled artifact set

FX-1 full extraction of **RFC 8785, JSON Canonicalization Scheme (JCS)**.
Source `.cache/rfc-8785.txt`, sha256 `63d52294eb0e…b240`, 984 lines, read in
full including Appendices A–I.

**Status: passes 1 and 2 complete; pass 3 (cross-check) partially complete.**
The record does not yet declare `distillation.profile: full` — that claim
requires all three passes, and pass 3 was interrupted by a session limit before
finishing. What it did land is recorded below; what it did not is in *Known
gaps*.

## Artifacts

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 91 verbatim statements and blocks, §2–§6.1 and Appendices A–I, in source order. 36 flagged `_[lowercase/implied]_` — pass 3 added statements 35–37, the three §3.2.3 "measures", to match their extraction as `R-0026/27/28` with `verb: none`. Includes Appendix A in full, Appendix B Table 1 with all 26 rows and footnotes (1)–(4), both Appendix F six-step procedures, and the §5 three-step procedure. Excludes §1, §6.2 informative references, Acknowledgements and Authors' Addresses, none of which carry a normative or testable statement. |
| requirements | `requirements.yaml` | 41 entries `R-0001`–`R-0041` in source order. 32 carry a BCP 14 verb, matching the source count exactly (25 MUST, 4 MUST NOT, 2 RECOMMENDED, 1 SHOULD); 9 are lowercase obligations with `verb: none`. One entry, `R-0036`, is `kind: inferred` and declared non-verbatim. `reconciliation` is empty because the counts agree. |
| schema | `schema/` | One verbatim file and three derived. RFC 8785 ships **no** CDDL, ABNF, JSON Schema or grammar of any kind — that absence is structural and is argued in `schema/README.md`. |
| messages | `messages.yaml` | 16 structures, 61 fields. Applicability is **partial** and the file says so: RFC 8785 defines no wire messages, headers or envelopes. What is captured is the output form, the input constraints, the per-type serializations, the complete §3.2.2.2 escaping table, the sort key, and the four appendix structures. |
| protocol | `protocol.md`, `protocol.yaml` | Partial, and the partiality is the finding. No exchange protocol exists, but §5 (normative) and Appendix F (carrying **no** BCP 14 keyword) both specify processing order, and that order is what R-O-05 contradicts. Three flows, five error paths. |
| examples | `examples/vectors.yaml` | 44 entries — 43 executable vectors and 1 recorded absence. All 26 Appendix B rows, the §3.2.3 seven-key sorting vector, the §3.2.4 byte dump, and the Appendix D and E cases. 7 error vectors each carry `violates.rule` verbatim plus `violates.locator`. 4 derived outputs carry `in_source: false`. |
| design-notes | `design-notes.md` | 6 adopt / 6 adapt / 8 reject against ARCH-0001, ARCH-0002 P1/P4/P5, ADR-0001 and DEC-002 option 5. 12 open questions, then 8 source defects numbered 13–20. Concludes that **DEC-002 option 3 should be withdrawn rather than out-scored**, while recording that option 3 wins namespace governance outright. |

**Not applicable:** `state-machine` — RFC 8785 defines no lifecycle, no
persistent state and no transitions. The two Appendix F procedures and the §5
procedure are straight-line sequences and are held in `protocol.md`. The
scaffold stub was removed rather than left as a file of TODOs.

## A counting trap, stated once

Appendix B Table 1 has **26 data rows**, of which **24 carry a serialization**;
the rows for `7fffffffffffffff` (NaN) and `7ff0000000000000` (Infinity) have an
empty JSON Representation cell. Both numbers are correct about different
things, and pass 1 produced one artifact saying 24 and another saying 26. Where
a figure appears in this record, it names which it means.

## What passes 2 and 3 changed

Pass 2 was adversarial and re-derived everything from the source rather than
reading the artifacts as truth. It found **10 defects and fixed 10**. The one
that mattered: `schema/sorting.md` carried the Hebrew property name
**decomposed** as `U+05D3 U+05BC` instead of the precomposed `U+FB33` the
§3.2.3 test vector specifies — wrong bytes, wrong UTF-16 length, and a wrong
sort position. That is precisely the hazard `examples/README.md` warns about,
committed inside the record that warns about it, and it is signature-breaking.
It is also the best available evidence for this topic's condition (6).

Others: a false "re-checkable" invariant about where U+20AC appears raw; a
dropped `[IEEE754]` inside quotation marks; a byte-offset off by one; a wrong
fixture byte count; three wrong token cells in a derived breakdown; and three
cases of extractor prose altered into or spliced inside a `violates.rule` field
that is verbatim everywhere else.

## What pass 3 landed before it was interrupted

1. **`constrained_by` is wired** across all 61 fields of `messages.yaml` — 105
   links to requirement ids, none left empty. This was the largest integration
   gap and it is closed.
2. **The ABNF was not valid RFC 5234 and now is.** Rules named `char` and
   `DIGIT` **are** the core rules, because §2.1 makes rule names
   case-insensitive, so a conforming tool rejected the grammar outright.
   Renamed to `jcs-char` and `digit0-9`; the language defined is unchanged.
   Only a real parser check surfaces this, which is why pass 1 recorded the
   check as not run rather than claiming it.
3. **`normative.md` flags reconciled from 33 to 36** — statements 35–37 added.
4. **`requirements.yaml` `reconciliation`** now records the `R-0006` ↔ `R-0039`
   cross-reference.

## Known gaps

1. **`i-json-input.schema.json` has not been checked against the JSON Schema
   2020-12 metaschema.** Pass 3 was interrupted before confirming it.
2. **The 44 vectors have not been validated against the schema and the ABNF**
   as a set.
3. **`protocol.yaml` structures have not been cross-checked** against
   `messages.yaml`.
4. **The 33-vs-9 lowercase-obligation enumeration was not written down.** Pass
   3 derived the 36 flags and the per-statement verdicts, but the verdicts
   existed only in its context and were lost when it terminated. The flags
   encode the conclusion; the reasoning needs redoing if anyone wants it.
5. **`$id` in `i-json-input.schema.json` is a placeholder**, pending whether
   this library publishes schema identifiers at all — a project decision, not a
   record one. See `library#44`.
6. **Derived files here do not use the `.derived.` filename infix** that
   `rfc-8949` uses; the marker is in each file's header instead. `library#44`.

Gaps 1–3 are why `profile: full` is not declared and why
`bin/check-pr-extraction` correctly still blocks the PR.

## A tooling warning that outlives this record

`bin/_yaml.py` has **no block-scalar support** and returns the literal string
`"|-"` for every `|-` value. Every `input:` and `expected:` in `vectors.yaml`
reads as `"|-"` through it, and both `bin/validate` and
`bin/check-pr-extraction` import it — so **any CI check over those values is
vacuous**. The in-file warnings in `protocol.yaml` and `messages.yaml` against
`>` and `|` are working around this, not expressing a style preference. A
defect of the `sorting.md` class above would not be caught by CI today.
