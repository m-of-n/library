---
schema: "library-summary/v1"
id: rfc-5280
record: rfc-5280
type: summary
updated: "2026-10-08"
---

# Internet X.509 Public Key Infrastructure Certificate and CRL Profile

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | D. Cooper (NIST), S. Santesson (Microsoft), S. Farrell (Trinity College Dublin), S. Boeyen (Entrust), R. Housley (Vigil Security), W. Polk (NIST) |
| **Published** | May 2008 |
| **Identifier** | RFC 5280 · DOI 10.17487/RFC5280 |
| **Source** | https://www.rfc-editor.org/rfc/rfc5280.txt |
| **Digest** | `a2f2628c0a83…` (sha-256 of the .txt, retrieved 2026-10-08) |
| **Obsoletes** | RFC 3280, 4325, 4630 (header) |
| **Updated by** | RFC 6818, 9549, 9598, 9608, 9618 — all held; see Limits |

## Overview

RFC 5280 profiles the X.509 v3 certificate and v2 CRL for Internet use: which
fields and extensions conform, how Internet name forms are carried, and — in
§6 — an algorithm for deciding whether a chain of such certificates
authorises a conclusion. The model is a **name-binding** one: a CA signs a
subject name together with a public key, and delegation happens when the
subject is itself a CA.

Delegation is therefore not a distinct object. It is **three flags on the same
object**: the `cA` boolean in Basic Constraints (§4.2.1.9), which decides
whether the key *"may be used to verify certificate signatures"*; the
`keyCertSign` bit in Key Usage (§4.2.1.3), which must agree with it; and
`pathLenConstraint`, which *"gives the maximum number of non-self-issued
intermediate certificates that may follow this certificate in a valid
certification path."* There is no separate delegation certificate and no
authorization field — an X.509v3 certificate that carries an authorization
carries it in an extension whose meaning is documented outside the RFC.

Trust starts at a **trust anchor**, which this document declines to define:
*"The selection of a trust anchor is a matter of policy: it could be the top CA
in a hierarchical PKI, the CA that issued the verifier's own certificate(s), or
any other CA in a network PKI"* (§6), and it is *"an input to the algorithm"*
with *"no requirement that the same trust anchor be used to validate all
certification paths"* (§6.1). §6.2 adds that *"the selection of one or more
trusted CAs is a local decision."* The CA bundle a reader inherits is not in
this specification; it is the convention that grew around it.

## §4.2.1.10 Name Constraints — the section #19 Stage 2 named

This is X.509's scoped delegation, and it is better than the PKI's reputation
for it. The extension *"MUST be used only in a CA certificate"* and *"indicates
a name space within which all subject names in subsequent certificates in a
certification path MUST be located"*, as **permitted** and **excluded**
subtrees, with exclusion winning: *"Any name matching a restriction in the
excludedSubtrees field is invalid regardless of information appearing in the
permittedSubtrees."* Conforming CAs MUST mark it critical and MUST NOT issue an
empty one.

The per-name-form rules answer #14's Alice/Bob/Carol question directly. For
**Internet mail addresses** a constraint *"MAY specify a particular mailbox,
all addresses at a particular host, or all mailboxes in a domain"* — so
`root@example.com` is one mailbox, `example.com` is every mailbox on that host,
and `.example.com` is *"all the Internet mail addresses in the domain
`example.com`, but not Internet mail addresses on the host `example.com`."*
**So `*@foo.com` is expressible**: Alice, as a CA, issues Bob a CA certificate
with `permittedSubtrees` containing an `rfc822Name` of `foo.com`, and Bob
cannot then certify `carol@bar.com`. For DNS names, *"Any DNS name that can be
constructed by simply adding zero or more labels to the left-hand side of the
name satisfies the name constraint"*; for IP addresses the field is CIDR —
eight octets for IPv4, so `192.0.2.0/24` is `C0 00 02 00 FF FF FF 00`.

**§6.1.4(g) is the mechanism, and it is SPKI's AIntersect under another
name.** Walking the path, `permittedSubtrees` becomes *"the intersection of its
previous value and the value indicated in the extension field"* and
`excludedSubtrees` becomes the **union** of its previous value and the new one.
The worked example in the text is *"the intersection of example.com and
foo.example.com is foo.example.com. And the intersection of example.com and
example.net is the empty set."* Monotone narrowing along a chain, exactly like
RFC 2693 §6.3 — the difference is **what** is narrowed. X.509 narrows the set
of *names a delegate may certify*; SPKI narrows the *authority a delegate may
pass on*. That distinction is this lane's finding and it is what the #14 table
should turn on.

### Where it leaks

Four limits are in the section's own text, and a reader should not take the
mechanism as airtight:

- **Per-name-form, and silent when absent.** *"Restrictions apply only when the
  specified name form is present. If no name of the type is in the certificate,
  the certificate is acceptable."* A certificate constrained on `rfc822Name`
  that carries no `rfc822Name` is unconstrained.
- **Processing is only partly mandatory.** Applications *"MUST be able to
  process name constraints that are imposed on the directoryName name form and
  SHOULD be able to process"* them on `rfc822Name`, `uniformResourceIdentifier`,
  `dNSName` and `iPAddress`. The critical bit is the backstop: a conforming
  application faced with a critical constraint on a name form it does not
  implement MUST *"either process the constraint or reject the certificate"* —
  which converts an unimplemented constraint into a compatibility failure, not
  a security failure. That is the right design and it is also why CAs avoid it.
- **Self-issued certificates are exempt** *"unless the certificate is the final
  certificate in the path"*, with the reason given in parentheses: otherwise
  name constraints would break key rollover.
- **`directoryName` comparison is a known swamp.** Implementations MUST perform
  the §7.1 DN comparison rules, but CAs *"SHOULD NOT rely on implementation of
  the full ISO DN name comparison algorithm"*, which *"implies name
  restrictions MUST be stated identically to the encoding used in the subject
  field."* A constraint that matches only byte-identically-encoded DNs is a
  fragile constraint.

### Does anyone use them?

#14 asks this explicitly, so it is answered here with locators rather than
left to the report. The evidence found on 2026-10-08 is consistent and
negative, and all of it is **secondary** — none of it is a library record, and
a report citing it should say so:

| Source | What it says | Locator |
|---|---|---|
| EFF SSL Observatory thread, April 2011 | Two certificates with name constraints in the whole dataset; thread title is *"Name constraints: a reasonable idea that hasn't panned out in practice"* | lists.eff.org/pipermail/observatory/2011-April/000174.html |
| Mozilla CA policy wiki | A page maintained specifically for name-constrained CAs, i.e. the case is special enough to need one | wiki.mozilla.org/CA:NameConstraints |
| openssl-dev, May 2016 | *"[openssl.org #3502] nameConstraints bypass bug"* — the mechanism has had implementation defects in the most-deployed stack | mta.openssl.org/pipermail/openssl-dev/2016-May/007225.html |

The commonly repeated explanations — that CA/Browser Forum rules and
commercial incentives discourage selling name-constrained subordinate CAs, and
that usage is near zero outside the US Federal Bridge — are **assertions from
mailing lists and blog posts, not from a measured study**, and this record does
not endorse them. If #14 wants to make the "nobody uses them" claim load-
bearing, it needs a current scan of CT logs or a dated survey record, and
neither exists in this library. That is a genuine ingestion gap and it is
recorded in this lane's topic answer rather than papered over.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is the path-validation algorithm the Internet's trust decisions run on. |
| Cryptography | adjacent | Profiles algorithm identifiers and signature fields; defines no primitive. |
| This project | core | **R-M-01** names this document as the thing the native encoding SHALL NOT be. |

Bears on **R-M-01** (the negative requirement is about *this* profile, so the
claim is only defensible with the record read), **R-M-03** by contrast (names
here are global and hierarchical, subordinate *"in the X.500 naming tree"* under
the RFC 1422 rule §3.2 recounts — the opposite of issuer-relative), **R-M-10**
(`pathLenConstraint` is the *integer* delegation control RFC 2693 §4.1.3
rejected; X.509 has the finer mechanism and SPKI declined it), **R-I-01** and
**R-I-05** (any claimed X.509 import mapping has to say what happens to
`cA`, `pathLenConstraint`, `nameConstraints`, `keyUsage`, `extendedKeyUsage`
and the policy tree — this record is where that table comes from), **R-I-02**
(§6.1's trust anchor is an *input*, which is the shape R-I-02 wants and is
easy to misread as requiring a native anchor), and **R-O-02** (§5 and §6.3 are
the revocation design R-O-02 prefers short-lived validity over).

## Implementations

Searched 2026-10-08. Unlike SPKI, the problem here is abundance, not scarcity;
listed by what a reader would reach for, and name-constraint support is the
column that matters for this lane.

| Name | Kind | Language | URL |
|---|---|---|---|
| OpenSSL | open source | C | https://www.openssl.org/ |
| Go `crypto/x509` | open source | Go | https://pkg.go.dev/crypto/x509 |
| mozilla::pkix / NSS | open source | C++ | https://firefox-source-docs.mozilla.org/security/nss/ |
| rustls / webpki | open source | Rust | https://github.com/rustls/webpki |
| Bouncy Castle | open source | Java | https://www.bouncycastle.org/ |
| GnuTLS | open source | C | https://www.gnutls.org/ |

Commercial: not surveyed — every CA product and every OS trust store
implements this profile, so the list would be a list of the industry and would
inform nothing. Recorded as a deliberate non-search, not an empty section.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey |
| `summary.md` | this file — the only written artifact |

No `distilled/`. Summary bar, not FX-1; full extraction is owned by **#45**.

## Limits

- **Read scope is narrow and deliberately so.** §1, §3.2, §4.2.1.9, §4.2.1.10,
  §6 preamble, §6.1, §6.1.4(g) and §6.2. The document is 8,459 lines; the
  certificate-field profile (§4.1), the policy and policy-mapping machinery
  (§4.2.1.4, §4.2.1.11–13, §6.1.3–6.1.5), the whole CRL profile (§5), CRL
  processing (§6.3), name matching and internationalization (§7) and the ASN.1
  modules (Appendices A–B) are **not** covered. Anything #14 says about policy
  constraints, `inhibitAnyPolicy` or CRL mechanics is not sourced from this
  summary.
- **The `updates` edges are not wired.** RFC 6818, 9549, 9598, 9608 and 9618
  each carry `Updates: 5280` in their own headers and all five are held in this
  library, so five `updates: [rfc-5280]` edges are missing from the crosswalk.
  They belong on *those* records — inverses are derived, never authored
  (`docs/references.md` §2) — so this lane wires them there and does not
  author `updated_by` here. **RFC 9598 matters most for #14**: it is the
  internationalized-email-address update, so the mail-address constraint rules
  quoted above are as of 2008 and not the current state.
- **Name constraints constrain names, not authority.** A name-constrained
  subordinate CA is still a CA for everything *within* its subtree: every key
  usage, every extended key usage, every policy. There is no way to say "Bob
  may certify `*@foo.com` **for code signing only**" in this extension; that
  needs `extendedKeyUsage` plus §4.2.1.12's rules, which this read did not
  cover. #14's *"can delegation be scoped?"* has two answers for X.509 — yes
  over names, and separately over purposes — and they compose only through the
  path-validation algorithm, not in one field.
- **No authorization object at all.** §3.2's model has nothing corresponding to
  an SPKI tag. X.509 attribute certificates are a different document (RFC 5755,
  not held); what RFC 2693 §3.2 calls the X.509v3 route — authorization carried
  in an extension — makes the issuer *"an authority on both the authorization
  and the name"*, which is the construct RFC 2693 §8 argues against.
- **Revocation is specified but its operation is out of scope.** This document
  gives the CRL format and a processing algorithm; whether a relying party
  fetches, whether a CRL is current, and what happens on failure are not
  decided here. §6.3's CRL must share a trust anchor with the certificate path.
  #14's *"does anyone actually run it?"* cannot be answered from this record —
  OCSP (`rfc-6960`), must-staple (`rfc-7633`), `rfc-9608`'s
  no-revocation-available extension and Certificate Transparency
  (`rfc-6962`, `rfc-9162`) are all held as stubs and all bear on it.
- **It does not contradict `rfc-2693`; `rfc-2693` contradicts it.** The edge is
  authored on the SPKI records with the argument, because the disagreement is
  theirs: this document states a profile and makes no claim that the name-
  binding model is the right one. Keeping the direction straight matters for
  the crosswalk — RFC 5280 is the incumbent, not a disputant.
