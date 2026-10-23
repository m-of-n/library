---
schema: "library-summary/v1"
id: pics-1-1-labels
record: pics-1-1-labels
type: summary
updated: "2026-10-23"
---

# PICS 1.1 Label Distribution: Label Syntax and Communication Protocols

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic` — a W3C Recommendation of 1996-10-31, listed **Retired** on 2009-11-24 by the W3C publication history (https://www.w3.org/standards/history/REC-PICS-labels/, read 2026-10-23). The RFC 2026 ladder does not apply to W3C documents; this is a mapping, not a quotation. |
| **Authors** | Tim Krauskopf, Jim Miller, Paul Resnick, Win Treese. Editor: Jim Miller. PICS technical subcommittee |
| **Published** | 1996-10-31 (W3C Recommendation, `REC-PICS-labels-961031`) |
| **Identifier** | https://www.w3.org/TR/REC-PICS-labels-961031 |
| **Source** | https://www.w3.org/TR/REC-PICS-labels-961031 |
| **Digest** | `a1acf19869f6b8df9ab7387b6172fd0002960dd0f82983c82df614a0cbd8948d` (text/html, retrieved 2026-10-23) |

**Locators.** The document has no section numbers. Locators below are its
headings, with the HTML anchor — e.g. *MICs and Digital Signatures* (`#MICs`),
whose subsection *Signature Details* carries the signing rules.

## Overview

A PICS 1.1 label is a service identifier (the rating service's URL), options,
and a rating — attribute–value pairs whose meaning is defined elsewhere, by the
rating system the service URL leads to (*General Format* `#General`;
pics-1-1-services). This document fixes the label syntax as an
`application/pics-labels` label list and three ways to deliver it: embedded in
HTML by `META http-equiv`, in an RFC-822 `PICS-Label` header (with an HTTP
`Protocol-Request` extension), or from a **label bureau** queried by URL
(*Overview*; *Embedding* `#Embedding`; *Using* `#Using`; *Requesting*
`#Requesting`). Security is two optional add-ons — "This specification
includes two independent security features" (*MICs and Digital Signatures*):
a message integrity check binding a label to content, and an RSA-MD5 signature
binding a label to its rating service.

**Answers to the R-0006 ∅ cells, with locators.**

- **Does a label bind the content it labels, and how?** **Only optionally,
  by the `MIC-md5` (alias `md5`) option**: a base64 MD5 digest of "the item
  being rated" (*General Format*, *Information about the document that is
  labeled*). The bytes are stated: "we recommend the direct use of the MD5
  algorithm on the source document", and because labels can be embedded in
  what they label, "care must be taken to ensure that the message digest is
  computed excluding all PICS labels in the document" — for HTML, every `META`
  element carrying a PICS label and the whitespace after it is removed first
  (*MICs and Digital Signatures*, `MIC-md5 or md5`). The check is
  recompute-and-compare on retrieval (same place; *Glossary*, "MIC"). The
  document deliberately does not canonicalise content — it declined MOSS's
  normalisation: "We have chosen not to adopt MOSS directly for PICS, largely
  because of this complexity."
- **Without a MIC**, a label is bound by **name or by context**, not by
  digest. The `for` option names a URL or URL prefix, but it is optional for
  specific labels; an embedded label "applies to that document, regardless of
  what URL is used to locate the document" (*Embedding*); an HTTP-header label
  likewise applies to the document requested "regardless of the URL specified
  in the "for" option" (*Using*); bureau responses are matched to requests
  **by position** and may omit `for` (*Response to Query for Labels Separate
  From Documents*). `at` (last-modified date) and `until`/`exp` are offered as
  cheaper, weaker checks; of `until` the text says "This, too, does not guard
  against a concerted malicious attack." (*MICs and Digital Signatures*).
  Generic labels apply by URL-prefix string match and cannot carry a
  meaningful digest of one resource.
- **Is the MIC itself signed?** Not necessarily. The `signature-RSA-MD5`
  option signs only the options the service chooses to transmit, and *Signature
  Details* says "Any option may be omitted, but it will be common for the
  options mic-md5 (or md5) and full (or complete-label) to be omitted." A
  signed label therefore commonly carries no signed content binding.
- **What is signed, and is it canonicalised?** A "special form" of the label
  (*Signature Details*): selected options sorted alphabetically by shortest name, options at
  their default value dropped, each written as short name, space, shortest
  value (case-insensitive strings lowercased), then `r (`, the transmit-name /
  value pairs in US-ASCII order, and `)`. `signature-rsa-md5` itself is never
  included. **No step outputs the service URL or the `PICS-1.1` header**, so
  the signed bytes do not name the rating service whose vocabulary gives the
  ratings meaning; that tie rests on which public key the verifier uses.
- **How does a verifier proceed?** Stated in prose (*MICs and Digital
  Signatures*, third bullet of the RSA description): the client "takes the
  label it received and converts it back into the same special form in which it
  was originally signed", recomputes MD5, base64-decodes the signature,
  decrypts it with the service's public key, and compares; on mismatch "the
  signature is invalid". Service options apply too (*Signature Details*, last
  paragraph). **Canonicalisation runs at verification, on received input.**
  Key distribution is left to each service, and PICS "assumes that no keys will
  ever have to be invalidated" (*MICs and Digital Signatures*).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Content integrity and label authenticity are optional add-ons; the core is a labelling and distribution format. |
| Cryptography | adjacent | Fixes MD5 and RSA-MD5 with no algorithm agility — "PICS specifically requires the use of the RSA signature algorithm with the MD5 message digest." (*Signature Details*). Both are broken; the interest is structural. |
| This project | adjacent | `ARCH-0001` §3.1 calls PICS the *"conceptual parent of attestations"*; its §6 maps a PICS label to `ArtifactStatement`. Prior art, not a candidate. |

Bears on, as prior art only:

- **R-M-07** — the 1996 answer to "bind a content digest" is *optionally*,
  with the digest commonly left outside the signature. A label without `MIC-md5`
  is an `ArtifactStatement` that would fail R-M-07; the exclusion rule for
  self-embedded labels is a precise precedent for defining *which bytes* a
  digest covers.
- **R-O-05** (proposed) / **DEC-002** / **R-O-03** — the special form is a cited
  canonical form that the **verifier** regenerates from the received label —
  the pattern R-O-05 forbids — and the signed bytes carry no type indicator.
  Together with pics-dsig-1-0, two ratified W3C signature schemes on R-0006
  condition (3)'s wrong side.
- **DEC-007** — a label carries transmit-names and numbers only; meaning is
  resolved by dereferencing the service URL (*General Format*;
  pics-1-1-services). That separation is what proposed DEC-007 generalises, and
  the unsigned service URL (above) is its weak point.
- **R-I-01** — the `ARCH-0001` §6 *PICS label* import row: subject by
  URL/prefix/context, digest optional MD5, issuer as service key, no
  delegation. The row's import profile can now be written from the library.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| W3C libpics — PICS-client, C, built on libwww | open source, reference | not checked | https://www.w3.org/PICS-client/ |
| W3C Java PICS parsers (`w3c.pics.label`) | open source, reference | not checked | https://www.w3.org/PICS/refcode/Parser/PICSAPI.html |

Searched 2026-10-23. Both are W3C's own 1996–1998 reference code and
unmaintained. Browser-side consumers of the era (e.g. content-rating features
in 1990s browsers) were not verified against a primary source and are not
listed. Licences left unfilled rather than guessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`.** This pass (library#87) claims the **summary bar**: the
record is `summarized`, declares no `distillation` block and adds nothing to
`distilled/`, so FX-1 does not fire. FX-1 extraction of this record is owned by
library#89. It would add the *Detailed Syntax* BNF and
the HTTP and bureau query grammars as verbatim schema, the bureau exchange as a
protocol model, and the *Example* label lists as vectors.

**No verbatim normative text** beyond short, locator-bearing fragments; under
FX-1 that belongs in `distilled/normative.md`. The source uses no BCP 14
keywords.

## Limits

1. **Neither security feature is required**, and nothing obliges a client to
   check a MIC or a signature, or to reject a label that lacks one. The `signed`
   completeness request asks for a signature (*Detailed Syntax of HTTP Requests
   for Labels With Document*), but servers may ignore completeness.
2. **The signed bytes do not distinguish services.** The special form omits
   the service URL, so two services' labels with equal options and ratings
   sign identical bytes. Whether that matters depends on a
   key-per-service assumption the document makes but does not enforce
   ("PICS assumes that each service will distribute the public keys in some way
   it chooses."). DSig 1.0 puts the service URL into its canonical form
   (pics-dsig-1-0, *Canonicalization*).
3. **Multi-party labels are unsolved.** For a service that allows self-rating,
   labels "may need to be signed by both the service and the content producer",
   and "The PICS specification does not propose a solution to this problem"
   (*MICs and Digital Signatures*). No delegation from service to labeller is
   expressible — consistent with `ARCH-0001` §3.3 and R-001 §11.1.
4. **Binding by URL is advisory.** For a bureau label whose `for` differs from
   the requested URL, "a suspicious client may choose not to believe the
   suggestion" (*Response to Query for Labels Separate From Documents*), and
   ancestry is case-sensitive string matching. A generic label is a claim about
   a URL namespace, not about content.
5. **DSig 1.0 replaces both security options.** pics-dsig-1-0 declares
   `MIC-md5` and `signature-RSA-MD5` superseded by `resinfo` and `sigblock`,
   and in doing so drops this document's explicit rule for excluding embedded
   labels before hashing. That record carries a `contradicts` edge to this one,
   on the PICS 1.1 grammar; the reason is in its Limits 1.
6. **Status of PICS 1.2.** DSig 1.0's status section mentions an expected
   PICS 1.2; this record does not establish whether it was published.
