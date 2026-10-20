---
schema: "library-summary/v1"
id: rfc-9165
record: rfc-9165
type: summary
updated: "2026-10-20"
---

# Additional Control Operators for the Concise Data Definition Language (CDDL)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | C. Bormann |
| **Published** | December 2021 |
| **Identifier** | RFC 9165 · DOI 10.17487/RFC9165 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9165.txt |
| **Digest** | `94f86116c04fde0f11d54576465181090ec33983d78db82527c0703a41976774` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

Six control operators added to CDDL: `.plus`, `.cat`, `.det`, `.abnf`,
`.abnfb` and `.feature`. All six are new — zero overlap with RFC 8610's
fourteen — and this document redefines none of them.

**The useful way to read them is by what they do to the target**, a split this
record names and the registry does not:

- **restrictive** — the result is a subset of the target, and in general a
  *proper* one: the operator can reject an instance the target alone admits.
  All fourteen of RFC 8610's, plus `.abnf` and `.abnfb`.
- **constructive** — the result is *computed* and generally **disjoint** from
  the target. `.plus`, `.cat` and `.det`, the first of their kind in CDDL:
  `(BASE .plus 1)` where `BASE = 0` is the type `1`.
- **annotative** — the result *equals* the target. `.feature` alone, and the
  only control operator in CDDL that cannot make any instance invalid.

Three incompatible kinds now share one flat namespace, which matters for
anyone building a validator: implement all twenty behind a single "narrow the
target" interface and **four of them are wrong**. `distilled/messages.yaml`
carries the five-phase evaluation order this implies.

All six are type controls, and that is forced rather than chosen: `ctlop`
appears only inside `type1`, so **CDDL has no group-control syntax at all** —
equally true of RFC 8610's fourteen, and still true of RFC 9682's replacement
grammar, which carries `type1` and `ctlop` over unchanged. The document uses
five distinct type positions for them, from a bare rule right-hand side to a
map key under an occurrence indicator.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | supporting | `.cat`/`.det` compute literals, which is how a schema can name a byte sequence it does not spell out. |
| Naming | **core** | `.abnf` controllers are case-insensitive by default, which reaches ARCH-0002 P1's label space. See below. |

**The finding to act on: case insensitivity is the default, and the document
never says so.** §1.1 brings RFC 7405 into scope, and in RFC 5234 a quoted
string is case-**insensitive** unless marked `%s`. Checked by script: the only
letter-bearing quoted strings in Figure 5's composed controller are `"T"` and
`"Z"`, with **no `%s` or `%i` anywhere** — so
`Tag0 = #6.0(text .abnf date-time)` admits `1990-12-31t23:59:60z`.

Under ARCH-0002 P1 a local label *is* identity, so
`text .abnf '"build-provenance"'` would also match `Build-Provenance` — **a
collision inside one key's own namespace, arriving from the schema layer**.
The rule for D4 is one line: *any `.abnf` controller constraining an identifier
writes `%s` explicitly.* This is the only one of the 44 side conditions in
`rfc-8610`'s `grammar-gaps.derived.txt` that this document closes, and it
closes it only partially.

**Cross-field constraints are still impossible, and `.plus` is the operator
that looks as though it should help.** §2 settles it in one sentence: *"For
these operators, as with all control operators, targets and controllers are
types."* An operand is a type expression *in the specification*, not a value in
an instance — and `.plus`'s only example computes over a generic parameter
bound at instantiation to produce **map labels**. The smuggling route is closed
independently: `occur` takes literal integers, not types, so a computed result
cannot become an occurrence count. **`Threshold`'s `1 ≤ k ≤ n` and `Validity`'s
`not_before ≤ not_after` remain inexpressible.**

What does change is a deliverable. **`.feature` gives a disciplined way to
*declare*, in the schema, an invariant the schema cannot check**, in a form a
tool emits on every instance. `rfc-8610`'s extraction found DEC-002's
acceptance test fails at its own first fixture and left a two-way choice — move
the invariant to expected results, or name the verifier component. This makes
it three-way, and it fixes the failure mode that record named: a reader of
`statement.cddl` currently cannot tell that the threshold invariant is
unchecked. **It enforces nothing** — a tool that discards `.feature` is
conformant, and `V-0018` is the document's own demonstration of that.

## Implementations

The RFC names none. Its own evidence of practice is that the operators "were
not yet ready at the time [RFC8610] was completed". *Searched on 2026-10-19; no
named implementation in the document, and no third-party CDDL or ABNF
implementation is installed here* — so this record's dedent, closure checker,
case-sensitivity census and CDDL recogniser settle structure, not conformance.

## Limits

- **`element` versus `elements` is a real fork a tool author must resolve.** §3
  requires the controller to begin with *"one valid "element""* — singular —
  one sentence after naming the production as *"(called "elements" in
  [RFC5234])"*. In RFC 5234, `elements` admits `DIGIT DIGIT` and `"a" / "b"` as
  a selector; `element` does not. **Every selector the document prints is a
  bare rulename**, so no example distinguishes them. A distinguishing fixture
  pair is in `examples/README.md`.
- **A computed literal is not portable across source-file line endings**, and
  the condition appears only inside a code comment: *"; on a system where the
  newline is \n, is the same string as:"*. A CRLF checkout silently changes
  what a `.cat`-computed fixture admits — a repository hazard for us, and
  `content.sha256` cannot catch it, because the file would be ours.
- **Figure 6 does not parse as CDDL** — *executed, not argued*. `bar = ...`
  uses `...` as a prose placeholder, but `rangeop = "..." / ".."` and no `type2`
  begins with a dot. An Earley recogniser built from RFC 8610's Appendix B (this
  library's own; no third-party CDDL tool is installed here) rejects the figure
  and stalls at the first `.` of `bar = ...`, while accepting the other eight
  figures and ~11 KB of RFC 8610's own CDDL. Held as `V-0013` with
  `expect: indeterminate`.
- **`.feature`'s controller has no admissibility rule** — only the 2-element
  array form is defined — and `.feature` is the only registered control
  operator no instance can test.
- `.cat` is not commutative *in type*, so operand order is a correctness
  question rather than a style one; and §2.3's two single-item dedent forms are
  offered as alternatives but are **not** equivalent (`"" .det rhs` yields text
  and invokes the UTF-8 `MUST`; `rhs .det ""` does not). §2.3's dedent counts
  leading **space** characters only, so a tab-indented literal dedents by zero.
- The extraction is at **passes 1 and 2 of 3** — extract and verify; cross-check
  has not run and no `profile` is declared. The four claims pass 1 flagged as
  ours rather than the source's **all survived the verify pass**, and three are
  now executed against RFC 8610's grammar rather than argued from it: all six
  are type controls (`ctlop` occurs in exactly one production in both
  Appendix B *and* RFC 9682's replacement grammar); the `element`/`elements`
  reading; the operator-class taxonomy (the two assignments genuinely at risk,
  `.within` and `.default`, are restrictive on RFC 8610's own words —
  "the identical formal semantics (intersection)" and "the implied .ne
  control"); and Figure 6's non-parse. **One limit is worth carrying forward:**
  this library holds no `rfc-5234` record and no cached RFC 5234, so the
  `element`/`elements` productions are the record's one load-bearing claim that
  cannot be checked against a source here.

## What this did to `rfc-8610`, which is at `profile: full`

**Two of the four Tier 2 CDDL lanes independently found the same false claim**
in `rfc-8610`'s `control-operators.derived.yaml` — that all names other than
its fourteen are Unassigned — from two different sources, on the same day. The
`rfc-9741` lane got there more completely and the sentence is already gone.
**That convergence is exactly what `rfc-8610`'s gate existed to produce.**

**And one of its defects is narrowed rather than withdrawn.** `rfc-8610`
records that Appendix B redefines `CRLF = %x0A / %x0D.0A`, admitting a bare LF
against RFC 5234's core rule. **RFC 9165 §3 makes the identical
redefinition** — but *declares* it, scopes it exactly ("the syntax of ABNF
itself (_not_ the syntax expressed in ABNF!)"), calls it "customary for ABNF",
and is written by one of RFC 8610's own authors. So the substance is deliberate
community practice. What remains defective in `rfc-8610` is only that it is
**undeclared**, camouflaged among four core rules redefined identically — a
documentation defect, not a grammar one.

## Where it cuts against MD-3

`rfc-8610`'s extraction found that **option 5 is registry-reduced, not
registry-free**, and that §6.1's dotted-name rule prices the *namespaced* form
(IETF Review) above the *global* one (Specification Required). RFC 9165 is the
**first document to use that extension point**, and it registered six names —
**all flat and global, zero internal dots**. So that finding is now a measured
regularity in the only sample that exists: *the namespace that gets consumed is
the one the policy subsidises.*

The escape hatch also costs more than that record could see. RFC 9165 is
Standards Track, written by one of RFC 8610's own authors, for operators that
"were not yet ready" in 2019 — so the realistic path for a new operator is an
IETF document on an IETF timescale, or prose.

One concrete consequence for our own linting: Figure 8's
`/ (any .feature "allowed-type-extension")` readmits the whole tag space while
*looking* governed, so a lint rule enforcing option 5's no-tags exclusion must
treat `any .feature "…"` as a **hit, not an exemption**.
