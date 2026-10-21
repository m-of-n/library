---
record: rfc-9338
kind: design-notes
title: "rfc-9338 — design notes"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9338 — design notes

**What this file is.** How *COSE: Countersignatures* bears on our design: what
we adopt, adapt or reject, mapped onto `ARCH-0001`, `ARCH-0002 P1`, `DEC-002`,
`DEC-003`, `DEC-005`, `R-M-12`, `R-O-01`, `R-O-03`, `R-O-05`, the
`canonical-encoding` conditions and `MD-3`; where the source **cuts against**
`MD-3`; the source's own defects; and what remains open.

| | |
|---|---|
| **Source** | `.cache/rfc-9338.txt`, 921 lines |
| **Digest** | `3fd3a4b1cb4060070ffcf6104de0c12c6c5bed6cf2329d9019a16f7717365dde` |
| **Standing** | **STD 96** with RFC 9052, Standards Track, `Updates: 9052` |
| **Normative surface** | **2 BCP 14 keywords**, both `MUST`, neither about countersignatures |
| **Errata** | **1** — EID 7338, *Reported*, §3.3 (searched 2026-10-20) |
| **Adopt / adapt / reject** | 3 adopt · 4 adapt · 5 reject |
| **Cuts against MD-3** | **5**, each naming the `DEC-002` option it affects |
| **Source defects** | **7**, recorded and not repaired; **1 of them is new and reproducible** |

## Provenance, and what cannot be checked here

Every quotation of RFC 9338 in this file is a contiguous span of
`.cache/rfc-9338.txt`, cut by line range or verified mechanically as a
substring of the whitespace-normalised source, and carries its `§`. The
coverage table in §3 is **derived** — by script, from this library's verbatim
capture of RFC 9052's CDDL at
`records/ietf/rfc-9052/distilled/schema/cose.cddl` — and the derivation is
`schema/bstr-slot-census.derived.txt`. The byte strings in §3 and §4 were
constructed and are in `examples/vectors.yaml`.

**Every quotation or characterisation of `ARCH-0001`, `ARCH-0002`, `DEC-002`,
`DEC-003`, `DEC-005`, `MD-3`, `R-M-12`, `R-O-01`, `R-O-03`, `R-O-05` and
`PLAN-*` is `[unverifiable-here]`.** This library is standalone by design
(`CLAUDE.md`) and holds none of those documents; the convention is
`records/ietf/rfc-9741`'s and `records/ietf/rfc-9964`'s. The *findings* in this
file are measured against the source and against RFC 9052's CDDL; the `mofn`
ids say which of our decisions a measured finding bears on, and none of them is
load-bearing for whether the finding is true.

**Decision status, stated once so nothing below over-claims.** `MD-3`
`[unverifiable-here]` narrowed `DEC-002` to **option 5** — reduced CBOR data
model, no IANA tags, COSE as export only — on 2026-09-28. **It is a narrowing,
not an acceptance, and no `DEC-002` ADR exists.** `docs/extraction.md` is
explicit that an extraction which only confirms the narrowing is not evidence,
so §7 below names where this document cuts against it.

---

## 1. What this document is

A repair, and a small one. §1: the working group *"decided to remove all of the
countersignature text from [RFC9052], which obsoletes [RFC8152]"*, and this
document puts the mechanism back with new labels. What it adds to the wire is
two unprotected header parameters (11 and 12), one CBOR tag (19), and three
CDDL rules of which two are one-line aliases of RFC 9052 types.

It carries **two** BCP 14 keywords in 921 lines, and neither is about
countersignatures: §4's inherited determinism rule and §6's tag-length floor.
Every migration obligation — the whole backward-compatibility contract of a
repair document — is **lowercase**. `requirements.yaml`'s reconciliation names
each one.

---

## 2. What we adopt

**A-1. The countersignature as the shape of a witness or receipt over one
exported statement, and only that.** §3.1 is the property that earns it:
*"Specifically, the countersigner does not need to be related to the producer
of what is being countersigned, as key and algorithm identification can be
placed in the countersignature attributes."* `rfc-9338#R-0063`. Nothing else in COSE
lets a third party speak about somebody else's message without re-signing it.
**Scoped in §3 and §9 below to the targets where it binds something.**

**A-2. The `context` text string as the shape of an authenticated type
indicator** — a type discriminator inside the signed bytes rather than beside
them. That is what `R-O-05` `[unverifiable-here]` asks for and what
`canonical-encoding` condition (4) is about. We adopt the **shape**. §3 shows
the document's own values failing to discriminate, so this is an adopt with a
worked counter-example attached, which is more useful than either alone.

**A-3. The algorithm-class restriction, as a `DEC-005` input.** §3.1: *"It
should be noted that only a signature algorithm with appendix (see Section 8.1
of [RFC9052]) can be used for countersignatures."* `rfc-9338#R-0074`, with the
reason given: *"This is because the body should be able to be processed without
having to evaluate the countersignature, and this is not possible for signature
schemes with message recovery."* `rfc-9338#R-0075`. A real constraint on any
algorithm list, stated once and in a sentence that reads like an aside. It costs
us nothing — nothing we are considering has message recovery — and it is worth
carrying because it is a *reason*, not a list.

---

## 3. The coverage derivation — the headline, re-derived

This is the part of the extraction that matters, and it has to be derived
rather than asserted, because **RFC 9338 states the answer for exactly one of
its eight permitted target structures.**

### 3.1 The rule, verbatim

§3.3, `other_fields`: *"Omitted if there are only two bstr fields in the target
structure."* `rfc-9338#R-0097` *"This field is an array of all bstr fields after
the second."* `rfc-9338#R-0098` *"As an example, this would be an array of one
element for the COSE_Sign1 structure containing the signature value."*
`rfc-9338#R-0099`

And the `context` string follows it: *"CounterSignature" for countersignatures
using the COSE_Countersignature structure when other_fields is absent.*
`rfc-9338#R-0089` — *"CounterSignatureV2" for countersignatures using the
COSE_Countersignature structure when other_fields is present.* `rfc-9338#R-0091`

So **which targets get the version-2 signed bytes is arithmetic on RFC 9052's
grammar**, and the only switch is `other_fields`.

### 3.2 The count is by TYPE SLOT, and §3.3's own example proves it

`COSE_Sign1 = [Headers, payload : bstr / nil, signature : bstr]`, and
`Headers = (protected : empty_or_serialized_map, unprotected : header_map)`
with `empty_or_serialized_map = bstr .cbor header_map / bstr .size 0` — all
from `cose.cddl`, verbatim.

The claim *"an array of one element ... containing the signature value"* holds
**only** if `protected` is `bstr` field one and `payload : bstr / nil` is
`bstr` field two. Drop `protected` and the two `bstr` fields are `payload` and
`signature`, so `other_fields` is omitted. Drop `payload : bstr / nil` and the
two are `protected` and `signature`, so `other_fields` is omitted again. **Both
must count, and the document's own sentence is the only thing that fixes
it.** `rfc-9338#R-0099`

### 3.3 The table, derived by script from `cose.cddl`

| target | `bstr` type slots, in order | wire items when the payload/ciphertext is `nil` | `other_fields` | `context` (full form) | in which permitted-target list |
|---|---|---:|---:|---|---|
| `COSE_Sign1` | protected, payload, signature | 3 → **2** | **[signature]** | `CounterSignatureV2` | §2 **and** §3.3 |
| `COSE_Mac` | protected, payload, tag | 3 → 2 | **[tag]** | `CounterSignatureV2` | §2 **and** §3.3 |
| `COSE_Mac0` | protected, payload, tag | 3 → 2 | **[tag]** | `CounterSignatureV2` | §2 **and** §3.3 |
| `COSE_Signature` | protected, signature | 2 → 2 | omitted | `CounterSignature` | §2 **and** §3.3 |
| `COSE_Sign` | protected, payload | 2 → 1 | omitted | `CounterSignature` | **§3.3 only** |
| `COSE_Encrypt` | protected, ciphertext | 2 → 1 | omitted | `CounterSignature` | §2 **and** §3.3 |
| `COSE_Encrypt0` | protected, ciphertext | 2 → 1 | omitted | `CounterSignature` | §2 **and** §3.3 |
| `COSE_recipient` | protected, ciphertext | 2 → 1 | omitted | `CounterSignature` | **§2 only** |

**`other_fields` reaches three of eight.** Five of eight therefore sign RFC
8152's context string, so the document's only domain separator does not
separate the two versions of the algorithm for most targets. §1 says so
outright, from the other direction: the new algorithm *"is designed to produce
the same countersignature value in those cases where the computed cryptographic
value was already included"* `rfc-9338#R-0009`, and *"the only thing that would
need to be done is to change the value of the header parameter"*
`rfc-9338#R-0010`.

**Of the three that do get `other_fields`, it carries a SIGNATURE for exactly
one.** `COSE_Mac` and `COSE_Mac0` get a **MAC tag** — §3 says so: *"When done
on a COSE_Mac or COSE_Mac0, the payload is included as well as the MAC
value."* `rfc-9338#R-0056` So *"binds the target's signature bytes"* is true of
`COSE_Sign1` and of nothing else.

**§3's widest claim does not survive this.** *"The new version now includes the
cryptographic material generated for all of the structures rather than just for
a subset."* `rfc-9338#R-0052` For `COSE_Sign` no cryptographic material is
included at all.

### 3.4 Where a sibling pass's headline has to be **scoped**, and one limb **refuted**

The framing this pass was handed was: *a countersignature on a `COSE_Signature`
does not cover the signature it countersigns*, with §1's *"The exception to this
is the COSE_Signature structure where there is no cryptographically computed
value"* `rfc-9338#R-0008` against §3's *"the normal countersignature semantics are
preserved"* `rfc-9338#R-0054`, *both cannot hold*.

**That depends on a reading of `Countersign_structure.payload` which the
document does not state, and the better-supported reading goes the other way.**
§3.3 defines the field as *"The payload to be signed, encoded in a bstr type.
The payload is placed here independently of how it is transported."*
`rfc-9338#R-0096` — and **four of the eight permitted targets have no `payload`
field at all**: `COSE_Signature`, `COSE_Encrypt`, `COSE_Encrypt0`,
`COSE_recipient`. Two readings are available.

**Reading P (positional).** The target's **second `bstr` slot** fills
`payload`. Three independent things support it:

1. *"all bstr fields after the second"* `rfc-9338#R-0098` presupposes that the
   first two are carried elsewhere — and `body_protected` is defined as *"The
   serialized protected attributes from the target structure"* `rfc-9338#R-0093`,
   i.e. the first. `payload` is the only remaining slot for the second.
2. §1's *"the third slot of the array"* `rfc-9338#R-0006`. RFC 8152 §4.5 reused
   RFC 9052's `Sig_structure` and took the target as *a set of protected
   attributes, a set of unprotected attributes, and a body, in that order*
   (RFC 8152 §4.5, read for this derivation on 2026-10-20 and **not copied into
   this library**). The "body" **is** the third array element — the second
   `bstr`. For `COSE_Signature` that is the signature; for `COSE_Encrypt` the
   ciphertext; for `COSE_Sign1` and the MAC structures the payload, which is
   precisely where the old algorithm went wrong.
3. §1's *"the same countersignature value in those cases where the computed
   cryptographic value was already included"* `rfc-9338#R-0009` is **only true
   under reading P**. The cases where the value was already included are exactly
   `COSE_Signature`, `COSE_Encrypt`, `COSE_Encrypt0` and `COSE_recipient`, and
   they stay the same only if their crypto value keeps landing in `payload`.

**Reading S (semantic).** `payload` means the content, which is what *"placed
here independently of how it is transported"* is about — a detached-payload
instruction. Under S, a `COSE_Signature` target's signature bytes are in no
field of `Countersign_structure`.

**Both were built.** `examples/vectors.yaml` V-0013 (reading P, 93 bytes) and
V-0014 (reading S, 48 bytes), from Appendix A.1.1's own components.

**Verdicts, one per limb:**

- **The `bstr`-slot table: CONFIRMED**, row for row, re-derived mechanically.
- **"`other_fields` binds the target's signature bytes" is true of exactly one
  of the seven §3.3 targets: CONFIRMED.** `COSE_Mac`/`COSE_Mac0` carry a tag.
- **"§3.3's target enumeration is seven and `COSE_recipient` is not among it":
  CONFIRMED**, and `COSE_recipient` does carry a `Headers` bucket, so there is
  no structural reason for the omission.
- **"A countersignature on a `COSE_Signature` does not cover the signature":
  REFUTED as stated, SCOPED to reading S.** Under reading P, which has three
  independent supports and reading S has one, the signature lands in `payload`
  and §3's claim holds. What is true under **both** readings is weaker and
  still worth having: **the enclosing `COSE_Sign`'s protected bucket is covered
  nowhere**, because `body_protected` is *"from the target structure"*
  `rfc-9338#R-0093` and the target is the `COSE_Signature`. A countersignature over
  one signer's `COSE_Signature` does not bind the message's content type or
  `crit`.
- **"§1 and §3 contradict each other": SCOPED to an under-specification, not a
  contradiction.** They are reconcilable under reading P and irreconcilable
  under reading S, and §3.3 chooses neither. Calling it a contradiction
  over-states what the text supports; calling it nothing under-states it. It is
  a **two-way ambiguity in the one sentence the document exists to get right**,
  and the measurable consequence is in §10 defect 2.
- **"Two signers over one payload produce a byte-identical
  `Countersign_structure`, so a countersignature over Alice's `COSE_Signature`
  verifies unchanged as one over Bob's": REFUTED under reading P, CONFIRMED
  under reading S.** Constructed both ways, not argued:
  `examples/vectors.yaml` `collisions`. Under S both are
  `sha256:88b49d7260ca695ceab460c7f3464cc5e2de77ee488a72332d022811272fab3c`,
  because the structure depends on the `COSE_Signature`'s **protected** bucket
  and `kid` is **unprotected** in all six of the document's examples. Under P
  each signer's own signature value distinguishes them.
- **"A countersignature on a `COSE_Sign` binds no signature at all": CONFIRMED,
  and UNCONDITIONAL.** `signatures : [+ COSE_Signature]` is an array, not a
  `bstr` field, so it is neither the second `bstr` slot nor a member of *"all
  bstr fields after the second"* under either reading. V-0007 is the whole
  45-byte to-be-signed structure and no signature value appears in it. This is
  the limb that bears on §9.

---

## 4. `body_protected` / `sign_protected` — the same ambiguity, in two more fields

§3.3: `body_protected` is *"The serialized protected attributes from the target
structure"* `rfc-9338#R-0093`; `sign_protected` is *"The serialized protected
attributes from the signer structure"* `rfc-9338#R-0094`, and the process inputs
name *"the signer information (COSE_Signature)"* `rfc-9338#R-0084` as separate
from the target.

**When the target is itself a `COSE_Signature`, both inputs are
`COSE_Signature`s and the field names stop disambiguating them.** RFC 9052 §4.4
uses the *same two field names* in `Sig_structure` for the **body** and the
**signer**, so a reader who transfers that meaning — which the names invite —
gets a different answer from a reader who follows RFC 9338's own definitions.

**The document's own example cannot settle it**, and that is a measurement
rather than a complaint: Appendix A.1.1 says *"The same header parameters are
used for both the signature and the countersignature"* `rfc-9338#R-0135`, so both
candidate values for `sign_protected` are `h'a10126'` and the two readings give
**byte-identical** results. There is no example anywhere in the document where
they differ.

**And the omission rule names only one of the two abbreviated context
strings.** `sign_protected` is *"omitted for the Countersignature0V2
attribute"* `rfc-9338#R-0094`. For an abbreviated countersignature over a
`COSE_Encrypt0`, whose context string is `"CounterSignature0"` by §3.3's own
bullets, the text does not say whether the field is absent or
present-and-empty — and the two give different signed bytes. The charitable
reading is that *"the Countersignature0V2 attribute"* means the label-12
attribute whatever the context string. The document does not say so.

**For us.** Our export is a single-signer `COSE_Sign1` `[unverifiable-here,
`DEC-005`]`, where none of this bites: `body_protected` is unambiguous and
`other_fields` is `[signature]`. The moment a *k*-of-*n* export becomes a
`COSE_Sign` with *n* `COSE_Signature`s, every one of these ambiguities becomes
load-bearing at once. §9.

---

## 5. What we adapt, and how

**AD-1. The `context` string becomes `(defining key, local label)`-scoped, not
a global text string.** `R-M-12` `[unverifiable-here]` requires an extension
point to be a *(key, local label)* pair, and `ARCH-0002 P1` makes type identity
*(defining key, label)*. RFC 9338's discriminator is a bare global text string
in a registry nobody keys. We keep the *position* — inside the signed bytes,
§3.3 — and replace the *value* with a key-relative one. §3 is the worked reason:
a global string that five of eight targets share cannot discriminate.

**AD-2. Protected, not unprotected.** §2 puts label 11 *"as an unprotected
attribute"* `rfc-9338#R-0033` and §3.2 puts label 12 *"as an unprotected header
parameter"* `rfc-9338#R-0081`. That is structurally necessary for a countersignature
— a value the primary signature covered could not be added afterwards — and it
means **anything we place beside a countersignature is unsigned by the primary
signer**. `records/ietf/rfc-9052/distilled/design-notes.md` records
protected-only placement as our adaptation; adopting a countersignature at all
is therefore a **deliberate, recorded exception to a rule we have already
written down**, not something to discover later.

**AD-3. The determinism obligation is inherited and partial.** §4: *"The
deterministic encoding rules are defined in Section 4.2 of [RFC8949]."*
`rfc-9338#R-0111` *"These rules are further narrowed in Section 9 of [RFC9052]."*
`rfc-9338#R-0112` *"The narrowed deterministic encoding rules MUST be used to
ensure that all implementations generate the same byte string for the"* — and
the source's next two words are its own quoted phrase, `"to be signed"`,
followed by *"value."* `rfc-9338#R-0113` **The quotation is broken at the nested
quotation marks rather than re-punctuated: the source writes them, and healing
them into single quotes would be an alteration.** **Scoped to the to-be-signed
value, not to the
message** — so an implementation gets a byte-stable `Countersign_structure` and
a byte-unstable message, exactly as `rfc-9052`'s extraction found for its
parent. Appendix A.3.1 demonstrates it: that example's recipient unprotected
map is written `{-1: …, 4: …}` and RFC 8949 §4.2.1 bytewise key ordering would
put `4` first. The document's own example is not in deterministic key order,
and §4 does not require it to be.

**AD-4. Chaining is kept, bounded.** §3.1: *"This also means that the
countersignature can itself be countersigned."* `rfc-9338#R-0064` with §3's *"including
chained countersignatures"* `rfc-9338#R-0047`. No depth limit, no processing
order, no termination rule — and because each link's target is
`COSE_Signature`-shaped, **a chain of countersignatures is a chain of the
weakest row in §3.3's table**. If we ever carry a chain we state a depth bound
and a processing order, and we do not inherit the silence.

---

## 6. What we reject, and why

**RJ-1. The abbreviated form (label 12), entirely.** §3.2: the verification
parameters *"are provided by the same context used to describe the encryption,
signature, or MAC processing"* `rfc-9338#R-0078`, and §1.3 defines *"Context"* as
*"information that is not part of the COSE message"* `rfc-9338#R-0024`. A witness
or transparency service is **by definition** outside that context. §3 adds that
the structure *"only contains the signature value and nothing else"*
`rfc-9338#R-0049`. There is no field for a key identifier, and the document gives
label 12 **no permitted-target list anywhere**.

**RJ-2. The countersignature as the carrier for `Endorse`.** Already settled in
`records/ietf/rfc-9052/distilled/design-notes.md` §6 on four grounds, and §3
above sharpens the third of them: there is nowhere to put the weight or the
scope, and the attributes that do exist are global COSE labels that `R-M-12`
bars natively.

**RJ-3. CBOR tag 19 on the wire.** §5.1 registers it `rfc-9338#R-0118` and it is the
only new CBOR tag in this lane. `MD-3`'s option 5 excludes IANA tags. §7 cut 1
is where this is argued, because the cut is **shallow and names a real cost**,
and the shallow part has to be said as plainly as the cost.

**RJ-4. Relying on the `context` string as a version indicator.** §3 gives the
non-convertibility rule a mechanism: *"as the signature computation includes a
parameter identifying which structure is being used, the converted structure
will fail signature validation"* `rfc-9338#R-0050`. True between the full and
abbreviated forms. **Not** true between version 1 and version 2, for five of
eight targets, where the string is identical. We do not build a version check on
it.

**RJ-5. The notary reading of what a countersignature attests.** §3 offers it
and withdraws its essential element in the same sentence: *"A notary typically
includes a timestamp to indicate when notarization occurs; however, such a
timestamp has not yet been defined for COSE."* `rfc-9338#R-0040` A countersignature
attests **existence without time**, which is most of what a witness is wanted
for. Any receipt of ours carries its own time field, in the protected bucket,
and cites nothing for it because there is nothing to cite — `R-O-03`
`[unverifiable-here]` applies.

---

## 7. Where this document cuts against MD-3

`MD-3` `[unverifiable-here]` is a dated **narrowing** of `DEC-002`, not an
acceptance, and `docs/extraction.md` requires an extraction to say where the
source cuts against it. **Five cuts. Three name the `DEC-002` option they
favour, one is stated in option 5's favour, and one indicts the narrowing's
silence rather than any option.** `[analysis]` throughout: the document takes no
view on our decision.

### 7.1 MD-3 header by header

Option 5 is *reduced CBOR data model, no IANA tags, COSE as export only, type
identity `(defining key, label)` per `ARCH-0002 P1`* `[unverifiable-here]`.
Header by header, this document's surface is **four code points**:

| this document's element | kind | registry | option-5 verdict |
|---|---|---|---|
| `Countersignature version 2` = **11** | COSE header parameter, unprotected | COSE Header Parameters (**global**, Value Registry blank `rfc-9338#R-0121`) | **admissible** — a header parameter is not an IANA tag. Costs `R-M-12`: see cut 2 |
| `Countersignature0 version 2` = **12** | COSE header parameter, unprotected | same | **rejected by us** on RJ-1, not by option 5 |
| **CBOR tag 19** | IANA CBOR tag | CBOR Tags | **excluded by option 5's one spelled-out exclusion** — cut 1 |
| `Countersign_structure` | to-be-signed array, never transmitted `rfc-9338#R-0019` | none | **admissible and invisible**: not emitted, so option 5's encoding rules never see it |

**The export mapping, in one line.** A receipt over a `COSE_Sign1` export is a
`COSE_Countersignature` at label 11 in that `COSE_Sign1`'s unprotected map,
untagged, whose `Countersign_structure` is
`["CounterSignatureV2", body_protected, sign_protected, external_aad, payload,
[signature]]` — `examples/vectors.yaml` V-0008 is a worked 120-byte instance of
exactly that shape. **No CBOR tag is emitted anywhere in it.**

### 7.2 Cut 1 — tag 19, and the cut is shallow. **Costs option 5, and names the one thing option 5 cannot carry.**

§5.1 registers tag 19 with the Semantics *"COSE standalone V2
countersignature"* `rfc-9338#R-0118`, and §3.1 supplies the escape: *"The full
countersignature structure can be encoded as either tagged or untagged,
depending on the context."* `rfc-9338#R-0067` The label-11 and label-12 forms are
**untagged**. So option 5 can carry every in-message countersignature this
document defines at full fidelity and never emit a tag. **The literal clause
cuts; the cut is shallow.**

**What option 5 cannot carry is a *detached* countersignature, and that is the
cost to name.** Tag 19 exists for nothing else — *standalone* is in its
registered Semantics. A transparency receipt or a witness statement that must
be stored, cited or served **separately** from the statement it covers has
exactly one sanctioned way to identify itself out of context, and option 5
forbids it. The alternative is our own framing, which `R-O-03`
`[unverifiable-here]` then obliges us to cite, and there is nothing to cite.
**Name it against option 5 explicitly: the receipt either lives inside the
message it witnesses, or it is an invention.**

**And the standalone form is under-specified even for whoever does emit the
tag**, which blunts the cost. `protocol.yaml` flow F-4 is empty by measurement:
nothing in RFC 9338 says how a standalone countersignature names the structure
it countersigns, how the two are associated, or what a recipient does with a
tag-19 item it cannot match to a target — and a verifier needs
`body_protected`, `external_aad`, `payload` and `other_fields` **from the
target** to rebuild `ToBeSigned`. So option 5 forecloses a mechanism that is
one registry row and no procedure. Options 1 and 3 `[unverifiable-here]` do not
forbid the tag, but they do not supply the missing procedure either: **no
option gets a working detached receipt out of this document.** That is why this
cut is recorded as *real but shallow*, and why it points at an increment rather
than at a different option.

### 7.3 Cut 2 — the extension point is a global label with no key component. **Favours nothing in `DEC-002`; indicts the mechanism. Costs option 5 at the `R-M-12` joint.**

§3: a full countersignature *"has the same structure as COSE_Signature"*
`rfc-9338#R-0046` and so *"can have protected and unprotected attributes,
including chained countersignatures"* `rfc-9338#R-0047`. §5.2 put labels 11 and 12
in the **COSE Header Parameters** registry with the Value Registry **blank**
`rfc-9338#R-0121`. So a countersignature nests a second, **unbounded** instance of
the same global label space, scoped by neither key nor countersigner, and §3.1
lets it recurse `rfc-9338#R-0064`.

**The contrast is in this library and it is exact.** `rfc-9360` §3's
`x5*-sender` labels were placed by IANA in the COSE Header **Algorithm**
Parameters registry, which scopes them to an *(algorithm, label)* pair — a
weaker scoping than `R-M-12`'s *(key, label)*, but a scoping. RFC 9338 chose the
unscoped registry. `R-M-12` and `ARCH-0002 P1`'s *(defining key, label)* have
**no native expression here**, which is the same finding `rfc-9052`'s
extraction reached about COSE generally; this document is the sharpest instance
of it, because the thing being nested is a whole second copy of the header
space.

### 7.4 Cut 3 — option 5's determinism is byte-stable only for what is signed. **Favours option 1. Costs option 5 and option 2 equally.**

§4's `MUST` `rfc-9338#R-0113` binds the *"to be signed"* value. The transmitted message is
left to RFC 9052 §9, which `rfc-9052`'s extraction found applies to the
to-be-signed structures and **not** to the transmitted message. **Appendix
A.3.1 is the live demonstration**, measured in this pass: its recipient
unprotected map is written `{-1: …, 4: …}`, and under RFC 8949 §4.2.1 bytewise
ordering the encoded keys are `0x20` and `0x04`, so deterministic order puts
`4` first. One of the document's own six examples is not in deterministic key
order, in a document whose single encoding `MUST` is about determinism.

An option that makes the **whole encoding** canonical — option 1
`[unverifiable-here]` — does not have this seam. Option 5 inherits it from COSE
and option 2 names CBOR+CDDL and inherits it too. This is the same cut
`rfc-9804`'s extraction made for `canonical-encoding`, arriving here from a
different document; it is recorded as a convergence rather than as news.

### 7.5 Cut 4 — the type indicator option 5 wants exists here and carries the wrong value. **Stated in option 5's favour, narrowly.**

`canonical-encoding` condition (4) wants an **authenticated type indicator
inside the signed bytes**, and `R-O-05` `[unverifiable-here]` is where that
lives. RFC 9338 has one: `context`, field 1 of `Countersign_structure`, inside
`ToBeSigned` by construction. **That is a genuine point in favour of the COSE
family and therefore of option 5** — compare `rfc-8742`, whose extraction found
a container with *no* in-band type indicator at all, and `rfc-9679`'s bare
`ckt`.

**Narrowly**, because §3 shows the indicator's own values failing: five of eight
targets sign RFC 8152's string. So what option 5 inherits is the right
**slot** with a demonstrated-bad **value**, and our AD-1 replaces the value.
A cut in option 5's favour that still owes a correction is worth more than a
clean confirmation, which is `docs/extraction.md`'s point.

### 7.6 Cut 5 — the narrowing says nothing about **receipts**, and this document is where that silence costs. **Indicts the narrowing.**

Option 5 legislates the encoding and the export. A *receipt over* an export is
neither: it is a second party's statement about our statement. `MD-3` has no
clause for it, so the shape arrives by inertia from whatever COSE offers — and
what COSE offers is §3's table, in which the receipt binds a signature for one
target shape and nothing for the rest. **That is not an argument against option
5. It is an argument that the `DEC-002` ADR owes a receipt clause whichever
option wins**, and §9 below is the clause: *a receipt binds the signature value
of an attached-payload `COSE_Sign1`, and no other target of this document gives
a receipt anything cryptographic to bind.*

---

## 8. Mapping to our decisions

| decision | what this document contributes | verdict |
|---|---|---|
| **`ARCH-0001` §4.1 (KeyId)** | Nothing structural. The countersigner's identity hint is COSE `kid` (label 4) and it is in the **unprotected** bucket in all six examples, so it is not inside the signed bytes. §3.3's only identity instruction is lowercase and hands the work to the application: *"the application performs the appropriate checks to ensure that the key is correctly paired with the signing identity"* `rfc-9338#R-0110` | **no carrier.** A key-relative receipt identity is ours to define; `R-O-03` has nothing to cite here |
| **`ARCH-0001` §7 (`DEC-002` open)** | One registry row's worth: tag 19, the only new CBOR tag in the COSE lane | **input**, via §7.2 |
| **`ARCH-0002 P1` (key-relative naming)** | Negative evidence, sharply. The nested header space is keyed by integers in a global registry with a blank Value Registry `rfc-9338#R-0121` | **no native expression**; §7.3 |
| **`DEC-002`** | 4 code points, 1 of them a tag; 5 cuts in §7 | **input, not closed** |
| **`DEC-003`** | Nothing new. This document adds no claim, no label and no serialisation rule beyond the four code points, and its determinism rule is RFC 9052's | **no bearing** — recorded so the absence is a measurement rather than an omission |
| **`DEC-005` (envelope for `ArtifactStatement`)** | Two real inputs: A-3's algorithm-class restriction `rfc-9338#R-0074`, which narrows any algorithm list we write; and §3's table, which says the envelope choice **determines** whether a receipt can bind a signature. A `COSE_Sign1` envelope admits a binding receipt; a `COSE_Sign` envelope does not | **strong input** |
| **`R-M-12` (extension point = (key, local label))** | The nested, unbounded global label space; §7.3 | **hazard, not adopt** |
| **`R-O-01`** | The payload is authoritative and `kid` is a hint — unchanged here, and the countersignature adds a *second* hint in a *second* unprotected bucket | **consistent, unhelpful** |
| **`R-O-03` (cited, not invented silently)** | Two places where there is nothing to cite: a **detached** receipt (§7.2) and a **timestamp** (RJ-5). Both are inventions we must then cite ourselves | **binding constraint** |
| **`R-O-05` (authenticated type indicator)** | `context`, in the right slot, with a demonstrated-bad value; §7.5 | **adopt the shape, replace the value** |

### The six `canonical-encoding` conditions

| condition | does RFC 9338 bear on it? |
|---|---|
| **(1) injective encoding** | **Partly, and negatively.** `Countersign_structure` is not injective over what it *means*: for five of eight targets the version-1 and version-2 algorithms produce the **same** byte string under the **same** context string, so one encoding has two provenances. That is injectivity failing at the *protocol-version* level rather than the value level — the same shape as `rfc-8742`'s file-level finding, and no condition covers it either |
| **(2) decoder rejects non-canonical input** | **No.** The document has no decoder obligation at all. Its only `MUST` about encoding is on the **producer** of `ToBeSigned` `rfc-9338#R-0113`, and §3's one named failure is a signature-validation failure, not a rejection |
| **(3) canonicalise once, at authoring** | **Yes, and it is the one condition this document satisfies cleanly.** §3.3 step 2 canonicalises exactly once, at the moment of signing, and the result is never transmitted `rfc-9338#R-0019`. The precondition makes the ordering explicit: the target *"needs to have all of its cryptographic functions finalized before computing the signature"* `rfc-9338#R-0086` |
| **(4) authenticated type indicator inside the signed bytes** | **Yes, positively in form and negatively in content.** §7.5 |
| **(5) canonical order for set-valued fields** | **No, and there is a gap.** Label 11's value may be *"one or more countersignature values"* `rfc-9338#R-0031` — `COSE_Countersignature / [+ COSE_Countersignature]` — and **nothing fixes the order of that array, nor how a second countersigner converts the single form to the array form**. A set of witnesses is exactly a set-valued field, and this is condition (5) unaddressed on the one field where we would need it |
| **(6) declared Unicode normalisation rule** | **No.** `normaliz*` and `Unicode` occur **0 times** in the source. The four `context` strings are ASCII literals, so nothing depends on it here |

---

## 9. Does `rfc-9052`'s open-question-7 answer survive this derivation?

`records/ietf/rfc-9052/distilled/design-notes.md` §6 carries a correction dated
2026-10-20 that answers its own open question 7 — *does extending the target
from `COSE_Sign1` to `COSE_Sign` extend the binding?* — with **no**. **Read for
this pass and not edited; it is at `profile: full`.**

**Its answer survives, and the decisive limb survives unconditionally.**

1. **Its table is confirmed row for row**, re-derived here by script rather than
   by hand (`schema/bstr-slot-census.derived.txt`). The only difference is that
   this record carries `COSE_recipient` as an eighth row, which that correction
   deliberately omitted because §3.3's target list omits it. Both are right
   about their own scope.
2. **"A countersignature over a `COSE_Sign` binds no signature at all" is
   confirmed and is independent of every ambiguity in §3.** `signatures` is an
   array; the `bstr` count never reaches it; `other_fields` is omitted; reading
   P and reading S agree. V-0007 is the whole 45-byte structure. So a witness
   receipt over a *k*-of-*n* export would attest the payload and the body
   protected header and say nothing about **who signed it**, which is the whole
   content of a threshold statement. **That conclusion needs no reading of
   `payload` and is the one to carry back.**
3. **One limb of it is narrower than stated, and this is what to carry back
   second.** The correction says *"Countersigning each `COSE_Signature`
   individually is not the escape either"*, and then — correctly — records the
   `payload` ambiguity. This pass adds the three supports for reading P (§3.4),
   under which **countersigning each `COSE_Signature` individually does bind
   that signer's signature bytes**, in the `payload` slot. So that escape route
   is **not closed; it is contingent on an under-specification**, which for a
   *k*-of-*n* receipt is worse than closed in one way and better in another:
   - better, because a per-signer receipt shape **exists** and binds the right
     bytes under the better-supported reading;
   - worse, because two implementations that disagree about reading P versus
     reading S produce different `ToBeSigned` values **under the same context
     string** `"CounterSignature"`, so the disagreement surfaces as an
     unexplained verification failure with no version indicator to blame;
   - and in either case the receipt is **per-signer, not per-export**: *k*
     countersignatures, each binding one signature value, none binding the
     threshold, the payload or the body's protected header (§4). A *k*-of-*n*
     receipt is not one object in this mechanism.

   **Net: question 7's answer is unchanged — there is no defined mechanism for a
   *k*-of-*n* receipt — but the reason is now "under-specified and per-signer"
   rather than "binds nothing", and the first branch of question 7 remains the
   only one with a defined mechanism behind it.** Reported, not edited.
4. **A third thing to carry back that the correction does not have.** Under
   *both* readings, countersigning a `COSE_Signature` leaves the **enclosing
   `COSE_Sign`'s protected bucket** uncovered (§3.4, §4). For a threshold export
   whose protected bucket is where the threshold parameters would live, that is
   a second, independent reason the per-signer route does not yield a receipt
   over the *export*.

---

## 10. Source defects — recorded, not repaired

**Seven. One is new to this pass and reproducible; one is the only erratum.**

1. **Erratum 7338 — the `Countersign_structure` CDDL does not parse.**
   *Reported*, Technical, §3.3, Carsten Bormann, 2023-02-06. Errata searched
   2026-10-20 at `errata.rfc-editor.org/rfc9338` and
   `errata.rfc-editor.org/eid7338`: **this is the only erratum on RFC 9338**,
   and no Verified, Held-for-Document-Update or Rejected entry exists. The
   trailing `/` after `"CounterSignature0V2"` is a choice operator with no right
   operand, and RFC 8610 Appendix B — held verbatim in this library at
   `records/ietf/rfc-8610/distilled/schema/cddl.abnf` line 141 — gives
   `type = type1 *(S "/" S type1)`, so a trailing `/` requires a following
   `type1` and the fragment is a syntax error. **In a document whose §1.2
   advertises XPath extraction** `rfc-9338#R-0016` **and says the grammar exists for
   *"the automated validation tools used during the writing of this document"***
   `rfc-9338#R-0021`. Kept intact in `schema/rfc9338.cddl`; repaired only in
   `schema/countersign-structure.derived.cddl`.
2. **The two permitted-target lists disagree, in both directions, and neither is
   in the errata.** §2 permits label 11 in seven structures and **omits
   `COSE_Sign`** `rfc-9338#R-0033`; §3.3's process takes seven and **adds
   `COSE_Sign`, drops `COSE_recipient`** `rfc-9338#R-0084`. Union eight,
   intersection six. And **Appendix A.1.1 — the document's only signed-message
   example — countersigns a tagged `COSE_Sign`**, which §2 does not permit and
   to which §3 assigns no countersignature semantics at all. Fixture
   `examples/fixtures/V-0001-sign-countersign-on-body.diag`: label 11 is at
   index 1 of the `98(…)` array, in the **body's** unprotected map.
3. **NEW, AND REPRODUCIBLE: Appendix A.6.1's stated size is wrong by 20
   bytes.** The text says *"The size of the binary file is 159 bytes"*
   `rfc-9338#R-0140` and the message it prints encodes to **139 bytes**. The 20 is exactly
   the tag head (two octets for `97`, one for `17`) plus A.5.1's 19-octet
   `recipients` array, which a `COSE_Mac0` does not have; and A.5.1's and
   A.6.1's preambles are **byte-identical runs of source text**, so the number
   was carried over from A.5.1. Five of the six stated sizes reproduce exactly
   (180, 275, 326, 136, 159), which is also what validates the encoder — as does
   the fact that all **13** embedded `<< … >>` maps encode to precisely the hex
   the document's own diagnostic comments claim. `examples/vectors.yaml` V-0006.
   **No erratum covers it.**
4. **§3.1 describes its own example wrongly.** *"An example of a
   countersignature on a signature can be found in Appendix A.1.1."*
   `rfc-9338#R-0073` A.1.1 is a countersignature on a signed **message**
   (`COSE_Sign`), not on a `COSE_Signature`. The document has **no** example of
   a countersignature on a `COSE_Signature` — the one case §3.4's ambiguity
   turns on. Not in the errata.
5. **Label 12 has no permitted-target list anywhere.** §2 has exactly one
   labelled entry and its target list is for label 11; Table 1 gives label 12 a
   name, a value type and a Description and no targets; §3.2 names no structure.
   Where the abbreviated countersignature may appear is undefined.
6. **§3.3's `sign_protected` omission rule names one of the two abbreviated
   context strings.** *"omitted for the Countersignature0V2 attribute"*
   `rfc-9338#R-0094` leaves the `"CounterSignature0"` case unstated, and the two
   choices give different signed bytes. §4.
7. **The collected CDDL does not stand alone, and no erratum covers it.** The
   file §1.2's XPath yields references `COSE_Signature` and
   `empty_or_serialized_map`, both defined in RFC 9052 and neither here, so even
   with erratum 7338 applied it fails name resolution. `schema/README.md` has
   the census; `schema/countersign-structure.derived.cddl` supplies the imports
   and says so.

**Not a defect, recorded so a later pass does not re-litigate it:** Appendix
A.3.1's recipient unprotected map is not in RFC 8949 §4.2.1 key order. §4's
`MUST` binds the to-be-signed value, not the message, so nothing is violated.
It does mean these fixtures are countersignature vectors and **not**
deterministic-encoding vectors.

---

## 11. Open questions

1. **Does `Countersign_structure.payload` take the target's second `bstr` slot
   (reading P) or the content (reading S)?** The document does not say and both
   have textual support (§3.4). **Whoever writes a receipt profile decides**,
   and must state it, because the two produce different signed bytes **under the
   same `context` string**. The IETF COSE WG is the right venue for an erratum
   or a clarification; this is a candidate to file.
2. **Is a receipt per-export or per-signer?** §9 shows this mechanism only
   offers per-signer, and only under reading P. **Blocks** any transparency or
   witness increment over a *k*-of-*n* export.
3. **If a receipt must be detached, what do we cite?** §7.2: tag 19 is the only
   sanctioned answer, option 5 forbids it, and the tag comes with no
   association procedure anyway. `R-O-03` then makes the receipt framing an
   invention we must cite ourselves.
4. **Where does a receipt's time come from?** RJ-5: COSE has no timestamp
   `rfc-9338#R-0040`. A protected `iat`-shaped field of ours, or a CWT claim via
   `rfc-8392`, are the two candidates and neither is this document's.
5. **Do we ever accept a countersignature over a `COSE_Mac` or
   `COSE_Encrypt`?** §6 caps them at 64 and 32 bits of integrity protection
   `rfc-9338#R-0129` `rfc-9338#R-0130` against a `MUST` of at least 256 `rfc-9338#R-0128` — two
   configurations in which the document's own `MUST` cannot be met. And with
   more than two parties sharing a MAC key, *"data origin authentication is not
   provided"* `rfc-9338#R-0125` at all.
6. **Does our profile bound countersignature chain depth, and in what order are
   chains processed?** AD-4: the document bounds neither.

---

## 12. Reasoned beyond the source — every inference in this file

Each is marked in place; collected here so the list is auditable.

- **The `bstr`-slot table (§3.3).** `[derived]` from RFC 9052's verbatim CDDL by
  script, not from any statement in RFC 9338, which gives the answer only for
  `COSE_Sign1`. Mechanism: `schema/bstr-slot-census.derived.txt`.
- **Reading P versus reading S, and the three supports for P (§3.4).**
  `[inference]`. Support 2 rests on RFC 8152 §4.5, read on 2026-10-20 and **not
  copied into this library**; the library holds `rfc-8152` as a summary-only
  record, so that half of the support is **not checkable from this
  repository** and is marked as such here rather than asserted silently.
- **The Alice/Bob collision under reading S (§3.4).** `[constructed]` —
  `examples/vectors.yaml` `collisions`, built both ways, not argued.
- **A.6.1's 139 bytes and the 20-byte explanation (§10.3).** `[constructed]`
  from the document's own diagnostic notation; five of six sizes reproduce and
  13 of 13 embedded maps match the document's own hex comments.
- **A.3.1's non-deterministic map order (§7.4, §10).** `[measured]` against RFC
  8949 §4.2.1.
- **Every occurrence count** (`detach` 0, `nil` 0, `normaliz*` 0, `Unicode` 0,
  `verifier` 0, `state` 0, and the rest) `[measured]` whole-word and
  case-insensitively over all 921 lines; the full sets are in `protocol.yaml`
  and `state-machine.yaml`.
- **The erratum census.** `[measured]` — `errata.rfc-editor.org/rfc9338` and
  `/eid7338`, fetched 2026-10-20: one erratum, status *Reported*. Stated as
  what the search returned, not as an absence.
- **Every adopt / adapt / reject verdict, and every MD-3 cut.** `[analysis]`.
  The document takes no view on our decisions; the `DEC-002` option named in
  each cut is ours.
- **Every characterisation of `ARCH-*`, `DEC-*`, `MD-3`, `R-M-*`, `R-O-*` and
  `PLAN-*`.** `[unverifiable-here]` — not held in this library.
