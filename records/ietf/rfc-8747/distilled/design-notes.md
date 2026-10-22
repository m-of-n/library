---
schema: "library-doc/v1"
id: rfc-8747-design-notes
record: rfc-8747
type: design-notes
updated: "2026-10-21"
---

# RFC 8747 — design notes

## 0. Provenance and what can be checked here

Every quotation of RFC 8747 below was cut from `.cache/rfc-8747.txt` by line
range by script and verified as a contiguous substring of the
whitespace-normalised source; none was retyped. The source is 683
newline-delimited lines with **zero** form feeds, so there is no page
decoration and no running header to exclude.

Quotations of `mofn` documents — `ARCH-0001`, `ARCH-0002`, `DEC-002`,
`DEC-003`, `MD-3`, `R-O-01` — are marked
**[unverifiable from this repository]**. This library is standalone by design:
`CLAUDE.md` says it is *"independently cloneable, forkable, and citable by
projects that are not this one."* The only statement of MD-3 that **is** in
this repository is `docs/extraction.md`, and it is quoted from there.

Quotations of sibling records resolve against those records' own files, with
this record's files excluded from the corpus — the rule `hazards.md` gained
after a sibling's wrong quotation resolved against its own copy of the same
wrong quotation.

## 1. What this document is, in one line

It defines **one claim** — `cnf`, CWT claim key 8 — and three ways to put a
proof-of-possession key inside it. That is the whole of its wire contribution.
Its value to us is almost entirely in what it says a **Key ID is not**.

## 2. What we adopt

**A-1. The three-way enumeration of how a key may be identified.** §3.1's
Table 1 is exhaustive and small: `COSE_Key` (1), `Encrypted_COSE_Key` (2),
`kid` (3). That is `DEC-003`'s own option list — raw key against identifier —
already drawn on the standards track, a decade of deployment ahead of us.
Adopted as the shape of the decision, not as a format.

**A-2. "Exactly one."** §3.1: *"The "cnf" claim value MUST represent only a
single proof-of- possession key."* One of the document's four MUSTs, and the
right default for a statement that binds one issuer key. Adopted.

> **The break in that quotation is the source's and is NOT healed.** Source
> lines 180–181 cut `proof-of-possession` **at the hyphen**, so the
> whitespace-normalised source reads `proof-of- possession` and
> `requirements.yaml`'s `R-0028` carries it that way. This note first quoted it
> healed, which would have made the quoted token occur nowhere in RFC 8747 —
> the defect `hazards.md` §2 names, caught here by the pass that wrote it. It
> is the only hyphenation break in the document's eight keyword-bearing
> sentences.

**A-3. Ignore-unknown as the consumer default.** §3.1: *"in the absence of such
requirements, all confirmation members that are not understood by
implementations MUST be ignored."* The only MUST here that binds a recipient.
Adopted as the extension-tolerance rule for our own confirmation-shaped maps.

## 3. What we adapt

**AD-1. `cnf` is a claim, ours would be a field.** Nothing to carry across but
the cardinality rule in A-2.

**AD-2. The registry is the extension point, and we do not want one.** §3.1
says other specifications *"can register other members used for confirmation"*
and §3.5 *encourages* registering alternative proof mechanisms in the registry
§7.2 establishes. Adapted by refusal: see §7.3 below.

## 4. What we reject

**RJ-1. A bare `kid` as an identifier we would rely on.** §3.4 and §6 are the
reasons, and they are the reason this record was upgraded from `marginal`.
Set out in §5.

**RJ-2. The optional tag.** §7.2.2 registers `Encrypted_COSE_Key` as
*"COSE_Encrypt or COSE_Encrypt0 structure (with an optional corresponding
COSE_Encrypt or COSE_Encrypt0 tag)"*. Rejected for our own use: an optional tag
is two encodings of one value. See §7.1.

## 5. The finding: what a Key ID is NOT

This is what the record is held for, and all four limbs are the document's own
words.

**5.1 Not derived.** §3.4: *"The content of the "kid" value is application
specific."* It then names a derivation as one option among others — *"some
applications may choose to use a cryptographic hash of the public key value as
the "kid" value"* — and specifies **no key encoding, no parameter subset and no
digest algorithm**. `DEC-003` must *"specify: canonical key bytes before
hashing"* **[unverifiable from this repository]**; this is the standards-track
document that shows exactly what is left when you do not: a name with a
suggested construction and no way to check it.

**5.2 Not unique, and the collision is foreseen.** §3.4: *"In cases where the
Key ID is not a cryptographic value derived from the key or where not all of
the parties involved are validating the cryptographic derivation, implementers
should expect collisions where different keys are assigned the same Key ID."*
Lower case *should expect* — and that is itself the finding. The failure is
predicted in the text and **nothing is mandated against it**. The follow-up is
advice too: recipients *"should be prepared to handle such situations"*.

**5.3 Uniqueness is operational, not structural.** §6 moves the burden to the
issuer: it *"needs to make sure that it does not issue another CWT with
different claims containing the same Key ID within the lifetime of the CWTs"*,
because *"Failure to do so may allow one party to impersonate another party,
with the potential to gain additional privileges."* So impersonation is the
stated consequence, and the defence is an issuer's discipline over time rather
than a property of the identifier. `R-O-01` requires every signed object to
have an issuer key *specifiable as a KeyId* **[unverifiable from this
repository]** — this document prices the underived alternative, and the price
is paid in operational care that nothing can audit.

**5.4 Not even the same for both parties — the sharpest limb.** §3.4:

> Note that the value of a Key ID for a specific key is not necessarily the
> same for different parties.  When sending a COSE encrypted message with a
> shared key, the Key ID may be different on both sides of the conversation,
> with the appropriate one being included in the message based on the recipient
> of the message.

**[analysis]** A `kid` is therefore a **(party, local label)** pair resolved by
table lookup. `ARCH-0002 P1` makes an extension point a **(defining key, local
label)** pair resolved by derivation **[unverifiable from this repository]**.
Same shape, different first element, and the difference is the whole of P1: a
party-relative alias has an owner but no cryptographic root, so nothing in the
bytes disambiguates it. `ADR-0001` rejected private-use ranges because no
principal is attached; here a principal of sorts **is** attached and it still
does not help, because the principal is a lookup table rather than a key. This
is "escape from a registry, not a namespace" arrived at from the other side —
and it is a **definition by contrast**, which is why this record earns its
place even though we adopt almost nothing from it.

## 6. The canonical-encoding conditions

`topics/canonical-encoding.yaml` is in this repository, so this is checkable.
This document supplies the mechanism for **none** of the six conditions. It
defines no encoding rules, states nothing about determinism — `canonical`,
`deterministic` and `normaliz*` each occur **zero** times in 683 lines — and
its only structural obligation delegates to RFC 8152. Recorded as a negative
rather than omitted, because an extraction that reports only what a document
supplies leaves the reader unable to tell a gap from an oversight.

## 7. Where it cuts against MD-3

`docs/extraction.md` states MD-3 as *"option 5: reduced CBOR, no IANA tags,
COSE as export only"* — the only in-repository statement of the gloss, and the
wording used here.

### 7.1 Cut 1 — an OPTIONAL tag is two encodings of one value. Costs option 5.

§7.2.2 registers `Encrypted_COSE_Key`'s value type with *"an optional
corresponding COSE_Encrypt or COSE_Encrypt0 tag"*, and §3.3's worked example
carries the COSE_Encrypt0 **untagged**. Both are conforming.

This bounds a live finding rather than adding one: `rfc-9964`'s Cut A found
every COSE example in RFC 9964 tagged 18, with the untagged form never
printed. Both hold — the tag is customary at top level and explicitly optional
when nested, which is where an export mapping would put one.

**The cost is second-order but real.** Option 5 wants no IANA tags; this
registry entry makes the tag optional rather than absent, so a deterministic
profile has to **choose**, and the registry does not choose for it. An
export mapping that nests a `cnf` must state which form it emits. Nothing in
RFC 8747 says.

### 7.2 Cut 2 — the extension point is a registry, and it is the registry for the half of the protocol that is missing. Costs option 5 and option 3.

§3.5 withholds the nonce exchange (`R-0064`, `R-0065`) and then directs
alternatives to IANA: applications using other means of proving possession are
*"encouraged to register them"* in the registry §7.2 establishes.

**[analysis]** So the document's answer to "how do I actually prove
possession?" is *register your mechanism*. That is the governance shape
`ARCH-0002 P1` rejects, reached by a route the other records in this lane do
not take: not a tag registry or an algorithm registry, but a registry for a
**protocol step**. Option 5's "no IANA tags" does not reach this, because a
confirmation-method registration is not a tag — which is worth saying plainly,
since it means option 5 is **narrower than it sounds**: it excludes one
registry-shaped dependency and says nothing about the others.

### 7.3 Cut 3 — a definition by contrast is still a dependency on a lookup table. Costs every option equally.

§3.4's party-relative `kid` (§5.4) is not an argument for any DEC-002 option
over another: a `kid` resolved by table lookup is as opaque under option 1 as
under option 5. Recorded so the cut list is not read as uniformly favouring
option 5 — `docs/extraction.md` is explicit that an extraction mapping cleanly
onto option 5 and reporting nothing else *"has confirmed a choice rather than
tested it"*.

### 7.4 Convergence, not a cut — "exactly one" and ignore-unknown

A-2 and A-3 sit well with every option on the table and are adopted in §2.
Named here so the section is not read as four cuts.

## 8. Open questions

1. **Does our KeyId have to answer §3.4's party-relativity at all?** If a
   KeyId is derived, both parties compute the same one and the problem
   dissolves. Worth stating in the `DEC-003` ADR as a *property we gain*,
   not merely a cost we avoid.
2. **Which encoding of a nested `Encrypted_COSE_Key` would an export mapping
   emit?** §7.1's cut leaves it open and so do we.
3. **RFC 7800 is held but not cached.** §3.2 calls `cnf` *"equivalent to"* the
   JWT original; the equivalence is checkable only against a document whose
   bytes this library does not hold. `records/ietf/rfc-7800` exists; a
   `bin/fetch-source` would close it.
4. **The registry §7.2 establishes is where `rfc-9679`'s `ckt` lands.** RFC
   9679 §8 registers COSE Key Thumbprint as Confirmation Key 5 in *this*
   registry, so the thumbprint our `DEC-003` lane is weighing is a member of
   this document's `cnf` map. That edge is in `relations.see_also` and is the
   reason this record is not merely prior art.

## 9. Source defects

**None found.** Pass 1 looked for the classes this lane has met — a size or
count that does not reproduce, a table whose rows do not cover their space, a
cross-reference to the wrong section, an example whose bytes contradict its
caption. The two §3.4/§3.3 examples are CBOR diagnostic notation with no
octet counts to check, Table 1's three rows match §7.2.2's three registrations
in name, key and value type, and every internal cross-reference resolves
(§3.1→§7.2, §3.3→§3.3, §3.4→§6, §3.5→§7.2). Reported as a negative because
"no defects found" and "not looked for" must be distinguishable.

## 10. What passes 2 and 3 should attack

1. **The 111 `stated` / 7 `inferred` split.** Unusually high for this lane —
   most records are overwhelmingly `inferred`. Each `stated` entry claims its
   text is literally the document's. All 118 texts are verified contiguous, but
   *contiguous* and *stated rather than inferred* are different claims.
2. **R-0038 and R-0052 each occur TWICE in the source.** A duplicate-text
   group: the one place a wrong id still matches the quoted words. Neither is
   cited from any artifact yet; check before any pass wires them.
3. **R-0040 begins "and MAY contain other COSE_Key members"** — a mid-sentence
   split off R-0039. It carries the MAY, so the split is defensible, but a
   fragment beginning with a conjunction is one step from the truncation class.
4. **My own counts in `messages.yaml`'s `coverage`.** I wrote 21 ids and 11
   fields, measured 17 and 8, and corrected them — so the field has already
   been wrong once. Recount rather than carry.
5. **The protocol artifact is PRODUCED, not N/A**, on the ground that three
   roles are named while §3.5 withholds the exchange. Test the inference, not
   the counts: the five sibling records that declare it N/A do so on grounds
   this one does not share.
