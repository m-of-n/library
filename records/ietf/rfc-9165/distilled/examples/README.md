---
record: rfc-9165
kind: examples
title: "rfc-9165 — examples and test vectors"
extracted: "2026-10-19"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` — **18 vectors, `rfc-9165#V-0001` … `rfc-9165#V-0018`, in source
order with no gaps.** 17 `valid`, 1 `indeterminate`, 0 `invalid`.

RFC 9165 is a document about a notation, so every example in it is CDDL or ABNF
text rather than bytes. The vectors are therefore schema fixtures first. The
document prints **no instance anywhere** — not one data item, not one hex
string — so where a vector carries an `instance` it is marked as such in its
`provenance`.

## Provenance, per vector

Four of the eighteen are not printed anywhere in the document, so provenance is
stated on every vector rather than assumed:

| provenance | n | what it means |
|---|---|---|
| `SOURCE CDDL` / `SOURCE ABNF` | 13 | the document's own bytes, lifted by line range |
| `SOURCE PROSE` | 1 | the document's own bytes, from running prose rather than a figure (V-0015's misspelled label) |
| `COMPUTED BY US` | 3 | produced by applying the **document's own rules** — §2.3's two-step dedent and §2.2's concatenation — to source line ranges. V-0005, V-0011, V-0012 |
| `OURS` | 1 | an instance we wrote to exhibit a defect the source states in its own words. V-0018 only |

**Why the three computed vectors exist, and why they are not padding.** The
operators in this document *construct strings*, and the strings they construct
are what a tool must actually parse. The document computes **one** of them —
Figure 4, the result of Figure 3's first rule — and stops. V-0005 is the second
rule's result by the same two rules; V-0011 and V-0012 are Figure 5's two
composed ABNF controller strings, which no figure prints. Without them the
record holds the inputs to `.det` and not its outputs, and the outputs are the
fixtures.

All three were **re-derived independently** of the generator, from the cache, by
a second script: each reproduces byte-for-byte. V-0004 was additionally checked
the other way round — applying our implementation of the source's dedent rule to
lines 211–214 and concatenating reproduces the source's **own** Figure 4
literal, which is a check on our reading of the algorithm rather than on our
arithmetic.

## How a vector is built

- **`cddl` / `abnf`** — lifted from the cached source **by line range, by
  script, never retyped.** The only transformation is removal of the common left
  margin, which a YAML block scalar performs in any case. Relative indentation
  inside a block, the RFC's own comments, and the RFC's own spelling (including
  the lower-case hex in `%x00-7f`) are the source's. **All ten declared source
  ranges re-slice byte-identically**, and each range is a contiguous run of the
  source — no vector joins two non-adjacent ranges, and **none crosses a page
  frame, because this source has none.**
- **`instance`** — only on V-0015 and V-0018, and `provenance` says whose it is.
- **`matches`** — what the schema admits, in one line.
- **`expect`** — `valid`, `invalid`, or `indeterminate`.
- **`equivalence`** — on the two vectors where the source asserts two spellings
  denote the same type (V-0002, V-0004).
- **`violates`** — on the two negatives.
- **`notes`** — the source's own sentences in quotation marks; anything marked
  **OURS** or **CHECKED BY SCRIPT** is this library's reading or arithmetic.

## The one `indeterminate` vector is the source's own fault, not a hedge

**V-0013 (Figure 6)** carries `expect: indeterminate` because **the figure does
not parse as CDDL.** `bar = ...` and `baz = ...` use `...` as a prose
placeholder — the trailing comment says so outright, "complex stuff that
doesn't all need to be in the detail" — but in CDDL `...` is only a range
operator: RFC 8610 Appendix B gives `rangeop = "..." / ".."`, and no `type2`
alternative begins with a dot, so a bare `...` cannot stand as a type. Marking
the figure `valid` would assert it parses; marking it `invalid` would assert the
source wrote a broken example rather than a sketch. The precedent is
`rfc-8610#V-0037`, which is `indeterminate` for the same discipline — the source
declines to settle it, so the vector does not settle it either.

## Both negatives are the source's own, and both are `expect: valid`

That is not a mistake. **In each case the validity *is* the finding.**

- **V-0015** — the misspelled label `organisation` against Figure 7. The source
  names it as the cost of the idiom: "Leaving the extension point in but not
  marking its use as special would render mistakes (such as using the label
  "organisation" instead of "organization") invisible." The wildcard admits it,
  so it is valid; `.feature` lets a tool *report* it and never reject it.
- **V-0018** — an instance carrying both spellings of SenML's `v` against
  Figure 9. The source concedes the gap in its own words: "The language
  currently has no way to enforce mutually exclusive use of features, as would
  be needed in this example." The instance is ours because the source states
  the defect without printing an instance that exhibits it, and `provenance`
  says so.

So this record has **no vector that a conforming tool must reject.** That is a
true statement about the document and worth saying plainly: every one of its
examples is meant to match.

## Violations the document does not print — candidate fixtures, OURS

Listed here rather than in `vectors.yaml`, because **none of them is the
source's example** and `vectors.yaml` holds only what the document prints or
what the document's own rules compute. Each is a reachable violation of a
stated `MUST`, and each is the fixture a tool's negative test would need:

| would violate | a fixture that reaches it | note |
|---|---|---|
| `rfc-9165#R-0016` | `a = "x" .plus 1` | parses under `ctlop = "." id`; forbidden only by prose |
| `rfc-9165#R-0016` | `a = 1 .plus "x"` | the controller side of the same rule |
| `rfc-9165#R-0023` | `a = 1 .cat "x"` | a numeric target for a string operator |
| `rfc-9165#R-0026` | `a = "x" .cat h'ff'` | text target, byte controller holding a byte that is not valid UTF-8 — the **one reachable violation** of the UTF-8 rule, since concatenating two complete valid strings cannot produce an invalid one |
| `rfc-9165#R-0047` | `a = text .abnf 1` | a numeric controller |
| `rfc-9165#R-0048` | `a = text .abnf h'ff'` | a byte-string controller that is not valid UTF-8 |
| `rfc-9165#R-0050` | `a = text .abnf 'DIGIT\nDIGIT = %x30-39'` | a selector that is a `rulename` — valid. Contrast `'DIGIT DIGIT\n…'`, a `concatenation`, which is ill-formed under `element` and well-formed under `elements`; **this is the pair that distinguishes the two readings of the source's own wording.** See `../schema/README.md` |
| `rfc-9165#R-0055` | `a = text .abnf 'x\nx = 1*DIGIT'` | `DIGIT` is referenced and not defined — closure fails, with no core-rule import to save it |

The last two are the ones worth writing first: the `element`/`elements`
ambiguity is a real fork in the specification, and closure is the rule a tool is
most likely to omit because ABNF libraries usually ship the core rules by
default and this document forbids relying on them.

## Which production each vector is an instance of — cross-check, EXECUTED

**Added 2026-10-20 (cross-check pass).** FX-1's cross-check asks that every
example validate against the schema. Running all 18 through the recogniser
showed the vectors sit at **three different productions**, which the file had
not recorded, and turned up one mis-keyed block.

| production | n | vectors |
|---|---|---|
| CDDL `cddl` — a whole document | 9 | V-0001 V-0002 V-0003 V-0004 V-0010 V-0013 V-0014 V-0016 V-0017 |
| CDDL `type1` — a type expression quoted in prose | 3 | V-0006 V-0007 V-0008 |
| ABNF controller string | 4 | V-0005 V-0009 V-0011 V-0012 |
| instance, not schema text | 2 | V-0015 V-0018 |

- **8 of the 9 whole documents parse**; the ninth is `V-0013`, which is
  `indeterminate` *because* it does not (Figure 6, source line 382 column 9).
  That reproduces the verify pass's result on an independent run.
- **The three prose one-liners parse as `type`, `type1` and `grpent`** and as
  none of `cddl`, `rule`, `type2` or `memberkey`. They are well-formed CDDL at
  the production the source uses them at. A reader who ran them through a tool
  expecting a document would get a spurious failure, which is why the table is
  here.
- **`V-0005` was keyed `cddl:` and is not CDDL.** It parses as *no* CDDL
  production at all, and loads cleanly as ABNF — 4 rules, 0 undefined, 3 of the
  4 reachable from the selector `roid`. Its own `matches` calls it "the
  controller string", and its two sibling `COMPUTED BY US` blocks V-0011 and
  V-0012 key the same kind of object `abnf:`. **Re-keyed `abnf:`; the bytes are
  unchanged.** Prose right, data wrong — see the vector's own `[correction]`.
- **Closure re-derived from the vectors themselves**, not from the schema
  files: V-0011 (`date-time`) reaches **14 of 14**, V-0012 (`full-date`)
  reaches **5 of 14**, 0 undefined in both. That is the verify pass's corrected
  count, reproduced by a third implementation.
- **The two instance-bearing vectors are the honest limit.** `V-0015`'s
  `{"organisation": "ACME"}` against Figure 7 and `V-0018`'s `{"v": 1, 2: 1}`
  against Figure 9 need a CDDL **validator**, not a recogniser: the schemas
  parse and the instances are well formed, but the *match* is argued from
  RFC 8610's map-matching rules, not run. No third-party CDDL implementation is
  installed here. This is the one part of deliverable 4 that is reasoned rather
  than executed, and it is the source's own examples that make it so — the
  document prints no instance anywhere.

## Mechanical state

Passes 1, 2 and 3 of 3 — extract, verify and cross-check. All of the
following were checked by script against `.cache/rfc-9165.txt`, and every one
was **recomputed by the verify pass with its own implementation** rather than by
re-running pass 1's; the cross-check pass then re-ran the starred ones a third
time, independently again:

- **\*** 18 vectors, ids `V-0001`–`V-0018` contiguous with no gaps, parsing
  identically under both `bin/_record_yaml` and `bin/_yaml`.
- **\*** 10 of 10 declared source ranges re-slice byte-identically after
  **common**-margin removal, and every range is contiguous in the raw source.
  The common margin is not a constant: the RFC's body margin is 3 columns, but
  a figure adds its own, so `V-0009`'s single line carries **6**. A re-slicer
  that assumes 3 reports a false mismatch on that one vector — noted because
  the cross-check pass wrote one and had to fix it, not the record.
- **\*** 3 of 3 `COMPUTED BY US` blocks re-derive exactly from the source by the
  document's own §2.3 dedent and §2.2 concatenation. **The verify pass found
  V-0011 and V-0012 one line short** — the `.det` join of Figure 5's two
  literals produces a blank line before `DIGIT`, which both blocks omitted
  although V-0011's own `notes` asserted it. Fixed; all three now re-derive
  byte-for-byte against an independent dedent. **The cross-check pass re-derived
  all three a third time** from a dedent written from §2.3's two numbered steps,
  locating the three byte-string literals by scanning for `<name> = '` and its
  closing quote rather than trusting any declared line range: **3 of 3 exact,
  including the trailing newline**, and the blank line before `DIGIT` present in
  both Figure 5 blocks. It also re-confirmed the algorithm the other way round —
  the same `det()` reproduces the source's **own** Figure 4 literal exactly.
- V-0004's literal content equals our computation of `"oid" .det cbor-tags-oid`,
  which checks our reading of the algorithm against the source's own result.
  **The verify pass made the condition explicit:** the equality holds only once
  the RFC's three-column body margin is removed from Figure 4 as well as from
  Figure 3. Dedenting is margin-invariant in its *operand* — which is what makes
  Figure 3 a correct example — but not in its *result*, which is flush left by
  construction, so Figure 4 as printed is not literally its own answer.
- The 3 prose-quoted one-liners (V-0006, V-0007, V-0008) are each present in the
  whitespace-normalised source.
- 25 further quotations in `notes` fields hand-enumerated and verified contiguous
  (the automated pass cannot resolve them: the source's own text is full of
  nested quotation marks).
- **\*** ABNF closure re-derived for every controller: `cbor-tags-oid` 4 rules / 0
  undefined / closed from both selectors (3 of the 4 reachable from each);
  Figure 5's composition 14 rules / 0 undefined / closed from both selectors,
  **across the `.det` join** — 5 of the 14 reachable from `full-date`
  (`full-date`, `date-fullyear`, `date-month`, `date-mday`, `DIGIT`) and all 14
  from `date-time`. Pass 1 recorded the first of those two as 4, counting it
  exclusively while counting the second inclusively; corrected. **Reproduced a
  third time by the cross-check pass**, off the vectors rather than the schema
  files: 5 and 14, 0 undefined.
- **\*** The case-insensitivity census re-derived, and then **executed**: the
  composed `date-time` rule-list loaded into an Earley recogniser matches
  `1990-12-31t23:59:60z` and rejects `1990-12-31x23:59:60Z`, so the acceptance
  is case folding and not a permissive parser. Re-run by the cross-check pass:
  `1990-12-31T23:59:60Z` and `1990-12-31t23:59:60z` accepted,
  `1990-12-31x23:59:60Z` and `1990-12-31T23:59:60` (no offset) rejected.
  **But see `../schema/README.md`'s `[correction]` of 2026-10-20: the census is
  verified and the premise it is applied to is testimony**, because RFC 5234 and
  RFC 7405 are both uncached here and the recogniser folds case by construction.
- **\*** **Figure 6's non-parse executed** rather than argued. The recogniser
  stalls at the first `.` of `bar = ...`, source line 382 column 9, and accepts
  the other eight figures — so `V-0013`'s `indeterminate` stands on a run, not a
  reading. Reproduced by the cross-check pass at the same line and column.

**Nothing here has been run through a third-party CDDL or ABNF implementation** —
none is installed in this environment. The dedent implementation, the closure
checker, the case-sensitivity census and the CDDL recogniser are this library's
own, and they settle **structure, not conformance**. Items marked **\*** were
computed three times, by three passes, with three implementations.
