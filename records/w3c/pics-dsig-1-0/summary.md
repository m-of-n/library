---
schema: "library-summary/v1"
id: pics-dsig-1-0
record: pics-dsig-1-0
type: summary
updated: "2026-10-23"
---

# PICS Signed Labels (DSig) 1.0 Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic` — a W3C Recommendation of 1998-05-27, listed **Retired** on 2009-11-24 by the W3C publication history (https://www.w3.org/standards/history/REC-DSig-label/, read 2026-10-23); the retired edition says PICS is superseded by POWDER. The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. |
| **Authors** | Yang-hua Chu, Philip DesAutels, Brian LaMacchia, Peter Lipp. Editor: Philip DesAutels. W3C Digital Signature Working Group |
| **Published** | 1998-05-27 (W3C Recommendation, `REC-DSig-label-19980527`; the cached page says "Last updated: 1998-06-01T14:03:02Z", a markup-only change per its Change History) |
| **Identifier** | https://www.w3.org/TR/1998/REC-DSig-label-19980527/ |
| **Source** | https://www.w3.org/TR/1998/REC-DSig-label-19980527/ |
| **Digest** | `69ecbc8314b767137281e6c3515bbb3a79fa2270434eae7cac18548c36eb261a` (text/html, retrieved 2026-10-23) |

**Locators.** The document has no section numbers. Locators below are its
headings, with the HTML anchor where one exists — e.g. *Canonicalization*
(`#Canonicalization`). "Overview" is *DSig 1.0 Overview* (`#DSig_1_0_Overview`).

## Overview

DSig 1.0 turns a PICS 1.1 label into a signed statement — *signer believes
statement about information resource* (Overview) — by adding two PICS
extensions: `resinfo`, a list of hashes of the labelled resource, and
`sigblock`, one or more parallel signatures over the rest of the label
(Overview; *DSig Extensions*). The label is always **detached**: "At no time
does a DSig 1.0 signature label 'wrap' the information resource it is signing"
(Overview). What is signed is not the transmitted bytes but a
**reconstructed and canonicalised** label: the signer builds an *equivalent
standalone label* (service options folded into label options, `sigblock`
removed, fields dropped per any `include`/`exclude` token), serialises it by
fixed rules, and signs that (*Signing a label*; *Creating an equivalent
standalone label* `#equivalent_label`; *Canonicalization*). The verifier must
do the same reconstruction: "it is important that signing and verifying
applications canonicalize labels in the same way" (*The "include" and
"exclude" tokens*). It is crypto-neutral — algorithms are URL-named
"signature suites" (*Signatures* `#Signature`) — with MD5, SHA-1, RSA-MD5 and
DSS mandatory to implement (Appendix 3).

**Answers to the R-0006 ∅ cells, with locators.**

- **What is hashed.** The labelled resource, by `resinfo`: one or more
  `(hash-algorithm-URL, base64 hash, optional date)` entries, each with a
  different algorithm (*Resource Reference Information Extension*
  `#Reference_Information`). Which bytes of the resource are hashed is **not
  defined** for HTML, and for other media types Appendix 2 says a
  specification of "how the document is normalized for hashing into the label
  must be created". `resinfo` is optional, and not usable in a generic label
  (*generic* option under *Applying PICS to DSig*; *Resource Reference
  Information Extension*).
- **What is signed.** The canonical form of the equivalent standalone label.
  That includes the `PICS-1.1` header, the service URL, all options and
  extensions — so `resinfo`, and with it the content binding, **is** covered
  by default — and the ratings (*Canonicalization*). It **excludes the whole
  `sigblock`**: "none of the information within the entire sigblock extension,
  including the Attribution Information section, contributes to the hash of
  the label that is signed as part of the signature option" (*Attribution
  Information* `#AttribInfo`). So the signature-suite URL, the keyholder
  fields, the signing time (`"on"` is "advisory only", *The "On" token*) and
  the `include`/`exclude` field-list are all **unauthenticated** — unless a
  suite chooses to "mix into the hash of the data information concerning the
  algorithms used to generate the hash and signature" (*Hashing* `#Hashing`),
  which is permitted, not required. An `exclude` naming `resinfo` yields a
  valid signature that binds no content.
- **Whether it canonicalises, and when.** Yes — on both sides. Signing: build
  the standalone label, canonicalise, sign (*Signing a label*). Verification:
  the signed bytes are not transmitted; the verifier rebuilds them from the
  received label list, using "all options available to it: both service and
  label options" (*Canonicalization*, last paragraph), and the
  `include`/`exclude` tokens exist to "convey this information to
  applications trying to verify the signature" (*Creating an equivalent
  standalone label*). Canonicalisation therefore runs **during verification,
  on untrusted input**.
- **How a verifier proceeds.** There is **no verification section**. The
  procedure is implied, not stated: (1) take the label from the received
  label list; (2) rebuild the equivalent standalone label, removing `sigblock`
  and applying that Signature's `include`/`exclude`; (3) canonicalise;
  (4) verify the `SigCrypto` value under the named suite, locating the key via
  `ByKey`/`ByHash`/`ByName`/`ByCert` (*Keyholder tokens* `#Keyholder`);
  (5) separately, recompute the resource hash and compare against `resinfo`
  (purpose stated in *Resource Reference Information Extension*; no step
  obliges it). Whether to act on the result is left out of scope: "Whether
  information contained within an unsigned or unverified label should be used
  is a trust management question" (*Signature Block Extension*
  `#Signature_Block`). The W3C reference implementation (below) checks resinfo
  hashes and sigblock signatures as separate tests with tri-valued results —
  that is the implementation's procedure, not the Recommendation's.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A signed-assertion format whose own text names "a security hole in the above proposal" (Appendix 1) and whose verifier canonicalises untrusted input. |
| Cryptography | adjacent | Defines no primitive; binds algorithms by URL-named suites (*URLs as identifiers* `#URLID`). The mandatory set (MD5, SHA-1, RSA-MD5, DSS; Appendix 3) is obsolete. |
| This project | adjacent | Not a candidate for anything: retired and PICS-bound. Held as **prior art and counter-example**. |

Bears on, as prior art only:

- **R-O-05** (proposed, `ARCH-0001-PROPOSAL-v0.2.0` §6) — DSig is a ratified
  instance of what R-O-05 forbids: signed bytes not transmitted, regenerated
  by the verifier from a received structure. It also lacks the *authenticated
  type indicator*: the suite URL sits in the unsigned `sigblock`.
- **DEC-002** / **R-O-03** — the *Canonicalization* rules are a citable
  canonical form, and Limits 2 records why they are under-specified. With
  RFC 2692's sign-as-transmitted requirement and RFC 9804's sign-the-canonical
  form, DSig is a third data point on R-0006 condition (3).
- **DEC-005** — a detached signature label carried *beside* the content
  rather than an envelope around it; parallel signatures supported, cascaded
  ones not within one label (*Parallel and cascaded signatures*).
- **R-M-07** — `resinfo` is a multi-algorithm content-digest set in 1998, the
  shape of in-toto's digest map; the generic-label exclusion and the `exclude`
  loophole show a signed statement that binds no digest remaining valid.
- **R-M-12** — algorithm, certificate-family and suite identifiers are URLs,
  which "in effect creates a distributed registry of unique names" (*URLs as
  identifiers*): registry-free, but DNS-rooted rather than key-rooted.
- **DEC-007** — Appendix 1: the label carries only the service URL, so "the
  semantics of the rating service" can change after signing "without
  invalidating the label"; the suggested fix is a separate signature label on
  the service description. That is the argument for a hash-identified, signed
  vocabulary.
- **R-I-01** — the `ARCH-0001` §6 *PICS label* import row can now be written
  from the library: what a DSig label authenticates and what it does not.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| W3C DSig 1.0 Reference Implementation (`w3c.www.dsig`, Java 1.1) | open source, reference | not checked | https://www.w3.org/PICS/refcode/Parser/dsigapi.html |

Searched 2026-10-23. The only implementation found is W3C's own 1998
reference code, invoked from W3C's Java PICS parsers. No maintained
implementation found; none is expected for a retired specification. Licence
left unfilled rather than guessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`.** This pass (library#87) claims the **summary bar**: the
record is `summarized`, declares no `distillation` block and adds nothing to
`distilled/`, so FX-1 does not fire. FX-1 extraction of this record is owned by
library#89. What it would add that this summary
cannot: the *Canonicalization* rules and both extension BNFs as verbatim
schema, and the *An Example* steps as test vectors — which would force a
decision on the defects in Limits 2.

**No verbatim normative text** beyond short, locator-bearing fragments; under
FX-1 that belongs in `distilled/normative.md`. The source uses no BCP 14
keywords; its obligations are lowercase "must"/"should".

## Limits

1. **`contradicts` pics-1-1-labels — on its own grammar.** *DSig Extensions*
   says "A DSig 1.0 Signature Label is a standard PICS 1.1 label." *Detailed
   Syntax of the sigblock Extension* then concedes "This extension is not a
   valid PICS 1.1 extension because Base64 encoding uses a '/' which cannot be
   represented as a PICS 1.1 datum", and rests interoperability on the belief
   that "all existing PICS parsers will support the grammar presented below".
   PICS 1.1's `quotedname` does exclude `/` (pics-1-1-labels, *Detailed
   Syntax*). Both claims cannot hold; DSig records the conflict itself and
   does not resolve it.
2. **The canonical form is under-specified, and its own example departs from
   it.** *Canonicalization* sorts options alphabetically by shortest name and
   transmit-names alphabetically, but says nothing about the order of entries *inside* an
   extension — yet Step 3 of *An Example* prints the `resinfo` hashes as MD5
   then SHA-1, the reverse of Steps 2 and 4. The rule says symbols are
   lowercased and the header is the `pics-1.1` symbol; the example prints
   `PICS-1.1`, and a space after the leading parenthesis that the rule appears
   to forbid. DSig does not carry over PICS 1.1's rules for default-valued
   options or shortest value forms (pics-1-1-labels, *Signature Details*), so
   whether an explicit `gen false` and its absence canonicalise alike is not
   stated. Two conforming implementations can produce different bytes — the
   condition (1) / (2) risk, inside the step the verifier must repeat.
3. **Coverage is set by unsigned data.** The `include`/`exclude` list lives in
   `sigblock`, outside the signed bytes, and the canonical form records
   nothing about what was omitted. A verifier learns what a signature covers
   only from unauthenticated input.
4. **No defined bytes for the content hash.** *Resource Reference Information
   Extension* says "the document retrieved must be the same document or the
   hash(s) contained in the resinfo extension will not be valid", but not
   which bytes are hashed — in particular DSig does not restate PICS 1.1's
   rule that embedded PICS labels are excluded before hashing
   (pics-1-1-labels, *MICs and Digital Signatures*). Appendix 2 defers
   non-HTML normalisation to specifications not yet written.
5. **The rating vocabulary is not bound** (Appendix 1), and the only
   mitigation offered is a trust-engine policy. DSig 2.0 was to build on RDF
   and drop `include`/`exclude` (note under *The "include" and "exclude"
   tokens*); no DSig 2.0 record exists in the library, and this record does
   not assert that one was published.
6. **Trust is out of scope.** Attribution Information is optional and
   unsigned, and applications "may augment" it after signing (*Attribution
   Information*); reliance is "a trust management question". There is no
   principal, delegation or revocation model — consistent with R-001 §11.1's
   reading of PICS.
7. **Endorsement, not authorship.** A sigblock means the key holder "asserts
   that the statements made within the label are valid" (*Semantics of
   Embedded Signature Blocks*), and "A signature does not indicate that the
   signer created the label, only that they believe the statements made within
   it are valid." (*PICS Architecture*), and the `by` option "need not be the
   same as that of the signer(s)" (*Applying PICS to DSig*). An import under
   R-I-01 cannot take the signer to be the label's author.
