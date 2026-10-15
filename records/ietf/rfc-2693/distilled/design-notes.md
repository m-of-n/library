---
record: rfc-2693
kind: design-notes
title: "rfc-2693 — bearing on our design"
extracted: "2026-10-12"
reviewed_by: ""
---

# RFC 2693 — bearing on our design

RFC 2693 is the ancestor this architecture descends from. Its 5-tuple, its
reduction rule, its unsigned ACL and its boolean delegation bit are restated
almost one for one in the model requirements. This file therefore reads less
like an evaluation of a candidate and more like an audit of an inheritance: what
we took, what we took and must finish, and what the working group left us that
we should refuse.

**Three things to hold while reading.**

1. **The source binds nothing in BCP 14 terms.** `requirements.yaml` records a
   measured keyword count of zero. Its 251 entries are lowercase rules,
   definitions and working-group decisions. §6 calls its own processing plan
   *"an example that may be followed, but its primary purpose is to clarify the
   semantics"* (R-0106). Wherever we adopt something here, **we** make it
   normative. The RFC does not, and a citation to it is a citation to a
   rationale.
2. **Our decisions are cited as the library restates them.** The glosses below
   for R-M-*, R-O-*, DEC-*, ADR-0001 and D-3 come from `record.yaml`
   `bears_on`, `summary.md` and the design notes of rfc-8785, rfc-8949 and
   rfc-9804, which quote ARCH-0001, ADR-0001 and the D-3 minute. ARCH-0001
   itself lives outside this repository and was not reread for this pass. A
   reviewer with ARCH-0001 open should check each mapping row against the
   current text.
3. **Two numbering schemes collide.** `schema/README.md` numbers the source
   defects D-01 to D-13. Meeting decisions are D-n (D-3 here). They are
   unrelated. This file always writes the former as *schema D-NN* and the
   latter as bare *D-3*.

Requirement ids are `rfc-2693#R-NNNN`, written R-NNNN below. Vector ids are from
`examples/vectors.yaml`.

**Nothing here decides DEC-004 or R-M-10.** Both are cited as evidence. A DEC
is accepted only in an ADR.

---

## 1. What we adopt

1. **Authorization bound to a key, with names kept off the access-control
   path.** §3.3: *"A basic SPKI certificate defines a straight authorization
   mapping: authorization -> key"* (R-0052). §8 gives the security argument in
   two parts. The two-certificate construct needs two trusted issuers, *"In the
   former case, there is only one issuer to trust. In the latter case, there are
   two."* (R-0247). Its join is by name across name spaces, which *"is more
   complex than string matching and might even involve a human guess"*
   (R-0249). §3.3 then puts the name mapping where it can fail safely: a
   subversion of key -> name *"does not permit the attacker to defeat the access
   control"* (R-0055). This is the basis of R-M-02 (a principal is its key or
   key digest) and of keeping authorization and naming apart (R-M-04).

   **We adopt §8's exception along with the rule.** *"If the two certificates
   come from the same issuer, and therefore with the same name space, then both
   of the security differentiators above are canceled."* (R-0250). The argument
   is against cross-issuer name joins, not against names. Mapping item
   R-M-03/R-M-04 below depends on that distinction.

2. **The local, unsigned root of authority.** *"An ACL entry has potentially
   the same content as a certificate body, but has no Issuer (and is not
   signed)."* (R-0003). The ACL *"is the source of empowerment for
   certificates"* (R-0002). A 5-tuple's issuer may be *"the reserved word
   'Self'"* (R-0121). That tuples derived from ACL entries take `Self` is
   R-0122, the record's one `kind: inferred` entry: the source states both
   halves but never joins them. We adopt the shape: every chain ends at a local
   policy entry that is trusted because the verifier holds it, never because
   someone signed it.

3. **One composition rule, monotone in authority.** §6.3 (R-0136 to R-0139):

   ```
   <I1,S1,D1,A1,V1> + <I2,S2,D2,A2,V2>  =>  <I1,S2,D2,AIntersect(A1,A2),VIntersect(V1,V2)>
   provided  the two intersections succeed,  S1 = I2,  D1 = TRUE
   ```

   Authority can only narrow along a chain. Nothing in the rule can widen A or
   V. This is the core of R-M-05, and it is worth keeping in exactly this form:
   one binary operator, three provisos, and no other way to join tuples.

4. **Ordering is the prover's job, so verification is a fold.** *"All
   reduction operations are in the order provided by the prover."* (R-0171).
   The verifier does no search. It applies the rule to a sequence and accepts
   or rejects. Path discovery ([ELIEN]) stays outside the verifier. This is
   where R-M-05's determinism actually comes from: a verifier that only folds
   cannot reach different answers on the same input. It is also cheap. §6.3.4
   has a delegator append *"a single additional certificate"* to the sequence
   it received (R-0174).

5. **Determinism as a property validity must preserve.** §5.1 rules out
   *"wandering anti-matter CRLs"* (R-0074) because their outcome is *"at least
   timing dependent"* and an adversary can suppress them *"merely network
   tampering"* (R-0073). It then states the principle outright: *"Every
   authorization computation is deterministic, under SPKI rules."* (R-0075).
   The timed-CRL conditions follow from it. The certificate names the CRL key
   (R-0077). The CRL carries dates (R-0079). Ranges must not intersect (R-0080,
   R-0081). So *"no CRL can be issued to show up as a surprise at the
   verifier"* (R-0083). Revalidations follow the same rules (R-0090). This is
   the reasoning R-O-02 and R-M-09 need. A revocation mechanism is admissible
   only if it keeps the computation a function of its inputs.

6. **The certificate names who may confirm it.** *"In SPKI, the certificate
   issuer must specify the issuer of validity confirmations."* (R-0072). The
   online-test issuer may differ from the certificate issuer (R-0071), but the
   certificate fixes who it is. No ambient revocation authority exists.

7. **Boolean delegation, with the reasoning attached.** *"Of these three, the
   group chose boolean control."* (R-0060). The subject *"may exercise any
   permission granted"* (R-0061) and, *"if delegation is TRUE, may also delegate
   that permission or some subset of it"* (R-0062). The two arguments that
   decided it carry over directly. Depth is unpredictable, since *"One can
   always need to go one more level down, by creating a temporary signing
   key"*. And depth does not bound proliferation: *"there is no control on the
   width of the delegation tree"* (R-0064). This is R-M-10 as it currently
   stands (*"Delegation SHALL be an explicit boolean (or equivalent)"*, quoted
   in the rfc-9580 summary). §4.2's corollary comes with it. A delegator can
   always mint a key and delegate to itself (R-0065), so separating delegators
   from exercisers buys nothing.

8. **Names are relative to the key that defines them.** *"If a (local) SDSI
   name occurs within a certificate, then the public key of the issuer is the
   identifier of the name space in which that name is defined."* (R-0033).
   Outside a certificate, the name must carry its key (R-0034, R-0035). §7.3
   makes the point that settles it: the name is not `"jim"` but the whole
   construct `(name (hash sha1 |…|) jim)` (R-0224). This is R-M-03. It is also,
   26 years early, **exactly the shape ADR-0001 prescribes for native extension
   points**, a `(key, local label)` pair (quoted in the rfc-8785 design notes).
   SDSI applied it to principals' names. ADR-0001 applies it to type
   identifiers, predicate types and tags. The precedent is worth citing in the
   ADR's lineage.

9. **The safe rule for unordered name reduction.** When the verifier holds an
   unordered pool, *"a safe rule for name reduction is to apply only those
   4-tuples that define a name as a key"* (R-0182). Name-to-name definitions
   are first reduced to name-to-key (R-0183), and *"Any naming loops are avoided
   by this process"* (R-0184). This is a termination guarantee that is cheap to
   test. Keep it as the rule for any verifier that does not receive a
   prover-ordered sequence.

10. **Threshold subjects as the root's fault tolerance.** K of N with
    `0<K<=N` (R-0165). Members may use different algorithms: *"the keys in a
    threshold subject do not need to have the same algorithm"* (R-0240). §7.7
    shows the pattern that matters most for us. The ACL controls itself through
    a stricter quorum, `(k-of-n #05# #07# …)` for `(acl-edit)` against
    `#03# #07#` for normal use, so the root set can *"elect new members to that
    set and retire old members"* (R-0243). This is R-M-06 together with key
    rollover at the root, without a CA. The algorithm-heterogeneity remark is
    directly useful for a post-quantum transition, where a root can be
    `k-of-n` over classical and PQ keys at once.

11. **One authorization per certificate.** *"It is desirable that
    authorizations be limited to one per certificate"* (R-0051). The reasons are
    stated in §3.2: one issuer would have to be an authority on everything, the
    lifetime shortens to the shortest attribute, and aggregation *"amounts to
    the building of a dossier"*. We adopt it as a default, not an invariant.

12. **Short-lived certificates as the default answer to revocation.**
    §5.6: a short-lived certificate *"always requires fewer signature
    verifications than the use of certificate plus online test result"*,
    especially *"if the online test result is issued by the same key that issued
    the certificate"* (R-0102). §7 states the same choice at the level of keys:
    *"under SPKI one does not declare a key to be bad but rather stops
    empowering it and instead empowers some other key"* (R-0220), and *"all key
    lifetime control becomes certificate lifetime control"* (R-0222). This is
    R-O-02's strongest prior-art argument, and it costs us no new mechanism.

## 2. What we adapt, and how

Everything in this section is a place where RFC 2693 states an idea and leaves
the rule unfinished. Each item names the gap, cites where the sibling artifacts
recorded it, and says what our profile has to add. None of these additions
contradicts the source. Each fills something the source left open.

1. **AIntersect, completed into DEC-004 option 1.** §6.3.1 is DEC-004 option 1
   (*"byte-string sets + intersection"*). It is specified by four `*`-forms,
   the padding rule and five worked examples (R-0141 to R-0156). That is enough
   to show the semantics and not enough to implement them. Our profile must
   supply:

   - **Byte-level equality.** Two authorizations *"intersect by matching,
     element for element"* (R-0142), with no statement about encoding, case or
     normalisation. Rule: elements match if and only if their octets are
     identical. No case folding and no Unicode normalisation happen inside
     AIntersect. Normalisation, if any, happens at authoring, as in the rfc-9804
     notes, condition 6.
   - **A result for every pair of forms.** The examples cover `(*)` with
     anything, set with set, set with atom, and prefix with prefix. Nothing
     covers range with range, range with prefix, prefix with set, or set with
     range (protocol.md, gap §6.3.1). Every pair needs a defined result, and
     the result must be representable as one of the forms. See open question 2:
     closure forces half-open bounds.
   - **The range operators and orderings.** The template is
     `(* range <ordering> <lower-limit>? <upper-limit>?)` (R-0154). The only
     example writes `ge #30# le #39#`, and the operators are never defined
     (`SPKI-631-08`). The orderings `alpha, numeric, time, binary, date`
     (R-0155) are named and nothing more. `numeric` over a byte string has three
     plausible readings, and the one example cannot choose among them
     (schema D-10, `SPKI-631-13`). Rule: each ordering gets a byte-level
     comparison function, and the operators are `g`, `ge`, `l`, `le`.
   - **A canonical result representation.** `SPKI-631-11` returns `(tag read)`,
     not `(tag (* set read))`, so a singleton set collapses. `SPKI-631-10`
     prints the set in the first operand's order. A result that only has to be
     compared can be compared as a set. A result that gets **signed**, as in a
     Certificate Result Certificate (§6.6) or any re-issued attenuated grant,
     needs one canonical spelling, or two verifiers produce different bytes from
     the same reduction. Rule: singleton sets collapse, set members sort
     bytewise, and nested `*`-forms are normalised before signing. This is the
     same canonical-order requirement ARCH-0002 P4 and `Threshold.members`
     need. See the rfc-8785 design notes, which list *"a tag's value set"*
     under DEC-004 option 1.
   - **The padding rule stated as the rule.** §6.3.1 has two descriptions that
     agree only through padding. One is *"normal set intersection, when ...
     a normal list is taken to mean all lists that start with those elements"*
     (R-0156). The other treats a list *"as if it had enough (*) entries
     implicitly appended"* (R-0151). The examples README shows they disagree on
     `(dns)` against `(dns (*))` under the strict set reading
     (`SPKI-657-04`, `-05`). Rule: the padding rule is normative, and the
     set-theoretic sentence is commentary.
   - **The decision rule.** RFC 2693 reduces to a final tuple (R-0117) but
     never says how a request is checked against it (`SPKI-657-12`). Rule: a
     request R is granted under the final authorization A if and only if
     `AIntersect(A, R) = R`. Granting whenever the intersection is merely
     non-empty would let a request for `(ftp host /)` succeed against a grant
     of `(ftp host /pub)`.

   R-M-08 says intersection semantics are *per profile*. The adaptation is that
   a profile **declares** its semantics in this algebra and does not ship code
   for it. See §3 item 4.

2. **VIntersect, with the boundary decided.** `Vmin = max(...)`,
   `Vmax = min(...)`, failure only *"if Vmin > Vmax"* (R-0157, R-0158). That
   makes intervals closed. A closed interval breaks §5.2's *"CRL validity date
   ranges must not intersect"* (R-0080) for back-to-back CRLs `[100,200]` and
   `[200,300]`, while the restatement in R-0081 accepts them (`SPKI-52-04`).
   Rule: intervals are half-open, `[not-before, not-after)`. Failure is then
   `Vmin >= Vmax`, and consecutive CRLs or revalidations tile without
   overlapping. Keep R-0159's precondition, that times are monotonic, as an
   explicit requirement on the time representation, which is a DEC-002 matter.

   **The infinite defaults need a profile decision, not inheritance.** A
   missing not-before means minus infinity and a missing not-after means plus
   infinity (R-0127, R-0128). Given adopt item 12, a profile that wants
   short-lived certificates to be the norm should require not-after on every
   signed certificate. Only ACL entries, which are local, may omit it.

3. **Threshold reduction, specified.** §6.3.3 gives the shape (R-0166 to
   R-0170) and leaves the edges open:

   - **Delegation intersection is never defined** (schema D-08). Rule: the K
     subordinate delegation bits combine by AND. That is the only reading that
     keeps the rule monotone.
   - **The threshold tuple's own delegation bit.** For the K branches to
     converge *"by delegating their shares"* (R-0019), the tuple holding the
     threshold subject must carry D = TRUE, which the source never says
     (protocol.md, ambiguity §1.1/§6.3/§6.3.3). Rule: make it explicit.
     §7.7's example never states its D bit.
   - **More than K valid branches.** The source selects K and sets the rest to
     `(null)` (R-0167), with no rule for which K. Since the AIntersect of K
     branches depends on which K are chosen, *which* K affects the result. Rule:
     the prover names the K, consistent with R-0171. The verifier checks
     exactly those, and extra branches are ignored rather than intersected.
   - **Where `(null)` sits** (schema D-07) and **proof order for a tree**: the
     prover-ordered sequence of R-0171 is linear, and a threshold proof has K
     branches (protocol.md, gap §6.3.4 vs §6.3.3). Rule: a proof is a tree
     whose threshold nodes list their K branches in member-index order.
   - **Distinct members.** Nothing stops one key from appearing twice among the
     N and satisfying two shares. Rule: the K selected members must be distinct
     after canonical identification (item 4). This is the same invariant
     `Threshold.members` needs in ARCH-0001 §4.1.

4. **`S1 = I2` needs one identity form.** Issuer and subject may each be
   *"a public key (or its hash)"* (R-0121, R-0123). The source never says
   whether a key equals its own hash in the provisos (protocol.md, ambiguity
   §6.3). With several hash algorithms, one key also has several hashes. Rule:
   every principal is brought to one canonical identifier before comparison, the
   `KeyId` of ARCH-0001 §4.1, and equality is octet equality of KeyIds. This
   pushes the problem into DEC-003, where it already is: KeyId needs a
   canonical key encoding, and the rfc-9804 notes record that the `rcbor`
   `keyid()` defect is open under every DEC-002 option.

5. **Name 4-tuples, narrowed.** RFC 2693 writes the 4-tuple three ways (protocol.md,
   inconsistency §6.2/§6.4/§6.5). §6.2 says *"Name: a byte string"*
   (R-0131). The X.509v1 translation then places a compound name in that slot
   (R-0195, schema D-02), and §6.4's two classes leave out the threshold subject
   that §6.2 allows (schema D-03). Rule: a name certificate defines **one**
   label relative to its issuer. Compound names exist only as references to be
   reduced (R-0178, R-0179), never as the thing being defined. Allowing a
   threshold subject in a name definition is an open question (8).

6. **The ACL entry gets a specified shape for us, even though SPKI left it
   free.** *"An ACL entry is free to be implemented in any way the developer
   chooses, since it is never communicated"* (R-0056). That works for one
   verifier. Our determinism claim is stronger: two verifiers with the same
   policy and the same proof reach the same answer, and an auditor can
   reproduce the decision. That needs the root policy to be a defined structure
   that can be hashed. Rule: an ACL entry is the 5-tuple body with issuer `Self`
   (R-0057, R-0122). It is never signed, but it is canonically encoded so that a
   decision record can name the policy it was made under.

7. **Certificate translation as the import boundary.** §6.5 lets any format be
   translated into tuples after its own verification (R-0192 to R-0207). This is
   a sound pattern for **importing** X.509, OpenPGP or other foreign credentials
   into our model, a direction R-I-03 (export) does not cover. The adaptation
   is to admit what it costs. Tuples are produced *"via trusted software"*
   (R-0119), and X.509v3 translation needs *"chain validation code specific to
   each root key"* (R-0201). Every translator is part of the trusted computing
   base, and each one gets its own conformance tests. Translation output is
   explicit tuples, never implicit grants (see §3 item 5).

8. **Certificate Result Certificates as an optimisation with a new issuer.**
   §6.6 lets a computing entity sign the answer to *"What is Subject S allowed
   to do"* (R-0214 to R-0216). It is useful for caching and for constrained
   verifiers. But the CRC's issuer is the entity that did the computation, not
   the ACL's owner, and the source gives no rule for how a later verifier comes
   to trust it, or what its validity is (protocol.md, gap §6.6). Rule: a CRC
   is accepted only if the computing entity's key is itself empowered by the
   verifier's ACL for that tag. A CRC's validity is the VIntersect of everything
   it summarises, including deferred online tests (R-0163).

## 3. What we reject, and why

1. **Wandering anti-matter CRLs.** Already rejected by the source (R-0074), for
   the reason we would give: non-determinism, and revocation that fails open
   under network tampering (R-0073). Recorded so that nobody reintroduces
   unsequenced revocation lists under a different name. A CRL feed that
   *"follows some dissemination process unrelated to the needs of the
   consumers"* is this design.

2. **Integer delegation depth.** The working group's original design, rejected
   *"by the inability to predict the proper depth of delegation"* (§4.1.4,
   context of R-0064). **This is a live contradiction with `rfc-9580`.**
   OpenPGP's Trust Signature level is integer control, specified, implemented
   and deployed for 25 years (rfc-9580 summary). We side with RFC 2693 on the
   strength of R-0064, because width is unbounded and depth is therefore not a
   proliferation control. The evidence on the other side should be weighed in
   R-M-10's ADR, not dismissed. See open question 9.

3. **The "no control" conclusion. Its premise stays, as a stated limit.** The
   argument that a holder can *"loan out the empowered private key or ... set up
   a proxy service"* (§4.1.1) is correct, and the source does not refute it.
   §4.1.4 only notes that hardware keys and missing connectivity *"might
   inhibit"* an oracle (R-0063). We keep boolean delegation as a statement of
   the issuer's intent, enforced against honest delegates, and we say plainly
   that **no delegation control stops a delegate from proxying**. RFC 2692 calls
   this a *"potential flaw in any system providing authorization"* (summary,
   Limits). It belongs in our threat model as an accepted residual risk.

4. **Application-specific intersection code.** *"Special semantics would
   require special reduction software."* (R-0146). Reject for the native model.
   An intersection only the application can compute makes R-M-05's determinism
   depend on every verifier running the same version of that code, and makes
   the authorization unauditable by anyone without it. A tag whose meaning
   cannot be expressed in the profile algebra (§2 item 1) is out of profile.
   Per-profile semantics under R-M-08 are allowed only as **declared**
   semantics.

5. **Implicit authorizations.** §6.5.3 lets an X.509v3 certificate *"declare an
   implicit authorization of the form (tag (*))"*, and §6.5.7 makes
   `(tag (ssl))` implicit in every SSL certificate (R-0199, R-0208). `(tag (*))`
   is the maximal grant. A translator that invents it is minting unlimited
   authority from a document that never stated any. Reject in the native model.
   On import (§2 item 7), every grant a translated tuple carries must be traced
   to something the source credential states, or to an explicit local policy
   entry that names the mapping.

6. **Abbreviations that change the set.** §6.5.7 says
   `(tag (* set (ssl) (dns www.datafellows.com)))` *"could have been
   abbreviated as"* `(tag (ssl www.datafellows.com))`. Under §6.3.1 these
   denote different sets, and the abbreviated form no longer reduces against a
   separate `(dns)` root (protocol.md, ambiguity §6.5.7). Reject any
   authoring convenience that is not an identity under AIntersect. Tags are
   compared as sets, so a rewrite that changes the set changes the grant.

7. **Global reserved words as native type identifiers.** Every S-expression's
   first element is its *"type"* (R-0016). SPKI's types (`tag`, `name`, `hash`,
   `k-of-n`, `*`, `Self`) are fixed words with no defining key. ADR-0001 makes
   native type identifiers key-relative. We take the *structure* (a
   distinguished first element names the form) and reject the vocabulary
   *as identifiers*. Whether the algebra's own forms (`*`, `set`, `prefix`,
   `range`) count as extension points or as fixed grammar is open question 11.

8. **S-expressions as a consequence of adopting SPKI.** RFC 2693 *uses*
   S-expressions (R-0015) and defines no encoding. The Abstract promises *"a
   canonical form"* that this document does not contain. Choosing SPKI
   semantics does not choose DEC-002 option 1. The semantics adopted above are
   encoding-neutral, and DEC-002 is decided on its own record (rfc-9804).

9. **"Validity intervals of length zero are not possible" as a constraint on
   us.** §5.5 says it, then defines a one-time revalidation that *"represents a
   validity interval of zero"* (R-0095, R-0101, schema D-09). We take the second
   sentence. A nonce-bound, single-use confirmation (R-0099, R-0100) is a
   distinct kind of validity condition, not a timed interval of width zero.
   `state-machine.yaml` M08 models the nonce binding and single use, and passes
   §5.5's zero interval into VIntersect only as the completion instant
   [tc, tc] (M08-T02, M08-T06).

## 4. Mapping to our decisions

| Ours | What RFC 2693 contributes | Status |
|---|---|---|
| **R-M-02** (*a principal MAY be identified solely by key or key digest*) | §2.7: *"The public key, viewed as a byte string, is therefore an identifier for the keyholder"* (R-0028), and a collision-free hash of it is one too (R-0029). §3.3 and §8 for why authorization binds to the key (adopt 1). | **Adopted.** Needs §2 item 4 (one canonical form before comparison). |
| **R-M-03** (names interpreted relative to the issuing key) | R-0033, R-0034, R-0035, R-0224: the issuer's key is the name space, and a name outside a certificate carries its key. | **Adopted** (adopt 8, 9). |
| **R-M-04** (name and authorization certificates separate) | §6.2: a name certificate *"is qualitatively different from an authorization certificate, a separate intermediate form is defined for it"* (R-0129). The 4-tuple has no D and no A, and name reduction leaves both unchanged (R-0191). | **Adopted**, with the 4-tuple narrowed to one label (§2 item 5). |
| **R-M-05** (deterministic composition) | §6.3 rule (R-0136 to R-0139), prover-supplied order (R-0171), R-0075's *"Every authorization computation is deterministic"*. | **Adopted.** Determinism holds only once §2 items 1–4 are closed. As written, AIntersect over undefined form pairs and `S1 = I2` over key-or-hash are each a place where two verifiers can differ. |
| **R-M-06** (threshold subjects) | §6.3.3 (R-0165 to R-0170), §7.7 (R-0240, R-0243): K of N, mixed algorithms, a separate `(acl-edit)` quorum. | **Adopted** in principle. The reduction is underspecified: §2 item 3 gives five rules the source lacks. |
| **R-M-08** (intersection semantics per profile) | §6.3.1 AIntersect is the algebra. R-0141 and R-0145 put the vocabulary in the application's hands. | **Adapted** (§2 item 1, §3 item 4). The semantics are declared, never coded. |
| **R-M-09** (validity intersection) | §6.3.2 VIntersect (R-0157 to R-0163), online-test intervals intersected in (R-0115, R-0162), 4-tuple validity intersected during name reduction (R-0190). | **Adapted**: half-open intervals, monotonic time, a profile decision on infinite defaults (§2 item 2). |
| **R-M-10** (*"Delegation SHALL be an explicit boolean (or equivalent)"*) | §4.1.4 is the decision and its reasons (R-0060 to R-0064). §4.2 (R-0065). | **Adopted**, against rfc-9580's integer control (§3 item 2, open question 9). The oracle limit is recorded as residual risk (§3 item 3). |
| **R-O-02** (CRLs vs positive on-line validation) | §5.2 timed CRLs and §5.3 revalidations under the determinism rule. §5.5 one-time revalidation. §5.6 short-lived certificates. §5.1 rules out the anti-matter CRL. §5.7.2's *"the whole validity condition model is flawed"*, conceded *"not reflected"* (R-0104). | **Evidence for short-lived certificates as the default** (adopt 12), with timed revalidation as the fallback. The anti-matter design is excluded (§3 item 1). The verifier-decides question is open (open question 7). |
| **DEC-004** (tag language) | **Option 1 is §6.3.1.** | Evidence only. Option 1 is not implementable from RFC 2693 alone. §2 item 1 lists the six things a profile must add before it is. |
| **DEC-002** (native encoding) | None. The document defines no encoding (§3 item 8). | Not affected. The semantics adopted here are encoding-neutral. |
| **DEC-003** (issuer/subject identifiers on the wire) | `S1 = I2` over *"a public key (or its hash)"* is where identifier ambiguity becomes an authorization bug (§2 item 4). | **Pressure on DEC-003**: one canonical KeyId per principal is a precondition of R-M-05, not only of naming. |
| **R-M-12 / ADR-0001** (key-relative extension points) | SDSI's `(name K label)` is ADR-0001's `(key, local label)`, applied to principals' names (adopt 8). SPKI's own type words are global (§3 item 7). | **Precedent for ADR-0001**, plus open question 11. |
| **ARCH-0001 §4.1** `Threshold.members`, **ARCH-0002 P4** (repeatable hashing of sets) | AIntersect's printed set results are unordered (`SPKI-631-10`). Threshold members carry no stated order or distinctness. | Both need the same bytewise canonical order and a distinctness rule (§2 items 1, 3). Neither comes from the source. |
| **D-3** (*reduced CBOR, no IANA tags, COSE export only*) | See below. | **No header-by-header mapping applies.** One consequence for DEC-004 under D-3. |

### D-3

The `extract` skill requires D-3 to be addressed explicitly for COSE, CBOR and
envelope documents, with a header-by-header mapping. **RFC 2693 is none of the
three.** It defines no envelope, no headers, no encoding and no tags in the CBOR
sense, so there is no header to map. That is the finding, not an omission.

**There is one consequence, and it concerns DEC-004 option 1 under D-3.** If
the native encoding is reduced CBOR with major type 6 excluded, the `*`-forms of
§6.3.1 cannot be CBOR tags. They must be marked in-band, as SPKI itself does:
as a distinguished first element of an array (R-0016's *"type"*). So
`(* prefix <bytes>)` becomes an array whose first element marks the form and
whose second is a `bstr`. SPKI's structure already fits D-3's no-tags rule for
this reason. The open point is what the marker *is* under ADR-0001
(open question 11). Byte-string elements map to CBOR major type 2, and an
authorization list maps to an array. Neither needs a tag.

## 5. Open questions

1. **Is tag equality bytewise, with no exception?** §2 item 1 proposes it.
   The alternative is per-ordering equality for `alpha` (case?) and `date`
   (time zone?). Bytewise is the only rule that cannot make two verifiers
   differ, and it moves the burden to authoring. Confirm before DEC-004's ADR.

2. **Is the `*`-form algebra closed under AIntersect?** Prefix with range under
   `alpha` is a range, but only with a strict upper bound: `prefix "ab"` is
   `[ab, ac)`. Set with range filters the set. Range with range is a range.
   Closure therefore needs strict operators (`g`, `l`), which the source never
   defines. If closure fails for any pair, a reduction yields a value that
   cannot be written down, and so cannot go into a CRC or an attenuated grant.
   **This is a good first spike for DEC-004 option 1**: enumerate every pair of
   forms, with a property test against a set-based reference model.

3. **What does `numeric` mean over a byte string?** Unsigned big-endian
   integer, ASCII decimal, or something else (`SPKI-631-13`, schema D-10). The
   same question applies to `time` and `date`, and connects to R-0159's
   monotonic-time precondition.

4. **Which K, and whose order, in a threshold proof?** §2 item 3 proposes that
   the prover names the K and branches go in member-index order. Check this
   against `protocol.yaml`'s threshold flow and `state-machine.yaml` before
   adopting. `state-machine.yaml` OQ-13 (f) asks the related question of who
   sets unselected entries to (null).

5. **Does a key equal its own digest in `S1 = I2`?** §2 item 4 proposes
   canonicalising to KeyId first. If DEC-003 allows several digest algorithms,
   is that one KeyId per (key, algorithm), and does any equality across
   algorithms exist?

6. **How does a verifier come to trust a Certificate Result Certificate?**
   §2 item 8 proposes requiring the computing entity to be empowered for the
   tag by the verifier's own ACL. Is a CRC worth having at all in our model, or
   is a cached proof enough?

7. **Who decides validity, issuer or verifier?** §5.7.2 records Rivest's
   argument that *"it is the verifier and not the issuer who is taking a
   risk"* and leaves it *"not reflected in the SPKI structure definition"*
   (R-0104), possibly with *"inputs from both"*. R-O-02 needs a position. One
   option: the issuer sets the maximum interval, and the verifier may demand
   fresher evidence (a one-time revalidation) but never accept staler.

8. **May a name certificate define a name as a threshold subject?** §6.2 allows
   it (R-0132). §6.4's classes do not (schema D-03). A threshold-valued name is
   a group with a quorum, which is useful, but the safe-reduction rule of
   R-0182 was stated for names defined as keys. Does it stay terminating?

9. **R-M-10 against twenty-five years of OpenPGP.** RFC 2693 rejected integer
   depth on argument, and rfc-9580 deployed it. Is there a deployment study of
   trust-signature depth in practice (`ulrich-2011-openpgp-wot` is a
   candidate)? R-M-10's *"(or equivalent)"* leaves room. Does anything need
   it?

10. **Is delegation intersection really AND?** §2 item 3 proposes AND for the K
    branches (schema D-08). It is the only monotone choice, but the source
    gives no rule at all, and the rfc-2692 and SDSI records might. Check them
    before adopting.

11. **Under ADR-0001, are the algebra's own markers extension points?**
    `*`, `set`, `prefix`, `range` and the five orderings are a fixed grammar in
    SPKI. If they are grammar, they are fixed words in the profile, like CBOR
    major types. If they are extension points, ADR-0001 makes them
    key-relative, and the tag algebra becomes extensible per defining key.
    The former is simpler. The latter is what R-M-08's *"per profile"* might
    mean. This decides the D-3 marker question above.

12. **Source defects bearing on us.** Recorded elsewhere and not repaired:
    schema/README.md lists D-01 to D-13, state-machine.yaml lists the
    lifecycle gaps as open questions OQ-01 to OQ-26, and examples/README.md
    and protocol.md hold the rest. The ones that change a rule above are schema
    D-02, D-03, D-07, D-08, D-09 and D-10, together with `SPKI-52-04`,
    `SPKI-631-08` and `SPKI-657-12`. Schema D-11, the undefined `(tag …)`
    wrapper, is open question 15. protocol.md's gap §6.3.2 vs §6.1 also
    changes a rule: a deferred VIntersect carries online tests that the
    five-element 5-tuple has no slot for, and our R-M-05 tuple must choose one
    (the schema and `messages.yaml` carry them in the tuple's validity, as an
    optional `online_tests` list). One more matters for implementers: §6.4
    says name 4-tuples *"should be delivered in the order needed by the
    prover"* (R-0176), which reads as a slip for "by the verifier", since §6.3.4
    has the prover *supplying* the order. Do not build on the literal reading.

13. **What does an absent delegation field mean?** A certificate *"can
    contain validity conditions, authorization and delegation information"*
    (R-0006), so delegation is optional in a certificate or an ACL entry, but
    every 5-tuple carries *"Delegation: a boolean"* (R-0124), and the source
    never says what an absent field becomes (schema gap G-01). `messages.yaml`
    reads absence as FALSE, from R-0062's *"if delegation is TRUE"*. R-M-10's
    *"explicit boolean"* points the other way: require the field on every
    certificate and ACL entry, so that no default is ever applied. Decide in
    R-M-10's ADR.

14. **Can a name denote anything but a key?** The Abstract says the structures
    *"bind either names or explicit authorizations to keys or other
    objects"*, and the glossary has *"a name (with the understanding that the
    name is mapped by certificate to some key or other object)"* (R-0014).
    §6.1 narrows a name Subject to *"a name used to identify a public key"*
    (R-0123), and §6.2 gives a name 4-tuple's Subject no object-hash
    alternative (R-0132), so no 4-tuple can bind a name to an object, and name
    reduction (R-0177, R-0183) ends only at keys. `messages.yaml` (`subject`
    notes, item 3) noticed the contradiction; no defect list recorded it.
    R-M-03 names principals, so following §6.1 costs us nothing, but a profile
    that wants names for objects, such as content digests, needs a 4-tuple
    Subject form the source does not give. Decide with R-M-03.

15. **Is a 5-tuple Authorization the `(tag …)` form or its body?** §6.1 says
    only *"Authorization: an S-expression."* (R-0125), and §6.3.1 introduces
    authorizations as bare lists (R-0141, R-0147). Every `AIntersect` example,
    and every authorization §6.5.3, §6.5.7 and §7.7 name, is wrapped in
    `(tag …)`, a form the source never defines (schema D-11, G-11). The schema
    and `messages.yaml` take the wrapped form, so the bare §6.3.1 forms are tag
    bodies (`SPKI-631-01`, `-02`, `-04`). It matters because `AIntersect` of a
    wrapped and a bare authorization fails at the first element (`tag` against
    `ftp`): a profile that admitted both would deny mixed chains without saying
    why. Proposed: one form, the wrapped one, with the body as the unit of the
    algebra. Settle it with DEC-004.
