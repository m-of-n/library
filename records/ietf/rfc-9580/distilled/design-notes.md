---
record: rfc-9580
kind: design-notes
title: "rfc-9580 — bearing on our design"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 9580 — bearing on our design

RFC 9580 is the only foreign format ARCH-0001 gives a native kind of its own
(`Endorse`), and, with X.509, one of two whose identity objects have an import
requirement of their own (R-I-04 and R-I-05). ARCH-0001 §1 places it in one sentence: *"PGP Web of Trust is an
**interchange and introducer pattern**, not the validation algorithm."* R-I-04,
the `Endorse` kind, the matrix row and WP4 all follow from that sentence. The
rfc-2693 notes audit an inheritance, and the rfc-5280 notes survey a boundary.
This file drafts an import mapping. It reads the full text for what WP4 would
have to carry, what it would have to drop, and what the one deployed scoped
delegation mechanism teaches the native model.

**Four things to hold while reading.**

1. **The source binds implementations, and on import our translator is one.**
   `requirements.yaml` counts 365 BCP 14 keywords and holds 421 entries. Their
   conformance target is an OpenPGP implementation. The native model is not
   one, so a 9580 MUST cited here is a precedent, not an obligation. The
   exception is the WP4 translator. It parses and verifies OpenPGP packets, so
   every consuming-side rule binds it: §5.2.5 on malformed signatures,
   §5.2.3.7 on critical subpackets, and §10 on packet grammars.
2. **Our decisions are quoted from their primary sources, which this pass
   read.** They are:
   - ARCH-0001 v0.1.1 (updated 2026-09-21) and its CHANGELOG;
   - ADR-0001;
   - ARCH-0002 v0.5.0, in which P1 is accepted, P2, P3, P5 and P6 are
     provisionally accepted by D-2, and P4 and P7 are held;
   - DECISIONS-0001;
   - the 2026-09-28 minute (`project/meetings/2026-09-28.md`), which records
     D-1 to D-7;
   - the v0.2.0 proposal, used for the text of R-M-11, R-M-12 (accepted by
     ADR-0001), R-O-05 and R-O-06, and for its §11. R-M-11, R-O-05 and R-O-06
     are proposed, not accepted: DECISIONS-0001 item 4 says *"the new
     requirements have no force"*.

   Two scheduling facts frame the whole file. The proposal's §11 says
   *"Nothing is proposed for WP4 or WP5 — OpenPGP introducer import, X.509
   import — which the execution plan places out of scope for the semester."*
   And D-1 keeps *"very short further scenarios (email delegation among
   them)"* as *"use cases that drive *schema definition*, not as specified
   targets"*. RFC 9580 is the deployed form of the email-delegation scenario.
   So the import mapping below is groundwork, and the parts that matter now are
   the ones the email-delegation schema needs (notes 2 and 3).

   Priorities are ARCH-0001's. R-M-02 to R-M-08, R-I-01, R-I-02 and R-O-01
   are **M**ust. R-M-09, R-M-10, R-I-04, R-O-02 and R-O-03 are **S**hould.
   R-O-04 is **C**ould.
3. **Ids and section numbers.**
   - `rfc-9580#R-NNNN` is written R-NNNN, and N-NNN is an entry of
     `normative.md`.
   - A quotation with neither is descriptive text, and carries its section and
     source line. Line numbers count the `.cache/rfc-9580.txt` byte order mark
     as line 1, as every artifact of this record does.
   - Ids of other records are always written in full (`rfc-2693#R-NNNN`,
     `rfc-5280#R-NNNN`), because the R-NNNN series collide.
   - "The 2693 notes" and "the 5280 notes" are
     `records/ietf/rfc-2693/distilled/design-notes.md` and
     `records/ietf/rfc-5280/distilled/design-notes.md`.
   - A bare § is a section of RFC 9580. A section of any other document carries
     that document's name: ARCH-0001 §4.2, RFC 2693 §4.1, proposal §11.
   - The numbered sections of this file are *notes*. "Note 3" is section 3
     below. The items of notes 13, 14 and 15 are also called adopt n, adapt n
     and reject n, and the items of note 17 are open question n.
   - Vector ids (`PGP-…`) are from `examples/vectors.yaml`. Ids from this
     record's other artifacts carry their file.

   RFC 9580 is read as published (July 2024). Implementation behaviour (GnuPG,
   Sequoia) comes from `record.yaml` `implementations`, which records secondary
   sources, and is marked *outside the source*.
4. **Nothing here decides R-I-04, R-M-10, DEC-003, DEC-004 or WP4.** Adopt,
   adapt and reject are this file's reading of the evidence: note 13 adopts 11
   items, note 14 adapts 9 and note 15 rejects 14. Note 17 holds the open
   questions. A DEC is accepted only in an ADR (ARCH-0001 §9, R-D-02).

---

## 1. Where ARCH-0001 already places OpenPGP

ARCH-0001 says more about OpenPGP than about any foreign format except X.509.
None of it cites RFC 9580, which is not in `related_rfcs`. The closest
reference is §10's *"OpenPGP / GnuPG trust-signature model (meta-introducers)"*.

| ARCH-0001 text | What RFC 9580 says |
|---|---|
| §1: *"PGP Web of Trust is an **interchange and introducer pattern**, not the validation algorithm."* | **Literally true: there is no validation algorithm to adopt.** *"Because OpenPGP places final authority for validity upon the receiver of a signature, it may be that one signer's casual act might be more rigorous than some other authority's positive act."* (§5.2.1, line 1491). *"A revoked certification is no longer a part of validity calculations."* (R-0151) names a computation the document never defines. The phrase "web of trust" occurs once, in the title of the [SHAMBLES] reference (§16.2, line 7539). |
| §3.1 row: principal *"Key + UIDs"*; name scope *"Global-ish (email)"*; trust *"Web of Trust; later trust-signatures (meta-introducers)"*; fault tolerance *"Multiple introducers; owner-defined trust"*; status *"Identity and mail; weak authorization language"* | All five hold. A User ID is *"intended to represent the name and email address of the keyholder"*, and *"there are no restrictions on its content"* (N-312). Meta-introducers are level 2 (R-0117). The authorization language is Key Flags (five usages and two advisory flags, N-181) plus free-form notations (N-165). Note 9 qualifies "weak". |
| §3.2 row: *"OpenPGP signatures \| identity and data signatures \| OpenPGP packets \| Introducer import candidate"* | Data signatures (0x00, 0x01, 0x02, 0x40, 0x50) appear in this row and in no matrix row or R-I requirement (open question 4). |
| §3.3 item 4: *"PGP remains useful as an **introducer graph import**, mapped onto name certs or weighted endorsements — not as the reducer."* | Confirmed. The reducer it declines does not exist in the source (row 1). |
| §4.2 `Endorse`: binds *“issuer treats subject as introducer at weight w”*, *"Optional PGP-shaped import; not required for AuthzCert reduction"* | The weight w is the trust amount (R-0119). A trust signature also carries a **depth** (the level) and a **scope** (the Regular Expression). `Endorse` has neither field (note 2). |
| R-I-04 · S · *"Import OpenPGP identity signatures as `NameCert` and/or `Endorse`, never as `AuthzCert` unless an explicit profile says so."* | The escape hatch is needed. A level ≥ 1 trust signature is authorization-shaped (note 2). |
| §6 matrix: *"OpenPGP key + UIDs + sigs \| I \| P \| Key, NameCert, Endorse \| No tag language; trust values are local to importer"* | **"Trust values are local" conflates two things.** The Trust packet is local (N-310, R-0224, R-0225). The trust-signature level and amount are signed, and exportable by default (R-0109). That they sit in the hashed area is derived: the source states no placement (messages.yaml, subpacket-trust-signature). They travel with the certificate. What is local is how to *combine* them (note 4). |
| WP4: *"Mapping spec: OpenPGP introducers ↔ NameCert/Endorse"* | The arrow runs both ways while the matrix gives export as P. Like SPKI and unlike X.509, an OpenPGP export can be signed by the native key itself (note 11). |

Three things the source has that no matrix row or R-I requirement covers:

- **data signatures**, which only §3.2's row names (open question 4);
- **subkeys**: a principal that is a key *set* under one primary (note 10);
- **revocation as issuer-signed single statements**, with escrow (note 5).

---

## 2. Trust signatures: delegation riding on a name binding (R-I-04, R-M-04, R-M-10)

**What the source has.** *"The signer asserts that the key is not only valid
but also trustworthy at the specified level."* (§5.2.3.21, N-155). The body is
*"(1 octet "level" (depth), 1 octet of trust amount)"* (R-0114).

- *"Level 0 has the same meaning as an ordinary validity signature."* (R-0115)
- *"Level 1 means that the signed key is asserted to be a valid trusted
  introducer, with the 2nd octet of the body specifying the degree of trust."*
  (R-0116)
- *"Level 2 means that the signed key is asserted to be trusted to issue level
  1 Trust Signatures; that is, the signed key is a "meta introducer"."*
  (R-0117)
- *"Generally, a level n Trust Signature asserts that a key is trusted to issue
  level n-1 Trust Signatures."* (R-0118)
- *"The trust amount is in a range from 0-255, interpreted such that values
  less than 120 indicate partial trust and values of 120 or greater indicate
  complete trust."* (R-0119), and *"Implementations SHOULD emit values of 60 for
  partial trust and 120 for complete trust."* (R-0120)

**One signature, two statements.** The subpacket rides on a certification.
The certification binds a key to a User ID: *"In effect, the signer is
testifying to the belief that this public key belongs to the user identified by
this User ID."* (§10.1.5, N-423). The trust signature adds a second claim under
the same signature: this key's own certifications count. The 5280 notes find
the same fusion in X.509 (their note 3), where `cA` rides on the certificate
that carries the name. Here it is a subpacket rather than a field, which makes
it separable on import, but under one signature it is still one statement.

**Which signature types may carry it is unstated.** §5.2.3.21 speaks of *"the
key"*. §5.2.3.22 limits *"signatures by the target key on User IDs"* (R-0123),
which presumes a delegate who certifies User IDs, not a host signature over
one. A Direct Key signature by a third party is *"appropriate for statements
that non-self certifiers want to make about the key itself rather than the
binding between a key and a name"* (§5.2.1.10, N-081). A trust signature
carried there would be delegation with no name binding, the shape R-M-04
wants. The source neither allows nor forbids it (open question 6).

**Mapping onto R-I-04 (derived).**

| OpenPGP | ARCH-0001 §4.2 reading | ARCH-0002 P2 / P6 reading |
|---|---|---|
| certification 0x10–0x13 with no Trust Signature, or level 0 | `NameCert`: issuer's key binds the User ID to the subject key | *A says K has name "uid"* (P6) |
| level 1, amount a | `NameCert` + `Endorse` with w = a | the name statement, plus *A says K can speak about (names, all User IDs)* |
| level 1 + Regular Expression r | `NameCert` + `Endorse`; **r has no field** | the name statement, plus *A says K can speak about (names matching r)*: P2's delegation, scoped |
| level n ≥ 2 | `NameCert` + `Endorse`; **the depth has no field** | the delegation statement with depth n − 1 |

The right-hand column is the finding. ARCH-0002 P6 makes a name *"a statement
whose predicate is a name"*. Under P6, the authority to issue name statements is
authority over one predicate type. And ARCH-0002 P2 reads delegation as
*"A says B **can speak about** (Domain, Topic)"*. So a level ≥ 1 trust
signature is P2's delegation with Topic = name bindings. Its expression r scopes
the *subjects* the delegate may name, User ID strings, and P2's (Domain, Topic)
has no slot for that: a domain of discourse is *"a *set* of the schemas in
P3"* (P4), not a set of strings. R-I-04's line between `NameCert` and `AuthzCert` becomes a line
between predicate types. The *"explicit profile"* it anticipates is a P7
profile, with these parts:

- the tag type, a §8 regular expression over User IDs;
- its intersection semantics, which the source does not give (note 3);
- the required verifier behaviour;
- the rendering, the human-readable form per P3.

P7 is held, so this is a reading, not a recommendation.

There are three import options, and WP4 has to choose (open question 1):

1. **Lossy, within the current kinds.** Import level ≥ 1 as `NameCert` plus
   `Endorse(w = amount)`. Drop the level and the regular expression, and list
   both as dropped under R-I-01. This is the minimum honest v0.1 mapping. It is
   unsafe to use as a delegation: an `Endorse` with no scope, built from a
   trust signature that had one, would vouch for more than its issuer did.
   It is safe only because `Endorse` is *"not required for AuthzCert
   reduction"*.
2. **Extend `Endorse`** with depth and scope fields. That keeps the import
   faithful, and `Endorse` stays outside reduction.
3. **The profile.** Import level ≥ 1 as a delegation over the name predicate,
   which R-I-04 permits only *"unless an explicit profile says so"*. The amount
   becomes an attribute.

**Depth, and the 5280 notes' open question 9.** Those notes inferred *"level n
≈ pathLenConstraint n − 1"* from the topic answer and asked for a check against
rfc-9580. Against R-0115 to R-0118, it holds for n ≥ 1:

- level 1 lets the subject's certifications count, and its trust signatures do
  not, which is pathLenConstraint 0: *"no non-self-issued intermediate CA
  certificates may follow"* (rfc-5280, N-145);
- level 2 lets the subject make level-1 introducers, which is pathLenConstraint
  1;
- level 0 corresponds to no `cA`, because the certification itself is the
  end-entity binding.

It differs from X.509 in four ways (derived):

1. **There is no unbounded value.** In X.509, *"Where pathLenConstraint does not
   appear, no limit is imposed."* (rfc-5280, N-145). In SPKI, D = TRUE allows
   re-delegation without limit (rfc-2693#R-0062). In OpenPGP every trust
   signature carries a finite depth, at most 255.
2. **There is no separate boolean.** Level 0 is FALSE. X.509 has a mandatory
   boolean and an optional bound beneath it (the 5280 notes' note 2, item 1).
   OpenPGP has only the bound.
3. **There is no rule for a delegate who over-delegates.** Alice gives Bob
   level 2 and Bob gives Carol level 2. R-0118 says Bob is *"trusted to issue
   level n-1 Trust Signatures"*, that is, level 1. It does not say whether
   Bob's level-2 signature is ignored, or counts as level 1. X.509 takes the
   minimum: the counter *"may be reduced"* and never raised (rfc-5280#R-0414).
   The source does not choose (open question 7).
4. **The temporary-key objection has a partial structural answer.** RFC 2693
   §4.1.4 rejected integers because *"One can always need to go one more level
   down, by creating a temporary signing key"*. In OpenPGP a temporary signing
   key is a **subkey**, bound by the primary key's Subkey Binding signature
   (N-079). That binding is not a certification, so it spends no level. The
   answer covers *data* signing. For certification it rests on an unstated
   premise: R-0123 extends trust to *"signatures by the target key"*, and no
   rule credits a certification made by a certify-capable subkey to its
   primary. X.509's answer is the self-issued exemption, which rests on name
   equality, and the 5280 notes reject it (their reject 6). OpenPGP's answer
   rests on a statement between keys, the shape the 5280 notes' open question
   4 asks for, but only for subkey rotation. The source has no way to replace
   the primary key itself (note 10).

**What this adds to the `contradicts` edge.** There are now three designs on
record:

| family | delegation control | default | source |
|---|---|---|---|
| SPKI | boolean | unstated; rfc-2693 `messages.yaml` reads absence as FALSE (the 2693 notes' open question 13) | rfc-2693#R-0060 |
| X.509 | boolean, plus an optional integer bound under TRUE | absent bound means no limit | rfc-5280, N-145, rfc-5280#R-0161 |
| OpenPGP | a bounded integer only; level 0 is FALSE | absent Trust Signature means level 0 | R-0114 to R-0118 |

R-M-10 reads *"Delegation SHALL be an explicit boolean (or equivalent) on
`AuthzCert`."* If level ≥ 1 is read as TRUE with a bound, OpenPGP's design fits
*"(or equivalent)"*. The source gives no rationale for the integer and no
deployment data. It is a format specification, so it proves that the mechanism
can be specified, not that it works. GnuPG `tsign` and Sequoia `sq pki vouch
authorize` emit it (`record.yaml`, *outside the source*). The 2693 notes side
with RFC 2693 (their reject 2). This file adds evidence and decides nothing.

**The trust amount.** A third axis, which neither SPKI nor X.509 has. The source
gives a scale (R-0119), two recommended values (R-0120), and **no composition
rule**: nothing says what two partial introducers add up to. ARCH-0001 G3 wants
*"Deterministic reduction of authorization chains (SPKI 5-tuple style), not
unbounded WoT path search as the primary algorithm."* So the amount is an
`Endorse` weight that is carried and never reduced (adopt 9, reject 6).

---

## 3. Regular-expression scoping (R-M-08, DEC-004, DEC-008)

**What is constrained.** The Regular Expression is *"Used in conjunction with
Trust Signature packets (of level > 0) to limit the scope of trust that is
extended."* (R-0122). *"Only signatures by the target key on User IDs that
match the Regular Expression in the body of this packet have trust extended by
the Trust Signature subpacket."* (R-0123). The scope is over the **strings a
delegate may certify**. That confirms the `delegation-models` answer's
discriminator: OpenPGP scopes naming authority, as X.509 does, and not
speaking authority.

**The grammar has two definitions.** §5.2.3.22 says *"The Regular Expression
uses the same syntax as Henry Spencer's "almost public domain" Regular
Expression [REGEX] package. A description of the syntax is found in Section
8."* (R-0124). [REGEX] is an informative reference (§16.2, line 7486), and §8
(N-382) restates a grammar of its own. The source does not say which one
governs where they differ (open question 12).

**Four properties of the match, all left open (derived from R-0125 and
N-382).**

1. **Search, not whole-string match.** *"The Regular Expression matches (or does
   not match) a sequence of UTF-8-encoded Unicode characters from User IDs."*
   (R-0125). §8 defines `^` as *"matching the null string at the beginning of
   the input string"* and `$` likewise at the end (N-382). Those anchors mean
   something only under search semantics. So an unanchored `example\.com`
   matches any User ID that contains it, including
   `Eve <eve@evil.example> (example.com)`. The convention
   `<[^>]+[@.]example\.com>$` anchors only the right-hand end. It is vector
   PGP-053222-C01, and per `summary.md` it is the one shape GnuPG supports in
   practice (community reports, *outside the source*).
2. **Characters, not bytes.** `.` matches *"any single Unicode character"*, and a
   range is *"the full list of Unicode characters between them in codepoint
   order"* (N-382). There is no case folding and no normalisation. That agrees
   with the 2693 notes' adapt 1: equality is exact, and any normalisation
   happens at authoring. But mail domains are case-insensitive, so a scope over
   mail addresses with no case rule under-matches (derived).
3. **One hop at a time.** R-0123 says which signatures have trust extended by
   *this* subpacket. Nothing says how the expressions along a chain combine.
   Alice makes Bob a meta-introducer scoped to `foo.com`. Bob makes Carol an
   introducer scoped to `.*`. There are two readings:
   - **per hop.** Each expression filters only its own delegate's
     certifications. Carol may then vouch for anything, and Alice's scope has
     widened.
   - **conjunction.** Every expression on the path must match the final User
     ID. That narrows monotonically.

   The source does not choose (open question 7).
4. **No anchoring requirement, no case rule, no chain rule.** Each of these is a
   way for two conforming verifiers to disagree about one certification, which
   is an R-M-05 matter.

**The conjunction reading needs no intersection.** Under it, a verifier tests
one string against each expression on the path. That is the 2693 notes' decision
rule, `AIntersect(A, R) = R` (their adapt 1), in the special case of a request
that is a single value: R = {uid}, and containment is membership in every
scope. Membership needs no closure property, so the 2693 notes' open question 2
does not arise for single-value requests (adapt 3).

It does arise as soon as a narrowed grant must be **written down**: an
attenuated re-issue, or a Certificate Result Certificate (the 2693 notes'
adapt 8). Regular languages are closed under intersection, but the result can
be exponentially larger than its operands. Deciding whether one expression's
language is inside another's is PSPACE-complete, so no known algorithm avoids
exponential worst-case time (*outside the source*, both points: the classical
results for regular expressions, held in no record).

**Against DEC-008's boundary test.** ARCH-0002's proposed answer admits a
key-local rule when a verifier can evaluate it *"totally"*, *"within bounded
resources"*, *"without side effects"* and *"without privilege"*. Two checks
answer differently (derived):

| check | totally | bounded | no side effects | no privilege |
|---|---|---|---|---|
| does this User ID match r? | yes | yes, with an automaton; a backtracking matcher is exponential on some patterns (*outside the source*) | yes | yes |
| is r₂'s language inside r₁'s? | yes | **no** in general (PSPACE-complete; exponential worst case) | yes | yes |

So a §8 expression is a working instance of what DEC-008 calls *"a declarative
constraint language"*. It qualifies for membership tests, and only if the
profile mandates automaton semantics. It is a ready candidate for DEC-008's
first step, *"Write one constraint in the candidate declarative form and reduce
it by hand."*

**DEC-004 option 1 and the D-1 email scenario.** Option 1 is *"SPKI tag
S-expressions as-is (byte-string sets + intersection)"* (ARCH-0001 §7). The
email scenario's scope, `*@foo.com`, is a **suffix**. SPKI's `(* prefix …)`
matches from the left. Option 1 can therefore express the scenario in three
ways, each a profile choice (derived):

- a **structured address**, with domain labels as list elements in reverse
  order: `(mail com foo)`. A grant `(mail com foo)` then admits
  `(mail com foo bob)` by list padding (rfc-2693#R-0151). This is DNS hierarchy order, most
  significant label first, which X.509 gets by matching written names from the
  right (rfc-5280, N-156).
- a `(* set …)` that enumerates addresses, which only works when they are
  known in advance;
- a new suffix form, which RFC 2693 does not have.

The `delegation-models` answer says *"Alice/Bob/Carol is expressible in three of
the four families"*. For SPKI that holds only after the address is
structured, and the answer does not say so (open question 2).

**Criticality: an unknown restriction fails open.** *"When generating this
subpacket, it SHOULD be marked as critical."* (R-0129). The Trust Signature
subpacket carries no such advice. Under §5.2.3.7, an evaluator *"SHOULD ignore
any non-critical subpacket of a type that it does not recognize"* (R-0081).
The two cases come out opposite:

- an evaluator that does not know Trust Signatures ignores the grant, and
  extends no trust. That fails **closed**.
- an evaluator that does not know a non-critical Regular Expression ignores the
  restriction, and extends the trust without its scope. That fails **open**.
  Vector PGP-053222-C03 builds the case: a non-critical expression that lacks
  its terminating zero octet is ignored under R-0127, and the vector's
  derived outcome is *"the Trust Signature then applies without a scope limit"*.

**An unknown grant is safe to ignore, and an unknown restriction is not**
(derived). OpenPGP relies on the issuer to set the critical bit on the
restriction. ARCH-0002 P5 removes the asymmetry: *"unknown is critical unless
declared otherwise"*. This is P5's case, made by the exact feature D-1's email
scenario needs.

**Deployment.** Per `record.yaml`, GnuPG supports one practical shape of
expression, and `dev.gnupg.org` T6238 records that the domain restriction fails
for a User ID with no name part (*outside the source*). That is consistent with
properties 1 and 4 above. When the source does not say what a match is,
implementations converge on one convention, and that convention breaks on a
User ID it did not anticipate.

---

## 4. Where trust starts (R-I-02, `AclEntry`)

**Where the source agrees with us.** The root is local, unexported and not
specified:

- *"The Trust packet is used only within keyrings and is not normally exported.
  Trust packets contain data that record the user's specifications of which
  keyholders are trustworthy introducers, along with other information that
  implementation uses for trust information. The format of Trust packets is
  defined by a given implementation."* (§5.10, N-310);
- *"Trust packets SHOULD NOT be emitted to output streams that are transferred
  to other users"* (R-0224), and *"they SHOULD be ignored on any input other
  than local keyring files."* (R-0225);
- keyrings are out of scope: *"It is beyond the scope of this specification to
  discuss the details of keyrings or other databases."* (§3.6, line 621), as is
  *"key storage and management"* (§2, line 439).

This matches ARCH-0001's `AclEntry`, *"unsigned; issuer = `Self`"*, *"Local
policy root"*, and ARCH-0002's *"a set of trust roots **you chose yourself**"*.
The topic answer's claim that ARCH-0001's unsigned local root *"is therefore NOT
a departure"* is confirmed for OpenPGP.

**Where it differs.**

1. **OpenPGP has two local forms, and we have one.** Besides the
   implementation-defined Trust packet there is the **signed but local** certification:
   *"Non-exportable, or "local", certifications are signatures made by a user
   to mark a key as valid within that user's implementation only."* (§5.2.3.19,
   N-150). Locality is enforced at both ends of a transfer. On export *"any
   local certification signatures are deleted from the key"* (R-0110), the
   receiver *"likewise trims any local certifications"*, and key servers
   *"always trim local certifications from any key they handle"* (N-151).
   And *"When an implementation generates this subpacket and denotes the
   signature as non-exportable, the subpacket MUST be marked as critical."*
   (R-0111), so an implementation that does not know the subpacket does not
   honour the signature as a valid certification: a SHOULD (R-0080), and a
   MUST when the subpacket is in the hashed area (R-0178). Criticality
   governs evaluation, not transfer: such an implementation cannot know to trim
   it, and the bytes can still travel.

   Natively, a signed local statement buys nothing, because the verifier
   already trusts its own store, and `AclEntry` suffices (reject 13). What
   carries over is the mechanism for keeping a statement local. Both ends trim
   it, and the marker is must-understand, so an old implementation that passes
   it on has never treated it as valid.
2. **The root's format is the implementation's.** Ours is specified: the 2693
   notes' adapt 6 and the 5280 notes' adapt 4. The topic answer's *"the
   difference is that ours is specified"* holds for OpenPGP as well.

**R-I-02 holds by construction.** R-0225 is R-I-02 stated by the foreign format
itself. An imported Trust packet is never honoured, so an OpenPGP trust root
never crosses the import boundary. What does cross is trust signatures, and each
one is a statement by its issuer's key. An imported level-1 signature by Alice
empowers nobody until a native `AclEntry` empowers Alice, or empowers the
importer that vouches for the translation (derived; the 2693 notes' adapt 7).

**The amount is not local, and the combination is.** The matrix says *"trust
values are local to importer"*. Trust packets are local, but trust-signature
amounts are exported by default (R-0109), and signed wherever they sit in the
hashed area (derived). Only their combination is local, because no combination rule exists (note 2). The matrix note should say
*"trust amounts are carried; how to combine them is local to the importer"*
(open question 3).

---

## 5. Revocation against R-O-02

R-O-02 reads *"Short-lived validity preferred over revocation-heavy design;
revocation still representable."*, at priority S.

**What the source provides.** Revocation is a signed, single, positive
statement by the issuer:

- **Three revocation types.** A Key Revocation (0x20) *"is calculated directly
  on the key being revoked"*, and *"A revoked key is not to be used."* (N-082,
  R-0050). The Subkey Revocation (0x28) is its counterpart for a subkey
  (R-0052). A Certification Revocation (0x30) *"revokes an earlier User ID
  certification signature (Type IDs 0x10 through 0x13) or Direct Key signature
  (Type ID 0x1F)"* (N-084).
- **Who may revoke.** For a key: *"Only Revocation Signatures by the key being
  revoked, or by a (deprecated) Revocation Key, should be considered valid
  Revocation Signatures."* (R-0051). For a certification: *"It should be issued
  by the same key that issued the revoked signature or by a (deprecated)
  Revocation Key."* (R-0054). Both are lowercase. §10.1.5 repeats the rule for
  keys: Revocation Signatures *"are only accepted if they are issued by the key
  itself or by a key that is authorized to issue revocations via a Revocation
  Key subpacket"* (N-428).
- **Reasons, with different consequences.** *"If a key has been revoked
  because of a compromise, all signatures created by that key are suspect.
  However, if it was merely superseded or retired, old signatures are still
  valid."* (R-0149). The codes are in Table 10 (N-187). An implementation
  *"SHOULD implement this subpacket, include it in all Revocation Signatures,
  and interpret revocations appropriately."* (R-0148).
- **Explicit targets.** The Signature Target subpacket, *"For Revocation
  Signatures, … provides explicit designation of which signature is being
  revoked."* (R-0154).
- **Irrevocable signatures.** *"Signatures that are not revocable ignore any
  later Revocation Signatures. They represent the signer's commitment that its
  signature cannot be revoked for the life of its key."* (§5.2.3.20, N-153;
  R-0112).

**Delegated revocation is deprecated, and escrow replaces it.** *"This
mechanism is deprecated. Applications MUST NOT generate such a subpacket."*
(§5.2.3.23, R-0131). *"An application that wants the functionality of
delegating revocation can use an escrowed Revocation Signature."* (N-162). §13.9
gives the pattern: Alice produces *"a specific Revocation Signature (Signature
Type ID 0x20, 0x28, or 0x30) and distribute[s] it securely to a preferred
revoker who can hold it in escrow"* (N-541). It lists six advantages over the
Revocation Key (N-542):

1. *"The keyholder can constrain what types of revocation the preferred revoker
   can issue, by only escrowing those specific signatures."*
2. *"There is no public/visible linkage between the keyholder and the preferred
   revoker."*
3. *"Third parties can verify the revocation without needing to find the key of
   the preferred revoker."*
4. *"The preferred revoker doesn't even need to have a public OpenPGP Key if
   some other secure transport is possible between them and the keyholder."*
5. *"Implementation support for enforcing a revocation from an authorized
   Revocation Key subpacket is uneven and unreliable."*
6. *"If the fingerprint mechanism suffers a cryptanalytic flaw, the escrowed
   Revocation Signature is not affected."*

And: *"A Revocation Signature may also be split up into shares and distributed
among multiple parties, requiring some subset of those parties to collaborate
before the escrowed Revocation Signature is recreated."* (N-543).

**This is the revocation model the 5280 notes asked for, already deployed.**
Their adapt 5 wanted a single revocation statement, signed by a key the revoked
statement names, so that it can be escrowed. That is OpenPGP's revocation
signature: issuer-signed, about one key, binding or certification, positive,
and signable in advance.
Escrow then needs no new mechanism. It is a *use* of the ordinary revocation
statement, not a new object.

Advantage 3 is the architecturally important one. Verifying an escrowed
revocation needs only its issuer's key, not the preferred revoker's, so the
revoker never enters the trust computation. The escrow holder holds a **capability by possession**: it can
publish, and it cannot forge or widen (derived).

**The threshold variant is a k-of-n release control, not a k-of-n signer**
(N-543). The parties reconstruct bytes that already exist. None of them is a
principal in the model (derived). For R-M-06 this is a second kind of
threshold. It governs *who may release* a statement, not *who must sign* it, and
it needs no threshold principal. Once reconstructed, the signature can be
published by anyone who holds it.

**Hard and soft revocation rest on a time the signer asserts.** A revocation for
superseded or retired leaves *"old signatures"* valid (R-0149). "Old" can only
mean old by Signature Creation Time, which *"MUST be present in the hashed
area"* (R-0101) and is whatever the signer wrote. Two cases follow (derived):

- a **compromised** key can backdate. So compromise must cast doubt on
  everything, and R-0149 calls every signature *"suspect"*.
- a **soft** revocation is safe only while the key is uncompromised. If it is
  later found compromised, the soft revocation's split between old and new
  signatures is untrustworthy.

For an `ArtifactStatement` checked years later (G5), "was this signed before the
revocation?" needs evidence the signer cannot forge: a timestamp or a SCITT-style
receipt (R-O-04). That is the 5280 notes' open question 6 again, and the
Timestamp Signature (0x40) is OpenPGP's one-sentence gesture at it: *"This
signature is only meaningful for the timestamp contained in it."* (N-085).

**Which certification does a 0x30 revoke?** *"The signature is computed over
the same data as the certification that it revokes, and it should have a later
creation date than that certification."* (R-0055). Without a Signature Target,
a Certification Revocation identifies its target only by the data it is
computed over, the key and, for a certification, the User ID (a 0x30 also
revokes Direct Key signatures, N-084), plus its issuer. So it revokes every
earlier certification by that issuer on that binding, or the most recent one,
or the source does not say which (open question 8). The Signature Target names
the target by *"1 octet public key algorithm, 1 octet hash algorithm, N octets
hash"* (N-195), but what the hash is computed over is not stated: *"All
arguments are an identifier of that target signature."* (§5.2.3.33, line 2686;
open question 12).

**Validity: unbounded by default, and "latest wins".**

- Defaults run against R-O-02. For a signature, *"If this is not present or has
  a value of zero, it never expires."* (R-0107), and the same holds for a key
  (R-0104).
- A key's expiration lives in a self-signature, and *"An implementation that
  encounters multiple self-signatures on the same object MUST select the most
  recent valid self-signature and ignore all other self-signatures."* (R-0095).
  A keyholder extends a key by issuing a newer self-signature. So an expired key
  can come back, and the verdict depends on which self-signatures the verifier
  holds.
- The source knows the attack. Requiring a Direct Key signature for v6 keys
  *"prevents certain attacks where an adversary strips a self-signature
  specifying a Key Expiration Time or certain preferences"* (§5.2.3.10, line
  2126; R-0098). Stripping a *newer* self-signature still works. It brings back
  an older one, whose expiration or preferences the keyholder had replaced.

R-M-05 asks for determinism *"given an ordered cert set and ACL"*. "Latest
wins" is deterministic given the set, and an adversary who controls delivery
controls the set. RFC 2693's objection to *"wandering anti-matter CRLs"* (the
2693 notes' adopt 5) applies to supersession as much as to revocation (derived).
Natively, each statement fixes its own validity, a renewal is a new statement,
and nothing supersedes a statement except a revocation (reject 7).

**Irrevocable signatures.** Against R-O-02's *"revocation still
representable"*, a statement that *"ignore[s] any later Revocation
Signatures"* (R-0112) is a design that forgoes revocation. The source does not
say how it interacts with a Key Revocation for compromise, which makes
*"all signatures created by that key"* suspect (R-0149; open question 8). Short
validity expresses the same commitment without a flag (reject 8).

---

## 6. Key identity: fingerprints (R-M-02, R-O-01, DEC-003)

**What the source has.** *"A version 6 fingerprint is the 256-bit SHA2-256 hash
of the octet 0x9B, followed by the 4-octet packet length, followed by the
entire Public Key packet starting with the version field. The Key ID is the
high-order 64 bits of the fingerprint."* (§5.5.4.3, N-263). The hashed fields
are version, creation time, algorithm, a 4-octet key-material length and the
material (N-264). Fixture `A.3.1-direct-key-sig-hashed-data.annotated.txt`
shows the same framing at offsets 0x20 to 0x4e, inside a signature's hash
input. Version 4 uses SHA-1 and a 2-octet length (N-261, N-262).

**DEC-003, *"Must specify: canonical key bytes before hashing"*.** OpenPGP v6 is
a complete, deployed answer, and it settles three of DEC-003's sub-questions:

1. **The algorithm is inside the hashed bytes** (field d of N-264). This agrees
   with ARCH-0001's `Key`, *"Public key material + algorithm identifier"*. The
   5280 notes found the opposite in X.509's SKI method (1), which hashes the
   bare key bits (their DEC-003 row). Adopt 4.
2. **The input is framed.** A fixed first octet and an explicit length precede
   the body. That is domain separation, and §5.2.4 depends on it: a v6
   signature over a key hashes *"the salt and then octet 0x9B, followed by a
   4-octet length of the key, followed by the body of the key packet"*
   (R-0168), which is the fingerprint input after the salt. Adopt 4.
3. **The digest algorithm is fixed by the key version**, not parameterized
   (N-258). ARCH-0001's `KeyId` is a *"Digest of a canonical key encoding
   (algorithm of digest is parameterized)"*. OpenPGP changes its digest only
   through a new key version, which needs an RFC (N-566). The cost shows in
   §13.1: *"an OpenPGP implementation cannot completely discard the SHA-1
   algorithm, because it is required for implementing version 4 public keys"*
   (N-516). A version-4 identity is a SHA-1 identity for as long as it exists.
   If our digest is parameterized, the KeyId must say which digest it uses.
   OpenPGP's Issuer Fingerprint does that with its version octet (N-198,
   R-0159). Adapt 4.

**Where it departs from R-M-02.** The creation time is hashed. So *"since a
version 4 fingerprint is constructed by hashing the key creation time along
with other things, two version 4 keys created at different times yet with the
same key material will have different fingerprints."* (§14, N-553), and *"if
version 3, version 4, and version 6 format keys share the same RSA key
material, they will have different Key IDs as well as different fingerprints"*
(§5.5.4.3, line 3412). R-M-02 says *"A principal MAY be identified solely by key
or key digest"*. An OpenPGP fingerprint identifies a key *as packaged*, not a
key. On import, our KeyId is computed by our rule from the material and the
algorithm, and the OpenPGP fingerprint travels as provenance (reject 10;
adapt 9).

**Short identifiers.** *"Implementations SHOULD NOT assume that Key IDs are
unique."* (R-0005). For keys of a version greater than 4, the Issuer Key ID *"MUST NOT
be included in the signature"* (R-0103). §14.1 forbids mapping any part of a
v6 fingerprint into a constrained field such as a 20-octet one, unless that
field's own specification says how (R-0420). Reject 11.

**R-O-01: the issuer is established by verification, not read from a field.**
R-O-01 reads *"Every signed object SHALL have an issuer key that can be
specified as `KeyId`."* In OpenPGP, the issuer fingerprint is only a SHOULD:
*"This subpacket SHOULD be included in all signatures."* (R-0157). It may be in
the unhashed area, and an implementation *"MAY synthesize an Issuer Fingerprint
subpacket and store it in the unhashed section"* (R-0417). So the WP4
translator must take the issuer's KeyId from the key that actually verified the
signature. The 5280 notes reach the same rule for X.509's AKI (their R-O-01
row).

**Fingerprints are for machines.** *"An OpenPGP implementation should prioritize
mechanical fingerprint transfer and comparison where possible and SHOULD NOT
promote manual transfer or comparison of full fingerprints by a human unless
there is no other way to achieve the desired result."* (R-0404). That is
the split proposed R-O-05 makes: *"Any human-facing form SHALL be regenerated
from verified canonical bytes."* Identity is bytes, and the human-facing form is
derived from them, never compared.

---

## 7. What gets signed: R-O-05 and P5

R-O-05 (proposed) reads *"The signed payload SHALL be the canonical encoding
verbatim, carried with an authenticated type indicator. A verifier SHALL verify
the signature before decoding and SHALL NOT canonicalize input as part of
verification. Any human-facing form SHALL be regenerated from verified canonical
bytes."* RFC 9580 is evidence for each clause, mostly by counterexample.

**1. The signed bytes exist only as a reconstruction.** A v4 or v6 signature
hashes the signed data, then the signature fields *"through the end of the
hashed subpacket data and a final extra trailer"* (R-0175, N-211). For a
certification, the signed data is the key and the User ID, re-framed with
prefix octets: 0x9B and a 4-octet length for a v6 key (R-0168), then 0xB4 and a
4-octet length for the User ID (R-0172). Neither is inside the Signature packet.
*"Each Signature packet is calculated on the immediately preceding User ID
packet and the initial Public Key packet."* (§10.1.5, N-423). A verifier must
parse the packet sequence to know what the signature is over, before it can
verify anything. Fixture A.3.1 is such a reconstructed stream.

For the WP4 translator this is unavoidable. Natively, it is what R-O-05
excludes. A native statement carries its own subject inside its signed bytes
(derived).

**2. Canonicalization at verification, and the source's own case against it.**

- Text signatures: *"the implementation MUST first canonicalize the document by
  converting line endings to <CR><LF>"* (R-0166).
- Cleartext signatures: *"any trailing whitespace -- spaces (0x20) and tabs
  (0x09) -- at the end of any line is removed before signing or verifying a
  cleartext signed message."* (R-0266). Dash-escaping is undone first: *"The
  message digest is computed using the cleartext itself, not the dash-escaped
  form."* (R-0272).
- The source then records the cost in §7.3. The framework *"will fail to safely
  round-trip any textual stream that may include semantically meaningful
  whitespace"* (line 4552). *"it will be difficult for any human reading the
  message to know which part is covered by the signature"* (line 4563). It
  advises *"An implementation that knows it is working with a textual stream
  with any of the above characteristics SHOULD NOT use the Cleartext Signature
  Framework."* (R-0275).

That is DSSE's argument for R-O-05, made by the incumbent from experience
(adopt 6).

**3. An authenticated type indicator, done well, from a registry.** The
Signature Type ID and version are inside the hashed data. The trailer
separates versions: *"The data actually hashed by OpenPGP varies depending on
the signature version, in order to ensure that a signature made using one
version cannot be repurposed as a signature with a different version over
subtly different data."* (§5.2.4.1, N-213). That is the property R-O-05's
*"authenticated type indicator"* exists for (adopt 7). The indicator itself is a
value in an IANA registry (Table 4, N-071), allocated under Specification
Required (N-565). ARCH-0002 P1 makes it key-relative natively (reject 2).

**4. An unsigned region inside a signed object.** *"The second set of
subpackets (the "unhashed section") is not cryptographically protected by the
signature and should include only advisory information."* (R-0077). *"If a
subpacket is not hashed, then the information in it cannot be considered
definitive because it is not covered by the cryptographic signature."* (N-126).
§13.13 gives the attack: a preference found unhashed *"would open itself to an
attack where the recipient's certificate is tampered with to encourage the use
of a specific cipher or mode of operation."* (N-551). The rule
*"an implementation SHOULD ignore them when they are found with unknown
provenance in the unhashed section"* (R-0418) is a patch, and it covers only
*"Some subpackets"*.

Natively, a statement has no unsigned fields. Local annotations about a
statement live outside it, in the verifier's store (reject 3).

**5. Criticality is opt-in for subpackets, and that is P5's failure mode.**
*"Bit 7 of the encoded Subpacket Type ID is the "critical" bit."* (R-0079).
The rules are SHOULDs:

- *"If a subpacket is encountered that is marked critical but is unknown to the
  evaluating implementation, the evaluator SHOULD consider the signature to be
  in error."* (R-0080);
- *"An implementation SHOULD ignore any non-critical subpacket of a type that it
  does not recognize."* (R-0081).

The issuer must ask for criticality one subpacket at a time:

| subpacket | rule |
|---|---|
| Signature Creation Time, Key Expiration Time, Signature Expiration Time | SHOULD be critical (R-0102, R-0105, R-0108) |
| Regular Expression | SHOULD be critical (R-0129) |
| Key Flags | SHOULD be critical (R-0145) |
| Intended Recipient Fingerprint, in a v6 signature | SHOULD be critical (R-0163) |
| Exportable Certification, when it says non-exportable | **MUST** be critical (R-0111) |
| a notation | *"the criticality applies to that specific notation"* (N-172) |
| Trust Signature | no advice |

The **packet** layer is stricter. Criticality is fixed by the Type ID range,
*"Packets with Type IDs from 0 to 39 are critical."* (§4.3), and enforced with
MUSTs: an unknown critical packet means the implementation *"MUST reject the
whole packet sequence"* (R-0032), and *"an unknown non-critical packet MUST be
ignored"* (R-0033). That is criticality decided once, when the type is
allocated, rather than by each issuer for each instance.

The source also records what the late arrival cost: *"implementations of
the previous versions may reject unknown non-critical packets or accept unknown
critical packets"* (§10, line 5170). Once a default has shipped, criticality
cannot be fixed afterwards. That supports P5's choice to make must-understand
the default from the first version (adopt 5).

**6. Conflicts resolved by the receiver, on purpose.** *"In most cases, an
implementation SHOULD use the last subpacket in the hashed section of the
signature, but it MAY use any conflict resolution scheme that makes more
sense."* (R-0086). The source explains: *"the ambiguous language here allows a
receiver to be generous in what they accept, while putting pressure on a
creator to be stingy in what they generate."* (N-127). Two conforming verifiers
may read one signature differently (R-M-05). Under P5, two copies of one field
are invalid, as duplicate map keys are in CBOR (row 10 of the rfc-8949 notes'
option 5 decision table).
Reject 4.

**7. A bad statement is ignored, never repaired, and never fatal to the set.**
For malformed or unknown signatures:

- *"it MUST ignore the signature for validation purposes"* (R-0178);
- *"It MUST NOT indicate a successful signature validation for such a
  signature."* (R-0179);
- *"it MUST NOT halt processing on the packet stream or reject other signatures
  in the same packet stream just because an unknown or invalid signature
  exists."* (R-0180).

This fits our verifier, which reasons over a *set* of statements. A statement
that fails any P5 level is rejected, never repaired, and the rest of the set is
still evaluated (adopt 8).

**8. The signed hash is not a content identifier.** Every v4 and v6 signature
hashes the document and then the signature fields *"through the end of the
hashed subpacket data and a final extra trailer"* (R-0175), and a v6 signature
first feeds in a salt (R-0164). So the digest any OpenPGP data signature signs
is not a digest of the document. A WP4 translator cannot produce R-M-07's
content digest from a data signature without the document itself (derived;
open question 4). The salt's purpose is in note 12.

---

## 8. Notations and private ranges against R-M-12, ADR-0001 and P1

**What the source has.** Notation Data is the one namespaced extension point in
a signature. *"Notations can be used for any extension the issuer of the signature
cares to make."* (N-165). Names come in two namespaces:

- *"Notation names are arbitrary strings encoded in UTF-8. They reside in two
  namespaces: the IETF namespace and the user namespace."* (N-167);
- *"The IETF namespace is registered with IANA. These names MUST NOT contain the
  "@" character (0x40)."* (R-0137). The registry has *"No registrations at this
  time."* (N-168);
- *"Names in the user namespace consist of a UTF-8 string tag followed by "@",
  followed by a DNS domain name."* (N-169);
- *"Names in a user space are owned and controlled by the owners of that domain.
  Obviously, it's bad form to create a new name in a DNS space that you don't
  own."* (N-170).

**This is a near miss for P1, and it stops one step short.**
ARCH-0002 P1 makes every extension point *"a pair: **`(defining key, local
label)`**"*. OpenPGP's user namespace is a pair too, `(DNS domain, local tag)`,
and it does better than private-use ranges, because the namespace has an owner.
But three things separate it from P1 (derived):

1. **The owner is a DNS registrant, not a key.** The namespace is rooted in the
   DNS, which is a global registry, one level up.
2. **Nothing binds a name to its owner.** Any key can sign a notation named
   `x@example.com`. Ownership is enforced by *"bad form"*, which is etiquette.
3. **The meaning lives nowhere the verifier can reach.** The source suggests
   *"implementers MAY wish to arrange for that address to reach a person who can
   be consulted about the use of the named tag"* (R-0139). In P3's terms the
   schema is a mailbox.

Under P1 the defining key *is* the namespace, so naming a type is something only
that key can do. Its meaning is a P3 schema that the key publishes (adopt 3).

**The private ranges, in the source's own words.** *"S2K Specifiers, Signature
Subpacket Type IDs, User Attribute Subpacket Type IDs, image format IDs, and the
various algorithm IDs described in Section 9 all reserve the range 100 to 110
for Private and Experimental Use."*, and *"However, implementations need to be
careful with these and promote them to full IANA-managed parameters when they
grow beyond the original, limited system."* (§12.10, N-507).

ADR-0001 rejected private use because *"private use gives escape from a
registry, not a namespace"*, and two parties using one private label *"collide
with nothing to disambiguate them, because no principal is attached"*. RFC 9580
implies the risk and prescribes the cure P1 rejects: once a private value
grows, move it to the central registry. That is evidence for ADR-0001 from
inside an incumbent.

**The rest of OpenPGP's extension surface is registry-governed.** All
registries in the protocol group use Specification Required (N-565). Packet
types, fingerprint versions, encrypted message versions, and key and signature
versions use RFC Required (N-566). §12.11 asks extension proposals to declare
themselves in the Features subpacket or to explain why not, and otherwise
*"the proposal SHOULD be rejected"* (R-0401).

**On import (derived).**

- A user-namespace notation becomes a foreign label carried as an attribute,
  lossy per R-I-01. ADR-0001: *"Registry identifiers **may** appear at
  interchange boundaries, and such mappings are documented as lossy per
  R-I-01."*
- A **critical** notation that the translator does not understand makes the
  signature an error (R-0080), and P5 makes it a rejection. It must never be
  translated with the notation dropped.
- Policy URI (*"a URI of a document that describes the policy under which the
  signature was issued"*, N-179) and Preferred Key Server (N-176) are global
  locators. Under the proposed R-M-11 a locator is *"non-authoritative evidence
  about a subject, not … its definition"*. They are carried as provenance or
  dropped.

---

## 9. One signature form, many meanings (P2, P3, P6)

**The source is candid that its meanings are vague.** *"Please note that the
vagueness of these meanings is not a flaw but rather a feature of the system."*
(§5.2.1, line 1489). Three instances:

1. **One type, three predicates.** A binary signature *"means the signer owns
   it, created it, or certifies that it has not been modified."* (N-072). A
   verifier cannot tell which of the three was meant.
2. **Assurance levels that nobody populates.** The four certification types run
   from *"has not done any verification"* (0x11, N-076) to *"has done
   substantial verification"* (0x13, N-078). Then: *"Most OpenPGP
   implementations make their "key signatures" as generic (Type ID 0x10)
   certifications. Some implementations can issue 0x11-0x13 certifications, but
   few differentiate between the types."* (§5.2.1.7, line 1581). This is a
   cautionary precedent for any confidence or assurance field we add.
3. **Meaning that depends on the speaker.** Key Flags *"mean different things
   depending on who is making the statement. For example, a certification
   signature that has the "sign data" flag is stating that the certification is
   for that use. On the other hand, the "communications encryption" flag in a
   self-signature is stating a preference that a given key be used for
   communications."* (§5.2.3.29, N-182). And on telling "communications" from
   "storage": *"This decision is left wholly up to the implementation"* (line
   2549).

**Against P3 and P2.** ARCH-0002 P3 makes a type a schema carrying *"semantic
descriptions"*. Instances 1 and 3 are what a type without one looks like. In
P2's terms, *A says B has C*, instance 3 is the relation between A and B. When
A = B the flags are a preference. When A ≠ B they are a scope on A's claim.
One predicate type has two meanings, chosen by the speaker relation. The lesson
for our schemas: a predicate type's meaning must not depend on whether the
speaker is also the subject. If it must, that is two types (adapt 8).

**Where OpenPGP already has P2's shapes (derived).**

- **P6, a name as an attested string.** *"The self-signature is a statement, "My
  name X is tied to my signing key K", and it is corroborated by other users'
  certifications."* (§5.2.3.10, N-132). A self-signature is *A says A has name
  X*, and a third-party certification is *C says A has name X*.
- **A statement with no subject.** A Standalone Signature *"is a signature of
  only its own subpacket contents."* (N-074). With notations as the claim, it is
  the closest OpenPGP comes to P2's general form.
- **A statement about a statement.** A Third-Party Confirmation is *"a signature
  over another OpenPGP Signature packet. It is analogous to a notary seal on the
  signed data."* (N-086), and it *"SHOULD include a Signature Target subpacket
  that identifies the confirmed signature"* (R-0056). It imports as an
  `ArtifactStatement` whose subject digest identifies a statement, which
  satisfies R-M-07.
- **A role under one key.** Signer's User ID lets *"a keyholder to state which of
  their roles is making a signature"* (N-185). Under P2 the speaker is the key,
  so a role is a claim the key makes, carried as an attribute.

**"Weak authorization language", qualified.** ARCH-0001 §3.1 calls OpenPGP's
authorization language weak, and the topic answer says OpenPGP *"cannot get
near"* scoping by purpose *"because it has no authorization field"*. The source
has two partial ones:

- **Key Flags in a certification** scope that certification's use (N-182, the
  "sign data" example). The vocabulary is fixed and small (N-181): certify,
  sign, two kinds of encryption, authentication, and two advisory flags.
- **A critical notation** in the hashed area can carry any claim, with
  must-understand semantics (N-172). Its meaning is held outside the standard,
  like an X.509 policy OID (the 5280 notes' note 6).

Neither one composes with a trust signature in the source. Nothing says that
Key Flags on a level-1 certification limit what the introducer's own
certifications are for (open question 2).

**Two senses of "valid".** The source uses "valid" for a signature that
verifies (R-0179) and for a key accepted by *"validity calculations"* (R-0151).
It never defines the second. R-O-06 (proposed) asks a verifier to report name
resolution, authorization reduction and statement acceptance separately, and
our vocabulary has to keep them apart too.

---

## 10. Subkeys: a principal that is a key set

**What the source has.** A Subkey Binding signature *"is a statement by the
top-level signing key, indicating that it owns the subkey."* (N-079). A
signing subkey must consent: *"A signature that binds a signing subkey MUST have
an Embedded Signature subpacket in this binding signature that contains a 0x19
signature made by the signing subkey on the primary key and subkey."* (R-0049;
again as R-0326). The consenting signature *"is a statement by a signing subkey,
indicating that it is owned by the primary key."* (N-080). In a v6 certificate
*"Every subkey MUST have at least one Subkey Binding signature."* (R-0313), and
*"Every Subkey Binding signature MUST be a self-signature"* (R-0314). Binding
signatures can be revoked (R-0091), and Key Flags on the binding say what the
subkey is for (N-182).

**So an OpenPGP principal is a primary key plus the subkeys it has bound.** The
certificate (§10.1) is that set. ARCH-0001's `Principal` is *"`Key` \| `KeyId`
\| `Name` \| `Threshold` \| `Group`"*, and none of these is a key that speaks
through other keys.

**What a binding is, in our terms (derived).** A Subkey Binding is a statement
by the primary key that subkey S speaks for it, for the usages its Key Flags
name. N-079 says only that the primary key *"owns the subkey"*. That is
`AuthzCert`-shaped: delegation from the primary to the subkey, with the Key
Flags as its tag. It is not an identity signature, so R-I-04 does not govern
it, and the matrix row lists no target for it (open question 5).

**The back-signature is subject consent, which our delegation does not have.**
SPKI and ARCH-0001 let an issuer delegate to any subject without the subject
agreeing. For a *signing* subkey, OpenPGP requires the subkey's own signature
(R-0049). The source gives no reason. The derived one: without it, Alice could
bind Bob's signing key as her subkey, and claim Bob's signatures as hers. A
native delegation that makes the subject *speak for* the issuer has the same
exposure. Does it need the subject's countersignature (open question 5)?

**Why it matters beyond import.** Subkeys answer two questions the sibling notes
left open:

- RFC 2693's temporary-key objection to integer depth (note 2, item 4);
- the 5280 notes' open question 4, *"What is key rollover in our model"*.

OpenPGP's answer to both is a statement between keys, inside one principal, that
counts as no delegation hop. If R-M-10 admits a bound, the native model needs a
statement with the same property.

The two advisory Key Flags are a contrast for R-M-06. *"The private component of
this key may have been split by a secret-sharing mechanism."* (0x10) and *"The
private component of this key may be in the possession of more than one
person."* (0x80) (N-181) are claims nobody can check. R-M-06's threshold
principal is a structure a verifier evaluates.

---

## 11. Encoding: OpenPGP packets against D-3

D-3, in the 2026-09-28 minute, reads: *"DEC-002 — narrow to option 5. CBOR data
model, no IANA tags, COSE as export only; type identity is `(defining key,
label)` per P1; YAML is the human form with a canonical one-way mapping."*

**On the extract skill's D-3 rule.** The skill requires a header-by-header D-3
mapping for COSE, CBOR and envelope documents. RFC 9580 is neither COSE nor CBOR.
But a Signature packet is a signing envelope: a payload reference, an algorithm,
metadata and a signature. The table below is the structure-by-structure mapping
the rule asks for. Its result, as for X.509, is that nothing in the envelope
becomes native. What carries over is ideas, not bytes.

| OpenPGP (§4, §5.2.3, §5.5.4) | D-3 native | mapping |
|---|---|---|
| packet header: Packet Type ID from an RFC Required registry (N-566); critical by range 0–39 (§4.3) | a statement whose type is `(defining key, label)` | **Excluded natively** (P1). On import, the type ID is parsed and discarded. |
| lengths: 1-, 2- or 5-octet, and partial body lengths (§4.2.1) | CBOR definite lengths | Partial body lengths are OpenPGP's indefinite length, and the rfc-8949 notes have option 5 reject indefinite lengths in decoding (row 3 of their option 5 decision table). No counterpart. |
| *"the length information in each packet header is the canonical source of packet boundaries"* (N-032); a subfield that overruns MUST abort the parse (R-0021, R-0022) | well-formedness of nested CBOR items | **Same rule in substance:** an inner length that exceeds its container is malformed, never truncated. CBOR has this as well-formedness (P5's first level). |
| Signature: version, type, public-key algorithm, hash algorithm, hashed subpackets, unhashed subpackets, hash prefix, v6 salt, MPIs (§5.2.3) | a signed statement: canonical bytes plus a signature (R-O-05, proposed) | **Shape only.** The signed bytes are reconstructed (note 7, item 1), so they cannot be re-attached to a native statement. Translation produces a new statement, signed by the importer, with the OpenPGP packets kept as evidence by digest. |
| Signature Type ID and version, hashed, with a version trailer (N-213) | *"an authenticated type indicator"* (R-O-05, proposed) | **Same intent, registry identifier** (Table 4, N-071). Natively key-relative (P1). |
| hashed subpacket area | the statement's map | Each subpacket goes to a native field (`Validity`), an attribute, provenance, or is dropped, per adapt 9's table. |
| unhashed subpacket area (R-0077) | none | **Not carried.** A native statement has no unsigned region (reject 3). |
| critical bit, per subpacket (R-0079) | P5: must-understand by default | **Inverted.** The bit has no native counterpart. |
| *"use the last subpacket"* on conflict (R-0086) | duplicate keys are invalid | **Inverted** (reject 4). |
| time fields: *"an unsigned 4-octet number containing the number of seconds elapsed since midnight, 1 January 1970 UTC"* (N-013) | `Validity { not_before?, not_after?, online_check? }`; the time representation is DEC-002's | **Exact on import, with a horizon.** Four unsigned octets run out in 2106 (derived). Expirations are offsets from creation, though the source labels them *"(4-octet time field)"* (messages.yaml SD-M05), so import adds them to get an absolute `not_after`. Zero or absent means none (R-0104, R-0107; open question 9). |
| fingerprint: version-framed SHA2-256 over the key packet (N-263, N-264) | `KeyId` per DEC-003 | **Not reused** (note 6). Carried as provenance. |
| MPIs and native-format key material (§3.2, §5.5.5) | byte strings | Exact. An MPI's bit-length prefix is dropped once checked (R-0003). |
| User ID: *"UTF-8 text"* with *"no restrictions on its content"* (N-312) | a text string, valid UTF-8 (P5's validity level; row 13 of the rfc-8949 notes' option 5 table) | **May fail validity.** The source does not require a receiver to check the UTF-8. A User ID that is not valid UTF-8 is rejected or carried as bytes, never repaired (open question 9). |
| Regular Expression, with its trailing zero octet (R-0126 to R-0128) | a text string | The terminator is an artefact (*"For historical reasons"*, N-158). It is dropped on import. |
| notation: flags, name, value; the value is text only if the human-readable flag is set (N-165, N-166) | a key-relative label and a value | The name becomes a foreign label (note 8). The value is a text string if flagged, else a byte string. |

**Export.** The matrix gives OpenPGP export as P (partial), and WP4 writes `↔`.
Like SPKI and unlike X.509, an OpenPGP export can be **signed by the native key
itself**, because an OpenPGP issuer is a key, not a name (derived). A native
`NameCert` by key K can become a v6 certification by K, if K's algorithm is one
OpenPGP defines for v6 signatures (§9.1). The export is partial because:

- tags have no OpenPGP form;
- scopes have one only for User-ID regular expressions;
- key-relative types have none, except as user-namespace notations, which are
  DNS-relative (note 8);
- a native KeyId and an OpenPGP fingerprint name the same key differently
  (note 6), so the exporter must build the key packet with a creation time,
  which the native key does not have.

Under D-3, COSE is the export *envelope*. An OpenPGP export is a separate,
foreign-format export under R-I-01, and nothing in it is native.

---

## 12. Security considerations that carry over

| source | bearing on our design |
|---|---|
| [SHAMBLES] is titled *"Sha-1 is a shambles: first chosen-prefix collision on sha-1 and application to the PGP web of trust"* (§16.2, line 7537). *"While the material to be signed could be attacker controlled, hashing the salt first means that there is no attacker-controlled hashed prefix."* (§13.2, line 6372) | The one attack on the web of trust the source cites is a forged **identity certification**. It works when a signer signs content a requester chose, which is what an issuer of `NameCert`s does. The algorithm suite is unfrozen (NG3). Whatever it becomes, the signer should control the first hashed bytes, as v6 salting does (adapt 7). |
| *"Choosing a new random salt for each signature ensures that no repeated signatures are produced"* (N-520) | Signatures over identical payloads differ. A statement's identifier must therefore be the digest of its **payload**, never of its signature bytes (adapt 6). |
| *"Verifiers should be aware that even if the signer used a strong hash, an attacker could have modified the signature to use a weak one."* (N-513), and §5.2.5 treats *"A hash algorithm known to be weak (e.g., MD5)"* as a malformed signature (line 2867; R-0178) | Authenticating the algorithm octet does not help: v4 and v6 already hash it (N-211), and the attacker works over data that names the weak algorithm. The source's remedy is verifier policy, *"Only signatures using acceptably strong hash algorithms should be accepted as valid"* (N-513). Natively, algorithm acceptance belongs in DEC-008's fixed core, never in issuer-chosen fields (derived). |
| *"an OpenPGP implementation cannot completely discard the SHA-1 algorithm, because it is required for implementing version 4 public keys"* (N-516) | An identifier whose digest is fixed by format version keeps a weak hash alive. KeyIds must say which digest they use (adapt 4). |
| self-signature stripping (§5.2.3.10, line 2126; R-0098) | Supersession by "most recent" is suppressible (note 5; reject 7). |
| signature transplant: a verifier *"MAY choose to only accept a signature from a key that has a valid self-signature over a User ID that matches the message's From: header, as a way to avoid a signature transplant attack."* (R-0100) | A signature that does not name its context can be moved to another one. Native statements carry their subject inside the signed bytes (note 7, item 1). |
| surreptitious forwarding (§13.12, N-548, R-0416); Intended Recipient Fingerprint (R-0161) | The native model signs statements, not messages, and a statement is meant to be passed on. No counterpart is needed, and the subpacket is dropped on import. Recorded so that its absence reads as a decision. |
| *"If a subpacket is not hashed, then the information in it cannot be considered definitive"* (N-126); §13.13 (N-549 to N-551) | No unsigned fields (reject 3). |
| *"An OpenPGP implementation SHOULD limit the number of layers of compression it is willing to decompress in a single message."* (R-0419) | DEC-008's *"within bounded resources"* applies to decoders as well as to key-local rules. Nesting depth needs a fixed bound. |
| fingerprint usability (§13.6, R-0404); *"the topic of interoperable human-in-the-loop key verification needs more work"* (line 6497) | Identity is bytes, and rendering is P3's (note 6). Human key verification is unsolved in the incumbent too. |
| escrowed revocation (§13.9, N-540 to N-543) | Note 5; adopt 2. |
| a key that is both signing and encryption: *"Using a single key for encrypting and signing is discouraged."* (N-512) | Encryption is outside the native model. A native key is a signing key. |

---

## 13. What we adopt

Each item gives one line of evidence. The analysis is in the note cited.

1. **Revocation as a single, positive statement signed by the revoked
   statement's issuer**, with a reason (R-0051, R-0054, R-0148, R-0154;
   note 5). This is the 5280 notes' adapt 5, already deployed.
2. **Escrowed revocation, with no delegated-revocation object.** It is
   escrow-capable because the issuer signs (R-0131, N-162, N-541, N-542). Its
   verification needs only the revoked key (N-542, advantage 3; note 5).
3. **An extension name is a pair of an owner and a local tag** (N-169, N-170).
   We adopt OpenPGP's user-namespace shape, with the key as owner in place of
   the DNS domain, which is P1 (note 8).
4. **The algorithm and a framing prefix are inside the hashed key bytes** (N-264,
   R-0168; note 6). This answers part of DEC-003's *"canonical key bytes before
   hashing"*.
5. **Criticality decided once, when a type is defined, not by each issuer** —
   the packet layer's rule (§4.3, R-0032, R-0033; note 7, item 5). This is P5
   with the source's own history behind it (§10, lines 5168–5172).
6. **No canonicalization during verification.** §7.3 is the incumbent's own case
   (R-0166, R-0266, R-0275; note 7, item 2). Evidence for R-O-05.
7. **Domain separation of the signed bytes by statement type and format
   version** (N-213, R-0176, R-0177; note 7, item 3). This is R-O-05's
   authenticated type indicator.
8. **A bad statement is ignored, never reported as valid, and never stops
   evaluation of the rest of the set** (R-0178 to R-0180; note 7, item 7).
9. **Trust amount as a carried `Endorse` weight** (R-0119; note 2). This is
   ARCH-0001 §4.2's *"weight w"*, sourced.
10. **Identifiers are full digests, compared mechanically** (R-0005, R-0103,
    R-0404, R-0420; note 6).
11. **The local root is local input, and a foreign trust root never crosses
    import** (N-310, R-0224, R-0225; note 4). This agrees with `AclEntry`,
    R-I-02, the 2693 notes' adopt 2 and the 5280 notes' adopt 1.

## 14. What we adapt, and how

1. **Trust signatures as scoped delegation over the name predicate.** Under P2
   and P6, a level ≥ 1 trust signature is *A says K can speak about (names,
   r)*. If WP4 takes the profile route of note 2, its parts are:
   - the level becomes a depth;
   - the Regular Expression becomes a scope;
   - the amount becomes an attribute.

   The minimum v0.1 mapping is `NameCert` plus `Endorse`, with the level and the
   expression listed as dropped under R-I-01 (note 2, option 1). WP4 chooses.
2. **The Regular Expression as a candidate tag profile for the email
   scenario**, completed with what §5.2.3.22 and §8 leave open:
   - the match is anchored at both ends;
   - case and normalisation rules are fixed at authoring, and matching is exact;
   - automaton semantics are mandated;
   - the conjunction reading of chains (note 3).

   This is a candidate for DEC-004 and DEC-008, not a choice.
3. **Check a single-value request against every scope on the path, instead of
   computing intersections** (note 3). This is the 2693 notes' decision rule
   for the single-value case. It needs no closure. Intersections are computed
   only when a narrowed grant must be written down.
4. **A self-describing KeyId.** OpenPGP fixes the digest per key version and
   puts the version octet in the Issuer Fingerprint (N-198, R-0159). If DEC-003
   keeps the digest parameterized, the KeyId carries the digest identifier
   (note 6).
5. **Key binding as a statement between keys that is no delegation hop** (N-079,
   R-0049; note 10). If R-M-10 admits a bound, rollover and temporary keys need
   such a statement. Whether the bound key must countersign is open question 5.
6. **Statement identity is the payload digest.** v6 salting makes signature
   bytes unique per signing (N-520), so a statement is identified by its
   canonical payload, and so is a reference to it. Signature Target's
   *"N octets hash"* (N-195) is the precedent, with what is hashed stated
   (open question 12).
7. **The signer controls the first hashed bytes** (§13.2, line 6372;
   N-518). It is a hashing-discipline rule for whatever suite NG3 eventually
   picks, not an algorithm choice.
8. **A predicate type's meaning must not depend on the speaker relation.** Key
   Flags show what happens otherwise (N-182; note 9). If a self-statement and a
   third-party statement differ in meaning, they are two predicate types.
9. **The import mapping table** for WP4, R-I-01 and R-I-04, as the source makes
   the fields available. This is derived, and WP4 decides.

   | OpenPGP | native | R-I-01 class |
   |---|---|---|
   | Public Key packet (v4, v6) | `Key`. `KeyId` by our rule, never the fingerprint (note 6) | preserved; KeyId inferred |
   | OpenPGP fingerprint, Key ID, key creation time | `provenance: openpgp`, with the certificate's digest | preserved, as provenance only |
   | User ID + self-certification (0x10–0x13 by the key itself) | P6 name statement, speaker = subject | preserved |
   | User ID + third-party certification, level 0 | `NameCert`, speaker = certifier's KeyId | preserved; the 0x11–0x13 assurance distinction is dropped (note 9) |
   | Trust Signature, level ≥ 1 | `Endorse(w = amount)` (option 1), or the profile of adapt 1 | level and expression dropped (option 1), or preserved (profile) |
   | Exportable Certification = 0 | never imported, because both ends trim it (R-0110) | dropped |
   | Trust packet | never imported (R-0225) | dropped |
   | Key / Subkey / Certification Revocation (0x20, 0x28, 0x30) + Reason for Revocation | a revocation statement naming its target by digest, with its reason | preserved; a 0x30 with no Signature Target is inferred (open question 8) |
   | Revocation Key subpacket | not imported as a delegation of revocation | dropped (R-0131) |
   | Revocable = 0 | no counterpart | dropped (reject 8) |
   | Key Expiration, Signature Expiration | `Validity.not_after`, as creation time plus offset | preserved as a snapshot at import time; a later self-signature is not tracked (note 5) |
   | Subkey + Subkey Binding (+ embedded 0x19) | `Key`, plus a key-binding statement (adapt 5) | inferred; no ARCH-0001 row (open question 5) |
   | Key Flags | an attribute of the key-binding or name statement | preserved as attribute; not a tag |
   | Notation Data, user namespace | a foreign label and value, as an attribute | lossy (ADR-0001); a critical unknown notation rejects the signature (note 8) |
   | Policy URI, Preferred Key Server | provenance (R-M-11, proposed) | dropped or provenance |
   | Signer's User ID | an attribute (note 9) | preserved as attribute |
   | Third-Party Confirmation (0x50) + Signature Target | `ArtifactStatement` over the target statement's digest | inferred |
   | Binary or Text signature (0x00, 0x01) | `ArtifactStatement`, only with the document present (note 7, item 8) | inferred; predicate ambiguous (note 9; open question 4) |
   | preferences, Features, Key Server Preferences, Intended Recipient Fingerprint, Padding | none | dropped |

## 15. What we reject, and why

1. **OpenPGP packets as the native encoding.** Excluded by D-3. Every
   type identifier in the format is registry-allocated (N-565, N-566), which P1
   excludes. The exceptions are DNS-owned notation names and the private ranges
   (N-169, N-507), which P1 excludes for the reasons in note 8 (note 11).
2. **Registry-allocated type indicators natively**, however well authenticated
   (N-071; note 7, item 3). Per P1 and ADR-0001.
3. **Unsigned fields inside a signed statement** (R-0077, N-126, N-551). Local
   annotations live outside the statement (note 7, item 4).
4. **Receiver-chosen conflict resolution** (R-0086, N-127). Duplicates are
   invalid under P5 (note 7, item 6).
5. **Opt-in criticality per instance** (R-0079 to R-0081). An unknown
   restriction fails open (note 3; vector PGP-053222-C03). P5 inverts it.
6. **Trust computation by weighted introducers as a reducer.** The source gives
   no composition rule (R-0119, R-0151). G3 rules out *"unbounded WoT path
   search as the primary algorithm"*, and ARCH-0001 §3.3 says *"not as the
   reducer"* (note 2).
7. **Supersession by "most recent valid self-signature"** (R-0095). It is
   suppressible by stripping (line 2126) and makes validity non-monotone. A
   renewal is a new statement (note 5).
8. **Irrevocable signatures** (R-0112). This conflicts with R-O-02's *"revocation
   still representable"*. Short validity expresses the same commitment (note
   5).
9. **Delegated revocation by designation** (the Revocation Key, R-0131, N-163).
   Already deprecated by the source, for the reasons N-542 gives. Escrow
   replaces it (adopt 2).
10. **Creation time inside the key identifier** (N-264, N-553). Under R-M-02 a
    KeyId is a function of the key (note 6).
11. **Short key identifiers** (R-0005, R-0103). And no truncated fingerprint,
    which §14.1 allows only where the constrained field's own specification
    says how (R-0420).
12. **Canonicalization of the signed text at verification**: text signatures,
    cleartext whitespace trimming, dash-escaping (R-0166, R-0266, R-0272). §7.3
    gives the reasons (note 7, item 2).
13. **A signed-but-local statement kind.** `AclEntry` is the local root, and a
    signature over one's own store adds nothing (N-150; note 4).
14. **Vague-by-design statement types** (§5.2.1, line 1489; N-072). Under P3 a
    type carries its semantics, and a predicate whose meaning is one of three
    is three predicates (note 9).

---

## 16. Mapping to our decisions

| Ours (ARCH-0001 text, priority) | What RFC 9580 contributes | Status |
|---|---|---|
| **R-I-04** · S · *"Import OpenPGP identity signatures as `NameCert` and/or `Endorse`, never as `AuthzCert` unless an explicit profile says so."* | Certifications 0x10–0x13 map to `NameCert`. A level ≥ 1 trust signature is delegation over the name predicate, with a depth and a scope that `Endorse` cannot hold (note 2). | **Holds, and the escape hatch is needed.** Three import options (note 2). Under P6 the line falls between predicate types. |
| **R-I-01** · M · a mapping table per foreign format | The field inventory (adapt 9). | Input to WP4. |
| **R-I-02** · M · *"Import SHALL NOT require the foreign object to become a native trust anchor."* | Trust packets are ignored outside local keyrings (R-0225). Trust signatures are statements by their issuers (note 4). | **Holds by construction.** |
| **ARCH-0001 §4.2 `Endorse`** · *"issuer treats subject as introducer at weight w"* | w is the trust amount (R-0119). Depth and scope have no field. | **Adopted for w.** Depth and scope are open question 1. |
| **ARCH-0001 §6 matrix**, OpenPGP row | *"trust values are local to importer"* is true of Trust packets, not of trust-signature amounts (R-0109). Data signatures and subkeys have no row. | **Correction proposed** (open questions 3, 4, 5). |
| **ARCH-0001 §1, §3.3 item 4** · *"not the validation algorithm"*, *"not as the reducer"* | The source has no validation algorithm (§5.2.1, line 1491; R-0151). | **Holds.** Nothing to decline. |
| **R-M-02** · M · *"A principal MAY be identified solely by key or key digest."* | Fingerprints hash creation time and version along with the key (N-264, N-553). | **Contrast.** The import recomputes the KeyId (note 6). |
| **R-M-03** · M · *"Names SHALL be interpreted only relative to an issuing principal."* | Every certification is a statement by its certifier's key (N-423). User IDs are global-ish strings with *"no restrictions on its content"* (N-312). | **Evidence for**, in structure: OpenPGP's bindings are per-certifier, as SDSI's are. The *content* is global (NG5). |
| **R-M-04** · M · *"Name bindings and authorization bindings SHALL be distinct object kinds."* | A trust signature rides on a certification (note 2). A third-party Direct Key signature could separate them, and the source is silent (open question 6). | **Evidence for**, the same fusion the 5280 notes found in X.509. |
| **R-M-05** · M · *"Authorization composition SHALL be deterministic given an ordered cert set and ACL."* | Receiver-chosen conflict resolution (R-0086), no trust composition (R-0119), no chain rule for expressions (note 3), "most recent" supersession (R-0095), *"final authority for validity upon the receiver"* (line 1491). | **Unmet by OpenPGP, by design.** Evidence for stating every rule the source leaves to the receiver. |
| **R-M-06** · M · threshold principals | Key Flags 0x10 and 0x80 are unverifiable claims (N-181). Escrow shares are a k-of-n release control (N-543). | **Contrast**, plus a second kind of threshold (note 5). |
| **R-M-07** · M · *"Artifact statements SHALL bind at least one content digest."* | A data signature signs a hash over the document and its own fields, not a content digest (R-0175). 0x50 statements are about statements (N-086). | Import of data signatures needs the document (note 7, item 8). |
| **R-M-08** · M · *"Tag intersection semantics SHALL be defined for every tag profile the implementation claims."* | §8 defines matching for one expression, and nothing defines combination (note 3). | **A profile with its semantics missing.** Adapt 2 lists what it needs. |
| **R-M-09** · S · validity intersection | Expirations are offsets from creation (N-141, N-148). Absence or zero means never (R-0104, R-0107). | Exact on import, as a snapshot (note 11). |
| **R-M-10** · S · *"Delegation SHALL be an explicit boolean (or equivalent) on `AuthzCert`."* | A bounded integer, with level 0 as FALSE and no unbounded value (R-0114 to R-0118). No rule for over-delegation. Subkeys answer the temporary-key objection (note 2). | **Evidence for "(or equivalent)"**, read as TRUE plus a bound. Decides nothing. |
| **R-M-12 / ADR-0001 / ARCH-0002 P1** · key-relative extension points | The user namespace is `(DNS domain, tag)`, unbound to any key (N-169, N-170). Private ranges are to be promoted to IANA as they grow (N-507). | **Evidence for**, from inside an incumbent (note 8). |
| **R-O-01** · M · issuer specifiable as `KeyId` | Issuer Fingerprint is only a SHOULD (R-0157) and may be unhashed (R-0417). | On import, the issuer is the key that verified (note 6). |
| **R-O-02** · S · *"Short-lived validity preferred over revocation-heavy design; revocation still representable."* | Unbounded defaults (R-0104, R-0107). Single positive revocations, escrow, hard and soft reasons (note 5). | **Revocation: adopt.** Defaults: contrast. |
| **R-O-03** · S · canonicalization cited, not invented | Text canonicalization is specified (R-0166, R-0266) and harmful (§7.3). | Not affected natively. Evidence for R-O-05. |
| **R-O-04** · C · SCITT-like registration | Soft revocation depends on signer-asserted time (R-0101, R-0149). | Evidence for receipts as independent time (note 5). |
| **R-O-05** (proposed) · sign canonical bytes verbatim, with an authenticated type indicator | Reconstructed signed bytes (N-423, R-0172); canonicalization at verification (R-0166, R-0266); a type and version trailer (N-213). | **Evidence for every clause**, mostly by counterexample (note 7). |
| **R-O-06** (proposed) · separate verifier results | "Valid" means two things, one undefined (R-0179, R-0151). | Evidence for the vocabulary split (note 9). |
| **ARCH-0001 §4.2 `AclEntry`** | The Trust packet (N-310), and the signed-but-local certification (N-150). | **Agrees.** Ours is specified (note 4). |
| **ARCH-0001 §4.3** procedures | A certification is procedure 1, name resolution, input. A trust signature is procedure 1 input too: an `Endorse` under options 1 and 2, a delegation over the name predicate under option 3. It reaches procedure 2 only through a profile that makes it an authorization (note 2). | A classification for WP4. |
| **ARCH-0002 P2** · *"A says B can speak about (Domain, Topic)"* | A scoped trust signature is P2's delegation with Topic = names (note 2). | **A deployed instance**, scoped by strings, not by domain. |
| **ARCH-0002 P3** · a type is a schema | Vague signature types, unused assurance levels, speaker-dependent Key Flags (note 9). | **Evidence for**, by counterexample. |
| **ARCH-0002 P5** · validity checked, unknown rejected | Opt-in subpacket criticality, and the fail-open regex case (R-0081, R-0129; PGP-053222-C03). Packet criticality by range (R-0032). | **Evidence for**, the strongest in this record (note 3). |
| **ARCH-0002 P6** · a name is an attested string | *"My name X is tied to my signing key K"* (N-132). | **Agrees.** |
| **ARCH-0002 P7** (held) · authorization by profile | R-I-04's *"explicit profile"* is a P7 profile (note 2). | A concrete candidate when P7 is taken up. |
| **DEC-002 / D-3** | Packet format against reduced CBOR (note 11). | **A non-mapping, stated.** |
| **DEC-003** · *"Must specify: canonical key bytes before hashing."* | v6 fingerprint input: framing octet, length, version, creation time, algorithm, material length, material (N-264). | **Precedent.** Keep the algorithm and the framing. Drop the creation time. Make the digest self-describing (adopt 4, reject 10, adapt 4). |
| **DEC-004** · tag language | Option 1's prefix cannot state a domain suffix without structuring the address (note 3). | Evidence. Open question 2. |
| **DEC-008** (open) · key-local processing | A §8 expression passes the boundary test for membership, not for inclusion (note 3). | A ready candidate for its step 1. |
| **D-1** · email delegation as a schema scenario | RFC 9580 is that scenario, deployed. Vector PGP-053222-C01 is its scope. | Notes 2 and 3 are the scenario's inputs. |

---

## 17. Open questions

1. **Which import option for level ≥ 1 trust signatures?** The options are
   `NameCert` + `Endorse` with depth and scope dropped, `Endorse` extended with
   depth and scope, or a P7 profile importing a delegation over the name
   predicate (note 2). The first is the only one available without new fields.
   The third is where P2 and P6 point, and it needs P7.
2. **The `delegation-models` answer makes four claims about OpenPGP that this
   extraction corrects or qualifies.** The topic is not edited here. As for the
   5280 notes' corrections, #64 should carry them.
   - *"OpenPGP cannot get near it at all because it has no authorization
     field"*.
     **Qualification.** Key Flags in a certification scope that certification's
     use (N-182). A critical notation in the hashed area can carry any claim,
     with must-understand semantics (N-172). Neither composes with a trust
     signature in the source, and neither makes the scope about what the
     delegate may *say* (note 9).
     **Holds** for the conclusion: no source rule expresses "Bob may vouch for
     `*@foo.com` about code signing".
   - *"the RFC's stated reason for the change is a deployment verdict — support
     for the old mechanism was "uneven and unreliable""*.
     **Correction.** That is the fifth of six listed advantages (N-542), not
     *the* stated reason. The first listed is that the keyholder *"can
     constrain what types of revocation the preferred revoker can issue"*. The
     record's own summary gets this right (*"one of them"*).
   - *"Alice/Bob/Carol is expressible in three of the four families"*.
     **Qualification** for SPKI. `*@foo.com` is a suffix, and option 1's
     `(* prefix …)` matches from the left, so SPKI expresses it only with a
     structured address (note 3).
   - *"In OpenPGP it is a distinct SUBPACKET on a signature over a User ID"*.
     **Qualification.** That is the usual case, not a source rule. Which
     signature types may carry a Trust Signature is unstated (open question 6).
   - **Verified without correction:**
     - the §5.2.3.22 quotation, with words elided as marked (R-0123);
     - the §5.10 quotation *"defined by a given implementation"* (N-310);
     - level n issuing level n−1, and *"meta introducer"* (R-0117, R-0118);
     - partial below 120, complete at or above, and *"no composition rule
       given anywhere in the RFC"* (R-0119; confirmed by search);
     - *"Applications MUST NOT generate such a subpacket"* (R-0131), and the
       §13.9 constraint quotation (N-542).

   The 5280 notes' open question 9, *"level n ≈ pathLenConstraint n − 1"*,
   checked against R-0115 to R-0118: **holds for n ≥ 1**, with the four
   differences in note 2.
3. **Should the matrix's OpenPGP note change?** It reads *"trust values are
   local to importer"*. Proposed: *"trust amounts are carried; how to combine
   them is local to the importer"* (note 4). The matrix is ARCH-0001's, and this
   file does not edit it.
4. **Where do OpenPGP data signatures go?** ARCH-0001 §3.2 lists *"identity and
   data signatures"*, but the matrix row, R-I-04 and WP4 cover only keys,
   User IDs and introducers. A data signature maps to an `ArtifactStatement`
   only with the document present, because a signature signs a hash over the
   document and its own fields (R-0175), not a content digest. Its predicate is three predicates in one (N-072). If supply-chain
   import of OpenPGP-signed artifacts matters to D-1's primary target, this is
   a matrix row to add.
5. **How are subkeys imported, and does a native key binding need the bound
   key's consent?** A Subkey Binding is a statement between keys, inside one
   principal, which spends no delegation depth (note 10). No ARCH-0001 row or
   principal form covers it. The back-signature (R-0049) has no counterpart in
   SPKI or ARCH-0001 delegation. It is needed wherever a subject comes to speak
   *for* its issuer.
6. **Which signature types may carry a Trust Signature subpacket?** §5.2.3.21 does
   not say. A third-party Direct Key signature (N-081) carrying one would be
   delegation with no name binding, the shape R-M-04 wants. Is it conforming,
   and do implementations accept it? If they do, WP4 can import it without
   R-I-04's fusion problem. The sibling artifacts read it both ways:
   `messages.yaml` (subpacket-trust-signature) derives types 0x10–0x13 and
   notes that *"the source does not restrict types"*, and `protocol.yaml`
   (trust-signature-introduction, step 1) infers that a Direct Key signature
   may carry one.
7. **How do levels and expressions combine along a chain?** The source answers
   neither question (notes 2 and 3):
   - Bob, trusted at level 2, issues Carol a level-2 signature. Is it ignored,
     or truncated to level 1?
   - Are expressions per hop or conjoined? Under the per-hop reading, a
     meta-introducer's scope can widen.

   A native profile must state both. The conservative choices are truncation to
   the minimum, as X.509 does with its counter (rfc-5280#R-0414), and
   conjunction. `state-machine.yaml` M10 already models both as *"our
   reading"*: it intersects expressions along the chain (OQ-26) and takes the
   minimum depth (OQ-27). `protocol.yaml` records the gap as
   `trust-combination-undefined`. OQ-27 also asks how amounts combine (min,
   product or last hop), which is reject 6's question.
8. **Revocation targets and interactions.**
   - A Certification Revocation without a Signature Target revokes which
     certification: every earlier one by that issuer on that binding, or only
     the latest (R-0055)?
   - Does a Key Revocation for compromise override a signature marked not
     revocable (R-0112, R-0149)?
   - Which reasons are hard? Code 0, the private codes 100–110 and an absent
     subpacket are classified neither way, and `state-machine.yaml` M06 treats
     them as hard (OQ-20). And Reason for Revocation is *"used only in Key
     Revocation and Certification Revocation signatures"* (R-0146), which
     leaves a Subkey Revocation (0x28) unclassified (OQ-23, a source defect;
     messages.yaml SD-M07).
   - What does expiry do? The source never states the consequence of an
     expired key or signature, beyond one §13.8 example of an expired
     recipient key (line 6654; protocol.yaml `expired-key-consequence`).

   Import must pick a reading for each. The native model avoids the first two by
   naming targets by digest (adapt 6) and keeping every statement revocable
   (reject 8). It avoids the third by taking reasons from a closed list, with
   any code outside it read as hard. The first is `state-machine.yaml` OQ-25. The second is
   `protocol.yaml` `revocable-vs-key-revocation`, which also asks whether
   "later" means creation time or arrival.
9. **Edges of the time and text mappings.**
   - A zero or absent expiration means *"never"* (R-0104, R-0107). Under
     R-O-02, may a translated statement have no `not_after`, or does import
     impose one?
   - Four-octet times end in 2106.
   - User IDs are *"UTF-8 text"* (N-312) with no receiver check required. Is a
     User ID that is not valid UTF-8 rejected, or carried as bytes?
10. **Is there deployment evidence for trust-signature depth?** The 2693 notes'
    open question 9 names `ulrich-2011-openpgp-wot`. It is held as a stub in
    `uptake-failure`, with no source fetched. `gnupg-key-management` (*"tsign,
    trustspec"*) and `keys-openpgp-org-faq` are stubs too. RFC 9580 itself
    contains none. R-M-10's ADR should read at least the first before weighing
    OpenPGP's integer as evidence.
11. **The record's summary, checked against the full text.**
    - *"the phrase "web of trust" appears in this document exactly once, in an
      informative reference"*. **Confirmed** (line 7539), and sharper than
      stated: that reference is the chosen-prefix forgery of web-of-trust
      certifications [SHAMBLES], which motivates v6 salting (note 12).
    - *"Exportable Certification, where a non-exportable certification … "MUST
      be marked as critical""*. **Precise reading.** The MUST applies when the
      subpacket *"denotes the signature as non-exportable"* (R-0111).
    - The summary's Limits say the read scope was narrow. This pass read the
      whole source, and the Limits section is superseded for this record's
      `distilled/` artifacts. `summary.md` itself is not edited here.
12. **Source gaps that bear on design.** Recorded, not repaired:
    First, from the sibling artifacts. Each is recorded there with its quotes:
    - **What Signature Target hashes.** *"All arguments are an identifier of
      that target signature"* (line 2686), but nothing says what the N octets
      hash is computed over (N-195; messages.yaml SD-M11). R-0155's *"the size of
      the signature's hash"* suggests the target's own signed digest, which is
      messages.yaml's derived reading. Adapt 6 needs it
      stated.
    - **Critical-unknown is a SHOULD.** R-0080 makes an unknown critical
      subpacket an error only as a SHOULD. §5.2.5's MUSTs (R-0178, R-0179) list
      *"An unknown "critical" subpacket … in the hashed area"* among malformed
      or unknown signatures. So the hashed case is effectively a MUST, and the
      unhashed case is left at SHOULD (state-machine.yaml OQ-14; protocol.yaml
      `critical-subpacket-should-vs-must`). That is P5's failure mode in the
      source's own conformance language.
    - **Who may revoke a subkey contradicts itself.** §10.1.5 accepts
      revocations *"issued by the key itself"* (N-428), §5.2.1.12 only those by
      the top-level key (R-0053) (protocol.yaml `revocation-issuer-for-subkeys`).
    - **Which "most recent" self-signature.** R-0095 picks one per "object". It
      does not say whether a newer User ID self-signature can override a Direct
      Key signature's expiry and flags, on a v4 key or a v6 one, or what happens when the newest
      one omits a subpacket the older one had (protocol.yaml
      `most-recent-self-signature-scope`; state-machine.yaml OQ-19). Reject 7
      removes the question natively.
    - **Must a certifier carry the certify flag?** Key Flag 0x01 says *"This
      key may be used to make User ID certifications"* (N-181). Nothing says a
      verifier must reject a third-party certification from a key without it
      (state-machine.yaml OQ-18; protocol.yaml `key-flags-enforcement`). Read
      as delegation, 0x01 is the key's capability to certify at all, the
      counterpart of X.509's `keyCertSign`. An unenforced capability bit is a
      grant nobody checks.
    - **Is the back-signature hashed?** The embedded 0x19 that consents to a
      subkey binding (R-0049) may sit in either area (protocol.yaml
      `embedded-signature-area`). In the unhashed area the consent is not
      covered by the binding signature (note 10; reject 3).
    - **Search or match.** R-0125 and §8's anchors imply search, and nothing
      states it (note 3). `protocol.yaml` `trust-combination-undefined` notes
      that anchoring *"follows only from the Henry Spencer semantics"*.
    - **"Trust Signature packets" should read "subpacket"** (R-0122;
      messages.yaml SD-M25). Editorial, and quoted as written above.

    Then, found while writing these notes:
    - **Two grammars for the Regular Expression.** §5.2.3.22 cites Henry
      Spencer's package as an informative reference (R-0124; §16.2, line 7486),
      and §8 restates a grammar (N-382). Where they differ, which governs?
      `state-machine.yaml` lists the matcher as not modelled.
    - **Who may revoke is lowercase.** R-0051 and R-0054 use *"should be
      considered valid"* and *"should be issued"*. §10.1.5 states it as fact
      (N-428). The rule that decides whose revocation counts has no BCP 14
      keyword.
    - **Appendix A has no delegation example.** It contains no User ID
      certification, no trust signature, no regular expression and no
      revocation. The only in-source vector on the delegation path is §8's
      `[0-9]` (PGP-08-01). Trust signatures and scoped expressions have
      constructed vectors only (PGP-053221-C01 to -C05, PGP-053222-C01 to -C03),
      certifications and revocations have none, and no constructed outcome has
      been run against an implementation (examples/README.md, "Not
      verified"). Fixtures for the D-1 email
      scenario cannot be checked against the source's own examples.

    Then, found by the cross-check (pass 3):
    - **Revoking a binding signature has no signature type.** §5.2.3.10 says
      *"Revoking a binding signature effectively retires that subkey"*
      (R-0091, line 2092). The Certification Revocation revokes only
      *"an earlier User ID certification signature (Type IDs 0x10 through
      0x13) or Direct Key signature (Type ID 0x1F)"* (lines 1629-1630), and
      the Subkey Revocation *"is calculated directly on the primary key and
      the subkey being revoked"* (lines 1621-1622). No type revokes a 0x18
      itself (protocol.md, `subkey-revocation`). For R-O-02, the subkey is
      retired either way, and only 0x28 is a defined way to do it.
    - **The CRC24 MUST NOT list has gaps.** §6.1 forbids the footer for an
      encrypted message ending in v2 SEIPD, an armored *"sequence of Signature
      packets that only includes version 6 Signature packets"*, a v6 Transferable
      Public Key and a keyring of only v6 keys (lines 4283-4294). It does not
      cover an unencrypted v6 signed or one-pass-signed message, or a v6
      Transferable Secret Key. These fall back to the SHOULD NOT at lines
      4275-4277 and to the context test at lines 4279-4282. Whether "sequence
      of Signature packets" includes a whole signed message is unstated
      (protocol.yaml, `sign-message-inline` step 11).
    - **A failing final AEAD tag falls under two rules.** *"if the
      authentication tag fails to verify, the implementation MUST NOT attempt
      to parse nor release decrypted data to the user, and it MUST halt with
      an error"* (R-0406, lines 6518-6520). A truncated message, *"the final
      zero-octet chunk and possibly (part of) some chunks before it are
      missing"*, MAY have released authenticated chunks while streaming
      (R-0408, lines 6526-6531). A missing final chunk shows up only as a
      failing final tag. `state-machine.yaml` M13-T08 reads it as truncation
      (OQ-40). `protocol.yaml` `seipd-v2-decryption` step 4 reads it as a tag
      failure. Both release nothing further. They differ only on whether chunks
      already released may stand. A native profile that streams has to pick
      one reading.
