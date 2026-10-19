---
record: rfc-2692
kind: protocol
title: "rfc-2692 — protocol model"
extracted: "2026-10-18"
reviewed_by: ""
---

# rfc-2692 — protocol model

## Applicability: a requirements document with no protocol

RFC 2692 specifies no protocol. It has no transport, no framing, no encoding,
no request or response format and no error signalling, and it contains **no
BCP 14 keyword**. Its abstract describes it as a summary of requirements drawn
from "a list of things one might want to do with certificates". On the two
points where a protocol would be expected, it disclaims one:

- the CRL: "Its method of transmission is not specified." (§Validity and CRLs ¶2, p.4)
- repositories: "If the keyholder wishes to use a global repository, such as
  LDAP, the global PGP key server or the DNS database, that is up to the
  keyholder and not for the SPKI WG to specify." (§General Requirements ¶5, p.3)

Its status boilerplate nonetheless says "This memo defines an Experimental
Protocol". That is recorded as a source defect.

What the document does give is a set of named **roles** and, mostly one
sentence at a time, named or implied **exchanges**. Each is modelled here at
the level the source gives, and each step that is not literally in the source
is flagged `inferred: true` with a reason. Much of the material comes from the
"List of Certificate Uses", which the source calls "a brainstorming list", and
from "Open Questions", which records what certificates cannot do. List items
that describe an exchange become flows. The rest are mapped under `use_cases`,
and the Open Questions are recorded as `non_flows`.

Where the actual structures live is outside this document. RFC 2692 cites
only [DH] and [KOHN]. As a library pointer, not a claim made by the source,
the SPKI WG's companion documents are RFC 2693 and
draft-ietf-spki-cert-structure. Nothing here is taken from them.

## Reading `protocol.yaml`

| key | what it holds |
|---|---|
| `applicability`, `applicability_quotes` | the scope statement above, with the source's own disclaimers |
| `conventions` | quoting, locators, `inferred`, `on_error_basis`, `status`, `kind`, message names, `constrained_by` |
| `framing` | 5 statements that govern every flow |
| `roles` | 26 roles; `kind` is party, implementer, local-component, example-party, threat or historical |
| `messages_referenced`, `message_notes` | the 30 message names used; `in_source` flags names with no source counterpart |
| `flows` | 26 flows, 88 steps |
| `use_cases` | every List of Certificate Uses item mapped to its flow |
| `non_flows` | 7 things the source says certificates or the WG do not do |
| `error_paths` | 34 error paths |
| `source_defects_and_ambiguities` | 22 entries |
| `not_defined` | 16 things an implementer will not find in RFC 2692 |

- **Locators.** The sections are unnumbered, so a locator is the section title
  plus a paragraph count and page: "§Validity and CRLs ¶2 (p.4)". List items
  are located by their opening words, and Open Questions are numbered Q1 to Q4.
- **Inferred.** 37 of the 88 steps are `inferred: true`, each with an
  `inferred_reason`. Flows whose content is mostly inferred say so in their
  summary.
- **Errors.** `on_error_basis` is `stated`, `inferred` or `unspecified`. 52
  steps are `unspecified`: the source names the step and says nothing about
  failure. That gap belongs to the source.
- **Quotes.** All 327 quoted spans (quotes, on_error quotes, use-case items and
  wallet-card names) were checked mechanically against `.cache/rfc-2692.txt`
  with line wrapping undone, in-line double spaces kept, and "collision-" /
  "free" joined. None crosses a blank line or a page break. In this prose
  file, a double quote inside a quoted span is written as a single quote
  (blockquotes keep the source's marks). Where a source
  sentence runs over a page break the quote stops at the break and a
  `quote_notes` entry says so.
- **constrained_by.** Every flow carries `constrained_by: []`. Requirement ids
  are wired in pass 3 by a different agent.
- **Message names** are kebab-case after the source's noun and have not been
  reconciled with `messages.yaml`, which pass 1 does not see. Pass 3 reconciles
  them against `messages_referenced`.

## Roles

| role | kind | where the source names it |
|---|---|---|
| `keyholder` | party | §General Requirements ¶1 "KEYHOLDER"; "I" throughout the List |
| `verifier` | party | §General Requirements ¶5; §Validity and CRLs ¶2; "user of a certificate" §Background ¶2; "reader of a certificate" §Implementation ¶2 |
| `issuer` | party (our word) | "any keyholder empowered to grant or delegate the authorization in question" §Implementation ¶1; "creator of a certificate" ¶2 |
| `code-author` | party | "the author of code which uses the certificate" §General Requirements ¶4 |
| `certificate-code-developer` | implementer | "many different developers, frequently persons acting alone, operating out of garages or dorm rooms" §Implementation ¶1 |
| `crl-issuer` | party, **inferred** | implied by "a signature" on the CRL, §Validity and CRLs ¶2 |
| `online-validator` | party, **inferred** | "on-line validation", "on-line refinement of validity", §Validity and CRLs ¶1, ¶3, ¶4 |
| `global-repository` | party | LDAP, PGP key server, DNS, §General Requirements ¶5 |
| `smart-card` | party | List item "This signed-key should be considered equivalent" (p.9); §Implementation ¶1 |
| `central-administrator` | party | Other requirements, host authentication (p.10) |
| `notary-service` | party | "Timestamping / notary services" (p.10); Other requirements (p.10, p.11) |
| `key-cache` | local component | Other requirements, "cached locally" (p.11) |
| `revoker` | party, **inferred** | implied by "distribution of key revocations" (p.11) |
| `key-generating-administrator` | party | "the people generating the keys (e.g., administrators)" (p.11) |
| `name-binder` | party | "someone trustworthy binding that unique name to the key" (p.6) |
| `negative-fact-organization` | party | "some organization is capable of determining that fact" Q3 (p.12) |
| `bank`, `master-bank-certifier`, `other-bank` | example parties | electronic-check items (p.5-6); NACHA "perhaps" |
| `dns-name-owner` | example party | "DNS name owner" certificate (p.10) |
| `software-vouchee` | example party | "some reputable company or person" (p.6) |
| `application` | local component | "the audit identity should be in the domain of the particular application" (p.9) |
| `key-thief`, `key-loaner` | threats | Q1 (p.11), Q4 (p.12), signed-key item (p.10) |
| `online-directory`, `communicant` | historical | §Background ¶1 |

## Flows

Twenty-six flows, each with a diagram. Each step of the flow in
`protocol.yaml` is one solid or dashed arrow, in step order; a step taken only
on a condition sits in an `opt` block. A step
the source does not state is a dashed arrow (`-->>`) whose text ends in a
parenthesis beginning "inferred". A crossed arrow (`--x`) inside an `alt`
block is a failure outcome, marked the same way when the outcome is inferred.
A self-arrow is a local step. `autonumber` numbers the failure arrows too, so
step numbers in the text are the YAML `n`, not the diagram's numbers.

### 1. `direct-certificate-distribution`

§General Requirements ¶5, ¶6 (p.3); §Implementation of Certificates ¶5 (p.5);
§Validity and CRLs ¶1 (p.4); §Background ¶2 (p.2). *Status: assumed.* The
default model: "we assume that certificates will be distributed directly by the
keyholder to the verifier", because they may carry what the keyholder would not
publish. The keyholder releases a minimum of information. The verifier checks a
signature made "exactly as it is transmitted", with no reformatting except
white-space canonicalization of text, and decides whether the keyholder "has
been granted some specific authorization". **Inferred:** step 4, the
validity-period check. Failure outcomes for the signature check and the
authorization decision are inferred. Delivery failure is unspecified.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant V as verifier
  K->>K: choose the minimum to release, one certificate
  K->>V: spki-certificate, distributed directly
  V->>V: check the signature over the bytes as transmitted
  alt signature fails, or would need reformatting
    V--xV: not accepted (inferred outcome)
  end
  V-->>V: validity-period covers now (inferred)
  V->>V: on-line refinement of validity if used, see flows 9 to 13
  V->>V: has the keyholder been granted the authorization
```

### 2. `repository-publication`

§General Requirements ¶5 (p.3). *Status: considered.* Publishing to LDAP, the
global PGP key server or the DNS database is "up to the keyholder and not for
the SPKI WG to specify". **Inferred:** step 2, the verifier's retrieval. Both
steps' failures are unspecified.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant R as global-repository
  participant V as verifier
  K->>R: spki-certificate, at the keyholder's option, protocol not specified
  R-->>V: spki-certificate retrieved (inferred)
```

### 3. `certificate-issuance`

§Implementation of Certificates ¶1 to ¶7 (p.4-5); §General Requirements ¶2,
¶3, ¶6, ¶7, ¶8 (p.3); §Validity and CRLs ¶1 (p.4). *Status: required
capability.* Certificates "should be generated by any keyholder empowered to
grant or delegate the authorization in question". The subject is the public
key, a collision-free hash of it, a name to be resolved later, or a blinded
signature key. The certificate has a bare minimum of fields, minimum
information, optionally a validity period, no ASN.1 and no library code, and an
LR(0) grammar with no recursion "if possible". It is signed exactly as
transmitted. The creator is constrained "by the structure definition, not by
complaints (or error messages) from the reader", so there is no
reader-to-creator error channel. Guards cover constrained environments, light
bureaucracy for host authentication, highly trusted notary keys and not sharing
keys. **Inferred:** step 6, delivery to the subject keyholder, and step 7,
onward delegation by a delegatee. The source's only word on delegation control
is "Maybe we need a 'delegation-allowed' bit", dismissed because a key can be
loaned.

```mermaid
sequenceDiagram
  autonumber
  participant I as issuer
  participant K as keyholder
  I->>I: empowered to grant or delegate the authorization
  I->>I: identify subject by public-key, public-key-hash, name or blinded-signature-key
  I->>I: compose minimum fields and information, optional validity-period
  I->>I: encode without ASN.1 or library code, LR(0) and no recursion if possible
  I->>I: sign exactly as it will be transmitted
  Note over I: structure, not reader error messages, constrains the creator
  I-->>K: spki-certificate (inferred)
  K-->>K: if empowered to delegate, issue onward (inferred)
  Note over K: no delegation bit can stop a holder lending the private key
```

### 4. `authorization-definition`

§General Requirements ¶4 (p.3). *Status: required capability.* "The creation of
new authorizations should not require interaction with any other person or
organization but rather be under the total control of the author of the code
using the certificate." **Inferred:** steps 2 and 3, how issuers learn the
definition and that the code using it runs at the verifier.

```mermaid
sequenceDiagram
  autonumber
  participant A as code-author
  participant I as issuer
  participant V as verifier
  A->>A: define authorization, no interaction with anyone else
  A-->>I: issuers use the authorization (inferred)
  A-->>V: the author's code interprets it at the verifier (inferred)
```

### 5. `delayed-binding-resolution`

§General Requirements ¶3, ¶9 (p.3-4). *Status: required capability.* The
keyholder may be identified "via a collision-free hash of the public key or via
a name, later to be resolved into a key". SPKI should support the SDSI name
construct "if possible", and the bracketed note says SPKI and SDSI have merged.
No resolution procedure is given. **Inferred:** step 1, supplying the key and
comparing its hash. Name-resolution failure is unspecified.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant V as verifier
  K-->>V: public-key, hashed and compared with the certificate (inferred)
  alt hash mismatch
    V--xV: key is not the subject (inferred)
  end
  V->>V: resolve name into a key, method not given
```

### 6. `traditional-certificate-issuance`

§List of Certificate Uses, item "[traditional certificate]" (p.6). *Status:
brainstorm use.* The item reads "binding a key to a name". It needs unique identification of a
person, "which is difficult in non-digital space", and "someone trustworthy"
to bind the name. The key then "acquires attributes, permissions and authority
from the person bound to it". The Background explains that SPKI finds such
bindings "of extremely limited use for trust management". **Inferred:** step 1,
the keyholder submitting to identification.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant B as name-binder
  participant V as verifier
  K-->>B: be uniquely identified (inferred)
  B->>K: traditional-certificate binding the unique name to the key
  V->>V: key acquires the attributes of the named person
```

### 7. `direct-certificate-self-signing`

§List of Certificate Uses, item "[direct certificate]" (p.6). *Status:
brainstorm use.* A self-signed declaration of the name the keyholder goes by.
"The unique identification of the key is automatic", and the key's authority
comes "directly by other certificates, not indirectly through some person's
name". **Inferred:** step 2, presentation to a verifier.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant V as verifier
  participant I as issuer
  K->>K: direct-certificate, self-signed name declaration
  K-->>V: direct-certificate (inferred)
  I->>K: spki-certificate loads the key with authority directly
```

### 8. `personal-binding`

§List of Certificate Uses, item "[personal binding]" (p.6-7); §General
Requirements ¶9 (p.3). *Status: brainstorm use.* I sign someone else's key
with my nickname for them. It is "for my use only -- never given out", and
signed "to prevent tampering with my own private" directory of keys. The
quote stops at the p.6/p.7 page break, where the sentence continues "directory
of keys." It records nothing about how I satisfied
myself of the binding. The source says "singing" for "signing". **Inferred:**
no step. The tamper-detection outcome is inferred.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  K->>K: sign personal-binding of another key to my nickname
  Note over K: kept in my own directory, never given out
  K->>K: on use, check the signature
  alt signature fails
    K--xK: directory tampered with (inferred)
  end
```

### 9. `crl-validation`

§Validity and CRLs ¶1, ¶2, ¶5 (p.4). *Status: required capability, conditional
on "if SPKI uses CRLs".* There are three requirements: "the certificate that uses
it must explicitly tell the verifier where to find the CRL, the CRL must carry
explicit validity dates and the dates of a sequence of CRLs must not overlap."
A CRL "must have its own lifetime", and a lifetime of 0 "is not possible".
Validation is then "deterministic (aside from the question of clock skew)".
Transmission is "not specified". The source never names the CRL signer or the
key the verifier should expect. Annihilation of listed certificates and of
previous CRLs is stated only for the minimal CRL of flow 10. **Inferred:**
steps 3 (fetch from the stated location), 4 (CRL signature check), 5 (date
check), 6 (supersession applied to a conforming CRL) and 7 (annihilation
applied to a conforming CRL). The outcome of an unobtainable CRL is unspecified.
RFC 2692 does not say the certificate then fails.

```mermaid
sequenceDiagram
  autonumber
  participant I as issuer
  participant C as crl-issuer
  participant V as verifier
  I->>V: crl-location inside the certificate, where to find the CRL
  C->>C: crl with revoked list, sequence number, signature, validity dates
  Note over C: dates of successive CRLs must not overlap, lifetime never 0
  C-->>V: crl fetched from the stated location, transport not specified (inferred)
  V-->>V: verify the CRL signature, signer not named (inferred)
  V-->>V: now within the CRL validity dates (inferred)
  alt expired, missing dates or overlap
    V--xV: no deterministic result
  end
  V-->>V: a later CRL by sequence number annihilates the earlier (inferred for conforming CRL)
  V-->>V: is the certificate listed in the current CRL (inferred for conforming CRL)
  alt certificate listed
    V--xV: certificate annihilated (stated for minimal CRL)
  end
  V->>V: result deterministic aside from clock skew
```

### 10. `minimal-crl-propagation`

§Validity and CRLs ¶2 (p.4). *Status: described and rejected.* "A minimal CRL
contains a list of revoked certificates, identified uniquely, a sequence number
and a signature.  Its method of transmission is not specified." It annihilates
any certificate it lists and any previous CRL it meets. "Such a CRL leads to
non-deterministic program behavior", and that is why flow 9's three
requirements exist. **Inferred:** none.

```mermaid
sequenceDiagram
  autonumber
  participant C as crl-issuer
  participant V as verifier
  C->>V: minimal crl, by an unspecified method
  V->>V: annihilate each listed certificate and any previous CRL by sequence number
  V--xV: non-deterministic program behavior
```

### 11. `positive-online-validation`

§Validity and CRLs ¶1, ¶3, ¶4, ¶5 (p.4). *Status: required capability.* "SPKI
should support both positive and negative on-line validations", which is the
retail move to "on-line validation of a single check, ATM card or credit card".
"Any CRL or revalidation instrument must have its own lifetime", and the
lifetime cannot be 0 "because of communication delays and clock skews".
Treating the positive validation as the revalidation instrument is inferred.
**Inferred:** step 1 (the request) and step 3 (using the instrument within its
lifetime to refine validity).

```mermaid
sequenceDiagram
  autonumber
  participant V as verifier
  participant O as online-validator
  V-->>O: online-validation-request for one certificate (inferred)
  O->>V: positive-online-validation, a revalidation-instrument with its own lifetime
  Note over O: lifetime 0 is not possible
  V-->>V: use only within its lifetime to refine validity (inferred)
  alt lifetime over
    V--xV: not usable (inferred)
  end
```

### 12. `negative-online-validation`

§Validity and CRLs ¶3, ¶4, ¶5 (p.4). *Status: required capability.* The phrase
"negative on-line validations" is used once and never described. The only
negative statement in the document is the CRL ("A CRL is a negative
statement"), so the flow is modelled as an on-line negative statement under the
CRL lifetime rule. **Inferred:** both steps.

```mermaid
sequenceDiagram
  autonumber
  participant V as verifier
  participant O as online-validator
  V-->>O: online-validation-request, is it revoked (inferred)
  O-->>V: negative-online-validation, CRL-like, with its own lifetime (inferred)
  alt listed
    V--xV: certificate annihilated (inferred)
  end
```

### 13. `one-use-instrument-challenge-response`

§Validity and CRLs ¶5 (p.4). *Status: considered.* "one can consider an
instrument whose lifetime is 'one use' and which is delivered only as part of a
challenge/response protocol." Challenger, challenge content and binding are not
given. **Inferred:** step 1, the verifier as challenger. The outcomes of reuse
and of delivery outside a challenge/response are inferred.

```mermaid
sequenceDiagram
  autonumber
  participant V as verifier
  participant O as online-validator
  V-->>O: challenge (inferred sender and content)
  O->>V: response carrying one-use-instrument
  V->>V: use it once
  alt reused, or delivered outside challenge/response
    V--xV: not valid (inferred)
  end
```

### 14. `minimal-information-proof`

§General Requirements ¶6, ¶7 (p.3); §Background ¶2 (p.2); List item "I'm the
a purchasing agent" (p.9). *Status: required capability.* A certificate is "like
a single key rather than a key ring or a single credit card rather than a whole
wallet", and "at least some certificates" must be anonymous. The purchasing
agent shows a $15,000 authorization without a name and without sharing a
"Megacorp Purchasing Department Certificate", which would mean sharing the
private key. **Inferred:** step 3, proof of control of the private key, which
the source never describes.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant V as verifier
  K->>K: choose the single certificate for this permission
  K->>V: spki-certificate, anonymous where needed
  K-->>V: signed-request proving control of the private key (inferred)
  V->>V: decide on the authorization, not the name
```

### 15. `certificate-chain-following`

List items "I need a certificate to give me permission", "My bank would need a
certificate", "My bank would issue a certificate" (p.5-6); Other requirements,
"Trust model must be a web" (p.10). *Status: brainstorm use.* "My bank would
issue a certificate signing the key of a master bank certifier -- perhaps NACHA
-- so that I could follow a certificate chain from a key I know (my bank's) to
the key of any other bank". The guard: people "must be able to choose whom they
trust or consider reliable roots". **Inferred:** step 1 (my bank issues my
check-writing certificate) and step 4 (the master certifier certifies other
banks). Who certifies my bank, and how the chain is gathered, are unspecified.

```mermaid
sequenceDiagram
  autonumber
  participant B as bank
  participant K as keyholder
  participant M as master-bank-certifier
  participant O as other-bank
  participant V as verifier
  B-->>K: spki-certificate, permission to write electronic checks (inferred)
  B->>V: spki-certificate proving it is a bank, issuer not named
  B->>M: spki-certificate signing the master certifier key
  M-->>O: spki-certificate on each other bank key (inferred)
  V->>V: follow certificate-chain from my bank key, a root I chose, to the other bank
  alt link missing or root not chosen
    V--xV: unspecified, or not trusted (inferred)
  end
```

### 16. `smart-card-short-term-key`

List item "This signed-key should be considered equivalent" (p.9-10).
*Status: brainstorm use.* Smart cards "typically have slow processors and are
connected through low-bandwidth links". Using one only at login, "if you only use the smart card at 'login' time to
certify a short-term key pair", gives "high performance and low exposure of the
long term key". The certificate makes the signed key "equivalent to the
certifying-key until this certificate expires for the following purposes ...",
and the source elides the purposes. The guard notes that this "flies in the face
of attempts to prevent delegation". **Inferred:** steps 1 (who generates the
pair), 2 (hand-over to the card) and 4 (presentation to a verifier).

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant S as smart-card
  participant V as verifier
  K-->>K: generate short-term key pair (inferred)
  K-->>S: short-term public-key at login (inferred)
  S->>K: short-term-key-certificate signed by the long-term certifying key
  K-->>V: use the short-term key with its certificate (inferred)
  V->>V: treat as the certifying key for the listed purposes until expiry
  alt expired or purpose not listed
    V--xV: not equivalent
  end
```

### 17. `key-caching`

Other requirements, "Keys will need to be cached locally" and "Reliable
distribution of key revocations" (p.11). *Status: brainstorm use.* Keys are
cached "to avoid long delays fetching frequently used keys.  Cf. current name
servers." Caching "interacts with" revocation distribution. **Inferred:** step 1
(the lookup) and step 2 (the fetch source; a global repository is the only key
source the document names). The stale-entry outcome is inferred.

```mermaid
sequenceDiagram
  autonumber
  participant V as verifier
  participant C as key-cache
  participant R as global-repository
  V-->>C: look up public-key (inferred)
  opt miss
    R-->>C: fetch public-key, the long delay to avoid (inferred)
  end
  C->>V: public-key served locally, as a name server would
  Note over C: interacts with revocation distribution, flow 18
```

### 18. `revocation-distribution`

Other requirements, "Reliable distribution of key revocations" (p.11).
*Status: tentative.* "Reliable distribution of key revocations and other
certificates (e.g., the ceasing of the right to make new certificates).  May
involve goals like 'will have spread everywhere in 24 hours' or something like
that.  This interacts with caching." **Inferred:** step 1 (the issuer) and step 3
(cache invalidation). The exposure window is inferred.

```mermaid
sequenceDiagram
  autonumber
  participant X as revoker
  participant C as key-cache
  participant V as verifier
  X-->>X: issue key-revocation or certification-right-expiration-certificate (inferred issuer)
  X->>V: reliable distribution, goal of the order of 24 hours
  X-->>C: caches account for it (inferred)
  alt not yet arrived, or cache stale
    V--xV: revoked key or ceased right accepted (inferred)
  end
```

### 19. `certification-right-expiration`

Other requirements, "Especially in lower-end applications" and "Reliable
distribution of key revocations" (p.11); item "Timestamping / notary services"
(p.10). *Status: tentative.* Administrators "will change, and you will no longer
want them to be able to certify", but "you will usually also not want all keys
they have generated to expire". "This may imply a 'certification right
expiration' certificate requirement, probably to be implemented together with
notary services." **Inferred:** step 2 (timestamping each certification),
step 3 (the trigger, issuer and delivery of the expiration certificate) and
step 4 (the verifier enforcing the stated intent).

```mermaid
sequenceDiagram
  autonumber
  participant A as key-generating-administrator
  participant N as notary-service
  participant X as revoker
  participant V as verifier
  A->>V: spki-certificate on keys generated while in role
  N-->>A: timestamp each certification (inferred)
  X-->>V: certification-right-expiration-certificate when the administrator changes (inferred issuer)
  V-->>V: keep keys certified before, reject certifications after (inferred)
```

### 20. `reputation-voucher-introduction`

List item "I might generate a certificate (a 'reputation voucher')" (p.6).
*Status: brainstorm use.* I testify to "my friend's political opinion (e.g., libertarian
cypherpunk) or physical characteristics or anything else of interest" so as to "introduce him
to another friend". **Inferred:** step 2, the friend presenting it.

```mermaid
sequenceDiagram
  autonumber
  participant I as issuer
  participant K as keyholder
  participant V as verifier
  I->>K: reputation-voucher testifying to the friend
  K-->>V: reputation-voucher, introduction to another friend (inferred)
```

### 21. `mail-receiver-certification-chain`

List items "I am the current legitimate owner of a this DNS name or subtree"
and "I am the legitimate receiver of mail" (p.10). *Status: brainstorm use.* The
statement "might need to be signed by a key which itself had been certified by
the appropriate 'DNS name owner' certificate", for when "I know someone owns a
particular e-mail address but I don't know their key". **Inferred:** no step,
but the source hedges ("might need"). Who signs the DNS name owner certificate,
and how the verifier obtains the chain, are not stated. The first-person wording
is recorded as an ambiguity.

```mermaid
sequenceDiagram
  autonumber
  participant D as dns-name-owner
  participant I as issuer
  participant K as keyholder
  participant V as verifier
  D->>D: dns-name-owner-certificate, owner of the DNS name or subtree
  D->>I: dns-name-owner-certificate certifies this key
  I->>K: mail-receiver-certificate, legitimate receiver of mail at the address
  V->>V: from a known address to the unknown key via the certificate-chain
```

### 22. `software-certification`

List item "I want a certificate for some software" (p.6). *Status: brainstorm
use.* The subject is software, not a keyholder. The user wants "to make sure it
hasn't changed and that some reputable company or person stands behind it".
**Inferred:** step 1, issuance and delivery. The do-not-run outcome is inferred.

```mermaid
sequenceDiagram
  autonumber
  participant S as software-vouchee
  participant V as verifier
  S-->>V: spki-certificate for the software (inferred)
  V->>V: before running, check the software has not changed
  alt changed
    V--xV: do not run (inferred)
  end
```

### 23. `negative-fact-as-positive-attribute`

Open Questions Q3 (p.12). *Status: considered.* "The absence of attributes can be
determined only if all relevant records are digitized and all parties have
inescapable IDs." Still, the source answers:

> A certificate can communicate the 'positive' attribute "not already married" or "not registered as a voter in any other district".

That holds provided "some organization is capable of determining that fact".
"The method of determining such a negative fact is not part of the
certificate definition." **Inferred:** step 3, presentation for a marriage
license.

```mermaid
sequenceDiagram
  autonumber
  participant G as negative-fact-organization
  participant K as keyholder
  participant V as verifier
  G->>G: determine the negative fact, method outside the certificate definition
  alt records not all digitized or IDs escapable
    G--xG: absence cannot be determined
  end
  G->>K: spki-certificate with the positive attribute not already married
  K-->>V: present it for a digital marriage license (inferred)
```

### 24. `blinded-key-attribute`

§General Requirements ¶8 (p.3). *Status: required capability.* "Because one use
of SPKI certificates is in secret balloting and similar applications, an SPKI
certificate must be able to assign an attribute to a blinded signature key."
Blinding is not described. **Inferred:** step 1, submission of the blinded key.

```mermaid
sequenceDiagram
  autonumber
  participant K as keyholder
  participant I as issuer
  K-->>I: blinded-signature-key (inferred)
  I->>K: spki-certificate assigning an attribute to the blinded key
```

### 25. `online-directory-lookup` (historical)

§Background ¶1 (p.2). *Status: historical.* Diffie and Hellman's public-key
"telephone book": "look up his or her desired communication partner in the
directory, find that person's public key and open a secure channel to that
person." Kohnfelder noted that "an on-line service has the disadvantage of being
a performance bottleneck". **Inferred:** none.

```mermaid
sequenceDiagram
  autonumber
  participant P as communicant
  participant D as online-directory
  P->>D: directory-lookup for the partner
  D->>P: public-key
  P->>P: open a secure channel, no prior secret channel needed
  Note over D: an on-line service is a performance bottleneck
```

### 26. `signed-directory-entry` (historical)

§Background ¶1 (p.2). *Status: historical.* "To replace it, he proposed creation
of digitally signed directory entries which he called certificates." The guard
records that "certificate" has since "frequently been assumed to mean a binding
between name and key", which SPKI rejects as the main purpose. **Inferred:**
step 2, off-line verification and use.

```mermaid
sequenceDiagram
  autonumber
  participant D as online-directory
  participant P as communicant
  D->>P: signed-directory-entry, the first certificates
  P-->>P: verify and use without the on-line service (inferred)
```

## What certificates cannot do: non-flows

These are recorded so that nobody builds a flow the source says cannot exist.

| id | question | the source's answer | locator |
|---|---|---|---|
| `prove-non-composition` | prove I did not sign with my stolen key | "certificate format, contents or issuing machinery can not ensure the protection of a user's private key or prove whether or not a private key has been stolen or misused" | Q1, p.11 |
| `title-scan` | title scan for a house | the database of titles and liens "is a project not related to certificate structure" | Q2, p.11 |
| `prove-a-negative` | certify I am not already married | absence needs all records digitized and inescapable IDs; a positive attribute is possible (flow 23) | Q3, p.12 |
| `prevent-key-loaning` | stop a holder lending the private key | "a potential flaw in any system providing authorization"; a delegation-allowed bit would not help | Q4, p.12; p.10 |
| `reader-to-creator-errors` | error messages from reader to creator | deliberately absent; the structure constrains the creator | §Implementation ¶2 |
| `repository-protocol` | a repository protocol | "not for the SPKI WG to specify" | §General Requirements ¶5 |
| `crl-transport` | how a CRL travels | "not specified" | §Validity and CRLs ¶2 |

## The List of Certificate Uses

`use_cases` has 35 entries: the 29 items at the list's top level (the
wallet-card lead-in counted once, with its 33 cards kept verbatim under it) and
the 6 "Other requirements:" items. The three name-binding sub-items share their
parent's entry. 32 entries map to the flows above. Most are instances of flow 3
followed by flow 1, differing only in issuer and authorization: security
clearance (a governmental issuing authority), SAGE, DOC amateur radio licences,
the ephemeral root-access certificate with an application-domain audit identity,
the IP-address-space claim, and the wallet cards. 3 entries map to no flow and
say why: the house-contract and "80-year-old man" items are bare questions with
no mechanism, and "Digital signatures (unforgeability)" is a property, not an
exchange.

## Error paths

*S* means the outcome is stated in the source and *I* that it is inferred. Full
entries, with quotes, are in `error_paths`.

| id | trigger | outcome | basis | locator |
|---|---|---|---|---|
| `certificate-signature-invalid` | signature does not verify | not accepted | I | §Implementation ¶5 |
| `signature-check-needs-reformatting` | check would need reformatting | breaks the requirement; text white-space canonicalization allowed | S | §Implementation ¶5 |
| `reader-complaints-not-a-constraint` | creator relies on reader complaints | prevented by structure; no error message | S | §Implementation ¶2 |
| `certificate-outside-validity-period` | date outside validity period | not valid | I | §Validity ¶1 |
| `crl-location-not-given` | certificate uses a CRL without saying where | breaks requirement; verifier action unspecified | I | §Validity ¶2 |
| `crl-dates-missing-or-overlap` | no dates, or overlapping dates | non-determinism returns | S | §Validity ¶2 |
| `crl-nondeterminism` | minimal CRLs | non-deterministic program behavior | S | §Validity ¶2 |
| `crl-unobtainable` | CRL cannot be fetched | unspecified | I | §Validity ¶2 |
| `crl-signature-invalid` | CRL signature fails or wrong key | unspecified; signer not named | I | §Validity ¶2 |
| `instrument-expired` | CRL or revalidation past lifetime | not usable | I | §Validity ¶5 |
| `zero-lifetime-impossible` | lifetime 0 | not possible; one-use instrument offered | S | §Validity ¶5 |
| `clock-skew` | clocks disagree | deterministic only aside from skew; no tolerance | S | §Validity ¶2, ¶5 |
| `crl-superseded` | CRL meets an earlier one | earlier annihilated (minimal CRL) | S | §Validity ¶2 |
| `certificate-listed-in-crl` | certificate in the CRL | annihilated (minimal CRL) | S | §Validity ¶2 |
| `one-use-instrument-reused` | second use | outside lifetime | I | §Validity ¶5 |
| `one-use-instrument-outside-challenge-response` | delivered outside the protocol | not acceptable | I | §Validity ¶5 |
| `name-unresolved` | name cannot be resolved | unspecified | I | §General Requirements ¶3 |
| `key-hash-mismatch` | key does not match hash | not the subject | I | §General Requirements ¶3 |
| `unique-identification-difficult` | person not uniquely identifiable | unspecified | S | p.6 |
| `personal-binding-tampered` | private directory altered | signature reveals it | I | p.6 |
| `chain-broken` | missing or failing link | unspecified | I | p.6 |
| `untrusted-root` | chain starts at an unchosen key | not trusted | I | p.10 |
| `short-term-certificate-expired` | signed-key certificate expired | no longer equivalent | S | p.9 |
| `purpose-not-listed` | use outside the listed purposes | not equivalent | I | p.9 |
| `delegation-against-rules-by-key-loaning` | holder lends the private key | unpreventable by any bit | S | p.10; Q4 |
| `key-stolen-signature` | signature with a stolen key | certificates cannot prove it | S | Q1 |
| `revocation-not-yet-propagated` | verifier acts before arrival | may accept what is revoked | I | p.11 |
| `stale-cache` | cached key since revoked | served unless the cache accounts for revocations | I | p.11 |
| `certifier-right-ceased` | certification after the right ended | rejected; earlier keys kept | I | p.11 |
| `central-administrator-unreachable` | host auth cannot reach an administrator | must not block | I | p.10 |
| `dossier-aggregation` | many certificates gathered | privacy violation | S | §General Requirements ¶6 |
| `shared-private-key` | departmental certificate | key sharing, rejected | S | p.9 |
| `negative-fact-undeterminable` | records incomplete, IDs escapable | absence undeterminable | S | Q3 |
| `online-service-bottleneck` | every lookup on-line | performance bottleneck | S | §Background ¶1 |

## Source defects and ambiguities

The full entries, with quotes, are in `source_defects_and_ambiguities`.

- **Boilerplate.** The status says "This memo defines an Experimental Protocol";
  the document defines none.
- **Charter against scope.** The charter promises "key acquisition protocols",
  but §General Requirements ¶5 leaves distribution to the keyholder and puts
  repositories out of scope.
- **The CRL as actor.** "If it encounters some certificate that it lists, then
  it annihilates that certificate": the CRL is the grammatical subject, and the
  party applying it is never named.
- **Annihilation scope.** Listing and supersession semantics are given for the
  minimal CRL only. Whether sequence-number supersession survives the
  non-overlap rule is unclear.
- **CRL signer unnamed.** The certificate must say *where* the CRL is, not *who
  signs it*, so a CRL at the right place signed by anyone is not ruled out.
- **Certificate identifier undefined** ("identified uniquely").
- **"negative on-line validations"** and **"revalidation instrument"** are each
  used once and never defined. Their relation to the CRL and to positive
  validation is inferred.
- **One-use challenge/response.** No parties and no binding are given.
- **Clock skew** is named twice with no tolerance.
- **Typos.** "singing someone else's key" (p.6), "I'm the a purchasing agent" and
  "posses" (p.9), "a this DNS name" (p.10).
- **rfc822 item.** The editorial bracket sits inside the certificate statement's
  quotation marks.
- **First-person ownership claims** ("I am the current legitimate owner")
  read as self-signed, which cannot establish ownership. The signer is not named.
- **Dangling [SPKI] citation.** The References list only [DH] and [KOHN]. SDSI,
  NACHA, LDAP and PGP have no references.
- **Wallet list flat.** The cards are at the parent's indent, so where the list
  ends is unmarked.
- **"Other requirements:"** is nested in the brainstorming list. Its "must"
  ("Trust model must be a web") is of unclear force.
- **Web against master certifier.** The trust model "must be a web" while the
  chain example runs through NACHA. They are compatible but never reconciled.
- **Hedged mechanisms.** The delegation-allowed bit ("Maybe"), the certification
  right expiration certificate ("may imply", "probably") and the 24-hour goal
  ("or something like that").
- **"blinded signature key"** is not explained.
- **Page breaks.** Three sentences (SDSI, smart cards, personal binding) and
  one bracketed comment (the signed-key item's) cross page breaks. Quotes stop
  at the break.

## What RFC 2692 does not define

- Any transport, framing or encoding. The certificate structure is left to work
  the document does not cite (library pointer: RFC 2693,
  draft-ietf-spki-cert-structure).
- CRL transmission, CRL format beyond its minimal components, the certificate
  identifier, the CRL signer, and the verifier's response to a missing, expired
  or overlapping CRL.
- Any request or response for positive or negative on-line validation, or the
  party providing it.
- The one-use challenge/response: parties, content, binding.
- Repository protocols.
- Proof of possession of the private key.
- Name resolution. SDSI is named "if possible" and not defined.
- Chain discovery, assembly or delivery.
- Delegation control.
- Key-cache lifetimes and invalidation.
- The revocation distribution mechanism and its issuer. The 24-hour figure is a
  hedged example.
- The certification right expiration certificate and the notary or timestamp
  service it would use.
- Blinding for secret-ballot keys.
- The audit identity format, which belongs to "the domain of the particular
  application".
- Error signalling of any kind.
- Clock synchronization tolerances.

## Message names used

These are kebab-case names after the source's own nouns, listed in
`messages_referenced`, to be reconciled with `messages.yaml` in pass 3. Names
marked † have no counterpart in RFC 2692 and stand for inferred steps. Names
marked ‡ are partly in the source (the noun is there, the object is not
described).

`spki-certificate`, `authorization`, `validity-period`, `public-key`,
`public-key-hash`, `name`, `crl`, `crl-location`, `online-validation-request` †,
`positive-online-validation`, `negative-online-validation`,
`revalidation-instrument`, `challenge`, `response`, `one-use-instrument`,
`signed-request` †, `traditional-certificate`, `direct-certificate`,
`personal-binding`, `reputation-voucher`, `certificate-chain`,
`short-term-key-certificate`, `key-revocation`,
`certification-right-expiration-certificate`, `timestamp` ‡,
`dns-name-owner-certificate`, `mail-receiver-certificate` ‡,
`blinded-signature-key`, `signed-directory-entry`, `directory-lookup` ‡.
