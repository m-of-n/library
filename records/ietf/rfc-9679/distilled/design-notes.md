---
record: rfc-9679
kind: design-notes
title: "rfc-9679 — bearing on our design"
extracted: "2026-10-18"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§4.2`) are RFC 9679. Our own documents are cited by id (`ARCH-0002 P1`,
`MD-3`). Three markers distinguish voices:

- unmarked prose reports **RFC 9679** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 (v0.1.1) lists
**four** options; "option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3. `MD-3` (2026-09-28) narrowed DEC-002 to option
5 and **did not accept it**; `DECISIONS-0001` tier 1 item 2 says so in terms, and
item 4b records that **no DEC-002 ADR exists**. `ADR-0001` (accepted) is the only
binding instrument here, and what it binds is `ARCH-0002` P1.

**`DEC-003` has no owner.** This record's `bears_on` is `DEC-003` — *issuer /
subject identifiers on the wire*, whose options are "raw COSE key; COSE key
thumbprint; `did:key`; hash-uri (`sha256:…`); text KeyId" and whose one stated
obligation is "Must specify: canonical key bytes before hashing" (`ARCH-0001`
§7). **DEC-003 appears nowhere in `DECISIONS-0001`** — not in any tier, not in
the *What changed* table, not in the action lists. It is therefore unscheduled
and unassigned, while `R-O-01` makes `KeyId` mandatory on **every** signed
object and `ADR-0001`/`ARCH-0002` P1 make it the root of the naming scheme.
Nothing below closes it.

---

## What RFC 9679 computes, byte by byte

Stated first because the rest of this document depends on getting it exactly
right, and because two of our lanes have read it differently.

**The procedure (§3), three steps, MUST.** "The thumbprint of a COSE Key MUST be
computed as follows: 1. Construct a COSE_Key structure (see Section 7 of
[RFC9052]) containing only the required parameters representing the key as
described in Section 4 of this document. 2. Apply the deterministic encoding
described in Section 4.2.1 of [RFC8949] to the representation constructed in
step 1. 3. Hash the bytes produced in step 2 with a cryptographic hash function
H." And: "The SHA-256 hash algorithm MUST be supported; other algorithms MAY be
supported."

**What enters the digest (§4), per key type, not fixed.** §4's framing is
explicit: "Only the required parameters of a key's representation are used when
computing its COSE Key Thumbprint value", "The "kty" (label: 1) element MUST be
present for all key types, and the integer value specified in the IANA "COSE Key
Types" registry MUST be used. The tstr data type is not used with the "kty"
element", and "Many COSE Key parameters are specific to the chosen key type."

| §ref | key type | `kty` | required parameters, by label | defining spec cited |
|---|---|---|---|---|
| §4.1 | OKP | 1 | 1 `kty`, −1 `crv` (int), −2 `x` (bstr) | RFC 9053 §7.1 |
| §4.2 | EC2 | 2 | 1 `kty`, −1 `crv` (int), −2 `x` (bstr), −3 `y` (bstr) | RFC 9053 §7.1 |
| §4.3 | RSA | 3 | 1 `kty`, −1 `n` (bstr), −2 `e` (bstr) | **none** |
| §4.4 | Symmetric | 4 | 1 `kty`, −1 `k` (bstr) | **none** |
| §4.5 | HSS-LMS | 5 | 1 `kty`, −1 `pub` (bstr) | **none** |
| §4.6 | any other | — | *delegated*: "their defining specifications should be similarly consulted" | by reference |

**The order is derived, not stated.** §6 says the reduced structure is given
"with the minimum parameters in the correct order" and §5.1 calls the thumbprint
"a digest of the ordered essential parameters", but no section names an ordering
rule of its own. The order is whatever §3 step 2 produces. **[analysis]** For
every set in the table that is `kty` first and then the negative labels in
descending numeric order, because label 1 encodes as `0x01` and labels −1, −2,
−3 encode as `0x20`, `0x21`, `0x22`, and RFC 8949 §4.2.1 sorts by the bytewise
lexicographic order of the encoded keys. Verified against §6: re-encoding its
diagnostic notation under §4.2.1 sorting reproduces the printed hex exactly
(`examples/` `V-0012`).

**One pre-CBOR normalisation, for EC2 only (§4.2's Note).** "[RFC9052] supports
both compressed and uncompressed point representations. For interoperability,
implementations adhering to this specification MUST use the uncompressed point
representation. Therefore, the y-coordinate is expressed as a bstr. If an
implementation uses the compressed point representation, it MUST first convert
it to the uncompressed form for the purpose of thumbprint calculation."

**What is deliberately excluded (§5.1).** "Optional parameters of COSE Keys are
intentionally not included in the COSE Key Thumbprint computation so that their
absence or presence in the COSE Key does not alter the resulting value", and "By
excluding optional parameters, the COSE Key Thumbprint consistently refers to
the key itself, not to a key with additional attributes." §7 adds that "Key
identifiers are not included in the thumbprint calculation (similarly to other
optional parameters in the COSE_Key structure)."

**The one worked example (§6).** One EC2 P-256 key. 102 octets hashed, digest
`496bd8af…9da253ec`, which is also the `kid` in the same example, the `ckt` in
§5.6 and the base64url string in §5.7. **Every printed value in RFC 9679
descends from one key.** All six reproduce byte-for-byte from the key, with an
independently written encoder; see `examples/README.md`.

**What the digest does not contain.** No tag, no envelope, no `kid`, no
algorithm (for the five key types §4 enumerates), no hash-algorithm identifier,
no version of the parameter set, and no indication of which of those it is.

---

## What we adopt

**The construction itself, as the definition of `ARCH-0001` §4.1 `KeyId`.**
`KeyId` is "Digest of a canonical key encoding (algorithm of digest is
parameterized)"; `DEC-003` says "Must specify: canonical key bytes before
hashing". §3 is that specification, in three steps, and §4 is the list of which
bytes. It is the only document in our library that does this job for COSE keys.

**§5.1's exclusion rule, as the right rule.** A key identifier must not move when
a deployment adds an attribute. §5.1's argument is ours verbatim: "Different
application contexts may include various optional attributes in the COSE Key
structure. If these optional parameters were included in the thumbprint
calculation, the resulting values could differ for the same key depending on the
attributes present." Under `ARCH-0002` P1 a `KeyId` is a **namespace root**, so
an identifier that moves when an attribute appears relabels every type and every
name beneath it.

**§4.2's Note, and the discipline behind it.** Converting a compressed point
before encoding is a canonicalisation of the *key*, below the canonicalisation
of the *encoding*. §4.2 closing it for EC2 is the pattern to copy everywhere
else. `examples/` `V-0001` is the negative fixture.

**§5.2's multi-party clause, not its single-party one.** "when multiple parties
are involved in reproducing and comparing the COSE Key Thumbprint, it is crucial
that they know and use the same hash function to ensure consistent results."
Under P1 every party must *reproduce*, never merely match; see *What we reject*.

**§5.7's hash-algorithm-explicit form.** `urn:ietf:params:oauth:ckt:<hash>:<b64u>`,
with the hash identifier required to be a "Hash Name String" from the IANA
"Named Information Hash Algorithm Registry" and invalid identifiers something
"applications MUST detect and handle". This is where `ARCH-0001` §4.1's
"algorithm of digest is parameterized" actually gets carried. A bare 32-octet
`KeyId` carries it nowhere.

**§7's two warnings, as requirements on us.** That a thumbprint identifies
uniquely "only if a single unambiguous COSE Key representation for that key is
defined and used", and that "comparing thumbprint values is not a reliable means
of excluding the use of particular keys (or transformations thereof)". The second
bears directly on `R-O-02` (revocation still representable): a revocation keyed
on `KeyId` does not reach a transformation of the key.

---

## What we adapt, and how

**The thumbprint input is a COSE_Key, and under `ARCH-0002` P1 a COSE_Key is
interchange.** This is the adaptation everything else turns on. §3 step 1 says
"Construct a COSE_Key structure (see Section 7 of [RFC9052])" and §4 says the
`kty` value "MUST be" the integer from the IANA "COSE Key Types" registry. The
labels 1, −1, −2, −3 are IANA "COSE Key Type Parameters" and label 3 (`alg`) is
an IANA "COSE Key Common Parameter". `ADR-0001` is unambiguous about the class:
"CBOR tags and COSE header parameters are IANA allocated, so they are
interchange, not native", and `ARCH-0002` P1 extends it to "CBOR tags, COSE
header parameters and CWT claim keys". A COSE **Key** parameter is a fourth
registry that neither sentence names. See *Mapping*, cut A.

Two adaptations are available and they are not equivalent:

1. **Exempt key representations by name.** Option 5 declares that a key's byte
   representation uses COSE Key registry labels natively, as a bounded
   exception, and `ADR-0001`'s "Registry identifiers **may** appear at
   interchange boundaries" is widened to "and in key representations". Cheap to
   write, and it puts registry-allocated integers inside every native object's
   identity rather than at the export boundary. It is a widening of ADR-0001,
   not an application of it, and it has not been written.
2. **Treat the thumbprint as an export-boundary identifier only.** Then the
   native `KeyId` is something else, and under `R-O-01` every signed object has
   two issuer identities — one native, one in the COSE export — with no
   mechanism relating them. §5.5 is the precedent for how badly that goes.

**[analysis]** Choice 1 is the defensible one, and the reason is structural
rather than pragmatic. P1's argument is that a *type name* needs a principal
attached because two parties can independently coin the same label. A COSE Key
*parameter label* is not a coined name: it is a position in a fixed structure
whose referent is a mathematical component of a key. There is no namespace to
localise, because there is nothing a second party could mean by "label −2 of an
EC2 key" other than the x-coordinate. P1 displaces *vocabulary*, and a key's
parameter list is not vocabulary. This is our inference, ADR-0001 does not draw
the distinction, and it should be one paragraph of the DEC-002 ADR rather than a
silent practice.

**§5.2's "opaque value" posture — inverted.** "In many cases, only the party that
generates the key needs to be aware of the hash function used. For example, the
key producer might use the thumbprint value as a "kid" (key ID). In such
scenarios, the consumer of the "kid" treats it as an opaque value solely for key
selection." That is precisely what `ARCH-0002` P1 cannot have. If a `KeyId` is
the root of a name chain, every verifier resolving `(K, label)` must be able to
recompute `K` from key material it holds, not just string-match a value handed
to it. We take §5.2's second case ("multiple parties ... reproducing and
comparing") as the only case.

**§5.3, as the licence for non-COSE keys.** "Keys that are in other formats can
be represented as COSE Keys. The only prerequisites are that the COSE_Key
representation of the key be defined and the party creating the COSE Key
Thumbprint be in possession of the necessary key material." Useful for
`R-I-04`/`R-I-05` imports — an OpenPGP or X.509 key becomes a `KeyId` by being
expressed as a COSE_Key first. **[analysis]** Note what it does *not* license: a
different required-parameter set. §5.3 permits defining a *representation* of a
key in COSE; it does not permit defining a thumbprint over fewer parameters than
§4 requires for that `kty`.

**§5.4's SPKI analogy, taken as a portability argument.** "While logically
equivalent to a digest of the SPKI representation of the key, a COSE Key
Thumbprint is computed over the CBOR representation of that key rather than over
an ASN.1 representation of it." (SPKI here is X.509 Subject Public Key Info,
RFC 5280 §4.1.2.7 — **not** SPKI the certificate system of RFC 2693, which
`ARCH-0001` §3.1 also discusses. The collision of names is a reading hazard in
our own documents.) **[analysis]** The sentence concedes that the *construction*
is syntax-independent: digest a canonical representation of exactly the
essential components. That makes `DEC-003` answerable in the same shape under
any `DEC-002` option, which matters for sequencing — see cut D.

---

## What we reject, and why

**§4.4, thumbprints of symmetric keys.** §7 restricts them to the point of
withdrawal: "Developers MUST ensure that the symmetric key has sufficient
entropy", "Thumbprints MUST NOT be used with passwords or other low-entropy
secrets", "If a developer is unable to determine whether all symmetric keys used
in an application have sufficient entropy, then thumbprints of symmetric keys
MUST NOT be used", and "In most other deployment scenarios, it is more
appropriate to utilize a different naming scheme for key identifiers." Our
`Principal` is `Key | KeyId | Name | Threshold | Group` (`ARCH-0001` §4.1) and
every signed object has an issuer *key*; a symmetric secret is not a principal in
this model. Excluded, with §7 as the citation.

**§5.6 and §8's `ckt` confirmation method, as a native construct.** `ckt` is
confirmation key **5** in the IANA "CWT Confirmation Methods" registry, inside
the `cnf` claim of a CWT. `ARCH-0002` P1 names **CWT claim keys** explicitly as
"interchange, not native". So RFC 9679 has two halves and only one of them is a
candidate for the native model: §3–§4 (the computation) and §5.6/§8 (the CWT
carriage). **The document does not separate them and our ADR must.** The `ckt`
half belongs in the `ARCH-0001` §6 interchange matrix next to the existing
`COSE_Sign1 + CWT` row, which `R-I-01` already requires be written and which
`DECISIONS-0001` records as still missing.

**§8's registered description, as our hash policy.** The registry entry reads
"Confirmation Method Description: COSE Key SHA-256 Thumbprint". The registered
confirmation method is SHA-256 and nothing else — no agility, no parameter. Our
`KeyId` is parameterized by `ARCH-0001` §4.1, so we cannot adopt `ckt` as the
carrier of a parameterized digest. §5.7's URI form is the only carrier RFC 9679
supplies that says which hash ran.

**The implicit claim that a thumbprint is a key's identity.** §5.1 says the
thumbprint "consistently refers to the key itself, not to a key with additional
attributes". For OKP and EC2 that is true in the strong sense — the digest
covers `kty`, the curve and the coordinates, which is the key's *mathematical*
identity. For AKP it is not: the digest covers `kty`, `alg` and an opaque byte
string, which is an *algorithmic* identity. §5.1's sentence is written as though
one kind of identity were in play. Two are. See the next section.

---

## Mapping to our decisions

### 1. Is RFC 9679 fit to be `KeyId`? — **adapt, and not yet for the post-quantum path**

**Adopt the construction (§3, §5.1). Adapt the inputs (§3 step 1, §4). Do not
adopt it as the identity of a post-quantum principal until `ARCH-0002` has
decided whether an algorithm change is a principal change.**

Three things block a plain adoption. Two are ours to fix; the third is not.

| # | blocker | §ref | ours? |
|---|---|---|---|
| 1 | The thumbprint input is a registry-labelled COSE_Key; P1 calls that class interchange | §3 step 1, §4 | **ours** — one paragraph of the DEC-002 ADR (adaptation 1 above) |
| 2 | For RSA, Symmetric and HSS-LMS no defining specification is cited, so §7's "single unambiguous COSE Key representation" is undefined | §4.3, §4.4, §4.5, §7 | **ours** — pin the representation, or restrict to OKP/EC2 |
| 3 | For AKP — the only post-quantum key type — `alg` is inside the digest, and RFC 9679 offers no sanctioned subset | §4.6, RFC 9964 §3 and §6 | **not ours** |

What it buys if adopted: the one thing `DEC-003` demands ("canonical key bytes
before hashing"), a citation rather than an invention under `R-O-03`, a
reproducible 32-octet namespace root for P1, and a worked example that
reproduces. What it does not buy: anything about *carriage* — `DEC-003`'s other
options (`did:key`, `sha256:` hash-uri, text `KeyId`) are encodings *of* a
digest and are not alternatives to RFC 9679; they are alternatives to §5.7.
**[analysis]** So DEC-003 is really two decisions wearing one id: *what is
digested* (RFC 9679 answers it) and *how the digest is written down* (RFC 9679
§5.7 is one of four candidates). Separating them would let the first be settled
now and the second wait for DEC-002, and `ARCH-0001` §7 currently lists them as
one five-way choice.

### 2. The `alg`-inside-the-digest hazard — the sibling lane's reading, adjudicated

**The sibling lane's reading of RFC 9964 §6 is correct, and its locator
attribution needs one correction.** Verified against both sources.

**RFC 9964 §6 does fix the set.** Verbatim, bullets as printed:

> When computing the COSE Key Thumbprint as described in [RFC9679], the
> required parameters for AKPs are:
>
> *  "kty" (label: 1, data type: int, value: 7)
>
> *  "alg" (label: 3, data type: int, value: int)
>
> *  "pub" (label: -1, value: bstr)
>
> The COSE Key Thumbprint is produced according to the process described in
> Section 3 of [RFC9679].

So for AKP keys, `alg` is inside the digest. That much of the reading holds
exactly.

**[correction] RFC 9679 itself does not put `alg` in the digest, for any key
type it defines.** The reading as relayed — "RFC 9964 §6 defines AKP
thumbprints by reference to RFC 9679 §3 and fixes the required parameters" — is
right, but a reader may take from it that §3 or §4 is where `alg` enters. It is
not. §4.1–§4.5 enumerate five key types and **none** of them lists `alg`; §4
says only that `kty` "MUST be present for all key types". The clause that lets
`alg` in is **§4.6**: "As other key type values are defined, their defining
specifications should be similarly consulted to determine which parameters, in
addition to the "kty" element, are required." `alg` becomes required because
RFC 9964 §3 makes it so — "The alg JSON Web Key (JWK) parameter or COSE Key
Common parameter is REQUIRED for all AKP keys" — and §5.1 then pulls it in,
because §5.1 excludes only *optional* parameters. The chain is
§4.6 → RFC 9964 §3 → §5.1, not §4.

**[verified] The sharpest form of this, checked mechanically against the
cached source rather than argued: the string `alg` occurs ZERO times in
RFC 9679, and so does `AKP`.** Neither the parameter nor the key type that
makes it required is named anywhere in the document. So every statement of the
form "RFC 9679 puts `alg` in the thumbprint" is false as written; what is true
is that §4.6 delegates the required set, and a document RFC 9679 never cites
then puts `alg` in for a key type RFC 9679 never mentions. Two pass-1 agents of
this extraction disagreed on exactly this point and the disagreement was
settled against the source, not between them.

**The parameter set is per-key-type, open-ended, and extended by documents RFC
9679 has never seen.** That is the architectural fact, and it is sharper than
"`alg` is in". Proved in `examples/` with the document's own key: adding `alg`
(label 3, −7) to the §6 EC2 key leaves the thumbprint at `496bd8af…` unchanged
(`V-0007`), because §4.2 does not require it; the same label on an AKP key
changes the digest completely (`V-0004`/`V-0005`/`V-0006`). One parameter, one
label, one document, two opposite treatments.

**Why RFC 9964 is not being gratuitous.** AKP has no `crv`. RFC 9964 §3: "The
parameters for public and private information classes contain byte strings in a
format specified by the alg value." So `pub` is uninterpretable without `alg`,
and under §7's own test — uniqueness holds only if "a single unambiguous COSE
Key representation for that key is defined" — an AKP key *without* `alg` has no
unambiguous representation. **[analysis] RFC 9679 §7 is what forces `alg` in.
There is therefore no reading of RFC 9679 under which an `alg`-free AKP
thumbprint is conformant, and no argument available to us that RFC 9964 erred.**

**Does RFC 9679 offer a way out? One, and it runs the wrong direction.** §5.1's
last paragraph: "Different kinds of thumbprints could be defined by other
specifications that might include some or all additional COSE Key parameters, if
use cases arise where such different kinds of thumbprints would be useful." §7:
"If the inclusion of specific optional parameters in the thumbprint calculation
is important for a particular application, this specification would not be
suitable." **Both escape hatches are for supersets.** RFC 9679 contemplates a
thumbprint over *more* parameters and never one over *fewer*. A digest over
`(kty, pub)` alone would not be a COSE Key Thumbprint, would cite no document,
and under `R-O-03` ("Canonicalization algorithm for each concrete encoding SHALL
be cited, not invented silently") would be an invention.

**What it means for `ARCH-0002` P1, concretely.** P1 is accepted by `ADR-0001`,
so the key identifier is load-bearing for the whole naming scheme: a type is
`(defining key, local label)` and "Compound reference follows SDSI name chaining
exactly." If `KeyId` is an AKP thumbprint, then:

- **A parameter migration is a rename of everything.** ML-DSA-44 → ML-DSA-65 on
  the same `pub` is a new `KeyId` (`V-0004` vs `V-0005`), hence a new namespace,
  hence a new identity for every type that key defined and every name in its
  chain. Not a re-signing — a **renaming**. Existing statements do not become
  invalid; they become statements by a principal nobody can now name.
- **The same is true of an algorithm the key never changed.** `alg` is a property
  of a *use* of a key, not of the key material. AKP binds them, so one key
  usable under two algorithms is two principals.
- **The thumbprint cannot be the thing that survives the migration.** Whatever
  carries continuity across a parameter change has to be a relation between two
  principals, not an identity. `ARCH-0001` §4.2's `NameCert` is the construct
  that already does this — a stable `Name` under a stable naming key, resolving
  to whichever `KeyId` is current (`ARCH-0001` §4.3, "rewrite `Name` to `KeyId`
  via `NameCert` chains"). **[analysis]** So the honest statement is not "the
  thumbprint is unfit", it is **"a thumbprint is an identity and a name is a
  continuity, and P1 needs both."** A design that uses `KeyId` where it means
  "this key, now" and `Name` where it means "this principal, across changes" is
  unharmed by the hazard. A design that treats `KeyId` as the durable identifier
  is renamed by every parameter migration. Nothing in `ARCH-0001`,
  `ARCH-0002` or `ADR-0001` currently says which is intended, and `R-O-01`
  ("Every signed object SHALL have an issuer key that can be specified as
  `KeyId`") reads like the second.

**[correction] One cross-record claim narrowed.** This library's `rfc-9053`
summary says "anything naming a principal by `alg`-inclusive thumbprint
inherits this ambiguity for EdDSA keys", the ambiguity being that `alg` −8
covers both edwards25519 and edwards448. The antecedent is unmet: for OKP, §4.1
requires `kty`, **`crv`** and `x`, and does not require `alg`. No defined COSE
Key Thumbprint over an OKP key is `alg`-inclusive, and because `crv` is required
the thumbprint resolves the curve that `alg` −8 does not. The EdDSA ambiguity is
real at the algorithm layer and absent at the thumbprint layer.

### 3. Where this cuts against `MD-3`, and which options it favours

`MD-3` narrowed DEC-002 to option 5 — "CBOR data model, no IANA tags, COSE export
only; YAML as the human form" (`DECISIONS-0001` tier 1 item 2) — on 2026-09-28,
and is not an acceptance of it. Nine findings, each naming an option.

**Cut A — a registry option 5's own text never names, and only option 5 pays
for.** Option 5 excludes "reliance on the IANA CBOR Tags registry and no native
use of COSE header parameters" (proposal §3.3). Computing a thumbprint uses
**neither**. It uses the IANA "COSE **Key** Types" registry (§4, MUST) and the
"COSE Key Type Parameters" / "COSE Key Common Parameters" registries (the
labels). On the letter of option 5's exclusion list a COSE Key Thumbprint is
admissible; on `ARCH-0002` P1's broader "CBOR tags, COSE header parameters and
CWT claim keys" it is still not caught, because key parameters are a fourth
registry. **The tension is between option 5's text and P1's text, not between
either one and RFC 9679** — and it surfaces only at `DEC-003`, which is why
nobody has hit it. Under **option 2** ("CBOR + CDDL as canonical; COSE for
signed form") a COSE_Key is native and RFC 9679 drops in with zero adaptation.
**This is a cost option 5 pays that option 2 does not, and it is on the identity
path rather than the encoding path.** `MD-3` retains option 2 only as the
comparison fixture.

**Cut B — §5.5 is a direct, named cost to option 4, and to no other option.**
"The ckt of a COSE Key, as described in Section 7 of [RFC9052], and the jkt of a
JSON Web Key, as described in Section 4 of [RFC7517], are different even when the
underlying cryptographic key material is the same." And RFC 9679 declines to
bridge them: "This document does not register a JWT confirmation method [RFC7800]
for using "ckt" as a confirmation method for a JWT or a CWT confirmation method
[RFC8747] for using "jkt" as a confirmation method for a CWT." **Option 4** is
"Dual canonical (CBOR and JSON) with a documented bijection" (`ARCH-0001` §7). A
bijection at the *encoding* layer does not give one at the *identity* layer: the
same principal has two `KeyId`s, so under P1 two namespaces, and under `R-O-01`
every signed object has two issuer identities depending on which half of the
dual canon it was written in. There is no sanctioned bridge to document. **This
is the cleanest discriminating finding in the record and it eliminates option 4
on a ground DEC-002 never listed** — its drivers are "library availability,
SCITT alignment, SPKI fidelity, human debug", none of which is identity
stability.

**Cut C — the no-tags half of `MD-3` costs nothing here, and this document does
not discriminate option 2 from option 5.** §3 uses no CBOR tag at any step; the
thumbprint input is a bare map. §5.6's `ckt` sits in a CWT, which does carry
tags (RFC 8392 §6), but that is the interchange half. So on tags, options 2 and
5 score identically at `DEC-003`. Recorded because an extraction that only
confirms is not evidence (`docs/extraction.md`), and this is a place where the
narrowing's headline constraint turns out to be inert.

**Cut D — `DEC-003` does not wait on `DEC-002`, and the sequencing assumes it
does.** §5.4 concedes the construction is syntax-portable ("logically equivalent
to a digest of the SPKI representation of the key ... computed over the CBOR
representation of that key rather than over an ASN.1 representation of it").
**[analysis]** The same three-step shape is available under **option 1** (digest
a canonical S-expression key representation — RFC 9804 defines a canonical form
and our record scores it), **option 3** (that is RFC 7638's JWK Thumbprint, which
§5.5 says yields a *different* value) and **option 5**. What differs per option
is only which syntax the canonical key bytes are in. So the half of `DEC-003`
that `ARCH-0001` §7 flags as mandatory — "Must specify: canonical key bytes
before hashing" — is answerable now, in encoding-neutral form, exactly as `WP1`
is encoding-neutral by design. `DECISIONS-0001` has `DEC-003` nowhere and
treats everything as downstream of item 2; this is evidence that part of it is
not.

**Cut E — option 5's one strictly-stronger determinism rule is vacuous at
`DEC-003`.** The `rfc-8949` design notes record that option 5's native rule
(§4.2.1 with bytewise key sorting) is strictly stronger than COSE's own
RFC 9052 §9, which does not require sorting. RFC 9679 §3 step 2 requires §4.2.1,
so here they agree. But **checked mechanically**: every required-parameter label
in every key type of §4, plus AKP's, lies in −24..23 and encodes in one octet,
so §4.2.1's bytewise order and §4.2.3's length-first order coincide for every
thumbprint defined to date (`examples/README.md`). What §4.2.1 actually buys is
minimal-length `bstr` heads and minimal integer arguments. **Consequence for the
D5 package: `DEC-003` adds no rows to the fourteen-row determinism table.** It
adds the two rows in cut G instead, which are a different layer.

**Cut F — a canonicalisation option 5 has not specified, and it is not a CBOR
one.** The `canonical-encoding` topic's six conditions are all about the
serialisation layer. RFC 9679 needs one *below* it: §4.2's Note converts a
compressed point before any CBOR runs, and §4.3 leaves `n`'s leading octet
unpinned. Both are injectivity failures of the **key representation**, and
`examples/` `V-0001` and `V-0002`/`V-0003` show that both survive a perfectly
conforming §4.2.1 encoder. **[analysis] Call it condition (0): the key's own
byte representation must be pinned before any encoding rule applies.** It is
reachable by no determinism profile, it is not in the topic's six, and it fails
on the identity path — silently, as the topic says conditions (5) and (6) do.
Option 5 inherits it; so does every other option, because §5.4's portability
argument carries the problem along with the construction.

**Cut G — conditions (5) and (6) are vacuous for a COSE Key Thumbprint, and that
is good news nobody has recorded.** `DECISIONS-0001`'s standing note on item 2
says conditions (5) a canonical order for set-valued fields carried in arrays and
(6) a declared Unicode normalisation rule are "**reachable by no candidate and
stated in no document of ours.** They bite on the *identity* path, where
divergence fails silently rather than as a signature mismatch." Across all six
required-parameter sets that exist — §4.1–§4.5 and AKP's — a reduced COSE_Key
contains **no arrays and no text strings**: integer labels, integer and
byte-string values, nothing else, and §4 forecloses the one text possibility it
could have had, since "The tstr data type is not used with the "kty" element."
So as things stand the `KeyId` is the one identity-path construct in our design
where the two unreachable conditions do not apply. **[analysis]** It is not
guaranteed to stay that way: §4.6 delegates the set, so a future key type could
require a `tstr` or array-valued parameter and both conditions would arrive at
the identity path through a document we do not control. The remaining
identity-path hazard today is condition (0).

**Cut H — condition (3) is violated by construction, and the topic already says
so.** `R-O-05` (proposed) requires that "A verifier SHALL verify the signature
before decoding and SHALL NOT canonicalize input as part of verification", and
the topic notes that at an identifier "there are no received bytes to verify
verbatim. The digest IS produced by canonicalising." Recomputing a `KeyId` from a
received COSE_Key is canonicalising untrusted input — the exact DSSE objection
`ARCH-0001-PROPOSAL` §3.4 set out to answer. **[analysis]** The mitigation is
scope, not mechanism: the key material has been authenticated by the signature
it just verified, so recomputation runs on *verified* input. That only holds if
the verifier derives `KeyId` from the key it used to verify, never from a key
offered alongside an unverified statement. This is a rule option 5's profile
owes and nothing in our documents states.

**Cut I — the ADR must split RFC 9679 in two, and the RFC does not.** §3–§4 is a
`DEC-003` candidate; §5.6/§8's `ckt` and §5.7's `urn:ietf:params:oauth:ckt`
registration are interchange under P1 (CWT claim key; OAuth URN sub-namespace,
RFC 6755). Both halves are "RFC 9679" to a citation and only one is a candidate
for the native model. `R-I-01` requires the interchange half be documented as
lossy; `DECISIONS-0001` records the `ARCH-0001` §6 matrix row as unwritten.

### 4. `R-O-03` and what citing this buys

`R-O-03` is "Canonicalization algorithm for each concrete encoding SHALL be cited,
not invented silently" (`ARCH-0001` §5.3). RFC 9679 is a Standards Track RFC,
complete in itself for the computation, with one reproducible worked example and
exactly two normative dependencies for the encoding (RFC 8949 §4.2.1) and the
structure (RFC 9052 §7). Compare the topic's finding that citing RFC 8785 means
citing three artifacts. **What we would be citing is thin and clean. What we
would be adding is condition (0) and, for RSA/Symmetric/HSS-LMS, the whole key
representation** — and under `R-O-03` additions to a *silent* specification are a
cited profile, while modifications of a *prohibiting* one are not. §4.3 is silent
and §4.2's Note prohibits; so pinning RSA's leading octet is a profile, and
anything contradicting §4.2's uncompressed-point MUST is not.

---

## Open questions

Items this document cannot settle, with who must. **[beyond source]** marks ones
where this extraction had to reason past both RFC 9679 and our own documents.

1. **Is `KeyId` "this key, now" or "this principal, across changes"?** `R-O-01`
   and `ARCH-0002` P1 read as the second; §5.1 and RFC 9964 §6 only deliver the
   first. **[beyond source]** Until this is answered, no post-quantum migration
   plan can be written and no `NameCert`-as-continuity rule can be stated.
   *ARCH-0002 amendment — Paul.*
2. **Does the DEC-002 ADR exempt COSE Key parameter labels from `ARCH-0002` P1?**
   Cut A. Without an answer, `DEC-003` cannot select the thumbprint under option
   5, and `R-O-01` forces two issuer identities per object. *DEC-002 ADR (item
   4b) — Oct 28.*
3. **Should `DEC-003` be split into "what is digested" and "how it is written
   down"?** Cut D. The first is answerable now and encoding-neutral; the second
   is a four-way choice among §5.7's URI, `did:key`, `sha256:` hash-uri and a
   text `KeyId`. *ARCH-0001 v0.2.0.*
4. **Do we restrict `KeyId` to OKP and EC2 keys?** §4.3, §4.4 and §4.5 cite no
   defining specification, so §7's uniqueness precondition is unmet for RSA,
   Symmetric and HSS-LMS. Restricting is cheap now and expensive later. *DEC-003.*
5. **Condition (0) — where is the key representation pinned?** **[beyond
   source]** §4.2's Note is the only instance RFC 9679 supplies. Our profile
   needs the general rule, and the `canonical-encoding` topic's six conditions do
   not contain it. *Topic reopening or the DEC-002 ADR.*
6. **Which hash, and where is it carried?** `ARCH-0001` §4.1 parameterizes the
   digest algorithm and says nothing about carriage. §5.2 leaves the choice to
   the application; §8's `ckt` is SHA-256 only; §5.7's URI is the one explicit
   form. A bare 32-octet `KeyId` is algorithm-ambiguous. *DEC-003.*
7. **Does `R-O-02` survive §7's transformation caveat?** "comparing thumbprint
   values is not a reliable means of excluding the use of particular keys (or
   transformations thereof)". Under P1 a transformed key gets its own namespace,
   so no revocation keyed on `KeyId` reaches it (`examples/` `V-0013`).
   *ARCH-0001 §5.3 and the reduction work.*
8. **Is recomputation of `KeyId` restricted to verified key material?** Cut H.
   One sentence in option 5's profile. *DEC-002 ADR.*
9. **The `ARCH-0001` §6 interchange row for `ckt`.** `R-I-01` requires it;
   `DECISIONS-0001` records the `COSE_Sign1 + CWT` row as carrying neither the
   tag-stripping nor the key-sort divergence, and it now also owes the `ckt`
   confirmation method. *ARCH-0001 v0.2.0.*
10. **This record's `bears_on` is narrower than its analysis.** `record.yaml`
    names `DEC-003` only; the document bears on `DEC-002` (cuts A–I), `R-O-01`,
    `R-O-03`, `R-O-02` and `ARCH-0002` P1. Widening it is a metadata change this
    pass did not make. *Record maintainer.*

### Defects and ambiguities in RFC 9679 itself

Places where the source does not decide something it appears to decide, so an
implementer has to choose. Recorded rather than papered over.

11. **§6's full example is not deterministically encoded.** The printed hex for
    the five-parameter COSE_Key orders `kid` last, faithful to the diagnostic
    notation; RFC 8949 §4.2.1 sorts label 2 (`0x02`) second. Harmless for the
    thumbprint — §3 step 2 applies to the step-1 reduction, from which `kid` is
    already gone — but a determinism-dependent specification labels a
    non-deterministic encoding "the following CBOR encoding" and switches regime
    silently between two adjacent hex blocks. `examples/` `V-0011`; not in the
    errata as of `2026-09-22`. *Conformance-suite author.*
12. **§4.3, §4.4 and §4.5 cite no defining specification.** §4.1 and §4.2 both
    end "Further details are described in Section 7.1 of [RFC9053]"; the other
    three subsections end with the parameter list. For RSA that leaves `n`'s
    leading octet unpinned, which `examples/` `V-0002`/`V-0003` show is a real
    thumbprint divergence. *Open question 4.*
13. **No defined thumbprint discriminates §4.2.1 from §4.2.3 ordering.** Every
    required label lies in −24..23. An implementation can get §4.2.1's map
    sorting wrong and pass every value in this document, and that changes with
    the first COSE Key Type Parameter allocated outside the one-octet range,
    with nothing warning an implementer. *Conformance-suite author; also cut E.*
14. **§3 step 2 names §4.2.1 and §4.2.1 alone, which is narrower than
    "deterministic".** RFC 8949 §4.2.3 offers a second ordering and §4.2 says
    protocols "are free to define what they mean by a "deterministic format"".
    §3's reference is unambiguous, so this is not a defect — it is recorded
    because RFC 9052 §9, the COSE determinism section, does **not** require map
    key sorting, so RFC 9679 is strictly stricter than the COSE base it builds
    on and says nothing about the difference. An implementer who satisfies
    RFC 9052 §9 and assumes it covers RFC 9679 has not sorted.
