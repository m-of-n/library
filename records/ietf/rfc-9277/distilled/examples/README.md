---
record: rfc-9277
kind: examples
title: "rfc-9277 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` holds **14 vectors in two classes**:

- **`V-0001`–`V-0007`** are the source's own — **three complete annotated hex
  examples** and **four CDDL snippets**, lifted from the cache by line range, by
  script, never retyped.
- **`D-0001`–`D-0007`** are **derived — ours**, for the cases the document does
  not print.

**Every hex string in the file was executed** through a CBOR decoder written for
this pass, and each entry carries the result the decoder actually returned.

## Unusually for this lane, the source has real vectors

`rfc-8742` — the sibling record, the format this document labels — prints **zero
hex octets**. RFC 9277 prints three complete annotated hex dumps and four worked
`TN` values, and **all of them reproduce**:

| vector | § | method | bytes | decodes to |
|---|---|---|---|---|
| `V-0001` | §2.2.1 | CBOR Tag Wrapped | 25 | `55799(1668546929([{0: "current", 6: 3, 2: 1.5}]))` |
| `V-0002` | §2.3.1 | Labeled CBOR Sequence | 15 | `55800(1668547090('BOR'))`, then `0`, `8`, `15` |
| `V-0003` | Appendix C | Labeled CBOR Sequence | 12 | `55800(1330664270(h'424F52'))` — the Openswan label alone |

Checked at this pass, all passing:

- each hex string **rebuilt from its source line range** by stripping the
  annotation comments, and found identical to the string recorded here;
- each region carries its own **sha256**;
- `V-0001` decodes to §2.2.1's own diagnostic notation line for line — the half
  float `f9 3e00` is **exactly 1.5** and `63757272656e74` is `"current"`;
- the two stated fingerprints **are** the first eight bytes of their examples:
  `d9d9f7da63740171` and `d9d9f8da63740212`;
- the label **is** 12 bytes, 3 + 5 + 1 + 3;
- all four `TN` values recomputed from the Appendix B formula and **all four
  agree**: `TN(112)=1668546929`, `TN(272)=1668547090`, `TN(432)=1668547250`,
  `TN(11050)=1668557910`;
- all four CDDL slices are exact dedented contiguous slices at their declared
  lines.

## The three findings the source's own vectors carry

**1. `V-0001`'s map keys are not in deterministic order.** They are printed
`0, 6, 2`; RFC 8949 §4.2.1's bytewise rule gives `0, 2, 6` (`00 < 02 < 06`).
The document claims determinism only of "a deterministic first 8 to 12 bytes", so this is not
a contradiction — but the only CBOR Tag Wrapped example in the document has a
non-deterministically encoded **payload**, which is the same gap one layer in.

**2. `V-0004` does not match `V-0001`.** Appendix B.1's
`senml-cbor = #6.1668546929(bstr)` asserts a byte-string tag content;
`V-0001`'s tag content is an **array**, per Appendix B's "Exceptionally" rule.
B.1 is introduced by a cross-reference *to* §2.2.1, so a reader is invited to
apply the rule to the example it does not fit. **The document's own CDDL does not
match the document's own example.** Reported, not repaired.

**3. Neither worked example is a file anyone would store**, and the document says
so about one of them: §2.3.1, "This is a somewhat contrived example, as this is
not a media type that is likely to be committed to storage." `V-0003` is the only
vector built on a tag obtained for a real protocol — and the in-library IANA row
for that tag carries the reference "Michael Richardson; Samir Hussain", **not**
RFC 9277, so the document's own deployment did not take §2.1's advice about the
Reference field.

## The seven derived fixtures, and what each one is for

| vector | bytes | result | the point |
|---|---|---|---|
| `D-0001` | 29 | valid, same value as `V-0001` | the inner tag in an 8-byte head: a `file(1)` rule from §2.2.1 **misses it** |
| `D-0002` | 18 | valid, same value as `V-0002` | two non-preferred heads: the label is **15 bytes, not 12**, the fingerprint is wrong, **and the first eight bytes contain two zero bytes** |
| `D-0003` | 15 | valid | **relabelling**: `V-0002`'s payload behind `V-0003`'s label. Breaks no signature |
| `D-0004` | 30 | valid, 8 items | **a label at offset 15** — the concatenation case Appendix A.2 leaves open |
| `D-0005` | 18 | valid, 7 items | the same concatenation with the second label stripped — the fix A.2 names, and what it costs |
| `D-0006` | 12 | valid | **`TN(63)`: the label for `application/cbor-seq`, which needs no new allocation and which the document does not print** |
| `D-0007` | 15 | valid | a known outer tag with an **unregistered** inner tag `0x41414141`. The file parses; nothing says what to do |

**The two to read first are `D-0001` and `D-0002`**, because together they refute
§2's central claim. "Both use CBOR tags in a way that results in a deterministic
first 8 to 12 bytes." — that holds only under **preferred serialization**, and
this document requires nothing at all: it has **zero** BCP 14 keywords.
`schema/prefix-spellings.derived.txt` enumerates all **30** well-formed
definite-length spellings of the 12-byte label; **1** is 12 bytes long, **5**
match the stated fingerprint, and **25** put a zero byte inside the first eight —
defeating §2.1's own advice about C strings even when the registrant followed it.
*(`[correction]` 2026-10-20, pass 2: **20** here, re-derived as 25. The
enumeration itself was right; six prose restatements of it, including this one,
had drifted.)*

**`D-0003` is the condition-(4) fixture.** Swapping the inner tag makes the file
claim to be an Openswan configuration. It is well formed, it breaks no signature
over the payload, and nothing in RFC 9277 detects it, because under both methods
the indicator sits outside everything a signature over the content could cover.
§3 names the class — "(This is an instance of a check versus use issue.)" — and
states no rule.

## Two fixtures deliberately have no expected result

`D-0004` and `D-0007`. That is not an omission: **the document defines none**,
and the absence is what a test suite should assert.

- `D-0004` is `cat a.seq b.seq > c.seq` on two labelled files. RFC 8742 §2 makes
  it in spec; Appendix A.2 says a protocol must either define the semantics of
  embedded labels, tolerate them, or strip all but the first — **lower-case
  "must", no default**. A reader that rejects it and a reader that accepts it are
  both conformant.
- `D-0007` is a known outer tag with an unregistered inner one. 55800 announces
  only "indicates that the file contains CBOR Sequences"; the inner tag names a
  protocol the reader cannot know; the file parses cleanly; and the magic
  number's entire purpose fails open and silently. RFC 8949 §5.4 governs
  unrecognised tags in general and discourages rejecting them — that is
  RFC 8949's rule, not this one's.

## What a fixture consumer should know

- **The decoder is a model's output, not a library's.** It covers unsigned
  integers, byte strings, text strings, arrays, maps, tags and half-precision
  floats — enough for every fixture here and for `rfc-8742`'s eleven — and no
  more. It is not a CBOR implementation and is not shipped. A real harness should
  re-derive these byte strings from a conformant decoder and compare.
- **No fixture here is signed**, so none exercises `D-0003`'s point against a
  real signature. That fixture belongs on `rfc-9052` and would be ours.
- **No fixture exercises an indefinite-length byte string in the label.**
  RFC 8949 §3.2.3 admits one for the 3-byte content, which is why the
  30-spelling enumeration is a **floor** and not a count.
- **`vectors.yaml`'s `tn_values` table is written as block maps, not inline flow
  maps.** `bin/_yaml.py` returns a flow map as an opaque string, so an inline
  table would be unreadable to every tool in `bin/`. The file says so where it
  matters.
