---
record: rfc-2692
kind: design-notes
title: "rfc-2692 — bearing on our design"
extracted: "2026-10-18"
reviewed_by: ""
---

# RFC 2692 — bearing on our design

RFC 2692 is the requirements memo the SPKI working group wrote before RFC 2693
answered it. A surprising share of our own requirements descend from it: the
refusal of X.509 / PKIX behind R-M-01 (RFC 2692 refuses ASN.1, which reaches
further: adapt 8), the key-or-hash principal of R-M-02, the
determinism argument behind R-M-05 and R-M-09, sign-as-transmitted (proposed
R-O-05), registry-free authorization vocabularies (ADR-0001), and the
minimal-disclosure rule that ARCH-0003's wallet has to honour. It is also the
first document in this library to test the KSA specifications against
requirements they do not yet meet: a revocation the verifier can find, positive
on-line validation, and a certifier who retires without taking his certificates
with him. This file is an audit in both directions.

**Things to hold while reading.**

1. **Nothing in the source binds.** `requirements.yaml` records a measured BCP 14
   count of zero, source and extracted. The memo is Experimental: *"This memo
   defines an Experimental Protocol for the Internet community. It does not
   specify an Internet standard of any kind."* (Status of this Memo). Its
   lowercase *should* and *must* are the working group's register, not RFC
   2119's. Wherever something below is adopted, **we** make it normative, in a
   SPEC or an ADR. A citation to RFC 2692 is a citation to a rationale.

2. **The source has three layers of text, and they weigh differently.** The
   group *"first established a list of things one might want to do with
   certificates (attached at the end of this document), and then summarized that
   list of desires into requirements"* (Abstract). So:
   - **[WG]**: the group's summary requirements, in the Charter, Background,
     General Requirements, Validity and CRLs and Implementation of Certificates
     (R-0001 to R-0049).
   - **[list]**: the List of Certificate Uses, which the source calls *"a
     brainstorming list, accumulated on the SPKI mailing list, of uses of such
     certificates"*; its entries are R-0050 to R-0150. The six bullets under "Other
     requirements" (R-0138 to R-0150) sit inside this list despite their
     heading. A list item is a use the design should be able to serve, not a
     rule. Declining one is a scope decision with a reason, not a breach.
   - **[OQ]**: the section's lead (R-0151) and the answers in Open Questions
     (R-0152 to R-0158). The section
     says the questions *"do not have answers provided by certificate definition
     or issuing alone"* (R-0151). The answers are statements of limits.

   Every item below carries its layer. Security Considerations is one sentence,
   *"Security issues are discussed throughout this memo."*, so its content is
   mapped where it stands: privacy (adopt 5, adapt 7), CRL determinism (adopt 9,
   adapt 1), sign-as-transmitted (adopt 6), key lending and non-repudiation
   (adopt 15).

3. **Our decisions are read from m-of-n `origin/main` at `643fba2`**
   (2026-10-16) with `git -C ../mofn show origin/main:<path>`, never from the
   working tree, which is on an unrelated branch. Every quote of ours below was
   checked against that commit. Short names used below:

   | name | path at 643fba2 | standing |
   |---|---|---|
   | ARCH-0001 v0.1.2 | `spec/ARCH-0001-authorization-attestation.md` | draft; §5's R-M, R-I, R-O rows are the requirements of record |
   | proposal | `spec/ARCH-0001-PROPOSAL-v0.2.0.md` | *"Status: proposed. Nothing in this document is accepted."* Source of DEC-002 option 5, R-O-05, R-M-11, R-M-12 |
   | ARCH-0002 v0.6.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P2, P3, P5, P6 provisional (MD-2); P4, P7 held |
   | ARCH-0003 v0.3.1 | `spec/ARCH-0003-wallet-object-model.md` | draft, *"Nothing here is accepted."* Requirements W-01 to W-25 |
   | SPEC-0001 to SPEC-0005, UC-0001 v0.1.0 | `spec/SPEC-000n-*.md`, `spec/UC-0001-ksa-use-cases.md` | draft specifications under ADR-0003; *"where a specification and an architecture document differ, the specification governs."* (SPEC-0001) |
   | ADR-0001, ADR-0003 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0003-fksa-convergence.md` | accepted |
   | ADR-0002 | `spec/ADR-0002-provisional-principles.md` | *"Status: proposed. Nothing here is accepted."* |
   | DECISIONS-0001 v0.3.0 | `project/DECISIONS-0001.md` | the register; accepts nothing |
   | MD-1 to MD-7 | `project/meetings/2026-09-28.md` | dated decisions |
   | 2026-10-12 minute | `project/meetings/2026-10-12.md` | recommendations only; its Decisions section reads *"(filled during meeting)"* |
   | GLOSSARY-0001, CONTRIBUTING | `project/GLOSSARY-0001.md`, `CONTRIBUTING.md` §5 | process |

   **One status conflict touches this file.** ADR-0003 calls R-O-05 accepted:
   *"consistent with accepted R-O-05"*. DECISIONS-0001 item 4 says that until
   the v0.2.0 proposal is accepted, *"R-M-11/R-O-05/R-O-06 have no force"*, and
   ARCH-0001 v0.1.2 §5.3 has no R-O-05 row. This file treats R-O-05 as
   **proposed** throughout. The conflict is open question 16.

4. **Numbering collisions.**
   - A bare `R-NNNN` is this record's `rfc-2692#R-NNNN`. RFC 2693's are written
     `2693 R-NNNN`. **m-of-n uses `R-0003` for its cipher-suite research
     report** (ARCH-0003 §3.3, *"per R-0003 §5"*; SPEC-0001 §8.2) and `R-001`
     for its survey. Here those are written "mofn report R-0003". They have
     nothing to do with `rfc-2692#R-0003`, the Charter's list of applications.
   - `R-M-NN`, `R-I-NN`, `R-O-NN` are ARCH-0001 §5 (ours), except R-M-11, R-M-12
     and R-O-05, which are proposal §7 rows (R-M-12 accepted by ADR-0001 and
     relocated to ARCH-0002 P1).
   - `MD-n` are dated meeting decisions, renamed from `D-n` on 2026-10-11
     (GLOSSARY-0001: *"A bare `D-3` in older text is `MD-3`, never `D3`"*).
     `D0` to `D10` are deliverables. ADR-0003 numbers its own five decisions
     D1 to D5; they are always written "ADR-0003 D5" here.
   - `P1` to `P7` are ARCH-0002 principles; `W-NN` are ARCH-0003 draft
     requirements; `V1` to `V9`, `TV-n`, `N-n` and `DV-1` are SPEC-0002's
     verification steps and vectors.
   - `SR-…` ids are this record's `examples/vectors.yaml`. "Item N" counts the
     List of Certificate Uses 1 to 62 as `requirements.yaml` does (item 7 has
     sub-items 7.1 to 7.3); "Other requirements item N" counts that sub-list 1
     to 6; "Open Question N" is the source's N-th question with its answer.
   - DEC-002 options 1 to 5 and DEC-004 options 1 to 3 are always prefixed.

5. **Nothing here decides a DEC.** CONTRIBUTING §5: *"Only an ADR accepts a
   decision."* MD-3 narrowed DEC-002 to option 5, and DECISIONS-0001 item 2
   adds *"Still open: a narrowing is not an acceptance, and no ADR exists."*
   ADR-0003 D2 put option 5's encoding into SPEC-0002 and says of itself
   *"This ADR does not accept DEC-002"*. The DEC-002 subsection of §4 is
   evidence for the DEC-002 ADR (DECISIONS-0001 item 4b), and where RFC 2692
   favours another option it names it.

6. **The label (inferred)** marks anything the source implies rather than
   states, and every consequence we draw that goes beyond its words. Source typos are quoted
   as printed: *"singing"* for signing (R-0066), *"I'm the a"* and *"posses"*
   (R-0119), and *"a this"* (R-0128).

---

## 1. What we adopt

1. **A certificate answers an authorization question; a name rarely matters.**
   [WG] Background: *"The SPKI team directly addressed the issue of \<name,key\>
   bindings and realized that such certificates are of extremely limited use for
   trust management."* and *"a person's name is rarely of security interest"*
   (Background ¶2; argument, not an R-entry, whose operative consequences are
   R-0005 and R-0007). R-0005: *"A user of a certificate needs to know whether a
   given keyholder has been granted some specific authorization."* R-0007: *"The
   main purpose of an SPKI certificate is to authorize some action, give
   permission, grant a capability, etc. to or for a keyholder."*

   Ours: ARCH-0001 G1, *"Key-centric principals; names are not globally unique
   identifiers."* SPEC-0004 §10.4 keeps **names** and **authorization** as
   separate verdict lines, and authorization passes only on a path of keys.
   SPEC-0001 §7.3: *"It MUST NOT render a key by the key's self-asserted label
   alone"*.

   **Consequence:** the authorization result must never depend on a name. A
   conformance test that changes only names in a presentation (labels,
   `self.label`, name attestations) must leave the authorization line
   unchanged. UC-1's first must-fail row is the positive form: *"T, never
   delegated, signs the same attestation"* is `no-path`.

2. **The keyholder is its key, or a collision-free hash of it.** [WG] R-0008:
   *"The keyholder is most directly identified by the public key itself,
   although for convenience or other purposes some indirection (delayed binding)
   may be employed."* R-0009: *"That indirection can be via a collision-free hash
   of the public key or via a name, later to be resolved into a key."* RFC 2693
   realised both (2693 R-0028, R-0029).

   Ours: R-M-02, *"A principal MAY be identified solely by key or key
   digest."* SPEC-0002 §4.5 makes the kid the SHA-256 of the key's encoding, and
   §13.4 says *"Identifiers MUST NOT be truncated in signed or hashed bytes."*

   **Consequence:** "collision-free" is a property the identifier has to keep,
   so truncation is a correctness defect, not a size optimisation. ARCH-0003 §12
   item 2 records that *"the prototype truncates to 16 bytes; a meaningful
   identifier should be a full, algorithm-tagged digest."* RFC 2692's qualifier
   is the reason to fix the prototype, and DEC-003's canonical key bytes are the
   precondition (SPEC-0002 §6.3 fixes them for suite 1). The name indirection is
   narrowed (adapt 5). Tests: SR-GEN-01, SR-GEN-C08.

3. **A new authorization needs nobody's permission.** [WG] R-0010: *"The
   definition of attributes or authorizations in a certificate is up to the
   author of code which uses the certificate."* R-0011: *"The creation of new
   authorizations should not require interaction with any other person or
   organization but rather be under the total control of the author of the code
   using the certificate."*

   Ours: ADR-0001, *"Native extension points — type identifiers, predicate
   types, tags, header parameters — are identified relative to a defining
   principal, as a `(key, local label)` pair. The native model depends on no
   centrally allocated registry for their meaning."* ARCH-0002 P1: *"neither
   needs permission from a registry to exist"*. SPEC-0003 §5.2: *"Labels are
   local to their definer (ARCH-0002 P1): `(DefinitionId, label)` is globally
   unique; the label alone is not."*

   **Consequence:** creating an authorization type is writing a definition with
   a `type` entry, computing its DefinitionId and signing `define` (SPEC-0003
   §11.1). No step may consult a registry. SR-GEN-C01 (creation needs a
   registry, a violation) and SR-GEN-C02 (the code author alone, conforming)
   belong in the conformance suite.

   **A precision for ADR-0001's lineage (inferred).** ADR-0001 says *"SDSI
   localized principal names. Nobody localized type names."* In 1999 RFC 2692
   localized authorization definitions to *"the author of code which uses the
   certificate"*. That is localization by authority, not by key: the definition
   belongs to whoever writes the verifying code, and it is neither portable nor
   attributable. RFC 2692 is precedent for the **registry-free** half of
   ADR-0001, not the **key-relative** half, and ADR-0001's "nobody" holds only
   for the second. Note also *who* defines. RFC 2692 gives the definition to the
   verifier's code author; SPEC-0003 gives it to a definer key, who may or may
   not be the verifier (adapt 9).

4. **Certificates go from holder to verifier; repositories are the holder's
   choice.** [WG] R-0012: *"Because SPKI certificates might carry information
   that the keyholder might not want to publish, we assume that certificates
   will be distributed directly by the keyholder to the verifier."* R-0013:
   *"If the keyholder wishes to use a global repository, such as LDAP, the global
   PGP key server or the DNS database, that is up to the keyholder and not for
   the SPKI WG to specify."*

   Ours: SPEC-0001 §8.1, *"A presentation is what a persona hands a relying
   party: the statements needed to answer an ask — the claim, its delegation
   path, any reviews and approvals — and the definitions needed to render and
   type-check them."* SPEC-0001 §9.1: *"A directory, location or log is a
   locator only (SPEC-0003 §4.4)."* ARCH-0001 lists as non-goal NG4 *"Require a
   blockchain or any specific transparency log."*

   **Consequence:** an evaluation must be completable from one presentation and
   the wallet's own store, offline. No SPEC may make a repository lookup
   necessary for a **yes**. Tests: SR-GEN-02, SR-GEN-C11. What this choice costs
   revocation is adapt 1.

5. **One credit card, not the wallet.** [WG] R-0014: *"Because SPKI
   certificates will carry information that, taken together over all
   certificates, might constitute a dossier and therefore a privacy violation,
   each SPKI certificate should carry the minimum information necessary to get a
   job done."* R-0015: *"The SPKI certificate is then to be like a single key
   rather than a key ring or a single credit card rather than a whole wallet."*
   R-0016: *"The keyholder should be able to release a minimum of information in
   order to prove his or her permission to act."* RFC 2693 realised it as *"it
   is desirable that authorizations be limited to one per certificate"* (2693
   R-0051).

   Ours: ARCH-0003 W-09, *"A statement made in a context is signed only with a
   key enabled for it; a presentation discloses only statements held in that
   context."* SPEC-0001 §12: *"A presentation discloses exactly its contents;
   wallets show it before sending."*

   **The metaphor's roles, kept straight (inferred).** RFC 2692 says the
   *certificate* must be a card and not a wallet. ARCH-0003's wallet is the
   *holder*, which RFC 2692 never constrains: ARCH-0003 §2's *"Apple Wallet at
   the surface: cards you carry, show and check."* is the same picture with the
   roles right. What the metaphor constrains is each statement and each
   presentation.

   **Consequence:** (a) a presentation builder selects the minimum set of
   statements that makes the ask's answer **yes**, not everything held in the
   context; (b) templates default to one required attribute, because SPEC-0002
   §8.5's `has: [+ attribute]` allows many and each extra attribute is
   disclosure. The linkage cost that the kid adds is adapt 7. Tests: SR-GEN-03,
   SR-GEN-C03, SR-GEN-C04.

6. **Sign exactly the bytes that are sent; never reformat to check.** [WG]
   R-0044 and the first clause of R-0045: *"A certificate should be signed
   exactly as it is transmitted. There should be no reformatting called for in
   the process of checking a certificate's signature"*.

   Ours: SPEC-0002 §5, *"The envelope exists so that a verifier can verify
   before it decodes."* Its note on FKSA rejects the alternative: *"Because a
   verifier would have to decode, remove a field, and re-encode before it could
   check the signature — canonicalising during verification, exposing its
   decoder to unauthenticated input, and creating a second encoder whose output
   must match the producer's byte for byte."* ADR-0003: *"FKSA signs the
   re-encoded statement minus its signature; KSA transmits the signed bytes as
   they were signed and verifies them before decoding"*.

   **RFC 2692 is the oldest citation for SPEC-0002 §5's departure from FKSA,**
   and SPEC-0002 should cite it. FKSA's *"signature over the statement minus
   `signed`, re-encoded"* (SPEC-0002 Appendix C) is exactly the reformatting
   R-0045 excludes.

   **The domain-separation label is not a reformatting (inferred).** The signed
   input is `DS ‖ TBS`, and SPEC-0002 §6.4 says the label *"is prepended to the
   bytes being signed and is never transmitted."* The certificate's own bytes
   are signed as transmitted; a fixed 16-octet prefix is added.

   **Consequence:** no verifier code path may rebuild a TBS from decoded fields.
   SPEC-0002's N-1, a non-canonical TBS whose signature verifies, must fail at V5
   and never be re-encoded into passing. Tests: SR-IMP-C01,
   SR-IMP-C10. One clause of SPEC-0002 breaks the rule: abbreviated transport
   (open question 8).

7. **The structure definition, not the reader's error messages, constrains the
   issuer.** [WG] R-0040: *"In particular, the structure should be specific
   enough that the creator of a certificate is constrained by the structure
   definition, not by complaints (or error messages) from the reader of a
   certificate."*

   Ours: SPEC-0002 §7.1, *"The statement map is closed: a key not listed above
   MUST cause rejection."* SPEC-0003 §7.2's issuing interface *"checks
   conformance before signing"*. ARCH-0002 P5: *"a failure at any level is a
   rejection, never a repair"*.

   **Consequence:** the issuing wallet runs SPEC-0003 §7.1's conformance check
   and SPEC-0002 V7 and V8 on its own output before it signs. A producer that
   learns of its errors from relying parties' `template` reason codes is the
   design R-0040 rules out. Test: every acceptance-line must-fail row in UC-1
   must also be refused at issuance.

8. **Any empowered keyholder issues; there is no issuer of last resort.** [WG]
   R-0033: the certificates *"should be generated by any keyholder empowered to
   grant or delegate the authorization in question"*. Ours: ARCH-0003 W-14 and
   ADR-0003 D3, realised in SPEC-0004 §1,
   *"There is no global root, no default trust list, and no step at which merely
   discovering a key makes it trusted."* Tests: SR-IMP-C08,
   SR-IMP-C09.

9. **Determinism is the test any validity mechanism must pass.** [WG] RFC 2692
   describes the CRL it refuses: *"Its method of transmission is not specified.
   If it encounters some certificate that it lists, then it annihilates that
   certificate."* (Validity and CRLs ¶2, description, not an R-entry), and
   rules: *"Such a CRL leads to non-deterministic program behavior."* (R-0024).
   It then states three conditions (R-0025 to R-0027, quoted in adapt 1) and the
   result: *"Under this set of requirements, behavior of certificate validation
   is deterministic (aside from the question of clock skew)."* (R-0028). RFC 2693
   realised the conditions (2693 R-0077 to R-0083) and the principle, *"Every
   authorization computation is deterministic, under SPKI rules."* (2693
   R-0075).

   Ours: SPEC-0004 §3, *"An evaluator MUST produce the same answer for the same
   inputs"*; R-M-05; and the clock-skew caveat handled by making time an
   explicit input (SPEC-0004 §8).

   **We adopt RFC 2692's criterion, and it is stronger than ours.** RFC 2692 asks
   that validation be deterministic given the certificate and the time.
   SPEC-0004 asks only that it be deterministic given whatever statement set the
   wallet happens to hold. The gap between the two is the "wandering"
   revocation RFC 2692 refuses, and our `revoke` sits in it (adapt 1).

10. **Every freshness instrument has its own lifetime; zero is impossible; "one
    use" only inside a challenge/response.** [WG] R-0031: *"Any CRL or
    revalidation instrument must have its own lifetime."* R-0032: *"A lifetime of
    0 is not possible because of communication delays and clock skews, although
    one can consider an instrument whose lifetime is "one use" and which is
    delivered only as part of a challenge/response protocol."*

    Ours: R-M-09 and R-O-02, realised in SPEC-0002 §7.3, *"A statement is valid at time t if and only if
    `not-before ≤ t` when `not-before` is present and `t < not-on-or-after` when
    `not-on-or-after` is present."* SPEC-0001 §8.1: *"A relying party that
    supplied a nonce MUST check that the presentation carries it and that
    `audience` is its own kid."*

    **Half-open validity settles a case the source leaves open (inferred).**
    Under `[not-before, not-on-or-after)` an instrument with equal bounds is
    valid at no instant, which makes R-0032's impossible zero lifetime
    mechanical. Two instruments dated `[a, b)` and `[b, c)` share no instant, so
    *"the dates of a sequence of CRLs must not overlap"* can be checked without
    guessing an endpoint convention. SR-VAL-C03, which records back-to-back dates
    as undecided by the source, **conforms** under SPEC-0002 §7.3. The same rule
    repairs RFC 2693's closed intervals (rfc-2693 design notes, adapt 2).

    **Consequence:** every status or revalidation statement we define (adapt 1,
    adapt 2) uses SPEC-0002 `valid` with both bounds required. Tests: SR-VAL-04,
    SR-VAL-C03, SR-VAL-C10, SR-VAL-C11.

11. **A long-term key in hardware certifies short-term keys at login.** [list]
    Item 53, R-0123: *"if you only use the smart card at "login" time to certify
    a short-term key pair, you get high performance and low exposure of the long
    term key."* Ours: ARCH-0003 §3.2, *"Other keys — per context, per syntax, per
    device — are delegated from it by ordinary scoped delegation"*; SPEC-0001
    §3.1, *"so a compromise of an operational key is bounded by the scope and
    validity it was given."*

    **Consequence:** a wallet supports an identity key that signs only `trust`
    and `rotate`, held with `custody: hardware` (ARCH-0003 §3.3), and
    short-validity operational keys for everything else. What RFC 2692 says this
    does to delegation control is adapt 6 and reject 5. Tests: SR-USE-58.

12. **Ephemeral authority, with the audit identity in the application's own
    vocabulary.** [list] Item 50, R-0113: *"I'm that same sysadmin, I want an
    ephemeral certificate that grants me root access to certain systems for the
    day, or the week, or..."*; R-0114: *"the audit identity should be in the
    domain of the particular application"*; R-0115: *"For instance an "is a
    system administrator of this host" certificate would probably want to include
    an audit identity, so you can figure out which of your multiple admins
    screwed something up."*

    Ours: UC-4's delegation to an agent, *"until 17:00, depth 0"*; SPEC-0004
    §10.3, whose `because` *"MUST name: the digests of the statements used; for
    each covered attribute, the path as the sequence of anchor and
    trust-statement digests with the scope after each hop"*.

    **Consequence (inferred):** "the domain of the particular application" is P1
    applied to audit identities. The host's operator defines an `audit-id` type
    in its own definition, and the day-long `trust` statement carries it as an
    attribute; nothing global names the administrator. Ephemeral root access is
    therefore expressible today, as a `trust` with a one-day window and depth 0,
    and is **not** one of the uses we decline. Tests: SR-USE-53, SR-USE-54.

13. **Name-space owners delegate mail addresses.** [list] Item 55, R-0128: *"I
    am the current legitimate owner of a this DNS name or subtree."* (sic). Item
    56, R-0129: *"I am the legitimate receiver of mail sent to this rfc822 email
    address."*, with R-0130: *"this might need to be signed by a key which itself
    had been certified by the appropriate "DNS name owner" certificate"*. Item 54,
    R-0126: *"I am the current legitimate owner of a particular chunk of Internet
    address space."*

    Ours: MD-1's email-delegation schema scenario, UC-5, *"a relying party believes an address belongs to a key because
    the domain's delegate says so."* SPEC-0003 §6.3: *"This is the type behind
    the email-delegation scenario in UC-0001 §UC-5: a domain owner trusted about
    `*@foo.com` may delegate `*@eng.foo.com`, and not `*@bar.com`."* Item 54 is
    UC-6 over SPEC-0003 §6.2's `ip-prefix`.

    **UC-5 is RFC 2692 item 56, realised.** This is the earliest statement this
    library holds of the sponsor's original scenario. RFC 2692 lets ownership
    empower, and UC-5 does not: adapt 4. Tests: SR-USE-60, SR-USE-61,
    SR-USE-62, SR-USE-63.

14. **Trust starts where the relying party chooses, needs no bureaucracy, and
    keys are cached locally.** [list] Other requirements item 1: *"Trust model
    must be a web (people want to choose whom they trust). People must be able to
    choose whom they trust or consider reliable roots (maybe with varying
    reliabilities)."* (R-0138, R-0139). Item 3: *"Some applications (e.g., host
    authentication) require extremely light (or no) bureaucracy. Even
    communication with the central administrator may be a problem."* (R-0141,
    R-0142). Item 5: *"Keys will need to be cached locally to avoid long delays
    fetching frequently used keys."* (R-0146). [WG] R-0004: *"It is intended that
    the Simple Public Key Infrastructure will support a range of trust models."*

    Ours: SPEC-0004 §1, *"trust begins at anchors the relying party chose, in the
    context where it chose them"*; ADR-0003 D4, *"Every evaluation is relative to
    one context's anchors."*; SPEC-0004 §3, *"Nothing else — no network, no clock
    other than the evaluation time, no ordering of inputs — may affect the
    result."*; SPEC-0002 §10's key store.

    **The reason is in the source, and it is Kohnfelder's.** *"Kohnfelder took
    that suggestion and noted that an on-line service has the disadvantage of
    being a performance bottleneck. To replace it, he proposed creation of
    digitally signed directory entries which he called certificates."*
    (Background ¶1, history, not an R-entry). An evaluator that never blocks on
    the network keeps that argument.

    **Consequence:** anything on-line (status, revalidation, revocation) is
    fetched before the ask and enters the evaluation as an input statement. The
    evaluator itself never fetches. "With varying reliabilities" is not adopted
    (reject 6). Tests: SR-BG-01, SR-USE-70, SR-USE-72, SR-USE-74.

15. **The Open Questions' answers, kept as stated limits.** [OQ]
    - Open Question 1, R-0152: *"certificate format, contents or issuing
      machinery can not ensure the protection of a user's private key or prove
      whether or not a private key has been stolen or misused."* Ours: SPEC-0004
      §10.4's limit line, *"this establishes who said it and whether they were
      entitled to say it; it does not establish that it is true."*, and SPEC-0001
      §10, *"Correct signatures by an entitled key on false claims are not
      detected"*. SPEC-0004 §7.2's compromise rule leans on exactly what R-0152
      says a certificate cannot prove: open question 6.
    - Open Question 2, R-0153: *"Certificates might be employed to carry
      information in a tamper-proof way, but building the database necessary to
      record all house titles and all liens is a project not related to
      certificate structure."* Ours: NG4 and the optional R-O-04. Registers are
      not statement structure.
    - Open Question 3, R-0155 to R-0157: a negative fact travels as a positive
      attribute asserted by a party able to determine it, by a method outside the
      certificate. Applied to our `none` criterion in adapt 10.
    - Open Question 4 and item 53. R-0158: *"This is a potential flaw in any
      system providing authorization and an interesting topic for study."*
      R-0125: *"Maybe we need a "delegation-allowed" bit -- but there's nothing
      to stop someone who wishes to delegate against the rules from also loaning
      out their private key."* Ours: SPEC-0001 §10, *"Social engineering of
      delegation — a patient attacker who earns a delegation, as in the 2024
      xz-utils incident — is limited by narrow scope, shallow depth, short
      validity and approval processes, not prevented."*

    **Consequence:** the threat model lists key lending and signing proxies as an
    accepted residual risk. For high-value authorizations, such as item 46's
    *"permission to write digitally signed prescriptions for drugs"* (R-0109),
    hardware custody with device attestation (SPEC-0004 §4.5) makes lending
    harder and not impossible, because RFC 2693 already noted *"This doesn't
    prevent the user from setting up a signing oracle"* (2693 R-0063). Tests:
    SR-OQ-01 to SR-OQ-06.

## 2. What we adapt, and how

Each item names what RFC 2692 asks, where the KSA specifications stand, and the
change a later engineer would make.

1. **A revocation the verifier can find.** [WG] RFC 2692's requirement:
   *"Therefore, we take as a requirement that if SPKI uses CRLs, then the
   certificate that uses it must explicitly tell the verifier where to find the
   CRL, the CRL must carry explicit validity dates and the dates of a sequence of
   CRLs must not overlap."* (R-0025 to R-0027).

   Ours: ADR-0003 D5, *"Issuer revocation is adopted"*, with *"Short validity
   remains recommended; revocation distribution is not solved by this
   decision."* SPEC-0004 §7.1: *"An evaluator decides with the revocations it
   holds. It cannot know of one it has not received; the answer's reasons MUST
   state how many revocation statements were considered, and wallets SHOULD
   obtain current revocations before a high-stakes evaluation. Short validity
   windows remain RECOMMENDED."* And: *"A `revoke` that targets a `revoke` has
   no effect: revocation is permanent."*

   **Finding: under RFC 2692's test, a KSA `revoke` is the minimal CRL with one
   entry.** Against the three conditions:
   (a) a statement does not tell the verifier where its revocations live.
   SPEC-0002 §7.3's `valid = { ? 1 not-before: time, ? 2 not-on-or-after: time,
   ? 3 issued: time }` has no such field, although ARCH-0001 §4.1's `Validity`
   had one, *"{ not_before?, not_after?, online_check? }"*. (b) A `revoke` must
   carry `valid` (SPEC-0002 §7.1), and SPEC-0004 §7.1 applies its window
   (*"`r` valid at `t`"*), but an end date is optional, a `revoke` cannot itself
   be withdrawn (*"revocation is permanent"*), and it is unsequenced. (c) There is no sequence, so
   non-overlap has nothing to apply to. SPEC-0004 §3's determinism survives only
   because the non-determinism has moved into the input, namely which
   revocations happened to reach the wallet. That is RFC 2692's objection, and it
   is the attack RFC 2693 names: an adversary suppresses revocation by *"merely
   network tampering"* (2693 R-0073).

   **It compounds with adopt 4 (inferred).** RFC 2692 assumes certificates go
   *"directly by the keyholder to the verifier"* (R-0012). The keyholder is the
   *subject* of an attestation; the revoker is its *speaker* (SPEC-0002 §8.7,
   *"Only that statement's speaker may revoke it"*). A presenter has no reason
   to carry the revocation of its own credential, so in the presentation
   channel a revocation arrives only if the wallet fetches it from the speaker,
   and nothing in the statement says from whom or where. R-0025 is the half of
   the design we did not take.

   **Adaptation.** Two routes, which open question 1 chooses between:
   - **(a) Name the status source in the statement**, as RFC 2693 narrowed
     R-0025: *"The certificate must list the key (or its hash) that will sign the
     CRL"* (2693 R-0077) and *"may give one or more locations where that CRL
     might be fetched."* (2693 R-0078). Concretely: restore ARCH-0001's
     `online_check?` as an optional `valid` field naming a status kid and
     optional locators. A statement carrying it is valid at `t` only if the input
     set holds a status statement by that kid, about this statement, valid at
     `t`, with both bounds present; successive status statements from one kid
     tile under half-open dates (adopt 10). Validation is then deterministic in
     RFC 2692's sense: a certificate that names a source cannot pass without a
     current instrument, and no instrument can arrive as a surprise (2693 R-0082,
     R-0083).
   - **(b) Cap validity instead**, R-O-02's preference made binding. Templates
     whose statements matter set SPEC-0003 `max-validity`, and a profile makes
     `not-on-or-after` required; SPEC-0002 §7.1 makes `valid` only
     *"RECOMMENDED; REQUIRED for `rotate` and `revoke`"*. `revoke` stays a
     best-effort accelerator. Its reasons line should then report the age of the
     revocation data, not only *"how many revocation statements were
     considered"*, because of item 6 of Other requirements: *"This interacts with
     caching."* (R-0150). A count of zero does not tell the relying party whether
     anyone looked.

   **Consequence for the SPECs:** route (a) changes evaluation results, which is
   MAJOR under SPEC-0004's version policy; route (b) is a profile rule plus a
   change to the reasons field. Either should cite R-0024 to R-0028. **Test that
   shows the defect today:** SPEC-0004 Appendix A's ask 2, run in two
   wallets with the same anchors and statements except that only one holds TV-7
   (Alice's revoke), answer **yes** and **no** at 2026-10-22T12:00:00Z (inferred);
   under route (a) both must answer alike. Also SR-VAL-01, SR-VAL-C01 to
   SR-VAL-C07.

2. **Positive on-line validation, from machinery we already have.** [WG] R-0023:
   *"It may also be necessary to have on-line refinement of validity."* R-0029:
   *"A CRL is a negative statement."* R-0030: *"SPKI should support both
   positive and negative on-line validations."* And the reason, in ¶3 of the
   section (not an R-entry): *"These have been replaced in the retail world by
   positive statements -- on-line validation of a single check, ATM card or credit
   card."*

   Ours: R-M-09, *"Validity intersection SHALL be defined (time window ∩
   optional online checks)."* SPEC-0002 has `revoke`, which is negative, and
   nothing positive; `valid` has the window and no online checks.

   **Adaptation (inferred, buildable now).** A positive revalidation is an
   `attestation` about the same target, assigning a status type (for example
   `status = current`) with a short `valid` window, made by a status key. The
   *requirement* to hold one is bound through the template's `approval` process
   (SPEC-0003 §7): one input from a listed panel containing the status key, input
   kind 4, rule `[1, status, 1, where status == current]`. SPEC-0005 §6.1 item 5
   already requires every input statement to satisfy *"`s` is valid at `t` and
   not revoked;"*, so the attestation is covered only while a fresh revalidation
   exists. This also keeps RFC 2693's rule *"However, in SPKI, the certificate
   issuer must specify the issuer of validity confirmations."* (2693 R-0072),
   because the definer of the template chose the status key.

   **Limits.** SPEC-0005 §6.4 evaluates an approval process for *the statement's
   target*, so the revalidation vouches for the target (the release) rather than
   for one particular statement. SPEC-0005's input kinds are written as *"e.g.
   [9] review, [10] approve, [11] aggregate"*, so kind 4 is allowed but
   untested. And there is no nonce field in a statement, so R-0032's one-use
   instrument cannot be built this way (open question 3).

   **Consequence:** write it as a use case ("revalidated attestation") with
   vectors. If it works, R-M-09's "online checks" exist without a new field, and
   SR-VAL-C15, which expects a design with negative and no positive on-line
   validation to fail R-0030, stops failing against KSA.

3. **A certifier can retire without taking his certificates with him.** [list]
   Other requirements item 4: *"Especially in lower-end applications (e.g. host
   authentication) the people generating the keys (e.g., administrators) will
   change, and you will no longer want them to be able to certify. On the other
   hand, you will usually also not want all keys they have generated to expire.
   This may imply a "certification right expiration" certificate requirement,
   probably to be implemented together with notary services."* (R-0143 to
   R-0145).

   Ours: SPEC-0004 §6.3 follows a trust statement only if *"`s` is in the
   statement set, valid at the evaluation time, and not revoked (§7.1);"*, and
   §10.2 needs a path *"whose `cap` is later than the evaluation time"*. UC-6's
   must-fail row: *"After Alice revokes Dave's delegation → `revoked`."* SPEC-0001
   §5.1 lists a key state *"(active, retired, compromised)"*.

   **Finding: KSA does what R-0144 says you usually do not want.** When an
   administrator's delegation lapses or is revoked, every attestation that
   administrator ever made stops being covered, because paths are judged at the
   evaluation time. UC-6's must-fail row shows the mechanism: Dave's earlier
   assignment to Bob dies with Dave's delegation. That is right when a
   delegation is revoked for cause. R-0143 and R-0144 describe the benign case,
   an administrator who moves on, and KSA has no way to say which of the two it
   is. Rotation already has the semantics R-0144 asks for, *"The old key verifies
   the past only."* (SPEC-0004 §7.2), but only for a key that has a successor.
   The `retired` state has no evaluation rule anywhere in SPEC-0004.

   **Adaptation.** Give `retired`, or an explicit "stops certifying" statement,
   rotation's semantics without a successor: statements issued before the
   retirement keep their paths, and later ones do not. RFC 2692 names the catch
   itself, *"probably to be implemented together with notary services"*,
   because "issued before" is only as good as the evidence of issuance, and
   SPEC-0004 §7.2 says `issued` *"is not evidence of when a statement
   existed."* So the rule preserves a statement only when it carries independent
   time evidence (SPEC-0001 §11's transparency-log receipt or timestamp token),
   and falls back to today's behaviour otherwise.

   **Consequence:** this changes evaluation results (MAJOR for SPEC-0004) and
   belongs with ADR-0003 D5's follow-up. UC-6's revocation row stays, as the
   for-cause case. A second row beside it covers benign retirement: Dave stops
   certifying, and his earlier assignment to Bob still passes when it carries
   timestamp evidence. Tests: SR-USE-73, SR-USE-C04, SR-USE-C05.

4. **Ownership is not authority.** [list] In item 56, RFC 2692 lets an ownership
   certificate empower a key to certify addresses (R-0130, quoted in adopt 13).
   Ours: R-M-04 and ARCH-0002 P6; UC-5's must-fail note on `trust` and attestation, *"holding one never
   implies the other"*.

   **Adaptation (inferred):** an attestation that a key owns `foo.com`, which is
   R-0128's certificate, never empowers that key. Empowerment is a `trust`
   statement about a `dns-name` or `email` range, from a key the context trusts.
   A translator that imports an RFC 2692-style "DNS name owner" certificate emits
   an attestation, and any authority it implies comes from a local anchor that
   names the mapping, which is the rule the rfc-2693 notes apply to implicit
   authorizations (their reject 5).

   **The reverse lookup, adapted.** R-0131: *"This is in case I know someone owns
   a particular e-mail address but I don't know their key."* An ask in SPEC-0004
   §10.1 takes a `subject`, so it can check that a key has an address but cannot
   find which key does. The adaptation is discovery (SPEC-0001 §9.1: directory,
   introduction), which finds candidate keys and confers nothing, followed by one
   ask per candidate. **Consequence:** a wallet's "find by address" view shows
   its results as known and not trusted until an ask returns **yes**
   (SPEC-0001 §9, *"Discovery never confers trust."*).

5. **Names: bind a key to names; resolve a name to a key only by discovery.**
   [WG] R-0019: *"One attribute of a keyholder is a name. There are names the
   keyholder prefers to be called and there are names by which the keyholder is
   known to various other keyholders."* R-0020: *"An SPKI certificate must be
   able to bind a key to such names."* R-0021: *"The SDSI work of Rivest and
   Lampson has done an especially good job of defining and using local name
   spaces, therefore if possible SPKI should support the SDSI name construct."*
   (this quote crosses the page 3/4 break). [list] Item 7.2, R-0064: *"this
   certificate declares only a name or nickname by which the key's owner likes to
   be addressed."* Item 7.3, R-0067: *"It is for my use only -- never given out
   -- and is a signed certificate to prevent tampering with my own private
   directory of keys."* (this quote crosses the page 6/7 break).

   Ours: ARCH-0002 P6 makes a name an attested string. SPEC-0002 §8.3: *"`label`
   is a display string, not a binding."* GLOSSARY-0001 defines the speaker as *"A
   key, a key hash, or an alias resolving to one."*, while SPEC-0002's `says` is
   a kid only.

   **Adopted:** R-0020's binding, as an attestation by a speaker about a key
   (P6). R-0019's two kinds of name map onto `self.label` (the name the keyholder
   prefers, R-0064) and onto other keys' attestations plus the wallet's own label
   (the names others know it by).

   **Narrowed:** delayed binding by name (R-0009's second half) and the SDSI
   name as a subject (R-0021). SPEC-0002 §7.2 has no name target, and `says` is
   a kid, although ARCH-0001 §4.1's `Principal` includes `Name` and GLOSSARY-0001
   allows an alias as speaker. A grant to "Alice's bob" that follows whatever key
   Alice later binds to "bob" cannot be written. RFC 2692 says only *"may be
   employed"*, so this is a permitted narrowing, but it narrows R-M-03 as
   ARCH-0001 wrote it, and SPEC-0002 made it without saying so (open question
   12).

   **The personal binding, adapted (inferred).** R-0067 signs the private
   directory to prevent tampering. Ours are unsigned: ARCH-0003 §9 keeps
   `trusts/<context>.yaml` as *"unsigned anchors — owned personas only"*, and
   SPEC-0001 §5.4 keeps private notes. SPEC-0001 §10 says *"Anchor injection is
   defeated by acceptance (SPEC-0004 §4.4), not by signatures."*, but a process
   that can write the wallet's files skips acceptance altogether. The adaptation is to prefer
   SPEC-0004 §4.3's *own statement* source, a trust statement signed by an owned
   persona, over unsigned local anchors, or to MAC the anchor and label files
   under a wallet key so that a tampered anchor fails on load. **Consequence:**
   one integrity check over the wallet store at load. Test: edit an anchor file
   out of band, and evaluation in that context must refuse. Vectors: SR-USE-07
   to SR-USE-10, SR-GEN-C09, SR-GEN-C10.

6. **Key equivalence is delegation, and has to be granted as delegation.**
   [list] Item 53, R-0122: *"This signed-key should be considered equivalent to
   the certifying-key until this certificate expires for the following purposes
   ..."*; R-0124: *"I'll note here that this flies in the face of attempts to
   prevent delegation of certain rights."*

   Ours: SPEC-0002 §8.6, *"Without `may-delegate`, trust is one hop: the trusted
   key may attest, but trust statements it issues are not followed."* SPEC-0004
   §6.3 item 3, *"`deleg` is present, and `deleg.depth ≥ 1` (an absent depth is
   0);"*. SPEC-0004 §6.4: *"Keys that a rotation (§7.2) links count as one
   member."*

   **Finding (inferred):** a relying party that anchors a persona's identity key
   with no `may-delegate` will not accept statements from that persona's
   operational keys (adopt 11), because the identity key's `trust` to its
   operational key is a second hop. RFC 2692's own comment says this is right:
   equivalence for a purpose *is* delegation. But it hides ARCH-0003 §3.2's
   operational-key pattern from the most conservative anchors.

   **Adaptation:** either (a) a wallet that uses operational keys tells relying
   parties that an anchor for it needs `may-delegate` with `depth ≥ 1` and
   `ranges` equal to `about`, or (b) SPEC-0004 gains an intra-persona link like
   rotation's. Route (b) reopens what RFC 2692 warns about and must not let an
   equivalence through a depth-0 anchor (reject 5); it is open question 5.
   Tests: SR-USE-57, SR-USE-59, SR-USE-C01 to SR-USE-C03.

7. **The kid is the new dossier key.** [WG] R-0014's dossier (adopt 5), and
   R-0017: *"It is necessary for at least some certificates to be anonymous."*
   [list] Item 52, R-0119: *"I'm the a purchasing agent for a large corporation.
   I want to posses a certificate that tells our suppliers that I'm authorized to
   make purchases up to \$15,000."* (sic); R-0120: *"I don't want the suppliers
   to know my name, lest their sales people bug me too much."*; R-0121: *"I don't
   want to have to share a single "Megacorp Purchasing Department Certificate"
   with others doing the same job [the private key would need to be
   shared--yuck!]."*

   Ours: SPEC-0002 §14, *"A kid is a stable identifier and links every statement
   made with that key; personas that need to be unlinkable MUST use separate
   keys."* SPEC-0001 §3.1: *"a person who needs unlinkable identities MUST use
   separate personas with separate identity keys."* ARCH-0003 §1:
   *"Unlinkability is still available, but as a choice: separate personas with
   separate keys."*

   **Finding (inferred):** RFC 2692 takes the name out of the certificate and
   keeps the key, and in a key-centric system the key is the linkage handle.
   Every statement about `[1, kid]` and every statement by it can be gathered
   into exactly the dossier R-0014 warns about. Operational keys do not help,
   because the delegation path presented with each claim names the identity key
   (SPEC-0001 §8.1's presentation carries *"the claim, its delegation path"*).
   Only separate identity keys help, as SPEC-0001 §3.1 says.

   **Item 52, adapted:** expressible today. Megacorp's key issues `trust` to the
   agent's key about a purchase-limit type of base kind `integer` with range
   `[0, 15000]` (SPEC-0003 §6, kind 2), with no name anywhere, and one key per
   agent meets R-0121. What leaks is not the name but the link: the supplier sees
   the same agent kid on every purchase and Megacorp's kid on the path. That is
   sometimes what is wanted, and RFC 2692 wants both by application, since item
   51 values *"tracking abuse of that same spectrum"* (R-0117). **Consequence:**
   a wallet offers per-relationship personas where unlinkability is wanted and
   shows their cost, one delegation per persona; and `self` statements stay
   minimal by default, since SPEC-0001 §12 notes *"`self` statements publish a
   label and a controller kind."* Tests: SR-GEN-C05, SR-GEN-C06, SR-USE-56,
   SR-USE-C06, SR-USE-C07.

8. **Encoding constraints that hold under every DEC-002 option.** [WG] The
   Implementation of Certificates requirements, applied to SPEC-0002 as written.
   The option-by-option scoring is the DEC-002 subsection of §4.
   - **No ASN.1 anywhere native, including suite encodings.** R-0043: *"In
     particular, ASN.1 is not to be used."* R-M-01 forbids X.509 and PKIX;
     RFC 2692 forbids ASN.1, which reaches further. SPEC-0002 §6.2 lists suite 2,
     `ksa-p256-sha256`, as *"reserved; not yet specified"*, and §6.1 requires
     every suite to define *"the exact octets of `sig`"*. ECDSA signatures are
     conventionally DER-encoded (inferred), so when suite 2 is specified its
     signature must be fixed-width `r ‖ s` and its public key a raw point, never
     DER or SubjectPublicKeyInfo. X.509 stays at the import boundary (R-I-05).
     Tests: SR-IMP-01, SR-IMP-C03.
   - **Bounded nesting, so a constrained verifier need not recurse.** R-0049:
     *"For efficiency, if possible, an SPKI certificate should be packed and
     parsed without any recursion."* SPEC-0002 Appendix B defines *"value = int /
     bool / bstr / tstr / [* value] / { * tstr => value }"*, which is recursive,
     and §13.6 requires *"nesting depth of at least 16"*. A profile can cap
     `value` depth so that a fixed explicit stack suffices (inferred). Tests:
     SR-IMP-C06, SR-IMP-C07.
   - **A constrained-verifier profile.** R-0035: *"In addition, SPKI certificates
     should be usable in very constrained environments, such as smart cards or
     small embedded systems."* (this quote crosses the page 4/5 break). R-0036:
     *"The code to process them and the memory to store them should both be as
     small as possible."* Against them, SPEC-0002 §13.6, *"A verifier MUST accept
     a TBS of at least 65 536 octets"*, and suite 8's *"the 3309-octet signature
     of [FIPS204]"*. Verify-before-decode means a verifier holds or re-reads the
     TBS between V4 and V5 (inferred), so a smart card must buffer up to the
     minimum it is obliged to accept. Either SPEC-0001 §4.2 gets a smaller
     conformance class, or the profile says smart cards sign and do not verify,
     which is item 53's pattern (open question 7). Test: SR-IMP-02.
   - **Single touch for the decoder, not for verification.** R-0048 is kept for
     the parse, as SPEC-0002 §4.3 already claims: *"Every check above can be made
     in a single forward pass without re-encoding (mofn#78)."* It is rejected for
     verification order (reject 7).
   - **Few optional fields.** R-0038 and R-0039: *"There should be a bare minimum
     of fields necessary to get the job done and there should be an absolute
     minimum of optional fields."* SPEC-0002 §7.1 makes `valid` *"RECOMMENDED;
     REQUIRED for `rotate` and `revoke`"*, with all three of its fields optional,
     so a statement with no expiry is the default shape. With R-O-02 and adapt 1,
     a profile should make `not-on-or-after` required on `attestation`,
     `trust`, `review` and `approve` (inferred).

9. **Code-author vocabularies over a fixed algebra.** [WG] R-0010 and R-0011
   again, now as a constraint. Ours: SPEC-0003 §6, *"Every base kind is
   implemented by the verifier; a definition chooses one and may constrain it
   (§8), but cannot change its algebra."*; SPEC-0003 §13.1, *"It cannot change
   how ranges intersect, and it cannot execute."*; and DEC-008's floor, *"if a
   key may define how its own statements are validated, it may define them as
   always-valid."*

   **Finding:** R-0011 holds for every authorization expressible in SPEC-0003's
   eleven base kinds, and fails by design for one that needs a new algebra, such
   as a geographic region, a time-of-day window or an amount with a currency.
   Those need a base-kind registry entry, and SPEC-0002 §12 defines
   "Specification Required" as *"added by a revision of this specification
   accepted through an ADR"*, which is interaction with another organization.
   RFC 2693 fixed its algebra too (2693 R-0145) and named the price of leaving
   it: *"Special semantics would require special reduction software."*
   (2693 R-0146). We keep the fixed algebra, because
   DEC-008's argument is the stronger one. **Consequence:** the base-kind
   registry is the one place R-0011 is knowingly not met, so new kinds are added
   rarely and always with vectors. The list's range uses are covered now: item 47
   (R-0110, *"permission to spend up to \$X of a company's money"*) and item 52 by
   `integer`, item 54 by `ip-prefix`, item 55 by `dns-name`, and item 56 by
   `email`. The same tension in SPEC-0002 §12.7's usage codes is open question
   11.

10. **No objection is a positive fact, or it cannot be decided.** [OQ] Open
    Question 3, R-0154: *"The absence of attributes can be determined only if all
    relevant records are digitized and all parties have inescapable IDs."* R-0155:
    *"A certificate can communicate the 'positive' attribute "not already
    married" or "not registered as a voter in any other district"."* [list] Item
    37, R-0100: *"BBB-style certificate that no complaints exist against a
    business or doctor or dentist, etc."*

    Ours: ARCH-0003 W-24; SPEC-0005 §5.2's rule 5 holds when *"no input statement of that input
    satisfies `where`"*, and §9.1 concedes *"It cannot reveal an input the
    evaluator has not received; a relying party that matters SHOULD gather inputs
    from more than one source before relying on a negative-sensitive rule (rule
    5)."*

    **Adaptation.** R-0154 says when rule 5 can be trusted: when the record set
    is complete. For a *listed* panel of n members completeness is checkable, so
    pair rule 5 with `[1, input, n]` (every member has spoken), and the negative
    becomes a conjunction of positives, which is R-0155's move. For a *delegated*
    panel, membership is whoever D has delegated to (SPEC-0005 §4.2,
    *"Delegated membership uses only `D`'s direct trust statements."*), so the set
    is open and rule 5 can only mean "none received". **Consequence:** the
    renderer says "no rejection received from N of M members" rather than "no
    rejection", and a definition that applies rule 5 to a delegated panel draws a
    SPEC-0004 §9 policy warning. Test: UC-2's variant in which V3 rejects and an
    aggregate cites only V1 and V2, run by a relying party that does not hold V3's
    review, is *met* today and should read *met, incomplete*. Vectors: SR-USE-40,
    SR-OQ-03 to SR-OQ-05.

11. **A propagation bound is a validity bound.** [list] Other requirements item
    6: *"Reliable distribution of key revocations and other certificates (e.g.,
    the ceasing of the right to make new certificates). May involve goals like
    "will have spread everywhere in 24 hours" or something like that. This
    interacts with caching."* (R-0148 to R-0150). Ours: SPEC-0001 §1.3, *"Out of
    scope for this version: the binary transport codec and fragmentation (FKSA's
    binary/transport specification), revocation distribution, selective
    disclosure, and multi-speaker contracts (ARCH-0002 DEC-009)."*

    **Adaptation (inferred):** a deployment that cannot promise "will have spread
    everywhere in 24 hours" gets the same bound by capping validity at 24 hours
    with `max-validity`, which is R-O-02's preference given a number.
    **Consequence:** each context's templates state the revocation latency they
    tolerate as `max-validity`, and the verdict can say what the relying party is
    exposed to. This is route (b) of adapt 1. Test: SR-USE-75.

## 3. What we reject, and why

1. **The white-space concession.** [WG] The end of R-0045: *"(although one
   might canonicalize white space during certificate input, for example, if the
   format is text)"*. It is a canonicalisation at verification, unspecified
   (*"for example"*), which proposed R-O-05 forbids (*"SHALL NOT canonicalize
   input as part of verification"*) and which R-O-03 forbids for being uncited
   (*"Canonicalization algorithm for each concrete encoding SHALL be cited, not
   invented silently."*). Under KSA there is nothing for it to act on: the
   signed form is binary (SPEC-0002 §4.2), text strings are kept byte-exact with
   *"no whitespace trimming"* (SPEC-0002 §4.1), and the YAML human-review form
   *"is never signed or hashed"* (SPEC-0002 §11). **Consequence:** SPEC-0002 §11
   should also say that a verifier MUST NOT accept the human-review form as input
   to verification. Converting YAML to KSA-CBOR and then checking a signature is
   exactly the reformatting R-0045 excludes, and §11's *"A conforming tool
   converts between the two one-to-one."* makes it easy to build. SR-IMP-04 and
   SR-IMP-C02 expect the concession to be allowed; our conformance suite inverts
   them.

2. **Traditional certificates as a native construct.** [list] Item 7.1, R-0057:
   *"[traditional certificate] binding a key to a name, implying "all the
   attributes of the real person having this name are transferred to this key by
   this certificate"."* R-0059: *"In this model, a key starts out naked and
   acquires attributes, permissions and authority from the person bound to it."*
   RFC 2692's own Background is the reason (adopt 1). R-M-01 and R-I-05 are the
   rule: *"Import X.509 only as a foreign identity assertion about a key (name or
   attribute), marked `provenance: x509`."* **Consequence:** no native statement
   transfers authority by naming a person. Test: SR-USE-08.

3. **Blinded signature keys and anonymous speakers, declined for this version.**
   [WG] R-0018: *"Because one use of SPKI certificates is in secret balloting and
   similar applications, an SPKI certificate must be able to assign an attribute
   to a blinded signature key."* Our suites offer no blind signing (SPEC-0002
   §6.2: Ed25519; ML-DSA-65 provisional; P-256 reserved), every statement
   carries a `says` kid (SPEC-0002 §7.1), and SPEC-0001 §1.3 puts selective
   disclosure out of scope, as does ARCH-0003 §12 item 4: *"Selective disclosure
   in presentations (SD-JWT, RFC 9901) — the `disclosure` policy is the hook; out
   of scope this semester."* Balloting is not an MD-1 target (*"in-scope
   targets: software supply chain + archives/library."*). This is recorded as an
   unmet [WG] requirement, not an oversight: SR-GEN-04 and SR-GEN-C07 fail against
   KSA. R-0017 is met only on its subject-side reading (key-only subjects, adapt
   7); an anonymous speaker cannot be expressed. Open question 13.

4. **Stored-value, stateful and transferable instruments.** [list] Items 27 to
   29, 33, 34 and 39 to 42. Statements are immutable and evaluation is a pure
   function of its inputs (SPEC-0004 §3). So a counter (*"Starbuck's Coffee
   buy-10-get-1-free card"*, R-0090), a balance (*"DC Metro fare card"*, R-0091;
   *"Phone calling card"*, R-0092) or a bearer token (*"claim check for a
   suitcase"*, R-0096) cannot be a statement. Transferring a title (*"Stock
   certificate"*, R-0102; *"Car title"*, R-0104; *"deed to land"*, R-0105) needs a
   register, which R-0153 itself puts outside certificate structure and NG4 puts
   outside our requirements. A statement may attest a fact about such an
   instrument at a time; it is never the instrument. Tests SR-USE-30 to
   SR-USE-32, SR-USE-36, SR-USE-37 and SR-USE-42 to SR-USE-45 are out of scope,
   with this reason.

5. **An equivalence that overrides a no-delegation anchor.** [list] Item 53,
   R-0122 read against R-0124 (both in adapt 6). A signed key "equivalent to the
   certifying-key" under an anchor that grants no delegation is delegation
   against the anchor's will, and RFC 2692 says so itself. We keep SPEC-0002
   §8.6's one-hop default and accept R-0125's residual, that a format cannot stop
   key lending. **Consequence:** neither route in adapt 6 may introduce an
   implicit equivalence that a depth-0 anchor cannot refuse.

6. **Graded reliability inside native evaluation.** [list] Other requirements
   item 1's *"(maybe with varying reliabilities)"* (R-0139). SPEC-0004 §10.3
   answers yes or no, and ARCH-0001 §4.2 keeps weights in `Endorse` (*"issuer
   treats subject as introducer at weight w"*), described as *"Optional
   PGP-shaped import; not required for AuthzCert reduction"*. Reliability is
   expressed by scope: a less reliable root gets narrower `about` ranges in its
   context, not a number. A numeric combination rule would be a second,
   unspecified algebra (inferred); the delegation-models answer records that
   OpenPGP's trust amount has *"no composition rule given anywhere in the RFC."*
   Test: SR-USE-70 (the choice-of-roots half passes; the reliability half is
   declined).

7. **Single touch as a constraint on verification order.** [WG] R-0046 to
   R-0048: *"For efficiency, if possible, an SPKI certificate should be encoded
   in an LR(0) grammar. That is, neither packing nor parsing of the structure
   should require a scan of the data. Data should be read into the kind of
   structure a programmer would want to use without touching the incoming bytes
   more than once."* Verify-before-decode makes two passes over the TBS by
   construction (SPEC-0002 §3: a verifier *"verifies the signature over the
   received TBS, and only then decodes the TBS with a validating decoder"*), and
   the statement digest is a third (SHA-256 of `tbs`, SPEC-0002 §4.5). RFC 2692
   framed single touch as *"For efficiency, if possible"*; R-O-05 is a security
   rule. The efficiency goal loses where they conflict and is kept for the decoder
   (adapt 8). **Consequence:** no implementation may decode while hashing and act
   on decoded fields before V4 succeeds. SPEC-0002 §13.6's *"It MUST bound the
   work it performs on any input before V4 succeeds."* is the companion rule.
   Test: SR-IMP-C05 (no scan), which KSA-CBOR's parse meets.

8. **The minimal CRL, and the reading that SPEC-0004 §3 meets R-0028.** [WG] RFC
   2692 rules the minimal CRL out (R-0024); ours: R-M-05, ADR-0003 D5. We record that it must not return under
   the name `revoke`, and that "the same answer for the same inputs" (SPEC-0004
   §3) does not satisfy R-0028's *"behavior of certificate validation is
   deterministic"* while the inputs include whichever revocations happened to
   arrive. Adapt 1 is the repair.

## 4. Mapping to our decisions

Verdicts: **supports**, **narrows** (ours or the source restricts the other),
**contradicts**, **silent**. "Adopt n", "adapt n" and "reject n" point into §1
to §3.

| Ours (quoted) | RFC 2692 (quoted, R-id) | Verdict |
|---|---|---|
| **R-M-01** *"Native encoding SHALL NOT be X.509 / PKIX."* | *"No library code should be required for the packing or parsing of SPKI certificates. In particular, ASN.1 is not to be used."* (R-0042, R-0043), argued from developers *"operating out of garages or dorm rooms"* (R-0034) | **Supports, and reaches further.** R-M-01's reason is the information model (ARCH-0001 §1); RFC 2692's is the cost of implementation, which also excludes ASN.1 from suite encodings (adapt 8). This record is where R-M-01 is argued from first principles. |
| **R-M-02** *"A principal MAY be identified solely by key or key digest."* | R-0008, R-0009 (adopt 2) | **Supports.** "Collision-free" argues for full-length kids. |
| **R-M-03** *"Names SHALL be interpreted only relative to an issuing principal."* | *"An SPKI certificate must be able to bind a key to such names."* (R-0020); the SDSI construct (R-0021) | **Supports.** SPEC-0002 then **narrows** R-M-03: no name subjects, no alias speakers (adapt 5, open question 12). |
| **R-M-04** *"Name bindings and authorization bindings SHALL be distinct object kinds."* | Background ¶2; R-0005; item 7.2's direct certificate, under which a key gets authority *"directly by other certificates, not indirectly through some person's name"* (R-0063); item 7.1 is the counter-case (reject 2) | **Supports the separation of concerns; silent on object kinds.** ARCH-0002 P6 makes names one function over one form; RFC 2692 needs only that names stay off the authorization path (adopt 1). |
| **R-M-05** *"Authorization composition SHALL be deterministic given an ordered cert set and ACL."* | R-0024, R-0028 | **Supports the principle and extends it to validity.** Silent on composition order. KSA's revocation fails the extension (adapt 1). |
| **R-M-06** *"Threshold principals SHALL be representable without encoding them as a CA hierarchy."* | none | **Silent.** No threshold, quorum or k-of-n appears anywhere in the source. Item 48, *"permission to issue nuclear launch codes"* (R-0111), is the classic two-person case, listed with no mechanism (inferred). This answers the rfc-2693 design notes' open question 10: RFC 2692 gives no rule for combining delegation bits across threshold branches. |
| **R-M-07** *"Artifact statements SHALL bind at least one content digest."* | Item 6: *"to make sure it hasn't changed"* (R-0055) | **Supports** at list level; "hasn't changed" needs a content digest (inferred). |
| **R-M-08** *"Tag intersection semantics SHALL be defined for every tag profile the implementation claims."*, and ARCH-0002 P7 (held) | R-0010 | **Supports**: authorizations are defined per application, as P7's profiles would be. SPEC-0003's fixed base kinds narrow R-0011 (adapt 9). |
| **R-M-09** *"Validity intersection SHALL be defined (time window ∩ optional online checks)."* | *"An SPKI certificate, like any other, should be able to carry a validity period: dates within which it is valid."* (R-0022); R-0023, R-0030, R-0031 | **Supports; SPEC-0002 falls short.** `valid` has the window and no online checks (adapt 1, adapt 2). |
| **R-M-10** *"Delegation SHALL be an explicit boolean (or equivalent) on `AuthzCert`."* | R-0125's *"Maybe we need a "delegation-allowed" bit"*, and in the same sentence the reason it cannot be enforced; R-0124; R-0033 | **Origin, with its caveat attached.** RFC 2693 chose the bit (*"Of these three, the group chose boolean control."*, 2693 R-0060). SPEC-0002 §8.6 has an integer depth (*"With it, `depth` counts further hops"*); RFC 2692 is silent on depth, and its caveat applies to depth equally. Whether `depth` is R-M-10's "(or equivalent)" is the R-M-10 ADR's question. |
| **R-M-12 / ARCH-0002 P1 / ADR-0001** *"The native model depends on no centrally allocated registry for their meaning."* | R-0010, R-0011 | **Supports registry-freedom; silent on key-relativity** (adopt 3). |
| **R-I-02** *"Import SHALL NOT require the foreign object to become a native trust anchor."*, **R-I-05** | Item 7.1 (R-0057) | **Supports.** A traditional certificate imports as a name assertion (reject 2). |
| **R-I-03** *"Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT claims (at least one envelope in v1)."* | R-0044 | **Constrains (inferred).** An export is signed over different bytes from the native statement, so it is a re-issue, never the certificate as transmitted. See the DEC-002 subsection. |
| **R-O-01** *"Every signed object SHALL have an issuer key that can be specified as `KeyId`."* | R-0017 | **Compatible with the subject-side reading of anonymity; excludes anonymous speakers** (reject 3). |
| **R-O-02** *"Short-lived validity preferred over revocation-heavy design; revocation still representable."* | R-0022, R-0023, R-0029 to R-0032; Kohnfelder (Background ¶1) | **Supports representability; silent on the preference.** RFC 2692 never ranks short-lived certificates (that is 2693 R-0102). It ranks positive on-line validation above negative lists (Validity and CRLs ¶3). Its determinism conditions are what make "revocation still representable" safe (adapt 1, adapt 11). |
| **R-O-03** *"Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently."* | The end of R-0045 | **Contradicted by the concession, which we reject** (reject 1). R-0044 moves canonicalisation to authoring, where R-O-03 then governs. |
| **R-O-04** *"Optional registration of statements with a SCITT-like transparency service."* | R-0013; R-0145's *"notary services"*; item 60, *"Timestamping / notary services"* (R-0135) | **Supports optionality.** RFC 2692 makes notary evidence the precondition of certification-right expiration (adapt 3). |
| **R-O-05 (proposed)** *"A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification."* | R-0044, R-0045; R-0048 | **Supports; RFC 2692 is its earliest statement.** R-0048's single touch conflicts and loses (reject 7). |
| **ARCH-0002 P5** *"a failure at any level is a rejection, never a repair"* | R-0040 | **Supports** (adopt 7). |
| **DEC-003** issuer and subject identifiers | R-0009's *"collision-free hash"* | **Supports** full-length digests (adopt 2). |
| **DEC-004** tag language | R-0010; items 47, 52 and 54 to 56 | **Evidence:** the tag language must be definable by the code author and must express ranges; SPEC-0003's base kinds already do (adapt 9). |
| **DEC-008** (open) *"Key-local is right for declarative processing."* | R-0010, R-0011 | **Supports declarative, author-defined vocabularies; silent on processing.** 2693 R-0146 shows the cost of author-defined processing. |
| **DEC-009** (open), the contract form | Item 9: *"I want to sign a contract to buy a house. What kind of certificate do I need?"* (R-0072) | **Silent.** The same question, unanswered, in 1999. Open Question 2's answer (R-0153) removes only the title database from scope. |
| **G3** *"Deterministic reduction of authorization chains (SPKI 5-tuple style), not unbounded WoT path search as the primary algorithm."* | *"Trust model must be a web (people want to choose whom they trust)."* (R-0138) | **Compatible.** RFC 2692 defines its "web" in the parenthesis, as choice of roots, not as an algorithm. |
| **ARCH-0003 §1, §3.2 persona; W-01** | R-0017; item 52 | **Supports pseudonymity by persona; exposes kid linkage** (adapt 7). |
| **ARCH-0003 W-09; SPEC-0001 §8** | R-0012 to R-0016 | **Supports.** Selective disclosure (ARCH-0003 §12 item 4) is the unmet part of R-0016. |
| **ARCH-0003 W-15; SPEC-0004 §9** (agents are never roots) | Item 50's audit identity (R-0114, R-0115) | **Compatible (inferred):** the path names the person, and the audit identity is the application's. |
| **ARCH-0003 §9** *"unsigned anchors — owned personas only"* | Item 7.3 (R-0067, crosses the page 6/7 break) | **Narrows; adapt to integrity-protected anchors** (adapt 5). |
| **ADR-0003 D3** *"Acceptance is a local act by a persona whose controller is a person or organisation."* | *"People must be able to choose whom they trust or consider reliable roots"* (R-0139) | **Supports.** |
| **ADR-0003 D4** *"Every evaluation is relative to one context's anchors."* | *"the audit identity should be in the domain of the particular application"* (R-0114) | **Supports (inferred).** |
| **ADR-0003 D5** *"Issuer revocation is adopted"* | R-0024 to R-0028; R-0012 | **Contradicts as specified:** wandering under RFC 2692's test (adapt 1). |
| **SPEC-0002 §4.5** *"A transport MAY abbreviate them on the wire, provided the receiver reconstructs the full TBS before verification (§13.7)."* | R-0044, R-0045 | **Contradicts (inferred).** Reconstructing before verifying is reformatting before the signature check. The safety net, *"an abbreviation that reconstructs to the wrong bytes simply fails V4."* (SPEC-0002 §13.7), is real, but the rule belongs in a transport specification, not the core (open question 8). |
| **SPEC-0002 §13.6** resource minimums | R-0035, R-0036 | **Narrows** for smart cards (adapt 8). |
| **SPEC-0003 §6** base kinds | Items 47, 52 and 54 to 56 | **Supports.** `integer`, `ip-prefix`, `dns-name` and `email` cover the list's range uses. |
| **SPEC-0004 §7.2** rotation and compromise | R-0144; R-0152 | **Supports** rotation's *"The old key verifies the past only."*, which retirement also needs (adapt 3). The compromise rule over-trusts `issued` (open question 6). |
| **SPEC-0005 §5.2 rule 5** | R-0154, R-0155 | **Narrows** (adapt 10). |
| **MD-1** *"in-scope targets: software supply chain + archives/library."* | The List of Certificate Uses | **Scope, not failure.** Most list items are consumer or identity uses outside MD-1. Item 6 (software) is a target; items 54 to 56 are UC-5 and UC-6 schema scenarios. |
| **DEC-002 / MD-3** | Implementation of Certificates | The subsection below. |

### DEC-002 and MD-3

RFC 2692 is not a COSE, CBOR or envelope document. It defines no headers and no
encoding, so there is no header-by-header mapping to give, and that is the
finding rather than an omission. But Implementation of Certificates is a list of
encoding constraints, written before any canonical form existed (*"This leads to
a number of constraints on the structure and encoding of certificates."*), and
`docs/extraction.md` asks where a document cuts against MD-3. The options, as we
state them:

- **Option 1** (ARCH-0001 §7): *"Canonical S-expressions (RFC 9804) as
  canonical; JSON as diagnostic."*
- **Option 2**: *"CBOR + CDDL as canonical; COSE for signed form."*
- **Option 3**: *"JSON + RFC 8785 JCS as canonical; DSSE for signed form."*
- **Option 4**: *"Dual canonical (CBOR and JSON) with a documented bijection."*
- **Option 5** (proposal §3.3): *"CBOR as the canonical encoding, using the CBOR
  data model and deterministic encoding rules, but with no reliance on the IANA
  CBOR Tags registry and no native use of COSE header parameters."* MD-3:
  *"CBOR data model, no IANA tags, COSE as export only; type identity is
  `(defining key, label)` per P1; YAML is the human form with a canonical one-way
  mapping."* Realised as KSA-CBOR, SPEC-0002 §4.2, under ADR-0003 D2.

The minutes name option 5 and option 2 (MD-3: *"Option 2 is retained only as the
comparison fixture."*), and option 1 (2026-10-12: *"DEC-002 was narrowed to
option 5 on Sep 28; option 1 was scored on Oct 8 and now sits on the right side
of all four grounds it was withdrawn on."*). Options 3 and 4 are named in
neither minute and are scored in the last column for completeness. "rfc-9804
notes" below is `records/ietf/rfc-9804/distilled/design-notes.md`.

| RFC 2692 | Option 1 | Option 2 | Option 5 (KSA-CBOR) | Options 3 · 4 |
|---|---|---|---|---|
| *"A certificate should be signed exactly as it is transmitted."* (R-0044) | **Meets.** The canonical form is both signed and sent (rfc-9804 notes, condition 3). | **Meets.** COSE carries the protected header and payload as byte strings and signs a structure built from them as received (inferred). | **Meets.** `tbs` is carried as *"the octets exactly as signed"* (SPEC-0002 Appendix B); the signed input `DS ‖ TBS` adds a constant prefix (adopt 6). | **3:** meets only if JCS is confined to authoring and DSSE verifies the received bytes; RFC 8785's own procedure re-canonicalises (rfc-9804 notes, ground ii). **4:** fails if a signature over one form is checked against the other. |
| No reformatting to check a signature (R-0045) | **Meets.** | **Meets.** | **Meets**, except SPEC-0002 §4.5's abbreviated transport, which is option-independent (open question 8). | **3:** the JCS route is reformatting. **4:** the bijection at verification is reformatting. |
| The white-space concession, and binary or text (end of R-0045) | No whitespace in the canonical form. The advanced form is text and would need the concession, which we reject. | Binary: nothing for the concession to act on. | Binary; the YAML human form is never signed (SPEC-0002 §11). MD-3's "one-way" and §11's "one-to-one" disagree (open question 15). | **3:** text, the case the concession was written for, and JCS goes far beyond white space. **4:** as 3 for its JSON half. RFC 2692 itself is neutral on binary versus text. |
| *"No library code should be required for the packing or parsing"* (R-0042) | **Best.** A grammar of two productions (rfc-9804 R-0056, R-0057), hand-writable (inferred). | **Fails in practice.** Full CBOR plus COSE headers and algorithms (inferred). | **Partial.** The reduced data model is hand-writable. The validating decoder must be custom, since a generic decoder accepts non-deterministic input (canonical-encoding answer). The vectors were generated with `cbor2`. | **3:** fails; the number algorithm is not even in RFC 8785 (rfc-9804 notes, condition 1). |
| *"ASN.1 is not to be used."* (R-0043) | **Meets.** | **Meets natively**; COSE's X.509 header parameters (rfc-9360) can carry DER into a native object (inferred). | **Meets**; the suite 2 encoding must stay ASN.1-free (adapt 8). | **Meet.** |
| No scan to pack or parse (R-0046, R-0047) | **Meets both ways.** Length-prefixed strings and parenthesised lists; packing needs no counts (inferred). | **Parse meets:** the head gives type and extent (ARCH-0002's CBOR note). **Pack:** counts up front, and a runtime sort for text-keyed maps (inferred). | **As option 2.** Integer-keyed protocol maps have a static order; language maps and record values need the sort (SPEC-0002 §4.2 rule 3). | **3:** fails; a JSON string ends at an unescaped quote, found by scanning, and JCS sorts keys (inferred). |
| Touch the incoming bytes once (R-0048) | Decoder single-pass (rfc-9804 notes, condition 2). | — | Decoder single-pass (SPEC-0002 §4.3). | **Not a discriminator:** R-O-05 makes verification two-pass under every option (reject 7). |
| No recursion (R-0049) | Fails: lists nest (2693 R-0015). | Fails: arrays and maps nest. | Fails: `value` is recursive; a profile can bound it (adapt 8). | Fail. **Not a discriminator.** |
| *"relating directly to the kind of structures a C or PASCAL programmer would normally write"* (R-0041) | **Weakest.** Octet-strings and lists only; *"option 1's data model is far poorer than CBOR's or JSON's"* (rfc-9804 notes). | **Good.** Integer-keyed maps read as structs. | **Good.** Closed integer-keyed maps read as structs, and `[type, …]` targets as tagged unions (inferred). | **3:** objects read as structs, but numbers are not C integers (inferred). |
| The structure constrains the creator (R-0040) | No schema language accompanies the canonical form (inferred). | CDDL. | CDDL (SPEC-0002 Appendix B), closed maps and a rejecting decoder. | **3:** JSON Schema. |
| Small code, small memory (R-0035, R-0036) | Smallest decoder. | Largest. | Small decoder; the §13.6 minimums and suite 8's sizes are profile matters, option-independent. | **3:** JCS adds number formatting and UTF-16 sorting. |
| Authorizations created without any other organization (R-0010, R-0011) | **Meets:** no IANA actions (rfc-9804 R-0066). | **Fails as written:** ADR-0001, *"option 2 as originally written does not"* remain. | **Meets:** no IANA tags, `(defining key, label)`; SPEC-0002 §12's own registries are a residue (open question 11). | **3:** DSSE's payloadType is a global identifier (rfc-9804 notes, ground iv). |
| Sign-as-transmitted at the export boundary (R-0044, inferred) | Export needed. | **No export needed:** the native signed form is the COSE form. | COSE export is a second signature over a COSE structure, never the native bytes. | As option 5. |

**Where RFC 2692 cuts against option 5.**

1. **On R-0042 and R-0036, option 1 wins.** The proposal dismissed option 1
   because *"Selecting it would mean adopting a serialization with almost no
   modern library support"* (proposal §3.1), and DECISIONS-0001 still lists *"a
   far poorer data model and library availability, which DEC-002 names as a
   driver"*. RFC 2692 is the document that says *"No library code should be
   required"*. By its measure, the absence of libraries for a format that needs
   none costs nothing, so it inverts the driver option 1 was scored down on. And
   option 5's verifier cannot lean on a library for the property that matters
   most: SPEC-0002 §4.3 requires a decoder that *"rejects any input that is not
   exactly the KSA-CBOR encoding of some value in the data model"*, while the
   canonical-encoding answer records that *"a conforming DECODER accepts
   non-deterministic input happily."* Libraries help option 5's producers; its
   verifiers write custom code either way (inferred). The DEC-002 ADR should
   say which of the two it means by "library availability" (open question 17).
2. **On R-0047, option 1 wins narrowly when packing:** it needs no counts and no
   sort.
3. **At the export boundary, option 2 wins (inferred).** "COSE as export only"
   means every COSE consumer receives a re-signed object. Under option 2 the
   signed form is COSE and R-0044 holds end to end. This is a cost option 5 pays
   and option 2 does not.

**Where RFC 2692 favours option 5.**

1. **Over option 1, on R-0041 and R-0040:** a typed data model and a schema
   language match *"the kind of structures a C or PASCAL programmer would
   normally write"* and let the structure, rather than the reader, constrain the
   creator.
2. **Over option 2, on R-0011:** the registry objection is the reason option 5
   exists, and RFC 2692 makes it for authorizations.
3. **Over options 3 and 4, on R-0045:** one binary canonical form and no
   conversion at verification.

**Not discriminators.** R-0043 (every option meets it), R-0048 (R-O-05 makes
every option two-pass, and every decoder can be single-pass), R-0049 (every
option nests), and the SPEC-0002 §4.5 and §13.6 issues, which are profile
matters.

**Net, stated as evidence.** RFC 2692's encoding requirements split options 1
and 5 about evenly: option 1 on minimal code (R-0042, R-0036, R-0047), option 5
on typed structures (R-0041, R-0040). Both beat options 2, 3 and 4 on the
requirement each of those fails (R-0011; R-0045). That is not the picture MD-3
was taken on: the proposal scored option 1 down on library support, the very
criterion RFC 2692 inverts. This matches the 2026-10-12 minute's own caution,
*"Neither reopens MD-3 by itself; both are what the DEC-002 ADR must answer."*
Nothing here decides DEC-002.

## 5. Open questions

1. **Which revocation design meets R-0028?** (a) a status source named in the
   statement with dated, non-overlapping instruments; (b) enforced short
   validity, with the age of revocation data in the reasons; or (c) RFC 9580's
   escrowed revocation, which the delegation-models answer calls *"the single
   most directly reusable mechanism this lane found"*. Resolved by the ADR that
   follows ADR-0003 D5, editing SPEC-0002 §7.3 and SPEC-0004 §7.1. Evidence:
   adapt 1; SR-VAL-01, SR-VAL-C01 to SR-VAL-C07.

2. **Positive validation: a field or a process?** Does ARCH-0001's
   `online_check?` return to SPEC-0002's `valid`, or is positive revalidation a
   template's approval process (adapt 2)? Resolved by a SPEC-0002 and SPEC-0005
   revision under R-M-09, after a "revalidated attestation" use case with
   vectors shows whether the process route works. SR-VAL-C15 is the pass/fail
   test.

3. **One-use instruments from a third party.** R-0032's instrument, *"delivered
   only as part of a challenge/response protocol"*, needs a nonce the relying
   party chose inside a statement the validator signed. SPEC-0001 §8.1's nonce
   binds only the presenter, and SPEC-0004 §3 forbids state in evaluation. Is
   the one-use check a presentation-layer rule, with the relying party
   remembering nonces, or is it out of scope? Resolved in SPEC-0001 §8. Tests:
   SR-VAL-C12 to SR-VAL-C14.

4. **What does `retired` mean?** SPEC-0001 §5.1 lists the state and SPEC-0004
   gives it no rule. Should it take rotation-without-successor semantics gated
   on timestamp evidence (adapt 3), with a benign-retirement row added beside
   UC-6's for-cause revocation row? Resolved in SPEC-0004 §7 with SPEC-0001 §11;
   the delegation-models topic is the place to argue it. Tests: SR-USE-C04,
   SR-USE-C05.

5. **Operational keys under a depth-0 anchor.** Route (a) or (b) of adapt 6?
   Resolved in SPEC-0004 §6 and §7, together with ARCH-0003 §12 item 1 (*"Is a
   persona one identity key, or a set of peer keys with no root?"*).

6. **SPEC-0004 §7.2's compromise rule trusts a compromised key's own clock.**
   After the mark, *"every statement by `K` is used only if issued before the
   time of the compromise mark."* But `issued` *"is the speaker's own claim."* A
   thief holding K can set `issued` to any earlier time, so statements forged
   after the theft pass the rule (inferred). RFC 2692's answer to Open Question 1
   is the principle: the format cannot prove when a key was misused (R-0152). The
   options are to accept a compromised key's statements only with independent
   time evidence (SPEC-0001 §11), or not at all after the mark. Resolved in
   SPEC-0004 §7.2; the device-attestation and signature-foundations topics (both
   open, with no records yet) are where the background belongs. Test: add to UC-8 a statement by the stolen key, backdated to
   before the mark.

7. **Constrained verifiers.** Is there a conformance class for smart cards, with
   a smaller TBS minimum, bounded `value` nesting and no suite 8, or are smart
   cards signers only? Resolved in SPEC-0001 §4.2 and SPEC-0002 §13.6; the
   post-quantum-migration topic for suite sizes and cbor-implementation for the
   parser.

8. **SPEC-0002 §4.5's abbreviated transport.** Drop it from the core, or move it
   into the transport specification that SPEC-0001 §1.3 defers? Resolved in
   SPEC-0002 §4.5 and §13.7.

9. **Suite 2's encodings.** When suite 2 is specified, does SPEC-0002 fix a
   fixed-width `r ‖ s` signature and a raw point, excluding DER and
   SubjectPublicKeyInfo (R-0043)? Resolved in SPEC-0002 §6; the algorithm-bindings
   topic holds the evidence.

10. **One claim per statement, by default?** R-0014, R-0015 and 2693 R-0051
    argue yes; SPEC-0002 §8.5 allows many attributes. Resolved as template
    guidance in SPEC-0003 §7.

11. **Are usage codes and controller kinds core grammar or extension points?**
    SPEC-0002 §12.7 and §12.8 are central registries, and R-0011 and ADR-0001
    point to key-relative types. ARCH-0003 §3.3's capability `syntax` list
    already differs from SPEC-0002 §12.7's usage codes, which is the drift R-0010
    predicts. Resolved by the namespace-governance topic (open) and DEC-008's
    floor.

12. **Name subjects and delayed binding.** SPEC-0002 allows only kids where
    ARCH-0001 §4.1's `Principal` includes `Name` and GLOSSARY-0001 allows an alias
    as speaker. Keep the narrowing and amend ARCH-0001, or add a name target?
    Resolved by R-M-03's owner in SPEC-0002 §7.2, and in ARCH-0001 v0.2.0
    (DECISIONS-0001 item 4).

13. **Anonymous credentials.** Is there a future privacy profile with blind
    signatures (R-0018) or selective disclosure (ARCH-0003 §12 item 4)? No
    library topic owns it. Open one, provisionally `anonymous-credentials`,
    before any balloting or age-check scenario is written. Resolved by that topic
    and SPEC-0001 §1.3.

14. **Encryption keys.** Item 57, *"Encryption keys for E-mail and file
    encryption"* (R-0132), cannot be attested under a suite that describes them,
    because KSA suites have no key exchange (SPEC-0001 §8.2: *"which KSA's suites
    do not yet do"*). Resolved by the follow-up to mofn report R-0003 and
    SPEC-0002 §6, when the mailbox transport lands.

15. **YAML: one-way or one-to-one?** MD-3 says *"a canonical one-way mapping"*;
    SPEC-0002 §11 says *"converts between the two one-to-one"*. A one-to-one
    human form is a second encoding a verifier can be tempted to accept (reject
    1). Resolved by the DEC-002 ADR.

16. **What is R-O-05's standing?** ADR-0003 says *"consistent with accepted
    R-O-05"*; DECISIONS-0001 says *"R-M-11/R-O-05/R-O-06 have no force"*. This
    file treats it as proposed. Resolved by DECISIONS-0001 item 4, the
    acceptance of ARCH-0001 v0.2.0.

17. **What does DEC-002's "library availability" driver mean?** Encoder
    libraries, verifier libraries, or neither, given that SPEC-0002 §4.3 needs a
    custom validating decoder and RFC 2692 asks that no library be needed (§4,
    DEC-002 subsection). Resolved by the DEC-002 ADR (DECISIONS-0001 item 4b).

**Source defects, recorded and not repaired.** *"singing"* for signing in item
7.3 (R-0066), *"I'm the a"* and *"posses"* in item 52 (R-0119), and *"a this"*
in item 55 (R-0128). Transcription-level, with no effect on meaning. They are
noted because the extraction is verbatim and anyone diffing against the RFC will
meet them.

## 6. bears_on corrections

`record.yaml` lists R-M-01, R-M-02, R-M-05, R-M-09, R-O-02, R-O-03 and DEC-002.
Each was checked against ARCH-0001 v0.1.2 at 643fba2. `record.yaml` is not
edited here.

- **All seven stand.** Two need a note. **R-M-05** bears through validity
  determinism (R-0024, R-0028), not through composition, on which RFC 2692 is
  silent. **R-O-03** bears negatively: RFC 2692's white-space concession is an
  uncited canonicalisation, which we reject (reject 1).
- **Warranted additions:**
  - **R-M-03**: R-0019 to R-0021, names known to other keyholders and the SDSI
    construct (adapt 5).
  - **R-M-04**: Background ¶2 with R-0005 and R-0007, names off the
    authorization path (adopt 1).
  - **R-M-10**: R-0124 and R-0125, the "delegation-allowed" bit and why it cannot
    be enforced (adapt 6, reject 5).
  - **R-M-12**: R-0010 and R-0011, registry-free authorizations (adopt 3). Now
    ARCH-0002 P1 through ADR-0001; the id is already used in `bears_on`
    elsewhere in the library.
  - **R-O-05** (proposed; open question 16): R-0044 and R-0045, its earliest
    statement (adopt 6).
  - **DEC-003**: R-0009's *"collision-free hash"*, full-length kids (adopt 2).
  - **DEC-004**: R-0010 and the list's range uses (adapt 9).
- **Weak, optional:** R-M-07 (item 6), R-I-05 (item 7.1), R-O-01 (R-0017).
- **Outside the field's vocabulary.** The record schema describes `bears_on`
  as *"ARCH-0001 DEC-*/R-* ids this record informs."* ARCH-0003 W-09 and W-01,
  ADR-0003 D5, and SPEC-0002 and SPEC-0004 sections cannot be listed there; they
  are carried in §4's table instead. ADR-0003 D5 is the one this record bears on
  most sharply (adapt 1).
