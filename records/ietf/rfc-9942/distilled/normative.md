---
record: rfc-9942
kind: normative
title: "rfc-9942 — normative statements"
extracted: "2026-09-30"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9942, "CBOR Object Signing and Encryption (COSE) Receipts",
Standards Track, June 2026.
sha256 `da8ed24ef2d757ece900decf34a003a7b02679a16f4c1f25670ea59435372da0`
(1033 lines, plain text).

Quotation convention: text inside `> ` blocks and fenced blocks is verbatim from
the source. BCP 14 keywords are **bolded** in prose quotes for scanning only —
the words themselves are unaltered. Line numbers given as `L<n>` refer to the
source file above.

---

## §1.1 Requirements Notation

BCP 14 invocation (L115–L119):

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
> "OPTIONAL" in this document are to be interpreted as described in
> BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
> capitals, as shown here.

This clause is what makes the lowercase obligations recorded below
(§4.2, §4.4, §4.4.1, §5.2, §5.3.1, §7.1, §7.3, §8.2.1) **non**-BCP-14: they are
excluded from the keyword count by the document's own terms.

BCP 14 keywords in §1.1: none counted — the enumeration is the definition of
the terms, not a use of them.

---

## §2 New COSE Header Parameters

BCP 14 keywords: **zero** (confirmed).

Three header parameters are defined. The assignments are normative; the prose is
verbatim (L123–L139):

> This document defines three new COSE header parameters, which are
> introduced up front in this section and elaborated on later in this
> document.

> 394:  A COSE header parameter named "receipts" with a value type of
>    array where the array contains one or more COSE Receipts as
>    specified in this document.

> 395:  A COSE header parameter named "vds" (for Verifiable Data
>    Structure), which conveys the algorithm identifier for a VDS.
>    Correspondingly, see Section 8.2.2.1 for a registry defining the
>    integers used to identify VDSs.

> 396:  A COSE header parameter named "vdp" (for VDPs), which conveys a
>    map containing VDPs organized by Proof Type.  Correspondingly, see
>    Section 8.2.2.2 for a registry defining the integers used to
>    identify VDS Proof Types.

---

## §3 Terminology

BCP 14 keywords: **zero** (confirmed). Definitional, but normative for
interpretation of the rest of the document; retained verbatim.

> The terms "header" and "payload" are defined in [STD96].  The term
> "claim" is defined in [RFC8392].

> CDDL:  Concise Data Definition Language (CDDL) is defined in
>    [RFC8610].

> EDN:  CBOR Extended Diagnostic Notation (EDN) is defined in
>    [RFC8949], where it is referred to as "diagnostic notation", and
>    is revised in [CBOR-EDN].

> Entry:  An entry in a VDS for which proofs can be derived.

> Proof Type:  A property that can be obtained by verifying a given
>    proof over one or more entries in a VDS.  For example, a VDS, such
>    as a binary Merkle Tree, can support inclusion proofs where each
>    proof confirms that a given entry is included in a Merkle Tree
>    root.

> Proof Value:  An encoding of a Proof Type in CBOR [RFC8949].

> Receipt:  A COSE Single Signer Data Object, as defined in RFC 9052 of
>    [STD96], containing the header parameters necessary to convey one
>    or more VDP for an associated VDS.

> Verifiable Data Structure (VDS):  A data structure that supports one
>    or more VDS Proof Types.  This property describes an algorithm
>    used to maintain a VDS, for example, a binary Merkle Tree
>    algorithm.

> Verifiable Data Structure Proof (VDP):  A data structure used to
>    convey Proof Types for proving different properties, such as
>    authentication, inclusion, consistency, and freshness.  Parameters
>    can include multiple proofs of a given type or multiple types of
>    proof (inclusion and consistency).

---

## §4 VDSs in CBOR

BCP 14 keywords: **zero** in the section preamble.

> This document defines two extension points for enabling VDSs with COSE and
> provides concrete examples for the structures and proofs defined in
> Section 2.1.3 of [RFC9162] and Section 2.1.4 of [RFC9162].

(Quoted from L186–L190; the clause is reflowed in the source across those lines.)

### §4.1 Structures

BCP 14 keywords: **zero**.

> This document establishes a registry of VDS algorithms; see
> Section 8.2.2.1 for details.

### §4.2 Proofs

BCP 14 keywords: **1 MUST** (L217).

> RFC9162_SHA256 (395: 1) supports both (-1) inclusion and
> (-2) consistency proofs.

> This document establishes a registry of VDS algorithm proofs; see
> Section 8.2.2.2 for details.

**MUST (§4.2, L216–L220)** — security analysis before migration:

> Proof Types are specific to their associated "Verifiable Data
> Structure"; for example, different Merkle Trees might support
> different representations of inclusion proof or consistency proof.
> Implementers should not expect interoperability across "Verifiable
> Data Structures".  Security analysis **MUST** be conducted prior to
> migrating to new structures to ensure the new security and privacy
> assumptions are acceptable for the use case.

Non-BCP-14 obligation in the same passage (lowercase, **not** counted):

> Implementers should not expect interoperability across "Verifiable
> Data Structures".

### §4.3 Usage

BCP 14 keywords: **2 MUST** (L227, L232).

> This document registers a new COSE header parameter "receipts" (394)
> to enable Receipts to be conveyed in the protected and unprotected
> headers of Enveloped COSE Structures.

**MUST (§4.3, L227–L230)** — verifier confirms VDS and VDP against the
registries, *including later registrations*:

> When the "receipts" header parameter is present, the verifier **MUST**
> confirm that the associated VDS and VDPs match entries present in the
> registries established in this specification, including values added
> in subsequent registrations.

**MUST (§4.3, L232)** — tagging:

> Receipts **MUST** be tagged as COSE_Sign1.

#### §4.3 Figure 1 — CDDL for a COSE_Sign1 with Attached Receipts (normative)

Verbatim, L234–L339 (`Figure 1: CDDL for a COSE_Sign1 with Attached Receipts`):

```cddl
Signature_With_Receipt = #6.18(COSE_Sign1)

cose-label = int / text
cose-values = any

Protected_Header = {
  * cose-label => cose-values
}

Unprotected_Header = {
  &(receipts: 394)  => [+ bstr .cbor Receipt]
  * cose-label => cose-values
}

COSE_Sign1 = [
  protected   : bstr .cbor Protected_Header
  unprotected : Unprotected_Header
  payload     : bstr / nil
  signature   : bstr
]

Receipt = Receipt_For_Inclusion / Receipt_For_Consistency

; Note the proof formats shown here are for RFC9162_SHA256.
; Other VDSs may have different proof formats.


Receipt_For_Inclusion = #6.18(Signed_Inclusion_Proof)

Signed_Inclusion_Proof = [
  protected   :
    bstr .cbor RFC9162_SHA256_Inclusion_Protected_Header,
  unprotected : RFC9162_SHA256_Inclusion_Unprotected_Header,
  payload     : bstr / nil,
  signature   : bstr
]

RFC9162_SHA256_Inclusion_Protected_Header = {
  &(alg: 1) => int
  &(vds: 395) => int
  * cose-label => cose-values
}

RFC9162_SHA256_Inclusion_Unprotected_Header = {
  &(vdp: 396) => RFC9162_SHA256_Verifiable_Inclusion_Proofs
  * cose-label => cose-values
}

RFC9162_SHA256_Verifiable_Inclusion_Proofs = {
  &(inclusion-proof: -1) => RFC9162_SHA256_Inclusion_Proofs
}

RFC9162_SHA256_Inclusion_Proofs = [
  + RFC9162_SHA256_Inclusion_Proof
]

RFC9162_SHA256_Inclusion_Proof =
  bstr .cbor RFC9162_SHA256_Inclusion_Proof_Content

RFC9162_SHA256_Inclusion_Proof_Content = [
  tree_size: uint,
  leaf_index: uint,
  inclusion_path:[ + bstr ]
]


Receipt_For_Consistency = #6.18(Signed_Consistency_Proof)

Signed_Consistency_Proof = [
  protected   :
    bstr .cbor RFC9162_SHA256_Consistency_Protected_Header,
  unprotected : RFC9162_SHA256_Consistency_Unprotected_Header,
  payload     : bstr / nil, ; Newer Merkle Tree root
  signature   : bstr
]

RFC9162_SHA256_Consistency_Protected_Header = {
  &(alg: 1) => int,
  &(vds: 395) => int,
  * cose-label => cose-values
}

RFC9162_SHA256_Consistency_Unprotected_Header = {
  &(vdp: 396) => RFC9162_SHA256_Verifiable_Consistency_Proofs
  * cose-label => cose-values
}

RFC9162_SHA256_Verifiable_Consistency_Proofs = {
  &(consistency-proof: -2) => RFC9162_SHA256_Consistency_Proofs
}

RFC9162_SHA256_Consistency_Proofs = [
  + RFC9162_SHA256_Consistency_Proof
]

RFC9162_SHA256_Consistency_Proof =
  bstr .cbor RFC9162_SHA256_Consistency_Proof_Content

RFC9162_SHA256_Consistency_Proof_Content = [
  tree_size_1: uint,
  tree_size_2: uint,
  consistency_path: [ + bstr ]
]
```

Note the `payload : bstr / nil, ; Newer Merkle Tree root` comment is part of the
source CDDL and is reproduced as written.

Closing constraint of §4.3 (L397–L402):

> The specific structure of COSE Receipts is dependent on the structure
> of the COSE_Sign1 payload and the VDPs contained in the COSE_Sign1
> unprotected header.  The CDDL definition for VDPs is specific to each
> VDS.

Figure 2 (L341–L393) is labelled by the source as *informative* EDN
("The following informative EDN is provided:") and is therefore excluded here;
it is captured in the examples artifact.

### §4.4 Profiles

BCP 14 keywords: **1 SHOULD** (L409).

**SHOULD (§4.4, L407–L418)** — detached payload:

> New VDSs can require the definition of a profile.  The payload in
> such definitions **SHOULD** be detached.  Detached payloads force
> verifiers to recompute the root from the proof and protect against
> implementation errors where the signature is verified but the payload
> is incompatible with the proof.  Profiles of proof signatures that
> define additional protected header parameters are encouraged to make
> their presence mandatory to ensure that claims are processed with
> their intended semantics.  One way to include this information in the
> COSE structure is use of the "typ" (type) header parameter; see
> [RFC9596] and the similar guidance provided in [RFC9597].

Non-BCP-14 obligation in the same passage (lowercase, **not** counted):

> Profiles of proof signatures that define additional protected header
> parameters are encouraged to make their presence mandatory to ensure that
> claims are processed with their intended semantics.

### §4.4.1 Registration Requirements

BCP 14 keywords: **2 MUST** (L421, L423).

**MUST ×2 (§4.4.1, L421–L424)** — what every VDS specification must define:

> Each VDS specification applying for inclusion in this registry **MUST**
> define how to encode the VDS identifier and its Proof Types in CBOR.
> Each specification **MUST** define how to produce and consume the
> supported Proof Types.  See Section 5 as an example.

Non-BCP-14 obligation (lowercase "must", **not** counted) — per-hash-algorithm
registration (§4.4.1, L426–L434):

> Where a specification supports a choice of hash algorithm, a separate
> IANA registration must be made for each supported algorithm.  For
> example, to provide support for SHA256 and SHA3_256 with Merkle
> inclusion proofs and Merkle consistency proofs defined, respectively,
> in Section 2.1.3 of [RFC9162] and Section 2.1.4 of [RFC9162], both
> "RFC9162_SHA256" and "RFC9162_SHA3_256" require entries in the
> relevant IANA registries.  This document only defines
> "RFC9162_SHA256".

---

## §5 RFC9162_SHA256

BCP 14 keywords: **zero** in the section preamble.

> This section defines how the data structure described in Section 2.1
> of [RFC9162] is mapped to the terminology defined in this document,
> using [RFC8949] and [RFC9053].

### §5.1 Verifiable Data Structure

BCP 14 keywords: **zero** (confirmed).

> The integer identifier for this VDS is 1.  The string identifier for
> this VDS is "RFC9162_SHA256", a Merkle Tree where SHA256 is used as
> the hash algorithm (see Table 2).  See Section 2.1.1 of [RFC9162] for
> a complete description of this VDS.

### §5.2 Inclusion Proof

BCP 14 keywords: **zero** (confirmed) — but the section carries a normative
constraint imported by quotation from RFC 9162.

> See Section 2.1.3.1 of [RFC9162] for a complete description of this
> VDS Proof Type.

> The CBOR representation of an inclusion proof for RFC9162_SHA256 is:

Figure 3 (L456–L467), `Figure 3: CBOR-Encoded Inclusion Proof for
RFC9162_SHA256`, verbatim:

```cddl
inclusion-proof-content = [

    ; tree size at current Merkle Tree root
    tree-size: uint

    ; index of leaf in tree
    leaf-index: uint

    ; path from leaf to current Merkle Tree root
    inclusion-path: [ + bstr ]
]
```

> The term leaf-index is used for alignment with the use established in
> Section 2.1.3.2 of [RFC9162].

**Imported constraint (§5.2, L472–L477)** — verification failure condition,
quoted by RFC 9942 from RFC 9162. The source sets it as a block quotation
(leading `|`), so it is a normative requirement of this document by reference,
carrying lowercase imperative rather than a BCP 14 keyword:

> Note that [RFC9162] defines inclusion proofs only for leaf nodes, and
> that:
>
> |  If leaf_index is greater than or equal to tree_size, then fail the
> |  proof verification.

> The identifying index of a leaf node is relative to all nodes in the
> tree size for which the proof was obtained.

### §5.2.1 Receipt of Inclusion

BCP 14 keywords: **4 REQUIRED** (L495, L498, L517, L520) — all four are
**field designators** in the receipt tables below, not sentence-level
obligations.

> In a signed proof, the payload is the Merkle Tree root that
> corresponds to the log at size tree-size.  The protected header for
> an RFC9162_SHA256 inclusion proof signature is:

Figure 4 (L486–L490), `Figure 4: Protected Header for a Receipt of Inclusion`:

```cddl
protected-header-map = {
  &(alg: 1) => int
  &(vds: 395) => int
  * cose-label => cose-value
}
```

Protected-header field table (L495–L499), verbatim — **REQUIRED ×2**:

> alg (label: 1):  **REQUIRED**.  Signature algorithm identifier.  Value
>    type: int.

> vds (label: 395):  **REQUIRED**.  VDS algorithm identifier.  Value type:
>    int.

> The unprotected header for an RFC9162_SHA256 inclusion proof
> signature is:

Figure 5 (L504–L514), `Figure 5: A VDP in an Unprotected Header`:

```cddl
inclusion-proofs = [ + inclusion-proof ]

verifiable-proofs = {
  &(inclusion-proof: -1) => inclusion-proofs
}

unprotected-header-map = {
  &(vdp: 396) => verifiable-proofs
  * cose-label => cose-value
}
```

Unprotected-header field table (L517–L521), verbatim — **REQUIRED ×2**:

> vdp (label: 396):  **REQUIRED**.  Verifiable Data Structure Proofs.
>    Value type: Map.

> inclusion-proof (label: -1):  **REQUIRED**.  Inclusion proofs.  Value
>    type: Array of bstr.

Payload binding (L523–L524):

> The payload of an RFC9162_SHA256 inclusion proof signature is the
> Merkle Tree Hash as defined in [RFC9162].

Protected-header dependency (L553–L554):

> The VDS in the protected header is necessary to understand the
> inclusion proof structure in the unprotected header.

#### §5.2.1 Verification procedure — inclusion: PROOF FIRST, THEN SIGNATURE

Verbatim, L556–L566. Note the ordering: the proof is applied first and its
output *becomes* the payload that the signature is then checked over.

> Verification of the inclusion proof and signature occurs in two
> sequential steps:
>
> 1.  Inclusion Proof Verification: The verifier applies the inclusion
>     proof to the bytes of a candidate entry.  If this fails, the
>     proof is invalid.  If it succeeds, the resulting Merkle Tree root
>     becomes the COSE_Sign1 payload.
>
> 2.  Signature Verification: The verifier checks the COSE_Sign1
>     signature.  Successful verification confirms the entry's
>     inclusion in the VDS; otherwise, the signature is invalid.

Figure 6 (L530–L551) is an EDN example ("An EDN example for a Receipt
containing an inclusion proof ... is:") and is excluded here as illustrative;
captured in the examples artifact.

### §5.3 Consistency Proof

BCP 14 keywords: **zero** (confirmed).

> See Section 2.1.4.1 of [RFC9162] for a complete description of this
> VDS Proof Type.

> The CBOR representation of a consistency proof for RFC9162_SHA256 is:

Figure 7 (L574–L586), `Figure 7: CBOR-Encoded Consistency Proof for
RFC9162_SHA256`, verbatim:

```cddl
consistency-proof-content = [

    ; older Merkle Tree size
    tree-size-1: uint

    ; newer Merkle Tree size
    tree-size-2: uint

    ; path from older Merkle Tree to newer Merkle Tree
    consistency-path: [ + bstr ]

]
```

### §5.3.1 Receipt of Consistency

BCP 14 keywords: **4 REQUIRED** (L607, L610, L627, L629) — again all four are
**field designators**, not sentence-level obligations.

> In a signed consistency proof, the newer Merkle Tree root (proven to
> be consistent with an older Merkle Tree root) is a detached payload
> and corresponds to the log at size tree-size-2.

> The protected header for an RFC9162_SHA256 consistency proof
> signature is:

Figure 8 (L598–L602), `Figure 8: Protected Header for a Receipt of
Consistency`:

```cddl
protected-header-map = {
  &(alg: 1) => int
  &(vds: 395) => int
  * cose-label => cose-value
}
```

Protected-header field table (L607–L611), verbatim — **REQUIRED ×2**:

> alg (label: 1):  **REQUIRED**.  Signature algorithm identifier.  Value
>    type: int.

> vds (label: 395):  **REQUIRED**.  VDS algorithm identifier.  Value type:
>    int.

> The unprotected header for an RFC9162_SHA256 consistency proof
> signature is:

Unprotected header CDDL (L616–L625):

```cddl
consistency-proofs = [ + consistency-proof ]

verifiable-proofs = {
  &(consistency-proof: -2) => consistency-proofs
}

unprotected-header-map = {
  &(vdp: 396) => verifiable-proofs
  * cose-label => cose-value
}
```

Unprotected-header field table (L627–L630), verbatim — **REQUIRED ×2**:

> vdp (label: 396):  **REQUIRED**.  VDPs.  Value type: Map.

> consistency-proof (label: -2):  **REQUIRED**.  Consistency proofs.  Value
>    type: Array of bstr.

Payload binding (L632–L633):

> The payload of an RFC9162_SHA256 consistency proof signature is: The
> newer Merkle Tree Hash as defined in [RFC9162].

Protected-header dependency (L664–L665):

> The VDS in the protected header is necessary to understand the
> consistency proof structure in the unprotected header.

#### §5.3.1 Verification procedure — consistency: SIGNATURE FIRST, THEN PROOF

Verbatim, L667–L679. This is the **reverse** of the inclusion order in §5.2.1.

> The signature and consistency proof are verified in order.
>
> First, the verifier checks the signature on the COSE_Sign1.  If the
> verification fails, the consistency proof is not checked.  Second,
> the consistency proof is checked by applying a previous inclusion
> proof to the consistency proof.  If the verification fails, the
> append-only property of the VDS is not assured.  This approach is
> specific to RFC9162_SHA256; different VDSs may not support
> consistency proofs.  It is recommended that implementations return a
> single boolean result for Receipt-verification operations to reduce
> the chance of accepting a valid signature over an invalid consistency
> proof.

Non-BCP-14 obligation in the closing sentence (lowercase, **not** counted):

> It is recommended that implementations return a single boolean result for
> Receipt-verification operations to reduce the chance of accepting a valid
> signature over an invalid consistency proof.

Figure 9 (L637–L662) is an EDN example and is excluded here as illustrative;
captured in the examples artifact.

---

## §6 Privacy Considerations

### §6.1 Log Length

BCP 14 keywords: **zero** (confirmed). The section states a leakage property,
not an obligation, and is retained because the §6.2 MUST is scoped against it:

> Some structures and proofs leak the size of the log at the time of
> inclusion.  In the case that a log only stores certain kinds of
> information, this can reveal details that could impact reputation.

### §6.2 Header Parameters

BCP 14 keywords: **1 MUST** (L695).

**MUST (§6.2, L693–L697)** — privacy analysis by the receipt producer:

> Additional header parameters can reveal information about the
> transparency service or its log entries.  The receipt producer **MUST**
> perform a privacy analysis for all mandatory fields in profiles based
> on this specification.

---

## §7 Security Considerations

BCP 14 keywords: **zero** in the section preamble (confirmed).

> See the Security Considerations sections of:
>
> *  [RFC9162]
>
> *  [RFC9053]

### §7.1 Choice of Signature Algorithms

BCP 14 keywords: **zero** (confirmed). The section deliberately uses lowercase
"ought to be performed" and "It is recommended" — recorded here as
**non-BCP-14 obligations, excluded from the count** (L709–L715):

> A security analysis ought to be performed to ensure that the digital
> signature algorithm alg has the appropriate strength to secure
> receipts.

> It is recommended to select signature algorithms that share
> cryptographic components with the VDS used; for example, both
> RFC9162_SHA256 and ES256 depend on the SHA256 hash function.

### §7.2 Validity Period

BCP 14 keywords: **1 MAY** (L719).

**MAY (§7.2, L718–L723)**:

> In some cases, receipts **MAY** include strict validity periods, for
> example, activation not too far in the future or expiration not too
> far in the past.  See the iat, nbf, and exp claims in [RFC8392] for
> one way to accomplish this.  The details of expressing validity
> periods are out of scope for this document.

### §7.3 Status Updates

BCP 14 keywords: **zero** (confirmed). Lowercase "should", recorded as a
**non-BCP-14** statement, plus an explicit scope exclusion (L727–L729):

> In some cases, receipts should be "revocable" or "suspendable" after
> being issued, regardless of their validity period.  The details of
> expressing statuses are out of scope for this document.

---

## §8 IANA Considerations

BCP 14 keywords: **zero throughout all of §8** (confirmed — §8, §8.1, §8.2,
§8.2.1, §8.2.2, §8.2.2.1, §8.2.2.2). The IANA rules below are normative as
registry policy, expressed without BCP 14 keywords.

### §8.1 COSE Header Parameter

Registration rules, verbatim (L735–L744):

> IANA has added the COSE header parameters defined in Section 2, and
> as listed in Table 1, to the "COSE Header Parameters" subregistry
> [IANA.cose_header-parameters] in the "CBOR Object Signing and
> Encryption (COSE)" registry group.  These COSE header parameters fall
> in the 'Integer values from 256 to 65535' range (with a Specification
> Required registration procedure (see [RFC8126])).  The Value Registry
> listed for "vds" is the "COSE Verifiable Data Structure Algorithm"
> subregistry.  The map labels in the "vdp" are assigned from the "COSE
> Verifiable Data Structure Proofs" subregistry.

`Table 1: Newly Registered COSE Header Parameters` (L746–L777), verbatim:

```
+==========+=======+=======+============+==============+===========+
| Name     | Label | Value | Value      | Description  | Reference |
|          |       | Type  | Registry   |              |           |
+==========+=======+=======+============+==============+===========+
| receipts | 394   | array |            | Priority     | RFC 9942, |
|          |       |       |            | ordered      | Section 2 |
|          |       |       |            | sequence of  |           |
|          |       |       |            | CBOR encoded |           |
|          |       |       |            | Receipts     |           |
+----------+-------+-------+------------+--------------+-----------+
| vds      | 395   | int   | COSE       | Algorithm    | RFC 9942, |
|          |       |       | Verifiable | identifier   | Section 2 |
|          |       |       | Data       | for          |           |
|          |       |       | Structure  | Verifiable   |           |
|          |       |       |            | Data         |           |
|          |       |       |            | Structures   |           |
|          |       |       |            | that is used |           |
|          |       |       |            | to produce   |           |
|          |       |       |            | Verifiable   |           |
|          |       |       |            | Data         |           |
|          |       |       |            | Structure    |           |
|          |       |       |            | Proofs       |           |
+----------+-------+-------+------------+--------------+-----------+
| vdp      | 396   | map   | map key in | Location for | RFC 9942, |
|          |       |       | COSE       | Verifiable   | Section 2 |
|          |       |       | Verifiable | Data         |           |
|          |       |       | Data       | Structure    |           |
|          |       |       | Structure  | Proofs in    |           |
|          |       |       | Proofs     | COSE Header  |           |
|          |       |       |            | Parameters   |           |
+----------+-------+-------+------------+--------------+-----------+
```

### §8.2 VDS Registries

Verbatim (L780–L783):

> IANA has established the "COSE Verifiable Data Structure Algorithms"
> and "COSE Verifiable Data Structure Proofs" subregistries under a
> Specification Required policy as described in Section 4.6 of
> [RFC8126].

("Specification Required" is an RFC 8126 registration-policy name, not a BCP 14
keyword — it is not all-capitals and is excluded from the count.)

### §8.2.1 Expert Review

Five expert-review criteria, verbatim (L788–L808). All lowercase — normative as
registry policy, **not** BCP 14:

> Expert reviewers (see [RFC8126]) should take into consideration the
> following points:
>
> *  Experts are advised to assign the next available positive integer
>    for VDSs.
>
> *  Point squatting should be discouraged.  Reviewers are encouraged
>    to get sufficient information for registration requests to ensure
>    that the usage is not going to duplicate one that is already
>    registered and that the point is likely to be used in deployments.
>
> *  Specifications are required for all point assignments.  Early
>    allocation is permissible, see Section 2 of [RFC7120].
>
> *  It is not permissible to assign points in the "COSE Verifiable
>    Data Structure Algorithms" registry for which no corresponding
>    entry in the "COSE Verifiable Data Structure Proofs" registry
>    exists, and vice versa.
>
> *  The change controller for related registrations of structures and
>    proofs should be the same.

The fourth bullet is the paired-registration invariant: an algorithm entry may
not exist without a matching proof entry, and a proof entry may not exist
without a matching algorithm entry.

### §8.2.2 Templates and Initial Contents

#### §8.2.2.1 COSE Verifiable Data Structure Algorithms Initial Registry Contents

Registration Template, verbatim (L815–L833):

> Registration Template:
>    Name:
>       This is a descriptive name for the VDS that enables easier
>       reference to the item.
>
>    Value:
>       This is the value used to identify the VDS.
>
>    Description:
>       This field contains a brief description of the VDS.
>
>    Reference:
>       This contains a pointer to the public specification for the
>       VDS.
>
>    Change Controller:
>       For Standards Track RFCs, list the "IETF".  For others, give
>       the name of the responsible party.  Other details (e.g., postal
>       address, email address, home page URI) may also be included.

`Table 2: COSE Verifiable Data Structure Algorithms Initial Registry Contents`
(L835–L847), verbatim:

```
+================+=======+===============+============+===========+
| Name           | Value | Description   | Change     | Reference |
|                |       |               | Controller |           |
+================+=======+===============+============+===========+
| Reserved       | 0     | Reserved      |            | RFC 9942  |
+----------------+-------+---------------+------------+-----------+
| RFC9162_SHA256 | 1     | SHA256 Binary | IETF       | Section   |
|                |       | Merkle Tree   |            | 2.1 of    |
|                |       |               |            | [RFC9162] |
+----------------+-------+---------------+------------+-----------+
```

Initial contents: `Reserved` = 0 (no change controller, reference RFC 9942);
`RFC9162_SHA256` = 1 (change controller IETF, reference Section 2.1 of
[RFC9162]).

#### §8.2.2.2 COSE Verifiable Data Structure Proofs Registry

Registration Template, verbatim (L851–L875):

> Registration Template:
>    Verifiable Data Structure:
>       This value used identifies the related VDS.
>
>    Name:
>       This is a descriptive name for the Proof Type that enables
>       easier reference to the item.
>
>    Label:
>       This is the value used to identify the VDS Proof Type.
>
>    CBOR Type:
>       This contains the CBOR type for the value portion of the label.
>
>    Description:
>       This field contains a brief description of the Proof Type.
>
>    Reference:
>       This contains a pointer to the public specification for the
>       Proof Type.
>
>    Change Controller:
>       For Standards Track RFCs, list the "IETF".  For others, give
>       the name of the responsible party.  Other details (e.g., postal
>       address, email address, home page URI) may also be included.

("This value used identifies the related VDS." is reproduced exactly as printed
in the source, including the grammatical slip.)

`Table 3: COSE Verifiable Data Structure Proofs Initial Registry Contents`
(L877–L892), verbatim:

```
+==========+===========+=====+=====+===========+==========+=========+
|Verifiable|Name       |Label|CBOR |Description|Change    |Reference|
|Data      |           |     |Type |           |Controller|         |
|Structure |           |     |     |           |          |         |
+==========+===========+=====+=====+===========+==========+=========+
|1         |inclusion  |-1   |array|Proof of   |IETF      |RFC 9942,|
|          |proofs     |     |(of  |inclusion  |          |Section  |
|          |           |     |bstr)|           |          |5.2      |
+----------+-----------+-----+-----+-----------+----------+---------+
|1         |consistency|-2   |array|Proof of   |IETF      |RFC 9942,|
|          |proofs     |     |(of  |append-only|          |Section  |
|          |           |     |bstr)|property   |          |5.3      |
+----------+-----------+-----+-----+-----------+----------+---------+
```

Initial contents: for VDS `1`, `inclusion proofs` = label `-1`, CBOR type
array (of bstr); `consistency proofs` = label `-2`, CBOR type array (of bstr).
Both change controller IETF.

---

## Coverage

**Sections walked.** Every section of the document was read in full (all 1033
source lines, in four chunks): front matter and Abstract, §1, §1.1, §2, §3, §4,
§4.1, §4.2, §4.3, §4.4, §4.4.1, §5, §5.1, §5.2, §5.2.1, §5.3, §5.3.1, §6, §6.1,
§6.2, §7, §7.1, §7.2, §7.3, §8, §8.1, §8.2, §8.2.1, §8.2.2, §8.2.2.1, §8.2.2.2,
§9, §9.1, §9.2, Acknowledgements, Contributors, Authors' Addresses.

**BCP 14 keyword tally — 16 total, independently confirmed by grep over the
source.**

| Section | MUST | SHOULD | MAY | REQUIRED | Total | Source lines |
|---|---|---|---|---|---|---|
| §4.2 | 1 | – | – | – | 1 | L217 |
| §4.3 | 2 | – | – | – | 2 | L227, L232 |
| §4.4 | – | 1 | – | – | 1 | L409 |
| §4.4.1 | 2 | – | – | – | 2 | L421, L423 |
| §5.2.1 | – | – | – | 4 | 4 | L495, L498, L517, L520 |
| §5.3.1 | – | – | – | 4 | 4 | L607, L610, L627, L629 |
| §6.2 | 1 | – | – | – | 1 | L695 |
| §7.2 | – | – | 1 | – | 1 | L719 |
| **Total** | **6** | **1** | **1** | **8** | **16** | |

**Discrepancy against the stated ground truth of 16: none.** MUST 6, SHOULD 1,
MAY 1, REQUIRED 8. No MUST NOT, SHALL, SHALL NOT, SHOULD NOT, RECOMMENDED,
NOT RECOMMENDED, or OPTIONAL appears anywhere in the document body outside the
§1.1 enumeration.

**The document's unusual keyword profile is confirmed.** Half the keywords (8 of
16) are `REQUIRED` used as a **field designator** in the §5.2.1 and §5.3.1
receipt field tables — 4 each, marking `alg`, `vds`, `vdp`, and the respective
proof label as mandatory map entries. They are not sentence-level obligations
and carry no subject or verb. Only 8 keywords (the 6 MUSTs, 1 SHOULD, 1 MAY) are
prose obligations.

**Sections confirmed to carry zero BCP 14 keywords:** §2, §3, §5.1, §5.2, §5.3,
§6.1, §7 (preamble), §7.1, §7.3, and all of §8 including §8.1, §8.2, §8.2.1,
§8.2.2, §8.2.2.1 and §8.2.2.2. Also zero in the §4, §4.1 and §5 preambles. The
entire IANA Considerations section — three registry tables, two registration
templates and five expert-review criteria — is written without a single BCP 14
keyword.

**Non-BCP-14 obligations captured and deliberately excluded from the count.**
These use lowercase modal verbs, which §1.1 explicitly denies BCP 14 force:
§4.2 "Implementers should not expect interoperability"; §4.4 "are encouraged to
make their presence mandatory"; §4.4.1 "a separate IANA registration must be
made for each supported algorithm"; §5.2 the block-quoted RFC 9162 failure
condition "If leaf_index is greater than or equal to tree_size, then fail the
proof verification"; §5.3.1 "It is recommended that implementations return a
single boolean result"; §7.1 "A security analysis ought to be performed" and
"It is recommended to select signature algorithms that share cryptographic
components with the VDS used"; §7.3 "receipts should be 'revocable' or
'suspendable'"; and all five §8.2.1 expert-review bullets ("should take into
consideration", "are advised", "should be discouraged", "are encouraged", "are
required", "is permissible", "It is not permissible", "should be the same").

**Both verification procedures captured verbatim, in opposite orders.** §5.2.1
verifies the inclusion **proof first** — the recomputed Merkle Tree root becomes
the COSE_Sign1 payload — **then the signature**. §5.3.1 verifies the
**signature first** and does not check the proof at all if the signature fails,
**then the consistency proof**, closing with the lowercase recommendation to
return a single boolean. Neither procedure uses a BCP 14 keyword.

**Judged non-normative and excluded, with reason.**
- Abstract, Status of This Memo, Copyright Notice, Table of Contents —
  boilerplate and front matter.
- §1 Introduction — motivation only; it states the problem (burden on
  implementers, interoperability challenges) and makes no requirement.
- Figure 2 (§4.3, L341–L393) — the source itself labels it informative: "The
  following informative EDN is provided".
- Figures 6 and 9 (§5.2.1 L530–L551, §5.3.1 L637–L662) — EDN examples
  introduced as "An EDN example for a Receipt containing ... is:"; illustrative
  instances of the normative CDDL already captured above. All three EDN figures
  belong in the examples artifact.
- §9.1 / §9.2 reference lists — the §9.1 entries are the normative references
  this document depends on, but the list is citation metadata, not a
  requirement; it belongs in the record's reference edges.
- Acknowledgements, Contributors, Authors' Addresses — excluded per the
  artifact rules.

**Retained although keyword-free,** because they are normative content rather
than prose obligations: all CDDL blocks (Figures 1, 3, 4, 5, 7, 8 and the
§5.3.1 unprotected-header block), all three IANA tables, both registration
templates, the §2 header-parameter assignments (394/395/396), the §3
terminology, the §5.1 VDS identifiers, and both verification procedures.
