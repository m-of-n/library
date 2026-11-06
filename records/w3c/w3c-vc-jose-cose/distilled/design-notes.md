---
record: w3c-vc-jose-cose
kind: design-notes
title: "w3c-vc-jose-cose — bearing on our design"
extracted: "2026-11-03"
reviewed_by: ""
---

# VC-JOSE-COSE — bearing on our design

*Securing Verifiable Credentials using JOSE and COSE* is the W3C Recommendation
of 15 May 2025 (REC-vc-jose-cose-20250515; HTML, sha256
`6c70cf8d7de9d8a3ff28a743fea9d569a67a402111c3245fdafbaa2ad6709af9`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass).
It secures a VC Data Model 2.0 credential or presentation by wrapping it: the
document's own JSON is the payload of a JWS, an SD-JWT or a COSE_Sign1, and six
media types label the result. It defines no exchange, no trust model and no
canonicalisation. The word *canonical* occurs 0 times in the 1980 lines of
`.cache/w3c-vc-jose-cose.txt`, and *trust* once, inside *"untrusted data"* (§5
¶2).

It reaches us in five ways.

1. **R-I-06** (Could): export a subset of `AuthzCert` as a W3C Verifiable
   Credential. This is the securing mechanism such an export would cite for the
   enveloping route. §5.1 drafts the R-I-01 table it needs.
2. **DEC-003, accepted by ADR-0005.** The source requires a `kid` in three
   cases: present for a DID URL key (R-0065), and, where controlled identifier
   documents are used (§4.2 ¶1), an absolute URL when `iss` is absent and the
   issuer or holder is a URL (R-0072, R-0074). It recommends a form for it
   (R-0073). Neither the URL
   nor the recommended form is ADR-0005's `kid`.
3. **DEC-002, accepted by ADR-0004, and MD-3.** It is a signing-envelope
   document, so `docs/extraction.md` requires a header-by-header mapping and a
   record of where it cuts against option 5. That is §6.
4. **mofn#110**, which owns the rows of the ARCH-0001 §6 interchange matrix. Its
   W3C VC row and its COSE_Sign1 + CWT row are the two this record informs. §7
   is written for it.
5. **mofn report R-0006** (`research/0006-mechanism/report.md`). Its §2.2 W3C VC
   row reads *"**∅** for VC — no VC Data Model, Data Integrity or VC-JOSE-COSE
   record exists."* This record fills the enveloping route's cells: what is
   hashed, canonicalised, signed and carried, and how a verifier proceeds.

What it is not: a delegation model, a trust model or a status mechanism. *revoc*
occurs only in Example 18 (§8.2), which is non-normative.

**Things to hold while reading.**

1. **It binds, partly, and its non-normative parts carry weight.** *"As well as
   sections marked as non-normative, all authoring guidelines, diagrams,
   examples, and notes in this specification are non-normative. Everything else
   in this specification is normative."* (§1.1 ¶1, N-002). `bin/bcp14-count`
   finds 97 BCP 14 keywords. `requirements.yaml` extracts 85 requirements,
   R-0001 to R-0085, carrying 87 of them. The other 10 are 3 quoted mentions in
   §1.1.1, 6 keywords in §3.1.3 and 1 in Appendix A (its reconciliation). The
   HTML gives §3.1.3, §6, §7, §8 and Appendices A and B the class `informative`
   (checked over 53 section elements). So the six media type registrations sit in
   a non-normative section (SD-16), and the JOSE header rules are advice where
   their COSE twins bind (SD-15, TEN-05). The verification algorithms of §5.1 to
   §5.3 are normative and contain no keyword. Where something below is adopted,
   **we** make it normative in a SPEC or an ADR.

2. **It is a profile, and the library holds its foundations unevenly.** On the
   JOSE side `rfc-7515` and `rfc-7516` are stubs (a `.txt` of each is cached),
   and RFC 7517, RFC 7519, RFC 7638, RFC 8037, SD-JWT and Controlled Identifiers
   1.0 have no record. `w3c-did-core` is a stub and `w3c-vc-data-model-2-0` is
   summarised only. On the COSE side `rfc-9052`, `rfc-9053`, `rfc-9596`,
   `rfc-9597`, `rfc-8392` and `rfc-8747` are at `profile: full`. A row resting on
   the JOSE side is marked **[JOSE, outside this source]** and one resting on the
   data model **[VC DM, outside this source]**. Those are stated from general
   knowledge and never quoted, except RFC 7515, which is quoted only from
   `.cache/rfc-7515.txt`. COSE facts point at the held records' artifacts and are
   not quoted, because those sources are not cached.

3. **Our decisions are read from m-of-n at `db472d2`** (2026-11-02), with
   `git -C ../mofn show db472d2:<path>`, never from the working tree. Every quote
   of ours below resolves, whitespace collapsed, in the file this table gives for
   its short name. A quote's locator is therefore `<path>@db472d2`.

   | name | path at db472d2 | standing |
   |---|---|---|
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25; decides DEC-002 for option 5. Its text *"has **not been reviewed** by a second reader"* |
   | ADR-0005 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted 2026-10-25, `reviewed: false`; decides DEC-003 |
   | ADR-0001, ADR-0003 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0003-ksa-core-decisions.md` | accepted. ADR-0003: *"where they differ, the SPEC governs and the ARCH document is corrected."* |
   | ARCH-0001 v0.1.6 | `spec/ARCH-0001-authorization-attestation.md` | draft; §5 R-M, R-I and R-O rows; §6 matrix; §7 with DEC-001, DEC-004 and DEC-005 open |
   | ARCH-0001 changelog | `spec/ARCH-0001-CHANGELOG.md` | 0.1.3: *"The §6 matrix is untouched — that is mofn#110's lane."* |
   | ARCH-0002 v0.9.1 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P1.1, P5 and P5.2 draft |
   | ARCH-0002 changelog | `spec/ARCH-0002-CHANGELOG.md` | 0.8.0: *"The §6 matrix rows are left to mofn#110."* |
   | proposal | `spec/ARCH-0001-PROPOSAL-v0.2.0.md` | *"Status: proposed. Nothing in this document is accepted."* The source of R-O-05 |
   | SPEC-0001 v0.1.0, SPEC-0002 v0.3.0 | `spec/SPEC-0001-ksa-architecture.md`, `spec/SPEC-0002-ksa-core.md` | drafts; they govern under ADR-0003 |
   | ARCH-0003 v0.3.1 | `spec/ARCH-0003-wallet-object-model.md` | draft: *"Nothing here is accepted."* |
   | DECISIONS-0001 v0.4.1 | `project/DECISIONS-0001.md` | the register. Item 4: until the proposal is accepted, *"R-M-11/R-O-05/R-O-06 have no force"* |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing, now closed: ADR-0004, *"MD-3's narrowing is closed by acceptance"* |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft. *"Evidence only — it decides nothing."* |
   | CONTRIBUTING, BACKLOG-0001 | `CONTRIBUTING.md`, `project/BACKLOG-0001.md` | process |

   **`docs/extraction.md` is stale on one point.** It says, of MD-3, *"and **no
   DEC-002 ADR exists.**"* At `db472d2` ADR-0004 accepts DEC-002, so this file
   maps against ADR-0004 and its option 5. It still records where the source cuts
   against option 5, which is what that rule is for. `docs/` is not edited here.

4. **Numbering collisions.**
   - A bare `R-NNNN` is this record's `w3c-vc-jose-cose#R-NNNN`, and `N-NNN` is
     an entry of its `normative.md`. **mofn's research report R-0006 is not this
     record's R-0006** (the `vc` and `vp` MUST NOT); it is always written "mofn
     report R-0006". SPEC-0002's negative vectors are N-1 to N-10, written
     "SPEC-0002 vector N-7".
   - `SD-n` are the source defects of `normative.md`. `MSG-nn`, `ENC-nn` and
     `TEN-nn` are `messages.yaml`. Protocol flows, error paths and defects are
     cited by their ids in `protocol.yaml`. `M01` to `M06`, `ST-nn` and `NM-nn`
     are `state-machine.yaml`. Example numbers are the source's.
   - `R-M-NN`, `R-I-NN` and `R-O-NN` are ARCH-0001 §5, except R-O-05, which is a
     proposal §7 row. `MD-n` are dated meeting decisions. "ADR-0004 item 3" is the
     third item of that ADR's Decision section. `P1`, `P1.1`, `P5`, `P5.2` are
     ARCH-0002. `V1` to `V9` are SPEC-0002 §9.2. "Condition (n)" is one of the six
     conditions of mofn report R-0006 §3.2.
   - `§x ¶n` counts blocks as `normative.md` does: every paragraph, list, table
     and example of the section is one block, and an empty paragraph is not
     counted; an N-id beside it is the entry that reproduces the block.
     `requirements.yaml` counts paragraphs only, so the two differ where a list
     or an example comes earlier in the section. Of the locators below that
     matters for two: §1.1.2 ¶5 is a list, which requirements.yaml does not
     count (N-015), and §3.1.2 ¶13 is its paragraph 11 (R-0025, R-0026; N-044).

5. **Labels.** *(inferred)* marks anything the source implies rather than
   states, and every consequence drawn here. **Ours** marks the library's own
   proposal. Source errors are quoted as printed: *"evaluated according the
   verifier's validation policies"* (§5.4 ¶1, R-0078), *"listed in a controlled
   identifier documents or a DID Document"* (§4.2 ¶4, R-0072), *"JWK claim iss"*
   (§3.1.3 ¶8, N-052). Every example value below was decoded from the HTML, never
   from the `.txt`, whose span boundaries insert spaces into compact strings. Each
   count says how many candidates it examined.

---

## 1. What we adopt

1. **Sign the document's bytes, and canonicalise nothing.** *"The unsecured
   verifiable credential is the unencoded JWS payload."* (§3.1.1 ¶2, N-032).
   *"The unsecured verifiable credential is the unencoded COSE_Sign1 payload."*
   (§3.3.1 ¶2, N-073). The reason given: *"A benefit to this approach is that
   payloads can be made to conform directly to [VC-DATA-MODEL-2.0] without any
   mappings or transformation, while at the same time supporting registered
   header parameters and claims that are understood in the context of JOSE,
   SD-JWT, and COSE."* (§3 ¶3, N-027). The payload is decoded only after the
   envelope verifies: *"Set document to the decoded JWS payload."* (§5.1, N-111),
   inside the branch taken when processing completes successfully. ENC-01 records
   that no character encoding, serialisation or canonicalisation is stated.

   Ours: SPEC-0002 §5, *"The envelope exists so that a verifier can **verify
   before it decodes**."*; and mofn report R-0006 §3.2, condition (3):
   *"Canonicalisation runs **once, at authoring**, on trusted input, and never as
   part of verification."*

   **Condition (3) is met by construction for vc+jwt and vc+cose, and not for
   vc+sd-jwt.** The SD-JWT route transforms: *"The Issuer then converts the input
   JWT Claims Set (i.e., the unsecured verifiable credential) into an [SD-JWT]
   payload according to SD-JWT issuance instructions."* (§3.2.1 ¶2, N-056), and
   verification reverses it: *"Convert the SD-JWT payload back into the JWT
   Claims Set by reversing the process in [SD-JWT]."* (§5.2, N-113). That is
   protocol `no-mapping-versus-sd-jwt-conversion`. **Consequence (inferred):** an
   export (§5.1 below) writes the VC's JSON once, from a statement that has
   already reached V9, and signs those octets. No later step re-serialises them.

2. **The principal travels in the payload; `kid` is a hint.** *"If kid is
   present in the JOSE Header or the COSE Header, a verifier can use this
   parameter as a hint indicating which key was used to secure the verifiable
   credential, when performing a verification process as defined in RFC7515."*
   (§4.1.1 ¶1, N-093). The issuer named in the payload wins over the header:
   *"When issuer value is a string, iss value, if present, MUST match issuer
   value."* (§4.1.2 ¶2, R-0066) and *"When issuer value is an object with an id
   value, iss value, if present, MUST match issuer.id value."* (§4.1.2 ¶2,
   R-0067). Both bind the producer. No verifier check is stated (error path
   `iss-does-not-match-issuer`).

   Ours: ADR-0005, *"The native `kid` may be exported in COSE's `kid` header or
   DSSE's `keyid` as a **hint**; the principal travels in the payload."*; ARCH-0002
   P1.1, *"An export may place the KSA `kid` in the COSE `kid` header as a hint;
   an import never treats one as a principal."*; and SPEC-0002 V6, where *"the
   decoded `suite` and `says` equal the envelope's"* or the statement is
   `envelope-mismatch`.

   **Same rule, and ours adds the check (inferred).** R-0066 and R-0067 are
   SPEC-0002 §5's agreement rule applied to `iss`, without V6. **Consequence:** an
   importer rejects a VC whose `iss` differs from `issuer` (or `issuer.id`), as V6
   rejects a `says` that differs from the TBS's. Test: Example 21's credential
   (`iss` equal to `issuer`, the one such payload among 18 decoded) passes; the
   same payload with `iss` altered, and signed again, is rejected at that check,
   before any other claim is evaluated.

3. **Registered names on the envelope, the data model untouched.** Besides §3
   ¶3 above: *"When present in the COSE Header or as CWT Claims, members
   registered in the IANA CBOR Web Token (CWT) Claims registry or the IANA COSE
   Header Parameters registry are to be interpreted as defined by the
   specifications referenced in those registries."* (§3.3.3 ¶1, N-086), and
   R-0062 RECOMMENDS those two registries for members *"that might be confused
   with members defined by [VC-DATA-MODEL-2.0]"*. The JOSE twin names *"the IANA
   JSON Web Token Claims registry or the IANA JSON Web Signature and Encryption
   Header Parameters registry"* (§3.1.3 ¶2, N-046), in the non-normative §3.1.3.

   Ours: ADR-0001, *"Registry identifiers **may** appear at interchange
   boundaries, and such mappings are documented as lossy per R-I-01."*; ADR-0004
   item 3, *"the native model depends on none of CBOR Tags, COSE Header
   Parameters, COSE Algorithms, CWT Claims, or CWT Confirmation Methods. Each may
   appear at an interchange boundary, mapped lossily per R-I-01."*

   **The source draws our boundary itself (inferred):** registry-named members
   on the envelope, a payload that owes the envelope nothing. An export puts
   registry identifiers only there, and R-I-01's table lists each one (§5.1).

4. **A signature's time is not the statement's validity.** *"When the iat
   (Issued At) and/or exp (Expiration Time) CWT claims are present, they
   represent the issuance and expiration time of the signature, respectively."*
   and *"Note that these are different from the validFrom and validUntil
   properties defined in Validity Period, which represent the validity of the
   data that is being secured."* (§3.3.3 ¶4, N-089). *"Use of the nbf (Not
   Before) claim is NOT RECOMMENDED, as it makes little sense to attempt to
   assign a future date to a signature."* (§3.3.3 ¶4, R-0063). For JOSE the same
   sentences stand in §3.1.3 ¶6 (N-050), which is non-normative.

   Ours: SPEC-0002 §7.3 keeps a validity window apart from *"`issued` is the
   speaker's statement of when it signed."*

   **Consequence (inferred):** a KSA statement's `not-before` and
   `not-on-or-after` become the VC's `validFrom` and `validUntil` [VC DM, outside
   this source], never `nbf` or `exp`. `iat` is the export signature's time, which
   is not the KSA statement's `issued`: two signers, two times. Test: an export
   of a statement issued on one day and exported on the next carries the second
   day in `iat` and leaves `issued` out of the envelope.

5. **What leaves the wallet should be short-lived, because revocation will not
   follow it.** *"Status extension mechanisms such as credentialStatus SHOULD be
   checked."* (§5.4 ¶4, R-0083), and the sentence after it, *"If the extension
   mechanism type is not understood, this property MUST be ignored."* (§5.4 ¶4,
   R-0084; its text is identical to R-0082's, at §5.4 ¶3, about
   `credentialSchema`). The source defines no status mechanism; Example 18's
   `StatusList2021Entry` is non-normative.

   Ours: R-O-02, *"Short-lived validity preferred over revocation-heavy design;
   revocation still representable."*

   **Consequence (inferred):** a KSA `revoke` (SPEC-0002 §8.7) has no status type
   a foreign verifier understands, and R-0084 tells that verifier to ignore one it
   does not. An exported VC is therefore unrevocable in practice. Its
   `validUntil` is bounded by the statement's `not-on-or-after` and kept short,
   and R-I-01's table records revocation as dropped.

6. **One serialisation.** *"Implementations MUST support the JWS compact
   serialization."* (§3.1.2 ¶13, N-044, R-0025) and *"Use of the JWS JSON serialization
   is NOT RECOMMENDED."* (§3.1.2 ¶13, N-044, R-0026). SPEC-0002 §5 has one transmitted
   form too. An export emits compact JWS only. Whether these two rules, which
   close the presentation section, also govern credentials is not said (SD-24);
   emitting compact is safe under either reading (inferred).

## 2. What we adapt, and how

1. **A type indicator: the source's SHOULD becomes our MUST, on both sides.**
   *"The typ header parameter SHOULD be vc+jwt."* (§3.1.1 ¶3, R-0013). *"The typ
   (16) header parameter, as described in COSE "typ" (type) Header Parameter,
   SHOULD be application/vc+cose."* (§3.3.1 ¶3, R-0048). No step of §5.1 to §5.3
   reads it (ENC-07). §5.4 names it once, as the key to an undefined list: *"All
   claims expected for the typ MUST be present."* (§5.4 ¶1, R-0077; SD-23). And
   no example sets a registered value. Of the 19 distinct JOSE headers decoded
   from the HTML (12 outer, 7 carried in data URLs, the KB-JWT's among them), 16
   are `kid` and `alg` alone, and the only `typ` values are `vp+ld+json+sd-jwt`,
   `vc+ld+json+sd-jwt` and the KB-JWT's `kb+jwt`. All 7 encoded COSE_Sign1
   protected headers are the map {1: -35}; Example 26 prints its protected header
   elided after the first entry (TEN-13).

   Ours: condition (4), *"The encoding profile is named by an **authenticated
   type indicator** carried inside the signed bytes."*; proposed R-O-05, *"The
   signed payload SHALL be the canonical encoding verbatim, carried with an
   authenticated type indicator."*; natively, `kind` sits inside the TBS and
   SPEC-0002 §6.3 signs a label: *"`DS` is the label `KSA-STMT-SIG-v1` followed
   by one zero octet"*.

   **Adaptation (ours):** an export always sets `typ` (`vc+jwt`, or
   `application/vc+cose` in the protected bucket, where RFC 9596 confines it:
   `rfc-9596` `requirements.yaml`), and `cty` `vc` or content type (3)
   `application/vc` (R-0014, R-0049). Our importer requires `typ` and rejects a
   VC without it. That deviates from no producer requirement and only declines,
   as a consumer, what the source permits. P5.2 shows how to document such a
   deviation. Test: Example 1's JWS, whose header is `alg` and `kid` only, is
   rejected on import.

2. **Find the key from the header, never from the payload.** *"If iss is present
   in the JOSE Header, the JWT Claims, or the COSE Header, a verifier can use this
   parameter to obtain a JSON Web Key to use in the verification process."*
   (§4.1.2 ¶1, N-095). The JWT Claims are the payload. Against that, *"As a
   general rule, verifiers SHOULD strive to minimize the processing of untrusted
   data. This includes minimizing any processing of the protected header,
   unprotected header, or payload as part of the key discovery procedures."* (§5
   ¶2, R-0075). That is protocol `key-discovery-reads-untrusted-data` and ST-11.

   Ours: SPEC-0002 §5 (adopt 1), and proposed R-O-05, *"A verifier SHALL verify
   the signature before decoding and SHALL NOT canonicalize input as part of
   verification."*

   **Adaptation (ours):** an export puts every key-discovery hint in the
   protected header: `kid`, and `iss` replicated there for JOSE (§4.1.2 permits
   the JOSE Header), or `iss` inside CWT Claims (15) in the protected bucket for
   COSE, as Examples 24 and 25 do. Our importer reads hints from the header only.
   **The limit (inferred):** JOSE and COSE still make a verifier decode the
   protected header to learn `alg` before verifying. SPEC-0002 avoids that by
   carrying `suite` and `says` outside the TBS as hints checked at V6. An import
   path cannot remove it, only bound it (SPEC-0002 §13.6).

3. **Always send `iss`: it is what lets `kid` stay a hint.** R-0072 applies only
   *"When iss is absent"*. Read whole: *"When iss is absent, and the issuer is
   identified as a [URL], the kid MUST be an absolute [URL] to a verification
   method listed in a controlled identifier documents or a DID Document."* (§4.2
   ¶4, R-0072); R-0074 says the same of a holder. Both sit under §4.2's opening,
   *"When using controlled identifier documents with this specification, the
   following requirements apply."* (§4.2 ¶1, N-100). With `iss` present and equal to
   `issuer` (R-0066), the only MUST left on `kid` is R-0065, *"kid MUST be present
   when the key of the issuer or subject is expressed as a DID URL."* (§4.1.1 ¶2,
   R-0065), beside R-0073's RECOMMENDED form (reject 1).

   Ours: ADR-0005, *"a 32-octet byte string, `SHA-256(public-key encoding)`"*,
   exported *"as a **hint**"*.

   **Adaptation (ours):** set `iss`, always. Then the 32-octet `kid` can ride as
   a hint without breaking R-0072, and the verification method lookup of §4.2 is
   never forced. Without `iss`, and where controlled identifier documents are used
   (§4.2 ¶1), R-0072 rules the 32-octet `kid` out of the header and asks for an
   absolute URL, a form ADR-0005 does not define (§5, row 9). Test: such an export
   that omits `iss` and carries the 32-octet `kid` violates R-0072, and the
   negative fixture says so.

4. **One key per protocol: the export key is not the statement key.** The source
   fixes no algorithm and says nothing about using one key in two protocols.
   Ours: SPEC-0001 §5.3, *"A wallet SHOULD use a separate key per protocol —
   derived from one seed where convenient — and MUST record on the key any use
   outside KSA."*; SPEC-0002 §13.2, *"A key that is also used in another protocol
   cannot have a KSA signature replayed there, or a signature from there replayed
   as KSA, provided that protocol also domain-separates."*

   **Disjoint signing inputs (inferred).** A JWS signs *"ASCII(BASE64URL(UTF8(JWS
   Protected Header)) || '.' || BASE64URL(JWS Payload))"* (RFC 7515 §2, from
   `.cache/rfc-7515.txt`): base64url characters and full stops, never a zero
   octet. Suite 1 prepends a DS label, and every DS label ends in one (SPEC-0002
   §6.3, §6.4). A COSE_Sign1 signs a four-element `Sig_structure` array
   (`rfc-9052` `messages.yaml`), whose first octet is the array head 0x84, while
   a suite-1 signature input opens with `K` (0x4b). So no suite-1 signature input
   is a valid JWS or COSE_Sign1 signing input, or the reverse. That is SPEC-0002
   §13.2's condition, met here by structure rather than by a label. Suite 8
   passes its label as the ML-DSA context instead (§6.4) and is not assessed
   here.

   **Adaptation (ours):** the export is signed by a separate suite-1 key of the
   persona, recorded as SPEC-0001 §5.3 requires. SPEC-0002 §12.7 has no usage
   code for it (codes 1 to 6: statements, tls, ipsec, email, payments,
   transport), and adding one is *"added by a revision of this specification
   accepted through an ADR."* (SPEC-0002 §12). Open question 7.

5. **Spell the KSA principal as a URL, by a rule we write.** *"The value of the
   issuer property can be either a string or an object."* (§4.1.2 ¶2, N-096).
   R-0072 presumes an issuer *"identified as a [URL]"*, and the data model makes
   `issuer` a URL [VC DM, outside this source]. Ours: ADR-0005, *"Text
   renderings are presentation only (`SPEC-0002` §11)."*, and among its rejected
   alternatives the text form of a `kid`, *"a rendering of the same digest; kept
   for display, never signed"*, and `did:key`, because *"the key type is named by
   a multicodec code, from a registry maintained outside the project"*.

   **Gap (inferred):** in a VC export the URL spelling of a `kid` **is** signed,
   inside the payload, by the export signature. ADR-0005 rejected exactly that,
   for KSA-signed bytes, and defines no URL form for the boundary. The source
   offers no key-only URL in normative text. Its one example, a `did:jwk` in
   Example 17's `alsoKnownAs` (§8.1), is non-normative and puts JOSE registry
   names (`kty`, `crv`) inside the identifier. **Adaptation (ours):** define a
   boundary URL form for a `kid`, record it as lossy per R-I-01, and use it for
   `issuer`, `iss` and `credentialSubject.id`. Open question 2.

## 3. What we reject, and why

1. **The JWK Thumbprint as an identifier of ours.** *"When using [URL]
   identifiers, the kid is RECOMMENDED to be an absolute [URL] that includes a
   JWK Thumbprint URI as defined in [RFC7638]."* (§4.2 ¶5, R-0073). The
   thumbprint's preimage is a JSON object of registry-named members [JOSE,
   outside this source]. Measured on the source's only Ed25519 key (Example 17,
   `x` = `ANRjH_zxcKBxsjRPUtzRbp7FSVLKJXQ9APX9MP1j7k4`, 32 octets decoded): its
   RFC 7638 thumbprint is `FfMbzOjMmQ4efT6kvwTIJjelTqjl0xjEIWQ2qobsRMM`, which
   Example 17 prints, while its KSA `kid`, SHA-256 of the same 32 octets, is
   `07cb1bad800608e2ba4e0c48c6e6c8d56ee9dc9521d50119d96493984ad6fc3b`. One key,
   two SHA-256 identifiers. The key also passes SPEC-0002 §6.3's strict key rules
   (canonical, on the curve, not of small order), so it could be a suite-1 key.

   Ours: ADR-0005 rejects the COSE key thumbprint because its *"preimage is a
   registry-labelled `COSE_Key`"*. **The JWK thumbprint is its JOSE counterpart
   (inferred),** so the objection carries over natively. At the boundary ADR-0001
   permits it. **We reject** it as an identifier, and keep the RECOMMENDED form
   available as a rendering only if an export ever needs R-0073. **And the
   source's own instance is wrong:** the value §4.2 ¶5 prints,
   `NzbLsXh8uDCcd-6MNwXF4W_7noWXFZAfHkxZsRGC9Xs`, is the id of Example 17's P-521
   method, whose key's thumbprint is `GOwvnQ44eBJYLBsBHz-6XAcoAVyS-7FdaBqTTpDxArQ`
   (TEN-23, recomputed here).

2. **Ignoring what is not understood, on import.** *"Additional members may be
   present as header parameters and claims. If they are not understood, they
   MUST be ignored."* (§3.3.3 ¶5, R-0064). *"All claims that are not understood
   MUST be ignored."* (§5.4 ¶1, R-0079). R-0082 (§5.4 ¶3) and R-0084 (§5.4 ¶4)
   do the same for extension types. There is no exception for a critical
   parameter, while RFC 7515 §4.1.11 says *"If any of the listed extension Header
   Parameters are not understood and supported by the recipient, then the JWS is
   invalid."* The JOSE twin of R-0064 is in the non-normative §3.1.3, so for JOSE
   the clash is with advice (protocol `ignore-versus-crit`; ST-12).

   Ours: SPEC-0002 §7.1, *"The statement map is **closed**: a key not listed
   above MUST cause rejection."*; §13.5, *"an unknown kind or field is invalid. A
   verifier MUST NOT skip what it does not understand (ARCH-0002 P5)."*; P5.2,
   *"P5 governs the native model and the payload interior, in both directions. At
   an interchange boundary the foreign envelope's own rules govern its
   exterior."*, with *"our verifier **rejects** an envelope carrying unrecognised
   exterior fields"* on import and *"we **emit no** exterior field a conforming
   DSSE consumer would have to ignore, and we require nothing of foreign
   consumers"* on export.

   **We reject the ignore rule on import,** as a documented deviation in P5.2's
   sense, for header parameters. On export we emit no member a conforming
   verifier would have to ignore, and never `crit`. **Where P5.2 runs out
   (inferred):** it reasons that *"the payload interior is ours to govern"*. A VC's
   payload interior is the data model's, not ours, so P5.2 does not say whether
   our importer may reject an unknown VC claim that R-0079 tells it to ignore.
   Open question 6.

3. **`cnf` in exports (ARCH-0002 P1.1, draft), at the cost of a RECOMMENDED.**
   *"Use of a proof-of-possession key provided by the Holder to the Issuer to
   establish a cryptographic binding to the Holder in the Verifiable Credential
   that is verifiable by the Verifier in the Verifiable Presentation is
   RECOMMENDED."* (§4.1.3 ¶2, R-0069), with the verifier's MAY in R-0068. Ours:
   P1.1, *"**export emits no `cnf` claim.** Proof of possession is native
   (`SPEC-0002` §6.4, `KSA-POP-SIG-v1`)"*, because *"carrying `cnf` imports a
   second IANA registry, with **no allocation tiers**"*. Natively, SPEC-0001
   §8.1: *"`presented` is OPTIONAL. When present, `sig` is a **proof of
   possession**"*.

   **Not a conflict as the source words it, but a cost (inferred).** R-0069
   never names `cnf`: it follows R-0068's MAY on `cnf` under §4.1.3's heading,
   and no step of §5 checks a binding, so P1.1 narrows a means R-0069 leaves
   open (§5, row 13). Yet `cnf` is the only carrier for a proof-of-possession key
   the source describes, so an export without it reaches a foreign verifier as a
   bearer credential unless another binding is defined. The source's only working
   demonstration of holder binding is Example 22: its KB-JWT verifies under the
   P-384 `cnf` key carried in its own issuer-signed JWT, with SHA-384. That is the
   one signature of the 26 decoded from the document that verifies under a key
   the document prints (§7.7; protocol `possession-proof-undefined` notes that
   nothing is named for vp+jwt or vp+cose). P1.1's reason concerns the CWT
   Confirmation Methods registry. The JOSE `cnf` is RFC 7800's [JOSE, outside
   this source; `rfc-7800` is a stub], which P1.1 does not discuss. **We reject**
   `cnf` provisionally, as P1.1 says, and record the deviation from R-0069 in the
   R-I-01 table. Open question 5.

4. **The SD-JWT route, this semester.** Ours: ARCH-0003 §12 item 4,
   *"**Selective disclosure** in presentations (SD-JWT, RFC 9901) — the
   `disclosure` policy is the hook; out of scope this semester."* The source's
   SD-JWT route is also its most defective. §5.2 takes only *"inputMediaType:
   vc+sd-jwt"* (§5.2, N-112) although its heading and *"Upon receipt of the
   verifiable credential or presentation secured with [SD-JWT], the holder or
   verifier follows this algorithm:"* (§5.2, N-113) cover presentations (SD-17,
   TEN-10, ST-01). §1.1.2.2 misstates what a disclosure contains (SD-5, TEN-01),
   SD-JWT is cited as an unversioned draft (SD-30, TEN-29), and Example 22 ends
   with a tilde after its KB-JWT (TEN-03). **We reject** vc+sd-jwt for R-I-06 now.

5. **Exporting KSA presentations as vp+jwt or vp+cose.** R-I-06 exports
   credentials. The source's presentation routes have no possession step for
   vp+jwt or vp+cose (`possession-proof-undefined`), never verify the credentials
   they envelope (`enveloped-credentials-not-verified`, ST-09), leave mixed
   mechanisms unsettled (SD-25, TEN-18), and state how an enclosed credential is
   carried only for COSE, as base64 (R-0051; `enveloping-encoding-only-for-cose`).
   A KSA presentation stays native (SPEC-0001 §8.1).

6. **The source's examples as positive fixtures.** No example carries a
   registered `typ` (adapt 1). No signature but one KB-JWT verifies under any key
   the document prints (§7.7). Every COSE example pairs `alg` -35 with a 64-octet
   signature. The `kid`s are not URLs where R-0072 would require one if
   controlled identifier documents were used (§4.2 ¶1). Example 17 violates
   R-0070, and Example 20 uses a data URL parameter RFC 2397 does not define. They are negative or shape fixtures only (§7.7).

## 4. The record's verdict, tested

`record.yaml` says `useful` because the source is *"The securing mechanism
R-I-06's VC export would cite, and it fills R-0006's ∅ VC cells for the
enveloping route: signs the VC JSON bytes as an opaque JWS/COSE_Sign1 payload
with no canonicalisation (condition (3) met by construction), but its type
indicator `typ` is only a SHOULD, is never checked in §5, and no example carries
a registered value (JWS/COSE examples omit it; SD-JWT examples use the withdrawn
+ld+json values) — condition (4) available, not required."* Each clause was tested
against the source.

- **The mechanism R-I-06 would cite: holds, with a condition** (§6.4 items 3
  and 4). Of its three envelopes, only COSE_Sign1 is one ADR-0004 item 4 names.
- **Fills mofn report R-0006's ∅ cells for the enveloping route: holds** for
  what is hashed (no content digest on the JWS and COSE routes; SD-JWT hashes
  its disclosures), canonicalised (nothing), signed (the payload octets and the
  protected header) and carried, and for how a verifier proceeds (§5). It fills
  no cell of VC Data Integrity or of the data model.
- **Opaque payload, no canonicalisation: holds** for JWS and COSE_Sign1. 7 of 7
  decoded COSE_Sign1 payloads open with 0x7b, a JSON object. The clause's scope
  already excludes SD-JWT, which converts (adopt 1).
- **`typ` only a SHOULD: holds**: R-0013, R-0018, R-0028, R-0034, R-0048 and
  R-0054 are all SHOULD.
- **Never checked in §5: holds, but not "never named".** §5.4 names `typ` in
  R-0077, as the key to a list of expected claims no section defines (SD-23).
- **No example carries a registered value: holds** (adapt 1's census), Example
  26's elided protected header aside.
- **The parenthesis, *"SD-JWT examples use the withdrawn +ld+json values"*: overstated
  twice.** The six outer SD-JWT examples (Examples 4, 5, 6, 18, 19 and 20) omit
  `typ` exactly as the six outer JWS examples do: 16 of the 19 distinct JOSE
  headers decoded from the HTML carry no `typ` (adapt 1). The `+ld+json` values
  occur only in the three SD-JWTs carried in data URLs (the presentation that
  Examples 6 and 9 both envelope, Examples 21 and 22).
  And Appendix A says *"Changed media types from
  application/{vc,vp}+ld+json+{jwt,sd-jwt,cose} to
  application/{vc,vp}+{jwt,sd-jwt,cose}."*, not withdrawn.
- **Condition (4) available, not required: holds.** For COSE it holds because
  RFC 9596 forbids `typ` in the unprotected bucket (`rfc-9596`
  `requirements.yaml`), not because this source says where it goes.

**Verdict:** `useful` holds. The parenthesis should read *JWS, SD-JWT and COSE
headers omit it; the three SD-JWTs nested in data URLs use the +ld+json forms
Appendix A reports as changed*. Proposed only; `record.yaml` is not edited here.

## 5. Mapping to our decisions

Verdicts, exactly four: **adopts** (the source and our text agree, and we take
the source's rule), **constrains** (one narrows what the other leaves open),
**conflicts** (one object or implementation cannot satisfy both), **silent** (one
side does not reach the other's subject). Levels are the source's keywords as
printed: SHOULD is not MUST. Every quote of ours resolves in the path given, at
`db472d2`.

| # | Ours (quoted; path@db472d2) | Source (R-id, level) | Verdict |
|---|---|---|---|
| 1 | **R-I-06** *"Export a subset of `AuthzCert` as a W3C Verifiable Credential using a documented context."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.2) | R-0001, R-0003 MUST secure as §3.1 or §3.3; R-0012 MUST use RFC 7515; R-0047 MUST use COSE_Sign1; R-0045 MAY use COSE; the payload is the unencoded VC (§3.1.1 ¶2, §3.3.1 ¶2) | **constrains.** The source fixes how the export is secured; R-I-06 names no securing. Subset and context are ours and the data model's (§5.1) |
| 2 | **§6 W3C VC row**: *"ArtifactStatement or NameCert depending on type"*, *"Context must be pinned"* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §6) | none: the source secures whatever VC it is given | **silent.** The row also disagrees with R-I-06, which exports `AuthzCert` (ours; §7.2) |
| 3 | **ADR-0004 items 1–2** *"The CBOR data model, encoded under the core deterministic requirements of RFC 8949 §4.2.1"* (`spec/ADR-0004-dec-002-encoding.md`@db472d2) | every route's payload is JSON (TEN-09); R-0080 MUST compact JSON-LD; §1.1.2 ¶5 says CBOR | **silent.** Native encoding is not reached; KSA-CBOR never enters a VC (§6.4, item 1) |
| 4 | **ADR-0004 item 3** *"Each may appear at an interchange boundary, mapped lossily per R-I-01."* (`spec/ADR-0004-dec-002-encoding.md`@db472d2) | R-0062 RECOMMENDED registries; §3.1.3 ¶2 (non-normative); R-0071 MUST JWK | **adopts.** The registries sit on the envelope, which is the boundary. Item 3's list names no JOSE or JWK registry (§6.4, item 2) |
| 5 | **ADR-0004 item 4** *"COSE_Sign1 and DSSE are export envelopes only."* (`spec/ADR-0004-dec-002-encoding.md`@db472d2) | JWS (R-0012), SD-JWT (R-0027), COSE_Sign1 (R-0047) | **constrains.** Read as the set of export envelopes, it admits vc+cose alone (§6.4, item 3) |
| 6 | **MD-3** *"CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping."* (`project/meetings/2026-09-28.md`@db472d2) | as rows 3–5; JSON-LD terms are global names [VC DM, outside this source] | **constrains.** COSE is named and JOSE is not. Closed by ADR-0004 |
| 7 | **DEC-005** (open) *"Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §7) | JWS or COSE_Sign1; no DSSE | **silent.** DEC-005 is the envelope for `ArtifactStatement`; nothing decides the `AuthzCert` export's envelope (open question 1) |
| 8 | **R-I-03** *"Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT claims (at least one envelope in v1)."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.2) | R-0061 MAY CWT claims in a COSE header parameter; Examples 24 and 25 put `iss` and `sub` in protected label 15 | **constrains.** The "+ CWT claims" branch needs the source's MAY taken; our profile takes it (adapt 2) |
| 9 | **ADR-0005 items 1–2** *"a 32-octet byte string, `SHA-256(public-key encoding)`"*; *"Text renderings are presentation only (`SPEC-0002` §11)."* (`spec/ADR-0005-dec-003-key-identifier.md`@db472d2) | R-0065 MUST; R-0072 MUST; R-0074 MUST; R-0073 RECOMMENDED; RFC 7515: a `kid` *"MUST be a case-sensitive string"* | **constrains.** ADR-0005's items fix the native `kid`, and its interchange paragraph only permits exporting it as a hint (row 10), so an export's `kid` header is left open. Where controlled identifier documents are used and `iss` is absent (§4.2 ¶1, N-100), R-0072 narrows that header to an absolute URL, which cannot be the 32-octet `kid`, and R-0073 recommends a thumbprint URI, another digest (reject 1). One export can satisfy both by carrying the URL, or by sending `iss` (adapt 3) |
| 10 | **ADR-0005, Interchange (export)** *"The native `kid` may be exported in COSE's `kid` header or DSSE's `keyid` as a **hint**; the principal travels in the payload."* (`spec/ADR-0005-dec-003-key-identifier.md`@db472d2) | §4.1.1 ¶1 `kid` as a hint; R-0066, R-0067 MUST match `issuer` | **adopts** (adopt 2). It names no JOSE `kid`, which is a string (open question 3) |
| 11 | **ADR-0005, Interchange (import)** *"On import, a foreign `kid` that disagrees with the `kid` computed from the key is **rejected**"* (`spec/ADR-0005-dec-003-key-identifier.md`@db472d2) | R-0072 URL `kid`; R-0073 thumbprint URI; TEN-22 | **conflicts.** A URL or thumbprint `kid` never equals a computed KSA `kid`. Read literally, every conforming VC that carries one is rejected on import, while §6 marks W3C VC import **I** (open question 4) |
| 12 | **ADR-0001 / P1** *"Registry identifiers **may** appear at interchange boundaries, and such mappings are documented as lossy per R-I-01."* (`spec/ADR-0001-key-relative-naming.md`@db472d2) | §3 ¶3; §3.3.3 ¶1 | **adopts** (adopt 3) |
| 13 | **P1.1** (draft) *"**export emits no `cnf` claim.** Proof of possession is native (`SPEC-0002` §6.4, `KSA-POP-SIG-v1`)"* (`spec/ARCH-0002-key-relative-naming.md`@db472d2) | R-0069 RECOMMENDED; R-0068 MAY | **constrains** (reject 3). R-0069 recommends a proof-of-possession key binding and names no carrier; the one the source describes is `cnf` (§4.1.3 ¶1, R-0068), which P1.1 removes, so an export can follow R-0069 only by a binding the source does not describe |
| 14 | **P5 / P5.2** (draft) and SPEC-0002 §13.5 *"an unknown kind or field is invalid. A verifier MUST NOT skip what it does not understand (ARCH-0002 P5)."* (`spec/SPEC-0002-ksa-core.md`@db472d2) | R-0064, R-0079, R-0082, R-0084 MUST ignore | **conflicts** for R-0064 alone, on import: COSE header parameters are envelope exterior, where reject 2 extends P5.2's import rule (written for DSSE, the COSE analysis owed) to reject what R-0064 says MUST be ignored. **Silent** for R-0079, R-0082 and R-0084: they govern a VC's claims and extension properties, a payload interior that is the data model's, while P5 and the quoted §13.5 govern native statements and P5.2 reasons only about an interior that is ours (reject 2; open question 6). Export is compatible |
| 15 | **R-O-05** (proposed; DECISIONS-0001 item 4: no force) *"The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator."* (`spec/ARCH-0001-PROPOSAL-v0.2.0.md`@db472d2, §7) | ENC-01; R-0013, R-0048 SHOULD; §4.1.2 ¶1 reads `iss` from the payload; R-0075 SHOULD | **constrains.** R-O-05 makes mandatory what the source leaves SHOULD (adapt 1, adapt 2). Its first clause cannot hold for any export: the VC is not our canonical encoding (§6.4, item 1) |
| 16 | **R-O-03** *"Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.3) | no canonicalisation anywhere; 0 occurrences of *canonical* | **adopts.** Nothing to cite and nothing invented. Our profile still states the JSON it emits (§5.1) |
| 17 | **R-O-01** *"Every signed object SHALL have an issuer key that can be specified as `KeyId`."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.3) | no algorithm fixed; the examples use ES256, ES384 and EdDSA (Example 17) | **constrains.** The export key must be a suite key, today Ed25519, since suite 2 (P-256) is *"reserved; not yet specified"* (SPEC-0002 §6.2) |
| 18 | **R-O-02** *"Short-lived validity preferred over revocation-heavy design; revocation still representable."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.3) | R-0083 SHOULD check status; R-0084 MUST ignore an unknown status type | **adopts** (adopt 5) |
| 19 | **R-M-02** *"A principal MAY be identified solely by key or key digest."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.1) | §4.2's documents; R-0072; §4.1.2 ¶2 | **constrains.** A key-only principal survives only through a URL spelling (adapt 5) |
| 20 | **R-I-01** *"Publish a mapping table for each supported foreign format: what is preserved, dropped, or inferred."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.2) | the format's members, registries and ignore rules | **constrains.** The source fixes the rows such a table owes (§5.1) |
| 21 | **R-I-02** *"Import SHALL NOT require the foreign object to become a native trust anchor."* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §5.2) | no trust model; §4.2 resolves keys from a document at a URL | **silent** |
| 22 | **SPEC-0001 §5.3** *"A wallet SHOULD use a separate key per protocol — derived from one seed where convenient — and MUST record on the key any use outside KSA."* (`spec/SPEC-0001-ksa-architecture.md`@db472d2) | no key-reuse rule | **silent.** Our rule constrains our own export key (adapt 4) |
| 23 | **SPEC-0002 §7.3** *"`issued` is the speaker's statement of when it signed."* (`spec/SPEC-0002-ksa-core.md`@db472d2) | §3.3.3 ¶4; R-0063 NOT RECOMMENDED | **adopts** (adopt 4) |
| 24 | **ARCH-0003 §12 item 4** *"out of scope this semester."* (`spec/ARCH-0003-wallet-object-model.md`@db472d2) | §3.2 (R-0027 to R-0044); §5.2 | **constrains.** Ours removes vc+sd-jwt from this semester's export (reject 4) |
| 25 | **§6 COSE_Sign1 + CWT row** *"Align `iss`/`sub` with KeyId profile (DEC-003)"* (`spec/ARCH-0001-authorization-attestation.md`@db472d2, §6) | R-0066, R-0067 MUST; R-0061 MAY | **constrains.** Aligning `iss` with the `KeyId` makes the VC's `issuer` itself the `KeyId`'s URL spelling (adapt 5) |

Count: adopts 6, constrains 12, conflicts 2, silent 5, of 25 rows, row 14 counted
by its conflict (it is silent for three of its four requirements). **Both
conflicts fall on ADR-0005's import rule (row 11) and on ARCH-0002's draft P5.2
as reject 2 extends it to COSE headers (row 14); none falls on ADR-0004.** Pass 1
counted constrains 10 and conflicts 4: the cross-check pass re-derived rows 9,
13 and 14 from their quoted texts.

### 5.1 R-I-06: a `trust` statement exported as a W3C VC through this source (draft)

ADR-0004 lists `trust` as the kind that carries the `AuthzCert` role (TV-5).
This is the R-I-01 table such an export owes. It is a draft and every row is
*(inferred)*: the source defines no import or export of anything.

| KSA (SPEC-0002) | becomes | |
|---|---|---|
| the signed statement `[suite, says, tbs, sig, ? pub]` | nothing. The VC is a translation, signed again (adopt 1, adapt 4) | **dropped, replaced** |
| statement digest, SHA-256(`tbs`) | the VC's `id`, as a URL spelling of the digest [VC DM, outside this source] | **preserved by reference** (ours) |
| `kind` 5 and its DS label | the VC's `type` [VC DM, outside this source], plus `typ` `vc+jwt` or `application/vc+cose` and `cty` `vc` or content type (3) `application/vc` (R-0013, R-0014, R-0048, R-0049; ours MUST, adapt 1) | **respelled** |
| `says` | `issuer`, a URL spelling of the `kid` (open question 2), with `iss` equal to it in the protected header (R-0066, adapt 2, adapt 3) | **preserved, respelled** |
| `suite` 1 | the export key's own algorithm: `EdDSA` in JOSE (Example 17's JWK, non-normative) and -8 in COSE (`rfc-9053` `normative.md` §2.2) | **not carried** |
| the export key (adapt 4) | `kid`: its 32-octet KSA `kid` as a COSE `kid`, or a text rendering as a JOSE one (open question 3) | **hint only** |
| `this` = `[1, kid]` | `credentialSubject.id`, a URL spelling [VC DM, outside this source] | **respelled** |
| the threshold form, `trusts` and `threshold` | nothing in this source | **dropped** |
| `body.about`, attribute ranges named by `(DefinitionId, label)` | `credentialSubject` claims under a documented context, terms as IRIs that embed the DefinitionId (ours) | **inferred.** P1's identity survives only if the IRI carries the DefinitionId |
| `may-delegate` | nothing in this source | **dropped**, or context terms no foreign verifier interprets |
| `valid.not-before`, `valid.not-on-or-after` | `validFrom`, `validUntil` [VC DM, outside this source]; never `nbf` (R-0063) | **preserved** |
| `valid.issued` | nothing; `iat` is the export signature's time (§3.3.3 ¶4) | **dropped** |
| a `revoke` (§8.7) | no status type; an unknown one MUST be ignored (R-0084) | **dropped**; short `validUntil` instead (adopt 5) |
| holder binding | no `cnf` (P1.1); R-0069's RECOMMENDED can then be followed only by a binding the source does not describe (row 13) | **dropped**, open question 5 |
| — | `vc` and `vp` claim names, never (R-0006) | — |
| — | no `crit`, and no member a consumer would have to ignore (P5.2, reject 2) | — |
| — | compact JWS (R-0025); a COSE_Sign1 whose payload is the VC's JSON octets (§3.3.1 ¶2, TEN-09), tagged 18 or not (open question 11) | — |

Text values are copied byte for byte, because SPEC-0002 §4.1 forbids
normalisation, and the JSON is emitted once (adopt 1). The result, as for the
other foreign formats, is a translation: a new object the exporter signs, never
the KSA statement itself.

## 6. MD-3, ADR-0004 and DEC-002

MD-3 reads *"CBOR data model, no IANA tags, COSE as export only; type identity
is `(defining key, label)` per P1; YAML is the human form with a canonical
one-way mapping."* ADR-0004 decided DEC-002 for option 5 on 2026-10-25, and
ARCH-0001 §7 now reads *"accepted 2026-10-25 — option 5"*. Nothing in this
section reopens it. CONTRIBUTING §5: *"Only an ADR accepts a decision."* The
section exists because an extraction that can only confirm is not evidence,
and because ADR-0004 was taken without a second reader.

**This source is a signing-envelope document,** so `docs/extraction.md`'s rule
applies and the header-by-header mapping follows. Its result is an **export
mapping with no import into native form**: nothing in a VC becomes a KSA
statement, and SPEC-0001 §5.3's external statement is the only import route,
*"keeping its original bytes and mapping its speaker, subject and claims
through an interchange profile (ARCH-0001 §6)"*.

### 6.1 Structure by structure

| source construct | our statement or envelope (SPEC-0002) | export mapping | mapping |
|---|---|---|---|
| the payload: the VC's JSON, unencoded (MSG-01, ENC-01) | the TBS, KSA-CBOR (§4) | a translation of the statement (§5.1) | **re-encoded and re-signed** |
| JWS compact (MSG-06) | the envelope `[suite, says, tbs, sig, ? pub]` (§5) | emitted when JOSE is the route (open question 1) | **shape only** |
| JOSE `alg` (MSG-07) | `suite`, inside the TBS | the export key's algorithm | **not carried** |
| JOSE `kid` (MSG-07) | `says`, a 32-octet `kid` | a hint, as text (open question 3) | **hint** (adopt 2) |
| JOSE `typ` (MSG-07) | `kind` and DS label | always `vc+jwt` (adapt 1) | **same intent; ours unconditional** |
| JOSE `cty` (MSG-07) | none | `vc` | **label only** |
| `crit` (not named by the source) | closed maps (§7.1) | never emitted | reject 2 |
| `iss` in header or claims (MSG-08) | `says` | equal to `issuer`, in the protected header | adopt 2, adapt 3 |
| `iat`, `exp` (MSG-08) | `valid.issued` is the KSA signer's own signing time (§7.3); nothing expires a signature | the export signature's times | **export-only** (adopt 4) |
| `nbf` | `valid.not-before` | never: `validFrom` instead (R-0063) | adopt 4 |
| `cnf` (MSG-08; §4.1.3) | `presented` proof of possession (SPEC-0001 §8.1) | not emitted (P1.1) | reject 3 |
| `vc`, `vp` claims | none | never (R-0006) | — |
| SD-JWT, disclosures, KB-JWT (MSG-11 to MSG-15) | none | not emitted this semester | reject 4 |
| COSE_Sign1, tag 18 (MSG-18) | the envelope | emitted when COSE is the route; tag open (open question 11) | **shape only** |
| COSE alg (1) (MSG-19) | `suite` | -8 for an Ed25519 export key | **not carried** |
| COSE content type (3) (MSG-19) | none | `application/vc` (R-0049) | **label only** |
| COSE kid (4) (MSG-19) | `says` | the 32-octet `kid`, a hint | **same bytes, hint only** (adopt 2) |
| COSE typ (16) (MSG-19) | `kind` and DS label | `application/vc+cose`, protected (adapt 1) | **same intent; ours unconditional** |
| CWT Claims (15) (MSG-20) | `says`, `valid` | `iss` (adapt 2); `sub` only if it equals `credentialSubject.id` (ours) | **boundary only** |
| unprotected bucket (MSG-19) | `suite`, `says` and `pub` as hints (§5) | empty | **not used** |
| data URL (MSG-05) | none | not needed: credentials only (reject 5) | — |
| controlled identifier document, JsonWebKey, publicKeyJwk (MSG-22 to MSG-24) | `key-publish` and the key store (§10) | only if a URL issuer must resolve (open question 2) | **not carried** |

**What we deliberately do not carry, and why:**
- **`cnf`**, per P1.1 (reject 3).
- **Registry-named members inside the payload.** The JSON-LD context and terms
  are ours to document (R-I-06), built from DefinitionIds (§5.1).
- **`crit`**, and any member a consumer would have to ignore (P5.2).
- **The SD-JWT route** and **presentations** (reject 4, reject 5).
- **The JWS JSON serialization** (R-0026) and **nested encryption** (R-0016,
  R-0052): a MAY with no receiving step in §5 (`encryption-without-receive-step`).
- **A second copy of the principal in a header.** `kid` is a hint; the
  principal is `issuer` (adopt 2).

### 6.2 DEC-002's options, as we state them

From ARCH-0001 §7 at `db472d2`:

1. *"Canonical S-expressions (RFC 9804) as canonical; JSON as diagnostic."*
2. *"CBOR + CDDL as canonical; COSE for signed form."*
3. *"JSON + RFC 8785 JCS as canonical; DSSE for signed form."*
4. *"Dual canonical (CBOR and JSON) with a documented bijection."*
5. *"CBOR data model under RFC 8949 §4.2.1, restricted and decoder-enforced,
   with no IANA registry native; COSE and DSSE as export envelopes only."*
   Accepted by ADR-0004.

*"Drivers: library availability, SCITT alignment, SPKI fidelity, human debug."*
ADR-0004 adds namespace governance, order-only divergence and the
canonical-encoding conditions. Its rejected alternatives: option 2 because
*"Registry-allocated tags and header parameters are native under it; fails P1
(`ADR-0001`)."*; option 3 as *"Withdrawn on the four grounds of
`DECISIONS-0001` item 2"*; option 4 for *"Two canonical forms and a bijection
nobody has specified, for no driver the single form does not meet."*

### 6.3 Scored against this source

| this source | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 (KSA-CBOR) |
|---|---|---|---|---|---|
| **The payload a VC verifier receives is JSON under every route.** ENC-01; TEN-09; R-0080 | translates | translates: the envelope is native, the payload is not | closest: JSON native, but a statement is not a VC and is still mapped (inferred) | its JSON half only if the bijection reaches the data model (unspecified) | translates and re-signs |
| **Registry names stay on the envelope.** §3 ¶3; §3.3.3 ¶1; R-0062 | boundary (inferred) | **native**: fails P1 (ADR-0001) | boundary (inferred) | ADR-0004's cell: *"fails through its option-2 half (ours)"* | **boundary**, item 3: the split the source draws |
| **Type indicator.** R-0013, R-0048 SHOULD; never checked in §5 | not scored | COSE `typ` optional; protected when present (`rfc-9596`) | not scored | — | **unconditional**: `kind` in the TBS and a DS label |
| **The `kid` the source expects.** R-0072 URL; R-0073 thumbprint | respells | respells; its natural `kid`, RFC 9679's thumbprint, is rejected by ADR-0005 | respells | respells | respells (reject 1, adapt 5) |
| **Canonicalisation at verification.** none | — | — | — | — | — |
| **SCITT alignment.** vc+cose is a COSE_Sign1 with optional CWT claims (R-0061). The five cells are ADR-0004's own scores | *"none"* | *"native"* | *"via DSSE"* | *"partial"* | *"at the export boundary"*, as the source corroborates |

### 6.4 Where this source cuts against ADR-0004 and option 5, or leaves them underdetermined

1. **No export can be our canonical encoding verbatim. Names option 3, weakly.**
   Every route's payload is JSON. Even the COSE route, despite *"When using COSE,
   the Verifiable Credential or Presentation is encoded as a CBOR data
   structure."* (§1.1.2 ¶5, N-015), carries *"the unencoded COSE_Sign1 payload"*
   (§3.3.1 ¶2, N-073), and 7 of 7 decoded payloads open with 0x7b (TEN-09,
   protocol `cose-payload-json-or-cbor`). So an option 5 export pays a second
   encoding and a second signature for one claim, and R-O-05's first clause cannot
   hold for it. Only option 3's canonical form is JSON, and JCS would buy the VC
   route nothing, because it signs octets as produced. Option 3 is withdrawn, and
   options 1 and 2 pay the same translation. **A cost, not a reason to reopen.**
2. **ADR-0004 item 3 is a list, and the list is CBOR and COSE only.**
   Underdetermined. The JOSE route depends on registries the source itself names,
   *"the IANA JSON Web Token Claims registry or the IANA JSON Web Signature and
   Encryption Header Parameters registry"* (§3.1.3 ¶2, N-046), and every route's
   key discovery on JWK (R-0071). Item 3's heading excludes them natively. Its
   enumeration does not name them, although ARCH-0001 §7 asked the ADR to state
   the property *"as the list of registries it excludes"*. An R-I-01 table for
   vc+jwt must name them itself.
3. **The export envelope set has no JOSE in it, and the VC ecosystem's key
   discovery is JOSE-shaped.** Underdetermined, and the pressure falls on
   DEC-005, not DEC-002. ADR-0004 item 4, R-I-03 and DEC-005 name DSSE and
   COSE_Sign1 only. In the source the JWS and SD-JWT routes each carry a
   MUST-support serialisation (R-0025, R-0042), securing with COSE is a MAY
   (R-0045), and key discovery is JOSE's even on the COSE route. A COSE `kid` is
   a hint for *"a verification process as defined in RFC7515"* (§4.1.1 ¶1;
   protocol `kid-hint-cites-rfc7515-for-cose`),
   `iss` yields *"a JSON Web Key"* (§4.1.2 ¶1), and *"Verification material MUST
   be expressed in the publicKeyJwk property of a JsonWebKey."* (§4.2 ¶3, R-0071).
   So a COSE-only export, the one route item 4 admits, still needs JWKs as soon as
   an issuer must resolve through §4.2. And DEC-005 is *"Envelope for
   ArtifactStatement"*: no DEC decides the `AuthzCert` export's envelope.
4. **ADR-0005's interchange paragraph is written for COSE and DSSE.** Not a cut
   against option 5, but the most concrete friction in the source: a JOSE `kid`
   is a string (RFC 7515 §4.1.4), R-0072 and R-0073 want URLs, and ADR-0005
   defines neither a text nor a URL form (§5 rows 9 to 11).
5. **The two drafts at the boundary meet a RECOMMENDED and four MUSTs.** P1.1's
   `cnf` rule narrows how R-0069's RECOMMENDED can be followed (row 13), and
   P5.2's import rule, extended to COSE headers, conflicts with R-0064's MUST,
   while P5 is silent on the three MUSTs about a VC's claims (row 14). Neither is
   ADR-0004's, and both are drafts, so this is the place to settle them before
   acceptance.

Searched and found **not** to cut against option 5:
- **Canonicalisation.** The source canonicalises nothing, which every option
  tolerates (row 16).
- **Order-only divergence.** A VC with reordered members is a different signed
  object and verifies on its own terms. The source has no view on native order.
- **Registry use.** The source confines registry names to the envelope, which is
  item 3's boundary exactly (row 4).

### 6.5 Where it favours option 5

1. **Over option 2, on namespace governance.** The source keeps registry names
   out of the payload by design (§3 ¶3). Option 2 would make them native, and
   gain nothing for VCs: their payload is JSON under COSE too (§6.4, item 1).
2. **Over option 2, on the type indicator.** The source shows what an optional
   type indicator becomes: a SHOULD that §5 never checks and that no example sets
   (adapt 1). Option 5's `kind` cannot be omitted.
3. **On SCITT alignment, option 5's own claim holds.** vc+cose is one more
   COSE_Sign1 export, *"at the export boundary"*, as ADR-0004 scored it.

### 6.6 Not discriminators

Compact serialisation, data URLs, media type registration and nested
encryption: every option needs the same export code for them. Algorithm
identifiers: registry values at the boundary under every option. The JSON-LD
context R-I-06 asks for: owed under every option.

### 6.7 Net, stated as evidence

On ADR-0004's own criteria the source is nearly neutral, and where it leans it
leans toward option 5: registry names confined to the envelope, and a type
indicator that the optional design leaves unchecked. Its one cost to option 5 is
that every VC is a JSON translation signed again. Option 3 would avoid the
encoding hop and is withdrawn; options 1 and 2 pay the same. **The decisions it
actually presses are elsewhere:** ADR-0005's interchange paragraph (rows 9 to
11), the two boundary drafts P1.1 and P5.2 (rows 13 and 14), DEC-005's scope
(row 7), and ARCH-0001's own disagreement between R-I-06 and its §6 W3C VC row
(row 2). Nothing here decides DEC-002 again.

## 7. Implementation consequences for mofn#110

### 7.1 What mofn#110 owns

From the tree, not from the issue: *"The §6 matrix is untouched — that is
mofn#110's lane."* (ARCH-0001 changelog 0.1.3) and *"The §6 matrix rows are
left to mofn#110."* (ARCH-0002 changelog 0.8.0). P1.1's acceptance test makes
the COSE_Sign1 + CWT row carry the `kid` and `cnf` rules: *"The R-I-01 mapping
table for COSE_Sign1 + CWT carries a `kid` row and a `cnf` row stating the rules
above"*. BACKLOG-0001 T-053: *"Record interchange losses in the §6 matrix
(R-I-01)"*. mofn report R-0006 §2.5 says of the W3C VC row: *"the securing
mechanism is **unsourced** in the library; the row's mapping cannot be evidenced
until it is"*. This record is that source.

### 7.2 The W3C VC row

- **Which native kind.** R-I-06 exports `AuthzCert`; the row maps W3C VC to
  *"ArtifactStatement or NameCert depending on type"*. The row should say which
  kinds export (a `trust`, per ADR-0004's TV-5 role) and which an import maps to.
  Open question 9.
- **Export column `C`.** Cite this record for securing, and the profile of §5.1
  for the mapping.
- **Import column `I`.** Under ADR-0005 as written, a URL `kid` is rejected
  (row 11). The row either narrows import to VCs whose `kid` is absent or equals
  a computed `kid`, or ADR-0005 is amended. Open question 4.
- **"Context must be pinned"** stays the data model's matter. This source adds
  the media types, the `typ` values and the key rules below.

### 7.3 Media types and `typ` values

| media type (§6) | `typ` (R-id, level) | `cty` / content type (3) | export | import |
|---|---|---|---|---|
| application/vc+jwt | `vc+jwt` (R-0013 SHOULD) | `vc`, when present (R-0014 SHOULD) | **only if JOSE is admitted** (row 5; open question 1) | yes |
| application/vp+jwt | `vp+jwt` (R-0018 SHOULD) | `vp` (R-0019) | no (reject 5) | open (question 10) |
| application/vc+sd-jwt | `vc+sd-jwt` (R-0028 SHOULD) | `vc` (R-0029) | no (reject 4) | not this semester |
| application/vp+sd-jwt | `vp+sd-jwt` (R-0034 SHOULD) | `vp` (R-0035) | no | **no algorithm in §5** (SD-17) |
| application/vc+cose | `application/vc+cose` (R-0048 SHOULD) | `application/vc` (R-0049 SHOULD, unconditional; SD-22) | **yes** | yes, JSON payload |
| application/vp+cose | `application/vp+cose` (R-0054 SHOULD) | `application/vp` (R-0055) | no | open (question 10) |

The JOSE values omit `application/` and the COSE values carry it (ENC-07). §5's
inputs use the short form for all three, *"inputMediaType: vc+cose or vp+cose"*
(§5.3, N-114), so an implementation maps between the forms. The COSE
registrations identify *"a COSE object"*, not a COSE_Sign1 (TEN-28).

### 7.4 Securing mechanisms

- **JWS**: compact only (R-0025, R-0026); `typ`, `cty`, `kid`, `iss` and `alg`
  in the protected header; no `crit`, `vc`, `vp` or `nbf`.
- **COSE_Sign1**: payload = the VC's JSON octets (§3.3.1 ¶2; all 7 examples).
  An importer must decide whether to accept a CBOR payload, which §1.1.2 ¶5
  suggests and §5.3 does not say how to decode (open question 10). Protected:
  alg (1), content type (3), kid (4), CWT Claims (15) with `iss`, typ (16). The
  source states no tag rule; every example is tagged 18 (ENC-05).
- **SD-JWT**: out (reject 4).

### 7.5 Key discovery

- Send `iss`, equal to `issuer` (adapt 3). R-0072's URL `kid` is then not
  required, and §4.2's lookup is optional.
- If a URL issuer must resolve, the document's method is a `JsonWebKey`
  (R-0070) with `publicKeyJwk` (R-0071). The source states *"At the time of
  writing, there is no standard way to retrieve a public key in JWK format from
  a DID URL or controlled identifier documents."* (§4.2 ¶3, N-102;
  `cid-retrieval-undefined`). Example 17 is not a model: its Ed25519 method is
  `JsonWebKey2020` (TEN-23).
- **A suite-1 key has a JWK form** (`kty` OKP, `crv` Ed25519, `x` the 32 octets
  [JOSE, outside this source]; Example 17 prints one). **A suite-8 key has none
  in any source the library holds,** so a suite-8 export cannot be published
  through §4.2 yet (inferred).

### 7.6 Verification gaps an importer must close itself

Each was re-read in the `.txt` and, where marked, re-measured from the HTML.

| gap | where | ids | confirmed here |
|---|---|---|---|
| only *"inputMediaType: vc+sd-jwt"* for SD-JWT; *"Set mediaType to vc"* | §5.2 | SD-17, TEN-10, ST-01 | `.txt` lines 885, 891 |
| a credential-only input document beside *"inputMediaType: vc+jwt or vp+jwt"* | §5.1 | SD-18, TEN-11 | line 868 |
| *"Set mediaType to vc or vp"* with no rule | §5.1, §5.3 | SD-19, ST-02 | lines 873, 909 |
| no step reads `typ`; R-0077's expected claims undefined | §5.1 to §5.4 | SD-23, TEN-12, ST-08 | yes |
| §5.4's MUSTs sit under a SHOULD (R-0076) and change no output | §5, §5.4 | `validation-entered-by-should`, `validation-has-no-output`, ST-06, ST-07 | yes |
| key discovery *"is assumed to have succeeded prior to beginning the verification process"*; the key is no input | §5 ¶1 | `key-not-an-input`, ST-05 | line 856 |
| COSE payload: CBOR in §1.1.2 ¶5, the unencoded document in §3.3.1 ¶2 | §1.1.2, §3.3.1 | TEN-09, `cose-payload-json-or-cbor` | 7 of 7 payloads open 0x7b (HTML) |
| JOSE header rules non-normative, COSE twins normative | §3.1.3, §3.3.3 | SD-15, TEN-05 | HTML class `appendix informative` on §3.1.3, none on §3.3.3 |
| the COSE failure branch is *"If processing aborts for any reason:"* only | §5.3 | SD-21, ST-03 | line 912 |
| unsecured JWTs handled outside §5.1 | §1.1.2.1 | `alg-none-outside-algorithm`, ST-04 | yes |
| enveloped credentials never verified | §3.1.2, §5 | `enveloped-credentials-not-verified`, ST-09 | yes |
| MUST ignore with no `crit` exception | §3.3.3, §5.4 | `ignore-versus-crit`, ST-12 | yes |

### 7.7 Fixtures: what the examples can and cannot test

Measured from the HTML with probes kept in the pass's scratch directory; each
line states what was examined.

- **`typ`.** 19 distinct JOSE headers (12 outer, 7 carried in data URLs):
  `typ` values `vp+ld+json+sd-jwt`, `vc+ld+json+sd-jwt` and `kb+jwt` only, the
  other 16 `kid` and `alg` alone. 7 of 7 encoded COSE_Sign1 protected headers
  are {1: -35}. Examples 24 and 25 (CBOR diagnostic notation) show labels 1, 3,
  4 and 15 and no 16; Example 26's protected header is elided after its first
  entry.
- **COSE `alg` against signature length.** 7 of 7 COSE_Sign1 objects (Examples
  7, 8, 9, 18, 19, 20, and the base64 data URL of Example 23) carry `alg` -35
  with a 64-octet signature (TEN-21). -35 is ES384 (`rfc-9053` `normative.md`
  §2.1, Table 1). That record's requirements pair SHA-384 with P-384 as a
  suggestion, not a keyword, and a P-384 signature is 96 octets, while 64 is the
  P-256 length. The JWS examples are consistent: of 19 distinct compact objects,
  15 are ES256 with 64 octets and 4 are ES384 with 96.
- **Keys.** 10 JWK occurrences, 7 distinct keys, 3 distinct header `kid`s. No
  header `kid` is the RFC 7638 thumbprint of any printed key, and none is an
  absolute URL (TEN-22). Of 10 decoded payloads that name an issuer, 9 have no
  `iss`, the `kid` `ExHkBMW9fmbkvV266mRpuP2sUY_N_EWIN1lapUzO8ro`, and an issuer
  that is an https URL or a `did:web` DID (in one of them, only after a
  disclosure). That breaks R-0072 wherever those issuers use controlled
  identifier documents, the condition of §4.2 ¶1 (inferred, counting `did:web`
  as a URL).
- **Signatures (new here).** Every decoded signature was tried under every
  printed P-256 and P-384 key (4 distinct keys) with SHA-256 and SHA-384: 54
  trials over 19 JWS objects, 14 over 7 COSE_Sign1 objects. **0 of the 25
  signatures other than the KB-JWT verify**, whether signed by an issuer or a
  holder. The one that does is Example 22's KB-JWT, under the `cnf` key of its
  own issuer-signed JWT, which also shows the probe works.
- **Data URLs.** Example 20's COSE credential is printed in 4 distinct forms
  (6 occurrences in the display tabs, 7 with the Issuer Disclosures reprint):
  once as `data:application/vc+cose;base64,0oREo...+Q==` (an elided placeholder
  whose first octets are a COSE_Sign1 head) and 3 under `;base64url`, a parameter
  RFC 2397 does not define, over a value that decodes to the text
  `base64,0oREo...+Q==` or to a base64url encoding of that text (TEN-17). Against
  *"the credentials MUST be encoded using base64 as specified in [RFC2397]"*
  (§3.3.1 ¶5, R-0051).
- **Example 17** has a `JsonWebKey2020` method (against R-0070), and Example 22
  splits into 7 tilde-separated parts, the last empty (TEN-03).

**Consequence:** mofn#110's fixtures are our own. Positives: a vc+cose, and a
vc+jwt only if open question 1 admits JOSE, each with `typ`, `iss`, a `kid` hint
and an Ed25519 export key.
Negatives drawn from the source: no `typ` (Example 1), a non-URL `kid` with no
`iss` (Example 1 again, negative under R-0072 only where a controlled identifier
document is used), a `;base64url` data URL (Example 20), and a
`JsonWebKey2020` method (Example 17).

## 8. Open questions

1. **Which envelope carries R-I-06's export, and which decision owns the
   choice?** ADR-0004 item 4 names *"COSE_Sign1 and DSSE"*; DEC-005 covers
   `ArtifactStatement` only; R-I-03 names DSSE and COSE_Sign1 + CWT claims. The
   source offers JWS, SD-JWT and COSE_Sign1, with MUST-support serialisations
   for the first two (R-0025, R-0042) and securing with COSE as a MAY (R-0045).
   Settle it by widening DEC-005 or in a new DEC.
2. **How is a KSA principal spelled as a URL** for `issuer`, `iss` and
   `credentialSubject.id`? ADR-0005: *"Text renderings are presentation only
   (`SPEC-0002` §11)."* It rejected the text `KeyId` as *"kept for display, never
   signed"* and `did:key` for its multicodec registry. Example 17's `did:jwk` is
   non-normative and embeds JOSE registry names. An https document brings a web
   authority (§4.2). Settle it in ADR-0005's successor or in the R-I-01 VC table
   (adapt 5).
3. **What is the text form of an exported `kid`?** RFC 7515: *"Its value MUST be
   a case-sensitive string."* SPEC-0002 §11.3: *"Byte strings are quoted text:
   `'0x'` followed by lowercase hexadecimal."* R-0073 recommends a thumbprint URI.
   DSSE's `keyid`, which ADR-0005 already names, is a string too, so the question
   is older than this record.
4. **Does ADR-0005's import rule apply to a `kid` that is not a key digest?**
   P1.1: a *"COSE `kid` is a **(party, local label)** pair resolved by table
   lookup"*, and a VC's `kid` is a URL or a thumbprint URI. Read literally, the
   rule rejects every VC import that carries one (row 11). Settle it in P1.1
   before acceptance, and in mofn#110's import column.
5. **`cnf` in VC exports.** Keep P1.1's rule, under which an exported VC reaches
   a foreign verifier as a bearer credential unless another binding is defined,
   and R-0069's RECOMMENDED is not followed through `cnf`, or allow holder
   binding at the VC boundary? Example 22 is the source's only working binding, and it is
   SD-JWT's. Settle it in P1.1.
6. **May our importer reject an unknown VC claim?** P5.2 governs the exterior,
   and reasons that the payload interior is ours, which a VC's is not. R-0079,
   R-0082 and R-0084 say MUST ignore. Settle it in P5.2.
7. **Which key signs an export, and how is it linked to the persona?** SPEC-0001
   §5.3's separate key needs a usage code that SPEC-0002 §12.7 lacks, and a
   statement linking it to the identity key. Settle it in SPEC-0002 §12.7 and
   §8, through an ADR (§12's Specification Required).
8. **Which subset of `trust` exports, under which context?** The threshold form
   and `may-delegate` have no counterpart in this source, and DEC-004, the tag
   language, is open. Settle it in R-I-06's mapping document.
9. **R-I-06 against the §6 W3C VC row.** `AuthzCert`, or *"ArtifactStatement or
   NameCert depending on type"*? Settle it in mofn#110's row.
10. **The import profile.** Require `typ`? Accept a COSE payload that is CBOR
    (§1.1.2 ¶5) or only JSON (§3.3.1 ¶2 and every example)? Settle it in the
    R-I-01 VC table.
11. **Tag 18 on an exported COSE_Sign1.** ADR-0004 forbids tags natively and
    allows registries at the boundary. The source states no rule (ENC-05), and
    every example is tagged. Settle it in the export profile.
12. **The library holds JOSE weakly.** Every [JOSE, outside this source] row
    rests on documents without a record: RFC 7517, RFC 7519, RFC 7638, RFC 8037,
    SD-JWT (RFC 9901, as ARCH-0003 §12 names it) and Controlled Identifiers 1.0,
    with `rfc-7515` and `rfc-7800` as stubs. Ingest them, and take `rfc-7515` past
    stub, before §5.1 is built on. The `artifact-statements` topic, which owns
    this record, is the natural owner.

**Source defects, recorded and not repaired.** Each is already in this record's
artifacts; this file only collects them, and names what it re-measured.
- **Normative status:** §3.1.3 non-normative while its COSE twin binds (SD-15,
  TEN-05, re-checked in the HTML); the media types registered only in a
  non-normative section (SD-16).
- **Algorithms:** SD-17 to SD-21, SD-23; TEN-10 to TEN-12; protocol
  `sd-jwt-status-before-conversion`, `key-not-an-input`,
  `validation-has-no-output`; ST-01 to ST-08.
- **Encoding:** COSE payload JSON or CBOR (TEN-09, re-measured); SD-JWT
  conversion against §3's no-transformation claim
  (`no-mapping-versus-sd-jwt-conversion`).
- **Key discovery:** JOSE-only wording over COSE coverage (SD-29, TEN-27); a
  COSE `kid` hint pointing at RFC 7515 (`kid-hint-cites-rfc7515-for-cose`); the
  retrieval gap (`cid-retrieval-undefined`); Examples 11 and 13 unterminated
  (SD-14, TEN-24); the JWK Thumbprint URI attributed to RFC 7638, which defines
  no URI (SD-34, TEN-23).
- **Scope and placement of requirements:** the COSE content type (3)
  recommended and optional at once (SD-22, TEN-26); the serialisation rules
  closing the presentation sections (SD-24); mixed mechanisms in one
  presentation (SD-25, TEN-18); no encoding stated for an enveloped COSE
  presentation (SD-26); no antecedent for the media type that the MUSTs of
  §3.1.1 to §3.3.2 secure (SD-27).
- **Text:** SD-1 to SD-13, SD-28, SD-30 to SD-32; TEN-02, TEN-04, TEN-06,
  TEN-07, TEN-26, TEN-29.
- **Examples:** SD-14, SD-33; TEN-13 to TEN-25. Re-measured here: TEN-13, TEN-17,
  TEN-21, TEN-22 and TEN-23, plus the new signature result of §7.7.

## 9. bears_on corrections

`record.yaml` lists R-I-06 and DEC-003. Both were checked against ARCH-0001
v0.1.6 at `db472d2`. `record.yaml` is not edited here.

- **Both stand.** R-I-06: §5.1 is its securing profile. DEC-003: now accepted by
  ADR-0005, and rows 9 to 11 are where it meets this source. The comment's claim
  that §4.2 RECOMMENDS a JWK Thumbprint URI in an absolute URL `kid` is right
  (R-0073).
- **Warranted additions:**
  - **DEC-002**: §6; items 3 and 4 of ADR-0004 are underdetermined for JOSE.
  - **DEC-005**: its scope leaves the `AuthzCert` export's envelope undecided
    (row 7).
  - **R-I-01**: §5.1 is the table it asks for.
  - **R-I-03**: vc+cose with CWT claims is its COSE_Sign1 branch (row 8).
  - **R-O-05** (proposed): the type indicator and verification before decoding
    (adapt 1, adapt 2).
  - **R-O-02**: unknown status types are ignored, so exports must be
    short-lived (adopt 5).
  - **R-M-02**: a key-only principal must be spelled as a URL (row 19).
- **Weak, optional:** R-O-01 (row 17), R-O-03 (row 16), R-I-02 (row 21).
- **Outside the field's vocabulary.** ADR-0005's interchange paragraph,
  ARCH-0002 P1.1 and P5.2, SPEC-0001 §5.3 and SPEC-0002 §7.3 cannot be listed in
  `bears_on`. They are carried in §5's table; P5.2 (row 14, the conflict with
  R-0064) and P1.1 (row 13) are the ones this record bears on most sharply.
- **The usefulness reason** should be corrected as §4 proposes.

## 10. What this file decides

Nothing. CONTRIBUTING §5: *"Only an ADR accepts a decision."* Each adaptation
and open question names the SPEC section, ADR or DEC that would settle it. The
friction in §6.4 is evidence for ADR-0005's successor, for the two ARCH-0002
drafts before they are accepted, for DEC-005's scope, and for mofn#110's rows.
None of it reopens DEC-002.
