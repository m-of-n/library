---
record: rfc-8392
kind: normative
title: "rfc-8392 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 8392 — normative text, verbatim

**What this file is.** Every normative statement of RFC 8392, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing here is paraphrased and nothing is
retyped: each fenced block was lifted from `.cache/rfc-8392.txt` by line range
by script. Prose outside the fences is this extraction's, and says only where
a statement sits and what it is.

| | |
|---|---|
| **Source** | `.cache/rfc-8392.txt`, 1403 newline-delimited lines |
| **Digest** | `9021ff7c4d274cf34873fe4f4fb17c4fe323247dd0f96bfcab54909bfcdc5f13` |
| **BCP 14 keywords** | **9** — 8 MUST and 1 MUST NOT; `bin/bcp14-count`, boilerplate excluded |

**Region convention.** Each digest is the sha256 of the region's lines joined
by `\n` with no trailing newline — the convention established by two earlier
passes in this effort.

**Page decoration is never inside a region.** The source is a paginated RFC
with **25 form feeds**. Twenty-four of them sit inside a five-line page break
(running footer, the form-feed line, running header, blank, blank), at lines
58-62, 114-118, 170-174, 226-230,
282-286, 338-342, 394-398, 450-454, 506-510, 562-566, 618-622, 674-678,
730-734, 786-790, 842-846, 898-902, 954-958, 1010-1014, 1066-1070, 1122-1126,
1178-1182, 1234-1238, 1290-1294 and 1346-1350; the **twenty-fifth** is the
document's last two lines, 1402-1403 — footer and form feed, with no running
header after them because the document ends there.
**[corrected 2026-10-21, pass 3:** this read *"25 form feeds and 25 five-line
page breaks"* and listed the last range as 1402-**1404**. There is no line
1404 — the cache is 1403 newline-delimited lines, and `split` on a newline
returns a 1404th empty element after the final one. The 24 complete breaks were
re-verified to have exactly the shape named above, and the 25th to be two
lines.**]**

**Five** headings below are quoted as **two or three adjacent regions each**,
with the break declared in place: §6, §7.1, §7.2, §9.1.2 (twice) and
§9.3/§9.3.1 — **six declared breaks**, at 394-398, 450-454, 506-510, 674-678,
730-734 and 786-790. **[corrected 2026-10-21, pass 3:** this sentence said
*"Four sections"* and named only §7.1, §7.2, §9.1.2 and §6, while this file's
own body already declared the fifth at the §9.3/§9.3.1 heading. The seven other
page breaks that fall between two consecutively quoted regions — 226-230,
282-286, 338-342, 562-566, 618-622, 842-846 and 898-902 — separate distinct
statements or sections rather than splitting one passage, so they need no
in-place declaration.**]** **Nothing is welded
across the gap**: re-verified in pass 3 that no region contains a form-feed
line, a running footer or a running header, and that all 37 fenced blocks are
byte-identical to their declared line ranges. Note for any later pass:
Python's `splitlines()` splits on
form feeds as well as newlines and would shift every line number here by up to
25; this file was built with `split("\n")`.

**Where a line break falls inside a sentence**, the sentence is quoted as the
whole fenced region rather than reflowed, so the break is visible. The
`requirements.yaml` entries carry the same text whitespace-normalised, and that
file declares the normalisation.

---

## §1 — Introduction

Kept, though it is motivation, for one reason: it is the sentence the rest of
the document is answerable to, and every byte-cost finding in
`design-notes.md` is measured against it.
```
   The JSON Web Token (JWT) [RFC7519] is a standardized security token
   format that has found use in OAuth 2.0 and OpenID Connect
   deployments, among other applications.  JWT uses JSON Web Signature
   (JWS) [RFC7515] and JSON Web Encryption (JWE) [RFC7516] to secure the
   contents of the JWT, which is a set of claims represented in JSON.
   The use of JSON for encoding information is popular for Web and
   native applications, but it is considered inefficient for some
   Internet of Things (IoT) systems that use low-power radio
   technologies.

   An alternative encoding of claims is defined in this document.
   Instead of using JSON, as provided by JWTs, this specification uses
   CBOR [RFC7049] and calls this new structure "CBOR Web Token (CWT)",
   which is a compact means of representing secured claims to be
   transferred between two parties.  CWT is closely related to JWT.  It
   references the JWT claims and both its name and pronunciation are
   derived from JWT (the suggested pronunciation of CWT is the same as
   the English word "cot").  To protect the claims contained in CWTs,
   the CBOR Object Signing and Encryption (COSE) [RFC8152] specification
   is used.
```

*Source `.cache/rfc-8392.txt` lines 177-196 · `sha256:ec767f8bf68f73793b7ac11a9249f923adbc1959038cd3a3a9056952307c6609`*

## §1.1 — CBOR-Related Terminology
```
   In JSON, maps are called objects and only have one kind of map key: a
   string.  CBOR uses strings, negative integers, and unsigned integers
   as map keys.  The integers are used for compactness of encoding and
   easy comparison.  The inclusion of strings allows for an additional
   range of short encoded values to be used.
```

*Source `.cache/rfc-8392.txt` lines 200-204 · `sha256:622841f0e8e9fa75be5678fee9bbd9eb6b6f373a0b1e298e5c1e0f04a0480625`*

## §2 — Terminology

### The BCP 14 recital

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing. `bin/validate` recounts the
requirement texts with boilerplate stripping **off**, so an entry carrying this
paragraph would add 11 phantom keywords and break the reconciliation.
```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-8392.txt` lines 208-212 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*

### Inherited terminology
```
   This document reuses terminology from JWT [RFC7519] and COSE
   [RFC8152].
```

*Source `.cache/rfc-8392.txt` lines 214-215 · `sha256:6649ba7b4406c3c40292ab4f909e08746749a677dab0092cdeed7134637640cc`*

### StringOrURI

**The type that decides whether a COSE Key Thumbprint can be a CWT `iss`.**
See `design-notes.md` §2.
```
   StringOrURI
      The "StringOrURI" term in this specification has the same meaning
      and processing rules as the JWT "StringOrURI" term defined in
      Section 2 of [RFC7519], except that it is represented as a CBOR
      text string instead of a JSON text string.
```

*Source `.cache/rfc-8392.txt` lines 217-221 · `sha256:92d6fafb1ab5b7aa615089df26207a259d0245c6182d5f3a2f1f28b9cab34694`*

### NumericDate

Carries one of the nine BCP 14 keywords, and it is a **tag prohibition**: the
leading tag 1 `MUST be omitted`.
```
   NumericDate
      The "NumericDate" term in this specification has the same meaning
      and processing rules as the JWT "NumericDate" term defined in
      Section 2 of [RFC7519], except that it is represented as a CBOR
      numeric date (from Section 2.4.1 of [RFC7049]) instead of a JSON
      number.  The encoding is modified so that the leading tag 1
      (epoch-based date/time) MUST be omitted.
```

*Source `.cache/rfc-8392.txt` lines 231-237 · `sha256:8ed21f4916842446b18480faf1b22de37f39948325b2b2c59349fc121a5d084a`*

### Claim Name, Claim Key, Claim Value, CWT Claims Set
```
   Claim Name
      The human-readable name used to identify a claim.

   Claim Key
      The CBOR map key used to identify a claim.

   Claim Value
      The CBOR map value representing the value of the claim.

   CWT Claims Set
      The CBOR map that contains the claims conveyed by the CWT.
```

*Source `.cache/rfc-8392.txt` lines 239-249 · `sha256:a66b7a718523004810c2d687aa370795c00e5fa8cc4a774850e43abb86161a3c`*

## §3 — Claims

Two statements that between them decide how little a conformant CWT has to
carry, and one of the nine keywords (`MUST be ignored`).
```
   The set of claims that a CWT must contain to be considered valid is
   context dependent and is outside the scope of this specification.
   Specific applications of CWTs will require implementations to
   understand and process some claims in particular ways.  However, in
   the absence of such requirements, all claims that are not understood
   by implementations MUST be ignored.

   To keep CWTs as small as possible, the Claim Keys are represented
   using integers or text strings.  Section 4 summarizes all keys used
   to identify the claims defined in this document.
```

*Source `.cache/rfc-8392.txt` lines 253-262 · `sha256:a15bd3195177691ce211d3c4f1f79ac495acc8e99b7536b96b98ce73cd7c0bcc`*

## §3.1 — Registered Claims

No capitalised keyword. The force is carried by *"None of the claims defined
below are intended to be mandatory to use or implement"* and by the lowercase
*"should define"*.
```
   None of the claims defined below are intended to be mandatory to use
   or implement.  Rather, they provide a starting point for a set of
   useful, interoperable claims.  Applications using CWTs should define
   which specific claims they use and when they are required or
   optional.
```

*Source `.cache/rfc-8392.txt` lines 266-270 · `sha256:87e01435193a950c4b3ff96dcd6051959c4e6febdcfd1e3904b5d4501032eb20`*

### §3.1.1 — iss (Issuer) Claim
```
   The "iss" (issuer) claim has the same meaning and processing rules as
   the "iss" claim defined in Section 4.1.1 of [RFC7519], except that
   the value is a StringOrURI, as defined in Section 2 of this
   specification.  The Claim Key 1 is used to identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 274-277 · `sha256:6d9f39dbbf94c9531807808d8aa123b6de3f1ec88c32db439e56ef6d157332ae`*

### §3.1.2 — sub (Subject) Claim
```
3.1.2.  sub (Subject) Claim

   The "sub" (subject) claim has the same meaning and processing rules
   as the "sub" claim defined in Section 4.1.2 of [RFC7519], except that
   the value is a StringOrURI, as defined in Section 2 of this
   specification.  The Claim Key 2 is used to identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 287-292 · `sha256:25cfff9ce55960fe0d1d39e290b4782b12ac7792d49cc3db1531980850063617`*

### §3.1.3 — aud (Audience) Claim

**The one claim definition that admits an array.** §4's Table 1 and §9.1.2's
registry entry both say `text string` and nothing else; see
`design-notes.md` §7, defect D-3.
```
3.1.3.  aud (Audience) Claim

   The "aud" (audience) claim has the same meaning and processing rules
   as the "aud" claim defined in Section 4.1.3 of [RFC7519], except that
   the value of the audience claim is a StringOrURI when it is not an
   array or each of the audience array element values is a StringOrURI
   when the audience claim value is an array.  (StringOrURI is defined
   in Section 2 of this specification.)  The Claim Key 3 is used to
   identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 294-302 · `sha256:8aeb4d2f2bd419806daf27f90b88a7886986b068339d639f9588d0433ceee950`*

### §3.1.4 — exp (Expiration Time) Claim
```
3.1.4.  exp (Expiration Time) Claim

   The "exp" (expiration time) claim has the same meaning and processing
   rules as the "exp" claim defined in Section 4.1.4 of [RFC7519],
   except that the value is a NumericDate, as defined in Section 2 of
   this specification.  The Claim Key 4 is used to identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 304-309 · `sha256:ea118c87662a3d6b08e8c53ce09cb4801aeb6ca997db742dfddfbdc370af7a60`*

### §3.1.5 — nbf (Not Before) Claim
```
3.1.5.  nbf (Not Before) Claim

   The "nbf" (not before) claim has the same meaning and processing
   rules as the "nbf" claim defined in Section 4.1.5 of [RFC7519],
   except that the value is a NumericDate, as defined in Section 2 of
   this specification.  The Claim Key 5 is used to identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 311-316 · `sha256:ba5913f705e511c18cff98378a5826a90573dbc292e8ed5cf22511862055dcde`*

### §3.1.6 — iat (Issued At) Claim
```
3.1.6.  iat (Issued At) Claim

   The "iat" (issued at) claim has the same meaning and processing rules
   as the "iat" claim defined in Section 4.1.6 of [RFC7519], except that
   the value is a NumericDate, as defined in Section 2 of this
   specification.  The Claim Key 6 is used to identify this claim.
```

*Source `.cache/rfc-8392.txt` lines 318-323 · `sha256:a43d00130126df7dcb5d238f278d844ca16b72224afd18f5ea2e3b114cdca465`*

### §3.1.7 — cti (CWT ID) Claim

The only claim whose value is a **byte string**, and so the only claim slot a
bare digest fits into without re-encoding. Wrong slot — it is the `jti`
equivalent. `design-notes.md` §2.
```
3.1.7.  cti (CWT ID) Claim

   The "cti" (CWT ID) claim has the same meaning and processing rules as
   the "jti" claim defined in Section 4.1.7 of [RFC7519], except that
   the value is a byte string.  The Claim Key 7 is used to identify this
   claim.
```

*Source `.cache/rfc-8392.txt` lines 325-330 · `sha256:07f4fb7d1eb6d0cf164ad11e9fa40be5de50e5dbc05d215eb95fc58d3fe7784d`*

## §4 — Summary of the Claim Names, Keys, and Value Types

Table 1 in full, with its caption. This table and the §9.1.2 registry entries
are the **only** place the value types of the seven claims are collected, and
RFC 8392 ships no CDDL, ABNF, ASN.1 or JSON Schema of any kind (each of those
strings occurs **zero** times in the source — see `schema/README.md`), so this
table is the document's whole formal account of its data model.
```
4.  Summary of the Claim Names, Keys, and Value Types

             +------+-----+----------------------------------+
             | Name | Key | Value Type                       |
             +------+-----+----------------------------------+
             | iss  | 1   | text string                      |
             | sub  | 2   | text string                      |
             | aud  | 3   | text string                      |
             | exp  | 4   | integer or floating-point number |
             | nbf  | 5   | integer or floating-point number |
             | iat  | 6   | integer or floating-point number |
             | cti  | 7   | byte string                      |
             +------+-----+----------------------------------+

        Table 1: Summary of the Claim Names, Keys, and Value Types
```

*Source `.cache/rfc-8392.txt` lines 343-357 · `sha256:0ecc983d2a5d67286c0dec2d8fad0739d0a682b086dd038a23d5eebc0c51208d`*

## §5 — CBOR Tags and Claim Values

The document's single `MUST NOT`, and the escape hatch in the same paragraph.
```
5.  CBOR Tags and Claim Values

   The claim values defined in this specification MUST NOT be prefixed
   with any CBOR tag.  For instance, while CBOR tag 1 (epoch-based date/
   time) could logically be prefixed to values of the "exp", "nbf", and
   "iat" claims, this is unnecessary since the representation of the
   claim values is already specified by the claim definitions.  Tagging
   claim values would only take up extra space without adding
   information.  However, this does not prohibit future claim
   definitions from requiring the use of CBOR tags for those specific
   claims.
```

*Source `.cache/rfc-8392.txt` lines 359-369 · `sha256:5d0d10a883b074f11689911e4bf8156721caf18fd9c7c868dd729087aacd0ac7`*

## §6 — CWT CBOR Tag

**Quoted as two regions**: the page break at lines 394-398 falls inside this
section. Region 1 is the three ways to know a structure is a CWT and the
optionality statement; region 2 is the tag-pairing rule, which carries one of
the nine keywords, and Figure 1.
```
6.  CWT CBOR Tag

   How to determine that a CBOR data structure is a CWT is application
   dependent.  In some cases, this information is known from the
   application context, such as from the position of the CWT in a data
   structure at which the value must be a CWT.  One method of indicating
   that a CBOR object is a CWT is the use of the "application/cwt"
   content type by a transport protocol.

   This section defines the CWT CBOR tag as another means for
   applications to declare that a CBOR data structure is a CWT.  Its use
   is optional and is intended for use in cases in which this
   information would not otherwise be known.
```

*Source `.cache/rfc-8392.txt` lines 371-383 · `sha256:c38edb63fc36c8687fc65186c135290c25b1e1126bec8c82d17e259ec02681bf`*

*Page break at lines 394-398 — footer, running header and the blanks around them — omitted. The section continues:*

```
   If present, the CWT tag MUST prefix a tagged object using one of the
   COSE CBOR tags.  In this example, the COSE_Mac0 tag is used.  The
   actual COSE_Mac0 object has been excluded from this example.

   / CWT CBOR tag / 61(
     / COSE_Mac0 CBOR tag / 17(
       / COSE_Mac0 object /
     )
   )

                    Figure 1: Example of CWT Tag Usage
```

*Source `.cache/rfc-8392.txt` lines 399-409 · `sha256:496333a8ec83b2cd3072e7233c111eab518adfbdcf2a095630487308c0c1085c`*

## §7 — Creating and Validating CWTs

### §7.1 — Creating a CWT

**Quoted as two regions**: the page break at lines 450-454 falls between step 4
and step 5. Region 1 is the preamble and steps 1-4 (steps 1-3 and the three
bullets of step 4, carrying three of the nine keywords); region 2 is steps 5
and 6.

This is one of the two **procedures** in the document, and the reason
`protocol.yaml` and `state-machine.yaml` are **not** declared not-applicable
for this record.
```
7.  Creating and Validating CWTs

7.1.  Creating a CWT

   To create a CWT, the following steps are performed.  The order of the
   steps is not significant in cases where there are no dependencies
   between the inputs and outputs of the steps.

   1.  Create a CWT Claims Set containing the desired claims.

   2.  Let the Message be the binary representation of the CWT Claims
       Set.

   3.  Create a COSE Header containing the desired set of Header
       Parameters.  The COSE Header MUST be valid per the [RFC8152]
       specification.

   4.  Depending upon whether the CWT is signed, MACed, or encrypted,
       there are three cases:

       *  If the CWT is signed, create a COSE_Sign/COSE_Sign1 object
          using the Message as the COSE_Sign/COSE_Sign1 Payload; all
          steps specified in [RFC8152] for creating a COSE_Sign/
          COSE_Sign1 object MUST be followed.

       *  Else, if the CWT is MACed, create a COSE_Mac/COSE_Mac0 object
          using the Message as the COSE_Mac/COSE_Mac0 Payload; all steps
          specified in [RFC8152] for creating a COSE_Mac/COSE_Mac0
          object MUST be followed.

       *  Else, if the CWT is a COSE_Encrypt/COSE_Encrypt0 object,
          create a COSE_Encrypt/COSE_Encrypt0 using the Message as the
          plaintext for the COSE_Encrypt/COSE_Encrypt0 object; all steps
          specified in [RFC8152] for creating a COSE_Encrypt/
          COSE_Encrypt0 object MUST be followed.
```

*Source `.cache/rfc-8392.txt` lines 411-445 · `sha256:558d05d850ed05479a5c26350703222aba4117e625d95d2724b97419eb28aafc`*

*Page break at lines 450-454 omitted. The procedure continues:*

```
   5.  If a nested signing, MACing, or encryption operation will be
       performed, let the Message be the tagged COSE_Sign/COSE_Sign1,
       COSE_Mac/COSE_Mac0, or COSE_Encrypt/COSE_Encrypt0, and return to
       Step 3.

   6.  If needed by the application, prepend the COSE object with the
       appropriate COSE CBOR tag to indicate the type of the COSE
       object.  If needed by the application, prepend the COSE object
       with the CWT CBOR tag to indicate that the COSE object is a CWT.
```

*Source `.cache/rfc-8392.txt` lines 455-463 · `sha256:2548449c7e73c4b6d7f4b78e7abba7a36b8f0cf47c65cd4946e6a827be02ab94`*

### §7.2 — Validating a CWT

**Quoted as two regions**: the page break at lines 506-510 falls inside step 5's
second bullet. Region 1 is the preamble — which carries the rejection `MUST` —
and steps 1 to 5's first two bullets; region 2 is step 5's third bullet and
steps 6 and 7.

**Step 5's three bullets are severed by the page break**, so the third bullet is
quoted as the head of region 2 and not welded onto region 1. Read together they
are the three cases; read separately each is still a complete sentence.
```
7.2.  Validating a CWT

   When validating a CWT, the following steps are performed.  The order
   of the steps is not significant in cases where there are no
   dependencies between the inputs and outputs of the steps.  If any of
   the listed steps fail, then the CWT MUST be rejected -- that is,
   treated by the application as invalid input.

   1.  Verify that the CWT is a valid CBOR object.

   2.  If the object begins with the CWT CBOR tag, remove it and verify
       that one of the COSE CBOR tags follows it.

   3.  If the object is tagged with one of the COSE CBOR tags, remove it
       and use it to determine the type of the CWT, COSE_Sign/
       COSE_Sign1, COSE_Mac/COSE_Mac0, or COSE_Encrypt/COSE_Encrypt0.
       If the object does not have a COSE CBOR tag, the COSE message
       type is determined from the application context.

   4.  Verify that the resulting COSE Header includes only parameters
       and values whose syntax and semantics are both understood and
       supported or that are specified as being ignored when not
       understood.

   5.  Depending upon whether the CWT is a signed, MACed, or encrypted,
       there are three cases:

       *  If the CWT is a COSE_Sign/COSE_Sign1, follow the steps
          specified in Section 4 of [RFC8152] ("Signing Objects") for
          validating a COSE_Sign/COSE_Sign1 object.  Let the Message be
          the COSE_Sign/COSE_Sign1 payload.

       *  Else, if the CWT is a COSE_Mac/COSE_Mac0, follow the steps
          specified in Section 6 of [RFC8152] ("MAC Objects") for
          validating a COSE_Mac/COSE_Mac0 object.  Let the Message be
          the COSE_Mac/COSE_Mac0 payload.

```

*Source `.cache/rfc-8392.txt` lines 465-501 · `sha256:2c840a6996551ab565d9795b21e927a118f2e8792a2a9b5c1b7340568f045460`*

*Page break at lines 506-510 omitted. The procedure continues with the third bullet of step 5:*

```
       *  Else, if the CWT is a COSE_Encrypt/COSE_Encrypt0 object,
          follow the steps specified in Section 5 of [RFC8152]
          ("Encryption Objects") for validating a COSE_Encrypt/
          COSE_Encrypt0 object.  Let the Message be the resulting
          plaintext.

   6.  If the Message begins with a COSE CBOR tag, then the Message is a
       CWT that was the subject of nested signing, MACing, or encryption
       operations.  In this case, return to Step 1, using the Message as
       the CWT.

   7.  Verify that the Message is a valid CBOR map; let the CWT Claims
       Set be this CBOR map.
```

*Source `.cache/rfc-8392.txt` lines 511-523 · `sha256:22035d623bda1359717f49b2ff2f94e7ca406e516f0f8542c8e67284261c1c31`*

## §8 — Security Considerations

No capitalised keyword anywhere in this section — the strongest sentence in it
is the lowercase *"producers normally should sign the message and then encrypt
the result"*. Under §2's *"when, and only when, they appear in all capitals"*
that carries no normative force, which is recorded as a finding rather than
smoothed over.
```
8.  Security Considerations

   The security of the CWT relies upon on the protections offered by
   COSE.  Unless the claims in a CWT are protected, an adversary can
   modify, add, or remove claims.

   Since the claims conveyed in a CWT may be used to make authorization
   decisions, it is not only important to protect the CWT in transit but
   also to ensure that the recipient can authenticate the party that
   assembled the claims and created the CWT.  Without trust of the
   recipient in the party that created the CWT, no sensible
   authorization decision can be made.  Furthermore, the creator of the
   CWT needs to carefully evaluate each claim value prior to including
   it in the CWT so that the recipient can be assured of the validity of
   the information provided.

   Syntactically, the signing and encryption operations for Nested CWTs
   may be applied in any order; however, if both signing and encryption
   are necessary, producers normally should sign the message and then
   encrypt the result (thus encrypting the signature).  This prevents
   attacks in which the signature is stripped, leaving just an encrypted
   message, as well as providing privacy for the signer.  Furthermore,
   signatures over encrypted text are not considered valid in many
   jurisdictions.
```

*Source `.cache/rfc-8392.txt` lines 525-548 · `sha256:3c0c5644a0e2d07dba455179cd6bb8e66660e18570f663347f40a0518166d4af`*

## §9 — IANA Considerations

### §9.1 — CBOR Web Token (CWT) Claims Registry

The registry's own procedural rules. **Every force word in this section is
lowercase** — `should be applied`, `must only accept`, `should direct`, `is
suggested`, `should defer` — so a case-insensitive sweep reports a `MUST` at
line 596 and a BCP 14 count reports none: the sentence is *"IANA must only
accept registry updates from the Designated Experts"*, in lower case. Not one
of the document's nine capitalised keywords is in §9. The one range
restriction is the sentence beginning *"Registrations for the limited set of
values"*.
```
9.  IANA Considerations

9.1.  CBOR Web Token (CWT) Claims Registry

   IANA has created the "CBOR Web Token (CWT) Claims" registry
   [IANA.CWT.Claims].

   Registration requests are evaluated using the criteria described in
   the Claim Key instructions in the registration template below after a
   three-week review period on the cwt-reg-review@ietf.org mailing list,
   on the advice of one or more Designated Experts [RFC8126].  However,
   to allow for the allocation of values prior to publication, the
   Designated Experts may approve registration once they are satisfied
   that such a specification will be published.

   Registration requests sent to the mailing list for review should use
   an appropriate subject (e.g., "Request to register claim: example").
   Registration requests that are undetermined for a period longer than
   21 days can be brought to the IESG's attention (using the
   iesg@ietf.org mailing list) for resolution.

   Criteria that should be applied by the Designated Experts includes
   determining whether the proposed registration duplicates existing
   functionality, whether it is likely to be of general applicability or
   whether it is useful only for a single application, and whether the
   registration description is clear.  Registrations for the limited set
   of values between -256 and 255 and strings of length 1 are to be
   restricted to claims with general applicability.

   IANA must only accept registry updates from the Designated Experts
   and should direct all requests for registration to the review mailing
   list.

   It is suggested that multiple Designated Experts be appointed who are
   able to represent the perspectives of different applications using
   this specification in order to enable broadly informed review of
   registration decisions.  In cases where a registration decision could
   be perceived as creating a conflict of interest for a particular
   Expert, that Expert should defer to the judgment of the other
   Experts.

   Since a high degree of overlap is expected between the contents of
   the "CBOR Web Token (CWT) Claims" registry and the "JSON Web Token
   Claims" registry, overlap in the corresponding pools of Designated
   Experts would be useful to help ensure that an appropriate level of
   coordination between the registries is maintained.
```

*Source `.cache/rfc-8392.txt` lines 567-612 · `sha256:0b8822b4e69d447b6129f458e8ee6c3c461ac7988319f6c047f3c19522156772`*

### §9.1.1 — Registration Template

**The four allocation-policy tiers live in the `Claim Key:` field of this
template, not in a table.** `schema/claim-key-policy.derived.yaml` carries them
as data with the CBOR encoding cost of each tier computed from RFC 8949 §3.
```
9.1.1.  Registration Template

   Claim Name:
      The human-readable name requested (e.g., "iss").

   Claim Description:
      Brief description of the claim (e.g., "Issuer").

   JWT Claim Name:
      Claim Name of the equivalent JWT claim, as registered in
      [IANA.JWT.Claims].  CWT claims should normally have a
      corresponding JWT claim.  If a corresponding JWT claim would not
      make sense, the Designated Experts can choose to accept
      registrations for which the JWT Claim Name is listed as "N/A".

   Claim Key:
      CBOR map key for the claim.  Different ranges of values use
      different registration policies [RFC8126].  Integer values from
      -256 to 255 and strings of length 1 are designated as Standards
      Action.  Integer values from -65536 to -257 and from 256 to 65535
      along with strings of length 2 are designated as Specification
      Required.  Integer values greater than 65535 and strings of length
      greater than 2 are designated as Expert Review.  Integer values
      less than -65536 are marked as Private Use.

   Claim Value Type(s):
      CBOR types that can be used for the claim value.

   Change Controller:
      For Standards Track RFCs, list the "IESG".  For others, give the
      name of the responsible party.  Other details (e.g., postal
      address, email address, home page URI) may also be included.

   Specification Document(s):
      Reference to the document or documents that specify the parameter,
      preferably including URIs that can be used to retrieve copies of
      the documents.  An indication of the relevant sections may also be
      included but is not required.
```

*Source `.cache/rfc-8392.txt` lines 623-660 · `sha256:ed86273845fd579e72a465a8e8e0468465b635b80af9db015e944876a14abd03`*

### §9.1.2 — Initial Registry Contents

**Quoted as three regions**: the page breaks at 674-678 and 730-734 fall inside
this list. Region 1 is the `(RESERVED)` entry for key 0; region 2 is `iss`,
`sub`, `aud`, `exp`, `nbf` and `iat`; region 3 is `cti`. Eight entries in all,
one per registered claim key plus the reservation of 0.
```
9.1.2.  Initial Registry Contents

   o  Claim Name: (RESERVED)
   o  Claim Description: This registration reserves the key value 0.
   o  JWT Claim Name: N/A
   o  Claim Key: 0
   o  Claim Value Type(s): N/A
   o  Change Controller: IESG
   o  Specification Document(s): [RFC8392]
```

*Source `.cache/rfc-8392.txt` lines 662-670 · `sha256:a3771c2520df2e445df84d771a03f24f99810a0913da1e5ba2f6a5732eb27cec`*

*Page break at lines 674-678 omitted. The list continues:*

```
   o  Claim Name: iss
   o  Claim Description: Issuer
   o  JWT Claim Name: iss
   o  Claim Key: 1
   o  Claim Value Type(s): text string
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.1 of [RFC8392]

   o  Claim Name: sub
   o  Claim Description: Subject
   o  JWT Claim Name: sub
   o  Claim Key: 2
   o  Claim Value Type(s): text string
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.2 of [RFC8392]

   o  Claim Name: aud
   o  Claim Description: Audience
   o  JWT Claim Name: aud
   o  Claim Key: 3
   o  Claim Value Type(s): text string
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.3 of [RFC8392]

   o  Claim Name: exp
   o  Claim Description: Expiration Time
   o  JWT Claim Name: exp
   o  Claim Key: 4
   o  Claim Value Type(s): integer or floating-point number
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.4 of [RFC8392]

   o  Claim Name: nbf
   o  Claim Description: Not Before
   o  JWT Claim Name: nbf
   o  Claim Key: 5
   o  Claim Value Type(s): integer or floating-point number
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.5 of [RFC8392]

   o  Claim Name: iat
   o  Claim Description: Issued At
   o  JWT Claim Name: iat
   o  Claim Key: 6
   o  Claim Value Type(s): integer or floating-point number
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.6 of [RFC8392]
```

*Source `.cache/rfc-8392.txt` lines 679-725 · `sha256:ec24b45d7c28f8e7f63b325ae98377efac9007df67c2480d1b83040b37f23b88`*

*Page break at lines 730-734 omitted. The list continues:*

```
   o  Claim Name: cti
   o  Claim Description: CWT ID
   o  JWT Claim Name: jti
   o  Claim Key: 7
   o  Claim Value Type(s): byte string
   o  Change Controller: IESG
   o  Specification Document(s): Section 3.1.7 of [RFC8392]
```

*Source `.cache/rfc-8392.txt` lines 735-741 · `sha256:151470ecf2d839b9aad9fb7860a79b58d4afee34902ee4e04c13fcfa7505ffb2`*

### §9.2 — Media Type Registration, and §9.2.1 — Registry Contents
```
9.2.  Media Type Registration

   IANA has registered the "application/cwt" media type in the "Media
   Types" registry [IANA.MediaTypes] in the manner described in RFC 6838
   [RFC6838], which can be used to indicate that the content is a CWT.

9.2.1.  Registry Contents

   o  Type name: application
   o  Subtype name: cwt
   o  Required parameters: N/A
   o  Optional parameters: N/A
   o  Encoding considerations: binary
   o  Security considerations: See the Security Considerations section
      of [RFC8392]
   o  Interoperability considerations: N/A
   o  Published specification: [RFC8392]
   o  Applications that use this media type: IoT applications sending
      security tokens over HTTP(S), CoAP(S), and other transports.
   o  Fragment identifier considerations: N/A
   o  Additional information:

         Magic number(s): N/A
         File extension(s): N/A
         Macintosh file type code(s): N/A

   o  Person & email address to contact for further information:
      IESG, iesg@ietf.org
   o  Intended usage: COMMON
   o  Restrictions on usage: none
   o  Author: Michael B. Jones, mbj@microsoft.com
   o  Change controller: IESG
   o  Provisional registration?  No
```

*Source `.cache/rfc-8392.txt` lines 743-775 · `sha256:c7064257481ad508995232cbc0816f6bd947475b65a63cac2ed9986a78b5530b`*

### §9.3 — CoAP Content-Formats Registration, and §9.3.1 — Registry Contents

**Quoted as two regions**: the page break at 786-790 separates the lead-in from
the registry contents. §9.3.1's `Id: 61` is the first of the two 61s this
document allocates.
```
9.3.  CoAP Content-Formats Registration

   IANA has registered the CoAP Content-Format ID for the "application/
   cwt" media type in the "CoAP Content-Formats" registry
   [IANA.CoAP.Content-Formats].
```

*Source `.cache/rfc-8392.txt` lines 777-781 · `sha256:5d007f1784b78a4d08f56e2ef77400cb3e6b90649b71507c7cbda4e5136b2fbb`*

*Page break at lines 786-790 omitted. The section continues:*

```
9.3.1.  Registry Contents

   o  Media Type: application/cwt
   o  Encoding: -
   o  Id: 61
   o  Reference: [RFC8392]
```

*Source `.cache/rfc-8392.txt` lines 791-796 · `sha256:bdba67b063267ddbd81218398e788034f727e1845060d7b7c10fe1b554ab04e7`*

### §9.4 — CBOR Tag registration, and §9.4.1 — Registry Contents

The second 61: **CBOR Tag 61**, in a different registry, for the same type.
`rfc-9596`'s `design-notes.md` records the linting consequence.
```
9.4.  CBOR Tag registration

   IANA has registered the CWT CBOR tag in the "CBOR Tags" registry
   [IANA.CBOR.Tags].

9.4.1.  Registry Contents

   o  CBOR Tag: 61
   o  Data Item: CBOR Web Token (CWT)
   o  Semantics: CBOR Web Token (CWT), as defined in [RFC8392]
   o  Reference: [RFC8392]
   o  Point of Contact: Michael B.  Jones, mbj@microsoft.com
```

*Source `.cache/rfc-8392.txt` lines 798-809 · `sha256:c0a919303c060377886f707b60440709047bfc225d5292bd6e817efe42f5f0f8`*

## Appendix A — Examples

The lead-in is kept here because its second paragraph **defines a notation**
the rest of the appendix depends on, and because its first paragraph is the
document's own statement that the appendix is a worked set rather than
illustrative fragments. The figures themselves are in
`examples/vectors.yaml`, byte for byte, with the expected result of every
cryptographic operation over them.
```
Appendix A.  Examples

   This appendix includes a set of CWT examples that show how the CWT
   Claims Set can be protected.  There are examples that are signed,
   MACed, encrypted, and that use nested signing and encryption.  To
   make the examples easier to read, they are presented both as hex
   strings and in the extended CBOR diagnostic notation described in
   Section 6 of [RFC7049].

   Where a byte string is to carry an embedded CBOR-encoded item, the
   diagnostic notation for this CBOR data item can be enclosed in '<<'
   and '>>' to notate the byte string resulting from encoding the data
   item, e.g., h'63666F6F' translates to <<"foo">>.
```

*Source `.cache/rfc-8392.txt` lines 903-915 · `sha256:b37de625b35050097db89036b904b9d90c2febaa35adde0f3cf8ce195e74d3a9`*

### A.1 — Example CWT Claims Set

The one sentence of A.1 that is a rule rather than a figure caption:
```
   The CWT Claims Set used for the different examples displays usage of
   all the defined claims.  For signed and MACed examples, the CWT
   Claims Set is the CBOR encoding as a byte string.
```

*Source `.cache/rfc-8392.txt` lines 919-921 · `sha256:4770f3caeb6f1d11c7752d5f99e8bc7391be0866c7bc64e58d15511768e06cbf`*

### A.2 — Example Keys

The sentence that makes every subsequent hex block a joined run rather than a
multi-line value:
```
   This section contains the keys used to sign, MAC, and encrypt the
   messages in this appendix.  Line breaks are for display purposes
   only.
```

*Source `.cache/rfc-8392.txt` lines 943-945 · `sha256:bc7a91c728f3fa19fe53886d2f29248e7bd02d16389b5d5f220c0d7b2a2ce4be`*

---

## Three observations about this document's normative shape

Recorded here because they are facts about the text, not analysis, and because
each one changes what `requirements.yaml` could honestly contain.

**1. Nine keywords, and eight of the nine delegate or forbid rather than
require.** The census: tag-1 omission (§2), ignore-unknown-claims (§3), the
no-CBOR-tag prohibition on claim values (§5), the tag-pairing rule (§6), COSE
Header validity (§7.1 step 3), the three "all steps specified in [RFC8152]
... MUST be followed" bullets (§7.1 step 4), and the rejection rule (§7.2
preamble). **Not one of the nine fixes a claim key, a claim type, or a claim
that must be present.** Those live in §3.1.x's prose, §4's table and §9.1.2's
registry entries, which carry no keyword at all. That is why 10 of the
requirement entries are `kind: stated` against 9 keywords — one sentence,
§7.1 step 4, is a compound carrying three keywords in three separately
testable bullets — and why the great majority are `kind: inferred` with
`field` naming the phrase that carries the force.

**2. The strongest security sentence in the document is lowercase.** §8's
sign-then-encrypt guidance (*"producers normally should sign the message and
then encrypt the result (thus encrypting the signature)"*) is the one piece of
advice in RFC 8392 that prevents an attack it names — signature stripping —
and §2 restricts normative interpretation to keywords *"when, and only when,
they appear in all capitals, as shown here."* So it binds nobody.

**3. The document's two procedures are the only ordered content in it, and
both have a loop.** §7.1 step 5 says *"return to Step 3"* and §7.2 step 6 says
*"return to Step 1"*; both are the nested-CWT case. That loop, plus §7.2's
single rejection condition, is the whole of the state content — see
`state-machine.yaml`, which is **applicable** for this record and models
exactly that and nothing more.
