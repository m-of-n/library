---
schema: "library-summary/v1"
id: rfc-2693
record: rfc-2693
type: summary
updated: "2026-10-08"
---

# SPKI Certificate Theory

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | experimental — *"does not specify an Internet standard of any kind"* (Status of this Memo) |
| **Authors** | C. Ellison (Intel), B. Frantz (Electric Communities), B. Lampson (Microsoft), R. Rivest (MIT LCS), B. Thomas (Southwestern Bell), T. Ylonen (SSH) |
| **Published** | September 1999 |
| **Identifier** | RFC 2693 · DOI 10.17487/RFC2693 |
| **Source** | https://www.rfc-editor.org/rfc/rfc2693.txt |
| **Digest** | `6822d668195c…` (sha-256 of the .txt, retrieved 2026-10-08) |

## Overview

RFC 2693 argues that a certificate's job is **authorization, not
authentication**, and then builds the machinery that follows from taking that
seriously. Its claim is that the `<name,key>` certificate inherited from
Kohnfelder answers the wrong question: an application almost never decides on
the spelling of a name (§2.4), so the useful binding is `authorization -> key`
rather than `authorization -> name` plus `name -> key`. §8 makes the security
argument for that preference concrete — the two-certificate construct needs
**two** issuers to be trustworthy instead of one, and its join is by a name
string that one of the two issuers must have drawn from a foreign name space,
which is *"more complex than string matching and might even involve a human
guess."*

Where names are still wanted, they are **local**: a SDSI name is
`(name fred)` in the name space defined by a key, chained as
`(name fred sam)` (§2.6), and the convention preserved from SDSI 1.0 is that
*"if a (local) SDSI name occurs within a certificate, then the public key of
the issuer is the identifier of the name space in which that name is
defined"* (§2.8). There is no global name space and no root.

The document's operational core is §6, **tuple reduction**. Certificates of
any format — X.509v1, PGP, X.509v3, X9.57, SDSI 1.0, SPKI, SSL (§6.5) — are
first verified and then translated into a uniform intermediate form, so the
authorization computation is one algorithm over heterogeneous inputs. An
authorization **5-tuple** is `<Issuer, Subject, Delegation, Authorization,
Validity>`; a name **4-tuple** is `<Issuer, Name, Subject, Validity>`. Two
5-tuples compose into `<I1,S2,D2,AIntersect(A1,A2),VIntersect(V1,V2)>` only
when `S1 = I2` **and** `D1 = TRUE` (§6.3) — authority is monotonically
narrowed along a chain and never widened.

Where the chain stops is an **ACL**, and the ACL is the point #14's "ours"
column is already standing on: *"An ACL entry has potentially the same
content as a certificate body, but has no Issuer (and is not signed)"*
(§1.1). The source of empowerment is a local, unsigned list.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is an access-control architecture, and §8 is an explicit comparison of the attack surface of two certificate constructs. |
| Cryptography | none | Defines no primitives and names no algorithm. A PRINCIPAL is just *"a cryptographic key, capable of generating a digital signature"* (§1.1). |
| This project | core | The direct ancestor. Four of ARCH-0001 §5.1's model requirements are this document restated. |

Bears on **R-M-02** (§2.7: the public key, or a collision-free hash of it, *is*
the identifier), **R-M-03** (§2.8: names interpreted only relative to an
issuing key), **R-M-04** (§6.1 vs §6.2: the 5-tuple and the 4-tuple are
separate intermediate forms because an authorization certificate and a name
certificate are *"qualitatively different"*), **R-M-05** (§6.3 is the
composition rule, and it is deterministic because §6.3.4 puts path ordering on
the prover, not the verifier), **R-M-08** (§6.3.1 AIntersect is the tag
intersection semantics), **R-M-06** (§6.3.3 threshold subjects, K of N, with no
CA hierarchy anywhere), **R-M-09** (§6.3.2 VIntersect, time window intersected
with online-test results), **R-M-10** (§4.1.4 chose a **boolean**), **R-O-02**
(§5.6 argues short-lived certificates often beat certificate-plus-online-test),
and **DEC-004 option 1**, which is this document's §6.3.1 tag language
verbatim.

## Scoping, which is what #14 asks about

The answer is yes, and by more than prefix. §6.3.1 defines four `*`-forms
inside an authorization:

| Form | Meaning |
|---|---|
| `(*)` | all S-expressions and byte strings; intersecting it yields the other operand |
| `(* set <tag-expr>*)` | the listed elements |
| `(* prefix <byte-string>)` | all byte strings starting with the given one |
| `(* range <ordering> <lower>? <upper>?)` | all byte strings lexically or numerically between the limits, with `<ordering>` one of alpha, numeric, time, binary, date |

Two structural rules carry the weight. *"Additional elements of a list must
restrict the permission granted"* — so a longer list is the result of
intersecting it with a shorter one, and a short list behaves as if padded with
implicit `(*)` entries. And the authorization vocabulary itself is **not
registered**: *"The definition of attributes or authorizations in a certificate
is up to the author of code which uses the certificate"* (RFC 2692). So the
range scoping #14's "ours" column claims is in print here from 1999 — but as
an algebra over application-defined byte strings, not over a vocabulary anyone
agreed on. That gap is DEC-004's whole problem, and this document does not
close it.

## Delegation depth — the decision, and who disagrees

§4.1 records three camps and the reasoning, which is the most reusable page in
the document. **No control**: restricting delegation is futile because the
keyholder can loan out the key or run a signing oracle. **Integer control**:
limit the depth to limit proliferation. **Boolean control**: you sometimes need
to say "not further", and the worked example is the US Commerce Department
wanting a direct legal agreement with each manufacturer.

Boolean won (§4.1.4). Integer control *"was the original design and has
appeal, but was defeated by the inability to predict the proper depth of
delegation"*, with the added argument that *"there is no control on the width
of the delegation tree, so control on its depth is not a tight control on
proliferation."* §4.2 then declines to separate delegators from exercisers,
because a delegator can always mint a key and delegate to itself.

**This is where `rfc-9580` contradicts this record.** OpenPGP's Trust
Signature subpacket (RFC 9580 §5.2.3.21) is *integer* control — level n is
trusted to issue level n-1 — which is precisely the option this working group
considered and rejected. Two prior-art sources, same design question, opposite
answers; the `contradicts` edge is authored on `rfc-9580` and the argument is
recorded in both summaries.

## Why `contradicts rfc-5280` and `contradicts rfc-8551`

Not a style disagreement. The three documents define the same word
incompatibly and cannot both be right about what certificates are for:

- RFC 8551 §1.2: a Certificate *"binds an entity's name to a public key with a
  digital signature."*
- RFC 5280 profiles exactly that object as the Internet PKI.
- RFC 2693 §1.1: a CERTIFICATE is *"a signed instrument that empowers the
  Subject"*, and its companion RFC 2692 says name-key certificates *"are of
  extremely limited use for trust management."*

§8 is the load-bearing claim: the `(authorization->name) + (name->key)`
construct that X.509 attribute certificates require is **less secure** than
`(authorization->key)`, for two stated reasons — one more issuer to subvert,
and a cross-name-space string match in the join. §8 also states its own
exception honestly: if both certificates come from the same issuer and
therefore the same name space, *"both of the security differentiators above are
canceled."* A reviewer should hold us to that caveat, because it is the case
most real S/MIME deployments are in.

## Implementations

Searched 2026-10-08. All three are **archival**; none is a maintained
dependency, and this is the honest state of SPKI tooling.

| Name | Kind | Language | URL |
|---|---|---|---|
| JSDSI | open source | Java | https://jsdsi.sourceforge.net/ |
| libspki (N. Möller) | open source | C | announcement on gcrypt-devel, March 2003 |
| MIT SDSI/SPKI 2.0 distribution | open source | — | https://toc.csail.mit.edu/node/213 |

**A naming trap, recorded because it will mislead someone.** OpenSSL and
Ruby's `OpenSSL::Netscape::SPKI` use "SPKI" for Netscape **SPKAC** (Signed
Public Key And Challenge), a `<keygen>`-era enrolment blob. Ruby's own
documentation cites RFC 2692 and RFC 2693 for it. That citation is wrong: SPKAC
has no tag, no delegation bit and no reduction, and shares nothing with this
document but four letters. Searching for "SPKI implementations" returns it
first.

The live reading of SPKI is therefore **not** its own stack but its
descendants — Macaroons, Biscuit, UCAN — which #19 owns and this lane
deliberately did not ingest.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey |
| `summary.md` | this file — the only written artifact |

No `distilled/`. This record is at the **summary bar**, not FX-1; the full
extraction is owned by **#45**.

## Limits

- **It is theory, and says so.** The abstract promises the reasoning *"without
  going into technical detail about those structures."* The structure document
  is `draft-ietf-spki-cert-structure`, which **expired and was never
  published** — so the normative encoding of the model this project descends
  from does not exist as an RFC. `rfc-9804` published only the S-expression
  layer, thirty years later.
- **§6 is explicitly non-normative.** *"The processing plan presented here is
  an example that may be followed, but its primary purpose is to clarify the
  semantics."* R-M-05 demands determinism; this document demonstrates it
  without requiring it, and the demonstration has gaps — AIntersect's rules
  are given by example over a handful of cases, and *"special semantics would
  require special reduction software."*
- **Tag equality is undefined at the byte level.** AIntersect matches *"element
  for element"* with no statement about encoding, case or normalisation. Two
  tags that a human reads as equal need not intersect. DEC-002 and DEC-004
  inherit this, and `rfc-9804` §4.7 leaves octet-string equivalence
  application-variable, so the gap is not closed downstream either.
- **Threshold reduction is sketched, not specified.** §6.3.3 describes
  selecting K of N and setting the rest to `(null)`, but gives no rule for
  which K, no failure semantics when more than K reduce, and no worked example.
  R-M-06 will need more than this.
- **Revocation is unresolved in the document itself.** §5.7.2 records Rivest's
  argument that *"the whole validity condition model is flawed"* because the
  verifier, not the issuer, carries the risk — and then concedes it *"is not
  reflected in the SPKI structure definition."* R-O-02 picks a side this
  document left open.
- **Delegation is boolean, so authority cannot be attenuated in depth** — only
  in tag and in time. #14's table should not read the SPKI column as
  unconditionally richer than X.509's `pathLenConstraint`; on depth, X.509 has
  the finer control and SPKI rejected it on purpose.
- **No answer to the oracle problem.** §4.1.1's objection survives the vote:
  nothing in any of these designs stops a delegate from proxying its key.
  RFC 2692's Open Questions names it and calls it *"a potential flaw in any
  system providing authorization."*
- **SDSI was not ingested.** Reading this document does not require the SDSI
  paper — §2.6 states the name construct completely enough for #14's table —
  but the `contradicts` and name-chaining arguments here cite [SDSI] and
  [Ab97] (Abadi, *On SDSI's Linked Local Name Spaces*), and a report that
  wants to argue about name-chaining semantics will need them. They stay with
  #19 and are named in this lane's topic answer rather than quietly added.
- **Read scope:** §1.1, §2.4–§2.8, §3, §4, §5.5–§5.7, §6.1–§6.5, §7.5 and §8.
  §5.1–§5.4, §6.6 and §7.1–§7.4, §7.6–§7.7 were skimmed only; the key
  management sections are not covered here at all.
