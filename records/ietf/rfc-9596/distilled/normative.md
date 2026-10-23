---
record: rfc-9596
kind: normative
title: "rfc-9596 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9596 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9596, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing is paraphrased and nothing is retyped:
each fenced block was lifted from `.cache/rfc-9596.txt` by line range by
script.

| | |
|---|---|
| **Source** | `.cache/rfc-9596.txt`, 232 newline-delimited lines |
| **Digest** | `4beb37fe8cb3eec78cec2445c65dcf2db4866ba99a72e7b1e54e23e5bfa69b5e` |
| **BCP 14 keywords** | **3** — 1 OPTIONAL, 1 MAY, 1 MUST NOT; **no MUST, SHOULD, SHALL or RECOMMENDED at all** |
| **Page decoration** | **none.** Unpaginated RFC v3 rendering, **zero form feeds** |

**Region convention.** Each digest is the sha256 of the region's lines joined by
`\n` with no trailing newline.

**THE CENTRAL FACT ABOUT THIS DOCUMENT'S NORMATIVE SHAPE, AND IT IS A
COUNT.** Its body contains **three** capitalised BCP 14 keywords, all three in
§2, and **not one MUST, SHOULD, SHALL or RECOMMENDED**: `OPTIONAL` at line 112,
`MAY` at line 119 and `MUST NOT` at line 130. §1, §3, §4 and §5 contain none.
So **a conformant implementation of RFC 9596 performs no check whatsoever** —
§3's two reject rules are lowercase and §2 tells libraries to ignore the
parameter. Everything below is quoted so that claim can be tested against the
text rather than taken on trust.

---

## §1 — Introduction

The gap, and the argument imported from JOSE. **No capitalised keyword.**
```
   CBOR Object Signing and Encryption (COSE) [RFC9052] defines header
   parameters that parallel many of those defined by the JSON Object
   Signing and Encryption (JOSE) specifications [RFC7515] [RFC7516].
   However, one way in which COSE does not provide equivalent
   functionality to JOSE is that it does not define an equivalent of the
   "typ" (type) header parameter, which is used for declaring the type
   of the entire JOSE data structure.  The security benefits of having
   "typ" (type) are described in Section 3.11 of [RFC8725], which
   recommends its use for "explicit typing" -- using "typ" values to
   distinguish between different kinds of JSON Web Tokens (JWTs)
   [RFC7519].
```

*Source `.cache/rfc-9596.txt` lines 69-79 · `sha256:7cbd97a86e6848edcd519c4e663a2a0ad94d72411bc84aa820a64606dea38c58`*

### What this specification adds, and the value space it borrows

**The syntax decision is here, not in §2**, and it is the sentence `R-M-12` has
most to say about: both value spaces are global IANA registries.
```
   This specification adds the equivalent of the JOSE "typ" (type)
   header parameter to COSE so that the benefits of explicit typing can
   be brought to COSE objects.  The syntax of the COSE type header
   parameter value is the same as the existing COSE content type header
   parameter, allowing both unsigned integers as registered in the "CoAP
   Content-Formats" registry [CoAP.ContentFormats] and string media type
   values [MediaTypes] to be used.
```

*Source `.cache/rfc-9596.txt` lines 81-87 · `sha256:01057add0ff3aa713e273c89f2ca055a522b4eabf34a08ec1e427d5dcb43a81c`*

**And it is stated a third time, in the abstract, which this file deliberately
does not cover.** Lines 16-22 carry *"The syntax of the COSE type header
parameter value is the same as the existing COSE content type header
parameter."* — the first 110 characters of `requirements.yaml` R-0004's text
occur at **line 20** as well as at line 83, and line 20 is the first of the
three occurrences of the word `syntax` that `schema/README.md` counts. Every
region in this file lies between lines 69 and 164: an RFC abstract is not
normative text, so it is excluded on purpose, but the exclusion is now stated
rather than implied. **[added 2026-10-21, pass 3 — cross-check]** — the pass
that found `record.yaml` and `README.md` both describing these regions as
covering *the whole document except the references, the acknowledgements and
the authors' addresses*, which left the front matter, lines 1-65, unaccounted
for.

### The term "COSE object"
```
   The term "COSE object" is used as defined in [RFC9052].  An example
   of a COSE object is a COSE_Sign1 structure, as described in
   Section 4.2 of [RFC9052].
```

*Source `.cache/rfc-9596.txt` lines 89-91 · `sha256:b20603f0152c2f8deab1715c9ba606f16e4479808e6c98333dc8a6775bd80b33`*

## §1.1 — Requirements Notation and Conventions

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing. `bin/validate` recounts the
requirement texts with boilerplate stripping **off**, so an entry carrying this
paragraph would add 11 phantom keywords against a source count of 3.

**And it is the sentence that disarms §3.** *"when, and only when, they appear
in all capitals"* is why §3's two reject rules carry no force.
```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-9596.txt` lines 95-99 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*

## §2 — COSE "typ" (type) Header Parameter

**All three of the document's keywords are in this section.**

### What `typ` declares, and the line between it and content type
```
   The "typ" (type) header parameter is used by COSE applications to
   declare the type of this complete COSE object, as compared to the
   content type header parameter, which declares the type of the COSE
   object payload.  This is intended for use by the application when
   more than one kind of COSE object could be present in an application
   data structure that can contain a COSE object; the application can
   use this value to disambiguate among the different kinds of COSE
   objects that might be present.  It will typically not be used by
   applications when the kind of COSE object is already known.  Use of
   this header parameter is OPTIONAL.
```

*Source `.cache/rfc-9596.txt` lines 103-112 · `sha256:1df83610047f606e958f7db6737b9f26204ec3c8dbe84f268c45813150704467`*

### The value space — one `MAY`, and two global registries
```
   The syntax of this header parameter value is the same as the content
   type header parameter defined in Section 3.1 of [RFC9052]; it is
   either an unsigned integer as registered in the "CoAP Content-
   Formats" registry [CoAP.ContentFormats] or a string content type
   value.  Content type values have a media type name [MediaTypes] and
   MAY include media type parameters.
```

*Source `.cache/rfc-9596.txt` lines 114-119 · `sha256:196602347f8d04cc4689647c6daa3c79d78535060fe6d8154ceb08223894afe6`*

### What implementations do with it: nothing

**This is the sentence that explains why no implementation of label 16 can be
found.** It is not a gap in the ecosystem; it is the specification's
instruction.
```
   The "typ" (type) header parameter is ignored by COSE implementations
   (libraries implementing [RFC9052] and this specification), other than
   being passed through to applications using those implementations.
   Any processing of this parameter is performed by the COSE application
   using application-specific processing rules.  For instance, an
   application might verify that the "typ" value is a particular
   application-chosen media type and reject the data structure if it is
   not.
```

*Source `.cache/rfc-9596.txt` lines 121-128 · `sha256:0ab98363ce48cdbe3ed59504bb2f49938498b4d2f28fdd94d8706cad387b12eb`*

### The one MUST NOT — and it is what makes `typ` authenticated
```
   The "typ" parameter MUST NOT be present in unprotected headers.
```

*Source `.cache/rfc-9596.txt` lines 130-130 · `sha256:00600fd99b8108546fef3f32a62cfebdf5855817cf433870b8ed43d5af941543`*

### What `typ` does not describe

Two sentences, no keyword, and together they are the asymmetry with `rfc-9597`
§2 that `design-notes.md` §4 is about.
```
   The "typ" parameter does not describe the content of unprotected
   headers.  Changes to unprotected headers do not change the type of
   the COSE object.
```

*Source `.cache/rfc-9596.txt` lines 132-134 · `sha256:b5e640a9460db5758ebea2877e05cedec5c6e4e9d5dea4c5797b70701963be95`*

## §3 — Security Considerations

**Zero capitalised keywords, and the whole enforcement side of the mechanism is
here.** Both reject rules are lowercase `should`.
```
   The case for explicit typing of COSE objects is equivalent to the
   case made for explicit typing in Section 3.11 of [RFC8725]: Explicit
   typing can prevent confusion between different kinds of COSE objects.

   COSE applications employing explicit typing should reject COSE
   objects with a type header parameter value different than values that
   they expect in that application context.  They should also reject
   COSE objects without a type header parameter when one is expected.
```

*Source `.cache/rfc-9596.txt` lines 138-145 · `sha256:d9ab9ebcdd5d04dbff8b96059274b093de637822171667f15189690b30b1037c`*

## §4 — IANA Considerations, and §4.1 — the registration

Table 1 in full, with its caption.
```
   IANA has registered the following value in the IANA "COSE Header
   Parameters" registry [COSE.HeaderParameters].

    +======+=====+======+=======================+===========+=========+
    |Name  |Label|Value | Value Registry        |Description|Reference|
    |      |     |Type  |                       |           |         |
    +======+=====+======+=======================+===========+=========+
    |typ   |16   |uint /| [CoAP.ContentFormats] |Content    |Section 2|
    |(type)|     |tstr  | or [MediaTypes]       |type of the|of RFC   |
    |      |     |      | registry              |complete   |9596     |
    |      |     |      |                       |COSE object|         |
    +------+-----+------+-----------------------+-----------+---------+

                                  Table 1
```

*Source `.cache/rfc-9596.txt` lines 151-164 · `sha256:c8e0a583e81aefdb2f12e26f71a6ef8887feccb3dc7a8dc584a0c6059d339590`*

---

## Four observations about this document's normative shape

Facts about the text, not analysis, and each one changes what
`requirements.yaml` could honestly contain.

**1. Three keywords, and not one of them requires anything.** `OPTIONAL`
(line 112) makes the parameter's use optional; `MAY` (119) permits media type
parameters; `MUST NOT` (130) forbids unprotected placement. **There is no MUST,
no SHOULD, no SHALL and no RECOMMENDED anywhere in the document.** So the only
obligation RFC 9596 imposes on anybody is a prohibition on where the parameter
may sit — and that prohibition is what makes the parameter useful, because it
forces `typ` inside `Sig_structure`.

**2. The enforcement side is lowercase, and the library layer is told to stand
down.** §3: *"COSE applications employing explicit typing should reject COSE
objects with a type header parameter value different than values that they
expect in that application context. They should also reject COSE objects
without a type header parameter when one is expected."* Both lowercase. And §2:
*"The "typ" (type) header parameter is ignored by COSE implementations
(libraries implementing [RFC9052] and this specification), other than being
passed through to applications using those implementations."* **A conformant
implementation of RFC 9596 performs no check whatsoever**, and that is the
document's design rather than an oversight.

**3. The document ships no grammar and no example.** `CDDL`, `ABNF`, `ASN.1`
and `JSON Schema` occur **zero** times; `Figure`, `hex`, `vector` and
`diagnostic notation` occur **zero** times; `example` occurs **once**, at line
89, and it is a definition rather than a fixture — *"An example of a COSE
object is a COSE_Sign1 structure, as described in Section 4.2 of [RFC9052]."*
Table 1 and §2's prose are the whole of the document's formal account of
itself.

**4. The word `tag` does not appear in this document at all.** Neither `tag`
nor `tags` occurs anywhere in its 232 lines. The argument that `typ` is the
in-band, authenticated replacement for the CBOR tag MD-3 removes is therefore
**entirely ours**, assembled from §2's `MUST NOT`, RFC 9052 §4.4's
`Sig_structure` and RFC 8392 §7.1/§7.2's step order — and
`design-notes.md` marks it `[analysis]` for that reason.
