---
record: rfc-9165
kind: design-notes
title: "rfc-9165 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.3`) are RFC 9165. Other documents are named (`RFC 8610 §3.8`). Our own
documents are cited by id (`ARCH-0002 P1`, `MD-3`, `R-M-12`). Three markers
distinguish voices, following `records/ietf/rfc-8949/distilled/design-notes.md`:

- unmarked prose reports **RFC 9165** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project, or a claim in this
  library, that the sources do not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `MD-3` (2026-09-28) **narrowed** DEC-002
to option 5 and **no ADR for DEC-002 has been written** — `DECISIONS-0001`
item 2 says so in terms: "Still open: a narrowing is not an acceptance, and no
ADR exists." Nothing below may be read as an accepted encoding decision.

**What this record is for.** `rfc-8610` reached `profile: full` carrying a gate
in both `distilled/README.md` and `summary.md`: *nothing in that record may be
treated as the current state of CDDL until `rfc-9165`, `rfc-9682`, `rfc-9741`
and `draft-ietf-cbor-cddl-modules` are read.* This is one of the four. It closes
the operator-set quarter of that gate and nothing else: it says what CDDL's
control-operator vocabulary actually is, and it leaves modules, extended
diagnostic notation and the `rfc-9682`/`rfc-9741` changes untouched.

---

## What we adopt

**The full operator set as the real target, not RFC 8610's fourteen.** The
registry holds **at least twenty** control operators — RFC 8610's fourteen and
these six, with no overlap — and this record's own
`usefulness.reason` is the operative sentence: *"a CDDL tool that omits them
cannot validate our fixtures."* `schema/control-operators.derived.yaml` holds
all six as data — target, controller, result type, predicate, class — and is
written with the same field names as `rfc-8610`'s table so the two read as one
table of twenty operators.

> **[correction]** An earlier draft of this extraction stated that the
> registry holds **exactly** twenty. That is wrong, and it is the same error
> this record reports in `rfc-8610` under *What this invalidates*: a registry
> total derived from the documents one happens to have read. RFC 9165 claims
> nothing about the registry beyond its own six entries, and RFC 9090 (July
> 2021) predates it. Current registry state is `records/ietf/rfc-9741`'s to
> state, not this record's.

**`.feature` as the way to declare an invariant the schema cannot check.** This
is the one thing in Tier 2 that changes a deliverable, and it is set out under
*Mapping* 3 below.

**The three-phase picture of what a CDDL tool is.** The operators do not all
live in the same place in a toolchain, and `distilled/messages.yaml` records the
five phases. `.plus`, `.cat` and `.det` must be evaluated during
**specification expansion**, before any instance exists; `.abnf` and `.abnfb`
are recognizers invoked **during matching**; `.feature` writes to an **output
channel** and never affects the verdict. We adopt that shape for whatever
validates D4's schemas, because a tool built on the assumption that a control
operator is a predicate over an instance has nowhere to put four of the six.

**§6's drafting posture.** "As with CDDL itself, ABNF should be judiciously
applied, and overly complex (or "cute") constructions should be avoided." Both
`should`s are lower case and there is no decision procedure, so this is a
disposition and not a check — but it is the right disposition for a schema that
must stay reviewable, and it is consistent with `R-O-03`'s demand that an
algorithm be cited rather than silently invented.

---

## What we adapt, and how

**Computed literals are derived artifacts, and `R-O-03` applies to them.**
`R-O-03` requires that a canonicalization algorithm "SHALL be cited, not
invented silently". `.plus`, `.cat` and `.det` introduce a new way for a schema
to contain something a reviewer cannot see: the string a rule admits is no
longer in the rule.

> **[analysis]** This library already solved exactly this problem for files —
> `.derived.` in the filename, because "a header is read only by someone who
> opens the file" (`docs/extraction.md`). The same failure mode now exists
> *inside* a CDDL rule, and the filename convention cannot reach it. If D4's
> schemas use `.cat` or `.det`, the computed value must be written out
> somewhere a reviewer sees — a comment, a generated companion, or a test
> fixture. `distilled/examples/vectors.yaml` V-0005, V-0011 and V-0012 are
> exactly that artifact for this document's own figures, and the document
> itself only ever computes one of the three (Figure 4) and stops.

**`.abnf` where a value is already specified in ABNF, and `%s` always written
out.** Many of the identifiers we will carry are specified elsewhere in ABNF,
and §3's whole argument is that translating ABNF into a regular expression is
lossy or impossible — "that ABNF would usually need to be translated into a
regular expression (if that is even possible)". Where that applies we adopt
`.abnf` rather than `.regexp`. But see the case-sensitivity hazard under
*Mapping* 4: the adaptation is **always write the RFC 7405 `%s` prefix**, never
rely on a bare quoted string.

**The extension-point idiom, with the wildcard treated as the load-bearing
part.** Figure 7 pairs RFC 8610's socket/plug for known extensions with a
wildcard entry for unknown ones and `.feature` to mark them. The source names
which part does the work: "However, future extensions would be deemed invalid
unless the wildcard at the end of the map is added." We adapt by treating
`.feature` as documentation of an extension point and the wildcard as its
creation — and by recording the price the source itself states, that a wildcard
renders a misspelled label "invisible" (`rfc-9165#V-0015`).

---

## What we reject, and why

**Figure 9's `.feature` switch as a serialisation mechanism.** The document
shows a JSON/CBOR switch —
`JC<J,C> = J .feature "json" / C .feature "cbor"` — and then withdraws from it
twice in two sentences: "It remains to be seen if the enable/disable approach
can lead to new idioms of using CDDL" and "The language currently has no way to
enforce mutually exclusive use of features, as would be needed in this
example." An instance carrying *both* spellings satisfies it and is reported as
using both features (`rfc-9165#V-0018`). We do not build a dual-serialisation
story on a mechanism whose author says it cannot enforce the exclusivity it
needs.

**Registering a control operator of our own.** Set out under *Mapping* 2: the
cost is now measured, and it is higher than `rfc-8610`'s extraction could see.

**Figure 8's `any`-terminated type extension.** `allowed-types` ends
`/ (any .feature "allowed-type-extension")`, and RFC 8610's prelude defines
`any = #` — every data item, major type 6 included. Under option 5 that
readmits the entire CBOR tag space at the extension point, with `.feature`
marking its use and restricting nothing. We reject the idiom as written; see
*Mapping* 5.

---

## Mapping to our decisions

### 1. What the operator set gives D4, and what it still does not

`rfc-8610`'s extraction listed **six** things we need that CDDL cannot express.
RFC 9165 moves **one and a half** of them, and the half matters more than the
whole.

| rfc-8610's gap | after RFC 9165 |
|---|---|
| 1. cross-field constraints (`1 ≤ k ≤ n`, `n = len(members)`) | **unchanged.** See below — this is the finding Tier 2 was run for |
| 2. algorithm-dependent widths | unchanged |
| 3. sets / duplicate-freedom | unchanged |
| 4. Unicode normalisation of labels | unchanged, and **newly hazardous** — see *Mapping* 4 |
| 5. a semantic layer | **partially addressed.** `.feature` is an annotation that survives into a tool's output. It is the first thing in CDDL that is neither syntax nor constraint |
| 6. type-vs-group identity not locally decidable | unchanged. All six new operators are **type** controls; CDDL still has no group control syntax at all |

**Cross-field constraints are still inexpressible, and `.plus` is the operator
that looks as though it should fix it.** It does not, and the reason is one
sentence of §2: "For these operators, as with all control operators, targets and
controllers are types." An operand is a *type expression in the specification*,
not a value in the instance. The document's only `.plus` example computes over a
**generic parameter** bound at instantiation — "The parameter BASE allows the
non-conflicting use of a multiple of these interval groups in one map by
assigning different labels to the entries of the interval" — and what it
produces are **map labels**: "one group for the X dimension (using 0, 1, and 2
as labels)".

> **[analysis]** Relating two *keys* at authoring time is not relating two
> *values* at validation time, and the route that would smuggle it in is closed
> independently: RFC 8610's `occur = [uint] "*" [uint] / "+" / "?"` takes
> literal integers, not types, so a `.plus` result — which is a type — cannot
> become an occurrence count and `[k* member]` cannot be driven by another
> member's value. So `Threshold`'s `1 ≤ k ≤ n` and `n = len(members)` remain
> inexpressible, and so does `Validity`'s `not_before ≤ not_after`. **This is
> the single most consequential negative result in Tier 2** and it confirms
> rather than overturns `rfc-8610` item 1.

### 2. Where this document cuts against MD-3 — the registry cost, now measured

**Affects option 5 directly. Options 1 and 3 do not pay it.**

`rfc-8610`'s extraction (§3a of its design notes) found that **option 5 is
registry-reduced, not registry-free**: it drops the CBOR Tags registry
(RFC 8949 §9.2) and the COSE header parameters registry (RFC 9052 §11.1) and
adopts a third, the **CDDL Control Operators** registry, at the schema layer.
It further found that RFC 8610 §6.1's dotted-name rule **prices the namespaced
form above the global one** — a key-relative-looking `.mofn.canonical` contains
an internal dot and so needs *IETF Review*, while a flat `.mofncanonical` needs
only *Specification Required*.

RFC 9165 is the first document to actually use that extension point, and it is
evidence on exactly that question. **Six registrations, and every one of them is
in the flat global form:**

```
.plus   .cat   .det   .abnf   .abnfb   .feature
```

Zero internal dots. Zero namespaced names. `schema/registry-tables.txt` holds
Table 2 verbatim, and `schema/control-operators.derived.yaml` records the count
as `registry_names_with_an_internal_dot: 0`.

And the document states a *reason* for one of the six names, which is the only
naming rationale it gives: *"(The name .det is a shortcut for "dedenting cat".
The maybe more obvious name .dedcat has not been chosen as it is longer and may
invoke unpleasant images.)"* (§2.3). **Brevity and euphony.** Added by the
verify pass, which found it was the one §1–§6 sentence the extraction had
dropped without declaring. It is not a requirement and it carries no force —
but in a record whose finding is that §6.1's policy subsidises the flat global
name, the author's own stated criterion for choosing between two candidate
names is evidence, and it mentions neither scoping nor a defining principal.

> **[analysis]** This is the pattern `ADR-0001` is about, observed rather than
> predicted. §6.1 made the global name cheap and the scoped name dear, and the
> very first document through the door took six global names and no scoped ones.
> `rfc-8610`'s §3a called the dotted-name rule "backwards for us" and marked the
> claim as analysis; it is now a measured regularity in the only sample that
> exists. The namespace that gets consumed is the one the policy subsidises.

> **[analysis]** And the cost is worse than §3a could see, in a way that
> sharpens rather than softens it. §3a treated registration as our escape hatch
> from CDDL's expressiveness gap. RFC 9165 shows what taking that hatch actually
> costs: it is **Standards Track**, authored by one of RFC 8610's own three
> authors, and it arrived **two and a half years** after RFC 8610 (June 2019 to
> December 2021, both dates from this document's own reference list and masthead)
> for operators that §1 says "were not yet ready at the time [RFC8610] was
> completed". That is
> the demonstrated path for a new control operator. Our realistic options are
> therefore an IETF document on an IETF timescale, or prose. **Prose breaches
> nothing and reproduces RFC 9052 §1.4's split; registration breaches R-M-12's
> spirit at the schema layer and takes years.** The ADR must choose between
> those two, and `rfc-8610`'s §3a is right that it currently does not know it
> has to.

> **[correction]** Pass 1 wrote that RFC 9165 "spent four years in the working
> group" and attributed "were not yet ready at the time [RFC8610] was completed"
> to the **abstract**. Both are wrong and the verify pass fixed them. The source
> carries no drafting history at all — no I-D name, no working-group adoption
> date, nothing from which four years could be read; the only interval it
> supports is June 2019 (its own `[RFC8610]` reference) to December 2021 (its
> masthead), two and a half years. And the bracketed spelling `[RFC8610]` is
> **§1's**; the abstract writes "RFC 8610" unbracketed (source line 21), so the
> quotation as given was never the abstract's bytes. The *argument* survives
> intact — the path to a new control operator is a Standards Track RFC on an
> IETF timescale — but it must not be propped up by a number nobody measured.

**Against `R-M-12` and `ARCH-0002 P1` specifically.** `R-M-12` and `ADR-0001`
require that native extension points "SHALL be identified relative to a defining
principal" and that the native model "SHALL NOT depend on a centrally allocated
registry for their meaning". `ARCH-0002 P1` is sharper still: private-use ranges
"give **escape from a registry, not a namespace**", because "nothing in the
encoding can disambiguate them because no principal is attached". A CDDL control
operator name is a flat global identifier with no principal attached and no
private-use range at all — there is not even an escape hatch to criticise. **Option 1
(canonical S-expressions) does not pay this**, for the reason `rfc-8610` §3a
gives: canonicality there is a property of the encoding rather than of a schema,
so option 1 inherits no schema registry. This is a second document's worth of
evidence on the same side, and it points where the RFC 9804 extraction pointed.

### 3. `.feature` and DEC-002's own acceptance fixture — the one place MD-3 gains

**Affects option 5 favourably. The first such finding in this library's CDDL
chain, and it should be read as narrowly as it is written.**

`rfc-8610`'s §3e found that **DEC-002's acceptance test fails at its own first
fixture**: ARCH-0001 §7 asks for "round-trip fixtures for NameCert, AuthzCert
(including threshold subject), ArtifactStatement", and the threshold subject
carries `1 ≤ k ≤ n`, which CDDL cannot check. Its conclusion was that the ADR
"must either move the invariant into the fixture's expected-results file or name
the verifier component that owns it".

RFC 9165 adds a third option, and it is better than either:

```cddl
Threshold = {
  k: (uint .feature "threshold-k-bounded-by-n")
  n: uint
  members: [* Principal]
}
```

> **[analysis]** This does **not** close the gap — `.feature` constrains
> nothing, and `rfc-9165#V-0018` is the document's own demonstration that it
> cannot enforce anything. What it does is make the gap **declared, in the
> schema, in a form a tool emits on every instance it validates.** The failure
> mode §3e identified is not that the invariant is unchecked; it is that a
> reader of `statement.cddl` cannot tell that it is unchecked. `.feature` fixes
> precisely that, and nothing else. The ADR should still name the verifier
> component that owns the check; it should also annotate the schema, so that
> the schema and the ADR cannot drift apart silently.

> **[analysis]** Two conditions on using it this way, both from the source.
> First, a tool that discards `.feature` annotations is **conformant** — every
> statement about tool behaviour in §4 is hedged ("may mark", "might contain",
> "may simply report"), so the annotation is advisory to the toolchain and the
> CI check must be ours. Second, the two-element array form
> (`["name", "detail"]`) is the only shape the document defines; a one- or
> three-element array is grammatical and undefined, so our own convention must
> pin the arity.

### 4. Case insensitivity arrives in CDDL by the back door, and it collides with P1

**Affects every option that uses CDDL as its schema language — options 2, 4 and
5. This is the sharpest operational finding in the document.**

RFC 8610 §3.1 states that CDDL has no case insensitivity for text strings and
that regular expressions are the workaround; `rfc-8610`'s `grammar-gaps` records
it as **G-35**, and its `.regexp` notes add that case insensitivity "must be
written out, as in "[Cc][Aa][Ss][Ee]"".

§1.1 of this document brings RFC 7405 into scope: "the ABNF control operators
defined by this document allow use of the case-sensitive extensions defined in
[RFC7405]". Read that sentence twice. RFC 7405's `%s` is what makes a quoted
string case-**sensitive**, which means the *default* is case-**insensitive** —
RFC 5234 §2.3. So `text .abnf '"cbor"'` matches `CBOR` and `cBoR`.

Checked by script against the document's own example: the only letter-bearing
quoted strings in Figure 5's composed controller are `"T"` and `"Z"`, and **no
`%s` or `%i` appears anywhere**, so `Tag0 = #6.0(text .abnf date-time)` admits
`1990-12-31t23:59:60z`. That agrees with RFC 3339, which permits lower case — so
the document's own example is correct — but it is a property of ABNF's defaults
rather than a choice this document made, and **it is stated nowhere in it**.

> **[analysis]** G-35 is therefore **partially closed**, and it is the only one
> of `rfc-8610`'s 44 gaps that this document closes at all. But the way it
> closes is a hazard for us specifically. Under `ARCH-0002 P1` an extension point
> is a pair `(defining key, local label)` and the **local label is identity**:
> "Key *K*'s `build-provenance` and key *K′*'s `build-provenance` are different
> types." If a label's schema were written `text .abnf '"build-provenance"'`,
> then `Build-Provenance` would match the same type — a **collision inside one
> key's namespace**, which is exactly the failure P1 exists to prevent, arriving
> from the schema layer rather than from a registry. It also compounds
> `rfc-8610`'s gap 4: CDDL does no Unicode normalisation (§3.1, "Processing of
> CDDL does not involve Unicode normalization processes") and compares text
> "bytewise identical" (§3.8.6), so a label is byte-exact under every other
> construct in the language and case-folded under this one. **The rule for us is
> one line: any `.abnf` controller constraining an identifier writes `%s`
> explicitly.** That belongs in D4's schema conventions, and it is a CI-checkable
> grep.

### 5. Option 5's defining exclusion, and what §3b has to absorb

**Affects option 5 uniquely, because option 5 is defined by what it excludes.**

`rfc-8610` §3b found that option 5's "no major type 6" cannot be stated in CDDL
and is enforceable only as a lint rule over our own schema sources — grep for
`#6.`, for the nineteen prelude names that reach major type 6, and for bare
`any`. Two things here extend that list, and one of them is new in kind.

**Figure 5 is the worked example of exactly the construct option 5 forbids.**
`Tag1004 = #6.1004(text .abnf full-date)` and `Tag0 = #6.0(text .abnf
date-time)`. §3c of `rfc-8610`'s notes observed that COSE export puts a
`#6.nnn(…)` production in a file we author and that nothing in the language
distinguishes a native schema from an export schema. RFC 9165 does not change
that — but it is now the *canonical demonstration* of the idiom, in a Standards
Track RFC, which is what anyone writing our export schema will copy.

**Figure 8 adds a construct to the lint list that §3b did not name.**
`/ (any .feature "allowed-type-extension")` readmits the whole tag space, and it
does so with a `.feature` annotation that makes it *look* governed.

> **[analysis]** That is worse than a bare `any`, not better. A reviewer
> grepping for `any` finds it; a reviewer reading the schema sees a named,
> annotated, apparently deliberate extension point and has no reason to look
> harder. **The lint rule §3b proposes must therefore treat
> `any .feature "…"` as a hit, not as an exemption** — the annotation is
> documentation, not restriction. Options 1 and 3 do not pay this: canonical
> S-expressions have no tag space to exclude, and neither does JSON.

### 6. Which DEC-002 option does this document's schema story actually fit?

**Favours option 4 on the same ground `rfc-8610` §3d found, and more weakly than
that section did.**

`rfc-8610` §3d concluded that "option 4 is the only DEC-002 option whose schema
story RFC 8610 actually tells", because Appendix E is a documented
two-serialisation story for one schema. RFC 9165 adds a *mechanism* aimed at the
same place: Figure 9's JSON/CBOR switch, "using Sensor Measurement Lists (SenML)
[RFC8428] as the example data model used with both JSON and CBOR".

> **[analysis]** So the pattern repeats: the CDDL chain keeps supplying
> machinery for the dual-serialisation option, and MD-3 narrowed to a different
> one. But this is *weaker* evidence than §3d's, and the weakness should be
> stated rather than hidden, because the document itself retracts it in the
> next paragraph ("It remains to be seen…", "no way to enforce mutually
> exclusive use"). It is one more data point on the same side of the ledger as
> RFC 9804's and `rfc-8610` §3d's, and it is not a conclusion. **Still nothing
> in the CDDL chain says anything whatever about MD-3's YAML human form** —
> §3d's finding there stands untouched, since RFC 9165 adds no serialisation
> and no human notation at all.

### 7. What does *not* cut against MD-3, said plainly

Four things, so the section is not read as one-sided.

- **`.abnf` and `.abnfb` are encoding-neutral.** They constrain a string in the
  *data model*, not its serialisation, so they work identically under CBOR and
  JSON and cost option 5 nothing that option 2 does not also pay.
- **`.feature` is genuinely registry-free as an extension mechanism.** The
  feature *name* is an arbitrary string chosen by the specification author; no
  registry allocates it. It is the one construct in CDDL whose extension
  vocabulary is not centrally governed — and unlike socket/plug it does not even
  pretend to be a namespace, so it does not invite `ADR-0001`'s critique of
  private-use ranges.
- **`.plus` with a generic parameter is a clean way to assign label blocks**
  without a registry, and the idiom transfers directly to any map where we need
  several instances of one group under distinct integer labels.
- **The whole document costs option 5 no tag and no header.** It registers six
  operator names and touches neither the CBOR Tags registry nor the COSE header
  parameters registry, which is precisely what option 5 is defined to avoid.

### 8. What this costs a tool, which is what `usefulness.reason` is about

The record says "a CDDL tool that omits them cannot validate our fixtures". The
price of not omitting them is specific:

> **[analysis]** `.abnf` and `.abnfb` require a **complete second formal
> language** inside a CDDL string literal — an RFC 5234 parser *and* RFC 7405's
> extensions, both newly normative for CDDL, plus a recognizer over two
> different alphabets (bytes for `.abnfb`, code points for `.abnf`). Nothing in
> CDDL's grammar can check that a controller is valid ABNF, begins with an
> `element`, or is rule-closed — `ctlop = "." id` constrains none of it. The
> practical consequence for D4: **if our schemas use `.abnf`, our choice of CDDL
> tool narrows to implementations that embed an ABNF engine**, and that is a
> smaller set than "CDDL tools". If our fixtures can be expressed without
> `.abnf`, the tool constraint is worth more than the expressiveness.

---

## Open questions

1. **Does D4 use `.abnf` at all?** It buys exact reuse of ABNF already published
   for the identifiers we carry, and costs an ABNF engine in every validator
   plus the case-sensitivity discipline of *Mapping* 4. Not yet asked anywhere.
2. **Does the DEC-002 ADR annotate the schema with `.feature` for the invariants
   CDDL cannot check?** *Mapping* 3 argues it should, in addition to — not
   instead of — naming the verifier component. `rfc-8610` §3e left this as a
   two-way choice; it is now a three-way one.
3. **What is our convention for a `.feature` name?** The document gives none and
   registers none. Under `ARCH-0002 P1` the honest form would be key-relative,
   but a feature name is a free string with no principal attached, so it
   reproduces P1's problem in miniature at zero registry cost. Worth deciding
   before the first one is written, not after.
4. **Do we forbid computed literals in D4's schemas outright?** *What we adapt*
   argues for writing the computed value out. Forbidding `.cat` and `.det` is
   simpler, loses only readability of multi-line literals, and removes the
   line-ending hazard below entirely.
5. **Does the library need a record for the IANA CDDL registry?** Three records
   now hold pieces of it — `rfc-8610`'s fourteen, this record's six, and whatever
   `rfc-9682`/`rfc-9741`/`draft-ietf-cbor-cddl-modules` add. `rfc-8610`'s schema
   README already says the verbatim tables belong in such a record if it is ever
   created. The count is now 20 and will move again inside Tier 2.
6. **Two of the four Tier 2 documents remain.** This record closes the
   operator-set quarter of `rfc-8610`'s gate. Whether `rfc-9682` or `rfc-9741`
   registers further operators — and so whether 20 is already stale — is not
   decidable from here.

---

### Defects and ambiguities in RFC 9165 itself

Reported, never repaired. Full detail and locators in `schema/README.md`; the
two that bear on a deliverable are first.

1. **`element` versus `elements` — a fork a tool author must resolve.** §3
   requires an ABNF controller to begin with "one valid "element"" (singular),
   having one sentence earlier named the production as "(called "elements" in
   [RFC5234])". In RFC 5234 those differ in strength:
   `elements = alternation *c-wsp` admits `DIGIT DIGIT` and `"a" / "b"` as a
   selector; `element = rulename / group / option / char-val / num-val /
   prose-val` does not. **Every selector the document prints is a bare
   rulename**, so no example distinguishes the readings. The distinguishing
   fixture pair is in `examples/README.md`.
2. **Case insensitivity is the default and is never stated.** *Mapping* 4. The
   document's only mention of RFC 7405 presents it as an *addition* of
   case-sensitive extensions, which reads as though sensitivity were the base.
3. **A computed literal is not portable across source-file line endings, and
   the condition appears only in a code comment.** Figure 2's equality is
   qualified "; on a system where the newline is \n, is the same string as:".
   RFC 8610's `BCHAR` admits `CRLF = %x0A / %x0D.0A`, so under CRLF line
   endings `c` is `"foo\r\n  bar\r\n  baz\r\n"` and the asserted equality
   fails. **For us this is a repository hazard, not a theoretical one:** a CRLF
   checkout silently changes what a `.cat`-computed fixture admits, and
   `content.sha256` would not catch it because the source file is ours.
4. **Figure 4 spells a text-string result in byte-string notation.** §2.2's
   result rule, inherited by `.det`, makes `"oid" .det cbor-tags-oid` a *text*
   string; Figure 4 writes `'oid…'`. Equivalent in effect as an `.abnfb`
   controller, not in type.
5. **Figure 6 does not parse as CDDL.** `bar = ...` uses `...` as a prose
   placeholder, but CDDL's `...` is only a range operator. `rfc-9165#V-0013`,
   `expect: indeterminate`.
6. **`.feature`'s controller has no admissibility rule at all** — "The latter
   will usually be a string" is a hedge — and the two-element array is the only
   shape defined. One- and three-element arrays are grammatical and undefined.
7. **`.feature` is the only registered control operator no instance can test.**
   Every other one of the twenty is testable by exhibiting an instance it should
   reject. This one is observable only in a tool's diagnostic output, for which
   the document specifies no format.
8. **`.plus`'s float-to-integer conversion is floor, not truncation**, and the
   two differ on every negative non-integer: `-1.5 .plus 0` is `-2` under the
   stated rule and `-1` under C-style truncation. Not a defect in the document —
   it says "floor" and glosses it twice — but the easiest mistake in it.
9. **`.cat` is not commutative in *type*.** `"a" .cat 'b'` is a text string and
   `'a' .cat "b"` is a byte string, from the same bytes, so the UTF-8 `MUST`
   applies to one ordering and not the other. Operand order is a correctness
   question; the document does not say so.
10. **The two single-item dedent forms are offered as alternatives and are not
    equivalent.** `"" .det rhs` yields text whatever `rhs` was and so invokes
    the UTF-8 `MUST`; `rhs .det ""` preserves `rhs`'s type and does not.
11. **`rfc5234-core` is abbreviated by the source itself** ("; abbreviated
    here"), so Figure 5's core-rule set is one rule. Closure still holds.

### What this invalidates in this library's `rfc-8610` record

`rfc-8610` is at `profile: full`, so this is recorded rather than repaired here.

**[correction] Already fixed, by another lane, while this pass was running — and the
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

**[correction] `rfc-8610`'s source defect #7 should be narrowed, not withdrawn.**
It records that RFC 8610 Appendix B redefines `CRLF` as `%x0A / %x0D.0A`,
admitting a bare LF where RFC 5234's core rule is `%x0D %x0A`, and that it
"hides in plain sight". RFC 9165 §3 makes **the identical redefinition**, in its
own voice, *declares* it, scopes it precisely — "the syntax of ABNF itself
(_not_ the syntax expressed in ABNF!)" — and calls it "customary for ABNF", by
one of RFC 8610's own authors. So the *substance* is deliberate community
practice; what remains defective in RFC 8610 is that it is undeclared.

**Everything else in that record survives, and three of its findings are
strengthened.** Its table of fourteen is correct as a statement about RFC 8610;
no name here collides with any of the fourteen; and this document redefines none
of them. **G-11** (per-operator side conditions the grammar cannot express) now
covers these six operators as well as RFC 8610's fourteen — and more besides,
since `rfc-9741` and `rfc-9090` add their own. **G-44** — its *inference* that
`type1` admits at most one range-or-control operator, against RFC 8610's own
Table 1 — is independently corroborated six times over: every nested control
RFC 9165 prints is parenthesised (`(BASE .plus 1)`, `("oid" .det
cbor-tags-oid)`, `lhs .cat ("" .det rhs)`, `(text .feature "…")`,
`(any .feature "…")`) or composed through a named intermediate rule (Figure 5's
`rfc3339`), and not one chains two controls in a single `type1`. The two
apparent counter-examples, Figures 6 and 9, put the controls in separate `type1`s
across a `/`. **And item 1** — that cross-field constraints are inexpressible —
is confirmed against the one operator that looked capable of changing it.
