---
record: rfc-8742
kind: schema
title: "rfc-8742 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 8742 ships no grammar for the format it specifies, and that is the
finding.** §2 — the whole format — is twenty-four lines of prose containing a
two-case recursive definition, a two-case decoding rule and three statements
about what cannot be detected. There is no ABNF, no JSON Schema, and **no CDDL
rule for a CBOR Sequence**, because the document says CDDL cannot write one:
§4.1, *"Currently, CDDL does not provide for unadorned CBOR Sequences as a
top-level subject of a specification."*

So the three CDDL fragments the document *does* print are not the format. Two of
them are **array** rules standing in for a sequence rule, with an English comment
instructing the reader to read them otherwise; the third is about what goes
inside a byte string. They are captured verbatim; everything that describes the
format itself is derived and carries `.derived.` in its name.

**Three verbatim files, three derived.** `docs/extraction.md`, *Derived vs
verbatim*: an unmarked filename asserts the source's own bytes.

| file | claim | what it is |
|---|---|---|
| `cddl-fragments.cddl` | **verbatim** | all three CDDL fragments the document prints (§4.1 ×2, §4.3), lifted by line range with the RFC's three-space left margin intact. Three regions, each with its source line range and its own sha256 in a banner. Not parseable as CDDL — the margin is part of what is preserved |
| `registrations.txt` | **verbatim** | the three things this document registers: the §6.1 media type template complete, §6.2's Table 1, and the §6.3 structured-syntax-suffix template complete. Three regions with per-region digests. **Not one of the three is a CBOR tag** |
| `cddl-fragments-dedented.derived.cddl` | **derived** | the same three regions with the margin removed so a CDDL tool can read them. The removal round-trips |
| `cbor-seq.derived.abnf` | **derived** | the format as a grammar. **Two productions, one of which is a placeholder** — and the one-line first production is the honest statement of everything a grammar can say about a CBOR Sequence. Carries the three consequences that follow from `*item` |
| `cbor-seq-container.derived.cddl` | **derived** | **the central artifact.** The top-level rule §4.1 says cannot be written, written four ways — the document's own array-plus-comment (C1), §4.3's byte-string wrapper (C2), §2's own definite-length array (C3), and the indefinite-length variant, excluded with reasons (C4) — each with its byte cost and what it does not bind |

There is **no `*.schema.json`**. Nothing in RFC 8742 is JSON Schema shaped: the
document's entire content is a claim about byte concatenation, and JSON Schema
has no byte type and no notion of a file's framing. Writing one would be
inventing a second artifact to say what `cbor-seq.derived.abnf` says in one line.

## Mechanically checked, not asserted

The per-region digest convention is the library's: **`sha256` of the region's
lines joined by `\n`, with no trailing newline** — the convention
`records/ietf/rfc-9741/distilled/schema/README.md` states and
`records/ietf/rfc-9682` uses.

Six regions, all verified at pass 1:

| region | § | source lines | sha256 |
|---|---|---|---|
| `F01` | §4.1 | 195–197 | `db6109d27e15f12e64458c319aef88f65b3e24f0d8fe56ef14c2cf56c324410b` |
| `F02` | §4.1 | 206–209 | `34f33fbcc624b1ff1ab63c1bc53ff2d77d9bf904800c5ba1cb62c79dfb86ebbc` |
| `F03` | §4.3 | 245–249 | `8c0a1bf5b3f27a17825f9ebb2de0f2658ef70e821db79a2c0d4ed515829fd6d1` |
| `R01` | §6.1 | 278–317 | `cb796eb7cdd185d949023a1f4e412d228e78470ab42319f800eb54211603be19` |
| `T01` | §6.2 | 326–332 | `e9a45ef5666fb6c6b00f3d2d10dfcabc3710532804b9a74dd99b867f6b1f9b2b` |
| `R02` | §6.3 | 341–377 | `28edad49fd029ef4388b822bbb74c9cf7bbdc882aa0a51fafb1918cc4448ba7e` |

- each region is **byte-identical** to its declared source line range, and each
  declared digest verifies under exactly that convention;
- a **completeness sweep** over every source line outside the claimed regions
  finds **no CDDL rule, no table row and no registration field left
  uncaptured**. The §4.2 diagnostic-notation examples (source lines 229–231) are
  deliberately *not* here: they are instances, not schema, and they live in
  `../examples/vectors.yaml`;
- the dedented derived file **round-trips**: re-indenting every non-blank line by
  three spaces reproduces the verbatim regions exactly;
- the source carries **no form feeds, no page footers and no trailing whitespace
  on any line**, so no region needed page decoration removed, and **no aside**,
  so no bar was stripped. `R02` contains one hyphenation break the source makes
  (`any IESG-` / `designated successor.`, lines 373/374) and the region carries it
  unhealed.

## The one thing to know about `cddl-fragments.cddl`

**Do not concatenate the regions.** `F02` and `F03` both define `my-sequence`,
and **differently** — `F02`'s element is a bare choice, `F03`'s is a byte string
wrapping one. A naive concatenation is a CDDL file with a conflicting duplicate
rule name, which RFC 8610 Appendix C makes an error. Each region is its own file.

That is a sharper hazard than the one `rfc-9741`'s schema directory carries,
where the duplicated rule was *identical*. Here the two definitions conflict,
and a tool that merged them would silently take whichever came last.

## Why a derived container file exists at all

Because `R-O-03` requires that an algorithm be **cited, not invented silently**,
and here there is nothing to cite. §4.1 says CDDL cannot express the container;
`cbor-seq.derived.abnf` shows ABNF cannot either; so whatever rule a
specification of ours writes for a multi-statement file is **ours**, and the
filename has to say so before anyone quotes it as the standard's.

`cbor-seq-container.derived.cddl` is therefore not a convenience. It is the
discipline applied: four candidates, each with its byte cost, so that the
DEC-002 ADR chooses rather than inherits. See `../design-notes.md` §Cut 2 and
§Cut 3.
