---
record: rfc-2693
kind: normative
title: "rfc-2693 — normative statements"
extracted: "2026-10-11"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of RFC 2693
     (SPKI Certificate Theory), VERBATIM, with its locator, in source order.
     Verbatim source only: no analysis, no paraphrase, no opinion. Blockquotes
     and fenced blocks delimit verbatim text; everything outside them is
     structure (headings, locators, labels) only. -->

Source: RFC 2693, "SPKI Certificate Theory", C. Ellison, B. Frantz,
B. Lampson, R. Rivest, B. Thomas, T. Ylonen, September 1999. Network Working
Group, Category: Experimental. 2411 lines, sha256
`6822d668195c3d9b391f0c4f2b023341ba0e5a72e59d63c366a520de42c99098`.

## How to read this file

**Verbatim containers.** Two are used, and the distinction matters:

- A **blockquote** (`>`) reproduces running prose. The source's own line breaks
  are kept and its leading three-space RFC indent is removed; no word, spelling
  or punctuation mark is altered, the source's own typos included.
- A **fenced block** (```` ``` ````) reproduces the source's lines byte-exactly,
  indentation included. Every numbered list, display, rule, worked example and
  S-expression is fenced, together with the prose that introduces and follows
  it in the same run, so whitespace-significant material is never rewrapped.

Everything outside a quote or a fence — headings, statement numbers,
locators, flags, and the italic note on a section that yields no entry — is
structure added by this extraction, not source text. No two non-adjacent
passages are ever spliced into one entry: each entry is a single contiguous
run of source lines.

**Page breaks.** The source is the paginated plain-text RFC. Five entries run
across a page boundary — N-073 (§6), N-075 (§6.1), N-084 (§6.3.1), N-103
(§6.5.1) and N-145 (§8) — and each is flagged `_[page break removed]_`. In
those entries, and only those, the page furniture is deleted: the footer line
(`Ellison, et al.` … `Experimental` … `[Page n]`), the form feed, the running
header (`RFC 2693` … `SPKI Certificate Theory` … `September 1999`) and the
blank padding lines around them. Nothing else is touched. Where the boundary
falls mid-sentence the two halves are joined directly; where it falls between
list items or before a display, one of the source's own blank lines is left in
place, as everywhere else in the source. Every other entry lies wholly within
one page.

**BCP 14 keyword census: 0.** RFC 2693 contains no capitalised BCP 14 keyword
anywhere: no `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`,
`SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY` or `OPTIONAL`. It neither
cites RFC 2119 nor carries the BCP 14 boilerplate. Verified with
`bin/bcp14-count .cache/rfc-2693.txt --by-keyword`, which returns `0`, and with
an independent case-sensitive grep whose only hits are the two `NOT`s in the
Full Copyright Statement's warranty disclaimer (`BUT NOT LIMITED TO`,
`WILL NOT INFRINGE`), which are not BCP 14 usage.

**What counts as normative here.** With no keyword to key on, the document's
binding content is carried by lowercase prose, definitions and rule displays,
as in RFC 9804, but here with no keyword-bearing statement at all. An entry is
included when it does at least one of these:

- defines a term, structure or field: the §1.1 glossary, SDSI names, the
  5-tuple and the 4-tuple, the threshold subject, the `*`-forms;
- states a rule or algorithm: 5-tuple reduction, AIntersect, VIntersect,
  threshold-subject reduction, name reduction, certificate translation;
- states a validity condition or constraint: timed CRLs, timed and one-time
  revalidations, the issuer of validity confirmations;
- records a decision that fixes the design: boolean delegation, no restriction
  on a delegator exercising a permission, the ruling-out of wandering
  anti-matter CRLs, the adoption of SDSI names;
- states a property, assumption or limitation of the adopted design that bears
  on security or correctness;
- carries a lowercase obligation (*must*, *should*, *need(s) to*, *have to*,
  *demands*) that binds an implementation, issuer, verifier, prover,
  keyholder or structure;
- scopes how the rest is to be read: the source states the status of its own
  §6 processing plan in N-071;
- is a worked example that fixes the meaning of one of the above: the SDSI
  name, AIntersect, name-reduction, certificate-translation, SSL tag and
  threshold ACL examples.

When in doubt about an obligation-bearing sentence, it is included. Not
reproduced: history, motivation and commentary, political and philosophical
discussion, the arguments of the three camps in the delegation-depth debate
and the case against the rejected integer control, argument by illustrative
example, a mechanism the document describes but does not adopt (§5.7.1),
navigation and lead-ins, and the front and back matter (Status of this Memo, Copyright
Notice, Table of Contents, References, Acknowledgments, Authors' Addresses,
Full Copyright Statement, Acknowledgement). A lowercase *must* or *have to*
inside excluded material goes with it: the quotation from [DH] in §2, and the
hypotheticals of §2.5 and §7.2. One exception to the rule on mechanisms: where
a decision names what it rules out, the description is kept as the decision's
referent. So the anti-matter CRL of §5.1 (N-051, N-052) is reproduced because
N-054 rules it out, and the [R98] critique of §5.7.2 (N-068, N-069) because
N-070 says SPKI does not reflect it; the *should* in N-069 is the critique's,
not an SPKI rule. Every numbered section keeps its heading below; a section
that yields no entry says so in place, with the reason.

Inside sections that do yield entries, exactly these paragraphs are not
reproduced, so that every omission is a recorded decision rather than a drop:

- §2.4: all but its two entries, namely eight paragraphs on names as
  identifiers and on a global database of persons (philosophy, commentary);
- §2.6: the opening sentence (rhetoric);
- §2.7: the first two paragraphs (motivation);
- §3: the closing pointer to §3.1–§3.4 (navigation);
- §4: the second paragraph, which announces §4.1 and §4.2 (navigation);
- §4.1.4: the paragraph on why integer control was defeated (the case
  against a rejected alternative);
- §5.1: the first two paragraphs, on printed books of bad account numbers
  (history);
- §7.4: the last paragraph, on how different entities approach these
  requirements (commentary).

**The `_[lowercase/implied]_` marker.** In the library's other normative
extractions the marker flags an entry that carries binding content but no
BCP 14 keyword of its own. Here the census is zero, so **every entry carries
the marker**. It distinguishes nothing within this file; it is kept so that
the convention reads the same way across the library.

**Lowercase modal census of the entries**, for reconciliation with
`requirements.yaml`, counted mechanically over the verbatim text: *must* 25
times in 22 entries (N-011, N-012, N-013, N-021, N-024, N-026, N-027, N-030,
N-033, N-035, N-050, N-055, N-057, N-060, N-061, N-080, N-099, N-103, N-122,
N-138, N-145, N-146); *should* 14 times in 12 entries (N-008, N-014, N-027,
N-066, N-069, N-085, N-094, N-096, N-098, N-106, N-127, N-142). Neither is a
BCP 14 keyword.

**Citations.** Bracketed citations inside the captured text ([SDSI], [UPKI],
[ELIEN], [ECR], [R98] and the rest) resolve in the source's References
section, which is not reproduced.

**Counts.** 146 entries, `N-001` to `N-146`, in source order. They come from 54
of the 68 headed sections (the Abstract and 67 numbered sections); the other 14
yield no entry. Every entry carries `_[lowercase/implied]_`.


## Abstract

**N-001.** (Abstract) _[lowercase/implied]_

> The SPKI Working Group has developed a standard form for digital
> certificates whose main purpose is authorization rather than
> authentication.  These structures bind either names or explicit
> authorizations to keys or other objects.  The binding to a key can be
> directly to an explicit key, or indirectly through the hash of the
> key or a name for it.  The name and authorization structures can be
> used separately or together.  We use S-expressions as the standard
> format for these certificates and define a canonical form for those
> S-expressions.  As part of this development, a mechanism for deriving
> authorization decisions from a mixture of certificate types was
> developed and is presented in this document.

**N-002.** (Abstract) _[lowercase/implied]_

> This document gives the theory behind SPKI certificates and ACLs
> without going into technical detail about those structures or their
> uses.


## Section 1. Overview of Contents

_No entries — a guide to the sections that follow; no definition or
obligation._


### Section 1.1. Glossary

**N-003.** (§1.1 (lead-in)) _[lowercase/implied]_

> We use some terms in the body of this document in ways that could be
> specific to SPKI:

**N-004.** (§1.1 (ACL)) _[lowercase/implied]_

> ACL: an Access Control List: a list of entries that anchors a
> certificate chain.  Sometimes called a "list of root keys", the ACL
> is the source of empowerment for certificates.  That is, a
> certificate communicates power from its issuer to its subject, but
> the ACL is the source of that power (since it theoretically has the
> owner of the resource it controls as its implicit issuer).  An ACL
> entry has potentially the same content as a certificate body, but has
> no Issuer (and is not signed).  There is most likely one ACL for each
> resource owner, if not for each controlled resource.

**N-005.** (§1.1 (CERTIFICATE)) _[lowercase/implied]_

> CERTIFICATE: a signed instrument that empowers the Subject.  It
> contains at least an Issuer and a Subject.  It can contain validity
> conditions, authorization and delegation information.  Certificates
> come in three categories: ID (mapping <name,key>), Attribute (mapping
> <authorization,name>), and Authorization (mapping
> <authorization,key>).  An SPKI authorization or attribute certificate
> can pass along all the empowerment it has received from the Issuer or
> it can pass along only a portion of that empowerment.

**N-006.** (§1.1 (ISSUER)) _[lowercase/implied]_

> ISSUER: the signer of a certificate and the source of empowerment
> that the certificate is communicating to the Subject.

**N-007.** (§1.1 (KEYHOLDER)) _[lowercase/implied]_

> KEYHOLDER: the person or other entity that owns and controls a given
> private key.  This entity is said to be the keyholder of the keypair
> or just the public key, but control of the private key is assumed in
> all cases.

**N-008.** (§1.1 (PRINCIPAL)) _[lowercase/implied]_

> PRINCIPAL: a cryptographic key, capable of generating a digital
> signature.  We deal with public-key signatures in this document but
> any digital signature method should apply.

**N-009.** (§1.1 (SPEAKING)) _[lowercase/implied]_

> SPEAKING: A Principal is said to "speak" by means of a digital
> signature.  The statement made is the signed object (often a
> certificate).  The Principal is said to "speak for" the Keyholder.

**N-010.** (§1.1 (SUBJECT)) _[lowercase/implied]_

> SUBJECT: the thing empowered by a certificate or ACL entry.  This can
> be in the form of a key, a name (with the understanding that the name
> is mapped by certificate to some key or other object), a hash of some
> object, or a set of keys arranged in a threshold function.

**N-011.** (§1.1 (S-EXPRESSION)) _[lowercase/implied]_

> S-EXPRESSION: the data format chosen for SPKI/SDSI.  This is a LISP-
> like parenthesized expression with the limitations that empty lists
> are not allowed and the first element in any S-expression must be a
> string, called the "type" of the expression.

**N-012.** (§1.1 (THRESHOLD SUBJECT)) _[lowercase/implied]_

> THRESHOLD SUBJECT: a Subject for an ACL entry or certificate that
> specifies K of N other Subjects.  Conceptually, the power being
> transmitted to the Subject by the ACL entry or certificate is
> transmitted in (1/K) amount to each listed subordinate Subject.  K of
> those subordinate Subjects must agree (by delegating their shares
> along to the same object or key) for that power to be passed along.
> This mechanism introduces fault tolerance and is especially useful in
> an ACL entry, providing fault tolerance for "root keys".


## Section 2. Name Certification

_No entries — history of name certification (Diffie and Hellman's public
directory, Kohnfelder's thesis). Its one lowercase "must" belongs to the
quotation from [DH]._


### Section 2.1. First Definition of CERTIFICATE

_No entries — history (Kohnfelder's construct and the origin of the word
CERTIFICATE)._


### Section 2.2. The X.500 Plan and X.509

_No entries — history of X.500 and X.509, and commentary on their prospects._


### Section 2.3. X.509, PEM and PGP

_No entries — history (PEM, RIPEM, MOSS, PGP's web of trust)._


### Section 2.4. Rethinking Global Names

**N-013.** (§2.4) _[lowercase/implied]_

> Computer applications need to make decisions about keyholders.  These
> decisions are almost never made strictly on the basis of a
> keyholder's name.  There is some other fact about the keyholder of
> interest to the application (or to the human being running the
> application).  If a name functions at all for security purposes, it
> is as an index into some database (or human memory) of that other
> information.  To serve in this role, the name must be unique, in
> order to serve as an index, and there must be some information to be
> indexed.

**N-014.** (§2.4) _[lowercase/implied]_

> Where globally unique identifiers need to be used, perhaps the best
> ID is one that is uniform in appearance (such as a long number or
> random looking text string) so that it has no recognizable sub-field.
> It should also be large enough (from a sparse enough name space) that
> typographical errors would not yield another valid identifier.


### Section 2.5. Inescapable Identifiers

_No entries — political and philosophical discussion of inescapable
identifiers. It states no rule; its "would have to" is hypothetical._


### Section 2.6. Local Names

**N-015.** (§2.6) _[lowercase/implied]_

> The names we use are local names.  These are the names we write in
> our personal address books or use as nicknames or aliases with e-mail
> agents.  They can be IDs assigned by corporations (e.g., bank account
> numbers or employee numbers).  Those names or IDs do not need to be
> globally unique.  Rather, they need to be unique for the one entity
> that maintains that address book, e-mail alias file or list of
> accounts.  More importantly, they need to be meaningful to the person
> who uses them as indexes.

**N-016.** (§2.6) _[lowercase/implied]_

> Ron Rivest and Butler Lampson showed with SDSI 1.0 [SDSI] that one
> can not only use local names locally, one can use local names
> globally.  The clear security advantage and operational simplicity of
> SDSI names caused us in the SPKI group to adopt SDSI names as part of
> the SPKI standard.


#### Section 2.6.1. Basic SDSI Names

**N-017.** (§2.6.1) _[lowercase/implied]_

```
   A basic SDSI 2.0 name is an S-expression with two elements: the word
   "name" and the chosen name.  For example,

        george:  (name fred)

   represents a basic SDSI name "fred" in the name space defined by
   george.
```


#### Section 2.6.2. Compound SDSI Names

**N-018.** (§2.6.2) _[lowercase/implied]_

```
   If fred in turn defines a name, for example,

        fred:  (name sam)

   then george can refer to this same entity as

        george:  (name fred sam)
```


### Section 2.7. Sources of Global Identifiers

**N-019.** (§2.7) _[lowercase/implied]_

> When one creates a key pair, for use in public key cryptography, the
> private key is bound to its owner by good key safeguarding practice.
> If that private key gets loose from its owner, then a basic premise
> of public key cryptography has been violated and that key is no
> longer of interest.

**N-020.** (§2.7) _[lowercase/implied]_

> The private key is also globally unique.  If it were not, then the
> key generation process would be seriously flawed and we would have to
> abandon this public key system implementation.

**N-021.** (§2.7) _[lowercase/implied]_

> The private key must be kept secret, so it is not a possible
> identifier, but each public key corresponds to one private key and
> therefore to one keyholder.  The public key, viewed as a byte string,
> is therefore an identifier for the keyholder.

**N-022.** (§2.7) _[lowercase/implied]_

> If there exists a collision-free hash function, then a collision-free
> hash of the public key is also a globally unique identifier for the
> keyholder, and probably a shorter one than the public key.


### Section 2.8. Fully Qualified SDSI Names

**N-023.** (§2.8) _[lowercase/implied]_

> SDSI local names are of great value to their definer.  Each local
> name maps to one or more public keys and therefore to the
> corresponding keyholder(s).  Through SDSI's name chaining, these
> local names become useful potentially to the whole world.  [See
> section 2.6.2 for an example of SDSI name chaining.]

**N-024.** (§2.8) _[lowercase/implied]_

> To a computer system making use of these names, the name string is
> not enough.  One must identify the name space in which that byte
> string is defined.  That name space can be identified globally by a
> public key.

**N-025.** (§2.8) _[lowercase/implied]_

> It is SDSI 1.0 convention, preserved in SPKI, that if a (local) SDSI
> name occurs within a certificate, then the public key of the issuer
> is the identifier of the name space in which that name is defined.

**N-026.** (§2.8) _[lowercase/implied]_

```
   However, if a SDSI name is ever to occur outside of a certificate,
   the name space within which it is defined must be identified.  This
   gives rise to the Fully Qualified SDSI Name.  That name is a public
   key followed by one or more names relative to that key.  If there are
   two or more names, then the string of names is a SDSI name chain.
   For example,

        (name (hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|) jim therese)

   is a fully qualified SDSI name, using the SHA-1 hash of a public key
   as the global identifier defining the name space and anchoring this
   name string.
```


### Section 2.9. Fully Qualified X.509 Names

**N-027.** (§2.9) _[lowercase/implied]_

```
   An X.509 Distinguished Name can and sometimes must be expressed as a
   Fully Qualified Name.  If the PEM or original X.500 vision of a
   single root for a global name space had come true, this wouldn't be
   necessary because all names would be relative to that same one root
   key.  However, there is not now and is not likely ever to be a single
   root key.  Therefore, every X.509 name should be expressed as the
   pair

        (name <root key> <leaf name>)

   if all leaf names descending from that root are unique.  If
   uniqueness is enforced only within each individual CA, then one would
   build a Fully Qualified Name chain from an X.509 certificate chain,
   yielding the form

        (name <root key> <CA(1)> <CA(2)> ... <CA(k)> <leaf name>).
```


### Section 2.10. Group Names

**N-028.** (§2.10) _[lowercase/implied]_

> SPKI/SDSI does not claim to enforce one key per name.  Therefore, a
> named group can be defined by issuing multiple (name,key)
> certificates with the same name -- one for each group member.


## Section 3. Authorization

**N-029.** (§3) _[lowercase/implied]_

> Fully qualified SDSI names represent globally unique names, but at
> every step of their construction the local name used is presumably
> meaningful to the issuer.  Therefore, with SDSI name certificates one
> can identify the keyholder by a name relevant to someone.

**N-030.** (§3) _[lowercase/implied]_

> However, what an application needs to do, when given a public key
> certificate or a set of them, is answer the question of whether the
> remote keyholder is permitted some access.  That application must
> make a decision.  The data needed for that decision is almost never
> the spelling of a keyholder's name.

**N-031.** (§3) _[lowercase/implied]_

> Instead, the application needs to know if the keyholder is authorized
> for some access.  This is the primary job of a certificate, according
> to the members of the SPKI WG, and the SPKI certificate was designed
> to meet this need as simply and directly as possible.

**N-032.** (§3) _[lowercase/implied]_

> We realize that the world is not going to switch to SPKI certificates
> overnight.  Therefore, we developed an authorization computation
> process that can use certificates in any format.  That process is
> described below in section 6.


### Section 3.1. Attribute Certificates

**N-033.** (§3.1) _[lowercase/implied]_

```
   An Attribute Certificate, as defined in X9.57, binds an attribute
   that could be an authorization to a Distinguished Name.  For an
   application to use this information, it must combine an attribute
   certificate with an ID certificate, in order to get the full mapping:

        authorization -> name -> key
```

**N-034.** (§3.1) _[lowercase/implied]_

> Presumably the two certificates involved came from different issuers,
> one an authority on the authorization and the other an authority on
> names.  However, if either of these issuers were subverted, then an
> attacker could obtain an authorization improperly.  Therefore, both
> the issuers need to be trusted with the authorization decision.


### Section 3.2. X.509v3 Extensions

**N-035.** (§3.2) _[lowercase/implied]_

```
   X.509v3 permits general extensions.  These extensions can be used to
   carry authorization information.  This makes the certificate an
   instrument mapping both:

        authorization -> key

   and

        name -> key

   In this case, there is only one issuer, who must be an authority on
   both the authorization and the name.
```

**N-036.** (§3.2) _[lowercase/implied]_

> Some propose issuing a master X.509v3 certificate to an individual
> and letting extensions hold all the attributes or authorizations the
> individual would need.  This would require the issuer to be an
> authority on all of those authorizations.  In addition, this
> aggregation of attributes would result in shortening the lifetime of
> the certificate, since each attribute would have its own lifetime.
> Finally, aggregation of attributes amounts to the building of a
> dossier and represents a potential privacy violation.

**N-037.** (§3.2) _[lowercase/implied]_

> For all of these reasons, it is desirable that authorizations be
> limited to one per certificate.


### Section 3.3. SPKI Certificates

**N-038.** (§3.3) _[lowercase/implied]_

```
   A basic SPKI certificate defines a straight authorization mapping:

        authorization -> key
```

**N-039.** (§3.3) _[lowercase/implied]_

```
   If someone wants access to a keyholder's name, for logging purposes
   or even for punishment after wrong-doing, then one can map from key
   to location information (name, address, phone, ...) to get:

        authorization -> key -> name
```

**N-040.** (§3.3) _[lowercase/implied]_

```
   This mapping has an apparent security advantage over the attribute
   certificate mapping.  In the mapping above, only the

        authorization -> key

   mapping needs to be secure at the level required for the access
   control mechanism.  The

        key -> name

   mapping (and the issuer of any certificates involved) needs to be
   secure enough to satisfy lawyers or private investigators, but a
   subversion of this mapping does not permit the attacker to defeat the
   access control.  Presumably, therefore, the care with which these
   certificates (or database entries) are created is less critical than
   the care with which the authorization certificate is issued.  It is
   also possible that the mapping to name need not be on-line or
   protected as certificates, since it would be used by human
   investigators only in unusual circumstances.
```


### Section 3.4. ACL Entries

**N-041.** (§3.4) _[lowercase/implied]_

> SDSI 1.0 defined an ACL, granting authorization to names.  It was
> then like an attribute certificate, except that it did not need to be
> signed or issued by any key.  It was held in local memory and was
> assumed issued by the owner of the computer and therefore of the
> resource being controlled.

**N-042.** (§3.4) _[lowercase/implied]_

> In SPKI, an ACL entry is free to be implemented in any way the
> developer chooses, since it is never communicated and therefore does
> not need to be standardized.  However, a sample implementation is
> documented, as a certificate body minus the issuer field.  The ACL
> entry can have a name as a subject, as in SDSI 1.0, or it can have a
> key as a subject.  Examples of the latter include the list of SSL
> root keys in an SSL capable browser or the file .ssh/authorized_keys
> in a user's home UNIX directory.  Those ACLs are single-purpose, so
> the individual entries do not carry explicit authorizations, but SPKI
> uses explicit authorizations so that one can use common authorization
> computation code to deal with multiple applications.


## Section 4. Delegation

**N-043.** (§4) _[lowercase/implied]_

> One of the powers of an authorization certificate is the ability to
> delegate authorizations from one person to another without bothering
> the owner of the resource(s) involved.  One might issue a simple
> permission (e.g., to read some file) or issue the permission to
> delegate that permission further.


### Section 4.1. Depth of Delegation

**N-044.** (§4.1) _[lowercase/implied]_

> There were three camps in discussing depth of delegation: no control,
> boolean control and integer control.  There remain camps in favor of
> each of these, but a decision was reached in favor of boolean
> control.


#### Section 4.1.1. No control

_No entries — the argument of the no-control camp, which did not prevail. The
decision is in §4.1 and §4.1.4._


#### Section 4.1.2. Boolean control

_No entries — the argument of the boolean-control camp (the Commerce Department
example). The decision itself is stated in §4.1 and §4.1.4._


#### Section 4.1.3. Integer control

_No entries — the argument of the integer-control camp, which did not prevail.
The decision is in §4.1 and §4.1.4._


#### Section 4.1.4. The choice: boolean

**N-045.** (§4.1.4) _[lowercase/implied]_

> Of these three, the group chose boolean control.  The subject of a
> certificate or ACL entry may exercise any permission granted and, if
> delegation is TRUE, may also delegate that permission or some subset
> of it to others.

**N-046.** (§4.1.4) _[lowercase/implied]_

> The no control argument has logical appeal, but there remains the
> assumption that a user will value his or her private key enough not
> to loan it out or that the key will be locked in hardware where it
> can't be copied to any other user.  This doesn't prevent the user
> from setting up a signing oracle, but lack of network connectivity
> might inhibit that mechanism.

**N-047.** (§4.1.4) _[lowercase/implied]_

> As for controlling the proliferation of permissions, there is no
> control on the width of the delegation tree, so control on its depth
> is not a tight control on proliferation.


### Section 4.2. May a Delegator Also Exercise the Permission?

**N-048.** (§4.2) _[lowercase/implied]_

> We decided that a delegator is free to create a new key pair, also
> controlled by it, and delegate the rights to that key to exercise the
> delegated permission.  Therefore, there was no benefit from
> attempting to restrict the exercise of a permission by someone
> permitted to delegate it.


### Section 4.3. Delegation of Authorization vs. ACLs

_No entries — an argument by worked example (a DoD firewall) for delegated
authorization over nested ACLs. It is illustrative and states no rule._


## Section 5. Validity Conditions

**N-049.** (§5) _[lowercase/implied]_

> A certificate, or an ACL entry, has optional validity conditions.
> The traditional ones are validity dates: not-before and not-after.
> The SPKI group resolved, in discussion, that on-line tests of various
> kinds are also validity conditions.  That is, they further refine the
> valid date range of a certificate.  Three kinds of on-line tests are
> envisioned: CRL, re-validation and one-time.

**N-050.** (§5) _[lowercase/implied]_

> When validity confirmation is provided by some online test, then the
> issuer of those refinements need not be the issuer of the original
> certificate.  In many cases, the business or security model for the
> two issuers is different.  However, in SPKI, the certificate issuer
> must specify the issuer of validity confirmations.


### Section 5.1. Anti-matter CRLs

**N-051.** (§5.1) _[lowercase/implied]_

> An early CRL design followed this model.  It had a list of revoked
> certificate identifiers.  It also had a sequence number, so that one
> could tell which of two CRLs was more recent.  A newer CRL would
> replace an older one.

**N-052.** (§5.1) _[lowercase/implied]_

> This mode of operation is like wandering anti-matter.  When the
> issuer wants to revoke a certificate, it is listed in the next CRL to
> go out.  If the revocation is urgent, then that CRL can be released
> immediately.  The CRL then follows some dissemination process
> unrelated to the needs of the consumers of the CRL.  If the CRL
> encounters a certificate it has listed, it effectively annihilates
> that certificate.  If it encounters an older CRL, it annihilates that
> CRL also, leaving a copies of itself at the verifiers it encounters.

**N-053.** (§5.1) _[lowercase/implied]_

> However, this process is non-deterministic.  The result of the
> authorization computation is at least timing dependent.  Given an
> active adversary, it can also be a security hole.  That is, an
> adversary can prevent revocation of a given certificate by preventing
> the delivery of new CRLs.  This does not require cryptographic level
> effort, merely network tampering.

**N-054.** (§5.1) _[lowercase/implied]_

> SPKI has ruled out the use of wandering anti-matter CRLs for its
> certificates.  Every authorization computation is deterministic,
> under SPKI rules.


### Section 5.2. Timed CRLs

**N-055.** (§5.2 (three conditions)) _[lowercase/implied]_

```
   SPKI permits use of timed CRLs.  That is, if a certificate can be
   referenced in a CRL, then the CRL process is subject to three
   conditions.

   1.  The certificate must list the key (or its hash) that will sign
       the CRL and may give one or more locations where that CRL might
       be fetched.

   2.  The CRL must carry validity dates.

   3.  CRL validity date ranges must not intersect.  That is, one may
       not issue a new CRL to take effect before the expiration of the
       CRL currently deployed.
```

**N-056.** (§5.2) _[lowercase/implied]_

> Under these rules, no certificate that might use a CRL can be
> processed without a valid CRL and no CRL can be issued to show up as
> a surprise at the verifier.  This yields a deterministic validity
> computation, independent of clock skew, although clock inaccuracies
> in the verifier may produce a result not desired by the issuer.  The
> CRL in this case is a completion of the certificate, rather than a
> message to the world announcing a change of mind.

**N-057.** (§5.2 (delta-CRLs)) _[lowercase/implied]_

> Since CRLs might get very large and since they tend to grow
> monotonically, one might want to issue changes to CRLs rather than
> full ones.  That is, a CRL might be a full CRL followed by a sequence
> of delta-CRLs.  That sequence of instruments is then treated as a
> current CRL and the combined CRL must follow the conditions listed
> above.


### Section 5.3. Timed Revalidations

**N-058.** (§5.3) _[lowercase/implied]_

> CRLs are negative statements.  The positive version of a CRL is what
> we call a revalidation.  Typically a revalidation would list only one
> certificate (the one of interest), although it might list a set of
> certificates (to save digital signature effort).

**N-059.** (§5.3) _[lowercase/implied]_

> As with the CRL, SPKI demands that this process be deterministic and
> therefore that the revalidation follow the same rules listed above
> (in section 5.2).


### Section 5.4. Setting the Validity Interval

**N-060.** (§5.4) _[lowercase/implied]_

> Both timed CRLs and timed revalidations have non-0 validity
> intervals.  To set this validity interval, one must answer the
> question: "How long are you willing to let the world believe and act
> on a statement you know to be false?"

**N-061.** (§5.4) _[lowercase/implied]_

> That is, one must assume that the previous CRL or revalidation has
> just been signed and transmitted to at least one consumer, locking up
> a time slot.  The next available time slot starts after this validity
> interval ends.  That is the earliest one can revoke a certificate one
> learns to be false.

**N-062.** (§5.4) _[lowercase/implied]_

> The answer to that question comes from risk management.  It will
> probably be based on expected monetary losses, at least in commercial
> cases.


### Section 5.5. One-time Revalidations

**N-063.** (§5.5) _[lowercase/implied]_

> Validity intervals of length zero are not possible.  Since
> transmission takes time, by the time a CRL was received by the
> verifier, it would be out of date and unusable.  That assumes perfect
> clock synchronization.  If clock skew is taken into consideration,
> validity intervals need to be that much larger to be meaningful.

**N-064.** (§5.5) _[lowercase/implied]_

> For those who want to set the validity interval to zero, SPKI defines
> a one-time revalidation.

**N-065.** (§5.5) _[lowercase/implied]_

> This form of revalidation has no lifetime beyond the current
> authorization computation.  One applies for this on-line, one-time
> revalidation by submitting a request containing a nonce.  That nonce
> gets returned in the signed revalidation instrument, in order to
> prevent replay attacks.  This protocol takes the place of a validity
> date range and represents a validity interval of zero, starting and
> ending at the time the authorization computation completes.


### Section 5.6. Short-lived Certificates

**N-066.** (§5.6) _[lowercase/implied]_

> A performance analysis of the various methods of achieving fine-grain
> control over the validity interval of a certificate should consider
> the possibility of just making the original certificate short-lived,
> especially if the online test result is issued by the same key that
> issued the certificate.  There are cases in which the short-lived
> certificate requires fewer signatures and less network traffic than
> the various online test options.  The use of a short-lived
> certificate always requires fewer signature verifications than the
> use of certificate plus online test result.

**N-067.** (§5.6) _[lowercase/implied]_

> If one wants to issue short-lived certificates, SPKI defines a kind
> of online test statement to tell the user of the certificate where a
> replacement short-lived certificate might be fetched.


### Section 5.7. Other possibilities

_No entries — a one-sentence lead-in to §5.7.1 and §5.7.2._


#### Section 5.7.1. Micali's Inexpensive On-line Results

_No entries — describes a patented hash-chain mechanism [ECR] that the document
does not adopt._


#### Section 5.7.2. Rivest's Reversal of the CRL Logic

**N-068.** (§5.7.2) _[lowercase/implied]_

> Ron Rivest has written a paper [R98] suggesting that the whole
> validity condition model is flawed because it assumes that the issuer
> (or some entity to which it delegates this responsibility) decides
> the conditions under which a certificate is valid.  That traditional
> model is consistent with a military key management model, in which
> there is some central authority responsible for key release and for
> determining key validity.

**N-069.** (§5.7.2) _[lowercase/implied]_

> However, in the commercial space, it is the verifier and not the
> issuer who is taking a risk by accepting a certificate.  It should
> therefore be the verifier who decides what level of assurance he
> needs before accepting a credential.  That verifier needs information
> from the issuer, and the more recent that information the better, but
> the decision is the verifier's in the end.

**N-070.** (§5.7.2) _[lowercase/implied]_

> This line of thought deserves further consideration, but is not
> reflected in the SPKI structure definition.  It might even be that
> both the issuer and the verifier have stakes in this decision, so
> that any replacement validity logic would have to include inputs from
> both.


## Section 6. Tuple Reduction

**N-071.** (§6) _[lowercase/implied]_

> The processing of certificates and related objects to yield an
> authorization result is the province of the developer of the
> application or system.  The processing plan presented here is an
> example that may be followed, but its primary purpose is to clarify
> the semantics of an SPKI certificate and the way it and various other
> kinds of certificate might be used to yield an authorization result.

**N-072.** (§6 (inputs)) _[lowercase/implied]_

```
   There are three kinds of entity that might be input to the
   computation that yields an authorization result:

    1.  <name,key> (as a certificate)

    2.  <authorization,name> (as an attribute certificate or ACL entry)

    3.  <authorization,key> (as an authorization certificate or ACL
        entry)
```

**N-073.** (§6 (three stages)) _[lowercase/implied]_ _[page break removed]_

```
   These entities are processed in three stages.

    1.  Individual certificates are verified by checking their
        signatures and possibly performing other work.  They are then
        mapped to intermediate forms, called "tuples" here.

        The other work for SPKI or SDSI certificates might include
        processing of on-line test results (CRL, re-validation or one-
        time validation).

        The other work for PGP certificates may include a web-of-trust
        computation.

        The other work for X.509 certificates depends on the written
        documentation for that particular use of X.509 (typically tied
        to the root key from which the certificate descended) and could
        involve checking information in the parent certificate as well
        as additional information in extensions of the certificate in
        question.  That is, some use X.509 certificates just to define
        names.  Others use X.509 to communicate an authorization
        implicitly (e.g., SSL server certificates).  Some might define
        extensions of X.509 to carry explicit authorizations.  All of
        these interpretations are specified in written documentation
        associated with the certificate chain and therefore with the
        root from which the chain descends.

        If on-line tests are involved in the certificate processing,
        then the validity dates of those on-line test results are
        intersected by VIntersect() [defined in 6.3.2, below] with the
        validity dates of the certificate to yield the dates in the
        certificate's tuple(s).

    2.  Uses of names are replaced with simple definitions (keys or
        hashes), based on the name definitions available from reducing
        name 4-tuples.

    3.  Authorization 5-tuples are then reduced to a final authorization
        result.
```


### Section 6.1. 5-tuple Defined

**N-074.** (§6.1) _[lowercase/implied]_

> The 5-tuple is an intermediate form, assumed to be held in trusted
> memory so that it doesn't need a digital signature for integrity.  It
> is produced from certificates or other credentials via trusted
> software.  Its contents are the same as the contents of an SPKI
> certificate body, but it might be derived from another form of
> certificate or from an ACL entry.

**N-075.** (§6.1 (elements)) _[lowercase/implied]_ _[page break removed]_

```
   The elements of a 5-tuple are:

    1.  Issuer: a public key (or its hash), or the reserved word "Self".
        This identifies the entity speaking this intermediate result.

    2.  Subject: a public key (or its hash), a name used to identify a
        public key, the hash of an object or a threshold function of
        subordinate subjects.  This identifies the entity being spoken
        about in this intermediate result.

    3.  Delegation: a boolean.  If TRUE, then the Subject is permitted
        by the Issuer to further propagate the authorization in this
        intermediate result.

    4.  Authorization: an S-expression.  [Rules for combination of
        Authorizations are given below.]

    5.  Validity dates: a not-before date and a not-after date, where
        "date" means date and time.  If the not-before date is missing
        from the source credential then minus infinity is assumed.  If
        the not-after date is missing then plus infinity is assumed.
```


### Section 6.2. 4-tuple Defined

**N-076.** (§6.2) _[lowercase/implied]_

> A <name,key> certificate (such as X.509v1 or SDSI 1.0) carries no
> authorization field but does carry a name.  Since it is qualitatively
> different from an authorization certificate, a separate intermediate
> form is defined for it.

**N-077.** (§6.2 (elements)) _[lowercase/implied]_

```
   The elements of a Name 4-tuple are:

    1.  Issuer: a public key (or its hash).  This identifies the entity
        defining this name in its private name space.

    2.  Name: a byte string

    3.  Subject: a public key (or its hash), a name, or a threshold
        function of subordinate subjects.  This defines the name.

    4.  Validity dates: a not-before date and a not-after date, where
        "date" means date and time.  If the not-before date is missing
        from the source credential then minus infinity is assumed.  If
        the not-after date is missing then plus infinity is assumed.
```


### Section 6.3. 5-tuple Reduction Rules

**N-078.** (§6.3 (rule)) _[lowercase/implied]_

```
   The two 5-tuples:

      <I1,S1,D1,A1,V1> + <I2,S2,D2,A2,V2>

   yield

         <I1,S2,D2,AIntersect(A1,A2),VIntersect(V1,V2)>

   provided

       the two intersections succeed,

       S1 = I2

   and

       D1 = TRUE
```

**N-079.** (§6.3 (threshold subject)) _[lowercase/implied]_

> If S1 is a threshold subject, there is a slight modification to this
> rule, as described below in section 6.3.3.


#### Section 6.3.1. AIntersect

**N-080.** (§6.3.1) _[lowercase/implied]_

> An authorization is a list of strings or sub-lists, of meaning to and
> probably defined by the application that will use this authorization
> for access control.  Two authorizations intersect by matching,
> element for element.  If one list is longer than the other but match
> at all elements where both lists have elements, then the longer list
> is the result of the intersection.  This means that additional
> elements of a list must restrict the permission granted.

**N-081.** (§6.3.1) _[lowercase/implied]_

> Although actual authorization string definitions are application
> dependent, AIntersect provides rules for automatic intersection of
> these strings so that application developers can know the semantics
> of the strings they use.  Special semantics would require special
> reduction software.

**N-082.** (§6.3.1 (example)) _[lowercase/implied]_

```
   For example, there might be an ftpd that allows public key access
   control, using authorization certificates.  Under that service,

       (ftp (host ftp.clark.net))

   might imply that the keyholder would be allowed ftp access to all
   directories on ftp.clark.net, with all kinds of access (read, write,
   delete, ...).  This is more general (allows more access) than

       (ftp (host ftp.clark.net) (dir /pub/cme))

   which would allow all kinds of access but only in the directory
   specified.  The intersection of the two would be the second.
```

**N-083.** (§6.3.1 (positional form)) _[lowercase/implied]_

```
   Since the AIntersect rules imply position dependency, one could also
   define the previous authorization string as:

       (ftp ftp.clark.net /pub/cme)

   to keep the form compact.
```

**N-084.** (§6.3.1 (*-forms)) _[lowercase/implied]_ _[page break removed]_

```
   To allow for wild cards, there are a small number of special S-
   expressions defined, using "*" as the expression name.

   (*)
             stands for the set of all S-expressions and byte-strings.
             In other words, it will match anything.  When intersected
             with anything, the result is that other thing.  [The
             AIntersect rule about lists of different length treats a
             list as if it had enough (*) entries implicitly appended to
             it to match the length of another list with which it was
             being intersected.]

   (* set <tag-expr>*)
             stands for the set of elements listed in the *-form.

   (* prefix <byte-string>)
             stands for the set of all byte strings that start with the
             one given in the *-form.

   (* range <ordering> <lower-limit>? <upper-limit>?)
             stands for the set of all byte strings lexically (or
             numerically) between the two limits.  The ordering
             parameter (alpha, numeric, time, binary, date) specifies
             the kind of strings allowed.
```

**N-085.** (§6.3.1) _[lowercase/implied]_

> AIntersect() is normal set intersection, when *-forms are defined as
> they are above and a normal list is taken to mean all lists that
> start with those elements.  The following examples should give a more
> concrete explanation for those who prefer an explanation without
> reference to set operations.

**N-086.** (§6.3.1 (examples)) _[lowercase/implied]_

```
   AIntersect( (tag (ftp ftp.clark.net cme (* set read write))),
               (tag (*)) )

   evaluates to (tag (ftp ftp.clark.net cme (* set read write)))

   AIntersect( (tag (* set read write (foo bla) delete)),
               (tag (* set write read) ) )

   evaluates to (tag (* set read write))

   AIntersect( (tag (* set read write (foo bla) delete)),
               (tag read ) )

   evaluates to (tag read)

   AIntersect( (tag (* prefix http://www.clark.net/pub/)),
               (tag (* prefix http://www.clark.net/pub/cme/html/)) )

   evaluates to (tag (* prefix http://www.clark.net/pub/cme/html/))

   AIntersect( (tag (* range numeric ge #30# le #39# )), (tag #26#) )

   fails to intersect.
```


#### Section 6.3.2. VIntersect

**N-087.** (§6.3.2 (definition)) _[lowercase/implied]_

```
   Date range intersection is straight-forward.

       V = VIntersect( X, Y )

   is defined as

       Vmin = max( Xmin, Ymin )

       Vmax = min( Xmax, Ymax )

   and if Vmin > Vmax, then the intersection failed.
```

**N-088.** (§6.3.2) _[lowercase/implied]_

> These rules assume that daytimes are expressed in a monotonic form,
> as they are in SPKI.

**N-089.** (§6.3.2 (online tests)) _[lowercase/implied]_

> The full SPKI VIntersect() also deals with online tests.  In the most
> straight-forward implementation, each online test to which a
> certificate is subject is evaluated.  Each such test carries with it
> a validity interval, in terms of dates.  That validity interval is
> intersected with any present in the certificate, to yield a new,
> current validity interval.

**N-090.** (§6.3.2 (deferred online tests)) _[lowercase/implied]_

> It is possible for an implementation of VIntersect() to gather up
> online tests that are present in each certificate and include the
> union of all those tests in the accumulating tuples.  In this case,
> the evaluation of those online tests is deferred until the end of the
> process.  This might be appropriate if the tuple reduction is being
> performed not for answering an immediate authorization question but
> rather for generation of a summary certificate (Certificate Result
> Certificate) that one might hope would be useful for a long time.


#### Section 6.3.3. Threshold Subjects

**N-091.** (§6.3.3) _[lowercase/implied]_

> A threshold subject is specified by two numbers, K and N [0<K<=N],
> and N subordinate subjects.  A threshold subject is reduced to a
> single subject by selecting K of the N subjects and reducing each of
> those K to the same subject, through a sequence of certificates.  The
> (N-K) unselected subordinate subjects are set to (null).

**N-092.** (§6.3.3) _[lowercase/implied]_

> The intermediate form for a threshold subject is a copy of the tuple
> in which the threshold subject appears, but with only one of the
> subordinate subjects.  Those subordinate tuples are reduced
> individually until the list of subordinate tuples has (N-K) (null)
> entries and K entries with the same subject.  At that point, those K
> tuples are validity-, authorization- and delegation- intersected to
> yield the single tuple that will replace the list of tuples.


#### Section 6.3.4. Certificate Path Discovery

**N-093.** (§6.3.4) _[lowercase/implied]_

> All reduction operations are in the order provided by the prover.
> That simplifies the job of the verifier, but leaves the job of
> finding the correct list of reductions to the prover.

**N-094.** (§6.3.4) _[lowercase/implied]_

> The general algorithm for finding the right certificate paths from a
> large set of unordered certificates has been solved[ELIEN], but might
> be used only rarely.  Each keyholder who is granted some authority
> should receive a sequence of certificates delegating that authority.
> That keyholder may then want to delegate part of this authority on to
> some other keyholder.  To do that, a single additional certificate is
> generated and appended to the sequence already available, yielding a
> sequence that can be used by the delegatee to prove access
> permission.


### Section 6.4. 4-tuple Reduction

**N-095.** (§6.4 (two classes)) _[lowercase/implied]_

```
   There will be name 4-tuples in two different classes, those that
   define the name as a key and those that define the name as another
   name.

    1.  [(name K1 N) -> K2]

    2.  [(name K1 N) -> (name K2 N1 N2 ... Nk)]
```

**N-096.** (§6.4 (name reduction)) _[lowercase/implied]_

```
   As with the 5-tuples discussed in the previous section, name
   definition 4-tuples should be delivered in the order needed by the
   prover.  In that case, the rule for name reduction is to replace the
   name just defined by its definition.  For example,

        (name K1 N N1 N2 N3) + [(name K1 N) -> K2]

             -> (name K2 N1 N2 N3)

   or, in case 2 above,

        (name K1 N Na Nb Nc) + [(name K1 N) -> (name K2 N1 N2 ... Nk)]

             -> (name K2 N1 N2 ... Nk Na Nb Nc)
```

**N-097.** (§6.4) _[lowercase/implied]_

> With the second form of name definition, one might have names that
> temporarily grow.  If the prover is providing certificates in order,
> then the verifier need only do as it is told.

**N-098.** (§6.4 (unordered pool)) _[lowercase/implied]_

> If the verifier is operating from an unordered pool of tuples, then a
> safe rule for name reduction is to apply only those 4-tuples that
> define a name as a key.  Such applications should bring 4-tuples that
> started out in class (2) into class (1), and eventually reduce all
> names to keys.  Any naming loops are avoided by this process.


#### Section 6.4.1. 4-tuple Threshold Subject Reduction

**N-099.** (§6.4.1) _[lowercase/implied]_

> Some of a threshold subject's subordinate subjects might be names.
> Those names must be reduced by application of 4-tuples.  The name
> reduction process proceeds independently on each name in the
> subordinate subject as indicated in 6.3.3 above.

**N-100.** (§6.4.1) _[lowercase/implied]_

> One can reduce individual named subjects in a threshold subject and
> leave the subject in threshold form, if one desires.  There is no
> delegation- or authorization-intersection involved, only a validity-
> intersection during name reduction.  This might be used by a service
> that produces Certificate Result Certificates [see 6.7].


#### Section 6.4.2. 4-tuple Validity Intersection

**N-101.** (§6.4.2) _[lowercase/implied]_

> Whenever a 4-tuple is used to reduce the subject (or part of the
> subject) of another tuple, its validity interval is intersected with
> that of the tuple holding the subject being reduced and the
> intersection is used in the resulting tuple.  Since a 4-tuple
> contains no delegation or authorization fields, the delegation
> permission and authorization of the tuple being acted upon does not
> change.


### Section 6.5. Certificate Translation

**N-102.** (§6.5) _[lowercase/implied]_

> Any certificate currently defined, as well as ACL entries and
> possibly other instruments, can be translated to 5-tuples (or name
> tuples) and therefore take part in an authorization computation.  The
> specific rules for those are given below.


#### Section 6.5.1. X.509v1

**N-103.** (§6.5.1) _[lowercase/implied]_ _[page break removed]_

```
   The original X.509 certificate is a <name,key> certificate.  It
   translates directly to a name tuple.  The form

        [Kroot, (name <leaf-name>), K1, validity]

   is used if the rules for that particular X.509 hierarchy is that all
   leaf names are unique, under that root.  If uniqueness of names
   applies only to individual CAs in the X.509 hierarchy, then one must
   generate

        [Kroot, (name CA1 CA2 ... CAk <leaf-name>), K1, validity]

   after verifying the certificate chain by the rules appropriate to
   that particular chain.
```


#### Section 6.5.2. PGP

**N-104.** (§6.5.2) _[lowercase/implied]_

```
   A PGP certificate is a <name,key> certificate.  It is verified by
   web-of-trust rules (as specified in the PGP documentation).  Once
   verified, it yields name tuples of the form

        [Ki, name, K1, validity]

   where Ki is a key that signed that PGP (UserID,key) pair.  There
   would be one tuple produced for each signature on the key, K1.
```


#### Section 6.5.3. X.509v3

**N-105.** (§6.5.3) _[lowercase/implied]_

> An X.509v3 certificate may be used to declare a name.  It might also
> declare explicit authorizations, by way of extensions.  It might also
> declare an implicit authorization of the form (tag (*)).  The actual
> set of tuples it yields depends on the documentation associated with
> that line of certificates.  That documentation could conceptually be
> considered associated with the root key of the certificate chain.  In
> addition, some X.509v3 certificates (such as those used for SET),
> have defined extra validity tests for certificate chains depending on
> custom extensions.  As a result, it is likely that X.509v3 chains
> will have to be validated independently, by chain validation code
> specific to each root key.  After that validation, that root-specific
> code can then generate the appropriate multiple tuples from the one
> certificate.


#### Section 6.5.4. X9.57

**N-106.** (§6.5.4) _[lowercase/implied]_

> An X9.57 attribute certificate should yield one or more 5-tuples,
> with names as Subject.  The code translating the attribute
> certificate will have to build a fully-qualified name to represent
> the Distinguished Name in the Subject.  For any attribute
> certificates that refer to an ID certificate explicitly, the Subject
> of the 5-tuple can be the key in that ID certificate, bypassing the
> construction of name 4-tuples.


#### Section 6.5.5. SDSI 1.0

**N-107.** (§6.5.5) _[lowercase/implied]_

> A SDSI 1.0 certificate maps directly to one 4-tuple.


#### Section 6.5.6. SPKI

**N-108.** (§6.5.6) _[lowercase/implied]_

> An SPKI certificate maps directly to one 4- or 5- tuple, depending
> respectively on whether it is a name certificate or carries an
> authorization.


#### Section 6.5.7. SSL

**N-109.** (§6.5.7 (ssl and dns tags)) _[lowercase/implied]_

```
   An SSL certificate carries a number of authorizations, some
   implicitly.  The authorization:

        (tag (ssl))

   is implicit.  In addition, the server certificate carries a DNS name
   parameter to be matched against the DNS name of the web page to which
   the connection is being made.  That might be encoded as:

        (tag (dns <domain-name>))
```

**N-110.** (§6.5.7 (global cert)) _[lowercase/implied]_

```
   Meanwhile, there is the "global cert" permission -- the permission
   for a US-supplied browser to connect using full strength symmetric
   cryptography even though the server is outside the USA.  This might
   be encoded as:

        (tag (us-crypto))
```

**N-111.** (§6.5.7) _[lowercase/implied]_

> There are other key usage attributes that would also be encoded as
> tag fields, but a full discussion of those fields is left to the
> examples document.

**N-112.** (§6.5.7 (SSL root key ACL entry)) _[lowercase/implied]_

```
   An ACL entry for an SSL root key would have the tag:

        (tag (* set (ssl) (dns (*))))

   which by the rules of intersection is equivalent to:

        (tag (* set (ssl) (dns)))

   unless that root key also had the permission from the US Commerce
   Department to grant us-crypto permission, in which case the root key
   would have:

        (tag (* set (ssl) (dns) (us-crypto)))
```

**N-113.** (§6.5.7 (CA certificate)) _[lowercase/implied]_

```
   A CA certificate, used for SSL, would then need only to communicate
   down its certificate chain those permissions allocated in the ACL.
   Its tag might then translate to:

        (tag (*))
```

**N-114.** (§6.5.7 (leaf server certificate)) _[lowercase/implied]_

```
   A leaf server certificate for the Datafellows server might, for
   example, have a tag field of the form:

        (tag (* set (ssl) (dns www.datafellows.com)))

   showing that it was empowered to do SSL and to operate from the given
   domain name, but not to use US crypto with a US browser.
```

**N-115.** (§6.5.7 (abbreviation)) _[lowercase/implied]_

```
   The use of (* set) for the two attributes in this example could have
   been abbreviated as:

        (tag (ssl www.datafellows.com))

   while CA certificates might carry:

        (tag (ssl (*))) or just (tag (*))

   but separating them, via (* set), allows for a future enhancement of
   SSL in which the (ssl) permission is derived from one set of root
   keys (those of current CAs) while the (dns) permission is derived
   from another set of root keys (those empowered to speak in DNSSEC)
   while the (us-crypto) permission might be granted only to a root key
   belonging to the US Department of Commerce.  The three separate tests
   in the verifying code (e.g., the browser) would then involve separate
   5-tuple reductions from separate root key ACL entries.
```

**N-116.** (§6.5.7) _[lowercase/implied]_

> The fact that these three kinds of permission are treated as if ANDed
> is derived from the logic of the code that interprets the permissions
> and is not expressed in the certificate.  That decision is embodied
> in the authorization code executed by the verifying application.


### Section 6.6. Certificate Result Certificates

**N-117.** (§6.6 (two questions)) _[lowercase/implied]_

```
   Typically, one will reduce a chain of certificates to answer an
   authorization question in one of two forms:

    1.  Is this Subject, S, allowed to do A, under this ACL and with
        this set of certificates?

    2.  What is Subject S allowed to do, under this ACL and with this
        set of certificates?
```

**N-118.** (§6.6) _[lowercase/implied]_

> The answer to the second computation can be put into a new
> certificate issued by the entity doing the computation.  That one
> certificate corresponds to the semantics of the underlying
> certificates and online test results.  We call it a Certificate
> Result Certificate.


## Section 7. Key Management

**N-119.** (§7) _[lowercase/implied]_

> Cryptographic keys have limited lifetimes.  Keys can be stolen.  Keys
> might also be discovered through cryptanalysis.  If the theft is
> noticed, then the key can be replaced as one would replace a credit
> card.  More likely, the theft will not be noticed.  To cover this
> case, keys are replaced routinely.

**N-120.** (§7) _[lowercase/implied]_

> The replacement of a key needs to be announced to those who would use
> the new key.  It also needs to be accomplished smoothly, with a
> minimum of hassle.

**N-121.** (§7) _[lowercase/implied]_

> Rather than define a mechanism for declaring a key to be bad or
> replaced, SPKI defines a mechanism for giving certificates limited
> lifetimes so that they can be replaced.  That is, under SPKI one does
> not declare a key to be bad but rather stops empowering it and
> instead empowers some other key.  This limitation of a certificate's
> lifetime might be by limited lifetime at time of issuance or might be
> via the lifetime acquired through an on-line test (CRL, revalidation
> or one-time).  Therefore, all key lifetime control becomes
> certificate lifetime control.


### Section 7.1. Through Inescapable Names

_No entries — a hypothetical (key management through inescapable names) that
the section itself rules out._


### Section 7.2. Through a Naming Authority

_No entries — a hypothetical (a single global naming authority) that the
section itself rejects. Its chain of "would have to" is part of the
hypothetical._


### Section 7.3. Through <name,key> Certificates

**N-122.** (§7.3) _[lowercase/implied]_

> Instead of inescapable names or single-root naming authorities, we
> have names assigned by some entity that issues a <name,key>
> certificate.  As noted in sections 2.8 and 2.9, above, such names
> have no meaning by themselves.  They must be fully qualified to have
> meaning.

**N-123.** (§7.3) _[lowercase/implied]_

```
   Therefore, in the construct:

        (name (hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|) jim)

   the name is not

        "jim"

   but rather

        "(name (hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|) jim)"
```

**N-124.** (§7.3) _[lowercase/implied]_

> This name includes a public key (through its hash, in the example
> above).  That key has a lifetime like any other key, so this name has
> not achieved the kind of permanence (free from key lifetimes) that an
> inescapable name has.  However, it appears to be our only
> alternative.

**N-125.** (§7.3) _[lowercase/implied]_

> This name could easily be issued by the named keyholder, for the
> purpose of key management only.  In that case, there is no concern
> about access control being subverted by some third-party naming
> authority.


### Section 7.4. Increasing Key Lifetimes

**N-126.** (§7.4) _[lowercase/implied]_

> By the logic above, any name will hang off some public key.  The job
> is then to increase the lifetime of that public key.  Once a key
> lifetime exceeds the expected lifetime of any authorization granted
> through it, then a succession of new, long-lifetime keys can cover a
> keyholder forever.

**N-127.** (§7.4) _[lowercase/implied]_

> For a key to have a long lifetime, it needs to be strong against
> cryptanalytic attack and against theft.  It should be used only on a
> trusted machine, running trusted software.  It should not be used on
> an on-line machine.  It should be used very rarely, so that the
> attacker has few opportunities to find the key in the clear where it
> can be stolen.


### Section 7.5. One Root Per Individual

**N-128.** (§7.5) _[lowercase/implied]_

> In the limit, one can have one highly protected naming root key for
> each individual.  One might have more than one such key per
> individual, in order to frustrate attempts to build dossiers, but let
> us assume only one key for the immediate discussion.

**N-129.** (§7.5) _[lowercase/implied]_

> If there is only one name descending from such a key, then one can
> dispense with the name.  Authorizations can be assigned to the key
> itself, in raw SPKI style, rather than to some name defined under
> that key.  There is no loss of lifetime -- only a change in the
> subject of the certificate the authorizing key uses to delegate
> authority.

**N-130.** (§7.5) _[lowercase/implied]_

```
   However, there is one significant difference, under the SPKI
   structure.  If one delegates some authorization to

        (name (hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|) carl)

   and a different authorization to

        (hash sha1 |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|)

   directly, both without granting the permission to delegate, that key
   can delegate at will through <name,key> certificates in the former
   case and not delegate at all in the latter case.
```

**N-131.** (§7.5) _[lowercase/implied]_

> In the case of key management, we desire the ability to delegate from
> a long lived, rarely used key to a shorter lived, often used key --
> so in this case, the former mechanism (through a SDSI name) gives
> more freedom.


### Section 7.6. Key Revocation Service

**N-132.** (§7.6) _[lowercase/implied]_

> In either of the models above, key |TLCgPLFlGTzgUbcaYLW8kGTEnUk=|
> will issue a certificate.  In the first model, it will be a
> <name,key> certificate.  In the second, it will be an authorization
> certificate delegating all rights through to the more temporary key.

**N-133.** (§7.6) _[lowercase/implied]_

> Either of those certificates might want an on-line validity test.
> Whether this test is in the form of a CRL, a re-validation or a one-
> time test, it will be supplied by some entity that is on-line.

**N-134.** (§7.6) _[lowercase/implied]_

> As the world moves to having all machines on-line all the time, this
> might be the user's machine.  However, until then -- and maybe even
> after then -- the user might want to hire some service to perform
> this function.  That service could run a 24x7 manned desk, to receive
> phone calls reporting loss of a key.  That authority would not have
> the power to generate a new key for the user, only to revoke a
> current one.

**N-135.** (§7.6) _[lowercase/implied]_

> If, in the worst case, a user loses his master key, then the same
> process that occurs today with lost wallets would apply.  All issuers
> of authorizations through that master key would need to issue new
> authorizations through the new master key and, if the old master key
> had been stolen, cancel all old authorizations through that key.


### Section 7.7. Threshold ACL Subjects

**N-136.** (§7.7) _[lowercase/implied]_

> One can take extraordinary measures to protect root keys and thus
> increase the lifetimes of those keys.  The study of computer fault-
> tolerance teaches us that truly long lifetimes can be achieved only
> by redundancy and replacement.  Both can be achieved by the use of
> threshold subjects [section 6.3.3], especially in ACL entries.

**N-137.** (§7.7) _[lowercase/implied]_

> If we use a threshold subject in place of a single key subject, in an
> ACL (or a certificate), then we achieve redundancy immediately.  This
> can be redundancy not only of keys but also of algorithms.  That is,
> the keys in a threshold subject do not need to have the same
> algorithm.

**N-138.** (§7.7) _[lowercase/implied]_

> Truly long lifetimes come from replacement, not just redundancy.  As
> soon as a component fails (or a key is assumed compromised), it must
> be replaced.

**N-139.** (§7.7 (acl-edit)) _[lowercase/implied]_

```
   An ACL needs to be access-controlled itself.  Assume that the ACL
   includes an entry with authorization

       (tag (acl-edit))
```

**N-140.** (§7.7 (threshold root)) _[lowercase/implied]_

```
   Assume also that what might have been a single root authorization
   key, K1, is actually a threshold subject

       (k-of-n #03# #07# K1 K2 K3 K4 K5 K6 K7)

   used in any ACL entry granting a normal authorization.
```

**N-141.** (§7.7 (acl-edit subject)) _[lowercase/implied]_

```
   That same ACL could have the subject of an (acl-edit) entry be

       (k-of-n #05# #07# K1 K2 K3 K4 K5 K6 K7)
```

**N-142.** (§7.7) _[lowercase/implied]_

> This use of threshold subject would allow the set of root keys to
> elect new members to that set and retire old members.  In this
> manner, replacement is achieved alongside redundancy and the proper
> choice of K and N should allow threshold subject key lifetimes
> approaching infinity.


## Section 8. Security Considerations

**N-143.** (§8) _[lowercase/implied]_

```
   There are three classes of information that can be bound together by
   public key certificates: key, name and authorization.  There are
   therefore three general kinds of certificate, depending on what pair
   of items the certificate ties together.  If one considers the
   direction of mapping between items, there are six classes: name->key,
   key->name, authorization->name, name->authorization, authorization-
   >key, key->authorization.
```

**N-144.** (§8) _[lowercase/implied]_

```
   The SPKI working group concluded that the most important use for
   certificates was access control.  Given the various kinds of mapping
   possible, there are at least two ways to implement access control.
   One can use a straight authorization certificate:

       (authorization->key)

   or one can use an attribute certificate and an ID certificate:

       (authorization->name) + (name->key)
```

**N-145.** (§8 (two ways)) _[lowercase/implied]_ _[page break removed]_

```
   There are at least two ways in which the former is more secure than
   the latter.

    1.  Each certificate has an issuer.  If that issuer is subverted,
        then the attacker can gain access.  In the former case, there is
        only one issuer to trust.  In the latter case, there are two.

    2.  In the second case, linkage between the certificates is by name.
        If the name space of the issuer of the ID certificate is
        different from the name space of the issuer of the attribute
        certificate, then one of the two issuers must use a foreign name
        space.  The process of choosing the appropriate name from a
        foreign name space is more complex than string matching and
        might even involve a human guess.  It is subject to mistakes.
        Such a mistake can be made by accident or be guided by an
        attacker.
```

**N-146.** (§8) _[lowercase/implied]_

> This is not to say that one must never use the second construct.  If
> the two certificates come from the same issuer, and therefore with
> the same name space, then both of the security differentiators above
> are canceled.
