---
record: draft-ietf-cbor-cde
kind: schema
title: "draft-ietf-cbor-cde — schemas"
extracted: "2026-10-16"
reviewed_by: ""
---

# Schemas

Two of these files are the source's own bytes. Five are ours. The filename
carries the distinction and `bin/validate` enforces it: a `.derived.` infix is
mandatory on anything this library wrote, and an unmarked name asserts
verbatim bytes (`docs/extraction.md`, "Derived vs verbatim — the filename
carries it"). Each file repeats the claim in its own header.

| file | claim | what it is | what it does not constrain |
|---|---|---|---|
| `cde-control-operator.cddl` | **verbatim** | the `.cde` / `.cdeseq` CDDL control-operator definition, byte-for-byte including the document's three-space page margin | nothing beyond the operators themselves; their entire semantics is stated by delta from `.cbor`/`.cborseq` |
| `try-float16-encode.c` | **verbatim** | Appendix F Figure 1, the source's own C function, byte-for-byte including interior comment alignment | it covers **one leg** of float shortening (binary32 → binary16) and is not a complete shortest-head implementation |
| `cde-constraints.derived.cddl` | derived | the three named CDE constraints rendered as checkable CDDL | written from prose; none of it appears in the document |
| `shortest-head.derived.cddl` | derived | the shortest-head constraint as a grammar | the source states this entirely in prose and two example tables and ships no grammar |
| `cde-encode.derived.pseudocode.txt` | derived | the CDE encoding procedure | the document contains **no** encoding procedure; it states CDE as three named constraints in prose and restates parts as an informative checklist |
| `cde-check.derived.pseudocode.txt` | derived | the CDE-checking decoder predicate | the document ships **no** decoder algorithm; Appendix C.3.2 states the duties as three numbered MUSTs plus a closing rule |
| `float-shortest-head.derived.pseudocode.txt` | derived | shortest-head for IEEE 754, all legs | written from §3.1.2 and C.1.1 item 2; the source gives an algorithm for one leg only (the C function above) |

## Why so much of this is ours

CDE ships almost no formal grammar. It defines an encoding profile in prose
and leaves the operative procedures — how an encoder produces CDE, and what a
checking decoder verifies — to an appendix that declares itself informative.
Five of seven files here are therefore the library's own rendering, and none
of them may be quoted as the standard's grammar. That is `R-O-03` ("cited, not
invented silently") applied to a directory listing.

## Known under-constraint

The derived CDDL files cannot express CDE's two genuinely procedural rules:

- **Shortest-head** is a predicate over the relationship between a value and
  its chosen head length. CDDL can describe the admissible heads but cannot
  require that the shortest admissible one was used; that obligation lives in
  the pseudocode.
- **Lexicographic map sorting** is an ordering constraint across sibling
  entries, strengthened by §3.3 to **strictly greater** so that it also
  excludes duplicate keys. CDDL has no vocabulary for sibling order.

Both are stated in `cde-constraints.derived.cddl` as comments at the point
where the grammar stops being able to help, so a reader who validates against
the CDDL alone does not mistake a pass for CDE conformance.

**Pass 2 and pass 3 have not run.** Nothing here has been adversarially
re-derived against the source, and no example has been validated against these
schemas. They are readable; nothing may be built on them.
