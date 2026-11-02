---
schema: "library-summary/v1"
id: rfc-3820
record: rfc-3820
type: summary
updated: "2026-11-01"
---

# Internet X.509 PKI Proxy Certificate Profile

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — Proposed Standard, not obsoleted or updated (RFC Editor metadata, 2026-11-01) |
| **Authors** | S. Tuecke, V. Welch, D. Engert, L. Pearlman, M. Thompson |
| **Published** | 2004-06 |
| **Identifier** | RFC 3820 · DOI 10.17487/RFC3820 |
| **Source** | https://www.rfc-editor.org/rfc/rfc3820.txt |
| **Digest** | `sha256:4a41b3624516675cd50d8a13d616e5289655851bf7912591bb9d2563f0caba40` (the .txt, retrieved 2026-11-01) |

## Overview

Lets an end entity certificate holder delegate without a CA. A Proxy Certificate
(PC) has its own key pair, is signed by an end entity certificate or another PC,
and takes a subject name made by appending one CN to its issuer's (§2.6, §3.4).
The argument is that restricted proxying gives single sign-on and delegation
with a minimal change to path validation, no change to TLS, and no private key
ever crossing between the parties (§2.7). A critical `ProxyCertInfo` extension
marks the certificate, bounds further delegation with `pCPathLenConstraint`, and
carries a policy in a language identified by OID (§3.8).

The authority model is the interesting part. A PC's rights are the union of what
is granted to its own identity and what it inherits, and the inherited part is
the issuer's rights intersected with the PC's policy (§3.8.2). The document
defines that composition and then leaves the policy language to others, so path
validation only collects policies and returns them to the application (§4.1.6,
§4.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Delegation semantics, with a compromise analysis in §6 |
| Cryptography | `adjacent` | Defines no primitive. It adds path-processing rules over RFC 3280 |
| This project | `adjacent` | Native encoding is excluded by R-M-01. This is prior art for what delegation needs to say |

- **R-M-10** (delegation is an explicit boolean or equivalent). This answers the
  expectation left in `rfc-5280`'s design notes: yes, this is where PKIX delegates
  *authority*. `pCPathLenConstraint` is an integer, and 0 forbids further
  signing, but its absence means unlimited and an end entity always has unlimited
  depth (§3.8.1). Delegation is therefore on by default, the opposite of an
  explicit grant. A PC cannot have `cA` TRUE (§3.7), so the boolean that governs
  CAs says nothing here. Each PC has its own key pair and adds a CN, so a level of
  depth is both a new key and a new name (§2.6, §3.4).
- **R-M-08** (tag intersection defined per profile). A counter-example.
  Intersection is stated as the rule, but it is computed by a policy language
  this document does not define, and §3.8.2 is explicitly agnostic about policy
  content. Only `id-ppl-inheritAll` and `id-ppl-independent` have defined meaning.
- **DEC-004** (tag language). Pluggable-by-OID is the design to weigh. It buys
  extensibility at the cost that a relying party who cannot read a policy must
  deny, or ignore the whole chain (§3.8.2).
- **R-O-02** (short-lived validity preferred). §6.1 names short validity as the common limit on a compromised PC, and
  §4 says no revocation mechanism is defined for proxy certificates.

For the topic's question, §3.8.2 is one worked composition: union across
identities, intersection along a chain. The reference list cites neither SPKI
RFC, so any comparison with `rfc-2693` 5-tuple reduction is ours.

## Implementations

Searched 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://docs.openssl.org/master/man7/proxy-certificates/ |
| Grid Community Toolkit, a fork of the Globus Toolkit | open source | Apache-2.0 | https://github.com/gridcf/gct |

Commercial: searched, none found on 2026-11-01. OpenSSL verification requires an
explicit opt-in per its documentation. Evidence of use is grid computing (§2.2);
we did not measure current deployment.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and typed relations |
| `summary.md` | this document |

No `distilled/`. This PR claims the summary bar. An FX-1 extraction would be
worthwhile if R-M-10 is decided against this design, and no issue owns one yet.
Verbatim normative text lives under FX-1, so this summary cites sections only.

## Limits

- **Revocation is inconsistent.** §4 says no mechanism is defined for revoking
  proxy certificates, and §4.1 has no revocation step. §6.2 then suggests an EEC
  could use CRL Distribution Points or OCSP to revoke PCs it issued, without
  saying how a validator would use them.
- **Validation does not decide authorization.** §4.1 only returns
  `proxy_policy_list`. When a certificate is validated at authentication, before
  any request exists, the relying party needs a later authorization check or must
  reject certificates carrying policies (§3.8.2).
- **Names chain, and nothing enforces their uniqueness.** §6.3 concedes that two
  PCs with identical names and keys but different rights can be substituted in
  path validation, so a relying party trusts every Proxy Issuer in the chain. A
  Proxy Issuer can also reissue a name to another entity and in effect steal an
  Attribute Certificate bound to it (§5.1.4).
- **The promised keyCertSign argument is missing.** §1 says §2 explains why an
  end entity signing a PC does not violate the keyCertSign restriction. §2 never
  addresses that bit, and §3.1 and §3.6 speak only of the Digital Signature bit.
- **Delegation tracing is unresolved** (§5.4), and how to make a PC the holder of
  an Attribute Certificate stays open (§5.1.4).
- **It is pinned to RFC 3280**, which `rfc-5280` has since replaced, and this RFC
  has no update. How the §4.1 inputs map to 5280 path validation is unstated.
- **Source defects.** §4.1.2(c) initialises `proxy_issuer_public_key_parameters`,
  which is not the state variable that item names; §4.1.5 reads
  `proxy_issuer_public_key_algorithm`, which is never initialised; §4.1.3(c)
  writes `policyPolicy`. Two errata are Held for Document Update: 2954 (§5.1.2,
  editorial) and 4039 (§7, the IANA table omits `id-ppl-anyLanguage` and misspells
  `id-ppl-inheritAll`).
- **Read scope:** the complete .txt, plus RFC Editor metadata and errata. RFC 3280
  and RFC 3281 were not read.
