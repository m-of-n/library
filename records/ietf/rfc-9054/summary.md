---
schema: "library-summary/v1"
id: rfc-9054
record: rfc-9054
type: summary
updated: "2026-10-20"
---

# CBOR Object Signing and Encryption (COSE): Hash Algorithms

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | informational — "This document is not an Internet Standards Track specification; it is published for informational purposes" (Status of This Memo; Category: Informational) |
| **Authors** | J. Schaad |
| **Published** | August 2022 |
| **Identifier** | RFC 9054 · DOI 10.17487/RFC9054 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9054.txt |
| **Digest** | `75a6bf62b4226baa1e14ccdcc4c603b8a039084ad79677db029e0bbec4525e6f` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

Eight hash algorithm identifiers in the "COSE Algorithms" registry, and
deliberately nothing else. §1 states that COSE defines no digested-object
structure "along the lines of the DigestedData ASN.1 structure in [CMS]" and
that "This omission was intentional", because algorithm plus content plus
digest "does not, by itself, provide any strong security service" — so the
document supplies identifiers for two named uses, **indirect signing** (sign a
hash and a pointer, download the content later) and **object identification**
(certificate fingerprints), and leaves the carrier to the application.

Its one structural contribution is a change to registry *semantics*: a new
**"Filter Only"** value in the Recommended column (§2, §4.1), marking an
algorithm fit only for narrowing a candidate set and "not to be used for
purposes that require collision resistance". The eight values are SHA-1
(−14, Filter Only), SHA-256/64 (−15, Filter Only), SHA-256 (−16),
SHA-512/256 (−17), SHAKE128 (−18), SHA-384 (−43), SHA-512 (−44) and
SHAKE256 (−45), each with an empty COSE capabilities array (§3.1–§3.3).

It is Informational and it reads like it: **two operative BCP 14 statements in
the whole document**, both in §2 and both SHOULD-strength. There is no MUST
anywhere outside the §1.1 boilerplate.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | It registers identifiers and warns about them; every security property is deferred to the application's own analysis (§2, §5). |
| Cryptography | **core** | It is the identifier space for *which hash*, which is the first field of every digest we emit. `DEC-005`. |
| This project | **core** | `R-M-07` requires an artifact statement to bind a content digest, and `R-O-03` requires the algorithm to be **cited, not invented silently**. This is the citation. |

**The finding to act on: it names the algorithm and refuses the carrier, so
`R-M-07`'s content digest has an identifier and no structure to travel in.**
§1 and §2.1 both say so — "[COSE] did not provide a default structure for
holding a hash value". The two structures §2.1 prints are explicitly examples,
and one of them does not work: `COSE_Hash_V` uses `#` for CDDL comments where
CDDL uses `;` (**erratum 7335**, status *Reported*, checked 2026-10-20), and `#`
is CDDL's tag operator, so the fragment does not parse; once that is fixed it is
still a parenthesised **group**, not a type, so it cannot be instantiated
without a `{ }` wrapper the document never supplies. `COSE_Hash_Find` is a
proper array type and does parse. So of the two offered digest carriers, one is
unusable as printed and neither is normative.

The consequence for us is exact. Citing `-16` for SHA-256 discharges the
algorithm half of `R-O-03`; **the four-field hash structure around it —
algorithm, value, pointer to what was hashed, additional data (§2.1) — is ours
to invent, with no COSE citation available.** §2.1 does leave one piece of
advice worth lifting, and it is a canonicalization rule in disguise: additional
data must either be of fixed known size or have the lengths of the hashed
pieces included, "so that the resulting byte string has a unique interpretation
as the additional data. (Encoding as a CBOR array accomplishes this
requirement.)"

**On SHA-1 and truncation, which are constraints on us, not trivia.** §3.1
registers SHA-1 at −14 while saying it "should no longer be used", citing the
2017 full collision and RFC 6194; the registration exists only because "there
are still times where SHA-1 needs to be used" — unreplaceable HSMs, and
filtering. §3.2 registers **SHA-256/64** at −15, a 64-bit truncation of SHA-256
defined *in this document* (§3.2's note separates it from FIPS 180-4's
SHA-512/256, which is a different construction), and requires that its use
"requires analysis of the potential problems that could result from a
collision, or it must be limited to where the purpose of the hash is
noncryptographic". §3.3 declines to register short SHAKE lengths at all. §2
carries the only two normative sentences: a hash susceptible to practical
collision attacks "SHOULD NOT be used for a cryptographic purpose", and
theoretical collision attacks "SHOULD trigger" a suitability review.

**But "Filter Only" is a registry column, not a wire field.** An algorithm
identifier tells a verifier *which* H; nothing in COSE tells it whether that H
was fit for the purpose it was used for. The fitness judgement lives in a
registry a verifier is not required to consult and in a document with no MUSTs.
`rfc-9360` is where that gap becomes exploitable — see its summary, and the
`contradicts` edge it carries to this record.

**Where it meets `rfc-9679`, and the answer is nowhere.** `rfc-9679` (COSE Key
Thumbprint, `profile: full` here) is the candidate definition of `KeyId` under
`DEC-003`. It **cites RFC 9054 zero times and never mentions the "COSE
Algorithms" registry at all** — its H is "chosen by the application" and, as
that record's `distilled/` records, is not carried in the thumbprint value, so
two parties on different H never match on any key and cannot tell why. So this
document does *not* supply the identifier space RFC 9679 selects from, because
RFC 9679 names no identifier space. That makes RFC 9054 the available *remedy*
rather than a dependency: **`-16` is the citation that would close RFC 9679's
algorithm-agility hole, and RFC 9679 cannot reach it.** The shape is the same as
the `rfc-8230` edge `rfc-9679` already carries — a rule that exists and is
unreachable from the document that needs it. `see_also: rfc-9679` records it
from this side.

On `DEC-003` specifically: this document answers the *hash identifier* half of
the mandatory clause and is silent on the half `DEC-003` calls mandatory —
**canonical key bytes before hashing**. It says nothing about what gets hashed,
anywhere, for anything.

## Implementations

The RFC names none and has no implementation-status section. It registers
identifiers for algorithms specified elsewhere — FIPS 180-4, FIPS 202 and
RFC 3174 — so an implementation is any hash library plus a lookup table; there
is no RFC 9054 code to build on and none to look for. *Searched on 2026-10-20
for an implementation named by the document: none, and none is owed.* The one
dependency worth recording instead is **downstream**: `rfc-9964` (ML-DSA in
COSE, Standards Track) cites RFC 9054 in its **§9.1 Normative References** and
uses it with RFC 9053 as the template for its own registration actions
(§8.1.1) — so an Informational document is a normative reference of a
Standards Track one, the same standing problem `rfc-9052`'s record raises about
RFC 9053.

| Name | Kind | License | URL |
|---|---|---|---|
| _none named by the document_ | — | — | — |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`, and none is owed yet.** This PR claims the **summary bar**:
the record is `summarized`, declares no `distillation` block, and touches no
`distilled/`, so FX-1 does not fire (`docs/extraction.md`). The judgement is
proportionate rather than economical — the whole normative content is eight
registry rows, two SHOULD-strength sentences and one registry-column
definition, and the two CDDL fragments are non-normative examples, one of which
does not parse. **What would trigger an extraction** is a decision to make
either §2.1 structure the basis of our own digest carrier; `requirements.yaml`
would then have to reconcile two BCP 14 statements, and `schema/` would have to
carry a `*.derived.cddl` repair of `COSE_Hash_V` with erratum 7335 applied —
work that only makes sense once `R-M-07`'s carrier is being designed. No issue
owns that today.

**No verbatim normative text here.** Under FX-1 that belongs in
`distilled/normative.md` with its locator; in a summary the rule is to cite the
§ and let the reader open the source, so the fragments quoted above are short
and locator-bearing by design.

**No examples or test vectors, in the record or in the source.** The RFC prints
not one digest value and not one encoded identifier, so there is nothing to
hold as a fixture. Any vector we want is ours to compute.

## Limits

1. **It settles no digest structure, and that is the whole of what we needed.**
   §1 calls the omission intentional and argues the application is "better off
   defining this type of structure" itself. Reasonable for COSE; it means
   `R-M-07` and `R-O-03` cannot both be satisfied by citation alone on the COSE
   path. **`DEC-002` option 1 (canonical S-expressions) is ahead here**, and
   this is a datum rather than a point scored: SPKI defines `(hash sha1 |…|)`
   as a self-describing hash object (`rfc-2693` §2.8, §7.3), so the carrier
   *and* the algorithm name are cited together. COSE gives the algorithm number
   and nothing to put it in.
2. **"Filter Only" is unenforceable and invisible.** It is defined in an
   Informational document with no MUST, lives in a registry column, and is not
   carried on the wire. A verifier handed `[-14, h'…']` cannot tell whether the
   sender was filtering or binding. Every use of −14 or −15 that matters
   therefore needs an *application* rule, and ours has to say so explicitly.
3. **§2's SHOULD NOT is conditioned on a judgement no implementation can
   make.** "A hash function that is susceptible to practical collision attacks
   SHOULD NOT be used for a cryptographic purpose" — "practical" is a moving
   target by the document's own admission (§5: "the cryptographic strength of
   hash algorithms will be reduced over time"), and §2's escape hatch is wide:
   the only reason to use such a function "is when there is absolutely no other
   choice (e.g., a Hardware Security Module (HSM) that cannot be replaced)".
   That is a deployment excuse promoted to a specification clause.
4. **SHA-256/64 is a new truncation defined in a document that registers
   rather than specifies.** §3.2's note is the whole of its definition — "a
   simple truncation of SHA-256 to 64 bits defined in this specification" —
   with no statement of which 64 bits (leading, by convention, and the document
   does not say so) and no test vector. An interoperability hazard in one
   sentence, in an Informational RFC.
5. **It neither constrains nor is constrained by `rfc-9679`.** Checked both
   directions: 0 citations of RFC 9054 in RFC 9679, and RFC 9054's
   object-identification case is certificates rather than keys (§1, citing
   [ESS] and [COSE-x509]). The two documents that between them should have
   settled "which hash names a key" do not meet, and `DEC-003` inherits the
   join.
6. **Nothing here is about agility in a protocol, only about agility as
   advice.** §2 and §5 both say algorithm agility "needs to be considered a
   requirement" and cite BCP 201, but the document defines no negotiation, no
   downgrade rule, no deprecation mechanism and no way to express "this
   endpoint accepts these H". `rfc-9360` §2's "MUST support SHA-256" is the
   only mandatory-to-implement floor anywhere in this lane, and it is in the
   other document.

## Where it cuts against MD-3

**It does not cut, and the reason is worth recording rather than omitting.**
MD-3 narrowed `DEC-002` to option 5 — reduced CBOR, no IANA tags, COSE export
only. RFC 9054 registers **zero CBOR tags**: the string "tag" occurs once in
the whole document and it is the word "tagged" in §4.1's prose about the
Recommended column. Its eight allocations are negative integers in the COSE
Algorithms registry, which option 5 already accepts by keeping COSE as the
export form, and §4.1's rationale for two-byte identifiers is a size argument
that agrees with "reduced CBOR" rather than straining it.

**The cost it exposes is one layer down from where option 5's exclusions
operate**, and that is the part the `DEC-002` ADR should hear. Option 5 says
"no IANA tags"; this document shows the expensive dependency is not tags but
the *absent structure* — COSE has no digest carrier at all (§1, §2.1), so under
any COSE-exporting option our digest-bearing structure is a native invention
that `R-O-03` then obliges us to cite, and there is nothing to cite. Option 1
does not pay that cost (`rfc-2693` §2.8's `(hash …)` form). This is the same
shape `rfc-9165`'s extraction found one layer up — option 5 is
*registry-reduced, not registry-free* — and the same shape `rfc-9360`'s record
finds one layer down, where the exclusion operates on CBOR and the content is
ASN.1. **Three records in this lane now agree that option 5's exclusion clause
names the wrong layer to be the defence it reads like.** That convergence, not
this document alone, is the evidence.
