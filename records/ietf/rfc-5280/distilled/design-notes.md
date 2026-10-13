---
record: rfc-5280
kind: design-notes
title: "rfc-5280 — bearing on our design"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 5280 — bearing on our design

RFC 5280 is the document this architecture is defined against. ARCH-0001
describes itself as a *"Canonical working architecture for a native model that
is not X.509, with defined interchange to other formats"* (front matter), records
`native_format_excludes: [X.509, PKIX]`, and makes the exclusion its first model
requirement. Where the rfc-2693 notes audit an inheritance, this file surveys a
boundary. It asks exactly where R-M-01's line runs, what crosses it on import
(R-I-05), and which X.509 mechanisms are prior art for ours even though the
format is excluded. It also tests the `delegation-models` topic answer against
the full text. That answer's central claim is that X.509 scopes *naming*
authority while SPKI scopes *speaking* authority.

**Four things to hold while reading.**

1. **The source binds heavily, but not us.** `requirements.yaml` counts 532 BCP
   14 keywords in the source and holds 623 entries. Their conformance targets
   are CAs, CRL issuers and certificate-using systems, and R-M-01 says we are
   not one. A 5280 MUST cited here is a precedent with deployment behind it, not
   an obligation we inherit.
2. **Our decisions are quoted from their primary sources, which this pass
   read.** The rfc-2693 notes could not read ARCH-0001. This file did. The
   sources are:
   - ARCH-0001 v0.1.1 (updated 2026-09-21) and its CHANGELOG;
   - ADR-0001;
   - ARCH-0002 v0.5.0, in which P1 is accepted, P2, P3, P5 and P6 are
     provisionally accepted by D-2, and P4 and P7 are held;
   - DECISIONS-0001;
   - the 2026-09-28 minute (`project/meetings/2026-09-28.md`), which records
     D-1 to D-7;
   - the v0.2.0 proposal, used for the text of R-M-12 (accepted by ADR-0001),
     R-O-05 and R-O-06, and for two remarks it makes on R-M-01 and WP5. R-O-05
     and R-O-06 are proposed, not accepted: DECISIONS-0001 item 4 says *"the
     new requirements have no force"*.

   Two locations are easy to mistake. `docs/requirements.md`
   defines what an *extracted* requirement is and holds no R-M, R-I or R-O row
   (*"A thing we decided is an `R-*` in ARCH-0001, not an extracted
   requirement."*). D-n are in the minute, not in DECISIONS-0001. Priorities
   are ARCH-0001's: R-M-01, R-M-03, R-M-04, R-I-01 and R-I-02 are **M**ust, and
   R-M-09, R-M-10, R-I-05 and R-O-02 are **S**hould.
3. **Ids.**
   - `rfc-5280#R-NNNN` is written R-NNNN, and N-NNN is an entry of
     `normative.md`.
   - A quotation with neither is descriptive text, and carries its section
     and source line.
   - RFC 2693 ids are always written in full (`rfc-2693#R-NNNN`), because the
     two R-NNNN series collide.
   - "The 2693 notes" means `records/ietf/rfc-2693/distilled/design-notes.md`.

   RFC 5280 is read as published (May 2008). Where a later update is known to
   change a point, it is named as a held record and marked *outside the
   source*. None was read.
4. **Nothing here decides R-M-10, DEC-002, DEC-004 or WP5.** Adopt, adapt and
   reject are this file's reading of the evidence. A DEC is accepted only in an
   ADR (ARCH-0001 §9, R-D-02).

---

## 1. Where R-M-01 draws the line

**The requirement, verified.** The record's usefulness note says *"R-M-01 names
this document as what the native encoding SHALL NOT be"*. R-M-01 is not in
`docs/requirements.md`. It is ARCH-0001 §5.1, priority M:

> R-M-01 · M · Native encoding SHALL NOT be X.509 / PKIX.

It names a family, not RFC 5280. Identifying the family with this document is
safe, but the identification is ours. The source calls itself *"one part of a
family of standards for the X.509 Public Key Infrastructure (PKI) for the
Internet"* (§1, line 196). It describes *"the architectural model assumed by the
Public-Key Infrastructure using X.509 (PKIX) specifications"* (§3, N-006).
RFC 5280 is the base profile of what R-M-01 names. The other members of the
family that the library holds are stubs: OCSP (`rfc-6960`), trust anchors
(`rfc-5914`, `rfc-5937`) and the updates. The usefulness note is accurate if "names this document" is
read as "names the family whose base profile this is".

**What the words exclude, and what ARCH-0001 excludes.** R-M-01's text excludes
an *encoding*. ARCH-0001 as a whole excludes more:

| Layer | ARCH-0001 text | RFC 5280 counterpart |
|---|---|---|
| encoding | R-M-01; front matter `native_format_excludes`; §3.2 *"not a reason to native-encode PKIX"* | §4.1 `Certificate` and §5.1 `CertificateList`, each signed over its DER encoding (N-029, N-241) |
| information model | §1 *"X.509 / PKIX is an **interchange target**, not the information model."* | DN-named issuer and subject (R-0023, §4.1.2.6); the CA-asserted binding (N-030) |
| reducer | §6 *"**Forbidden native mapping:** X.509 certificate path validation as the native reducer."*; the matrix note *"Do not treat CA bit as AuthzCert"* | §6.1 path validation; §4.2.1.9 `cA` |
| trust and threshold | R-I-02 *"Import SHALL NOT require the foreign object to become a native trust anchor."*; R-M-06 *"Threshold principals SHALL be representable without encoding them as a CA hierarchy."* | §6.1.1(d) trust anchor input; the §3.2 hierarchies |

Import is not excluded:

- The matrix row maps an *"X.509 EE / CA cert"* to *"Key + NameCert (DN as
  labels under a `x509:` namespace of the *importer*, not of the CA) +
  provenance"*.
- R-I-05 reads *"Import X.509 only as a foreign identity assertion about a key
  (name or attribute), marked `provenance: x509`."*
- WP5 is *"Mapping spec: X.509 → annotated NameCert (import only)"*.

§1's *"interchange target"* is therefore import-only in v0.1, because the
matrix's export column for X.509 is "—", meaning *"out of scope this version"*.
The v0.2.0 proposal (§11, not accepted) adds that WP5 is one the *"execution plan
places out of scope for the semester"*.

**Why.** ARCH-0001 states no rationale for R-M-01. The nearest statements are:

- G1, *"Key-centric principals; names are not globally unique identifiers."*;
- the §3.1 row for X.509, with its cells *"DN + key"*, *"Intended global
  (X.500); local in practice"* and *"Hierarchical CA, optional bridge / mesh"*;
- ARCH-0002 P1, *"the same move R-M-01 already makes for X.509"*;
- the proposal's gloss, which is not accepted: R-M-12 *"is the natural
  completion of R-M-01: that requirement rejects a central *identity*
  authority, and this one rejects a central *vocabulary* authority."*

Read against those, the source supplies six concrete conflicts. Each one sets a
source fact against one of our texts, and together they are what would come in
with the encoding if R-M-01 were dropped (derived):

1. **The issuer is a name, and chaining is by name.** *"The issuer field MUST
   contain a non-empty distinguished name (DN)."* (R-0023). *"Name chaining is
   performed by matching the issuer distinguished name in one certificate with
   the subject name in a CA certificate."* (§4.1.2.4, N-048). Path processing
   checks that *"The certificate issuer name is the working_issuer_name."*
   (§6.1.3(a)(4), R-0421). Against R-O-01, *"Every signed object SHALL have an
   issuer key that can be specified as `KeyId`."*, and R-M-02.
2. **The key identifier is a hint, not an identity.** *"Applications are not
   required to verify that key identifiers match when performing certification
   path validation."* (§4.2.1.2, N-081). Of generation methods the source says
   *"Other methods of generating unique numbers are also acceptable."* (N-084).
   Nobody can recompute a subject key identifier from the key, so it is not
   ARCH-0001's `KeyId`, a *"Digest of a canonical key encoding"*.
3. **Names are global, and they collide.** *"While X.509 mandates that names be
   unambiguous, there is a risk that two unrelated authorities will issue
   certificates and/or CRLs under the same issuer name."* (§8, N-475). Against
   G1 and R-M-03.
4. **Revocation authority attaches to names, not keys.** *"(Note that since CAs
   and CRL issuers are identified by name, the scope of a CRL is not affected by
   the key used to sign the CRL or the key(s) used to sign certificates.)"* (§5,
   N-230).
5. **Every extension point is a registry identifier.** *"Extensions in
   certificates and CRLs are identified using object identifiers. The objects
   are defined in an arc delegated by IANA to the PKIX Working Group."* (§9,
   N-483). Key purposes *"MUST be assigned in accordance with IANA or ITU-T
   Recommendation X.660"* (R-0194). An OID arc is delegated, not key-relative.
   The identifier is global, and its meaning is fixed by whoever holds the arc,
   under a root no key controls. R-M-12 requires the reverse: *"The native
   model SHALL NOT depend on a centrally allocated registry for their
   meaning."*
6. **What validation proves is a name-to-key binding.** *"Certification path
   processing verifies the binding between the subject distinguished name
   and/or subject alternative name and subject public key."* (§6, N-320). The
   output is a key and a policy tree (§6.1.6, R-0489). That is ARCH-0001 §4.3's
   procedure 1, *"Name resolution"*, not procedure 2, *"Authorization
   reduction"*. This is the precise reason path validation is forbidden as the
   native reducer: it reduces the wrong relation.

A seventh conflict is with a provisionally accepted principle, not a
requirement. *"A non-critical extension MAY be ignored if it is not recognized"*
(R-0072) and Appendix B's *"those unknown elements ought to be ignored"*
(R-0619) set the default that ARCH-0002 P5 inverts: *"an unknown field in a
signed payload is an error, not something to skip"*.

So R-M-01 is narrower in its words than in its reach. Its text says encoding.
ARCH-0001 excludes the information model and the reducer as well, and items 1
to 6 are what that information model would bring with it.

---

## 2. Delegation control: a boolean and an integer (R-M-10)

**What RFC 5280 has.** Three fields on a CA certificate gate the subject key's
power to certify, and bound it.

- **`cA`**, `BOOLEAN DEFAULT FALSE` in basicConstraints. *"The cA boolean
  indicates whether the certified public key may be used to verify certificate
  signatures."* (§4.2.1.9, N-144).
  - In a v3 certificate, absence fails closed: *"If the basic constraints
    extension is not present in a version 3 certificate, or the extension is
    present but the cA boolean is not asserted, then the certified public key
    MUST NOT be used to verify certificate signatures."* (R-0155).
  - Every intermediate is checked: *"If certificate i is a version 3
    certificate, verify that the basicConstraints extension is present and that
    cA is set to TRUE."* (§6.1.4(k), R-0461).
  - A v1 or v2 intermediate needs *"out-of-band means"*, or rejection
    (R-0462).
- **`keyCertSign`**, bit 5 of keyUsage. It is tied to `cA` in both directions
  (R-0099, R-0154). It is checked only when keyUsage is present: *"If a key usage
  extension is present, verify that the keyCertSign bit is set."* (§6.1.4(n),
  R-0465).
- **`pathLenConstraint`**, `INTEGER (0..MAX) OPTIONAL`. All three of the
  following are §4.2.1.9, N-145:
  - *"it gives the maximum number of non-self-issued intermediate certificates
    that may follow this certificate in a valid certification path."*
  - *"A pathLenConstraint of zero indicates that no non-self-issued
    intermediate CA certificates may follow in a valid certification path."*
  - *"Where pathLenConstraint does not appear, no limit is imposed."*

  The state variable that carries it *"is initialized to n, is decremented for
  each non-self-issued certificate in the path, and may be reduced to the value
  in the path length constraint field"* (§6.1.2(k), R-0414; §6.1.4(l)–(m),
  R-0463, R-0464).

**What having both means for R-M-10.** R-M-10 reads *"Delegation SHALL be an
explicit boolean (or equivalent) on `AuthzCert`."*, at priority S. There are
five findings.

1. **The boolean is primary, and the integer is subordinate to it.** *"The
   pathLenConstraint field is meaningful only if the cA boolean is asserted and
   the key usage extension, if present, asserts the keyCertSign bit"* (N-145).
   *"CAs MUST NOT include the pathLenConstraint field unless the cA boolean is
   asserted and the key usage extension asserts the keyCertSign bit."*
   (R-0161). X.509 is not "integer control" in RFC 2693's sense. RFC 2693 §4.1
   framed the choice as *"three camps in discussing depth of delegation: no
   control, boolean control and integer control"*. X.509 is an arrangement the
   camps did not separate: a boolean gate, with an optional integer bound that
   applies only under TRUE.
2. **Without the integer, X.509 means what SPKI means.** *"Where
   pathLenConstraint does not appear, no limit is imposed."* (N-145). A CA
   certificate with no pathLenConstraint acts as an SPKI tuple with D = TRUE. Its
   subject may certify, and may give its own subordinates the same power. The
   deployed default of the "finer mechanism" is the coarse one.
3. **The integer adds exactly one capability: an issuer can bind its delegate's
   delegates.** With a boolean only, an issuer that sets D = TRUE cannot stop its
   subject issuing D = TRUE in turn. pathLenConstraint 0 lets the subject certify
   while forbidding anything it certifies from acting as an intermediate. That is
   a two-hop rule the boolean cannot state (derived from N-145 and §6.1.4(l)–(m)).
   RFC 2693's width argument holds in X.509 as well: *"there is no control on the
   width of the delegation tree, so control on its depth is not a tight control
   on proliferation"* (rfc-2693#R-0064). No bound on how many certificates a CA
   may issue appears anywhere in 5280. But the width argument is about
   proliferation, and the two-hop capability is not a proliferation control.
4. **X.509 answers RFC 2693's other objection, with a mechanism we cannot
   copy.** RFC 2693 §4.1.4 rejected integers because *"One can always need to go
   one more level down, by creating a temporary signing key (e.g., for use in a
   laptop)."* X.509 provides exactly that escape. The count covers only
   *non-self-issued* certificates (N-145, R-0463), and *"These self-issued
   certificates are not counted when evaluating path length or name
   constraints."* (§6.1, R-0384). But *"A certificate is self-issued if the same
   DN appears in the subject and issuer fields"* (R-0383), so the escape rests
   on name equality. Under R-M-02 a new key is a new principal, with no name to
   share, so the exemption has no basis in our model unless a rollover statement
   supplies one (open question 4).
5. **"Explicit" does not come automatically, and X.509 shows the cost.** DER
   omits default values: *"a BasicConstraints extension whose cA value is FALSE
   would omit the cA boolean from the encoded certificate."* (Appendix B,
   N-507). So X.509's delegation boolean is explicit only when it is TRUE. The
   three controls also read silence in three directions:
   - absent basicConstraints means *not a CA* (R-0155);
   - absent keyUsage means *no keyCertSign check* (R-0465);
   - absent pathLenConstraint means *no limit* (N-145).

   That is one delegation decision with three ways to read silence. D-3's
   reduced CBOR has no DEFAULT mechanism, so a profile can require `delegate` on
   every AuthzCert. That is the 2693 notes' proposal in their open question 13,
   and X.509 is the argument for it.

**Where `cA` sits in our model.** `cA` decides whether *"the certified public key
may be used to verify certificate signatures"*, so it delegates the power to
certify name-to-key bindings. In ARCH-0001 that power is naming (R-M-03,
`NameCert`), not authorization (`AuthzCert`). That is why the matrix says *"Do
not treat CA bit as AuthzCert"*, and why an imported pathLenConstraint has
nothing to map onto under R-M-10 as written (derived).

**What 5280 adds to the `contradicts` edge.** `rfc-9580` carries
`contradicts: rfc-2693` on delegation depth, and the 2693 notes side with
RFC 2693 (their reject item 2 and open question 9). This file does not settle
it. RFC 5280 adds four facts to the evidence:

- **A second deployed integer control, in an independent family.** The first
  is OpenPGP's trust-signature level, per the `delegation-models` answer.
- **Here the integer refines a mandatory boolean**, and defaults to the
  boolean's semantics. So this evidence supports "boolean plus an optional
  bound", not "integer instead of boolean".
- **The counting rule depends on names**, through the self-issued exemption. A
  key-centric design cannot inherit it unchanged.
- **No rationale for the integer, and no deployment data.** 5280 shows that
  the mechanism can be specified and implemented, not that it works.

So there are two readings of R-M-10, and an ADR has to choose between them.

- **Strict.** Delegation *is* a boolean, an integer is excluded, and an
  imported pathLenConstraint is dropped. This is consistent with the matrix.
- **Permissive.** *"(or equivalent)"* admits a bound beneath the boolean.
  X.509 is then the precedent, and it supplies a counting rule.

Under both readings, explicit presence is the part that X.509's DER shows does
not come free.

---

## 3. Name constraints as scoped delegation (R-M-04, DEC-004)

**What is constrained.** *"The name constraints extension, which MUST be used
only in a CA certificate, indicates a name space within which all subject names
in subsequent certificates in a certification path MUST be located."* (R-0162).
*"Restrictions apply to the subject distinguished name and apply to subject
alternative names."* (N-149). Issuer alternative names fall outside it: *"(That
is, issuer alternative names are not used in name chaining and name constraints
are not enforced.)"* (§4.2.1.7, N-138). Nothing in §4.2.1.10 or §6.1.4(g)
reaches keyUsage, extendedKeyUsage or certificate policies.

**Name constraints apply to subject names, never to authorizations.** That
confirms the `delegation-models` answer's discriminator. X.509 scopes which
names a CA may certify, not what a key may say.

**Monotone narrowing.** Each CA certificate can only narrow:

> (1) If permittedSubtrees is present in the certificate, set the
> permitted_subtrees state variable to the intersection of its previous value
> and the value indicated in the extension field. [...]
>
> (2) If excludedSubtrees is present in the certificate, set the
> excluded_subtrees state variable to the union of its previous value and the
> value indicated in the extension field. [...]

(§6.1.4(g), R-0451 and R-0452; elisions ours.)

- **Exclusion wins.** *"Any name matching a restriction in the
  excludedSubtrees field is invalid regardless of information appearing in the
  permittedSubtrees."* (N-151).
- **Each certificate is checked by containment.** Its names must be
  *"within one of the permitted_subtrees"* and *"not within any of the
  excluded_subtrees"* (§6.1.3(b)–(c), R-0422, R-0423). The test is
  containment, not non-empty overlap. That is the rule the 2693 notes propose
  for SPKI requests (their adapt 1, *"`AIntersect(A, R) = R`"*), and X.509 is a
  deployed instance of it.
- **An empty intersection fails closed, but only for names of that form.**
  The source's example is *"the intersection of example.com and example.net is
  the empty set"* (R-0451). The state variable defines the subtrees *"within
  which all subject names in subsequent certificates in the certification path
  MUST fall"* (§6.1.2(b), R-0404), and for the input sets *"If the set for a
  name type is empty, then the certification path will be considered invalid
  if any certificate in the certification path includes a name of that name
  type."* (§6.1.1(h), R-0395). The conclusion is derived from those three.

**Per name form, and open wherever unmentioned.** *"Restrictions apply only when
the specified name form is present. If no name of the type is in the
certificate, the certificate is acceptable."* (N-149). *"If permittedSubtrees
does not include a particular name type, the permitted_subtrees state variable
is unchanged for that name type."* (R-0451). §8 states the consequence: *"In
general, using the nameConstraints extension to constrain one name form (e.g.,
DNS names) offers no protection against use of other name forms (e.g.,
electronic mail addresses)."* (N-474). Each form has its own matching rule:

| form | rule | source |
|---|---|---|
| dNSName | *"Any DNS name that can be constructed by simply adding zero or more labels to the left-hand side of the name satisfies the name constraint."*, so the constraint's own name is inside it | N-156; matched label by label, case-insensitively (R-0558) |
| URI | *"For URIs, the constraint applies to the host part of the name."*, and *"the constraint ".example.com" is not satisfied by "example.com""*, so a leading period excludes the host itself | N-154 |
| rfc822Name | *"MAY specify a particular mailbox, all addresses at a particular host, or all mailboxes in a domain"*; and *"".example.com" indicates all the Internet mail addresses in the domain "example.com", but not Internet mail addresses on the host "example.com""* | R-0176, N-155; applied to `emailAddress` in the DN when there is no subjectAltName (R-0177) |
| iPAddress | *"eight (8) octets, encoded in the style of RFC 4632 (CIDR) to represent an address range"*, or 32 octets for IPv6 | R-0185, R-0186 |
| directoryName | DN1 is within DN2 *"if DN1 contains at least as many RDNs as DN2, and DN1 and DN2 are a match when trailing RDNs in DN1 are ignored"* | R-0550 |
| otherName, ediPartyName, registeredID | *"The syntax and semantics for name constraints for otherName, ediPartyName, and registeredID are not defined by this specification"* | N-162 |

Support is uneven by design.

- Applications *"MUST be able to process"* directoryName constraints (R-0167).
- For rfc822Name, URI, dNSName and iPAddress they only *"SHOULD be able to
  process"* them (R-0168).
- The fallback is that *"the application MUST either process the constraint
  or reject the certificate"* (R-0169).

So for the forms that matter on the Internet, two conforming verifiers can
answer differently: one evaluates the constraint and one rejects the
certificate. Both answers are safe, but they are not the same answer (derived).

**The self-issued exemption.** *"Name constraints are not applied to self-issued
certificates (unless the certificate is the final certificate in the path).
(This could prevent CAs that use name constraints from employing self-issued
certificates to implement key rollover.)"* (N-150). Steps §6.1.3(b)–(c) skip
such certificates (R-0422, R-0423). This is the same exemption as §2 item 4, for
the same reason, resting on the same thing: name equality.

**The criticality rule.** *"Conforming CAs MUST mark this extension as critical"*
(R-0163). The source gives no reason. The inferred one is that a verifier which
ignored the extension would accept names outside the scope. §4.2's rule exists
to stop exactly that: a system *"MUST reject the certificate if it encounters a
critical extension it does not recognize"* (R-0071).

5280 needs a per-extension mark because its default runs the other way
(R-0072). It also discourages critical marking for the sake of
interoperability: *"caution ought to be exercised in adopting any critical
extensions"* (N-067), and see R-0078. Under ARCH-0002 P5 every field is
must-understand, so the mark has no native counterpart. The rule's purpose
survives as P5, and the flag does not.

**Could DEC-004 option 1 be expressed with name constraints?** Option 1 is
*"SPKI tag S-expressions as-is (byte-string sets + intersection)"* (ARCH-0001
§7). Form by form (derived):

| option 1 (rfc-2693 §6.3.1) | name constraints |
|---|---|
| `(*)` | a name form left unmentioned, which is open by default |
| `(* set ...)` | several `GeneralSubtree` entries in one `permittedSubtrees` |
| `(* prefix ...)` over bytes | hierarchical subtrees, over structured names only: DNS labels from the right, RDNs from the left, address bits under a mask |
| `(* range <ordering> ...)` | none. `GeneralSubtree` has `minimum` and `maximum`, but *"thus, the minimum MUST be zero, and maximum MUST be absent."* (R-0170, R-0171, N-153). CIDR is the only range, and only of aligned blocks |
| element-by-element list matching | none; a `GeneralName` is one name |
| intersection along a chain | yes, with the same shape (R-0451) |
| exclusions | `excludedSubtrees`; option 1 has no exclusions |

Option 1 cannot be expressed this way, and what is missing is not syntax:

1. **The constrained object is a subject name**, not what a key may say. A tag
   would have to be disguised as a name form, which turns an authorization into
   a name and breaks R-M-04.
2. **The only open-ended form is typed by an OID.** For `otherName`, *"The
   format and semantics of the name are indicated through the OBJECT
   IDENTIFIER in the type-id field."* (N-133). R-M-12 excludes that, and the
   constraint semantics for `otherName` are undefined anyway (N-162).
3. **There is no request.** 5280 checks the names a certificate carries, not
   a request against a grant.
4. **There are no ranges and no lists.**

What name constraints do show is that **the core of option 1, monotone
intersection along a chain checked by containment, is specified, standardised
and implemented for names**. The record lists six implementations that enforce
it (`record.yaml` `implementations`). Whether anyone *uses* them is a separate
question. The topic answer records that claim as resting on secondary sources
only.

**Against the 2693 notes.** Both mechanisms narrow monotonically, so on that
point X.509 agrees with the 2693 notes' adopt 3. X.509 differs in three ways,
and each carries a stated cost:

- **It has exclusions, and §8 shows they fail open.** *"name constraints stated
  as excludedSubtrees will not match and invalid paths will be accepted and
  name constraints expressed as permittedSubtrees will not match and valid
  paths will be rejected"* (N-473). Hence *"CAs SHOULD state name constraints
  for distinguished names as permittedSubtrees wherever possible"* (R-0587).
- **Its matching rules differ per form**, with three different rules for names
  carried in DNS form alone. AIntersect has one generic algebra.
- **It is open by default across forms.** SPKI is open by default only past the
  end of a list (rfc-2693#R-0151). Both leave some region the grant does not
  mention, and so permits. In X.509 that region is whole name forms; in SPKI it
  is the trailing list positions.

**Against R-M-04.** R-M-04 reads *"Name bindings and authorization bindings
SHALL be distinct object kinds."* ARCH-0002 P6 (provisional, D-2) re-reads the
five kinds as *"functions over one form, distinguished by predicate type"*.
X.509 fails both readings. One certificate, under one signature, carries the
subject name, the key, `cA`, pathLenConstraint, keyUsage, nameConstraints and
the policy constraints.

The source's own §2 sees the problem coming: *"As supplemental authorization and
attribute management tools emerge, such as attribute certificates, it may be
appropriate to limit the authenticated attributes that are included in a
certificate."* (§2, line 353). That is RFC 5280's own case for R-M-04. Against
the full text, the topic answer's claim of *"the sharpest support in the
literature for R-M-04"* holds.

---

## 4. Trust anchors as local policy

**Where the source agrees with us.** The anchor is an input. It is chosen
locally, and trusted because of how it arrived:

- *"The selection of a trust anchor is a matter of policy"*, and *"The path
  validation procedure is the same regardless of the choice of trust anchor."*
  (§6, N-323).
- *"The trust anchor is an input to the algorithm."* (§6.1, N-329).
- *"The trust anchor information is trusted because it was delivered to the
  path processing procedure by some trustworthy out-of-band procedure."*
  (§6.1.1(d), R-0390).
- *"When the trust anchor is provided in the form of a self-signed certificate,
  this self-signed certificate is not included as part of the prospective
  certification path."* (§6.1, R-0381). The self-signature proves possession,
  not trust: *"(This proves that the issuer possesses both the public and
  private keys.)"* (§4.2.1.1, N-075).
- *"The selection of one or more trusted CAs is a local decision."* (§6.2,
  N-404), and *"In some environments, the local domain is the most trusted."*
  (§3.2, N-012).

This matches three of ours:

- ARCH-0001's `AclEntry`: *"unsigned; issuer = `Self`"*, *"Local policy root"*;
- ARCH-0002's *"a set of trust roots **you chose yourself**"*;
- RFC 2693's ACL (rfc-2693#R-0003).

The topic answer's claim that ARCH-0001's unsigned local trust root *"is
therefore NOT a departure"* is confirmed for X.509.

**Where it differs, and the difference is ours to specify.**

1. **The anchor is a name as well as a key.** Its information is *"the trusted
   issuer name"*, *"the trusted public key algorithm"*, *"the trusted public
   key"* and optional parameters (§6.1.1(d), R-0389). Path processing starts
   from the name: *"The working_issuer_name is initialized to the trusted issuer
   name provided in the trust anchor information."* (§6.1.2(j), R-0413). Ours is
   a key, a `KeyId`, together with a tag.
2. **The anchor's own constraints are optional and unspecified.** §6.2 says
   that *"certificate extensions can be used to specify recommended inputs to
   path validation"*, and then: *"The path validation algorithm presented in
   Section 6.1 does not assume that trust anchor information is provided in
   self-signed certificates and does not specify processing rules for additional
   information included in such certificates. Implementations that use
   self-signed certificates to specify trust anchor information are free to
   process or ignore such information."* (N-406). The inputs are optional too:
   *"Conforming implementations are not required to support the setting of all
   of these inputs."* (R-0397).

   So two conforming verifiers given the same anchor certificate can disagree,
   one honouring its name constraints and the other ignoring them. That is the
   gap behind the topic answer's *"the difference is that ours is specified"*.
   It is an R-M-05 matter, not a matter of style.
3. **Scope on an anchor is expressed as verifier input.** *"For example, a
   trusted CA may only be trusted for a particular certificate policy. This
   restriction can be expressed through the inputs to the path validation
   procedure."* (N-404). See also `initial-permitted-subtrees` (R-0395). In
   ARCH-0001 the same restriction is the tag on an `AclEntry`. The idea is the
   same; ours is a first-class object.
4. **Distribution is out of scope.** *"The authenticated distribution of trusted
   CA public keys (usually in the form of a "self-signed" certificate) is a
   security critical out-of-band process that is beyond the scope of this
   specification."* (§8, N-467). The `AclEntry` is in our scope by
   construction.

**R-I-02.** 5280 makes R-I-02 easy to honour (derived):

- an X.509 root that an importer trusts is configuration of the *import
  translator*: an input to the X.509 validation inside it, which §6.2 permits
  for any locally chosen anchor;
- the translated statement is issued by the importer, whose key a native
  `AclEntry` may empower;
- the X.509 root itself never enters the native ACL.

This is the import boundary of the 2693 notes' adapt 7, with the translator
inside the trusted computing base.

---

## 5. Revocation against R-O-02

R-O-02 reads *"Short-lived validity preferred over revocation-heavy design;
revocation still representable."*, at priority S.

**What 5280 provides.**

- **CRLs** (§3.3, §5). *"A CRL is a time-stamped list identifying revoked
  certificates that is signed by a CA or CRL issuer and made freely available
  in a public repository. Each revoked certificate is identified in a CRL by its
  certificate serial number."* (§3.3, N-016).
- **Scope.** Every CRL has one, and *"A complete CRL lists all unexpired
  certificates, within its scope, that have been revoked for one of the
  revocation reasons covered by the CRL scope."* (N-230).
- **Indirect CRLs.** *"If the scope of the CRL includes one or more
  certificates issued by an entity other than the CRL issuer, then it is an
  indirect CRL."* (N-231).
- **Delta CRLs.** *"A delta CRL only lists those certificates, within its
  scope, whose revocation status has changed since the issuance of a
  referenced complete CRL."* (N-232).
- **Entries.** An entry can carry a reason (§5.3.1), an invalidity date
  (§5.3.2) and, in an indirect CRL, the certificate's issuer (§5.3.3).
- **Status.** §6.3 computes it. *"This algorithm begins by assuming that the
  certificate is not revoked."* (R-0501), and it ends with a reason,
  UNREVOKED, or *"the cert_status UNDETERMINED"* (R-0537).

**5280's own position on revocation is not R-O-02's.**

- **Validity is defined through revocation.** *"The certificate validity period
  is the time interval during which the CA warrants that it will maintain
  information about the status of the certificate."* (§4.1.2.5, N-049). R-O-02
  separates the two, and 5280 does not.
- **Unbounded validity is a convention.** *"the notAfter SHOULD be assigned the
  GeneralizedTime value of 99991231235959Z"* (R-0036). It is balanced by
  *"the issuer MUST ensure that no valid certification path exists for the
  certificate after maintenance of status information is terminated"*
  (R-0037).
- **Revocation is optional at both ends.** For issuers, *"this profile does not
  require the issuance of CRLs"* (§3.3, N-018). For verifiers, *"Conforming
  applications are not required to support processing of delta CRLs, indirect
  CRLs, or CRLs with a scope other than all certificates issued by one CA."*
  (§5, N-234).
- **The published text has no provision for short-lived certificates.** The
  later answer is `rfc-9608`, *"No Revocation Available for X.509 Public Key
  Certificates"*, held as a stub with `updates: rfc-5280`. *Outside the
  source.*

**Determinism, against RFC 2693.** 5280 orders CRLs, but lets them overlap.

The ordering:

- the CRL number *"conveys a monotonically increasing sequence number for a
  given CRL scope and CRL issuer. This extension allows users to easily
  determine when a particular CRL supersedes another CRL."* (§5.2.3, N-266);
- *"the complete CRLs and delta CRLs MUST share one numbering sequence"*
  (R-0297), and of two CRLs issued at different times *"the two CRLs MUST NOT
  have the same CRL number"* (R-0300);
- *"Conforming CRL issuers MUST include the nextUpdate field in all CRLs."*
  (R-0280).

The overlap is permitted, not just left unaddressed:

- *"The next CRL could be issued before the indicated date, but it will not be
  issued any later than the indicated date."* (§5.1.2.5, N-252);
- for deltas, *"the CRL issuer may publish one or more delta CRLs before the
  time indicated by the nextUpdate field. If more than one current delta CRL
  for a given scope is encountered, the application SHOULD consider the one
  with the latest value in thisUpdate to be the most current one."* (N-283,
  R-0318);
- "suitably recent" is local: *"The meaning of "suitably recent" may vary with
  local policy, but it usually means the most recently issued CRL."* (§3.3,
  N-016).

So the status a verifier computes depends on which current CRL it happened to
fetch. That is the *"at least timing dependent"* outcome RFC 2693 ruled out
(rfc-2693#R-0073). 5280 bounds the damage to one `nextUpdate` period, because
§6.3.3 demands a CRL whose next update is still ahead (R-0506).

The same rules answer the 2693 notes' open question 7 in the way they suggest.
The issuer sets the maximum staleness (`nextUpdate`). The verifier may demand
fresher evidence, but may not accept staler (derived from R-0506 and N-016).

**What maps to escrowed revocation, and what does not.** The `delegation-models`
answer names RFC 9580 §13.9's escrowed revocation as *"the single most directly
reusable mechanism this lane found"*: *"Alice pre-signs her own revocation and
gives it to a holder."* RFC 9580 is not read here, and that description is the
answer's.

| 5280 element | maps? | why |
|---|---|---|
| a CRL entry: serial, `revocationDate`, `reasonCode`, `invalidityDate` | **the content maps** | One entry is a positive statement about one certificate, which is the shape of a single revocation statement. The serial is replaced by a digest of the revoked statement (derived). |
| `invalidityDate`: *"provides the date on which it is known or suspected that the private key was compromised or that the certificate otherwise became invalid."*, and *"This date may be earlier than the revocation date in the CRL entry"* (N-313) | **maps** | It is a claim a revocation statement may carry. It lets a verifier distrust signatures made before the revocation was published. |
| who signs: *"The CRL issuer is either the CA or an entity that has been authorized by the CA to issue CRLs."* (N-228), and *"Under such circumstances, the CA needs to revoke the certificate."* (N-015). The subject can only ask: a *"revocation request"* is where *"An authorized person advises a CA of an abnormal situation requiring certificate revocation"* (§3.5(f), N-019) | **does not map** | An escrowed revocation is signed in advance by the keyholder. 5280 has no subject-signed revocation. |
| the complete CRL | **does not map** | A complete CRL also asserts a negative: everything in its scope that it does not list is unrevoked (inferred from N-230). A negative cannot be signed in advance. Escrow needs only positive statements. |
| delta CRLs, CRL numbers, issuing distribution points, reason partitions | **does not map** | This machinery distributes complete lists efficiently. It has no counterpart for a single statement. |
| `certificateHold` and `removeFromCRL` | **does not map** | Hold is reversible: *"The status of a certificate is considered to have changed if it is revoked (for any revocation reason, including certificateHold), if it is released from hold, or if its revocation reason changes."* (N-279), and *"If (cert_status is removeFromCRL), then set cert_status to UNREVOKED."* (R-0534). Status can go from revoked back to unrevoked. A published escrowed revocation cannot be withdrawn, so it is monotone, and hold is not. |
| indirect CRLs (`cRLIssuer`, `indirectCRL`, `certificateIssuer`) | **the deprecated counterpart** | This is delegated revocation, the mechanism RFC 9580 deprecated (per the topic answer, *"Applications MUST NOT generate such a subpacket"*). 5280 keeps it, conditioned on the certificate naming the CRL issuer (R-0206) and on the CRL asserting `indirectCRL` (R-0509). Verifier support is optional by specification (N-234), which matches the deployment signal the topic answer reports for OpenPGP: *"uneven and unreliable"*. |

One 5280 security consideration makes the strongest case for escrow, from
inside X.509: *"Loss of a CA's private signing key may also be problematic. The
CA would not be able to produce CRLs or perform normal key rollover."* (§8,
N-465). A revocation that already exists does not need the key to survive.

**Historical validation.** *"An entry MUST NOT be removed from the CRL until it
appears on one regularly scheduled CRL issued beyond the revoked certificate's
validity period."* (R-0003). *"Note that mechanisms are not available for
validating a certificate with respect to a time outside the certificate
validity period."* (§6.1, N-328). X.509 revocation forgets a certificate once
the certificate has expired.

An `ArtifactStatement` (G5) may be checked years after it was signed. So the
question "was this statement valid when it was made" needs evidence that
outlives the signer's certificate (open question 6).

---

## 6. The policy machinery

The machinery covers:

- certificatePolicies (§4.2.1.4) and policyMappings (§4.2.1.5);
- policyConstraints, with its requireExplicitPolicy and inhibitPolicyMapping
  fields (§4.2.1.11), and inhibitAnyPolicy (§4.2.1.14);
- the `valid_policy_tree`, built and pruned in §6.1.2(a)–(f), §6.1.3(d)–(f),
  §6.1.4(a)–(b) and (h)–(j), and §6.1.5(g).

**Most of what it computes is something we already have.** *"In a CA
certificate, these policy information terms limit the set of policies for
certification paths that include this certificate."* (§4.2.1.4, N-106). Along a
path:

- the policy sets intersect;
- `anyPolicy` acts as a wildcard (R-0106);
- the counters only fall: *"Once set, this variable may be decreased, but may
  not be increased."* (R-0407 to R-0409).

That is set intersection with `(*)`, the algebra that DEC-004 option 1 and
R-M-08 already require. Here it runs as a second intersection, parallel to name
constraints, over a second identifier space. What is left over has no
counterpart in our model:

1. **Mapping.** *"The pairing indicates the issuing CA considers its
   issuerDomainPolicy equivalent to the subject CA's subjectDomainPolicy."*
   (N-118). This is cross-domain equivalence between registry identifiers,
   translated inside the reducer. Under R-M-12 identifiers are `(key, label)`
   pairs. Under ARCH-0002 P3 and P4 meaning lives in schemas and domains of
   discourse, not in the hops of a chain. The tree exists *because of*
   mapping: each node records which policy its mapped successors came from
   (§6.1.4(b)).
2. **Delayed activation.** requireExplicitPolicy, inhibitPolicyMapping and
   inhibitAnyPolicy are `SkipCerts` counts: *"the number of additional
   certificates that may appear in the path before"* the constraint applies
   (N-166, N-167, N-190). A constraint that starts k hops later is the
   integer-depth design of §2 again, applied to policy.
3. **Optional enforcement.** A path succeeds with an empty policy set unless
   something demanded a policy. The success condition is *"If either (1) the
   value of explicit_policy variable is greater than zero or (2) the
   valid_policy_tree is not NULL, then path processing has succeeded."*
   (R-0488). Our composition fails when an intersection fails
   (rfc-2693#R-0137, *"provided the two intersections succeed,"*, the 2693
   notes' adopt 3). R-M-05 has no counterpart for a scope that can empty out
   and still succeed.
4. **Optional support.** *"For example, clients are not required to support the
   policy mappings extension."* (N-326). The extension *"MAY be supported by CAs
   and/or applications"* (R-0122), and inhibitPolicyMapping support is only a
   SHOULD (R-0188). DEC-008 is open, and its proposed answer keeps the
   reduction algorithm in a fixed core (*"Key-local is wrong for the core."*).
   Core steps that are optional are a determinism hazard (R-M-05).
5. **Display text inside signed data.** Processing of the CPS pointer is *"a
   local matter"* (N-110). User notices carry explicitText that *"SHOULD be
   normalized according to Unicode normalization form C (NFC)"* (R-0116). The
   referenced, possibly multilingual form, `noticeRef` (*"Messages MAY be
   multilingual"*, R-0112), is deprecated: *"Conforming CAs SHOULD NOT use the
   noticeRef option."* (R-0111).

   ARCH-0002 P3 puts human-facing text in the type's schema, and R-O-05
   (proposed) regenerates that text from verified bytes. X.509's one
   referenced-text design was dropped, and the source does not say why. That
   is evidence about P3's design space, not evidence against P3.
6. **Cost.** 5280's own design principle is *"Providing administrators with
   unbounded choices increases the chances that a subtle CA administrator
   mistake will result in broad compromise."* (§2.4, line 409). The algorithm
   was later replaced by `rfc-9618`, *"Updates to X.509 Policy Validation"*,
   held as a stub with `updates: rfc-5280`. *Outside the source.*

**Reject, as a mechanism.** The intersection core is already DEC-004's to define,
once. Each piece of the remainder conflicts with one of the decisions named
above: mapping, delayed activation, optional enforcement, optional support and
the display qualifiers.

On import, one policy output is worth keeping. That is the `valid_policy_tree`
that §6.1.6 returns (R-0489), kept as an *attribute* of the imported identity
assertion, which R-I-05 allows (*"name or attribute"*). It never becomes a tag
(open question 8).

**It reaches further than the topic answer allows (open question 1).** Policy
constraints are not only relying-party filters. An issuer can force them on
everything below its subject. Take a CA certificate for Bob that carries:

- nameConstraints permitting rfc822Name `foo.com`;
- certificatePolicies {P};
- policyConstraints {requireExplicitPolicy 0, inhibitPolicyMapping 0};
- inhibitAnyPolicy 0.

Then every later certificate in the path must assert P, because:

- explicit_policy becomes 0 at §6.1.4(i)(1) (R-0458);
- mapping stops at §6.1.4(i)(2) (R-0459);
- `anyPolicy` stops matching at §6.1.4(j) (R-0460);
- §6.1.3(f) then fails any certificate without P (R-0431).

Every subject name must also be at host `foo.com`.

This construction is derived, not a source example, and it has not been run
against an implementation. It expresses "Bob may certify `*@foo.com`, only under
policy P" with no help from the relying party. It cannot express two things.
The first is that P *means* code signing, since the meaning of P lives in a
policy document outside the certificate. The second is that the scope concerns
what Bob's key *says*, rather than which certificates Bob *issues*.

---

## 7. Encoding: DER against D-3

D-3, in the 2026-09-28 minute, reads: *"DEC-002 — narrow to option 5. CBOR data
model, no IANA tags, COSE as export only; type identity is `(defining key,
label)` per P1; YAML is the human form with a canonical one-way mapping."*

**Statement of the non-mapping.** No native object is encoded as X.509, and no
X.509 object is carried as a native statement. The table goes structure by
structure.

| X.509 (§4.1, §5.1, Appendix B) | D-3 native | mapping |
|---|---|---|
| `Certificate` and `CertificateList`: SEQUENCE {tbs, signatureAlgorithm, signatureValue}, signed over the DER-encoded tbs (N-029, N-241) | a signed statement: canonical bytes plus a signature (R-O-05, proposed) | **Shape only.** An X.509 signature covers DER bytes and cannot be re-attached to a translated statement. Translation produces a *new* statement, signed by the importer, with the certificate kept as evidence by digest. |
| the `signature` field inside tbs MUST equal the outer `signatureAlgorithm` (R-0008) | an algorithm authenticated inside the signed bytes | Same intent, different identifier space: an OID (R-M-12). |
| `version [0] EXPLICIT Version DEFAULT v1` | *"an authenticated type indicator"* (R-O-05, proposed) | **No counterpart.** X.509 has a version, not a type indicator. A certificate and a CRL are told apart only by their structure (inferred). |
| DER: *"ASN.1 DER encoding is a tag, length, value encoding system for each element."* (§4.1) | CBOR major types, *"no IANA tags"* | DER's tags are fixed by the ASN.1 grammar, not allocated from an IANA registry. D-3's no-tags rule is not what excludes DER. |
| OIDs everywhere: `extnID`, `AlgorithmIdentifier`, `AttributeType`, `CertPolicyId`, `KeyPurposeId`, the `otherName` type-id (§9, N-483) | `(defining key, label)`, per P1 | **Excluded natively** (R-M-12). On import an OID is data, a foreign label, never a native type identifier. ADR-0001: *"Registry identifiers **may** appear at interchange boundaries, and such mappings are documented as lossy per R-I-01."* |
| `critical BOOLEAN DEFAULT FALSE` (§4.1, N-068) | P5: must-understand by default | **Inverted.** The flag has no native counterpart. |
| DEFAULT components are omitted (N-507) | no DEFAULT; whether a field is present is a profile rule | X.509's booleans that are explicit only when TRUE do not carry over (§2 item 5). |
| SET OF ordered by encoding: *"the DER encoding of the SET OF values requires ordering of the encodings of the values"* (N-506) | a canonical order for set-valued fields (2693 notes adapt 1; rfc-9804 notes condition 5) | **Same rule in substance**: sort by encoded bytes. DER applies it only to SET OF. RFC 5280 uses SEQUENCE OF for most lists (`Extensions`, `GeneralNames`, `certificatePolicies`), and there the issuer's order is significant. |
| named bit lists with trailing zeros omitted (R-0611); minimal INTEGERs under the sign-bit rule (N-495) | the deterministic CBOR encoder rules | DER is a deterministic encoding made of encoder-side rules, and ARCH-0001 §3.1 records X.509 as *"Dominant for TLS"*. Such rules can work at scale, which D-3 needs to hold for CBOR. It is not a reason to adopt DER. |
| time: UTCTime through 2049, GeneralizedTime from 2050; Zulu; whole seconds (R-0045) | `Validity { not_before?, not_after? }` (ARCH-0001 §4.1); the time representation is DEC-002's | **Exact on import.** The validity period runs *"from notBefore through notAfter, inclusive"* (N-051): a closed interval in whole seconds. In the 2693 notes' half-open form that is `[notBefore, notAfter + 1 s)` (derived). |
| DirectoryString: a CHOICE of five string types, compared by StringPrep and caseIgnoreMatch (R-0540, R-0542) | UTF-8 byte strings with bytewise equality (2693 notes adapt 1) | **Lossy.** Import must transcode to UTF-8 and fix one spelling. Byte equality does not preserve X.509 equality (open question 7). |
| serial numbers of up to 20 octets (R-0018, R-0019) | no field | Larger than a 64-bit CBOR integer. Imported serials travel as bytes, and only as provenance (derived). |

**Signature verification on import** should run over the tbs bytes as received,
not over a re-encoding. 5280 signs *"the ASN.1 DER encoded tbsCertificate"*
(N-029) and says nothing about input that is not DER. Verifying the bytes as
received is R-O-05's principle (proposed) applied at the import boundary
(derived).

**Export.** The matrix gives X.509 export as "—", so no export mapping is
required, and none is given. The bridge, if X.509 identities ever ride on a
COSE_Sign1 export, is `rfc-9360`: *"CBOR Object Signing and Encryption (COSE):
Header Parameters for Carrying and Referencing X.509 Certificates"*. It is held
with status `fetched` and topic `cbor-implementation`, and was not read here.
Under D-3 its headers belong to the export envelope only, never to native
statements. It fits ARCH-0001 §3.2's case (a), *"existing signer identity some
tools still carry"*.

**On the extract skill's D-3 rule.** The skill requires a header-by-header D-3
mapping for COSE, CBOR and envelope documents. RFC 5280 is neither COSE nor
CBOR, but `Certificate` is a signing envelope: a payload, an algorithm and a
signature. So the table above is the structure-by-structure mapping the rule
asks for. Its result is a non-mapping: nothing in X.509's envelope becomes
native.

---

## 8. Security considerations that carry over

§8 opens with a property we keep: *"Since certificates and CRLs are digitally
signed, no additional integrity service is necessary."* (N-460). Signed objects
can therefore travel through untrusted channels and caches: *"certificates can
be distributed via untrusted communications and server systems, and can be
cached in unsecured storage in certificate-using systems."* (§3.1, N-009).

| §8 consideration | bearing on our design |
|---|---|
| *"compromise of a CA's private signing key may have a catastrophic effect"*; and if it is detected, *"all certificates issued to the compromised CA MUST be revoked"* (N-464, R-0581) | One key is one point of failure. R-M-06's threshold principals and the 2693 notes' adopt 10 (a `k-of-n` root) address it. 5280 has no threshold form. |
| key loss: *"The CA would not be able to produce CRLs or perform normal key rollover."* (N-465) | Escrowed revocation (§5). Rollover must not depend on the old key alone (open question 4). |
| *"If revocation information is untimely or unavailable, the assurance associated with the binding is clearly reduced."*; verifiers that cannot handle the delta-CRL critical extensions *"will not be able to obtain the most recent revocation information"* (N-466) | Optional revocation features give different verifiers different assurance. Revocation statements, if we have them, need one mandatory form (R-M-05). |
| trust anchor distribution is *"a security critical out-of-band process that is beyond the scope of this specification"* (N-467); and *"By substituting public keys for which an attacker has the private key, an attacker could trick the user into accepting false certificates."* (N-469) | The `AclEntry` store is in our trusted base and in our scope. It is specified, canonical and hashable (2693 notes adapt 6). |
| *"Selection of too many trusted CAs makes the trusted CA information difficult to maintain. On the other hand, selection of only one trusted CA could limit users to a closed community of users."* (N-468) | The same trade-off governs the size of an ACL. Recorded, not resolved. |
| *"CAs SHOULD decline to issue certificates to CAs or end entities that generate weak signatures."* (R-0584) | Algorithm policy belongs to verifiers and issuers. NG3 leaves the algorithm suite unfrozen. |
| *"Inconsistent application of name comparison rules can result in acceptance of invalid X.509 certification paths or rejection of valid ones."* (N-471); a CA MUST encode its DN *"identically"* wherever the DN chains (R-0585) | Bytewise equality, with normalisation done at authoring (2693 notes adapt 1). 5280 reaches the same rule from the failure side, yet still keeps string preparation at the verifier (§7.1). |
| excluded subtrees fail open on an encoding mismatch (N-473, R-0587) | Keep DEC-004's algebra positive-only (§3). |
| constraining one name form gives *"no protection against use of other name forms"* (N-474) | A grant must not be open along any dimension it does not mention (§3). |
| issuer names collide, so a CRL's path and the certificate's path must *"terminate at the same trust anchor"* (N-475, R-0589) | X.509's own fix is to read a name relative to a key, the anchor's. That is R-M-03 applied once, at the root, and it supports the matrix's `x509:` namespace *"of the *importer*, not of the CA"*. |
| mail local-parts are case-sensitive, but `emailAddress` matching is not (N-476) | An imported mail name keeps its local-part bytes. Folding their case would conflate two principals. |
| https in CRLDP or AIA: *"The relying party is forced to perform an additional path validation"*, *"unresolvable dependencies"*, *"unbounded recursion"* (N-478, R-0592) | ARCH-0001 §4.3 lists *"current time and optional online validity checks"* among the inputs of the decision procedure, and R-M-05 takes *"an ordered cert set and ACL"* as given. 5280 shows what happens when obtaining such inputs becomes part of validation. Status evidence is gathered first and passed in as input. |
| self-issued certificates for rollover: *"the CA protects its new public key using its previous private key and vice versa using two self-issued certificates"* (N-480) | Rollover as two statements between keys, with no exemption based on name equality (open question 4). |
| Latin1 and TeletexString confusion: *"When comparing names encoded using the Latin1String character set, false positives and negatives are possible."* (N-481) | One string type. Import transcodes once. |
| confusable names: *"people doing visual comparisons between two different names may think they are the same when in fact they are not"* (N-482) | Rendering (P3, DEC-007) is never identity. Identity is bytes. |

---

## 9. What we adopt

Each item gives one line of evidence. The analysis is in the section cited.

1. **The root is local input, trusted because of how it was delivered, not
   because it was signed** (R-0390, R-0381, N-404; §4). This agrees with
   `AclEntry` and the 2693 notes' adopt 2.
2. **Constraint state that can only narrow.** The evidence is *"may be
   decreased, but may not be increased"* (R-0407 to R-0409), intersection and
   union (R-0451, R-0452), and the falling depth counter (R-0463, R-0464; §§2,
   3). This agrees with the 2693 notes' adopt 3.
3. **Containment as the decision rule for a scoped grant.** A name must be
   *"within one of the permitted_subtrees"* (R-0422, R-0423; §3). This supports
   the 2693 notes' rule `AIntersect(A, R) = R`.
4. **Specify the result, not the procedure, and keep path finding outside the
   verifier.**
   - *"Implementations are REQUIRED to derive the same results but are not
     required to use the specified procedures."* (R-0001)
   - *"MUST provide functionality equivalent to the external behavior resulting
     from this procedure."* (R-0367)
   - *"The procedure performed to obtain this sequence of certificates is
     outside the scope of this specification."* (N-330)

   This agrees with the 2693 notes' adopt 4.
5. **Delegation as a fail-closed boolean.** Absence means the key *cannot
   certify* (R-0155, R-0461). Version 3 added the field to cut the dependence
   on out-of-band knowledge: *"reducing the reliance on out-of-band information
   demanded in PEM"* (N-013; §2). This agrees with R-M-10 and the 2693 notes'
   adopt 7, the integer apart.
6. **Positive constraints rather than exclusions**, on 5280's own failure
   analysis (N-473, R-0587; §3).
7. **Byte-identical authoring of anything that will be compared** (R-0183,
   R-0585, R-0222; §§3, 8).
8. **Reading names relative to the anchor's key, as the cure for collisions**
   (R-0589, R-0526; §8). This is evidence for R-M-03 and for the matrix's
   importer namespace.
9. **Sequence numbers for any status series**, so that deciding which entry
   supersedes which is a comparison of integers (N-266, R-0297, R-0300; §5).
10. **The issuer bounds staleness, and the verifier may demand fresher evidence**
    (R-0506, N-016; §5). This is the option in the 2693 notes' open question 7,
    as deployed.

## 10. What we adapt, and how

1. **The certificate names who may revoke it, in every case.** 5280 requires
   this only for indirect CRLs, and only when a distribution point is present:
   *"If the certificate issuer is not the CRL issuer, then the cRLIssuer field
   MUST be present"* (R-0206). The extension itself carries only a SHOULD on its
   criticality and a RECOMMENDS for support (R-0203, R-0204). Without it, §6.3.3
   falls back to whatever CRLs the issuer's *name* has produced (R-0537). What we
   need is the 2693 notes' adopt 6 (rfc-2693#R-0072) in every case: the
   statement fixes its revoker, by key.
2. **An explicit `delegate` field, present on every AuthzCert.** This is
   X.509's boolean without DER's DEFAULT (N-507; §2 item 5).
3. **Name constraints' chain intersection, generalised.**
   - Keep monotone intersection, checked by containment.
   - Drop exclusions, and drop dimensions that are open by default.
   - Let each profile declare its own forms and matching rules under R-M-08,
     where 5280 fixes five per-form rules in the specification itself and
     leaves three forms undefined (§3).
4. **The trust anchor as a specified object**: an `AclEntry` whose tag is
   always processed, never *"free to process or ignore"* (N-406; §4).
5. **The CRL entry as a single revocation statement.** Keep the content
   (subject, date, reason, invalidity date). Have it signed by a key that the
   revoked statement names, so that it can be escrowed. Drop the list (§5).
6. **The import mapping table** for WP5, R-I-01 and R-I-05, as the source makes
   the fields available. This is derived, and WP5 decides.

   | X.509 | native | R-I-01 class |
   |---|---|---|
   | `subjectPublicKeyInfo` | `Key`. `KeyId` is computed by our rule, never taken from the SKI (N-084) | preserved; KeyId inferred |
   | subject DN, `subjectAltName` | `NameCert` labels under the importer's `x509:` namespace | preserved as labels; the equality semantics are lost (§7) |
   | issuer DN, serial number, the X.509 path | `provenance: x509`, with the certificate's digest | preserved, as provenance only |
   | `notBefore`, `notAfter` | `Validity`, half-open (§7) | preserved |
   | `cA`, `keyCertSign`, pathLenConstraint, nameConstraints, the policy constraints | enforced by X.509 validation inside the translator, then dropped | dropped (*"Do not treat CA bit as AuthzCert"*) |
   | `valid_policy_tree`, `extendedKeyUsage` | candidate attributes (R-I-05) | inferred or dropped (open question 8) |
   | CRLDP, AIA (`id-ad-ocsp`) | the translator's status check at import time | dropped from the output |

7. **The criticality rule becomes P5.** Constraint fields are must-understand
   because every field is (§3).

## 11. What we reject, and why

1. **X.509 as the native encoding.** Rejected by R-M-01 (§1).
2. **Path validation as the reducer.** Rejected by ARCH-0001 §6. It proves a
   name-to-key binding (N-320, R-0489), which is procedure 1 of §4.3, not
   procedure 2.
3. **Chaining, revocation scope and anchors by name** (R-0421, N-230, R-0389).
   These conflict with R-M-02 and R-O-01.
4. **Exclusions in the authorization algebra.** They fail open when matching
   fails (N-473).
5. **Dimensions that are open by default.** A name form the constraint does not
   mention is not constrained at all (N-149, R-0451, N-474).
6. **The self-issued exemption** from depth and name constraints (N-150,
   R-0384). It rests on DN equality (R-0383), which means nothing for keys.
7. **Opt-in criticality, and ignoring the unknown** (R-0072, R-0619). ARCH-0002
   P5 inverts both.
8. **The policy machinery**: certificatePolicies, policyMappings, the policy
   tree, inhibitAnyPolicy, requireExplicitPolicy and inhibitPolicyMapping. Its
   intersection core duplicates DEC-004. The rest conflicts with R-M-12,
   R-M-05, DEC-008 and P3 (§6).
9. **Reversible revocation**: `certificateHold` and `removeFromCRL` (N-279,
   R-0534, N-311). A status that can return to unrevoked is not monotone.
10. **Complete-list revocation as the native mechanism.** Its negative assertion
    cannot be escrowed, verifier support for its variants is optional (N-234),
    and lists that are current at the same moment may overlap (N-252, R-0318).
11. **Defaults that depend on position.** In an indirect CRL, an entry without
    `certificateIssuer` belongs to *"the same as that for the preceding entry"*
    (N-316). Meaning that depends on order cannot survive a canonical sort of
    set-valued fields.
12. **String preparation at the verifier, for identity** (R-0540, R-0542).
    5280's own §8 shows the hazard (N-471). Equality is bytewise.
13. **Fetching inside validation** (N-478, R-0592). Status evidence enters
    reduction as an input (ARCH-0001 §4.3, R-M-05), and is gathered before
    reduction starts.
14. **The SKI as an identifier.** It is a hint (N-081), and it may be any unique
    number (N-084). DEC-003 requires *"canonical key bytes before hashing"*.
15. **Validity defined as a warranty to maintain status, and the 9999
    convention** (N-049, R-0036). Both conflict with R-O-02.

---

## 12. Mapping to our decisions

| Ours (ARCH-0001 text, priority) | What RFC 5280 contributes | Status |
|---|---|---|
| **R-M-01** · M · *"Native encoding SHALL NOT be X.509 / PKIX."* | The thing excluded. RFC 5280 is the base profile of the named family. Six concrete conflicts (§1). | **Holds.** Its words exclude an encoding. ARCH-0001 §1, §6 and R-M-06 extend the exclusion to the model and the reducer. |
| **R-M-02** · M · *"A principal MAY be identified solely by key or key digest."* | The issuer is a DN (R-0023). The SKI is not a key digest (N-084). | Contrast. X.509 needs a name where we need only a key. |
| **R-M-03** · M · *"Names SHALL be interpreted only relative to an issuing principal."* | Global DNs collide (N-475). The fix ties CRL and certificate paths to the same root key (R-0589). | **Evidence for**, and for the matrix's `x509:` namespace *"of the *importer*"*. |
| **R-M-04** · M · *"Name bindings and authorization bindings SHALL be distinct object kinds."* | Name constraints scope names only (R-0162, N-149). One certificate carries the name binding and every delegation control. §2 foresees moving authorization out (line 353). | **Strongest support** in the record. X.509 fails R-M-04 under both readings (§3). |
| **R-M-05** · M · *"Authorization composition SHALL be deterministic given an ordered cert set and ACL."* | Results are required to be equivalent (R-0001, R-0367). Against that: optional features (N-234, N-326, R-0397), *"free to process or ignore"* (N-406), overlapping CRLs (N-252, R-0318), and UNDETERMINED with no rule attached (R-0537). | **Evidence for the precondition.** The algorithm is deterministic; its inputs are not. |
| **R-M-06** · M · threshold principals *"without encoding them as a CA hierarchy"* | No threshold form. The compromise of one CA key is catastrophic (N-464). | Contrast. Nothing to import. |
| **R-M-08** · M · *"Tag intersection semantics SHALL be defined for every tag profile the implementation claims."* | Name constraints are one fixed profile with per-form semantics. *"MUST either process the constraint or reject the certificate"* (R-0169) means: claim it, or reject. | **Adapted** (§10 item 3). |
| **R-M-09** · S · validity intersection | Each certificate must be valid at the time in question (R-0379), and its interval is closed (N-051). | On import, maps exactly onto half-open intervals (§7). |
| **R-M-10** · S · *"Delegation SHALL be an explicit boolean (or equivalent) on `AuthzCert`."* | `cA` is the boolean, with the optional integer pathLenConstraint beneath it. DER makes FALSE implicit (N-507). The depth count exempts name-equal certificates (R-0384). | **Evidence on both sides** (§2). Two readings remain open. Explicit presence is supported under either. |
| **R-M-12 / ADR-0001 / ARCH-0002 P1** · M · key-relative extension points | Every identifier is an OID in an IANA-delegated arc (N-483, R-0194). | **Excluded natively.** OIDs are data at the boundary, lossy per R-I-01. |
| **R-I-01** · M · a mapping table: what is preserved, dropped or inferred | The field inventory (§10 item 6). | Input to WP5. |
| **R-I-02** · M · *"Import SHALL NOT require the foreign object to become a native trust anchor."* | The anchor may be any local input (§6.2), so an X.509 root can stay configuration of the translator (§4). | **Compatible.** |
| **R-I-05** · S · *"Import X.509 only as a foreign identity assertion about a key (name or attribute), marked `provenance: x509`."* | §6 proves exactly an identity assertion about a key (N-320). The policy tree and EKU are candidate attributes. | **Compatible.** The attribute question is open (open question 8). |
| **R-O-01** · M · an issuer key specifiable as `KeyId` | The AKI keyIdentifier is a MUST for conforming CAs (R-0082), but validation does not check it (N-081). | On import, the issuer key comes from path validation, not from the AKI. |
| **R-O-02** · S · *"Short-lived validity preferred over revocation-heavy design; revocation still representable."* | Validity is defined through revocation (N-049), and there is no short-lived provision (`rfc-9608` came later, outside the source). CRL entries map onto revocation statements; the lists do not (§5). | **Contrast, with a partial adapt.** Escrow is the native fit. |
| **R-O-03** · S · canonicalization cited, not invented | DER is cited ([X.690]), and is not native. | Not affected natively. |
| **R-O-05** (proposed) · *"The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator."* | X.509 signs the DER tbs bytes and authenticates its algorithm (R-0008), but has no type indicator. | A partial precedent (§7). |
| **R-O-06** (proposed) · separate results for the three procedures | §6 folds policy acceptance into path validity (R-0431, R-0488). | Contrast. |
| **ARCH-0001 §4.2 `AclEntry`; ARCH-0002's note on *"trust roots you chose yourself"*** | §6, §6.1.1(d) and §6.2 (R-0390, R-0381, N-404). | **Agrees.** Ours is specified (§4). |
| **ARCH-0001 §4.3** procedures | Path validation is procedure 1, name resolution. | A classification for WP5. |
| **ARCH-0001 §6** matrix and forbidden mapping | §1 and §2 give the source's reasons. | **Holds.** |
| **ARCH-0002 P2**: delegation scoped by *"(Domain, Topic)"* | X.509 scopes by names and by policy OIDs. A policy OID is the nearest thing to a topic, and its meaning is held out of band (§6). | Contrast. |
| **ARCH-0002 P5**: validity checked, the unknown rejected | `critical DEFAULT FALSE`, and *"ought to be ignored"* (R-0072, R-0619). | **Inverted.** |
| **DEC-002 / D-3** | DER against reduced CBOR (§7). | **A non-mapping, stated.** |
| **DEC-003** · *"Must specify: canonical key bytes before hashing."* | SKI method (1) hashes *"the value of the BIT STRING subjectPublicKey (excluding the tag, length, and number of unused bits)"* (§4.2.1.2, N-083), and leaves out the `AlgorithmIdentifier`. | A precedent for hashing the key bytes. Leaving out the algorithm conflates one key used under different algorithms, while ARCH-0001's `Key` includes an *"algorithm identifier"* (derived). |
| **DEC-004** · the tag language | Name constraints implement option 1's core for names, and option 1 cannot be expressed in them (§3). | Evidence only. |
| **DEC-008** (open) · its proposed fixed core | Optional core steps (N-326) and network recursion (R-0592). | Evidence for the proposed answer: a fixed, closed core. |

---

## 13. Open questions

1. **The `delegation-models` answer makes five claims about X.509 that this
   extraction corrects, qualifies or sharpens.** The topic is not edited here. Issue #64
   requires the answer to be corrected later.

   - *"within that subtree he is unrestricted — every key usage, every
     purpose"*.
     **Correction.** False for purposes: *"In a CA certificate, these policy
     information terms limit the set of policies for certification paths that
     include this certificate."* (N-106). With requireExplicitPolicy 0, an issuer
     forces that limit on every later certificate (R-0458, R-0431; §6).
     **Holds for key usage.** An issuer cannot force keyUsage or EKU into its
     subject's certificates.
   - *"Neither X.509 nor OpenPGP can express "Bob may speak for *@foo.com ABOUT
     CODE SIGNING"; X.509 needs extendedKeyUsage and the policy tree to get near
     it"*.
     **Correction.** EKU has no role in path validation: *"In general, this
     extension will appear only in end entity certificates."* (N-172), and §6
     never processes it. The policy machinery alone expresses "certify only
     `foo.com` names, and only under policy P" (§6).
     **Holds.** The discriminator survives, since the scope is over the
     certificates Bob issues and the meaning of P is held out of band. But
     "cannot express" is too strong.
   - *"In X.509 the delegation is three flags on the same certificate ... cA,
     keyCertSign, pathLenConstraint"*.
     **Correction.** pathLenConstraint is an integer, not a flag, and
     nameConstraints, policyConstraints and inhibitAnyPolicy are delegation
     controls on the same certificate too.
     **Holds.** The conclusion (*"no separate object to revoke, scope or
     audit"*) stands, and is stronger than stated.
   - *"X.509 shipped it too as pathLenConstraint. TWO OF THE FOUR HAVE THE FINER
     MECHANISM AND SPKI DECLINED IT"*.
     **Qualification.** X.509 has the boolean as well. Its integer is
     optional, subordinate, and defaults to the boolean's semantics (N-145,
     R-0161). The evidence is "a boolean plus an optional bound" (§2).
   - *"RFC 5280 supplies neither the non-overlap rule nor a requirement that a
     certificate point at its own CRL"*.
     **Confirmed, and sharper than stated:**
     - 5280 *permits* overlap (N-252, N-283);
     - the pointer is only a RECOMMENDS for support (R-0204);
     - the certificate must name a *different* CRL issuer (R-0206);
     - 5280 meets RFC 2692's other condition, explicit dates (R-0280).
   - **Verified without correction:**
     - the mail-constraint quotation (R-0176), with the precision that
       `*@foo.com` is the host form `foo.com`, and that `.foo.com` excludes the
       host;
     - *"X.509 intersects permitted subtrees and unions excluded ones"* (R-0451,
       R-0452), per name form, and with self-issued certificates exempt;
     - both trust-anchor quotations (N-323, N-404). The second begins
       *"The selection"* in the source.
2. **Which reading of R-M-10?** Either the strict reading (a boolean only, with
   an imported pathLenConstraint dropped), or *"(or equivalent)"* read as
   admitting a bound beneath the boolean (§2). The 2693 notes' open question 9
   should be weighed in the same place.

   One more document may bear on the integer side. `rfc-3820`, *"Internet
   X.509 PKI Proxy Certificate Profile"*, is held as a stub in the
   `authorization-reduction` topic. Its title and topic suggest it is where
   PKIX delegates *authority* rather than naming, but it is not read here, so
   that is an expectation, not a finding. It is the next document to read for
   this question.
3. **If a depth bound is admitted, does it count keys or principals?** X.509
   counts non-self-issued certificates, which amounts to counting name changes
   (R-0463, R-0384). In a key-centric model only keys are left to count. RFC
   2693's *"temporary signing key"* objection then applies in full.
4. **What is key rollover in our model, and does it use up depth or escape
   constraints?** X.509's answer is a pair of self-issued certificates, old key
   over new and new key over old (N-480). They are exempt from depth and name
   constraints because the DN matches. A native answer would be two statements
   between keys. Whether those are exempt is a design choice the source cannot
   make for us. If they are not exempt, rollover under a bound like
   pathLenConstraint uses up depth.
5. **What does UNDETERMINED mean?** §6.3.3 can return UNDETERMINED (R-0537).
   §6.1.3(a)(3) requires that *"At the current time, the certificate is not
   revoked."* (R-0420). Nothing maps UNDETERMINED to accept or to reject, which
   is a new finding (see item 11). R-O-06 (proposed) suggests reporting it as a
   distinct result. A native verifier needs a stated rule. Failing closed is the
   rule consistent with ARCH-0002 P5, *"Validity is checked, never assumed"*.
6. **How is an `ArtifactStatement` checked after its signer's validity period
   ends?** X.509 drops revocations after expiry (R-0003), and cannot validate
   outside the validity period (N-328). The candidates are evidence fixed at
   signing time: a SCITT-style receipt (R-O-04, Could), or a trusted timestamp.
   Neither is decided.
7. **Equality on import.** X.509 compares:
   - DNs after StringPrep with case folding (R-0540, R-0542, R-0543);
   - DNS names case-insensitively (R-0557);
   - URIs after normalisation, and then case-sensitively (R-0577);
   - mail addresses with an exact local-part and a case-insensitive host
     (R-0580).

   Our labels compare bytewise. WP5 must fix one spelling per form at import,
   and must list X.509's equivalences as lost under R-I-01. Two names that are
   equal in X.509 may become two native labels.
8. **Does the policy tree survive import as an attribute?** R-I-05 allows *"name
   or attribute"*. Keeping `valid_policy_tree` or EKU as attributes keeps the
   information. Dropping them keeps the mapping small. Either way, the tree must
   never become a tag.
9. **OpenPGP level against pathLenConstraint**, if both are imported.
   pathLenConstraint 0 lets its subject certify end entities only. So the
   correspondence may be "level n ≈ pathLenConstraint n − 1". That is inferred
   from the topic answer's description of levels (*"level n may issue level
   n-1"*), and has not been checked against rfc-9580.
10. **X.509 attribute certificates are not held.** The matrix row *"X.509
    attribute certificate | I | P | AuthzCert (tag profile TBD)"* depends on
    RFC 5755, which the library does not hold. That is an ingestion gap, if the
    row is kept.
11. **Source defects and ambiguities that bear on design.** These are recorded,
    not repaired. First, those from the shared pass-1 list:
    - **§4.1.2.2: positive, or non-negative?** *"The serial number MUST be a
      positive integer"* (R-0015), against *"CAs MUST force the serialNumber to
      be a non-negative integer."* (R-0017). And *"Non-conforming CAs may issue
      certificates with serial numbers that are negative or zero."* (R-0020).
      Serial numbers are weak identifiers, so key imported certificates and
      revocations by digest, never by (issuer, serial).
    - **RECOMMENDS is not an RFC 2119 keyword.** Two rules this file leans on
      are stated only in that form: support for CRL distribution points
      (R-0204), and the key-identifier methods (R-0085, R-0094, R-0087). The
      certificate's pointer to its revocation source is therefore not even a
      BCP 14 recommendation in form.
    - **Rules carried in ASN.1 comments and lowercase text.**
      - At most one `onlyContains*` boolean may be TRUE; this comes from an
        ASN.1 comment (N-294; R-0334, inferred).
      - *"The removeFromCRL (8) reasonCode value may only appear in delta
        CRLs"* is lowercase (N-311; R-0359, inferred).
      - The comparison rules that define name equality are partly lowercase:
        *"the mapping shall include case folding"* (line 5353), *"shall perform
        a case-insensitive exact match"* (line 5462), *"shall perform a
        case-sensitive exact match"* (line 5533), and *"Binary comparison should
        be used"* (line 1320).
      - The unknown-element rule that P5 inverts is *"ought to be ignored"*
        (line 7557).
      - In a nameConstraints URI field the value *"must hold a DNS name"* (line
        7546).

      The lesson for our schemas: a constraint lives in the schema as a
      checkable rule (P5's "valid" level), never in a comment.
    - ***"Upper Bounds MUST be regarded as mandatory"*** (R-0600) has no actor.
      On import, who rejects an over-long value? Under P5, the importer does.
    - **§7.2's SHALL and SHALL NOT for display conversion** sit under a
      lowercase *"should"* (line 5422). Display conversion is advisory, and
      identity is the ACE bytes. That is R-O-05's split between the signed form
      and the display form (proposed).
    - **Not carried.** The rest of the shared list does not bear on design: the
      duplicated ASN.1 definitions, the repeated key-identifier paragraphs, the
      typos, and `keyEncipherment`'s *"shall be set"*, which is at line 1669, not
      1688.

    Then, new in this pass:
    - **UNDETERMINED has no consequence** (open question 5). §6.1.3(a)(3) and
      §6.3.3 never meet. This is a gap, not a contradiction.
    - **Name-constraint intersection is defined only by DNS examples.**
      §6.1.4(g) gives *"the intersection of example.com and foo.example.com is
      foo.example.com"* and *"the intersection of example.com and example.net is
      the empty set"* (R-0451), both in dNSName style. Nothing gives the results
      for:
      - the leading-period forms of URI and rfc822Name;
      - one of rfc822Name's mailbox, host and domain forms against another.

      For example, the mail constraints `example.com` and `.example.com` share
      no address under N-155's definitions. Implementations must infer all of
      these results. It is the same gap the 2693 notes found in AIntersect
      (*"A result for every pair of forms"*).
    - **A possible conflict between §3.3 and §5.2.4.** Two rules meet here:
      - *"An entry MUST NOT be removed from the CRL until it appears on one
        regularly scheduled CRL issued beyond the revoked certificate's validity
        period."* (R-0003);
      - *"A CRL issuer MAY optionally list a certificate on a delta CRL with
        reason code removeFromCRL if the notAfter time specified in the
        certificate precedes the thisUpdate time specified in the delta CRL"*
        (R-0314).

      If the first CRL after expiry is that delta, the entry is removed without
      ever having appeared on a CRL issued after the validity period. That
      holds unless "regularly scheduled CRL" means complete CRLs only, and the
      source does not say so.
12. **The rfc-2693 notes' glosses, checked against ARCH-0001.** Four differ from
    the text:
    - R-M-03 says *"issuing principal"*, not "issuing key";
    - R-M-04 says *"distinct object kinds"*, not "certificates separate";
    - R-M-10 ends *"on `AuthzCert`"*, and is priority S;
    - R-O-02 is glossed there as "(CRLs vs positive on-line validation)", but
      its text is *"Short-lived validity preferred over revocation-heavy design;
      revocation still representable."*

    Their conclusion for R-O-02 fits the real text. The gloss should be
    corrected when #64 closes.
13. **ARCH-0002 cites R-M-01 in an SPKI context.** Its correction note says
    *"R-M-01's framing was right and got over-applied: SPKI is prior art we take
    ideas from, and fidelity to its formalism is not a goal."* R-M-01's text is
    about X.509 and says nothing about SPKI fidelity. Either the note means a
    different requirement, or R-M-01 carries a framing its text does not state.
    That is worth one line in ARCH-0002's next revision. It is not settled
    here.
