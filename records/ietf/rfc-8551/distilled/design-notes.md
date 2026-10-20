---
record: rfc-8551
kind: design-notes
title: "rfc-8551 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

# RFC 8551 — bearing on our design

RFC 8551 is the deployed signing and encryption envelope for MIME. It is a
profile of the Cryptographic Message Syntax (CMS): it says which CMS content
types, signed attributes and algorithms an S/MIME agent uses, how a MIME entity
is canonicalised before it is signed or encrypted, and how the result is
labelled so that mail software can recognise it. It has two decades of
deployment behind it, and a record of algorithm change across five versions,
from S/MIME v2 (RFC 2311, March 1998) to v4.0 (April 2019).

It reaches us in three ways. **R-I-01 and R-I-05**: if a wallet ever imports a
signed mail message, this is the format, and §5 drafts the mapping table R-I-01
asks for. **MD-3**: it is a signing-envelope document, so `docs/extraction.md`
requires a structure-by-structure mapping and a record of where it cuts against
option 5; that is §6. And **the lessons of two decades of deployment**: algorithm
agility, gateway damage, header protection, Efail. Most of them fall on choices
SPEC-0002 has already made, and a few fall on gaps in it. What RFC 8551 is not
is a delegation or trust model. `record.yaml` says so, and §4 tests the claim.

**Things to hold while reading.**

1. **It binds, and says so.** *"This is an Internet Standards Track document."*
   (Status of This Memo). Unlike RFC 2692, its BCP 14 keywords have force:
   `requirements.yaml` measures 190 in the source and extracts 151 requirements,
   R-0001 to R-0151. §1.3 adopts RFC 8174, so lowercase *should* and *must* are not
   normative, and it adds three levels of its own. SHOULD+, for example: *"However,
   the authors expect that a requirement marked as SHOULD+ will be promoted at
   some future time to be a MUST."* (§1.3, N-005). Where something below is
   adopted, **we** make it normative in a SPEC or an ADR. Citing RFC 8551 cites a
   deployed precedent, not a rule we are bound by.

2. **It is a profile, and most of its structure is CMS, which this library does
   not hold.** *"This specification defines how to create a MIME body part that
   has been cryptographically enhanced according to the Cryptographic Message
   Syntax (CMS) [CMS], which is derived from PKCS #7 [RFC2315]."* (§1.1 ¶2; not an
   N-entry). The Appendix A module (N-174) defines only `SMIMECapability`,
   `SMIMECapabilities`, `SMIMEEncryptionKeyPreference`,
   `SMIMECapabilitiesParametersForRC2CBC` and a handful of OIDs. `ContentInfo`,
   `SignedData`, `SignerInfo`, the encoding signed attributes are hashed in, and
   `EnvelopedData` are RFC 5652's, and `AuthEnvelopedData` is RFC 5083's.
   `messages.yaml` makes the same split with `normative_status: profiled`. A row
   below that rests on a CMS rule is marked **[CMS, outside this source]**. It is
   stated from general knowledge of RFC 5652, never quoted, and should be checked
   once an rfc-5652 record exists (open question 14).

3. **Trust lives elsewhere, and the pointer is stale.** §4 ¶1 (N-137): *"This
   specification does not cover how S/MIME agents handle certificates -- only
   what they do after a certificate has been validated or rejected.  S/MIME
   certificate issues are covered in [RFC5750]."* RFC 5750 is the v3.2 document;
   the source's own §7.1 says *"[SMIMEv4] refers to [RFC2634], [RFC5035],
   [RFC5652], [RFC8550], and this document."* So the binding of a mail address to
   a key, path validation and revocation are RFC 8550's and RFC 5280's, and
   `rfc-8550` is a stub. This file says nothing about them beyond what RFC 8551
   states.

4. **Our decisions are read from m-of-n `origin/main` at `643fba2`**
   (2026-10-16) with `git -C ../mofn show 643fba2:<path>`, never from the working
   tree. Every quote of ours below was checked against that commit. The short
   names and their standing:

   | name | path at 643fba2 | standing |
   |---|---|---|
   | ARCH-0001 v0.1.2 | `spec/ARCH-0001-authorization-attestation.md` | draft; §5's R-M, R-I and R-O rows are the requirements of record; §6 is the interchange matrix |
   | proposal | `spec/ARCH-0001-PROPOSAL-v0.2.0.md` | *"Status: proposed. Nothing in this document is accepted."* The source of DEC-002 option 5, R-O-05, R-M-11 and R-M-12 |
   | ARCH-0002 v0.6.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P2, P3, P5 and P6 provisional (MD-2); P4 and P7 held |
   | ARCH-0003 v0.3.1 | `spec/ARCH-0003-wallet-object-model.md` | draft: *"Nothing here is accepted."* W-01 to W-25 |
   | SPEC-0001 to SPEC-0005, UC-0001, all v0.1.0 | `spec/SPEC-000n-*.md`, `spec/UC-0001-ksa-use-cases.md` | drafts under ADR-0003: *"where a specification and an architecture document differ, the specification governs."* (SPEC-0001) |
   | ADR-0001, ADR-0003 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0003-fksa-convergence.md` | accepted |
   | ADR-0002 | `spec/ADR-0002-provisional-principles.md` | *"Status: proposed. Nothing here is accepted."* |
   | DECISIONS-0001 v0.3.0 | `project/DECISIONS-0001.md` | the register: *"A register, not an authority."* |
   | MD-1 to MD-7 | `project/meetings/2026-09-28.md` | dated decisions |
   | 2026-10-12 minute | `project/meetings/2026-10-12.md` | recommendations only; its Decisions section is empty |
   | GLOSSARY-0001, CONTRIBUTING | `project/GLOSSARY-0001.md`, `CONTRIBUTING.md` §5 | process |

   **The R-O-05 status conflict touches this file.** ADR-0003 says the
   verify-before-decode envelope was adopted *"as consistent with accepted
   R-O-05"*. DECISIONS-0001 item 4 says that until the proposal is accepted,
   *"R-M-11/R-O-05/R-O-06 have no force"*, and ARCH-0001 §5.3 has no R-O-05 row.
   This file treats R-O-05 as **proposed**, and treats SPEC-0002 §5, which states
   the same rule as specification text, as the operative form. The conflict is
   the rfc-2692 notes' open question 16 and is not repeated here.

5. **Numbering collisions.**
   - A bare `R-NNNN` is this record's `rfc-8551#R-NNNN`, and `N-NNN` is an entry of
     its `normative.md`. **SPEC-0002's negative vectors are also named N-1 to N-6**;
     they are always written "SPEC-0002 vector N-3" here. m-of-n's cipher-suite
     research report is `R-0003` (ARCH-0003 §3.3); it is written "mofn report
     R-0003" and has nothing to do with this record's R-0003 (*"MUST support
     SHA-256."*).
   - `MSG-nn`, `ENC-nn` and `TEN-nn` are `messages.yaml`; `S-nn` are the
     source-defect entries of `examples/vectors.yaml`; `M01` to `M11` and `ST-nn`
     are `state-machine.yaml`; protocol flows and error paths are cited by their
     ids in `protocol.yaml`; "schema finding n" is the numbered Findings list in
     `schema/README.md`.
   - `R-M-NN`, `R-I-NN` and `R-O-NN` are ARCH-0001 §5, except R-M-11, R-M-12 and
     R-O-05, which are proposal §7 rows (R-M-12 accepted by ADR-0001 and relocated
     to ARCH-0002 P1). `MD-n` are dated meeting decisions (GLOSSARY-0001: *"A bare
     `D-3` in older text is `MD-3`, never `D3`"*). ADR-0003's five decisions are
     written "ADR-0003 D2". `P1` to `P7` are ARCH-0002; `W-NN` ARCH-0003; `V1` to
     `V9` SPEC-0002 §9.2; `TV-n` SPEC-0002 Appendix A. DEC-002 options are always
     prefixed.

6. **Labels.** *(inferred)* marks anything the source implies rather than
   states, and every consequence we draw beyond its words. **[CMS, outside this
   source]** is item 2's marker. Source typos are quoted as printed:
   `receipentKeyId` (Appendix A, which flags it itself in an ASN.1 comment: *"is
   spelled incorrectly but is kept for -- historical reasons"*, the `--` being
   the comment marker) and *"File extensions(s)"* (§5.1, §5.2).

---

## 1. What we adopt

1. **Verify before acting on "signed", and act on decrypted content only after
   its integrity check.** §6 ¶15 (N-164): *"If messaging environments make use of
   the fact that a message is signed to change the behavior of message processing
   (examples would be running rules or UI display hints), without first verifying
   that the message is actually signed and knowing the state of the signature,
   this can lead to incorrect handling of the message."* §6 ¶24 (N-170): *"It is
   therefore recommended that mail systems migrate to using AES-GCM as quickly as
   possible and that the decrypted content not be acted on prior to finishing the
   integrity check."* Neither is BCP 14. The first states a risk; the second's
   lowercase *recommended* is named (line 2654) in the reconciliation of
   `requirements.yaml` as normative-sounding text left out. Protocol error path
   `unverified-signed-indicator` models the first.

   Ours: SPEC-0001 §1.2 principle 5, *"Verify the bytes before reading them."*;
   SPEC-0002 §3, a verifier *"verifies the signature over the received TBS, and
   only then decodes the TBS with a validating decoder"*; and proposed R-O-05,
   *"A verifier SHALL verify the signature before decoding and SHALL NOT
   canonicalize input as part of verification."*

   **RFC 8551 is the deployed failure case for the rule R-O-05 states
   (inferred).** It names the risk without making a requirement of it. SPEC-0002
   already puts V4 before V5. What RFC 8551 adds is the interface half. The
   envelope's `suite`, `says` and `pub` are hints (SPEC-0002 §5's table), so a
   wallet that shows a speaker's label from the envelope, or sorts a presentation
   by speaker, before V9 is the §6 ¶15 failure. **Consequence:** a wallet renders
   no speaker, kind or claim from an envelope that has not reached V9. Test: an
   envelope whose outer `says` names one key while the TBS it carries, validly
   signed by that key, names another as its `says` renders no speaker, only
   `envelope-mismatch` at V6 (SPEC-0002 vector N-3 is the byte-level form:
   *"outer says (Bob) does not equal inner says (Alice)."*). A TBS signed by a
   key other than the one the envelope names fails earlier, at V4, as
   `signature` (SPEC-0002 §9.2).

   §6 ¶15 goes on: *"Visual indicators on messages may need to have the signature
   validation code checked periodically if the indicator is supposed to give
   information on the current status of a message."* Ours: SPEC-0004 §8, *"An
   evaluator MUST report the evaluation time in its answer."*; and SPEC-0001 §9.6,
   where a compromise mark means *"every acceptance record that relied on it is
   re-evaluated."* **Consequence (inferred):** a verdict shown later is shown with
   its evaluation time, or re-evaluated when it is displayed.

2. **Each signed piece is its own origin.** R-0149 (§6 ¶25, N-171): *"Clients
   MUST treat each encrypted or signed piece of a MIME message as being of
   different origins both from unprotected content and from each other."* R-0148:
   *"Clients SHOULD treat each of the different pieces of the multipart/mixed
   construct as being of different origins."* The cause is the same paragraph's
   *"The other attack that is highlighted in [Efail] is due to an error in how
   mail clients deal with HTML and multipart/mixed messages."*

   Ours: SPEC-0001 §8.1, *"A presentation without a proof of possession is still
   evaluable: every statement in it protects itself."*; SPEC-0004 §10.3, where
   `because` *"MUST name: the digests of the statements used"*. In the design
   record: ARCH-0002 P2 (provisional, MD-2), where **says** is the signature,
   *"not metadata about the statement — the cryptographic act is the saying"*, so
   a sentence belongs only to the key whose signature made it.

   **A presentation is S/MIME's multipart/mixed (inferred):** statements by
   different speakers, and unsigned presentation fields, in one container.
   **Consequence:** the renderer attributes each statement's sentence to that
   statement's speaker. It never folds two statements into one sentence, and it
   never renders the presentation's `audience`, `nonce` or `created` as said by
   anyone unless `presented` carries a proof of possession over them (adapt 4).
   Test: a presentation holding Alice's attestation and Mallory's `review` of it
   renders two attributed sentences, and the review's `comment` never appears
   inside Alice's.

3. **Authenticated encryption never attributes; only a signature says.** §2.4.4
   (N-028): *"This content type does not provide authentication or
   non-repudiation."* §6 ¶16 (N-165): *"Many people assume that the use of an
   authenticated encryption algorithm is all that is needed for the sender of the
   message to be authenticated.  In almost all cases, this is not a correct
   statement."* Among the preconditions that follow: *"The message must have
   exactly one sender and one recipient."* And even when all of them hold, §6 ¶21
   (N-167): *"users need to be aware that there is no way to prove this to a
   third party."* §3.4 ¶1 (N-104) states the multi-recipient case: *"Any
   recipient for whom the message is encrypted can replace it without
   detection."*

   Ours: SPEC-0001 §8.2, *"Statements protect their own integrity and
   authenticity, so the transport is untrusted and the verdict is the same
   however a statement arrived."*; ARCH-0002 P2, the signature is *"not metadata
   about the statement — the cryptographic act is the saying"*.

   **Consequence:** when the mailbox's HPKE encryption is specified (SPEC-0001
   §8.2, provisional), nothing it authenticates enters trust evaluation. A review
   request or an approval that crosses the mailbox is believed only as the KSA
   statement it carries. This is also why R-O-01, *"Every signed object SHALL have
   an issuer key that can be specified as `KeyId`."*, is the right floor: an
   object authenticated with a shared key has no issuer key a third party can
   check (inferred).

4. **Signer-asserted time orders; it never proves.** §2.5.1 ¶1 (N-037): *"The
   time of signing will most likely be created by a signer and therefore is only
   as trustworthy as that signer."* S/MIME still orders by it. R-0055:
   *"Receiving agents SHOULD store the preference data if the signature on the
   message is valid and the signing time is greater than the currently stored
   value."* R-0069 and R-0070 do the same for capabilities. And it bounds it, in
   R-0071: *"Values of the signing time that lie far in the future (that is, a
   greater discrepancy than any reasonable clock skew), or a capabilities list in
   messages whose signature could not be verified, MUST NOT be accepted."*

   Ours: SPEC-0004 §7.2, *"`issued` is the speaker's own claim. It orders a key's
   statements relative to its rotation; it is not evidence of when a statement
   existed."*; SPEC-0001 §11, *"`valid.issued` is the speaker's own claim and is
   not such evidence."* **No ARCH, ADR, DEC or MD text at 643fba2 maps here.**
   ARCH-0003 §3.7 carries `issued: Time` with no stated semantics, and R-M-09
   (*"Validity intersection SHALL be defined (time window ∩ optional online
   checks)."*) concerns validity windows, not the signer's own time. The rule
   lives only in the SPECs.

   **Same design, same limit.** SPEC-0004 orders a key's statements around a
   rotation by `issued` exactly as S/MIME orders its caches by signingTime, and
   both say the value is the signer's claim. **The rule S/MIME has and we lack
   (inferred):** no SPEC bounds `issued` against the evaluation time. Under SPEC-0004
   §7.2, after a rotation, a statement by the old key is used only if its `issued`
   is earlier than the `rotate`'s. A `rotate` issued with a clock far ahead
   therefore leaves eligible everything the old key issues before that time. **Consequence:** a `rotate` whose
   `issued` is later than the evaluation time by more than a stated skew is not
   yet effective, R-0071's rule in our terms. The source gives no number either
   (protocol `no-reasonable-skew-value`; `timestamp-undefined` records that its
   *"checking the timestamp"* is undefined). Open question 10.

5. **Verifiers broad, signers narrow.** §2.2 ¶1 (N-017): *"By having the different
   requirements, the maximum amount of interoperability is achieved, as it allows
   for specialized protection of private key material but maximum signature
   validation."* Receiving agents MUST support both ECDSA P-256 and EdDSA (R-0005,
   R-0006). A sending agent *"MUST support at least one of the following
   algorithms"* (R-0009). §1.1 ¶6 gives the reason for splitting the lists:
   *"Thus, the requirements and recommendations for the two types of agents are
   listed separately when appropriate."*

   Ours: SPEC-0001 §5.2, *"A wallet MUST support suite 1 (`ksa-ed25519-sha256`)
   and SHOULD support a post-quantum suite once one is final in SPEC-0002."*;
   SPEC-0002 §6.1, *"A verifier MUST report a statement under an unregistered or
   unsupported suite as unverifiable (§9), which is distinct from invalid."*;
   ARCH-0003 §3.3, *"A wallet supports several suites — classical and
   post-quantum side by side"*.

   **Consequence (inferred):** SPEC-0001 §4.2's conformance classes should
   say what RFC 8551 says: a Statement Verifier verifies every final suite, and a
   Statement Producer needs only one. As written, the Statement Verifier class
   names SPEC-0002 §6 without saying which suites.

6. **What a peer can do is learned only from its verified signatures, keyed by
   its key, and the newest wins.** R-0068: *"If the receiving agent has not yet
   created a list of capabilities for the sender's public key, then, after
   verifying the signature on the incoming message and checking the timestamp,
   the receiving agent SHOULD create a new list containing at least the signing
   time and the symmetric capabilities."* The second half of R-0071 refuses an
   unverified list. Note *"for the sender's public key"*: S/MIME keys its
   capability cache by key, not by name (inferred from the wording; state machine
   M08).

   Ours: SPEC-0002 §8.4, `speaks`: *"The speaker claims it can produce and
   understand statements using these definitions."*; SPEC-0002 §10, *"A key MUST
   NOT be added because a statement merely names it, because it appears as an
   envelope `pub` on a statement of another kind, or because a `rotate` names
   it."* Keying by key rather than by name is G1, *"Key-centric principals; names
   are not globally unique identifiers."*, and R-M-02, *"A principal MAY be
   identified solely by key or key digest."*

   **Consequence:** what a wallet records about what a persona speaks comes only
   from verified `speaks` statements, keyed by kid. A later one, by `issued` and
   subject to adopt 4's bound, replaces an earlier one. S/MIME's list is
   explicitly partial; whether ours is complete is open question 1.

7. **Signer identifiers must be unique, or verification becomes a search.** §2.6
   ¶2 (N-055): *"It is important to understand that some certificates use a value
   for subjectKeyIdentifier that is not suitable for uniquely identifying a
   certificate."* R-0063: implementations *"MUST be prepared to try each matching
   certificate during signature verification before indicating an error
   condition."* A change of identifier also costs readers. §2.6 ¶1 (N-054):
   *"Messages that use the subjectKeyIdentifier choice cannot be read by S/MIME v2
   clients."*

   Ours: SPEC-0002 §13.4, *"`kid` is the hash of the full public key, so two keys
   cannot share a kid without a SHA-256 collision. Identifiers MUST NOT be
   truncated in signed or hashed bytes."*; V3 obtains the key *"from the key store
   by (`suite`, `says`)"*.

   **Consequence:** KSA's key lookup is a function, not a search. One (suite, kid)
   gives at most one key, so a verifier that tries several keys for one `says`
   has a corrupt key store (inferred). And the kid's derivation belongs to the
   suite (SPEC-0002 §6.1, the `digest` row), so a new derivation is a new suite.
   Old readers report it unverifiable rather than misread it, which avoids
   S/MIME's v2 break by construction (inferred).

8. **Opaque signed bytes survive intermediaries; clear-signed text does not.**
   §3.5.1 ¶3 (N-110): *"However, the SignedData format protects the message
   content from being changed by benign intermediate agents.  Such agents might do
   line wrapping or content-transfer encoding changes that would break the
   signature."* §3.1.3 ¶2 (not an N-entry) lists what an 8-bit-incapable relay can
   do, *"none of which are acceptable for a clear-signed message"*. And §3.2 ¶4
   (N-092, ENC-02) keeps the outer transfer encoding outside the secured object:
   *"It is completely distinct from, and unrelated to, the transfer encoding of the
   MIME entity secured by the CMS object"*.

   Ours: SPEC-0002 §5, where `tbs` is *"the TBS exactly as signed"*; SPEC-0002 §11,
   the YAML form *"is never signed or hashed: the signed object is always the
   KSA-CBOR encoding."*; SPEC-0001 §8.2's email transport, *"a presentation carried
   as an attachment of media type `application/ksa-presentation`"*.

   **Consequence:** a presentation that rides email is an opaque binary
   attachment, base64 at the MIME layer. It is never a text body and never the YAML
   form. The MIME transfer encoding is outside every KSA signature and harmless,
   for ENC-02's reason. A KSA statement has no clear-signed form (reject 6).

9. **Bound the work an unauthenticated input can cause.** R-0121 (§3.7 ¶2,
   N-125): *"An S/MIME implementation MUST be able to receive and process
   arbitrarily nested S/MIME within reasonable resource limits of the recipient
   computer."* §6 ¶8 (N-157): *"An attacker could send certificates with keys that
   would result in excessive cryptographic processing -- for example, keys larger
   than those mandated in this specification, as such keys could swamp the
   processing element."* Neither is quantified; `protocol.yaml` lists among what
   the source does not define *"A limit for 'reasonable resource limits' on
   nesting or for oversized keys."*

   Ours: SPEC-0002 §13.6, *"A verifier MUST accept a TBS of at least 65 536 octets
   and nesting depth of at least 16, and MAY reject larger or deeper inputs as
   `encoding`. It MUST bound the work it performs on any input before V4
   succeeds."*; and every suite fixes its key length (§6.3, *"the 32-octet
   encoding"*; §6.5, *"the 1952-octet encoding"*). **No ARCH, ADR, DEC or MD text
   at 643fba2 bounds a verifier's work on unauthenticated input.** The nearest,
   ARCH-0003 W-22 (process criteria *"total, bounded, side-effect-free,
   unprivileged"*, within DEC-008's boundary), bounds process evaluation, not
   decoding or verification. The rule lives only in SPEC-0002 §13.6.

   **Consequence:** KSA already states the numbers RFC 8551 leaves to
   "reasonable", and §6 ¶8's oversized-key attack has no KSA form: a key of the
   wrong length is rejected before any arithmetic (inferred from SPEC-0002 §6.3's
   strict key rules). It is recorded so that no future suite brings back variable
   key sizes without a cap. The source makes the same observation for its curves,
   *"Key sizes for ECDSA and EdDSA are fixed by the curve."* (§4.2), so the
   key-size tables (R-0130 to R-0141) have no KSA counterpart.

10. **A combination is as strong as its weakest part.** R-0019 (§2.3 ¶6, N-022):
    *"MUST use the weaker of the two as part of any cryptographic strength
    computations they might do."* R-0002 (§2.1 ¶1, N-014): *"It is RECOMMENDED that
    the algorithm used for digesting the body of the message be of similar strength
    to, or greater strength than, the signature algorithm."* R-0002 rests on a
    split the same paragraph states: *"The algorithms here are used for digesting
    the body of the message and are not the same as the digest algorithms used as
    part of the signature algorithms."*

    Ours: SPEC-0002 has the same split. A target `[2, digest-alg, bytes]` names its
    own digest (§12.5: SHA-256, SHA-384, SHA-512), separate from the suite's
    `digest`. And SPEC-0001 §11: *"For such statements a wallet SHOULD use a
    post-quantum suite, or obtain an independent timestamp"*. In the design
    record: ARCH-0003 §3.3, *"A wallet supports several suites — classical and
    post-quantum side by side"*, for *"ML-DSA where verification is decades
    away"*; and MD-1's archives target, *"in-scope targets: software supply chain
    + archives/library."*, which is where verification decades later matters.

    **Two rules SPEC-0002 lacks (inferred).** (a) R-0002's. Nothing relates a
    target's `digest-alg` to the statement's suite. A suite-8 attestation about a
    SHA-256 digest is no stronger than that digest, whatever ML-DSA-65 adds. (b)
    R-0019's, applied to a path. An attestation that must outlive the post-quantum
    transition does so only if every trust statement on its path (SPEC-0004 §6)
    does too. SPEC-0001 §11's advice therefore applies to the whole path, not only
    the leaf. Suite 8 itself pairs ML-DSA-65 with SHA-256 for statement digests and
    kids (SPEC-0002 §6.5); whether that pairing meets R-0002's *similar strength*
    is for the post-quantum-migration topic (strength categories are outside this
    source). Open question 4.

11. **A hint outside the signature for one-pass processing, checked against the
    signed bytes.** §3.5.3.2 (N-119): *"The micalg parameter allows for one-pass
    processing when the signature is being verified."* §3.2.2 ¶7 (N-099): the
    smime-type is *"a suitable hint for mail client applications to indicate
    whether a message is "signed", "authEnveloped", or "enveloped" without having
    to tunnel into the CMS payload."* For an unrecognised micalg, R-0120 asks only
    that receivers *"recover gracefully"*.

    Ours: SPEC-0002 §5, where `suite` and `says` are *"no — a hint; checked against
    the TBS in step V6"*, and *"The envelope exists so that a verifier can verify
    before it decodes."*

    **SPEC-0002's envelope is micalg with the missing check (inferred).** S/MIME's
    hints sit outside the signed bytes, as ours do, but RFC 8551 has no rule that a
    verifier compare micalg with the SignerInfo's digest algorithm, or smime-type
    with the CMS content type. SPEC-0002 V6 makes a disagreement
    `envelope-mismatch`. **Consequence:** keep V6, and keep the hints out of every
    user-facing decision until it passes (adopt 1). [CMS, outside this source]:
    a SignerInfo's `digestAlgorithm` and `signatureAlgorithm` are themselves outside
    the signed attributes; RFC 6211 (not held) later added an attribute to protect
    them. KSA's suite is inside the signed bytes: *"A statement's suite is inside
    its TBS and is therefore covered by its signature."* (SPEC-0002 §6.1).

## 2. What we adapt, and how

Each item names what RFC 8551 does, where the KSA specifications stand, and the
change a later engineer would make.

1. **An algorithm lifecycle that announces its direction, and a policy for the
   historic.** §1.3 (N-005) defines SHOULD+, SHOULD- and MUST-. Of MUST-:
   *"Although its status will be determined at a later time, it is reasonable to
   expect that if a future revision of a document alters the status of a MUST-
   requirement, it will remain at least a SHOULD or a SHOULD-."* §1.5 to §1.7 and
   Appendix B record each version's moves, and state machine M11 models them.
   Appendix B ¶1 (N-175) gives the cost: *"This means that if a user has historic
   emails and their user agent has been updated to only support the current set of
   recommended algorithms, some of those old emails will no longer be
   accessible."* B.2 (N-177) gives the answer: *"For this reason, it is strongly
   suggested that user agents treat these signatures differently from those on
   current messages."*

   Ours: SPEC-0002 §6.2's status column has `default`, `reserved; not yet
   specified` and `provisional`; §12: *"Every registry in this section is
   append-only."*, and *"a withdrawn entry becomes "reserved, never assigned"."*

   **Gap (inferred):** SPEC-0002 has a word for a suite on its way in
   (`provisional`) and none for one on its way out. Withdrawn as written, a suite's
   statements all become unverifiable at once (§6.1), which is Appendix B's *"no
   longer be accessible"* for an archive (MD-1). **Adaptation:** add two statuses.
   `deprecated` means verify, never sign (SHOULD- and MUST- in S/MIME's terms).
   `historic` means verify with a policy marker, and use for authorization only
   statements with independent time evidence from before the deprecation date
   (SPEC-0001 §11). Add a SPEC-0004 §9 policy row for each. The kid's derivation
   is per suite (adopt 7), so deprecating a suite deprecates its kids too, and
   rotation (SPEC-0004 §7.2) is the migration path. Test: TV-4 re-evaluated with
   suite 1 marked historic verifies with a marker, never silently. Open question
   3.

2. **Algorithm transition by parallel signatures.** A SignedData carries a set
   of SignerInfos. §3.5.3.1 (N-114): *"The signerInfos field contains the
   signatures for the MIME entity."* multipart/signed names several digest
   algorithms. R-0118: *"If multiple message digest algorithms are used, they MUST
   be separated by commas per [RFC1847]."* How the results combine is not
   defined. Protocol `multiple-signers-undefined` records the gap, and error path
   `multiple-signatures-mixed` gives the outcome *"Unspecified in this
   source."*

   Ours: one envelope, one suite, one `sig`. The statement digest is *"SHA-256 of
   the statement's TBS, under the statement's own suite"* (SPEC-0002 §4.5). A key
   *"belongs to exactly one cipher suite"* (SPEC-0001 §5.1). And suite 8 *"MUST NOT
   be the only suite a wallet offers until they are."* (SPEC-0002 §6.5).

   **Finding (inferred):** KSA can express a transition only as two keys making
   two statements, linked by a trust statement from the identity key (SPEC-0001
   §3.1). That yields two digests and two speakers for one claim. Three
   consequences follow.
   - Everything that cites a statement by digest binds one copy: `revoke` (§8.7),
     `review` and `approve` of `[3, …]` (§8.10), `aggregate.inputs` (§8.11). A
     `revoke` of the Ed25519 copy leaves the ML-DSA copy live.
   - Distinctness in thresholds and panels is by kid. SPEC-0004 §6.4: *"Keys that
     a rotation (§7.2) links count as one member."* SPEC-0005 §4.3: *"A party that
     controls two unlinked keys is two members unless the panel's author prevents
     it"*. A reviewer who holds parallel suite keys, both delegated, counts twice.
     The design record says otherwise for panels: ARCH-0003 W-24, *"`distinct:
     speaker` counts keys, and keys delegated from the same identity key count
     once"*. ARCH-0003 is a draft (*"Nothing here is accepted."*) and SPEC-0005
     governs under ADR-0003, so as specified the reviewer counts twice; W-24 is
     route (b) below already written down.
   - In CMS, parallel signers are linked by their certificates' subject name,
     which we reject (reject 3). The link has to be explicit.

   **Adaptation, two routes.** (a) A multi-signature envelope over one TBS, with
   the suite moved out of the TBS into a per-signature authenticated element.
   This is COSE_Sign's shape and DEC-002 option 2's native form, and it changes
   signed bytes, which is MAJOR under SPEC-0002's version policy. (b) Keep one
   signature per statement, and make parallel suite keys of one persona count as
   one member, as rotation-linked keys already do (SPEC-0004 §6.4, SPEC-0005
   §4.3), with `revoke` covering the persona's copies. Open question 2. This is
   cut 3 against option 5 in §6.4.

3. **Designate the encryption key by signature, never by name.** §2.5.3 ¶1
   (N-048): *"The encryption key preference attribute allows the signer to
   unambiguously describe which of the signer's certificates has the signer's
   preferred encryption key."* R-0057 and its sequel: *"This, however, represents
   only a preference, and the receiving agent can use any certificate in replying
   to the sender that is valid."* Without the attribute, the recipient's key is
   found by subject name (R-0060; reject 3).

   Ours: SPEC-0001 §3.1, *"Further keys — per context, per device, per protocol —
   are delegated from the identity key by ordinary trust statements (SPEC-0002
   §8.6)"*; SPEC-0002 §12.7, usage code 6 `transport (SPEC-0001 §8)`; SPEC-0001
   §8.2, mailbox messages *"encrypted to the recipient persona's key with HPKE
   [RFC9180]"*, which requires key exchange, *"which KSA's suites do not yet
   do"*.

   **Adaptation (inferred):** once the mailbox is specified, the recipient
   persona's transport key is designated by a signed statement of its identity
   key. That is the KSA form of SMIMEEncryptionKeyPreference, and a sender
   encrypts only to a designated key, never to one found by label. Unlike S/MIME,
   the designation is the only route. There is no fallback to "any certificate …
   that is valid", because a KSA key has no validity apart from trust evaluation:
   *"A key in the key store is known, not trusted."* (SPEC-0002 §10). Which kind
   carries the designation, a `trust` about a transport-usage type or an
   `attestation` by the identity key, is open question 7. It is cached as adopt 6
   says.

4. **Unsigned outer metadata: protect it or label it.** §3.1 ¶10 (N-075), R-0082:
   *"In order to protect outer, non-content-related message header fields (for
   instance, the "Subject", "To", "From", and "Cc" fields), the sending client MAY
   wrap a full MIME message in a message/rfc822 wrapper in order to apply S/MIME
   security services to these header fields."* R-0083: *"Given the security
   difference between headers, it is RECOMMENDED that the receiving client provide
   a distinction between header fields, depending on where they are located."* The
   default is unprotected. §3.1 ¶1 (N-068): *"A MIME entity that is the whole
   message includes only the MIME message headers and MIME body and does not
   include the rfc822 header."*

   Ours: SPEC-0001 §8.1's presentation map carries `audience`, `nonce` and
   `created`, and *"`presented` is OPTIONAL."* Yet *"A relying party that supplied
   a nonce MUST check that the presentation carries it and that `audience` is its
   own kid."*

   **Finding (inferred):** a presentation's `audience`, `nonce` and `created` are
   KSA's rfc822 header. They sit outside every statement's signature and are
   covered only when the presenter adds `presented`. As written, SPEC-0001 §8.1
   makes the nonce check mandatory and the proof of possession optional, so a
   relying party can "check" a nonce that anyone could have inserted. The gap is
   inherited from the design record, not introduced by SPEC-0001: ARCH-0003 §3.8's
   `Presentation` already has `audience: ? KeyId`, `nonce: ? Bytes` and
   `proof: ? Signature`, all optional and independent. No ARCH, ADR, DEC or MD
   text at 643fba2 ties the nonce to the proof.
   **Adaptation:** a relying party that supplied a nonce requires `presented` and
   verifies its `sig` before it checks `nonce` or `audience`. Without `presented`,
   those fields are rendered as unprotected, as R-0083 asks of the outer header.
   Test: a presentation with no `presented` whose `nonce` equals the challenge
   fails the freshness check. Open question 5.

5. **Email as a carrier: one media type, an extension as a hint, never reliance
   on the extension.** §3.2.1 ¶4 (N-096): *"When a MIME entity of type
   application/pkcs7-mime (for example) arrives at a gateway that has no special
   knowledge of S/MIME, it will default the entity's media type to
   application/octet-stream and treat it as a generic attachment, thus losing the
   type information."* And R-0107 and R-0108: *"A proper S/MIME implementation
   MUST use the media types and MUST NOT rely on the file extensions."* §5
   registers both media types (N-149, N-150).

   Ours: SPEC-0001 §8.2 names `application/ksa-presentation`. ARCH-0003 §7 names
   *"a presentation as a MIME attachment (`application/mofn-presentation`)"*, and
   gives the reason for carrying rather than building: *"S/MIME and OpenPGP
   clients are heavy; we would carry presentations, not reimplement either"*.

   **Finding:** our two documents give two media types for the same attachment,
   and neither is registered. SPEC-0001 governs, so ARCH-0003 §7 is the one to
   correct. **Adaptation:** one name, and a file extension as a gateway hint
   (S/MIME's `.p7m` move). Identification is by decoding, never by name or
   extension: an attachment is a presentation only if it decodes as one under
   SPEC-0002 §4.3. Whether to register the media type with IANA is open question
   6. Registering would be a registry dependence at the transport, which MD-3's
   "no IANA tags" does not reach.

6. **Keep the evidence with the archived signature.** B.2 (N-177): *"Certification
   authorities are not required to keep certificates on a CRL beyond one update
   after a certificate has expired.  This means that unless CRLs are cached as part
   of the message it is not always possible to check to see if a certificate has
   been revoked."* And: *"If a message is known to be historic and it has been in
   the possession of the client for some time, then it might still be considered
   to be secure."*

   Ours: MD-1, *"in-scope targets: software supply chain + archives/library."*;
   SPEC-0001 §6.2's acceptance records keep, *"for each statement relied on: the
   verdict, the context, and the anchors used"*; SPEC-0004 §7.1, *"the answer's
   reasons MUST state how many revocation statements were considered"*.

   **Adaptation (inferred):** for the archives target a count is not enough. An
   acceptance record should keep the digests of the revocation and rotation
   statements considered, and any timestamp evidence. Then re-evaluating an
   archived record years later can tell "no revocation existed" from "none was
   held". That is B.2's cached-CRL lesson, in a design whose revocations are
   statements and can be kept by digest. B.2's last clause, possession for some
   time, is SPEC-0001 §11's independent timestamp made by the holder: an archive's
   own receipt dates when it first held the statement. Test: re-run UC-3 after the
   reviewer's key is marked compromised. A record reviewed before the mark, with
   an archive receipt, still renders as reviewed, with a marker naming the receipt
   relied on. Open
   question 11.

7. **Mailbox encryption, when it is specified.** This collects what §3 and §6
   teach about the envelope we do not yet have (SPEC-0001 §8.2, provisional). The
   design record is ARCH-0003 §7: a mailbox with messages *"encrypted to the
   recipient persona's key"* (HPKE) and *"the suite's `key_exchange` part becomes
   non-empty"*, under W-19, *"The verdict is independent of transport. Channel
   encryption provides confidentiality only, never trust."*
   - **AEAD only.** §3.3 ¶1 (N-101): *"Thus, it is possible to replace ciphertext
     in such a way that the processed message will still be valid, but the meaning
     can be altered."* §6 ¶24's Efail paragraph shows the CBC case. HPKE is
     AEAD-based (RFC 9180, outside this source; inferred).
   - **Encrypt to self.** R-0112: *"In addition to encrypting a copy of the
     content-encryption key (CEK) for each recipient, a copy of the CEK SHOULD be
     encrypted for the originator and included in the EnvelopedData (see [RFC5652],
     Section 6)."* A wallet keeps its own sent requests readable.
   - **One recipient per message.** §6 ¶18: *"Having more than one recipient would
     allow for the second recipient to create a message that the first recipient
     would believe is from the sender by stripping the second recipient from the
     message."* The mailbox already has this shape: messages are *"addressed by
     kid"*.
   - **Sign inside, and name the recipient inside the signature.** §3.7 ¶4
     (N-127): *"A recipient of a message that is signed and then encrypted can
     assume that the signed message itself has not been altered but that a careful
     attacker could have changed the unauthenticated portions of the encrypted
     message."* §3.7 ¶3 (N-126): *"When signing first, the signatories are then
     securely obscured by the enveloping."* The source does not name it, but a
     signed-then-encrypted message that does not name its recipient inside the
     signature can be decrypted and re-encrypted to someone else (surreptitious
     forwarding; inferred, not in this source). A KSA statement is durable (*"A
     statement is a durable assertion; replaying it is not an attack on it."*,
     SPEC-0002 §13.8), so the risk is confined to mailbox messages whose meaning
     depends on the recipient, such as a review request or a possession challenge.
     The answer is SPEC-0001 §8.1's: bind `audience` under a signature. Signing
     first also hides the speaker's kid from the relay, which then sees *"only
     ciphertext and a recipient kid"* (SPEC-0001 §8.2).
   - **No weaker copies, padding, no compression.** R-0146: *"In other words, a
     sender SHOULD NOT send a copy of a message using weaker cryptography than they
     would use for the original of the message."* §6 ¶22 (N-168): *"Applications
     for which this is a concern need to provide some type of padding so that the
     length of the message does not provide this information."* §6 ¶23 (N-169)
     warns that *"care needs to be taken when designing a protocol that relies on
     using compression, so as not to create a compression oracle."* KSA defines no
     compression; keep it so. CompressedData has no counterpart.
   - **A capability announcement for key exchange.** SMIMECapabilities exists
     because a sender must pick a cipher its recipient can decrypt (§2.7.1). A
     signed statement needs no such negotiation (adopt 5), but key exchange will.
     The mailbox definition needs a signed list of supported key-exchange suites,
     cached as adopt 6 says.

   Tests: one per bullet, in the mailbox definition's vectors when it lands. Open
   question 8.

8. **Canonicalise at authoring, under one cited algorithm, not one per media
   type.** R-0085 (§3.1.1 ¶1, N-077): *"Each MIME entity MUST be converted to a
   canonical form that is uniquely and unambiguously representable in the
   environment where the signature is created and the environment where the
   signature will be verified."* §3.1.1 ¶2 (N-078): *"The exact details of
   canonicalization depend on the actual media type and subtype of an entity and
   are not described here."* §3.1.1 ¶3 (N-079): *"In general, canonicalization will
   be performed by the non-security part of the sending agent rather than the
   S/MIME implementation."* For text, R-0088 to R-0091; R-0089 reads *"The line
   ending MUST be the pair of characters \<CR\>\<LF\>"*.

   Ours: proposal §3.4, *"Canonicalization happens once, at authoring time, on
   trusted input."*; R-O-03, *"Canonicalization algorithm for each concrete
   encoding SHALL be cited, not invented silently."*; SPEC-0002 §4.3, *"Rejection
   MUST NOT be replaced by repair"*.

   **What we take:** canonicalisation belongs to the producer, before signing.
   R-0085 and proposed R-O-05 agree on when. **What we change:** RFC 8551 does not
   say what the canonical form is. It hands the definition to each media type's
   standard (R-0087) and the work to code outside the security boundary, so the
   S/MIME signer signs whatever the non-security part handed it. That is the
   failure R-O-03 exists to prevent. KSA has one canonical form, cited (RFC 8949
   §4.2.1 as restricted by SPEC-0002 §4.2), and the verifier's rejecting decoder
   checks it, so a producer's bug becomes a rejection, not a signature over
   unintended bytes. **A precision (inferred):** a multipart/signed first part
   stored in local line endings has to be rebuilt to \<CR\>\<LF\> before its
   digest can be computed. The source prints its own samples without them: *"Though
   not shown here, the end of each line is \<CR\>\<LF\>."* (§3.1.4 ¶1). In
   practice, then, clear-signed S/MIME canonicalises at verification. KSA never
   does (SPEC-0002 §3, property 1).

## 3. What we reject, and why

1. **Liberal acceptance, and graceful handling of the unknown.**
   §1.1 ¶5 (N-002): *"In general, the best strategy is to follow the Robustness
   Principle (be liberal in what you receive and conservative in what you
   send)."* R-0030: *"Receiving agents SHOULD handle attributes or values that they
   do not recognize in a graceful manner."* R-0047 makes it a MUST for capability
   values, and R-0120 asks the same of micalg. `requirements.yaml` marks R-0030 and
   R-0047 testable only in part, because *"graceful is not defined"*.

   Ours: ARCH-0002 P5, *"an unknown field in a signed payload is an error, not
   something to skip."*, argued from *"CVE-2025-59420: Authlib accepted unknown
   `crit` header parameters"*; SPEC-0002 §7.1, *"The statement map is closed: a key
   not listed above MUST cause rejection."*; §13.5, *"A verifier MUST NOT skip what
   it does not understand (ARCH-0002 P5)."*

   **Why:** a signed attribute the verifier does not understand is signed content
   it did not evaluate, which is P5's CVE case. RFC 8551 half agrees. A structural
   violation of either S/MIME attribute fails the signature (R-0039 and R-0051:
   *"If a signature is detected as violating these requirements, the signature
   SHOULD be treated as failing."*). And a signer must be shown what it signs
   (R-0031: *"Interactive sending agents that include signed attributes that are
   not listed here SHOULD display those attributes to the user, so that the user is
   aware of all of the data being signed."*). We keep R-0031's half: SPEC-0001 §7.1
   already makes the claim phase show *"the sentence the statement will render
   as"*. We reject the graceful half. The robustness principle survives only as
   algorithm breadth (adopt 5), where "liberal" means verifying more suites, not
   accepting malformed input.

2. **A signer named through a certificate, and a certificate required to
   sign.** R-0124 (§3.9 ¶1, N-132): *"A sending agent that signs messages MUST have
   a certificate for the signature so that a receiving agent can verify the
   signature."* R-0061: *"S/MIME v4.0 implementations MUST support both
   issuerAndSerialNumber and subjectKeyIdentifier."* And §1.2 (N-003) defines a
   Certificate as *"A type that binds an entity's name to a public key with a
   digital signature."*

   Ours: R-M-02, *"A principal MAY be identified solely by key or key digest."*;
   R-O-01 (adopt 3); SPEC-0002 §10, where a key enters the store from a verified
   `key-publish` or an out-of-band import *"followed by the same check that the kid
   is the SHA-256 of the key"*; R-M-01, *"Native encoding SHALL NOT be X.509 /
   PKIX."*

   **Why:** issuerAndSerialNumber names the signer as the key a CA numbered N,
   which is relative to a CA and built on a name. The subjectKeyIdentifier choice
   is a certificate extension that need not be unique (adopt 7). In KSA a key
   verifies with no third party at all. **Consequence:** an imported S/MIME
   signature's speaker is the key in the signer's certificate, named by its KSA
   kid where its algorithm has a suite (§5's import table). The certificate is at
   most a foreign identity assertion about that key (R-I-05).

3. **Keys linked by name, and an arbitrary choice among them.** R-0060
   (§2.5.3.1, N-053): *"If an SMIMEEncryptionKeyPreference attribute is not found
   in a SignedData object received from the desired recipient, the set of X.509
   certificates SHOULD be searched for an X.509 certificate with the same subject
   name as the signer of an X.509 certificate that can be used for key
   management."* And: *"If multiple X.509 key management certificates are found,
   the S/MIME agent can make an arbitrary choice between them."* (Protocol
   `key-selection-wording` records that the sentence reads as if it meant the
   issuer.)

   Ours: G1, *"Key-centric principals; names are not globally unique
   identifiers."*; ARCH-0002 P6, *"a 'name' is just a type of attested string."*;
   SPEC-0001 §7.3, a wallet *"MUST NOT render a key by the key's self-asserted label
   alone"*; SPEC-0004 §3, *"An evaluator MUST produce the same answer for the same
   inputs"*.

   **Why:** in S/MIME two keys belong together because a CA wrote the same name
   into two certificates. In KSA they belong together only because a key said so
   (adapt 3). And an arbitrary choice is an input the evaluation does not
   determine, which SPEC-0004 §3 forbids. Test: two transport keys with the same
   `self.label` and no designation. The sender refuses; it does not pick one.

4. **The type indicator and the content digest as optional attributes.** §2.5
   (N-032) makes generating *"Message digest (Section 11.2 in [RFC5652])"* and
   *"Content type (Section 11.1 in [RFC5652])"* a SHOULD (R-0027). The §3.5.3.3
   sample's signed attributes carry messageDigest and no content type (examples
   S-05). [CMS, outside this source]: RFC 5652 makes both mandatory whenever
   signed attributes are present, and without them the content type is outside the
   signature.

   Ours: proposed R-O-05, *"The signed payload SHALL be the canonical encoding
   verbatim, carried with an authenticated type indicator."*; SPEC-0002 `kind`
   (key 1, REQUIRED) inside the TBS, and the domain-separation label, which *"is
   prepended to the bytes being signed and is never transmitted."*

   **Why:** a type indicator that can be left out is not the one R-O-05 asks for.
   KSA's is unconditional: `kind` in the TBS and the label in the signed input.
   **Consequence (inferred):** an imported S/MIME signature whose signed
   attributes lack a content type is imported with its type marked
   unauthenticated. The §3.5.3.3 sample is that case.

5. **Attributes and algorithms named by OIDs from delegated arcs.** §2.5.2 ¶6
   (N-045): *"Additional OIDs from the smimeCapabilities OID tree are then
   allocated for the other algorithms usages."* R-0045: *"In the event that an OID
   is ambiguous, it needs to be arbitrated by the maintainer of the registered
   SMIMECapabilities list as to which type of algorithm will use the OID, and a new
   OID MUST be allocated under the smimeCapabilities OID to satisfy the other use of
   the OID."* §2.5 ¶10 (N-035): *"Additional attributes and values for these
   attributes might be defined in the future."* smime-type guideline 3 (N-098):
   *"If no common string is assigned, then the common string of "OID.\<oid\>" is
   recommended"*. The arcs themselves are in the Appendix A module (N-174), under
   `us(840) rsadsi(113549) pkcs(1) pkcs-9(9)`.

   Ours: ADR-0001, *"Native extension points — type identifiers, predicate types,
   tags, header parameters — are identified relative to a defining principal, as a
   `(key, local label)` pair."*; ARCH-0002 P1, *"neither needs permission from a
   registry to exist"*; SPEC-0002 §7.1, *"all extensibility is through attributes
   whose types are defined in definitions"*.

   **Why:** natively an OID is a global identifier, excluded under P1 exactly as a
   CBOR tag is. At import an OID is a foreign label (rfc-5280 notes, §7).
   **A precision for ADR-0001's lineage (inferred).** ADR-0001 says *"SDSI
   localized principal names. Nobody localized type names."* An OID arc does
   localize type names, to the arc's owner. The S/MIME working group allocates
   attribute types under `id-aa`, inside RSA Data Security's `rsadsi(113549)` arc,
   without asking anyone. That is hierarchical delegation from a central root, the
   X.500 pattern for names, and its cost is visible in §2.5.2: an ambiguous
   allocation needs *"the maintainer"* to arbitrate. "Nobody localized type names"
   holds for **key-relative** localization, which is the claim that matters. It
   does not hold for **authority-relative** localization, which OIDs had before
   SDSI; the module's 1988 ASN.1 (N-173: *"This module uses the 1988 version of
   ASN.1."*) is this source's evidence of age. The rfc-2692 notes draw the same
   distinction for RFC 2692's code-author localization (their adopt 3).

6. **Clear-signing as the native form of a statement.** R-0114: *"In general, the
   multipart/signed form is preferred for sending, and receiving agents MUST be
   able to handle both."* §3.5.1 ¶2 (N-109): *"Messages signed using the
   multipart/signed format can always be viewed by the receiver whether or not they
   have S/MIME software."* In that format the second part *"contains the "detached
   signature" CMS SignedData object in which the encapContentInfo eContent field is
   absent."* (§3.5.3, N-113).

   Ours: SPEC-0002 §5 and §11 (adopt 8); proposed R-O-05, *"Any human-facing form
   SHALL be regenerated from verified canonical bytes."*

   **Why:** clear-signing buys readability without software, at adopt 8's cost.
   We get readability differently: by rendering from definitions after
   verification (SPEC-0003 §10). **What we keep is detachment.** A SignerInfo with
   signed attributes is a signature over a digest of the content. §2.1 ¶1:
   *"The result of this is placed in the message-digest attribute of the signed
   attributes."* That is exactly a KSA `attestation` whose `this` is
   `[2, 1, digest]`, which R-M-07 requires (*"Artifact statements SHALL bind at
   least one content digest."*). Detached content needs no clear-signed format.

7. **Two encodings where one would do.** ENC-01 records that the source defines
   BER and DER and assigns neither (*"Source silent."*). Signing time has two
   encodings chosen by year: R-0032, *"Sending agents MUST encode signing time
   through the year 2049 as UTCTime"*, and R-0033, *"signing times in 2050 or later
   MUST be encoded as GeneralizedTime."*, with a two-digit-year rule (R-0034). R-0046
   has absent-or-NULL parameters, and the same section's own example breaks it
   (TEN-01, S-10). Capabilities are matched by *"binary comparisons"* (ENC-06), so
   every one of these choices changes the bytes compared.

   Ours: SPEC-0002 §4.2, *"It is the single canonical encoding for every signed or
   hashed object (ADR-0003 D2)."*; §4.4, *"so every instant has exactly one
   encoding"*.

   **Why:** each pair is a place where two conforming implementations can
   disagree about bytes, and the source's own example violates its own MUST in
   the same section. ADR-0003 D2 and SPEC-0002 §4.4 already reject this. RFC 8551
   is a deployed demonstration of what they avoid. §6 scores it.

## 4. The record's verdict, tested

`record.yaml` says the record is `useful` because *"S/MIME 4.0 specifies no
delegation and no trust model, deferring certificates entirely."* Each clause
was tested against `.cache/rfc-8551.txt`, not assumed.

- **No delegation: holds.** Searched for *delegat*, *on behalf*, *proxy* and
  *authori*. *delegat* occurs twice, both in the IANA templates: *"Change
  Controller: LAMPS working group delegated from the IESG"* (N-149, N-150).
  *authori* occurs only as certification and certificate authorities (§3.9,
  B.2), in the §1.2 definitions of data integrity and data confidentiality
  (*"unauthorized changes"*, *"authorized to know the data"*), and as
  *"unauthorized parties"* (§6 ¶5). Nothing in the source lets one key grant
  another anything.
- **No trust model: holds.** Outside the copyright notice, *trust* occurs three
  times: the signing time is *"only as trustworthy as that signer"* (§2.5.1);
  *"a trusted gateway might remove the envelope"* (§3.1.2); and §6 ¶8 advises
  caution for agents that use large keys *"without first validating the
  certificate to a trust anchor"*. That is the only mention of an anchor, and it
  sets no policy. §4 ¶1 is the whole position (item 3 of the list above).
- **The third clause, deferring certificates entirely, is overstated.** RFC
  8551 defers certificate validation, *"only what they do after a certificate has
  been validated or rejected"*, but it does not defer depending on certificates. A signer must have
  one (R-0124). A receiving agent must be able to retrieve them (R-0125) and should
  store them (R-0126). Signers are identified only through certificates (R-0061 to
  R-0063). The certificate an SMIMEEncryptionKeyPreference attribute references
  is included unless already available (R-0052, R-0053). Recipient keys
  are chosen by certificate, including by subject name (R-0058 to R-0060). There is
  a certs-only message (§3.8, R-0122, R-0123). And §6 ¶8 advises validating to an
  anchor before using large keys. S/MIME's identity model is X.509's, and these are
  the places it enters.
- **The one signed key-to-key link.** In SMIMEEncryptionKeyPreference the
  signer's key names another of its certificates for encryption. It is a
  designation, explicitly *"only a preference"*, and it confers nothing; the named
  certificate must still be *"valid"* by the deferred rules. It is the closest RFC
  8551 comes to one key speaking for another, and it is not delegation
  (inferred). The delegation-models answer says *"The one S/MIME-specific
  contribution to delegation is §3.8's certs-only message"*. The key-preference
  attribute has a better claim to the word, though neither confers authority
  (open question 15; the topic is not edited here).
- **The trusted gateway** of §3.1.2 holds the recipient's decryption key. That
  is a decryption capability shared with a site by key custody, not by any
  statement (inferred), and it is not delegation in the source's terms either.

**Verdict:** `useful` holds. The reason's last clause should read *defers
certificate validation to RFC 5750 as printed (RFC 8550 for v4.0), while making
certificates the only way signers and recipients are identified*. That is
proposed only; `record.yaml` is not edited here.

## 5. Mapping to our decisions

Verdicts: **supports**, **narrows** (ours or the source restricts the other),
**contradicts**, **silent**, and, where none of those fits, **applies**
(R-I-01), **contrast** (R-M-02) and **scope** (MD-1). "Adopt n", "adapt n" and "reject n" point into §1 to
§3. The first two rows are the record's `bears_on`.

| Ours (quoted) | RFC 8551 (quoted, R-id) | Verdict |
|---|---|---|
| **R-I-01** *"Publish a mapping table for each supported foreign format: what is preserved, dropped, or inferred."* | The whole message format; ARCH-0001 §6 has no CMS or S/MIME row | **Applies.** §5.1 below drafts the table. Whether CMS becomes a "supported foreign format" is open question 9. |
| **R-I-05** *"Import X.509 only as a foreign identity assertion about a key (name or attribute), marked `provenance: x509`."* | R-0124; the §1.2 definition of Certificate; §4 ¶1 | **Supports.** An S/MIME signer's identity is a certificate's, so import happens at the certificate (reject 2). |
| **R-I-02** *"Import SHALL NOT require the foreign object to become a native trust anchor."* | §6 ¶8, *"validating the certificate to a trust anchor"* | **Supports (inferred).** The CA path that validates an S/MIME signer stays foreign: SPEC-0004 §4.3, *"A signature never makes an anchor."* |
| **R-I-03** *"Export to in-toto Statement + DSSE OR COSE_Sign1 + CWT claims (at least one envelope in v1)."* | §1 ¶3, S/MIME for *"the signing of software-generated documents"* | **Silent.** CMS is not an export target and nothing here asks for one; a COSE export re-signs (rfc-9052 notes §1a). |
| **R-M-01** *"Native encoding SHALL NOT be X.509 / PKIX."* | R-0124 | **Supports.** RFC 8551 is X.509 underneath; nothing in it is a candidate native encoding. |
| **R-M-02** *"A principal MAY be identified solely by key or key digest."* | R-0061 to R-0063 | **Contrast.** S/MIME's subjectKeyIdentifier is near to a key digest but not unique (adopt 7). |
| **R-M-05** *"Authorization composition SHALL be deterministic given an ordered cert set and ACL."*; SPEC-0004 §3 | *"can make an arbitrary choice between them"* (§2.5.3.1) | **Contradicted by the source; we reject it** (reject 3). |
| **R-M-07** *"Artifact statements SHALL bind at least one content digest."* | §2.1 ¶1, the message-digest attribute | **Supports.** A SignerInfo over signed attributes is a statement about a digest (reject 6). |
| **R-O-01** *"Every signed object SHALL have an issuer key that can be specified as `KeyId`."* | R-0124, R-0061; §2.4.4 and §6 ¶16 to ¶21 | **Supports**, with a contrast: an S/MIME signer has a key but is named through a certificate. AuthEnvelopedData has no issuer key at all (adopt 3). |
| **R-O-02** *"Short-lived validity preferred over revocation-heavy design; revocation still representable."* | B.2, CRLs not kept *"beyond one update after a certificate has expired"* | **Silent on the preference.** Supports keeping revocation evidence with archived statements (adapt 6). |
| **R-O-03** *"Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently."* | §3.1.1 ¶2, *"are not described here"*; R-0087 | **Contradicted by the source**: canonicalisation is delegated per media type (adapt 8). |
| **R-O-05 (proposed)** *"A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification."* | §6 ¶15, §6 ¶24; micalg (N-119); R-0027 | **Supports** (adopt 1, adopt 11). The optional content-type attribute falls short of its *"authenticated type indicator"* (reject 4). |
| **R-M-12 / ARCH-0002 P1 / ADR-0001** *"The native model depends on no centrally allocated registry for their meaning."* (ADR-0001's wording; proposal §7's R-M-12 row reads *"The native model SHALL NOT depend on a centrally allocated registry for their meaning."*) | OID arcs, R-0045 | **Contradicted natively**; OIDs are foreign labels at import. Adds a precision to ADR-0001's lineage (reject 5). |
| **ARCH-0002 P5** *"an unknown field in a signed payload is an error, not something to skip."* | R-0030, R-0047, R-0120 | **Contradicted by the source; we reject it** (reject 1). |
| **G1** *"Key-centric principals; names are not globally unique identifiers."*; **ARCH-0002 P6** (provisional) | R-0060 | **Contradicted by the source** (reject 3). |
| **NG5** *"Treat email addresses as globally secure names."* (a non-goal) | none | **Silent.** RFC 8551 never binds an address to a key; that is RFC 8550's, held as a stub. |
| **DEC-002 / MD-3** | the CMS envelope | §6. |
| **DEC-003** issuer and subject identifiers: *"Must specify: canonical key bytes before hashing."* | §2.6 ¶2 | **Supports** a full-length key digest (adopt 7). |
| **ADR-0003 D2** *"One canonical encoding for every hashed or signed object — statements and definitions alike."* | ENC-01; R-0032, R-0033; R-0046 | **Supports** (reject 7). |
| **DEC-008** (open) *"Signature verification, canonicalization, the reduction algorithm, and the definition of what "valid" means must stay fixed."* | §2.5.2's arbitration, R-0045 | **Supports** a fixed-core algorithm registry, at a cost option 2 does not pay (§6.4, cut 1). |
| **ARCH-0002 P2** (provisional) *"the cryptographic act is the saying"* | §2.4.4; §6 ¶16 to ¶21 | **Supports**: only a signature attributes (adopt 3). |
| **DEC-005** *"Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema."* | §3.5.1; §2.1 ¶1 | **Silent.** CMS is not an option. Evidence only that a signature over a digest makes clear-signing unnecessary (reject 6). |
| **SPEC-0001 §8.1** presentation | §3.1 ¶10, R-0082, R-0083 | **Narrows** (adapt 4): the nonce check needs the proof of possession. |
| **SPEC-0001 §8.2** transport | §2.4.4; §6 ¶16 to ¶24; §3.2.1 ¶4 | **Supports** an untrusted transport (adopt 3). Adapt 5 (media type) and adapt 7 (mailbox). |
| **SPEC-0001 §11** long-term verification | Appendix B; R-0002; R-0019 | **Supports**; extend to the whole path and to suite deprecation (adopt 10, adapt 1, adapt 6). |
| **SPEC-0002 §5** envelope hints | micalg, smime-type (N-119, N-099) | **Supports**, and is stronger (adopt 11). |
| **SPEC-0002 §6.2, §12.3** suites | §1.3's levels; Appendix B; M11 | **Narrows**: no status on the way out (adapt 1). |
| **SPEC-0002 §4.5, §6** one suite per statement | multiple SignerInfos; R-0118 | **Narrows**: transition needs parallel statements (adapt 2). |
| **SPEC-0002 §8.4** `speaks` | SMIMECapabilities, R-0068 to R-0072 | **Supports**, with a question about completeness (adopt 6, open question 1). |
| **SPEC-0002 §13.4, §13.6** | §2.6; R-0121; §6 ¶8 | **Supports**; KSA states the numbers (adopt 7, adopt 9). |
| **SPEC-0004 §7.2** `issued` | §2.5.1 ¶1; R-0071 | **Supports**, missing R-0071's future bound (adopt 4). |
| **UC-5; SPEC-0003 §6.3** *"This is the type behind the email-delegation scenario in UC-0001 §UC-5"* | none | **Silent.** RFC 8551 has no domain-scoped vouching for an address; UC-5 is the KSA-native replacement for what RFC 8550 does with CAs. |
| **MD-1** *"in-scope targets: software supply chain + archives/library."* | §1 ¶3; Appendix B | **Scope.** Software signing is named in §1 ¶3; historic messages are the archive problem (adapt 6). |
| **ARCH-0003 §7** secure email, carried and not reimplemented | §3.2.1 ¶4; §5 | **Supports carrying; the media type disagrees with SPEC-0001** (adapt 5). |

### 5.1 R-I-01: an S/MIME signed message as an external statement (draft)

SPEC-0001 §5.3: *"A wallet MAY import a signed object from another protocol as an
external statement, keeping its original bytes and mapping its speaker, subject
and claims through an interchange profile (ARCH-0001 §6), so that it can be
reasoned about by the same evaluation."* ARCH-0001 §6 has no row for CMS or
S/MIME. This is the table such a row would point to. It is a draft and every
row is *(inferred)*: RFC 8551 defines no import into anything.

| S/MIME / CMS element | becomes | |
|---|---|---|
| the received `ContentInfo` bytes | evidence, kept and cited by digest | **preserved** |
| signature verification | done once, at import, by a CMS verifier over the bytes as received (rfc-5280 notes §7) | **inferred.** KSA verifiers cannot redo it: no suite is RSA, and ECDSA P-256 is suite 2, *"reserved; not yet specified"* |
| signer's public key (from its certificate) | `[1, kid]` only where the algorithm has a suite: Ed25519 → suite 1, after checking the 32-octet encoding; others → no kid | **preserved for Ed25519, dropped otherwise.** An RSA or ECDSA signer cannot be a KSA speaker today |
| signer's certificate (name, mail address) | a foreign identity assertion about the key, `provenance: x509` (R-I-05); never an anchor (R-I-02) | **inferred**, signed by the importer |
| `messageDigest` attribute | the claim's target, `[2, digest-alg, bytes]`, where the digest is SHA-256, SHA-384 or SHA-512 (SPEC-0002 §12.5) | **preserved** |
| `contentType` attribute | recorded; if it is absent, the type is marked unauthenticated (reject 4) | **preserved or flagged** |
| `signingTime` | an attribute of the imported claim (*the signer says it signed at T*), not the importer's `valid.issued`, which is the importer's own claim | **preserved, as a claim** |
| the content itself (eContent, or the first part of a multipart/signed) | not carried; only its digest | **dropped** |
| `SMIMECapabilities` | nothing native; perhaps the mailbox's announcement later (adapt 7) | **dropped** |
| `SMIMEEncryptionKeyPreference` | nothing native until adapt 3 exists | **dropped** |
| `certificates` and `crls` in the SignedData | evidence by digest; never anchors | **preserved as evidence** |
| unsigned attributes, including countersignatures [CMS, outside this source] | nothing | **dropped** |
| several SignerInfos | one external statement per SignerInfo | **inferred** |
| outer mail headers (From, Subject) | nothing, or an annotation marked unprotected (adapt 4) | **dropped** |
| smime-type, micalg, name and filename | nothing; they are hints | **dropped** |
| EnvelopedData, AuthEnvelopedData | not imported; decrypted first, and any signed content inside is imported | **inferred** |

The result is a translation, a new statement the importer signs, as the rfc-5280
and rfc-9580 notes conclude for their formats. Nothing in the S/MIME envelope
becomes a native statement.

## 6. MD-3 and DEC-002

MD-3 reads: *"CBOR data model, no IANA tags, COSE as export only; type identity
is `(defining key, label)` per P1; YAML is the human form with a canonical
one-way mapping."* DECISIONS-0001 item 2: *"Still open: a narrowing is not an
acceptance, and no ADR exists."* ADR-0003 D2 put option 5's encoding into
SPEC-0002 and says of itself *"This ADR does not accept DEC-002"*. The 2026-10-12
minute recommends keeping MD-3 *"as the working direction"*, with *"the ADR must
answer the option-1 evidence explicitly"*. Nothing in this section decides
DEC-002.

**S/MIME is a signing envelope**: a content type, signed attributes, algorithm
identifiers, a signer identifier and a signature, encoded in ASN.1. So the rule
in `docs/extraction.md` applies, and the structure-by-structure mapping follows.
Its result, as for X.509 and OpenPGP, is a **non-mapping**: nothing in CMS
becomes native, and import is translation (§5.1).

### 6.1 Structure by structure

| CMS / S/MIME construct | our statement or envelope (SPEC-0002) | COSE export, where relevant | mapping |
|---|---|---|---|
| `ContentInfo` {contentType OID, content} (MSG-01) | the envelope array `[suite, says, tbs, sig, ? pub]` (§5) | `COSE_Sign1` (rfc-9052 notes §1) | **Shape only.** ContentInfo's type is an OID, excluded natively (reject 5). KSA's outer type is the array's shape, checked at V1 |
| `id-data` / `eContentType` (MSG-02, MSG-04; R-0020, R-0021) | `kind` inside the TBS, plus the DS label `KSA-STMT-SIG-v1\0` in the signed input | protected `content type`, label 3 (rfc-9052 notes §1) | **Same intent, authenticated unconditionally.** In CMS the content type is authenticated only through the contentType attribute [CMS, outside this source] (reject 4) |
| `SignedData` version and `digestAlgorithms` (MSG-03) | none; the suite fixes the digest (§6.1) | — | **Not carried** |
| `eContent` present (§3.5.2) | `tbs`, *"the octets exactly as signed"* (Appendix B CDDL) | payload, a bstr | **Same idea.** The content travels inside the signed structure as bytes |
| `eContent` absent: detached (§3.5.3, R-0115) | a statement whose `this` is `[2, digest-alg, digest]`; the content travels separately | payload `nil`, detached (rfc-9052 `messages.yaml`) | **Kept as targeting, not as a format** (reject 6) |
| `certificates`, `crls` (§3.8, MSG-33) | none in a statement; `key-publish`, `trust` and `revoke` statements travel in a presentation (SPEC-0001 §8.1) | X.509 headers exist in rfc-9360 (not read here); not carried | **Not carried.** A certs-only message is a presentation with no claim (inferred) |
| `SignerInfo` (MSG-05) | the statement | — | **The SignerInfo with its signed attributes *is* the statement**; KSA has no separate attribute layer |
| `sid`: `issuerAndSerialNumber` (MSG-06) | none | — | **Excluded** (reject 2) |
| `sid`: `subjectKeyIdentifier` | `says`, a 32-octet kid, unique (§4.5) | unprotected `kid`, label 4, a hint (rfc-9052 notes §1) | **Same intent; KSA's is a full digest** (adopt 7) |
| `digestAlgorithm`, `signatureAlgorithm` (MSG-16, MSG-17) | `suite`, inside the TBS (§6.1) | protected `alg`, label 1, from IANA's COSE Algorithms (rfc-9052 notes §2) | **One code names the pair.** The CMS fields are outside the signed attributes [CMS, outside this source] (adopt 11) |
| `signedAttrs` (MSG-07, MSG-08) | the statement map | protected header bucket | **Closed, not an open bag** (reject 1) |
| — `messageDigest` | `this = [2, …]`, or, when the content is the statement, the statement digest | payload | adopt 10, reject 6 |
| — `contentType` | `kind` + DS label | `content type` | reject 4 |
| — `signingTime` (MSG-09; R-0032 to R-0035) | `valid.issued` (§7.3), one time encoding (§4.4) | CWT `iat` (rfc-9052 notes §1: needs the CWT Claims header, not in RFC 9052) | **Same claim, one encoding** (adopt 4, reject 7) |
| — `SMIMECapabilities` (MSG-10, MSG-11) | `speaks` for definitions; nothing for suites | — | **Partly carried** (adopt 6, adapt 7) |
| — `SMIMEEncryptionKeyPreference` (MSG-14) | none yet | — | adapt 3 |
| — `signingCertificate(V2)` (§2.5, R-0028, R-0029) | `says` plus `pub`, checked by kid at V3 | — | **The key binds itself**; no certificate to bind |
| — an attribute the receiver does not know (R-0030) | a key not listed: rejection (§7.1) | `crit` (rfc-9052 notes §1) | **Inverted** (reject 1) |
| `signature` | `sig` over `DS ‖ TBS` | the COSE signature over `Sig_structure`, a second signature (rfc-9052 notes §1a) | **Does not port** |
| `unsignedAttrs` | none: *"An envelope is not itself hashed or signed"* (§5); its hints are checked at V6 | unprotected bucket | **Not carried.** A countersignature becomes a separate `review` or `approve` of `[3, digest]` |
| several `SignerInfo`s | one signature per statement | `COSE_Sign` with several signatures | **Not carried as written** (adapt 2) |
| `EnvelopedData`, `AuthEnvelopedData`, `RecipientInfo` (MSG-15, MSG-22) | nothing in the core; the mailbox, provisional (SPEC-0001 §8.2), addressed by kid | `COSE_Encrypt`, outside R-I-03 | **Not carried** (adapt 7) |
| `CompressedData` (MSG-24) | none | — | **Not carried** |
| `application/pkcs7-mime` with `smime-type` (MSG-27, MSG-28) | `application/ksa-presentation` (SPEC-0001 §8.2); the type is checked by decoding | — | adapt 5 |
| `multipart/signed` with `protocol` and `micalg` (MSG-36, MSG-37) | no native counterpart; micalg's role is the envelope's `suite` hint | — | reject 6, adopt 11 |
| `message/rfc822` wrapper (MSG-26) | presentation fields covered by `presented` (SPEC-0001 §8.1) | — | adapt 4 |
| X.509 certificate (§1.2) | a foreign identity assertion (R-I-05) | rfc-9360 | §5.1 |

**What we deliberately do not carry**, and why:
- **OIDs**, for content types, attributes, algorithms and capabilities (P1;
  reject 5).
- **issuerAndSerialNumber** and every name-relative signer identifier (R-M-02,
  reject 2).
- **Unsigned attributes**, and any unsigned region inside a statement (SPEC-0002
  §5).
- **BER**, and any second encoding: two time types, NULL or absent (SPEC-0002
  §4.2, reject 7).
- **SET OF with one value**: S/MIME's attributes are sets that may hold only
  one value (R-0038, R-0050), a constraint KSA's maps never need.
- **Byte-comparison of algorithm parameters** (ENC-06): a suite code is an
  integer.
- **Certificates inside signed objects.** A key is introduced by its own
  `key-publish` (SPEC-0002 §10).
- **Compression**, the RC2 parameter type (schema finding 8), the `smime-type`
  values and the micalg names.

### 6.2 DEC-002's options, as we state them

- **Option 1** (ARCH-0001 §7): *"Canonical S-expressions (RFC 9804) as canonical;
  JSON as diagnostic."*
- **Option 2**: *"CBOR + CDDL as canonical; COSE for signed form."*
- **Option 3**: *"JSON + RFC 8785 JCS as canonical; DSSE for signed form."*
- **Option 4**: *"Dual canonical (CBOR and JSON) with a documented bijection."*
- **Option 5** (proposal §3.3): *"CBOR as the canonical encoding, using the CBOR
  data model and deterministic encoding rules, but with no reliance on the IANA
  CBOR Tags registry and no native use of COSE header parameters."* Realised as
  KSA-CBOR, SPEC-0002 §4.2, under ADR-0003 D2.

DEC-002's drivers: *"library availability, SCITT alignment, SPKI fidelity, human
debug."* Option 1 is scored only where RFC 8551 bears on it; otherwise "not
scored". Options 3 and 4 are named in neither minute and are scored in the last
column for completeness.

### 6.3 Scored against RFC 8551

| RFC 8551 | Option 1 | Option 2 | Option 5 (KSA-CBOR) | Options 3 · 4 |
|---|---|---|---|---|
| **Algorithm names need a namespace and an arbiter.** R-0043 to R-0046; micalg values *"will be taken from the IANA "Hash Function Textual Names" registry."* (N-120) | not scored | **Inherits one.** IANA COSE Algorithms, with its review process (rfc-9052 notes §2) | **Runs its own.** SPEC-0002 §6.2 and §12.3; §12 says *"Specification Required"* means *"added by a revision of this specification accepted through an ADR."* | 3: not scored. 4: two namings (inferred) |
| **One encoding.** ENC-01; R-0032, R-0033; TEN-01 | **Meets**: one canonical form by definition | **Meets only with deterministic rules adopted**; COSE itself allows variation (inferred) | **Meets**: §4.2, §4.3, §4.4 | **4 fails by construction**, a second canonical form. 3: text, JCS |
| **Opaque bytes survive gateways.** §3.5.1 ¶3, §3.1.3 | meets as an opaque attachment (inferred) | meets | meets | **3**: a text format carried as text meets this only as an attachment (inferred) |
| **Authenticated type indicator, always.** R-0027; S-05 | not scored | `content type` is optional in COSE; the rfc-9052 notes adopt it at a cost of *"one media-type registration"* | **Meets unconditionally**: `kind` plus DS label | 3: DSSE's `payloadType` is inside PAE and so signed, but is a global string (rfc-8785 notes §8) |
| **Extensions by open, OID-named attributes.** R-0030; §2.5 ¶10 | meets P1: no IANA actions (rfc-2692 notes §4, citing rfc-9804 R-0066) | **Fails natively**: the COSE header registry is CMS's attribute-OID space by another name (ADR-0001, *"option 2 as originally written does not"*) | **Meets**: closed maps, `(DefinitionId, label)` | 3: `payloadType` is a global identifier (rfc-8785 notes §8) |
| **Parallel signatures for transition.** §3.5.3.1; R-0118 | not scored | **Meets natively**: `COSE_Sign`, one protected `alg` per signer | **Not as written**: one suite and one signature per statement (adapt 2) | 3: DSSE carries several signatures (not checked here) |
| **One-pass hint, checked.** N-119; V6 | — | `kid` in the unprotected bucket is a hint | **Meets**, with V6 | — |
| **Installed-base interop.** §1.4, *"S/MIME version 4.0 agents ought to attempt to have the greatest interoperability possible with agents for prior versions of S/MIME."* | none | **COSE consumers natively** (SCITT); no CMS interop | **Only through export**; every external consumer gets a re-signed object (rfc-9052 notes §1a) | 3: DSSE consumers natively |
| **Readable without the software.** §3.5.1 ¶2 | the advanced form is text, but is not the signed form (inferred) | no | no; the YAML form is never signed (SPEC-0002 §11) | **3**: JSON is readable as received (inferred) |
| **A media type at the transport.** §5; SPEC-0001 §8.2 | needed | needed | needed | needed |

### 6.4 Where RFC 8551 cuts against MD-3 and option 5

1. **Algorithm agility needs a namespace with an arbiter, and option 5 does not
   escape one. It runs one.** §2.5.2 shows the work is permanent. An OID turned
   out to be ambiguous (*"rsaEncryption was ambiguous because it could refer to
   either a signature algorithm or a key encipherment algorithm"*). Parameters
   needed byte-exact documentation (R-0041). And every version from §1.5 to
   Appendix B re-tabulates the algorithms. Option 5 takes no IANA tags, but
   SPEC-0002 §12 is a central registry for suites, kinds, targets and digests, with
   an ADR as its arbiter. That is right under DEC-008's fixed core (*"if a key may
   define how its own statements are validated, it may define them as
   always-valid."*), which is the rfc-9052 notes' answer to the `alg` problem.
   But it is a cost **option 2 does not pay**: option 2 inherits IANA's COSE
   Algorithms registry and its review. RFC 8551 is evidence that this is a
   perpetual maintenance burden, not a one-time table. **Names option 2.**
2. **The installed base is the design centre of every deployed envelope, and
   option 5 gives it up.** §1.4 (above). §1.1 ¶5's robustness principle. §2.2's
   asymmetric algorithm lists. Appendix B's whole purpose. RFC 8551 subordinates
   everything to interoperation with agents already deployed. Under option 5, every
   COSE consumer receives a re-signed object (rfc-9052 notes §1a), and no consumer
   of any deployed format verifies a KSA signature. Option 2 at least serves SCITT and COSE
   consumers natively (DEC-002's *"SCITT alignment"* driver). No option serves
   S/MIME consumers, because none is CMS (R-M-01), so this cut is against option
   5 relative to option 2 only. It is a cost, not a defect, but MD-3 should count
   it. **Names option 2.**
3. **Algorithm transition by parallel signatures comes free in option 2 and is
   absent from option 5 as specified.** Adapt 2's finding: under SPEC-0002 a
   post-quantum transition means two keys, two statements and two digests, with
   the threshold and panel double counting that follows from distinctness by
   kid. CMS has had parallel SignerInfos since PKCS #7 [CMS, outside this
   source], and `COSE_Sign` gives
   option 2 the same thing with a protected `alg` per signer. Option 5 could define
   a multi-signature envelope; SPEC-0002 has not. This is a cost **option 5 as
   specified** pays and option 2 does not. **Names option 2**, or a SPEC-0002
   change.
4. **Readability without the software (weak).** multipart/signed exists so that
   *"Messages signed using the multipart/signed format can always be viewed by the
   receiver whether or not they have S/MIME software."* (§3.5.1 ¶2). The option 5
   signed form is unreadable without a tool, and the YAML form is never signed. Of the options,
   only option 3's JSON can be read as it arrives (inferred), and option 3 is
   recommended for withdrawal on other grounds (DECISIONS-0001 standing note:
   *"Option 3 should be withdrawn rather than out-scored"*). Recorded against
   DEC-002's *"human debug"* driver. It does not move the result. **Names option
   3.**

Searched and found **not** to cut against option 5:
- **Detached signatures.** A target `[2, digest-alg, digest]` gives every
  detachment CMS's absent eContent gives (reject 6).
- **Canonicalisation.** RFC 8551's per-media-type rule is the failure R-O-03
  forbids under every option (adapt 8).
- **Streaming.** CMS's silence on BER versus DER (ENC-01) leaves room for
  indefinite lengths, which a streaming producer needs [CMS, outside this
  source], and SPEC-0002 §4.1 forbids them. That costs nothing for statements,
  because large content is referenced by digest (R-M-07) (inferred).

### 6.5 Where RFC 8551 favours option 5

1. **Over option 2, on extensibility.** CMS's open, OID-named attribute bag is
   what P1 rejects, and COSE's header registry is the same structure (§6.3, row 5).
2. **Over option 4, and over CMS itself, on one encoding.** BER and DER, UTCTime
   and GeneralizedTime, NULL and absent are each a disagreement a single
   deterministic encoding cannot have (reject 7).
3. **Over option 2, on the type indicator.** It is mandatory by construction in
   KSA and optional in COSE, as it was in S/MIME's §2.5 (reject 4).

### 6.6 Not discriminators

Opaque binary versus clear-signed text: every option except 3 is binary, and 3
can be carried as an attachment. One-pass hints: any envelope can carry one and
check it. Resource bounds: SPEC-0002 §13.6 is option-independent. Media-type
registration: every option needs one to ride email. Unknown-field handling: P5
can be implemented under any option.

### 6.7 Net, stated as evidence

On encoding, RFC 8551 favours option 5 over CMS-shaped designs and over option
4, and it is nearly neutral between options 2 and 5. It cuts against option 5
in three places, and **all three name option 2**: a perpetual algorithm registry
that option 5 must run itself, the deployed consumers that only option 2 reaches
without re-signing, and parallel signatures for algorithm transition, which
COSE_Sign has and SPEC-0002 lacks. None of them concerns namespace governance,
which is the ground option 5 was created on (proposal §3.2), so none of them
reopens MD-3 by itself. They are what the DEC-002 ADR should weigh beside the
option-1 evidence the 2026-10-12 minute names. Nothing here decides DEC-002.

## 7. Open questions

1. **Is `speaks` a complete list or a partial one?** SMIMECapabilities is
   explicitly partial: *"The semantics of the SMIMECapabilities attribute specify a
   partial list as to what the client announcing the SMIMECapabilities can
   support."* (§2.5.2 ¶3). SPEC-0002 §8.4 says *"A relying party SHOULD check that an
   attester speaks a definition before relying on its attestations under it"*,
   which only makes sense for a complete list. Settle it in SPEC-0002 §8.4 and
   SPEC-0004 §9.
2. **Parallel signatures: one statement with several signatures, or one
   statement per suite with linked keys?** Adapt 2, routes (a) and (b). It
   decides whether a statement's digest depends on its suite, and whether
   SPEC-0004 §6.4 and SPEC-0005 §4.3 count parallel suite keys once. Settle it in
   SPEC-0002 §5 and §6 (MAJOR if route a), with the post-quantum-migration topic.
3. **A suite status vocabulary on the way out.** `deprecated` and `historic`,
   with SPEC-0004 §9 policy rows (adapt 1). Settle it in SPEC-0002 §6.2 and §12.3.
4. **Weakest-link strength.** Should a target's `digest-alg` be bound to its
   suite's strength (R-0002), and should SPEC-0001 §11's post-quantum advice apply
   to every statement on a path (R-0019)? Does suite 8's own pairing of ML-DSA-65
   with SHA-256 meet R-0002 (adopt 10)? Settle it in SPEC-0002 §6.5 and §7.2 and
   SPEC-0001 §11.
5. **The nonce without a proof of possession.** Must a relying party that
   supplied a nonce require `presented`? Adapt 4. Settle it in SPEC-0001 §8.1.
6. **The email media type.** `application/ksa-presentation` (SPEC-0001 §8.2)
   or `application/mofn-presentation` (ARCH-0003 §7)? With a file extension? Is
   an IANA media-type registration an "interchange boundary" in ADR-0001's sense,
   where *"Registry identifiers may appear at interchange boundaries, and such
   mappings are documented as lossy per R-I-01."*? Settle it in SPEC-0001 §8.2,
   then correct ARCH-0003 §7.
7. **Which statement designates a persona's transport key?** A `trust` from the
   identity key about a transport-usage type, or an `attestation` by the identity
   key (adapt 3)? Settle it in SPEC-0002 §8 and §12.7, when SPEC-0001 §8.2's
   mailbox is specified.
8. **The mailbox's ordering and binding.** Sign, with the recipient's kid inside
   the signed bytes, then encrypt (adapt 7)? The source does not name surreptitious
   forwarding; that is our inference. Settle it in the mailbox definition (ARCH-0003
   §7).
9. **Is CMS / S/MIME a "supported foreign format" under R-I-01?** If it is, §5.1
   becomes a MAP-NNNN document (CONTRIBUTING §6) and a row in ARCH-0001 §6. An
   S/MIME signer whose key is RSA or ECDSA cannot be a KSA speaker until a suite
   exists for it. Settle it with the WP5 owner, since X.509 import is WP5, and the
   proposal (§11) records that *"the execution plan places out of scope for the
   semester"* WP4 and WP5.
10. **Future-dated `issued`.** Should SPEC-0004 §7.2 refuse a `rotate`, or any
    ordering, whose `issued` exceeds the evaluation time by more than a stated skew
    (adopt 4)? What skew?
11. **Archive evidence.** Should acceptance records keep the digests of the
    revocation and rotation statements considered, not only their count (adapt 6)?
    Settle it in SPEC-0004 §10.3 and SPEC-0001 §6.2, for the MD-1 archives target.
12. **Conformance classes and suites.** Should SPEC-0001 §4.2 say a Statement
    Verifier verifies every final suite while a Producer needs one (adopt 5)?
13. **Unauthenticated content types on import.** Is an imported S/MIME signature
    with no `contentType` attribute admissible at all, or only as a weaker
    external statement (reject 4)? Settle it in the §5.1 profile if question 9 is
    answered yes.
14. **The library holds no CMS record.** Every [CMS, outside this source] row
    rests on RFC 5652 (and RFC 5083, and RFC 6211), and `rfc-8550` is a stub.
    Schema finding 5 already records that the module's import from
    `cms-2001(14)` cannot be checked from this source. Ingest `rfc-5652`, and take
    `rfc-8550` past stub, before §5.1 or §6.1 is built on. The
    namespace-governance topic, which owns this record, is the natural owner.
15. **The delegation-models answer and SMIMEEncryptionKeyPreference.** The topic
    says certs-only is *"The one S/MIME-specific contribution to delegation"*. §4
    finds the key-preference attribute a closer candidate, though neither confers
    authority. Should the answer say so? Settle it in `topics/delegation-models.yaml`
    (not edited here).

**Source defects, recorded and not repaired.** Each is already recorded in this
record's artifacts. This file only collects them.
- **References:** §7.1 swaps the [SMIMEv3.1] and [SMIMEv3.2] sets, and Appendix
  A calls RFC 5751 [SMIMEv2] (schema findings 1 and 2; TEN-09; protocol
  `reference-label-swap`). §4 ¶1 points at [RFC5750] where §7.1's [SMIMEv4] names
  RFC 8550. That one is noted in `state-machine.yaml`'s `not_modelled` and in
  the delegation-models answer, with no defect id of its own.
- **Requirement tensions:** R-0037 and R-0049, *"MUST include a single
  instance"* against *"If present"* (TEN-02; protocol
  `if-present-vs-must-include`); R-0022, *"the media type MUST be stored"* in
  eContent (TEN-03); R-0108 against §3.10's identification by suffix
  (protocol `extensions-vs-identification`); R-0125 puts a sending-side need on a
  receiving agent (protocol `retrieval-actor`).
- **A reason that does not match its rule:** R-0080's AES-128 CBC fallback is
  argued from a presumption about AES-GCM implementations (protocol
  `rule2-fallback-reasoning`, an ambiguity). The requirement itself is
  unambiguous and testable (`requirements.yaml`: `testable: yes`); only its
  stated reason is in question.
- **The NULL rule against its own example:** TEN-01, S-10, ENC-06.
- **Registrations and names:** application/pkcs7-signature registers no
  optional parameters, yet the §3.5.3.3 sample sends `name=smime.p7s` (TEN-07,
  schema finding 10); "RSA-OAEP" and "RSAES-OAEP" name one algorithm (schema
  finding 11); application/pkcs7-signature is not itself a §3.10 criterion
  (schema finding 12); "File extensions(s)" (schema finding 13). B.2's id-dsa
  sentence names no field (TEN-11).
- **smime-type naming:** guideline 1's `authEnv-*` against the registered
  `authEnveloped-data` (TEN-04, schema finding 9), and guideline 3's example OID is
  an algorithm, not a content type (TEN-05).
- **Samples:** §3.6's body is a bare zlib stream, not a ContentInfo (S-01,
  TEN-08). §3.5.3.3's messageDigest does not match its printed content (S-02,
  TEN-13), and its SignerInfo has version 2 and no content-type attribute (S-04,
  S-05). §3.4's GCM parameters and the mac length disagree (S-06). The
  rsaEncryption parameters differ between samples (S-07). The samples use dropped
  algorithms and key sizes (S-08, TEN-12). The §3.1.4 "image/jpeg" part is an
  OpenPGP packet (S-09).
- **Module:** `usa(840)` against `us(840)`, the misspelled `receipentKeyId`, an
  empty OID list, a capability comment narrower than §2.5.2, and the RC2
  parameter type that survives (schema findings 3, 4, 6, 7 and 8; TEN-09 for
  `usa(840)`, TEN-10 for the OID list and the comment).
- **Cross-references and gaps:** §3.1 cites §3.2 and §3.5 for content that is in
  §3.3, §3.4 and §3.6 (protocol `cross-reference-3.1`; TEN-06). The source leaves
  undefined: how several signers combine (`multiple-signers-undefined`),
  *"checking the timestamp"* (`timestamp-undefined`), a value for reasonable
  clock skew (`no-reasonable-skew-value`), and what "indicating an error
  condition" does (`error-condition-undefined`).

## 8. bears_on corrections

`record.yaml` lists R-I-01 and R-I-05. Both were checked against ARCH-0001
v0.1.2 at 643fba2. The record schema describes the field as *"ARCH-0001 DEC-\*/R-\*
ids this record informs."* `record.yaml` is not edited here.

- **Both stand.** **R-I-01**: §5.1 is the table R-I-01 asks for, and ARCH-0001 §6
  has no CMS row (open question 9). **R-I-05**: R-0124 makes certificates
  mandatory for signers, so S/MIME's identity is X.509's and import happens at the
  certificate.
- **Warranted additions:**
  - **R-O-05** (proposed): verify before acting, hints checked, opaque bytes, and
    the optional content type (adopt 1, adopt 8, adopt 11, reject 4).
  - **R-O-01**: a signer identified through a certificate rather than a key, and
    AuthEnvelopedData's lack of an issuer key (reject 2, adopt 3).
  - **R-M-12**: OID arcs, and the precision on ADR-0001's lineage (reject 5). Now
    ARCH-0002 P1 through ADR-0001; the id is already used in `bears_on` elsewhere
    in the library.
  - **DEC-002**: §6, including the three cuts that name option 2.
  - **R-O-03**: canonicalisation *"not described here"* and delegated per media
    type (adapt 8).
- **Weak, optional:** R-M-07 (the message-digest attribute, reject 6), R-M-02
  and DEC-003 (non-unique subjectKeyIdentifier, adopt 7), R-I-02 (§6 ¶8's trust
  anchor), R-O-02 (Appendix B.2).
- **Outside the field's vocabulary.** SPEC-0001 §8.1 and §8.2, SPEC-0002 §6.2 and
  §8.4, and SPEC-0004 §7.2 cannot be listed in `bears_on`. They are carried in §5's
  table. SPEC-0001 §8.1 is the one this record bears on most sharply (adapt 4).
- **The usefulness reason** should be refined as §4 proposes.

## 9. What this file decides

Nothing. CONTRIBUTING §5: *"Only an ADR accepts a decision."* Each adaptation and
open question above names the SPEC section or ADR that would settle it. The cuts
against option 5 in §6.4 are evidence for the DEC-002 ADR (DECISIONS-0001 item
4b), not a recommendation.
