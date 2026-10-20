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

**State: pass 1 (extract) complete. NO `profile` is declared.** Verify and
cross-check have not run, and under `docs/extraction.md` an unfinished
extraction is neither `full` nor `partial`. `record.yaml` carries
`distillation.standard: FX-1` with one `passes` entry. **No `reviewed_by` is
signed anywhere.**

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
`draft-ietf-cbor-edn-literals` carries 10 in 100 KB with 216 of 226 `inferred`.
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
| schema | `schema/` | **8 verbatim files in 15 regions, 2 derived.** The central artifact is `control-operators.derived.yaml`: all six operators as data, in Table 2's registry order, with target, controller, result type, predicate, control kind, class and per-operator gaps — written with `rfc-8610`'s field names so the two read as one table of twenty operators. All 15 verbatim regions re-verified byte-for-byte with per-region `sha256`, and for all 15 the digest equals that of the same lines `rstrip`ped, proving no trailing whitespace. See `schema/README.md` |
| messages | `messages.yaml` | **13 constructs** — the 6 operators, 3 string structures, 1 operation, 3 idioms — and a **5-phase evaluation order**, which is the part a tool gets wrong. `constrained_by` **is** populated here, unlike in `rfc-8610` where the file header states it is omitted throughout: 62 distinct requirement ids referenced, **0 dangling** |
| examples | `examples/` | **18 vectors, `V-0001`–`V-0018`, source order, no gaps.** 17 `valid`, 1 `indeterminate`, 0 `invalid`. Provenance is explicit per vector: 14 the source's own bytes by line range, 3 `COMPUTED BY US` from the document's **own** §2.3 dedent and §2.2 concatenation, 1 `OURS`. 10 of 10 declared ranges re-slice byte-identically; 3 of 3 computed blocks re-derive exactly. See `examples/README.md` |
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
  between parties, and no second role that acts. §6 adds nothing: it
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
16 of those 20 *restrictive* (the result is a subset of the target), 3 *constructive*
(the result is computed and in general disjoint from the target), 1
*annotative* (the result equals the target). A tool that implements all twenty of them
behind one "narrow the target" interface gets four of them wrong.

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
- **G-44 is corroborated six times over.** It is `rfc-8610`'s *inference* that
  `type1` admits at most one range-or-control operator, so controls do not
  chain, against RFC 8610's own Table 1 implying they do. RFC 9165 never states
  the rule and obeys it everywhere: `(BASE .plus 1)`, `("oid" .det
  cbor-tags-oid)`, `lhs .cat ("" .det rhs)`, `(text .feature "…")`,
  `(any .feature "…")`, and Figure 5's composition through the named rule
  `rfc3339`. The two apparent counter-examples, Figures 6 and 9, put their
  controls in separate `type1`s across a `/`.
- **G-42 and G-43 are untouched.** This document never mentions operator
  precedence, never cites Table 1, and does not touch the cut `^`.
- **Five new gaps**, listed in `schema/control-operators.derived.yaml` under
  `cross_field_constraints.grammar_gaps_touched`, for any successor to
  `grammar-gaps.derived.txt`.

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
