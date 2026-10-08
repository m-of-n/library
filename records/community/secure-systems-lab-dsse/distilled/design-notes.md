---
record: secure-systems-lab-dsse
kind: design-notes
title: "secure-systems-lab-dsse — bearing on our design"
extracted: "2026-10-08"
reviewed_by: ""
---

# DSSE — bearing on our design

DSSE is named in **DEC-005** (envelope for `ArtifactStatement`), in **R-I-03**
(export target), and in **DEC-002 option 3**, which pairs it with RFC 8785 JCS.
Its critique of canonicalisation is the argument **R-O-05** has to survive.

**Nothing here decides anything.** DEC-002 and DEC-005 are open, and a DEC is
accepted only in an `ADR-NNNN` (ARCH-0001 §9.2).

Two of the five findings below are **corrections to this record's own earlier
summary**, written when `envelope.md` and the attack notebook were unread. Both
corrections weaken claims that were in our favour, which is why they matter.

---

## 1. CORRECTION — the `(t, n)` envelope carries `n`, not `t`

**Withdrawn.** The earlier summary said:

> **`(t, n)` multi-signature is already in the envelope.** […] The export target
> named in R-I-03 therefore already carries threshold semantics, which bears
> directly on R-M-06 and is a cheaper interchange story for threshold subjects
> than expected.

That is wrong, and the clause that refutes it is in the same sentence the
summary quoted. P11 reads in full:

> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification
> against at least `t` of `n` unique trusted public keys **where `t` is
> application-specific**.

`t` is a *verifier-side parameter supplied out of band*. It is not a field. The
envelope schema (E1) has `payload`, `payloadType` and `signatures` — and nothing
else. `envelope.md` then says so directly (E3):

> An envelope MAY have more than one signature, **which is equivalent to separate
> envelopes with individual signatures**.

A DSSE envelope is a bag of independent signatures over the same bytes. It
carries `n`. It cannot carry `k`.

**Why this matters more here than it would elsewhere.** For m-of-n the threshold
is not envelope metadata, it is *the semantic content* — a `Threshold` subject
under ARCH-0001 §4.1 is `k` of a named member set, and R-M-06 exists because
that subject has to survive interchange. So the interchange story for threshold
subjects is **not** cheaper than expected; it is exactly as expensive as it
looked before this record was read. Exporting an `AuthzCert` with a threshold
subject to DSSE requires `k` and the member set to travel **inside
`SERIALIZED_BODY`**, where they are authenticated by PAE, and a DSSE verifier
that does not know our payload type will check `n` signatures and have no idea
what `k` was supposed to be.

A second-order consequence: because E3 declares a multi-signature envelope
*equivalent* to separate single-signature envelopes, a DSSE-native intermediary
may legitimately split or merge them. Any threshold meaning a reader infers from
how many signatures happen to be in the envelope is therefore not merely absent
but actively unsafe to infer.

## 2. CORRECTION — DSSE licenses a non-global `payloadType`, so the R-M-12 objection is weaker than recorded

The earlier summary, and the `canonical-encoding` topic answer, both say option
3's envelope reintroduces a global type identifier excluded by R-M-12:

> **`PAYLOAD_TYPE` is a globally allocated string** — a media type or a URI.

True of the recommendation, but the recommendation is a **SHOULD**, not a MUST
(P3: *"To prevent collisions, the value SHOULD be either"*), and `envelope.md`
§Other data structures explicitly licenses the escape (E7):

> Use a default `payloadType` if omitted and/or code `payloadType` as a
> shorter string or enum.

A short string or an enum is not an IANA media type and not a URI. Since PAE
length-prefixes the type bytes whatever they are, a locally-scoped type
indicator is still fully authenticated. **So DSSE does not force a centrally
allocated identifier; its default recommends one.**

This is a real weakening of the fourth ground recorded against option 3. It is
not a reversal, for two reasons worth stating precisely. The escape is in
`envelope.md`, which is labelled *"the recommended data structure"*, and taking
it means diverging from what every deployed DSSE consumer expects — so the cost
reappears as ecosystem cost rather than as a specification conflict. And E7's
same list licenses *"an encoding other than JSON, such as CBOR or protobuf"*,
which, if taken, deletes the JSON half of option 3 altogether.

## 3. `MUST ignore unrecognized fields` collides with ARCH-0002 P5

E6:

> Producers, or future versions of the spec, MAY add additional fields.
> Consumers MUST ignore unrecognized fields.

ARCH-0002 **P5** requires that validity be checked and **unknown be rejected**,
binding both encoder and verifier. These are opposite defaults, and the
collision is at the **envelope** layer, where DSSE's MUST is normative for
anything calling itself a DSSE consumer.

**Scope this precisely, because the obvious overstatement is wrong.** DSSE is
ignore-unknown for *fields* only. For *types* it is reject-unknown, and P8 says
so: *"Reject if PAYLOAD_TYPE is not a supported type."* So the conflict is
narrow — unknown sibling fields of `payload` / `payloadType` / `signatures` —
and it does not touch the payload interior, which is ours to govern under our
own payload type.

Consequence for **R-I-03**: a conforming DSSE export boundary cannot enforce P5
on the envelope. Either the export profile documents a deliberate deviation from
E6, or P5 is understood to govern the payload interior only and the envelope
exterior is explicitly out of its scope. That is a question for the ARCH-0002
amendment that the `canonical-encoding` topic already routes to P5 — it is **not**
a library decision and no document of ours currently states which reading holds.

## 4. `KEYID` MUST NOT be used for security decisions — a trap for DEC-003

P4:

> KEYID: Optional, unauthenticated hint […] It **MUST NOT** be used for security
> decisions; it may only be used to narrow the selection of possible keys to try.

Our `KeyId` is the **opposite**: under R-M-02 it *is* the principal's name, and
DEC-003 is specifically about putting issuer and subject identifiers on the wire
— with options including a COSE key thumbprint and a hash-uri.

The two terms collide exactly, and the failure mode is quiet: a mapping table
written under R-I-01 that lines up our `KeyId` against DSSE's `keyid` because
they share a name would place the principal's *name* in the one envelope field
DSSE declares unauthenticated and forbids relying on. An implementer following
both documents would be conformant to each and wrong.

**The rule this yields for any DSSE export profile:** the principal travels in
`SERIALIZED_BODY`, never in `signatures[].keyid`. `keyid` may carry the same
value as a hint, and nothing may depend on it. This belongs in whatever states
R-I-03's export mapping, and it is the same shape as finding 1 — DSSE's envelope
authenticates only `payloadType` and `payload`, so everything we need
authenticated has to be in the payload.

## 5. Injectivity by framing rather than by canonicalisation — and the evidence for condition (4)

The `canonical-encoding` topic answer lists six conditions for a canonical form
to be safe. DSSE is the proof that **condition (1), injectivity, has a second
route that is not canonicalisation at all**. PAE (P5) length-prefixes both
fields with ASCII decimal lengths and no leading zeros:

```none
PAE(type, body) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body
```

Length-prefixed framing is injective over the `(type, body)` pair by
construction, with no escaping, no ordering rule and no normalisation. It buys
injectivity *of the signed tuple* without buying it for the payload interior —
which is precisely DSSE's position: frame unambiguously, then decline to make
any claim about the bytes inside.

Two things follow for us.

**Condition (4) now has a worked attack behind it, not just an argument.** The
notebook (N1-N3) is Lodato's September 2020 proof-of-concept: a payload crafted
to parse as one message under CBOR and a *different* message under protobuf,
with `payloadType` flipped after signing because it was outside the signature.
This is the direct ancestor of R-O-05's *"authenticated type indicator"* clause,
and this record is the citation for it.

**It also sharpens condition (1) in a way the topic answer does not yet say.**
The attack's payload is a **polyglot**: injective *within* CBOR and injective
*within* protobuf, yet ambiguous across the pair. A canonical form that is
injective over its own value space therefore does not by itself prevent
type confusion — condition (1) has to hold over the `(profile, bytes)` pair, not
over bytes under one profile. This is an argument for the authenticated type
indicator being load-bearing rather than belt-and-braces, and it is a specific
hazard for **DEC-002 option 4** (dual canonical CBOR and JSON with a documented
bijection), where two profiles are live simultaneously and a bijection is
asserted between them.

---

## Minor — a defect in DSSE's own text

E4 lists the required fields as `payload`, `payloadType`, **`signature`**,
`signature.sig` — singular — while the schema in E1 and the `(t, n)` procedure
in P12 use **`signatures`**, an array. The singular form appears nowhere else in
either document. It is a drafting slip rather than an ambiguity, but a mapping
table written under R-I-01 should use E1's `signatures[]`, and anyone reading
only §Parsing rules would get the shape wrong.
