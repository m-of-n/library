---
schema: "library-summary/v1"
id: sdsi-1-1
record: sdsi-1-1
type: summary
updated: "2026-10-26"
---

# SDSI — A Simple Distributed Security Infrastructure, version 1.1

|  |  |
|---|---|
| **Type** | spec (an academic working paper, not a standard) |
| **Maturity** | _unset_: the document calls itself a working document for version 1.1, defers precise specifications to a companion paper (§2), and states no other standing |
| **Authors** | Ronald L. Rivest (MIT Laboratory for Computer Science), Butler Lampson (Microsoft Corporation) |
| **Published** | 1996-10-02 (the document's own timestamp, "Wednesday October 2 8:18 PM EDT 1996") |
| **Identifier** | https://people.csail.mit.edu/rivest/pubs/RL96.ver-1.1.html |
| **Source** | https://people.csail.mit.edu/rivest/pubs/RL96.ver-1.1.html |
| **Digest** | `sha256:69dad884…` (full value in `record.yaml`), HTML, fetched 2026-10-26 |

**Locators.** The HTML prints section numbers as `*.`. The numbers used below are rebuilt from the document's own cross-references (it calls Compression "Section 3.3", Reconfirmation Queries "6.2" and Transport mechanisms "6.5"). They run §1 Introduction, §2 Overview, §3 Data structures, §4 Standard object types (§4.2 Principals, §4.4 Signed objects), §5 Local names (§5.1 Names, §5.2 Name/Value Bindings, §5.3 Certificates), §6 Protocols (§6.1 Get, §6.2 Reconfirmation, §6.3 Auto-Certs, §6.4 Delegation Certificates), §7 Groups and ACLs (§7.1 membership algorithm, §7.2 Membership queries, §7.3 ACLs) and §8 Application Scenarios (§8.3 Kerberos-like tickets, §8.9 Key Compromise). §2 has no subsections; it is cited by its bold run-in paragraph titles.

## Overview

SDSI argues that a PKI built on a global name hierarchy is both too complex and too weak to write an access-control list against (§1), and replaces it with **keys as principals and names local to each key**. A principal **is** a public signature-verification key; two principals are the same *if and only if they have the same public key* (§4.2). Every principal can bind local names to values, and can export those bindings by signing certificates. Others then reach them through chains such as `bob's alice`, i.e. `(ref: bob alice)` (§2 "Linked local name spaces", §5.2). On top of names sit **groups**: owner-defined sets, which may be built from other people's groups, and which ACLs name (§7). The design is on-line: issuers run servers, and **revocation lists are replaced by periodic reconfirmation** (§2 "On-line Internet orientation", §6.2). Version 1.1 still keeps a small set of `!!` special roots, and it has a special rule that turns email addresses into chains rooted at `DNS!!` (§2, §5.2). Both were dropped when SDSI merged into SPKI (`rfc-2693` keeps no global root).

## What #14 needs from SDSI 1.1, by locator

This section serves library#14's delegation comparison. Its running example: Dave relies on Alice for `*@foo.com`, Alice delegates `*@eng.foo.com` to Bob, and Bob says Carol's key is `carol@eng.foo.com`.

**1. Linked local name spaces.** A name is any octet string that does not start with a special character (e.g. `tom@nsf.gov`), or any S-expression wrapped as `(Local-Name: n)` (§5.1). A name is bound when its owner signs a `Cert:` that carries `Local-Name:` and `Value:` fields, i.e. a name/value certificate. The value should be a `Principal:`, a `Group:`, a `Quote:`, or a `ref:` (or one of these wrapped in `Encrypted:` or `Assert-Hash:`) (§5.3). Bindings can be symbolic: bob can bind his `lawyer` to `ted's lawyer`, so the meaning follows ted's later changes (§5.2; §2 "Linked local name spaces", the `tim` / `mit's Tim-Black` example). Chaining is `REF(P, n1, …, nk)`: start from the **current** principal and look up each name in turn in the name space of the principal the previous step returned (§5.2, "Details of ref:"). `bob's alice's mother` is defined "for me" (§2) only if I bound `bob`, bob bound `alice`, and that principal bound `mother` (§2). Two binding rules matter for the comparison:

- **Bindings for one name add up; they do not replace each other.** If a name already has a valid certificate, *the new certificate augments the old one*: an application acts correctly if it uses either binding (§5.2). Servers may prefer the newest certificate. Even so, *technically the older certificates are still valid until they expire* (§5.3).
- **Special roots.** Names ending in `!!` (`VeriSign!!`, `IAPR!!`, `USPS!!`, `DNS!!`) are reserved, and *their names are bound to the same principal in every name space* (§2 "Accomodation for standard roots"). How that is arranged is left open: *we do not try to describe this in more detail* (same paragraph). A principal may therefore have several global names, one for each path from a root (§2). A `Principal:` may carry `Global-Name:` hints. They only suggest which certificates to fetch (§4.2).

**2. Groups, and "everyone in G".** A group is a set, almost always of principals but possibly of any S-expression (§7). Its name is local to an owner, and only the owner may change its definition (§2 "Groups"). It may be written as a list `(Group: tom mary …)` or as set algebra: `AND:`, `OR:`, `NOT:`, `MINUS:`, and a threshold `ANY:` (§7). `ALL!` is the group of everyone (§7). "Everyone in group G" is just the group's name, written in an ACL, e.g. `(ACL: (read: mit's faculty))` (§7.3, §2 "Groups"). Three properties to note:

- *A group does not have an associated public key*, and *No principal is authorized to speak for the group* (§7). A group is a set of keys, not a speaker.
- Membership is decided by `MEMBER(x, g)`. It returns TRUE, FALSE or FAIL, detects cycles, and uses only local data plus the credentials the client supplies. The server does not go and ask other servers (§7.1). A negative needs positive evidence: to show `(NOT: B)`, the group's owner must have issued a certificate saying the principal is not in `B` (§7).
- A **membership certificate** (`Membership.Cert:`) is the signed answer to a `Membership.Query:`. On FAIL it carries a `Hint:`, which is the group definition partly evaluated, in the **server's** name space (§7.2).

**3. Authority and delegation: a separate object from a name binding.** SDSI 1.1 has **no authorization certificate**. Authority comes from being in a group that an ACL names (§7, §7.3). §2 ("Delegation Certificates") names two ways to delegate: groups, and delegation certificates. A delegation certificate *gives the delegee the authority to sign statements of certain types on behalf of the delegator* (§2). Its form is `(Delegation-Cert: (Template: <form>) (Group: <group>) (Signed: …))`. It authorizes every member of `<group>` to sign objects matching `<form>` on behalf of the signing principal. The example authorizes principal A to sign `Membership.Cert:` objects for `fudge-lovers` (§6.4). A delegate's signature carries `Signing-For:`, and a `Credentials:` field must show the authorization (§4.4). So **delegation is a distinct object type** from the name/value `Cert:`. It delegates **signing on someone's behalf**, not names. Its stated main purpose is a principal authorizing its own servers, though *it is easy to imagine other possible uses for them, as well* (§6.4). There are no queries named "Delegate". The two query protocols are `Get` (§6.1) and `Membership` (§7.2), plus `Reconfirm` (§6.2).

**4. Where trust starts.** At the verifier. *No hierarchical global infrastructure is required.* (§2 "Egalitarian design"). Everyone can act as a CA, under whatever policy they choose (§2 "Each principal is a certification authority"). Each name is resolved in the current principal's own space (§5.2). Access is decided by the resource owner's ACL and its own group definitions (§7.1, §7.3). The one exception is the `!!` special roots, which every name space shares by convention. Adding a key to your own name space is meant to be manual and to need judgement, and the authors expect a typical user to do it perhaps 5 to 20 times (§2 "Manual process for creating identity certificates"). Auto-certificates are self-signed and *should not be trusted without suitable corroboration* (§6.3).

**5. Scoping a delegate.**

- **By rights (Delegation-Cert).** `Template:` limits which objects a delegate may sign. *The matching routine is the same as for the* `Template:` of a `Get.Query:` (§6.4). That rule (§6.1) is structural: octet strings must be equal, and every element of a template list must match some element of the object. It has **no wildcards, prefixes or ranges**. A template can therefore fix a field, e.g. one `Group:`, or leave it free. It cannot express "any name ending in `eng.foo.com`". The document says nothing about re-delegation, depth, or a validity field of its own, though any `Signed:` may carry `Expiration-Date:` and `Re-confirm:` (§4.4).
- **By names (namespace structure).** A name binding hands over a whole subtree: whatever the bound principal later binds under it is reachable. No constraint narrows what Bob may bind in his own space. Scoping by name comes from **where in the chain** a principal is bound, not from any constraint the binding carries.
- **By threshold.** `ANY:` gives k-of-n membership (§7, §7.1). A request signed by several principals pools their memberships (§7.1, "Multiply-signed requests").

**6. Revocation, reconfirmation and online agents.** There are no CRLs (§2, §6.2): *Instead, signatures may be designated as needing periodic reconfirmation.* (§6.2). A signature may carry `Re-confirm: (Period: …) (Principal: …)`. It is then valid only if the original signer, or the named reconfirmation principal (typically a server), has re-signed it within the last period (§4.4, §6.2). A reconfirmation either re-signs the object or returns the newer certificate that superseded it (§6.2). `Expiration-Date:` is a hard limit that reconfirmation cannot extend (§4.4). Servers are on-line agents listed in a principal's `Server-At:` / `Server:` fields. They hold certificates the principal signed, possibly while the principal itself is off-line, and they sign error replies (§4.2, §6.3). Key compromise is handled with no new mechanism: a "hot-list" service keeps a group such as `compromised-principals` (§8.9). A short-lived membership certificate serves as a Kerberos-like ticket (§8.3).

**7. Email addresses.** SDSI 1.1 is the one design in #14's set that **builds email names into its name resolution**. §2 ("DNS names have a special status") makes `Bob.Smith@penguin.microsoft.com` equal to `DNS!!'s com's microsoft's penguin's Bob.Smith`. §5.2 gives the rule. If the string has its own local definition, that is used. Otherwise `name@ak…a2.a1` becomes the first of the forms `(ref: ak…a1.DNS!! name)`, `(ref: a(k-1)…a1.DNS!! ak name)`, …, `(ref: DNS!! a1 a2 … ak name)` whose first component is defined locally. `DNS!!` itself *may not be re-defined*, but the user may define the other `….DNS!!` names locally, which the paper offers as protection against corrupted DNS (§5.2). *This mechanism allows one to write ordinary email addresses in an ACL* (§5.2). Auto-certificates also carry an email name field (§6.3).

**The running example in SDSI 1.1** (our construction from §5.2, not the paper's). Dave binds `foo.com.DNS!!` in his own space to Alice's key. Alice binds `eng` to Bob's key. Bob binds `carol` to Carol's key. Dave's ACL entry `carol@eng.foo.com` then resolves to `(ref: foo.com.DNS!! eng carol)`, i.e. **Dave's** `foo.com.DNS!!`'s `eng`'s `carol`, which is Carol's key. Three things follow:

- Alice's "`*@eng.foo.com` to Bob" is a **name binding**, not a scoped delegation. Bob never signs the string `carol@eng.foo.com`. He binds `carol` in his own space.
- Bob's reach is limited by **position**, not by a constraint. Under Dave's local root, Bob can only answer for names below `eng`.
- If Dave does not bind `foo.com.DNS!!` (or a longer suffix), the same address resolves through the global `DNS!!` root (§5.2). That makes DNS the trust anchor, and §5.2 relies on DNS security *which is soon to appear, we presume*.

Making Alice's grant to Bob an authority over **signing** rather than over names (say, signing `Membership.Cert:` for one group) needs a `Delegation-Cert:`, whose template cannot express a domain suffix (§6.1, §6.4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`core`** | An access-control architecture: ACLs over named groups, a membership-decision algorithm (§7.1), and revocation by reconfirmation (§6.2) |
| Cryptography | `none` | Names RSA-with-SHA1, MD5 and SHA1 as examples (§3.2, §4.1). Defines no primitive. Its signature formats (§4.4) are encoding, not cryptography |
| This project | `adjacent` | The origin of the key-relative naming we keep. We take it through `rfc-2693`, which kept local names and dropped the global roots and the DNS rule |

- **R-M-02** (principal is a key): §2 "Principals are public keys" and §4.2. Identity is the key alone, and the other `Principal:` fields are advisory.
- **R-M-03** (names relative to an issuer): §5.1–§5.2. Every name lives in one principal's space, and `REF` resolves from the current principal. The `!!` special roots and the `DNS!!` fallback are the **counter-case**. They are global names inside a key-relative system, and the paper does not describe how they would be governed (§2).
- **R-M-04** (name and authorization bindings distinct): SDSI 1.1 keeps `Cert:` (name/value), `Membership.Cert:` and `Delegation-Cert:` as separate types (§5.3, §6.4, §7.2), but in a **weaker** form than `rfc-2693`. Authorization here means **group membership** named in an ACL, and §2 says a single certificate can sometimes do more than one job (identity, name/value, membership). There is no authorization-to-key certificate. That arrived with SPKI.
- **R-M-06** (threshold without CA hierarchy): `ANY:` threshold groups and multiply-signed requests (§7, §7.1), in a system with no hierarchy (§2).

## Implementations

**Searched 2026-10-26** (web search for SDSI 1.1 implementations and source code).

| Name | Kind | License | URL |
|---|---|---|---|
| MIT SDSI/SPKI 2.0 distribution | open source, reference code for the **merged 2.0** design | not stated on the page | https://toc.csail.mit.edu/node/213 |

**This search found no implementation of 1.1 as such.** The MIT project page names a SDSI **1.0** C library (Matt Fredette's 1997 MIT thesis) and a 1.0 implementation by Wei Dai. It describes 1.1 as a redesign meant to simplify further and merge with SPKI. The code it distributes is SDSI/SPKI 2.0. The SPKI-era libraries (JSDSI, libspki) are recorded on `rfc-2693` and are not repeated here. All of it is archival.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This record is at the summary bar. It was summarised for **m-of-n/library#14** (the delegation and trust comparison of X.509, S/MIME, OpenPGP and SDSI/SPKI), which needs the section-located facts above and no more. The record is `type: spec`, so FX-1 would apply to any future extraction. That extraction needs **its own issue**: none exists yet, and #14 does not own it. It would mainly add value on §5.2's `REF` and DNS rules, the `MEMBER` algorithm (§7.1), and the reconfirmation protocol (§6.2), which are the parts precise enough to become test vectors.

## Limits

- **A working paper, not a specification.** §2 defers a detailed specification to a companion paper. This record does not hold it and did not find it.
- **Special-root governance is missing.** The `!!` roots, and the `DNS!!` dependency that §5.2 builds email resolution on, rest on procedures §2 declines to describe. This is the part `rfc-2693` removed. It is not set as `contradicts`, because 2693 is SDSI's successor revising it, not a rival claim.
- **Multiple bindings are a union.** Because bindings augment rather than replace (§5.2), and old certificates stay valid until they expire (§5.3), the reliable way to un-bind a name is reconfirmation or a short expiry. "Issue a new certificate" does not do it. A comparison that treats a SDSI name binding as unique is wrong.
- **Delegation is thin.** `Delegation-Cert:` gets one paragraph and one example (§6.4). It does not define re-delegation, how a delegate's signature on a membership certificate is checked against the owner's ACL, or how its template interacts with name evaluation. Anything #14 says beyond the §6.4 text is our inference and should be marked as such.
- **Internal inconsistencies.** §6.3's auto-cert example uses `Email-address:`, the machine-readable field list names `Email:`, and the prose describes `Email-Name:`, all in the same subsection. §7.3's second example binds with `Name:` where §5.3 uses `Local-Name:`. An implementer would have to choose.
- **REF and DNS rule edge case.** `REF2`'s DNS branch is annotated as returning ERROR when P is not a local name space (§5.2). On our reading, an email-form name is therefore meant to be expanded only in the evaluator's own space, not halfway through a chain. The paper does not say this outright.
