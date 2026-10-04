---
record: rfc-8785
kind: schema
title: "rfc-8785 — schemas"
extracted: "2026-10-03"
reviewed_by: ""
---

# rfc-8785 — schemas

## RFC 8785 ships no schema of its own

**RFC 8785 contains no CDDL, no ABNF, no JSON Schema and no formal grammar of
any kind.** That is not an oversight in this extraction; it is a property of
the document, and it is a finding in its own right.

The absence is structural rather than accidental, and the document says why in
three places:

- **The serialization rules are delegated, not defined.** §3.2.2 states that
  the primitive serialization "is identical to that of ECMAScript", and
  §3.2.2.3 delegates number serialization outright — *"Such data MUST be
  serialized according to Section 7.1.12.1 of [ECMA-262], including the 'Note
  2' enhancement"* — and then declines to reproduce it: *"Due to the relative
  complexity of this part, the algorithm itself is not included in this
  document."* A grammar for JCS numbers would have to restate an algorithm the
  document deliberately did not restate.
- **The input constraints are delegated too.** §3.1 requires that data "MUST be
  adapted for I-JSON [RFC7493] formatting" and then lists three consequences in
  prose. I-JSON itself is a prose profile of RFC 8259 and has no schema either.
- **The parts that most need a formal statement are the parts a grammar cannot
  express.** Property-name sorting (§3.2.3) and duplicate-name prohibition
  (§3.1) are not context-free; "array element order MUST NOT be changed"
  (§3.2.3) relates input to output; and the correct serialization of a number
  is a numeric predicate. A grammar for JCS would have been silent on exactly
  the rules that make JCS canonical.

The one formal artifact the document does ship is the **ECMAScript sample
canonicalizer of Appendix A**. It is held here verbatim. In practice it has
served as the specification's executable reference — but note its own banner:
it implements neither error handling nor UTF-8 generation, so it is not a
conformant implementation.

Consequence for this library: everything in this directory except
`canonicalizer.ecmascript.js` is **ours**, written for this record, and must
never be cited as RFC 8785's own schema.

## Files

| file | covers | kind | source |
|---|---|---|---|
| `canonicalizer.ecmascript.js` | the sample canonicalizer, in full, with the source's own comment banners and page indentation preserved | **verbatim** | Appendix A, complete (lines 518–579 of the cached text) |
| `i-json-input.schema.json` | the §3.1 constraints on **input** data, as JSON Schema 2020-12: object/array/string/number/literal, binary64 magnitude bounds, and a recorded gap wherever JSON Schema cannot reach | **derived** | §3.1 in full, §3.2.2.1, §3.2.2.3, Appendix B notes (1) and (3), Appendix D, Appendix E, E.1 |
| `canonical-output.abnf` | the JCS **output** grammar as ABNF (RFC 5234), in two layers: code points (structure, literals, the complete §3.2.2.2 escaping, the ECMAScript number output language) and octets (the RFC 3629 UTF-8 encoding §3.2.4 requires) | **derived** | §3.2.1, §3.2.2.1, §3.2.2.2, §3.2.2.3, §3.2.3, §3.2.4, Appendix B; number productions additionally from ECMA-262 §7.1.12.1, which §3.2.2.3 makes normative by reference |
| `sorting.md` | the §3.2.3 sorting algorithm as an implementable procedure — the one JCS rule no grammar can express | **derived** | §3.2.3 in full, with §3.1 and Appendix A |

Naming note: the sibling `rfc-8949` record marks derived files with a
`.derived.` infix. These four filenames were fixed by the extraction task that
produced them, so the marker lives in each file's header instead — every
derived file says `DERIVED` in its opening lines and names the sections it was
built from, and the verbatim file carries `---- BEGIN VERBATIM ----` /
`---- END VERBATIM ----` markers around the untouched region. A reviewer should
not have to rely on the filename.

## How the three derived files divide the work

They are not alternative views of one thing; they constrain three different
objects, and **a harness needs all three**.

```
input document ──────► i-json-input.schema.json   (§3.1: is this canonicalizable?)
       │
       ▼  canonicalization
canonical octets ────► canonical-output.abnf      (§3.2.1/2/4: is this well-formed JCS?)
       │
       └─────────────► sorting.md                 (§3.2.3: is the member order right?)
```

`canonical-output.abnf` **cannot** check member order — it admits any
permutation (its gap item 1). A string can satisfy the entire grammar and not
be canonical JCS. `sorting.md` is therefore not supplementary prose; it is the
missing half of the output check, and it has to be run separately.

Test fixtures belong in `../examples/`, not here. This directory holds the
schemas and the algorithm; the vectors that exercise them are a different
artifact.

## What was checked

Pass 1 had no CDDL, ABNF or JSON Schema validator available in this workspace,
so at the end of pass 1 **no derived file here had been run through a real
parser for its own language**. Pass 3 closed that for both derived files, and
the two results are recorded at the end of this section; everything between
here and there is pass 1's work, which is weaker but mechanical, not assertion:

- **The verbatim region was diffed against lines 518–579 of the cached source:
  byte-identical** (sha256 of the region
  `c4c656fd9455facd9ae760bade4c67e0252475c5c2a7aa8af1092f7b8182a909`). The file
  also passes `node --check`, so the retained page indentation has not broken
  it.
- **The sample canonicalizer was executed against every example the source
  gives**, and reproduces all of them exactly: the §3.2.2 / §3.2.3 worked
  example, the §3.2.4 UTF-8 byte dump byte-for-byte, the §3.2.3 sorting test
  data in the expected order, and the 24 rows of the Appendix B number table
  that carry a JSON representation (the table has **26** data rows; rows 10
  and 11, NaN and Infinity, have an empty cell and are error cases, not
  serializations).
- **The ABNF's number and string productions were transcribed rule-for-rule
  into a validator** and run over the 24 serializable Appendix B rows (of 26)
  plus **499,848** binary64 values (400,000 uniformly random bit patterns,
  100,000 log-uniform magnitudes, and a hand-built edge set). Every
  serialization is admitted by the grammar; the observed corpus reached a
  maximum of **17 significant
  digits** and a maximum exponent magnitude of **324**, which is exactly what
  the `*20DIGIT` and `*2DIGIT` bounds in the file predict. 24 non-conforming
  spellings (`-0`, `+1`, `01`, `.5`, `1E30`, `1e30`, `0.0`, `1e+07`, `NaN`, …)
  are correctly rejected.
- **The escaping was checked exhaustively over U+0000–U+02FF**, each code point
  compared against the §3.2.2.2 rules and against the grammar; and 21
  non-conforming string spellings (`"\u0008"`, `"\u000A"`, `"\u000F"`, `"\/"`,
  `"\u00e9"`, `"\ud83d\ude00"`, …) are correctly rejected.
- **The UTF-16 vs code-point sorting divergence was established by brute
  force**, not asserted: 275,145,156 single-character name pairs sampled across
  the whole scalar range and densely through U+D000–U+E100. Every disagreeing
  pair has a supplementary-plane character on one side and a character in
  U+E000–U+FFFF on the other; **no BMP-only pair disagrees**. That is the exact
  condition behind the source's note that UTF-8 or UTF-32 sorting is
  "incompatible with this specification".
- **The JSON Schema parses**, its `minimum` and `maximum` are bit-exact against
  Appendix B's "Max neg number" / "Max pos number" rows
  (`ffefffffffffffff` / `7fefffffffffffff`), it accepts all 13 input examples
  the source gives, and it rejects Appendix D's `1.4e+9999`. Each documented
  gap was then **confirmed empirically to be a real false positive** — see
  below.
- **Every quoted passage was diffed against the cached source**: 8 blockquotes
  in `sorting.md` and 27 quoted sentences across the ABNF, the JSON Schema and
  the verbatim file's header. All verbatim, after one defect was found and
  fixed (the §3.2.2.3 quote in the ABNF had dropped the `[IEEE754]` citation
  from inside its quotation marks), and after four property names in
  `sorting.md`'s §3.2.3 test-data quote were restored to the source's escape
  spellings (`\u20ac`, `\ufb33`, `\ud83d\ude00`, `\u00f6`) from the literal
  characters they had been written as.

**Pass 3, with real tooling installed.** Both outstanding parser checks ran:

- **`i-json-input.schema.json` was validated against the JSON Schema 2020-12
  metaschema** with `jsonschema` 4.26.0 (Python). `Draft202012Validator` is the
  class the `$schema` keyword selects; `check_schema` raises nothing, and an
  explicit `iter_errors` run against the full metaschema reports **0 errors** —
  not merely the first, the complete list. The schema then instantiates and
  every `$ref` resolves. **No schema-level error was found and nothing was
  changed.** The `$id` remains a placeholder (`library#44`); that is a
  publication decision, not a validity defect, and the metaschema does not care.
- **`canonical-output.abnf` was transcribed rule-for-rule into an executable
  validator a second time**, independently of pass 1's transcription, and
  guarded by 36 positive and 31 negative controls before use — including `-0`,
  `1E+30`, `1e30`, `1e+0`, `0.0000001`, an uppercase-hex escape, a `\u0008`
  written long, an escaped solidus, an escaped non-ASCII character, a lone
  surrogate and whitespace after a name-separator, all correctly rejected. All
  67 controls behave. This is a transcription check, not an RFC 5234 tool run;
  the RFC 5234 conformance of the file itself is the separate `jcs-char` /
  `digit0-9` finding recorded in `../README.md`.
- **Independent confirmation of gap item 4 below.** The 24 serializing Appendix
  B rows were decoded from their IEEE 754 bit patterns and re-serialized by a
  real ECMAScript engine (`String(d)` under Node). **24 of 24 reproduce the
  vector's `expected` exactly.** The grammar still cannot check the digits —
  that is the gap — but the corpus standing in for it now has an engine behind
  it.

## What no schema here can express

Stated gaps, not omissions. Each is a real RFC 8785 rule that the derived files
cannot decide; each lives in full in the file it belongs to
(`canonical-output.abnf` gap items 1–8, `i-json-input.schema.json`
`$defs/NOT-EXPRESSIBLE` items 1–8) and in `../requirements.yaml` and
`../normative.md`. Collected here for the cross-check pass.

**Unexpressible in *both* derived schema languages:**

1. **No duplicate property names** (§3.1, via I-JSON — `rfc-8785#R-0003`). Not context-free, so no
   ABNF; and the JSON Schema data model has already collapsed duplicates
   last-wins before a validator runs, so no JSON Schema either. Confirmed:
   `{"a":1,"a":2}` parses to `{"a": 2}` and validates cleanly. **Must be
   checked on the raw token stream**, by something that is neither of these
   files.

**Unexpressible in the output grammar:**

2. **Member sort order** (§3.2.3 — `rfc-8785#R-0020`, `rfc-8785#R-0021`,
   `rfc-8785#R-0023`; the sort *predicate* those three invoke is
   `rfc-8785#R-0025` through `rfc-8785#R-0029`) — the largest gap in the ABNF.
   See `sorting.md`.
3. **"Array element order MUST NOT be changed"** (§3.2.3 — `rfc-8785#R-0024`,
   with the scan obligation `rfc-8785#R-0022`) — a relation between
   input and output; only a differential test can see it.
4. **That a serialized number is the correct shortest round-trip decimal for
   its double** (§3.2.2.3 — `rfc-8785#R-0018`). The grammar pins the shape,
   never the value. A
   serializer emitting `1e+31` where `1e+30` was required passes. This is why
   Appendix B exists, and it belongs to `../examples/`.
5. **The digit-level consequences of minimal *k*** (§3.2.2.3 —
   `rfc-8785#R-0018`, the same requirement as item 4, whose substance is the
   ECMA-262 algorithm RFC 8785 declines to reproduce): that trailing positions in
   `int-form` are zeros, that no fractional part ends in `0`, and that there
   are at most 17 significant digits. Confirmed as a real gap — the grammar
   accepts `1.0`, `4.50`, `0.50` and `1.230`, none of which JCS can emit.
6. **"MUST … terminate with an appropriate error"** for lone surrogates
   (§3.2.2.2 — `rfc-8785#R-0017`) and NaN/Infinity (§3.2.2.3 —
   `rfc-8785#R-0019`). The grammar excludes all three from
   the output language, but non-derivability is not termination: an
   implementation that *silently drops* a lone surrogate emits output this
   grammar accepts while violating the MUST.
7. **Byte order mark** (**no requirement id — and that absence is the gap**).
   RFC 8785 never mentions one, so no `rfc-8785#R-NNNN` exists to cite: this is
   the only one of the thirteen that names no requirement, because there is no
   requirement to name. The nearest JCS statement is `rfc-8785#R-0030`
   ("MUST be encoded in UTF-8"), which does not reach the question. The two
   ABNF layers together exclude a leading `ef bb bf`, but by inheritance from
   RFC 8259 §8.1, not by any JCS statement. Inherited-not-stated.

**Unexpressible in the input schema:**

8. **"MUST be expressible as IEEE 754 [IEEE754] double-precision"** (§3.1 —
   `rfc-8785#R-0005`) —
   only the magnitude bound is expressible. The round-trip-exactness half is not, and
   most validators have already parsed the literal to a double, destroying the
   evidence. Confirmed with the document's own example: Appendix D's
   `int64Max: 9223372036854775807` **validates cleanly** and is not expressible
   as a double (it becomes `9223372036854775808`).
9. **Lone surrogates** (§3.1 / §3.2.2.2 note — `rfc-8785#R-0004` for the input
   rule, `rfc-8785#R-0017` for the termination duty) — no portable JSON Schema
   expression. JSON Schema 2020-12 does not require the ECMA-262 `u` flag, so
   the obvious pattern means different things in different validators, and most
   host parsers have already replaced or rejected the defect before validation.
   Deliberately **not** faked with a pattern. Note the asymmetry: the output
   ABNF *can* exclude lone surrogates structurally, because it sees octets.
10. **"Parsed JSON string data MUST NOT be altered during subsequent
    serializations"** (§3.1, Appendix E — `rfc-8785#R-0007`, with
    `rfc-8785#R-0041` for the Appendix E stream/schema-parser half) and the
    §3.1 Note forbidding Unicode normalization (`rfc-8785#R-0008`).
    Both are properties of the **pipeline**, not of any
    document. Confirmed: Appendix E's own failure case — `"055"` → `"55"`,
    `"2019-01-28T07:45:10Z"` → `"2019-01-28T07:45:10.000Z"` under a
    reviver-based parse — validates perfectly both before and after, as do NFC
    and NFD spellings of the same text.
11. **NaN / Infinity** (§3.2.2.3, Appendix B note 3 — `rfc-8785#R-0019`) — not
    representable in the
    JSON Schema data model at all; enforcement belongs to the parser.
12. **Appendix B note (1)'s ±9007199254740991 safe-integer range**
    (`rfc-8785#R-0038`) — a SHOULD,
    and **deliberately not enforced**, because it is narrower than the §3.1
    MUST and the note itself says "how numbers are used in applications does
    not affect the JCS algorithm". Layer it separately if wanted.
13. **Appendix D's "wrap big numbers as strings"** (`rfc-8785#R-0039`, the
    Appendix D `MUST`, together with its §3.1 twin `rfc-8785#R-0006`, the
    `RECOMMENDED` — the same obligation at two strengths; see the
    `reconciliation` note in `../requirements.yaml`) — an instruction
    to the author of an *application* schema, not a checkable constraint on
    arbitrary input.

**The dangerous subset.** In items 1, 10 and 12 — and in 8 — non-conforming
data validates **cleanly**. A green result from `i-json-input.schema.json` is
therefore *not* evidence that §3.1 was met. Any harness built on this directory
should say so where it reports results.

## Open for the later passes

- ~~Run both derived files through a real RFC 5234 tool and a real JSON Schema
  2020-12 validator.~~ **Done, in pass 3.** The RFC 5234 run found and fixed the
  `jcs-char` / `digit0-9` core-rule collision; the JSON Schema 2020-12
  metaschema run reports 0 errors. See *What was checked* above.
- Items 1 and 9 want a raw-token-level checker that is neither file. If one is
  written for this library, it serves RFC 8259 and I-JSON too, not just JCS.
- `$id` in `i-json-input.schema.json` is a placeholder
  (`https://m-of-n.example/…`) pending a decision on whether this library
  publishes schema identifiers at all.
