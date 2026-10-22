---
record: rfc-8747
kind: normative
title: "rfc-8747 — normative statements"
extracted: "2026-10-21"
reviewed_by: ""
---

# RFC 8747 — normative text, verbatim

**What this file is.** Every normative statement of RFC 8747, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order, together with its one table and all four of its
IANA registration blocks. Nothing here is paraphrased and nothing is retyped:
each fenced block was lifted from `.cache/rfc-8747.txt` by line range by
script. Prose outside the fences is this extraction's, and says only where a
statement sits and what it is.

| | |
|---|---|
| **Source** | `.cache/rfc-8747.txt`, 683 newline-delimited lines |
| **Digest** | `9b695379f119f9675828d054f1b0e76014c06c9a59dccef8bb417e0420272dda` |
| **Maturity** | **Standards Track**, read off the front page at line 7 — quoted below, not assumed |
| **BCP 14 keywords** | **8** — 4 MUST, 2 MAY, 1 SHOULD, 1 MUST NOT; `bin/bcp14-count`, boilerplate excluded |

**Region convention.** Each digest is the sha256 of the region's lines joined
by a newline with no trailing newline — the convention established by earlier
passes in this effort.

**There is no page decoration in this document.** The source has **ZERO form
feeds**, so no region can contain a page break, a running header or a running
footer, and none is excluded anywhere below. That is unusual for an RFC `.txt`
and worth stating plainly: the sibling records in this lane carry 25 or more.
No region below is split for pagination, and every fence is one contiguous run
of source lines. Built with `split` on a newline, never `splitlines` — which
splits on form feeds and would be harmless here but is wrong on principle.

**One byte of the source is not printable.** Line 1 is a **UTF-8 byte-order
mark** and nothing else. It is inside the hashed bytes, so it is part of the
digest above, and it is why line 2 rather than line 1 begins the blank run
before the masthead. No region below starts at line 1.

**Where a line break falls inside a sentence**, the sentence is quoted as the
whole fenced region rather than reflowed, so the break stays visible. Eight
line ends in this document fall **at a hyphen** — lines 25, 90, 177, 180, 598,
615, 616 and 619 — and three of those are inside normative sentences quoted
here: line 90 (`proof-` / `of-possession`), line 177 (`proof-of-` /
`possession`) and line 180 (`proof-of-` / `possession`). **Nothing is healed.**
`requirements.yaml` carries the same sentences whitespace-normalised, so they
read `proof- of-possession` and `proof-of- possession` there, with the space
the break leaves. Joining at a hyphen would make the quoted token occur nowhere
in the source; joining at a space is ordinary normalisation and is not a heal.

**What is dropped, and stated as dropped:** the Status of This Memo (lines
32-44), the Copyright Notice (46-59), the Table of Contents (61-85), both
reference lists (556-633), the Acknowledgements (635-644) and the Authors'
Addresses (646-683). The masthead and the Abstract are kept, the first because
`maturity: standard` is a claim about the front page and the second because it
is the document's own one-paragraph statement of scope.

---

## Front matter — the maturity claim, quoted

`record.yaml` says `maturity: standard`. This is the page it is read from. An
RFC being an RFC does not make it Standards Track, and two maturity values
were wrong in this effort before anyone quoted the masthead.

```
Internet Engineering Task Force (IETF)                          M. Jones
Request for Comments: 8747                                     Microsoft
Category: Standards Track                                       L. Seitz
ISSN: 2070-1721                                                Combitech
                                                             G. Selander
                                                             Ericsson AB
                                                              S. Erdtman
                                                                 Spotify
                                                           H. Tschofenig
                                                                Arm Ltd.
                                                              March 2020
```

*Source `.cache/rfc-8747.txt` lines 5-15 · `sha256:a6414785963d4d8595f2f5e241d2b856bf7ada968ca209d719f162ba721d74c0`*

## Abstract

```
   This specification describes how to declare in a CBOR Web Token (CWT)
   (which is defined by RFC 8392) that the presenter of the CWT
   possesses a particular proof-of-possession key.  Being able to prove
   possession of a key is also sometimes described as being the holder-
   of-key.  This specification provides equivalent functionality to
   "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)" (RFC
   7800) but using Concise Binary Object Representation (CBOR) and CWTs
   rather than JavaScript Object Notation (JSON) and JSON Web Tokens
   (JWTs).
```

*Source `.cache/rfc-8747.txt` lines 22-30 · `sha256:5dfcac326d8852c3dd5dab2a0426a964cf6a74359d5609dbbcccc61380f55bcf`*

## §1 — Introduction

Kept as the document's own scope statement. Note the line break at 90-91: it
cuts `proof-` from `of-possession` **at the hyphen**.

```
   This specification describes how a CBOR Web Token (CWT) [RFC8392] can
   declare that the presenter of the CWT possesses a particular proof-
   of-possession (PoP) key.  Proof of possession of a key is also
   sometimes described as being the holder-of-key.  This specification
   provides equivalent functionality to "Proof-of-Possession Key
   Semantics for JSON Web Tokens (JWTs)" [RFC7800] but using Concise
   Binary Object Representation (CBOR) [RFC7049] and CWTs [RFC8392]
   rather than JavaScript Object Notation (JSON) [RFC8259] and JSON Web
   Tokens (JWTs) [JWT].
```

*Source `.cache/rfc-8747.txt` lines 89-97 · `sha256:645291ffc9ea3a9dbced20c1a133bf30864297241b9876898e4319f2d9ce39d7`*

## §2 — Terminology

### The BCP 14 recital

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing. `bin/validate` recounts the
requirement texts with boilerplate stripping **off**, so an entry carrying this
paragraph would add 11 phantom keywords and make the extraction read 19 against
a source of 8.

```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-8747.txt` lines 101-105 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*

### Inherited terminology

The editions this document normatively cites are **RFC 8152** and **RFC 7049**.
It has no normative reference to any later COSE or CBOR document; `8949`,
`9052` and `9053` occur **zero** times in the source.

```
   This specification uses terms defined in the CBOR Web Token (CWT)
   [RFC8392], CBOR Object Signing and Encryption (COSE) [RFC8152], and
   Concise Binary Object Representation (CBOR) [RFC7049] specifications.
```

*Source `.cache/rfc-8747.txt` lines 107-109 · `sha256:68c51921c301d52cb082bab156d49ca74674049116757dffa855218f8fd0c372`*

### The three roles — the document's whole party model

These three definitions are what `protocol.yaml` models. They are the only
roles the document defines, and it defines no message between them.

```
   These terms are defined by this specification:

   Issuer
      Party that creates the CWT and binds the claims about the subject
      to the proof-of-possession key.

   Presenter
      Party that proves possession of a private key (for asymmetric key
      cryptography) or secret key (for symmetric key cryptography) to a
      recipient of a CWT.

      In the context of OAuth, this party is also called the OAuth
      Client.

   Recipient
      Party that receives the CWT containing the proof-of-possession key
      information from the presenter.

      In the context of OAuth, this party is also called the OAuth
      Resource Server.
```

*Source `.cache/rfc-8747.txt` lines 111-130 · `sha256:be669185d1808fcbbe27586f138d2f48418104ab10094936bb038a82a308293e`*

### How the examples are written

A presentation rule a fixture builder must obey, and the document's **only**
citation of RFC 8610 — for Appendix G, the diagnostic notation. Not for CDDL:
the string `CDDL` occurs once in the whole source, inside the RFC 8610
reference entry at line 630.

```
   This specification provides examples in CBOR extended diagnostic
   notation, as defined in Appendix G of [RFC8610].  The examples
   include line breaks for readability.
```

*Source `.cache/rfc-8747.txt` lines 132-134 · `sha256:acb579ae959c68ac66ef248d92cbd179687b2efb3e3c288b8a759db61a040fd5`*

## §3 — Representations for Proof-of-Possession Keys

```
   By including a "cnf" (confirmation) claim in a CWT, the issuer of the
   CWT declares that the presenter possesses a particular key and that
   the recipient can cryptographically confirm that the presenter has
   possession of that key.  The value of the "cnf" claim is a CBOR map
   (which is defined in Section 2.1 of [RFC7049]) and the members of
   that map identify the proof-of-possession key.

   The presenter can be identified in one of several ways by the CWT,
   depending upon the application requirements.  For instance, some
   applications may use the CWT "sub" (subject) claim [RFC8392] to
   identify the presenter.  Other applications may use the "iss"
   (issuer) claim [RFC8392] to identify the presenter.  In some
   applications, the subject identifier might be relative to the issuer
   identified by the "iss" claim.  The actual mechanism used is
   dependent upon the application.  The case in which the presenter is
   the subject of the CWT is analogous to Security Assertion Markup
   Language (SAML) 2.0 [OASIS.saml-core-2.0-os] SubjectConfirmation
   usage.
```

*Source `.cache/rfc-8747.txt` lines 138-155 · `sha256:40f7ed108b47d04aaaa9c3c06f87b137fa490d700dc4b4e91b210dee6d3054ff`*

## §3.1 — Confirmation Claim

Carries two of the document's eight BCP 14 keywords, at lines 172 and 180, and
— one sentence after the second of them — the at-most-one rule in **lower
case**.

```
   The "cnf" claim in the CWT is used to carry confirmation methods.
   Some of them use proof-of-possession keys, while others do not.  This
   design is analogous to the SAML 2.0 [OASIS.saml-core-2.0-os]
   SubjectConfirmation element in which a number of different subject
   confirmation methods can be included (including proof-of-possession
   key information).

   The set of confirmation members that a CWT must contain to be
   considered valid is context dependent and is outside the scope of
   this specification.  Specific applications of CWTs will require
   implementations to understand and process some confirmation members
   in particular ways.  However, in the absence of such requirements,
   all confirmation members that are not understood by implementations
   MUST be ignored.

   Section 7.2 establishes the IANA "CWT Confirmation Methods" registry
   for CWT "cnf" member values and registers the members defined by this
   specification.  Other specifications can register other members used
   for confirmation, including other members for conveying proof-of-
   possession keys using different key representations.

   The "cnf" claim value MUST represent only a single proof-of-
   possession key.  At most one of the "COSE_Key" and
   "Encrypted_COSE_Key" confirmation values defined in Table 1 may be
   present.  Note that if an application needs to represent multiple
   proof-of-possession keys in the same CWT, one way for it to achieve
   this is to use other claim names (in addition to "cnf") to hold the
   additional proof-of-possession key information.  These claims could
   use the same syntax and semantics as the "cnf" claim.  Those claims
   would be defined by applications or other specifications and could be
   registered in the IANA "CBOR Web Token (CWT) Claims" registry
   [IANA.CWT.Claims].
```

*Source `.cache/rfc-8747.txt` lines 159-190 · `sha256:4c19b4f27a5a4f80e63979b2558c496a44750d99733e076dc48577352fa61cc7`*

### Table 1 — the complete set of ways a CWT may identify a PoP key

The table is reproduced with its own rule characters, including the `+====+`
header separator. Its three data rows are the whole of what this document
allows, and `requirements.yaml` carries each row as its own entry.

```
       +--------------------+-----+-------------------------------+
       | Name               | Key | Value type                    |
       +====================+=====+===============================+
       | COSE_Key           | 1   | COSE_Key                      |
       +--------------------+-----+-------------------------------+
       | Encrypted_COSE_Key | 2   | COSE_Encrypt or COSE_Encrypt0 |
       +--------------------+-----+-------------------------------+
       | kid                | 3   | binary string                 |
       +--------------------+-----+-------------------------------+

        Table 1: Summary of the "cnf" Names, Keys, and Value Types
```

*Source `.cache/rfc-8747.txt` lines 192-202 · `sha256:37f268cebdd1917a6932f41d41f34fd47035b89cd4196fa626b90254c8776093`*

## §3.2 — Representation of an Asymmetric Proof-of-Possession Key

```
   When the key held by the presenter is an asymmetric private key, the
   "COSE_Key" member is a COSE_Key [RFC8152] representing the
   corresponding asymmetric public key.  The following example
   demonstrates such a declaration in the CWT Claims Set of a CWT:
```

*Source `.cache/rfc-8747.txt` lines 206-209 · `sha256:ad56a7f3416960daac6313177dd0e8ceb7b7ad28b87c7198d1e6432fb7fdc98e`*

The example itself is in `examples/README.md`, fenced and digested, with its
decoded values in `examples/vectors.yaml`.

Four of the eight BCP 14 keywords are in the next region alone — lines 227,
228, 231 and 235. Note that line 227 also carries a **lower-case** `required`,
which `bin/bcp14-count` correctly does not count.

```
   The COSE_Key MUST contain the required key members for a COSE_Key of
   that key type and MAY contain other COSE_Key members, including the
   "kid" (Key ID) member.

   The "COSE_Key" member MAY also be used for a COSE_Key representing a
   symmetric key, provided that the CWT is encrypted so that the key is
   not revealed to unintended parties.  The means of encrypting a CWT is
   explained in [RFC8392].  If the CWT is not encrypted, the symmetric
   key MUST be encrypted as described in Section 3.3.  This procedure is
   equivalent to the one defined in Section 3.3 of [RFC7800].
```

*Source `.cache/rfc-8747.txt` lines 227-236 · `sha256:6e2788adbe001b83c304606644836373dd49e28e65012a451dcba4ab1703ed52`*

## §3.3 — Representation of an Encrypted Symmetric Proof-of-Possession Key

```
   When the key held by the presenter is a symmetric key, the
   "Encrypted_COSE_Key" member is an encrypted COSE_Key [RFC8152]
   representing the symmetric key encrypted to a key known to the
   recipient using COSE_Encrypt or COSE_Encrypt0.

   The following example illustrates a symmetric key that could
   subsequently be encrypted for use in the "Encrypted_COSE_Key" member:
```

*Source `.cache/rfc-8747.txt` lines 240-246 · `sha256:7e61da9b7ddfa0467ec3843dfabf9f47398d940a3768f20cfe2e0a716100dc2e`*

**The sentence this extraction found a defect against.** Measured: the §3.3
COSE_Key printed at lines 248-253 is **not**, byte for byte, the plaintext of
the §3.3 ciphertext printed at lines 271-272. They are the same three
key-value pairs in a different map entry order — `3, 1, -1` encrypted against
`1, 3, -1` printed. The ciphertext authenticates and reproduces exactly from
the order it actually carries. See `examples/vectors.yaml` →
`source_defects` → `rfc-8747#D-0001`.

```
   The COSE_Key representation is used as the plaintext when encrypting
   the key.
```

*Source `.cache/rfc-8747.txt` lines 255-256 · `sha256:797964914e5c86d12d44e8994f4cc4eea70121f3e91d2e1f9cfb7138b4238c93`*

```
   The following example CWT Claims Set of a CWT illustrates the use of
   an encrypted symmetric key as the "Encrypted_COSE_Key" member value:
```

*Source `.cache/rfc-8747.txt` lines 258-259 · `sha256:1397826b3ae9eba0cee07c5ed1cf9f3c8ba0dc89834a544df0459483821e7290`*

```
   The example above was generated with the key:

   h'6162630405060708090a0b0c0d0e0f10'
```

*Source `.cache/rfc-8747.txt` lines 277-279 · `sha256:e013429ac4a68103f8bcb33a2ab1560165471ac773b54b9c3c4470ee73fd5ac1`*

## §3.4 — Representation of a Key ID for a Proof-of-Possession Key

**The section this record is held for.** No BCP 14 keyword appears anywhere in
it; its four load-bearing sentences carry `may`, `should`, `should` and `may`
in lower case, at lines 305, 312, 315 and 323.

```
   The proof-of-possession key can also be identified using a Key ID
   instead of communicating the actual key, provided the recipient is
   able to obtain the identified key using the Key ID.  In this case,
   the issuer of a CWT declares that the presenter possesses a
   particular key and that the recipient can cryptographically confirm
   the presenter's proof of possession of the key by including a "cnf"
   claim in the CWT whose value is a CBOR map containing a "kid" member
   identifying the key.

   The following example demonstrates such a declaration in the CWT
   Claims Set of a CWT:
```

*Source `.cache/rfc-8747.txt` lines 283-293 · `sha256:e6cf2f57e81d6be88e850d986c5b4dd9d15ba7861e760fc81df3c6d6a2beb1c4`*

```
   The content of the "kid" value is application specific.  For
   instance, some applications may choose to use a cryptographic hash of
   the public key value as the "kid" value.

   Note that the use of a Key ID to identify a proof-of-possession key
   needs to be carefully circumscribed, as described below and in
   Section 6.  In cases where the Key ID is not a cryptographic value
   derived from the key or where not all of the parties involved are
   validating the cryptographic derivation, implementers should expect
   collisions where different keys are assigned the same Key ID.
   Recipients of a CWT with a PoP key linked through only a Key ID
   should be prepared to handle such situations.

   In the world of constrained Internet of Things (IoT) devices, there
   is frequently a restriction on the size of Key IDs, either because of
   table constraints or a desire to keep message sizes small.

   Note that the value of a Key ID for a specific key is not necessarily
   the same for different parties.  When sending a COSE encrypted
   message with a shared key, the Key ID may be different on both sides
   of the conversation, with the appropriate one being included in the
   message based on the recipient of the message.
```

*Source `.cache/rfc-8747.txt` lines 304-325 · `sha256:cb7eac2f358a7f496864a85c847318f7991a827b4ad72b92738752108a72cdab`*

## §3.5 — Specifics Intentionally Not Specified

Two explicit refusals, at lines 337-339 and 340-341. They are why `protocol.yaml`
models a role triangle and not a message flow.

```
   Proof of possession is often demonstrated by having the presenter
   sign a value determined by the recipient using the key possessed by
   the presenter.  This value is sometimes called a "nonce" or a
   "challenge".  There are, however, also other means to demonstrate
   freshness of the exchange and to link the proof-of-possession key to
   the participating parties, as demonstrated by various authentication
   and key exchange protocols.

   The means of communicating the nonce and the nature of its contents
   are intentionally not described in this specification, as different
   protocols will communicate this information in different ways.
   Likewise, the means of communicating the signed nonce is also not
   specified, as this is also protocol specific.

   Note that other means of proving possession of the key exist, which
   could be used in conjunction with a CWT's confirmation key.
   Applications making use of such alternate means are encouraged to
   register them in the IANA "CBOR Web Token (CWT) Confirmation Methods"
   registry established in Section 7.2.
```

*Source `.cache/rfc-8747.txt` lines 329-347 · `sha256:d6ffedf457da74756edc5545d12ef4e07e9e26182724b1ea969e0083d5658884`*

## §4 — Security Considerations

Carries the document's remaining two BCP 14 keywords: the only SHOULD at line
357 and the only MUST NOT at line 391. Also carries, at line 354, the
**lower-case** `must` that is its central secrecy obligation.

```
   All the security considerations that are discussed in [RFC8392] also
   apply here.  In addition, proof of possession introduces its own
   unique security issues.  Possessing a key is only valuable if it is
   kept secret.  Appropriate means must be used to ensure that
   unintended parties do not learn private key or symmetric key values.

   Applications utilizing proof of possession SHOULD also utilize
   audience restriction, as described in Section 3.1.3 of [RFC8392],
   because it provides additional protections.  Audience restriction can
   be used by recipients to reject messages intended for different
   recipients.  (Of course, applications not using proof of possession
   can also benefit from using audience restriction to reject messages
   intended for different recipients.)

   CBOR Web Tokens with proof-of-possession keys are used in context of
   an architecture, such as the ACE OAuth Framework [ACE-OAUTH], in
   which protocols are used by a presenter to request these tokens and
   to subsequently use them with recipients.  Proof of possession only
   provides the intended security gains when the proof is known to be
   current and not subject to replay attacks; security protocols using
   mechanisms such as nonces and timestamps can be used to avoid the
   risk of replay when performing proof of possession for a token.  Note
   that a discussion of the architecture or specific protocols that CWTs
   with proof-of-possession keys are used with is beyond the scope of
   this specification.

   As is the case with other information included in a CWT, it is
   necessary to apply data origin authentication and integrity
   protection (via a keyed message digest or a digital signature).  Data
   origin authentication ensures that the recipient of the CWT learns
   about the entity that created the CWT, since this will be important
   for any policy decisions.  Integrity protection prevents an adversary
   from changing any elements conveyed within the CWT payload.  Special
   care has to be applied when carrying symmetric keys inside the CWT
   since those not only require integrity protection but also
   confidentiality protection.

   As described in Section 6 (Key Identification) and Appendix D (Notes
   on Key Selection) of [JWS], it is important to make explicit trust
   decisions about the keys.  Proof-of-possession signatures made with
   keys not meeting the application's trust criteria MUST NOT be relied
   upon.
```

*Source `.cache/rfc-8747.txt` lines 351-392 · `sha256:045eecb3a70fdffcda18b4f36675c18d12ed0692de8c49f9e597308969b9633b`*

## §5 — Privacy Considerations

Four lines, one lower-case `recommended`, and a direct tension with §6's
intentional-reuse case below.

```
   A proof-of-possession key can be used as a correlation handle if the
   same key is used on multiple occasions.  Thus, for privacy reasons,
   it is recommended that different proof-of-possession keys be used
   when interacting with different parties.
```

*Source `.cache/rfc-8747.txt` lines 396-399 · `sha256:bc21fed90cf80ce52270c5a53a105d2628778f9d9da2da4b4bbb1894486ebb23`*

## §6 — Operational Considerations

**The other section this record is held for.** Key ID uniqueness is stated here
as something an issuer `needs to make sure` of — an operational discipline,
not a property of the identifier — with impersonation as the named failure.
The qualifier `unless intentionally desired` is part of that sentence.

```
   The use of CWTs with proof-of-possession keys requires additional
   information to be shared between the involved parties in order to
   ensure correct processing.  The recipient needs to be able to use
   credentials to verify the authenticity and integrity of the CWT.
   Furthermore, the recipient may need to be able to decrypt either the
   whole CWT or the encrypted parts thereof (see Section 3.3).  This
   requires the recipient to know information about the issuer.
   Likewise, there needs to be agreement between the issuer and the
   recipient about the claims being used (which is also true of CWTs in
   general).

   When an issuer creates a CWT containing a Key ID claim, it needs to
   make sure that it does not issue another CWT with different claims
   containing the same Key ID within the lifetime of the CWTs, unless
   intentionally desired.  Failure to do so may allow one party to
   impersonate another party, with the potential to gain additional
   privileges.  A case where such reuse of a Key ID would be intentional
   is when a presenter obtains a CWT with different claims (e.g.,
   extended scope) for the same recipient but wants to continue using an
   existing security association (e.g., a DTLS session) bound to the key
   identified by the Key ID.  Likewise, if PoP keys are used for
   multiple different kinds of CWTs in an application and the PoP keys
   are identified by Key IDs, care must be taken to keep the keys for
   the different kinds of CWTs segregated so that an attacker cannot
   cause the wrong PoP key to be used by using a valid Key ID for the
   wrong kind of CWT.  Using an audience restriction for the CWT would
   be one strategy to mitigate this risk.
```

*Source `.cache/rfc-8747.txt` lines 403-429 · `sha256:27b3b3d5c1f5e3a79a495acc13969285bf7a4fa8133bb574aacf7e090fb54bce`*

## §7 — IANA Considerations

The common registration procedure. Eight sentences, seven lower-case force
words, no BCP 14 keyword.

```
   The following registration procedure is used for all the registries
   established by this specification.

   Values are registered on a Specification Required [RFC8126] basis
   after a three-week review period on the <cwt-reg-review@ietf.org>
   mailing list, on the advice of one or more designated experts.
   However, to allow for the allocation of values prior to publication,
   the designated experts may approve registration once they are
   satisfied that such a specification will be published.

   Registration requests sent to the mailing list for review should use
   an appropriate subject (e.g., "Request to Register CWT Confirmation
   Method: example").  Registration requests that are undetermined for a
   period longer than 21 days can be brought directly to IANA's
   attention (using the iana@iana.org mailing list) for resolution.

   Designated experts should determine whether a registration request
   contains enough information for the registry to be populated with the
   new values and whether the proposed new functionality already exists.
   In the case of an incomplete registration or an attempt to register
   already existing functionality, the designated experts should ask for
   corrections or reject the registration.

   It is suggested that multiple designated experts be appointed who are
   able to represent the perspectives of different applications using
   this specification in order to enable broadly informed review of
   registration decisions.  In cases where a registration decision could
   be perceived as creating a conflict of interest for a particular
   expert, that expert should defer to the judgment of the other
   experts.
```

*Source `.cache/rfc-8747.txt` lines 433-462 · `sha256:1036d9b3851fd8fdfb6e2b3af0e739aea0eba8b835e8c1cb6c13d0d4d3e97e88`*

## §7.1 — CBOR Web Token Claims Registration

```
   This specification registers the "cnf" claim in the IANA "CBOR Web
   Token (CWT) Claims" registry [IANA.CWT.Claims], established by
   [RFC8392].
```

*Source `.cache/rfc-8747.txt` lines 466-468 · `sha256:db7c90ddb6c73414804b2cfe50a60af6b9fa1650836eb37883e51a3f717c0e71`*

### §7.1.1 — Registry Contents: the complete `cnf` registration

Reproduced whole. `Claim Key: 8` and `Claim Value Type(s): map` are the two
facts a decoder needs, and neither is stated anywhere else in the document.

```
7.1.1.  Registry Contents

   *  Claim Name: "cnf"

   *  Claim Description: Confirmation

   *  JWT Claim Name: "cnf"

   *  Claim Key: 8

   *  Claim Value Type(s): map

   *  Change Controller: IESG

   *  Specification Document(s): Section 3.1 of RFC 8747
```

*Source `.cache/rfc-8747.txt` lines 470-484 · `sha256:96b795a573d4c3ef254d955baa9e6b69063e26248a5ea91a0e2b420207abf53f`*

## §7.2 — CWT Confirmation Methods Registry

The authoritative spelling of the registry name is here and at §3.1. **§3.5
spells it differently** — `CBOR Web Token (CWT) Confirmation Methods` — which
is a source defect recorded in `README.md`.

```
7.2.  CWT Confirmation Methods Registry

   This specification establishes the IANA "CWT Confirmation Methods"
   registry for CWT "cnf" member values.  The registry records the
   confirmation method member and a reference to the specification that
   defines it.
```

*Source `.cache/rfc-8747.txt` lines 486-491 · `sha256:d13e0deddbcb6dbd95f95eaf87585b9bf08995a256757a79d733cd37ab43afdb`*

### §7.2.1 — Registration Template

Seven fields. This is where the rules for future registrants actually live:
the `JWT Confirmation Method Name` field carries the `N/A` escape, and
`Confirmation Key` is defined as a bare CBOR map key value with **no stated
range and no allocation tiers** — unlike RFC 8392 §9.1.1, which tiers its
Claim Key space.

```
7.2.1.  Registration Template

   Confirmation Method Name:
      The human-readable name requested (e.g., "kid").

   Confirmation Method Description:
      Brief description of the confirmation method (e.g., "Key
      Identifier").

   JWT Confirmation Method Name:
      Claim Name of the equivalent JWT confirmation method value, as
      registered in the "JSON Web Token Claims" subregistry in the "JSON
      Web Token (JWT)" registry [IANA.JWT].  CWT claims should normally
      have a corresponding JWT claim.  If a corresponding JWT claim
      would not make sense, the designated experts can choose to accept
      registrations for which the JWT Claim Name is listed as "N/A".

   Confirmation Key:
      CBOR map key value for the confirmation method.

   Confirmation Value Type(s):
      CBOR types that can be used for the confirmation method value.

   Change Controller:
      For Standards Track RFCs, list the "IESG".  For others, give the
      name of the responsible party.

   Specification Document(s):
      Reference to the document or documents that specify the parameter,
      preferably including URIs that can be used to retrieve copies of
      the documents.  An indication of the relevant sections may also be
      included but is not required.  Note that the designated experts
      and IANA must be able to obtain copies of the specification
      document(s) to perform their work.
```

*Source `.cache/rfc-8747.txt` lines 493-526 · `sha256:eb14cfff0afe3ab543ed29d66c87ea52d0257c7efc075ccbb978c7031034edb1`*

### §7.2.2 — Initial Registry Contents: the three confirmation methods

All three registrations, reproduced whole. The `Encrypted_COSE_Key` entry is
the **only** place in the document where the word `tag` appears — line 544 —
and it appears as a **lower-case** `optional`, not as a BCP 14 OPTIONAL. Note
also that these value types do not match Table 1's: the table says `COSE_Key`
and `COSE_Encrypt or COSE_Encrypt0` where the registry says `COSE_Key
structure` and `COSE_Encrypt or COSE_Encrypt0 structure (with an optional
corresponding COSE_Encrypt or COSE_Encrypt0 tag)`.

```
7.2.2.  Initial Registry Contents

   *  Confirmation Method Name: "COSE_Key"
   *  Confirmation Method Description: COSE_Key Representing Public Key
   *  JWT Confirmation Method Name: "jwk"
   *  Confirmation Key: 1
   *  Confirmation Value Type(s): COSE_Key structure
   *  Change Controller: IESG
   *  Specification Document(s): Section 3.2 of RFC 8747

   *  Confirmation Method Name: "Encrypted_COSE_Key"
   *  Confirmation Method Description: Encrypted COSE_Key
   *  JWT Confirmation Method Name: "jwe"
   *  Confirmation Key: 2
   *  Confirmation Value Type(s): COSE_Encrypt or COSE_Encrypt0
      structure (with an optional corresponding COSE_Encrypt or
      COSE_Encrypt0 tag)
   *  Change Controller: IESG
   *  Specification Document(s): Section 3.3 of RFC 8747

   *  Confirmation Method Name: "kid"
   *  Confirmation Method Description: Key Identifier
   *  JWT Confirmation Method Name: "kid"
   *  Confirmation Key: 3
   *  Confirmation Value Type(s): binary string
   *  Change Controller: IESG
   *  Specification Document(s): Section 3.4 of RFC 8747
```

*Source `.cache/rfc-8747.txt` lines 528-554 · `sha256:24882d90399ae3807164072d8143b2f157f90ac7fcba603f1e81f4948048d487`*

---

## Verbatim coverage, counted

| | |
|---|---|
| fenced regions | **28** |
| source lines inside a fence | **389** of 683 |
| regions byte- and digest-exact against their declared range | checked at write time |
| form feeds inside any region | **0** — the source has none |

The lines not inside a fence are the front-matter boilerplate, the table of
contents, the five printed examples (which live in `examples/README.md`, fenced
and digested there), both reference lists, the Acknowledgements and the
Authors' Addresses — plus the blank lines between quoted regions.

