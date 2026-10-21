---
record: rfc-9597
kind: design-notes
title: "rfc-9597 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2`) are RFC 9597's. Our own documents are cited by id (`ARCH-0002 P1`,
`DEC-005`, `MD-3`, `R-M-12`). Three markers distinguish voices, following
`records/ietf/rfc-8949/distilled/design-notes.md` and `rfc-9741`'s:

- unmarked prose reports **RFC 9597** or **our decisions**, as cited;
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

What *is* checkable here, and was: `docs/extraction.md`'s statement of MD-3
(*"option 5: reduced CBOR, no IANA tags, COSE as export only"*),
`topics/canonical-encoding.yaml`'s six conditions and its identification of
DEC-002 options 1 and 3, and the artifacts of `records/ietf/rfc-9052`,
`records/ietf/rfc-8392`, `records/ietf/rfc-9596` and `records/ietf/rfc-9943`.

**How quotations of the library's own artifacts are normalised here.** A
quotation of another record's `design-notes.md` or `summary.md` is quoted from
its **rendered** text: markdown emphasis (`*`, `**`) and code markers
(backticks) are dropped, because they are formatting rather than words.
Quotations of the **source** are not normalised beyond whitespace, are cut from
`.cache/` by line range by script, and where one **is** elided the elision is
visible as `...` and the full sentence is carried verbatim in
`requirements.yaml`; where a sentence spans a line break the break is declared
and the obligation-bearing half is quoted. This pass's own quote audit found
four defects in its own prose under those rules, and each is recorded in place
where it occurred rather than edited away.

*[correction 2026-10-21, pass 3 — cross-check] This said source quotations are
**never elided**. Two in this directory are — see the correction at D-4 — so
the rule is now stated as what it actually is. A blanket "never" is worse than
the narrower truth, because it stops a reader checking.*

**Decision status.** DEC-002 in `ARCH-0001` §7 lists **four** options; "option
5" exists only as *proposed* text in `ARCH-0001-PROPOSAL-v0.2.0` §3.3, which is
unmerged; `MD-3` (2026-09-28) *narrows* DEC-002 to option 5 and
`DECISIONS-0001` item 2 says *"a narrowing is not an acceptance"*. **No DEC-002
ADR has been written.** Within this library option 1 is canonical S-expressions
(`records/ietf/rfc-9804`) and option 3 is JCS over JSON
(`records/ietf/rfc-8785`), per `topics/canonical-encoding.yaml`.

---

## 1. What this record decides, in one paragraph

**This is where a protected `iss` comes from, and the document does not require
it to be protected.** §2 only *recommends* it, and its one hard placement rule
is weaker than it reads. So the decision this record forces on us is not
*whether* to use label 15 — `rfc-9943` §6 already shows the shape — but to
**state protected-only placement ourselves and cite a precedent for it**, because
RFC 9597 gives a conformant producer permission to emit an unsigned `iss`.

---

## 2. The finding to act on: protected placement is RECOMMENDED, and that is not enough

**CONFIRMED against the source.** §2:

> It is RECOMMENDED that the CWT Claims header parameter only be used in a protected header to avoid the contents being malleable.

RECOMMENDED, not required. And §2's one hard placement rule does not close it:

> The header parameter MUST only occur once in either the protected or unprotected header of a COSE structure.

**That bars label 15 appearing in *both* buckets; it expressly permits it
appearing in the unprotected one.** RFC 9052 §4.4's `Sig_structure` is
`[context, body_protected, external_aad, payload]` and the unprotected header is
not an input. **So a fully conformant producer can emit a CWT Claims header
parameter — `iss`, `sub`, everything — that no signature covers at all.**

**[analysis] And that coverage boundary is now demonstrated rather than read.**
`records/ietf/rfc-8392`'s extraction, in this same pass, rebuilt
`Sig_structure` from RFC 9052 §4.4 and **verified RFC 8392's A.3 signature from
exactly those four fields** — so the unprotected map is provably not an input,
not merely absent from a definition we read. The document whose examples prove
it is the one this parameter exists to extend.

The defence RFC 9597 does provide is placed on the party under attack. §1:

> Recipients of the CWT Claims header parameter MUST NOT use the information in the CWT Claims header parameter beyond the integrity protection or authentication afforded to the CWT Claims header and the information used to derive its intended interpretation.

That is a real `MUST NOT` and it is correct. It is also **unenforceable by the
producer, untestable by a conformance checker, and defeated by any COSE API
that presents a merged view of the two header maps to its caller.** Note its
second conjunct — the protection afforded to *"the information used to derive
its intended interpretation"* — which means an *unprotected* `typ` would cap
the claims' usability too, and `rfc-9596` §2 makes `typ` protected-only by
`MUST NOT`. The two documents interlock here, and only for an implementer who
joins three sentences across two specifications published the same month.

**What we do.** Our profile states protected-only placement with mandatory
`iss`/`sub` and cites `rfc-9943` §6 as the precedent — *"The protected header of
a Signed Statement and a Receipt MUST include the CWT Claims header parameter as
specified in Section 2 of [RFC9597]"* and *"The CWT Claims value MUST include
the Issuer Claim (Claim label 1) and the Subject Claim (Claim label 2)"*. That
is `R-O-03`'s cite-don't-invent discipline applied to a placement rule.

---

## 3. The duplication MUST has two escape hatches, and one is a predicate nobody defines

**CONFIRMED.** §2:

> In cases where CWT claims are present both in the payload and the header of a CWT, an application receiving such a structure MUST verify that their values are identical, unless the application defines other specific processing rules for these claims.

§4 gives the rationale:

> The reason for applications to verify that CWT claims present in both the payload and the header of a CWT are identical, unless they define other specific processing rules for these claims, is to eliminate potential confusion that might arise by having different values for the same claim, which could result in inconsistent processing of such claims.

**Hatch 1 — the `unless` clause voids it by profile.** An application may
legally declare that header and payload claims differ, which is precisely the
confusion §4 says the rule eliminates. Nothing constrains what those *"other
specific processing rules"* may be.

**Hatch 2 — it fires only for "a CWT", and no document defines when that is.**
`records/ietf/rfc-8392` §6 opens *"How to determine that a CBOR data structure
is a CWT is application dependent."* Meanwhile §2's last paragraph here says:

> The CWT Claims header parameter MAY be used in any COSE object using header parameters, such as COSE_Sign objects. Its use is not restricted to CWTs.

So **the scope of this document's only hard duplication rule rests on a
classification the defining document explicitly declines to specify.**

**[analysis] That is what makes `rfc-9596` load-bearing rather than decorative
in this lane.** A protected-header `typ` is the one in-band, signature-covered
way to make "this is a CWT" a fact a verifier can check, which is the predicate
this `MUST` needs. §1 reaches for `typ` for a related reason and only
`RECOMMENDED`s it; `rfc-9596` §2 makes its own use *"OPTIONAL."* **The chain is
RECOMMENDED over OPTIONAL, resting on a predicate that is application
dependent.**

**And "identical" is not defined.** Byte equality of the encoded items, or
equality of the CBOR data items? A preferred and a non-preferred encoding of the
same integer are one value and two byte strings. For a determinism-sensitive
library that is a `DEC-002` touchpoint and the document settles nothing: a
verifier comparing bytes and a verifier comparing values disagree on inputs
neither would call malformed. **[analysis] The cheap fix is ours and is one
line: compare the decoded CBOR data items, and require RFC 8949 §4.2.1 on both
sides so the two questions coincide.**

---

## 4. R-M-12 — this is the failure R-M-12 exists to prevent, happening in the field

**CONFIRMED, and it is the strongest piece of *evidence* for `R-M-12` in this
lane.** §1 records what happens without a `(key, local label)` extension point:

> Directly including CWT claim values as COSE header parameter values would not work, since there are conflicts between the numeric header parameter assignments and the numeric CWT claim assignments.

And the remedy:

> Instead, this specification defines a single header parameter registered in the IANA "COSE Header Parameters" registry that creates a location to store CWT claims in a COSE header parameter.

**[analysis] The collision is total across the cheap range.** CWT claim keys
1/2/3/4 are `iss`/`sub`/`aud`/`exp` (`records/ietf/rfc-8392` §9.1.2) while COSE
header parameters 1/2/3/4 are `alg`/`crit`/`content type`/`kid` (RFC 9052 §3.1).
Two independently governed global integer label spaces grew into each other,
and the only available remedy was to **buy one label in the first registry and
nest the second registry inside it.**

**Label 15 is a one-level approximation of `(key, local label)` where the "key"
is an IANA allocation instead of ours.** The shape is right and the owner is
wrong. It is evidence rather than argument **because the IETF paid for it rather
than predicting it**, which is why this record's `tags` carry `evidence`. Worth
citing in the eventual `R-M-12` justification, which otherwise rests on
reasoning about the CBOR tag registry and the simple-value registry
(`records/ietf/iana-cbor-simple-values`, held for exactly that argument) and has
**no case where two registries actually collided.**

**[analysis] And the collision was cheap to survive only because label 15 was
available.** `records/ietf/rfc-8392`'s extraction priced the equivalent move on
the other side: in the CWT Claims registry the cheap range (−256…255) is
**Standards Action** *and* restricted to claims of general applicability, and
the only policy-free range costs **5 octets against 1**. A second collision,
after the cheap COSE header labels run out, has no equally cheap remedy.

---

## 5. What we adopt

1. **Label 15 itself, in the protected header.** It is the registered way to
   put `iss` and `sub` where a verifier reads them without parsing the payload,
   and `rfc-9943` §6 is the ratified precedent for requiring it.
2. **§1's nesting pattern as a design rule.** When two label spaces we do not
   own would collide, buy one label and nest. That is the shape `R-M-12` wants;
   we differ only in who owns the outer label.
3. **§4's provisionality discipline, promoted to a `MUST`.** See §6.3.
4. **§3's statement of the privacy price, as a thing to decide rather than
   inherit.** See §7.5.

---

## 6. What we adapt, and what we reject

### 6.1 Protected-only placement — adapted from RECOMMENDED to MUST

§2 recommends; our profile requires, citing `rfc-9943` §6 (§2 above).

### 6.2 "Identical" — adapted into a defined comparison

Compare decoded CBOR data items, under RFC 8949 §4.2.1 on both sides (§3
above). The document defines nothing; we must.

### 6.3 §4's lower-case `must ensure` — adapted into a normative rule

> Processing information in claims prior to validating that their integrity is cryptographically secure can pose security risks. This is true whether the claims are in the payload or a header parameter. Implementers must ensure that any tentative decisions made based on previously unverified information are confirmed once the cryptographic processing has been completed. This includes any information that was used to derive the intended interpretation of the CWT claims parameter.

Lower case, and §1.1 restricts normative force to keywords
*"when, and only when, they appear in all capitals, as shown here."* **In a
document whose entire purpose is to make claims readable before verification,
the rule against acting on unverified claims carries no normative force under
its own terms.** We make it a `MUST`, and we add the failure action the document
omits: a tentative decision that is not confirmed is a rejection, not a
continuation.

### 6.4 Unprotected placement — rejected outright

Permitted by §2, and it produces an unsigned `iss`. We forbid it.

### 6.5 The `unless` escape hatch — rejected for our own profile

We will not define *"other specific processing rules"* that let header and
payload claims differ. If they differ, the object is invalid.

### 6.6 The flat global claim-label space as our extension point — rejected

`Claim-Label = int / text` has no key component (§7.4). Our own fields do not go
in there; see `records/ietf/rfc-8392`'s design notes §6.2 for what the Private
Use range costs.

---

## 7. MD-3, header by header — and where this document cuts against it

`MD-3` narrowed DEC-002 to **option 5**: `docs/extraction.md`, which is in this
repository, states it as *"reduced CBOR, no IANA tags, COSE as export only"*.
A **narrowing, not an acceptance.**

### 7.1 The header-by-header mapping

RFC 9597 defines exactly one header, so the mapping is short — and its interest
is in which of our fields can and cannot ride inside it.

| our field (ARCH-0001 §4.1) | carrier in this document | label | registry | option-5 verdict |
|---|---|---|---|---|
| issuer principal | `iss` **inside** label 15 | 15 → 1 | COSE Header Parameters → CWT Claims | **carry, protected.** The reason to use this document at all |
| subject | `sub` inside label 15 | 15 → 2 | → CWT Claims | **carry, protected** |
| validity window | `exp`, `nbf` inside label 15 | 15 → 4, 5 | → CWT Claims | carry — and **nothing in either document reads them** |
| statement id | `cti` inside label 15 | 15 → 7 | → CWT Claims | carry |
| statement type | **not here** — `rfc-9596` `typ` | 16 | COSE Header Parameters | §1 only `RECOMMENDED`s it, and `rfc-9596` §2 makes it `OPTIONAL` |
| `KeyId` of the signing key | **not here** — COSE `kid` | 4 | COSE Header Parameters | RFC 9597 says nothing about `kid`; see `rfc-8392`'s notes |
| our own fields | a Private Use claim key inside label 15 | 15 → < −65536 | none | **reject** — 5 octets each and unscoped |
| the claims' *interpretation* | §1's three sources: other headers, `typ`, or anything | — | — | **ours to fix**: §1 permits "other methods" without constraining them |

**The export mapping, in one line.** One COSE header parameter, label 15, in
the **protected** bucket, holding a CBOR map of CWT claim keys 1–7 only, with
`typ` (label 16) beside it in the same bucket to make the interpretation
in-band, and nothing of ours inside label 15.

**What we deliberately do not carry:** label 15 in the unprotected bucket
(§6.4), any Private Use claim key (§6.6), and any reliance on §1's unconstrained
*"Other methods"* (the table's last row).

### 7.2 Cut 1 — **for** option 5's no-tags clause, cleanly, and this is the one place the lane helps MD-3

Label 15 is a COSE **header parameter**, not a CBOR tag. Claims reach the header
with **no involvement of the CBOR Tags registry at all**, and when the header is
protected they are inside `Sig_structure`. MD-3's *"no IANA tags"* is untouched
by anything in this document, and this is **the one way in the COSE set to carry
CWT claims without ever touching tag 61** — see `records/ietf/rfc-8392`'s design
notes for why tag 61 and the COSE tags come as a pair, which that record
confirmed from §6's text and from all five of its printed CWTs.

### 7.3 Cut 2 — the registry dependence is not merely permitted, it is **named**. **Costs option 5; options 1 and 3 do not pay it.**

This is the cost `records/ietf/rfc-9052`'s design notes deferred by name: *"the
CWT claim keys are their own registry, so CWT interchange carries a second,
larger registry dependence than the tag; that is a DEC-003 and DEC-005 matter
and is outside this record."*

**Here it is not a consequence but a column.** §2's Table 1 gives label 15 a
**Value Registry** of `[CWT.Claims]`, so this parameter *defines its own value
space as an IANA registry*. Nesting a registry inside a header parameter removes
the tag dependence and installs a claim-key dependence in its place.

`topics/canonical-encoding.yaml`, which is in this repository, records that
option 3 *"is registry-free by construction"* and that **option 1 also wins that
criterion**, *"by the same argument and without paying option 3's §5 cost."* So
on namespace governance this document moves option 5 **further behind both.**
`rfc-9052`'s formulation holds and is now confirmed one layer down, quoted
exactly: **"No tags" and "no registry dependence" are different rules, and MD-3 states the first.**
**[analysis] The word *only* is this extraction's, not that record's, and it is
the whole of what these three documents add to the claim.**

### 7.4 Cut 3 — option 5's type identity is `(defining key, label)` and nothing here can express it. **Costs option 5.**

`ARCH-0002 P1` wants key-relative identity. The source's own CDDL —
non-normative, and the only structural description it offers — is:

```
CWT-Claims = {
 * Claim-Label => any
}

Claim-Label = int / text
```

A flat global space with **no key component**, and even the strictest ratified
profile the library holds keeps it open: `records/ietf/rfc-9943`'s Figure 3
gives `CWT_Claims = { &(iss: 1) => tstr, &(sub: 2) => tstr, * label => any }`
with `label = int / tstr`. **The tightest consumer in the library still admits
any global label.** This is the same cut `rfc-9596`'s record makes about `typ`'s
two registries and `rfc-8392`'s makes about the claim registry: **three
documents in one lane, three different registries, one shape.**

### 7.5 Cut 4 — privacy is structural, and it reaches the naming scheme. **Costs option 5 and option 3 alike; option 1 the same.**

§3:

> Some of the registered CWT claims may contain privacy-sensitive information. Since CWT claims in COSE headers are not encrypted, when privacy-sensitive information is present in these claims, applications and protocols using them should ensure that these COSE objects are only made visible to parties for which it is appropriate for them to have access to this sensitive information.

**Pre-decryption visibility *is* the feature** (§1 names it as the point), so
publication is the price. **[analysis] Under `ARCH-0002 P1` the issuer key
identifier is the root of the whole naming scheme, so a protected-header `iss`
publishes the principal in the clear on every object we emit** — including
objects whose payload we encrypted precisely so it would not be read. That is a
trade to make deliberately rather than inherit, and no DEC-002 option changes
it: the field is outside the ciphertext under every encoding.

### 7.6 Cut 5 — **[analysis]** the mechanism has no implementation, so adopting it makes us an early implementer rather than a late one. **Costs option 5 specifically.**

MD-3's *"COSE as export only"* clause is an interoperability argument: export in
COSE because other people read COSE. This record's own search (2026-10-20,
recorded in `record.yaml`) found **no library implementing the published
RFC** — `python-cwt` implements `draft-ietf-cose-cwt-claims-in-headers-06` and
marks it **experimental**, two years after publication — and the only concrete
uses found are specifications: `rfc-9943` §6 requires label 15, `rfc-9942` §4.4
points at the same guidance, and `draft-ietf-scitt-scrapi` prints it.

**[analysis] For a parameter whose whole value is interoperability, that
inverts the argument for option 5's export clause at exactly this joint.** It
does not touch the clause as a whole — COSE_Sign1 itself has several
implementations, as `rfc-8392`'s record lists — but the specific field we would
put `iss` in has none, so "export in COSE because it interoperates" is not yet
true of *this* header. Recorded as a cost with a shelf life: it expires the day
a library ships label 15.

**[pass 2, 2026-10-20 — RE-DATED, NOT RE-ASSERTED.]** This is the one argument
in the record that rests on a search rather than on a document, so pass 2
treats it as evidence with a timestamp rather than as a finding to confirm.
**Pass 2 did not repeat the search**, and deliberately: a second unreproducible
search on the same day adds a date and no information, and would make a
one-source claim look corroborated. So the claim stands on **pass 1's
2026-10-20 search alone**, by one agent, and nothing here raises its
confidence.

What that means for anyone reading this cut:

- Treat the sentence as *"as of 2026-10-20, one search found no library
  implementing the published RFC"* — not as *"no implementation exists."*
- It is the **only** cut in this file that a reader cannot check against a
  cached source in this repository. Every other cut here is checkable against
  `.cache/rfc-9597.txt` or another record's artifacts, and pass 2 did check
  those.
- **What would refresh it**, in order of strength: a `python-cwt` release note
  that drops `draft-ietf-cose-cwt-claims-in-headers-06` for RFC 9597; an entry
  in a COSE interop matrix; a second independent library. Any one of those
  retires the cut.
- **It expires on its own**, unlike every other cut in this file, so a profile
  must not be built on it. Weight it accordingly in the `DEC-002` ADR: it is
  the weakest evidence in this record and it is the only piece with an expiry
  date.

---

## 8. DEC-005 — the weakest `bears_on`, and the honest statement of it

This record is filed `bears_on: [DEC-005]` and the document names **no
algorithm, no key type and no hash anywhere.** Its only genuine `DEC-005`
connection is §1's observation that an issuer value in the header is readable
before decryption and that *"the issuer value is used for key discovery"* (§1,
source lines 79–80) — a precondition for selecting a key, and therefore an
algorithm, rather than a selection rule. *[correction 2026-10-21, pass 3 —
cross-check] The quotation marks around that clause were missing, which left a
verbatim fragment of §1 reading as our own words and an orphaned full stop
before the dash. `summary.md` carries the same clause marked, so the two now
agree.*

The stronger edges are to `R-M-12` (§4) and to `DEC-003`/`R-O-01` (where `iss`
lands and whether it is signed). **[analysis] `R-M-12` is now carried, so the
remaining question for whoever owns `DEC-005` is whether to drop it**; this
pass widened `bears_on` to six ids rather than leaving the mismatch silent, and
the evidence for each addition is annotated in `record.yaml`. `summary.md`
carries the same statement.

---

## 9. The six `canonical-encoding` conditions, as this document leaves them

| condition | RFC 9597's contribution |
|---|---|
| (1) injective encoding | **nothing**, and §2's undefined *"identical"* makes the gap bite: the duplication check's result depends on whether you compare bytes or values |
| (2) decoder rejects non-canonical input | **nothing** |
| (3) canonicalise once, at authoring | **compatible by silence**; nothing here re-encodes |
| (4) authenticated type indicator inside the signed bytes | **§1 is the whole of the document's answer and it is the weakest possible one**: `MAY` from other headers, `RECOMMENDED` via `rfc-9596`'s `typ`, `MAY` by any other method. Condition (4) is the one this document most nearly addresses and it lands on a recommendation |
| (5) canonical order for set-valued fields | **nothing** |
| (6) Unicode normalisation rule for identity-bearing text | **nothing.** `Unicode`, `normalization` and `normalisation` occur **zero** times, and the text this parameter exists to expose — `iss` — is the identity-bearing text |

**[analysis] Condition (4) is where this record does the most work and still
falls short.** It supplies the *location* for an interpretation signal and
declines to require one. `rfc-9596` supplies the signal and makes it
`OPTIONAL`. Neither closes (4); together they make it closable in one sentence
of our own profile, which is a better position than either document alone.

---

## 10. The summary's findings, tested against the source

| claim | verdict |
|---|---|
| Protected placement is RECOMMENDED, not required, and §2's one hard rule bars only *both* buckets, so a conformant producer can emit claims no signature covers | **CONFIRMED** (§2), and the coverage boundary is now **demonstrated** by `rfc-8392`'s verified A.3 signature rather than read off RFC 9052 §4.4 |
| The duplication MUST has two escape hatches, one of them a predicate `rfc-8392` §6 declines to define | **CONFIRMED** (§3). Both quoted verbatim |
| §1's collision rationale is field evidence for `R-M-12` | **CONFIRMED** (§4), and the 1/2/3/4 collision is now stated from both registries |
| Label 15's Value Registry column names `[CWT.Claims]`, so the parameter installs a claim-key dependence rather than merely permitting one | **CONFIRMED** (§7.3). It is a column of Table 1, not an inference |
| §3 and §4 contain zero capitalised BCP 14 keywords; all 8 are in §1 and §2 | **CONFIRMED exactly.** Recounted here by line: 102, 105, 107, 108 in §1 and 148, 152, 154, 157 in §2 |
| The only structural description of the value is non-normative and the document says so | **CONFIRMED** (§7.4), and the declaration is captured **in the same verbatim region** as the fragment so the two cannot be separated |
| No library implements the published RFC | **not re-testable from the source** — it is a search result, not a source fact. Recorded in §7.6 as this record's own `record.yaml` states it, with the shelf life named |

**Nothing in the summary is refuted.** This is the record in the lane whose
summary survives contact with the source best, and the reason is visible: at
265 lines with 8 keywords, there was little room for the summary to drift.

---

## 11. Source defects and ambiguities — reported, never repaired

**D-1 · "Identical" is undefined, in the document's only hard comparison
rule.** §2 (quoted in §3 above). Byte equality or data-item equality; the
document does not say, and the two differ on inputs neither would call
malformed. No erratum covers it (checked 2026-10-20).

**D-2 · The duplication rule is scoped to a classification no document
defines.** §2's *"both in the payload and the header of a CWT"* against
`rfc-8392` §6's *"How to determine that a CBOR data structure is a CWT is
application dependent"* and §2's own *"Its use is not restricted to CWTs."*
Not a contradiction — a rule with an undecidable antecedent.

**D-3 · It adds a step to CWT processing and does not announce itself as
updating CWT.** `rfc-8392` §7.2's seven validation steps contain nothing about
header claims, and this document carries **no `Updates: 8392` header**. An
implementer working from RFC 8392 alone never learns the rule exists. **This
record's `record.yaml` records why `updates` was considered and rejected as a
relation** — a CWT that declines label 15 needs nothing from this document, so
`updates` would assert an incompleteness in RFC 8392 that is not there. The
missing forward pointer is the finding; the relation is not the place to put it.

**D-4 · The document's most important instruction is lower case.** §4, quoted
whole rather than elided, because the elided clause is the load-bearing one:

> Implementers must ensure that any tentative decisions made based on previously unverified information are confirmed once the cryptographic processing has been completed.

In a document whose purpose is pre-verification readability. §3's privacy
guidance is in the same position. Under §1.1 neither binds. Recorded rather
than smoothed over.

**[correction, found by this pass's own quote audit]** An earlier draft of this
file quoted that sentence as *"Implementers must ensure that any tentative
decisions ... are confirmed once the cryptographic processing has been
completed"* — an **ellipsis splice**, which is the first of the five
transcription defect classes this lane's audit was built to catch and which it
duly caught here. The elided span is *"made based on previously unverified
information"*, the clause that names **what** the decision rested on and so the
most load-bearing part of the sentence.

**[correction 2026-10-21, pass 3 — cross-check]** That paragraph ended
*"Nothing in this directory now elides a quotation."* **Withdrawn** — it was
false when written and the lane-wide audit found two surviving elisions in this
very directory: `protocol.yaml`'s quotation of §1's `MUST NOT`, which elides
*"in the CWT Claims header parameter"* after *"use the information"*, and
`requirements.yaml`'s *"These include encrypted COSE structures ... and/or those
featuring a detached signature"*, which elides *", which may or may not be an
encrypted CWT,"*. Pass 3 also found and removed a third, the `*"either … or"*`
construction recorded at D-6 below.

What is actually true is narrower, and is the convention this directory keeps:
**an elision is always visible as `...` and the full sentence is carried
verbatim in `requirements.yaml`** — R-0002 holds the `encrypted COSE structures`
sentence whole, and R-0014 the `MUST NOT`. The blanket claim is the defect, not
the practice. The same unqualified sentence appears in `rfc-8392`'s and
`rfc-9596`'s design notes, where four declared bullet abbreviations apiece make
it false in the same way.

**D-5 · The interpretation chain bottoms out in an unconstrained permission.**
§1 (source lines 106–107):

> Other methods for determining the intended interpretation MAY also be used.

Any method at all, with no requirement that it be in band, authenticated, or
even stated. The `RECOMMENDED` in the preceding sentence is therefore not a
floor. *[correction 2026-10-21, pass 3 — cross-check] That sentence was printed
as unmarked prose, so a verbatim `MAY` of the source was indistinguishable from
this file's own voice. It is `R-0013`, and it is now a blockquote like every
other source quotation here.*

**D-6 · The placement `MUST` is ambiguous, and the whole placement model turns
on which reading is taken. [found 2026-10-20, pass 2 — verify; not in pass 1's
defect list]** §2, source lines 153–155 — the sentence's first word, *The*, is
the last word of line 153, so `normative.md` captures the whole placement
paragraph as lines 152–155; this note read *154–155* until pass 3 recomputed
the span:

> The header parameter MUST only occur once in either the protected or unprotected header of a COSE structure.

The English admits three readings and the document disambiguates none of them:

1. **Once across both buckets** — so label 15 may be in the protected bucket or
   in the unprotected one, but never in both. This is the reading
   `schema/cwt-claims-header.derived.cddl` takes, and it is the reading that
   makes that file's enumeration of **exactly three** conformant shapes
   complete.
2. **At most once per bucket** — so a fourth shape exists, label 15 in both
   buckets with one occurrence each, and the derived CDDL is then *incomplete*
   rather than wrong. Under this reading §2's duplication `MUST` (payload
   against header) acquires a sibling problem it never addresses: which of two
   headers wins.
3. **Exactly once, i.e. required** — reading `MUST only occur once` as
   asserting the occurrence. This one is defeated from inside §2, whose last
   paragraph says the parameter *"MAY be used in any COSE object using header
   parameters"*, and by the absence of any sentence requiring label 15
   anywhere in the document.

**Reading 1 is the right one and this record keeps it** — reading 3 is excluded
by §2 itself, and reading 2 would leave the document's one cardinality rule
saying nothing about the case it most obviously exists to prevent. But it is a
reading, not a statement, and a profile that enforces "not in both" is
enforcing our interpretation of an ambiguous `MUST`. **No erratum covers it
(checked 2026-10-20).** It belongs with D-1: this document's two hard rules are
its duplication `MUST` and its placement `MUST`, and **both of them turn on
wording the document leaves undefined** — *"identical"* in the first, and in
the second the scope of the either/or: whether *"MUST only occur once in either
the protected or unprotected header of a COSE structure"* counts occurrences
across the two buckets together or within each one.

*[corrected 2026-10-21, pass 3 — cross-check] This sentence named the second
one as `*"either … or"*`, an **elided quotation**, in the same section as D-4's
own correction note, which states that "Nothing in this directory now elides a
quotation." The construction is now named without quotation marks and the rule
is quoted whole. The same elision stood in `README.md` and had been copied into
`summary.md`; both are corrected.*

---

## 12. Open questions

1. **Where does the interpretation signal actually come from in our profile?**
   §1 offers three sources and requires none. If the answer is `rfc-9596`'s
   `typ`, our profile must require it — because `rfc-9596` §2 makes it
   `OPTIONAL` and §1 here only `RECOMMENDED`s it, so the chain is
   recommendation over option.

2. **Do we ever put a claim in both the payload and the header?** If never, the
   duplication rule is moot for us and D-1's ambiguity costs nothing. If ever,
   we owe the comparison definition in §6.2. **[analysis] The cheaper answer is
   "never": carry each claim in exactly one place and say which.**

3. **Where is a tentative decision confirmed, and what happens when it is
   not?** §4 names the duty and omits the failure action, and
   `state-machine.yaml` records that this is the one place a lifecycle would
   have been useful — it describes two states of a decision and names neither.
   Our profile owes both.

4. **Does a protected-header `iss` leak more than we can accept?** §3 makes
   publication structural, and under `ARCH-0002 P1` the issuer identifier is the
   root of the naming scheme. The question is not answerable from this document
   and should not be deferred past the first encrypted statement we emit.

5. **Do we wait for an implementation?** §7.6 records that none exists for the
   published RFC. Adopting label 15 makes us an early implementer, which is a
   position with costs and with one benefit — our fixtures would be the first,
   and `examples/README.md` records that **every fixture for label 15 would be
   ours** under `R-O-03` because the document prints not one byte.
