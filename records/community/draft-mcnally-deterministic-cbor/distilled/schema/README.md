---
record: draft-mcnally-deterministic-cbor
kind: schema
title: "draft-mcnally-deterministic-cbor — schemas"
extracted: "2026-10-16"
reviewed_by: ""
---

# draft-mcnally-deterministic-cbor — schemas

## dCBOR ships one line of formal grammar, and it is a quotation

**draft-mcnally-deterministic-cbor-18 contains no CDDL profile of dCBOR, no
ABNF, no JSON Schema, no pseudocode and no reference code.** Its entire formal
content is a single CDDL rule in Section 3 —

```
   number = int / float
```

— and even that is not dCBOR's. Section 3 introduces it as *"The CDDL Standard
Prelude as defined in [RFC8610] Appendix D defines:"*, quoting RFC 8610 in
order to make a point about how a dCBOR *application* should write its own
CDDL: that a numeric field needs no type choice, because Numeric Reduction
settles the encoding. It is held here as `cddl-prelude-number.cddl`, which is
the only verbatim file in this directory.

**So four of the five artifacts below are ours.** Nothing in them may be cited
as dCBOR's own grammar.

The absence is structural, not an oversight, and the document is explicit about
two of the three reasons:

- **Section 3 outsources the check to implementations instead of publishing a
  grammar.** It adds two CDDL *control operators*, `.dcbor` and `.dcborseq`
  (registered in Section 6, Table 2), defined only as *"exactly like `.cbor`
  and `.cborseq` … except that they also require the encoded data item(s) to
  conform to dCBOR"*. A control operator is a hook for a validator to call out
  to a dCBOR codec. Publishing one is the admission that CDDL cannot express
  the thing — which is correct, and is the finding below.
- **Section 8.6 ("Why not define an API?") declines to specify a procedure.**
  The authors *"acknowledge that such guidance might be useful"* and choose not
  to widen the document's scope, directing the reader to the four
  implementations in Section 4 instead. That is why there is no pseudocode to
  copy.
- **And the rules themselves are mostly not schema-shaped.** dCBOR narrows the
  *encoding*: definite length only, preferred serialization, bytewise
  lexicographic map key order, no duplicate keys, one NaN, NFC. None of those
  is a property of an instance of the CBOR generic data model, which is what
  CDDL describes — RFC 8949 Section 2 makes serialization variants invisible at
  that level on purpose. A CDDL profile of dCBOR would be silent on exactly the
  rules that make dCBOR deterministic.

Counted bluntly: of dCBOR's **seven narrowing rules and 15 numbered normative
requirements** (Sections 2.1–2.7), the derived CDDL here enforces **one and a
half** — Section 2.6 in full, and the DCBOR_INT half of Section 2.5 — and the
derived ABNF adds **one more**, Section 2.1, decided from the initial byte
(it also re-decides 2.6, this time on encoded bytes). The rest need a
procedure, which is why two of the five files are pseudocode.

## Files

| file | kind | covers | deliberately does not constrain | source |
|---|---|---|---|---|
| `cddl-prelude-number.cddl` | **verbatim** | the document's only formal notation: the CDDL rule `number = int / float`, byte-for-byte from line 417 of the cached text, with the two surrounding sentences quoted in the header so the citation cannot be overstated | anything. It is a quotation of RFC 8610's prelude, not a dCBOR rule, and it constrains no dCBOR behaviour at all. It must not be compiled with the prelude — a prelude name defined twice is a redefinition error | Section 3, complete |
| `dcbor-profile.derived.cddl` | **derived** | the dCBOR data model as CDDL (RFC 8610): major type 7 restricted to `false` / `true` / `null` plus floats, integers bounded to DCBOR_INT, and Section 2's recursion through array elements, both halves of every map entry, and tag content. Informative rules for the Section 8.5 escape hatch (bignum tags 2/3, float-array tags 80/81/82) | numeric reduction, the single NaN, preferred serialization, definite length, map key order, map key uniqueness, NFC, and the duty to *reject* — nine stated gaps, listed in the file. **A fixture can satisfy every rule in it and not be dCBOR** | Sections 2, 2.5, 2.6, 3, 6 (Tables 1–2), 7.2 (Table 4 rows 3–4), 8.5 |
| `dcbor-head.derived.abnf` | **derived** | the *head* as ABNF (RFC 5234): which initial bytes dCBOR admits and the 0/1/2/4/8-byte argument each selects. Decides Section 2.1 and Section 2.6 by construction — the two rules decidable from the initial byte alone, and the two the CDDL cannot see | everything value-dependent: which argument width is the *shortest* (2.2), that a major type 1 argument stays below 2^63 (Table 4), and every distinction among `f9`/`fa`/`fb` encodings — canonical vs payload NaN, reducible `42.0` vs irreducible `1.5`, preferred `f97c00` vs rejected `fa7f800000`. It is a head grammar: it cannot reach content, nesting or map arity | Sections 2.1, 2.5, 2.6, 8.2, 8.4; frame from RFC 8949 §3, §3.1–3.3 |
| `numeric-reduction.derived.pseudocode.txt` | **derived** | Section 2.5 in full, both directions: the encoder's reduction to DCBOR_INT and `preferred_float`, the canonical NaN, the decoder's rejection set, and the equality predicate that Sections 2.3 and 2.4 need. Ten derivation notes record every reading decision | well-formedness (assumed — RFC 8949 Appendix C), and everything non-numeric. It decides nothing about strings, containers or simple values | Sections 2.2, 2.4, 2.5, 7.1 (Table 3, 41 rows), 7.2 (Table 4, 11 rows), 8.1, 8.3 |
| `dcbor-validate.derived.pseudocode.txt` | **derived** | the recursive conformance decision over all seven rules — Sections 2.1 through 2.7 — on encoded bytes, plus the encoder-side duties including the reduce-then-sort-then-check ordering that `encode_map` must follow. Calls the numeric file rather than restating it | whether a *rejection* actually happened (an implementation that silently repairs a violation passes this procedure and breaks the requirement); which subset of CBOR an implementation chooses to support, which Section 2 leaves free; and well-formedness. `nfc()` is left as a dependency on a Unicode implementation this record does not hold | Sections 2, 2.1–2.7, 3, 8.5; frame from RFC 8949 §3, §4.1, §4.2.1, Appendix C; UNICODE-NORM |

Naming follows `docs/extraction.md`, *Derived vs verbatim*: every file this
library wrote carries `.derived.` in its name, the one verbatim file carries no
infix, and each file's header repeats the claim in its first lines. The
verbatim file additionally marks its copied region with
`---- BEGIN VERBATIM ----` / `---- END VERBATIM ----`; that region is one line.

## How the four derived files divide the work

They constrain four different objects, and a harness that wants a conformance
answer needs the last one.

```
application data ──► dcbor-profile.derived.cddl        (2.6 + DCBOR_INT: is this shape admissible?)
       │
       ▼ encode (reduce, then sort, then check)
   initial byte ───► dcbor-head.derived.abnf           (2.1 + 2.6: is this byte admitted at all?)
   numeric item ───► numeric-reduction.derived.…txt    (2.5: is this the one legal encoding of the value?)
   whole item  ────► dcbor-validate.derived.…txt       (2.1–2.7, recursively: is this dCBOR?)
```

Only the last is a conformance decision. The CDDL is for stating what an
application's own data looks like; the ABNF is the cheap byte-level filter and
the direct comparison point against the sibling `rfc-8949` record's
`cbor-head.derived.abnf`.

Test fixtures belong in `../examples/`, not here. In particular the two
diagnostic-notation figures in Section 2.5 — Figure 1, the valid CBOR map with
keys `10` and `10.0`, and Figure 2, the invalid dCBOR map Numeric Reduction
turns it into — are examples, not grammar, and are not duplicated in this
directory.

## What was checked

No CDDL tool and no RFC 5234 tool is installed in this workspace, and no CBOR
library either, so **neither grammar file has been run through a real parser
for its own language**; that is the first job for anyone who has one. What pass
1 did instead is mechanical, not assertion:

- **The verbatim region was diffed against line 417 of the cached source:
  byte-identical**, three leading spaces included (sha256 of the region,
  newline included:
  `1589dd679dd894ac874f897c35b4f190688a65afb3e8e4172b9a37f58f6bdf6c`).
- **`numeric-reduction.derived.pseudocode.txt` was transcribed into Python and
  run against every vector the source gives.** All **41 rows of Table 3**
  (Section 7.1) encode to exactly the bytes the source states — including the
  three subnormal boundaries, both `uint64` boundaries, both `int64`
  boundaries, `-0.0 → 00`, and the three canonicalized values `f97c00`,
  `f9fc00`, `f97e00`. All **11 rows of Table 4** (Section 7.2) are rejected,
  each for the reason the source gives for it. 0 mismatches in 52 vectors.
- **The decoder rendering was also run over negative vectors the source does
  not supply**, to confirm the rules bite where the tables are silent: `-0.0`
  spelled `f98000`, `fa80000000` and `fb8000000000000000` is rejected as
  reducible (derivation note 6 in `numeric-reduction.derived.pseudocode.txt`
  records that the source's own tables never say so), as are `f9c000` (−2.0) and
  `fb4028000000000000` (12.0 at double width), while `f7`, `f8ff` and `e0` fall
  to the Section 2.6 rejection instead.
- **The ABNF's admitted initial-byte set was rebuilt from its own terminals and
  compared against a set derived independently from Sections 2.1 and 2.6:
  202 bytes, no extras, none missing.** Of RFC 8949's 229 well-formed initial
  bytes, dCBOR excludes exactly 27 — `5f 7f 9f bf` (the indefinite-length
  heads), `ff` (break), `e0`–`f3` (simple values 0–19), `f7` (`undefined`) and
  `f8` (simple values 32–255). Argument widths were checked byte by byte
  against RFC 8949 Section 3: 0/1/2/4/8 as required, no mismatches. Major types
  0–6 keep all 28 of their heads; major type 7 keeps 6 of 29.
- **The CDDL was audited mechanically** for duplicate rule names, references to
  undefined rules, and redefinition of an RFC 8610 prelude name: none. 14 rules.
  The four unreferenced ones are deliberate and documented in place —
  `dcbor-tag-201` is a convenience root subsumed by `dcbor-tagged`, and the
  three Section 8.5 rules are marked informative.
- **Every passage quoted in a header was diffed against the cached source.**

## What no artifact here can express

Stated gaps, not omissions. Each is a real dCBOR requirement; each lives in full
in the file it belongs to (`dcbor-profile.derived.cddl` gaps 1–9, and the two
pseudocode files' closing sections) and in `../requirements.yaml`.

1. **Numeric Reduction (Section 2.5 rule 1)** — unexpressible in *both* grammar
   languages, and the reason the pseudocode exists. CDDL has no "has a non-zero
   fractional part" operator, and a float and the integer it reduces to are
   *numerically equal*, so no `.ne` formulation separates them. The CDDL admits
   `42.0`, `12.0` and `-0.0`; every one of them is a Table 3 or Table 4 case.
2. **The single NaN (Section 2.5 rule 2)** — IEEE 754 makes every NaN compare
   unequal to everything including itself, which is the source's own
   observation in Section 8.3. No value comparison in CDDL can pin one NaN.
3. **Preferred serialization (Section 2.2)** — a predicate over the encoding,
   which the generic data model deliberately hides. The ABNF enumerates the
   five argument widths; requiring the shortest that carries the value is not a
   grammar's job.
4. **Map key order (2.3) and uniqueness (2.4)** — CDDL maps are unordered and
   CDDL cannot require distinctness across a `* keytype => valuetype` entry.
   Worse here than in plain CBOR: under Numeric Reduction the duplicate need not
   exist in the application's data at all (Figures 1 and 2).
5. **NFC (Section 2.7)** — `tstr` constrains the major type only, and no CDDL
   operator applies a Unicode normalization form. Note what this means for
   interoperability, which the source does not discuss: two conforming
   implementations compiled against different Unicode versions can disagree
   about the same bytes. The only such crack in dCBOR's determinism.
6. **"MUST reject" (every decoder requirement)** — non-derivability is not
   rejection. An implementation that silently repairs — normalizes on input,
   re-sorts a map, reduces a float it should have refused — satisfies every
   artifact here and breaks the requirement. Only a differential test over a
   real implementation sees it, and the four implementations are listed in
   Section 4. **This is the one gap no file in this directory can close.**

## Findings this pass is handing on

Four things the extraction found in the source itself, recorded here because
they belong to whoever writes `../requirements.yaml`, `../examples/` and
`../design-notes.md`:

1. **The integer bound is appendix-only, and that is the sharpest reading
   decision in this directory.** Section 2.5 introduces `DCBOR_INT = [-2^63,
   2^64-1]` solely as the target range for *floating point* reduction. **No
   numbered requirement in Section 2 says an untagged integer outside DCBOR_INT
   is invalid** — and RFC 8949 major type 1 reaches −2^64, so unrestricted CBOR
   allows it. The only statement that rejects it is Table 4 in Section 7.2
   ("65-bit negative integer value", under a heading saying these MUST be
   rejected). Both derived grammars and the pseudocode take DCBOR_INT as
   bounding the whole numeric model, in both directions — the reading the
   tables force — and say so where they do it.
2. **Section 2.7 restarts its numbering**: every other subsection numbers the
   decoder requirement after the encoder one (2.1 is 1 then 2; 2.5 is 1, 2, then
   3), but 2.7 numbers both of its items "1". Still 15 numbered items; it means
   "2.7 requirement 1" is ambiguous and must be cited by role.
3. **Section 2.5 labels its roles differently from every other subsection** —
   "dCBOR implementations that support floating point numbers" for rules 1 and
   2, "dCBOR decoders …" only for rule 3. So the single-NaN rule binds *both*
   directions directly, while reduction reaches a decoder only through rule 3.
   A requirements table that keys all 15 items as encoder/decoder pairs will
   mis-key these three.
4. **Three editorial slips in Appendix A, with the vectors themselves correct.**
   Table 3 labels −127 as "(−2^8 − 1)", which is −257 (−127 is −(2^7 − 1)), and
   −32768 as "(−2^16)", which is −65536 (−32768 is −2^15); both encodings,
   `387e` and `397fff`, are right for the decimal values given. And the note
   "Most negative double that converts to int64" on −9223372036854774784.0 is
   imprecise: −2^63 is itself exactly representable as a binary64, is in
   DCBOR_INT, and is more negative — Table 3's own integer row gives its
   encoding. The vector pins the most negative double *strictly greater than*
   `INT64_MIN`. Worth reporting upstream; the draft is at −18 and still open.

## Open for the later passes

- Run `dcbor-profile.derived.cddl` through a real RFC 8610 tool and
  `dcbor-head.derived.abnf` through a real RFC 5234 tool. Neither has been
  parsed by anything but the audit described above. Watch for two things in the
  CDDL: whether the tool accepts a range spanning `-9223372036854775808..`
  `18446744073709551615` (65 bits of span), and whether it accepts `#6(...)`
  with no tag number.
- Add the negative vectors the source omits to `../examples/`: the three `-0.0`
  spellings, an integral float at each width, a misordered map, a duplicate-key
  map, a non-NFC text string, `f7`, `f8ff`, and the four indefinite-length
  heads. Table 4 has 11 rows and all 11 are numeric; **nothing in Appendix A
  exercises Sections 2.1, 2.3, 2.4, 2.6 or 2.7 at all.**
- Decide whether this library wants a derived JSON Schema here. Pass 1 says no,
  deliberately: dCBOR's distinctive constraints — byte strings, the canonical
  NaN, integers beyond 2^53, map key *order* — have no JSON counterpart, so a
  JSON Schema would restate only the parts that are not dCBOR. Recorded so a
  later pass does not read the absence as an oversight.
- The `.dcbor` / `.dcborseq` usage sketch in the CDDL is commented out, because
  no tool implements an operator that Section 6 only *requests* IANA register.
  Uncomment it if a tool that does appears.
