---
record: rfc-9053
kind: design-notes
title: "rfc-9053 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.1`) are RFC 9053. Other RFCs are named (`RFC 9052 §3.1`). Our own documents
are cited by id (`ARCH-0002 P1`, `MD-3`, `R-I-03`). Three markers distinguish
voices:

- unmarked prose reports **RFC 9053** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources do
  not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) lists
**four** options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged. `ADR-0001`
(accepted) constrains DEC-002 and says option 2 "as originally written does
not" remain on the table. `MD-3` (2026-09-28) narrows DEC-002 to option 5.
**No ADR for DEC-002 has been written**, and `DECISIONS-0001` tier 1 item 2 says
so in terms: "Still open: a narrowing is not an acceptance, and no ADR exists."
Nothing below may be read as an accepted encoding decision.

**What this record is for.** RFC 9053 is the **algorithm half** of COSE. It
defines no messages — those are RFC 9052's — and almost no structures. What it
defines is 43 code points and, for each, the key type, curve, key length, nonce
length, tag length, signature encoding and header parameters it requires. Under
MD-3 that makes it exactly one thing to us: **the catalogue the export path
draws from.** It is also, read against our own documents, the clearest evidence
in the COSE set about what option 5 costs and what it does not.

---

## What we adopt

**The four signature code points, as the closed set our export may name.**
§2.1 Table 1 and §2.2 Table 2: ES256 = −7, ES384 = −35, ES512 = −36,
EdDSA = −8. Nothing else in the document is reachable from a signing-only export
profile, and `algorithm-values.derived.cddl` keeps them in their own group for
that reason.

**The key-type and curve numbering (§7, Tables 17 and 18).** `OKP` = 1,
`EC2` = 2, `Symmetric` = 4, `Reserved` = 0; P-256 = 1, P-384 = 2, P-521 = 3,
X25519 = 4, X448 = 5, Ed25519 = 6, Ed448 = 7. We adopt these **as interchange
identifiers**, which is what `ADR-0001` already requires: "Registry identifiers
**may** appear at interchange boundaries, and such mappings are documented as
lossy per R-I-01."

**§7.1's cross-check obligation, as a verifier rule.** "Applications MUST check
that the curve and the key type are consistent and reject a key if they are
not." Table 18's fourth column is the binding, and it is not optional: the same
byte string is a valid Ed25519 public key and a valid X25519 public key, and
§2.2.1 says "the public key from one should not be used with the other
algorithm." This lands directly on **DEC-003** — see *Mapping*, item 4.

**§2.1.1's mitigation, as a structural rule for our export.** "As the hash
algorithm is part of the signature algorithm identifier, this attack is
mitigated by including a signature algorithm identifier in the protected-header
bucket." Our export puts `alg` in the protected bucket, always, and never in the
unprotected one. This is the same move `ARCH-0002` P5 makes for decoding order
and `R-O-05` (proposed) makes for verify-before-decode: the thing that selects
the algorithm must be inside the thing the signature covers.

**§2.1's ECDSA signature encoding, exactly as written.** `Signature = I2OSP(R,
n) | I2OSP(S, n)` where `n = ceiling(key_length / 8)`; "The length is rounded up
to the nearest byte and is left padded with zero bits to get to the correct
length." Two integers concatenated, fixed width, **no ASN.1 and no DER**.

> **[analysis]** This is the single most likely implementation defect on our
> export path, because every general-purpose crypto library this project is
> likely to use returns a DER `SEQUENCE { INTEGER r, INTEGER s }` from an ECDSA
> signing call. A COSE exporter that passes that value through produces a
> signature no COSE verifier accepts, and the document prints no vector that
> would catch it (`examples/README.md`). Applying the formula gives 64 / 96 /
> **132** bytes for P-256 / P-384 / P-521; the 132 is `ceiling(521/8) = 66`
> doubled, and it is the number implementations get wrong. The RFC prints the
> formula and no sizes.

**§2.2.1's determinism, as the reason EdDSA is the fixture algorithm.**
"Signing and nonbatch signature verification are deterministic operations and do
not need random numbers of any kind." For `MD-4`'s lane #13 (the option-5
encoder fixtures, D5 due **Oct 28**) this is decisive: EdDSA fixtures are
byte-reproducible from the primitive, with no extra machinery and no seeded RNG
in the test harness.

**§9's duplicate-label prohibition.** "Applications MUST NOT generate messages
with the same label used twice as a key in a single map. Applications MUST NOT
parse and process messages with the same label used twice as a key in a single
map." This is the same rule RFC 8949 §5.3.1 makes a *validity* failure and the
one `ARCH-0002` P5 already adopts. Note that RFC 9053 states it for **messages**
generally, not only for `COSE_KDF_Context` — unlike the minimum-length rule
beside it (see *Mapping*, item 3).

---

## What we adapt, and how

**The algorithm tables — adapted into data, not into our vocabulary.** We take
Tables 1–23 as a lookup our exporter consults at the boundary, held in
`messages.yaml` with 43 code points and their constraints. We do **not** take
them as native type identifiers; `ADR-0001` forecloses that. The adaptation is
therefore a *table*, not a *namespace*, and the thing that matters for the ADR is
that the table is small and closed on the signing path: four rows.

**§10's registry framing — adapted as the real citation.** §10 says "IANA has
updated all COSE registries except for "COSE Header Parameters" and "COSE Key
Common Parameters" to point to this document instead of [RFC8152]." RFC 9053 is
therefore the *reference* for code points it did not allocate, not their
allocator; the only row it newly adds is `IV-GENERATION` = 34 (§10.2, Table 23,
Recommended: **No**). What we cite in the ADR is the **IANA "COSE Algorithms"
registry**, with RFC 9053 §2.1/§2.2 as the source of each algorithm's
*constraints*. See *Mapping*, item 3.

**§8's capabilities — adapted as an idea, rejected as a structure.** The idea
that a party can advertise "I accept EdDSA over Ed25519 and Ed448" as data is
exactly what our schema scenarios need (`MD-4`, Ndewedo's archives vocabulary).
The structure is a positional CBOR array whose meaning is its position
(`examples/README.md`), and §8 makes the list **immutable on registration**:
"If it is later found that a new capability is needed for a key type or
algorithm, it will require that a new code point be assigned to deal with that."
We take the concept into a named-field map under P1 and leave the array at the
boundary.

**§1.4's prose-is-normative stance — adapted into our own schema discipline,
inverted.** §1.4: "the CBOR data objects defined here are described in prose.
Additional (non-normative) descriptions of the COSE data objects are provided in
a subset of CDDL". COSE made prose normative because CDDL was not yet an RFC.
RFC 8610 has been an RFC since June 2019, and this library holds its full
extraction, so the reason has expired. `WP1` ("JSON Schema or CDDL for logical
types in §4") should make **the schema normative and the prose explanatory** —
the opposite of the choice RFC 9053 was forced into.

> **[analysis]** This is not a small difference in practice. Because §1.4 makes
> the prose normative, nothing upstream constrains RFC 9053's structures
> mechanically: four of the five files in `schema/` are ours, and the document
> ships one CDDL fragment in 2443 lines. Under `R-O-03` ("Canonicalization
> algorithm for each concrete encoding SHALL be cited, not invented silently")
> this is the position to avoid being in, and we avoid it by shipping the schema
> as the artifact rather than as an appendix.

---

## What we reject, and why

**Everything in §3, §4, §5 and §6 — the MAC, content encryption, KDF and key
distribution halves.** 39 of the 43 code points. Our export signs; it does not
encrypt, MAC, derive or distribute keys. Concretely this drops: all four HMAC
and four AES-MAC identifiers (§3), all twelve AEAD identifiers (§4), the whole
HKDF apparatus and `COSE_KDF_Context` (§5), `direct` and the four `direct+HKDF`
identifiers (§6.1), the three AES-KW identifiers (§6.2), and all ten ECDH
identifiers (§6.3, §6.4). We also therefore never build a `COSE_KDF_Context`,
which is the one structure §9's determinism rule covers.

**All nine algorithm-specific header parameters (Tables 9, 10, 15).** Not
because option 5 forbids them, but because **none of them applies to a
signature**. See *Mapping*, item 1 — this is the finding, not a preference.

**`IV-GENERATION` (34) and the §8 immutability model.** The code point because
we never derive an IV; the model because it is the registry pathology `ARCH-0002`
P1 was written against (*Mapping*, item 4d).

**Compressed point encoding for `y` (§7.1.1).** §7.1.1 allows `y` to be a CBOR
`false`/`true` carrying the sign bit. We reject it on the export path.

> **[analysis]** Two reasons, both ours. First, it makes a single map label
> (−3) carry two unrelated CBOR types, which is the shape `ARCH-0002` P3 ("a
> type is a schema") exists to prevent. Second, and decisively for
> **DEC-003**: if a `KeyId` is a digest over a canonical key encoding, then the
> *same* public key digests to two different values depending on whether `y` was
> sent as a bstr or as a bool. §7.1.1 offers no canonical choice between them.
> A `KeyId` scheme that does not pin this is not injective, which is condition
> (1) of the six `canonical-encoding` conditions in `DECISIONS-0001`'s standing
> note. Either pin the uncompressed form, or adopt RFC 9679's thumbprint, which
> pins it upstream.

**Any claim about EdDSA signature lengths attributed to this document.** §2.2
says only "[RFC8032] describes the method of encoding the signature value."
`key-structures.derived.cddl` therefore leaves `EdDSA_signature` an
unconstrained `bstr`, and fixtures that assert 64 bytes must cite RFC 8032.

---

## Mapping to our decisions

### 1. The export path under MD-3 — which algorithms, which headers, what must be carried

`MD-3` narrowed DEC-002 to option 5: "CBOR data model, no IANA tags, COSE as
export only; type identity is `(defining key, label)` per P1; YAML is the human
form". `R-I-03` requires "Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT
claims (at least one envelope in v1)". So the question this record answers is:
what must a `COSE_Sign1` carry for a **stock COSE implementation** to verify it?

**First, the obligation nobody has discharged.** RFC 9052 §10 — "This document
is designed to provide a set of security services but not impose algorithm
implementation requirements for specific usage" and "It is intended that a
profile of this document be created that defines the interoperability
requirements for that specific application." RFC 9053 adds no
mandatory-to-implement set either; §10.4 is about registration policy, not about
conformance. **Neither COSE document names a single algorithm an implementation
must support.** The export profile is therefore not an optional deliverable: a
COSE export with no stated algorithm set is not interoperable with anything in
particular, and `R-I-01` ("Publish a mapping table for each supported foreign
format") already owes the table.

**The algorithms our export must name**, with what each requires:

| algorithm | `alg` | CBOR (OURS) | `kty` | `crv` | hash | signature | algorithm-specific headers |
|---|---|---|---|---|---|---|---|
| ES256 | −7 | `0x26` | **MUST** be EC2 (2) | P-256 (1) *suggested*, not required | SHA-256 | 64 B, `I2OSP(R,32)‖I2OSP(S,32)` | **none** |
| ES384 | −35 | `0x3822` | **MUST** be EC2 (2) | P-384 (2) *suggested* | SHA-384 | 96 B | **none** |
| ES512 | −36 | `0x3823` | **MUST** be EC2 (2) | P-521 (3) *suggested* | SHA-512 | **132 B** | **none** |
| EdDSA | −8 | `0x27` | **MUST** be OKP (1) | **MUST be present**; Ed25519 (6) or Ed448 (7) | n/a (pure) | per RFC 8032 | **none** |

CBOR head bytes and signature sizes are **OURS** — computed under RFC 8949 §3.1
and from §2.1's own formula. RFC 9053 prints decimal code points and the formula,
and no bytes and no sizes.

**The answer to "what header parameters does each require" is: none beyond
`alg`.** RFC 9053 defines algorithm-specific header parameters **only** for the
KDF and ECDH recipient algorithms — Table 9 (`salt`, −20), Table 10 (the six
PartyU/PartyV context parameters, −21…−26) and Table 15 (`ephemeral key` −1,
`static key` −2, `static key id` −3). Every signature algorithm, every MAC, every
AEAD and AES Key Wrap define **none**. `algorithm-headers.derived.cddl` carries
the empty groups explicitly so the absence is legible rather than inferred.

**What option 5 must carry, concretely.** For EdDSA over Ed25519, the minimum
verifiable `COSE_Sign1` is:

1. **`protected`** — a `bstr` wrapping the deterministically encoded header map
   `{1: -8}`. That is `0xa10127` as a map, `0x43a10127` once wrapped (**OURS**).
   Three bytes of content. `alg` **must** be here and not in the unprotected
   bucket (§2.1.1).
2. **`unprotected`** — may be empty (`{}`). `kid` (RFC 9052 §3.1, label 4) rides
   here or in the protected bucket, and is where **DEC-003**'s `KeyId` lands.
3. **`payload`** — a `bstr` of our canonical statement bytes, or `nil` for the
   detached form (see item 2 below).
4. **`signature`** — a `bstr` in RFC 8032's encoding; for ECDSA, §2.1's
   fixed-width concatenation, **never DER**.
5. **The verification key** — a `COSE_Key` with `kty` 1, `crv` 6, `x`; or
   `kty` 2, `crv` 1, `x`, `y` for ES256. Per §2.1/§2.2's key checks: if `alg` is
   present in the key it **MUST** match, and if `key_ops` is present it **MUST**
   include `verify`.
6. **Nothing else.** No `crit`, no `content type`, no IV, no algorithm-specific
   parameter, and — because `COSE_Sign1_Tagged` = `#6.18` is RFC 9052's and
   option 5 declines the tag registry — no tag, which means the recipient must
   be told out of band that these bytes are a `COSE_Sign1`.

**And one thing neither COSE document gives us: determinism of the transmitted
bytes.** §9's first bullet is "The restriction applies to the encoding of the
COSE_KDF_Context". The identical §9 of RFC 9052 scopes the identical
minimum-length rule to "the Sig_structure, the Enc_structure, and the
MAC_structure". Each document covers the *inputs to the cryptographic
computation* and neither covers the message as transmitted.

> **[analysis]** The protected bucket survives this, because RFC 9052 carries it
> as `empty_or_serialized_map` — a `bstr` whose bytes are both signed and
> transmitted, so whatever the signer chose is what the verifier sees. The outer
> array and the unprotected bucket do not. If our export must be
> byte-reproducible — and it must, because D5 is a fixture package — we impose
> RFC 8949 §4.2.1 ourselves and cite it. **Under `R-O-03` that citation is
> mandatory and it cannot be to RFC 9053 or RFC 9052.** Neither says it.

**The P1 collision, which is the real cost.** Under `ARCH-0002` P1 a type
identifier is `(defining key, local label)` "carried as ordinary map entries"
(proposal §3.3). Put that entry in an exported `COSE_Sign1`'s protected header
and RFC 9052's `header_map` admits it — `* label => values`. Then:

- **Not listed in `crit`.** A stock verifier checks the signature and **ignores**
  our type entry. The type is authenticated but not *enforced*: the bytes are
  covered, the semantics are not. `R-O-05`'s authenticated type indicator
  survives the export as data and dies as a check.
- **Listed in `crit`.** RFC 9052 §3.1: `crit` "is used to indicate which
  protected header parameters an application that is processing a message is
  required to understand." **[analysis]** No stock implementation understands a
  label we allocated, so every stock verifier must refuse the message — and the
  export has stopped being an export.

There is no third position. **This is the concrete price of "COSE as export
only" and it should be written into the ADR in these words**, because the
alternative framings hide it: "lossy per R-I-01" sounds like dropped fields, and
what is actually dropped is enforcement of the one field P1 exists to protect.

### 2. The pre-hash refusal — a standing COSE position, and what it costs us

§2.2, in full:

> The document additionally describes two variants of the EdDSA algorithm: Pure
> EdDSA, where no hash function is applied to the content before signing, and
> HashEdDSA, where a hash function is applied to the content before signing and
> the result of that hash function is signed. For EdDSA, the content to be
> signed (either the message or the prehash value) is processed twice inside of
> the signature algorithm. For use with COSE, only the pure EdDSA version is
> used. This is because it is not expected that extremely large contents are
> going to be needed and, based on the arrangement of the message structure, the
> entire message is going to need to be held in memory in order to create or
> verify a signature. Therefore, there does not appear to be a need to be able to
> do block updates of the hash, followed by eliminating the message from memory.
> Applications can provide the same features by defining the content of the
> message as a hash value and transporting the COSE object (with the hash value)
> and the content as separate items.

RFC 9964 §7.2 (`records/ietf/rfc-9964`), on ML-DSA:

> This document does not specify algorithms for use with HashML-DSA as described
> in Section 5.4 of [FIPS-204]. As the verify routines are different, future
> support for HashML-DSA would require the registration of additional
> algorithms. Section 8.3 of [RFC9881] explains the rationale for disallowing
> HashML-DSA, including the increased complexity and compatibility concerns with
> existing implementations.

**Is this one position or two local decisions?** [analysis] One position, and
the reasons differ in a way that makes the convergence stronger rather than
weaker. RFC 9053 argues from the *message structure* — the whole message is in
memory anyway, so streaming buys nothing — and offers a workaround. RFC 9964
argues from *verify-routine divergence and implementation compatibility*, and
offers none. Different authors, different algorithm families, different
grounds, same outcome; and in neither case is a pre-hash code point merely
unassigned — both documents go out of their way to say they are not assigning
one. The published statements are **nine years apart** (RFC 8152, July 2017,
which this document obsoletes and from which §1.2 says the algorithm sections
were lifted, to RFC 9964, May 2026); the twelve-year figure in this extraction's
brief needs the pre-RFC-8152 COSE drafts, which this library does not hold.
Call it: **COSE declines pre-hash variants and pushes the hash into the
payload.** An ADR that assumes a `HashEdDSA` or `HashML-DSA` code point will
appear is assuming against a position COSE has now restated across two
algorithm generations.

**What it means for us, and it is not nothing.** Our statements may be large:
`R-I-07` puts SPDX or CycloneDX *inside* an `ArtifactStatement` predicate, and
an SBOM is not a small document. Pre-hashing is the usual answer. COSE's answer
is §2.2's last sentence — define the payload as a hash and transport the content
alongside.

> **[analysis]** Taking that route changes what `R-O-05` can promise, and the
> change is adverse. In the direct form, a verifier checks one signature over
> the canonical statement bytes and `ARCH-0002` P5's "verify before decode"
> holds end to end. In the pre-hash form, the verifier checks a signature over a
> **digest**, and must then canonicalise and digest the statement itself to
> compare. Canonicalisation moves from the authoring path to the **verify**
> path, where a divergence between two implementations fails *silently* — the
> signature verifies and the comparison does not, or worse, two different
> statements canonicalise alike. That is condition (3) of the six
> `canonical-encoding` conditions ("canonicalise once at authoring") broken
> outright, and conditions (5) and (6) — canonical order for set-valued fields,
> and a declared Unicode normalisation rule — become security-critical instead
> of merely unstated. `DECISIONS-0001`'s standing note already records (5) and
> (6) as "reachable by no candidate and stated in no document of ours."

**And a smaller point that cuts the other way for algorithm choice.** §2.2:
"For EdDSA, the content to be signed … is processed twice inside of the
signature algorithm." ECDSA makes one pass over a hash. [analysis] For large
statements, this document's own sentence is a reason the export profile should
name **ES256 as well as** EdDSA rather than EdDSA alone — a 2× pass over a large
payload is a real cost, and §2.2's "it is not expected that extremely large
contents are going to be needed" is an assumption about COSE's deployment that
`R-I-07` does not share.

### 3. Standing — an Informational algorithm source under a Standards Track structure

The front matter: **"Category: Informational"**, and "This document is not an
Internet Standards Track specification; it is published for informational
purposes. … It represents the consensus of the IETF community. It has received
public review and has been approved for publication by the Internet Engineering
Steering Group (IESG). Not all documents approved by the IESG are candidates for
any level of Internet Standard; see Section 2 of RFC 7841."

Its companion is not. RFC 9053's own normative reference entry reads: "Schaad,
J., "CBOR Object Signing and Encryption (COSE): Structures and Process",
**STD 96**, RFC 9052". The structure half is an **Internet Standard**; the
algorithm half is Informational.

**Does the document address its own standing?** Only obliquely, and only in
§10.4, which is about *registration* rather than about itself: "Standards Track
or BCP RFCs are required to register a code point in the Standards Action range.
… The fact that the Standards Action range is only available to Standards Track
documents does not mean that a Standards Track document cannot have points
assigned outside of that range."

> **[analysis]** Put §10.4 beside §10's opening — "IANA has updated all COSE
> registries except for "COSE Header Parameters" and "COSE Key Common
> Parameters" to point to this document instead of [RFC8152]" — and the
> arrangement resolves. RFC 9053 did not allocate the algorithm code points; it
> inherited the rows from RFC 8152 (July 2017) and IANA re-pointed their
> Reference column. The only row it newly adds is `IV-GENERATION` = 34, marked
> Recommended: **No** with an empty Capabilities column. An Informational
> document is thus the citation of record for 42 code points it did not
> allocate. Nothing in the document says this; it is the only reading on which
> §10 and §10.4 are consistent.

**What it means for citing it as the algorithm source.** Three rules for the
ADR and for `R-I-01`'s mapping table:

1. **Cite the registry for the number, and RFC 9053 for the constraint.**
   "ES256 = −7" is an IANA "COSE Algorithms" assignment for which RFC 9053 is
   the Reference. "ES256 requires `kty` EC2, admits only P-256/P-384/P-521, and
   encodes its signature as `I2OSP(R,n)‖I2OSP(S,n)`" is §2.1, and is
   Informational text.
2. **Never cite RFC 9053 alone.** Our own record carries
   `updated_by: rfc-9864`. A citation of 9053 without 9864 is incomplete by this
   library's own relation graph.
3. **Do not treat Informational as weak.** It is IETF consensus and
   IESG-approved, and RFC 9052 — an Internet Standard — normatively depends on
   it for every algorithm it can be used with. The practical consequence of the
   Informational category here is narrower than it sounds: it constrains which
   *registry range* the document may allocate in (§10.4), not how much weight its
   algorithm constraints carry.

> **[analysis]** The sharper standing problem is not the category, it is §1.4:
> "the CBOR data objects defined here are described in prose" and the CDDL
> descriptions are "(non-normative)". So the normative content of the
> algorithm half of COSE is **prose in an Informational document**, with no
> machine-checkable rendering anywhere upstream. That is why four of the five
> files in `schema/` are ours and why `R-O-03`'s "cited, not invented silently"
> has to be discharged by filename convention rather than by citation: there is
> nothing to cite.

### 4. Where this document cuts against MD-3

`MD-3` is a dated **narrowing** of DEC-002, taken 2026-09-28, not an acceptance
of it, and `docs/extraction.md` requires this section to say where the source
supports a different option or exposes a cost option 5 pays. Five places. Two
support option 5, three do not.

**(a) The option-5 / option-2 distinction does not bite where we touch COSE.
Favours: option 2 as originally written.** `ADR-0001`'s ground for constraining
DEC-002 is that "CBOR tags and COSE header parameters are IANA allocated, so
they are interchange, not native", and option 5's own wording is "no native use
of COSE header parameters". On the only path `R-I-03` requires — a signed
export — RFC 9053 defines **no algorithm-specific header parameters at all**
(item 1). The entire registry dependence of our export reduces to one label,
`alg` = 1, which is RFC 9052's and not RFC 9053's, carrying one integer from a
four-row table. **Option 2 and option 5 produce byte-identical exports on the
signing path.** The narrowing's *conclusion* may well be right; its stated
*reason* does not distinguish the two options here, and an ADR that repeats the
reason without this qualification is overstating its evidence.

**(b) Curve substitution has a registry-shaped mitigation and no other.
Favours: a closed carve-out in P1, i.e. option 2's registry identifiers for the
cryptographic sub-vocabulary.** §2.1.1, on changing the curve used to validate a
signature: "The only requirements on the new curve are that its order be the
same as the old one and that it be acceptable to the client. … **We currently do
not have any way to deal with this version of the attack except to restrict the
overall set of curves that can be used.**"

> **[analysis]** The phrase — "the overall set of curves that can be used" — names
> a *global* predicate. Under P1, where an identifier is `(defining key, local
> label)`, there is no overall set
> — two principals may each define a label that names a 256-bit curve and
> nothing in the encoding relates them. The mitigation COSE relies on is
> unstateable in a key-relative namespace. `ADR-0001`'s enumeration of extension
> points is "type identifiers, predicate types, tags, header parameters" and
> does **not** name algorithms, curves or key types; §2.1.1 is the reason that
> list must stay closed, and the DEC-002 ADR should say so in a sentence rather
> than leaving it to be inferred. This is the one place in the COSE set where a
> central registry does work key-relative naming cannot, and it is not a small
> place: it is the integrity of the signature itself.

**(c) Neither §9 requires the transmitted bytes to be deterministic. Favours:
option 1 (canonical S-expressions).** Item 1 establishes the scoping. Canonical
S-expressions are canonical *by construction* — length-prefixed, one encoding
per value — so option 1 inherits determinism from its encoding and needs no
profile to get it. Option 5 must author a determinism profile for the native
form **and** accept that the export bytes are deterministic only because we
chose to make them so, with the citation pointing to RFC 8949 §4.2.1 rather than
to anything in COSE. `DECISIONS-0001`'s standing note already records option 1
as "on the right side of all four of those grounds" that withdraw option 3;
**this is a fifth ground, and it is new.** What still stops option 1 being a
conclusion is unchanged: "a far poorer data model and library availability,
which DEC-002 names as a driver."

**(d) Three registry pathologies that `(defining key, label)` does not have.
Favours: option 5.** Recorded because an extraction that only hunts for
counter-evidence is as useless as one that only confirms.

- **Table 8 has no Value column.** Four KDFs — "HKDF SHA-256", "HKDF SHA-512",
  "HKDF AES-MAC-128", "HKDF AES-MAC-256" — are given a name, a PRF and a
  description and **no code point**, reaching the wire only inside the compound
  identifiers −10…−13 and −25…−34. Naming a component is free under P1 and
  requires an allocation under a registry, so the registry simply did not do it.
- **`IV-GENERATION` = 34 overloads the registry.** §6.1.2: "If HKDF is used for
  generating the IV, the algorithm identifier is set to 34 ("IV-GENERATION")" —
  which is the `AlgorithmID` field of `COSE_KDF_Context`, never an `alg` header.
  "COSE Algorithms" therefore holds two namespaces in one column, with the
  constraint stated only in one sentence of §6.1.2. [analysis] Under P1 the two
  uses would be two labels in two namespaces and the overload could not arise.
  Note the cost is one we never pay: we never build a `COSE_KDF_Context`.
- **§8 makes capability lists immutable and pays for it in code points.** "If it
  is later found that a new capability is needed for a key type or algorithm, it
  will require that a new code point be assigned to deal with that." A
  named-field map does not have this property.

**(e) If only one envelope ships in v1, this document is an argument for DSSE
first. Favours: option 3's envelope.** `R-I-03` requires "at least one envelope
in v1", and option 5 keeps both. But item 1's P1 collision is specific to COSE:
a COSE type identifier is an integer in a registry-governed header map, and our
`(defining key, label)` can only ride there as a parameter a stock verifier must
either ignore or refuse. DSSE's payload type is a **string the signer chooses**,
and `R-M-12` / P1 is satisfiable in it with no registry and no `crit` dilemma.

> **[analysis]** This inverts the SCITT-alignment driver `MD-3` leaned on.
> SCITT alignment is a real argument for COSE, and `ARCH-0001` §3.2 lists
> `COSE_Sign1` as the SCITT envelope — but SCITT alignment is an argument about
> *who will read our exports*, not about *whether our type identity survives the
> export*, and on the second question COSE is the worse of the two envelopes for
> precisely the reason P1 was adopted. If v1 ships one envelope, the evidence
> here says DSSE; if it ships COSE first, the ADR owes an explicit statement
> that the native type identifier is carried unenforced. Either is defensible.
> Neither is what MD-3 says, because MD-3 did not reach the question.

**What this section does not say.** None of (a)–(e) reopens `MD-3`, and
`DECISIONS-0001` is explicit that the library's findings do not: "This does not
reopen MD-3 and nobody should read it as doing so. It is the material the ADR
must answer, and the reason the ADR is the decision rather than the minute."
(a), (b) and (e) are material for item **4b**, the DEC-002 ADR, due **Oct 28**.

### 5. DEC-003 — what `KeyId` must digest, settled by two sentences

`ARCH-0001` §4.1 defines `KeyId` as "Digest of a canonical key encoding
(algorithm of digest is parameterized)", and DEC-003 lists "COSE key thumbprint"
among five options with the note "Must specify: canonical key bytes before
hashing."

Two sentences in this document decide what those bytes must contain.
§2.2.1: "Public values are computed differently in EdDSA and Elliptic Curve
Diffie-Hellman (ECDH); for this reason, the public key from one should not be
used with the other algorithm." And Table 18, which binds X25519 (4) / X448 (5)
to ECDH and Ed25519 (6) / Ed448 (7) to EdDSA.

> **[analysis]** An OKP key is `{kty, crv, x}` and `x` is an opaque byte string
> of the same length for Ed25519 and X25519. **`crv` is the only field that
> distinguishes them.** A `KeyId` digested over `x` alone — or over any
> "canonical key encoding" that omits `crv` — assigns one identifier to a
> signing key and an ECDH key that must not be interchanged, which is a
> collision in the identifier space `ARCH-0001` R-O-01 builds on ("Every signed
> object SHALL have an issuer key that can be specified as `KeyId`"). This
> lane's `rfc-9679` extraction shows the thumbprint input includes `kty` (1) and
> `crv` (−1) for both OKP and EC2, so **DEC-003 choosing RFC 9679 closes the
> hole and DEC-003 choosing "a canonical key encoding" unqualified does not.**
> Add §7.1.1's `y`-as-bool ambiguity (*What we reject*) and the conclusion is
> the same from two directions.

A third, smaller DEC-003 input: §6.3.1's "static key id" (Table 15, label −3) is
a bare `bstr` and the document never says it is RFC 9052's `kid`, nor how it is
derived. COSE shipped a key identifier with no stated derivation and needed
RFC 9679, five years later, to give it one.

---

## Open questions

1. **Does our export carry the `COSE_Sign1` tag (`#6.18`)?** Option 5 declines
   the CBOR Tags registry; RFC 9052 defines both the tagged and untagged forms.
   Untagged means the recipient is told out of band which message type the bytes
   are — the same out-of-band dependence §8.3's capability sequence has
   (`examples/README.md`). Owner: the DEC-002 ADR.
2. **Which signature algorithms does the profile name, and is ES512 in it?**
   This extraction's reading is ES256 and EdDSA/Ed25519, on §2.2.1 (fixture
   determinism) and §2.2 (two passes) respectively. ES512's 132-byte signature
   and §2.1's hash-truncation rule are both unexercised corners with no vector
   behind them; naming it buys reach and costs a test surface nothing upstream
   tests.
3. **Does the exported protected header carry our `(defining key, label)` type
   identifier at all?** Item 1 shows both answers cost something. A third
   option — carry it only in the payload, and let the COSE header hold nothing
   but `alg` and `kid` — keeps the export clean and makes the type invisible to
   any COSE-aware tooling, including SCITT. Not obviously wrong; not currently
   written down anywhere.
4. **If the payload becomes a hash (item 2), what canonicalisation does the
   verifier run?** Conditions (5) and (6) of the `canonical-encoding` six — a
   canonical order for set-valued fields in arrays, and a declared Unicode
   normalisation rule — move from unstated to security-critical. `mofn#72`
   owns condition (2); nothing owns (5) and (6).
5. **Does RFC 9864 change any of the above?** It `updates` RFC 9053 and this
   record names it in `relations.updated_by`. Nothing in this extraction has
   been checked against it, and rule 2 of *Standing* says a citation of 9053
   alone is incomplete.
6. **Is a deterministic-ECDSA requirement ours to impose?** §2.1 says
   implementations "SHOULD use a deterministic version of ECDSA such as the one
   defined in [RFC6979]". §2.1.1 adds that combining randomness and determinism
   addresses fault attacks, citing `[CFRG-DET-SIGS]`. For reproducible fixtures
   we need the SHOULD as a MUST; for fault resistance the cited draft says
   neither pure determinism nor pure randomness is right. The two pull apart and
   no document of ours has chosen.
