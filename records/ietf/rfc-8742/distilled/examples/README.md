---
record: rfc-8742
kind: examples
title: "rfc-8742 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` holds **16 vectors in two classes, and the classes are not
cosmetic**:

- **`V-0001`–`V-0005`** are the source's own, lifted from the cache by line
  range, by script, never retyped. **Five is every example RFC 8742 prints.**
- **`D-0001`–`D-0011`** are **derived — ours**. Every one was executed through a
  CBOR well-formedness checker written for this pass, and each carries the
  result the checker actually returned.

## The finding that matters most here

**RFC 8742 contains no bytes.** For a specification whose entire content is a
claim about byte concatenation, the document prints **three CDDL fragments, two
lines of diagnostic notation and one registry table, and not one hex octet.**

That is worth stating precisely, because it is unusual in this lane: `rfc-9277`
prints complete annotated hex for both of its envelopes, and `rfc-8949` prints
test vectors by the page. **There is nothing *of the document's* to make a
fixture from — and eleven fixtures were still derivable, which is this
directory.** So **any conformance test for RFC 8742 is ours**, and under
`R-O-03` — an algorithm "SHALL be cited, not invented silently" — ours has to be
marked as ours. The `D-` prefix is that marking.

*(`[cross-check]` 2026-10-21, pass 3: that sentence read "Here there is nothing
to make a fixture from", which is `summary.md`'s wording and is the claim
`../design-notes.md` §8 **refutes** — it was still standing, unqualified, in the
directory the refutation produced. The scoped version is above.)*

And it is worse than "no vectors", because the document also records that the
*notation* cannot write the thing: §4.2, diagnostic notation "also does not
provide for unadorned CBOR Sequences at this time" (`rfc-8742#R-0033`), and
"Note that it is somewhat difficult to discuss zero-length CBOR Sequences in the
latter form" (`rfc-8742#R-0036`). **The fixtures cannot be written honestly in
the source's own notation either** — which is why `D-0001`, the empty sequence,
exists and has no `V-` counterpart.

## The source's own five

| vector | § | lines | kind | what it is |
|---|---|---|---|---|
| `V-0001` | §4.1 | 195–197 | CDDL | `bytes .cborseq my-array` — a sequence *inside* a byte string, the one case CDDL handles natively |
| `V-0002` | §4.1 | 206–209 | CDDL | the top-level workaround: an array rule plus **two comment lines that are the actual specification of the container** |
| `V-0003` | §4.3 | 245–249 | CDDL | the same, with each element wrapped in a byte string |
| `V-0004` | §4.2 | 229 | diagnostic | `[1, 2, 3]` — the recommended form, and it is one array |
| `V-0005` | §4.2 | 231 | diagnostic | `1, 2, 3` — the bracket-free form, permitted only "In a more informal setting" |

All five were re-verified as dedented contiguous slices of the cache at their
declared line ranges; the only transformation is removal of the common
three-space left margin. **None has an instance**: `V-0001`–`V-0003` print no
data, and `V-0004`/`V-0005` *are* the data, in a notation with no bytes.

`V-0001`–`V-0003` also cannot be instantiated as printed: `my-foo` and `my-bar`
are named and never defined anywhere in RFC 8742. They are carried as printed,
unresolved — the same situation as `rfc-9741`'s `COSE_Sign1`.

## The eleven derived fixtures, and what each one is for

| vector | bytes | result | the point |
|---|---|---|---|
| `D-0001` | *(zero bytes)* | valid, 0 items | the empty sequence is valid and has no notation |
| `D-0002` | `010203` | valid, `[1, 2, 3]` | `V-0005` in bytes |
| `D-0003` | `83010203` | valid, one array | `V-0004` in bytes — **the whole cost of §2's own alternative is the leading `83`** |
| `D-0004` | `0102` | **valid**, `[1, 2]` | `D-0002` with the tail removed, and **no decoder can tell** |
| `D-0005` | *(zero bytes)* | valid, 0 items | `D-0002` destroyed, byte-identical to `D-0001` |
| `D-0006` | `830102` | **invalid** | `D-0003` with the tail removed, and it **is** detected |
| `D-0007` | `011f03` | **invalid** at offset 1 | one corrupt entry costs the tail |
| `D-0008` | `410141024103` | valid, 3 byte strings | §4.3's wrapper applied to `D-0002` |
| `D-0009` | `4101411f4103` | valid as byte strings; middle content malformed | the wrapper recovers 2 of 3 from `D-0007`'s corruption |
| `D-0010` | `41015a` | **invalid** | a corrupt byte-string *head* still strands the tail |
| `D-0011` | `010203040506` | valid, 6 items | `cat a.seq b.seq > c.seq` is in spec |

**The pair to read first is `D-0004` against `D-0006`.** The same deletion — drop
the last element — is **silent** in a CBOR Sequence and **loud** in a
definite-length array, and the difference is one byte of head. §2 already
recommends the array in a parenthesis (`rfc-8742#R-0014`); those two fixtures are
what the recommendation buys, in four bytes against three.

**The pair to read second is `D-0007` against `D-0009`.** The same corrupted byte
destroys the tail of a bare sequence and costs one element of a
byte-string-wrapped one. The document offers §4.3 as a *performance*
optimisation for skipping and fan-out; `D-0009` is the **durability** argument it
does not make, and `D-0010` is where that argument stops.

## What a fixture consumer should know

- **The derived fixtures are a model's output, not a library's.** The checker
  written for this pass covers unsigned integers, byte strings, text strings,
  arrays, maps, tags and half-precision floats — enough for every fixture here
  and for cross-checking `rfc-9277`'s three hex vectors, and no more. It is not
  a CBOR implementation and is not shipped. A real test harness should re-derive
  these eleven byte strings from a conformant decoder and compare.
- **`D-0001` and `D-0005` are deliberately the same bytes.** That duplication is
  the finding, not an oversight: a test suite should assert that the empty log
  and the destroyed log *cannot* be told apart.
- **No fixture here exercises an indefinite-length container.** §2 offers the
  indefinite-length array as an alternative (`rfc-8742#R-0014`) and every
  deterministic profile this library holds excludes it; the exclusion is recorded
  in `schema/cbor-seq-container.derived.cddl` C4 rather than fixtured.
- **No fixture here is signed.** §5 says the format "provides no cryptographic
  integrity protection of any kind" (`rfc-8742#R-0041`), and the one sentence
  that matters for us — that per-element COSE does not bind "the relationship of
  the elements in the sequence" (`rfc-8742#R-0042`) — cannot be fixtured from
  this document, because COSE is named and not used. A fixture for it belongs on
  `rfc-9052` and would be ours.
- **`D-0003`'s `83` is the only framing byte anywhere in this directory.** Every
  other fixture's bytes are entirely elements. That is `messages.yaml`'s
  `framing_bytes_contributed_by_this_document: 0`, made visible.
