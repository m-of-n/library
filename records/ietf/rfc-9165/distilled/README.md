---
record: rfc-9165
kind: index
title: "rfc-9165 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: all three passes complete — extract, verify, cross-check.
`distillation.profile: full` against `standard: FX-1`.** **No `reviewed_by` is
signed anywhere**, so these artifacts are readable but not yet buildable-on;
pass 4 is a person's. `record.yaml`'s `passes[*].note` is the full account of
each pass.

The verify pass upheld all four of pass 1's self-flagged claims, executed three
of them against RFC 8610's grammar rather than arguing them, and fixed six
defects of our own — the largest being a blank line the `.det` join produces
that three derived blocks omitted while their own prose asserted it.

**The cross-check pass found seven more, all ours.** Five are the same family as
pass 2's — a claim stated in prose that the data did not carry — and **two are
propagation failures**: a correction pass 2 made in one artifact that never
reached another artifact stating the same claim. The `rfc-9741`,
`draft-ietf-cbor-cddl-modules` and `rfc-9682` cross-checks each found exactly
that, so it was swept for deliberately here.

**The two propagation failures, listed first because they are the ones a reader
would otherwise still believe:**

- **The 4-vs-5 reachability miscount survived in `V-0010`'s notes.** Pass 2 fixed
  it in `schema/README.md`, `schema/embedded-abnf-dedented.derived.abnf`,
  `examples/README.md` *and* `V-0012`'s notes — four artifacts — and missed the
  fifth, where `closed from both `full-date` (4 rules reachable) and `date-time`
  (all 14)` is the exclusive-against-inclusive pairing pass 2 itself named.
  Re-derived at **5 of 14** and corrected.
- **The non-partition survived in this file**, which stated the classes as bare
  set inclusion — under which restrictive and annotative overlap, because
  equality is a subset. Pass 2 fixed that with `proper` plus a partition
  criterion in `control-operators.derived.yaml` and `summary.md`; it did not
  reach the index. Corrected above.

The other four of pass 2's corrections were checked across every artifact that
states them and **all propagated cleanly**: the `.det` blank line, the "three
regions nested inside two others" count, "four years" (now only inside
`design-notes.md`'s own correction note), and the hyphenated `left-hand`.

**And the five of the same family as pass 2's:**

1. **A multi-line YAML flow sequence** in `schema/control-operators.derived.yaml`
   — the only one in this library's YAML — which `bin/_record_yaml` could not
   parse at all and which `bin/_yaml`, the reader `bin/validate` uses, parsed
   **silently wrong**, turning the first colon inside the G-28 finding into a map
   key. The verify pass's own note claims "every YAML parsing identically under
   both loaders"; it did not. Respelled as a block sequence.
2. **"8 verbatim files"** here and in `record.yaml`, against `schema/README.md`'s
   7. Seven is right; the eighth was `schema/README.md` itself.
3. **`V-0005` was keyed `cddl:`** and is an ABNF controller string — its own
   `matches` says so and its two siblings key the same object `abnf:`. Found by
   *running* it: it parses as no CDDL production and loads cleanly as ABNF.
4. **The maximal-munch gap was filed as the sixth gap this document adds**, in a
   key headed `adds_new_ones_of_its_own`, while the item's own last sentence said
   it belongs to RFC 8610. Recounted to five and moved; see below.
5. **The uncached-source limit named one claim where there are two**, and the
   unnamed one is this record's headline finding. See *The RFC 5234 limit*.

It also attacked the largest unexercised claim in the record — `messages.yaml`'s
five-phase evaluation order — and **split it**: three of the four phase
boundaries do have a basis in the source, one does not, and the one that does
not **changes verdicts** on a fixture the pass wrote and executed. All of that
is now in `messages.yaml` under `boundaries` and `schedule_sensitivity`.

Source: RFC 9165, *Additional Control Operators for the Concise Data Definition
Language (CDDL)*, C. Bormann, Standards Track, December 2021.

**Read this before using anything here.** `bin/bcp14-count` reports exactly
**5** BCP 14 keyword occurrences in 23 KB, all five the bare keyword `MUST`
(source lines 141, 179, 182, 279, 280), and **not one of them is an obligation
on an actor** — every one is a type-admissibility or well-formedness rule on an
operator's operand. That is expected and correct. **This is a grammar
extension**: it adds six entries to CDDL's one declared extension point, and
its normativity is carried by *operator definitions and matching rules*, exactly
as RFC 8610's is. The siblings are the calibration: `rfc-8610` carries 2
keywords in 125 KB with 137 of 139 requirements `inferred`, and
`draft-ietf-cbor-edn-literals` carries 10 in 164 KB with 216 of 226 `inferred`.
Here it is **79 of 84 inferred**, each naming in its `field` the phrase,
algorithm step, grammar production or stated absence that carries the force.

## Why this record exists

`rfc-8610` reached `profile: full` carrying a **gate**, in both its
`distilled/README.md` and its `summary.md`: *nothing in that record may be
treated as the current state of CDDL until `rfc-9165`, `rfc-9682`, `rfc-9741`
and `draft-ietf-cbor-cddl-modules` are read.* This is one of the four, and it
closes **the operator-set quarter of that gate and nothing more.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **78 verbatim bullets and 13 reproduced blocks** across 9 locators (§1, §1.1, §2, §2.1, §2.2, §2.3, §3, §4, §5, §6). All 78 confirmed contiguous substrings of the whitespace-normalised source **and** inside the locator's own section range, by section map rather than document-wide; all 13 fenced blocks byte-identical to their declared source line ranges. The 13 blocks are both tables, all nine figures, the dedenting definition and the `CRLF` production |
| requirements | `requirements.yaml` | **84 entries, `R-0001`–`R-0084`, source order, no gaps: 5 stated, 79 inferred.** `source_keyword_count` and `extracted_keyword_count` both 5, with a reconciliation that states the real baseline — a grammar extension's normativity is in its operator definitions — and names what was counted instead. Every `text` was **sliced out of the cache by line range and boundary marker, never retyped.** §1.1's boilerplate is deliberately never quoted: `bin/validate` counts texts with stripping off, so quoting it would add 11 phantom keywords |
| schema | `schema/` | **7 verbatim files in 15 regions, 2 derived** (10 files in the directory, counting this `README.md`, which is neither). *[correction] 2026-10-20 (cross-check pass): this said 8. `schema/README.md` said 7 and 7 is right — the eighth was `README.md` itself, which `docs/extraction.md` excludes from the convention and which asserts nothing about its own bytes.* The central artifact is `control-operators.derived.yaml`: all six operators as data, in Table 2's registry order, with target, controller, result type, predicate, control kind, class and per-operator gaps — written with `rfc-8610`'s field names so the two read as one table of twenty operators. All 15 verbatim regions re-verified byte-for-byte with per-region `sha256`, independently again by the verify pass, and for all 15 the digest equals that of the same lines `rstrip`ped, proving no trailing whitespace. Three of the 15 are nested inside two others by source line range — A-2 in F-3, A-3 and A-4 in F-5 — because the ABNF lives inside the CDDL literals. See `schema/README.md` |
| messages | `messages.yaml` | **13 constructs** — the 6 operators, 3 string structures, 1 operation, 3 idioms — and a **5-phase evaluation order**, which is the part a tool gets wrong. The order is **ours**, and the cross-check pass gave it **per-boundary provenance**: 1→2 and 2→3 forced by the document's own Figures 1 and 5, 4→5 forced by §4's own words ("may mark **the instance**", "the label (map key) **actually used**"), and **3→4 forced by nothing** — with an executed fixture on which the two schedules disagree. The only ordering statement in the whole source is *inside* `.det`. `constrained_by` **is** populated here, unlike in `rfc-8610` where the file header states it is omitted throughout: 62 distinct requirement ids referenced, **0 dangling** |
| examples | `examples/` | **18 vectors, `V-0001`–`V-0018`, source order, no gaps.** 17 `valid`, 1 `indeterminate`, 0 `invalid`. Provenance is explicit per vector: 14 the source's own bytes by line range, 3 `COMPUTED BY US` from the document's **own** §2.3 dedent and §2.2 concatenation, 1 `OURS`. 10 of 10 declared ranges re-slice byte-identically; 3 of 3 computed blocks re-derive exactly — after the verify pass found `V-0011` and `V-0012` one line short, the `.det` join's blank line before `DIGIT`, and fixed them. See `examples/README.md` |
| design-notes | `design-notes.md` | the operator set as the real target; the cross-field verdict; **eight numbered mappings onto our decisions**, of which five cut against MD-3 and one — `.feature` as a way to declare an invariant the schema cannot check — is the first finding in this library's CDDL chain that goes MD-3's way; 11 source defects; and what this invalidates in `rfc-8610` |

## Not applicable

- **protocol** — **a genuine call rather than an absence, so the reasoning is
  recorded.** This document defines no roles, no peers and no exchange. §4 comes
  closer than anything in `rfc-8610` did: it names a second party, "the process
  requesting the validation", and describes an information flow to it —
  "A CDDL tool may simply report the set of features being used; the control
  then only provides information to the process requesting the validation." But
  that is a **single-party tool invocation returning a result to its caller**,
  not an exchange between peers. The speculative enable/disable interface —
  "One could also imagine a tool that takes arguments, allowing the tool to
  accept certain features and reject others (enable/disable)" — is tool
  *configuration*, is explicitly imagined rather than specified, and is
  withdrawn from in the next paragraph. There is no message, no error path
  between parties, no encoding or framing, and no second role that acts **on the
  data** — the requesting process asks and is told, which is an invocation
  contract, not a peer exchange. §6 adds nothing: it
  incorporates RFC 8610's security considerations, whose own §5 says a content
  rules language "does not bring any security issues on itself".
- **state-machine** — no states and no transitions. Matching is a predicate
  over one specification and one instance. The one thing that might look like
  state is `.feature`'s **outcome set**, which this document widens from two
  values to three in effect (invalid / valid / valid-and-using-features-F) — but
  an outcome set is not a lifecycle: nothing persists between instances, no
  instance is *in* a state, and the enable/disable feature set is configuration
  fixed before a run, not state carried through one. The precedent is
  `draft-ietf-cbor-edn-literals`, whose extraction made the same distinction
  about §5.1's three-outcome resolution rule: "what varies between stages of the
  §5 chain is CONFIGURATION, not state". Contrast `rfc-9053`, which **does**
  carry a state machine, because its key-usage counters persist across messages.
  And the document itself forecloses the one construct that would need state:
  "The language currently has no way to enforce mutually exclusive use of
  features, as would be needed in this example."

## The operator set, which is what this record is for

Six operators, **all new**, **none** of them among `rfc-8610`'s fourteen, and
this document redefines none of those fourteen, so the two documents define
**20 distinct operators** between them.

**Twenty is not the registry total.** It is the number of distinct operators RFC 8610 and RFC 9165 define between them. RFC 9165 says only that "IANA has registered the contents of Table 2 into the "CDDL Control Operators" registry of [IANA.cddl]" and makes no claim about what else that registry holds; RFC 9090 (July 2021) predates this document and registers operators of its own. For current registry state read `records/ietf/rfc-9741`. **This extraction asserted 20 as the registry total in its first draft** — the same error it reports below in `rfc-8610` — and the number is scoped here rather than quietly corrected.

| operator | § | kind | class | target | controller | predicate / effect |
|---|---|---|---|---|---|---|
| `.plus` | §2.1 | type control | **constructive** | numeric (`MUST`) | numeric (`MUST`) | constructs `{ t + c }` over the cross-product, result in the target's numeric type, float→int by **floor** |
| `.cat` | §2.2 | type control | **constructive** | string (`MUST`) | string (`MUST`), need not match | constructs `{ bytes(t) ‖ bytes(c) }`, result in the target's string type, text result `MUST` be valid UTF-8 |
| `.det` | §2.3 | type control | **constructive** | string (inherited) | string (inherited) | as `.cat`, each operand **independently dedented** first |
| `.abnf` | §3 | type control | restrictive | either string type | string (`MUST`); byte string `MUST` be valid UTF-8 and is **coerced** to text | target matches iff its **code points** derive from the controller's `element` under RFC 5234 + RFC 7405 |
| `.abnfb` | §3 | type control | restrictive | either string type | as `.abnf` | as `.abnf`, but over **bytes** |
| `.feature` | §4 | type control | **annotative** | any type, no rule stated | none stated; "will usually be a string", or a 2-element array | **nothing.** The target's matching is unchanged; the operator attaches a name for a tool to report |

**All six are type controls, and that is forced rather than chosen:** `ctlop`
occurs only inside `type1`, which is a type production, so **CDDL has no group
control operator syntax at all** — and that is equally true of RFC 8610's
fourteen.

**The class column is ours and the registry records nothing like it.** Three
semantically incompatible kinds of operator now share one flat namespace:
16 of those 20 *restrictive* (the result is a subset of the target, and in
general a **proper** one), 3 *constructive* (the result is computed and in
general disjoint from the target), 1 *annotative* (the result equals the
target). The test that keeps the three disjoint is
`schema/control-operators.derived.yaml`'s `partition_criterion`: **can this
operator reject an instance the target alone would accept?** — restrictive yes,
annotative no, constructive inapplicable because its result is not related to
the target by inclusion at all. A tool that implements all twenty of them
behind one "narrow the target" interface gets four of them wrong.

*[correction] 2026-10-20 (cross-check pass): this paragraph stated the classes
as **bare set inclusion**, under which restrictive and annotative overlap —
equality is a subset, so `.feature` would satisfy both. That is exactly the
defect the verify pass found and fixed with `proper` plus an explicit partition
criterion, and the fix reached `control-operators.derived.yaml` and `summary.md`
but **not this file**. The second of two such misses this pass found; see
`V-0010`'s `[correction]` for the first.*

## Does anything here let CDDL express a cross-field constraint? No

This is what Tier 2 was run for, and the answer is negative. `.plus` is the
operator that looks as though it should change it.

§2 settles it in one sentence: **"For these operators, as with all control
operators, targets and controllers are types."** An operand is a *type
expression in the specification*, not a value in the instance. The document's
only `.plus` example computes over a **generic parameter** bound at
instantiation, and what it produces are **map labels** — "one group for the X
dimension (using 0, 1, and 2 as labels)". Relating two keys at authoring time is
not relating two values at validation time. The route that would smuggle it in
is closed independently: RFC 8610's `occur = [uint] "*" [uint] / "+" / "?"`
takes literal integers, not types.

So `Threshold`'s `1 ≤ k ≤ n` and `n = len(members)` remain inexpressible, and so
does `Validity`'s `not_before ≤ not_after`. **`rfc-8610` item 1 is confirmed,
not overturned.**

**What `.feature` does change** is that the gap can now be *declared in the
schema*, in a form a tool emits on every instance. It does not close the gap —
`.feature` constrains nothing and `V-0018` is the document's own demonstration
that it cannot enforce anything — but the failure mode `rfc-8610` §3e named was
that a reader of `statement.cddl` cannot tell the invariant is unchecked.
`.feature` fixes exactly that. See `design-notes.md` *Mapping* 3.

## Of `rfc-8610`'s 44 grammar gaps, one closes

- **G-35 closes partially** — the only one of the 44 this document touches in
  that direction. RFC 8610 §3.1 states CDDL has no case insensitivity for text
  strings and that regular expressions are the workaround. `.abnf` supplies it
  **by default**, because RFC 5234 §2.3 makes quoted strings case *insensitive*
  and RFC 7405's `%s` is what makes one sensitive. Checked by script: the only
  letter-bearing quoted strings in Figure 5's composed controller are `"T"` and
  `"Z"`, no `%s` or `%i` appears, so `Tag0` admits `1990-12-31t23:59:60z`. **The
  document states none of this**, and under `ARCH-0002 P1` — where a local label
  *is* identity — a case-folded label match is a collision. See `design-notes.md`
  *Mapping* 4.
- **G-11 extends** — per-operator target and controller side conditions the
  grammar cannot express. G-11 is headed "all fourteen operators"; these six add
  six further sets of side conditions, and the grammar constrains none of them.
- **G-28 extends too** — *added by the verify pass*, and it is the mechanism of
  the case-insensitivity finding above. G-28 records that case sensitivity is
  already split between two notations in one grammar; embedded ABNF is a
  **third**, with a third rule. The record stated the consequence (G-35) without
  the cause (G-28).
- **G-44 is corroborated six times over — and is now executed, not inferred.**
  It is `rfc-8610`'s *inference* that `type1` admits at most one
  range-or-control operator, so controls do not chain, against RFC 8610's own
  Table 1 implying they do. RFC 9165 never states the rule and obeys it
  everywhere: `(BASE .plus 1)`, `("oid" .det cbor-tags-oid)`,
  `lhs .cat ("" .det rhs)`, `(text .feature "…")`, `(any .feature "…")`, and
  Figure 5's composition through the named rule `rfc3339`. The two apparent
  counter-examples, Figures 6 and 9, put their controls in separate `type1`s
  across a `/`. The verify pass then **ran** the rule against Appendix B:
  `a = 1 .plus 2 .cat 3` does not parse and `a = (1 .plus 2) .cat 3` does.
- **G-42 and G-43 are untouched.** This document never mentions operator
  precedence, never cites Table 1, and does not touch the cut `^`.
- **Five new gaps**, listed in `schema/control-operators.derived.yaml` under
  `cross_field_constraints.grammar_gaps_touched.adds_new_ones_of_its_own`, for
  any successor to `grammar-gaps.derived.txt`. *[correction] 2026-10-20
  (cross-check pass): this said six. The sixth was the maximal-munch gap, which
  is not one this document adds — see below.*
- **One gap this document only exposed**, now under its own key
  `exposed_in_rfc_8610s_grammar`: an operator name is **not maximally munched**,
  so `a = 1 .plus` parses as `.p` applied to a type called `lus`. The verify
  pass found it; the cross-check pass executed the generalisation the verify
  pass had asserted — `a = 1 .<op>` with **no controller at all** parses for
  **all twenty** registered names, because every one is at least two letters and
  so leaves a valid typename behind. Not one of the twenty is safe.

### Where the maximal-munch gap belongs — decided by the cross-check pass

**The grammar half belongs in `rfc-8610`'s `grammar-gaps.derived.txt`.** Every
production involved — `ctlop = "." id`, `id`, `S = *WS`,
`type1 = type2 [S (rangeop / ctlop) S type2]` — is RFC 8610 Appendix B's; RFC
9165 states no CDDL production at all, its only production being the ABNF
`CRLF`; and the property holds for RFC 8610's own fourteen with no reference to
this document. It is also the exact mirror of **G-27**, which is numbered in
that file and is the one side of the trap Appendix B comments on. Splitting a
symmetric defect across two records leaves a reader of that ledger seeing one
half with no pointer to the other. The precedents both run the same way: the
`registry_state_is_not_rfc_8610` finding and the narrowed CRLF framing were both
reached here and both landed **in** `rfc-8610`.

**The registry half belongs here, and it is this document's own doing.** Exactly
two of the twenty names are proper prefixes of another registered name:
`.cbor` of `.cborseq` (RFC 8610's) and **`.abnf` of `.abnfb` — both registered
by RFC 9165**. For those two pairs the shorter reading is itself a *registered*
operator applied to a plausible typename, so `a = 1 .abnfb` parses as `.abnf`
applied to the type `b` (executed). That turns the hazard from a mis-parse a
tool would reject into a silently well-formed constraint with a different
meaning — and it is a consequence of this document's naming choices, the second
such finding here after §2.3's `.dedcat` aside.

**Not moved by this pass, and the move has three dependents.** `rfc-8610` is at
`profile: full`, another lane may hold it, and a cross-record edit is the owning
agent's to sequence. The cost is concrete: adding this as a **forty-fifth
entry** to `rfc-8610/distilled/schema/grammar-gaps.derived.txt` — or amending
G-27 to cover the controller side — invalidates a tally in three places, because
**44 is written down three times**:

1. `rfc-8610/distilled/schema/grammar-gaps.derived.txt` itself — "44 items,
   G-01 through G-44. 41 carry a checkability verdict";
2. `rfc-8610/distilled/schema/cddl.abnf`, whose header note sums the 44 against
   RFC 9682 as "2 + 1 + 1 + 2 + 38 = 44" — and which *already* carries a
   correction for summing to 42 when it omitted two of them;
3. `rfc-9682/distilled/schema/grammar-gaps-status.derived.txt`, a status sheet
   that asks of *exactly* those 44 "does RFC 9682 change it?" and tallies back
   to 44. It is a status sheet, not a ledger, so it is a **dependent** and not
   an alternative home.

**Amending G-27 rather than adding a forty-fifth entry keeps all three tallies
at 44**, which
is the cheaper of the two routes and is this pass's recommendation. `rfc-9682`
was being edited by another lane while this pass ran. Reported, not repaired,
and the sequencing is upstream of this record.

### The RFC 5234 limit, and why it does not make this `partial`

This library holds **no `rfc-5234` record and no cached RFC 5234** — and no
RFC 7405 either, which the cross-check pass confirmed. **Two** claims rest on
that, not the one the verify pass named: the `element`/`elements` productions,
and **case insensitivity itself**, which is this record's headline finding. Both
are now labelled as testimony at every appearance.

It is nonetheless compatible with `profile: full`, on four grounds:

1. **It is a reference-level limit, not a document-level one.** RFC 9165 is
   fully cached and fully extracted. Of its references the library caches only
   RFC 8610; RFC 7405, RFC 3339, RFC 8943 and RFC 8949 are uncached too. If an
   uncached normative reference forced `partial`, no record in this library
   could ever be `full`.
2. **The library has already accepted this exact dependency at `full`.**
   `rfc-8610` is `standard: FX-1`, `profile: full`, and its G-29 asserts
   "RFC 5234's own CRLF is `%x0D %x0A` only" — a claim about RFC 5234's content
   from the same uncached document. Disqualifying it here would apply a new
   standard to one record.
3. **Nothing in the FX-1 artifact set turns on it.** No requirement text, no
   schema region, no vector, no computed literal and no design mapping depends
   on an RFC 5234 production. `rfc-9165#R-0050` quotes §3's "one valid
   "element"" verbatim and verifies against *this* document's cache. What the
   uncached productions decide is only the *consequence* of a source defect.
4. **`profile: partial` would misdescribe the record.** `docs/extraction.md`
   requires a `profile_reason` naming what is **not covered** — a paywalled
   source, a secondary reference, a catalogue read for one lane. Nothing about
   RFC 9165 is uncovered here. The honest statement is a declared limit, which
   is what this is.

**The recommendation, which is not this pass's to execute:** ingest RFC 5234
and RFC 7405. That closes both claims and would let the case-insensitivity
finding be verified rather than attested. `bin/ingest` was deliberately not run
by this pass.

## Source defects found

Reported, never repaired. Full detail in `schema/README.md` and
`design-notes.md`; the three that bear on a deliverable are first.

1. **`element` versus `elements` — a real fork.** §3 requires an ABNF controller
   to begin with "one valid "element"" (singular), one sentence after naming the
   production as "(called "elements" in [RFC5234])". In RFC 5234 those differ in
   strength, and **every selector the document prints is a bare rulename**, so no
   example distinguishes the readings. A tool author must choose.
2. **Case insensitivity is the default and is never stated.** §1.1's only
   mention of RFC 7405 presents it as *adding* case-sensitive extensions, which
   reads as though sensitivity were the base.
3. **A computed literal is not portable across source-file line endings**, and
   the condition appears only in a code comment: "; on a system where the newline
   is \n, is the same string as:". A CRLF checkout silently changes what a
   `.cat`-computed fixture admits.
4. **Figure 4 spells a text-string result in byte-string notation.** §2.2's
   result rule, inherited by `.det`, makes `"oid" .det cbor-tags-oid` a *text*
   string. Equivalent in effect as an `.abnfb` controller, not in type.
5. **Figure 6 does not parse as CDDL** — `bar = ...` uses `...` as a prose
   placeholder, but CDDL's `...` is only a range operator. `V-0013`,
   `expect: indeterminate`.
6. **`.feature`'s controller has no admissibility rule at all**, and the
   two-element array is the only shape defined; one- and three-element arrays are
   grammatical and undefined.
7. **`.feature` is the only registered control operator no instance can test.**
   Every other one of the twenty is testable by exhibiting an instance it should
   reject.
8. **`.cat` is not commutative in type**, so operand order is a correctness
   question. The document does not say so.
9. **The two single-item dedent forms are offered as alternatives and are not
   equivalent** — `"" .det rhs` yields text whatever `rhs` was and invokes the
   UTF-8 `MUST`; `rhs .det ""` does not.
10. **§2.3's dedent is defined over leading *space* characters**, so a
    tab-indented literal dedents by zero and its embedded ABNF silently stays
    indented. Consistent with RFC 8610's `SP = %x20`, stated in neither.
11. **`rfc5234-core` is abbreviated by the source itself** ("; abbreviated
    here"), so Figure 5's core-rule set is one rule. Closure still holds.

## What this invalidates in `rfc-8610`, which is at `profile: full`

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

**One defect should be narrowed, not withdrawn.** `rfc-8610`'s source defect #7
records that Appendix B redefines `CRLF` as `%x0A / %x0D.0A` and that it "hides
in plain sight". RFC 9165 §3 makes the **identical** redefinition, in its own
voice, *declares* it, scopes it precisely, and calls it "customary for ABNF" —
by one of RFC 8610's own authors. The substance is deliberate community
practice; what remains defective there is that it is undeclared.

**Everything else in that record survives**, and its table of fourteen is
correct as a statement about RFC 8610.

## This record does not close the whole gate

`rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules` remain. Whether any of
them registers further control operators — and so whether **20** is already
stale — is not decidable from here. `rfc-8610`'s gate stands until all four are
read.
