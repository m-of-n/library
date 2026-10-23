---
record: rfc-8747
kind: design-notes
title: "rfc-8747 — bearing on our design"
extracted: "2026-10-21"
reviewed_by: ""
---

# RFC 8747 — bearing on our design

**Section numbers are RFC 8747's** unless another document is named. Our own
documents are cited by id (`ARCH-0002 P1`, `DEC-002`, `DEC-003`, `R-O-01`,
`MD-3`, `ADR-0001`).

**Provenance of every quotation here, and the limits on it.** Quotations of RFC
8747 are cut from `.cache/rfc-8747.txt` by line range by script and are
**never retyped**; each carries the requirement id whose text it is, so a
reader can resolve it. Quotations of `m-of-n` documents — `ARCH-0001`,
`ARCH-0002`, `DEC-003`, `R-O-01` — are **not in this repository**. The wordings
used below are taken from this record's own `record.yaml` `bears_on` evidence
and from `docs/extraction.md`, both of which are in this worktree; **they
cannot be verified against `m-of-n` from here** and each should be re-checked
before it is relied on. `rfc-9741`'s cross-check pass set this convention and
this file follows it.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 lists **four**
options. *Option 5* exists only as proposed text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3, unmerged. `MD-3` (2026-09-28) **narrows**
`DEC-002` to option 5 — `docs/extraction.md` states it as *option 5: reduced
CBOR, no IANA tags, COSE as export only* — and **no `DEC-002` ADR exists**. A
narrowing is not an acceptance. Nothing below may be read as an accepted
encoding decision. Within this library option 1 is canonical S-expressions
(`records/ietf/rfc-9804`) and option 3 is JCS over JSON
(`records/ietf/rfc-8785`), per `topics/canonical-encoding.yaml`.

**What this extraction added beyond the summary, mechanically.** Five results,
all in `examples/vectors.yaml` and all re-derived at write time with a CBOR
codec, AES-128 and CCM written for this pass and gated on FIPS 197 C.1 and RFC
3610 vector 1 before use:

1. The §3.3 `COSE_Encrypt0` **decrypts and authenticates** under the key the
   document prints, and re-encrypting the recovered plaintext reproduces all
   48 printed octets.
2. **It does not reproduce from the COSE_Key the document prints.** The
   recovered plaintext holds the same three pairs in entry order `3, 1, -1`
   where §3.3 prints `1, 3, -1`. Source defect `rfc-8747#D-0001`.
3. The §3.2 point **is on P-256** — a real key, not filler.
4. The `cnf` value is **19 octets** with a `kid` against **77** with a
   `COSE_Key`: a ratio of **4.05**. §3.4's sentence about size pressure in
   constrained devices now has numbers behind it.
5. The §3.4 `kid` is **not** the SHA-256 of the §3.2 `COSE_Key` encoding,
   truncated or whole. The document suggests a hash of the public key and its
   own example does not do it.

---

## 1. What we adopt

**Nothing, as a format.** This is prior art, not something to conform to. We
hold it for what it establishes about identifiers, and `usefulness.reason` in
`record.yaml` already says so.

Two things are adopted as **arguments**:

- **The three-way enumeration itself.** "Table 1: Summary of the "cnf" Names, Keys, and Value Types" (rfc-8747#R-0036)
  Table 1's three rows are the complete set of ways a standards-track CWT may
  identify a proof-of-possession key: the key inline, the key encrypted, or a
  label. There is no fourth. That closes a design space for `DEC-003` rather
  than opening one.
- **The cost of the underived label, priced in the source's own words.** §3.4
  and §6 are the standards-track statement of what a bare label is not, and
  they are the reason this record was upgraded from `marginal`.

## 2. What we adapt, and how

**The size argument, now measured rather than asserted.** "In the world of constrained Internet of Things (IoT) devices, there is frequently a restriction on the size of Key IDs, either because of table constraints or a desire to keep message sizes small." (rfc-8747#R-0058)
The document states the pressure and gives no numbers. We have them: 19
octets against 77, from its own examples, measured with our own encoder. If
`R-O-01`'s `KeyId` is a digest, the digest's length is the whole of that cost,
and a 16-octet label is what this document's own example chose.

**The `cnf` shape, as a model we do not instantiate.** A map whose members name
alternative ways of identifying one key is a good shape. We would want exactly
one member and no registry. See cut D.

## 3. What we reject, and why

**The `cnf` claim itself.** We have no proof-of-possession step, and §3.5
declines to specify one anyway: "The means of communicating the nonce and the nature of its contents are intentionally not described in this specification, as different protocols will communicate this information in different ways." (rfc-8747#R-0064)
Carrying `cnf` would import a second IANA registry (cut D) for a mechanism the
document does not define.

**The underived `kid` as a `KeyId`.** This is the central rejection and the
source supplies the reason in three independent places:

- "The content of the "kid" value is application specific." (rfc-8747#R-0053)
- "In cases where the Key ID is not a cryptographic value derived from the key or where not all of the parties involved are validating the cryptographic derivation, implementers should expect collisions where different keys are assigned the same Key ID." (rfc-8747#R-0056)
- "Note that the value of a Key ID for a specific key is not necessarily the same for different parties." (rfc-8747#R-0059)

Note the register of all three: `application specific`, `should expect`, `not
necessarily the same`. **None of §3.4 carries a BCP 14 keyword** — measured,
zero — so a reader who takes §3.4 for a prohibition has misread it. It is
advice, and the advice is that the identifier has no root.

---

## 4. Mapping to our decisions

### 4.1 `DEC-003` — Table 1 is the option list, already drawn

`record.yaml` records `DEC-003` as choosing between a *raw COSE key* and a
*text KeyId* and as requiring that we *specify: canonical key bytes before
hashing*. Verified at source, and the verdict is sharper than the summary's:

| `DEC-003` option | RFC 8747's equivalent | what the document fixes |
|---|---|---|
| raw COSE key | `COSE_Key`, Confirmation Key 1 | rfc-8747#R-0033 — value type only; no required members are named here, only delegated to RFC 8152 |
| encrypted key | `Encrypted_COSE_Key`, Confirmation Key 2 | rfc-8747#R-0034 — and the tag is optional, so the encoding is not fixed either |
| text KeyId | `kid`, Confirmation Key 3 | rfc-8747#R-0035 — `binary string`, and **nothing else**: no length, no encoding, no derivation |

**What this document shows is left when you do not specify the canonical key
bytes.** §3.4 names the construction `DEC-003` must pin down and pins down none
of it: "For instance, some applications may choose to use a cryptographic hash of the public key value as the "kid" value." (rfc-8747#R-0054)
That sentence names a *cryptographic hash* of *the public key value* and
supplies no digest algorithm, no key encoding, no parameter subset and no
truncation rule. **And its own example does not follow it** — measured, the
§3.4 `kid` is not the SHA-256 of the §3.2 `COSE_Key` encoding. So the document
offers a derivation, omits every parameter needed to reproduce it, and does not
demonstrate it. That is the complete case for `DEC-003`'s mandatory clause, made
by a standards-track RFC against itself.

**One thing `DEC-003` should borrow and one it should not.** Borrow the
enumeration: three ways, no fourth. Do not borrow the registry (cut D).

### 4.2 `R-O-01` — uniqueness is an operational practice here, with a deliberate exception

`record.yaml` records `R-O-01` as *Every signed object SHALL have an issuer key
that can be specified as KeyId.* RFC 8747 is the standards-track precedent for
the second half of that, and it prices it.

**§6 makes uniqueness the issuer's discipline, not a property of the
identifier:** "When an issuer creates a CWT containing a Key ID claim, it needs to make sure that it does not issue another CWT with different claims containing the same Key ID within the lifetime of the CWTs, unless intentionally desired." (rfc-8747#R-0091)
with the failure named: "Failure to do so may allow one party to impersonate another party, with the potential to gain additional privileges." (rfc-8747#R-0092)

**The finding this extraction adds, and it is not in the summary.** That
sentence ends `unless intentionally desired`, and §6 then supplies the case:
"A case where such reuse of a Key ID would be intentional is when a presenter obtains a CWT with different claims (e.g., extended scope) for the same recipient but wants to continue using an existing security association (e.g., a DTLS session) bound to the key identified by the Key ID." (rfc-8747#R-0093)
So the document does not merely *tolerate* a Key ID collision. It names a case
in which reusing one is **correct**, and the reason is continuity of an existing
security association. `R-O-01`'s `KeyId` therefore inherits a precedent in which
non-uniqueness is sometimes the goal — which is a stronger reason to make our
`KeyId` derived than the collision sentence alone, because a derived identifier
makes the intentional case *impossible* rather than merely discouraged. If we
want the DTLS-continuity behaviour, a derived `KeyId` forbids it and something
else has to carry session continuity.

**And it stands in tension with §5 — but NOT in contradiction, which is what
this section claimed and pass 2 reversed.** §5 advises:
"Thus, for privacy reasons, it is recommended that different proof-of-possession keys be used when interacting with different parties." (rfc-8747#R-0085)
§5 is a rule about **different parties**; §6's intentional case is explicitly
"for the **same recipient**" (lines 420-421). Reusing one key across several
CWTs issued to one recipient is therefore fully consistent with a different key
per party, and the two statements do not conflict on the document's own terms.
The real tension is weaker and worth keeping: §6 blesses exactly the repeated
use of one key that makes it the correlation handle §5's rationale warns about
— but only within a single party's view, which is the view §5 does not govern.
An extraction that reported this as a flat contradiction would overstate the
document's incoherence, and one that reported only §6 would hand us half of the
tension.

### 4.3 `ARCH-0002 P1` — the contrast, verified at source

**It holds, exactly.** Both halves were resolved as contiguous substrings of
the whitespace-normalised source, with no relaxation:

- "Note that the value of a Key ID for a specific key is not necessarily the same for different parties." (rfc-8747#R-0059)
- "When sending a COSE encrypted message with a shared key, the Key ID may be different on both sides of the conversation, with the appropriate one being included in the message based on the recipient of the message." (rfc-8747#R-0060)

The second is the sharp one, and the wording survives checking: the Key ID *may
be different on both sides of the conversation*, with selection *based on the
recipient of the message*. So **a `kid` is a (party, local label) pair resolved
by table lookup.** `ARCH-0002 P1` makes an extension point a **(defining key,
local label) pair resolved by derivation**. Same arity, different first element,
and the difference is the whole of P1: a party-relative alias has an owner but
no cryptographic root, so nothing in the bytes disambiguates it. `ADR-0001`
rejected private-use ranges because no principal is attached; here a principal
*is* attached and it is a **lookup table rather than a key**, which is the same
defect reached from the other side.

**A second, independent way the `kid` namespace lacks a root — new here.**
"and MAY contain other COSE_Key members, including the "kid" (Key ID) member." (rfc-8747#R-0040)
So a `kid` may sit **inside** the `COSE_Key` under Confirmation Key 1 *and*
beside it as Confirmation Key 3, in the same `cnf` map. The document states no
precedence between them and does not require that they agree. Our derived CDDL
admits `{1: COSE_Key, 3: kid}` deliberately for that reason — §3.1 restricts
Confirmation Key 1 against 2 only — and `schema/README.md` records the
admission as the document's, not ours. Two places for one identifier with no
stated relation is a naming scheme with two roots, which is P1's failure mode
twice over.

---

## 5. `MD-3` — the required mapping, and where this document cuts against it

`MD-3` narrowed `DEC-002` to **option 5**: *reduced CBOR, no IANA tags, COSE as
export only* (`docs/extraction.md`). `docs/extraction.md` is also explicit that
an extraction which only confirms option 5 teaches the pending ADR nothing, so
§5.3 below is the part that matters.

### 5.1 Structure-by-structure mapping onto our statement fields

**Caveat on our side of this table.** Our statement's field names are in
`m-of-n`, not here; the rows below name the *role* a field plays (`R-O-01`'s
issuer `KeyId`) rather than asserting a field name this repository cannot
check.

| RFC 8747 structure | code point | maps onto | verdict |
|---|---|---|---|
| `cnf` claim | CWT claim key 8 | nothing | **not carried.** We have no proof-of-possession step; §3.5 does not define one either |
| `COSE_Key` | Confirmation Key 1 | an inline issuer key, were we to carry one | **not carried.** rfc-8747#R-0039 delegates the required members to RFC 8152, so adopting it imports RFC 8152's key registry |
| `Encrypted_COSE_Key` | Confirmation Key 2 | nothing | **not carried.** Needs a key the recipient already holds; we have no such channel |
| `kid` | Confirmation Key 3 | `R-O-01`'s issuer `KeyId` — the one real correspondence | **shape adopted, semantics rejected.** A byte string label is the right shape; *application specific* with foreseen collisions is not |
| unknown `cnf` members | any other label | nothing | **not carried.** rfc-8747#R-0025 makes the socket silent-drop |
| `iss`, `sub`, `aud`, `exp`, `iat` | RFC 8392's claim keys | RFC 8392's record, not this one | out of scope here |

### 5.2 The export mapping, if we ever needed one

Under option 5 — COSE as export only — the whole of RFC 8747 we would emit is
**one map entry**: claim key 8 carrying `{3: <our KeyId bytes>}`, which is
**19 octets** for a 16-octet label as §3.4's example sizes it. Three
consequences, each measured:

- **We would emit the `kid` form and never the other two.** `COSE_Key` costs
  **77** octets for the same job and imports RFC 8152's key parameter
  registry; `Encrypted_COSE_Key` needs a pre-shared key.
- **The tag question does not arise for the `kid` form.** It arises only under
  Confirmation Key 2. That is a point *for* the `kid` form under option 5's
  no-tags rule, and it is the only place in this document where option 5 is
  cleanly ahead.
- **Nothing in this document pins map order**, so our own profile must. See
  cut B — the document's own example is the evidence that this is not
  theoretical.

**What we deliberately do not carry:** the `cnf` claim itself; both key
representations; the extension socket; the `CWT Confirmation Methods` registry
dependence; and the proof-of-possession protocol, which does not exist to carry
 — "Likewise, the means of communicating the signed nonce is also not specified, as this is also protocol specific." (rfc-8747#R-0065)

### 5.3 Where the document cuts against `MD-3`

Six cuts, A–F. **Four** cost option 5 (A, B, C, D), one of which (A) also
corroborates a cut `rfc-8392` already found; **one** is a point in option 5's
favour (E); and **one** costs every option equally (F), recorded so the list is
not read as a ranking on every ground. The point in favour is recorded because
an extraction that only finds costs is as uninformative as one that only
confirms. (This said "Five cuts" and accounted for five, leaving F out of its
own enumeration while `README.md` correctly said six.)

#### Cut A — the optional tag means one `cnf` has two wire forms, and the registry does not choose. **Costs option 5 and option 3 alike; corroborates `rfc-8392`'s cut 3.**

"* Confirmation Method Name: "Encrypted_COSE_Key" * Confirmation Method Description: Encrypted COSE_Key * JWT Confirmation Method Name: "jwe" * Confirmation Key: 2 * Confirmation Value Type(s): COSE_Encrypt or COSE_Encrypt0 structure (with an optional corresponding COSE_Encrypt or COSE_Encrypt0 tag) * Change Controller: IESG * Specification Document(s): Section 3.3 of RFC 8747" (rfc-8747#R-0117)
and §3.3's worked example carries the `COSE_Encrypt0` **untagged**, as a bare
three-element array. Measured: **71 octets untagged against 72 tagged, a
difference of exactly 1 octet.** Three things follow.

First, the word `tag` occurs **exactly once** in the whole 683-line source —
line 544, inside that registration. Second, the `optional` in it is
**lower-case**, so it is not a BCP 14 OPTIONAL and the choice is not even
permissive-by-keyword; it is unstated. Third, **Table 1 omits the tag clause
altogether** (rfc-8747#R-0034), so the document's two
statements of the same value type do not agree.

The bearing on `MD-3`: option 5's *no IANA tags* is satisfied by the untagged
form, and the document's own example uses it — so option 5 is **congruent
here, not vindicated**. The cut is that congruence is **ours**, not the
format's: this registry admits both forms, so a receiver cannot reject a tagged
`cnf` on this document's authority. `rfc-8392` reached the same conclusion from
§5's escape hatch and called it cut 3 — *option 5's no-tags property is not
inherited*. **This is an independent second witness**, from a different
document and a different mechanism, and two independent witnesses is what makes
it a property of the CWT family rather than of one RFC.

#### Cut B — the document's own worked example does not reproduce, and the cause is map order alone. **Costs option 5 more than option 3, and option 1 not at all.**

This is the extraction's strongest finding and it is measured, not argued.
"The COSE_Key representation is used as the plaintext when encrypting the key." (rfc-8747#R-0047)

Decrypting the §3.3 ciphertext under the key, IV and `Enc_structure` the
document prints: the 8-octet CCM tag **verifies**, and re-encrypting the
recovered plaintext reproduces all **48** printed octets. But the recovered
plaintext is `a3030501042058206684523a…` — entry order **3, 1, -1** —
where §3.3 prints the same three pairs as `a3010403052058206684523a…` —
entry order **1, 3, -1**. Encrypting the printed order yields a ciphertext that
differs from octet 1 onward. The printed order **is** RFC 8949 §4.2.1
deterministic; the encrypted order is **not**.

Why this bears on `DEC-002` rather than being a mere erratum:

- **Option 5 pays the full cost.** Reduced CBOR with no canonical form stated
  must *construct* determinism by subtraction — `topics/canonical-encoding.yaml`
  says option 5 *must CONSTRUCT registry-freedom by subtraction* and the same
  shape applies to ordering. Under option 5 an order-only divergence is
  **invisible at the data-model layer**: both maps have the same three pairs and
  compare equal as maps. It becomes visible only where the bytes are signed or
  encrypted — which is exactly where this document's example broke.
- **Option 3 pays less.** JCS mandates a member ordering, so a JCS-shaped
  profile makes this class of divergence **unrepresentable** rather than merely
  detectable. The ordering `R-O-05` is recorded as forbidding is a different
  question; on *this* ground option 3 is ahead.
- **Option 1 does not pay it at all.** Canonical S-expressions have no maps.
  Order is content, so the two spellings are **different values**, not two
  encodings of one — the divergence surfaces as a value mismatch at the first
  comparison rather than at the first signature check.

So on *detectability of an order-only divergence*, this document ranks option 1
ahead of option 3 ahead of option 5 — the **reverse** of `MD-3`'s narrowing,
and on a ground `DEC-002` does not list. `rfc-9804`'s extraction put option 1
on the right side of all four grounds that withdraw option 3; this adds a
fifth ground, from a document in the CBOR family rather than outside it.

#### Cut C — RFC 8747 contributes nothing to the determinism story. **Costs option 5.**

Measured over the whole source: `canonical` **0**, `deterministic` **0**,
`encoding` **0**. The document names RFC 7049 and RFC 8152 and inherits
whatever they give. So the *reduced* in *reduced CBOR* cannot be sourced from
the CWT proof-of-possession layer; it has to be ours, written down by us, and
cut B is the measured consequence of its not being.

#### Cut D — carrying `cnf` would import a second IANA registry, one with no allocation tiers. **Costs option 5 specifically, because *no IANA tags* is option 5's own rationale.**

"This specification establishes the IANA "CWT Confirmation Methods" registry for CWT "cnf" member values." (rfc-8747#R-0107)
and the template defines the key space with no structure at all:
"Confirmation Key: CBOR map key value for the confirmation method." (rfc-8747#R-0112)

**No range, no integer/text split, no allocation tiers.** Contrast RFC 8392
§9.1.1, whose `Claim Key` field carries four allocation policy tiers. Under
`Specification Required` (rfc-8747#R-0097) a flat integer
space is governed by expert review alone, and under `ARCH-0002 P1` a label with
no principal attached is what `ADR-0001` rejected.

The bearing: option 5 removes dependence on the **CBOR Tags** registry. If an
export mapping carries `cnf`, option 5 **acquires** a dependence on the `CWT
Confirmation Methods` registry instead — a less structured registry than the
one it escaped. `topics/canonical-encoding.yaml` records that option 3 *is
registry-free by construction* and that option 1 *also wins that criterion*;
this moves option 5 further behind both on namespace governance, which is the
same direction `rfc-8392`'s cut 2 found.

**And it shows option 5 is narrower than it sounds.** *No IANA tags* does not
reach this dependency at all, because a confirmation-method registration is
**not a tag**. Option 5 excludes one registry-shaped dependency and says
nothing about the others — and §3.5 makes that concrete in the sharpest
possible way: the document withholds the proof-of-possession exchange
(rfc-8747#R-0064, rfc-8747#R-0065) and then
directs alternatives to IANA — "Applications making use of such alternate means are encouraged to register them in the IANA "CBOR Web Token (CWT) Confirmation Methods" registry established in Section 7.2." (rfc-8747#R-0067)
So the document's answer to *how do I actually prove possession?* is **register
your mechanism**: a registry for a **protocol step**, not for a tag or an
algorithm. That is the governance shape `ARCH-0002 P1` rejects, reached by a
route no other record in this lane takes.

**The actionable conclusion is not about `DEC-002` at all: do not carry
`cnf`.** Then the cut does not apply, and saying so is the point of recording
it.

#### Cut E — a point *for* option 5: the `kid` form is the cheapest and the only tag-free one. **Favours option 5.**

Of the three confirmation methods, exactly one involves no COSE structure, no
tag question and no second registry beyond its own label: Confirmation Key 3, a
byte string. Measured, it is **19 octets against 77** —
4.05 times smaller — and it is the form the document's own §3.4 example
uses. An option-5 export that needed to say *which key signed this* in a
CWT-shaped envelope would reach for exactly that member, and nothing in this
document stands in the way. Recorded because `docs/extraction.md` asks where a
source *supports* a different option as well as where it costs one, and because
four cuts against and none for would misrepresent the document.

#### Cut F — a definition by contrast is still a dependency on a lookup table. **Costs every option equally.**

§3.4's party-relative `kid` is **not** an argument for any `DEC-002` option
over another. A `kid` resolved by table lookup is exactly as opaque under
option 1 as under option 5: canonical S-expressions make the *label* a
determinate value and say nothing about what it denotes. Recorded so the cut
list is not read as a ranking of the options on every ground — cut B ranks
them on one specific ground (detectability of an order-only divergence) and
this one explicitly does not.

#### Convergence, not a cut — the exactly-one rule and ignore-unknown

"The "cnf" claim value MUST represent only a single proof-of- possession key." (rfc-8747#R-0028)
and "However, in the absence of such requirements, all confirmation members that are not understood by implementations MUST be ignored." (rfc-8747#R-0025)
sit well with **every** option on the table, and §1 above adopts the
enumeration they belong to. Named here so §5.3 is not read as six cuts with
nothing on the other side.

---

## 6. The canonical-encoding conditions

`topics/canonical-encoding.yaml` is in this repository, so this is checkable.
**This document supplies the mechanism for none of the six conditions.** It
defines no encoding rules and states nothing about determinism: measured over
all 683 lines, `canonical` **0**, `deterministic` **0**, `normaliz*` **0**,
`injective` **0**, `ordering` **0**. Its only structural obligation,
rfc-8747#R-0039, delegates to RFC 8152.

Recorded as a **negative** rather than omitted, because an extraction that
reports only what a document supplies leaves a reader unable to tell a gap
from an oversight. Cut B is what that gap costs, measured on the document's
own worked example.

---

## 7. Source defects

Recorded, not repaired, per `docs/extraction.md`.

| # | locator | what the document claims | what it prints |
|---|---|---|---|
| `D-0001` | §3.3 | the printed `COSE_Key` is the plaintext (rfc-8747#R-0047) | a ciphertext whose plaintext is the same map in entry order `3, 1, -1` rather than `1, 3, -1`. Authenticates; reproduces exactly from the order it carries. Arithmetic in `examples/vectors.yaml` |
| `D-0002` | §3.5 against §3.1 and §7.2 | one registry | **two spellings.** rfc-8747#R-0067 calls it `CBOR Web Token (CWT) Confirmation Methods`; rfc-8747#R-0026 and rfc-8747#R-0107 call it `CWT Confirmation Methods`. Three mentions, two names |
| `D-0003` | §3.1 Table 1 against §7.2.2 | one value type per method | **two wordings.** Table 1 says `COSE_Key` and `COSE_Encrypt or COSE_Encrypt0`; the registrations say `COSE_Key structure` and the same plus `(with an optional corresponding … tag)`. The tag clause exists in only one of the two |
| `D-0004` | §3.1 | — | the at-most-one rule is **lower-case** `may be present` (rfc-8747#R-0029), one sentence after a MUST. Under §2's *when, and only when, they appear in all capitals* it binds nobody. Arguably entailed by rfc-8747#R-0028, but not stated with force |
| `D-0005` | §3.3 line 269 | — | the protected-header annotation uses **backslash delimiters** inside a `/…/` comment. All **four** backslashes in the document are on that one line, and §2 cites only Appendix G of RFC 8610 |
| `D-0006` | line 1 | — | the cached `.txt` begins with a **UTF-8 byte-order mark** on a line of its own. Inside the hashed bytes, so inside `content.sha256` |

**And two defects were in this repository rather than in the source — both in
`summary.md`, both now FIXED by the cross-check pass.** First, it quoted
rfc-8747#R-0028 with the line-break hyphenation **healed**: `proof-of-possession`
where the source reads `proof-of-` / `possession` across lines 180-181, so the
quotation resolved only under a source-side hyphen heal. Second, it wrote that
collisions were to be `"expected"`, where §3.4 reads "implementers should
**expect** collisions" — an inflection placed inside quote marks, and
`expected` occurs **0** times in the document. The second was found by a
short-span pass over 6–24 character spans, which the ≥25-character whole-span
audit cannot see. Both had been reported twice without being decided; the
hyphenation now reads the way the source reads it with the break named, and the
collision clause now quotes the document's own words. `requirements.yaml` R-0028
and R-0056 carry both sentences unaltered, as they always did.

A third defect in this repository, found by the cross-check pass and also
fixed: **`summary.md`'s "Artifacts in this record" still said "No `distilled/`,
deliberately"** — written 2026-10-20, before the extraction, and left standing
through both later passes while ten artifacts were added beside it. The primary
human- and AI-facing document said the record had no distilled artifacts.

The claim that stood here, that all **seven** `bears_on` quotations in
`record.yaml` resolved **exact**, was withdrawn by pass 2: the comment block
holds **nine** quotations, four of them m-of-n and unverifiable from this
repository. Of the five bearing on RFC 8747, three were exact and two were
declared ellipses; the cross-check pass removed both ellipses, so **all five
now resolve exact**. See `README.md`, known gaps 3 and 4.

---

## 8. Open questions

1. **Does a derived `KeyId` forbid something we want?** §6 names a case where
   reusing a Key ID across CWTs is *intentionally desired* —
   rfc-8747#R-0093 — for continuity of an existing security
   association. A derived `KeyId` makes that impossible. *`R-O-01`'s owner, or
   the `DEC-003` ADR.*
2. **How do §5 and §6 get reconciled in our design?** §5 advises a fresh key
   per party (rfc-8747#R-0085); §6 blesses one key across
   CWTs **for the same recipient**. Both lower-case. They do not contradict —
   §5 is cross-party and §6's case is same-party (see §4.2) — so what we owe is
   a positive choice about correlatability within one party's view, not the
   resolution of a conflict. *`DEC-003`.*
3. **If a `KeyId` is derived, what are the canonical key bytes?** §3.4 is the
   demonstration that naming the construction is not enough —
   rfc-8747#R-0054 names a hash of the public key and supplies
   no algorithm, encoding, parameter subset or truncation, and the document's own
   example does not satisfy it. *`DEC-003`'s mandatory clause.*
4. **Does our profile pin map order, and where is that written?** Cut B is the
   measured cost of not pinning it, in a standards-track RFC. *`DEC-002` ADR,
   one sentence in option 5's profile.*
5. **Two places for one identifier: which wins?** rfc-8747#R-0040
   permits a `kid` inside a `COSE_Key` while Confirmation Key 3 sits beside it,
   with no stated precedence. If we ever carry both, we must say. *`DEC-003`.*
6. **Is RFC 9679's `ckt` a fourth row of Table 1 or a different kind of thing?**
   `record.yaml`'s `relations` note records that RFC 9679 §8 registers `ckt` at
   Confirmation Key 5 in the registry *this* document establishes. RFC 8747
   predates it and says nothing about it, so this question is RFC 9679's record
   to answer; noted here because Table 1's closure claim in §1 above is a claim
   about **this document**, not about the registry's eventual contents.

---

## 9. What passes 2 and 3 should attack

`hazards.md` is explicit that pass 1's self-nominated priorities are usually
clean and that every serious defect a verify pass finds is in something pass 1
did **not** nominate. So work this list **and** choose your own targets.

1. **The `stated` / `inferred` split — ADJUDICATED by pass 2 and now 110 / 8.**
   This read 111 / 7 and said the pass had leaned toward `stated` because
   *contiguous* and *literally stated* are different claims. Pass 2 found the
   deeper problem: the criterion was undeclared and applied two ways. Six
   entries carry a `force carried by '<non-keyword phrase>'` marker in their
   `field` — the record's own sign that the force is the extraction's reading —
   and three were `inferred` while three were `stated`. And SKILL.md's wording
   ("anything not literally stated") cannot be the criterion here, because all
   118 texts are verbatim contiguous substrings, which would make the split
   118 / 0. `requirements.yaml` now **declares** the criterion it actually
   uses — asserted obligation or binding definition versus description,
   analogy, equivalence or framing — and applying it consistently moved
   rfc-8747#R-0009 to `inferred`, with
   rfc-8747#R-0011 and
   rfc-8747#R-0076 deliberately left `stated`.
2. **rfc-8747#R-0038 and rfc-8747#R-0052 are
   byte-identical** — the record's only duplicate-text group and therefore the
   whole attack surface for an id that resolves to a real but wrong statement.
   `bin/check-id-joins --surface` finds exactly this pair and nothing else.
3. **rfc-8747#R-0040 begins with a conjunction** — it
   is the second half of a mid-sentence split off rfc-8747#R-0039.
   It carries the MAY, so the split is defensible, but a fragment opening with
   *and* is one step from the truncation class.
4. **The protocol artifact is PRODUCED, not N/A — SUSTAINED by the cross-check
   pass.** This is the one artifact-level judgement here a reasonable verifier
   could reverse. Test the inference, not the word counts: of the lane's **25**
   FX-1 records, **18** declare this artifact N/A and **7** produce it — *this
   record among the seven*, so six others do. `rfc-9679` is one of the 18, and
   it declared N/A by pointing at *this* document, which is why deferring again
   was not available. (This said "18 … N/A, **8** produce it", which is 26 of
   25; counted from `distillation.not_applicable` and `distillation.artifacts`
   across `records/*/*/record.yaml` for topics `cbor-implementation` and
   `canonical-encoding` at `standard: FX-1`, it is 18 and 7. The same wrong
   figure stood in `record.yaml`'s pass-1 note.)
5. **The CCM result is this pass's own claim.** The AES and CCM were written
   for this pass and gated on FIPS 197 C.1 and RFC 3610 vector 1, but defect
   `D-0001` rests on them. Re-derive it independently rather than confirming
   it; the CBOR arithmetic, the 48 = 40 + 8 and the determinism of each entry
   order are checkable without any cipher at all.
6. **`bin/check-id-joins --quote-join` examined fewer pairs than this record
   carries, and this entry was itself two figures out of step with
   `README.md`.** It said 22 of 35 where `README.md` said 25 of 38 — one
   record, one check, two denominators and two numerators, which is
   `hazards.md` §6 inside a single pass. The check has since been fixed and
   both files re-measured from it: **31 examined, 31 carried, 0 to read**, with
   the seven remaining exclusions named in `README.md`, known gap 1. The
   warning that stood here still stands in general — a zero finding is not
   coverage unless the examined count says what was looked at.
7. **Counts stated in a file other than the one they describe.** `README.md`
   and `record.yaml` both count these artifacts. Every figure in them was read
   off the files at write time, but that is exactly the fossil class
   (`hazards.md` §6) and it is where this pass is most likely to have left
   something stale.
