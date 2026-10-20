---
record: rfc-9741
kind: schema
title: "rfc-9741 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

RFC 9741 ships **no grammar**. It adds nothing to RFC 8610's ABNF and defines
no new syntax: a control operator is already `ctlop = "." id` in the Appendix B
grammar, and `type1 = type2 [S (rangeop / ctlop) S type2]` already admits any
`id` after the dot. What this document ships is **fourteen names and the prose
that says what each one means**. So the schema artifacts here are of two kinds:
the source's own CDDL and tables, captured verbatim, and one derived file that
turns fourteen paragraphs of prose into data a tool can apply.

**Three verbatim files, three derived.** `docs/extraction.md`, *Derived vs
verbatim*: an unmarked filename asserts the source's own bytes.

| file | claim | what it is |
|---|---|---|
| `cddl-fragments.cddl` | **verbatim** | all six CDDL fragments the document prints, lifted by line range with the RFC's three-space left margin intact. Six regions, each with its source line range and its own sha256 in a banner. Not parseable as CDDL — the margin is part of what is preserved |
| `tables.txt` | **verbatim** | all seven tables with their caption lines, same treatment, seven regions with per-region digests. Table 1 is the whole document on one page; Table 7 is the IANA registration |
| `base10-numeral.iregexp` | **verbatim** | the one regular expression the document prints, `0\|-?[1-9][0-9]*`, quoted from inline §2.2 prose at source line 252. Its dialect is **I-Regexp (RFC 9485)** per §1.1, *not* the XSD dialect RFC 8610 §3.8.3 gives `.regexp` |
| `cddl-fragments-dedented.derived.cddl` | **derived** | the same six regions with the margin removed so a CDDL tool can read them. The removal round-trips in both directions |
| `control-operators.derived.yaml` | **derived** | **the central artifact.** All fourteen operators as data: target, controller, the predicate each imposes, its IANA entry, its injectivity as a text form, and its effect on rfc-8610's 44 side conditions — **none of which RFC 9741 closes**; G-35 is partially closed by `rfc-9165`, not here |
| `printf-profile.derived.txt` | **derived** | the exact C `printf` profile §2.3 adopts — what is excluded, what is redefined, and four under-specifications that let two conforming validators disagree |

## Mechanically checked, not asserted

52 checks, all passing, re-derived from `.cache/rfc-9741.txt` — and **re-run
independently at pass 2** from the cache, with its own scripts, all still
passing. The per-region digest convention is `sha256` of the region's lines
joined by `\n` with **no trailing newline**; pass 2 recovered it by brute force
because no file stated it, and it is stated here now so the next pass does not
have to.

- each of the **13 verbatim regions** (6 CDDL + 7 tables) is byte-identical to
  its declared source line range, and each declared per-region sha256 verifies;
- a **completeness sweep** over every source line outside the claimed regions
  finds **no table row, table rule or CDDL rule left uncaptured**. The only
  lines that look like table rows and are not captured here are source lines
  416–428, §3.1's implementation-note aside, which is prose and lives in
  `../normative.md` and `../requirements.yaml`;
- the dedented derived file **round-trips**: re-indenting every non-blank line
  by three spaces reproduces the verbatim regions exactly;
- all **8 vectors** in `../examples/vectors.yaml` carry a `cddl` block that is a
  dedented contiguous slice of the cache at its declared line range, and each of
  the four `instance` values occurs in the source.

## The one thing to know about `cddl-fragments.cddl`

**Do not concatenate the regions.** `F03` and `F04` each define `hexlabel<K>`,
identically, because the source prints the rule twice — once under `my_alg_19`
and once under `any_alg`. A naive concatenation is a CDDL file with a duplicate
rule name. RFC 8610 Appendix C makes that an error only when the second
definition *differs*, which it does not here, but no tool should be asked to
decide that. Each region is its own file; that is how `../examples/vectors.yaml`
carries them.

Figure 1's caption (source lines 383–384) is inside the verbatim `F06` region
and dropped from the dedented one, because it is not CDDL.

## Why there is no `*.schema.json` and no ABNF

Nothing in RFC 9741 is JSON Schema shaped, and the document adds no ABNF. The
grammar that governs these operators is `records/ietf/rfc-8610/distilled/schema/cddl.abnf`
(verbatim) and its dedented companion; neither changes. **A tool that already
parses CDDL needs no parser change to accept these fourteen operators — it
needs fourteen semantic cases.** That is exactly why
`control-operators.derived.yaml` exists, and why rfc-8610's gap **G-11** is
*extended* by this document rather than closed.

## What the operators cannot state

The question this record was extracted to answer, with the answer in one line:
**a CDDL schema still cannot state that a text string is in any Unicode
normalisation form.** Eight of the fourteen pin a canonical text form, but only
for text that is a transcoding of a byte string or of an integer. See
`control-operators.derived.yaml` → `text_identity_summary`, and
`../design-notes.md` §1.
