---
record: draft-ietf-cbor-cddl-modules
kind: examples
title: "draft-ietf-cbor-cddl-modules — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` holds **every block the document prints**, in source order, with
no gaps: **19 vectors**, `V-0001`–`V-0019`. Every `text:` block was lifted from
`.cache/draft-ietf-cbor-cddl-modules.txt` **by line range, by script, never
retyped**; the only transformation is removal of the Internet-Draft's
three-column left margin. The generator asserts the round trip in both
directions and with both of this library's YAML readers (`bin/_record_yaml.py`
and `bin/_yaml.py`): what a parser reads back out of the file is byte-identical
to the dedented source slice, including the 63-space continuation of the two
RFC 8792 `\` wraps. **0 round-trip failures.**

## What a "vector" is for this record

This document defines a **notation and a composition**, not a wire format.
There are no CBOR bytes to decode and no signatures to verify, so a vector is
one printed block together with its role in the document and what can actually
be checked about it:

| role | count | vectors |
|---|---|---|
| command line + module-structured input | 6 | `V-0002`, `V-0004`, `V-0006`, `V-0008`, `V-0010`, `V-0012` |
| composed output (basic CDDL) | 7 | `V-0003`, `V-0005`, `V-0007`, `V-0009`, `V-0011`, `V-0013`, `V-0016` |
| the ABNF grammar | 1 | `V-0017` |
| shell command line | 2 | `V-0018`, `V-0019` |
| command line alone, no input file | 1 | `V-0014` |
| a directive printed on its own | 1 | `V-0015` |
| environment-variable value | 1 | `V-0001` |

## `expect` tally, and why three of them are not `valid`

**9 valid · 2 invalid · 4 incomplete · 4 not-applicable.** No negative was
invented. Every one is the document's own.

- **`invalid` ×2 — `V-0008` and `V-0010`.** Both are directives the document
  prints as working examples and its **own Appendix A cannot derive**:
  `;# include cose.label, cose.values from rfc9052 as cose` (source line 388)
  and `;# import cose.empty_or_serialized_map from rfc9052 as cose` (line 414).
  Appendix A's `id` admits neither `-` nor `.` (`R-0082`), where RFC 8610's
  `id` admits both. Three dotted selectors in two of the seven directive
  instances the document prints. `../schema/grammar-gaps.derived.txt` G-01.
- **`incomplete` ×4 — `V-0002`, `V-0004`, `V-0006`, `V-0008`.** All four are
  *module inputs*, and their incompleteness is **by design**: the dangling rule
  name is exactly what the directive resolves. This is worth stating precisely,
  because it fixes the sense of §2.1's central claim. Read as basic CDDL on its
  own, **every one of the six module files the document prints has at least one
  rule name that resolves to nothing** — `COSE_Key`, `cose.COSE_Key`, `label`
  and `values`, `cose.empty_or_serialized_map`. So "each module source file can
  at the same time be basic CDDL on its own" (`R-0023`) is a claim about
  **lexical** well-formedness. RFC 8610's one dispensation for an undefined
  name is §3.9's socket convention — "Tools honor that convention by not
  raising an error if such a type or group is not defined at all"
  (`rfc-8610#R-0079`) — and it applies **only** to names with a leading `$` or
  `$$`, which none of these are.
- **`not-applicable` ×4 — `V-0001`, `V-0014`, `V-0018`, `V-0019`.** A shell
  command line or an environment-variable value; no CDDL grammar applies.

## The one that matters: `V-0009` is broken and should not be

`V-0009` (source lines 399–401) is the only **composed output** in the document
with a dangling reference, and it has two. Checked mechanically, not by eye:

```
mydata = {* label => values}
cose.label = int / tstr
cose.values = any
```

The block defines `mydata`, `cose.label` and `cose.values`. `mydata` references
`label` and `values`, which are defined **nowhere** in the block and are **not**
among the 40 names of the RFC 8610 Appendix D prelude — verified against this
library's verbatim capture at
`records/ietf/rfc-8610/distilled/schema/prelude.cddl`, whose full name list is
`any b64legacy b64url bigfloat bigint bignint biguint bool bstr bytes cbor-any
decfrac eb16 eb64legacy eb64url encoded-cbor false float float16 float16-32
float32 float32-64 float64 int integer mime-message nil nint null number regexp
tdate text time true tstr uint undefined unsigned uri`.

The cause is visible in `V-0008`, the input that produced it: its module file
still reads `mydata = {* label => values}`, naming the **unprefixed** rules,
where the corresponding line in `V-0004` *was* updated to the prefixed spelling
(`start = cose.COSE_Key`). The line the author appears to have intended is
`mydata = {* cose.label => cose.values}`. The document nonetheless introduces
the output with "Again, only exactly the rules mentioned are included"
(`R-0058`), presenting it as a correct demonstration — and it is the **only**
place the document demonstrates `include` together with an `as` clause.

**The other six composed outputs are all closed**: `V-0003`, `V-0005`,
`V-0007`, `V-0011`, `V-0013` and `V-0016` each define every non-prelude name
they reference. The two folded ones were checked after unfolding.

Reported, not repaired. The block in `vectors.yaml` is the document's bytes.

## How to re-derive the closure check

The check is a rule-name reachability test, not a parse: harvest every
left-hand side as *defined*, harvest every identifier in the right-hand sides
after dropping comments, control operators (`.cbor`, `.size`), member keys
(`Fritz:`) and text literals, and subtract the defined set and the 40 prelude
names. Everything left dangles. `V-0011` and `V-0013` must be unfolded per
RFC 8792 first — remove the trailing `\`, the line break and the leading
whitespace of the continuation line, which fires exactly once in each.

## Diff pairs worth keeping

Four pairs of vectors differ in exactly one respect, and each pair is the whole
evidence for a rule the document states only by example:

| pair | one difference | what it demonstrates |
|---|---|---|
| `V-0003` / `V-0005` | the `as cose` clause | **what prefixing is**: four names grow a `cose.` prefix; `int`, `tstr`, `bstr`, `any` do not (`R-0053`) |
| `V-0007` / `V-0011` | `include … from` vs `import … from` | explicit `include` is **not** transitive (`R-0056`); explicit `import` is (`R-0060`) |
| `V-0011` / `V-0013` | the selector written without its prefix | emits **one extra line**, the alias at source line 456 (`R-0064`) — which is the whole basis for that rule, and it is never stated as one (G-21) |
| `V-0005` / `V-0016` | `-s` on the command line | the root rule is emitted as `$.start.$`, a name used once in the document and nowhere defined (G-18) |

## Reproducing any of this

`V-0018` and `V-0019` are the document's own instructions: `gem install cddlc`
(Ruby ≥ 3.0), at **version 0.2.5 or later** (`R-0092`), then
`cddlc -2 -tcddl <file> | cddl - gp 10`. Note that Appendix B writes the
conversion flags as two arguments where every example in §2.5–§2.7 writes them
as one (G-20), and that **Appendix B declares itself "for information only"**
(`R-0088`) — so the tool and its version floor are informative, and every
composed output above is whatever that implementation emits rather than what a
specification requires. Nothing in this directory was produced by running it.
