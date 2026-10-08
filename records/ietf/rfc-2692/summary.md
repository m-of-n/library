---
schema: "library-summary/v1"
id: rfc-2692
record: rfc-2692
type: summary
updated: "2026-10-08"
---

# SPKI Requirements

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | experimental — *"It does not specify an Internet standard of any kind"* (Status of this Memo) |
| **Authors** | C. Ellison (Intel) |
| **Published** | September 1999 |
| **Identifier** | RFC 2692 · DOI 10.17487/RFC2692 |
| **Source** | https://www.rfc-editor.org/rfc/rfc2692.txt |
| **Digest** | `6a88c1563590…` (sha-256 of the .txt, retrieved 2026-10-08) |
| **Length** | 787 lines; the requirements occupy roughly 3 pages and the rest is the use-case list they were derived from |

## Overview

RFC 2692 is the **working method, not the design**: the SPKI group *"first
established a list of things one might want to do with certificates … and then
summarized that list of desires into requirements"*, and this document is that
summary with the raw list attached. It is short, and it is the document that
makes `rfc-2693` legible, because almost every peculiarity of SPKI appears here
first as a demand rather than as a decision.

The pivotal paragraph is the one about Kohnfelder. Having traced the term
*certificate* to his 1978 thesis, the memo says the SPKI team *"directly
addressed the issue of `<name,key>` bindings and realized that such
certificates are of extremely limited use for trust management"*, because *"a
person's name is rarely of security interest"* and what a verifier needs is
*"whether a given keyholder has been granted some specific authorization."*
RFC 2693's entire architecture is that sentence worked out.

The rest divides into three things ARCH-0001 readers will recognise. **Who the
principal is**: *"The keyholder is most directly identified by the public key
itself"*, with indirection *"via a collision-free hash of the public key or via
a name, later to be resolved into a key."* **Who defines the vocabulary**:
*"The definition of attributes or authorizations in a certificate is up to the
author of code which uses the certificate"*, and creating a new authorization
*"should not require interaction with any other person or organization."*
**What a certificate should contain**: the least possible — *"like a single key
rather than a key ring or a single credit card rather than a whole wallet"* —
argued from privacy, because the aggregate of a keyholder's certificates
*"might constitute a dossier."*

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The requirements are security requirements, and the CRL section is a correctness argument about non-deterministic validation. |
| Cryptography | none | No primitive, no algorithm, no key format. |
| This project | core | The only place R-M-01 and R-O-03 are *argued* rather than asserted. |

Bears on **R-M-01** — this is where "not X.509 / PKIX" comes from, and the
reasoning is about who writes the code, not about the format's merits:
certificate generators will be *"written by many different developers,
frequently persons acting alone, operating out of garages or dorm rooms"*, so
*"No library code should be required for the packing or parsing of SPKI
certificates. In particular, ASN.1 is not to be used."* Also **R-M-02**
(key or key-hash as the identifier), **R-M-05** and **R-M-09** (the CRL
requirements below), **R-O-02** (CRLs vs positive on-line validation),
**R-O-03** (sign-as-transmitted, below), and **DEC-002**, which inherits the
encoding constraints this memo set.

## The encoding requirements, which are DEC-002's prehistory

Read as constraints on DEC-002, four of them are still live and one has aged
badly:

- *"A certificate should be signed exactly as it is transmitted. There should
  be no reformatting called for in the process of checking a certificate's
  signature"* — with the parenthetical concession *"although one might
  canonicalize white space during certificate input, for example, if the format
  is text."* This is **R-O-03's problem stated before any canonical form
  existed**, and the concession is the crack: the moment input is canonicalized,
  signed-as-transmitted is no longer true. `rfc-9804` §6.2 resolves it by
  signing the canonical form rather than the transmitted one, which is a
  different answer from the one asked for here.
- *"an SPKI certificate should be as simple as possible … a bare minimum of
  fields … an absolute minimum of optional fields"*, with the reason given
  sharply: *"the creator of a certificate is constrained by the structure
  definition, not by complaints (or error messages) from the reader."*
- **LR(0) and no recursion**: *"neither packing nor parsing of the structure
  should require a scan of the data"*, and *"packed and parsed without any
  recursion."* This has aged badly and is worth saying so — an S-expression is
  a tree, and `rfc-9804`'s canonical form is parsed with a stack or a
  recursion. The requirement was not met by the design it produced.
- Usability *"in very constrained environments, such as smart cards or small
  embedded systems"*, which is the same argument DEC-002's CBOR options make.

## Revocation: the requirement nobody else wrote down

The CRL paragraph is the most quotable thing in the memo and is directly
relevant to #14's *"what is revocation, and does anyone actually run it?"*. A
minimal CRL — a list, a sequence number and a signature, with transmission
unspecified — *"leads to non-deterministic program behavior"*, because whether
a certificate validates depends on which CRL the verifier happened to see. The
memo therefore requires that **if** SPKI uses CRLs, the certificate *"must
explicitly tell the verifier where to find the CRL, the CRL must carry explicit
validity dates and the dates of a sequence of CRLs must not overlap"* — under
which *"behavior of certificate validation is deterministic (aside from the
question of clock skew)."*

That is R-M-05's determinism requirement applied to revocation, and **no other
record in this lane states it.** RFC 5280 §6.3 gives a CRL processing
algorithm but no non-overlap rule and no requirement that the certificate point
at its own CRL (the CRL Distribution Points extension is optional). The memo
also reframes the mechanism: *"A CRL is a negative statement … the digital
equivalent of the little paper books of bad checks"*, replaced in retail by
positive on-line validation, so *"SPKI should support both positive and
negative on-line validations"* — and *"Any CRL or revalidation instrument must
have its own lifetime"*, with a zero lifetime ruled impossible by
communication delay and clock skew.

## Why `contradicts rfc-5280`

Three incompatible assertions, not a preference:

1. *"ASN.1 is not to be used"* and *"No library code should be required for the
   packing or parsing"* against RFC 5280, which is an ASN.1 profile whose
   Appendix A **is** a module and whose DN comparison rules (§7.1) are exactly
   the library-grade code this memo forbids.
2. *"signed exactly as it is transmitted … no reformatting"* against DER, which
   is a re-encoding rule applied before signature verification.
3. Determinism of validation under overlapping CRLs, above.

RFC 2693 §8 carries the same disagreement at the level of *what a certificate
is for*; this memo carries it at the level of *how one is encoded*. Both edges
are authored, because they are different claims.

## Implementations

**None, and that is the right answer for a requirements document.** Searched
2026-10-08: a requirements memo has no implementations of its own, and the
tooling that would implement its requirements is surveyed on `rfc-2693`
(JSDSI, libspki, the MIT SDSI/SPKI 2.0 distribution — all archival). The
`implementations` block here is deliberately empty with a search date rather
than copying that survey, which would drift.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on` |
| `summary.md` | this file — the only written artifact |

No `distilled/`. Summary bar, not FX-1; full extraction is owned by **#45**.

## Limits

- **It is a brainstorm, and labels itself one.** *"The list below is a
  brainstorming list, accumulated on the SPKI mailing list"* — roughly six of
  the document's thirteen pages. The entries are uneven (electronic cheques and
  security clearances beside *"my friend's political opinion (e.g., libertarian
  cypherpunk)"*) and none is traced to the requirement it produced. The
  derivation the abstract claims is not shown.
- **Requirements are written in lowercase "should".** There is no BCP 14
  keyword anywhere; every obligation is *should*, *must be able to* or *it is
  necessary*. Nothing here is testable as written, and an extraction will have
  to say so (`rfc-9804`'s record hit the same wall and recorded the lowercase
  ratio as the finding).
- **It does not define delegation.** Delegation appears once, in passing —
  certificates *"should be generated by any keyholder empowered to grant or
  delegate the authorization in question"* — with no depth rule, no boolean,
  no scoping. All of that is `rfc-2693` §4, so this record does **not** fill a
  column in #14's table; it explains why the SPKI column looks as it does.
- **It names SDSI as a dependency and does not resolve it.** *"The SDSI work of
  Rivest and Lampson has done an especially good job of defining and using
  local name spaces, therefore if possible SPKI should support the SDSI name
  construct. [Note: SPKI and SDSI have merged.]"* The reference `[SDSI]` is
  cited by `rfc-2693` and is not held. See this lane's topic answer.
- **Open Questions is honest and unhelpful.** Non-repudiation is dismissed as
  a private-key-protection problem; proving a negative needs *"all relevant
  records digitized and all parties have inescapable IDs"*, neither expected
  *"in our lifetimes"*; and the delegate who loans out a valuable private key
  is called *"a potential flaw in any system providing authorization and an
  interesting topic for study."* Our R-M-07/R-M-11 work on what a signature
  *cannot* establish is the same problem and gets no help here.
- **Anonymity and blinding are requirements this project has not considered.**
  *"It is necessary for at least some certificates to be anonymous"*, and a
  certificate *"must be able to assign an attribute to a blinded signature
  key."* ARCH-0001 has no requirement in that direction. Recorded as an
  unexamined divergence, not as a gap to close.
- **Security Considerations is one sentence**: *"Security issues are discussed
  throughout this memo."*
- **Read scope:** the whole document, except that the use-case list was read
  for the certificate-taxonomy entries (traditional / direct certificate) and
  skimmed otherwise.
