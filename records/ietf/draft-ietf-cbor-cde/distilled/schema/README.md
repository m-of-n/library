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

## What the verify and cross-check passes did to these files

**Pass 2 (verify, 2026-10-18)** re-checked both verbatim extracts byte for byte
against the cached source — `leaf = #6.24(bytes .cde any)` at source line 915,
and Figure 1 at source lines 2195–2215 — and found that
`try-float16-encode.c` **did not compile**: the figure's caption had been left
bare inside the BEGIN/END VERBATIM region. The caption now sits in a comment
just outside it, the region is byte-identical to lines 2195–2215, and `cc -c`
exits 0. It also cross-checked the source's own `try_float16_encode` against an
independent implementation over 125,560 inputs, including all 65,536 binary16
bit patterns widened to binary64: no disagreement.

**Pass 3 (cross-check, 2026-10-18)** ran the suite that had never been run. It
transcribed `cde-check.derived.pseudocode.txt`,
`float-shortest-head.derived.pseudocode.txt`, `cde-encode.derived.pseudocode.txt`'s
`head()` and `lex_strictly_greater()`, and the data-model rules of the two CDDL
files into one runnable checker and put **every vector that carries bytes — 117
of the 118 — through all of it: 96 valid accepted, 21 invalid rejected, 0
failures**, and every rejection under a rule the vector's own `violates` cites.
The 118th, `V-0012`, carries no bytes because the source prints none; it was
synthesised exactly as its own notes instruct (`0x9f`, 256 encoded items,
`0xff`) and is rejected, with the definite-length counterpart accepted as a
control. The checker was then shown to **discriminate** on 54 cases the source
never prints — indefinite-length text, array and map heads (the source exhibits
only the byte-string one), non-preferred heads at every argument width,
non-preferred float widths including subnormals and NaN payloads, misordered,
duplicate and byte-string-keyed maps, bignum range and leading-zero edges,
reserved `ai`, a sub-32 one-byte simple value and trailing data — 54 correct, 0
wrong. Finally the re-encode check the source itself proposes
(`cde_encode(generic_decode(input)) == input`, Appendix C preamble) was run over
all 96 valid vectors: **96 byte-identical, 0 mismatched.**

**The division of labour these files claim holds exactly, and it is lopsided.**
Of the 21 runnable invalid vectors, the CDDL layer catches **none**; the
head-level rules (definite-length-only and shortest-head over the argument)
catch **9**; the value-level rules (float preferred serialization, bignum range
and leading zeros, UTF-8 validity, strict key ordering) catch **12**; and the
extra-code check of `cde-encode.derived.pseudocode.txt` §4.2 — the RFC 8949
§5.6.1 `-0.0` = `0.0` equivalence — catches the **1** that nothing else does
(`V-0007`). `V-0116` is caught by two layers at once, which is why the three
numbers sum to 22 over 21 vectors. The CDDL layer's nil score is **not a
defect**: it is the *Known under-constraint* above, measured. The one thing
either CDDL file can reject on its own is a tag 2/3 whose content is not a byte
string (`bignum-content = bytes`), and the source never prints such a case, so
it appears only among the discrimination cases (`c20a`).

Still outstanding: nothing but a human `reviewed_by`, and a run of these files
through a real RFC 8610 parser, which is not installed here. The checker above
is a transcription of the pseudocode, not a CDDL tool.
