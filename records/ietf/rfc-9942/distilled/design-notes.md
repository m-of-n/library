---
record: rfc-9942
kind: design-notes
title: "rfc-9942 — bearing on our design"
extracted: "2026-09-30"
reviewed_by: ""
---

RFC 9942 is the receipt format the SCITT architecture depends on: a
`COSE_Sign1` whose payload is a Merkle Tree root, whose protected header names
the data structure that root belongs to, and whose unprotected header carries
the path a verifier walks to recompute that root from an entry it holds
(§4.3 Figure 1, §5.2.1). It is a small document — three header parameters,
one data structure, two proof types — and it is the hardest document in this
library to reconcile with our own encoding decision, because every one of
those four things is an IANA registration and one of them is a registration a
*verifier* is obliged to consult (§4.3).

Everything below about RFC 9942 is derived from the source text
(`content.sha256: da8ed24e…`), never from our summary, and carries the RFC's
own section and figure numbers. Requirement ids of the form `R-00NN` refer to
`distilled/requirements.yaml` in this record.

**Three of the ids this file maps to are not defined inside this repository.**
`DEC-005` and `R-M-12` have no in-repo definition at all; `D-3` is a meeting
decision glossed in a single line of `docs/extraction.md`. Every statement
below about what one of them *means* is a **reconstruction** supplied to the
extraction, not something this repository can resolve. Each point of reliance
is marked **[gloss]** and the reconstructions are itemised in
*Mapping to our decisions → Where we relied on a reconstructed gloss*.

---

## What we adopt

**A1 — The proof payload is registry-free, and that is the part worth
taking.** This is the single most important observation in the file, because
it is what makes the rest of the collision tractable. Strip the labels and a
proof is a flat CBOR array of integers and byte strings with no identifier in
it at all:

> `inclusion-proof-content = [ tree-size: uint, leaf-index: uint,
> inclusion-path: [ + bstr ] ]` — §5.2 Figure 3

> `consistency-proof-content = [ tree-size-1: uint, tree-size-2: uint,
> consistency-path: [ + bstr ] ]` — §5.3 Figure 7

Nothing in either structure needs a registry to be read, written, or
verified. The registry dependency in RFC 9942 lives entirely in the *labels*
that address these structures (394, 395, 396, -1, -2) and in the *identifier*
that selects between them (`395: 1`, §5.1). We adopt both proof-content
structures **verbatim, field for field, including the field order**, and we
adopt none of the labels. That is the whole shape of our answer to D-3 for
this document, and it is cheap because the authors put the semantics in the
arrays and the registry dependency only in the addressing.

**A2 — The payload is the root, and the verifier computes it.** §5.2.1 makes
the verifier construct the thing the signature covers:

> "Inclusion Proof Verification: The verifier applies the inclusion proof to
> the bytes of a candidate entry. If this fails, the proof is invalid. If it
> succeeds, the resulting Merkle Tree root becomes the COSE_Sign1 payload." —
> §5.2.1, step 1

This is the correct binding and we adopt it unchanged. The signature is over
a root; the proof is the only way to arrive at that root from an entry; so a
forged proof produces a different root and the signature fails. The entry, the
proof and the signature are bound into one object without any field having to
cross-reference another. Our witness verification is this, in this order, for
inclusion.

**A3 — The structure identifier is inside the signature; the proof is
outside it.** `alg` (1) and `vds` (395) are both REQUIRED in the **protected**
header (§5.2.1 Figure 4, §5.3.1 Figure 8 — R-0010, R-0011, R-0015, R-0016),
while `vdp` (396) and the proof arrays sit in the **unprotected** header
(§5.2.1 Figure 5, §5.3.1 — R-0012, R-0013, R-0017, R-0018). The RFC states the
reason for the first half:

> "The VDS in the protected header is necessary to understand the inclusion
> proof structure in the unprotected header." — §5.2.1 (and verbatim again at
> §5.3.1 for consistency)

We adopt the split and the reasoning behind it. The *interpretation rule* for
the proof must be authenticated, because a verifier that can be told to read a
proof under the wrong rule can be attacked. The *proof itself* need not be,
because it is checked by reconstruction, not by trust. Our witness object puts
the structure name and the signature algorithm inside the signature and the
path outside it.

**A4 — A single boolean is the right verification API.** §5.3.1 ends with an
unusual piece of advice:

> "It is recommended that implementations return a single boolean result for
> Receipt-verification operations to reduce the chance of accepting a valid
> signature over an invalid consistency proof." — §5.3.1 (R-0020)

A specification recommending a *coarser* API to stop implementers misusing the
finer one is an admission about how easy this is to get wrong, and the
admission is more valuable than the advice. We adopt it as a rule rather than
a recommendation: our witness verification exposes one entry point returning
one boolean, and the per-step results are not reachable from outside the
verifier. The failure mode it guards against — a caller that checks the
signature result and forgets the proof result — is a two-line bug in any
language with multiple return values, and it silently converts an append-only
guarantee into a bare signature check. See B2 for the half of this we
strengthen.

**A5 — Pair the signature hash with the structure hash.** §7.1:

> "It is recommended to select signature algorithms that share cryptographic
> components with the VDS used; for example, both RFC9162_SHA256 and ES256
> depend on the SHA256 hash function." — §7.1 (R-0023)

A concrete, testable design constraint, and a cheap one. A receipt signed with
an algorithm stronger than its tree hash is misleading about its own strength;
one signed with a weaker algorithm wastes the tree. We adopt this as a
constraint our witness profile states, and our algorithm table pairs each
structure with the signature algorithms whose hash matches it. §7.1's first
sentence — "A security analysis ought to be performed to ensure that the
digital signature algorithm alg has the appropriate strength to secure
receipts" (R-0022) — is lowercase and therefore advisory; the pairing rule is
the part that can be checked mechanically.

**A6 — Many witnesses, ordered.** Label 394 takes an array, and Table 1
describes it as a "Priority ordered sequence of CBOR encoded Receipts" (§8.1
Table 1); §4.3's Figure 1 types it `[+ bstr .cbor Receipt]` — one or more, not
zero or more. Figure 2 (§4.3) shows two receipts over the same statement from
different tree sizes. We adopt the cardinality and the ordering: a witness
list, order-significant, non-empty when present. One witness is a single point
of failure and the format already says so.

**A7 — Receipts are stored as the bytes we received.** §3 defines a Receipt as
"A COSE Single Signer Data Object, as defined in RFC 9052 of [STD96],
containing the header parameters necessary to convey one or more VDP for an
associated VDS", and §4.3 requires "Receipts MUST be tagged as COSE_Sign1"
(R-0003). A receipt is signed by someone else over bytes we did not choose, so
re-encoding it destroys it. Our *witnesses* field holds the received bytes
exactly, and any native view we build of a receipt is a derived projection
with no authority. This sounds obvious and it is the thing D-3 did not
anticipate; see the import-asymmetry finding in *Mapping to our decisions*.

---

## What we adapt, and how

**B1 — The detached payload becomes mandatory.** §4.4 states the mitigation
for the central attack on this format and then declines to require it:

> "New VDSs can require the definition of a profile. The payload in such
> definitions SHOULD be detached. Detached payloads force verifiers to
> recompute the root from the proof and protect against implementation errors
> where the signature is verified but the payload is incompatible with the
> proof." — §4.4 (R-0004 carries the SHOULD sentence)

Read that against A2 and A3 together. The proof sits in the unprotected header
(§5.2.1 Figure 5), so it is not covered by the receipt's signature; the
signature covers only `alg`, `vds` and the root. If the root is **attached**,
an implementation can verify the signature over the attached root, never
recompute anything, and report success — and the proof in the unprotected
header can be anything at all, including a proof for a different entry, since
nothing signed constrains it. Detaching the payload is what closes that hole,
because a verifier with no payload has no choice but to derive one from the
proof.

Three things make the SHOULD weaker than it first appears. It is addressed to
**profile authors for new VDSs**, not to issuers of the one VDS this document
defines (§4.4's subject is "New VDSs"). For `RFC9162_SHA256` inclusion
receipts, detachment appears only in an example, parenthetically — "An EDN
example for a Receipt containing an inclusion proof for RFC9162_SHA256 with a
detached payload (see Section 4.4)" (§5.2.1) — and the CDDL permits either,
`payload : bstr / nil` (§4.3 Figure 1). And the structure's grammar therefore
admits the vulnerable form at every level. §5.3.1 is firmer for consistency —
"the newer Merkle Tree root … is a detached payload" is declarative — but
that is one of the two proof types, stated in prose, with the same permissive
CDDL behind it.

We adapt by inverting the modality: in our witness profile the root **MUST**
be absent from the stored witness, and a witness carrying a root is invalid on
receipt rather than merely discouraged. The cost is nil — the root is
recomputable by definition — and the benefit is that the misuse A4 guards
against at the API level becomes unrepresentable at the data level. A
mitigation that is both free and mandatory is the right shape for the one
attack a format exists to prevent.

**B2 — One verification order, not two.** The two proof types are given
opposite orders in the same document:

| | order | source |
|---|---|---|
| inclusion | proof, then signature | "Verification of the inclusion proof and signature occurs in two sequential steps: 1. Inclusion Proof Verification … 2. Signature Verification" — §5.2.1 |
| consistency | signature, then proof | "The signature and consistency proof are verified in order. First, the verifier checks the signature on the COSE_Sign1. If the verification fails, the consistency proof is not checked. Second, the consistency proof is checked by applying a previous inclusion proof to the consistency proof." — §5.3.1 |

For inclusion the order is forced and correct: the proof *produces* the
payload (A2), so it cannot run second. For consistency the stated order is in
tension with the stated detachment in the same subsection. If the newer root
is a detached payload, a verifier cannot check the signature first without
obtaining that root from somewhere outside the receipt; and if it obtains it
by applying the consistency path, then the proof ran first and §5.3.1's own
sentence is wrong about its own document. §5.3.1 also warns that "This
approach is specific to RFC9162_SHA256; different VDSs may not support
consistency proofs," so the order is not even general within RFC 9942.

We adapt to one order for all witness kinds: **derive the root from the proof,
then verify the signature over the derived root.** It is A2 generalised, it is
the only order compatible with B1's mandatory detachment, and it removes a
per-proof-type branch from the verifier — which is exactly the class of
branch A4 exists to protect implementers from. Recorded as a possible source
defect in O5.

**B3 — Registry membership becomes a profile check, not a registry
lookup.** §4.3's verifier obligation is the collision in one sentence:

> "When the "receipts" header parameter is present, the verifier MUST confirm
> that the associated VDS and VDPs match entries present in the registries
> established in this specification, including values added in subsequent
> registrations." — §4.3 (R-0002)

The trailing clause is what makes this more than identifier consumption.
"Including values added in subsequent registrations" means a conforming
verifier's accept set is not fixed at the time it is written: it is the live
state of two IANA subregistries. Two implementations of RFC 9942, both
correct, disagree about whether a receipt verifies, and which one is right
depends on when each last read `iana.org`. The registry becomes a runtime
input to a cryptographic verification.

We adapt by keeping the *shape* of the obligation and changing its *source of
truth*: our verifier MUST confirm that the structure name and proof-kind names
in a witness are ones our own profile defines, and MUST reject a witness
naming anything else. That is a closed set, versioned with our specification,
checkable offline, and identical in every implementation of a given version.
It satisfies the security purpose of R-0002 — do not interpret a proof under a
rule you do not know — without making verification depend on a service we do
not operate. The price is stated honestly in C1: we lose automatic forward
compatibility with VDSs registered after our version ships, and gaining a new
structure becomes a version of our spec rather than a fetch.

**B4 — The identifier becomes a name, not an integer.** §5.1 gives both forms:
"The integer identifier for this VDS is 1. The string identifier for this VDS
is "RFC9162_SHA256"" (§5.1, and Table 2 at §8.2.2.1). The integer is the
registry allocation; the string is self-describing and was not allocated to
anyone. We carry the name. Under D-3's "reduced CBOR" the cost is a handful of
bytes per witness, paid once per witness, against a decoder that needs no
allocation table to say what it is looking at. **[gloss — D-3]** On export the
name maps to `395: 1` by an explicit two-column table in our specification,
which is the only place the integer 1 appears in our system.

**B5 — The privacy analysis obligation is adopted and widened.** §6.2 is the
one MUST in the document aimed at the producer rather than the verifier:

> "The receipt producer MUST perform a privacy analysis for all mandatory
> fields in profiles based on this specification." — §6.2 (R-0021)

Scoped to mandatory fields in profiles, which leaves the optional fields and
the base document's own leakage outside it. We adopt the obligation and widen
it to every field we define, mandatory or not, because §6.1's own example is
about a field nobody would have flagged as sensitive — see B6.

**B6 — `tree-size` is a disclosure and must be treated as one.** §6.1:

> "Some structures and proofs leak the size of the log at the time of
> inclusion. In the case that a log only stores certain kinds of information,
> this can reveal details that could impact reputation. For example, if a
> transparency log only stored breach notices, a receipt for a breach notice
> would reveal the number of previous breaches at the time the notice was
> made transparent." — §6.1

This is not avoidable within the format: `tree-size` is the first field of an
inclusion proof and `tree-size-1`/`tree-size-2` are the first two fields of a
consistency proof (§5.2 Figure 3, §5.3 Figure 7), and the proof cannot be
verified without them. So every receipt a witness ever issues carries an
approximate count of everything that witness had ever seen, and two receipts
from the same witness bound how much happened between them. We adapt by
recording this as a property of our witness profile rather than a
consideration: a witness's log is **semantically homogeneous at the witness's
own choosing, and a single-purpose log is a counter published to every
relying party**. Our guidance is that a witness serving a narrow statement
class is a privacy decision, not an operational one. We cannot fix the format;
we can refuse to let the leak be discovered by whoever deploys it.

**B7 — Profiles make their own extensions mandatory.** §4.4: "Profiles of
proof signatures that define additional protected header parameters are
encouraged to make their presence mandatory to ensure that claims are
processed with their intended semantics" (R-0005), with §4.4 pointing at the
`typ` header parameter (RFC 9596, RFC 9597) as one way to carry the
information. The underlying rule is sound and generalises past COSE: an
optional field that changes the meaning of the fields around it is a field
that can be stripped to change meaning. We adapt it into our own rule — any
field in our witness profile that alters the interpretation of another field
is mandatory and inside the signature — and we decline the mechanism, since
`typ` is another registry-defined header parameter (C2). Our structure name,
already mandatory and already inside the signature per A3, is doing the work
`typ` would do.

---

## What we reject, and why

**C1 — Registry-dependent verification (§4.3, R-0002). Rejected, and this is
the one real cost.** The reasoning is in B3; what belongs here is the honest
accounting of what rejecting it loses. It loses conformance: a system that
does not consult the IANA subregistries is not a conforming RFC 9942 verifier,
whatever else it does correctly, because R-0002 is a MUST on the verifier. It
loses forward compatibility by construction — a VDS registered next year
verifies in a conforming implementation and does not verify in ours until we
ship a version. And it loses the ability to make the claim "we verify COSE
Receipts" without qualification; the honest claim is "we verify COSE Receipts
for the structures our profile names". We accept all three, because the
alternative is a verifier whose accept set is mutable by a third party, and a
cryptographic check whose result depends on network state is not a
cryptographic check. Note what we are *not* rejecting: nothing stops us
consulting the registry at specification-authoring time to choose compatible
values, which is a build-time dependency and harmless.

**C2 — The three header parameters as labels (394, 395, 396; §2, §8.1
Table 1). Rejected under D-3.** These are burned allocations in the
`'Integer values from 256 to 65535'` range of the "COSE Header Parameters"
subregistry under a Specification Required procedure (§8.1, citing RFC 8126).
They cost us nothing to *use* — the allocations are already made — and the
reason to decline them is the one R-M-12 names: adopting them puts the meaning
of our fields in a registry we do not control and in documents we have not
extracted. **[gloss — R-M-12]** Our fields are named by role in a schema we
version. The labels appear in exactly one place, the export table.

**C3 — The two new subregistries as our extension mechanism (§8.2).
Rejected.** This is the level at which RFC 9942 is not merely a registry
*consumer* but a registry *author*: IANA "has established the "COSE Verifiable
Data Structure Algorithms" and "COSE Verifiable Data Structure Proofs"
subregistries under a Specification Required policy as described in Section
4.6 of [RFC8126]" (§8.2). The expert-review criteria (§8.2.1) describe a
genuinely well-designed registry — assign the next positive integer; discourage
point squatting; specifications required for all point assignments with early
allocation permissible per RFC 7120 §2; "It is not permissible to assign
points in the "COSE Verifiable Data Structure Algorithms" registry for which
no corresponding entry in the "COSE Verifiable Data Structure Proofs" registry
exists, and vice versa" (R-0027); and "The change controller for related
registrations of structures and proofs should be the same" (§8.2.1).

Those last two are the interesting ones and they are the reason this is a
*design* rejection and not just a D-3 rejection. The pairing rule and the
shared change controller exist because a structure identifier and its proof
labels are **one unit of meaning split across two registries**, and the
registry design has to work to keep the halves together. Our schema does not
have that problem: a structure and its proof kinds are declared in one place
in one document, and the invariant the expert reviewers are asked to enforce
by hand is a structural property of our definition. We reject the mechanism
and adopt the invariant — structures and their proof kinds are defined
together, versioned together, and neither can exist without the other.

**C4 — A standards action per hash algorithm (§4.4.1). Rejected as a
process.** §4.4.1 is explicit:

> "Where a specification supports a choice of hash algorithm, a separate IANA
> registration must be made for each supported algorithm. For example, to
> provide support for SHA256 and SHA3_256 with Merkle inclusion proofs and
> Merkle consistency proofs defined, respectively, in Section 2.1.3 of
> [RFC9162] and Section 2.1.4 of [RFC9162], both "RFC9162_SHA256" and
> "RFC9162_SHA3_256" require entries in the relevant IANA registries. This
> document only defines "RFC9162_SHA256"." — §4.4.1 (R-0008)

Changing hash function is therefore not a parameter in this design; it is a
standards action plus an expert review plus, under §8.2.1's pairing rule, a
matching entry in the second registry. The identifier `RFC9162_SHA256` welds
the structure and the hash into one opaque token, which is why. For a project
whose algorithm suite is deliberately deferred, a format in which the hash
agility story is "apply to IANA" is not usable as the canonical form. We
reject the coupling and separate the two: our witness names a *structure*
(binary Merkle tree, RFC 9162 construction) and a *hash* independently, both
inside the signature, both from closed sets our profile defines. Moving to
SHA3-256 is then a value change, and the migration gate we keep is RFC 9942's
own, which is a real one — "Security analysis MUST be conducted prior to
migrating to new structures to ensure the new security and privacy assumptions
are acceptable for the use case" (§4.2, R-0001).

One caution on separating them: a structure identifier that welds in the hash
cannot be misinterpreted, and two independent fields can. Our profile must
therefore enumerate the permitted (structure, hash) pairs rather than take the
cross product, which recovers the safety property of the welded token without
the registration.

**C5 — The unified envelope as a claim about interoperability (§4.2).
Rejected.** §1 motivates the document by interoperability — "The combination
of representations of various VDSs and VDP can significantly increase the
burden for implementers and create interoperability challenges for
transparency services. This document describes how to convey VDS and
associated VDP types in unified Enveloped COSE Structures" (§1) — and §4.2
withdraws it:

> "Proof Types are specific to their associated "Verifiable Data Structure";
> for example, different Merkle Trees might support different representations
> of inclusion proof or consistency proof. Implementers should not expect
> interoperability across "Verifiable Data Structures"." — §4.2

What is unified is the *envelope*: tag 18, label 395 for the structure, label
396 for the proofs. What is not unified is anything inside label 396, where
the actual proof lives. An implementation that handles the envelope handles
nothing it did not already have code for. We reject treating the envelope as
an interoperability asset, and we note the sharper form of the point: the
envelope makes a non-interoperable payload *look* uniform, which is worse than
an obviously specific format, because a receipt for an unknown structure is
syntactically indistinguishable from one the verifier can check. R-0002 is the
mitigation for exactly that — and R-0002 is the requirement we reject in C1,
so B3's closed profile check is carrying the load here too. The two are one
decision.

**C6 — CBOR tag 18 and the `#6.18` wrappers (§4.3 Figure 1). Rejected.** Three
of them per receipt-bearing statement: `Signature_With_Receipt =
#6.18(COSE_Sign1)`, `Receipt_For_Inclusion = #6.18(Signed_Inclusion_Proof)`,
`Receipt_For_Consistency = #6.18(Signed_Consistency_Proof)` (§4.3 Figure 1),
plus `Receipts MUST be tagged as COSE_Sign1` (§4.3, R-0003). A CBOR tag is a
registry allocation that in this document discriminates nothing — the same tag
marks the outer statement and both receipt kinds, so it cannot tell a verifier
which it is holding. Dropped from the canonical form, emitted on export. This
matches the sibling treatment in `records/ietf/rfc-9943/distilled/design-notes.md`.

**C7 — The optionality of the detached payload.** Rejected; see B1. Recorded
separately because it is the one place where we overrule a modality rather than
re-source or re-name a field, and it should be visible as such to a reviewer.

**C8 — Validity periods and status, as this document leaves them (§7.2,
§7.3). Rejected as a stopping point.** §7.2: "In some cases, receipts MAY
include strict validity periods, for example, activation not too far in the
future or expiration not too far in the past. See the iat, nbf, and exp claims
in [RFC8392] for one way to accomplish this. The details of expressing
validity periods are out of scope for this document" (R-0024). §7.3: "In some
cases, receipts should be "revocable" or "suspendable" after being issued,
regardless of their validity period. The details of expressing statuses are
out of scope for this document" (R-0025). Both name a requirement and decline
to meet it, which is a legitimate scoping choice for a format document and not
a legitimate position for a system. The gap this opens does not belong to
RFC 9942 alone; see the cross-record finding in *Open questions*, O2.

---

## Mapping to our decisions

<!-- ARCH-0001 / ARCH-0002 principles, DEC-*, meeting decisions D-n.
     COSE/CBOR/envelope documents MUST address D-3 (option 5: reduced CBOR,
     no IANA tags, COSE export only) and give the header/field mapping. -->

### The finding that reframes D-3 for this record: the dependency runs inbound

D-3 is glossed in `docs/extraction.md` line 36 as **"option 5: reduced CBOR,
no IANA tags, COSE as export only"**, and `docs/extraction.md` lines 35–38
require this record to give the header-by-header mapping. Before the mapping,
the thing that mapping cannot express.

"COSE as export only" assumes the COSE dependency is **outbound**: we hold a
reduced canonical form, and COSE is a projection we emit at the boundary. For
every other COSE document in this library that assumption holds. It does not
hold for RFC 9942, because **a receipt is not something we export — it is
something we receive**, signed by a party that is not us, over bytes we did
not choose. §3's definition makes the point: a Receipt is "A COSE Single
Signer Data Object, as defined in RFC 9052 of [STD96]". The witness produced
it; we cannot re-encode it without destroying the signature; and we cannot
verify it without understanding its labels.

So at the import boundary the three options are:

1. **Hold the registry knowledge.** Decode `394/395/396/-1/-2` and the IANA
   allocations behind them, verify the receipt as RFC 9942 requires, including
   R-0002's live-registry check. Conformant, and it is the thing D-3 and
   R-M-12 exist to prevent — semantic dependency on registries we do not
   control, at the heart of a verification path.
2. **Treat receipts as opaque bytes.** Store what we were handed, never look
   inside. Satisfies D-3 trivially, and destroys the receipt's entire value: an
   unverified inclusion proof is a byte string with no meaning, and the
   non-equivocation property we wanted the witness for is not obtained.
3. **Verify once at the boundary, then re-attest.** A decoder that knows the
   RFC 9942 labels lives *only* in the import adapter, outside the canonical
   form and outside anything a relying party has to implement. It verifies the
   receipt per A2/A3/B1/B2 against our closed profile (B3), stores the
   received bytes verbatim (A7), and stores alongside them a native witness
   record in our own reduced form — a projection with no authority of its own
   unless we sign it.

**Option 3 is what the mapping below assumes**, and it is a proposal, not a
decision this repository records. It is the honest reading of D-3's intent —
registry knowledge confined to an adapter at the boundary, zero registry
dependency in the canonical form or in the verification path a relying party
runs — but D-3 as glossed does not distinguish import from export, and
choosing option 3 is choosing something D-3 did not say. **[gloss — D-3]** It
also raises the question the export half does not: whether our native
projection is *trustworthy*, since it is derived by our adapter rather than
signed by the witness. See O1.

### D-3 — header by header

Our statement and witness fields are named below **by role**, not by
identifier, because the field names live in ARCH-0001 / DEC-007 outside this
repository. Read *witnesses*, *witness-bytes*, *structure*, *hash*,
*proof-kind*, *proofs*, *algorithm*, *key-reference*, *root*, *signature* as
roles, to be bound to our actual field names when those ids resolve. This is a
reconstruction, not an in-repo definition. **[gloss — D-3]** Role names are
kept consistent with the sibling mapping in
`records/ietf/rfc-9943/distilled/design-notes.md` wherever the two overlap.

| label | name | where | RFC 9942's rule | our field (role) | carry natively? | on export / import |
|---|---|---|---|---|---|---|
| — | CBOR tag **18** (`#6.18`) | outermost, and on each receipt | Mandatory: `Signature_With_Receipt = #6.18(COSE_Sign1)`, `Receipt_For_Inclusion = #6.18(…)`, `Receipt_For_Consistency = #6.18(…)` (§4.3 Fig. 1); "Receipts MUST be tagged as COSE_Sign1" (§4.3, R-0003) | none | **no** — registry allocation, and it discriminates nothing: the same tag marks the statement and both receipt kinds (C6) | emitted on export; on import, required and then discarded |
| **394** | `receipts` | **unprotected** header of the outer statement (§4.3 Fig. 1) | `&(receipts: 394) => [+ bstr .cbor Receipt]` — mandatory member of `Unprotected_Header` as that rule is written, one or more, "Priority ordered sequence" (§8.1 Table 1) | *witnesses* — an ordered, non-empty-when-present list (A6) | **yes as an ordered list, no as label 394** | our *witnesses* list ↔ the 394 array, element order preserved. Each element is *witness-bytes*, stored exactly as received (A7) |
| — | the receipt as bytes | inside the 394 array | `bstr .cbor Receipt` (§4.3 Fig. 1) | *witness-bytes* | **yes** — the only field of a witness with cryptographic authority | identity in both directions; never re-encoded |
| **1** | `alg` | **protected** header of the receipt | "alg (label: 1): REQUIRED. Signature algorithm identifier. Value type: int." (§5.2.1 Fig. 4, R-0010; §5.3.1 Fig. 8, R-0015) | *witness.algorithm* | **yes**, mandatory, inside the signature | emitted always; our identifier ↔ a COSE algorithm value by an explicit table. Constrained by A5 to pair with *hash* |
| **395** | `vds` | **protected** header of the receipt | "vds (label: 395): REQUIRED. VDS algorithm identifier. Value type: int." (§5.2.1 Fig. 4, R-0011; §5.3.1 Fig. 8, R-0016). Value registry: "COSE Verifiable Data Structure Algorithm" subregistry (§8.1 Table 1). Only value defined: `1` = `RFC9162_SHA256` (§5.1, §8.2.2.1 Table 2; `0` Reserved) | *witness.structure* **plus** *witness.hash*, both mandatory, both inside the signature | **yes as two names, no as the integer 1** (B4, C4) | `structure` + `hash` → `395: 1` by a two-column table, the only place the integer 1 exists in our system. On import, `395: 1` → the one permitted pair, and any other value is rejected by profile (B3) |
| **396** | `vdp` | **unprotected** header of the receipt | "vdp (label: 396): REQUIRED. Verifiable Data Structure Proofs. Value type: Map." (§5.2.1 Fig. 5, R-0012); "vdp (label: 396): REQUIRED. VDPs. Value type: Map." (§5.3.1, R-0017). Map labels assigned from the "COSE Verifiable Data Structure Proofs" subregistry (§8.1 Table 1). Contents are VDS-specific (§4.2, §4.3 note in Fig. 1) | *witness.proofs* — a map keyed by *proof-kind* names | **yes as a map keyed by name, no as label 396 with integer keys** | our map ↔ the 396 map, key by key through the proof-kind table |
| **-1** | `inclusion-proof` | key inside the 396 map | "inclusion-proof (label: -1): REQUIRED. Inclusion proofs. Value type: Array of bstr." (§5.2.1 Fig. 5, R-0013). `RFC9162_SHA256 (395: 1) supports both (-1) inclusion and (-2) consistency proofs` (§4.2). Registered: VDS 1, "inclusion proofs", label -1, CBOR type array (of bstr), change controller IETF (§8.2.2.2 Table 3) | *witness.proofs["inclusion"]* → a list of inclusion proofs | **the key: no.** The *contents*: **yes, verbatim** — `[tree-size, leaf-index, inclusion-path]`, field order preserved (§5.2 Fig. 3, A1) | proof-kind name `inclusion` ↔ `-1`; each element stays a `bstr .cbor` of the three-element array, unchanged in both directions |
| **-2** | `consistency-proof` | key inside the 396 map | "consistency-proof (label: -2): REQUIRED. Consistency proofs. Value type: Array of bstr." (§5.3.1, R-0018). Registered: VDS 1, "consistency proofs", label -2, CBOR type array (of bstr), change controller IETF (§8.2.2.2 Table 3) | *witness.proofs["consistency"]* → a list of consistency proofs | **the key: no.** The *contents*: **yes, verbatim** — `[tree-size-1, tree-size-2, consistency-path]` (§5.3 Fig. 7, A1) | proof-kind name `consistency` ↔ `-2`; contents unchanged |
| — | `payload` | body of the receipt | `bstr / nil` (§4.3 Fig. 1). Semantically the Merkle Tree root: "the payload is the Merkle Tree root that corresponds to the log at size tree-size" (§5.2.1); "The payload of an RFC9162_SHA256 inclusion proof signature is the Merkle Tree Hash as defined in [RFC9162]" (§5.2.1); for consistency, "the newer Merkle Tree root … is a detached payload and corresponds to the log at size tree-size-2" (§5.3.1). SHOULD be detached for new VDS profiles (§4.4, R-0004) | *witness.root* — **absent**, always | **no — deliberately absent** (B1). It is derivable from the proof by definition (A2), and storing it enables the one attack this format exists to prevent | emitted as `nil`. On import, a receipt carrying an attached root is **rejected**, not merely tolerated (B1, C7) |
| — | `signature` | body of the receipt | `bstr` (§4.3 Fig. 1) | *witness.signature* | **yes** | direct |
| — | `* cose-label => cose-values` | every header map in Fig. 1; `* cose-label => cose-value` in §5.2.1/§5.3.1 | `cose-label = int / text`, `cose-values = any` (§4.3 Fig. 1) | our extension points | **the escape hatch, and only key-relative and only inside the signature** (B7) | our key-relative extensions ride as `text` labels in the receipt's **protected** map, never as integers and never in the unprotected map |
| — | `typ` | protected, suggested | §4.4 points at `typ` (RFC 9596) and the guidance in RFC 9597 as "One way to include this information" | none | **no** — another registry-defined header parameter, and our mandatory *structure* name already does the work (B7, C2) | not emitted |
| — | `kid` | protected, in examples only | Appears in §4.3 Figure 2's EDN (`/ kid / 4 : h'abcdef12…'`) and in no CDDL or field table in this document | *key-reference* — an opaque, key-relative reference resolved by our own rule | **yes**, carried as our own field | emitted as label 4 when the export target needs it. Note this document never requires it, so how the witness's key is found is out of scope here — O3 |

**What the export mapping is.** A witness leaves our system as a single
deterministic function `export(witness) → COSE_Sign1`, and arrives through its
inverse:

1. Wrap as tag 18, four-element array, per §4.3 Figure 1 and R-0003.
2. Protected map: label 1 from *witness.algorithm*; label 395 from the
   (*structure*, *hash*) pair via the two-column table — the single value `1`
   today, since "This document only defines "RFC9162_SHA256"" (§4.4.1); then
   our key-relative extensions as `text` labels, here and nowhere else (B7).
3. Unprotected map: label 396, a map whose keys come from the proof-kind
   table (`inclusion` → `-1`, `consistency` → `-2`) and whose values are the
   proof arrays **already in RFC 9942's encoding**, because A1 means no
   transcoding is needed — each stays a `bstr` wrapping
   `[tree-size, leaf-index, inclusion-path]` or
   `[tree-size-1, tree-size-2, consistency-path]`.
4. Payload: `nil`. Always, per B1.
5. Signature: *witness.signature*, unchanged — and this is the asymmetry that
   makes the receipt case different from the statement case. We do not compute
   this signature. The witness did. Whatever bytes it signed are the bytes that
   verify, so **export is only safe if it reproduces them exactly**, which
   means in practice that export of a received witness emits *witness-bytes*
   and the field-by-field table above describes the *import* direction and the
   export of witnesses we issue ourselves. See O1.
6. Attach to the outer statement: the 394 array in the unprotected header, in
   *witnesses* order (A6).

Import is the same table read right to left, plus three rejections that have
no counterpart on export: a `395` value outside our profile (B3), an attached
payload (B1), and an unknown key in the `396` map (B3).

**What we deliberately do not carry.** CBOR tag 18 and all three `#6.18`
wrappers; the labels 394, 395 and 396 as labels; the proof labels `-1` and
`-2` as labels; the integer `1` as the structure identifier, except in the
export table; the "COSE Verifiable Data Structure Algorithms" and "COSE
Verifiable Data Structure Proofs" subregistries as our extension mechanism
(§8.2, C3); R-0002's live-registry verification check (§4.3, C1); the `typ`
header parameter (§4.4, C2); the attached-payload form (§4.4, B1); and any
integer extension label. What we *do* carry is everything inside the proof
arrays, verbatim, because that is the part with no registry in it (A1).

Two cautions on the table. The whole right-hand column rests on the
import-asymmetry proposal above, which is option 3 and not a recorded
decision. And `cose-value` in the §5.2.1 and §5.3.1 header maps is undefined
in RFC 9942 — see O5 — so the extension-socket row cites a rule that does not
mechanically resolve in the RFC's own schema.

### DEC-005 — the signing envelope

`DEC-005` is the signing-envelope choice and is **still open**. This record's
`record.yaml` declares `bears_on: [DEC-005, R-M-12]`. There is no in-repo
definition of DEC-005; four topic files name it in `bears_on`
(`topics/scitt.yaml`, `topics/cbor-implementation.yaml`,
`topics/cbor-ecosystem.yaml`, `topics/artifact-statements.yaml`) and none
states it. The reading below — that DEC-005 chooses the envelope our signed
form takes — is a **reconstruction**. **[gloss — DEC-005]**

What RFC 9942 contributes to that choice, and it is narrower than the record's
`applicability: core` suggests:

- **It is evidence about the witness layer, not about the envelope.** RFC 9942
  defines no statement envelope. It defines a receipt and one header parameter
  (394) by which a receipt attaches to *somebody else's* envelope (§4.3
  Figure 1). The envelope evidence in this topic is RFC 9943's, not this
  document's.
- **It raises the cost of choosing COSE, and the cost lands in an unexpected
  place.** If DEC-005 chooses COSE, then under D-3 the statement half is an
  export mapping and the receipt half is an *import* that cannot be reduced
  away. Choosing COSE for the envelope therefore also chooses an RFC 9942
  decoder in the verification path, or the re-attestation adapter of option 3.
  That consequence is not visible from the statement side alone and is the
  main thing this record has to say to DEC-005.
- **It is a reason the envelope decision cannot be deferred past the witness
  decision.** The attachment point for 394 is the outer statement's
  *unprotected* header (§4.3 Figure 1). Any envelope we choose needs an
  attachment region outside the signature with the properties A6 describes —
  ordered, multi-valued, strippable without changing the statement's identity.
  An envelope that lacks one cannot carry a receipt at all.
- **It does not settle the algorithm question and says so.** §7.1's pairing
  rule (A5) constrains the signature algorithm relative to the structure hash
  but names only `ES256` and `SHA256`, by example (§7.1). The algorithm suite
  stays where it was.

### R-M-12 — native extension points must be key-relative, not registry-dependent

R-M-12 and D-3's "no IANA tags" are **the same commitment stated twice** —
once as a requirement on our extension mechanism, once as a decision about our
encoding. The wording of R-M-12 used here is a **reconstruction**; the id has
no in-repo definition. `docs/scope.md` line 119 corroborates the registry
reading without defining the requirement, noting that the IANA COSE Header
Parameters registry is "a single `dataset` record even though it bears heavily
on R-M-12". **[gloss — R-M-12]**

Worth recording about that corroboration: **the registry it names is not in
the library.** `records/iso/iana-cose-algorithms` (status `stub`) is the COSE
*Algorithms* registry, not COSE *Header Parameters*; no record covers the
Header Parameters registry that §8.1 writes into, and none covers either of
the two subregistries §8.2 creates. So the registry R-M-12 is said to bear
heavily on, and the registries this document makes load-bearing for
verification, are things we hold no record of at all.

**RFC 9942 collides with R-M-12 at three levels, each stronger than the
last.**

1. **It burns three COSE header parameters.** 394 `receipts`, 395 `vds`, 396
   `vdp` (§2), added by IANA to the "COSE Header Parameters" subregistry in
   the `'Integer values from 256 to 65535'` range with a Specification
   Required registration procedure (§8.1 Table 1, citing RFC 8126). This is
   the ordinary level and the cheapest to decline: the allocations are already
   made, so using them costs no application, and the objection is semantic
   rather than procedural (C2).
2. **It creates two new subregistries.** "COSE Verifiable Data Structure
   Algorithms" and "COSE Verifiable Data Structure Proofs", both Specification
   Required per RFC 8126 §4.6 (§8.2), with five expert-review criteria
   (§8.2.1) including the pairing rule (R-0027) and the shared-change-
   controller rule. Here the document is not consuming a registry but
   **designing one as the intended growth path**: §4.1 and §4.2 each end by
   establishing a registry, and §4.4.1 makes a specification plus two matching
   registrations the price of a new structure (R-0006, R-0007, R-0008). The
   extension mechanism *is* IANA. Declining it means we need our own growth
   path, which C3 gives: structures and their proof kinds defined together in
   one versioned document.
3. **It makes registry membership load-bearing for verification.** §4.3,
   R-0002: the verifier MUST confirm the VDS and VDPs "match entries present
   in the registries established in this specification, **including values
   added in subsequent registrations**". This is the sharpest form of the
   collision available and the reason this record is singled out in
   `docs/extraction.md`. Levels 1 and 2 are about where meaning lives. Level 3
   is about where a *verification result* comes from: a conforming verifier's
   accept set is the live state of an IANA registry, so correctness of a
   cryptographic check becomes a function of when the implementation last
   synchronised with a third party. R-M-12 as glossed forbids registry
   dependence in extension points; §4.3 goes further than anything R-M-12
   anticipates by putting the registry in the *verification path*. We reject
   it (C1) and keep its security purpose (B3).

**Both poles of R-M-12, in one topic.** This library also holds
`draft-mih-scitt-agent-action-capsule`, which states a binding invariant twice
(its §4 and §12.1): *"verifiers MUST treat unregistered values as
informational and MUST NOT reject a Capsule for carrying one. Registration
governs shared meaning, never acceptance."* Set against RFC 9942 §4.3, the two
documents are the two possible answers to the same question:

| | RFC 9942 §4.3 (R-0002) | capsule §4, §12.1 |
|---|---|---|
| what a registry governs | **acceptance** — a value absent from the registry fails verification | **meaning only** — an unregistered value is informational |
| verifier's duty on an unknown value | MUST confirm membership; non-membership is a verification failure | MUST NOT reject for carrying it |
| accept set | the live registry, "including values added in subsequent registrations" | fixed by the verifier's own profile |
| who can change the outcome of a verification | IANA, after publication | nobody |

That pair is worth more to us than either document's schema, and it is the
most useful thing this record offers R-M-12. It also shows the two answers are
not symmetric in cost. The capsule's rule is free to implement and gives up
the ability to *fail closed* on something a verifier does not understand.
RFC 9942's rule fails closed and pays for it with a mutable accept set. Our
B3 is a third position: fail closed against a **closed, versioned,
locally-held** profile — the capsule's immutability with RFC 9942's
strictness. Whether that is coherent in general, or only coherent because our
profile happens to be small, is O4.

**One honest qualification on the contrast.** The capsule pole is held at
`status: stub`, `confidence: low`, with no extraction — the quotation above
reaches us through that record's `summary.md` quoting the draft, not through an
extraction of the draft, so its locators (§4, §12.1) are not ones this library
has verified against source bytes. The RFC 9942 pole is verified here against
`da8ed24e…`. The two poles are not equally well held, and a reviewer should
know that before leaning on the comparison.

### Where we relied on a reconstructed gloss

Marked **[gloss]** above. The wordings below were supplied to the extraction;
they are reconstructions, not definitions this repository can resolve.

| id | reconstruction relied on | corroboration inside this repository |
|---|---|---|
| **D-3** | "option 5: reduced CBOR, no IANA tags, COSE as export only" | `docs/extraction.md` line 36 — stated in-repo, so this one is quoted rather than reconstructed. The meeting that decided it is external, and the gloss is silent on the import direction, which is this record's whole problem |
| **DEC-005** | the signing-envelope choice, still open | **none.** `topics/scitt.yaml`, `topics/cbor-implementation.yaml`, `topics/cbor-ecosystem.yaml` and `topics/artifact-statements.yaml` each name the id in `bears_on` without defining it; this record's `record.yaml` declares `bears_on: [DEC-005, R-M-12]` |
| **R-M-12** | "native extension points must be key-relative, not registry-dependent" | `docs/scope.md` line 119 — corroborates the registry reading, does not define the requirement. And the registry it names, IANA COSE Header Parameters, has no record in this library |
| **statement and witness field names** | the roles *witnesses*, *witness-bytes*, *structure*, *hash*, *proof-kind*, *proofs*, *algorithm*, *key-reference*, *root*, *signature* | **none.** Field names live in ARCH-0001 / DEC-007, outside this repository; `schema/record.schema.yaml` names ARCH-0001 as the home of these ids. Role names are aligned with the sibling mapping in `records/ietf/rfc-9943/distilled/design-notes.md` so the two tables can be read together |

Every claim in this file *about RFC 9942* comes from the source and carries a
locator. Every claim about *what we should do* depends on the glosses above
and should be re-checked when ARCH-0001 is readable from here.

---

## Open questions

**O1 — Is the witness mapping invertible, and if not, what is a native witness
worth?** This is first because it is the highest-value open item in the file
and the one the import asymmetry creates. We do not produce a receipt's
signature; a witness does, over bytes the witness chose (§3, §4.3 Figure 1).
So a native witness record in our reduced form is a *projection* of something
signed, and re-encoding it to COSE will reproduce the verifying bytes only if
the mapping is byte-exact in both directions — which depends on the witness's
own CBOR encoding choices, not ours. A7 and export step 5 therefore keep
*witness-bytes* as the authoritative field and make the native record derived.
Two things follow and neither is settled. First, a relying party who trusts our
native record is trusting **our adapter**, not the witness, unless we sign the
projection ourselves — which is option 3's re-attestation, and it means our
transparency claim is one hop longer than RFC 9942's. Second, if we ever issue
witnesses rather than only consume them, export step 5 becomes a signature we
*do* compute, and the invertibility question becomes a conformance question
instead. Until this is decided, the D-3 table's right-hand column is a design
intent, not a specification.

**O2 — How does a relying party learn that a receipt it holds is stale? This
gap belongs to neither record that creates it.** RFC 9942 puts validity
periods out of scope — "The details of expressing validity periods are out of
scope for this document" (§7.2, R-0024) — and status out of scope — "The
details of expressing statuses are out of scope for this document" (§7.3,
R-0025). Read that against RFC 9943 §4, which states that "A Receipt's
verification key, signing algorithm, validity period, header parameters or
other claims MAY change each time a Receipt is produced" (RFC 9943 §4, read
from `.cache/rfc-editor-org-rfc-rfc9943-txt.bin`, the bytes recorded on
`records/ietf/rfc-9943`). So the architecture document says the parameters of
a receipt are per-issuance mutable, and the format document declines to say how
mutability is expressed or how a holder learns about it. Neither document is
wrong within its own scope and the system has no answer: a receipt is a signed
statement about a past tree state with no expiry, no status, and no channel by
which its issuer can tell a holder it is no longer good. The gap spans both
records and belongs to neither, which is exactly why it needs recording
somewhere that is not inside either one. `topics/scitt.yaml` already carries
the sharper version of it — a transparency service permitted to roll its
statement sequence back, with no notification channel — and this record's
contribution is the narrower, format-level half: §7.2 and §7.3 are where the
hole is cut.

**O3 — How is the witness's key found?** This document never says. `kid`
appears only in §4.3 Figure 2's informative EDN and in no CDDL and no field
table; the receipt's own protected header is specified as `alg` and `vds` and
nothing else (§5.2.1 Figure 4, §5.3.1 Figure 8). `alg` identifies the
algorithm, not the key. So a verifier holding a receipt has no field telling it
which key to check the signature with, and §7 delegates security
considerations wholesale to RFC 9162 and RFC 9053 without filling this in. The
answer presumably lives in RFC 9943's trust model, which is a different record;
the point for us is that **our witness profile must specify key resolution
itself**, because adopting RFC 9942's header set gives us no help, and the
D-3 table's `kid` row is consequently our invention rather than a mapping.

**O4 — Is a closed, locally-held profile a coherent general answer, or does it
work only because our profile is small?** B3 and C1 replace a live-registry
check with a profile check. That is clean while the profile has one structure
and two proof kinds — which is also all RFC 9942 itself defines ("This
document only defines "RFC9162_SHA256"", §4.4.1; one entry plus Reserved in
Table 2, §8.2.2.1; two entries in Table 3, §8.2.2.2). If our profile grows, or
if we ever need to accept a witness from a party who uses a structure
registered after our version shipped, the registry's forward compatibility
(R-0002's "including values added in subsequent registrations") is doing real
work we will have given up. The question is what our version-negotiation story
is, and we do not have one. Related, and unverified: this record's
`implementations` note reports a `vds=2` (Microsoft CCF) registration beyond
the single VDS this RFC defines, marked UNVERIFIED precisely because
confirming it needs the IANA registry we do not hold. If that is real, the
forward-compatibility problem is already live rather than hypothetical.

**O5 — Source defects in the CDDL, and whether we can validate against the
RFC's own schema at all.** Four, all in §5.2.1 and §5.3.1, all erratum-grade:

- **`verifiable-proofs` is defined twice with different bodies.** §5.2.1
  Figure 5: `verifiable-proofs = { &(inclusion-proof: -1) => inclusion-proofs }`.
  §5.3.1: `verifiable-proofs = { &(consistency-proof: -2) => consistency-proofs }`.
  Same rule name, two incompatible definitions. RFC 8610 has `//=` and `/=`
  for extending a rule; plain `=` twice is a redefinition.
- **`protected-header-map` is defined twice**, §5.2.1 Figure 4 and §5.3.1
  Figure 8, with byte-identical bodies. Harmless semantically, still a
  duplicate rule.
- **`unprotected-header-map` is defined twice**, §5.2.1 Figure 5 and §5.3.1,
  also with identical bodies — and both reference the ambiguous
  `verifiable-proofs`, so the duplication is what makes the first defect
  reachable.
- **`cose-value` is used and never defined.** §5.2.1 Figure 4, §5.2.1
  Figure 5, §5.3.1 Figure 8 and §5.3.1's unprotected map all end in
  `* cose-label => cose-value`. The document defines `cose-values` — plural —
  in §4.3 Figure 1, and `cose-value` singular appears nowhere as a rule.
  `cose-label` is likewise only defined in §4.3 Figure 1, so the §5 fragments
  are not self-contained even setting the typo aside.
- A fifth, lesser: `inclusion-proofs = [ + inclusion-proof ]` (§5.2.1
  Figure 5) and `consistency-proofs = [ + consistency-proof ]` (§5.3.1)
  reference singular rule names that are never defined either. §5.2 defines
  `inclusion-proof-content` and §4.3 Figure 1 defines
  `RFC9162_SHA256_Inclusion_Proof`; neither is spelled `inclusion-proof`.

The consequence is concrete and it is the reason this sits in open questions
rather than in a defect log: **the §5 CDDL cannot be mechanically validated as
written**, so we cannot use the RFC's own schema as the conformance artifact
for our import adapter. `distilled/schema/receipts-merged.derived.cddl` in
this record is a derived reconciliation and is therefore *our* reading, not
the RFC's. Anything our adapter validates, it validates against our
reconciliation. Whether to file an erratum, and what the §5.3.1
verification-order tension in B2 means alongside these, is the open part.

**O6 — Does the prose/CDDL mismatch on where receipts may appear matter?**
§4.3 says the parameter exists "to enable Receipts to be conveyed in the
protected and unprotected headers of Enveloped COSE Structures", and Figure 1
in the same section puts `&(receipts: 394)` only in `Unprotected_Header`;
`Protected_Header` is `{ * cose-label => cose-values }` with no 394 member.
A receipt in the protected header would be covered by the outer signature,
which is a materially different object — the issuer would be signing over the
witness's attestation, creating an ordering dependency between issuance and
registration that the unprotected form deliberately avoids. We assume the
unprotected form throughout (A6, the 394 row of the D-3 table), because that
is what the CDDL says and what Figure 2 shows. If the protected form is
intended, our attachment-region reasoning in A6 and DEC-005 needs revisiting.

**O7 — What does a proof actually guarantee? We have not checked, and we
cannot from here.** §5.1 defines the only VDS by reference — "See Section
2.1.1 of [RFC9162] for a complete description of this VDS" — §5.2 and §5.3
define the proof types by reference to RFC 9162 §2.1.3.1 and §2.1.4.1, §5.2.1
defines the payload as "the Merkle Tree Hash as defined in [RFC9162]", §5.2
quotes RFC 9162's own failure condition ("If leaf_index is greater than or
equal to tree_size, then fail the proof verification.", R-0009) and notes that
"[RFC9162] defines inclusion proofs only for leaf nodes", and §7 delegates
security considerations to RFC 9162 and RFC 9053. **Every security property of
this format is inherited.** See the dependency closure below.

### Dependency closure — what this record rests on, and what we hold

Checked against the library on 2026-09-30:

| record | held? | `status` | why it matters here |
|---|---|---|---|
| `records/ietf/rfc-9162` | yes | **`stub`**, `confidence: low` | **The critical one.** The only defined VDS (§5.1), both proof types (§5.2, §5.3), the Merkle Tree Hash the payload is (§5.2.1), the leaf-index failure condition (§5.2, R-0009), and the entire security analysis (§7) |
| `records/ietf/rfc-9052` | yes | `fetched` | `COSE_Sign1` itself; the Receipt is defined as "A COSE Single Signer Data Object, as defined in RFC 9052 of [STD96]" (§3), and §4.3 requires the COSE_Sign1 tagging (R-0003) |
| `records/ietf/rfc-9053` | yes | `fetched` | §5 maps RFC 9162's structure "using [RFC8949] and [RFC9053]"; `alg` values including the `ES256` of §7.1; one of the two security-considerations delegations (§7) |
| `records/ietf/rfc-8949` | yes | `read` | CBOR; the encoding of every proof structure (§4, §5.2, §5.3) |
| `records/ietf/rfc-8610` | yes | `fetched` | CDDL; needed to adjudicate the O5 defects, in particular what a duplicate rule definition means |
| `records/ietf/rfc-9943` | yes | `distilled` | The architecture this receipt serves; the §4 passage in O2 |
| `records/ietf/rfc-9596`, `rfc-9597` | yes | `fetched`, `fetched` | The `typ` mechanism §4.4 suggests and we decline (C2, B7) |
| `records/ietf/rfc-8392` | yes | `fetched` | The `iat`/`nbf`/`exp` claims §7.2 points at (C8) |
| `records/ietf/rfc-9338` | yes | `fetched` | The other half of STD 96 (§9.1) |
| `records/ietf/rfc-8126` | **no** | — | The Specification Required policy and §4.6 that both §8.1 and §8.2 rest on |
| `records/ietf/rfc-7120` | **no** | — | The early-allocation rule in §8.2.1 |
| IANA COSE Header Parameters registry | **no** | — | What §8.1 writes into. `records/iso/iana-cose-algorithms` (`stub`) is the *Algorithms* registry, a different one |
| the two VDS subregistries (§8.2) | **no** | — | What R-0002 makes a verifier consult at verification time |

**On RFC 9162 specifically**, because the answer is worse than "stub": its
`record.yaml` is still the unedited ingest template. `authors: []`, `date: ""`,
`content.sha256: ""`, `content.retrieved: ""`, `bears_on: []`, `tags: []`,
`topic: namespace-governance` — which is not this topic. **The bytes have
never been fetched**, so there is no digest and nothing to extract from. The
companion `records/ietf/rfc-6962` (Certificate Transparency v1) is also
`stub`. So every claim in this file about what an inclusion or consistency
proof *guarantees* — that the path binds the entry to the root, that the
consistency path establishes append-only growth, that the failure conditions
are sufficient — is inherited from a document this library has not read, not
checked here. RFC 9162 is the highest-value next extraction in this topic by a
wide margin, and until it is done, A2's correctness, B1's threat model and
B2's reordering all rest on an unread dependency.
