---
schema: "library-summary/v1"
id: rfc-9360
record: rfc-9360
type: summary
updated: "2026-10-20"
---

# CBOR Object Signing and Encryption (COSE): Header Parameters for Carrying and Referencing X.509 Certificates

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track ("This is an Internet Standards Track document", Status of This Memo) |
| **Authors** | J. Schaad (Ivaylo Petrov served as document editor after Schaad's death in 2020; Acknowledgements) |
| **Published** | February 2023 |
| **Identifier** | RFC 9360 · DOI 10.17487/RFC9360 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9360.txt |
| **Digest** | `3dbe546adf08e309b429c8e71b2ee8384292fb8767338d3eb17d1c4e5adefc23` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

Four COSE header parameters that carry or point at X.509 certificates —
`x5bag` (32, an unordered set), `x5chain` (33, an ordered candidate path),
`x5t` (34, a hash of the end-entity certificate) and `x5u` (35, a URI) — plus
three algorithm-scoped equivalents for static-static ECDH (`x5t-sender` −27,
`x5u-sender` −28, `x5chain-sender` −29, §3) and one media type,
`application/cose-x509` (§4.3). §1 records the reversal it embodies: while
writing RFC 8152 the COSE WG "decided that no use cases were presented that
showed a need to support certificates", and since then "a number of cases have
been defined in which X.509 certificate support is necessary".

It is a **carriage** specification and says so repeatedly. Certificates from
any of these parameters are untrusted input (§2); the relying party still has
to validate them under RFC 5280 §6 or "a different trust structure" (§2);
trust-anchor management is out of scope and §5 names firmware upgrade as the
realistic mechanism; and §2 concedes that "there still needs to be an entity
that is responsible for handling the possible certificate revocation" without
saying which. The two CDDL rules are the whole wire format:
`COSE_X509 = bstr / [ 2*certs: bstr ]` and
`COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]`, where
"The contents of `bstr` are the bytes of a DER-encoded certificate."

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **core** | Ten operative MUSTs and three MUST NOTs, all about what a relying party may conclude from a certificate it did not already trust (§2, §5). |
| Cryptography | adjacent | It specifies no algorithm; it selects hash identifiers from the COSE Algorithms registry and defers everything else to RFC 5280. |
| This project | **core** | `DEC-003` (KeyId), `DEC-005`, `R-O-01`, `R-O-05`, `R-M-12`, and the sharpest `DEC-002` cut in this lane. |

**The finding to act on: §5's claim that the `x5t` hash does not matter is
false in the configuration §2 itself recommends, and nothing excludes a Filter
Only algorithm from that position.** §5 says flatly that "The security of the
algorithm used for 'x5t' does not affect the security of the system, as this
header parameter selects which certificate that is already present on the
system should be used, but it does not provide any trust." But §2 defines, four
times, the opposite use: "The end-entity certificate MUST be integrity
protected by COSE. This can, for example, be done by … sending an 'x5chain' in
the unprotected header combined with an 'x5t' in the protected header", and the
`x5t` entry says it "can be used alone or together with the 'x5bag',
'x5chain', or 'x5u' header parameters to provide integrity protection of the
end-entity certificate." In that configuration the certificate is **not**
already on the system: it arrives in an unprotected bucket §2 says "allows an
intermediary to remove or add certificates", or is fetched from a URI, and the
protected `x5t` is the only thing binding it. That needs second-preimage
resistance at minimum and collision resistance wherever an attacker can
influence which certificate gets issued — which is the identity-misbinding
attack **§5's own next paragraph describes**.

`COSE_CertHash` accepts any value from the COSE Algorithms registry, and the
only constraint is interoperability: "applications that use this header
parameter MUST support the hash algorithm 'SHA-256' but can use other hash
algorithms." `rfc-9054` registers SHA-1 (−14) and SHA-256/64 (−15) as
**Filter Only**, which `rfc-9054` §4.1 defines as "not to be used for purposes
that require collision resistance" — and `rfc-9054` §3.2 cites *this
document's* draft as the justification for registering a 64-bit truncation,
resting on exactly the §5 claim above. The two cannot both stand;
**`contradicts: rfc-9054`** records it, and the root defect is internal to this
document rather than to `rfc-9054`, which only inherits it. The rule for us is
one line: *where `x5t` carries the integrity binding, `hashAlg` is restricted
to `Recommended: Yes` values, and the restriction lives in the protected
bucket.*

**`kid` occurs zero times in the whole document.** It adds four ways to
identify a key and never relates any of them to COSE's own key identifier
(RFC 9052 §3.1, label 4). So a `COSE_Sign1` may carry `x5chain` and no `kid`,
and `R-O-01` — "Every signed object SHALL have an issuer key that can be
specified as `KeyId`" — is then unsatisfiable *from the message*, without a
rule we write: either derive the `KeyId` from the certificate's
SubjectPublicKeyInfo, or require `kid` alongside. `DEC-003`'s mandatory clause
("canonical key bytes before hashing") has a ready answer on this path and the
document gives the wrong one: `x5t`'s hash is "computed over the DER-encoded
certificate" (§2) — the whole certificate, not the key. `rfc-9679` §5.4 draws
precisely this distinction, preferring SPKI digests to "digests of complete
certificate values", so the library already holds the argument for not reusing
`x5t` as a `KeyId`.

**The naming tension, stated as precisely as the document permits.**
`ARCH-0002 P1` is key-relative naming, accepted by `ADR-0001`. A certificate
carries a CA-issued *global* name. This document never names the Subject field
and never places it against the key; all it says is that "End-entity X.509
certificates contain identities that a passive on-path attacker … can use to
identify and track the subject", and that `x5t` and `x5u` "are just
alternative permanent identifiers" usable for the same tracking (§5). So the
global name space arrives silently, as a property of the opaque `bstr`.
**The sharpest form of the tension is §5's identity-misbinding paragraph**:
"Without proof of possession, an attacker can trick the CA into issuing an
identity-misbinding certificate with someone else's 'borrowed' public key but
with a different subject." That attack exists only because the name and the key
are separable. Under P1 the name *is* the key, so there is nothing to misbind —
the RFC's own worst case is an argument for P1, and it is better evidence than
anything we would have asserted. Overclaiming to avoid: the document does not
argue against key-relative naming, it is silent on it, and §2's actual case for
certificates is operational rather than architectural ("the full suite of
enrollment protocols, trust anchors, trust chaining, and revocation checking").

**An `R-M-12` data point that is not a confirmation.** §3's `x5t-sender`,
`x5u-sender` and `x5chain-sender` live in the **COSE Header Algorithm
Parameters** registry (§4.2), not the general header registry: labels −27/−28/
−29 mean these things *only* under the five ECDH-SS algorithms in Table 2, and
the same integers are free elsewhere. That is a ratified precedent for scoping
a label by a value in the protected header rather than globally. It is not
`R-M-12`'s *(key, local label)* pair, but it is the nearest ratified relative,
and it shows the pattern is implementable inside COSE without a fresh registry
per extension point — which is more than `rfc-9052`'s extraction could say.

**`R-O-05` support, and the better of two sibling choices.** `x5t` carries its
`hashAlg` **in-band**, and in the configuration §2 recommends, **inside the
protected bucket** — an authenticated algorithm indicator in exactly the shape
`R-O-05`'s type-indicator clause wants. `rfc-9679`'s `ckt` is the opposite
choice: a bare digest with nowhere to name H. Same working group, same
question, two answers; this is the one to copy.

## Implementations

The RFC names none and carries no implementation-status section. §1 cites two
consumers by draft — `[Constrained-BRSKI]`
(`draft-ietf-anima-constrained-voucher-19`) and `[EDHOC]`
(`draft-ietf-lake-edhoc-19`, since published as RFC 9528, which this library
holds as `rfc-9528`) — as the use cases that reversed the WG's 2017 decision,
so the real implementation surface is whatever those protocols ship. *Searched
on 2026-10-20 for an implementation named by the document: none.* Worth
recording as a negative result in its own right: for a document whose entire
content is wire format, **it prints no example at all** — not one COSE object,
not one certificate, not one `x5t` value — so there is no fixture to take and
nothing to check an encoder against. `rfc-9338`, by the same author in the same
year, carries six.

| Name | Kind | License | URL |
|---|---|---|---|
| _none named by the document_ | — | — | — |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`, and the judgement is deliberate rather than economical.**
This PR claims the **summary bar**: the record is `summarized`, declares no
`distillation` block, and touches no `distilled/`, so FX-1 does not fire
(`docs/extraction.md`). The reason is that this document is on the path we are
arguing *against* — `record.yaml` has carried `usefulness.verdict: marginal`
since 2026-09-22 on exactly that ground — and an FX-1 set would be 14
requirements, two CDDL rules and zero test vectors. **What would trigger an
extraction** is a decision to accept certificates for interoperability, which
is a `DEC-003` call: `requirements.yaml` would then have to carry the four
restatements of "the end-entity certificate MUST be integrity protected" as
separate testable entries with their differing conditions, `schema/` would hold
both CDDL rules plus a `*.derived.cddl` profile naming which `hashAlg` values
we permit, and `examples/` would have to be written from scratch because the
source supplies none. No issue owns that today.

**No verbatim normative text here.** Under FX-1 that belongs in
`distilled/normative.md` with its locator; in a summary the rule is to cite the
§ and let the reader open the source, so the fragments quoted above are short
and locator-bearing by design.

**Two relation edges are asserted from this record and need naming**, because
both are judgements rather than extractions: `contradicts: rfc-9054` (the
Filter Only / `x5t` conflict above) and `contradicts: rfc-9679` (§5.4 of
RFC 9679 misdescribes this document — see Limits). `see_also: rfc-8742` records
a citation gap, not a similarity.

## Limits

1. **"The end-entity certificate MUST be integrity protected by COSE" is
   unenforceable by schema, and it is the document's central obligation.** It
   appears four times (§2, once per parameter), each with "for example" and a
   list of three mechanisms, none mandated; §5 adds a fifth, *conditional*
   form — "Unless it is known that the Certificate Authority (CA) required
   proof of possession of the subject's private key …" — which makes the
   obligation depend on a CA practice statement that is nowhere in the message.
   The property is about the whole COSE object, so a validator holding one
   header cannot tell whether it holds. Any profile of ours has to collapse
   these five into one checkable rule.
2. **§5's `x5t` security claim is wrong as written** (above), and the
   errata search returns nothing for RFC 9360 (checked 2026-10-20), so it is
   recorded nowhere but here.
3. **`rfc-9679` §5.4 misdescribes this document, and that record is at
   `profile: full`.** It writes: *"the "x5t" (X.509 certificate SHA-1
   thumbprint) [RFC9360] value defined for X.509 certificate objects"*. The
   string "SHA-1" occurs **zero** times in RFC 9360; `x5t` here is
   hash-agile — `[hashAlg, hashValue]` with SHA-256 mandatory to support. The
   parenthetical is RFC 7515 §4.1.7's JOSE registry name, where `x5t` **is**
   defined as a SHA-1 digest, imported wholesale and attached to the COSE
   citation. `contradicts: rfc-9679` records it; the fix belongs to that record
   and is reported, not made here.
4. **Trust is entirely out of scope, said plainly, and that is most of what a
   certificate was for.** No anchor format, no revocation mechanism, no
   path-building rule beyond citing RFC 5280 §6, and §2's observation that
   someone must handle revocation with no statement of who. Adopting `x5chain`
   buys the CA ecosystem and none of its operations.
5. **`x5bag` accepts unbounded work.** §2: unordered, "there could be duplicate
   certificates", may "contain certificates that are completely extraneous to
   the message", and may "not contain the full set of certificates needed to
   build any particular chain" — with path building left to the verifier. A
   constrained relying party cannot bound the cost of a conforming message.
6. **`application/cose-x509` is defined as "a CBOR sequence" and RFC 8742 is
   cited zero times.** §4.3's registration says the data is "a CBOR sequence of
   single-entry COSE_X509 structures (encoding "bstr")" — a third wire framing
   for the same information, alongside the bare `bstr` and the
   `[ 2*certs: bstr ]` array — naming a construct `rfc-8742` defines, including
   its own `application/cbor-seq` media type, without referencing it.
   `see_also: rfc-8742`.
7. **One small thing it gets right, worth copying.**
   `COSE_X509 = bstr / [ 2*certs: bstr ]` makes the one-element array
   *invalid*: a single certificate has exactly one encoding. That is an
   ambiguity removed by construction rather than by a canonicalization rule —
   and the price is that every decoder must accept two shapes for one field.
8. **`x5u` reintroduces network dependence inside a signature check**, and §5
   admits the ordering problem it creates: validating certificates "can require
   that network resources be accessed", but validating them only after the
   signature "can potentially be built" into an oracle, so §5 requires both to
   complete before acting and resolves the order no further.

## Where it cuts against MD-3

**This is the sharpest cut in the COSE lane, and it cuts by evasion rather
than by violation — which is the finding.** MD-3 narrowed `DEC-002` to
**option 5: reduced CBOR, no IANA tags, COSE export only**. Count what this
document would cost option 5 on option 5's own terms: eight IANA allocations
(four header labels, three algorithm-scoped labels, one media type) and
**zero CBOR tags**. So option 5's literal "no IANA tags" clause survives
completely untouched — and the profile acquires ASN.1.

That is the mechanism. `COSE_X509` is `bstr`, and §2 states that "The contents
of `bstr` are the bytes of a DER-encoded certificate." A reduced-CBOR profile
reduces the CBOR; **it does not reach inside a byte string.** Carrying one
certificate therefore buys a second encoding (DER), a second parser, a second
*canonical form* — DER is itself a canonicalization, with its own rules and its
own history of parser differentials — and a second trust system (RFC 5280 §6
path validation, revocation, anchors). None of that is governed by "reduced
CBOR", none of it is expressible in our CDDL, and none of it is excluded by
"no IANA tags". **Option 5's exclusion clause is scoped to the wrong layer to
be the defence it reads like.**

Two consequences the `DEC-002` ADR should hear, and one correction to the
obvious reading:

- **Do not score this as option 5 losing to another option.** Every `DEC-002`
  option pays this cost identically — option 1 (canonical S-expressions) would
  carry the same DER inside the same opaque octet string. So the DER-in-a-header
  problem is an argument about **scope**, not about encoding: it says the
  decision that matters is "do we carry certificates at all", and that decision
  belongs to `DEC-003`, not `DEC-002`. The thing option 5 should say and does
  not is that its exclusions do not and cannot reach a payload.
- **What option 5 *can* exclude here is the whole parameter set**, and that is
  cheap to write and worth writing: a lint rule rejecting labels 32, 33, 34, 35
  and −27, −28, −29 in a native statement. Note it must reject `x5t` (34) too,
  even though `x5t` is the only one of the four that carries no ASN.1 — because
  §2's hash is over the DER certificate, so accepting it accepts the DER
  canonical form by reference without carrying the bytes.
- **The convergence across this lane is the actual evidence.** `rfc-9165`'s
  extraction found option 5 is *registry-reduced, not registry-free* one layer
  up (§6.1's dotted-name policy prices the namespaced form above the global
  one); `rfc-9054`'s record finds the costly dependency is an *absent
  structure* rather than a tag; this record finds the exclusion stops at the
  CBOR layer while the content is below it. Three independent documents, the
  same shape. MD-3 is a narrowing and not an acceptance, and what these three
  jointly recommend is that the ADR restate the exclusion as a property of
  *what we accept*, not of *which CBOR constructs we emit*.

