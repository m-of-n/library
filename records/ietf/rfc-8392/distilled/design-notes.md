---
record: rfc-8392
kind: design-notes
title: "rfc-8392 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§3.1.1`) are RFC 8392's. Our own documents are cited by id (`ARCH-0002 P1`,
`DEC-003`, `MD-3`, `R-O-01`). Three markers distinguish voices, following
`records/ietf/rfc-8949/distilled/design-notes.md` and `rfc-9741`'s:

- unmarked prose reports **RFC 8392** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption, or a claim in one of our own
  artifacts, that the source does not support.

**Which quotations below are checkable here, and which are not.** This library
is **standalone by design** — independently cloneable and citable by projects
that are not `mofn` (`CLAUDE.md`). The `mofn` documents this file cites are
**not present in this repository**: `ARCH-0001`, `ARCH-0001-PROPOSAL-v0.2.0`,
`ARCH-0002` (P1–P5), `ADR-0001`, `MD-3`, `DECISIONS-0001`, and the `R-O-*` /
`R-I-*` / `R-M-*` rules. **Every quotation of those documents here is
reproduced from the extracting agent's context and cannot be verified from this
repository.** Treat each as a citation to be re-checked against `mofn` before it
is relied on. `rfc-9741`'s cross-check pass set this convention and this file
follows it.

What *is* checkable here, and was: `docs/extraction.md`'s statement of MD-3
(*"option 5: reduced CBOR, no IANA tags, COSE as export only"*),
`topics/canonical-encoding.yaml`'s six conditions and its identification of
DEC-002 options 1 and 3, `records/ietf/rfc-9052`'s and `records/ietf/rfc-9053`'s
artifacts, and `records/ietf/rfc-9679`'s §5.7 finding. Each is in this worktree.

**How quotations of the library's own artifacts are normalised here.** A
quotation of another record's `design-notes.md` or `summary.md` is quoted from
its **rendered** text: markdown emphasis (`*`, `**`) and code markers
(backticks) are dropped, because they are formatting rather than words.
Quotations of the **source** are not normalised beyond whitespace, are cut from
`.cache/` by line range by script, and are **never elided** — where a sentence
spans a line break the break is declared and the obligation-bearing half is
quoted. This pass's own quote audit found four defects in its own prose under
those rules, and each is recorded in place where it occurred rather than edited
away.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged. `MD-3`
(2026-09-28) *narrows* DEC-002 to option 5. **No DEC-002 ADR has been
written**, and `DECISIONS-0001` item 2 says so in terms: *"a narrowing is not
an acceptance"*. Nothing below may be read as an accepted encoding decision.
Within this library, option 1 is canonical S-expressions (`records/ietf/rfc-9804`)
and option 3 is JCS over JSON (`records/ietf/rfc-8785`); both identifications
come from `topics/canonical-encoding.yaml`, which is here.

**What this extraction added beyond the summary, mechanically.** Five
cryptographic results and three censuses, all in `examples/vectors.yaml`: the
A.3 signature **verifies**, the A.4 and A.7 MAC tags **reproduce**, A.5 and A.6
**decrypt with valid CCM tags**, A.6's plaintext is the A.3 object byte for
byte, and the A.2.3 private key is **the** private key for its printed public
point. ECDSA P-256, HMAC-SHA-256 and AES-128-CCM were implemented for this pass
over `hashlib` alone, with the AES core gated on FIPS 197 C.1 first. Two of the
summary's claims are narrowed as a result and one source defect is new.

---

## 1. What this record decides, in one paragraph

`ARCH-0001` §6 carries "COSE_Sign1 + CWT" as an interchange row and asks that
`iss`/`sub` align with the `KeyId` profile. **They cannot, and the obstacle is a
type rather than a policy.** §3.1.1's value is a StringOrURI, which §2 defines
as a CBOR **text** string; `DEC-003`'s leading `KeyId` candidate — `rfc-9679`'s
COSE Key Thumbprint — is a bare **byte** string. Choosing the CWT envelope
therefore closes a question `rfc-9679` left open: it **forces the §5.7 URI
form**, `urn:ietf:params:oauth:ckt:<hash>:<value>`, and with it pins the hash
function in the wire format rather than in a side agreement. That is the one
decision a reviewer should take from this record, and §2 below is its evidence.

---

## 2. DEC-003 — a thumbprint cannot be an `iss`, and the type is why

**CONFIRMED against the source.** §2's StringOrURI definition, verbatim:

> The "StringOrURI" term in this specification has the same meaning and processing rules as the JWT "StringOrURI" term defined in Section 2 of [RFC7519], except that it is represented as a CBOR text string instead of a JSON text string.

§3.1.1 and §3.1.2 both take that type:

> The "iss" (issuer) claim has the same meaning and processing rules as the "iss" claim defined in Section 4.1.1 of [RFC7519], except that the value is a StringOrURI, as defined in Section 2 of this specification.

Three slots exist in a CWT and none is free for a bare digest.

| slot | CBOR type | locator | verdict |
|---|---|---|---|
| `iss` 1, `sub` 2 | **tstr** | §3.1.1, §3.1.2, §4 Table 1 | a 32-octet digest does not fit; it must be encoded as text |
| `cti` 7 | **bstr** | §3.1.7 | fits exactly, **wrong meaning** — see below |
| COSE `kid` 4 | bstr | RFC 9052 §3.1, not this document | fits, and is a hint by normative construction |

`cti` is the only byte-string claim the document defines, and §3.1.7 says what
it means:

> The "cti" (CWT ID) claim has the same meaning and processing rules as the "jti" claim defined in Section 4.1.7 of [RFC7519], except that the value is a byte string.

§9.1.2's registry entry for it records `JWT Claim Name: jti`. So `cti` is an
identifier **of the token**, not of a key, and putting a `KeyId` there would be
a silent reinterpretation of a registered claim — exactly what `R-O-03` exists
to prevent.

**[analysis] The consequence for `DEC-003`, stated as a choice rather than a
discovery.** `rfc-9679` recorded that only its §5.7 URI form names the hash
function `H`, and left *"choosing between the bare digest and the
self-describing URI"* open. The CWT envelope removes the choice: there is no
bstr slot with the right meaning, so a `KeyId` in a CWT **is** the §5.7 URI, and
`H` becomes part of the signed bytes. That is a gain, not a cost — a verifier
can no longer be wrong about which hash produced the name — and it is paid for
in length: `urn:ietf:params:oauth:ckt:sha-256:` is 33 characters of prefix
before the digest.

**A second, smaller consequence.** §3.1.1 inherits JWT's semantics wholesale
(RFC 7519 §4.1.1), so `iss` names an **issuer**, while `R-O-01`'s *"issuer key
that can be specified as KeyId"* names a **key**. Nothing in RFC 8392 says those
are the same thing, and nothing in it settles whether a `KeyId` means "this key,
now" or "this principal, across changes" — the question `rfc-9964`'s extraction
found unanswered in all four of our architecture documents. The CWT envelope
does not settle it either: it hands you two text slots and lets you put a key in
one and a principal in the other without saying which is which.

---

## 3. R-O-01 — the reference signed CWT does not bind its own issuer key

**CONFIRMED, and now proved rather than inferred.** `examples/vectors.yaml`
V-0005: Figure 11 is the document's **only** signed CWT, and decoded from
Figure 10's hex it is

```
18([ h'a10126',
     {4: h'4173796d6d65747269634543445341323536'},
     h'<80-octet claims set>',
     h'<64-octet signature>' ])
```

`alg` (−7) is protected; the key identifier is label 4 in the **unprotected**
bucket. This pass then built `Sig_structure` as RFC 9052 §4.4 defines it —
`["Signature1", body_protected, external_aad, payload]`, 99 octets — and **the
signature verifies from exactly those four fields.** The `{4: kid}` map is
therefore provably not an input, not merely absent from a definition we read.

**All five printed CWTs do the same**: every one carries `kid` in the
unprotected bucket and nothing but `alg` in the protected one. That is
COSE-conformant and it is not a forgery route — the signature verifies or it
does not. Under `R-O-01` it means the statement does not bind its own issuer
key, and a verifier that *selects* a key by the unprotected `kid` can be steered
into failing.

**What we do about it.** Put `KeyId` in the protected bucket. `rfc-9597` is the
registered mechanism for doing that with a *claim* (label 15), `rfc-9596` is the
registered mechanism for doing it with a *type* (label 16), and `rfc-9943` §6 is
the ratified precedent for requiring the first. All three are in this library.

---

## 4. What we adopt

1. **The claims-set shape.** A CBOR map of small-integer keys is the right
   payload shape and §3 gives the reason we would give: To keep CWTs as small as possible, the Claim Keys are represented using integers or text strings.
   §2 fixes it as The CBOR map that contains the claims conveyed by the CWT. — a map, not an array
   and not a tagged item.

2. **§5's tag prohibition at the value layer**, which is `MD-3`'s no-tags clause
   arriving from 2018 and from a different direction:
   The claim values defined in this specification MUST NOT be prefixed with any CBOR tag. With the stated reason:
   Tagging claim values would only take up extra space without adding information.
   And again for one tag by name, in §2: The encoding is modified so that the leading tag 1 (epoch-based date/time) MUST be omitted.
   A Standards Track document stripping tags at the value layer for exactly
   option 5's reason is independent support worth citing.

3. **§7.1 step 6 / §7.2 steps 2–3 as a design rule, not just a procedure.** The
   document's own step order is the cleanest available proof that a CBOR tag is
   not authenticated: tags go on after the object exists and come off before
   validation. We adopt the rule it implies — **no security-relevant signal
   outside `Sig_structure`** — and `protocol.md` draws it.

4. **§7.2's single rejection discipline.** If any of the listed steps fail, then the CWT MUST be rejected -- that is, treated by the application as invalid input.
   One terminal failure for the whole procedure, with no partial acceptance, is
   the right default for us. We do **not** adopt its silence about *reporting*
   (see §6.4).

5. **The `aud`-as-array capability, from §3.1.3 and not from the registry.** We
   will need multi-audience statements, §3.1.3 permits them, and Table 1 and
   the registry do not. Adopting the prose form and recording why is the honest
   path; see defect D-3.

---

## 5. What we adapt, and how

1. **Protected-header placement becomes mandatory, not optional.** RFC 8392
   puts `kid` in the unprotected bucket in five of five examples and never says
   where a key identifier belongs. Our profile states protected-only placement
   and cites `rfc-9943` §6 as the precedent rather than inventing the rule
   (`R-O-03`).

2. **A claim-set profile, which §3 declines to give.** The set of claims that a CWT must contain to be considered valid is context dependent and is outside the scope of this specification.
   And §3.1: None of the claims defined below are intended to be mandatory to use or implement.
   So a CWT with no claims at all is conformant, and the derived CDDL in
   `schema/` has **no required member** because that is the source's position.
   Our profile supplies `iss` and `sub` as required, following `rfc-9943` §6,
   which requires both — in the *header*, via `rfc-9597`, not in the payload.

3. **A canonical encoding, which §7.1 step 2 does not name.**
   Let the Message be the binary representation of the CWT Claims Set. is the step at which determinism
   would have to be decided, and it is not: `canonical` and `deterministic`
   occur **zero** times in the source. **[analysis] Measured consequence, and
   it is better news than expected:** all five printed CWTs and the printed
   claims set are already in RFC 8949 §4.2.1 deterministic map order — each
   re-encodes byte-identically under a §4.2.1 encoder — so adopting §4.2.1
   costs nothing against the standard's own vectors. **All three printed
   `COSE_Key`s are not** (`examples/vectors.yaml` V-0011). That asymmetry is a
   `DEC-003` trap, not a `DEC-002` one: a thumbprint over the printed bytes of
   A.2.1, A.2.2 or A.2.3 differs from one over their §4.2.1 re-encoding, which
   is why `rfc-9679`'s "canonical key bytes before hashing" clause is not
   pedantry.

4. **Fail-closed where §3 fails open.** However, in the absence of such requirements, all claims that are not understood by implementations MUST be ignored.
   We adapt this to: unknown claims are ignored **only** inside a declared
   extension range, and anything else is a rejection. §3's rule is why a
   Private Use claim-key collision is silent rather than loud (§6.2 below).

5. **A nesting depth bound.** §7.1 step 5 and §7.2 step 6 both loop with no
   limit, and A.6's prose says so outright: Note that there is no limitation to the number of layers; this is an example with two layers.
   An implementation needs a bound the document does not give it;
   `state-machine.yaml` records the two loops and their differing re-entry
   points.

---

## 6. What we reject, and why

### 6.1 CBOR tag 61 — rejected, and it costs nothing authenticated

§6 defines it, §9.4.1 registers it, and §6 makes it optional in terms:
Its use is optional and is intended for use in cases in which this information would not otherwise be known.
§7.2 step 3 permits the untagged case outright:
If the object does not have a COSE CBOR tag, the COSE message type is determined from the application context.

**And it was never an authenticated signal.** §7.1 step 6:
If needed by the application, prepend the COSE object with the appropriate COSE CBOR tag to indicate the type of the COSE object. If needed by the application, prepend the COSE object with the CWT CBOR tag to indicate that the COSE object is a CWT.
§7.2 step 2: If the object begins with the CWT CBOR tag, remove it and verify that one of the COSE CBOR tags follows it.
This pass confirmed it from the other side: `Sig_structure` has four fields and
no tag is one of them, and A.3's signature verifies from those four alone.

So **dropping tag 61 under MD-3 costs no authenticated information**, and
`rfc-9596`'s protected-header `typ` is a strictly stronger replacement. What it
*does* cost is fixtures — see Cut 1.

### 6.2 The CWT Claims registry as our extension point — rejected on `R-M-12`

`R-M-12` requires an extension point to be a `(key, local label)` pair. A CWT
claim key is neither: it is a globally allocated label from one registry
(§9.1), or an unscoped Private Use integer below −65536. **Priced, and the
price is in `schema/claim-key-policy.derived.yaml`:**

| claim-key range | policy (§9.1.1) | CBOR cost |
|---|---|---|
| integer −256…255 | Standards Action | **1 octet** for 0…23 and −1…−24, 2 for the rest |
| text string, length 1 | Standards Action | 2 octets |
| integer −65536…−257, 256…65535; tstr length 2 | Specification Required | 3 octets |
| integer > 65535 | Expert Review | 5 octets to 2³²−1, **9** beyond |
| text string longer than 2 | Expert Review | 4 octets at length 3, `1 + n` after |
| **integer < −65536** | **Private Use** | **5 octets** to −2³², 9 beyond |

Computed by this extraction from RFC 8949 §3 head encodings, not quoted.
**[correction] the summary's version of this table flattened the Expert Review
row to "5 bytes".** That is true of integers and false of text strings, where a
three-character key costs 4. The headline survives and is sharper: **the only
policy-free range costs five times the cheapest**, and seven claims of our own
in Private Use pay 35 octets of keys against 7 for the registered set. There is
also **no Private Use range for text keys at all**, so "pick a URI-ish label and
avoid the registry" is not available either.

And the failure is silent. §3's ignore-the-unknown rule means two issuers who
both reach for −65537 do not collide loudly; the verifier drops what it does not
recognise. There is no mechanism anywhere in the document for scoping a label to
the key that defined it.

### 6.3 The three out-of-band recognition signals — rejected for our export

§6 gives three ways to know a structure is a CWT, and the first is the
document's own disclaimer: How to determine that a CBOR data structure is a CWT is application dependent.
Then In some cases, this information is known from the application context, such as from the position of the CWT in a data structure at which the value must be a CWT.
and One method of indicating that a CBOR object is a CWT is the use of the "application/cwt" content type by a transport protocol.
None is inside the signature. We reject all three in favour of `rfc-9596`'s
protected `typ`, which is — and `rfc-9596`'s own record says so — the only
signal in this set that is both in band and authenticated.

### 6.4 Silence on failure reporting — rejected

§7.2's one error path says what a recipient must *do* and nothing about what it
must *say*: there is no error code, no distinguishable failure reason, and no
reporting duty, for seven steps. For us a verifier that cannot say *which* check
failed is unusable in an audit, so our profile adds failure reasons. This is an
addition, marked as one.

### 6.5 §8's sign-then-encrypt guidance as *guidance* — rejected; we make it a rule

§8's strongest sentence is lowercase:

> Syntactically, the signing and encryption operations for Nested CWTs may be applied in any order; however, if both signing and encryption are necessary, producers normally should sign the message and then encrypt the result (thus encrypting the signature). This prevents attacks in which the signature is stripped, leaving just an encrypted message, as well as providing privacy for the signer. Furthermore, signatures over encrypted text are not considered valid in many jurisdictions.

Under §2's *"when, and only when, they appear in all capitals, as shown here"*
that binds nobody, in the one paragraph of the document that prevents an attack
it names. We make it a `MUST` in our profile.

---

## 7. MD-3, header by header — and where this document cuts against it

`MD-3` narrowed DEC-002 to **option 5**: `docs/extraction.md`, which is in this
repository, states it as *"reduced CBOR, no IANA tags, COSE as export only"*.
A **narrowing, not an acceptance.** The mapping first, then the cuts.

### 7.1 The header-by-header mapping

**What our statement fields would ride in, and under which allocation.**

| our field (ARCH-0001 §4.1) | CWT / COSE carrier | label | registry | option-5 verdict |
|---|---|---|---|---|
| issuer principal | `iss` claim | 1 | CWT Claims (§9.1) | **carry**, as `rfc-9679` §5.7's URN — §2 above |
| subject | `sub` claim | 2 | CWT Claims | **carry** |
| `KeyId` of the signing key | COSE `kid` | 4 | COSE Header Parameters (RFC 9052) | **carry, but protected**, not where all five examples put it (§5.1) |
| statement type | `rfc-9596` `typ` | 16 | COSE Header Parameters | **carry** — the in-band replacement for the tag we drop (§6.1) |
| algorithm | COSE `alg` | 1 | COSE Algorithms (RFC 9053) | carry; RFC 8392 names none at all (§8 below) |
| validity window | `exp` 4, `nbf` 5 | 4, 5 | CWT Claims | carry — **and nothing in RFC 8392 ever reads them** (§6.4, `state-machine.yaml`) |
| issuance time | `iat` claim | 6 | CWT Claims | carry, **as an integer**; see Cut 4 |
| statement id | `cti` claim | 7 | CWT Claims | carry; the one bstr slot, and not a `KeyId` (§2) |
| our own fields | Private Use claim keys < −65536 | — | none | **reject** — 5 octets each and unscoped (§6.2) |
| "these bytes are a CWT" | CBOR tag 61 | — | CBOR Tags (§9.4.1) | **drop** — unauthenticated, costs nothing (§6.1) |
| "these bytes are a COSE_Sign1" | COSE tag 18 | — | CBOR Tags | **drop** — same argument, `rfc-9053`'s record carries it |
| claim-set canonical form | — | — | — | **ours**; §7.1 step 2 names none (§5.3) |

**The export mapping, in one line.** A `COSE_Sign1` with `alg` and `typ` and
`kid` all protected, payload a §4.2.1-deterministic CBOR map of CWT claim keys
1–7 only, **no tag at any layer**, and every field of ours outside 1–7 carried
by a mechanism that is not a CWT claim key.

**What we deliberately do not carry:** tag 61, tag 18, the `application/cwt`
media type and CoAP Content-Format 61 as *transport* signals (§6.3), any
Private Use claim key (§6.2), any float claim (Cut 4), and `aud` as an array
unless we accept defect D-3 knowingly.

### 7.2 Cut 1 — the fully untagged export has no reference bytes. **Costs option 5; option 3 does not pay it.**

**[analysis], and measured.** `examples/vectors.yaml` V-0010: of the five CWTs
Appendix A prints, **four carry a COSE tag and no tag 61, one carries both, and
not one is untagged.** Every example begins `d2` (18), `d83dd1` (61 over 17),
`d0` (16), `d0` (16) or `d1` (17). §7.2 step 3 permits the untagged form and the
defining document demonstrates it nowhere, so **an option-5 fixture package has
no reference bytes in RFC 8392 to check itself against.** The first untagged CWT
any of us produces is unvalidated against the standard's own examples.

Option 3 (JCS over JSON) pays nothing here: `topics/canonical-encoding.yaml`
records that JSON *"has no tag space and no header space"*, so there is no
untagged variant to be missing an example of. This is a **tooling** cost rather
than a security one, and it is the cheapest of the four cuts to pay — we write
the fixtures — but it should be paid knowingly.

### 7.3 Cut 2 — option 5 trades the tag registry for a larger one. **Costs option 5; options 1 and 3 do not pay it.**

This is the cost `records/ietf/rfc-9052`'s design notes deferred **to exactly
here**, in their own words: *"the CWT claim keys are their own registry, so CWT
interchange carries a second, larger registry dependence than the tag; that is a
DEC-003 and DEC-005 matter and is outside this record."* It lands, and §6.2
prices it. The CBOR Tags registry dependence option 5 removes is **one number**;
the CWT Claims registry dependence it installs is **a governed namespace with
four allocation tiers, a mailing list, a three-week review and a 21-day
escalation path** (`protocol.yaml`, flow `register-a-claim-key`).

`topics/canonical-encoding.yaml` records that option 3 *"is registry-free by
construction"* and that **option 1 also wins that criterion**, *"by the same
argument and without paying option 3's §5 cost"*. So on namespace governance
this document moves option 5 **further behind both**, not level with them. The
honest framing is `rfc-9052`'s, quoted exactly: **"No tags" and "no registry dependence" are different rules, and MD-3 states the first.**
**[analysis] And the word that matters is one this extraction adds: MD-3 states
*only* the first.**

### 7.4 Cut 3 — §5's escape hatch means "no tags" is our decoder rule, not the format's. **Costs option 5.**

§5's prohibition has a clause in the same paragraph:

> However, this does not prohibit future claim definitions from requiring the use of CBOR tags for those specific claims.

So option 5's no-tags property is **not inherited** from CWT. It survives only
as long as we control which registered claims we are willing to read, which
makes "no tags" a *positive decoder rule of ours* rather than a property of the
format — the same point `rfc-9052`'s design notes §3.3 makes at the tag layer,
arriving here from the claim layer. `topics/canonical-encoding.yaml` already
names the shape of the fix: option 5 *"must CONSTRUCT registry-freedom by
subtraction, with a positive rule excluding major type 6, decoder rejection, and
a named untagged export profile"*. This cut says that rule has to cover
**future claim definitions** too, not only the tag space.

### 7.5 Cut 4 — the one claim shape the document chose to exhibit is the one that re-encodes differently. **Costs option 5 and option 3 alike; option 1 cannot express it at all.**

**[analysis], and measured.** §4's Table 1 and §9.1.2 both admit
`integer or floating-point number` for `exp`, `nbf` and `iat`, and A.7 prints
`iat` as `1443944944.5`, encoded `fb 41d584367c200000` — a float64.
`examples/vectors.yaml` V-0009: this pass reproduced A.7's MAC tag and then
measured that **binary32 round-trips 1443944944.5 to 1443944960.0**, so float64
is the only IEEE width that holds the value. RFC 8949 §4.2.2's shortest-float
rule happens to agree — but **RFC 8392 states no width rule at all**, so a
re-encoder that narrows a float claim is conformant to RFC 8392 and destroys the
MAC.

Option 5's answer is the `rcbor` exclusion `topics/canonical-encoding.yaml`
describes — *"no floats, no tags, definite lengths only"* — which solves it by
deleting the case, at the price of a decimal having to travel as an integer or a
string. Option 3 pays a worse version of the same bill: the topic records
RFC 8785 Appendix B serialising 2⁶⁸ as *"a DIFFERENT integer, silently, with a
signature that verifies perfectly"*. Option 1 has **no number type at all**
(RFC 9804), so the field needs a hand-built mapping. **No option escapes this;
option 5 escapes it most cheaply, and that is a point in option 5's favour
stated so the balance is honest.**

### 7.6 Cut 5 — option 5's type identity is `(defining key, label)`, and nothing in CWT can express it. **Costs option 5.**

`ARCH-0002 P1` wants type identity to be key-relative. The CWT claim space is
`int / tstr`, flat and global, with no key component (`schema/
cwt-claims-set.derived.cddl`'s `claim-key` rule, and §9.1.1 is the only
structure over it). The nesting trick `rfc-9597` uses — buy one COSE header
label and put the whole claim space inside it — is a one-level approximation
where the "key" is an IANA allocation instead of ours. **There is no spelling of
a key-relative claim name in RFC 8392 at all.** This is the same cut
`rfc-9596`'s and `rfc-9597`'s records make about their own value spaces; three
documents in one lane, three different registries, one shape.

---

## 8. DEC-005 — it mandates no algorithm, and that is the whole answer

**CONFIRMED.** RFC 8392 names **no algorithm in any normative sentence.** §7.1
step 4 hands all three cases to RFC 8152 — three of the document's nine BCP 14
keywords are those three delegations — and the only algorithm identifiers in the
document (−7, 4, 10) are inside Appendix A's examples. Its `DEC-005`
contribution is the envelope shape and the claim slots.

**[analysis]** The algorithm catalogue is `rfc-9053`'s, and that record's
extraction already found that neither COSE document names a mandatory-to-
implement set either. So **the whole CWT-over-COSE stack specifies no algorithm
anywhere**, and `DEC-005` gets no constraint from any of the three. What this
record *does* contribute to `DEC-005` is a working algorithm *witness*: A.3
demonstrates ES256 end to end with a verified signature, A.4 and A.7 demonstrate
HMAC 256/64, and A.5 and A.6 demonstrate AES-CCM-16-64-128 — three algorithm
families, five vectors, all reproduced here.

---

## 9. R-O-03 and R-O-05 — no canonicalization is cited because none exists, until it does

**CONFIRMED.** §7.1 step 2 names no canonical form and there is nothing in
RFC 8392 to cite. For `R-O-03` that is not a violation; it is a trap. The
Message travels as an opaque `bstr`, so **determinism is sidestepped rather
than solved**: copying bytes works and re-encoding does not. The moment any
party rebuilds a claims set rather than forwarding its bytes, the signature
dies, and the document offers no rule that would have prevented it.

**`R-O-05` is satisfied by accident and should not be relied on.** `R-O-05`
asks that canonicalisation run once, at authoring, on trusted input, and never
as part of verification (`topics/canonical-encoding.yaml`, conditions (3) and
(4)). §7.2 never re-encodes anything: step 5 validates over received bytes and
step 7 only *decodes*. So the CWT validation path is `R-O-05`-compatible — but
by silence, and silence is permission rather than a rule, which is the same
distinction the topic draws for option 1's condition (5).

**Against the six `canonical-encoding` conditions**, as this document leaves
them:

| condition | RFC 8392's contribution |
|---|---|
| (1) injective encoding | **nothing.** No canonical form, no map-order rule, floats admitted. [analysis] Its *examples* are §4.2.1-ordered, which is evidence about practice and not a rule |
| (2) decoder rejects non-canonical input | **nothing**, and §3 points the other way: unknown claims must be *ignored* |
| (3) canonicalise once, at authoring | **compatible by silence** — §7.2 never re-encodes |
| (4) authenticated type indicator inside the signed bytes | **absent, and the document's three substitutes are all outside it** (§6.3). This is the hole `rfc-9596` fills |
| (5) canonical order for set-valued fields | **nothing.** `aud` is the only set-shaped field and §3.1.3 gives its array no order |
| (6) Unicode normalisation rule for identity-bearing text | **nothing.** `Unicode`, `normalization` and `normalisation` occur **zero** times, and `iss`/`sub` are the identity-bearing text in this envelope. Under `ARCH-0002 P1` the issuer name is the root of the naming scheme, so this is the condition that bites |

Condition (6) is the sharp one. `rfc-8610` found CDDL does no normalisation and
`draft-mcnally-deterministic-cbor` found dCBOR §2.7 requires NFC; **RFC 8392
says nothing, and its `iss` is a free-form text string.** Two issuers whose
names differ only by normal form are two principals to a byte comparison and one
to a human.

---

## 10. The summary's findings, tested against the source

Each was re-derived from `.cache/rfc-8392.txt` in this pass. **Three confirmed,
two narrowed, one corrected.**

| claim | verdict |
|---|---|
| A thumbprint cannot be an `iss` because §3.1.1/§3.1.2 require StringOrURI while a COSE Key Thumbprint is a bare byte string, so the CWT envelope forces `rfc-9679` §5.7's URI form and pins the hash | **CONFIRMED** (§2). The type quotations are verbatim and the three-slot census is complete: `cti` is the only bstr claim and §9.1.2 records its JWT name as `jti` |
| `rfc-9596`'s protected `typ` is strictly stronger than the tag it replaces, because §7.1 step 6 prepends tags after the signature exists and §7.2 steps 2–3 strip them before validation | **CONFIRMED, and now proved from the other side** (§6.1): `Sig_structure` has four fields, no tag is one of them, and A.3's signature verifies from those four alone |
| §9.1.1's four policy tiers cost 1–2 / 3 / 5 / 5 bytes, so the policy-free range costs 5× the cheapest | **CONFIRMED in its conclusion, NARROWED in one cell** (§6.2). The Expert Review row is 5 octets for integers and **4 and up** for text strings, and both the Expert Review and Private Use integer rows become **9** beyond ±2³². The 5× headline and the 35-vs-7 arithmetic stand |
| Two of the five Appendix A CWTs are not reproducible from the printed key without applying two unverified errata | **NARROWED — the stronger half is refuted.** Both MAC tags reproduce from Figure 6's own 32 octets of `k`. The errata concern the key's `kid` *label* and `alg` *value*, which no HMAC computation reads. A.2.2 is a **working** fixture that **fails a conformance check on its own `alg` declaration**. The practical advice — prefer A.2.3 + Figure 10 — stands, because that one is self-consistent as well as working |
| A.2.2's key is wrong twice with both errata still *Reported*, pushing in opposite directions, and as printed it fails RFC 9053 §3.1 | **CONFIRMED mechanically** (defect D-1). Figure 6's bytes give `kid` at label 2 and `alg` 10; Figure 7 prints label 4 and `alg` 4. It then MACs two objects whose protected headers declare `alg` 4 |
| §3.1.3 permits an `aud` array while Table 1 and the §9.1.2 registry entry both say text string only | **CONFIRMED** (defect D-3). All three printed claims sets use the scalar, so the array form has no fixture anywhere |

---

## 11. Source defects and ambiguities — reported, never repaired

**D-1 · A.2.2's key disagrees with its own diagnostic rendering, twice, and the
two errata contradict each other.** Figure 6's hex decodes to
`{-1: k, 1: 4, 2: h'Symmetric256', 3: 10}`; Figure 7 prints `kid` at label
**4** and `alg` as **4 / HMAC 256/64 /**. Erratum **7982** says the label should
be 2 (believe the hex); erratum **8655** says the value should be 4 (believe the
diagnostic). **Both were status *Reported* as of 2026-10-20**, eight years on.
Figures 5 and 9 both print `kid` at label 2, so Figure 7 is the outlier. Label 4
is the COSE **header** label for `kid`; in a `COSE_Key` the label is 2.
Confirmed by decoding in this pass; `examples/vectors.yaml` V-0003.

**D-2 · As printed, that key fails a conformance check.** Its bytes declare
`alg` 10 (AES-CCM-16-64-128) and it is then used to MAC Figures 12 and 18, both
of which declare `alg` 4 (HMAC 256/64) in their protected headers. RFC 9053
§3.1: *"If the "alg" field is present, it MUST match the HMAC algorithm being
used."* **Nothing is unusable as a result** — see the narrowing in §10 — but a
conformance checker reading the key and the object together rejects the pair.

**D-3 · §3.1.3 permits an `aud` array; §4 and §9.1.2 exclude it.** §3.1.3:
or each of the audience array element values is a StringOrURI when the audience claim value is an array. (StringOrURI is defined in Section 2 of this specification.)
§4's Table 1 row is `| aud  | 3   | text string                      |` and
§9.1.2's entry is `o  Claim Value Type(s): text string`. **No erratum covers
this** (checked 2026-10-20). A validator generated from Table 1 or from the IANA
registry — which is what a code generator reads — **rejects a conformant CWT.**
If we build CDDL for the CWT claim space, this is the one cell we must not take
from the registry.

**D-4 · A.6's prose describes a header parameter the figure does not carry.
NEW IN THIS PASS; no erratum.** A.6 says
The content type is set to CWT to indicate that there are multiple layers of COSE protection before finding the CWT Claims Set.
Decoded, the object's protected bucket is `{1: 10}` and its unprotected bucket
is `{4: kid, 5: iv}`. **RFC 9052 label 3 — content type — is absent from
both.** So the only multi-layer signal in the document's one nested example is
§7.2 step 6's tag check. `examples/vectors.yaml` V-0008.

**D-5 · A typo in the document's load-bearing security sentence.** §8 opens
The security of the CWT relies upon on the protections offered by COSE. — *"relies upon on"*. Harmless, quoted as
printed everywhere in this directory, and recorded so nobody "fixes" it into a
quotation that then fails a verbatim check.

**D-6 · A grammatical slip in §7.2 step 5.** Depending upon whether the CWT is a signed, MACed, or encrypted, there are three cases:
— *"whether the CWT is a signed, MACed, or encrypted"*, against §7.1 step 4's
correct *"whether the CWT is signed, MACed, or encrypted"*. Same class as D-5
and recorded for the same reason.

**D-7 · Three of the appendix's nine diagnostic-notation figures do not parse.**
Figure 5 (source lines 967–968) and Figure 7 (983–985) are **missing the comma**
after the `k` entry; Figure 19 (1301–1302) has a **trailing comma** inside a
one-entry map. Cosmetic, and practical: anyone building fixtures by parsing the
RFC's diagnostic notation rather than its hex hits three parse errors in a
nine-figure appendix. Use the hex — this extraction did, which is how it found
them. `examples/vectors.yaml` V-0012.

**D-8 · Both normative encoding references are obsolete, and one locator moved.**
RFC 8392 cites RFC 7049 for CBOR (superseded by RFC 8949) and RFC 8152 for COSE
(superseded by RFC 9052 and RFC 9053). §2's *"Section 2.4.1 of [RFC7049]"* is
§3.4.2 in RFC 8949. §7's procedures — the only procedures in the document —
therefore cite a document this library marks `marginal`, and **nobody can follow
§7 without a substitution table RFC 8392 does not supply.** Normal ageing rather
than a defect; recorded because `protocol.yaml` has to carry the substitutions
and does.

---

## 12. Open questions

1. **Does `KeyId` mean "this key, now" or "this principal, across changes"?**
   `rfc-9964`'s extraction found that none of `ARCH-0001`, `ARCH-0002`,
   `ADR-0001` or the v0.2.0 proposal says. RFC 8392 makes the question *visible*
   by giving you two text slots — `iss` and `sub` — and no rule about which
   holds a key and which holds a principal. **Whoever owns `DEC-003` has to
   answer it before the claim mapping in §7.1 can be fixed.**

2. **Does the `rfc-9679` §5.7 URN go in `iss`, in `sub`, or in a protected
   `kid`?** §2 above shows the URN is the only thumbprint form a CWT claim can
   hold, and §3 shows `kid` is where every example puts the key identifier and
   is unauthenticated there. Three placements, three different meanings, and
   RFC 8392 constrains none of them.

3. **Do we accept defect D-3's `aud` array?** If yes, our CDDL departs from the
   IANA registry and we must say so in the profile. If no, we need a
   multi-audience mechanism that is not `aud`.

4. **What bounds the nesting depth?** §7.1 step 5 and §7.2 step 6 are unbounded
   and A.6's prose says so. A number has to be chosen, and the two loops'
   differing re-entry points (creation at step 3, validation at step 1) mean an
   inner layer may legally carry its own tag 61 — so the bound has to be
   enforced on the *validation* side.

5. **Who reads `exp`?** Nothing in RFC 8392 does, so **a conformant validator
   accepts an expired CWT.** Our profile has to state where expiry is checked,
   and `state-machine.yaml` records that the gap is in the standard rather than
   in our model of it.

6. **Does condition (6) get answered at the `iss` layer or above it?** `iss` is
   free-form text and is the root of the naming scheme under `ARCH-0002 P1`.
   `rfc-9741`'s extraction found that a CDDL schema cannot state a normalisation
   constraint; RFC 8392 states none either. The rule has to live in our profile,
   and the one-line form `rfc-9741` derived for SDSI name chains — normalise
   after joining, never per label — is the nearest precedent we hold.
