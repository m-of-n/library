---
record: rfc-9597
kind: normative
title: "rfc-9597 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9597 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9597, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing is paraphrased and nothing is retyped:
each fenced block was lifted from `.cache/rfc-9597.txt` by line range by
script. Prose outside the fences is this extraction's.

| | |
|---|---|
| **Source** | `.cache/rfc-9597.txt`, 265 newline-delimited lines |
| **Digest** | `b6baaec655bc86606602a6f6e93f0103db6e6f98460f1e43437e74a6a5e02bdd` |
| **BCP 14 keywords** | **8** — 2 MUST, 1 MUST NOT, 2 RECOMMENDED, 3 MAY; `bin/bcp14-count`, boilerplate excluded |
| **Page decoration** | **none.** This is an unpaginated RFC v3 rendering with **zero form feeds** and no running footers, so no region here removes anything |

**Region convention.** Each digest is the sha256 of the region's lines joined by
`\n` with no trailing newline.

**The whole document is quoted below except the references, the
acknowledgements and the authors' addresses.** At 265 lines it is the smallest
record in library#39 Tier 2's CWT lane, and everything load-bearing is in §1
and §2: **all 8 BCP 14 keywords are in those two sections**, 4 in each.

---

## §1 — Introduction

**§1 is normative, not background**, and that is the first thing to know about
this document: it contains 4 of the 8 keywords, including the one `MUST NOT`.
Quoted in four parts, one per paragraph, because each paragraph does different
work.

### The three cases the parameter exists for
```
   In some applications of COSE, it is useful to have a standard
   representation of CWT claims [RFC8392] available in the header
   parameters.  These include encrypted COSE structures, which may or
   may not be an encrypted CWT, and/or those featuring a detached
   signature.  Another use case is using CWT claims with payloads that
   are not CWT Claims Sets, including payloads that are not CBOR at all.
   For instance, an application might want to include an "iss" (issuer)
   claim in a COSE_Sign1 structure when the payload being signed is a
   non-CBOR data structure, such as a bitmap image, and the issuer value
   is used for key discovery.
```

*Source `.cache/rfc-9597.txt` lines 71-80 · `sha256:3cf264414d157659dd57f9240a2c40f42f6072125f7fec27aa5f500c1ecaff50`*

### The JOSE precedent, and the gap this document says it closes
```
   Section 5.3 of [RFC7519], "JSON Web Token (JWT)", defined a similar
   mechanism for expressing selected JWT-based claims as JSON Object
   Signing and Encryption (JOSE) header parameters.  This JWT feature
   was motivated by the desire to have certain claims, such as the
   Issuer value, be visible to software processing the JWT, even though
   the JWT is encrypted.  No corresponding feature was standardized for
   CWTs, which was an omission that this specification corrects.
```

*Source `.cache/rfc-9597.txt` lines 82-88 · `sha256:3d139b0e8057cd7a1a951fa8059acb38c1802342191f458aa3435d52e05d68b6`*

### Why it is ONE parameter holding a nested map — a label collision

The document's own rationale, and the strongest piece of field evidence for
`R-M-12` in this lane.
```
   Directly including CWT claim values as COSE header parameter values
   would not work, since there are conflicts between the numeric header
   parameter assignments and the numeric CWT claim assignments.
   Instead, this specification defines a single header parameter
   registered in the IANA "COSE Header Parameters" registry that creates
   a location to store CWT claims in a COSE header parameter.
```

*Source `.cache/rfc-9597.txt` lines 90-95 · `sha256:996278425d4cf5bc75a67ba8ea554ac0b52765f7458aade4a64c7763e99cdc63`*

### The interpretation paragraph — 4 of the 8 keywords, including the MUST NOT

This paragraph carries `MAY` (line 102), `RECOMMENDED` (105), `MAY` (107) and
`MUST NOT` (108). It is the whole of the document's answer to "how does a
recipient know what these claims mean", and the answer is placed on the
recipient.
```
   This specification does not define how to use CWT claims and their
   semantics for particular applications, whether they are in the COSE
   payload or the CWT Claims header parameter, or both.  Therefore,
   understanding how to process the CWT Claims header parameter requires
   unambiguously knowing the intended interpretation.  The necessary
   information about this MAY come from other header parameters.  Unless
   there already is a natural way of providing this information at an
   appropriate level of integrity protection and authentication, a
   RECOMMENDED way to include this information in the COSE structure is
   use of the "typ" (type) Header Parameter [RFC9596].  Other methods
   for determining the intended interpretation MAY also be used.
   Recipients of the CWT Claims header parameter MUST NOT use the
   information in the CWT Claims header parameter beyond the integrity
   protection or authentication afforded to the CWT Claims header and
   the information used to derive its intended interpretation.
```

*Source `.cache/rfc-9597.txt` lines 97-111 · `sha256:e075226068e8cfb87af8b1814ace7fe90c4ac7d817c1823a89809e5a3c891d45`*

## §1.1 — Requirements Terminology

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing. `bin/validate` recounts the
requirement texts with boilerplate stripping **off**, so an entry carrying this
paragraph would add 11 phantom keywords against a source count of 8.
```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-9597.txt` lines 115-119 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*

## §2 — Representation

### The lead-in and Table 1 — the registration itself
```
   This document defines the following COSE header parameter:

   +========+=======+=======+==============+===============+===========+
   | Name   | Label | Value | Value        | Description   | Reference |
   |        |       | Type  | Registry     |               |           |
   +========+=======+=======+==============+===============+===========+
   | CWT    | 15    | map   | map keys in  | Location      | Section 2 |
   | Claims |       |       | [CWT.Claims] | for CWT       | of RFC    |
   |        |       |       |              | Claims in     | 9597      |
   |        |       |       |              | COSE Header   |           |
   |        |       |       |              | Parameters    |           |
   +--------+-------+-------+--------------+---------------+-----------+

                                  Table 1
```

*Source `.cache/rfc-9597.txt` lines 123-136 · `sha256:99b7d80343a03a6839553f6bce9b24548af0659386d669b55e5c4fcababa33ee`*

### The CDDL, and the source's own declaration that it is non-normative

**The document says this itself**, which is why `schema/` carries the fragment
as verbatim and marks it `non_normative: true` rather than treating it as a
constraint.
```
   The following is a non-normative description for the value type of
   the CWT claim header parameter using CDDL [RFC8610].

   CWT-Claims = {
    * Claim-Label => any
   }

   Claim-Label = int / text
```

*Source `.cache/rfc-9597.txt` lines 138-145 · `sha256:46dd790f24c88511122028b20e3173824106f96466ff48570134d29522f3397b`*

### The duplication rule — one of the two MUSTs, with two escape hatches
```
   In cases where CWT claims are present both in the payload and the
   header of a CWT, an application receiving such a structure MUST
   verify that their values are identical, unless the application
   defines other specific processing rules for these claims.
```

*Source `.cache/rfc-9597.txt` lines 147-150 · `sha256:e5676797c531597b7bcfb54a18ddc7bede1480c7d1fbb0d4643223c0dc8979ac`*

### Placement — a RECOMMENDED and a MUST, and the MUST is weaker than it reads

Note what the `MUST` forbids: label 15 appearing in **both** buckets. It
expressly permits it appearing in the **unprotected** one.
```
   It is RECOMMENDED that the CWT Claims header parameter only be used
   in a protected header to avoid the contents being malleable.  The
   header parameter MUST only occur once in either the protected or
   unprotected header of a COSE structure.
```

*Source `.cache/rfc-9597.txt` lines 152-155 · `sha256:33cc87cba69ed35061306a3897b43a37ab58afb42f0b7cd72e264db2b95a4456`*

### Scope — the parameter is not restricted to CWTs
```
   The CWT Claims header parameter MAY be used in any COSE object using
   header parameters, such as COSE_Sign objects.  Its use is not
   restricted to CWTs.
```

*Source `.cache/rfc-9597.txt` lines 157-159 · `sha256:88e294f9ca906ae8e1f609baa1ac8292d8fccf12c54020f3905fa30dd88e5461`*

## §3 — Privacy Considerations

**Zero capitalised keywords.** The one force word is the lowercase *"should
ensure"*, and the first clause is a statement of fact that is structural rather
than incidental.
```
   Some of the registered CWT claims may contain privacy-sensitive
   information.  Since CWT claims in COSE headers are not encrypted,
   when privacy-sensitive information is present in these claims,
   applications and protocols using them should ensure that these COSE
   objects are only made visible to parties for which it is appropriate
   for them to have access to this sensitive information.
```

*Source `.cache/rfc-9597.txt` lines 163-168 · `sha256:20e39ac7141df675e457f39dd3162c83ac2ae0e296f6de85c28784df3620bf85`*

## §4 — Security Considerations

**Zero capitalised keywords**, in four paragraphs, one of which is the
document's most important instruction to an implementer.
```
   Implementers should also review the security considerations for CWT,
   which are documented in Section 8 of [RFC8392].
```

*Source `.cache/rfc-9597.txt` lines 172-173 · `sha256:7d7b916b54f66d5b6279fb1214eb9382ef9e0804a5305be67605d013c3e925a9`*

### Detached content
```
   As described in [RFC9052], if the COSE payload is transported
   separately ("detached content"), then it is the responsibility of the
   application to ensure that it will be transported without changes.
```

*Source `.cache/rfc-9597.txt` lines 175-177 · `sha256:115d6d7e8a6faa6c59fb1cb2f2a84145aac1068942b95fdb0d069aa933b7c821`*

### The rationale for the duplication rule
```
   The reason for applications to verify that CWT claims present in both
   the payload and the header of a CWT are identical, unless they define
   other specific processing rules for these claims, is to eliminate
   potential confusion that might arise by having different values for
   the same claim, which could result in inconsistent processing of such
   claims.
```

*Source `.cache/rfc-9597.txt` lines 179-184 · `sha256:562419d4c97868b6b97f4f24358c7c2b05207db7c922ae999fcebd929dd37837`*

### The instruction that carries no force — lowercase `must ensure`
```
   Processing information in claims prior to validating that their
   integrity is cryptographically secure can pose security risks.  This
   is true whether the claims are in the payload or a header parameter.
   Implementers must ensure that any tentative decisions made based on
   previously unverified information are confirmed once the
   cryptographic processing has been completed.  This includes any
   information that was used to derive the intended interpretation of
   the CWT claims parameter.
```

*Source `.cache/rfc-9597.txt` lines 186-193 · `sha256:dc3d651bd7c9397840fe9eea4606464027c2125eaa887cdc0725d5a59edd44b1`*

## §5 — IANA Considerations
```
   IANA has registered the new COSE header parameter "CWT Claims"
   defined in Table 1 in the "COSE Header Parameters" registry
   [COSE.HeaderParameters].
```

*Source `.cache/rfc-9597.txt` lines 197-199 · `sha256:2641efb9babbbebdfe379ef18eb3694de65ace353919ffe6afbf643c7a950875`*

---

## Three observations about this document's normative shape

Facts about the text, not analysis, and each one changes what
`requirements.yaml` could honestly contain.

**1. All 8 keywords are in §1 and §2, 4 in each, and §3, §4 and §5 have
none.** Counted from the source: `MAY` at line 102, `RECOMMENDED` at 105, `MAY`
at 107 and `MUST NOT` at 108 in §1; `MUST` at 148, `RECOMMENDED` at 152, `MUST`
at 154 and `MAY` at 157 in §2.

**2. So the document's most important security instruction carries no normative
force under its own terms.** §4's *"Implementers must ensure that any tentative
decisions made based on previously unverified information are confirmed once the
cryptographic processing has been completed"* is lowercase, and §1.1 restricts
interpretation to keywords *"when, and only when, they appear in all capitals,
as shown here."* In a document whose entire purpose is to make claims readable
**before** verification, the rule against acting on unverified claims is
advice. §3's privacy guidance is in the same position.

**3. The only structural description of the value is declared non-normative by
the document itself**, in the sentence immediately before it. So `CWT-Claims = {
* Claim-Label => any }` with `Claim-Label = int / text` constrains nothing: the
**empty map `{}`** is admitted, `*` permits zero entries, and no normative
sentence forbids a float, boolean or byte-string claim label. Table 1's Value
Type column says `map` and nothing narrows it with force.
