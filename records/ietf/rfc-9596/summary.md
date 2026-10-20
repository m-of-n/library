---
schema: "library-summary/v1"
id: rfc-9596
record: rfc-9596
type: summary
updated: "2026-10-20"
---

# CBOR Object Signing and Encryption (COSE) "typ" (type) Header Parameter

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track |
| **Authors** | M.B. Jones (Self-Issued Consulting), O. Steele (Transmute) |
| **Published** | 2024-06 |
| **Identifier** | RFC 9596 · DOI 10.17487/RFC9596 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9596.txt |
| **Digest** | `4beb37fe8cb3eec78cec2445c65dcf2db4866ba99a72e7b1e54e23e5bfa69b5e` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

One COSE header parameter — **label 16, `uint / tstr`** — declaring the type of
the **complete** COSE object, as against label 3's content type, which declares
the type of the payload. §2 draws that line itself: `typ` describes *"the type
of this complete COSE object, as compared to the content type header parameter,
which declares the type of the COSE object payload."* The argument is imported
wholesale from JOSE: §1 cites RFC 8725 §3.11's case for *"explicit typing"*,
and §3 says the COSE case *"is equivalent to"* it.

**The document is three normative sentences long.** Its body contains exactly
three capitalised BCP 14 keywords — one OPTIONAL, one MAY and one MUST NOT, all
in §2 — and **no MUST, SHOULD, SHALL or RECOMMENDED at all** (counted here,
§1.1's boilerplate list excluded). The one MUST NOT is the interesting one:
*"The "typ" parameter MUST NOT be present in unprotected headers."*

So the mechanism is: an optional, signature-covered label, which COSE libraries
are told to ignore, carrying a type name from one of two IANA registries, with
the entire enforcement side left to applications in lowercase prose.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Cross-protocol confusion between kinds of signed object is the attack class; this is the standard defence, and the only *authenticated* type signal in the COSE/CWT set. |
| Cryptography | `none` | Names no algorithm, key type or hash. |
| This project | **core** | It closes the out-of-band gap `rfc-9053`'s extraction left open when option 5 declined the COSE tag. See below. |
| Naming | **core** | Its value space is two global registries with no key component, which is what `ARCH-0002 P1` and `R-M-12` reject. See the MD-3 section. |

### The finding to act on: this is the signed replacement for the tag MD-3 removes

`rfc-9053`'s `distilled/design-notes.md` — a `profile: full` record — lists what
a minimum verifiable `COSE_Sign1` must carry under MD-3 and ends item 6 with the
cost: because `COSE_Sign1_Tagged` is `#6.18` and *"option 5 declines the tag
registry — no tag, which means the recipient must be told out of band that these
bytes are a `COSE_Sign1`."* **Nothing in this library had named the in-band
substitute. It is label 16, and it is strictly better than what it replaces.**

- §2's MUST NOT forces `typ` into the protected bucket, and RFC 9052 §4.4's
  `Sig_structure` is `[context, body_protected, external_aad, payload]`. So
  `typ` is **inside the signature**.
- The CBOR tags are not. `rfc-8392`'s own procedure proves it from inside the
  document: §7.1 step 6 prepends the COSE and CWT tags *after* the signature
  exists, and §7.2 steps 2–3 strip them *before* validation begins. An attacker
  can add or remove tag 18 or tag 61 without touching a signature.

**Therefore MD-3's no-tags rule loses no authenticated information, and
adopting `typ` gains some.** That is worth writing into the `DEC-002` ADR when
it is written, because it converts a recorded cost into a recorded non-cost.
Note the standing caveat from `ADR-0001` — *"CBOR tags and COSE header
parameters are IANA allocated, so they are interchange, not native"* — so `typ`
belongs on the export boundary and nowhere else, which is exactly where MD-3
puts COSE anyway.

### What its absence enables, and what its presence does not prevent

The attack is substitution between kinds of object that share a key and a
shape. Our own case is concrete: an `ArtifactStatement` and a revocation or
delegation statement, both `COSE_Sign1`, both signed by the same issuer key,
both carrying a CBOR map payload. Without a type indicator inside the
signature, a verifier that accepts one will accept the other's bytes in the
other's slot, and every signature check passes. `typ` in the protected header
is what makes those two objects non-interchangeable.

**But the check is ours to write, and the RFC gives no conformance target for
it.** §2 is explicit that the library layer does nothing: *"The "typ" (type)
header parameter is ignored by COSE implementations (libraries implementing
[RFC9052] and this specification), other than being passed through to
applications using those implementations."* And §3's two enforcement sentences
are lowercase — *"COSE applications employing explicit typing should reject
COSE objects with a type header parameter value different than values that they
expect in that application context. They should also reject COSE objects
without a type header parameter when one is expected."* Under §1.1's *"when,
and only when, they appear in all capitals"*, neither carries normative force.
**A conformant implementation of RFC 9596 performs no check whatsoever.**

### Does a CWT need it? No — and that is the problem

`rfc-8392` §6 gives three ways to know a CBOR structure is a CWT: application
context, the `application/cwt` content type from a transport, or CBOR tag 61.
This document adds a fourth. Ranked by whether a verifier can trust them:

| Signal | In band? | Inside the signature? |
|---|---|---|
| application context (`rfc-8392` §6) | no | n/a |
| `application/cwt` via transport (`rfc-8392` §9.2.1) | no | no |
| CBOR tag 61 (`rfc-8392` §6, §9.4.1) | yes | **no** |
| `typ` in the protected header (§2) | yes | **yes** |

Only the last is both. And `rfc-9597`'s duplication MUST — the one hard rule
protecting a verifier that reads claims from a COSE header — is scoped to
claims *"present both in the payload and the header of a CWT"*, while
`rfc-8392` §6 opens with *"How to determine that a CBOR data structure is a CWT
is application dependent."* **So `typ` is the mechanism that
turns `rfc-9597`'s MUST from conditional-on-an-undefined-predicate into
testable**, and §2 makes its use *"OPTIONAL."* That is the join a reviewer
should look at hardest in this lane.

### `typ` explicitly does not reach the bucket `rfc-9597` permits its claims to sit in

§2, two sentences: *"The "typ" parameter does not describe the content of
unprotected headers. Changes to unprotected headers do not change the type of
the COSE object."* Meanwhile `rfc-9597` §1 names `typ` as *"a RECOMMENDED way
to include this information in the COSE structure"* for deriving the intended
interpretation of its CWT Claims header parameter, and `rfc-9597` §2 only
RECOMMENDS that that parameter be protected.

**So when a producer takes the permitted unprotected placement, the recommended
disambiguator is declared, by its own text, not to describe it.** `rfc-9597`
§1's MUST NOT does close the hole — a recipient may not use the information
beyond the protection afforded to *"the CWT Claims header and the information
used to derive its intended interpretation"* — but only for an implementer who
joins three sentences across two documents published the same month by an
overlapping author set.

Not a `contradicts`: the two can be obeyed simultaneously and neither asserts
something the other denies. It is an **asymmetry of protection strength** — one
document makes unprotected placement a MUST NOT violation, the other merely
discourages it — and it is the reason our profile should require protected
placement for both parameters in one sentence rather than inherit two different
strengths.

### DEC-005: it names no algorithm, and that is its contribution

Zero algorithm identifiers in the document. Its `DEC-005` bearing is the
*argument* it adopts from RFC 8725 §3.11 and restates in §3: confusion between
kinds of signed object is defeated by **typing the object**, not by restricting
the algorithm set. For `DEC-005` that is a real input and a constraining one —
it says a narrow algorithm list is not the mitigation for cross-protocol
confusion, so narrowing `DEC-005` buys us nothing against this attack class and
we need the type indicator regardless of which algorithms we pick.

## Where it cuts against MD-3 — DEC-002 option 5

`MD-3` (2026-09-28) narrowed `DEC-002` to option 5 and is a **narrowing, not an
acceptance**; no `DEC-002` ADR exists. Option 5 has two clauses that matter
here, and this document lands on opposite sides of them.

**It rescues the "no IANA tags" clause** — the finding above. Option 5 can drop
tag 18 and tag 61 and lose nothing authenticated, because `typ` carries the
type inside `Sig_structure`.

**It cuts against the "type identity is `(defining key, label)` per P1"
clause.** §2 fixes the value space to an unsigned integer from the CoAP
Content-Formats registry — the registry's name is hyphenated across a line
break in the source, so it is glossed here rather than quoted through the break
— *"or a string content type value. Content type values have a media type name
[MediaTypes] and MAY include media type parameters."* **Both are global
registries with no key component**, which is precisely the shape `ARCH-0002 P1`
and `R-M-12` reject. There is no way to spell a `(defining key, label)` type
name in `typ` except by burying it inside a media type string — itself a global
allocation — or inside the "MAY include media type parameters" clause, which
the document does not constrain at all. **So the mechanism that saves option
5's no-tags clause can only name types the way option 5's P1 clause forbids.**

The honest conclusion is `rfc-9052`'s and it holds again: "no tags" and "no
registry dependence" are different rules, and MD-3 states only the first. Our
export would carry a type name we do not control.

**One concrete consequence for our own linting**, in the same register as
`rfc-9165`'s `any .feature` note: a lint rule enforcing option 5's no-tags
exclusion must **not** treat a `typ` value of `61` as a tag hit. `rfc-8392`
registered 61 twice — CBOR Tag 61 (§9.4.1) and CoAP Content-Format Id 61
(§9.3.1), both for CWT. Under MD-3 the first is forbidden and the second is
available through `typ`. Same number, different registry, opposite verdicts.

## Implementations

*Searched 2026-10-20. No implementation of label 16 was found, in any
language.* The RFC names none and has no implementation-status section. The
negative result is specific rather than vague:

| Name | Kind | License | URL |
|---|---|---|---|
| `python-cwt` | Python CWT/COSE; **RFC 9596 is not in its compliance list at all** | MIT | https://github.com/dajiaji/python-cwt |

`python-cwt` is the most complete CWT/COSE implementation this library has
found, and `typ` does not appear in its stated specification coverage. §2 gives
the structural reason the search came up empty: *"Any processing of this
parameter is performed by the COSE application using application-specific
processing rules"*, so there is nothing for a library to implement beyond
passing an opaque value through — and a library that already passes unknown
header parameters through supports `typ` without saying so.

**Nothing in the library requires it, either.** Across its own definition and
both ratified consumers held here, `typ` is never mandatory: §2 —
*"Use of this header parameter is OPTIONAL"*; `rfc-9597` §1 — RECOMMENDED, with
*"Other methods for determining the intended interpretation MAY also be used"*;
`rfc-9942` §4.4 — *"One way to include this information in the COSE structure
is use of the "typ" (type) header parameter"*, lowercase. The explicit-typing
defence is available everywhere and required nowhere.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on` |
| `summary.md` | this document |
| `summary.html` | GENERATED and untracked — `bin/render-html`, see `docs/generated-views.md` |

**No `distilled/`.** Nothing has been added to a `distilled/` directory, so
FX-1 does not fire (`docs/extraction.md`, CLAUDE.md "Extracting, not
touching"); library#39 Tier 2 owns the eventual extraction. This is the thinnest
record in the lane and an FX-1 pass would mostly document absences: three
stated requirements, one `messages.yaml` entry, one IANA registration table,
**no CDDL**, **no examples and not one byte of hex**, no state machine and no
protocol. The honest FX-1 shape is `normative.md` + `requirements.yaml` +
`design-notes.md` with four `not_applicable` declarations — which is worth
doing precisely because the absences are the content.

Also absent and worth acting on: **`RFC 8725` ("JSON Web Token Best Current
Practices", BCP 225) is not in this library.** §1 and §3 rest the entire
security case on its §3.11 and this document reproduces none of the argument —
§3's whole substance is *"The case for explicit typing of COSE objects is
equivalent to the case made for explicit typing in Section 3.11 of [RFC8725]:
Explicit typing can prevent confusion between different kinds of COSE
objects."* So the warrant for the mechanism we would adopt is a document we do
not hold.
That is a `cites` gap and an ingest candidate, not a defect in this record.

## Limits

- **The enforcement side is entirely non-normative and the library layer is
  told to ignore the parameter.** Both of §3's reject rules are lowercase
  (quoted above), §2 says COSE implementations ignore `typ`, and the body of the
  document contains **no capitalised MUST, SHOULD or RECOMMENDED at all**. The
  mechanism is a label with no check attached anywhere in the specification
  stack. For us that means `typ` is cheap to emit and the whole defence is in
  code we write, with no conformance target to test against.
- **The same type has two wire spellings and the document gives no equality
  rule.** `typ: 61` (CoAP Content-Format, `rfc-8392` §9.3.1) and
  `typ: "application/cwt"` (media type, `rfc-8392` §9.2.1) denote the same type
  and compare unequal under any byte comparison. Media type names are
  case-insensitive — RFC 2045 §5.1, *"The type, subtype, and parameter names
  are not case sensitive"*, a document this library does not hold — while a
  CBOR `tstr` is not, and §2 permits media type *parameters* unconstrained, so
  `application/cwt`, `Application/CWT` and `application/cwt; v=1` are three
  values and one type. §3's only guidance is to reject a *"parameter value
  different than values that they expect in that application context"*, and
  "different" is undefined. **A
  confusion-resistance mechanism with an unspecified equality relation can be
  defeated by respelling the type.** Same shape as `rfc-9165`'s finding that
  `.abnf` controllers are case-insensitive by default and nobody says so: the
  comparison rule is where the default hides. Our rule is one line — map both
  spellings to a single canonical form before comparing, and state which form
  is canonical.
- **`typ` and content type can disagree and nothing notices.** They are
  separate labels (16 and 3) with the same syntax and overlapping value spaces,
  and §2 distinguishes them only by scope — complete object versus payload.
  Nothing requires them to be consistent, nothing forbids a `typ` naming a CWT
  over a payload whose content type says otherwise, and `rfc-9943`'s Figure 3
  makes `content_type` (3) CDDL-optional in the protected header while requiring
  label 15. A verifier reading one and not the other is conformant.
- **It settles nothing about what type names to use.** The parameter is defined
  and the vocabulary is left to applications. For us that is the open question:
  option 5's P1 type identity cannot be expressed in `typ`'s value space (see
  the MD-3 section), so adopting `typ` means either registering a media type or
  emitting an unregistered string the document provides no rule for.
- **Nothing here is reviewed.** Written from the source and from three adjacent
  `profile: full` records (`rfc-9052`, `rfc-9053`, `rfc-9942`); the keyword
  count, the four-signal table and the `Sig_structure` coverage argument are
  ours, and no human has checked them.
