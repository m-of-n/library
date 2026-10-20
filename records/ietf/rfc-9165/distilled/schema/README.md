---
record: rfc-9165
kind: schema
title: "rfc-9165 — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

RFC 9165 ships **no grammar of its own for CDDL.** It adds six names to CDDL's
one declared extension point and defines them in prose. The one formal
production it states in its own voice belongs to the *embedded* metalanguage,
not to CDDL: `CRLF = %x0A / %x0D.0A`.

So this directory holds three kinds of thing: the document's **own CDDL
figures** (verbatim, because they are the only formal statement of how the
operators compose), the **ABNF the figures carry inside CDDL string literals**
(verbatim, and separately, because it is a second formal language), and **two
derived files** — the ABNF after the document's own operators have been applied
to it, and the six operators rendered as data.

The filename carries the derived/verbatim distinction and `bin/validate`
enforces it: a `.derived.` infix is mandatory on anything this library wrote,
and an unmarked name asserts the source's own bytes (`docs/extraction.md`,
"Derived vs verbatim — the filename carries it"). Each file repeats the claim in
its own header.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `control-operators.derived.yaml` | derived | **the central artifact of this record.** All six operators as data: target, controller, result type, predicate, control kind, class, IANA entry, per-operator gaps, and the comparison against `rfc-8610`'s fourteen. Also the `cross_field_constraints` verdict and the `operator_classes` taxonomy | the predicates are **our rendering of prose**. RFC 9165 ships no formal semantics for any of the six, and the IANA registry carries only a name and a reference |
| `embedded-abnf.abnf` | **verbatim** | the **four** ABNF regions the document prints: §3's `CRLF` redefinition (its own voice), Figure 3/4's `cbor-tags-oid` rule-list, and Figure 5's `rfc3339` and `rfc5234-core` rule-lists | **it will not parse as it stands,** and that is the point — see below. It is also not a complete ABNF of anything: `rfc5234-core` is abbreviated by the source itself ("; abbreviated here") |
| `embedded-abnf-dedented.derived.abnf` | derived | the same ABNF **after the document's own operators have run** — the three controller strings a tool actually parses, produced by applying §2.3's two-step dedent and §2.2's concatenation. Carries the closure and case-sensitivity results | it is **not** the source's bytes. Cite `embedded-abnf.abnf`. The dedent is our implementation of the source's algorithm, not a reference one |
| `computed-literals.cddl` | **verbatim** | Figures 1 and 2 — the `.plus` and `.cat` examples, margin intact | Figure 2's asserted equality is **conditional on the source file's line endings**; see below |
| `dedenting.cddl` | **verbatim** | Figure 3 — `.abnfb` over a `.det`-composed controller | — |
| `dedenting-result.cddl` | **verbatim** | Figure 4 — the source's own rendering of Figure 3's computed result. Separate file because it **redefines** `oid` | spells a text-string result in byte-string notation; see below |
| `abnf-in-cddl.cddl` | **verbatim** | Figure 5 — the only full worked example, defining CBOR tag 1004 and tag 0 from RFC 3339's ABNF | — |
| `features.cddl` | **verbatim** | Figures 6–9 — the four `.feature` idioms, in four regions. They define disjoint rule names, so unlike Figures 3 and 4 they share a file | **Figure 6 does not parse as CDDL**; see below |
| `registry-tables.txt` | **verbatim** | Table 1 (name and purpose) and Table 2 (name and reference), with their captions and centring | Table 2 is the **whole** of a registry entry. No target type, no controller type, no semantics, no operator class |
| `README.md` | — | this file | — |

**15 verbatim regions across 7 files, each carrying its source line range and a
sha256 of exactly those lines.** All 15 were re-verified byte-for-byte against
the cache by a checker that parses the BEGIN/END markers and re-slices
independently of the generator: 15/15 exact, 15/15 digests verify, and for all
15 the digest equals that of the same lines `rstrip`ped, which independently
proves **no line in any region carries trailing whitespace.**

**Three regions are nested inside two others, deliberately.** `embedded-abnf.abnf`
region A-2 (lines 211–214) falls inside `dedenting.cddl` region F-3 (207–215),
and regions A-3 (323–340) and A-4 (344–345) both fall inside `abnf-in-cddl.cddl`
region F-5 (312–346). That is not duplication: the ABNF *lives inside* the CDDL
byte-string literals, and the two languages need separate files because a tool
for one cannot read the other. Twenty-four source lines are covered twice and
127 distinct source lines in all. (Pass 1 said "two regions inside two others"
and then named A-4's non-adjacency to A-3 in the next paragraph; A-4 is inside
F-5 for the same reason A-3 is. Corrected by the verify pass.)

**A-3 and A-4 are not adjacent in the source** and are never presented as one
run. Source lines 341–343 fall between them and are CDDL, not ABNF — `' .det
rfc5234-core` closes one literal and `rfc5234-core = '` opens the next.

## Why the verbatim ABNF file cannot be parsed, and why that matters

RFC 5234 is line-oriented: a line indented relative to its rule is a
*continuation*, so an indented rule-list collapses into a single rule. The
RFC prints its ABNF inside CDDL literals, inside figures, inside a three-column
body margin, so every line is indented.

For `rfc-8610` the equivalent problem was a presentation accident and the
dedented companion was a convenience. **Here it is the specification's own
semantics.** Removing the indentation is exactly what `.det` does, and §2.3
defines it to the character. So `embedded-abnf-dedented.derived.abnf` is not a
reformatting of the verbatim file — it is the verbatim file with the document's
own operator applied, and it is what a conforming tool holds in memory.

**Dedenting is margin-invariant** (OURS). Under a uniform margin every line of a
literal shifts by the same amount and §2.3 step 1's minimum shifts with it, so
dedenting the margin-bearing form and the author's flush-left form give
identical bytes. That is what lets a figure printed inside an RFC's body margin
be a correct example rather than an approximation, and it is why the derived file
can be built from the margin-bearing capture without un-indenting it first.

## What was checked mechanically

- **Rule closure, both controllers, and it holds.** §3 requires it —
  "(Note that all rules referenced need to be defined in each ABNF operator
  controller string -- there is no implicit import of core ABNF rules from
  [RFC5234] or other rules.)" — and the document satisfies it.
  `cbor-tags-oid`: 4 rules, 0 undefined, closed from both `oid` and `roid`
  (3 of the 4 reachable from each selector). Figure 5's
  `rfc3339 .det rfc5234-core`: 14 rules (13 plus `DIGIT`), 0 undefined, closed
  from `full-date` (**5** of the 14 reachable — `full-date`, `date-fullyear`,
  `date-month`, `date-mday`, `DIGIT`) and from `date-time` (all 14) —
  **closure holds across the `.det` join**, which is the thing worth checking,
  and the source's own "; abbreviated here" elision breaks nothing because
  `rfc3339` references no core rule other than `DIGIT`. (Pass 1 said "4 rules
  reachable" from `full-date` while counting `date-time`'s reachable set
  inclusively at 14; the two were counted differently. Re-derived and made
  consistent by the verify pass: both counts now include the selector.)
- **Case sensitivity.** The only quoted strings containing letters anywhere in
  this ABNF are `"T"` and `"Z"`, and **no RFC 7405 `%s` or `%i` prefix appears.**
  RFC 5234 §2.3 makes quoted strings case *insensitive*, so
  `Tag0 = #6.0(text .abnf date-time)` admits `1990-12-31t23:59:60z`.
  **Re-derived and then EXECUTED by the verify pass.** The census is
  comment-invariant: the composed `date-time` controller holds ten quoted
  strings — `"."`, `"+"`, `"-"`, `":"`, `"Z"`, `":"`, `":"`, `"-"`, `"-"`,
  `"T"` — and the same ten whether or not ABNF comments are stripped, since no
  comment in it contains a quotation mark; two bear letters; `%` occurs only in
  `%x30-39`. The composed `cbor-tags-oid` controller holds **no** quoted string
  at all, so the finding is Figure 5's alone. Then the composed rule-list was
  loaded into the recogniser and matched against instances: `date-time` accepts
  `1990-12-31t23:59:60z`, `1990-12-31T23:59:60z` and `1990-12-31t23:59:60Z` as
  well as the all-upper form, and **rejects** `1990-12-31x23:59:60Z` and
  `1990-12-31T23:59:60` (no offset) — so the acceptance is case folding and not
  a permissive parser.
- **Lower-case hex is fine.** `%x00-7f`, `%x81-ff`, `%x80-ff` are valid because
  RFC 5234's `HEXDIG` is built from case-insensitive quoted strings.
- **Round-trip.** Re-applying our dedent to the verbatim regions reproduces the
  derived file exactly; the derived file's three blocks were re-derived a second
  time by an independent script.

## What `rfc-8610` must absorb

**Already fixed, by another lane, while this pass was running — and the
convergence is the point.** `rfc-8610/distilled/schema/control-operators.derived.yaml`
used to state, in `syntax.extension_point.policy_note`: *"All names other than
the fourteen below are Unassigned."* Present tense, no date qualifier, and false
as a statement of registry state. This extraction reached that finding from
RFC 9165 alone — six names assigned in December 2021 — and **the `rfc-9741`
extraction reached it independently and more completely on the same day**
(commit `9adcb8d`, library#39 Tier 2), **This record did not read RFC 9741**, so that lane's finding is cited from
its artifact and not from the source: it records RFC 9741 §1 as saying "RFCs
have added to this extension point in both an application-specific [RFC9090]
and a more general [RFC9165] way." and §4 as registering fourteen more. That lane has already removed the sentence and put
`registry_state_is_not_rfc_8610` in its place, so nothing is owed here.

**Two of the four Tier 2 lanes finding the same false claim in a
`profile: full` record, from two different sources, is exactly what
`rfc-8610`'s gate existed to produce.**

Everything else in that file survives. Its table of fourteen is correct *as a
statement about RFC 8610*; no name registered here collides with any of the
fourteen, and this document redefines none of them. The two documents define **20 distinct operators** between them — which is **not** the registry total, since RFC 9165 claims nothing about the registry beyond its own six entries and RFC 9090 (July 2021) predates it. Current registry state is `records/ietf/rfc-9741`'s to state.

## Defects and discrepancies, recorded not repaired

Reported here because `docs/extraction.md` forbids repairing them in a verbatim
file.

1. **`element` versus `elements` — a real fork in the specification.** §3's
   structure rule requires the controller to begin with "one valid "element""
   (singular). The sentence immediately before it names the production
   differently: "ABNF defines a list of rules, not a single expression (called
   "elements" in [RFC5234])". In RFC 5234 these are different productions of
   different strength — `elements = alternation *c-wsp`, whereas
   `element = rulename / group / option / char-val / num-val / prose-val`. Under
   the narrow reading a selector of `DIGIT DIGIT` or `"a" / "b"` is ill-formed;
   under the wide reading it is fine. **Every selector this document prints is a
   bare rulename** (`full-date`, `date-time`, `oid`, `roid`), so no example
   distinguishes the readings and a tool author must choose. The distinguishing
   fixture pair is in `../examples/README.md`.

   **Verify pass: both halves hold, with three refinements and one limit.**
   The selector census is complete and mechanical: the source mentions `.abnf`
   or `.abnfb` on fourteen lines, of which **five are applications** — source
   lines 207, 208 and 225 (Figures 3 and 4) and 313 and 315 (Figure 5) — and
   the rest are the abstract, the two registry tables and §3's prose. Those
   five carry exactly **four distinct selectors**, `oid`, `roid`, `full-date`
   and `date-time`, every one a bare rulename. (i) A sharper witness than `"a" / "b"` is **`4DIGIT`**:
   a `repeat` prefix makes it a `repetition`, which `elements` reaches through
   `alternation`/`concatenation` and `element` does not reach at all. (ii) The
   fork costs an author nothing, because `group = "(" *c-wsp alternation
   *c-wsp ")"` **is** an `element`, so parenthesising any `elements` makes it
   an `element`; the fork bites a *tool* reading someone else's ABNF, not a
   specification writer. (iii) The two readings are therefore not different
   *expressive power* but different *tolerance*, which is why no example can
   distinguish them. **The limit:** this library holds **no `rfc-5234` record
   and no cached copy of RFC 5234**, so the two productions quoted above are
   the only part of this finding that cannot be checked against a source here.
   They are correct as written, but that is testimony, not verification —
   ingesting RFC 5234 is what would close it, and until then this is the one
   load-bearing claim in the record resting on an uncached document.
2. **Figure 4 spells a text-string result in byte-string notation.** §2.2's
   result rule — which §2.3 inherits by "works like .cat" — makes the result of
   `"oid" .det cbor-tags-oid` a **text** string, because the target `"oid"` is a
   text string. Figure 4 renders it as `'oid…'`, a byte-string literal. The two
   are interchangeable *as an `.abnfb` controller*, since `rfc-9165#R-0048`
   admits either and coerces a byte string to text, so the figure is equivalent
   in **effect** and not in **type**.
3. **Figure 6 does not parse as CDDL, and this is now EXECUTED, not argued.**
   `bar = ...` and `baz = ...` use `...` as a prose placeholder — the trailing
   comment says so — but CDDL's `...` is only a range operator:
   `rangeop = "..." / ".."`, and no `type2` alternative begins with a dot.
   Pass 1 reasoned this from the grammar. The verify pass **ran** it: an Earley
   recogniser built from `../../../rfc-8610/distilled/schema/cddl-dedented.derived.abnf`
   (this library's own, written for the pass — no third-party CDDL tool is
   installed here) rejects Figure 6 and **stalls at the first `.` of `bar = ...`,
   source line 382 column 9**. Replacing the two `...` with any real type makes
   the figure parse, so the `...` is the sole cause; `a = ...` and `a = (...)`
   fail while `a = 1 ... 2` and `a = 1..2` parse. The recogniser was validated
   first: it accepts the other **eight** of the document's nine figures,
   including Figure 5 whole, and ~11 KB of RFC 8610's own CDDL
   (`prelude.cddl`, `prelude-json-subset.cddl`, `ijson-types.cddl`,
   `reputon-compact.cddl`, `reputon-verbose.cddl`), so the rejection is the
   grammar's and not the tool's. Recorded as `rfc-9165#V-0013`,
   `expect: indeterminate`.
4. **Figure 2's asserted equality is conditional on line endings, and the
   condition is stated only in a code comment.** "; on a system where the
   newline is \n, is the same string as:". RFC 8610's `BCHAR` admits
   `CRLF = %x0A / %x0D.0A`, so a multi-line byte-string literal carries whatever
   bytes the source file has; under CRLF line endings `c` is
   `"foo\r\n  bar\r\n  baz\r\n"` and the equality fails. **A computed literal is
   therefore not portable across source-file line endings,** and nothing in the
   document's normative text says so.
5. **`CRLF` is redefined — and here it is *declared*.** `CRLF = %x0A / %x0D.0A`
   admits a bare LF where RFC 5234's core rule is `%x0D %x0A`. This is the
   **same redefinition** that `rfc-8610`'s extraction recorded as source defect
   #7 in RFC 8610 Appendix B, where it "hides in plain sight". RFC 9165 makes it
   openly, scopes it precisely ("the syntax of ABNF itself (_not_ the syntax
   expressed in ABNF!)"), and calls it "customary for ABNF". **So the substance
   of that rfc-8610 defect is deliberate community practice, by the same
   author; what remains defective there is that it is undeclared.** That
   narrows the rfc-8610 finding rather than withdrawing it.
6. **The abbreviated `rfc5234-core`.** "; abbreviated here" means Figure 5 is
   not a complete reusable core-rule set. It happens not to matter — closure
   holds — but anyone lifting `rfc5234-core` into their own schema is lifting one
   rule.

## Not held here

No `$id` is claimed by any file: nothing here is a JSON Schema. The verbatim
tables are held in this directory rather than in an IANA record because this
library has **no record for the Concise Data Definition Language (CDDL)
registry**; `rfc-8610`'s schema README makes the same call about §6.1's table and
says that if such a record is created, the verbatim tables belong there.

## State

**Passes 1 and 2 of 3** — extract and verify. Cross-check has not run and no
`reviewed_by` is signed. Every mechanical claim above was produced by scripts
run against `.cache/rfc-9165.txt`, and the verify pass recomputed all of them
with its own implementations rather than re-running pass 1's: 15/15 regions
byte-identical with digests verifying, the dedent re-derived from scratch, and
Figure 6, the case-insensitivity census and G-44 **executed** against RFC 8610's
Appendix B with an Earley recogniser written for the pass. **Nothing has been
run through a third-party CDDL or ABNF implementation**, none being installed
here — so that recogniser settles structure, not conformance. Every semantic
claim still rests on the source's prose.
