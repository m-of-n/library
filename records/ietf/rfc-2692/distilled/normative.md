---
record: rfc-2692
kind: normative
title: "rfc-2692 — normative statements"
extracted: "2026-10-18"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of RFC 2692
     (SPKI Requirements), VERBATIM, with its locator, in source order.
     Verbatim source only: no analysis, no paraphrase, no opinion. Blockquotes
     and fenced blocks delimit verbatim text; everything outside them is
     structure (headings, locators, labels) only. -->

Source: RFC 2692, "SPKI Requirements", C. Ellison, September 1999. Network
Working Group, Category: Experimental. 787 lines, sha256
`6a88c1563590e8094bb37cda5c5d29ef70f8384e5a3a0528bce29c501826976d`.

## How to read this file

**Verbatim containers.** Two are used, and the distinction matters:

- A **blockquote** (`>`) reproduces running prose. The source's own line breaks
  are kept and its leading three-space RFC indent is removed; no word, spelling
  or punctuation mark is altered, the source's own typos included.
- A **fenced block** (```` ``` ````) reproduces the source's lines byte-exactly,
  indentation included. Every item of the List of Certificate Uses (with any
  indented commentary beneath it) and every Open Question (with its indented
  answer) is fenced, so whitespace-significant nesting is never rewrapped.

Everything outside a quote or a fence — headings, statement numbers,
locators, flags, and the italic notes — is structure added by this
extraction, not source text. No two non-adjacent passages are ever spliced
into one entry: each entry is a single contiguous run of source lines.

**Locators.** The source's headings are unnumbered. Each locator is `§` plus
the heading exactly as it appears in the body (and in the Table of Contents),
then a position within it:

- `¶n` — the *n*th paragraph of that section, counting every paragraph,
  reproduced or not (so `§Background ¶2` is the second paragraph of
  Background; ¶1 is not reproduced);
- `#n` — the *n*th bulleted use in the List of Certificate Uses, numbered
  1–62 in source order over the bullets at the list's own indent (six
  spaces); `#7a`–`#7c` are the three nested bullets under #7 (nine spaces);
- `OR-n` — the *n*th of the six nine-space bullets after the label
  `Other requirements:` (see that subsection);
- `Qn` — the *n*th of the four bulleted questions in Open Questions, each
  with its indented answer.

The source's flat numbering is the source's own: the wallet cards that follow
#15 (`There are a number of cards one carries in a typical wallet ...`) are
printed at the same indent as every other use, not nested under #15, and the
source does not mark where that sub-list ends. This file does not decide it;
#16 onwards are numbered as the source prints them.

**Page breaks.** The source is the paginated plain-text RFC. Four entries run
across a page boundary — N-014 (§General Requirements ¶9), N-020
(§Implementation of Certificates ¶1), N-037 (§List of Certificate Uses #7c)
and N-083 (§List of Certificate Uses #53) — and each is flagged
`_[page break removed]_`. In those entries, and only those, the page furniture
is deleted: the footer line (`Ellison` … `Experimental` … `[Page n]`), the
form-feed line, the running header (`RFC 2692` … `SPKI Requirements` …
`September 1999`) and the blank padding lines around them. Nothing else is
touched. In the first three the boundary falls mid-sentence and the two
halves are joined directly. In N-083 it falls between the two paragraphs of
the bracketed commentary (`... long term key.` / `I'll note here ...`), and
one of the source's own blank lines is left in place, as at every other
paragraph boundary in the source. Every other entry lies wholly within one
page.

**BCP 14 keyword census: 0.** RFC 2692 contains no capitalised BCP 14 keyword
anywhere: no `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`,
`SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY` or `OPTIONAL`. It neither
cites RFC 2119 nor carries the BCP 14 boilerplate, and RFC 8174's rule that
only capitals are keywords postdates it. Verified with
`bin/bcp14-count .cache/rfc-2692.txt --by-keyword`, which returns `0`, and with
an independent case-sensitive grep whose only hits are the two `NOT`s in the
Full Copyright Statement's warranty disclaimer (`BUT NOT LIMITED TO`,
`WILL NOT INFRINGE`), which are not BCP 14 usage. The two capitalised-initial
`May`s are not keywords either: the sentence-initial `May involve goals` of
N-098 and the month in [KOHN] (References).

**What counts as normative here.** RFC 2692 is a requirements document: its
binding content is the lowercase prose that says what SPKI certificates, and
the processing around them, must, should or may do. An entry is included
when it does at least one of these:

- states a requirement on SPKI certificates, their structure, encoding,
  issuance, distribution, validity or revocation — every paragraph of
  General Requirements, Validity and CRLs, and Implementation of
  Certificates, and the six `Other requirements`;
- defines a term the requirements use: KEYHOLDER (N-006), the negative and
  positive statement of N-017;
- states a goal of the working group that is a requirement on the design:
  the Abstract's "as easy, simple and extensible a way as possible" (N-001)
  and the Charter's "are to be simple to understand, implement, and use" and
  "will support a range of trust models" (N-003, N-004);
- records a decision or finding that fixes the design: that <name,key>
  bindings are of extremely limited use for trust management and a
  certificate user needs to know about authorization (N-005), the assumption
  of direct distribution by the keyholder (N-010);
- is a **use** in the List of Certificate Uses. The source says the
  requirements were summarised from this list (N-002), that the envisioned
  certificates are "needed to meet the demands of the list given at the end
  of this document" (N-020), and points to "the list of needs in this
  document" (N-005). Each use is therefore reproduced as a use case the
  design must serve — not as an obligation in its own words. A use phrased
  as a question (#9, #10, #12–#14) is still a use. Indented commentary under
  a use (#50, #53, #54, #56) is kept with it, as it is part of the same
  contiguous run; its lowercase modals are the commentators', not SPKI
  rules (the "should" of #53 is inside a quoted certificate statement);
- marks a scope boundary or security limitation of the design: each Open
  Question is reproduced with its answer, because the answers state what
  certificate definition does not and cannot do (protect or prove the
  protection of a private key, build a title database, determine a negative
  fact, prevent key loaning). None of them states a requirement on SPKI; the
  questions are kept as the referents of the answers;
- scopes how the rest is to be read: the Abstract's account of how the
  requirements were derived (N-002), the brainstorming status of the use
  list (N-027), the premise of the Open Questions (N-099), and Security
  Considerations, whose one sentence places the security content throughout
  the memo (N-104).

When in doubt about an obligation-bearing sentence, it is included. Not
reproduced: the front and back matter (Status of this Memo, Copyright Notice,
Table of Contents, References, Author's Address, Full Copyright Statement,
Acknowledgement) and, inside sections that do yield entries, exactly these
paragraphs, so that every omission is a recorded decision rather than a
drop:

- Charter of the SPKI working group ¶1: motivation (Internet protocols that
  already require a public key infrastructure);
- Background ¶1: history (Kohnfelder's thesis, Diffie and Hellman's public
  directory, the 1978-onward meaning of "certificate").

Where history sits inside a paragraph that also carries a requirement or
definition, the whole paragraph is reproduced, since an entry is never cut
mid-paragraph: so §Validity and CRLs ¶2 keeps its description of the minimal
CRL (the referent of the requirement it states), and ¶3 its retail analogy
(the source of the "positive" and "negative" of ¶4).

**Lowercase modal accounting.** Over the whole source, case-sensitively,
`must`, `should`, `may`, `shall`, `required`, `recommended` and `optional`
occur 45 times; `shall` and `recommended` never occur. 40 lie inside
entries; the other 5 are in the Full Copyright Statement (lines 739, 741,
745: `may`; 749: `must`; 750: `required`) and are excluded as boilerplate.
Counted mechanically over the verbatim text of the entries:

- *must* 8 times in 5 entries (N-013, N-014, N-016, N-019, N-093);
- *should* 25 times in 15 entries (N-009, N-011, N-014, N-015, N-018, N-020, N-021, N-022, N-023, N-024, N-025, N-026, N-038, N-080, N-083);
- *may* 5 times in 5 entries (N-008, N-015, N-095, N-096, N-097), and sentence-initial *May* once in 1 entry (N-098);
- *required* once in 1 entry (N-023);
- *optional* once in 1 entry (N-021).

None of these is a BCP 14 keyword. The softer obligation words follow the same
rule: every `require(s)`, `need(s)`, `necessary` and `is/are to` in the body
lies inside an entry except Charter ¶1's `require` (line 66) and
Background ¶1's `needs` (line 91), excluded with their paragraphs, and the
Full Copyright Statement's `needed` (line 747).

**The `_[lowercase/implied]_` marker.** In the library's other normative
extractions the marker flags an entry that carries binding content but no
BCP 14 keyword of its own. Here the census is zero, so **every entry carries
the marker**. It distinguishes nothing within this file; it is kept so that
the convention reads the same way across the library.

**Source text kept as printed.** These are the source's own and are not
corrected: `singing someone else's key` (#7c, for *signing*); `I'm the a
purchasing agent` and `posses` (#52); `owner of a this DNS name` (#55); the
closing quotation mark of #56 placed after its bracketed aside
(`certificate]."`); the two-dot opening of #14 (`..a digital Voter
Registration Card?`); the verbless OR-6 (`Reliable distribution of key
revocations ...`); and the bracket of #53 that opens at `[This is desirable`
and closes at `private key.].`. The `[Note: SPKI and SDSI have merged.]` at
the end of N-014 is the source's own editorial note.

**Citations.** The one bracketed citation inside the captured text,
`[SPKI]` (N-001), has no entry in the source's References section, which
lists only [DH] and [KOHN] (both cited in the excluded Background ¶1) and is
not reproduced.

**Counts.** 104 entries, `N-001` to `N-104`, in source order: Abstract 2;
Charter of the SPKI working group 2; Background 1; General Requirements 9;
Validity and CRLs 5; Implementation of Certificates 7; List of Certificate
Uses 72 (the introductory paragraph, uses #1–#62, the nested #7a–#7c, and
OR-1 to OR-6); Open Questions 5; Security Considerations 1. The other seven
headed parts (Status of this Memo, Copyright Notice, Table of Contents,
References, Author's Address, Full Copyright Statement, Acknowledgement)
yield no entry and say so in place.


## Status of this Memo

_No entries — publication status boilerplate (Experimental; distribution unlimited)._



## Copyright Notice

_No entries — copyright boilerplate._



## Abstract

**N-001.** (§Abstract ¶1) _[lowercase/implied]_

> The IETF Simple Public Key Infrastructure [SPKI] Working Group is
> tasked with producing a certificate structure and operating procedure
> to meet the needs of the Internet community for trust management in
> as easy, simple and extensible a way as possible.

**N-002.** (§Abstract ¶2) _[lowercase/implied]_

> The SPKI Working Group first established a list of things one might
> want to do with certificates (attached at the end of this document),
> and then summarized that list of desires into requirements.  This
> document presents that summary of requirements.



## Table of Contents

_No entries — navigation._



## Charter of the SPKI working group

_¶1 not reproduced — motivation (protocols that already require a public key
infrastructure); its "require" describes existing protocols, not SPKI._

**N-003.** (§Charter of the SPKI working group ¶2) _[lowercase/implied]_

> The task of the working group will be to develop Internet standards
> for an IETF sponsored public key certificate format, associated
> signature and other formats, and key acquisition protocols.  The key
> certificate format and associated protocols are to be simple to
> understand, implement, and use. For purposes of the working group,
> the resulting formats and protocols are to be known as the Simple
> Public Key Infrastructure, or SPKI.

**N-004.** (§Charter of the SPKI working group ¶3) _[lowercase/implied]_

> The SPKI is intended to provide mechanisms to support security in a
> wide range of Internet applications, including IPSEC protocols,
> encrypted electronic mail and WWW documents, payment protocols, and
> any other application which will require the use of public key
> certificates and the ability to access them. It is intended that the
> Simple Public Key Infrastructure will support a range of trust
> models.



## Background

_¶1 not reproduced — history (Kohnfelder's thesis, Diffie and Hellman's
public directory); its "needs" belongs to the account of [DH]._

**N-005.** (§Background ¶2) _[lowercase/implied]_

> The SPKI team directly addressed the issue of <name,key> bindings and
> realized that such certificates are of extremely limited use for
> trust management.  A keyholder's name is one attribute of the
> keyholder, but as can be seen in the list of needs in this document,
> a person's name is rarely of security interest.  A user of a
> certificate needs to know whether a given keyholder has been granted
> some specific authorization.



## General Requirements

**N-006.** (§General Requirements ¶1) _[lowercase/implied]_

> We define the term KEYHOLDER of a public key to refer to the person
> or other entity that controls the corresponding private key.

**N-007.** (§General Requirements ¶2) _[lowercase/implied]_

> The main purpose of an SPKI certificate is to authorize some action,
> give permission, grant a capability, etc. to or for a keyholder.

**N-008.** (§General Requirements ¶3) _[lowercase/implied]_

> The keyholder is most directly identified by the public key itself,
> although for convenience or other purposes some indirection (delayed
> binding) may be employed.  That indirection can be via a collision-
> free hash of the public key or via a name, later to be resolved into
> a key.

**N-009.** (§General Requirements ¶4) _[lowercase/implied]_

> The definition of attributes or authorizations in a certificate is up
> to the author of code which uses the certificate.  The creation of
> new authorizations should not require interaction with any other
> person or organization but rather be under the total control of the
> author of the code using the certificate.

**N-010.** (§General Requirements ¶5) _[lowercase/implied]_

> Because SPKI certificates might carry information that the keyholder
> might not want to publish, we assume that certificates will be
> distributed directly by the keyholder to the verifier.  If the
> keyholder wishes to use a global repository, such as LDAP, the global
> PGP key server or the DNS database, that is up to the keyholder and
> not for the SPKI WG to specify.

**N-011.** (§General Requirements ¶6) _[lowercase/implied]_

> Because SPKI certificates will carry information that, taken together
> over all certificates, might constitute a dossier and therefore a
> privacy violation, each SPKI certificate should carry the minimum
> information necessary to get a job done.  The SPKI certificate is
> then to be like a single key rather than a key ring or a single
> credit card rather than a whole wallet.  The keyholder should be able
> to release a minimum of information in order to prove his or her
> permission to act.

**N-012.** (§General Requirements ¶7) _[lowercase/implied]_

> It is necessary for at least some certificates to be anonymous.

**N-013.** (§General Requirements ¶8) _[lowercase/implied]_

> Because one use of SPKI certificates is in secret balloting and
> similar applications, an SPKI certificate must be able to assign an
> attribute to a blinded signature key.

**N-014.** (§General Requirements ¶9) _[lowercase/implied]_ _[page break removed]_

> One attribute of a keyholder is a name.  There are names the
> keyholder prefers to be called and there are names by which the
> keyholder is known to various other keyholders.  An SPKI certificate
> must be able to bind a key to such names.  The SDSI work of Rivest
> and Lampson has done an especially good job of defining and using
> local name spaces, therefore if possible SPKI should support the SDSI
> name construct.  [Note: SPKI and SDSI have merged.]



## Validity and CRLs

**N-015.** (§Validity and CRLs ¶1) _[lowercase/implied]_

> An SPKI certificate, like any other, should be able to carry a
> validity period: dates within which it is valid.  It may also be
> necessary to have on-line refinement of validity.  This is frequently
> achieved via a Certificate Revocation List (CRL) in previous
> certificate designs.

**N-016.** (§Validity and CRLs ¶2) _[lowercase/implied]_

> A minimal CRL contains a list of revoked certificates, identified
> uniquely, a sequence number and a signature.  Its method of
> transmission is not specified.  If it encounters some certificate
> that it lists, then it annihilates that certificate.  If it
> encounters a previous CRL, as indicated by sequence number, then it
> annihilates that previous CRL.  Such a CRL leads to non-deterministic
> program behavior.  Therefore, we take as a requirement that if SPKI
> uses CRLs, then the certificate that uses it must explicitly tell the
> verifier where to find the CRL, the CRL must carry explicit validity
> dates and the dates of a sequence of CRLs must not overlap.  Under
> this set of requirements, behavior of certificate validation is
> deterministic (aside from the question of clock skew).

**N-017.** (§Validity and CRLs ¶3) _[lowercase/implied]_

> A CRL is a negative statement.  It is the digital equivalent of the
> little paper books of bad checks or bad credit cards that were
> distributed to cashiers in the 1970's and before.  These have been
> replaced in the retail world by positive statements -- on-line
> validation of a single check, ATM card or credit card.

**N-018.** (§Validity and CRLs ¶4) _[lowercase/implied]_

> SPKI should support both positive and negative on-line validations.

**N-019.** (§Validity and CRLs ¶5) _[lowercase/implied]_

> Any CRL or revalidation instrument must have its own lifetime.  A
> lifetime of 0 is not possible because of communication delays and
> clock skews, although one can consider an instrument whose lifetime
> is "one use" and which is delivered only as part of a
> challenge/response protocol.



## Implementation of Certificates

**N-020.** (§Implementation of Certificates ¶1) _[lowercase/implied]_ _[page break removed]_

> The authorization certificates that are envisioned for SPKI (and
> needed to meet the demands of the list given at the end of this
> document) should be generated by any keyholder empowered to grant or
> delegate the authorization in question.  The code to generate
> certificates should be written by many different developers,
> frequently persons acting alone, operating out of garages or dorm
> rooms.  This leads to a number of constraints on the structure and
> encoding of certificates.  In addition, SPKI certificates should be
> usable in very constrained environments, such as smart cards or small
> embedded systems.  The code to process them and the memory to store
> them should both be as small as possible.

**N-021.** (§Implementation of Certificates ¶2) _[lowercase/implied]_

> An SPKI certificate should be as simple as possible.  There should be
> a bare minimum of fields necessary to get the job done and there
> should be an absolute minimum of optional fields.  In particular, the
> structure should be specific enough that the creator of a certificate
> is constrained by the structure definition, not by complaints (or
> error messages) from the reader of a certificate.

**N-022.** (§Implementation of Certificates ¶3) _[lowercase/implied]_

> An SPKI certificate should be described in as simple a method as
> possible, relating directly to the kind of structures a C or PASCAL
> programmer would normally write.

**N-023.** (§Implementation of Certificates ¶4) _[lowercase/implied]_

> No library code should be required for the packing or parsing of SPKI
> certificates.  In particular, ASN.1 is not to be used.

**N-024.** (§Implementation of Certificates ¶5) _[lowercase/implied]_

> A certificate should be signed exactly as it is transmitted.  There
> should be no reformatting called for in the process of checking a
> certificate's signature (although one might canonicalize white space
> during certificate input, for example, if the format is text).

**N-025.** (§Implementation of Certificates ¶6) _[lowercase/implied]_

> For efficiency, if possible, an SPKI certificate should be encoded in
> an LR(0) grammar.  That is, neither packing nor parsing of the
> structure should require a scan of the data.  Data should be read
> into the kind of structure a programmer would want to use without
> touching the incoming bytes more than once.

**N-026.** (§Implementation of Certificates ¶7) _[lowercase/implied]_

> For efficiency, if possible, an SPKI certificate should be packed and
> parsed without any recursion.



## List of Certificate Uses

**N-027.** (§List of Certificate Uses ¶1) _[lowercase/implied]_

> The list below is a brainstorming list, accumulated on the SPKI
> mailing list, of uses of such certificates.

**N-028.** (§List of Certificate Uses #1) _[lowercase/implied]_

```
      -  I need a certificate to give me permission to write electronic
         checks.
```

**N-029.** (§List of Certificate Uses #2) _[lowercase/implied]_

```
      -  My bank would need a certificate, proving to others that it is
         a bank capable of cashing electronic checks and permitted to
         give permission to people to write electronic checks.
```

**N-030.** (§List of Certificate Uses #3) _[lowercase/implied]_

```
      -  My bank would issue a certificate signing the key of a master
         bank certifier -- perhaps NACHA -- so that I could follow a
         certificate chain from a key I know (my bank's) to the key of
         any other bank in the US and, similarly, to any other bank in
         the world.
```

**N-031.** (§List of Certificate Uses #4) _[lowercase/implied]_

```
      -  I might generate a certificate (a "reputation voucher") for a
         friend to introduce him to another friend -- in which
         certificate I could testify to my friend's political opinion
         (e.g., libertarian cypherpunk) or physical characteristics or
         anything else of interest.
```

**N-032.** (§List of Certificate Uses #5) _[lowercase/implied]_

```
      -  I might have a certificate giving my security clearance, signed
         by a governmental issuing authority.
```

**N-033.** (§List of Certificate Uses #6) _[lowercase/implied]_

```
      -  I want a certificate for some software I have downloaded and am
         considering running on my computer -- to make sure it hasn't
         changed and that some reputable company or person stands behind
         it.
```

**N-034.** (§List of Certificate Uses #7) _[lowercase/implied]_

```
      -  I need certificates to bind names to public keys:
```

**N-035.** (§List of Certificate Uses #7a) _[lowercase/implied]_

```
         -  [traditional certificate] binding a key to a name, implying
            "all the attributes of the real person having this name are
            transferred to this key by this certificate".  This requires
            unique identification of a person (which is difficult in
            non-digital space, as it is) and someone trustworthy binding
            that unique name to the key in question.  In this model, a
            key starts out naked and acquires attributes, permissions
            and authority from the person bound to it.
```

**N-036.** (§List of Certificate Uses #7b) _[lowercase/implied]_

```
         -  [direct certificate] binding a name to a key, implying "I
            (the person who is able to use the associated private key to
            make this signature) declare that I go by the name of
            XXXXXXX."  The unique identification of the key is automatic
            -- from the key itself or a cryptographic hash of the key.
            The binding is done by the key itself -- in a self-signed
            certificate.  In this model, a key is loaded with
            attributes, permissions and authority directly by other
            certificates, not indirectly through some person's name, and
            this certificate declares only a name or nickname by which
            the key's owner likes to be addressed.
```

**N-037.** (§List of Certificate Uses #7c) _[lowercase/implied]_ _[page break removed]_

```
         -  [personal binding] binding a key to a nickname.  This kind
            of certificate is signed by me, singing someone else's key
            and binding it to a nickname by which I know that person.
            It is for my use only -- never given out -- and is a signed
            certificate to prevent tampering with my own private
            directory of keys.  It says nothing about how I certified
            the binding to my own satisfaction between the key and my
            friend.
```

**N-038.** (§List of Certificate Uses #8) _[lowercase/implied]_

```
      -  I might be doing genealogy and be collecting what amounts to
         3x5 cards with facts to be linked together.  Some of these
         links would be from one content to another reference [e.g.,
         indexing and cross-referencing].  Others might be links to the
         researcher who collected the fact.  By rights, the fact should
         be signed by that researcher.  Viewing only the signature on
         the fact and the link to the researcher, this electronic 3x5
         card becomes a certificate.
```

**N-039.** (§List of Certificate Uses #9) _[lowercase/implied]_

```
      -  I want to sign a contract to buy a house.  What kind of
         certificate do I need?
```

**N-040.** (§List of Certificate Uses #10) _[lowercase/implied]_

```
      -  I have found someone on the net and she sounds really nice.
         Things are leading up to cybersex.  How do I make sure she's
         not really some 80-year-old man in a nursing home?
```

**N-041.** (§List of Certificate Uses #11) _[lowercase/implied]_

```
      -  I have met someone on the net and would like a picture of her
         and her height, weight and other measurements from a
         trustworthy source.
```

**N-042.** (§List of Certificate Uses #12) _[lowercase/implied]_

```
      -  Can I have a digital marriage license?
```

**N-043.** (§List of Certificate Uses #13) _[lowercase/implied]_

```
      -  Can I have a digital divorce decree?
```

**N-044.** (§List of Certificate Uses #14) _[lowercase/implied]_

```
      -  ..a digital Voter Registration Card?
```

**N-045.** (§List of Certificate Uses #15) _[lowercase/implied]_

```
      -  There are a number of cards one carries in a typical wallet
         which could become certificates attached to a public key:
```

**N-046.** (§List of Certificate Uses #16) _[lowercase/implied]_

```
      -  health insurance card
```

**N-047.** (§List of Certificate Uses #17) _[lowercase/implied]_

```
      -  prescription drug card
```

**N-048.** (§List of Certificate Uses #18) _[lowercase/implied]_

```
      -  driver's license (for permission to drive)
```

**N-049.** (§List of Certificate Uses #19) _[lowercase/implied]_

```
      -  driver's license (for permission to buy alcohol)
```

**N-050.** (§List of Certificate Uses #20) _[lowercase/implied]_

```
      -  supermarket discount card
```

**N-051.** (§List of Certificate Uses #21) _[lowercase/implied]_

```
      -  supermarket check-cashing card [I know -- anachronism]
```

**N-052.** (§List of Certificate Uses #22) _[lowercase/implied]_

```
      -  Blockbuster Video rental card
```

**N-053.** (§List of Certificate Uses #23) _[lowercase/implied]_

```
      -  ATM card
```

**N-054.** (§List of Certificate Uses #24) _[lowercase/implied]_

```
      -  Credit card
```

**N-055.** (§List of Certificate Uses #25) _[lowercase/implied]_

```
      -  membership card in the ACLU, NRA, Republican party, Operation
         Rescue, NARAL, ACM, IEEE, ICAR....
```

**N-056.** (§List of Certificate Uses #26) _[lowercase/implied]_

```
      -  Red Cross blood donor card
```

**N-057.** (§List of Certificate Uses #27) _[lowercase/implied]_

```
      -  Starbuck's Coffee buy-10-get-1-free card
```

**N-058.** (§List of Certificate Uses #28) _[lowercase/implied]_

```
      -  DC Metro fare card
```

**N-059.** (§List of Certificate Uses #29) _[lowercase/implied]_

```
      -  Phone calling card
```

**N-060.** (§List of Certificate Uses #30) _[lowercase/implied]_

```
      -  Alumni Association card
```

**N-061.** (§List of Certificate Uses #31) _[lowercase/implied]_

```
      -  REI Membership card
```

**N-062.** (§List of Certificate Uses #32) _[lowercase/implied]_

```
      -  Car insurance card
```

**N-063.** (§List of Certificate Uses #33) _[lowercase/implied]_

```
      -  claim check for a suitcase
```

**N-064.** (§List of Certificate Uses #34) _[lowercase/implied]_

```
      -  claim check for a pawned radio
```

**N-065.** (§List of Certificate Uses #35) _[lowercase/implied]_

```
      -  authorization for followup visits to a doctor, after surgery
```

**N-066.** (§List of Certificate Uses #36) _[lowercase/implied]_

```
      -  Better Business Bureau [BBB] style reputation certificates
         [testimonies from satisfied customers]
```

**N-067.** (§List of Certificate Uses #37) _[lowercase/implied]_

```
      -  BBB-style certificate that no complaints exist against a
         business or doctor or dentist, etc.
```

**N-068.** (§List of Certificate Uses #38) _[lowercase/implied]_

```
      -  LDS Temple Recommend
```

**N-069.** (§List of Certificate Uses #39) _[lowercase/implied]_

```
      -  Stock certificate
```

**N-070.** (§List of Certificate Uses #40) _[lowercase/implied]_

```
      -  Stock option
```

**N-071.** (§List of Certificate Uses #41) _[lowercase/implied]_

```
      -  Car title
```

**N-072.** (§List of Certificate Uses #42) _[lowercase/implied]_

```
      -  deed to land
```

**N-073.** (§List of Certificate Uses #43) _[lowercase/implied]_

```
      -  proof of ownership of electronic equipment with an ID number
```

**N-074.** (§List of Certificate Uses #44) _[lowercase/implied]_

```
      -  time card certificate [activating a digital time clock]
```

**N-075.** (§List of Certificate Uses #45) _[lowercase/implied]_

```
      -  proof of degree earned [PhD, LLD, MD, ...]
```

**N-076.** (§List of Certificate Uses #46) _[lowercase/implied]_

```
      -  permission to write digitally signed prescriptions for drugs
```

**N-077.** (§List of Certificate Uses #47) _[lowercase/implied]_

```
      -  permission to spend up to $X of a company's money
```

**N-078.** (§List of Certificate Uses #48) _[lowercase/implied]_

```
      -  permission to issue nuclear launch codes
```

**N-079.** (§List of Certificate Uses #49) _[lowercase/implied]_

```
      -  I'm a sysadmin, I want to carry a certificate, signed by SAGE,
         that says I'm good at the things sysadmins are good at.
```

**N-080.** (§List of Certificate Uses #50) _[lowercase/implied]_

```
      -  I'm that same sysadmin, I want an ephemeral certificate that
         grants me root access to certain systems for the day, or the
         week, or...

         Certain applications *will* want some form of auditing, but the
         audit identity should be in the domain of the particular
         application...  For instance an "is a system administrator of
         this host" certificate would probably want to include an audit
         identity, so you can figure out which of your multiple admins
         screwed something up.
```

**N-081.** (§List of Certificate Uses #51) _[lowercase/implied]_

```
      -  I'm an amateur radio operator.  I want a signed certificate
         that says I'm allowed to engage in amateur radio, issued by the
         DOC.  [I currently have a paper version of one].  This would be
         useful in enforcing access policies to the amateur spectrum;
         and in tracking abuse of that same spectrum.  Heck!  extend
         this concept to all licensed spectrum users.
```

**N-082.** (§List of Certificate Uses #52) _[lowercase/implied]_

```
      -  I'm the a purchasing agent for a large corporation.  I want to
         posses a certificate that tells our suppliers that I'm
         authorized to make purchases up to $15,000.  I don't want the
         suppliers to know my name, lest their sales people bug me too
         much.  I don't want to have to share a single "Megacorp
         Purchasing Department Certificate" with others doing the same
         job [the private key would need to be shared--yuck!].
```

**N-083.** (§List of Certificate Uses #53) _[lowercase/implied]_ _[page break removed]_

```
      -  "This signed-key should be considered equivalent to the
         certifying-key until this certificate expires for the following
         purposes ..."
            [This is desirable when you wish to reduce the exposure of
            long-term keys.  One way to do this is to use smart cards,
            but those typically have slow processors and are connected
            through low-bandwidth links; however, if you only use the
            smart card at "login" time to certify a short-term key pair,
            you get high performance and low exposure of the long term
            key.

            I'll note here that this flies in the face of attempts to
            prevent delegation of certain rights.  Maybe we need a
            "delegation-allowed" bit -- but there's nothing to stop
            someone who wishes to delegate against the rules from also
            loaning out their private key.].
```

**N-084.** (§List of Certificate Uses #54) _[lowercase/implied]_

```
      -  "I am the current legitimate owner of a particular chunk of
         Internet address space."
            [I'd like to see IPSEC eventually become usable, at least
            for privacy, without need for prior arrangement between
            sites, but I think there's a need for a "I own this
            address"/"I own this address range" certificate in order for
            IPSEC to coexist with existing ip-address-based firewalls.]
```

**N-085.** (§List of Certificate Uses #55) _[lowercase/implied]_

```
      -  "I am the current legitimate owner of a this DNS name or
         subtree."
```

**N-086.** (§List of Certificate Uses #56) _[lowercase/implied]_

```
      -  "I am the legitimate receiver of mail sent to this rfc822 email
         address.  [this might need to be signed by a key which itself
         had been certified by the appropriate "DNS name owner"
         certificate]."
            [This is in case I know someone owns a particular e-mail
            address but I don't know their key.]
```

**N-087.** (§List of Certificate Uses #57) _[lowercase/implied]_

```
      -  Encryption keys for E-mail and file encryption
```

**N-088.** (§List of Certificate Uses #58) _[lowercase/implied]_

```
      -  Authentication of people or other entities
```

**N-089.** (§List of Certificate Uses #59) _[lowercase/implied]_

```
      -  Digital signatures (unforgeability)
```

**N-090.** (§List of Certificate Uses #60) _[lowercase/implied]_

```
      -  Timestamping / notary services
```

**N-091.** (§List of Certificate Uses #61) _[lowercase/implied]_

```
      -  Host authentication
```

**N-092.** (§List of Certificate Uses #62) _[lowercase/implied]_

```
      -  Service authentication
```



### Other requirements

_Not a heading in the source: the label `Other requirements:` (line 547) is
indented under use #62 and introduces the six items below, which are
numbered here `OR-1` to `OR-6`. The label is fenced with OR-1, the item it
introduces._

**N-093.** (§List of Certificate Uses OR-1) _[lowercase/implied]_

```
         Other requirements:

         -  Trust model must be a web (people want to choose whom they
            trust).  People must be able to choose whom they trust or
            consider reliable roots (maybe with varying reliabilities).
```

**N-094.** (§List of Certificate Uses OR-2) _[lowercase/implied]_

```
         -  Some applications (e.g., notary services) require highly
            trusted keys; generation complexity is not an issue here.
```

**N-095.** (§List of Certificate Uses OR-3) _[lowercase/implied]_

```
         -  Some applications (e.g., host authentication) require
            extremely light (or no) bureaucracy.  Even communication
            with the central administrator may be a problem.
```

**N-096.** (§List of Certificate Uses OR-4) _[lowercase/implied]_

```
         -  Especially in lower-end applications (e.g. host
            authentication) the people generating the keys (e.g.,
            administrators) will change, and you will no longer want
            them to be able to certify.  On the other hand, you will
            usually also not want all keys they have generated to
            expire.  This may imply a "certification right expiration"
            certificate requirement, probably to be implemented together
            with notary services.
```

**N-097.** (§List of Certificate Uses OR-5) _[lowercase/implied]_

```
         -  Keys will need to be cached locally to avoid long delays
            fetching frequently used keys.  Cf. current name servers.
            The key infrastructure may in future get used almost as
            often as the name server.  The caching and performance
            requirements are similar.
```

**N-098.** (§List of Certificate Uses OR-6) _[lowercase/implied]_

```
         -  Reliable distribution of key revocations and other
            certificates (e.g., the ceasing of the right to make new
            certificates).  May involve goals like "will have spread
            everywhere in 24 hours" or something like that.  This
            interacts with caching.
```



## Open Questions

**N-099.** (§Open Questions ¶1) _[lowercase/implied]_

> Given such certificates, there remain some questions, most to do with
> proofs of the opposite of what a certificate is designed to do.
> These do not have answers provided by certificate definition or
> issuing alone.

**N-100.** (§Open Questions Q1) _[lowercase/implied]_

```
   -  Someone digitally signs a threatening e-mail message with my
      private key and sends it to president@whitehouse.gov.  How do I
      prove that I didn't compose and send the message?  What kind of
      certificate characteristic might help me in this?

         This is an issue of (non-)repudiation and therefore a matter of
         private key protection.  Although this is of interest to the
         user of certificates, certificate format, contents or issuing
         machinery can not ensure the protection of a user's private key
         or prove whether or not a private key has been stolen or
         misused.
```

**N-101.** (§Open Questions Q2) _[lowercase/implied]_

```
   -  Can certificates help do a title scan for purchase of a house?

         Certificates might be employed to carry information in a
         tamper-proof way, but building the database necessary to record
         all house titles and all liens is a project not related to
         certificate structure.
```

**N-102.** (§Open Questions Q3) _[lowercase/implied]_

```
   -  Can a certificate be issued to guarantee that I am not already
      married, so that I can then get a digital marriage license?

         The absence of attributes can be determined only if all
         relevant records are digitized and all parties have inescapable
         IDs.  The former is not likely to happen in our lifetimes and
         the latter receives political resistance.

         A certificate can communicate the 'positive' attribute "not
         already married" or "not registered as a voter in any other
         district".  That assumes that some organization is capable of
         determining that fact for a given keyholder.  The method of
         determining such a negative fact is not part of the certificate
         definition.
```

**N-103.** (§Open Questions Q4) _[lowercase/implied]_

```
   -  The assumption in most certificates is that the proper user will
      protect his private key very well, to prevent anyone else from
      accessing his funds.  However, in some cases the certificate
      itself might have monetary value [permission to prescribe drugs,
      permission to buy alcohol, ...].  What is to prevent the holder of
      such a certificate from loaning out his private key?

         This is a potential flaw in any system providing authorization
         and an interesting topic for study.  What prevents a doctor or
         dentist from selling prescriptions for controlled substances to
         drug abusers?
```



## References

_No entries — bibliography ([DH], [KOHN]); the citations resolve here.
Its "May" (line 657) is the month of [KOHN]._



## Security Considerations

**N-104.** (§Security Considerations ¶1) _[lowercase/implied]_

> Security issues are discussed throughout this memo.



## Author's Address

_No entries — contact details._



## Full Copyright Statement

_No entries — copyright and warranty boilerplate. Its five lowercase modals
("may" ×3, "must", "required"; lines 739–750) and its capitalised
`NOT` ×2 / `WILL` govern use of the document, not SPKI._



## Acknowledgement

_No entries — RFC Editor funding notice._
