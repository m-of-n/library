---
schema: "library-summary/v1"
id: rfc-9580
record: rfc-9580
type: summary
updated: "2026-10-08"
---

# OpenPGP

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | P. Wouters, Ed. (Aiven), D. Huigens (Proton AG), J. Winter (Sequoia PGP), Y. Niibe (FSIJ) |
| **Published** | July 2024 |
| **Identifier** | RFC 9580 · DOI 10.17487/RFC9580 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9580.txt |
| **Digest** | `36540e57b63d…` (sha-256 of the .txt, retrieved 2026-10-08) |
| **Obsoletes** | RFC 4880 (OpenPGP Message Format), 5581 (Camellia), 6637 (ECC) — header |

## Overview

RFC 9580 is the current OpenPGP specification: packet formats, v6 keys and
signatures, the AEAD-protected data packets, and the signature subpacket
registry. It describes itself as *"only the format and methods needed to read,
check, generate, and write conforming packets"* and *"not a step-by-step
cookbook"*, and it is scrupulous about that boundary — which is what makes it
the most interesting record in this lane.

Its delegation mechanism is a **distinct, signed, scoped object**, and of the
four families compared for #14 it is the only one that is all three at once. A
**Trust Signature** subpacket (§5.2.3.21) carries *"1 octet 'level' (depth), 1
octet of trust amount"*: level 0 is an ordinary validity signature, level 1
asserts the signed key is *"a valid trusted introducer"*, level 2 asserts it is
trusted to issue level 1 trust signatures — *"that is, the signed key is a
'meta introducer'"* — and *"generally, a level n Trust Signature asserts that a
key is trusted to issue level n-1 Trust Signatures."* The trust amount is
0–255, where *"values less than 120 indicate partial trust and values of 120 or
greater indicate complete trust"*, with a SHOULD to emit 60 and 120.

Scoping is a separate subpacket. A **Regular Expression** (§5.2.3.22) is *"used
in conjunction with Trust Signature packets (of level > 0) to limit the scope
of trust that is extended"*, and the rule is exact: *"Only signatures by the
target key on User IDs that match the Regular Expression in the body of this
packet have trust extended by the Trust Signature subpacket."* So #14's
Alice/Bob/Carol case is directly expressible — Alice issues Bob a level-1
trust signature carrying a regular expression matching `@foo.com`, and Bob's
certification of `carol@bar.com` carries no trust for Alice. The grammar is
Henry Spencer's, restated in §8: branches, pieces with `*`/`+`/`?`, ranges,
and the anchors `^` and `$`.

Where trust starts is **nowhere in this document**, on purpose. The Trust
packet (§5.10) *"is used only within keyrings and is not normally exported"*,
records *"the user's specifications of which keyholders are trustworthy
introducers"*, and *"The format of Trust packets is defined by a given
implementation."* Local, unexported, unsigned, implementation-defined — the
same shape as RFC 2693's ACL and the same shape as ARCH-0001's unsigned local
trust root. OpenPGP ships the delegation *mechanism* and leaves the trust
*computation* out of the standard entirely; the phrase "web of trust" appears
in this document exactly once, in an informative reference.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A full key, signature and revocation model, with a long Security Considerations covering key-overwriting and signature-type confusion. |
| Cryptography | core | Specifies the primitives, key formats and AEAD constructions directly, not by reference. |
| This project | core | **R-I-04** names OpenPGP identity signatures explicitly, and §5.2.3.21–22 is the closest deployed analogue of a scoped delegation certificate. |

Bears on **R-I-04** directly — *"Import OpenPGP identity signatures as
`NameCert` and/or `Endorse`, never as `AuthzCert` unless an explicit profile
says so."* This document shows why that requirement is right and where it gets
hard: §5.2.1.4–7's four certification types (Generic 0x10, Persona 0x11,
Casual 0x12, Positive 0x13) are all name bindings and map cleanly to
`NameCert`, **but a level ≥ 1 Trust Signature is not a name binding** — it is
an assertion that a key may speak for others, which is an `AuthzCert`-shaped
claim riding on a `NameCert`-shaped object. R-I-04's "unless an explicit
profile says so" is exactly the escape hatch that needs writing, and
`R-I-01`'s mapping table is where the distinction has to be recorded.

Also **R-M-02** (a key is identified by fingerprint; §5.2.3.35 Issuer
Fingerprint), **R-M-08** (the regular expression is a name-scoping operator
with no stated intersection semantics — see Limits), **R-M-10** (integer
delegation depth, below), and **R-O-02** (§13.9's escrowed revocation
signatures, below).

## Why `contradicts rfc-2693`

Same design question, documented opposite answers, and the edge is authored
here because this is the later document.

RFC 2693 §4.1 records three camps on delegation depth and §4.1.4 chose
**boolean**: integer control *"was the original design and has appeal, but was
defeated by the inability to predict the proper depth of delegation"*, with the
supporting argument that *"there is no control on the width of the delegation
tree, so control on its depth is not a tight control on proliferation."*
RFC 9580 §5.2.3.21 is **integer control** — a level octet, with level n
trusted to issue level n-1.

Both cannot be right about whether depth control is workable, and the
disagreement is informative rather than academic for **R-M-10**, which
currently says *"Delegation SHALL be an explicit boolean (or equivalent)"*.
OpenPGP's twenty-five years of deployment is the evidence on the other side,
and the honest reading is that both are partly vindicated: the level octet is
*specified* and *implemented* (GnuPG `tsign`, Sequoia `sq pki vouch
authorize`), and in practice almost nothing beyond level 1 is used — which is
RFC 2693's prediction, not its refutation. A reviewer should treat this as a
live argument, not a settled one. The trust *amount* octet is a third axis
neither SPKI nor X.509 has: partial trust that composes across multiple
introducers, with no composition rule given here.

## Revocation, which is where this document is strongest

#14 asks what revocation is and whether anyone runs it, and OpenPGP has the
most interesting answer in the lane. §5.2.3.23's **Revocation Key** subpacket —
the original "designated revoker", i.e. delegation of revocation authority —
is now **deprecated**: *"This mechanism is deprecated. Applications MUST NOT
generate such a subpacket."*

What replaces it is not a mechanism but a **pattern**: §13.9's escrowed
Revocation Signature. Alice pre-signs her own revocation and hands it to a
third party to hold and publish. The document lists the advantages and one of
them is a judgement about deployment that is rare to see in an RFC:
*"Implementation support for enforcing a revocation from an authorized
Revocation Key subpacket is uneven and unreliable."* The others are
architecturally relevant to us — the keyholder *"can constrain what types of
revocation the preferred revoker can issue, by only escrowing those specific
signatures"*, there is *"no public/visible linkage between the keyholder and
the preferred revoker"*, and third parties verify without needing the revoker's
key at all.

**This is a delegation mechanism with no delegation object**, and it is worth
R-O-02's attention: capability-by-possession-of-a-pre-signed-statement, which
needs no revocation infrastructure, no online check and no policy. It is also
the one design in this lane that a group self-organising around `foo.com` with
no external CA could adopt unchanged.

Two further scoping controls belong in the same picture: §5.2.3.19
**Exportable Certification**, where a non-exportable certification is *"made by
a user to mark a key as valid within that user's implementation only"* and
*"MUST be marked as critical"* — a signature that is deliberately local, which
no other record here has; and §5.2.3.29 **Key Flags**, whose usage note is the
cleanest statement of a problem this project also has: the same flags *"mean
different things depending on who is making the statement"*, a self-signature
expressing a preference where a certification expresses a constraint.

## Implementations

Searched 2026-10-08. OpenPGP is the only family in this lane where the scoped
delegation mechanism is reachable from a command line, so the notes record
*what the tool does with trust signatures*, not just that the tool exists.

| Name | Kind | Language | URL |
|---|---|---|---|
| GnuPG | open source | C | https://gnupg.org/ |
| Sequoia PGP | open source | Rust | https://sequoia-pgp.org/ |
| OpenPGP.js | open source | JavaScript | https://openpgpjs.org/ |
| rpgp | open source | Rust | https://github.com/rpgp/rpgp |
| Ribose RNP | open source | C++ | https://www.rnpgp.org/ |

**Two deployment findings that #14 should use, both secondary sources:**

- GnuPG emits trust signatures with `tsign` / `tlsign`, but community reports
  describe it as supporting effectively **one shape** of regular expression —
  bracketed between `<[^>]+[@.]` and `>$` — rather than the §8 grammar.
- `dev.gnupg.org` **T6238**, *"regexp for trust signature domain restriction
  does not work if key only has an e-mail address"*, is a live defect in the
  exact feature #14 is asking about: the domain restriction fails for a User ID
  with no name part, which is the common modern shape.

So the honest answer to *"can delegation be scoped?"* for OpenPGP is **yes in
the specification, partially in the dominant implementation**. Sequoia's
`sq pki link authorize` and `sq pki vouch authorize` expose the mechanism more
fully. Both are mailing-list and bug-tracker sources, not records, and a report
citing them should say so.

Commercial: none found on 2026-10-08. OpenPGP's commercial surface is hosted
mail (Proton) and support contracts around GnuPG rather than proprietary
implementations of the format.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey |
| `summary.md` | this file — the only written artifact |

No `distilled/`. Summary bar, not FX-1; full extraction is owned by **#45**.

## Limits

- **No trust computation anywhere.** The level octet, the trust amount and the
  regular expression are *carried*; nothing says how a relying party combines
  two partial-trust introducers, what happens when a level-2 introducer's
  regular expression is wider than its own issuer's, or in what order
  signatures are evaluated. RFC 2693 §6.3 at least sketches a reduction
  algorithm and states its composition rule; this document deliberately
  sketches none. **R-M-05's determinism requirement is unmet by OpenPGP**, and
  that is a specification choice, not an oversight.
- **Regular-expression scoping has no stated intersection rule.** X.509 §6.1.4(g)
  says permitted subtrees intersect along the path and excluded subtrees union;
  SPKI §6.3.1 defines AIntersect. §5.2.3.22 says only which signatures *"have
  trust extended"* by one subpacket. Whether a meta-introducer's expression
  constrains its delegates' expressions is undefined, which is the difference
  between a scoping mechanism and a scoping *algebra* — and R-M-08 wants the
  algebra.
- **The match is not anchored and the spec does not say whether it should be.**
  §5.2.3.22 says the expression *"matches (or does not match) a sequence of
  UTF-8-encoded Unicode characters from User IDs"*; §8 provides `^` and `$` but
  requires neither. An unanchored `@foo\.com` matches a User ID containing that
  text anywhere, so whether `Eve <eve@evil.com> (@foo.com)` matches depends on
  the implementation. The GnuPG convention of always emitting `…>$` reads as a
  workaround for precisely this, and T6238 is what happens when the convention
  meets a User ID it did not anticipate.
- **Scoping is over User ID *strings*, not over authority.** A trust signature
  restricts *which names* a delegate may vouch for. It cannot say "Bob may
  vouch for `*@foo.com` **about code signing**" — there is no authorization
  field and no tag. Same structural limit as X.509 name constraints, and the
  same reason both differ from the SPKI/ARCH-0001 model: the object delegated
  is naming authority, not speaking authority.
- **Certification types are specified and then conceded to be unused.**
  §5.2.1.7 states it plainly: *"Most OpenPGP implementations make their 'key
  signatures' as generic (Type ID 0x10) certifications. Some implementations
  can issue 0x11-0x13 certifications, but few differentiate between the
  types."* An assurance-level field nobody populates is a cautionary precedent
  for any confidence or assurance field this project might add.
- **Read scope is narrow.** §5.2.1 (signature types), §5.2.3.19–24, §5.2.3.29,
  §5.2.3.35, §5.10, §8 and §13.9. The packet syntax (§4), key material and v6
  key formats (§5.5), the AEAD and SEIPD packets (§5.13), the algorithm
  registries (§9), the armor and cleartext formats (§6–7), and the whole of
  §12–§13 except §13.9 are **not** covered. Anything #14 says about OpenPGP
  key distribution, WKD, keyservers or algorithm agility is not sourced here.
- **Keyserver and distribution policy is out of scope for the RFC**, so "who
  decides the root" has no answer in this document beyond §5.10's "the local
  keyring, in a format the implementation chose." For #14 that is the honest
  entry: the root is *a keyring you built*, and the standard declines to say
  how.
