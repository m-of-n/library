---
record: rfc-8610
kind: design-notes
title: "rfc-8610 — bearing on our design"
extracted: "2026-10-18"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§3.8.6`, `Appendix C`) are RFC 8610; cross-references inside this file name
its own headings in italics (*Mapping* 1b). Requirement ids of the form
`rfc-8610#R-0026` are this record's `distilled/requirements.yaml`. Our own
documents are cited by id (`ARCH-0002 P1`, `MD-3`, `R-M-12`). Three markers
distinguish voices:

- unmarked prose reports **RFC 8610** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) lists
**four** options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `ADR-0001` (accepted) constrains
DEC-002 and says option 2 "as originally written does not" remain on the table.
`MD-3` (2026-09-28) narrows DEC-002 to option 5. **No ADR for DEC-002 has been
written** — `DECISIONS-0001` tier-1 item 4b is that ADR and is dated **Oct 28**.
Nothing below may be read as an accepted encoding decision.

**What this document is, before anything is drawn from it.** RFC 8610 is a
**schema language**, not an encoding and not a protocol. It carries exactly two
all-capitals BCP 14 keywords in 125 KB (`rfc-8610#R-0070`, `rfc-8610#R-0139`),
and only the first is RFC 8610 speaking in its own voice. Its normativity is
carried by a grammar (Appendix B) and a matching relation (Appendix C), both
declared normative in their opening sentence (`normative.md`, Appendix B and
Appendix C — `rfc-8610#R-0093` carries that sentence for Appendix A only, which
is the one instance of it `requirements.yaml` holds as an id). Reading it as
a source of obligations yields almost nothing; reading it as a definition of
what can and cannot be *said* about a data structure yields a great deal, and
most of what it yields for us is **what it cannot say**.

---

## What we adopt

**The group as the single composition primitive (§2, `rfc-8610#R-0004`).**
"there is only one kind of composition in CDDL: the _group_". A group is
neutral between array and map until brackets are put around it
(§2.1, `rfc-8610#R-0012`). This maps cleanly onto `ARCH-0002` P6's claim that
`NameCert`, `AuthzCert`, `ArtifactStatement` and `Endorse` are **functions over
one form** rather than four object types: the shared part of P2's *A says B has
C* is a named group, and each predicate type wraps it. P6 and CDDL groups are
the same factoring move, and §2.1's Figure 6 (`identity` factored out of
`person` and `dog`) is literally it.

**The root type as the first rule (§2.2.4, `rfc-8610#R-0027`; Appendix C,
`rfc-8610#R-0101`).** "that role is simply taken by the first rule defined in
the file", and a group may not be a root — "it must be a type"
(`rfc-8610#R-0028`). D4 therefore has no `start` symbol to invent and no naming
convention to agree; the file order carries it.

**The matching relation as the definition of validity (Appendix C,
`rfc-8610#R-0099`).** "an instance (data item) "matches" a CDDL specification if
it is allowed by the CDDL specification". The array rule
(§2.1, `rfc-8610#R-0010`) and the map rule (§2.1, `rfc-8610#R-0011`) are the
whole of it, and the map rule is **exhaustive by default**: a map matches only
if "the map has no name/value pair that is not covered by the group". That
default is `ARCH-0002` P5's *unknown is critical unless declared otherwise*,
already built into the language. P5 does not have to fight CDDL here; it has to
resist the extensibility idiom CDDL teaches (below).

**Cut semantics, and the `:` shortcut that carries them (§3.5.4,
`rfc-8610#R-0055`, `rfc-8610#R-0056`, `rfc-8610#R-0057`).** A cut "locks in" a
pick on a key match alone, "independently of whether the value matches as well,
so when it does not, the entire map fails to match". This is exactly the
behaviour P5 wants for a statement field: a `validity` key carrying a wrong-typed
value must fail the statement, not fall through to a wildcard. Because `:`
*is* a cut, our schemas get it for free as long as we write `key: type` and never
`"key" => type`. **[analysis]** That is a one-line house rule for D4 and it is
worth stating explicitly in the schema README, because the two spellings look
interchangeable and are not.

**Occurrence semantics, including the default (§3.2, `rfc-8610#R-0038`,
`rfc-8610#R-0039`; §3.5.1, `rfc-8610#R-0051`).** "If no occurrence indicator is
specified, the group entry is to occur exactly once (as if 1*1 were specified)",
and in a map "With no occurrence indicator, an entry is mandatory". Mandatory-by-
default is the right default for a signed statement and matches P5.

**`.cbor` and `.cborseq` as the description of a bstr-wrapped payload
(§3.8.4, `rfc-8610#R-0071`, `rfc-8610#R-0072`).** "the byte string carries a
CBOR-encoded data item. Decoded, the data item matches the type given as the
right-hand-side argument". This is the construct `R-O-05` (proposed) needs —
"The signed payload SHALL be the canonical encoding verbatim" — and the one
RFC 9052 §3 uses for `empty_or_serialized_map`. CDDL can *describe* it without
any tag, which is exactly what option 5 wants: the CBOR-ness of the payload is a
schema fact, not a wire fact. Its EDN notation `<< … >>`
(Appendix G.3, `rfc-8610#R-0135`) is how our test vectors should write it.

**Generics for P6's one-form-many-predicates (§3.10, `rfc-8610#R-0082`).**
"the formal parameters are bound to the actual arguments supplied … (as if there
were a rule of the form parameter = argument)". `statement<ptype, pred>` is the
natural expression of P2's form with P6's predicate-type discriminator, and the
RFC's own example is `message<t, v> = {type: t, value: v}` — the same shape.

**EDN as the test-vector notation (Appendix G, which `normative.md` records as
opening "This appendix is normative.").** Issue #39 already assigns diagnostic
notation this role via `draft-ietf-cbor-edn-literals`. RFC 8610 Appendix G is
its first normative extension: whitespace ignored inside prefixed byte strings
(G.1, `rfc-8610#R-0133`), unprefixed single quotes for UTF-8 byte strings
(G.2 — `normative.md`; no requirement id carries that particular sentence),
`<< >>` for embedded CBOR (G.3, `rfc-8610#R-0135`), slash-delimited comments
that are whitespace (G.6, `rfc-8610#R-0138`). The comment facility is what
makes a 40-line signed statement readable as a fixture, and the RFC's own
`/grasp-message/` example in G.6 is the pattern to copy.

**The three-way separation of what a tool may claim (§4.2, `rfc-8610#R-0085`,
`rfc-8610#R-0086`).** "In no case is it intended that a CDDL tool would be
"writing code" for an implementation", and how far a description is enforced "is
left to the designers and implementers of that application". We adopt this as a
boundary on D4 itself: the schema is a *description*, the verifier is a separate
artifact, and no fixture may be generated from the schema and then used to
validate the schema.

---

## What we adapt, and how

**The extensibility idiom — adopted in shape, inverted in default
(§3.5.1 Figure 7; §3.9, `rfc-8610#R-0079`–`rfc-8610#R-0081`).** RFC 8610 teaches
`* tstr => any` as the way to leave a struct open, then points at the socket/plug
mechanism — §3.5.1's closing line is "(See Section 3.9 for one way to explicitly
identify an extension point.)". We take the
socket, not the wildcard. A socket is a *named* extension point that tools
"honor … by not raising an error if such a type or group is not defined at all"
(`rfc-8610#R-0079`), and plugs "must be augmentations, i.e., they must be using
"/=" and "//="" (`rfc-8610#R-0081`). That is a registry-free extension mechanism
and the only one in the language. But see *What we reject* — the wildcard form
is incompatible with P5, and the socket form inherits ADR-0001's namespace
critique.

**The prelude — used, never extended (Appendix D, `rfc-8610#R-0123`,
`rfc-8610#R-0124`).** "The following prelude is automatically added to each CDDL
file" and "the prelude is deemed to be fixed". We take `uint`, `nint`, `int`,
`bstr`/`bytes`, `tstr`/`text`, `bool`, `nil`, `float*` and the bare `#n` major
types. We take **none** of the nineteen prelude names that are or reach major
type 6 (sixteen direct `#6.` productions — `tdate`, `time`, `biguint`,
`bignint`, `decfrac`, `bigfloat`, `eb64url`, `eb64legacy`, `eb16`,
`encoded-cbor`, `uri`, `b64url`, `b64legacy`, `regexp`, `mime-message`,
`cbor-any` — plus the three unions over them, `bigint`, `integer`, `unsigned`).
**[analysis]** Because the prelude is fixed we cannot remove them, so under
option 5 "no IANA tags" becomes a *lint rule over our own schema sources*, not a
schema constraint. That is treated at length below.

**`.size` — used for field widths, never read as a byte constraint
(§3.8.1, `rfc-8610#R-0063`–`rfc-8610#R-0065`).** `bstr .size 32` is the right
way to say a `KeyId` is a 256-bit digest. But §3.8.1 is explicit that "this
control is not a representation constraint; a number that fits into fewer bytes
can still be represented in that form, and an inefficient implementation could
use a longer form (unless that is restricted by some format constraints outside
of CDDL, such as the rules in Section 3.9 of [RFC7049])". For integers `.size`
is a *range*, equivalently `0...256**N` (`rfc-8610#R-0064`), not a width. We use
it only on byte and text strings, where §3.8.1 says it "directly controls the
number of bytes in the string".

**`.bits` — not a length (§3.8.2, `rfc-8610#R-0066`–`rfc-8610#R-0068`).** A
`.bits` constraint says which bits may be set, and §3.8.2's own worked example
notes that an all-clear instance "could be "h''" or "h'00'" or even "h'000000'"
as well". If any DEC-004 tag profile carries a bitfield, it needs `.size` and
`.bits` together.

**Appendix E's JSON story — adapted as a *cost sheet* for DEC-002 option 4,
not as a bijection.** Appendix E is normative (`normative.md`, Appendix E) and
does give one schema two serializations, but it names three leaks in doing so:
`uint`/`nint`/`int` stop being type constraints and "becomes a predicate that
the number be integral" (`rfc-8610#R-0127`); float precision "is only to restrict
the set of permissible values", which "is unlikely to be very useful"
(`rfc-8610#R-0128`); and I-JSON caps interoperable integers at
`[-(2**53)+1, (2**53)-1]`, "a smaller range than that covered by CDDL "int""
(`rfc-8610#R-0129`). Closing the appendix: "a data model described in CDDL is
always restricted by what can be expressed in the serialization"
(`rfc-8610#R-0131`). We adapt this into the interchange matrix `ARCH-0001` §6
owes under `R-I-01`, as the row for any JSON-shaped export.

**`.default` — the one place CDDL touches the wire, adapted with care
(§3.8.6, `rfc-8610#R-0078`).** The implied `.ne` exists "to prevent this value
from being sent over the wire", and the control "is only meaningful when the
control type is used in an optional context". **[analysis]** That is the only
RFC 8610 construct that excludes a *byte pattern* rather than a *value set*, and
it is therefore the only one that interacts with a determinism profile. Used on
a `Validity` field it would make the absent and the explicitly-default forms
non-interchangeable — which is what we want for a canonical encoding, and a trap
for an encoder that writes defaults. It must be used deliberately or not at all.

---

## What we reject, and why

**`* tstr => any` as the extensibility idiom (§3.5.1 Figure 7).** Direct
collision with `ARCH-0002` P5: a wildcard turns the exhaustive map rule
(`rfc-8610#R-0011`) into an accept-anything rule, and §3.5.4 shows the precise
failure — `{ "optional-key": "nonsense" }` matches, because "the first entry of
the group does not match, the second one (the wildcard) does". Worse for us,
`any` is `#` (Appendix D), which includes major type 6, so one wildcard readmits
the whole tag space option 5 excludes. Rejected outright in native schemas.

**CDDL comments as the carrier of P3's semantic layer (§3.1,
`rfc-8610#R-0032`; §3.1, `rfc-8610#R-0033`).** Comments "finish at the end of a
line" and, with whitespace, are "completely optional" — i.e. not part of the
language. `ARCH-0002` P3 says a type is a schema carrying representation,
constraints on usage, semantic descriptions, human-review tags, and possibly
multilingual short descriptions. **CDDL expresses the first row and has no
mechanism for the other four.** §3.2 even says so sideways, qualifying a
statement with "outside any directives/annotations that could possibly be
defined" (`rfc-8610#R-0041`) — annotations do not exist in CDDL 1.0. Rejecting
comments as P3's carrier is not a criticism of CDDL; it is the finding that P3
needs a container *around* CDDL, not a convention inside it.

**The `=>` spelling for member keys in native schemas (§3.5.1,
`rfc-8610#R-0049`; §3.5.4, `rfc-8610#R-0057`).** `=>` has no cut; `:` has.
Rejected for any field whose wrong-typing must fail the statement, which under
P5 is all of them. (`=>` remains necessary where the key is a named type —
§3.5.1 says "the double arrow is necessary if a type is named by an identifier"
— and that is exactly a table, not a struct.)

**Reliance on operator precedence (§3.11, `rfc-8610#R-0083`,
`rfc-8610#R-0084`).** The RFC's own advice, and we take it: "the specification
writer is encouraged not to rely on them, but to insert parentheses liberally".
§3.11's `group3 = (+ a / b / c)` worked example shows a repetition binding over
a type choice where a reader expects the opposite, and the RFC concedes the
semantics "could be counterintuitive". D4 parenthesises.

**Any claim that a CDDL schema constrains bytes.** Four independent statements
in the source forbid it: §2.2.3 "CDDL does not provide any language means to
restrict the choice of serialization variants" (`rfc-8610#R-0026`); §3.2 "does
not make any prescription as to whether arrays or maps use definite-length or
indefinite-length encoding" (`rfc-8610#R-0041`); §3.8.1 ".size … is not a
representation constraint" (`rfc-8610#R-0065`); Appendix E "always restricted by
what can be expressed in the serialization" (`rfc-8610#R-0131`). Treated as its
own section below, because #39's framing of this record depends on it.

---

## Mapping to our decisions

### 1. CDDL as the schema language for D4's encoding-neutral types

Issue #39 calls `rfc-8610` "**CDDL**, the schema language for D4's
encoding-neutral types". Assessed for exactly that claim.

#### 1a. What goes across cleanly

| `ARCH-0001` §4.1 / §4.2 construct | CDDL expression | basis |
|---|---|---|
| `Key`, `KeyId`, signatures, `ArtifactId.digest.hex` | `bstr`, `bstr .size N` | §3.3; §3.8.1 `rfc-8610#R-0063` |
| P1 local label, `Name.labels` elements, P3 descriptions | `tstr` | §3.3 |
| `delegate: bool` | `bool` | §3.3 |
| `Validity` instants | `uint` / `int` | §3.3 |
| `Name = { issuer: Principal, labels: [string, …] }` | a map with a recursive rule reference | Appendix C `rfc-8610#R-0100` — "Rule names can be used in the rule itself" |
| `subjects: [ArtifactId, …]` | `[+ artifact-id]` | §3.4 `rfc-8610#R-0044`; §3.2 `rfc-8610#R-0038` |
| `Threshold.members` | `[+ principal]` | same |
| the statement itself | a struct with `:` member keys | §3.5.1 `rfc-8610#R-0047`, `rfc-8610#R-0048` |
| P6's five kinds as one form | a named group plus a generic rule | §2.1 Figure 6; §3.10 `rfc-8610#R-0082` |
| P1's `(defining key, local label)` | a 2-entry map or 2-element array of `(KeyId, tstr)` | §2.1 `rfc-8610#R-0007` |
| R-O-05's signed payload | `bstr .cbor statement` | §3.8.4 `rfc-8610#R-0071` |
| DEC-004 tag "opaque byte string" v0.1 profile | `bstr` | §3.3 |

So the **representation** row of P3's table goes across in full, and P1's
key-relative identifier is trivially expressible — it is two ordinary fields, and
CDDL is indifferent to the fact that one of them is a key. That part of #39's
claim holds.

#### 1b. What CDDL cannot express, that we need

These are not inconveniences; each is a named invariant of `ARCH-0001` §4.1 or
`ARCH-0002`, and in each case the source states the absence.

1. **Cross-field constraints. `Threshold` is inexpressible.** `ARCH-0001` §4.1
   defines `Threshold = { k: int, n: int, members: [Principal, …] }` **"with
   `1 ≤ k ≤ n` and `n = len(members)`"**. CDDL has no construct for either half.
   `.lt`/`.le`/`.gt`/`.ge` constrain a type against "a value given as a
   right-hand-side type (containing just that single value)"
   (§3.8.6, `rfc-8610#R-0076`) — a literal, never a sibling field. Occurrence
   indicators take literal unsigned integers (§3.2, `rfc-8610#R-0038`), never a
   reference. There is no negation and no syntactic predicate
   (Appendix A, `rfc-8610#R-0096`: "CDDL does not provide the syntactic predicate
   operators NOT ("!") or AND ("&") from PEG"), so the constraint cannot even be
   smuggled in as an exclusion. **[analysis]** This is the sharpest finding in
   this record, because DEC-002's own acceptance test in `ARCH-0001` §7 is
   "round-trip fixtures for NameCert, AuthzCert (including threshold subject),
   ArtifactStatement" — **and the threshold subject is named in the test
   itself.** The named acceptance fixture exercises the one
   invariant the proposed schema language cannot check. `k ≤ n` and
   `n = len(members)` must live in the verifier and in a negative fixture, and
   the ADR must say where. The same hole swallows `Validity`'s
   `not_before ≤ not_after`, which `ARCH-0001` §4.1 implies and no document
   states.
2. **Algorithm-dependent field widths.** `ArtifactId.digest` is
   `{ alg, hex }`; the length of `hex` depends on `alg`. CDDL cannot express the
   dependency, only an enumeration of the valid pairs as a type choice —
   `{alg: "sha-256", hex: bstr .size 32} / {alg: "sha-512", hex: bstr .size 64}`.
   That works (§2.2.2, `rfc-8610#R-0017`) and costs a hand-written alternative
   per algorithm, rewritten whenever `R-M-07`'s digest agility moves. Same shape
   for `Key`'s "Public key material + algorithm identifier".
3. **Sets.** `ARCH-0002` P4 makes a domain of discourse "a *set* of the schemas
   in P3". CDDL has arrays and maps and no set: it cannot say an array is
   duplicate-free (no negation, `rfc-8610#R-0096`) and it cannot order one.
   §3.5 is explicit that CDDL has **no vocabulary for ordering at all** —
   "neither JSON nor CBOR supports this, so no attempt was made to support this
   in CDDL either" (`rfc-8610#R-0046`). P4's hash-as-identity therefore cannot be
   made well defined by a CDDL schema under *any* DEC-002 option. This confirms,
   from a second source, the gap `rfc-8949`'s extraction recorded as "Canonical
   ordering for set-valued arrays" and `DECISIONS-0001`'s standing note records
   as condition (5).
4. **Unicode normalization of labels.** §3.1: "Processing of CDDL does not
   involve Unicode normalization processes" (`rfc-8610#R-0037`), and §3.8.6's
   equality rule compares text strings "if they are bytewise identical"
   (`rfc-8610#R-0077`). Under P1 a type *is* `(defining key, label)` with the
   label a text string, so two normalization variants are two types, silently.
   CDDL cannot state a normalization rule; it has no construct for one. This is
   `DECISIONS-0001` condition (6), and RFC 8610 is a third source saying no
   candidate reaches it.
5. **P3's semantic layer.** As above: representation only. No annotations, no
   descriptions, no review tags, no multilingual strings. **[analysis]** D4's
   deliverable is therefore not "a CDDL file"; it is a *container* — a document
   or a structured record — that carries CDDL for the representation row and
   something else for the other four. That is a scope statement D4 does not
   currently make, and it changes what Oct 21 delivers.
6. **Type-vs-group identity is not locally decidable.** Appendix C: "whether the
   name defined by a rule stands for a type or a group isn't always determined by
   syntax alone" and the determination "may need to span several levels of rule
   definitions" (`rfc-8610#R-0104`). **[analysis]** This is the clearest instance
   of the gap between what the grammar admits and what the type system means: a
   file can be grammatical and still have no determinate reading until a whole
   dependency graph is resolved. For D4 it means a per-file syntax check is not a
   schema check, and the RFC's own convention for disambiguating — writing
   `a = (b,)` to make the group reading stand out — is a comment-level
   discipline, not a checkable rule.
7. **Ordering of alternatives is semantic, and plug order is part of it.**
   Appendix A: prioritized choice, "locking in the first successful match and
   disregarding any further potential matches" (`rfc-8610#R-0094`); Appendix C:
   "the first choice that matches wins" (`rfc-8610#R-0106`) and a `/=`/`//=`
   choice "is populated in the order the rules are given" (`rfc-8610#R-0102`).
   **[analysis]** Consequence for us: `Principal = Key / KeyId / Name /
   Threshold / Group` is **order-dependent**, and since `Key` and `KeyId` are both
   byte-string-shaped, whichever is written first consumes both. A `Principal`
   union must be *discriminated* by shape or by an explicit field, or reordering
   the rule silently changes the language. Equally: if D4 assembles schemas from
   plug files per §3.9, the *concatenation order of the files* is semantic. No
   document of ours says so, and it is a build-system property, not a schema
   property.
8. **Map matching is non-deterministic and the RFC knows it.** §3.5.3: "For each
   candidate name/value pair that the PEG algorithm would try, a matching member
   is picked out of the entire map" (`rfc-8610#R-0053`), and where the pick
   matters, "CDDL tools cannot detect such cases automatically, and … the
   specification writer is simply urged to not write pathologically
   non-deterministic specifications" (`rfc-8610#R-0054`). That is an unchecked
   drafting obligation on us, with no tool support, in the construct our
   statements are made of.

**Verdict on #39's framing.** CDDL is a *competent* schema language for the
representation of our statement and certificate types, and it is genuinely
encoding-neutral between CBOR and JSON (Appendix E). It is **not sufficient for
D4** as D4 is currently scoped: it cannot state `Threshold`'s k/n invariant, the
digest-length dependency, set-ness, normalization, or any of P3's four
non-representational rows. The honest statement for the ADR is that CDDL covers
*structure* and that every *invariant* and every *meaning* in our model sits
outside it — in the verifier, in prose, or in a container D4 has not yet named.

### 2. CDDL is informative about encoding by design

**What the source says, four times.** §2.2.3: the `#n.m` notation "is about a set
of values at the data model level … it does not mandate that these values also
do have to be serialized as half-precision floats: CDDL does not provide any
language means to restrict the choice of serialization variants"
(`rfc-8610#R-0026`). §3.2: CDDL "does not make any prescription as to whether
arrays or maps use definite-length or indefinite-length encoding. That is, there
is no correlation between leaving the size of an array "open" in the spec and the
fact that it is then interchanged with definite or indefinite length"
(`rfc-8610#R-0041`). §3.8.1: `.size` "is not a representation constraint … an
inefficient implementation could use a longer form (unless that is restricted by
some format constraints outside of CDDL, such as the rules in Section 3.9 of
[RFC7049])" (`rfc-8610#R-0065`). Appendix E: a CDDL data model "is always
restricted by what can be expressed in the serialization" (`rfc-8610#R-0131`).
And §3.5: there is no map-ordering vocabulary at all (`rfc-8610#R-0046`).

**Where it does constrain bytes, and it is almost nowhere.** Two places only,
and both narrowly: `bstr .size N` and `tstr .size N` fix "the number of bytes in
the string" (§3.8.1, `rfc-8610#R-0063`), which is a length of *content*, not of
encoding; and `.default`'s implied `.ne` keeps a value off the wire
(§3.8.6, `rfc-8610#R-0078`). Everything else in the language is a statement about
a set of data-model values.

**Therefore: a CDDL schema alone cannot make an encoding deterministic.** Every
determinism question `rfc-8949` §4.2 leaves open — argument shortness, float
form, definite lengths, map key order, tag presence, NaN, negative zero — is
outside CDDL by the source's own statements. §3.8.1's parenthetical is the
RFC's own pointer at the division of labour: the constraint lives in "format
constraints outside of CDDL", which for us is CDE / dCBOR /
`draft-ietf-cbor-serialization`, all held in this library as siblings in #39.
`R-O-05`'s "The signed payload SHALL be the canonical encoding verbatim" cannot
be discharged by any schema, and `R-O-03`'s "cited, not invented silently"
therefore binds a *second* artifact beside D4's schema.

**What the *CDDL informative, prose normative* pattern costs a verifier.**
RFC 9052 §1.4 states it flatly — this library's `rfc-9052` extraction records
"The CDDL grammar is informational; the prose description is normative."
RFC 8610 §4.2 compounds it from the other side: an application "may decide not to
check the data structure at all", and "how far the data description must be
enforced by an application is left to the designers and implementers of that
application" (`rfc-8610#R-0085`). Put together, three costs fall on a verifier:

1. **The machine-checkable artifact is the non-authoritative one.** A verifier
   that validates against the CDDL has validated against a document the
   specification says is not the specification. Where the two diverge, prose
   wins, so a CDDL-passing message can be non-conformant and a CDDL-failing
   message can be conformant.
2. **There is no conformance level to appeal to.** RFC 8610 fixes none
   (`rfc-8610#R-0085`), so two implementations that both claim "CDDL validation"
   may share no checks. *Validates against the schema* is not a statement about
   security.
3. **The split is invisible in the artifact.** Nothing in a `.cddl` file says
   which half governs. **[analysis]** This is exactly what this library's own
   `.derived.` convention guards against one level up (docs/extraction.md,
   *Derived vs verbatim*), and the same remedy applies to D4: the schema file
   must carry, in its header, a statement of what it is **not** authoritative for
   — determinism, cross-field invariants, meaning — and name the artifact that
   is. If D4 ships a CDDL file with no such header, we will have reproduced
   RFC 9052 §1.4's problem by accident rather than by choice.

**[correction] An assumption worth retiring.** The framing in #39 — CDDL as
"the schema language for D4's encoding-neutral types" — reads as though choosing
CDDL settles D4. It settles the representation and leaves the invariants, the
determinism profile and the semantic layer unallocated. Nothing in RFC 8610
supports the stronger reading, and §4.2 and §2.2.3 contradict it directly.

### 3. Where this document cuts against MD-3

`MD-3` (2026-09-28) narrowed DEC-002 to option 5 — reduced CBOR, no IANA tags,
COSE export only, YAML as the human form. It is a narrowing, not an acceptance,
and no ADR exists. Five findings here bear against it or expose costs it did not
score. Each names the option it affects.

#### 3a. CDDL's own extension story depends on a registry — R-M-12, one layer up

**Affects option 5 directly; options 1 and 3 do not pay it.**

`R-M-12` (and `ADR-0001`, accepted): "Native extension points — type
identifiers, predicate types, tags, and header parameters — SHALL be identified
relative to a defining principal … The native model SHALL NOT depend on a
centrally allocated registry for their meaning." Option 5 discharges that by
excluding the CBOR Tags registry and native COSE header parameters.

RFC 8610 then says this about itself: "CDDL uses controls as its main extension
point" (§3.8.3.2), and further control operators "may be defined by new versions
of this specification or by registering them according to the procedures in
Section 6.1" (§3.8, `rfc-8610#R-0062`). §6.1 creates the **CDDL Control
Operators** registry inside the **Concise Data Definition Language (CDDL)**
registry, requires each entry to carry a name and a documentation reference
(`rfc-8610#R-0090`), and sets the policy at "Specification Required" for
undotted names and **"IETF Review" for names that do include an internal dot**
(`rfc-8610#R-0092`). The prelude is separately "deemed to be fixed"
(`rfc-8610#R-0124`).

So the schema language MD-3 selects carries, at its declared main extension
point, exactly the centrally allocated namespace R-M-12 rejects. Three things
follow and none is in any document of ours:

- **Option 5 is registry-reduced, not registry-free.** It removes two registries
  (CBOR tags, RFC 8949 §9.2; COSE header parameters, RFC 9052 §11.1) and adopts
  a third. If namespace
  governance is the criterion — and `ARCH-0001-PROPOSAL-v0.2.0` §3.3 says it is
  the criterion that "was never scored", while `ADR-0001` makes it binding —
  then option 5's score on that criterion is better than option 2's and **not
  perfect**, which is how MD-3 has been read.
- **The dotted-name rule is backwards for us.** A key-relative-looking operator
  name such as `.mofn.canonical` contains an internal dot and therefore needs
  **IETF Review**, the *more* expensive policy, while a flat global name like
  `.mofncanonical` needs only Specification Required. §6.1 prices the
  namespaced form above the global one. **[analysis]** That is a small but exact
  instance of the pattern `ADR-0001` is about: the infrastructure makes the
  global name cheap and the scoped name dear.
- **It bites only where CDDL falls short.** We need a new operator only if we
  need to express something CDDL cannot — and *Mapping* 1b above lists five
  such things. So the registry dependency is not hypothetical; it is the natural escape hatch from
  the expressiveness gap, and taking it would breach R-M-12's spirit in the
  schema layer. **The alternative is prose, which breaches nothing and
  reproduces RFC 9052 §1.4's split.** The ADR must choose between those two and
  currently does not know it has to.

**Option 1 (canonical S-expressions, RFC 9804) does not pay this.** Canonicality
there is a property of the encoding, not of a schema, so option 1 needs no schema
language to be canonical and inherits no schema registry. This is an *additional*
ground on which option 1 sits on the right side, beside the four already
recorded in `DECISIONS-0001`'s standing note, and it reinforces that note's
finding that
option 1 "also wins namespace governance". It is not a conclusion — option 1's
data model and library availability are still the objections DEC-002 names as
drivers — but it is evidence, and it points the same way as the RFC 9804
extraction rather than the opposite way.

#### 3b. Option 5's defining exclusion cannot be stated in CDDL — only linted

**Affects option 5 uniquely, because option 5 is defined by what it excludes.**

Expressing "no major type 6" requires a negation, and
Appendix A says CDDL has none (`rfc-8610#R-0096`). The only expression available
is a positive whitelist of the admitted major types, and it must be restated
wherever a schema would otherwise write `any` — because Appendix D defines
`any = #`, and Appendix C says `#` matches "any data item"
(`rfc-8610#R-0113` for the constrained form; the bare `#` is "any data item").
The fixed prelude additionally ships nineteen names that are or reach major type
6 (listed under *What we adapt*), and we cannot remove them because the prelude is fixed
(`rfc-8610#R-0124`). And the extensibility idiom the RFC itself teaches,
`* tstr => any` (§3.5.1 Figure 7), readmits the whole tag space at every
extension point.

**[analysis]** Consequence: under option 5, "no IANA tags" is enforceable only
as a **lint rule over our own schema sources** — grep for `#6.`, for the
nineteen prelude names, and for bare `any` — plus a decoder rule in the verifier.
It is not, and cannot be, a property of the schema. Options 1 and 3 do not pay
this cost: canonical S-expressions have no tag space to exclude, and neither does
JSON. Option 2 is the only option for which the prelude's tag vocabulary is an
asset rather than a liability. **MD-3 did not score this**, and it is a real
maintenance obligation on every schema file D4 and D7 produce, forever.

#### 3c. COSE export puts the forbidden construct in a file we author

**Affects option 5 uniquely: it is the only option with both a declared export
envelope and a native prohibition on the same construct.**

RFC 9052 §2 identifies COSE messages by registry-allocated tags, and its own
CDDL spells them `#6.18(COSE_Sign1)` and `#6.98(COSE_Sign)`. If option 5 exports
to COSE at all — and `R-I-03` and the proposal §3.3 say it does — then our export
schema must contain a `#6.nnn(…)` production. RFC 8610 gives no module system:
`#39` lists `draft-ietf-cbor-cddl-modules` as a separate, later document, and in
RFC 8610 the only separation between files is the socket/plug convention, which
§3.9 says tools honour by *not raising an error* when a socket is undefined
(`rfc-8610#R-0079`). **[analysis]** So nothing in the language distinguishes a
native schema from an export schema, and a tool cannot tell them apart. The
`.derived.`-style remedy applies again: the separation has to be carried by
filename and header convention and checked by our own CI, exactly as this library
already does for derived artifacts. Without that, a reviewer reading
`statement.cddl` cannot tell whether a `#6.18` in it is a violation or the export
path.

#### 3d. MD-3's YAML human form gets no coverage from CDDL — and the option CDDL fits best is option 4

**Affects option 5's human-form half, and favours option 4 on schema support.**

RFC 8610 is a CBOR and JSON language and nothing else. Appendix E is the JSON
extension and is normative; there is no YAML appendix, no YAML prelude variant,
and no YAML in the language. The only YAML in the document is in Appendix F,
which is declared "for information only" (`rfc-8610#R-0132`) and describes the
accompanying CBOR diagnostic tools as able to convert "between binary CBOR, a
pretty-printed hexadecimal form of binary CBOR, CBOR diagnostic notation, JSON,
and YAML". That is a tool capability, not a schema target.

**[analysis]** Two consequences. First, if D4's schema is CDDL, the schema
covers the CBOR native form and a JSON export and says nothing whatever about
MD-3's YAML human form — so the YAML↔CBOR mapping is a third artifact, unowned,
and the injectivity problem the `rfc-8949` extraction flagged (no YAML spelling
for a byte string) gets no help from the schema layer. Second, and more
pointedly: **the DEC-002 option CDDL supports natively is option 4**, "Dual
canonical (CBOR and JSON) with a documented bijection" — Appendix E *is* a
documented two-serialization story for one schema. The source simultaneously
documents why that bijection is lossy (`rfc-8610#R-0127`, `rfc-8610#R-0128`,
`rfc-8610#R-0129`, `rfc-8610#R-0131`), so this is not an argument that option 4
should win; it is the observation that **option 4 is the only DEC-002 option
whose schema story RFC 8610 actually tells**, and the ADR should say why it is
not taking the one the schema language was built for.

#### 3e. The sufficiency claim fails at DEC-002's own acceptance fixture

**Affects option 5's claim to be sufficient; does not favour another option.**

DEC-002's acceptance test (`ARCH-0001` §7) is "round-trip fixtures for NameCert,
AuthzCert (including threshold subject), ArtifactStatement" — **the threshold
subject is named in the test itself.** *Mapping* 1b item 1 shows that
CDDL cannot express `Threshold`'s `1 ≤ k ≤ n` or `n = len(members)`. Option 5's
proposition is that *CBOR's data model plus CDDL, minus the registries*, is
enough; the first named acceptance fixture is one the schema half cannot check.
**[analysis]** No other DEC-002 option does better — options 1 and 3 ship no
schema language at all — so this is not a score against option 5. It is a
defect in the acceptance test as written, and the ADR must either move the
invariant into the fixture's expected-results file or name the verifier component
that owns it. Reported here because an extraction that only confirms is not
evidence, and this is a place where the narrowing's own test does not test what
it appears to.

#### 3f. What does *not* cut against MD-3, said plainly

Three things, so the section is not read as one-sided. CDDL expresses P1's
`(defining key, local label)` pair with no friction at all — it is two fields,
and the language has no opinion about it, which is precisely what R-M-12 wants
from an encoding layer. §3.9's socket/plug is a genuine registry-free extension
mechanism and the shape is right for P4's domains of discourse. And §3.8.4's
`.cbor` lets option 5 describe R-O-05's bstr-wrapped signed payload without
tag 24, which is the construct the `rfc-8949` extraction identified as the sharp
case. On those three, option 5 and RFC 8610 agree.

**[analysis] But the socket mechanism inherits ADR-0001's critique.** A socket
name — `$$statement-extensions` — is a *flat global name* within whatever set of
files is concatenated. Two parties that each plug `$$statement-extensions` with
different content collide, and nothing in the mechanism disambiguates them
because no principal is attached. That is word for word `ADR-0001`'s rejection of
private-use ranges: "private use gives escape from a registry, not a namespace".
§3.9's mechanism is escape from the IANA registry and is not a namespace. So the
one registry-free extension point CDDL offers reproduces, at the schema layer,
the failure mode P1 exists to fix. Nothing in RFC 8610 is at fault — it never
claimed otherwise — but anyone proposing sockets as the key-relative mechanism
for D4 should be told this first.

---

## Open questions

Items this document cannot settle, with who must. Items marked **[beyond
source]** are ones where this extraction had to reason past both RFC 8610 and our
own documents.

1. **Where do `Threshold`'s `k ≤ n` and `n = len(members)` live?** CDDL cannot
   hold them (§3.8.6 `rfc-8610#R-0076`; §3.2 `rfc-8610#R-0038`; Appendix A
   `rfc-8610#R-0096`). Verifier, expected-results file, or a registered control
   operator — and the third breaches R-M-12's spirit. *D4 (Oct 21), then the
   DEC-002 ADR.*
2. **Is D4 "a CDDL file" or a container that carries one?** P3's four
   non-representational rows have no CDDL expression, and §3.1's comments are
   not part of the language (`rfc-8610#R-0032`, `rfc-8610#R-0033`). **[beyond
   source]** This changes what Oct 21 delivers. *David, before Oct 21.*
3. **Does the native schema forbid bare `any`?** Under option 5 a single `any`
   readmits major type 6 (Appendix D; §3.5.1 Figure 7). A house rule plus a CI
   lint is the obvious answer; it has no owner. *D4/D5.*
4. **How are native and COSE-export schemas kept apart without CDDL modules?**
   §3.9's sockets do not separate files and §3.1 gives no module construct.
   **[beyond source]** Filename and header convention plus CI, by analogy with
   this library's `.derived.` rule. *DEC-002/DEC-005 ADR.*
5. **Is `Principal` discriminated, or is it order-dependent?** Prioritized choice
   makes `Key / KeyId` resolve by write order (Appendix A `rfc-8610#R-0094`;
   Appendix C `rfc-8610#R-0106`). **[beyond source]** A discriminating field or
   distinct shapes is needed before any fixture is frozen. *D4.*
6. **Is plug-file concatenation order part of the specification?** §3.9 assembles
   "potentially in separate files that are concatenated", and Appendix C says a
   choice "is populated in the order the rules are given" (`rfc-8610#R-0102`).
   **[beyond source]** If D4 uses sockets, the build order is semantic and must
   be pinned. *D4.*
7. **Which artifact is authoritative for D4 — the schema or the prose?** RFC 9052
   §1.4 chose prose; RFC 8610 §4.2 fixes no conformance level
   (`rfc-8610#R-0085`). Choosing silently is how RFC 9052's problem is inherited.
   *DEC-002 ADR.*
8. **Does option 5 ever register a CDDL control operator?** If yes, R-M-12 is
   breached one layer up (§3.8 `rfc-8610#R-0062`; §6.1 `rfc-8610#R-0092`). If no,
   every gap in *Mapping* 1b becomes prose. *DEC-002 ADR — Paul.*
9. **Why not option 4, given that Appendix E is the only DEC-002 schema story
   RFC 8610 tells?** **[beyond source]** The answer is probably the four leaks
   Appendix E itself documents, but no document of ours says so. *DEC-002 ADR.*
10. **Who owns the YAML↔CBOR mapping now that the schema layer cannot reach it?**
    MD-3 names YAML as the human form; RFC 8610 has no YAML. *Paul / D4.*
11. **Do `rfc-9165`, `rfc-9682`, `rfc-9741` and `draft-ietf-cbor-cddl-modules`
    change any of the above?** All four are siblings in #39 tier 2 and all four
    are `status: fetched`. `rfc-9682`'s own record note in this library says
    "Normative grammar corrections to RFC 8610; both remain current, so an
    implementation must read them together", and both `rfc-9165` and `rfc-9741`
    carry "Additional Control Operators" in their titles — i.e. the registry path of §6.1
    in use. **Nothing in this record may be treated as the current state of CDDL
    until those four are read.** *#39 tier 2.*
12. **Does anything in our model need `.regexp`?** It is the only CDDL construct
    with an external normative dependency (XSD, §3.8.3 `rfc-8610#R-0069`) and it
    carries the document's only SHOULD (`rfc-8610#R-0070`, which obliges a
    specification employing CDDL to identify the Unicode versions addressed). If
    D4 uses it, we inherit that obligation. *D4.*

### Defects and ambiguities in RFC 8610 itself

Places where the source does not decide something it appears to decide, or where
its own normative parts disagree. Reported, not repaired.

13. **Appendix G.2 names four EDN byte-string prefixes; §3.1 and Appendix B
    admit two.** Appendix G.2 (normative) says byte strings are "prefixed by >h<
    for base16, >b32< for base32, >h32< for base32hex, or >b64< for base64 or
    base64url" (`rfc-8610#R-0134`'s section). §3.1 (normative) says byte strings
    "may be prefixed by "h" or "b64"" (`rfc-8610#R-0036`'s section), and the
    Appendix B grammar has `bsqual = "h" / "b64"`. Both appendices are normative
    and the document never reconciles them. The charitable reading is that EDN
    and CDDL literal syntax are different languages that happen to share a
    notation — but the document does not say so, and §3.1 cross-references
    Appendix G.2 for exactly this notation. **This matters to us concretely:**
    #39 assigns EDN the test-vector role, so a vector written `b32'…'` is valid
    EDN and will not parse as a CDDL literal.
14. **The plain-text rendering of Appendix G.2 is corrupt.** `>h<`, `>b32<`,
    `>h32<`, `>b64<` are the `.txt` rendering of a markup element the renderer
    did not translate; the HTML and XML versions almost certainly show quoted or
    typewriter text. Recorded because the verbatim quote in `normative.md` and
    `requirements.yaml` necessarily reproduces the artifact, and a reader will
    otherwise think we mistyped it. Not a specification defect — a rendering one,
    in the exact file this record's `content.sha256` pins.
15. **§3.8.1's only pointer at "format constraints outside of CDDL" is stale.**
    It cites "the rules in Section 3.9 of [RFC7049]". RFC 7049 is obsoleted by
    RFC 8949, where Canonical CBOR §3.9 was replaced by §4.2 with materially
    different content (§4.2.1 bytewise ordering vs §4.2.3 length-first, which is
    the RFC 7049-compatible variant). This library holds `rfc-7049` as a
    superseded record. The parenthetical is the hinge between CDDL and any
    determinism profile, so for us the staleness is load-bearing: the sentence
    that tells us where determinism lives points at a retired section.
16. **The prelude's tag set is frozen at RFC 7049.** §3.6: "The tags defined by
    [RFC7049] are included in the prelude" (`rfc-8610#R-0058`'s section), and
    Appendix D: the prelude "is deemed to be fixed" (`rfc-8610#R-0124`). Every
    tag registered since 2013 must be redeclared per file (`rfc-8610#R-0059`).
    Not a defect in 2019; a currency problem in 2026, and one that RFC 8610
    cannot fix by its own terms.
17. **Appendix E Figure 15 admits float types whose values the same appendix says
    JSON cannot carry.** Figure 15's JSON-compatible prelude retains `float16`,
    `float32`, `float64` and `float`, while the appendix's closing paragraph
    states that "floating-point values such as NaN (not a number) and the
    infinities cannot be represented in JSON even if they are allowed in the CDDL
    generic data model" (`rfc-8610#R-0131`). A schema using Figure 15's `float`
    is therefore satisfiable by values no conformant JSON instance can express.
    The appendix states both halves and does not reconcile them.
18. **§3.5.3's drafting obligation has no decision procedure.** "the
    specification writer is simply urged to not write pathologically
    non-deterministic specifications" (`rfc-8610#R-0054`), in the same sentence
    that says tools cannot detect the condition. The condition is given by
    example and by cause — "more general" before "more specific", and a general
    rule consuming only a subset — and never as a test. Any CI check we write for
    D4 is therefore our own invention, which under `R-O-03` must be cited as
    ours.
19. **Table 1 does not list `^`.** §3.11 says the precedences "are defined in
    Appendix B and summarized in Table 1" (`rfc-8610#R-0084`); Appendix B gives
    `memberkey = type1 S ["^" S] "=>"`, so the cut is a grammar construct with a
    position but no row in the summary. Minor — §3.11 defers to Appendix B — but
    a reader working from Table 1 alone will not find the cut, and the cut is the
    construct §3.5.4 makes load-bearing.
