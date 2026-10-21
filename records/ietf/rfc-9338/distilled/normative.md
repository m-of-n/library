---
record: rfc-9338
kind: normative
title: "rfc-9338 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9338 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9338, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing is paraphrased and nothing is retyped:
each fenced block was cut from `.cache/rfc-9338.txt` by line range by script.

| | |
|---|---|
| **Source** | `.cache/rfc-9338.txt`, 921 newline-delimited lines (922 by `split("\n")`) |
| **Digest** | `3fd3a4b1cb4060070ffcf6104de0c12c6c5bed6cf2329d9019a16f7717365dde` |
| **Standing** | **STD 96**, Standards Track, `Updates: 9052` — all three off the front page, quoted below |
| **BCP 14 keywords** | **2**, both `MUST` — §4 (determinism) and §6 (tag length). Nothing else in the document is in all capitals |
| **CDDL fragments** | **5** blocks, **8** rules (§1.2 ×2, §2 ×2, §3.1 ×2, §3.2 ×1, §3.3 ×1) |
| **Worked examples** | **6**, Appendix A, in CBOR diagnostic notation; no octets printed for any whole message |
| **Errata** | **1** — EID 7338, *Reported*, Technical, §3.3 (searched 2026-10-20; see §3.3 below) |

**Region convention.** Each digest is the sha256 of the region's lines joined
by `\n` with no trailing newline.

**No page decoration, and no region is split.** This rendering has **0 form
feeds** and no running headers or footers in its 921 lines, checked with the
same patterns that match 25 page breaks in RFC 8392's rendering. Built with
`split("\n")`, never `splitlines()`.

**Two statements of force and nothing else.** Every obligation this document
places on a migrating implementation — the whole backward-compatibility
contract of a repair document — is **lowercase**, in a document that recites
BCP 14 in §1.1. `requirements.yaml`'s reconciliation names each one.

---

## Front page — the standing

`STD: 96` and `Updates: 9052` are facts about this document's place, not
commentary on it: RFC 9052 removed all countersignature text (§1 below) and
this document puts the mechanism back, so Internet Standard 96 is only
complete as the pair. `Category: Standards Track` is on the same page.

```
Internet Engineering Task Force (IETF)                         J. Schaad
Request for Comments: 9338                                August Cellars
STD: 96                                                    December 2022
Updates: 9052                                                           
Category: Standards Track                                               
ISSN: 2070-1721
```

*Source `.cache/rfc-9338.txt` lines 5-10 · `sha256:ef4ff1e216ffa3406658c0e0e79e29ed8087360559fbcc8d1b614ec9c1dd4c56`*


The Abstract states the deliverable set, and the `CBOR tags` plural is
answered by exactly one tag in §5.1.

```
Abstract

   Concise Binary Object Representation (CBOR) is a data format designed
   for small code size and small message size.  CBOR Object Signing and
   Encryption (COSE) defines a set of security services for CBOR.  This
   document defines a countersignature algorithm along with the needed
   header parameters and CBOR tags for COSE.  This document updates RFC
   9052.
```

*Source `.cache/rfc-9338.txt` lines 15-22 · `sha256:8edb70072f96fc7fa9872984baaf14e029288eb46ab06323f701bf48d2287195`*


---

## §1 — Introduction

**Why the document exists.** The defect is named against a specific structure
and a specific section of the obsoleted document.

```
   A countersignature is a second signature that confirms the primary
   signature.  During the process of advancing CBOR Object Signing and
   Encryption (COSE) to Internet Standard, it was noticed that the
   description of the security properties of countersignatures was
   incorrect for the COSE_Sign1 structure mentioned in Section 4.5 of
   [RFC8152].  To remedy this situation, the COSE Working Group decided
   to remove all of the countersignature text from [RFC9052], which
   obsoletes [RFC8152].  This document defines a new countersignature
   with the desired security properties.
```

*Source `.cache/rfc-9338.txt` lines 103-111 · `sha256:3b1e1e04b3ae4c7464760cae5d4432dbd21bd931c8e331a5eb76cd4f4d1cc240`*


**What the defect was.** Note *"the third slot of the array"* — this sentence
is the only place the document says how the RFC 8152 algorithm chose the value
it covered, and it is load-bearing for reading §3.3's `other_fields` rule. It
also concedes that the MAC structures were known to be wrong and shipped.

```
   The problem with the previous countersignature algorithm was that the
   cryptographically computed value was not always included.  The
   initial assumption that the cryptographic value was in the third slot
   of the array was known not to be true at the time, but in the case of
   the Message Authentication Code (MAC) structures this was not deemed
   to be an issue.  The new algorithm defined in this document requires
   the inclusion of more values for the countersignature computation.
   The exception to this is the COSE_Signature structure where there is
   no cryptographically computed value.
```

*Source `.cache/rfc-9338.txt` lines 113-121 · `sha256:d04dfae498f47ae223d83fead6c5e8c6673d37469e18b37f7c2cee1df40f959a`*


**The compatibility design, and the sentence that fixes which structures
change.** *"the same countersignature value in those cases where the computed
cryptographic value was already included"* is what makes the version-2
algorithm a no-op for five of the eight target structures; §3.3's arithmetic
is where that lands. See `design-notes.md` §2.

```
   The new algorithm defined in this document is designed to produce the
   same countersignature value in those cases where the computed
   cryptographic value was already included.  This means that for those
   structures the only thing that would need to be done is to change the
   value of the header parameter.
```

*Source `.cache/rfc-9338.txt` lines 123-127 · `sha256:83a0c123b5df98aa9003ddecea785879fe3a9c662bcd98c24df6905e5a865334`*


**The whole migration contract, and not one BCP 14 keyword in it.**
*"encouraged"*, *"will migrate"*, *"must be supported"*, *"may be
supported"* — all lowercase, 50 lines before §1.1 recites the keywords in
capitals. This is the document's entire statement about interoperating with
RFC 8152 senders.

```
   With the publication of this document, implementers are encouraged to
   migrate uses of the previous countersignature algorithm to the one
   specified in this document.  In particular, uses of
   "CounterSignature" will migrate to "CounterSignatureV2", and uses of
   "CounterSignature0" will migrate to "CounterSignature0V2".  In
   addition, verification of "CounterSignature" must be supported by new
   implementations to remain compatible with senders that adhere to
   [RFC8152], which assumes that all implementations will understand
   "CounterSignature" as header parameter label 7.  Likewise,
   verification of "CounterSignature0" may be supported for further
   compatibility.
```

*Source `.cache/rfc-9338.txt` lines 129-139 · `sha256:fba197f8c3e5bd7c3abcad8f9cbff4fa98fa886a04686dfdbf69c95bff41b5e4`*


### §1.1 — Requirements Terminology

The recital. It is quoted here and deliberately has **no** entry in
`requirements.yaml`: it recites eleven keywords and constrains nothing, and
counting it would add eleven phantom keywords to the reconciliation.

```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-9338.txt` lines 143-147 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*


### §1.2 — CBOR Grammar

**The extraction promise and the initial non-terminal.** The XPath expression
is the document's own claim that its CDDL is machine-extractable; erratum 7338
(§3.3) is a syntax error in the result. Note also that the collected CDDL
names `COSE_Signature` and `empty_or_serialized_map`, which are defined in
RFC 9052 and not here, so the extracted file does not stand alone —
`schema/README.md` has the dangling-reference census.

```
   CBOR grammar in this document uses the Concise Data Definition
   Language (CDDL) [RFC8610].

   The collected CDDL can be extracted from the XML version of this
   document via the XPath expression below.  (Depending on the XPath
   evaluator one is using, it may be necessary to deal with &gt; as an
   entity.)

         //sourcecode[@type='cddl']/text()

   CDDL expects the initial non-terminal symbol to be the first symbol
   in the file.  For this reason, the first fragment of CDDL is
   presented here.

         start = COSE_Countersignature_Tagged / Internal_Types

         ; This is defined to make the tool quieter:
         Internal_Types = Countersign_structure / COSE_Countersignature0

   The non-terminal Internal_Types is defined for dealing with the
   automated validation tools used during the writing of this document.
   It references those non-terminals that are used for security
   computations but are not emitted for transport.
```

*Source `.cache/rfc-9338.txt` lines 151-173 · `sha256:c1f980cc4b16299ec965d2f1237bbb1feeca7c57200e6d3a5453a500873fa786`*


### §1.3 — Document Terminology

**The definition of *context*, which is what §3.2 leans on.** Abbreviated
countersignatures take their verification parameters from *this* context —
*"information that is not part of the COSE message"* — which is why a third
party cannot use them.

```
   In this document, we use the following terminology.

   "Byte" is a synonym for "octet".

   The Constrained Application Protocol (CoAP) is a specialized web
   transfer protocol for use in constrained systems.  It is defined in
   [RFC7252].

   "Context" is used throughout this document to represent information
   that is not part of the COSE message.  Information that is part of
   the context can come from different sources, including protocol
   interactions, associated key structures, and application
   configuration.  The context to use can be implicit, identified using
   either the "kid context" header parameter defined in [RFC8613] or a
   protocol-specific identifier.  Context should generally be included
   in the cryptographic construction; for more details, see Section 4.4
   of [RFC9052].

   The term "byte string" is used for sequences of bytes, while the term
   "text string" is used for sequences of characters.
```

*Source `.cache/rfc-9338.txt` lines 177-196 · `sha256:46db7d0480f7b928cb73f6a9d62515fe57412e6d755cba42cafca544393d11a0`*


---

## §2 — Countersignature Header Parameters

**The permitted-target list, and the first of the document's two
disagreements with itself.** Seven structures, and **`COSE_Sign` is not among
them**. §3.3's list adds `COSE_Sign` and drops `COSE_recipient`. Note also
that this is the *only* labelled entry in the section: **label 12 gets no
prose definition and no permitted-target list anywhere in the document.**

```
   This section defines a set of common header parameters.  A summary of
   these header parameters can be found in Table 1.  This table should
   be consulted to determine the value of the label and the type of the
   value.

   The set of header parameters defined in this section is:

   V2 countersignature:  This header parameter holds one or more
      countersignature values.  Countersignatures provide a method of
      having a second party sign some data.  The countersignature header
      parameter can occur as an unprotected attribute in any of the
      following structures that are defined in [RFC9052]: COSE_Sign1,
      COSE_Signature, COSE_Encrypt, COSE_recipient, COSE_Encrypt0,
      COSE_Mac, and COSE_Mac0.  Details of version 2 countersignatures
      are found in Section 3.
```

*Source `.cache/rfc-9338.txt` lines 200-214 · `sha256:df3b54631986bb8f5b7d695958f9dcb0c31e59927860c43e9029ff1b5638f1f1`*


**Table 1 — the two registrations, verbatim including its rules.**

```
   +=================+=====+==========================+================+
   |Name             |Label| Value Type               |Description     |
   +=================+=====+==========================+================+
   |Countersignature |11   | COSE_Countersignature /  |V2              |
   |version 2        |     | [+ COSE_Countersignature |countersignature|
   |                 |     | ]                        |attribute       |
   +-----------------+-----+--------------------------+----------------+
   |Countersignature0|12   | COSE_Countersignature0   |V2 Abbreviated  |
   |version 2        |     |                          |Countersignature|
   +-----------------+-----+--------------------------+----------------+

                     Table 1: Common Header Parameters
```

*Source `.cache/rfc-9338.txt` lines 216-227 · `sha256:472bb5909b7780e347565615030090fd914f97719b7a097087f391be72e6b4df`*


**The header CDDL. Both parameters are optional in every map**, which is the
only thing the document says about where they may appear beyond §2's prose
list; the CDDL itself constrains no target.

```
   The CDDL fragment that represents the set of header parameters
   defined in this section is given below.  Each of the header
   parameters is tagged as optional because they do not need to be in
   every map; however, the header parameters required in specific maps
   are discussed above.

         CountersignatureV2_header = (
             ? 11 => COSE_Countersignature / [+ COSE_Countersignature]
         )

         Countersignature0V2_header = (
             ? 12 => COSE_Countersignature0
         )
```

*Source `.cache/rfc-9338.txt` lines 229-241 · `sha256:5633716f7d3b496b005b936ada00e6cc647ed243cc92d702aa7cd9e0e5a913c7`*


---

## §3 — Version 2 Countersignatures

**The notary analogy, and the withdrawal of its essential element.** *"such a
timestamp has not yet been defined for COSE"*. Also the extension claim —
*"all of the security structures defined"* — and the separate-operation rule
that `[GROUP-OSCORE]` is cited for.

```
   A countersignature is normally defined as a second signature that
   confirms a primary signature.  A normal example of a countersignature
   is the signature that a notary public places on a document as
   witnessing that you have signed the document.  A notary typically
   includes a timestamp to indicate when notarization occurs; however,
   such a timestamp has not yet been defined for COSE.  A timestamp,
   once defined in a future document, might be included as a protected
   header parameter.  Thus, applying a countersignature to either the
   COSE_Signature or COSE_Sign1 objects matches this traditional
   definition.  This document extends the context of a countersignature
   to allow it to be applied to all of the security structures defined.
   The countersignature needs to be treated as a separate operation from
   the initial operation even if it is applied by the same user, as is
   done in [GROUP-OSCORE].
```

*Source `.cache/rfc-9338.txt` lines 245-258 · `sha256:9fc6626f4620b4d6feff65e292cf63c90df9921b00dce3d29d426467c7558f66`*


**The two forms, and the non-convertibility rule with its reason.** The reason
given is *"a parameter identifying which structure is being used"* — the
`context` text string of §3.3, which is also the document's only domain
separator between version 1 and version 2.

```
   COSE supports two different forms for countersignatures.  Full
   countersignatures use the structure COSE_Countersignature, which has
   the same structure as COSE_Signature.  Thus, full countersignatures
   can have protected and unprotected attributes, including chained
   countersignatures.  Abbreviated countersignatures use the structure
   COSE_Countersignature0.  This structure only contains the signature
   value and nothing else.  The structures cannot be converted between
   each other; as the signature computation includes a parameter
   identifying which structure is being used, the converted structure
   will fail signature validation.
```

*Source `.cache/rfc-9338.txt` lines 260-269 · `sha256:6f873d9ca0c2dbc507780dc99a27b3c06da7d7675cd008189831ba58b65b483f`*


**The algorithm change, stated at its widest.** *"all of the structures rather
than just for a subset"*. §3.3's arithmetic does not deliver this for five of
the eight structures; `design-notes.md` §3 is the derivation.

```
   The version 2 countersignature changes the algorithm used for
   computing the signature from the original version that is specified
   in Section 4.5 of [RFC8152].  The new version now includes the
   cryptographic material generated for all of the structures rather
   than just for a subset.
```

*Source `.cache/rfc-9338.txt` lines 271-275 · `sha256:939657a1a63aefdf7eef15e6e842883b021ac07711a8ff87a83cfc8daca068e7`*


**The per-structure security semantics — and the sentence that §1's
`COSE_Signature` concession has to be reconciled with.** *"When done on a
COSE_Signature or COSE_Sign1, the normal countersignature semantics are
preserved"*. `COSE_Sign` is given **no** semantics here, although §3.3 permits
it and Appendix A's only signed-message example uses it.

```
   COSE was designed for uniformity in how the data structures are
   specified.  One result of this is that for COSE one can expand the
   concept of countersignatures beyond just the idea of signing a
   signature to being able to sign most of the structures without having
   to create a new signing layer.  When creating a countersignature, one
   needs to be clear about the security properties that result.  When
   done on a COSE_Signature or COSE_Sign1, the normal countersignature
   semantics are preserved.  That is, the countersignature makes a
   statement about the existence of a signature and, when used with a
   yet-to-be-specified timestamp, a point in time at which the signature
   exists.  When done on a COSE_Mac or COSE_Mac0, the payload is
   included as well as the MAC value.  When done on a COSE_Encrypt or
   COSE_Encrypt0, the existence of the encrypted data is attested to.
   It should be noted that there is a distinction between attesting to
   the encrypted data as opposed to attesting to the unencrypted data.
   If the latter is what is desired, then one needs to apply a signature
   to the data and then encrypt that.  It is always possible to
   construct cases where the use of two different keys results in
   successful decryption, where the tag check succeeds, but two
   completely different plaintexts are produced.  This situation is not
   detectable by a countersignature on the encrypted data.
```

*Source `.cache/rfc-9338.txt` lines 277-297 · `sha256:17920460a498c8ec8c0da02b30d2d84a6aa3631735ae58437d2021cb8e053d81`*


### §3.1 — Full Countersignatures

**The countersigner is unrelated to the producer, and chaining is unbounded.**
This is the `R-M-12` exposure: a second, nested instance of the same global
header label space, scoped by nothing.

```
   The COSE_Countersignature structure allows for the same set of
   capabilities as a COSE_Signature.  This means that all of the
   capabilities of a signature are duplicated with this structure.
   Specifically, the countersigner does not need to be related to the
   producer of what is being countersigned, as key and algorithm
   identification can be placed in the countersignature attributes.
   This also means that the countersignature can itself be
   countersigned.  This is a feature required by protocols such as long-
   term archiving services.  More information on how countersignatures
   are used can be found in the evidence record syntax described in
   [RFC4998].
```

*Source `.cache/rfc-9338.txt` lines 301-311 · `sha256:9eac935baaae0cbf73bf0d119fe92f9608d85b7700f8fb48d8e2d4e92ecbd548`*


**Tagged or untagged, CBOR tag 19, and the two CDDL rules.** *"depending on
the context"* is what makes the header-parameter form tag-free — the hinge of
`design-notes.md` §7 on MD-3.

```
   The full countersignature structure can be encoded as either tagged
   or untagged, depending on the context.  A tagged
   COSE_Countersignature structure is identified by the CBOR tag 19.
   The countersignature structure is the same as that used for a signer
   on a signed object.  The CDDL fragment for full countersignatures is:

         COSE_Countersignature_Tagged = #6.19(COSE_Countersignature)
         COSE_Countersignature = COSE_Signature
```

*Source `.cache/rfc-9338.txt` lines 313-320 · `sha256:da1be7c394c81dea18f01e53892b3be0652d63561d3ac97747258707383e89c1`*


**The cross-references, one of which does not describe its own example.**
*"a countersignature on a signature ... Appendix A.1.1"* — A.1.1 carries label
11 in the **body's** unprotected map of a tagged `COSE_Sign`, so it is a
countersignature on a signed *message*, not on a `COSE_Signature`. Recorded as
a source defect in `design-notes.md` §10.

```
   The details of the fields of a countersignature can be found in
   Section 4.1 of [RFC9052].

   An example of a countersignature on a signature can be found in
   Appendix A.1.1.  An example of a countersignature in an encryption
   object can be found in Appendix A.3.1.
```

*Source `.cache/rfc-9338.txt` lines 322-327 · `sha256:27ca4a6c159ae81d75d4921a71acb80e6ae86ebdb42a74256b4928651af5aab4`*


**The algorithm-class restriction, stated once, as an aside.** A real
constraint on any algorithm list: signature schemes with message recovery are
excluded, and the reason is given.

```
   It should be noted that only a signature algorithm with appendix (see
   Section 8.1 of [RFC9052]) can be used for countersignatures.  This is
   because the body should be able to be processed without having to
   evaluate the countersignature, and this is not possible for signature
   schemes with message recovery.
```

*Source `.cache/rfc-9338.txt` lines 329-333 · `sha256:a01cc1af219484cbe276e6a63c7f50767c0ef41d313d9bfd81ffcafeb2d85575`*


### §3.2 — Abbreviated Countersignatures

**Why the abbreviated form cannot carry a third-party witness.** The
verification parameters come from *"the same context used to describe the
encryption, signature, or MAC processing"*, and §1.3 defines *context* as
information outside the message. A witness is by definition not in it.

```
   Abbreviated countersignatures support encrypted group messaging where
   identification of the message originator is required but there is a
   desire to keep the countersignature as small as possible.  For
   abbreviated countersignatures, there is no provision for any
   protected attributes related to the signing operation.  That is, the
   parameters for computing or verifying the abbreviated
   countersignature are provided by the same context used to describe
   the encryption, signature, or MAC processing.
```

*Source `.cache/rfc-9338.txt` lines 337-344 · `sha256:d684fec4552e56475542c243181e57dd7b501c75e4e9cfdb622390bebc24de34`*


**The abbreviated structure, and its placement rule.**

```
   The CDDL fragment for the abbreviated countersignatures is:

         COSE_Countersignature0 = bstr

   The byte string representing the signature value is placed in the
   Countersignature0 attribute.  This attribute is then encoded as an
   unprotected header parameter.
```

*Source `.cache/rfc-9338.txt` lines 346-352 · `sha256:421ac120ec1e62ed0a388f1a9383b3bbeceb267434b8e583f6eb87ddad229f10`*


### §3.3 — Signing and Verification Process

**The process inputs and the second permitted-target list.** Seven structures
again, but **`COSE_Sign` is in and `COSE_recipient` is out** — the mirror
image of §2's list. Also the one ordering constraint in the document:
*"needs to have all of its cryptographic functions finalized before computing
the signature"*.

```
   In order to create a signature, a well-defined byte string is needed.
   The Countersign_structure is used to create the canonical form.  This
   signing and verification process takes in the countersignature target
   structure (COSE_Signature, COSE_Sign1, COSE_Sign, COSE_Mac,
   COSE_Mac0, COSE_Encrypt, or COSE_Encrypt0), the signer information
   (COSE_Signature), and the application data (external source).  A
   Countersign_structure is a CBOR array.  The target structure of the
   countersignature needs to have all of its cryptographic functions
   finalized before computing the signature.  The fields of the
   Countersign_structure, in order, are:
```

*Source `.cache/rfc-9338.txt` lines 356-365 · `sha256:f751fed4fa3528774f25b45fda6a786c2bc729995a6137c7395cd3eb9db4f089`*


**`context` — the four strings and their switch.** The switch is
`other_fields` present/absent, which is arithmetic on the *target*, not a
choice the signer makes. Five of eight target structures therefore keep
RFC 8152's strings.

```
   context:  A context text string identifying the context of the
      signature.  The context text string is one of the following:

      *  "CounterSignature" for countersignatures using the
         COSE_Countersignature structure when other_fields is absent.

      *  "CounterSignature0" for countersignatures using the
         COSE_Countersignature0 structure when other_fields is absent.

      *  "CounterSignatureV2" for countersignatures using the
         COSE_Countersignature structure when other_fields is present.

      *  "CounterSignature0V2" for countersignatures using the
         COSE_Countersignature0 structure when other_fields is present.
```

*Source `.cache/rfc-9338.txt` lines 367-380 · `sha256:66c41b5c21f35f7a29c20c26c94de716791e714931176263f947bedca311b55d`*


**`body_protected` and `sign_protected`.** `body_protected` is defined as
*"from the target structure"* while being *named* for the body; when the
target is itself a `COSE_Signature` inside a `COSE_Sign` those are different
things and the enclosing body's protected bucket is covered nowhere. The
omission rule names *"the Countersignature0V2 attribute"*, one of the two
abbreviated context strings. `design-notes.md` §4.

```
   body_protected:  The serialized protected attributes from the target
      structure, encoded in a bstr type.  If there are no protected
      attributes, a zero-length byte string is used.

   sign_protected:  The serialized protected attributes from the signer
      structure, encoded in a bstr type.  If there are no protected
      attributes, a zero-length byte string is used.  This field is
      omitted for the Countersignature0V2 attribute.
```

*Source `.cache/rfc-9338.txt` lines 382-389 · `sha256:0dbb2de72f433ef7aac66ece7f0e7283f99c07391b459d7930a806fcf45afce5`*


**`external_aad` and `payload`.** *"The payload is placed here independently
of how it is transported"* is the detached-payload instruction for this field;
it is also the strongest textual support for reading `payload` as *content*
rather than as *the target's second `bstr`*, which is the ambiguity
`design-notes.md` §3 turns on.

```
   external_aad:  The externally supplied additional authenticated data
      (AAD) from the application, encoded in a bstr type.  If this field
      is not supplied, it defaults to a zero-length byte string.  (See
      Section 4.4 of [RFC9052] for application guidance on constructing
      this field.)

   payload:  The payload to be signed, encoded in a bstr type.  The
      payload is placed here independently of how it is transported.
```

*Source `.cache/rfc-9338.txt` lines 391-398 · `sha256:63d9afab29511877f532de4c8ca8289afa2f88c1303a92208a10bf66205f9213`*


**`other_fields` — the whole of the repair, in four sentences.** *"Omitted if
there are only two bstr fields in the target structure"*, *"an array of all
bstr fields after the second"*, and the worked case that fixes the counting
origin: *"an array of one element for the COSE_Sign1 structure containing the
signature value"* is true only if `protected` is `bstr` field one and
`payload : bstr / nil` is `bstr` field two. `schema/bstr-slot-census.derived.txt`
is the derivation off RFC 9052's own CDDL.

```
   other_fields:  Omitted if there are only two bstr fields in the
      target structure.  This field is an array of all bstr fields after
      the second.  As an example, this would be an array of one element
      for the COSE_Sign1 structure containing the signature value.
```

*Source `.cache/rfc-9338.txt` lines 400-403 · `sha256:27e16fa8791918fa70dd95b8a1acc5253244956081dd8aaf92cebdb035ab97b6`*


**The `Countersign_structure` CDDL — printed here with erratum 7338 intact.**
The trailing `/` after `"CounterSignature0V2"` is a choice operator with no
right operand; RFC 8610 Appendix B has `type = type1 *(S "/" S type1)`, so the
fragment does not parse. **Not repaired here.** The repaired rule is in
`schema/countersign-structure.derived.cddl`, named as derived.

```
   The CDDL fragment that describes the above text is:

         Countersign_structure = [
           context : "CounterSignature" / "CounterSignature0" /
                     "CounterSignatureV2" / "CounterSignature0V2" /,
           body_protected : empty_or_serialized_map,
           ? sign_protected : empty_or_serialized_map,
           external_aad : bstr,
           payload : bstr,
           ? other_fields : [+ bstr ]
         ]
```

*Source `.cache/rfc-9338.txt` lines 405-415 · `sha256:4dd8c1be5ff1bac855d923e0473ff13bd03e4dec3f7645d0893790e4de48c23a`*


**The signing procedure — four steps.**

```
   How to compute a countersignature:

   1.  Create a Countersign_structure and populate it with the
       appropriate fields.

   2.  Create the value ToBeSigned by encoding the Countersign_structure
       to a byte string, using the encoding described in Section 4.

   3.  Call the signature creation algorithm passing in K (the key to
       sign with), alg (the algorithm to sign with), and ToBeSigned (the
       value to sign).

   4.  Place the resulting signature value in the correct location.
       This is the "signature" field of the COSE_Countersignature
       structure for full countersignatures (see Section 3.1).  This is
       the value of the Countersignature0 attribute for abbreviated
       countersignatures (see Section 3.2).
```

*Source `.cache/rfc-9338.txt` lines 417-433 · `sha256:d39d196c0e6902ed78e4a37e7c62b4add633872c1aa0b5065f4dde8d9d2ac200`*


**The verification procedure — three steps, plus the application's own
checks.** The last paragraph is the only error-adjacent obligation in the
document and it is lowercase: the application *"performs the appropriate
checks"*.

```
   The steps for verifying a countersignature:

   1.  Create a Countersign_structure and populate it with the
       appropriate fields.

   2.  Create the value ToBeSigned by encoding the Countersign_structure
       to a byte string, using the encoding described in Section 4.

   3.  Call the signature verification algorithm passing in K (the key
       to verify with), alg (the algorithm used to sign with),
       ToBeSigned (the value to sign), and sig (the signature to be
       verified).

   In addition to performing the signature verification, the application
   performs the appropriate checks to ensure that the key is correctly
   paired with the signing identity and that the signing identity is
   authorized before performing actions.
```

*Source `.cache/rfc-9338.txt` lines 435-451 · `sha256:038c4398c7105547b8e2583aa938bccee6c17c8c54d1a0a83b110e311ee991c4`*


---

## §4 — CBOR Encoding Restrictions

**BCP 14 keyword 1 of 2.** The determinism obligation is *inherited* — RFC
8949 §4.2 as narrowed by RFC 9052 §9 — and it is scoped to the *"to be
signed"* value, not to the transmitted message.

```
   The deterministic encoding rules are defined in Section 4.2 of
   [RFC8949].  These rules are further narrowed in Section 9 of
   [RFC9052].  The narrowed deterministic encoding rules MUST be used to
   ensure that all implementations generate the same byte string for the
   "to be signed" value.
```

*Source `.cache/rfc-9338.txt` lines 455-459 · `sha256:9da684ca94bbe4bff91b9087e5a5f26066be6b21ce09ae271f07b93bddf64852`*


---

## §5 — IANA Considerations

```
   The registries and registrations listed below were created during the
   processing of [RFC8152].  The majority of the actions are to update
   the references to point to this document.
```

*Source `.cache/rfc-9338.txt` lines 463-465 · `sha256:52ef99d30d95aa9c534bcedbf6898ffcbb1f33e6f780c35649bfb50eb5c32457`*


### §5.1 — CBOR Tags Registry

**The only new CBOR tag in this document, and its semantics.** *"COSE
standalone V2 countersignature"* — the tag exists for a countersignature
detached from what it countersigns, which is why `design-notes.md` §7 can
name the MD-3 cut precisely.

```
   IANA created a registry titled "CBOR Tags" registry as part of
   processing RFC 7049, which was subsequently replaced by [RFC8949].

   IANA has assigned a new tag for the CounterSignature type in the
   "CBOR Tags" registry.

   Tag:  19
   Data Item:  COSE_Countersignature
   Semantics:  COSE standalone V2 countersignature
   Reference:  RFC 9338
```

*Source `.cache/rfc-9338.txt` lines 469-478 · `sha256:93b8a94afbe653bb632a8fa2e691bb78c0f39a61d1acb60aa0ec9e5896734e43`*


### §5.2 — COSE Header Parameters Registry

```
   IANA created a registry titled "COSE Header Parameters" as part of
   processing [RFC8152].

   IANA has registered the Countersignature version 2 (label 11) and
   Countersignature0 version 2 (label 12) in the "COSE Header
   Parameters" registry.  For these entries, the "Value Type" and
   "Description" are shown in Table 1, the "Value Registry" is blank,
   and the "Reference" is "RFC 9338".
```

*Source `.cache/rfc-9338.txt` lines 482-489 · `sha256:2398b33ac509111e79e5015cd234ce749ef7d105c20efbd4af262b7d86d6e2d4`*


**Table 2 — identical in content to Table 1, printed twice.**

```
   +=================+=====+==========================+================+
   |Name             |Label| Value Type               |Description     |
   +=================+=====+==========================+================+
   |Countersignature |11   | COSE_Countersignature /  |V2              |
   |version 2        |     | [+ COSE_Countersignature |countersignature|
   |                 |     | ]                        |attribute       |
   +-----------------+-----+--------------------------+----------------+
   |Countersignature0|12   | COSE_Countersignature0   |V2 Abbreviated  |
   |version 2        |     |                          |Countersignature|
   +-----------------+-----+--------------------------+----------------+

                   Table 2: New Common Header Parameters
```

*Source `.cache/rfc-9338.txt` lines 491-502 · `sha256:d0603417c8418527bb8b701dd278f4839033f4614710ac843609c4ef968c39d7`*


**The deprecation, and it is the whole of it.** RFC 8152's countersignatures
are retired by a Description-field edit in a registry, not by a normative
statement in this document. There is no `MUST NOT` and no `SHOULD NOT`
anywhere against labels 7 and 9.

```
   IANA has modified the existing "Description" field for "counter
   signature" (7) and "CounterSignature0" (9) to include the words
   "(Deprecated by RFC 9338)".
```

*Source `.cache/rfc-9338.txt` lines 504-506 · `sha256:544937c52afb3b825e0b3aa0ca13e121f6b44bda2af0509bcbf876cb3a02a6fa`*


---

## §6 — Security Considerations

**BCP 14 keyword 2 of 2, and the ceilings it does not lift.** The `MUST` is on
*tag length*; the two numbered ceilings that follow are stated as facts, not
obligations, and they cap the countersignature's strength regardless of the
countersignature algorithm.

```
   Please review the Security Considerations section in [RFC9052]; these
   considerations apply to this document as well, especially the need
   for implementations to protect private key material.

   When either COSE_Encrypt or COSE_Mac is used and more than two
   parties share the key, data origin authentication is not provided.
   Any party that knows the message-authentication key can compute a
   valid authentication tag; therefore, the contents could originate
   from any one of the parties that share the key.

   Countersignatures of COSE_Encrypt and COSE_Mac with short
   authentication tags do not provide the security properties associated
   with the same algorithm used in COSE_Sign.  To provide 128-bit
   security against collision attacks, the tag length MUST be at least
   256 bits.  A countersignature of a COSE_Mac with AES-MAC (using a
   128-bit key or larger) provides at most 64 bits of integrity
   protection.  Similarly, a countersignature of a COSE_Encrypt with
   AES-CCM-16-64-128 provides at most 32 bits of integrity protection.
```

*Source `.cache/rfc-9338.txt` lines 510-527 · `sha256:a402e2802e250b0cbf2e39b61579409a0ad67b354b103b742a01151d50f204fe`*


---

## Appendix A — Examples

**What the examples are and what they are not.** Diagnostic notation, with a
named external tool required to turn them into bytes, and an XPath promise for
extracting them. No key material is printed anywhere in the document, so no
signature in Appendix A can be *verified* from this document alone;
`examples/README.md` records what was reproduced instead.

```
   This appendix includes a set of examples that show the different
   features and message types that have been defined in this document.
   To make the examples easier to read, they are presented using the
   extended CBOR diagnostic notation (defined in [RFC8610]) rather than
   as a binary dump.

   The examples are presented using the CBOR diagnostic notation.  A
   Ruby-based tool exists [CBORDIAG] that can convert between the
   diagnostic notation and binary.  The referenced webpage includes
   installation instructions.

   The diagnostic notation can be converted into binary files using the
   following command line:

   diag2cbor.rb < inputfile > outputfile

   The examples can be extracted from the XML version of this document
   via an XPath expression, as all of the sourcecode is tagged with the
   attribute 'type="cbor-diag"'.  (Depending on the XPath evaluator one
   is using, it may be necessary to deal with &gt; as an entity.)

   //sourcecode[@type='cbor-diag']/text()
```

*Source `.cache/rfc-9338.txt` lines 596-617 · `sha256:c67b98dd18386fa6e42bc26610703e8228ac8757fe363d9257a8152cef8a83c8`*


**The six examples themselves are reproduced as fixtures, not quoted here** —
`examples/fixtures/` holds each as an exact run of source lines with its own
digest, and `examples/vectors.yaml` carries the stated size, the encoded size
and the byte-level result for each. **One of the six does not match its stated
size**; see `examples/README.md`.

---

## What is normative here and is not in `requirements.yaml`

One statement, deliberately: the **§1.1 BCP 14 recital** (lines 143-147). It
recites all eleven keywords and constrains nothing, and `bin/validate` counts
requirement texts with `boilerplate=False`, so an entry for it would add
eleven phantom keywords and break the reconciliation. It is quoted above
instead.

Everything else in §1-§6 and Appendix A's lead-in that carries force,
definition, structure, registry content or a stated measurement has an entry.
The reverse direction — entries whose statement is *not* in this file — is
empty by construction: every `text` in `requirements.yaml` is a span of a
region reproduced above.
