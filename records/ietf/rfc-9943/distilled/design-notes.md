---
record: rfc-9943
kind: design-notes
title: "rfc-9943 — bearing on our design"
extracted: "2026-09-30"
reviewed_by: ""
---

RFC 9943 is the ratified, fully worked version of the shape this project is
designing: a signed statement whose asserter is modelled in the protected
header and whose assertion is an opaque payload, made transparent by
registration into an append-only structure that returns an offline-verifiable
receipt. Everything below is derived from the source text
(`content.sha256: 204aea02…`), never from our summary. Locators are the RFC's
own section and figure numbers.

Three of the four decision ids this record is mapped to — `DEC-002`,
`DEC-007`, `R-M-12` — are **not defined inside this repository**. Every
statement below about what one of them means is a **reconstruction**, not an
in-repo definition. Each point of reliance is marked **[gloss]**, and the
reconstructions are listed in *Mapping to our decisions → Where we relied on a
reconstructed gloss*.

---

## What we adopt

**A1 — Transparency is additive, not destructive.** The receipt goes in the
*unprotected* header, so the transparent statement is byte-identical to the
signed statement in everything the issuer signed:

> "A Transparent Statement remains a valid Signed Statement and may be
> registered again in a different TS." — §3, *Transparent Statement*

This is the single most reusable idea in the document. Transparency becomes a
layer a statement can acquire, lose, or acquire twice, without the statement
changing identity. Our statement form must have the same property: a witness
attachment point outside the signature that can be stripped to recover the
original bytes exactly.

**A2 — The signed form and the logged form are the same bytes, and the rule
that makes that true is explicit.**

> "However, the unprotected header of a Signed Statement MUST be set to an
> empty map before the Signed Statement can be included in a Statement
> Sequence." — §6.3

Without this the envelope is malleable: two log entries with different
unprotected headers carry the same signature, and the log cannot say which one
it committed to. The rule is non-obvious and easy to omit. Our reduced-CBOR
profile needs the exact equivalent — a stated rule that the attachment region
is emptied before hashing for the log.

**A3 — Mandatory asserter, mandatory subject.**

> "The CWT Claims value MUST include the Issuer Claim (Claim label 1) and the
> Subject Claim (Claim label 2) [IANA.cwt]." — §6

Two mandatory fields, both in the *protected* header, both therefore covered
by the signature. `iss` answers *who asserts*; `sub` answers *over what*, and
because it is a stable grouping key it is what makes "every statement about
this artifact" a query rather than a search. §6.3 reinforces it:

> "An Issuer that knows of a changed state of quality for an Artifact SHOULD
> Register a new Signed Statement using the same 15 CWT iss and sub Claims."

Amendment is a new statement under the same `(iss, sub)` pair, not a mutation.
We adopt both the pair and the append-only amendment idiom. **[gloss —
DEC-007]**

**A4 — The assertion stays opaque to the service.**

> "The Statement is considered opaque to TS and MAY be encrypted." — §3,
> *Statement*

The transparency layer never parses the claim. It checks who signed, applies
an admission rule over metadata, and commits. That division of labour is what
lets one service carry heterogeneous statement types, and what keeps the
service from becoming an authority on content. We adopt the opacity. We do not
adopt its *optional typing* — see B2.

**A5 — Detached and hashed payloads are first-class.**

> "Statement payloads might be too large or too sensitive to be sent to a
> remote TS. In these cases, a Statement can be made over the hash of a
> payload rather than the full payload bytes." — §6.2

Figure 4 shows the detached case on the wire: `payload` is `nil`. The CDDL
types it `bstr / nil`. This lets a statement be made about bytes that are never
transmitted — the same manoeuvre this library already performs on third-party
documents (record the digest, never the bytes). Adopt.

**A6 — Many witnesses, no single trusted log.** §6.3 and §7 allow one signed
statement to be registered at several services, each returning its own
receipt, the receipts aggregated in one array at label 394. §9.7 states the
intent: "The SCITT architecture does not require trust in a single centralized
TS." A relying party that trusts service B and not service A verifies the
B-receipt and ignores the A-receipt. Adopt the cardinality: our witness
attachment point is a *list* from the start, not a single slot retrofitted
later.

**A7 — The admission rule is itself in the log.**

> "Registration Policies and trust anchors MUST be made Transparent and
> available to all Relying Parties of the TS by Registering them as Signed
> Statements on the VDS." — §5.1.1.1
>
> "The TS MUST apply the Registration Policy that was most recently committed
> to the VDS at the time of Registration." — §5.1.1.1

This turns "the service checked something" into a replayable claim: the rule
in force at time *t* is recoverable from the log itself, so an auditor can
re-run a past admission decision. It also gives a general pattern —
*control-plane changes are content-plane entries* — worth reusing for anything
an operator can change. Adopt the mechanism. Its encoding is unusable as
specified; see C3.

**A8 — Receipts verify offline.**

> "It is universally verifiable without online access to the TS." — §4

A relying party holding the statement, the receipt and the service's public
key needs no network. This is what makes a receipt worth carrying, and it
constrains the format: everything needed to check the proof must be inside it.
Adopt as a hard constraint on our own witness format.

**A9 — The honest statement of what registration proves.**

> "Issuers can make false Statements either intentionally or unintentionally;
> registering a Statement only proves it was produced by an Issuer." — §9.2

We adopt this as a design constraint, not merely as documentation: nothing in
our format may be shaped so that a receipt reads as an accuracy claim. The
witness record names what it witnesses — inclusion at a position, at a time,
under a rule — and carries no field that could be read as an endorsement of
the payload.

---

## What we adapt, and how

**B1 — `alg` becomes mandatory.** In the normative CDDL of Figure 3 the
algorithm identifier is optional:

```
? &(alg: 1) => int
```

Combined with "Key discovery protocols are out of scope of this document."
(§6) and §4's "A Receipt's verification key, signing algorithm, validity
period, header parameters or other claims MAY change each time a Receipt is
produced.", a conformant signed statement can arrive with no algorithm
identifier, no key, and no way to find either. **Adaptation:** in our form the
algorithm identifier is mandatory and inside the signed region. On export we
emit label 1 unconditionally even though the RFC permits its absence — a
superset of conformant is still conformant.

**B2 — The payload type becomes mandatory.** §3 says statements "must be
tagged with a relevant media type (as specified in [RFC6838])", and §6 says
"An Issuer must first decide on a suitable format (3: payload type) to
serialize the Statement payload" — but Figure 3 makes label 3 optional. An
opaque payload with no declared type is not an assertion, it is a blob; a
relying party cannot even decide whether it has a parser. **Adaptation:** our
body type is mandatory and signed. This is the one place where we make the
*assertion side* stricter than SCITT does, and it is deliberate: opacity to
the *service* must not mean opacity to the *relying party*.

**B3 — The asserter identifier is URI-shaped unconditionally.** §6 constrains
`iss` in one branch only:

> "When x5t or x5chain is present in the protected header, the iss Claim value
> MUST be a string that meets URI requirements defined in [RFC8392]. The iss
> Claim value's length MUST be between 1 and 8192 characters in length."

When the issuer is identified by `kid` instead, `iss` is an unconstrained
`tstr` (Figure 3: `&(iss: 1) => tstr`) — so the mandatory identity field has a
shape that depends on which optional key-binding mechanism was chosen.
**Adaptation:** one shape, always. We keep the length bound as a parser safety
rail and drop the conditionality.

**B4 — Issuer time is carried in the statement.** The only time in the system
is the service's:

> "The Registration time is recorded as the timestamp when the TS added the
> Signed Statement to its VDS." — §7

and it is explicitly not issuance order:

> "Unless advertised in the TS Registration Policy, the Relying Party cannot
> assume that the ordering of Signed Statements in the VDS matches the
> ordering of their issuance." — §9.1

So the log orders *registration*, and an issuer's own chronology is
unrecoverable from it. For a sequence of amended statements under one
`(iss, sub)` pair — precisely the idiom §6.3 recommends — that is a real
defect: "which of these two did the issuer write later" has no answer.
**Adaptation:** an issuer-asserted time inside the signed region. It is not
trustworthy on its own; it is evidence the issuer is bound to, which is more
than the log gives.

**B5 — Bootstrapping narrows from three options to one.** §5.1.2:

> "TSs MUST support at least one of the three following bootstrapping
> mechanisms:
> * Preconfigured Registration Policy and trust anchors;
> * Acceptance of a first Signed Statement whose payload is a valid
>   Registration Policy, without performing Registration checks; or
> * An out-of-band authenticated management interface."

"At least one of three" is not interoperability — two conformant services can
share no bootstrapping path. §9.4.3 then ranks them itself:

> "Bootstrapping mechanisms that solely rely on Statement registration to set
> and update registration policy can be audited without additional
> implementation-specific knowledge; therefore, they are preferable.
> Mechanisms that rely on preconfigured values and do not allow updates are
> unsuitable for use in long-lived service deployments in which the ability to
> patch a potentially faulty policy is essential."

**Adaptation:** we take the second option as the *only* one — genesis is a
self-describing first entry — because it is the only one that keeps the
control plane inside the audit surface (A7). The third, an out-of-band
management interface, is exactly the hole A7 was designed to close and is
unauditable by construction. The first is ruled out by §9.4.3's own words.

**B6 — Rollback becomes an entry, not a silence.** See C2 for the defect. The
adaptation: if our design must tolerate an epoch break at all, then (a) the
break is declared as a signed, registered entry under the same
control-plane-as-content-plane pattern as A7, naming the abandoned position
and the superseded key; (b) witness validity is scoped to a
`(service key, epoch)` pair, so a relying party holding a witness over a
discarded prefix can *tell*; and (c) the prior log is retained and remains
fetchable, so the fork point is checkable rather than asserted. None of the
three is in RFC 9943.

**B7 — Our extension socket must not live in the attachment region.** Figure 3
puts `* label => any` on the unprotected header, which invites us to park
key-relative extensions there. Figure 7 removes it (C7). **Adaptation:** every
key-relative extension we carry lives in the *protected* map, inside the
signature, and the attachment region holds witnesses and nothing else. This is
the right rule independently — an extension outside the signature is not
evidence of anything — but Figure 7 is what forces it.

**B8 — COSE becomes an export target, not the canonical form.** The whole of
the D-3 mapping below. Our canonical form is a reduced CBOR profile; the SCITT
envelope is what we emit when a statement leaves for a Transparency Service,
and the mapping is a total, deterministic function in one direction.
**[gloss — D-3, DEC-002]**

---

## What we reject, and why

**C1 — The envelope as our canonical form.** Rejected under D-3. RFC 9943's
on-the-wire object is a tagged CBOR item (`Signed_Statement = #6.18(COSE_Sign1)`,
Figure 3) whose every structural position is a registry allocation: CBOR tag
18; COSE header labels 1, 3, 4, 33, 34; the CWT-Claims container at label 15;
CWT claim labels 1 and 2; receipt and proof labels 394, 395 and 396 from
RFC 9942; label 3's value drawn from the media-type registry or the CoAP
Content-Format registry; and §10's two further media types and two further
Content-Format numbers. Five registries to decode one statement. That is the
dependency D-3 declines to take on. **[gloss — D-3]** Details in the mapping.

**C2 — §9.4.2's rollback permission, as written.** This is the sharpest thing
in the document and we reject it outright. §5.1.3 makes append-only a MUST on
the data structure:

> "Append-only: a property required for a VDS to be applicable to SCITT,
> ensuring that the Statement Sequence cannot be modified, deleted, or
> reordered." — §5.1.3

§9.4.2 then permits the service to do exactly that:

> "TSs whose receipt signing keys have been compromised can roll back their
> Statement Sequence to a point before compromise, establish new credentials,
> and use the new credentials to issue fresh Receipts going forward." — §9.4.2

Read against each other, the architecture's headline property is *append-only
unless the operator declares a compromise*, where the declaration is
unverifiable, the exception is uncapped, and nothing is said about how anyone
learns it happened. §9.4.2 closes with "Revocation strategies for compromised
keys are out of scope for this document.", so there is no status channel
either. For a relying party holding a receipt over the discarded prefix, in
full:

1. The receipt still verifies cryptographically, against a key now known to be
   compromised, and nothing in the receipt says which.
2. There is no defined query — no status, no revocation list, no notification
   channel — by which the holder can discover that the entry it proves
   inclusion of is no longer in the sequence.
3. Consistency proofs do not help. The new sequence is signed under new
   credentials and does not chain to the old one, so the check that would
   detect an *unsanctioned* fork cannot distinguish this *sanctioned* one from
   it; it simply fails, or is never attempted because the new service identity
   looks like a different service.
4. Auditors are the architecture's fork-detection mechanism (§4: "any
   inconsistency can easily be pinpointed by any Auditor with read access to
   the TS"), and this inconsistency is one the specification has pre-approved.

The honest statement for anyone relying on the property: **append-only is a
property of the data structure, not of the service.** RFC 9943 buys
detectability of a dishonest *issuer*; it does not buy detectability of a
compromised *log*. Our design faces the same question — key compromise at a
witness is not hypothetical — and cannot answer it this way. B6 is the answer
we take instead.

**C3 — The absence of any Registration Policy syntax, as a conformance
model.** §5.1.1:

> "This specification leaves implementation, encoding, and documentation of
> Registration Policies and trust anchors to the operator of the TS."

Set that beside §5.1.1.1's MUST that policies be registered as signed
statements on the log, and §5.1.1.2:

> "TSs MUST ensure that for any Signed Statement they register, enough
> information is made available to Auditors to reproduce the Registration
> checks that were defined by the Registration Policies at the time of
> Registration." — §5.1.1.2

The policy is mandatorily *transparent* and not, in any portable sense,
*interpretable*. An auditor can retrieve the policy bytes from the log and
cannot mechanically evaluate them without operator-specific knowledge — the
very thing §9.4.3 praises the preferred bootstrapping mode for avoiding. Two
conformant services share no policy language, so "reproduce the Registration
checks" is satisfiable only per-operator. We reject this as a conformance
model. If we define an admission rule at all, it gets a declared content type
and a rule expression the checker can evaluate without out-of-band knowledge —
otherwise A7 buys transparency of an opaque blob, which is theatre.

**C4 — §9.6 as an agility story.** §9.6 is reproduced here in its entirety:

> "Because the SCITT architecture leverages [STD96] for Statements and
> Receipts, it benefits from the format's cryptographic agility."

There is no algorithm profile, no mandatory-to-implement set, no minimum
strength, no deprecation path, and — per B1 — not even a requirement that the
algorithm be named. Agility delegated wholly to the container is not agility;
it is the absence of a decision, and it means two conformant implementations
can fail to interoperate on algorithms alone with neither at fault. We reject
it as sufficient. Our profile names a mandatory-to-implement set. This is also
the hinge for post-quantum migration, which the document does not mention.

**C5 — The IANA surface of §10.** §10 registers
`application/scitt-statement+cose` and `application/scitt-receipt+cose`, and
§10.3 burns CoAP Content-Format numbers 277 and 278. We carry none of it
natively. Note what this surface is *for*: all three top-level objects —
`Signed_Statement` and `Receipt` (Figure 3) and `Transparent_Statement`
(Figure 7) — are `#6.18(COSE_Sign1)`, so the CBOR tag does not discriminate
between them. Discrimination is done entirely by the media type and by which
labels are present. That is worth knowing on its own terms: **the registered
tag buys no type information here**, so declining it costs us nothing at the
tag layer. What it does cost is that our native form must carry its own
discriminator as an ordinary field, since we will not have a media type doing
that work inside the format.

**C6 — No error model and no registration states.** §6.3 gives five ordered
steps with MUSTs on each and defines no failure outcome for any of them: no
rejected state, no reason codes, no duplicate-submission semantics at the same
service (the document addresses only registration at *different* services), no
retry rule, and no way to poll for a receipt whose production "MAY be
asynchronous from Registration" (§6.3, step 5). The state machine has a happy
path and no other path. This is deliberate — the wire protocol is delegated to
SCRAPI (`draft-ietf-scitt-scrapi`, held) — so the right verdict is *incomplete
for our purposes* rather than *wrong*: RFC 9943 is an architecture, and an
architecture with no error model cannot be implemented from alone. If we build
a registration interface, we define its states and its errors ourselves.

**C7 — Figure 7's `Unprotected_Header`: a duplicate rule name, and a closed
map.** Two defects, and the second is the one that bites. Figure 3 (§6.1)
defines:

```
Unprotected_Header = {
  ? &(x5chain: 33) => COSE_X509
  ? &(receipts: 394)  => [+ bstr .cbor Receipt]
  * label => any
}
```

Figure 7 (§7), introduced as "a normative CDDL definition of Transparent
Statements", defines a rule of the same name as:

```
Unprotected_Header = {
  &(receipts: 394)  => [+ bstr .cbor Receipt]
}
```

**First defect — the name collision.** Two definitions of one rule name cannot
coexist in a single CDDL model, so the two figures cannot be concatenated into
one schema. Verified against the source; confirmed independently by the schema
and messages passes of this extraction.

**Second defect — the map is closed, and that is not a cosmetic difference.**
Figure 7 does not merely promote 394 from optional to mandatory. It drops
`? &(x5chain: 33) => COSE_X509` **and** it drops `* label => any`. Three
consequences follow, in increasing order of seriousness:

1. It contradicts §6, which permits exactly that unprotected `x5chain`:
   "Additionally, an x5chain that corresponds to either x5t or kid identifying
   the leaf certificate in the included certification path MAY be included in
   the unprotected header of the COSE Envelope."
2. It contradicts §6.3's permission for a service to read the unprotected
   header at all — "A TS MAY accept a Signed Statement with content in its
   unprotected header and MAY use values from that unprotected header during
   verification and registration policy evaluation." — since under Figure 7
   there is no conformant place for that content once the statement is
   transparent.
3. **It closes the socket.** The `* label => any` escape hatch that R-M-12
   depends on is present on the unprotected header of a *Signed* Statement and
   absent from the unprotected header of a *Transparent* Statement. So a
   key-relative extension parked in the attachment region has nowhere to live
   the moment a receipt is attached: attaching transparency would make the
   statement non-conformant, or force the extension to be dropped. This is a
   direct hit on the D-3 mapping, and B7 is our response — our extensions go
   in the protected map, never in the attachment region.

We reject the presentation and do not copy it. We take the charitable reading
of intent — Figure 7 states the *additional* constraint that makes a signed
statement a transparent one — but the charitable reading is not what the
normative CDDL says, and an implementer validating against Figure 7 as written
will reject documents §6 and §6.3 explicitly permit. Recorded as a source
defect and a candidate erratum (O7).

---

## Mapping to our decisions

<!-- ARCH-0001 / ARCH-0002 principles, DEC-*, meeting decisions D-n.
     COSE/CBOR/envelope documents MUST address D-3 (option 5: reduced CBOR,
     no IANA tags, COSE export only) and give the header/field mapping. -->

### D-3 — header by header

D-3 is glossed in `docs/extraction.md` line 36 as **"option 5: reduced CBOR,
no IANA tags, COSE as export only"**, and `docs/extraction.md` lines 35–38
require this record to give the header-by-header mapping. That is what
follows.

Our statement fields are named below **by role**, not by identifier, because
the field names live in ARCH-0001 / DEC-007 outside this repository. Read
*asserter*, *subject*, *body*, *body-type*, *algorithm*, *key-reference*,
*signature*, *witnesses* as roles, to be bound to our actual field names when
those ids resolve. This is a reconstruction, not an in-repo definition.
**[gloss — DEC-007]**

| label | name | where | RFC 9943's rule | our field (role) | carry natively? | on export |
|---|---|---|---|---|---|---|
| — | CBOR tag **18** (`#6.18`) | outermost | Mandatory on all three objects (Fig. 3, Fig. 7) | none | **no** — registry allocation, and it discriminates nothing (C5) | emitted; our own type discriminator is dropped, its information having moved into the media type |
| **1** | `alg` | protected | `? &(alg: 1) => int` — optional | *algorithm* | **yes**, and **mandatory** (B1) | emitted always; our identifier maps to a COSE algorithm value by an explicit table |
| **3** | content type | protected | `? &(content_type: 3) => tstr / uint` — optional | *body-type* | **yes**, and **mandatory** (B2) | emitted always, as `tstr` (media type). The `uint` branch is the CoAP Content-Format registry and we never emit it |
| **4** | `kid` | protected | `? &(kid: 4) => bstr`; MUST be present when neither `x5t` nor `x5chain` is (§6); OPTIONAL to implement (§6) | *key-reference* | **yes** — an opaque, key-relative reference resolved by our own rule, not by a registry | emitted when we export without a certificate; satisfies §6's fallback branch |
| **15** | CWT Claims container | protected | **Mandatory**: "The protected header of a Signed Statement and a Receipt MUST include the CWT Claims header parameter as specified in Section 2 of [RFC9597]." (§6) | none — we have no nesting layer | **no**. Pure indirection: a registry-defined box whose semantics live in a document we have not extracted (RFC 9597) | **synthesised on export**, built from *asserter* and *subject* |
| 15 → **1** | `iss` | inside 15 | Mandatory (§6); URI-shaped only when `x5t`/`x5chain` present; 1–8192 chars | *asserter* | **yes**, mandatory, URI-shaped unconditionally (B3) | *asserter* → `15:{1:…}` verbatim |
| 15 → **2** | `sub` | inside 15 | Mandatory (§6) | *subject* | **yes**, mandatory | *subject* → `15:{2:…}` verbatim |
| **33** | `x5chain` | protected **and** unprotected (Fig. 3); **absent from Fig. 7** | `? &(x5chain: 33) => COSE_X509`. Protected: "support for either x5t or x5chain in the protected header is REQUIRED to implement" when using X.509 (§6). Unprotected: MAY (§6), but see C7 | none | **no.** X.509 path building is a trust model we are not adopting into the canonical form | emitted **only** if the export target's registration policy requires a certificate path; otherwise absent, and we rely on the `kid` branch. Never in the unprotected map, since Figure 7 forbids it there |
| **34** | `x5t` | protected | `? &(x5t: 34) => COSE_CertHash` | none | **no**, same reason | same as 33 |
| **394** | `receipts` | unprotected | `[+ bstr .cbor Receipt]`; optional in Fig. 3, **mandatory and sole member** in Fig. 7; semantics in RFC 9942 (§7) | *witnesses* (a list — A6) | **yes as a list, no as label 394.** Our attachment point is key-relative and outside the signature (A1, A2) | our *witnesses* list maps to the 394 array. Receipts a service hands back are stored **as received bytes** — we do not re-encode a signed object we cannot reproduce |
| 395 | VDS algorithm | protected (of a *Receipt*) | Not in 9943's CDDL; appears in Fig. 10. Defined by RFC 9942 | none | **no** — receipt-internal | passthrough inside the opaque receipt bytes |
| 396 | proofs | unprotected (of a *Receipt*) | Not in 9943's CDDL; appears in Fig. 9. Defined by RFC 9942 | none | **no** | passthrough inside the opaque receipt bytes |
| — | `payload` | body | `bstr / nil` — `nil` for detached (Fig. 4) | *body*, with a detached/hashed variant (A5) | **yes** | direct; detached exports as `nil` |
| — | `signature` | body | `bstr` | *signature* | **yes** | direct |
| — | `* label => any` | **protected and CWT_Claims always; unprotected only in Fig. 3, NOT in Fig. 7** | `label = int / tstr` | our extension points | **the escape hatch we use — but only in the protected map** (B7, C7) | our key-relative extensions ride in the **protected** map as `tstr` labels. The attachment region is witnesses only |

Two cautions on that table. Labels 395 and 396 appear in Figures 9 and 10 but
in neither normative CDDL; they reach the wire only through `* label => any`
and RFC 9942, so anything said about them here is inherited from a document we
have not extracted. And the last row is the one the Figure 7 correction
changed: **the extension socket in the attachment region does not survive
transparency.** A design that parked key-relative fields in the unprotected map
would silently lose them, or become non-conformant, the moment a receipt
arrived.

**What the export mapping is.** Our statement leaves for a SCITT Transparency
Service as a single deterministic function `export(statement) → COSE_Sign1`:

1. Wrap as tag 18, four-element array, per Figure 3.
2. Build the protected map: label 1 from *algorithm* (always present, unlike
   the source's optional rule); label 3 from *body-type* (always present);
   label 4 from *key-reference*, or labels 33/34 instead if the target
   service's policy demands a certificate path; label 15 as a freshly built
   map containing `1: asserter` and `2: subject`; then our key-relative
   extensions as `tstr` labels — **here, and nowhere else** (B7).
3. Unprotected map: **empty**, per §6.3's normalisation requirement (A2).
   This is the form that is signed and the form that is logged.
4. Payload: *body*, or `nil` when detached.
5. Signature over the COSE `Sig_structure`, since §6.3 step 2 and §7.1 both
   require verification "per Section 4.4 of RFC 9052 [STD96]". **This means
   the signature is computed over the exported encoding, not over our
   canonical encoding** — see O4, the highest-value open question in this file.
6. On registration the service returns a receipt; we attach it to *witnesses*
   as opaque bytes and, to emit a transparent statement, place it at label 394
   as the **sole** member of the unprotected map (Figure 7).

**What we deliberately do not carry.** The CBOR tag 18 wrapper; the CWT-Claims
container at label 15 as a structure (only its two contents, flattened); both
X.509 header parameters (33, 34) and the certificate-path trust model behind
them; the receipt and proof labels 394, 395, 396 as labels; the `uint` branch
of the content type, which is the CoAP Content-Format registry; §10's two
media types and two Content-Format numbers; and any integer extension label.
Each is registry-dependent, and each is reconstructible at export time from
fields we do hold — which is the test D-3 sets, and the reason "COSE as export
only" is affordable rather than merely principled.

### DEC-002 — canonical encoding

DEC-002's option 2 is "CBOR + CDDL as canonical; COSE for signed form", with a
recorded direction to start from a reduced CBOR profile. That phrasing is a
**reconstruction**; DEC-002 has no in-repo definition. **[gloss — DEC-002]**
RFC 9943 is confirming evidence for the *method* and a warning about the
*scope*:

- **Confirming.** It does exactly what option 2 describes — CBOR for structure,
  CDDL for the normative definition (Figures 3 and 7, each introduced as "a
  normative CDDL definition"), COSE for the signed form. A ratified Standards
  Track document built this way is the best available argument that the
  combination works.
- **Warning.** RFC 9943's CDDL is not a conformance test. Figure 3's three
  maps all end in `* label => any` with `label = int / tstr`, and its only
  mandatory element is label 15. A document that validates against Figure 3
  may contain no algorithm, no content type, no key reference, and arbitrary
  unknown content. Figure 7 then swings to the opposite extreme — a closed map
  of exactly one member that contradicts §6 and §6.3 (C7). Neither figure is
  the thing we want. Our reduced profile must be tight enough that validation
  is evidence, and consistent enough that one model covers the whole document.
- **Reduction is the right instinct, and RFC 9943 shows why.** Of the seven
  header positions it defines, exactly one is mandatory, and the mandatory one
  is a container from another RFC. The document's actual information content —
  who, over what, of what type, signed how, with what key — is five fields.
  The rest is registry plumbing. Our reduced profile carries the five.

### DEC-007 — the statement/assertion shape

DEC-007 is the statement/assertion shape: who asserts, over what. That gloss
is a **reconstruction**, not an in-repo definition. **[gloss — DEC-007]**
RFC 9943's answer, stated precisely:

- **The asserter is modelled, twice over, and inside the signature.** An
  identity (`iss`, mandatory), a subject (`sub`, mandatory), a key binding
  (`kid`, or `x5t`/`x5chain`), and a signature covering all of it. §5.1.1.1
  adds the service-side obligation: "The Issuer identity MUST be bound to the
  Signed Statement by including an identifier in the protected header."
- **The assertion is not modelled at all.** `payload : bstr / nil`, opaque to
  the service, optionally detached, optionally hashed, optionally encrypted,
  and — in the CDDL — optionally untyped.
- **And the document says so.** §9.2: "registering a Statement only proves it
  was produced by an Issuer."

**Assessment.** The asymmetry is correct for a transparency layer, and we adopt
it with one change. It is correct because the two questions have different
answerers: *who asserted this* is answerable by cryptography and belongs in
the envelope; *is it true* is answerable only by domain knowledge the service
does not have and must not pretend to. Collapsing them is how notarisation
gets mistaken for endorsement. §9.2 is the document declining to make that
mistake, and A9 turns the declination into a constraint on our format.

It is also the exact inverse of the failure mode on the other side of this
topic: `draft-ietf-vcon-vcon-core-04` models the content in detail and has no
asserter in its data model at all (recorded in this record's `implementations`
note). One document models the speaker and not the speech; the other models
the speech and not the speaker. Our shape needs both, and RFC 9943 is the
better half to start from, because the asserter half is the half that is hard
to retrofit — it has to be inside the signature, and you cannot move a field
inside a signature after the fact.

The one change is B2: **opaque to the service must not mean untyped to the
relying party.** DEC-007 asks "over what", and `sub` answers it at the level of
*which artifact*; it does not answer *what kind of claim this is*. The content
type is the only field that does, and RFC 9943 makes it optional. We make it
mandatory. That is the whole of our disagreement with the shape.

### R-M-12 — native extension points must be key-relative, not registry-dependent

R-M-12 and D-3's "no IANA tags" are **the same commitment stated twice** —
once as a requirement on our extension mechanism, once as a decision about our
encoding. The wording of R-M-12 here is a **reconstruction**; the id has no
in-repo definition, though `docs/scope.md` line 119 corroborates the reading,
noting that the IANA COSE Header Parameters registry "bears heavily on
R-M-12". **[gloss — R-M-12]**

**What adopting the envelope would actually cost**, concretely, under "no IANA
tags":

1. **The base is registry-defined and cannot be made otherwise.** Tag 18;
   labels 1, 3, 4, 15, 33, 34 in the protected header; labels 1 and 2 inside
   the CWT-Claims container; 394, 395, 396 for receipts and proofs. Adopting
   the envelope as canonical means our decoder holds a table of allocations
   from four registries — CBOR Tags, COSE Header Parameters, CWT Claims, and,
   for label 3's `uint` branch, CoAP Content-Formats — before it can read a
   single field. None of these allocations costs us an *application* to IANA;
   they are already made. The cost is not procedural, it is **semantic
   dependency**: the meaning of our canonical form would live in registries we
   do not control and in documents we have not extracted (RFC 9597 for label
   15, RFC 9360 for 33/34, RFC 9942 for 394/395/396). That is the dependency
   R-M-12 exists to prevent.
2. **Extending it in the intended way does cost an allocation.** The idiomatic
   COSE extension is a new integer header label, and a new integer label needs
   registry action to be interoperable. §10 shows the pattern in operation:
   RFC 9943 needed two new media types and two new CoAP Content-Format numbers
   simply to name its two objects. If our profile grew a field, the
   SCITT-native way to carry it would be another allocation, and our release
   cadence would be coupled to a registry's.
3. **Which is precisely what R-M-12 forbids**, so the native answer is: our
   extension points are named by key, relative to our own namespace, and
   require no allocation from anyone.

**Does `* label => any` change the answer?** Partially — and the partial
matters in three directions, the third of which only became visible after the
Figure 7 check.

- **It reduces the cost of *our* extensions to zero, in the protected map.**
  `label = int / tstr`, and in Figure 3 the wildcard appears on
  `Protected_Header`, `CWT_Claims` and `Unprotected_Header`. So we can carry
  key-relative extensions as `tstr` labels — namespaced strings we mint
  ourselves — with no registry action, covered by the RFC's own normative
  CDDL, and inside the signature. This is a genuinely good fit with R-M-12 and
  is why "COSE as export only" is cheap rather than lossy: we do not have to
  drop our own fields in order to export.
- **It does not change the cost of the *base* at all.** The wildcard admits
  additional labels; it does not make labels 15, 1 or 2 optional. The
  mandatory core stays registry-defined however many `tstr` labels we add.
- **It is not present where we might most want it.** Figure 7's
  `Unprotected_Header` is a closed map (C7): no wildcard, no `x5chain`, just
  394. So the hatch exists on the signed side and closes on the attachment
  side. Anything key-relative must therefore be inside the signature, which is
  B7.
- **And it cuts against us in one further respect.** There is no
  must-understand mechanism in RFC 9943. §6.3 step 3 says only "The TS MUST
  check the attributes required by a Registration Policy are present in the
  protected headers" — so a protected header the service's policy does not
  name is simply not examined. A key-relative extension we add rides along
  inside the signature and carries **no guarantee that the service considered
  it**. For export that is acceptable (the receipt witnesses inclusion, not
  comprehension), but we must not design semantics that depend on a
  Transparency Service having *acted on* one of our extension fields.

**Net.** R-M-12 is satisfiable natively and survives export, provided our
extensions live in the protected map. The answer to "what would adopting the
envelope cost" is: a decoder that depends on four registries and three
unextracted RFCs to read our own canonical form. That is why D-3 chose option
5, and why this record is evidence for that choice rather than against it.

### §9.4's key-management MUST triple

Worth isolating, because it is the **only normative content in the whole of
§9**:

> "Issuers and TSs MUST:
> * carefully protect their private signing keys
> * avoid using keys for more than one purpose
> * rotate their keys at a cryptoperiod (defined in [RFC4949]) appropriate for
>   the key-algorithm and domain-specific regulations" — §9.4

Three things follow. First, **none of the three is testable from the wire**: no
relying party can check protection, purpose separation, or cryptoperiod by
inspecting a statement or a receipt. They are operational obligations with no
verification path, so they belong in `requirements.yaml` as `testable: no`,
and they cannot be the basis of any guarantee we offer. Second, the second
bullet — *avoid using keys for more than one purpose* — sits in mild tension
with §6's "Issuers MAY use different signing keys ... for different Artifacts
or sign all Signed Statements under the same key.", which explicitly blesses
one key across every statement; the reconciliation is presumably that
"purpose" means signing-versus-other-use rather than per-artifact, but the
document does not say so. Third, and most usefully: the fact that §9's only
MUSTs are about key hygiene tells us where the real security content is.
Everything that actually constrains an implementation lives in §5–§7, and §9
is where the unsolved problems were parked — rollback, revocation, agility,
ordering, completeness. Reading §9 as the security model would be a mistake;
it is closer to an inventory of what the architecture does not do.

### Where we relied on a reconstructed gloss

Marked **[gloss]** above. None of `DEC-002`, `DEC-007` or `R-M-12` is defined
inside this repository; the wordings below are reconstructions supplied to the
extraction, not definitions we can resolve here.

| id | reconstruction relied on | corroboration inside this repository |
|---|---|---|
| **D-3** | "option 5: reduced CBOR, no IANA tags, COSE as export only" | `docs/extraction.md` line 36 — stated in-repo, so this one is quoted rather than reconstructed. The meeting that decided it is still external |
| **DEC-002** | option 2 is "CBOR + CDDL as canonical; COSE for signed form", with a direction to start from a reduced CBOR profile | **none.** `topics/canonical-encoding.yaml`, `topics/cbor-implementation.yaml`, `topics/cbor-ecosystem.yaml` and `topics/scitt.yaml` name the id in `bears_on` without defining it |
| **DEC-007** | the statement/assertion shape: who asserts, over what | `topics/scitt.yaml`, whose recorded answer reads "For DEC-007 the shape is worth copying - iss and sub are mandatory, the assertion is an opaque tagged payload" — consistent with the gloss, but itself one of our own conclusions rather than a definition |
| **R-M-12** | "native extension points must be key-relative, not registry-dependent" | `docs/scope.md` line 119, "The IANA COSE Header Parameters registry is a single `dataset` record even though it bears heavily on R-M-12" — corroborates the registry reading, does not define the requirement |

Everything in this file that is a claim *about RFC 9943* comes from the source
and carries a locator. Everything that is a claim about *what we should do*
depends on the glosses above and should be re-checked when ARCH-0001 is
readable from here. That re-check is O1.

---

## Open questions

**O4 is first because it is the highest-value open item in this file.**

**O4 — Is the export mapping invertible?** Step 5 of the export mapping is
forced by §6.3 step 2 and §7.1, which both require verification "per Section
4.4 of RFC 9052 [STD96]": **the COSE signature is computed over the exported
bytes, not over our canonical bytes.** So a statement destined for a
Transparency Service acquires a *second* signature, over an encoding that is
not the one our canonical signature covers. For a relying party to check our
canonical signature after receiving a transparent statement, `export` must be
invertible on exactly the fields the canonical signature covers. That is
asserted here as design intent and **has not been demonstrated**. If the
mapping is not invertible, then "COSE as export only" means our statements
lose their canonical signature on export — a materially different decision
from the one D-3 records, and one that should go back to the meeting rather
than be settled in a design note.

**O1 — The decision ids do not resolve from inside this repository.**
`DEC-002`, `DEC-007` and `R-M-12` are link targets with no definition here;
`D-3` is a meeting decision glossed in one line of `docs/extraction.md`. Every
**[gloss]** marker above is a place where a judgement rests on a
reconstruction. This is a library-wide problem rather than one with this
record — `schema/record.schema.yaml` names ARCH-0001 as the home of these
ids — but it caps the confidence of the mapping section at whatever the
glosses are worth.

**O2 — What, exactly, does label 15 oblige?** RFC 9597 defines the CWT Claims
header parameter; RFC 9943 mandates it and says nothing beyond "as specified
in Section 2 of [RFC9597]" (§6). We do not know from this document what
RFC 9597 says about claims appearing in *both* a COSE header and a CWT
payload, about duplicate claims, or about what a verifier must do on conflict.
Our export synthesises this container (mapping step 2) and we cannot currently
prove the synthesis is correct.

**O3 — How is the issuer's key actually found?** §6 says "Key discovery
protocols are out of scope of this document.", and §6.3 says the service "MUST
verify the signature of the Signed Statement with the signature algorithm and
verification key of the Issuer per [RFC9360]". Key resolution is thus both out
of scope and delegated, in adjacent sentences. Until RFC 9360 is extracted we
cannot say what `x5t`/`x5chain` oblige a verifier to do, and so cannot finish
B3 or the 33/34 rows of the mapping.

**O5 — Do we need a transparency layer at all, and at what cardinality?** A6
adopts a witness *list*. RFC 9943's own residual guarantee is narrow: §9.3
notes an issuer "can refuse to register their Statements with a TS or
selectively submit some but not all the Statements they issue", and offers only
the advice that relying parties should not accept statements whose receipts
they cannot discover — while discovery is explicitly out of scope ("How these
statements are managed or stored as well as how participating entities
discover and notify each other of changes is out of scope of this document.",
§1). Completeness is therefore unprovable in this architecture. Whether we take
on that layer, and what we claim for it, is undecided.

**O6 — What is our answer to C2?** B6 sketches one: declared epoch breaks,
epoch-scoped witness validity, a retained prior log. It is a sketch. The
underlying question — *what does a relying party do when the entity that
witnessed its statement loses its key* — is one RFC 9943 puts out of scope
("Revocation strategies for compromised keys are out of scope for this
document.", §9.4.2), and it is not out of scope for us.

**O7 — Source defect: Figure 7's `Unprotected_Header`.** C7, both halves. The
duplicate rule name should be checked against RFC 8610's rules on rule
redefinition, and the closed map should be checked against §6 and §6.3, which
it contradicts. If both hold, this warrants an erratum report. Note that the
second half is not merely editorial: it determines whether a key-relative
extension can survive the attachment of a receipt (B7).

### Dependency closure — what RFC 9943 cannot be implemented without

RFC 9943 defines almost no structure of its own. Its normative CDDL is seven
labels, five of them defined elsewhere, and its security argument is inherited
in full. The closure below is the set of documents that must be readable
before anything here is more than a reading of one document's prose.

**All five of these records exist in this library. None has a `distilled/`
directory. They are therefore unextracted frontier gaps, not missing records**
— the distinction matters, because the work needed is extraction, not
ingestion:

| record | held? | status | why RFC 9943 needs it |
|---|---|---|---|
| `records/ietf/rfc-9597` | **yes** | `fetched` | Defines the CWT Claims header parameter at **label 15**, the one mandatory element of the entire protected header (§6). Without it we do not know what our export's synthesised container means. **O2** |
| `records/ietf/rfc-9360` | **yes** | `fetched` | Defines `x5t` (34) and `x5chain` (33), and is the document §6.3 delegates verification-key resolution to. §5.1.1.1's certificate-path MUST is unimplementable without it. **O3** |
| `records/ietf/rfc-8392` | **yes** | `fetched` | Defines CWT and the `iss`/`sub` claims, and is what §6 invokes for the "URI requirements" constraining `iss`. B3 turns those requirements into an unconditional rule and cannot state them precisely until this is read |
| `records/ietf/rfc-8610` | **yes** | `fetched` | CDDL. Figures 3 and 7 are both declared normative; validating them — including the `&(name: n)` group-enum notation, the `.cbor` control, and the duplicate-rule-name question in **O7** — requires it |
| `records/ietf/rfc-9162` | **yes** | **`stub`** | The only concretely named Verifiable Data Structure: §7 notes "the Verifiable Data Structure algorithm RFC9162_SHA256 is value 1", and §5.1.3 puts the analysis out of scope — "Specific VDSs, such as those described in [RFC9162] and [RFC9942], and the review of their security requirements for SCITT are out of scope for this document." So **every claim about what a receipt actually guarantees is inherited from a record we hold only as a stub** |

Two further dependencies are in better shape, noted for completeness:
`records/ietf/rfc-9942` (COSE Receipts) is `distilled` and defines labels 394,
395 and 396 and the receipt format itself; `records/ietf/rfc-9052` (COSE, as
STD 96) is `fetched` and is what §6.3 and §7.1 point at for the signature
verification procedure; `records/ietf/rfc-8949` (CBOR, as STD 94) is `read`.

**Ranked, with reasons.**

1. **`rfc-9162`** — first, and not close. It is the only one still at `stub`,
   and it is where the entire security argument lives. §5.1.3 declares VDS
   security requirements out of scope for RFC 9943, which means the question
   this record exists to answer — *what does a receipt actually prove* — is
   answered in RFC 9162 and nowhere in RFC 9943. Until it is read, every claim
   in this file about the strength of a transparency guarantee is inherited
   rather than checked. It is also the weakest link in the closure by status.
2. **`rfc-9597`** — label 15 is the single mandatory element of the protected
   header, and our export *synthesises* that container (mapping step 2). We
   are constructing a structure whose rules we have not read. **O2**.
3. **`rfc-9360`** — blocks **O3** and the 33/34 rows of the mapping. Needed
   before we can say what declining X.509 actually costs on export.
4. **`rfc-8392`** — needed for precision on B3: the exact "URI requirements"
   that constrain `iss`, which we are proposing to apply unconditionally.
5. **`rfc-8610`** — needed for precision on **O7** and to validate Figures 3
   and 7 mechanically rather than by eye.

Items 1–3 change conclusions. Items 4–5 sharpen wording that is already in the
right direction.
