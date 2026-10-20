---
schema: "library-summary/v1"
id: rfc-9597
record: rfc-9597
type: summary
updated: "2026-10-20"
---

# CBOR Web Token (CWT) Claims in COSE Headers

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track |
| **Authors** | T. Looker (Mattr), M.B. Jones (Self-Issued Consulting) |
| **Published** | 2024-06 |
| **Identifier** | RFC 9597 · DOI 10.17487/RFC9597 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9597.txt |
| **Digest** | `b6baaec655bc86606602a6f6e93f0103db6e6f98460f1e43437e74a6a5e02bdd` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

One COSE header parameter — **label 15, value type `map`** — whose contents are
a CWT Claims Set. §1 names the three cases it exists for: encrypted COSE
structures, detached signatures, and payloads that are not CWT Claims Sets
"including payloads that are not CBOR at all". JOSE had the equivalent in
RFC 7519 §5.3 and COSE did not, which §1 calls *"an omission that this
specification corrects."*

**The reason it is one parameter holding a nested map, rather than claims placed
directly in the header, is a label collision — and the document says so.** §1:
*"Directly including CWT claim values as COSE header parameter values would not
work, since there are conflicts between the numeric header parameter
assignments and the numeric CWT claim assignments."* The collision is total
across the cheap range: CWT claims 1/2/3/4 are `iss`/`sub`/`aud`/`exp` while
COSE header parameters 1/2/3/4 are `alg`/`crit`/`content type`/`kid`. The fix
was to buy one allocation and nest the whole claim space inside it.

Three normative sentences follow, and the rest of the document is
considerations. Everything load-bearing is in §1 and §2.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | It decides whether `iss` is inside or outside the signature, which is a coverage question, not a layout one. |
| Cryptography | `none` | Names no algorithm, no key type, no hash. Zero. |
| This project | `core` | If we export `COSE_Sign1 + CWT claims` per `R-I-03`, this is where `iss`/`sub` go, and `rfc-9943` §6 already requires it of that shape. |
| Naming | **core** | §1's collision rationale is field evidence for `R-M-12`. See below. |

### The finding to act on: protected placement is RECOMMENDED, and that is not enough

§2: *"It is RECOMMENDED that the CWT Claims header parameter only be used in a
protected header to avoid the contents being malleable."* RECOMMENDED, not
required — and §2's one hard placement rule is weaker than it first reads:
*"The header parameter MUST only occur once in either the protected or
unprotected header of a COSE structure."* That bars label 15 appearing in
**both** buckets; it expressly permits it appearing in the unprotected one.

RFC 9052 §4.4's `Sig_structure` is
`[context, body_protected, external_aad, payload]`. The unprotected header is
not an input. **So a fully conformant producer can emit a CWT Claims header
parameter — `iss`, `sub`, everything — that no signature covers at all.**

The document's defence is placed on the party under attack, not on the format.
§1: *"Recipients of the CWT Claims header parameter MUST NOT use the
information in the CWT Claims header parameter beyond the integrity protection
or authentication afforded to the CWT Claims header and the information used to
derive its intended interpretation."* That is a real MUST NOT and it is correct,
but it is unenforceable by the producer, untestable by a conformance checker,
and defeated by any COSE API that presents a merged view of the two header maps
to its caller.

**Every serious consumer therefore has to close this itself, and the first
ratified one did.** `rfc-9943` §6 — *"The protected header of a Signed Statement
and a Receipt MUST include the CWT Claims header parameter as specified in
Section 2 of [RFC9597]"* and *"The CWT Claims value MUST include the Issuer
Claim (Claim label 1) and the Subject Claim (Claim label 2)"*. So the action is
not to invent a rule: our profile states protected-only placement with
mandatory `iss`/`sub`, and cites RFC 9943 §6 as the precedent, which is what
`R-O-03`'s "cited, not invented silently" discipline asks of us even though
this is a placement rule rather than a canonicalization one.

### The duplication MUST has two escape hatches, and one is a predicate nobody defines

§2: *"In cases where CWT claims are present both in the payload and the header
of a CWT, an application receiving such a structure MUST verify that their
values are identical, unless the application defines other specific processing
rules for these claims."* §4 gives the rationale — eliminating *"potential
confusion that might arise by having different values for the same claim"*.

Both escape hatches matter:

1. **The `unless` clause voids it by profile.** An application may legally
   declare that header and payload claims differ, which is precisely the
   confusion §4 says the rule eliminates. Nothing constrains what those "other
   specific processing rules" may be.
2. **It fires only for "a CWT", and no document defines when that is.**
   `rfc-8392` §6 opens with *"How to determine that a CBOR data structure is a
   CWT is application dependent."* Meanwhile §2's last paragraph here says the
   parameter *"MAY be used in any COSE object using header parameters, such as
   COSE_Sign objects. Its use is not restricted to CWTs."* So the scope of this
   document's only hard duplication rule rests on a classification the defining
   document explicitly declines to specify.

**That is what makes `rfc-9596` load-bearing rather than decorative in this
lane**: a protected-header `typ` is the one in-band, signature-covered way to
make "this is a CWT" a fact a verifier can check, which is the predicate this
MUST needs. §1 reaches for it for a related reason and only RECOMMENDS it.

And "identical" is not defined. Byte equality of the encoded items, or equality
of the CBOR data items? A preferred and a non-preferred encoding of the same
integer are one value and two byte strings. For a determinism-sensitive library
that is a `DEC-002` touchpoint and the document settles nothing; a verifier
comparing bytes and a verifier comparing values disagree on inputs neither
would call malformed.

### `R-M-12`: this is the failure R-M-12 exists to prevent, happening in the field

`R-M-12` requires an extension point to be a `(key, local label)` pair. §1
records what happens without one: two independently governed global integer
label spaces — the COSE Header Parameters registry and the CWT Claims registry
— grew into each other across their whole cheap range, and the only available
remedy was to buy one label in the first registry and nest the second registry
inside it.

**Label 15 is a one-level approximation of `(key, local label)` where the "key"
is an IANA allocation instead of ours.** The shape is right and the owner is
wrong. That is the strongest piece of *evidence* for `R-M-12` in this lane —
evidence rather than argument, because the IETF paid for it rather than
predicting it, and the tag is set to `evidence` for that reason. Worth citing in
the eventual `R-M-12` justification, which currently rests on reasoning about
the CBOR tag registry and the simple-value registry
(`iana-cbor-simple-values`, held for exactly that argument) and has no case
where two registries actually collided.

### DEC-005: the weakest `bears_on` of the three, stated plainly

This record is filed `bears_on: [DEC-005]` and the document names **no
algorithm, no key type and no hash anywhere**. Its only genuine `DEC-005`
connection is §1's observation that an issuer value in the header is readable
before decryption and *"is used for key discovery"* — a precondition for
selecting a key, and therefore an algorithm, rather than a selection rule.

The stronger edges are to `R-M-12` (above) and to `DEC-003`/`R-O-01` (where
`iss` lands and whether it is signed). `bears_on` is left as recorded rather
than quietly widened; this paragraph is the flag, and whoever owns `DEC-005`
should decide whether to add `R-M-12` or to drop `DEC-005`.

## Where it cuts against MD-3 — DEC-002 option 5

**For option 5's no-tags clause, cleanly.** Label 15 is a COSE **header
parameter**, not a CBOR tag. Claims reach the header with no involvement of the
CBOR Tags registry at all, and when the header is protected they are inside
`Sig_structure`. MD-3's "no IANA tags" is untouched by anything in this
document, and the mechanism is the one way in the COSE set to carry CWT claims
without ever touching tag 61 — see `rfc-8392`'s record for why tag 61 and the
COSE tags come as a pair.

**Against option 5, and this is the cost `rfc-9052` deferred to exactly here.**
That record's `distilled/design-notes.md` §3.2 closes with: *"the CWT claim keys
are their own registry, so CWT interchange carries a second, larger registry
dependence than the tag; that is a DEC-003 and DEC-005 matter and is outside
this record."* Label 15's **Value Registry column is `[CWT.Claims]`** (§2,
Table 1), so this parameter does not merely permit that dependence — it names
the registry as the definition of its own value space. Nesting a registry inside
a header parameter removes the tag dependence and installs a claim-key
dependence in its place. `rfc-9052`'s formulation holds and is now confirmed one
layer down: **"no tags" and "no registry dependence" are different rules, and
MD-3 states only the first.**

Two further costs, both measurable:

- **Option 5's type identity is `(defining key, label)` per `ARCH-0002 P1`, and
  nothing here can express that.** `Claim-Label = int / text` is a flat global
  space with no key component, and even the strictest ratified profile keeps it
  open: `rfc-9943`'s Figure 3 gives `CWT_Claims = { &(iss: 1) => tstr,
  &(sub: 2) => tstr, * label => any }` with `label = int / tstr`. The tightest
  consumer in the library still admits any global label.
- **Privacy is structural, not incidental, and it reaches the naming scheme.**
  §3: *"Since CWT claims in COSE headers are not encrypted"*. Pre-decryption
  visibility *is* the feature, so publication is the price. Under `ARCH-0002 P1`
  the issuer key identifier is the root of the whole naming scheme, so a
  protected-header `iss` publishes the principal in the clear on every object we
  emit. That is a trade to make deliberately rather than inherit.

## Implementations

*Searched 2026-10-20. No library was found that implements the published RFC.*
That is the result, and the detail is worth keeping:

| Name | Kind | License | URL |
|---|---|---|---|
| `python-cwt` | Python; implements `draft-ietf-cose-cwt-claims-in-headers-06`, **marked experimental**, not RFC 9597 | MIT | https://github.com/dajiaji/python-cwt |
| SCITT `draft-ietf-scitt-scrapi` | specification, not a library; its Signed Statement example carries label 15 in the protected header with `iss` (1) and `sub` (2) nested | — | https://datatracker.ietf.org/doc/draft-ietf-scitt-scrapi/ |

Two years after publication, the most complete CWT implementation in the
library's reach still cites the **draft** and flags it experimental, and the
only concrete uses found are specifications rather than code: `rfc-9943` §6
requires label 15, `rfc-9942` §4.4 points at the same guidance, and SCRAPI
prints it. For a parameter whose whole value is interoperability, that matters:
**we would be an early implementer, not a late one.** The RFC itself names no
implementation and has no implementation-status section.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on` |
| `summary.md` | this document |
| `summary.html` | GENERATED and untracked — `bin/render-html`, see `docs/generated-views.md` |

**No `distilled/`.** Nothing has been added to a `distilled/` directory, so
FX-1 does not fire (`docs/extraction.md`, CLAUDE.md "Extracting, not
touching"); library#39 Tier 2 owns the eventual extraction. This is the
*smallest* of the three records in the lane — the whole document is 265 lines
and its body holds **8 capitalised BCP 14 keywords** (2 MUST, 1 MUST NOT,
2 RECOMMENDED, 3 MAY, all in §1 and §2; counted here, boilerplate excluded).
An FX-1 pass on it would be short but not empty: a `requirements.yaml` of 8
stated plus the lowercase inferred ones, a `schema/` holding the four CDDL lines
(verbatim, and declared non-normative by the source), one `messages.yaml` entry
for label 15, and `design-notes.md`. There are **no test vectors to extract** —
the document prints not one byte, no hex, no diagnostic-notation example and no
complete COSE object, which is itself the finding an `examples/` artifact would
have to record.

No `contradicts` edge is set. `rfc-9596` makes protected placement a MUST NOT
violation for `typ` where this document only RECOMMENDS it for label 15, which
is an asymmetry rather than an incompatibility — the two can both be obeyed at
once — so `see_also` with the asymmetry written out is the honest relation.
No `updates: rfc-8392` either, for the reason in Limits.

## Limits

- **It adds a MUST to CWT processing and does not announce itself as updating
  CWT.** `rfc-8392` §7.2's seven validation steps contain nothing about header
  claims, and this document's duplication rule is step eight for anyone who
  opts in — yet RFC 9597 carries no "Updates: 8392" header, and `rfc-8392` has
  no way to point forward. An implementer working from RFC 8392 alone never
  learns the rule exists. **Recorded as `see_also` rather than `updates`,
  deliberately**: a CWT that declines label 15 needs nothing whatever from this
  document, so `updates` would assert an incompleteness in RFC 8392 that is not
  there. The missing forward pointer is the finding; the relation is not the
  place to put it.
- **The only structural description of the value is non-normative, and the
  document says so.** §2: *"The following is a non-normative description for the
  value type of the CWT claim header parameter using CDDL [RFC8610]."* So
  `CWT-Claims = { * Claim-Label => any }` with `Claim-Label = int / text`
  constrains nothing: an **empty map `{}`** is admitted, `* ` permits zero
  entries, and no normative sentence forbids a float, boolean or byte-string
  claim label. Table 1's Value Type column says `map` and nothing narrows it
  further with force. For `R-O-03`'s cite-don't-invent discipline there is
  nothing here to cite.
- **§3 and §4 contain zero capitalised BCP 14 keywords.** All 8 are in §1 and
  §2 (counted above). So the document's most important security instruction —
  *"Implementers must ensure that any tentative decisions made based on
  previously unverified information are confirmed once the cryptographic
  processing has been completed"* (§4) — is lowercase, and §1.1 restricts
  interpretation to keywords *"when, and only when, they appear in all
  capitals, as shown here."* The rule against acting on unverified claims, in a
  document whose entire purpose is to make claims readable before verification,
  carries no normative force under the document's own terms. §3's privacy
  guidance is in the same position.
- **It does not say how to use any claim it relocates.** §1: *"This
  specification does not define how to use CWT claims and their semantics for
  particular applications, whether they are in the COSE payload or the CWT
  Claims header parameter, or both."* Correct scoping, and it means the
  mechanism is inert without a profile. Ours does not exist yet.
- **Nothing here is reviewed.** Written from the source and from two adjacent
  `profile: full` records (`rfc-9052`, `rfc-9943`); the keyword count and the
  `Sig_structure` coverage argument are ours, and no human has checked them.
