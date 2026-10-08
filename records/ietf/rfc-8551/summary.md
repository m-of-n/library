---
schema: "library-summary/v1"
id: rfc-8551
record: rfc-8551
type: summary
updated: "2026-10-08"
---

# S/MIME Version 4.0 Message Specification

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | J. Schaad (August Cellars), B. Ramsdell (Brute Squad Labs), S. Turner (sn3rd) |
| **Published** | April 2019 |
| **Identifier** | RFC 8551 · DOI 10.17487/RFC8551 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8551.txt |
| **Digest** | `dac39f749a08…` (sha-256 of the .txt, retrieved 2026-10-08) |
| **Obsoletes** | RFC 5751 (header) |

## Overview

RFC 8551 defines how to wrap a MIME body part in CMS so that mail can be
signed, encrypted, authenticated-encrypted or compressed, and how to carry the
result as `application/pkcs7-mime` or as a detached
`application/pkcs7-signature` inside `multipart/signed`. Its substance is
plumbing: which CMS content types are used, which algorithms are mandatory at
which key sizes, the MIME canonicalization and transfer-encoding rules a
signature has to survive, and the `smime-type` parameter that tells a receiver
what it is holding.

**It specifies no trust model and no delegation.** The whole of its position on
the question is §4: *"This specification does not cover how S/MIME agents
handle certificates — only what they do after a certificate has been validated
or rejected."* Everything about identity, path building and trust anchors is a
different document, and the identity model S/MIME therefore has is X.509's,
unchanged, via `rfc-5280`.

For #14's table this is the answer, and it is a negative one: **S/MIME is not a
fifth trust model.** It is a message format that consumes whatever PKIX
decides. The row should say so rather than restating the X.509 row in different
words, and the only distinctively S/MIME contribution to delegation is a
transport convenience — §3.8's *"certs-only"* message, which carries
certificates and CRLs in a `SignedData` with *"the SignedData encapContentInfo
eContent field MUST be absent, and the signerInfos field MUST be empty"*, i.e.
an envelope with no signature and no content whose only job is to move
credentials around.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | It profiles algorithms and key sizes, and §6 is a long and careful discussion of historic-mail downgrade — but it decides nothing about trust. |
| Cryptography | adjacent | Mandates algorithm choices (§2.1–2.3, §4.1–4.5) by reference; defines no primitive. |
| This project | adjacent | Not a model we compare against. It is the **incumbent deployment** of the thing ARCH-0001's email example is about, which is why the comparison includes it. |

Bears on **R-I-01** — if this project ever claims S/MIME interchange, the
mapping table has to state that the identity half comes from PKIX and this
document contributes only the envelope — and **R-I-05**, for the same reason:
an imported S/MIME signer identity *is* an X.509 identity assertion and must be
marked `provenance: x509`, not treated as a second kind of claim. It bears on
no other `R-*` or `DEC-*`, and inventing more would be dishonest.

## The pointer in §4 is to the wrong document

A defect worth recording, because a reader following it lands a version
behind. §4 says *"S/MIME certificate issues are covered in [RFC5750]"* —
RFC 5750 is the **v3.2** Certificate Handling specification. RFC 8551's own
companion is **RFC 8550**, *S/MIME Version 4.0 Certificate Handling*, published
the same month by the same authors; RFC 8551 cites RFC 8550 only in §7.3's
`[SMIMEv4]` reference-convention list, never from the normative text that
sends the reader after certificates.

So the one cross-reference in this document that a reader following the
delegation question would actually follow points at the superseded companion.
We hold `rfc-8550` as a stub; it, not this record, is where S/MIME's position
on name constraints, trust anchors and email-address matching lives, and it is
the next thing to ingest if #14 wants more than "S/MIME inherits PKIX".

## What it does contribute: canonicalization, which bears on R-O-05's problem

§3.1 is the only part of this document that is architecturally interesting to
us, and it is interesting by analogy rather than by relevance. A MIME entity
must be canonicalized before signing — line endings normalised, transfer
encodings chosen so the bytes survive relaying — because the signature covers
a representation that intermediaries are entitled to rewrite. That is the same
shape of problem as R-O-03/R-O-05: *what exactly did the signature cover, and
who is allowed to touch it afterwards.* S/MIME's answer is to pin a transfer
encoding and canonical form per content type; `rfc-9804` §6.2's answer is a
canonical form for signing distinct from a display form. Noted as a parallel,
not as evidence for a decision — nothing here constrains DEC-002.

## Implementations

Searched 2026-10-08. A web search for RFC 8551 conformance returned only
mirrors of the RFC itself and no implementation conformance statement naming
8551 specifically, so the list below is by what implements S/MIME 4.0's
mechanisms, not by a claimed conformance badge. That is a weaker result than
`rfc-9804`'s Appendix A survey and is stated as such.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL (`openssl cms`, `openssl smime`) | open source | Apache-2.0 | https://docs.openssl.org/master/man1/openssl-cms/ |
| Bouncy Castle (`bcmail`, `bcpkix`) | open source | MIT-style | https://www.bouncycastle.org/ |
| Mozilla Thunderbird (via NSS) | open source | MPL-2.0 | https://www.thunderbird.net/ |
| Microsoft Outlook / Exchange | commercial | — | https://learn.microsoft.com/en-us/exchange/policy-and-compliance/smime |
| Apple Mail | commercial | — | https://support.apple.com/guide/mail/welcome/mac |

Unlike the other records in this lane, **the commercial column is the
important one**: S/MIME's deployment is enterprise mail clients with an
inherited CA bundle, which is exactly #14's *"who decides the root"* question
answered by "your IT department did."

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey |
| `summary.md` | this file — the only written artifact |

No `distilled/`. Summary bar, not FX-1; full extraction is owned by **#45**.

## Limits

- **It answers almost nothing #14 asks.** Of the five specific questions —
  name-range restriction, delegation as a distinct object, who decides the
  root, revocation in practice, and the no-external-CA group — this document
  addresses **none**. That is the finding, and the record exists so the report
  does not have to guess.
- **It does not bind an email address to a key.** Despite being the email
  security standard, the `rfc822Name`/`emailAddress` binding is in `rfc-5280`
  §4.2.1.6 and `rfc-8550`; this document's §1.2 merely defines a certificate as
  *"a type that binds an entity's name to a public key"* and moves on. #14's
  premise that *"everyone can bind an email address to a key"* is true of
  S/MIME only through PKIX.
- **Read scope:** header, Abstract, §1.1–§1.2, §3.8–§3.9, §4, §6 (the
  historic-mail and key-size discussion only), §7.2–§7.3 references, and the
  §3.1 canonicalization rules at a structural level. §2 (CMS options and
  attributes in detail), §3.2–§3.7, §5 (IANA) and Appendices A–B (ASN.1
  module, historic mail) were not covered.
- **`rfc-8550` is the gap this record exposes, not fills.** It is held as a
  stub with no summary. Everything about S/MIME trust is there. This lane did
  not ingest or summarise it: the issue scopes six records and widening is
  forbidden, and the honest alternative — pretending §4's pointer is enough —
  would have been worse. Named in the topic answer as the next step for #14.
- **No `contradicts` edge, deliberately.** `rfc-2693` contradicts *this*
  document's §1.2 definition of a certificate, and that edge is authored there
  with the argument. Nothing in this document asserts anything incompatible
  with anything else we hold, because it asserts almost nothing about trust at
  all — which is itself the point.
