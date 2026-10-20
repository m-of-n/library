---
record: rfc-9596
kind: design-notes
title: "rfc-9596 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2`) are RFC 9596's. Our own documents are cited by id (`ARCH-0002 P1`,
`DEC-005`, `MD-3`, `R-M-12`). Three markers distinguish voices, following
`records/ietf/rfc-8949/distilled/design-notes.md` and `rfc-9741`'s:

- unmarked prose reports **RFC 9596** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption, or a claim in one of our own
  artifacts, that the source does not support.

**Which quotations below are checkable here, and which are not.** This library
is **standalone by design** (`CLAUDE.md`), so the `mofn` documents this file
cites — `ARCH-0001`, `ARCH-0001-PROPOSAL-v0.2.0`, `ARCH-0002` (P1–P5),
`ADR-0001`, `MD-3`, `DECISIONS-0001`, and the `R-O-*` / `R-I-*` / `R-M-*` rules
— are **not present in this repository.** Every quotation of them here is
reproduced from the extracting agent's context and **cannot be verified from
this repository**; treat each as a citation to be re-checked against `mofn`
before it is relied on. `rfc-9741`'s cross-check pass set this convention.

**One further document is cited and not held, and this time it is not ours.**
**RFC 8725** (*"JSON Web Token Best Current Practices"*, BCP 225) is **not in
this library**, and §1 and §3 rest the entire security case of this mechanism on
its §3.11. So the warrant for the thing we would adopt is a document we do not
hold. That is a `cites` gap and an ingest candidate, recorded here and in
`requirements.yaml` R-0002.

What *is* checkable here, and was: `docs/extraction.md`'s statement of MD-3,
`topics/canonical-encoding.yaml`'s six conditions and its identification of
DEC-002 options 1 and 3, and the artifacts of `records/ietf/rfc-9052`,
`records/ietf/rfc-9053`, `records/ietf/rfc-8392`, `records/ietf/rfc-9597`,
`records/ietf/rfc-9942` and `records/ietf/rfc-9943`.

**How quotations of the library's own artifacts are normalised here.** A
quotation of another record's `design-notes.md` or `summary.md` is quoted from
its **rendered** text: markdown emphasis (`*`, `**`) and code markers
(backticks) are dropped, because they are formatting rather than words.
Quotations of the **source** are not normalised beyond whitespace, are cut from
`.cache/` by line range by script, and are **never elided** — where a sentence
spans a line break the break is declared and the obligation-bearing half is
quoted. This pass's own quote audit found four defects in its own prose under
those rules, and each is recorded in place where it occurred rather than edited
away.

**Decision status.** DEC-002 in `ARCH-0001` §7 lists **four** options; "option
5" exists only as *proposed* text in `ARCH-0001-PROPOSAL-v0.2.0` §3.3, which is
unmerged; `MD-3` (2026-09-28) *narrows* DEC-002 to option 5 and
`DECISIONS-0001` item 2 says *"a narrowing is not an acceptance"*. **No DEC-002
ADR has been written.**

---

## 1. What this record decides, in one paragraph

**`rfc-9053`'s extraction recorded a cost that option 5 pays, and this record
names the thing that removes it.** That record's design notes end item 6 with:
*"option 5 declines the tag registry — no tag, which means the recipient must be
told out of band that these bytes are a `COSE_Sign1`."* **Nothing in this
library had named the in-band substitute. It is label 16, and it is strictly
better than what it replaces** — because §2's `MUST NOT` puts it inside the
signature and no CBOR tag ever was. That converts a recorded cost of option 5
into a recorded non-cost, which is the single most useful thing in this record.
The price is paid in §7.4: the only names `typ` can carry are the kind
`ARCH-0002 P1` rejects.

---

## 2. The finding to act on: this is the signed replacement for the tag MD-3 removes

**CONFIRMED, with one important scoping correction to how the argument must be
presented.**

§2's one obligation:

> The "typ" parameter MUST NOT be present in unprotected headers.

RFC 9052 §4.4's `Sig_structure` is `[context, body_protected, external_aad,
payload]`, so forcing `typ` out of the unprotected bucket puts it **inside the
signature**. **[analysis] And this pass demonstrated that boundary rather than
reading it**: the sibling `records/ietf/rfc-8392` extraction rebuilt
`Sig_structure` from RFC 9052 §4.4 and **verified RFC 8392's A.3 signature from
exactly those four fields**, so the unprotected map is provably not an input.

The CBOR tags are not inside the signature, and `rfc-8392`'s own procedure
proves it from inside that document: §7.1 step 6 prepends the COSE and CWT tags
*after* the signature exists, and §7.2 steps 2–3 strip them *before* validation
begins. **So MD-3's no-tags rule loses no authenticated information, and
adopting `typ` gains some.**

**[correction] But the word `tag` does not occur in RFC 9596 at all.** Measured
over all 232 lines: `tag` **0**, `tags` **0**. This document makes **no claim
whatever** about CBOR tags, does not mention them, and does not present itself
as a replacement for one. **The entire "typ replaces the tag" argument is ours**
— assembled from §2's `MUST NOT`, RFC 9052 §4.4, and RFC 8392 §7.1/§7.2's step
order. It is sound and it is `[analysis]`, and it must be cited that way in the
`DEC-002` ADR rather than attributed to RFC 9596.

Note the standing caveat from `ADR-0001` — *"CBOR tags and COSE header
parameters are IANA allocated, so they are interchange, not native"* — so `typ`
belongs on the export boundary and nowhere else, which is exactly where MD-3
puts COSE anyway.

---

## 3. What its absence enables, and what its presence does not prevent

**CONFIRMED, and the second half is sharper than the summary had it.**

The attack is substitution between kinds of object that share a key and a
shape. **[analysis] Our own case is concrete:** an `ArtifactStatement` and a
revocation or delegation statement, both `COSE_Sign1`, both signed by the same
issuer key, both carrying a CBOR map payload. Without a type indicator inside
the signature, a verifier that accepts one will accept the other's bytes in the
other's slot, and **every signature check passes.** `typ` in the protected
header is what makes those two objects non-interchangeable.

**But the check is ours to write, and the RFC gives no conformance target for
it.** §2 is explicit that the library layer does nothing:

> The "typ" (type) header parameter is ignored by COSE implementations (libraries implementing [RFC9052] and this specification), other than being passed through to applications using those implementations.

> Any processing of this parameter is performed by the COSE application using application-specific processing rules.

And §3's two enforcement sentences are **lowercase**:

> COSE applications employing explicit typing should reject COSE objects with a type header parameter value different than values that they expect in that application context. They should also reject COSE objects without a type header parameter when one is expected.

Under §1.1's BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.
neither carries normative force. **A conformant implementation of RFC 9596
performs no check whatsoever.**

**[analysis] And the count makes it stronger than a reading of two sentences.**
The document's body contains **three** capitalised BCP 14 keywords — `OPTIONAL`
(line 112), `MAY` (119), `MUST NOT` (130) — and **no MUST, SHOULD, SHALL or
RECOMMENDED at all.** Not one of the three *requires* anything: one makes the
use optional, one permits media type parameters, one forbids a placement. **The
only obligation in the document is a prohibition, and it is a prohibition that
makes the mechanism useful rather than one that makes it work.**

---

## 4. `typ` explicitly does not reach the bucket `rfc-9597` permits its claims to sit in

**CONFIRMED.** §2, two sentences:

> The "typ" parameter does not describe the content of unprotected headers. Changes to unprotected headers do not change the type of the COSE object.

Meanwhile `rfc-9597` §1 names `typ` as *"a RECOMMENDED way to include this
information in the COSE structure"* for deriving the intended interpretation of
its CWT Claims header parameter, and `rfc-9597` §2 only *RECOMMENDS* that that
parameter be protected.

**So when a producer takes the permitted unprotected placement, the recommended
disambiguator is declared, by its own text, not to describe it.** `rfc-9597`
§1's `MUST NOT` does close the hole — a recipient may not use the information
beyond the protection afforded to *"the CWT Claims header and the information
used to derive its intended interpretation"* — but only for an implementer who
joins three sentences across two documents published the same month by an
overlapping author set.

**Not a `contradicts`**: the two can be obeyed simultaneously and neither
asserts something the other denies. It is an **asymmetry of protection
strength** — one document makes unprotected placement a `MUST NOT` violation,
the other merely discourages it — and it is the reason our profile should
require protected placement for **both** parameters in one sentence rather than
inherit two different strengths. `record.yaml` records why `contradicts` was
considered and rejected.

---

## 5. Does a CWT need it? No — and that is the problem

**CONFIRMED, and the table is re-derived from both sources.**
`records/ietf/rfc-8392` §6 gives three ways to know a CBOR structure is a CWT:
application context, the `application/cwt` content type from a transport, or
CBOR tag 61. This document adds a fourth. Ranked by whether a verifier can
trust them:

| signal | in band? | inside the signature? |
|---|---|---|
| application context (`rfc-8392` §6) | no | n/a |
| `application/cwt` via transport (`rfc-8392` §9.2.1) | no | no |
| CBOR tag 61 (`rfc-8392` §6, §9.4.1) | yes | **no** |
| `typ` in the protected header (§2) | yes | **yes** |

**Only the last is both**, and the third row is now proved rather than inferred
(§2 above).

And `rfc-9597`'s duplication `MUST` — the one hard rule protecting a verifier
that reads claims from a COSE header — is scoped to claims *"present both in the
payload and the header of a CWT"*, while `rfc-8392` §6 opens *"How to determine
that a CBOR data structure is a CWT is application dependent."* **So `typ` is
the mechanism that turns `rfc-9597`'s `MUST` from
conditional-on-an-undefined-predicate into testable** — and §2 makes its use:

> Use of this header parameter is OPTIONAL.

**That is the join a reviewer should look at hardest in this lane**, and the
three-document chain is worth stating as one sentence: *a `MUST` whose
antecedent is undefined, resting on a `RECOMMENDED` pointer, to a parameter
whose use is `OPTIONAL`.* Our profile closes all three in one line by requiring
`typ` and defining its value.

---

## 6. What we adopt, adapt and reject

### Adopt

1. **Label 16 in the protected header, required.** The mechanism is right, the
   placement rule is the strongest in the lane, and it is the in-band
   substitute for the tag option 5 drops (§1, §2).
2. **§2's scope distinction**: `typ` types the **complete object**, content type
   types the **payload**. We carry both and keep them distinct.
3. **The argument from RFC 8725 §3.11 as the warrant**, with the gap recorded:
   we do not hold RFC 8725, so the warrant must be ingested before it is leaned
   on.

### Adapt

4. **§3's lowercase reject rules, promoted to `MUST`.** Both of them — the
   wrong-value case and the absent-value case. The document's own text is in §3
   and binds nobody.
5. **A defined equality relation**, which the document lacks entirely (§7.5).
   One line: map both spellings to a single canonical form before comparing, and
   state which form is canonical.
6. **A consistency rule between `typ` (16) and content type (3).** Nothing in
   RFC 9596 requires them to agree.

### Reject

7. **`typ`'s value space as our type-identity mechanism** — two global
   registries with no key component (§7.4).
8. **`OPTIONAL` as the strength of the requirement.** Across its own definition
   and both ratified consumers the library holds, `typ` is **never** mandatory:
   §2 says `OPTIONAL`; `rfc-9597` §1 says `RECOMMENDED` and adds *"Other methods
   for determining the intended interpretation MAY also be used"*; `rfc-9942`
   §4.4 says, in lowercase, *"One way to include this information in the COSE
   structure is use of the "typ" (type) header parameter"*. **The
   explicit-typing defence is available everywhere and required nowhere.** We
   require it.

---

## 7. MD-3, header by header — and where this document cuts against it

`MD-3` narrowed DEC-002 to **option 5**: `docs/extraction.md`, which is in this
repository, states it as *"reduced CBOR, no IANA tags, COSE as export only"*.
A **narrowing, not an acceptance.** Option 5 has two clauses that matter here,
and this document lands on **opposite sides** of them.

### 7.1 The header-by-header mapping

This document defines one header, so the mapping is short — and the row that
matters is the first.

| our field (ARCH-0001 §4.1) | carrier | label | registry | option-5 verdict |
|---|---|---|---|---|
| statement type | **`typ`** | **16** | COSE Header Parameters, **values** from [CoAP.ContentFormats] or [MediaTypes] | **carry, protected, and REQUIRE it** — this is the row this record exists for |
| payload type | content type | 3 | same two value registries | carry if the payload is not our own CBOR; **and nothing requires it to agree with `typ`** |
| "these bytes are a COSE_Sign1" | was CBOR tag 18 | — | CBOR Tags | **drop**, and `typ` replaces it *inside* the signature |
| "these bytes are a CWT" | was CBOR tag 61 | — | CBOR Tags | **drop**, same argument |
| issuer / subject | **not here** — `rfc-9597` label 15 | 15 | COSE Header Parameters → CWT Claims | see `rfc-9597`'s notes |
| `KeyId` | **not here** — COSE `kid` | 4 | COSE Header Parameters | see `rfc-8392`'s notes |
| the type **name** itself | a media type or a CoAP Content-Format id | — | two global registries | **the cut** — §7.4 |

**The export mapping, in one line.** `typ` (label 16) in the **protected**
bucket of every `COSE_Sign1` we export, carrying one canonical type name per
statement kind, beside `rfc-9597`'s label 15 and a protected `kid`, with **no
CBOR tag at any layer**.

**What we deliberately do not carry:** any CBOR tag (§2 replaces the signal),
`typ` in the unprotected bucket (§2 forbids it anyway), and any reliance on a
`typ` value being *checked* by a library (§3 above).

### 7.2 Cut 1 — **for** option 5's no-tags clause, and it converts a recorded cost into a non-cost

The finding of §2. Option 5 can drop tag 18 and tag 61 and lose nothing
authenticated, because `typ` carries the type inside `Sig_structure`. **This is
the strongest thing any record in this lane says in option 5's favour**, and it
answers a cost `rfc-9053`'s extraction recorded by name. Stated with the
scoping correction of §2: the argument is **ours**, not RFC 9596's, because the
word `tag` does not occur in RFC 9596.

### 7.3 Cut 2 — one concrete consequence for our own linting

**[analysis]**, in the same register as `rfc-9165`'s `any .feature` note. A lint
rule enforcing option 5's no-tags exclusion must **not** treat a `typ` value of
`61` as a tag hit. `records/ietf/rfc-8392` registered 61 **twice** — CBOR Tag 61
(§9.4.1) and CoAP Content-Format Id 61 (§9.3.1), both for CWT. **Under MD-3 the
first is forbidden and the second is available through `typ`.** Same number,
different registry, opposite verdicts. A grep-based lint gets this wrong by
construction, so the rule has to be written against the decoded item's major
type rather than against a number.

### 7.4 Cut 3 — the mechanism that saves option 5's no-tags clause can only name types the way option 5's P1 clause forbids. **Costs option 5.**

**CONFIRMED, and the quotation is now cut from the source rather than glossed
through the line break.** §2 fixes the value space:

> The syntax of this header parameter value is the same as the content type header parameter defined in Section 3.1 of [RFC9052]; it is either an unsigned integer as registered in the "CoAP Content- Formats" registry [CoAP.ContentFormats] or a string content type value. Content type values have a media type name [MediaTypes] and MAY include media type parameters.

**Both branches are global registries with no key component**, which is
precisely the shape `ARCH-0002 P1` and `R-M-12` reject. There is no way to spell
a `(defining key, label)` type name in `typ` except by burying it inside a media
type string — itself a global allocation — or inside the *"MAY include media
type parameters"* clause, which the document does not constrain at all.

**[analysis] Note where that sentence sits.** The value space is stated in **§1**
as well as §2 (source lines 83–87), so a reader who skips the introduction as
background misses half the document's statement of its own type space. That is
the same shape as `rfc-9597`, where half the keywords are in §1.

`topics/canonical-encoding.yaml`, which is in this repository, records that
option 3 *"is registry-free by construction"* and that option 1 also wins that
criterion. The honest conclusion is `rfc-9052`'s and it holds again, quoted exactly:
**"No tags" and "no registry dependence" are different rules, and MD-3 states the first.**
**[analysis] The word *only* is this extraction's, and so is the consequence:
our export would carry a type name we do not control.**

### 7.5 Cut 4 — a confusion-resistance mechanism with no equality relation. **Costs option 5 and option 3 alike.**

**CONFIRMED and sharpened.** The same type has **two wire spellings**:
`typ: 61` (CoAP Content-Format, `rfc-8392` §9.3.1) and
`typ: "application/cwt"` (media type, `rfc-8392` §9.2.1). They denote the same
type and compare unequal under any byte comparison. **[analysis] And this
extraction measured the size consequence too:** the integer form costs **2
octets** of value (`0x18 0x3d`) against **16** for the string
(`0x6f` plus 15 characters), so the two spellings of one type differ by an order
of magnitude as well as in bytes — which means the cheap spelling and the
self-describing spelling are different choices, not interchangeable ones.

Media type names are case-insensitive — RFC 2045 §5.1, *"The type, subtype, and
parameter names are not case sensitive"*, **a document this library does not
hold** — while a CBOR `tstr` is not, and §2 permits media type *parameters*
unconstrained. So `application/cwt`, `Application/CWT` and
`application/cwt; v=1` are three values and one type. §3's only guidance is to
reject a *"parameter value different than values that they expect in that
application context"*, and "different" is undefined.

**A confusion-resistance mechanism with an unspecified equality relation can be
defeated by respelling the type.** Same shape as `rfc-9165`'s finding that
`.abnf` controllers are case-insensitive by default and nobody says so: **the
comparison rule is where the default hides.** Option 3 pays the same bill in
JSON — a type string there has the same two problems and no registry of integer
aliases to make it worse — so this cut does not discriminate between them; it
is a gap we close under any option.

### 7.6 Cut 5 — **[analysis]** no implementation exists, which is the weakest clause of option 5's export argument. **Costs option 5 specifically.**

MD-3's *"COSE as export only"* clause is an interoperability argument. This
record's own search (2026-10-20, recorded in `record.yaml`) found **no
implementation of label 16 in any language**, and §2 gives the structural
reason:

> Any processing of this parameter is performed by the COSE application using application-specific processing rules.

**[analysis] So there is nothing for a library to implement beyond passing an
opaque value through — and a library that already passes unknown header
parameters through supports `typ` without saying so.** That cuts both ways and
the second way is the more useful: **adopting `typ` costs no library support**,
because every COSE library that is transparent to unknown protected parameters
already carries it. The cost is that **no library will check it for us**, which
is §3's point restated as an engineering fact. Unlike `rfc-9597`'s equivalent
cut, this one does not expire when somebody ships: there is nothing to ship.

---

## 8. DEC-005 — it names no algorithm, and that is its contribution

**CONFIRMED.** Zero algorithm identifiers in the document. Its `DEC-005`
bearing is the **argument** it adopts from RFC 8725 §3.11 and restates in §3:

> The case for explicit typing of COSE objects is equivalent to the case made for explicit typing in Section 3.11 of [RFC8725]: Explicit typing can prevent confusion between different kinds of COSE objects.

**[analysis] For `DEC-005` that is a real input and a constraining one.** It
says a narrow algorithm list is not the mitigation for cross-protocol
confusion — typing the object is — so narrowing `DEC-005` buys us nothing
against this attack class and we need the type indicator **regardless of which
algorithms we pick.** The three records in this lane agree on this from three
directions: `rfc-8392` mandates no algorithm either, and `rfc-9597` names none
at all.

---

## 9. The six `canonical-encoding` conditions — and condition (4) is this record's

| condition | RFC 9596's contribution |
|---|---|
| (1) injective encoding | **nothing**, and §7.5's missing equality relation is a small instance of the same disease one layer up: two byte strings, one meaning |
| (2) decoder rejects non-canonical input | **nothing**, and §2 points the other way: libraries are told to ignore the parameter |
| (3) canonicalise once, at authoring | not addressed |
| (4) **authenticated type indicator carried inside the signed bytes** | **THIS IS IT, AND IT IS THE ONLY DOCUMENT IN THE LANE THAT SUPPLIES IT.** `topics/canonical-encoding.yaml` states condition (4) in those words and records that `R-O-05` *"delivers (3) and (4)"*. Label 16 in the protected bucket is the mechanism; §2's `MUST NOT` is what makes it authenticated. **What the document does not supply is the obligation** — `OPTIONAL` — **or the vocabulary** |
| (5) canonical order for set-valued fields | **nothing** |
| (6) Unicode normalisation rule for identity-bearing text | **nothing, and it bites here.** A `typ` value in the `tstr` branch is identity-bearing text compared for equality, and the document gives no normalisation rule, no case rule and no equality rule. `Unicode`, `normalization` and `normalisation` occur **zero** times |

**[analysis] This is the record that most nearly closes a `canonical-encoding`
condition and the one whose gap is cheapest to close.** Condition (4) needs a
required, protected, canonically-spelled type indicator. RFC 9596 supplies
three of those four properties and leaves "required" and "canonically spelled"
to us — two sentences of profile, against the open-ended work conditions (5) and
(6) need.

---

## 10. The summary's findings, tested against the source

| claim | verdict |
|---|---|
| This is the signed replacement for the tag MD-3 removes; `typ` is inside `Sig_structure` and the CBOR tags are not | **CONFIRMED** (§2), and the `Sig_structure` boundary is now **demonstrated** by the sibling `rfc-8392` extraction's verified A.3 signature. **With one scoping correction: the word `tag` occurs ZERO times in RFC 9596**, so the whole replacement argument is ours and must be cited as `[analysis]` |
| A conformant implementation of RFC 9596 performs no check whatsoever: §2 tells libraries to ignore it and §3's two reject rules are lowercase | **CONFIRMED** (§3), and strengthened by the full keyword census: **3 keywords, no MUST / SHOULD / SHALL / RECOMMENDED at all**, and not one of the three requires anything |
| Its body has exactly three capitalised BCP 14 keywords — one OPTIONAL, one MAY, one MUST NOT, all in §2 | **CONFIRMED exactly**, recounted by line: 112, 119, 130 |
| `typ`'s value space is two global registries with no key component, which `ARCH-0002 P1` rejects | **CONFIRMED** (§7.4). The quotation is now cut from the source rather than glossed around the line break, and the value space is also stated in **§1** — which the summary did not note |
| `typ` explicitly does not describe unprotected headers, exactly where `rfc-9597` permits its claims to sit | **CONFIRMED** (§4) |
| The same type has two wire spellings and no equality rule, so the mechanism can be defeated by respelling | **CONFIRMED and sharpened** (§7.5): the two spellings also differ by an order of magnitude in size — 2 octets against 16 — which this extraction measured |
| `typ` and content type can disagree and nothing notices | **CONFIRMED** (§6, §7.1): §2 distinguishes them only by scope and requires no consistency |
| RFC 8725 is not in this library and the security case rests on its §3.11 | **CONFIRMED** (§1 of this file's preamble, and `requirements.yaml` R-0002) |
| No implementation of label 16 was found, in any language | **not re-testable from the source** — a search result, not a source fact. §7.6 records it with the structural reason §2 gives, and draws the half of the consequence the summary did not: **adopting `typ` costs no library support**, because any COSE library transparent to unknown protected parameters already carries it |

**Nothing in the summary is refuted. One claim is scoped** — the tag-replacement
argument is ours, not the document's — **and three are sharpened.**

---

## 11. Source defects and ambiguities — reported, never repaired

**D-1 · The enforcement side of the mechanism carries no normative force, and
the library layer is told to stand down.** Both of §3's reject rules are
lowercase, §2 says COSE implementations ignore `typ`, and the body contains **no
capitalised MUST, SHOULD, SHALL or RECOMMENDED at all.** The mechanism is a
label with no check attached anywhere in the specification stack. Not a defect
in the drafting sense — it is deliberate, and §2 explains why — but it is a
defect in what the document can be *conformance-tested* against: there is
nothing to test.

**D-2 · The same type has two wire spellings and the document gives no equality
rule.** §7.5. No erratum covers it (checked 2026-10-20).

**D-3 · `typ` and content type can disagree and nothing notices.** Separate
labels (16 and 3) with the same syntax and overlapping value spaces,
distinguished only by scope. Nothing requires consistency, and
`records/ietf/rfc-9943`'s Figure 3 makes `content_type` (3) CDDL-optional in the
protected header while requiring label 15.

**D-4 · It settles nothing about what type names to use.** The parameter is
defined and the vocabulary is left to applications, so adopting `typ` means
either registering a media type or emitting an unregistered string the document
provides no rule for. **[analysis] And §4.1 registers the parameter without
registering a single value**, so the first `typ` value anyone writes down is
unexampled.

**D-5 · The value space is stated twice, in two sections, and the registry name
is severed by the line wrap in both.** §1 (lines 83–87) and §2 (114–119) each
state it, and the plain-text wrap cuts *"CoAP Content-Formats"* in two at
86/87 and again at 116/117, hyphen and all. **Not healed anywhere in this
directory**: `schema/source-renderings.txt` carries the byte-exact lines and
`requirements.yaml` R-0004 and R-0010 carry the flowed span with the hyphen
visible. Recorded because two silently healed line breaks are among the five
transcription defects this lane's own quote audit found in its own prose.

**D-6 · The security case is a forward reference to a document the reader may
not have.** §3's whole substance is that the case *"is equivalent to"* RFC 8725
§3.11's, and none of the argument is reproduced. For us that is a `cites` gap:
**RFC 8725 is not in this library.**

---

## 12. Open questions

1. **What type names do we use?** The parameter is defined and the vocabulary
   is not. Register a media type, or emit an unregistered string? §7.4 says
   neither can express `(defining key, label)`, so this is a choice between two
   kinds of compromise and it should be made explicitly.

2. **Which spelling is canonical — the integer or the string?** §7.5 shows they
   differ by an order of magnitude in size and compare unequal. One line of
   profile fixes it; the line has to be written.

3. **Must `typ` and content type agree?** D-3. Our profile should say yes and
   say how, since `rfc-9943` makes content type optional in the one ratified
   profile we hold.

4. **Do we ingest RFC 8725?** The warrant for a mechanism we intend to require
   is a BCP we do not hold. D-6.

5. **Where in the verification order is `typ` read?** `typ` is inside the
   signature, so its value is only trustworthy *after* verification — and the
   point of a type indicator is to decide *how to verify*.
   `state-machine.yaml` records that the document gives no ordering at all, and
   `rfc-9597` §4's lowercase warning about tentative decisions is the nearest
   thing to guidance in the lane. **[analysis] This is the one open question
   here that is a genuine design problem rather than a drafting gap**, and it is
   the same shape as condition (3)'s "canonicalise once, never at verification".
