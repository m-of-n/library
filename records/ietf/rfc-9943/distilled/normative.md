---
record: rfc-9943
kind: normative
title: "rfc-9943 — normative statements"
extracted: "2026-09-30"
reviewed_by: "davidhsiaotw 2026-10-05 — 5 of 128 locators opened in source, all resolve; no spliced quotes among the 5; completeness of the extraction not assessed"
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9943, "An Architecture for Trustworthy and Transparent Digital
Supply Chains" (SCITT), Standards Track, June 2026.

Quotations are verbatim from the RFC text. Line wrapping introduced by the RFC
text formatter has been joined with a single space; no word, punctuation mark,
or capitalisation has been altered. BCP 14 keywords are reproduced in the
capitalisation the source uses.

## Finding: every prohibition in this document is phrased positively

This document contains **zero** instances of `MUST NOT`, `SHALL`, `SHALL NOT`,
`SHOULD NOT`, `RECOMMENDED`, and `NOT RECOMMENDED` outside the BCP 14
boilerplate sentence in §1.1. Every constraint is expressed as an affirmative
obligation (`MUST`, `MUST support`, `MUST be set to an empty map`) or as a
permission (`MAY`). There is a single `SHOULD` in the entire document (§6.3),
one `REQUIRED` and one `OPTIONAL` (both §6, both in the "to implement" sense).
An implementer looking for a list of forbidden behaviours will not find one:
the negative space is defined by what the mandatory checks in §5.1.1.1 and the
validation rules in §7.1 require, not by explicit prohibitions.

## §1. Introduction

No normative keyword. Scope statements only (reproduced because they bound
conformance):

- (§1) "For simplicity, the scope of this document is limited to use cases
  originating from the software supply chain domain."
- (§1) "How these statements are managed or stored as well as how participating
  entities discover and notify each other of changes is out of scope of this
  document."

## §1.1. Requirements Notation

The RFC 2119 / RFC 8174 boilerplate paragraph. It is the interpretation clause,
not a requirement, and is excluded from the keyword tally below:

> (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
> "OPTIONAL" in this document are to be interpreted as described in BCP 14
> [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as
> shown here."

## §2. Software Supply Chain Scope (and §2.1, §2.2, §2.2.1, §2.2.2, §2.2.3)

No normative keyword anywhere in §2 or any of its subsections. Use-case
narrative and threat illustration (Figure 1) only. Excluded as motivation.

## §3. Terminology

Three normative keyword instances, in two statements, hide inside the term
definitions: the first statement below carries both a MUST and a MAY. Both
statements bind implementations. (The per-section table under Coverage counts
these three.)

- (§3, *Receipt*) "Receipt Profiles implemented by a TS MUST support inclusion
  proofs and MAY support other Proof Types (see Section 3 of [RFC9942]), such
  as consistency proofs."
- (§3, *Statement*) "The Statement is considered opaque to TS and MAY be
  encrypted."

Non-BCP-14 obligations stated in the same section (lowercase; not counted, but
an implementer must honour them):

- (§3, *Statement*) "To help interpret Statements, they must be tagged with a
  relevant media type (as specified in [RFC6838])."
- (§3, *Transparency Service*) "The identity of a TS is captured by a public
  key that must be known by Relying Parties in order to validate Receipts."

Structural definitions that constrain the wire format:

- (§3, *Envelope*) "In COSE, an Envelope consists of a protected header
  (included in the Issuer's signature) and an unprotected header (not included
  in the Issuer's signature)."
- (§3, *Issuer*) "In SCITT Statements and Receipts, the iss Claim is a member of
  the COSE header parameter 15: CWT Claims defined in [RFC9597], which embeds a
  CBOR Web Token (CWT) Claims Set [RFC8392] within the protected header of a
  COSE Envelope."
- (§3, *Transparent Statement*) "The Receipt is stored in the unprotected header
  of COSE Envelope of the Signed Statement."

## §4. Definition of Transparency

One normative keyword instance — an agility permission that verifiers must
tolerate:

- (§4) "A Receipt's verification key, signing algorithm, validity period, header
  parameters or other claims MAY change each time a Receipt is produced."

Supporting property statement (no keyword, but load-bearing for §7.1):

- (§4) "A Receipt is a signature over one or more VDP that a Signed Statement is
  registered in the VDS. It is universally verifiable without online access to
  the TS."

## §5. Architecture Overview

One normative keyword instance:

- (§5) "In addition, Figure 2 illustrates multiple TSs and multiple Receipts as
  a single Signed Statement MAY be registered with one or more TS."

Scope constraint on what this document specifies (lowercase `must`, not
counted):

- (§5) "In order to accommodate as many TS implementations as possible, this
  document only specifies the format of Signed Statements (which must be used
  by all Issuers) and a very thin wrapper format for Receipts, which specifies
  the TS identity and the agility parameters for the signed proofs."

### §5.1. Transparency Service

- (§5.1) "TSs MUST produce COSE Receipts [RFC9942]."

### §5.1.1. Registration Policies

- (§5.1.1) "To enable auditability, TSs MUST maintain Registration Policies."

Delegated to the implementation (no keyword):

- (§5.1.1) "Beyond the mandatory Registration checks, the scope of additional
  checks, including no additional checks, is up to the implementation."
- (§5.1.1) "This specification leaves implementation, encoding, and
  documentation of Registration Policies and trust anchors to the operator of
  the TS."

### §5.1.1.1. Mandatory Registration Checks

The densest normative section in the document. Ten keyword instances.

1. (§5.1.1.1) "During Registration, a TS MUST syntactically check the Issuer of
   the Signed Statement by cryptographically verifying the COSE signature
   according to [STD96]."
2. (§5.1.1.1) "The Issuer identity MUST be bound to the Signed Statement by
   including an identifier in the protected header."
3. (§5.1.1.1) "If the protected header includes multiple identifiers, all those
   that are registered by the TS MUST be checked."
4. (§5.1.1.1) "TSs MUST maintain a list of trust anchors (see definition of
   trust anchor in [RFC4949]) in order to check the signatures of Signed
   Statements either separately or inside Registration Policies."
5. (§5.1.1.1) "TSs MUST authenticate Signed Statements as part of a Registration
   Policy."
6. (§5.1.1.1) "When using X.509 Signed Statements, the TS MUST build and
   validate a complete certification path from an Issuer's certificate to one of
   the root certificates currently registered as a trust anchor by the TS."
7. (§5.1.1.1) "The protected header of the COSE_Sign1 Envelope MUST include
   either the Issuer's certificate as x5t or the chain including the Issuer's
   certificate as x5chain, as defined in [RFC9360]."
8. (§5.1.1.1) "If x5t is included in the protected header, an x5chain with a
   leaf certificate corresponding to the x5t value MAY be included in the
   unprotected header."
9. (§5.1.1.1) "Registration Policies and trust anchors MUST be made Transparent
   and available to all Relying Parties of the TS by Registering them as Signed
   Statements on the VDS."
10. (§5.1.1.1) "The TS MUST apply the Registration Policy that was most recently
    committed to the VDS at the time of Registration."

Non-normative example accompanying item 4, retained because it fixes the
intended breadth of "trust anchor":

- (§5.1.1.1) "For instance, a trust anchor could be an X.509 root certificate
  (directly or its thumbprint), a pointer to an OpenID Connect identity
  provider, or any other trust anchor that can be referenced in a COSE header
  parameter."

### §5.1.1.2. Auditability of Registration

- (§5.1.1.2) "The operator of a TS MAY update the Registration Policy or the
  trust anchors of a TS at any time."
- (§5.1.1.2) "TSs MUST ensure that for any Signed Statement they register,
  enough information is made available to Auditors to reproduce the Registration
  checks that were defined by the Registration Policies at the time of
  Registration. At a minimum, this consists of the Signed Statements themselves,
  any additional collateral data required to perform their authentication, and
  the applicable Registration Policy at the time of Registration."

### §5.1.2. Initialization and Bootstrapping

- (§5.1.2) "Since the mandatory Registration checks rely on having registered
  Signed Statements for the Registration Policy and trust anchors, TSs MUST
  support at least one of the three following bootstrapping mechanisms:"
  - (§5.1.2) "Preconfigured Registration Policy and trust anchors;"
  - (§5.1.2) "Acceptance of a first Signed Statement whose payload is a valid
    Registration Policy, without performing Registration checks; or"
  - (§5.1.2) "An out-of-band authenticated management interface."

### §5.1.3. Verifiable Data Structure

- (§5.1.3) "This VDS MUST support the following security requirements:"

The three required VDS properties, verbatim:

- (§5.1.3) "Append-only: a property required for a VDS to be applicable to
  SCITT, ensuring that the Statement Sequence cannot be modified, deleted, or
  reordered."
- (§5.1.3) "Non-equivocation: there is no fork in the registered sequence of
  Signed Statements accepted by the TS and committed to the VDS. Everyone with
  access to its content sees the same ordered collection of Signed Statements
  and can check that it is consistent with any Receipts they have verified."
- (§5.1.3) "Replayability: the VDS includes sufficient information to enable
  authorized actors with access to its content to check that each data structure
  representing each Signed Statement has been correctly registered."

Explicit non-requirements:

- (§5.1.3) "In addition to Receipts, some VDSs might support additional Proof
  Types, such as proofs of consistency or proofs of non-inclusion."
- (§5.1.3) "Specific VDSs, such as those described in [RFC9162] and [RFC9942],
  and the review of their security requirements for SCITT are out of scope for
  this document."

### §5.1.4. Adjacent Services

No normative keyword. Deployment guidance only; excluded as motivation.

## §6. Signed Statements

Nine normative keyword instances — the message-format conformance core.

- (§6) "Issuers MAY use different signing keys (identified by kid in the
  protected header from [STD96]) for different Artifacts or sign all Signed
  Statements under the same key."
- (§6) "Additionally, an x5chain that corresponds to either x5t or kid
  identifying the leaf certificate in the included certification path MAY be
  included in the unprotected header of the COSE Envelope."
- (§6) "When using X.509 certificates, support for either x5t or x5chain in the
  protected header is REQUIRED to implement."
- (§6) "Support for kid in the protected header and x5chain in the unprotected
  header is OPTIONAL to implement."
- (§6) "When x5t or x5chain is present in the protected header, the iss Claim
  value MUST be a string that meets URI requirements defined in [RFC8392]."
- (§6) "The iss Claim value's length MUST be between 1 and 8192 characters in
  length."
- (§6) "The kid header parameter MUST be present when neither x5t nor x5chain is
  present in the protected header."
- (§6) "The protected header of a Signed Statement and a Receipt MUST include
  the CWT Claims header parameter as specified in Section 2 of [RFC9597]."
- (§6) "The CWT Claims value MUST include the Issuer Claim (Claim label 1) and
  the Subject Claim (Claim label 2) [IANA.cwt]."

Non-BCP-14 obligations in §6 (lowercase; not counted, but conformance-bearing):

- (§6) "Signed Statements produced by Issuers must be COSE_Sign1 messages, as
  defined by [STD96]."
- (§6) "Profiles and implementation-specific choices should be used to determine
  admissibility of conforming messages."
- (§6) "An Issuer must first decide on a suitable format (3: payload type) to
  serialize the Statement payload."
- (§6) "Issuers and Relying Parties must be able to recognize the Artifact to
  which the Statements pertain by looking at the Signed Statement."

Identification rule and Receipt definition (no keyword):

- (§6) "The iss and sub Claims, within the CWT Claims protected header, are used
  to identify the Artifact the Statement pertains to."
- (§6) "A Receipt is a Signed Statement (COSE_Sign1) with additional Claims in
  its protected header related to verifying the inclusion proof in its
  unprotected header."

Out of scope:

- (§6) "Key discovery protocols are out of scope of this document."

### §6.1. Signed Statement Examples

No BCP 14 keyword. Carries the document's first **normative CDDL** block.

- (§6.1) "Figure 3 illustrates a normative CDDL definition [RFC8610] for the
  protected header and unprotected header of Signed Statements and Receipts."
- (§6.1) "The SCITT architecture specifies the minimal mandatory labels.
  Implementation-specific Registration Policies may define additional mandatory
  labels."

Figure 3 — CDDL Definition for Signed Statements and Receipts (§6.1),
**normative**, verbatim:

```cddl
Signed_Statement = #6.18(COSE_Sign1)
Receipt = #6.18(COSE_Sign1)

COSE_Sign1 = [
  protected   : bstr .cbor Protected_Header,
  unprotected : Unprotected_Header,
  payload     : bstr / nil,
  signature   : bstr
]

Protected_Header = {
  &(CWT_Claims: 15) => CWT_Claims
  ? &(alg: 1) => int
  ? &(content_type: 3) => tstr / uint
  ? &(kid: 4) => bstr
  ? &(x5t: 34) => COSE_CertHash
  ? &(x5chain: 33) => COSE_X509
  * label => any
}

CWT_Claims = {
  &(iss: 1) => tstr
  &(sub: 2) => tstr
  * label => any
}

Unprotected_Header = {
  ? &(x5chain: 33) => COSE_X509
  ? &(receipts: 394)  => [+ bstr .cbor Receipt]
  * label => any
}

label = int / tstr
```

Reading of Figure 3 for implementers: `CWT_Claims` (label 15) is the only
non-optional entry of `Protected_Header`, and within it both `iss` (1) and
`sub` (2) are non-optional — which is exactly what the two §6 `MUST`s above
state in prose. `alg` (1), `content_type` (3), `kid` (4), `x5t` (34) and
`x5chain` (33) are CDDL-optional in the protected header; `x5chain` (33) and
`receipts` (394) are CDDL-optional in the unprotected header. Both maps admit
`* label => any` extension, with `label = int / tstr`.

### §6.2. Signing Large or Sensitive Statements

No normative keyword. States a permitted construction:

- (§6.2) "In these cases, a Statement can be made over the hash of a payload
  rather than the full payload bytes."

### §6.3. Registration of Signed Statements

Twelve normative keyword instances — the registration procedure.

- (§6.3) "To register a Signed Statement, the TS performs the following steps:"

**Step 1 — Client Authentication** (no keyword):

- (§6.3) "A Client authenticates with the TS before registering Signed
  Statements on behalf of one or more Issuers. Authentication and authorization
  are implementation specific and out of scope of the SCITT architecture."

**Step 2 — TS Signed Statement Verification and Validation:**

- (§6.3) "The TS MUST perform signature verification per Section 4.4 of RFC 9052
  [STD96] and MUST verify the signature of the Signed Statement with the
  signature algorithm and verification key of the Issuer per [RFC9360]."
- (§6.3) "The TS MUST also check that the Signed Statement includes the required
  protected headers."
- (§6.3) "The TS MAY validate the Signed Statement payload in order to enforce
  domain-specific registration policies that apply to specific content types."

**Step 3 — Apply Registration Policy:**

- (§6.3) "The TS MUST check the attributes required by a Registration Policy are
  present in the protected headers."
- (§6.3) "Custom Signed Statements are evaluated given the current TS state and
  the entire Envelope and may use information contained in the attributes of
  named policies."

**Step 4 — Register the Signed Statement** (title only in the source; no
normative text).

**Step 5 — Return the Receipt:**

- (§6.3) "This MAY be asynchronous from Registration."
- (§6.3) "The TS MUST be able to provide a Receipt for all registered Signed
  Statements."
- (§6.3) "Details about generating Receipts are described in Section 7."

**Rules spanning the steps:**

- (§6.3) "The last two steps may be shared between a batch of Signed Statements
  registered in the VDS."
- (§6.3) "A TS MUST ensure that a Signed Statement is registered before
  releasing its Receipt."
- (§6.3) "A TS MAY accept a Signed Statement with content in its unprotected
  header and MAY use values from that unprotected header during verification and
  registration policy evaluation."
- (§6.3) "However, the unprotected header of a Signed Statement MUST be set to
  an empty map before the Signed Statement can be included in a Statement
  Sequence."
- (§6.3) "The same Signed Statement may be independently registered in multiple
  TSs, producing multiple independent Receipts. The multiple Receipts may be
  attached to the unprotected header of the Signed Statement creating a
  Transparent Statement."
- (§6.3) "An Issuer that knows of a changed state of quality for an Artifact
  SHOULD Register a new Signed Statement using the same 15 CWT iss and sub
  Claims."

This is the document's only `SHOULD`.

## §7. Transparent Statements

Two normative keyword instances, plus the second **normative CDDL** block.

- (§7) "Client applications MAY register Signed Statements on behalf of one or
  more Issuers."
- (§7) "Client applications MAY request Receipts regardless of the identity of
  the Issuer of the associated Signed Statement."

Construction and timing rules (no keyword, but binding on the format):

- (§7) "The Client (which is not necessarily the Issuer) that registers a Signed
  Statement and receives a Receipt can produce a Transparent Statement by adding
  the Receipt to the unprotected header of the Signed Statement."
- (§7) "When a Signed Statement is registered by a TS a Receipt becomes
  available. When a Receipt is included in a Signed Statement, a Transparent
  Statement is produced."
- (§7) "Receipts are based on signed proofs as described in COSE Receipts
  [RFC9942], which also provides the COSE header parameter semantics for
  label 394."
- (§7) "The Registration time is recorded as the timestamp when the TS added the
  Signed Statement to its VDS."
- (§7) "The type of label 394 receipts in the unprotected header is a CBOR array
  that can contain one or more Receipts (each entry encoded as a .cbor-encoded
  Receipt)."
- (§7) "Figure 7 illustrates a normative CDDL definition of Transparent
  Statements. See Figure 3 for the CDDL rule that defines COSE_Sign1 as
  specified in Section 4.2 of RFC 9052 [STD96]."

Figure 7 — CDDL Definition for a Transparent Statement (§7), **normative**,
verbatim:

```cddl
Transparent_Statement = #6.18(COSE_Sign1)

Unprotected_Header = {
  &(receipts: 394)  => [+ bstr .cbor Receipt]
}
```

Note for implementers: Figure 7 redefines `Unprotected_Header` relative to
Figure 3. In Figure 3 `receipts` (394) is CDDL-optional; in the Transparent
Statement production it is non-optional, and the array is `[+ ...]` — one or
more entries. Making 394 mandatory is the semantic delta between a Signed
Statement and a Transparent Statement, but it is not the only textual one:
Figure 7's map also drops `? &(x5chain: 33) => COSE_X509` and drops
`* label => any`, so as written it is a closed one-member map. Read literally
that forbids the unprotected `x5chain` which §5.1.1.1 and §6 both permit, and
leaves no socket for the additional mandatory labels §6.1 contemplates. The two
figures also give one rule name two bodies, which RFC 8610 does not allow. Both
are recorded as source defects — `messages.yaml` INC-1 and `schema/README.md`
defect 2 — and are not repaired here.

Registry values fixed by the examples in §7 (stated as fact, not as a
requirement, but needed to parse a Receipt):

- (§7) "Per the "COSE Verifiable Data Structure Algorithms" registry documented
  in [RFC9942], the Verifiable Data Structure algorithm RFC9162_SHA256 is
  value 1. Labels identify inclusion proofs (-1) and consistency proofs (-2)."

Header labels appearing in the §7 examples (Figures 8-11), for orientation:
394 = receipts (unprotected), 396 = proofs (unprotected), 395 = Verifiable Data
Structure (protected), 15 = CWT Claims (protected), 1 = alg, 4 = kid.

### §7.1. Validation

Five normative keyword instances — the Relying Party obligations.

- (§7.1) "Relying Parties MUST apply the verification process as described in
  Section 4.4 of RFC 9052 [STD96] when checking the signature of Signed
  Statements and Receipts."
- (§7.1) "A Relying Party MUST trust the verification key or certificate and the
  associated identity of at least one Issuer of a Receipt."
- (§7.1) "A Relying Party MAY decide to verify only a single Receipt that is
  acceptable to them and not check the signature on the Signed Statement or
  Receipts that rely on VDSs they do not understand."
- (§7.1) "Relying Parties MAY be configured to re-verify the Issuer's Signed
  Statement locally."
- (§7.1) "In addition, Relying Parties MAY apply arbitrary validation policies
  after the Transparent Statement has been verified and validated. Such policies
  may use as input all information in the Envelope, the Receipt, and the
  Statement payload, as well as any local state."

API guidance (no keyword):

- (§7.1) "APIs exposing verification logic for Transparent Statements may
  provide more details than a single boolean result."

## §8. Privacy Considerations

No normative keyword. Retained statements that constrain deployment:

- (§8) "Interactions with TSs are expected to use appropriately strong
  encryption and authorization technologies."
- (§8) "Issuers and Clients are responsible for verifying that the TS's privacy
  and security posture is suitable for the contents of the Signed Statements
  they submit prior to Registration."
- (§8) "Issuers must carefully review the inclusion of private, confidential, or
  Personally Identifiable Information (PII) in their Statements against the TS's
  privacy posture." (lowercase `must`; not counted)

## §9. Security Considerations

No normative keyword in §9 itself. The three guarantees, verbatim, because they
are what an implementation is meant to deliver:

- (§9) "Statements made by Issuers about supply chain Artifacts are identifiable
  and can be authenticated."
- (§9) "Statement provenance and history can be independently and consistently
  audited."
- (§9) "Issuers can efficiently prove that their Statement is logged by a TS."
- (§9) "The first guarantee is achieved by requiring Issuers to sign their
  Statements. The second guarantee is achieved by proving a Signed Statement is
  present in a VDS. The third guarantee is achieved by the combination of both
  of these steps."

### §9.1. Ordering of Signed Statements

No normative keyword. One constraint on Relying Party assumptions:

- (§9.1) "Unless advertised in the TS Registration Policy, the Relying Party
  cannot assume that the ordering of Signed Statements in the VDS matches the
  ordering of their issuance."

### §9.2. Accuracy of Statements

No normative keyword.

- (§9.2) "Issuers can make false Statements either intentionally or
  unintentionally; registering a Statement only proves it was produced by an
  Issuer."

### §9.3. Issuer Participation

No normative keyword.

- (§9.3) "It is important for Relying Parties not to accept Signed Statements
  for which they cannot discover Receipts issued by a TS they trust."

### §9.4. Key Management

The only normative keyword instance anywhere in §9. It is a single `MUST` whose
scope is a three-item bullet list.

- (§9.4) "Issuers and TSs MUST:"
  - (§9.4) "carefully protect their private signing keys"
  - (§9.4) "avoid using keys for more than one purpose"
  - (§9.4) "rotate their keys at a cryptoperiod (defined in [RFC4949])
    appropriate for the key-algorithm and domain-specific regulations"

All three bullets are inside the `MUST`. Note the third is the only place the
document mandates key rotation, and it defers the period to "the key-algorithm
and domain-specific regulations".

### §9.4.1. Verifiable Data Structure

No normative keyword.

- (§9.4.1) "The security considerations for specific VDSs are out of scope for
  this document. See [RFC9942] for the generic security considerations that
  apply to VDSs and Receipts."

### §9.4.2. Key Compromise

No normative keyword.

- (§9.4.2) "TSs whose receipt signing keys have been compromised can roll back
  their Statement Sequence to a point before compromise, establish new
  credentials, and use the new credentials to issue fresh Receipts going
  forward."
- (§9.4.2) "Revocation strategies for compromised keys are out of scope for this
  document."

### §9.4.3. Bootstrapping

No normative keyword, but a clear preference ordering over the three §5.1.2
mechanisms, stated without BCP 14 words:

- (§9.4.3) "Bootstrapping mechanisms that solely rely on Statement registration
  to set and update registration policy can be audited without additional
  implementation-specific knowledge; therefore, they are preferable. Mechanisms
  that rely on preconfigured values and do not allow updates are unsuitable for
  use in long-lived service deployments in which the ability to patch a
  potentially faulty policy is essential."

### §9.5. Implications of Media Type Usage

No normative keyword.

- (§9.5) "The Statement (scitt-statement+cose) and Receipt (scitt-receipt+cose)
  media types describe the expected content of COSE envelope headers. The
  payload media type (content type) is included in the COSE envelope header."
- (§9.5) "Both media types describe COSE_Sign1 messages, which include a
  signature and therefore provide integrity protection."

### §9.6. Cryptographic Agility

No normative keyword.

- (§9.6) "Because the SCITT architecture leverages [STD96] for Statements and
  Receipts, it benefits from the format's cryptographic agility."

### §9.7. Threat Model

No normative keyword. Residual-property statements:

- (§9.7) "The SCITT architecture does not require trust in a single centralized
  TS."
- (§9.7) "It is the role of the relying party to decide which TSs and Issuers
  they choose to trust for their scenario."
- (§9.7) "Relying Parties and Auditors need not be trusted by other actors. So
  long as actors maintain proper control of their signing keys and identity
  infrastructure they cannot "frame" an Issuer or a TS for Signed Statements
  they did not issue or register."

## §10. IANA Considerations

No BCP 14 keyword; entirely normative in effect. Registrations are complete
(the RFC uses the past tense "IANA has registered").

- (§10) "IANA has registered the following media types in the "application"
  subregistry of the "Media Types" registry group [IANA.media-types]:"
  - (§10) "application/scitt-statement+cose (see Section 10.1)"
  - (§10) "application/scitt-receipt+cose (see Section 10.2)"

### §10.1. Registration of application/scitt-statement+cose

Table 1: SCITT Signed Statement Media Type Registration (§10.1), verbatim:

| Name | Template | Reference |
| --- | --- | --- |
| scitt-statement+cose | application/scitt-statement+cose | Section 6 of RFC 9943 |

Full registration template (§10.1), verbatim field by field:

- Type name: `application`
- Subtype name: `scitt-statement+cose`
- Required parameters: `N/A`
- Optional parameters: `N/A`
- Encoding considerations: `binary (CBOR data item)`
- Security considerations: `Section 9.5 of RFC 9943`
- Interoperability considerations: `none`
- Published specification: `RFC 9943`
- Applications that use this media type: "Used to provide an identifiable and
  non-repudiable Statement about an Artifact signed by an Issuer."
- Fragment identifier considerations: `N/A`
- Additional information:
  - Deprecated alias names for this type: `N/A`
  - Magic number(s): `N/A`
  - File extension(s): `.scitt`
  - Macintosh file type code(s): `N/A`
- Person & email address to contact for further information: `iesg@ietf.org`
- Intended usage: `COMMON`
- Restrictions on usage: `none`
- Author/Change controller: `IETF`

### §10.2. Registration of application/scitt-receipt+cose

Table 2: SCITT Receipt Media Type Registration (§10.2), verbatim:

| Name | Template | Reference |
| --- | --- | --- |
| scitt-receipt+cose | application/scitt-receipt+cose | Section 7 of RFC 9943 |

Full registration template (§10.2), verbatim field by field:

- Type name: `application`
- Subtype name: `scitt-receipt+cose`
- Required parameters: `N/A`
- Optional parameters: `N/A`
- Encoding considerations: `binary (CBOR data item)`
- Security considerations: `Section 9.5 of RFC 9943`
- Interoperability considerations: `none`
- Published specification: `RFC 9943`
- Applications that use this media type: "Used to establish or verify
  transparency over Statements. Typically emitted by a TS for the benefit of
  Relying Parties wanting to ensure Non-equivocation over all or part of a
  Statement Sequence."
- Fragment identifier considerations: `N/A`
- Additional information:
  - Deprecated alias names for this type: `N/A`
  - Magic number(s): `N/A`
  - File extension(s): `.receipt`
  - Macintosh file type code(s): `N/A`
- Person & email address to contact for further information: `iesg@ietf.org`
- Intended usage: `COMMON`
- Restrictions on usage: `none`
- Author/Change controller: `IETF`

### §10.3. CoAP Content-Format Registrations

- (§10.3) "IANA has registered the following Content-Format numbers in the "CoAP
  Content-Formats" subregistry within the "Constrained RESTful Environments
  (CoRE) Parameters" registry group [IANA.core-parameters] in the 256-9999
  range:"

Table 3: SCITT Content-Formats Registration (§10.3), verbatim:

| Content Type | Content Coding | ID | Reference |
| --- | --- | --- | --- |
| application/scitt-statement+cose | - | 277 | RFC 9943 |
| application/scitt-receipt+cose | - | 278 | RFC 9943 |

## §11.1. Normative References

The normative dependency set an implementation must satisfy, as listed:

- `[IANA.core-parameters]` — IANA, "Constrained RESTful Environments (CoRE)
  Parameters"
- `[IANA.cwt]` — IANA, "CBOR Web Token (CWT) Claims"
- `[IANA.media-types]` — IANA, "Media Types"
- `[RFC2119]` — "Key words for use in RFCs to Indicate Requirement Levels",
  BCP 14
- `[RFC6838]` — "Media Type Specifications and Registration Procedures", BCP 13
- `[RFC8174]` — "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words",
  BCP 14
- `[RFC8392]` — "CBOR Web Token (CWT)"
- `[RFC8610]` — "Concise Data Definition Language (CDDL): A Notational
  Convention to Express Concise Binary Object Representation (CBOR) and JSON
  Data Structures"
- `[RFC9360]` — "CBOR Object Signing and Encryption (COSE): Header Parameters
  for Carrying and Referencing X.509 Certificates"
- `[RFC9597]` — "CBOR Web Token (CWT) Claims in COSE Headers"
- `[RFC9942]` — "CBOR Object Signing and Encryption (COSE) Receipts"
- `[STD94]` — Internet Standard 94; at the time of writing comprises RFC 8949,
  "Concise Binary Object Representation (CBOR)"
- `[STD96]` — Internet Standard 96; at the time of writing comprises RFC 9052,
  "CBOR Object Signing and Encryption (COSE): Structures and Process", and
  RFC 9338, "CBOR Object Signing and Encryption (COSE): Countersignatures"

Note: `[RFC4949]` ("Internet Security Glossary, Version 2") is cited twice for
normative-sounding purposes — the definition of "trust anchor" in §5.1.1.1 and
of "cryptoperiod" in §9.4 — yet it is listed under §11.2 Informative
References, not §11.1. An implementer relying on those two definitions is
relying on an informative reference.

## Coverage

**Sections walked.** All of them, front matter to §11.2: Abstract, §1, §1.1,
§2, §2.1, §2.2, §2.2.1, §2.2.2, §2.2.3, §3, §4, §5, §5.1, §5.1.1, §5.1.1.1,
§5.1.1.2, §5.1.2, §5.1.3, §5.1.4, §6, §6.1, §6.2, §6.3, §7, §7.1, §8, §9,
§9.1, §9.2, §9.3, §9.4, §9.4.1, §9.4.2, §9.4.3, §9.5, §9.6, §9.7, §10, §10.1,
§10.2, §10.3, §11.1, §11.2, Contributors, Authors' Addresses. Source is 1772
lines of RFC plain text.

**Keyword tally: 50 instances**, excluding the §1.1 BCP 14 boilerplate
sentence. By keyword: MUST 30, MAY 17, REQUIRED 1, OPTIONAL 1, SHOULD 1.
MUST NOT 0, SHALL 0, SHALL NOT 0, SHOULD NOT 0, RECOMMENDED 0,
NOT RECOMMENDED 0.

Per section:

| Section | MUST | MAY | REQUIRED | OPTIONAL | SHOULD | Total |
| --- | --- | --- | --- | --- | --- | --- |
| §3 Terminology | 1 | 2 | 0 | 0 | 0 | 3 |
| §4 Definition of Transparency | 0 | 1 | 0 | 0 | 0 | 1 |
| §5 Architecture Overview | 0 | 1 | 0 | 0 | 0 | 1 |
| §5.1 Transparency Service | 1 | 0 | 0 | 0 | 0 | 1 |
| §5.1.1 Registration Policies | 1 | 0 | 0 | 0 | 0 | 1 |
| §5.1.1.1 Mandatory Registration Checks | 9 | 1 | 0 | 0 | 0 | 10 |
| §5.1.1.2 Auditability of Registration | 1 | 1 | 0 | 0 | 0 | 2 |
| §5.1.2 Initialization and Bootstrapping | 1 | 0 | 0 | 0 | 0 | 1 |
| §5.1.3 Verifiable Data Structure | 1 | 0 | 0 | 0 | 0 | 1 |
| §6 Signed Statements | 5 | 2 | 1 | 1 | 0 | 9 |
| §6.3 Registration of Signed Statements | 7 | 4 | 0 | 0 | 1 | 12 |
| §7 Transparent Statements | 0 | 2 | 0 | 0 | 0 | 2 |
| §7.1 Validation | 2 | 3 | 0 | 0 | 0 | 5 |
| §9.4 Key Management | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **30** | **17** | **1** | **1** | **1** | **50** |

**Sections with no BCP 14 keyword at all** (confirmed by exhaustive scan):
§1, §1.1 (boilerplate only), §2 and all of §2.1-§2.2.3, §5.1.4, §6.1, §6.2,
§8, §9, §9.1, §9.2, §9.3, §9.4.1, §9.4.2, §9.4.3, §9.5, §9.6, §9.7, §10,
§10.1, §10.2, §10.3, §11 and both reference subsections.

**Discrepancy against the briefed ground truth.** The brief stated that "§1,
§2, §4, §8 and all of §9 except §9.4 carry no normative keyword at all." That
is correct for §1, §2, §8 and §9 (only §9.4 carries one), but **wrong for §4**:
§4 contains one `MAY` — "A Receipt's verification key, signing algorithm,
validity period, header parameters or other claims MAY change each time a
Receipt is produced." Excluding it would give 49, not 50. §6.1, §6.2 and §5.1.4
are the other keyword-free subsections not named in the brief. Everything else
in the brief — the 50 total, the MUST 30 / MAY 17 / REQUIRED 1 / OPTIONAL 1 /
SHOULD 1 split, the zero counts for the six unused keywords, and the density in
§5.1.1.1 (10), §6 (9), §6.3 (12), §7.1 (5) — was confirmed independently
against the source.

**Judged non-normative and excluded.**

- §1 Introduction narrative, §2 and all its subsections (SSC problem statement,
  Figure 1 life-cycle threats, and the three use-case walkthroughs in §2.2.1-3):
  motivation and illustration. They constrain nothing.
- Abstract, Status of This Memo, Copyright Notice, Table of Contents,
  Contributors, Authors' Addresses: front and back matter.
- §11.2 Informative References: informative by definition. Flagged above only
  because `[RFC4949]` is cited for two definitions used inside normative
  sentences.
- Figures 1, 2 and 6 (ASCII diagrams): Figure 1 is a threat illustration,
  Figure 2 a concept relationship diagram, Figure 6 a data-flow sketch for
  hash-of-payload signing. None defines a format. Figures 3 and 7 are the two
  the source itself calls "normative CDDL" and are reproduced in full.
- Figures 4, 5, 8, 9, 10 and 11 (CBOR Extended Diagnostic Notation examples):
  non-normative examples. Not reproduced, but the header labels and the
  `RFC9162_SHA256 = 1` / inclusion-proof `-1` / consistency-proof `-2` registry
  values they depend on are recorded under §7, since a parser needs them.
- §1.1 RFC 2119 boilerplate: reproduced once above as the interpretation clause
  and excluded from the tally, per the counting convention.
- Lowercase `must` / `should` sentences (§3 x2, §5, §6 x4, §8): these read as
  obligations but are not BCP 14 keywords, so they are recorded verbatim in
  their sections under an explicit "non-BCP-14" label and kept out of the count.
  §6's "Signed Statements produced by Issuers must be COSE_Sign1 messages" is
  the most consequential of them — a format requirement stated without a
  keyword.
