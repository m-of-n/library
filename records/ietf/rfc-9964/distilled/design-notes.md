---
record: rfc-9964
kind: design-notes
title: "rfc-9964 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 9964 — bearing on our design

Voice markers, as `rfc-8949`: **unmarked** is the source or our own decisions as
cited; **[analysis]** is this extraction's reasoning; **[correction]** is a
project assumption the sources do not support.

RFC 9964 is a small document — 2906 lines, of which 2249 are Appendix A — with
one load-bearing section. §6 is the answer to a question RFC 9679 §4.6 asks and
declines to answer, and `records/ietf/rfc-9679` is at `profile: full` with that
dependency recorded. This extraction's job was to make the consequence
*measurable*. It is: see `examples/README.md`.

---

## What we adopt

**§6's COSE Key Thumbprint parameter set, as the definition of `KeyId` for any
post-quantum key we hold.** Verbatim, bullets as printed:

> When computing the COSE Key Thumbprint as described in [RFC9679], the
> required parameters for AKPs are:
>
> *  "kty" (label: 1, data type: int, value: 7)
>
> *  "alg" (label: 3, data type: int, value: int)
>
> *  "pub" (label: -1, value: bstr)
>
> The COSE Key Thumbprint is produced according to the process
> described in Section 3 of [RFC9679].

We adopt it because there is no alternative that `R-O-03` permits
("Canonicalization algorithm for each concrete encoding SHALL be cited, not
invented silently"). A digest over `(kty, pub)` alone would cite no document.
`rfc-9679`'s design notes reach the same conclusion by a different route and
that reasoning holds — see *Checks against the sibling records* below.

**The three code points, as our only registered post-quantum signature
identifiers.** `ML-DSA-44 = -48`, `ML-DSA-65 = -49`, `ML-DSA-87 = -50`
(§8.1.1), each "Capabilities: [kty]" and "Recommended: Yes". The key type is
`AKP = 7` (§8.1.2.1), with `pub` at label −1 and `priv` at label −2 (§8.1.3).

**The seed-only private key.** §4: "the priv parameter MUST be the seed and MUST
have a length of 32 bytes", and "This specification intentionally does not
define a means of utilizing the expanded private key representation defined by
US NIST FIPS so as to increase interoperability by having a single ML-DSA
private key representation for COSE and JOSE." A 32-octet private form is the
one piece of good news in the size story, and it removes a representation
choice we would otherwise have had to make.

**The six Appendix A figures, as fixtures.** Three JOSE, three COSE, one per
parameter set, with real keys, real signatures, the exact signed bytes, and
`kid` values that reproduce. **The library had no post-quantum fixtures before
this record.** `examples/vectors.yaml`.

---

## What we adapt, and how

**The size table becomes a budget, not a footnote.** §5, the document's own
warning:

> ML-DSA produces significantly larger public keys and signatures compared to
> traditional algorithms.  This size increase can create challenges for
> deployments with limited bandwidth, memory, or processing capacity.  ML-DSA
> may not be suitable for use cases requiring small keys or signatures.  Use of
> thumbprints as described in [RFC7638] and [RFC9679] can reduce the need to
> repeat public key representations.

Measured against our own objects: an `AuthzCert` under option 5 carries an
issuer and a subject principal. With `KeyId` that is 2 × 32 octets. With `Key`
(`R-M-02` permits either) it is 2 × 1312 at ML-DSA-44 and 2 × 2592 at
ML-DSA-87 — and a `Threshold` principal with *n* members multiplies it. A 3-of-5
threshold subject carried as keys is 6560 octets at ML-DSA-44 and 12 960 at
ML-DSA-87, before any signature.

**[analysis]** So §5's closing sentence is the document recommending the exact
construct whose `alg`-dependence makes our naming unstable. **The size argument
and the identity argument point opposite ways, and nothing in our documents has
had to weigh them against each other before.** That trade is the substance of
`DEC-003` and it is now quantified rather than asserted.

**The `ctx` requirement has nowhere to live, so it becomes a code rule.** §5:
"The ctx parameter MUST be the empty string for ML-DSA-44, ML-DSA-65, and
ML-DSA-87." **[analysis]** `ctx` is a FIPS 204 signing input. It has no label in
the COSE Key Common Parameters registry, none in COSE Header Parameters, and no
JWK member name — checked. So this MUST is **unobservable from the wire bytes
and unenforceable by any schema**, ours or anyone's: a signature produced with a
non-empty `ctx` is byte-indistinguishable from a conforming one and simply fails
to verify. It is the only normative requirement in §5 with that property, and it
belongs in our signing code with a test, not in a profile document.

**The validation duty is ours to carry out, and §7.3 says exactly what it is.**

> For the ML-DSA algorithms registered in this document, the priv key parameter
> is the seed, and therefore, the seed length check MUST be performed.  The
> length of the seed is 256 bits, which is 32 bytes.

and, on `pub`, that pkEncode/pkDecode "inputs need to be within the ranges given
in the algorithms", plus the FIPS 204 quotations "skDecode should only be run on
inputs that come from trusted sources" and "as the seed can be used to compute
the private key, it is sensitive data and shall be treated with the same
safeguards as a private key". **[analysis]** The second of those lands on us
harder than on a general implementation: our `KeyId` is a digest of `pub`, so a
`pub` that is the right length but out of range still yields a perfectly
well-formed 32-octet principal name. Identity is computable on an invalid key.

---

## What we reject, and why

**The JOSE half, as a native target.** §8.1.4 and §8.1.5 register the three
algorithms and the `AKP` key type for JOSE with "JOSE Implementation
Requirements: **Optional**", against "Recommended: **Yes**" on all three COSE
algorithm registrations (§8.1.1). The same document, the same algorithms, two
different strengths of recommendation. `MD-3` already makes CBOR the canonical
encoding; this is an independent reason not to treat the JWK form as anything
but interchange.

**HashML-DSA, as a planning assumption.** §7.2: "This document does not specify
algorithms for use with HashML-DSA ... As the verify routines are different,
future support for HashML-DSA would require the registration of additional
algorithms." `rfc-9053`'s design notes read this alongside RFC 9053 §2 and
conclude "COSE declines pre-hash variants and pushes the hash into the payload".
**That reading is correct and the quotation is accurate** — verified against
`.cache/rfc-9964.txt` lines 301–310. Consequence for `R-I-07` (SPDX or CycloneDX
*inside* a predicate): there is no pre-hash code point to reach for, so a large
predicate is signed whole or carried by digest with the bytes elsewhere.

**Table 1's "Private Key" column, as a field size.** 2560 / 4032 / 4896 are the
*expanded* key sizes, and the document's own note says so: "priv size is always
32 bytes and that KeyGen_internal is called to produce the expanded private keys
for "Private Key" in the table above." Our `priv` is 32 octets. A reader who
sizes a field from the table is wrong by two orders of magnitude; recorded as
`examples/vectors.yaml` V-0003 so a test can catch it.

---

## Mapping to our decisions

### 1. What our post-quantum export must carry, with code points

Every number below is from §8.1 or measured from Appendix A. Nothing here is
inferred.

**The key, as a COSE_Key (`messages.yaml` `AKP_COSE_Key`):**

| entry | label | encoded | value |
|---|---|---|---|
| `kty` | 1 | `01 07` | 7 (AKP) |
| `alg` | 3 | `03 382f` / `03 3830` / `03 3831` | −48 / −49 / −50 |
| `pub` | −1 | `20 590520` / `20 5907a0` / `20 590a20` | 1312 / 1952 / 2592 octets |
| `priv` | −2 | `21 5820` | the 32-octet seed; MUST NOT appear in a public key |
| `kid` | 2 | `02 5820` | 32 octets — not required by this document |

A minimal public key — `kty`, `alg`, `pub` and nothing else — is 1322, 1962 and
2602 octets; with `kid` and `priv` it is 1392, 2032 and 2672, which is what
Appendix A prints. **[analysis] And a minimal AKP public COSE_Key is
byte-identical to its own §6 thumbprint input** — measured for all three
parameter sets. That is a convenience for us (one encoding, two uses) and a
trap for anyone who assumes a thumbprint input is a *reduced* form of a key: for
AKP it is the whole public key.

**The `KeyId`, as the §6 thumbprint input — this is the part an export cannot
get wrong:**

```
a3  01 07  03 <alg>  20 <bstr head> <pub>
```

1322, 1962 and 2602 octets for the three parameter sets, under RFC 8949 §4.2.1
deterministic encoding (required by RFC 9679 §3 step 2 — **RFC 9964 never
restates it**), SHA-256 to 32 octets. Entry order is 1, 3, −1.

**The signature, as a COSE_Sign1 (`messages.yaml` `ML_DSA_COSE_Sign1`):**

```
d2  84  5827 <39-octet protected>  a0  <payload>  59 <len> <signature>
         protected = a2 01 <alg> 04 5820 <32-octet kid>
```

Signatures are 2420, 3309 and 4627 octets. **The envelope is tagged 18 in all
three of the document's examples** and the untagged form is never printed.

**And the thing an export must carry that is easy to miss: there is nothing
else.** RFC 9964 registers **no COSE header parameter and no JOSE header
parameter.** §8.1 touches six registries — COSE Algorithms, COSE Key Types, COSE
Key Type Parameters, JOSE Algorithms, JOSE Key Types, JWK Parameters — and "COSE
Header Parameters" is not among them. ML-DSA contributes three new *values* for
`alg` (label 1, RFC 9052's) and nothing more. **[analysis]** For our export
mapping that is unambiguously good news: the post-quantum signature path adds
exactly three integers to the interchange surface, and `R-I-01`'s mapping table
gains three rows rather than a section.

**Which of those three parameters a `KeyId` depends on: `kty`, `alg` and `pub`
— all three, and `alg` is the one that bites.** `priv` and `kid` are excluded.
A public and a private AKP key for the same material have the same thumbprint.

### 2. The `KeyId` consequence

**Stated concretely, with the bytes.** If `KeyId` is a COSE Key Thumbprint and
the key is AKP, then for one byte-identical 1312-octet `pub`:

| `alg` | `KeyId` | provenance |
|---|---|---|
| −48 | `b8969ab4b37da9f0684e42647eb8a0be8b5b661ebf5d76f0583bf5b8d3a8059a` | **printed by RFC 9964** as the `kid` of Figure 6 |
| −49 | `f507c41723160cdec5f245a8f6b6c0cd8144f1febae70df0c24fa4fcf187315d` | computed by this extraction |
| −50 | `de68d5ecb9465cd4c06dd1b246a20f50d0b928bdff52433e53e4d387e128f62b` | computed by this extraction |

Three 1322-octet inputs differing in **one octet** — offset 5, holding `2f`,
`30`, `31` — and three digests sharing **no prefix**. (Corrected by the verify
pass from "two octets": `0x38` at offset 4 is the shared major-type-1
one-byte-argument head of all three `alg` values, so only the argument byte
differs. The inputs begin `a3010703382f2059`, `a301070338302059`,
`a301070338312059`. A single octet relocates the whole digest.)
One leg is the document's own printed value and reproduces exactly,
which anchors the method before the other two are computed with it
(`examples/vectors.yaml` V-0007, V-0010, V-0011). `rfc-9679` V-0004/5/6 argued
this with 32 zero octets standing in for a key; this measures it on a real one.

**Under `ARCH-0002` P1 — accepted by `ADR-0001` — that is a namespace rename.**
P1: "An extension point is a pair: `(defining key, local label)`" and "Compound
reference follows SDSI name chaining exactly." So a parameter migration
ML-DSA-44 → ML-DSA-65 on the same key material does not re-sign anything; it
*renames* the principal, and with it every type that principal defined and every
compound name in its chain. Existing statements stay cryptographically valid and
become statements by a principal no verifier can now name.

**And it is worse than a migration story.** `alg` is a property of a *use* of a
key, not of the key material. V-0010 is a well-formed §6 thumbprint over the
Figure 6 key asserted under ML-DSA-65 — §6 types `alg` as a bare `int` with
nothing tying it to the key, and §6 itself says AKP suits "algorithms other than
ML-DSA". So **one key asserted under two algorithm identifiers is two
principals, today, with no migration involved.** §7.4 ("Mismatched AKP
Parameters") is the nearest the document comes, and it addresses a different
mismatch — `pub` against `priv`, not `alg` against key.

**The mitigations that exist.**

1. **`NameCert` is already the continuity construct, and nobody has said so.**
   `ARCH-0001` §4.2 gives `NameCert` as binding "name labels → principal",
   signed by a naming key, with reduction role "Name resolution only"; §4.3
   gives the procedure: "**Name resolution** — rewrite `Name` to `KeyId` via
   `NameCert` chains." A stable `Name` under a stable naming key resolves to
   whichever `KeyId` is current, so continuity is expressible in the model we
   already have. **[analysis] The honest statement is not that the thumbprint is
   unfit — it is that a thumbprint is an identity and a name is a continuity,
   and P1 needs both.** `rfc-9679` reaches the same formulation and it holds.

   **[analysis] But there is a regress `rfc-9679` does not raise, and it is the
   one that matters for a post-quantum deployment.** The naming key has a
   `KeyId` too. If the naming key is itself post-quantum, then *its* parameter
   migration renames the namespace that was supposed to supply continuity, and
   the `NameCert` chain rooted at it is renamed along with it. `NameCert` gives
   continuity for *subjects*, not for the root. Either the naming key is
   classical — which defeats the point of migrating — or continuity at the root
   needs something else: a cross-signature from the old root to the new, which
   is a construct our documents do not have and `ARCH-0001` §4.2's table does
   not list.

2. **Carry the `Key`, not the `KeyId`.** `R-M-02` is permissive: "A principal
   MAY be identified solely by key or key digest." **MAY.** And `DEC-003`'s
   first listed option is literally "raw COSE key". A raw `pub` is
   `alg`-independent, so **`DEC-003` option 1 is immune to this hazard and
   option 2 ("COSE key thumbprint") is not.** The cost is §5's: 1312–2592 octets
   per principal, multiplied by threshold membership. **[analysis] That is the
   real shape of `DEC-003`: not five equally-weighted options, but a size/identity
   trade in which exactly one option is stable under post-quantum parameter
   change and it is the expensive one.** `ARCH-0001` §7 lists the five flat.

   **[analysis] One measured detail makes the expensive option cheaper than it
   looks, under one condition.** A **minimal** AKP public COSE_Key — `kty`,
   `alg`, `pub`, nothing else, in RFC 8949 §4.2.1 order — is byte-identical to
   its §6 thumbprint input; verified for all three parameter sets. So *if our
   profile fixes that as the wire form of a carried key*, a verifier computes
   the `KeyId` by hashing the bytes it received: no subsetting, no re-sorting,
   no canonicalisation of untrusted input, and therefore none of the `R-O-05`
   tension `rfc-9679`'s Cut H raises. Carrying the key costs 1322 octets instead
   of 32 and *removes* a processing rule rather than adding one.
   **The condition is load-bearing and RFC 9964's own examples fail it** — all
   three carry `kid` and `priv` and put `kid` first — so this is a profile
   obligation on us, not a property we inherit.

3. **Digest agility does not help.** `ARCH-0001` §4.1 defines `KeyId` as a
   "Digest of a canonical key encoding (algorithm of digest is parameterized)".
   **[analysis]** Parameterising the *hash* is orthogonal: the instability is in
   the *input*. Changing SHA-256 to SHA-384 changes every `KeyId` too, and
   changing neither still leaves `alg` inside the preimage. Recorded because
   "the digest is parameterized" reads like agility and is not agility against
   this.

4. **A consistency rule we owe and have not written.** `alg` ends up in the
   exported bytes **twice**: inside the `KeyId` that the protected header's `kid`
   carries, and as the protected header's own `alg` (label 1), which RFC 9052
   requires for verification. A verifier must check the two agree, or it accepts
   a statement whose key identifier names a different algorithm than the one it
   verified under. V-0010 is exactly those bytes. **[analysis]** This is the
   `rfc-9679` Cut H shape — a rule the profile owes that no document of ours
   states — and it is not specific to any `DEC-002` option.

**The question our documents do not answer, checked mechanically.**
**Nothing in `ARCH-0001`, `ARCH-0002`, `ADR-0001` or `ARCH-0001-PROPOSAL-v0.2.0`
says whether `KeyId` means "this key, now" or "this principal, across changes".**
`grep -E 'rotat|continuity|rekey|re-key|same principal'` across all four returns
**one** hit, `ARCH-0001` G5, which is about artifact statements sharing principal
machinery and not about key change at all. `ARCH-0001` §4.1 says only "Digest of
a canonical key encoding". **[analysis]** Until that is decided, "is this the
same principal?" has no answer in the model, and RFC 9964 is the document that
makes the ambiguity cost something: under the first reading a parameter
migration is correct behaviour, under the second it is a bug, and the same bytes
satisfy both.

### 3. Where this cuts against `MD-3`, and which options it favours

`MD-3` narrowed `DEC-002` to **option 5** — proposal §3.3, verbatim:

> **DEC-002, proposed additional option 5.** CBOR as the canonical encoding,
> using the CBOR data model and deterministic encoding rules, but with **no
> reliance on the IANA CBOR Tags registry and no native use of COSE header
> parameters**. Types, predicate types, and tags are identified key-relatively
> per R-M-12, carried as ordinary map entries. COSE_Sign1 and DSSE remain
> **export** envelopes under R-I-03, with the mapping from key-relative
> identifiers to registered COSE labels documented as a lossy interchange step
> in the §6 matrix.

— on 2026-09-28, and **is not an acceptance of it**: `DECISIONS-0001` tier 1
item 2 says "Still open: a narrowing is not an acceptance, and no ADR exists."
Six findings, each naming an option.

**Cut A — the no-tags rule now has a measured cost, on the signature path, and
it corrects a sibling record's reading.** `rfc-9679`'s Cut C concluded that "the
no-tags half of `MD-3` costs nothing here, and this document does not
discriminate option 2 from option 5", because RFC 9679 §3 uses no CBOR tag at
any step. **That is right about RFC 9679 and it does not generalise.** All three
of RFC 9964's COSE examples are **tagged 18**: every `sign1` hex begins `d2` and
every `sign1_diag` begins `18([`. The document never prints the untagged form
and never discusses the choice. So the one document that defines post-quantum
COSE signatures exhibits only the IANA-tagged envelope, and under **option 5**
export must *add* tag 18 and import must *strip* it, as `rfc-8949`'s notes
predicted in the abstract. Under **option 2** ("CBOR + CDDL as canonical; COSE
for signed form") the tagged bytes are native and there is nothing to strip.
**A cost option 5 pays that option 2 does not** — one octet of bytes, but a
conformance rule, and on the path every signed statement traverses. Not a
contradiction of Cut C: a different document and a different layer, which is
why it is stated here rather than there.

**Cut B — option 5's own stated rationale is unachievable at the identity
layer, and this is the finding that cuts hardest.** Option 5 exists to keep
"the native model free of central allocation" (proposal §3.3); `ADR-0001`
rejects private-use ranges because they give "escape from a registry, not a
namespace". But a `KeyId` over a post-quantum key **contains an IANA
allocation**: −48, −49 or −50 from the COSE Algorithms registry, inside the
preimage, in the two-octet span at offsets 4–5 of which **one octet — offset 5 —
is the allocation itself** (`2f`, `30`, `31` for −48, −49, −50). **[analysis] The namespace root that P1 says
needs no permission from a registry has a registry number baked into its
bytes.** And unlike `rfc-9679`'s Cut A, where the registry dependence was in the
*labels* of the digested map, here it is in a **value that changes the digest** —
so it is not merely a dependence, it is a dependence with semantics.

Which options escape? **None.** §6's JWK set also requires `alg`, whose value is
the IANA JOSE Algorithms name `"ML-DSA-44"`, so **option 3** (JCS + DSSE) and
**option 4** inherit it; **option 1** (canonical S-expressions) would have to
digest some key representation, and the only ones FIPS 204 and RFC 9964 define
are these. The only escape is to digest `(kty, pub)` alone, which cites no
document and is therefore an invention under `R-O-03`. **[analysis] So this does
not reorder the options — it removes a claim option 5 makes for itself.** `MD-3`
narrowed on the strength of registry-independence; registry-independence is
not available for post-quantum principals under any candidate. That is a
material correction to the premise of the narrowing, and the ADR must state it
rather than inherit it.

**Cut C — option 4 is eliminated again, and this time with numbers.**
`rfc-9679`'s Cut B eliminated **option 4** ("Dual canonical (CBOR and JSON) with
a documented bijection") on §5.5's rule that `ckt` and `jkt` differ. This record
supplies the measurement: three keys, six digests, and in every pair **not one
of the 32 octet positions agrees** — re-derived by the verify pass, which
measured positional agreement rather than only the shared prefix: 0 of 32 for
all three pairs. (A handful of octet *values* recur at different positions, as
chance requires; no position matches.) All six are printed by this one document
as those keys' `kid` (`examples/vectors.yaml` V-0012). **[analysis] And one point sharper than the
rule.** §6 defines the two required sets **in the same section, over the same
three parameters, in the same document** — and still yields two values. So the
divergence is not an artefact of different parameter sets; it is purely the
serialisation. A bijection at the encoding layer cannot give one at the identity
layer, and this is the cleanest demonstration available that it cannot.

**Cut D — `DEC-005` is discriminated, on a ground `DEC-005` does not list.**
`DEC-005` is "Envelope for ArtifactStatement. Options: DSSE (in-toto world),
COSE_Sign1 (SCITT world), both with a single unsigned payload schema." RFC 9964
gives COSE three registered algorithm identifiers marked "Recommended: Yes",
gives JOSE the same three marked "Optional", and gives **DSSE nothing** — and
that is not an omission RFC 9964 could have fixed. `records/community/secure-systems-lab-dsse`
records DSSE as "Deliberately algorithm-agnostic — `Sign()` is 'an arbitrary
digital signature format' agreed out of band", with "Signature algorithm and key
management ... out of scope", and its `KEYID` "unauthenticated and `MUST NOT` be
used for security decisions". **[analysis] So for a post-quantum `ArtifactStatement`, COSE_Sign1
is the only one of `DEC-005`'s options with a standardised, interoperable
algorithm identifier, and "both" means maintaining one envelope that can name
its algorithm and one that cannot.** This favours `DEC-005`'s COSE_Sign1 option
and costs the DSSE and "both" options. It also happens to support `MD-3`'s
direction, and is recorded with the same weight as the cuts that do not.

**Cut E — a small place the narrowing is supported, recorded because an
extraction that only confirms is not evidence and one that only dissents is not
either.** `MD-3` keeps "YAML as the human form". §2 of RFC 9964: "Some examples
in this specification are truncated using "..." for readability", and §3's two
figures are truncated precisely because the values are 1312 octets. **[analysis]
A post-quantum key is not human-readable at any encoding, so our human form must
specify an elision convention — and RFC 9964's own practice (a `...` infix
showing prefix and suffix) is both the precedent and the cautionary tale, since
its Figure 2 `pub` prefix is wrong by one hex digit (`examples/README.md`). A
hand-maintained elided form drifts.** The lesson is that the elision must be
generated from the canonical bytes, never typed.

**Cut F — the determinism table gains no rows, and the identity path gains a
rule.** `rfc-9679`'s Cut E found that `DEC-003` adds nothing to the fourteen-row
determinism table because every required label encodes in one octet, so RFC 8949
§4.2.1's bytewise order and §4.2.3's length-first order coincide. **Confirmed
here for AKP specifically and mechanically**: labels 1, 3 and −1 encode as
`0x01`, `0x03`, `0x20`, one octet each. What §4.2.1 buys is the minimal `bstr`
head — `590520` for 1312 octets rather than a longer form — and the minimal
`alg` argument. **[analysis] But the printed COSE_Keys are not in §4.2.1 order
at all** (`kid` before `kty`), and the subsetting that produces the thumbprint
input from them comes out right **by accident**: dropping labels 2 and −2 from
`2, 1, 3, -1, -2` happens to leave `1, 3, -1`, which is §4.2.1 order. Measured
for all three figures. So the rule option 5's profile owes is "re-sort after
subsetting, always", and the RFC's own examples are the worst possible evidence
for it, because they work without it.

---

## Open questions

1. **Does `KeyId` name a key or a principal?** The question §2 above shows is
   unanswered in any of our documents. It must be settled before `DEC-003`, not
   after: the two readings make a post-quantum parameter migration respectively
   correct and broken, on identical bytes.
2. **What provides continuity at the naming-key root?** `NameCert` covers
   subjects; nothing covers the root. A root cross-signature is the obvious
   construct and `ARCH-0001` §4.2's table does not have it.
3. **Does the AKP `alg` have to be our `alg`?** §6 types it `int` and §6 says
   AKP suits "algorithms other than ML-DSA". **[analysis]** Under `ARCH-0002` P1
   a key-relative algorithm identifier is what we would otherwise want — but the
   thumbprint input takes an `int`, and a `(key, label)` pair is not an `int`. So
   P1 and §6 are structurally incompatible at this one field, and the resolution
   has to be that the thumbprint is an interchange construct we adopt whole, not
   a native one we parameterise. Worth stating in the ADR, because adopting §6
   *is* accepting one registry-allocated integer into the native namespace root.
4. ~~**Do the printed signatures verify?**~~ **ANSWERED — yes, all six, closed
   by the verify pass 2026-10-20.** FIPS 204 `KeyGen_internal` and
   `Verify_internal` were implemented for that pass and **gated on NIST ACVP
   known answers before being pointed at this document** (75/75 `keyGen`
   public keys reproduced; 90/90 `sigVer` verdicts agreed, 72 of them
   expected-reject). Then: all six printed public keys re-derive from the
   all-zeros seed byte for byte, and all six printed signatures verify under
   `ML-DSA.Verify(pk, M, σ, ctx="")`. Two consequences worth carrying into the
   ADR. First, **`R-0034` — "the `ctx` parameter MUST be the empty string" — is
   now the one requirement in this record whose satisfaction is demonstrated
   rather than asserted**, because the signatures only verify with
   `M' = 0x00 ‖ 0x00 ‖ M`; the MUST is still unverifiable *from a received
   object*, which was the original finding, but it is no longer unverifiable
   in principle. Second, **the authors' tooling is confirmed correct against
   FIPS 204**, so the Figure 2 prefix defect is a transcription slip in one
   figure and not a key-generation discrepancy. The record now has no
   unverified cryptographic claim.
5. **Which `DEC-003` option does the size budget actually permit?** §5's warning
   plus threshold principals gives 12 960 octets for a 3-of-5 subject at
   ML-DSA-87 carried as keys. **[analysis]** Nobody has costed it. The nearest
   thing we have to a size objective is the byte-cost argument in
   `rfc-8949`'s design notes against RFC 8949 §1.1 objective 2 (class-1
   constrained nodes, RFC 7228) — which is RFC 8949's objective, not one
   `ARCH-0001` states. **`ARCH-0001` sets no size budget at all**, and this is
   the first source that makes one necessary.

---

## Checks against the sibling records

The brief for this pass required their claims be treated as things to check.
Checked, against `.cache/rfc-9964.txt`.

**`rfc-9679`'s locators are accurate.** §3's "The alg JSON Web Key (JWK)
parameter or COSE Key Common parameter is REQUIRED for all AKP keys" is at lines
112–113, and §6's bullets at 246–256, exactly as its verify pass records. Its
`[corrected]` note — that the chain is §4.6 → RFC 9964 **§6**, which states the
set outright, rather than only §4.6 → §3 → §5.1, which derives it — is right,
and §6 is where `messages.yaml` and `examples/` attribute it.

**`rfc-9679`'s reading of "why RFC 9964 is not being gratuitous" holds.** AKP has
no `crv` — checked mechanically, `crv` occurs **zero** times in RFC 9964 — and
§3 says "The parameters for public and private information classes contain byte
strings in a format specified by the alg value." Without `alg` a `pub` has no
defined interpretation.

**`rfc-9679`'s Cut C needs the qualification in Cut A above.** "The no-tags half
of `MD-3` costs nothing here" is true of RFC 9679 and false of RFC 9964's
signature path. Not an error in that record — a limit of its scope, which this
record is the one positioned to extend.

**`rfc-9053`'s quotation of §7.2 is accurate** and its conclusion ("COSE
declines pre-hash variants") is supported by the text as printed.

**[correction] One assumption in this extraction's own brief needs correcting,
and it is worth recording because it would have weakened the central fixture.**
The brief described `pub`'s format as "specified by the alg value" and inferred
that this "forces `alg` inside the thumbprint". The inference is sound but the
*mechanism* in the brief is RFC 9964 §3; the operative text is **§6**, which
states the thumbprint set outright and needs no inference from §3 at all. The
difference matters for citation: a reader sent to §3 finds a statement about key
validity, not about thumbprints.

---

## Defects and ambiguities in RFC 9964 itself

Reported, never repaired (`docs/extraction.md`).

1. **Figure 2's `pub` prefix does not match the key it illustrates.** §3 line
   147 prints `h'ba71f9f64e11baeb589...'`; the same key's `pub` in Appendix A
   begins `ba71f9f64e11baeb58fa`. The 19th hex digit is `9` in the figure and
   `f` in the key. Prefix only; the suffix, `kid` and `priv` all match, and
   Figure 1 — the JWK rendering of the same key in the same section — is clean.
   Detail and method in `examples/README.md`.
2. **§6 names no hash function.** It defers to RFC 9679 §3, which takes the hash
   as a parameter. The string `SHA-256` occurs **zero** times in RFC 9964.
   SHA-256 is established only by the Appendix A `kid` values reproducing under
   it — an example, not a normative statement. For a document whose §6 is its
   load-bearing section, that is a real gap.
3. **§5's `ctx` MUST is unenforceable.** No registry this document touches has a
   label for `ctx`, so the requirement cannot be checked by any schema or
   verifier that reads only the wire bytes.
4. **Table 1's "Private Key" column invites the wrong field size.** Mitigated by
   the note immediately below it, which most readers of a table will not reach
   before sizing a field.
5. **The two halves of Appendix A are not a matched pair.** The JOSE examples
   sign "It's a dangerous business, Frodo, going out your door." (56 octets);
   the COSE examples sign "hello post quantum signatures" (29 octets). Same
   keys, different payloads, so no JOSE↔COSE round-trip fixture can be built
   from this document — which is a missed opportunity in a document whose §6
   defines two thumbprints for one key and whose §5.5 analogue in RFC 9679 says
   they differ.
6. **Not a defect, recorded to forestall a bug report:** the printed COSE_Keys
   are not in RFC 8949 §4.2.1 map order (`kid` precedes `kty`). Nothing requires
   them to be — §4.2.1 binds the thumbprint input, not the key — but see Cut F.
