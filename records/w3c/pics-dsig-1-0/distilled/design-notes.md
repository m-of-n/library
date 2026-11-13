---
record: pics-dsig-1-0
kind: design-notes
title: "pics-dsig-1-0 — bearing on our design"
extracted: "2026-11-12"
reviewed_by: ""
---

# PICS Signed Labels (DSig) 1.0 — bearing on our design

*PICS Signed Labels (DSig) 1.0* is the W3C Recommendation of 27 May 1998
(REC-DSig-label-19980527; `record.yaml` gives `maturity: historic` and records
its retirement on 2009-11-24). Source: the HTML, sha256
`69ecbc8314b767137281e6c3515bbb3a79fa2270434eae7cac18548c36eb261a`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass;
every line number below counts in its `bin/render-w3c --ordinal` rendering,
`.cache/pics-dsig-1-0.txt` (685 lines, sha256
`d9eafc9db7bd9a8b016c0d72ffd6d0c2c21f58ffafaec84e3e2a3cacdd7c2e94`, recomputed).
`bin/bcp14-count` finds no BCP 14 keyword in it: its obligations are lowercase.

DSig adds two extensions to a PICS 1.1 label. **resinfo** carries hashes of the
labelled resource. **sigblock** carries one or more signatures over a canonical
form of the label, together with certificates, key identification, a signing
time and coverage modifiers, none of which is signed. It replaces PICS 1.1's own
`MIC-md5` and `signature-RSA-MD5` options.

It reaches us in eight ways (`record.yaml` `bears_on`: DEC-002, DEC-005,
DEC-007, R-M-07, R-M-12, R-I-01, R-O-03, R-O-05).

1. **R-O-05.** DSig signs a form the verifier rebuilds from what it received. It
   is the design R-O-05 forbids, with its costs visible (X-01, K-01, §3, §4).
2. **DEC-007**, accepted by `ADR-0007`. Appendix 1 calls the unbound rating
   vocabulary a security hole (A-04, X-05).
3. **R-M-07.** resinfo is a digest set over one resource (A-03, D-01, C-01).
4. **R-M-12, now `ARCH-0002` P1.** Every algorithm, suite and certificate family
   is named by URL (X-04).
5. **R-I-01.** The `ARCH-0001` §6 PICS row says *"import profile only if
   needed"*. §5 drafts what that profile would carry and drop.
6. **DEC-005.** A detached label with the signature embedded in it: the road
   neither DEC-005 option takes (A-02, S-07, §6.5).
7. **DEC-002, accepted by `ADR-0004`, and MD-3.** §6, including where DSig cuts
   against option 5.
8. **R-O-03** and **mofn report R-0006** §2.2, whose PICS cells are empty. §7
   fills the ones this source answers.

What it is not: a transport protocol (Appendix 2 hands transport to PICS 1.1), a
trust model (it calls trust a trust-management question), or a specification of
any hash or signature algorithm (those live at the identifier URLs, outside
this source).

## Things to hold while reading

1. **Our decisions are read from m-of-n at `d7f7f89`** (origin/main), from the
   read-only snapshot this lane was given. Paths below are
   `<path>@d7f7f89`.

   | name | path | standing at d7f7f89 |
   |---|---|---|
   | ARCH-0001 v0.3.0 | `spec/ARCH-0001-authorization-attestation.md` | draft; §5 rows, §6 matrix, §7 decisions. **R-O-05 is a §5.3 requirement since v0.2.0** (`DECISIONS-0001` item 4); DEC-001, DEC-002, DEC-003, DEC-007 accepted; DEC-004, DEC-005 open |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (`ADR-0001`); P2, P3, P5 with P5.1 and P5.2, P6 accepted (`ADR-0002`); P1.1, P4, P7 draft; DEC-008, DEC-009 open |
   | ADR-0001 | `spec/ADR-0001-key-relative-naming.md` | accepted; R-M-12 becomes P1 |
   | ADR-0003 | `spec/ADR-0003-ksa-core-decisions.md` | accepted; the SPECs govern where they differ from an ARCH |
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25, `reviewed: false`; DEC-002 option 5 |
   | ADR-0005 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted; `kid` = SHA-256 of the suite's public-key encoding |
   | ADR-0007 | `spec/ADR-0007-dec-007-predicate-rendering.md` | accepted 2026-11-07, `reviewed: false`; DEC-007 option 2 |
   | SPEC-0001, SPEC-0002 v0.8.0, SPEC-0003 | `spec/SPEC-000{1,2,3}-*.md` | drafts; govern under `ADR-0003` |
   | ARCH-0003 | `spec/ARCH-0003-wallet-object-model.md` | draft |
   | DECISIONS-0001 v0.6.1 | `project/DECISIONS-0001.md` | the register |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing, closed by `ADR-0004` |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft; evidence, decides nothing; still calls R-O-05 *proposed* (§2.3), which v0.2.0 of ARCH-0001 overtook |
   | CONTRIBUTING | `CONTRIBUTING.md` | process; §5 |

   **`docs/extraction.md` is stale on one point**, as earlier design notes
   recorded: it says no DEC-002 ADR exists, and `ADR-0004` is that ADR. This
   file maps against `ADR-0004` and still records where the source cuts against
   option 5 (§6.3). `docs/` is not edited here.
2. **Quotation.** No word of DSig is typed here. A quotation of it is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote
   from `.cache/pics-dsig-1-0.txt`; optional anchors select a sub-span. A
   quotation of m-of-n is a `<!-- qm PATH Lx-y -->` marker: the words are lines
   x to y of `PATH` in the `d7f7f89` snapshot, a leading blockquote margin
   dropped and whitespace collapsed. They were written and checked by the lane's
   `qm.py`, and each was checked a second time by a fixed-string containment
   test (the `grep -F` of the brief, run on the whitespace-collapsed file), each
   against its own file only. `bin/check-quotes` cannot see a `qm` marker. **PICS 1.1 (`pics-1-1-labels`) is cited by locator
   and line, never quoted here**: its words are checked only against its own
   source, in its own record. Names in backticks (`resinfo`, `SigCrypto`) are
   identifiers, not quotations.
3. **Locators.** The source has no section numbers. A `§n` of the source is the
   renderer's structural ordinal and travels with its heading title or a line
   number, for example §8.1.2 (Canonicalization of the equivalent standalone
   label for signing) or §8.1.2 L534. `Lnnn` is a line of the `.txt` and is
   exact. A `§n` after another document's name (`SPEC-0002` §7.2) is that
   document's; a bare `§n` is a section of this file.
4. **Labels.** *(inferred)* marks what the source implies rather than states,
   and every consequence drawn here. **Ours** marks the library's proposal.
   **[outside this source]** marks a statement resting on a document the
   library does not hold for this record; such a statement is never quoted and
   never the sole ground of a verdict.
5. **Numbering.** `R-M-NN`, `R-I-NN`, `R-O-NN` are `ARCH-0001` §5. `P1` to `P7`,
   `P1.1`, `P5.1`, `P5.2` are `ARCH-0002`. `V1` to `V9` are `SPEC-0002` §9.2.
   *Condition (n)* is one of the six of mofn report R-0006 §3.2. `MD-n` are dated
   meeting decisions. Row ids here are `A-nn` adopt, `D-nn` adapt, `X-nn`
   reject, `C-nn` constrains, `K-nn` conflicts, `S-nn` silent; source defects
   are `SD-n`. **No requirement id of this record is cited**: the requirements
   lane assigns them in this same pass, and joining quotations to ids is the
   verify pass's job, as it was for `w3c-vc-data-integrity-1-0`.
6. **Levels.** The source's *must*, *should* and *may* are lowercase prose. A row
   reports them as printed and gives them no BCP 14 force.

---

## 1. Rows by verdict

37 rows: **9 adopt, 4 adapt, 9 reject, 6 constrains, 2 conflicts, 7 silent**.
*Adopt (confirms)* means the source does what a decision of ours already does,
and is recorded as independent evidence for it, not as a new commitment.
**constrains** means one side narrows what the other leaves open, so an
implementation can satisfy both by taking the narrower path; **conflicts** means
none can.

| id | verdict | in DSig | where | maps to | finding |
|---|---|---|---|---|---|
| A-01 | adopt (confirms) | A signature is the signer's assertion that the label's statements are valid, not a claim to have written them; `by` is informational | §6.1 (Semantics of Embedded Signature Blocks) L133-134; §5 (PICS Architecture) L76-79; §6.2 (Applying PICS to DSig) L148 | `ARCH-0002` P2; `ARCH-0001` §4.2 | the speaker is whoever holds the key, as P2 says |
| A-02 | adopt (confirms) | A label never wraps the resource it is about and can always be separated from it | §4 (DSig 1.0 Overview) L60-62 | `SPEC-0002` §7.2; `ARCH-0001` §4.2 attestation; DEC-005 | a detached assertion about a subject: KSA's `attestation` |
| A-03 | adopt (confirms) | The resource is its bytes, not its URL: a hash fails for any other document, whatever URL fetched it | §7.2 (Resource Reference Information Extension) L203, L205 | R-M-07, R-M-11; `SPEC-0002` §7.2 | the reason KSA withdrew the locator target, stated in 1998 |
| A-04 | adopt (the diagnosis) | Appendix 1: rating semantics can change after a label is made, without invalidating it | §9 (Appendix 1: Service Resource Information) L613-614 | DEC-007 (`ADR-0007`); `ADR-0003` D1; `SPEC-0003` §1, §13.2 | the hole DEC-007's acceptance test closes by construction; the mechanism is X-05 |
| A-05 | adopt (confirms) | The signing time in the sigblock is advisory; a protected date belongs inside what is signed | §7.3.4.6 (The "On" token: Time of Signature generation) L376-381 | `SPEC-0002` §7.3; `SPEC-0001` §11 | `issued` is already inside the TBS |
| A-06 | adopt (confirms) | Parallel signatures are independent and may be added at any time; a cascade is a label about a label | §7.4 (Parallel and cascaded signatures) L411; §5 L78 | R-M-06; mofn report R-0006 §5.1; `SPEC-0002` §8.6, §8.10 | a count of signatures is not a threshold. A cascade needs a label identity DSig never defines (S-04) |
| A-07 | adopt (corroborates R-O-03) | A canonicaliser specified in prose, re-invented without citing PICS 1.1's, whose worked example departs from its text twice | §8.1 (Signing a label) L519; §8.1.2 (Canonicalization of the equivalent standalone label for signing) L534-537; §8.2 (An Example) L569-575 | R-O-03 | §8 check 1 |
| A-08 | adopt (the designers' own verdict) | `include` and `exclude` exist only to work around PICS 1.1 protocols and are meant to be absent from DSig 2.0 | §7.3.4.7 (The "include" and "exclude" tokens: modifying the canonicalized form of the label) L385, L399 | R-O-05; `SPEC-0002` §7.1 (closed map) | partial coverage was a workaround its authors disowned |
| A-09 | adopt (the intent) | An incompatible change of an identifier is a new identifier; resinfo is closed, and new information is a new extension | §7.1 (URLs as identifiers) L198; §7.2 L216 | `SPEC-0002` §12 (append-only); `ARCH-0003` W-12 | immutable by convention here (*should*); by construction in ours |
| D-01 | adapt | resinfo: one resource, several hashes, one per algorithm; several versions of a document may not be labelled this way | §7.2 L206, L213; §7.2.1 (Detailed Syntax of the resinfo Extension in a PICS 1.1 Label) L220-222 | R-M-07; R-M-11 `aliases`; `SPEC-0002` §7.2, §12.5; mofn report R-0006 §2.3 | the source never says whether a verifier checks every hash or any one. A set form of ours must say, or the weakest algorithm governs (open question 3) |
| D-02 | adapt | Certificates, and links to them, ride unsigned and may be added or replaced after signing | §7.3.2 (Attribution Information) L294-296 | `SPEC-0002` §5 (`pub`), §10 (key store) | kept as a hint only: nothing in AttribInfo enters a key store or names a principal |
| D-03 | adapt | The key is named four ways: by key, by a suite-defined hash, by name, by CA and serial; all inside the unsigned sigblock | §7.3.4.1 (Keyholder tokens: information about keys related to the signature) L332-337; §7.3.4.3 ("ByHash") L360 | `ADR-0005`; R-M-02; R-O-01; R-M-03 | on import only `ByKey` yields a key; `ByHash` is the per-suite digest `ADR-0005` rejects |
| D-04 | adapt | The labeler and the signer may differ, and the rating service is neither | §5 L75-80 | `ARCH-0001` §4.2 (the PICS analogue) | under DSig the issuer is the signer and the rating service is the definer; `ARCH-0001`'s analogy fits PICS 1.1, not DSig |
| X-01 | reject | The verifier rebuilds the signed form: inherit service options, drop the sigblock, apply include or exclude, sort, lowercase, re-space | §8.1 L519; §8.1.1 (Creating an equivalent standalone label) L523, L530; §8.1.2 L534-538 | R-O-05; `ADR-0003` (rejected: sign a re-encoded statement); `SPEC-0002` §5, §13.1; P5.1; condition (3) | §4: conflicts on every clause |
| X-02 | reject | Nothing in the sigblock is signed: suite identifier, key identification, signing time, coverage list, certificates | §7.3.2 L296; §7.3.4.6 L381; §7.3.5 (Hashing) L407 | R-O-05 (authenticated type indicator); `SPEC-0002` §6.1; condition (4) | the algorithm is covered only if a suite mixes it into the hash, which the source permits and does not require |
| X-03 | reject | Partial coverage, declared in the unsigned sigblock | §7.3.4.7 L385, L390 | R-O-05 (human-facing form); P5.2; `SPEC-0002` §7.1 | §3.2: anyone can add fields the signature never covered, including `for` and `gen`, to a label signed whole, and it still verifies |
| X-04 | reject (natively) | Algorithms, certificate families and suites named by URL: a registry of names rooted in DNS, each identifier's meaning a document fetched from it | §7.1 L187-199 | P1 (`ADR-0001`; R-M-12); `ADR-0004` item 3; `ARCH-0002` DEC-008; `SPEC-0002` §6.1, §12 | global names; at a boundary, lossy. Appendix 3 prints two of its four mandatory identifiers with a doubled slash (§9 SD-1) |
| X-05 | reject (the mechanism) | The vocabulary is named by the service URL, signed by name only; Appendix 1's remedy is a trust-engine policy demanding a separate signed label on the description | §8.1.2 L535; §9 L613-614 | DEC-007 (`ADR-0007`, option 4 rejected); `SPEC-0003` §1, §4.4, §13.2; P4 (sponsor direction) | the remedy signs the description; nothing makes the label cite which description (open question 2) |
| X-06 | reject (for us) | resinfo and sigblock are declared optional, so a client that does not understand them ignores the content binding and the signature | §6.2 L169; §7.2 L214; §7.3.1 (Format Specification) L282 | P5; `ARCH-0001` §3.4 (critical-bit row); `SPEC-0002` §13.5 | an explicit optional flag is P5's opt-in skippability; choosing it for the security-bearing fields is what we decline |
| X-07 | reject | Whether to use an unsigned or unverified label is left to trust management | §4 L57; §7.3.1 L282 | `SPEC-0002` §3, §9.1; R-O-05 | KSA decodes only after the signature verifies |
| X-08 | reject (as obsolete) | Mandatory to implement: MD5 and SHA-1 hashing, RSA-MD5 and DSS suites, with no deprecation path | §7.1 L199; §7.3.3 (Signatures) L324; §11 (Appendix 3: Conforming Implementations) L624-630 | `SPEC-0002` §6.1, §6.2, §12; `SPEC-0001` §11 | no DSig suite is a KSA suite, so a DSig signature is unverifiable natively (§5) |
| X-09 | reject | A suite may add inputs to what is signed and decides whether partial signatures are allowed | §7.3.3 L324; §7.3.4.7 L385; §7.3.5 L407 | `ARCH-0002` DEC-008 (proposed answer); `SPEC-0002` §6.1 | part of verification is defined by a document at the suite's URL |
| C-01 | constrains | resinfo is not valid in a generic label, so a generic label can never bind a digest | §5.1 (PICS 1.1 labels and label lists) L127; §6.2 L153; §7.2 L215 | R-M-07; `SPEC-0002` §7.2, §13.10 | no generic DSig label can become an R-M-07 attestation (§5) |
| C-02 | constrains | Without `for`, the subject is implied by where the label was found | §7.2 L204 | R-M-11; `SPEC-0002` §7.2, §13.10 | the delivery context is not signed; on import such a label has no target |
| C-03 | constrains | Two times: the label's `on` (created; signed) and the sigblock's `on` (signed when; unsigned) | §6.2 L155; §7.3.4.6 L376-381 | `SPEC-0002` §7.3; `SPEC-0001` §11 | `issued` cannot be filled from either without inferring |
| C-04 | constrains | The server must transmit enough options to rebuild the standalone label that was signed | §8.1.2 L538 | `SPEC-0002` §4.5, §13.7 | §13.7 is the bounded form of this rule: identifiers only, and a wrong rebuild fails V4 |
| C-05 | constrains | Sets without an order: resinfo's hashes (the example sorts them, the text does not), repeated `comment` options, multi-value items | §8.1.2 L536-537; §8.2 L569-575 | condition (5); `ADR-0004` (*Not decided here*); `ARCH-0001` §7 DEC-002 | condition (5) left to an example in a deployed design; still owed by `SPEC-0002` (§6.3) |
| C-06 | constrains | Dates: two separators, optional seconds and fractions, any offset | §7.2.1 L227-253 | `SPEC-0002` §4.4 | an import converts; a fraction of a second has no KSA form |
| K-01 | conflicts | No verifier can check a DSig signature without canonicalising what it received | §8.1.1 L530; §8.1.2 L538 | R-O-05; P5.1, for an import verified by us | §4 |
| K-02 | conflicts | The canonical form lowercases every symbol, and a transmit-name is a symbol; PICS 1.1 makes transmit-names case-sensitive | §8.1.2 L534; `pics-1-1-labels` §7 (Detailed Syntax) L141 | condition (1); R-O-05, which assumes (1) | two labels PICS 1.1 says differ share one canonical form, so one signature verifies both (§8 check 2) |
| S-01 | silent | Who may sign, and whether a signature is trustworthy: a trust management system decides | §7.3 (The Signature Block Extension) L274; §7.3.1 L282; §7.3.2 L294 | `ARCH-0001` §4.3; `ADR-0003` D3, D4; `SPEC-0004` | KSA specifies the reduction DSig leaves to a TMS |
| S-02 | silent | Key distribution, revocation, rotation | none in the source | R-O-02; `ADR-0003` D5; `SPEC-0002` §8.7, §8.8 | left to the certificates and their PKI |
| S-03 | silent | Which bytes resinfo hashes when the label sits inside the document it hashes, or the document is transfer-encoded | §7.2 L203; §10 (Appendix 2: Transporting DSig 1.0 Labels) L620 | R-M-07; `SPEC-0002` §7.2 | for HTML the source points back to PICS 1.1, whose MIC removes the labels first (`pics-1-1-labels` §13, L401) *(inferred)* |
| S-04 | silent | A label has no identity: nothing names the label a cascaded signature signs | §7.4 L411 | `SPEC-0002` §3, §8.10 | KSA content-addresses a statement by SHA-256 of its TBS |
| S-05 | silent | The verification procedure is never stated | the whole source; §8 (Signing) describes signing only | `SPEC-0002` §9.2 | why `state-machine` is not applicable (§11) |
| S-06 | silent | Separation between a label signature and any other use of the key | none in the source | `SPEC-0002` §6.4, §13.2; `SPEC-0001` §5.3 | the canonical form opens with `( pics-1.1`, a prefix by accident of syntax, not a label |
| S-07 | silent | DSSE or COSE_Sign1 | none in the source | DEC-005 (open) | DSig is the third road both options exclude (§6.5) |

---

## 2. Row details

### 2.1 Adopt

**A-01 — a signature is a saying.** DSig defines what a signature on a label
means, and it is P2's form:

<!-- q L133-134 "Thus, by definition" .. "are valid" -->
> Thus, by definition a PICS label which includes a DSig sigblock extension has the following semantics: "The entity possessing the secret key that digitally signed this PICS 1.1 label had access to the secret key and the label at the same time and asserts that the statements made within the label are valid

and, from the architecture section:

<!-- q L77 "By signing an assertion label" .. "within it are valid" -->
> By signing an assertion label, the signer explicitly confirms belief in the truth of the statements contained within the label. A signature does not indicate that the signer created the label, only that they believe the statements made within it are valid

Ours:

<!-- qm spec/ARCH-0002-key-relative-naming.md L146-148 "Per SDSI and SPKI" .. "saying meaningful." -->
> Per SDSI and SPKI, **the speaker is the key.** There is no separate notion of "who signed this" versus "who said it", and no authority above A that makes A's saying meaningful.

The `by` option names whoever created the label, and in DSig

<!-- q L148 "the by option name need not be" .. "signer(s)" -->
> the by option name need not be the same as that of the signer(s)

so it is a claim inside the label, not a speaker. **Confirms P2, nothing to
change.** It also fixes what an import may say a DSig label means (ours): that
the key holder asserts these statements, never that the `by` entity made them.

**A-02 — detached, never wrapping.**

<!-- q L60-61 -->
> At no time does a DSig 1.0 signature label 'wrap' the information resource it is signing; The signature label can always be separated from the information resource;

A DSig label is an assertion about a resource that lives apart from it, which is
what a KSA `attestation` targeting a digest is (`SPEC-0002` §7.2). DEC-005's two
options wrap a *statement*, not its subject, so this is not evidence between
them (§6.5).

**A-03 — the bytes, not the URL.**

<!-- q L205 "A single document can have many URLs" .. "will not be valid." -->
> A single document can have many URLs; the URL used to retrieve a document may differ from the URL in the for option of a label that accompanies the document, but the document retrieved must be the same document or the hash(s) contained in the resinfo extension will not be valid.

Ours, `SPEC-0002` §7.2:

<!-- qm spec/SPEC-0002-ksa-core.md L448-450 "A relying party MUST NOT" .. "matches the target" -->
> A relying party MUST NOT treat content fetched from a locator as the subject unless that content matches the target

**Confirms R-M-07 and R-M-11.** The difference is force: resinfo is optional
(C-01, X-06), R-M-07 is a MUST.

**A-04 — the unbound vocabulary, named by its authors.**

<!-- q L613 -->
> There is a security hole in the above proposal. The semantics of the assertions (ratings) in a PICS 1.1 label are defined by the rating service, and the only information about the rating service contained within the label itself is the service's URL. Since the human-readable description pointed to by that URL is what defines the rating semantics, it is possible under the current scheme for the semantics of the rating service to change after the label has been created without invalidating the label.

Ours, `SPEC-0003` §13.2:

<!-- qm spec/SPEC-0003-ksa-definitions.md L497-500 "Because statements cite definitions by hash" .. "after the fact." -->
> Because statements cite definitions by hash, an attacker cannot change what a value means after the fact.

and `ADR-0007`'s acceptance test, met by construction:

<!-- qm spec/ADR-0007-dec-007-predicate-rendering.md L86 "a changed language map is a new body" .. "their own bytes" -->
> a changed language map is a new body, so it gets a new DefinitionId. Statements cite the old id and their signatures cover only their own bytes

**Adopted as the diagnosis.** The hole has two routes *(inferred)*: the service
changes its description, and anyone on the path changes it in transit, since the
description is fetched by URL. A DefinitionId closes both, because a fetched
body is accepted only if it hashes to the id the statement names (`SPEC-0003`
§4.2, §4.4). The remedy DSig offers is rejected as a mechanism in X-05.

**A-05 — the signing time is advisory.**

<!-- q L381 "Notice that the" .. "canonicalized label." -->
> Notice that the "on" time is advisory only to applications verifying the digital signature; as this section is part of the entire sigblock extension it is not cryptographically protected by the signature itself. (The contents of the sigblock do not contribute to the hash of the label that is signed by the signature.) If a cryptographically-protected date is desired, the correct way to implement it is to include the date within another PICS label extension; that extension may then contribute to the hash of the canonicalized label.

Ours, `SPEC-0002` §7.3, inside the TBS:

<!-- qm spec/SPEC-0002-ksa-core.md L462 "`issued` is the speaker's statement" .. "when it signed." -->
> `issued` is the speaker's statement of when it signed.

The source's fix and ours are the same move. `SPEC-0001` §11 adds the limit the
source does not state: a signed time is still the signer's own claim.

<!-- qm spec/SPEC-0001-ksa-architecture.md L421-422 "`valid.issued` is the speaker's own claim" .. "such evidence." -->
> `valid.issued` is the speaker's own claim and is not such evidence.

**A-06 — parallel signatures carry no threshold.**

<!-- q L411 -->
> Multiple parallel signatures on the same PICS 1.1 label may be created simply by including several "Signature" fields within the sigblock extension. Cascaded signatures (signatures on signatures) are not supported within a single DSig signature label. To create a cascaded signature, a DSig signature label may be signed using another DSig signature label.

The sigblock is unsigned (X-02), so a signature can be added and *(inferred)*
removed without disturbing the others: a count of signatures on a label is not
evidence that any number of parties agreed. Ours, mofn report R-0006 §5.1,
reasoning from DSSE:

<!-- qm research/0006-mechanism/report.md L1227-1231 "under **every** DEC-002 option" .. "**unsafe to infer**." -->
> under **every** DEC-002 option, `k` and the member set must travel **inside the signed payload**. And because the envelope is declared equivalent to separate envelopes, an intermediary may legitimately split or merge them — so threshold meaning inferred from signature count is not merely absent but **unsafe to infer**.

**Confirms.** KSA's threshold is a `trust` statement's `threshold` over its
`trusts` (`SPEC-0002` §8.6), inside the truster's TBS. A DSig cascade, one
label signing another, is KSA's `review` or `approve` of a statement, except
that DSig gives the inner label no identity to target (S-04).

**A-07 — a canonicaliser invented in prose.** DSig describes its own step this
way, and cites nothing further:

<!-- q L519 "Then the equivalent standalone label is canonicalized" .. "for transmission)." -->
> Then the equivalent standalone label is canonicalized (similar to canonicalizing a PICS label for transmission).

PICS 1.1 has two candidates, and DSig names neither. One is a compact
transmission form, single spaces, `l` and `r`, abbreviated option names
(`pics-1-1-labels` §6, L121), which is optional and orders nothing. The other
is the signature *special form* (`pics-1-1-labels` §13.1, L413-420), a different
algorithm from DSig's: §6.1 below compares the two row by row, and they differ
on seven of nine. Then the worked example departs from DSig's own text, twice.
The text:

<!-- q L534 "Symbols are case insensitive" .. "lowercases." -->
> Symbols are case insensitive and converted to lowercases.

<!-- q L535 "The header part is the" .. "serviceURL." -->
> The header part is the 'pics-1.1' symbol followed by the serviceURL.

and the example's canonical form, which keeps `PICS-1.1` in upper case and
reorders the resinfo hashes, MD5 first, where Step 2 put SHA1 first and the text
states no order for them:

<!-- q L569-575 -->
> ( PICS-1.1 "http://www.gcf.org/v2.5" l by "John Doe" extension ( optional "http://www.w3.org/TR/1998/REC-DSig-label/resinfo-1_0" ( "http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0" "cdc43463463=" "1997-02-05T08:15-0500" ) ( "http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0" "aba21241241=" ) ) for "http://www.w3.org/PICS/DSig/Overview" on "1994.11.05T08:15-0500" r ( color 1 density 0 suds 0.5 ) )

§8 check 1 rebuilt Step 2's label by the text alone: the output equals the
example only when both departures are applied, and with either one alone it
does not. Ours:

<!-- qm spec/ARCH-0001-authorization-attestation.md L455 "Canonicalization algorithm" .. "invented silently." -->
> Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently.

**Corroborates R-O-03, and shows what it guards against:** two canonicalisations
of one syntax, nineteen months apart, the later not citing the earlier and
disagreeing with itself.

**A-08 — partial coverage, disowned.**

<!-- q L399 -->
> Note: The "include" and "exclude" SigData types exist in this specification strictly to overcome limitations in PICS 1.1 protocols. W3C's new metadata infrastructure, Resource Description Framework (RDF) should not have these limitations and it is the intent of the DSig working group that "include" and "exclude" not be present in the DSig 2.0 specification, which will build on RDF.

R-O-05 and `SPEC-0002` §7.1's closed statement map leave no field of a signed
statement outside its signature. The source's own authors reached that verdict
for DSig 2.0. X-03 is what the workaround costs.

**A-09 — change means a new identifier.**

<!-- q L198 -->
> Any incompatible change in an identifier should be accomplished by creating an entirely new identifier URL.

<!-- q L216 "Resinfo is not extensible" .. "separate extension will need to be created." -->
> Resinfo is not extensible: In DSig 1.0, if other disambiguating or differentiating information is needed, a separate extension will need to be created.

Ours: `SPEC-0002` §12 registries are append-only, and a changed definition is a
new DefinitionId linked by `supersedes` (`ARCH-0003` W-12). **Adopted as intent**;
DSig's version is a *should* about a URL whose owner can break it, ours holds by
construction.

### 2.2 Adapt

**D-01 — resinfo is a digest set.**

<!-- q L206 -->
> Structurally, resinfo contains one or more hashes of the information resource; each hash includes a hash algorithm identifier, the actual hash of the resource and (optionally) the date the hash was computed.

<!-- q L213 "A resinfo extension can contain multiple hashes" .. "in one label." -->
> A resinfo extension can contain multiple hashes of the information resource. Each must necessarily use a different hash algorithm; it is not valid to label multiple versions of a single document by including multiple, distinct hashes in one label.

The source states what the set **is** (one resource, distinct algorithms) and
never what a **verifier** does with it: check every hash, every hash it
supports, or any one. *(inferred)* Under *any one*, the label is as strong as
its weakest algorithm, and the two the source mandates are MD5 and SHA-1 (X-08).
Ours: a KSA digest target names one digest (`SPEC-0002` §7.2, type 2, with
`digest-alg` from §12.5: SHA-256, SHA-384, SHA-512). R-M-11's `aliases` set,
which would bind several identifiers to one subject, has no KSA form yet
(`ARCH-0001` §5.5). mofn report R-0006 §2.3 already found that *"binds a content
digest"* is not one property across formats:

<!-- qm research/0006-mechanism/report.md L292-294 "must say which digest algorithms it accepts" .. "not in substance." -->
> must say which digest algorithms it accepts, or a `gitCommit` entry satisfies R-M-07 in form and not in substance.

**Adaptation (ours):** if an aliases or digest-set form is ever specified, it
states the verification rule — every digest whose algorithm the verifier
supports must match, and at least one must be supported — and the accepted
algorithms. On import, resinfo's MD5 and SHA-1 hashes are not R-M-07 digests
(§5). Open question 3.

**D-02 — unsigned, augmentable certificates.**

<!-- q L296 "None of the information contained within the Attribution Information section" .. "an expired certificate may be replaced)." -->
> None of the information contained within the Attribution Information section is signed by the label's signature because certificates themselves are expected to be self-verifying. (More precisely, none of the information within the entire sigblock extension, including the Attribution Information section, contributes to the hash of the label that is signed as part of the signature option.) Thus, applications may augment the contents of the Attribution Information section without invalidating the signature on the label (e.g. newly-discovered certificates may be included in the Attribution Information section as they are found, or an expired certificate may be replaced).

KSA has the same pattern once, deliberately: the envelope's `pub` is a hint,
checked against `says` (V3), and a key never enters the key store because a
statement merely carries or names it (`SPEC-0002` §10). **Adapted:** AttribInfo
is at most a hint to an importer, and never yields a principal or an anchor.

**D-03 — four ways to name the key.**

<!-- q L332 "There are four common ways" .. "identifying token:" -->
> There are four common ways to uniquely specify a particular key; each has its own identifying token:

<!-- q L360 -->
> Details on how the hash for a key is generated is a property of individual signature suites.

Ours, `ADR-0005`, which rejects a per-suite digest (its alternatives table) and
fixes one `kid` per key whatever the suite:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L52-53 "Suites that **share** a key algorithm" .. "whichever suite it signs under." -->
> Suites that **share** a key algorithm share `kid`s: the key is the principal (R-M-02), whichever suite it signs under.

**Adapted for import:** `ByKey` gives a key; `ByHash`'s digest is suite-defined,
so it names a key only under that suite, which is the alternative `ADR-0005`
rejected; `ByName` and `ByCert` are lookups in someone else's namespace (R-M-03
makes a name mean something only relative to its issuer). None of the four is
signed (X-02), and none can be a KSA `kid`, because no DSig suite is a KSA suite
(X-08).

**D-04 — the analogy, refined.** DSig separates three roles PICS 1.1 kept
together:

<!-- q L79-80 -->
> The labeler and signer may be, but do not have to be different entities in a DSig label. DSig 1.0 signature labels provide fields for storing information about both the label creator and the signer(s). The PICS rating system referenced in the signature label is an assertion system in DSig. The statement in the label (made via the PICS ratings) is an assertion that the labeler is making about the referenced content.

Ours, `ARCH-0001` §4.2:

<!-- qm spec/ARCH-0001-authorization-attestation.md L384 "This is the PICS analogue" .. "is the definition (DEC-007)." -->
> This is the PICS analogue: issuer ≈ rating service; subjects ≈ labeled objects; predicate ≈ rating tuple; validity ≈ label lifetime; content binding is the artifact digest. The rating system, which v0.1 left out, is the definition (DEC-007).

**Adaptation (ours):** under DSig the issuer is the **signer**, any key, and the
rating service is the **definer** of the vocabulary. That is KSA's split exactly:
any key may attest under any definition, and the definition has its own
definer. `ARCH-0001`'s *"issuer ≈ rating service"* describes PICS 1.1, where the
service signs its own labels (`pics-1-1-labels` §13, L402-404), and is one step
short of DSig. Not edited here; open question 11.

### 2.3 Reject

**X-01 — the verifier rebuilds what was signed.** Signing, as the source lays it
out:

<!-- q L519 "First we create an equivalent standalone label" .. "as a label extension." -->
> First we create an equivalent standalone label for the label to be signed. Then the equivalent standalone label is canonicalized (similar to canonicalizing a PICS label for transmission). Finally, a digital signature is generated, inserted into a sigblock extension, and that extension is placed in the label as a label extension.

and the verifier's share, never written as a procedure (S-05) but stated twice:

<!-- q L530 "(If the signature is being created" .. "trying to verify the signature.)" -->
> (If the signature is being created the application knows which fields it wants to include in or exclude from the equivalent standalone label. The "include" and "exclude" options convey this information to applications trying to verify the signature.)

<!-- q L538 -->
> When the client computes the equivalent standalone label format described above, it will use all options available to it: both service and label options. This implies a constraint on the server when it decides what options to include in the transmitted set. The transmitted set must include all options necessary as either service or label options to create the same equivalent standalone label as was signed.

Ours, `ADR-0003`'s rejected alternative, and the requirement it rests on:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L62-63 "**Sign a re-encoded statement.**" .. "(R-O-05)." -->
> **Sign a re-encoded statement.** It makes the verifier canonicalise during verification and run its decoder on unauthenticated input (R-O-05).

<!-- qm spec/ARCH-0001-authorization-attestation.md L457 "The signed payload SHALL" .. "verified canonical bytes." -->
> The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator. A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification. Any human-facing form SHALL be regenerated from verified canonical bytes.

**Rejected natively, as `ADR-0003` already did.** DSig is that alternative,
built: the verifier parses an untrusted label list, resolves inheritance, removes
an unsigned extension, applies an unsigned coverage list, sorts, folds case and
re-spaces, all before it can check a signature. §4 scores it clause by clause.

**X-02 — the sigblock signs nothing about itself.**

<!-- q L381 "(The contents of the sigblock" .. "signed by the signature.)" -->
> (The contents of the sigblock do not contribute to the hash of the label that is signed by the signature.)

<!-- q L407 "The signature algorithm may require" .. "hash and signature." -->
> The signature algorithm may require or accept other inputs in addition to the contents of the equivalent standalone label. For example, the signature suite may pad the data in a particular way, or mix into the hash of the data information concerning the algorithms used to generate the hash and signature.

So the suite URL that says which algorithm made the signature is authenticated
only if that suite chose to mix it into the hash. Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L325 -->
> A statement's suite is inside its TBS and is therefore covered by its signature.

**Rejected:** a statement's suite, speaker and time are inside its TBS; the
envelope's copies of `suite` and `says` are hints checked against it at V6
(`SPEC-0002` §5). DSig has hints and no signed copy to check them against.

**X-03 — coverage declared where nothing is signed.** The mechanism:

<!-- q L390 "After the equivalent standalone label has been generated" .. "are removed from the canonicalized label." -->
> After the equivalent standalone label has been generated following the default canonicalization rules, individual label options may be dropped if an "include" or "exclude" option is present. If an "include" option is present, any field not listed in the field-list is removed from the canonicalized label. If an "exclude" option is present, all fields listed in the field-list are removed from the canonicalized label.

Because the list sits in the sigblock, *(inferred)* nobody can tell a coverage
list the signer wrote from one added later. §3.2 builds the consequence. Ours,
P5.2 on an unsigned region that carries meaning:

<!-- qm spec/ARCH-0002-key-relative-naming.md L514-515 "A flat" .. "carry meaning in." -->
> A flat *"P5 stops at the payload"* hands an attacker the envelope exterior to carry meaning in.

**Rejected.** P5.2 speaks of an envelope's exterior; DSig puts an exterior inside
the payload's own syntax. Open question 5.

**X-04 — a registry rooted in DNS.**

<!-- q L191 -->
> To ensure the uniqueness of identifiers, the identifier must be a valid URL. This in effect creates a distributed registry of unique names which can be created and shared by any community of interest.

<!-- q L192 "Since the identifier is a URL" .. "We recommend the returned document:" -->
> Since the identifier is a URL, it must, when resolved, yield a a document. We recommend the returned document:

<!-- q L197 -->
> We require that such identifier description documents always be provided.

Ours, P1:

<!-- qm spec/ARCH-0002-key-relative-naming.md L74-80 "SDSI observed" .. "it rejected above." -->
> SDSI observed that a name means something only relative to the key that issued it, and that a global namespace requires a global authority nobody should have to trust. That critique was never applied one layer down. Tag numbers, header labels, claim keys and predicate-type URIs are all global identifiers handed out by a central party — so a model whose premise is that principals are keys inherits, at its extension points, exactly the global namespace it rejected above.

**Rejected natively.** A URL is unique because DNS allocates the name before it,
and it means whatever its owner serves at resolution time *(inferred)*: a
global namespace with a central root, and an identifier whose meaning is a
mutable document. P1's pair needs neither. `ADR-0001` permits such names at an
interchange boundary, mapped lossily:

<!-- qm spec/ADR-0001-key-relative-naming.md L55-56 "Registry identifiers" .. "per R-I-01." -->
> Registry identifiers **may** appear at interchange boundaries, and such mappings are documented as lossy per R-I-01.

One concrete cost, measured (§8 check 4): Appendix 3 prints the SHA1 and DSS
identifiers as `http://www.w3.org//TR/...`, with a doubled slash, where every
example and the HTML links behind them use a single one. The source never says
how identifiers compare, so whether the conformance list names the identifiers
its examples use depends on a rule it does not have.

**X-05 — the vocabulary signed by name.** The canonical form's header:

<!-- q L535 "A normalized DSig-1.0 label consists of three parts" .. "followed by the serviceURL." -->
> A normalized DSig-1.0 label consists of three parts in order: the PICS 1.1 header, the options, and the ratings. The header part is the 'pics-1.1' symbol followed by the serviceURL.

The service URL is signed; what it serves is not (A-04). The source's remedy:

<!-- q L614 -->
> If this is a concern, a simple policy in the trust engine that evaluates signatures could be established to require a separate signature label on the service description file.

Ours, `ADR-0007`, rejecting URI-named vocabularies:

<!-- qm spec/ADR-0007-dec-007-predicate-rendering.md L98-101 "**Option 4, SKOS / JSON-LD / SHACL.**" .. "the namespace governance P1 rejects." -->
> **Option 4, SKOS / JSON-LD / SHACL.** Their identifiers are URIs (global, and contrary to `ARCH-0002` P1). JSON-LD's canonicalisation would sit beside KSA-CBOR (`ADR-0004`) instead of under it. Reusing them would import exactly the namespace governance P1 rejects.

and the sponsor's direction for definitions (P4, draft):

<!-- qm spec/ARCH-0002-key-relative-naming.md L262-263 "in the manner of PICS" .. "not a URL reference alone" -->
> in the manner of PICS, but not a URL reference alone

**Rejected as a mechanism.** Appendix 1's policy is half of DEC-007 option 2: it
gets the description signed, by whoever chooses to sign it, and leaves the label
citing a URL. Which description the labeler meant is still not recorded in
anything signed *(inferred)*. KSA's `type-ref` carries the DefinitionId inside
the TBS (`SPEC-0002` §7.4) and the definition is published by its definer's
`define` (§8.9). Open question 2.

**X-06 — the security-bearing extensions are optional.**

<!-- q L214 -->
> The resinfo extension is an "optional" extension. Optional implies that even if the processing software does not understand the extension, it should still process the label.

<!-- q L282 "The sigblock extension is an" .. "cannot understand the signature information." -->
> The sigblock extension is an "optional" extension. Optional implies that even if the processing software does not understand the extension, it should still process the label. We do not require that the extension be understood (mandatory) because the information contained within the label may be useful to applications that cannot understand the signature information.

The flag itself is P5-compatible: every PICS 1.1 extension declares itself
`optional` or `mandatory`, as DSig's own §6.2 restates (L167-169), so skipping is
explicit. Ours, P5, and
`ARCH-0001` §3.4's reading of OpenPGP's critical bit, which applies here word
for word:

<!-- qm spec/ARCH-0002-key-relative-naming.md L394-396 "Beyond the three:" .. "never the other way round." -->
> Beyond the three: **an unknown field in a signed payload is an error, not something to skip.** The default is must-understand; skippability is opt-in and explicit, never the other way round.

<!-- qm spec/ARCH-0001-authorization-attestation.md L308 "Our profile is" .. "not a field that old verifiers ignore." -->
> Our profile is **stricter**: every unknown field is rejected, so nothing is "non-critical". OpenPGP pays for its split: a verifier that ignores a non-critical field may not see a meaning the issuer intended. Under our profile a new field is a new definition (`ARCH-0003` W-12), not a field that old verifiers ignore.

**Rejected for us.** A client that skips resinfo reads a hash-bound label as a
URL- or context-bound one *(inferred)*: the meaning the issuer intended is
exactly what it drops. Our importer rejects a label carrying an extension it
does not understand, optional or not.

**X-07 — unverified labels in use.** DSig's stated design goal:

<!-- q L57 "PICS compliant applications can syntactically parse" .. "semantic content of a DSig signature." -->
> PICS compliant applications can syntactically parse DSig 1.0 signature labels; only cryptographic functions need to be added to PICS-aware applications in order to make use of the semantic content of a DSig signature.

and the consequence it accepts:

<!-- q L282 "Whether information contained within an unsigned" .. "trust management question." -->
> Whether information contained within an unsigned or unverified label should be used is a trust management question.

Ours, `SPEC-0002` §5:

<!-- qm spec/SPEC-0002-ksa-core.md L288 -->
> The envelope exists so that a verifier can **verify before it decodes**.

**Rejected.** The source permits a consumer to use an unverified label; it does
not require it, so our importer can decline without leaving the source.

**X-08 — mandatory algorithms with no exit.**

<!-- q L624-630 -->
> In order to conform with this Recommendation, an implementation must support: resinfo 1.0 hash algorithms: MD5 hashing (http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0), SHA1 hashing (http://www.w3.org//TR/1998/REC-DSig-label/SHA1-1_0) sigblock 1.0 signature suites: MD5 hashing with RSA crypto (http://www.w3.org/TR/1998/REC-DSig-label/RSA-MD5-1_0), SHA1 hashing with DSA crypto (http://www.w3.org//TR/1998/REC-DSig-label/DSS-1_0) (known as DSS).

[outside this source] MD5 and SHA-1 are no longer collision-resistant, and the
source has no deprecation mechanism: an implementation *must* support all four
(§7.3.3 L324). Ours: `SPEC-0002` §6.2 registers no RSA or DSA suite, and a suite
not registered or not supported is **unverifiable** (§6.1, V2). So a DSig
signature cannot be verified by a KSA verifier at all; §5 takes the consequence.
`SPEC-0001` §11 is the long-term lesson: a statement that must outlive its
algorithm needs independent evidence that it existed before the algorithm fell.

**X-09 — the suite defines part of verification.**

<!-- q L324 "Signature suites have complete control" .. "given in the signature suite." -->
> Signature suites have complete control over the contents of the SigData immediately following the signature suite URL. The format of this data must satisfy the SigData portion of the BNF; beyond that requirement, the format of the data is governed by the definition given in the signature suite.

With X-02 (a suite may mix more into the hash) and §7.3.4.7 (partial coverage
only where the suite permits it, L385), a document at the suite's URL decides
what bytes are signed and whether coverage may be partial. Ours, DEC-008's
proposed answer (open):

<!-- qm spec/ARCH-0002-key-relative-naming.md L576-580 "**Key-local is wrong for the core.**" .. "always-valid.*" -->
> **Key-local is wrong for the core.** Signature verification, canonicalization, the reduction algorithm, and **the definition of what "valid" means** must stay fixed. The reason is short: *if a key may define how its own statements are validated, it may define them as always-valid.*

**Rejected:** KSA suites are entries in `SPEC-0002`'s own append-only registry
that fix the signature input exactly (`SPEC-0002` §6.1), and are immutable once
the specification leaves `0.x`. DSig is evidence for DEC-008's proposed answer.
Open question 6.

### 2.4 Constrains

**C-01 — a generic label binds no digest.**

<!-- q L215 -->
> The resinfo extension is not valid in a generic PICS 1.1 label. It is only valid within a specific (non-generic) PICS 1.1 label.

<!-- q L153 "If the generic option is used with a true value" .. "specific information resource to hash." -->
> If the generic option is used with a true value, the DSig 1.0 resinfo extension can not be used because there will not be a specific information resource to hash.

A generic label names a URL prefix. R-M-07 needs a digest; `SPEC-0002` withdrew
the locator target, and its §13.10 explains why a statement about a locator is
about whatever is there when someone looks:

<!-- qm spec/SPEC-0002-ksa-core.md L907-909 "A statement about a locator" .. "different days." -->
> A statement about a locator would be about whatever the locator resolves to when someone looks, so one signature could vouch for different content on different days.

**Constrains import:** no generic DSig label maps to an R-M-07 attestation.

**C-02 — the subject by context.**

<!-- q L204 "This resource may be identified by the for option" .. "based on a request, etc.)." -->
> This resource may be identified by the for option or may be implied by the context of the label (in the resource, delivered in the HTTP header with the resource, returned by a label bureau based on a request, etc.).

The context is not signed. A specific label with neither `for` nor resinfo binds
its signature to no subject at all *(inferred)*; whoever delivers it chooses one.
**Constrains import:** such a label has no target.

**C-03 — two times, neither the signing time.** The label's `on`:

<!-- q L155 -->
> The date on which this label was created. This may be different than the date the label was signed (which may be included within the DSig 1.0 sigblock extension).

The sigblock's `on` is the signing time, and it is unsigned (A-05).
**Constrains import:** `SPEC-0002` §7.3's `issued` is the speaker's statement of
when it signed. Filling it from the label's `on` asserts a coincidence of times
the source denies; filling it from the sigblock asserts something nobody
signed. Open question 9.

**C-04 — rebuilding is the server's burden.** L538 (quoted under X-01) makes
the transmitting server carry every option the verifier needs to rebuild the
signed form. Ours allows one narrow case of the same idea:

<!-- qm spec/SPEC-0002-ksa-core.md L890-892 "A transport that abbreviates identifiers" .. "simply fails V4." -->
> A transport that abbreviates identifiers (§4.5) MUST NOT be trusted to reconstruct them; the reconstructed TBS is verified in full, and an abbreviation that reconstructs to the wrong bytes simply fails V4.

**Constrains, and the comparison favours `SPEC-0002`:** §13.7 lets a transport
shorten identifiers and makes the receiver rebuild the exact TBS bytes, which
are then verified in full. DSig's rebuild is a canonicalisation of a parsed
structure; KSA's is a substitution into bytes whose result is checked.

**C-05 — sets with no stated order.** The text orders options, extensions by URL,
and transmit-names:

<!-- q L536 "The options are sorted alphabetically" .. "URL." -->
> The options are sorted alphabetically (i.e. lexicographically ordered by the unquoted US ASCII characters) by their shortest names (i.e. use full instead of complete-label, exp instead of until). Extension options are sorted first by "extension" and then by the "extension" URL.

It orders nothing inside an extension, and nothing among repeated `comment`
options; the example sorts resinfo's hashes anyway (A-07). That is condition (5),
the canonical order of a set, decided by an example and not by the text. Ours, still owed at `d7f7f89`:

<!-- qm spec/ADR-0004-dec-002-encoding.md L105-108 "**Condition (5), the order of set-valued arrays.**" .. "Owed to `SPEC-0002`." -->
> **Condition (5), the order of set-valued arrays.** `SPEC-0003` sorts range values; `SPEC-0002`'s `trusts`, `allow-keys` and `exclude-keys` are arrays whose order is signed and unstated, so two producers can emit one set as two byte strings. Owed to `SPEC-0002`.

**Constrains;** §6.3 item 1 takes it to ADR-0004.

**C-06 — dates.** §7.2.1 widens PICS 1.1's date (L227-253): `.` or `-`
separators, optional seconds and fractions, an offset from UTC. `SPEC-0002`
§4.4 has one encoding per instant, whole seconds, and rejects any other
spelling of its human form. **Constrains import:** convert to UTC, drop
fractions, and say so in the mapping.

### 2.5 Conflicts

**K-01 — verification is canonicalisation.** X-01 is the reject of DSig's
design for our own statements. K-01 is the conflict for an **import verified by
us**: there is no way to check a DSig signature that does not run the
canonicaliser over received input, so our verifier would break R-O-05's clauses
3 and 4 and P5.1:

<!-- qm spec/ARCH-0002-key-relative-naming.md L412-415 "Where a profile declares a canonical encoding" .. "or repair it." -->
> Where a profile declares a canonical encoding, a decoder SHALL **reject** input that is not in that profile's canonical form. It SHALL NOT normalise it, re-encode it, or repair it.

**Conflicts.** An import that wants a verified DSig label has to verify it
outside the KSA verifier, as an external statement (`SPEC-0001` §5.3) whose
evidence status the import profile states (§5).

**K-02 — case folded where PICS 1.1 keeps it.** DSig:

<!-- q L534 "PICS 1.1 tokens include" .. "considered symbols." -->
> PICS 1.1 tokens include left and right parenthesis, symbols, quoted-strings, and numbers. Symbols are case insensitive and converted to lowercases. Tokens in multi-value syntax are considered symbols.

A transmit-name (`suds`, `color/hue`) is not a parenthesis, a quoted string or a
number, so it is a symbol and is lowercased. PICS 1.1 makes transmit-names
case-sensitive (`pics-1-1-labels` §7 L141, §14 L471, which also allows URLs as
transmit-names). So two labels that PICS 1.1 says rate different categories,
`Suds 1` and `suds 1`, have one canonical form, and a signature over one
verifies over the other (§8 check 2). **Conflicts** with condition (1), which
R-O-05 assumes: the canonical form is not injective over the labels it signs.
The precondition is a rating system with transmit-names that differ only in
case; PICS 1.1 permits them, and whether any was ever published is not known.
§9 SD-6 records it as a source defect as well.

### 2.6 Silent

**S-01 — trust is somebody else's.**

<!-- q L274 -->
> The sigblock extension can also contain certificates that can be used by a trust management system (TMS) to decide if the signature is trustworthy.

<!-- q L294 "Attribution Information is not required" .. "in processing the label." -->
> Attribution Information is not required (i.e. this section of the extension may be empty), in which case trust management systems must depend on other information sources when interpreting the label. Furthermore, the information provided herein may or may not be used by the trust management system in processing the label.

KSA specifies what DSig hands to a TMS, `ARCH-0001` §4.3's statement
acceptance:

<!-- qm spec/ARCH-0001-authorization-attestation.md L400 "signature valid" .. "is conformed to" -->
> signature valid ∧ issuer authorized for that `PredicateType` ∧ subject digest matches the artifact under consideration ∧ every named template is conformed to

with anchors per context (`ADR-0003` D3, D4).

**S-02 — keys.** DSig defines no key distribution, revocation or rotation; it
carries certificates and leaves their validation to the PKI behind them. KSA:
`key-publish`, `revoke` and `rotate` (`SPEC-0002` §8.2, §8.7, §8.8); R-O-02
prefers short validity.

**S-03 — what resinfo hashes.**

<!-- q L620 "It is possible to use DSig labels in document other than HTML." .. "must be created." -->
> It is possible to use DSig labels in document other than HTML. To do this, a specification for how the label is embedded in that document type and how the document is normalized for hashing into the label must be created.

The sentence presumes the HTML case is settled. DSig never says how; PICS 1.1's
MIC computes its digest after removing every embedded label
(`pics-1-1-labels` §13, L401), and that is the only rule in either source that
makes a label able to sit inside what it hashes *(inferred)*. Nor does DSig say
whether the hash is over a transfer-encoded or a decoded entity. KSA's digest
target is over the bytes a relying party holds, and KSA never embeds a statement
in its subject.

**S-04 — no label identity.** A cascade signs one label with another (L411,
quoted under A-06), but DSig never says which bytes of the inner label the outer
label's resinfo would hash: the label list as
transmitted, the standalone label, or its canonical form *(inferred)*. KSA names
a statement by SHA-256 of its TBS (`SPEC-0002` §3, property 3), which is what a
`review` or `approve` targets.

**S-05 — no verification procedure.** The seven lines of the source that mention
verifying (L282, L294, L296, L328, L381, L390, L530; §8 check 7) describe
consequences for a verifier, never steps. `SPEC-0002` §9.2 is ordered and
complete; DSig's verifier is implied by its signer.

**S-06 — no domain separation.** A DSig canonical form begins `( pics-1.1` and
the service URL; nothing in it names the signing purpose, and the suite may add
algorithm information or not (X-02). Ours: a DS label in every signature input
(`SPEC-0002` §6.4) and a recommended key per protocol (`SPEC-0001` §5.3).
*(inferred)* Whether a DSig signature could be presented as a signature in
another protocol that signs ASCII text with the same key is a question the
source does not ask.

**S-07 — DEC-005.** §6.5.

---

## 3. What a DSig signature authenticates, and what it does not

### 3.1 By part of the label

| part of a received DSig label | covered by a `Signature`? | where |
|---|---|---|
| `pics-1.1` and the service URL | yes: the canonical form's header | §8.1.2 L535 |
| every label option, including service options it inherits and extensions such as resinfo | yes, unless removed by `include` or `exclude` | §8.1.1 L523; §8.1.2 L536 |
| the ratings | yes, unless removed by `include` or `exclude`, and with transmit-name case folded (K-02) | §8.1.2 L537 |
| `MIC-md5` and `signature-RSA-MD5`, if present | no: removed before signing | §6.2 L145, L157 |
| everything in the sigblock: AttribInfo, suite URL, key identification, `on`, `include`, `exclude`, `SigCrypto` | no | §7.3.2 L296; §7.3.4.6 L381 |
| fields named by `exclude`, or not named by `include` | no, though they stay in the received label | §7.3.4.7 L390 |
| the resource | only through resinfo, if present, understood and checked | §7.2 L203, L214 |
| what the ratings mean | no: only the service URL is signed | §9 L613 |
| what the hash, suite and certificate-family identifiers mean | no: documents at their URLs | §7.1 L192-197 |
| other signatures in the sigblock | no: parallel signatures are independent | §7.4 L411 |
| where the label was found, or its position in a label list | no | §7.2 L204; §8.1.1 L523 |

So a verified DSig signature tells a relying party *(inferred, from §6.1 and the
rows above)*: **the holder of the key that verifies it asserted, at a time it
states only unsigned, that the covered fields of this label are valid statements
about the resource the label identifies — by hash if resinfo is present and
checked, otherwise by URL or by context — in a vocabulary named by URL whose
content at signing time is not recorded.** It does not tell it who that key
holder is, which algorithm was used unless the suite chose to say so inside the
hash, which fields the signer meant to cover, or that the uncovered fields are
not an attacker's.

### 3.2 An unsigned `exclude` widens a label signed whole

*(inferred, from L381, L390 and L296, and checked by script: §8 check 3.)* A
signer signs a specific label with no `include` or `exclude`, as an embedded
label may be, without `for` (PICS 1.1 lets an embedded label omit it;
`pics-1-1-labels` §10, L255). Anyone who handles the label afterwards adds
`for "http://victim.example/"` and `gen true` to the label, and adds
`("exclude" (("options" "for" "gen")))` to the existing `Signature` section. The
verifier rebuilds the canonical form, removes the two excluded options, and gets
the bytes the signer signed: the signature verifies. A consumer that reads the
label as received (L57) now holds a verified label rating a whole site.

The precondition is a suite that permits partial signatures, and the example
sigblock shows `RSA-MD5-1_0` used with `exclude` (§7.4.1, L423-428). Nothing in
the source tells a verifier to treat excluded fields as absent, or lets a signer
say *no exclusions* in signed form. Two limits on the result: a label that
carries resinfo cannot be made generic (C-01), and a field the signer did cover
cannot be removed, since that changes the canonical form. **The rule this
gives an importer, ours:** read every claim from the verified canonical form,
never from the received label — R-O-05's last clause, applied to a foreign
format — and, under P5.2, reject a label whose coverage list it did not expect.
Open question 10.

---

## 4. R-O-05, clause by clause

`ARCH-0001` §5.3, since v0.2.0 (quoted under X-01).

| R-O-05 clause | DSig | verdict |
|---|---|---|
| the signed payload is the canonical encoding verbatim | the canonical form is never transmitted: the label travels with its sigblock, in any equivalent form, under any inheritance (§8.1.1 L523, L530) | **conflicts** |
| carried with an authenticated type indicator | the form opens with `pics-1.1` and the service URL, which are signed; the suite and the coverage list are not (X-02); there is no domain separation (S-06) | **conflicts**: partly met |
| verify before decoding | the label list is parsed and inheritance resolved before any signature can be checked (L538) | **conflicts** |
| no canonicalising during verification | canonicalising is how the verifier obtains the signed bytes (L530, L534) | **conflicts** |
| any human-facing form regenerated from the verified bytes | an application reads the label it received (L57), uncovered fields included (§3.2) | **conflicts** |

**Five of five, by design and not by defect.** The source states the trade:
signed labels stay readable by every PICS parser, and only cryptographic
functions need adding (L57). That property is what R-O-05 gives up, and DSig
shows the price of keeping it: an unsigned coverage list (§3.2), an unsigned
algorithm (X-02), a case fold that merges what PICS 1.1 keeps apart (K-02), and a
canonicaliser whose example disagrees with its text (A-07). Ours, on why
rejection matters:

<!-- qm spec/ARCH-0002-key-relative-naming.md L440-443 "R-O-05 requires canonicalisation" .. "the separation is cosmetic." -->
> R-O-05 requires canonicalisation to run once, at authoring, on trusted input, and never as part of verification. **Rejection is what makes that separation real.** If a verifier may repair what it receives, the canonicaliser is back inside the verifier and the separation is cosmetic.

---

## 5. R-I-01: the PICS row's import profile, for a DSig label (draft)

<!-- qm spec/ARCH-0001-authorization-attestation.md L441 "Publish a mapping table" .. "dropped, or inferred." -->
> Publish a mapping table for each supported foreign format: what is preserved, dropped, or inferred.

<!-- qm spec/ARCH-0001-authorization-attestation.md L500 "PICS label |" .. "import profile only if needed" -->
> PICS label | I | — | ArtifactStatement | Historic; import profile only if needed

Every row is *(inferred)*: the source defines no import or export. Label-level
rows (service, options, ratings, dates, delivery) are the label format's and are
drafted in `pics-1-1-labels`'s design notes, §5. These are the rows DSig adds.
The route would be `SPEC-0001` §5.3's:

<!-- qm spec/SPEC-0001-ksa-architecture.md L229-232 "A wallet MAY import a signed object" .. "the same evaluation." -->
> A wallet MAY import a signed object from another protocol as an **external statement**, keeping its original bytes and mapping its speaker, subject and claims through an interchange profile (ARCH-0001 §6), so that it can be reasoned about by the same evaluation.

| DSig construct | on import | |
|---|---|---|
| a `Signature` under `RSA-MD5-1_0` or `DSS-1_0` | no KSA suite: unverifiable natively (`SPEC-0002` §6.1, V2). Verified, if at all, by an isolated component outside the KSA verifier, against broken algorithms (X-08) | **not carried natively** |
| the signer, by `ByKey` | a foreign RSA or DSA key; it has no `kid`, since `ADR-0005` defines one only under a registered suite | **respelled, outside KSA** |
| `ByHash`, `ByName`, `ByCert` | nothing; a lookup hint at most (D-03) | **dropped** |
| AttribInfo certificates | nothing; never a key-store entry or an anchor (D-02) | **dropped** |
| the sigblock's `on` | nothing: unsigned (A-05, C-03) | **dropped** |
| `include` or `exclude` | reject the label, or take claims only from the canonical form (§3.2) | **dropped**, by rule |
| resinfo's SHA-1 and MD5 hashes | not R-M-07 digests: neither algorithm is in `SPEC-0002` §12.5. An importer that fetches the resource and binds it by SHA-256 makes that binding its own statement | **dropped**; **inferred** if re-bound |
| a generic label | no target (C-01) | **dropped** |
| a specific label without resinfo | no target satisfying R-M-07 (C-02) | **dropped** |
| the service URL | no DefinitionId. A definition minted by the importer from a fetched description has the importer as its definer, and records the description as fetched on that day, not as the labeler saw it (A-04) | **inferred** |
| several parallel `Signature`s | one external statement per verified signer; never a threshold (A-06) | **respelled** |
| a cascade | nothing: no inner label identity (S-04) | **dropped** |

**Net.** Every load-bearing row is dropped or inferred. The row's *"import
profile only if needed"* is right, and a profile, if one is ever needed, imports **evidence
that a key once signed a label**, not a statement a KSA verifier can check
(open question 1). Nothing here argues for raising the row's priority.

---

## 6. MD-3, ADR-0004 and DEC-002

MD-3 reads:

<!-- qm project/meetings/2026-09-28.md L51-53 "CBOR data model" .. "one-way mapping." -->
> CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping.

`ADR-0004` accepted DEC-002 for option 5 on 2026-10-25, and:

<!-- qm spec/ADR-0004-dec-002-encoding.md L132 "MD-3's narrowing is closed by acceptance" .. "acceptance" -->
> MD-3's narrowing is closed by acceptance

Nothing here reopens it:

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

DSig is a signing format and not a CBOR, COSE or envelope document. The
header-by-header mapping `docs/extraction.md` asks of envelope documents
becomes a part-by-part account of what is signed (§3, §6.1). The section exists
because an extraction that can only confirm is not evidence.

### 6.1 What DSig signs, beside what PICS 1.1 signs

Both canonicalise one label syntax. They are different algorithms, agreeing
only on the order of ratings and on who rebuilds the form; DSig cites neither
PICS 1.1's nor any other (A-07). PICS 1.1 locators are in `pics-1-1-labels`
(§13.1, Signature Details).

| | PICS 1.1 special form (`pics-1-1-labels` L413-420) | DSig canonical form (§8.1.2 L534-537) |
|---|---|---|
| header | none: no parenthesis, no version, no service URL | `( pics-1.1 <service URL> l` |
| which options | every transmitted option but `signature-rsa-md5`; one equal to its default is left out (L415) | every option of the standalone label, minus the sigblock, minus `MIC-md5` and `signature-RSA-MD5`, minus `include`/`exclude` effects; no default rule |
| option order | by shortest name | by shortest name; extensions then by URL |
| values | each value in its shortest spelling (L416) | the tokens as received, symbols lowercased |
| case | lower case only for case-insensitive strings, so transmit-names keep theirs | every symbol lowercased, transmit-names included (K-02) |
| spacing | name, space, value, space; then `r (`; no separator stated between rating pairs (L418) | one space between any two tokens, parentheses included |
| ratings | sorted by transmit-name; within a multi-value, single spaces | sorted by transmit-name |
| coverage | everything transmitted | everything not excluded; the exclusion unsigned |
| verified by | the client rebuilding the form (L405, L420) | the client rebuilding the form (L530, L538) |

### 6.2 Against the six conditions (mofn report R-0006 §3.2)

| condition | DSig | how |
|---|---|---|
| (1) injective | **not over PICS 1.1 labels** | the case fold merges transmit-names PICS 1.1 keeps apart (K-02); `exclude` makes it non-injective over received labels by design. Over the fields it keeps, the tokens are delimited and quoted strings keep their quotes *(inferred)* |
| (2) the decoder rejects non-canonical input | **no** | the received label is never required to be canonical; the canonicaliser normalises whatever arrives |
| (3) canonicalise once, at authoring, never in verification | **violated by construction** | X-01, K-01 |
| (4) authenticated type indicator | **partly** | the format and the vocabulary's name head the signed form; the suite and the coverage profile are unsigned, and nothing separates the signing purpose (X-02, S-06) |
| (5) canonical order for sets | **partly** | options, extensions and ratings ordered; resinfo's hashes, repeated `comment` options and multi-value items not, and the example orders one of them anyway (C-05) |
| (6) Unicode normalisation | **not applicable to Unicode** | PICS 1.1 labels are US-ASCII (`pics-1-1-labels` §7, L142). The case fold is a normalisation run by the verifier, the hazard (6) exists for, met in ASCII |

### 6.3 Where DSig cuts against option 5 and MD-3

1. **Condition (5), against the profile as it stands.** DSig is a deployed design
   whose text left a set's order open and whose example closed it, so two
   implementers reading the same specification sign different bytes (C-05, A-07).
   `ADR-0004` left condition (5) owed (quoted under C-05), and at `d7f7f89`
   `ARCH-0001` §7 still lists it owed:

<!-- qm spec/ARCH-0001-authorization-attestation.md L578-581 "**Still owed:**" .. "with condition (5)." -->
> **Still owed:** `trusts: [A, A]` with `threshold: 2` passes V8, since `SPEC-0002` has no distinctness rule and `SPEC-0004` §6.4 counts distinct kids. It fails closed; it goes to `SPEC-0002` with condition (5).

   Against the option-5 **profile**, not the encoding: mofn report R-0006 §3.2
   places Group B above any encoding.
2. **Re-serialisation by intermediaries: a driver `ADR-0004` never scored.** A
   DSig signature survives re-spacing, option-name abbreviation, reordering of
   options and ratings, and factoring of shared options into a service section,
   because its verifier canonicalises (§6.1). PICS label bureaus and servers do
   exactly those things to label lists (`pics-1-1-labels` §6, L121-133; §7,
   L143). A KSA signature survives none of them. **This names no DEC-002
   option**: under R-O-05 every option pays it, and `SPEC-0002` §13.7 keeps the
   one case that matters for size (C-04). It presses on R-O-05 and P5.1, both in
   force, and is recorded as a cost they carry, not as a reason to reopen.
3. **`ADR-0004` item 3 lists IANA's registries only.**

<!-- qm spec/ADR-0004-dec-002-encoding.md L46-50 "**No IANA registry is native.**" .. "lossily per R-I-01." -->
> **No IANA registry is native.** Named, because "no tags" was too narrow (`ARCH-0001` §7, inputs since v0.1.3): the native model depends on none of CBOR Tags, COSE Header Parameters, COSE Algorithms, CWT Claims, or CWT Confirmation Methods. Each may appear at an interchange boundary, mapped lossily per R-I-01.

   DSig names every algorithm, suite and certificate family by URL: a DNS-rooted
   namespace, which P1 excludes and item 3 does not name. **Underdetermined**, as
   `w3c-vc-data-integrity-1-0`'s design notes found for multiformats and W3C
   vocabularies. Open question 7.
4. **Legibility in text channels: weak, toward option 3, which is withdrawn.** A
   DSig label is US-ASCII that rides in an HTML `META` element or an RFC-822
   header as it is (Appendix 2, L618), and its signed form is legible text. A KSA
   envelope needs a transport encoding there, and its human form is regenerated
   by a tool (MD-3; `SPEC-0002` §11). `ADR-0004` scored *human debug* through
   `SPEC-0002` §11; DSig adds only the channel. Not a reason to reopen.

**What DSig's defects do not show.** They are not evidence for option 1 over
option 5. `ADR-0004` concedes that under option 5 canonicality is a rule an
implementation must state:

<!-- qm spec/ADR-0004-dec-002-encoding.md L74-77 "Option 1 wins governance" .. "parses every valid document" -->
> Option 1 wins governance and makes smallest-form a property of the grammar, so a conforming reader cannot omit the check. Under option 5 the same property is a rule an implementation must state; one that omits it still parses every valid document

DSig's failures (K-02, A-07, C-05) are semantic normalisations run at
verification — case folding, inheritance, ordering — and an in-grammar smallest
form, which is what option 1 buys, decides none of them *(inferred)*. They are
evidence for R-O-05 and P5.1 under every option.

### 6.4 Where it favours option 5 and `SPEC-0002`

- **No normalisation at verification.** `SPEC-0002` §4.1 keeps text byte-exact,
  with no case folding by producer or verifier, and P5.1 rejects rather than
  repairs; K-02 cannot happen.

<!-- qm spec/SPEC-0002-ksa-core.md L197 "valid UTF-8. Preserved byte-exact;" .. "by any producer or verifier" -->
> valid UTF-8. Preserved byte-exact; MUST NOT be normalised (no Unicode normalisation, no case folding, no whitespace trimming) by any producer or verifier

- **An authenticated suite and a DS label** (`SPEC-0002` §6.1, §6.4), where
  DSig's suite is unsigned and its purpose unseparated (X-02, S-06).
- **Closed maps.** No field of a signed KSA statement lies outside its signature
  (`SPEC-0002` §7.1); DSig's `exclude` creates such fields (§3.2).
- **The signed bytes travel** (`SPEC-0002` §5), where DSig's never do (§4).
- **MD-3's direction.** MD-3 makes the bytes primary and the YAML a view
  regenerated from them. DSig runs the same pair the other way: the legible
  label is transmitted and the canonical form derived by the verifier, the
  direction R-O-05 forbids.

### 6.5 DEC-005: an embedded signature, not an envelope

<!-- qm spec/ARCH-0001-authorization-attestation.md L634 -->
> Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema.

DSig keeps *a single payload schema* the other way round: the signature is an
optional extension inside the label, so an unsigned PICS label and a signed DSig
label share the PICS 1.1 grammar and a DSig-unaware client reads both (L57,
L175). That choice is what forces X-01. **Corroborates DEC-005's option set,
which contains envelopes only; silent between DSSE and COSE_Sign1.** Three
parallels, none a discriminator: DSig's parallel `Signature`s are DSSE's
`signatures` list, and like it carry no threshold (A-06); AttribInfo is an
unauthenticated certificate carrier like an unprotected header; DSig's
detachment (A-02) is a property of the attestation, which both envelopes wrap
alike.

### 6.6 Net, stated as evidence

Nothing here shows a defect in option 5 itself, which is what would supersede
`ADR-0004`. Three findings go to its reviewer: condition (5) is still owed and
DSig shows what leaving it to examples costs (6.3 item 1); item 3's registry
list does not name DNS-rooted identifiers (6.3 item 3); and intermediary
re-serialisation is a cost R-O-05 imposes under every option, never scored
(6.3 item 2). DSig's weight falls **outside DEC-002**: on R-O-05, whose every
clause it breaks (§4); on DEC-007, whose hole it names (A-04); on P5.2, which
does not reach an unsigned region inside a payload (X-03); and on R-I-01's PICS
row (§5).

---

## 7. mofn report R-0006 §2.2: the PICS cells this record answers

R-0006 left the PICS row of its mechanism table empty, with reasons:

<!-- qm research/0006-mechanism/report.md L231 "whether and how a label binds content" .. "binds content" -->
> whether and how a label binds content

and, in its *what is signed* cell:

<!-- qm research/0006-mechanism/report.md L231 "DSig 1.0 added signatures in 1998" .. "not in the library" -->
> DSig 1.0 added signatures in 1998 (R-001 §6.1); its construction is not in the library

and listed what would fill it:

<!-- qm research/0006-mechanism/unverified.md L41 "what DSig 1.0 signs" .. "and when" -->
> what DSig 1.0 signs, whether it canonicalises, and when

<!-- qm research/0006-mechanism/unverified.md L42 "how a DSig verifier proceeds" .. "proceeds" -->
> how a DSig verifier proceeds

From this source, for R-0006's columns (not edited here):

| R-0006 column | DSig 1.0 |
|---|---|
| what is hashed | the resource, by resinfo, under named algorithms, one hash each (§7.2 L206); optional, and not allowed in a generic label |
| canonicalised, and when | the label: at signing **and at verification**, by DSig's own canonicaliser (§8.1.2) |
| what is signed | the canonical form of the equivalent standalone label without its sigblock and without excluded fields, as input to the suite, which may add inputs (§7.3.5 L407) |
| what the envelope carries | no envelope. The sigblock inside the label: AttribInfo and one or more `Signature`s, all unsigned (§7.3.1, §7.3.2) |
| what the verifier does | never stated (S-05). Implied: rebuild, canonicalise, verify per suite (L530, L538) |
| where trust is placed | a trust management system (L282, L294) |
| what it leaves undefined | verification, key lifecycle, identifier comparison, label identity, resinfo's hashed bytes (S-01 to S-05; §9) |

And one correction to the cell R-0006 did write: DSig did not *add* signatures
to PICS. PICS 1.1 had its own (§10 below).

---

## 8. Arithmetic and blanket claims, checked

Scripts are in the lane's scratch directory (§12); each is specified here
closely enough to rebuild.

| # | claim | how checked | result |
|---|---|---|---|
| 1 | the Step 3 example departs from the §8.1.2 text in exactly two places | `dsig_canon.py`: the text's rules (L534-537) applied to Step 2's label (L554-564), compared token for token with Step 3 (L569-575) | equal only with both departures applied (`PICS-1.1` in upper case; resinfo's hashes sorted). With either alone, unequal. The example's spacing is one space between every two tokens, as the text says |
| 2 | case folding merges `Suds` and `suds` | `dsig_canon.py`: canonical forms of two one-rating labels | identical |
| 3 | an added `exclude` leaves the canonical form unchanged | `dsig_canon.py`: a label signed without `for` and `gen`, against the same label with both added and excluded | identical |
| 4 | two of Appendix 3's four identifiers print a doubled slash | `grep` of the `.txt` (L627, L630) and of the HTML: the printed text has `www.w3.org//TR`; the `HREF`s behind both are `/TR/1998/...`, one slash; L261, L429 and L560 use one slash | 2 of 4 |
| 5 | DSig followed PICS 1.1 by about a year and a half | 1996-10-31 to 1998-05-27, by `datetime` | 573 days, 1.57 years |
| 6 | 37 rows in §1 | counted by script from the table | 9, 4, 9, 6, 2, 7 |
| 7 | the source never states a verification procedure | `grep -i verif` over the `.txt` | 7 lines (L282, L294, L296, L328, L381, L390, L530); none is a step |

**Every *only*, *never*, *no* and *every* in this file's own prose was re-read**
against its row: each is scoped to the source as printed (the source never
says), not to the world. The intervals in A-07 and §10 are check 5's.

---

## 9. Source defects met while mapping

Recorded, not repaired. Each was re-read in the `.txt`, and the ones on
identifiers and examples were checked in the HTML.

- **SD-1. Appendix 3 prints two identifiers with a doubled slash.** SHA1 and DSS:

<!-- q L627 -->
> SHA1 hashing (http://www.w3.org//TR/1998/REC-DSig-label/SHA1-1_0)

<!-- q L630 -->
> SHA1 hashing with DSA crypto (http://www.w3.org//TR/1998/REC-DSig-label/DSS-1_0) (known as DSS).

  The examples use one slash (L261, L429, L560), as do the HTML links under these
  very lines. The source states no rule for comparing identifiers (X-04).
- **SD-2. The worked example contradicts the canonicalisation text** in two
  places (A-07; §8 check 1).
- **SD-3. One sentence has two readings.**

<!-- q L534 "Do not insert spaces for either" .. "of a PICS 1.1 label list." -->
> Do not insert spaces for either the leading left parenthesis or the the trailing right parenthesis of a PICS 1.1 label list.

  Read as forbidding a space outside the outermost parentheses, it adds nothing
  to the rule of one space between tokens, and the example follows it. Read as
  forbidding one just inside them, the example breaks it too.
- **SD-4. One or more signatures, or none.** §7.3.1 lists a sigblock's parts
  (L278-280):

<!-- q L278-280 -->
> A Signature Block consists of Attribution Information, and one or more Signatures.

  Its structure (L288-290) and its grammar write a starred signature, which
  admits none:

<!-- q L440 -->
> SigBlockURL AttributionInfo Signature* ')'

  The structure on L288-290 also opens one parenthesis after `extension` and
  closes two.

- **SD-5. Token case.** Quoted strings are case-sensitive (L183), and the defined
  tokens are `ByKey` (L333, L342) and `On` (L374, L376), while the examples write
  `byKey` (L424, L598) and the syntax and examples `on` (L379, L426, L431, L600).
- **SD-6. Transmit-name case** (K-02): L534 lowercases what PICS 1.1 L141 keeps.
- **SD-7. A standard PICS 1.1 label, and not a valid PICS 1.1 extension.**

<!-- q L175 "A DSig 1.0 Signature Label is a standard PICS 1.1 label." .. "standard PICS 1.1 label." -->
> A DSig 1.0 Signature Label is a standard PICS 1.1 label.

<!-- q L437 "Note: This extension is not a valid PICS 1.1 extension" .. "PICS 1.1 datum." -->
> Note: This extension is not a valid PICS 1.1 extension because Base64 encoding uses a '/' which cannot be represented as a PICS 1.1 datum.

  `record.yaml` already carries the `contradicts` edge for it.
- **SD-8. Which spelling a field-list uses.** An option-list is a list of option
  names (L398), but the source does not say whether `generic` or `gen`, or in
  which case, so an `exclude` naming one may or may not match the other.
- **SD-9. Name drift.** The grammar has `ratings-list` (L395); the text calls it
  `rating-list` (L537), and puts the include and exclude options in the suite
  (L536), where L390 makes them SigData fields of one signature.
- **SD-10. Text**, as printed:

<!-- q L183 "Multiple contiguous space characters are be treated" .. "are be treated" -->
> Multiple contiguous space characters are be treated

<!-- q L192 "yield a a document" .. "document" -->
> yield a a document

<!-- q L145 "This option has been superceded" .. "superceded" -->
> This option has been superceded

<!-- q L534 "the the trailing" .. "trailing" -->
> the the trailing

<!-- q L534 "No carriage-returns or linefeeds are present in a cannonicalized label." .. "label." -->
> No carriage-returns or linefeeds are present in a cannonicalized label.

<!-- q L390 "At most one" .. "field may appear;" -->
> At most one "include" or "exclude"; field may appear;

<!-- q L370 "the serial number a relevant certificate" .. "certificate" -->
> the serial number a relevant certificate

  and a closing quotation mark with no opening one at the end of L77 (quoted under
  A-01).

---

## 10. Our documents: claims this source tests

Four passages of m-of-n describe DSig. Three say DSig *added* signatures to
PICS, and one says DSig bound a vocabulary to its definer. This source says
neither. Recorded for their owners; m-of-n is not edited here.

<!-- qm research/0001-signatures-and-attestation/report.md L744-746 "PICS 1.1 was published as two W3C Recommendations" .. "May 1998 [@pics-dsig-1-0]." -->
> PICS 1.1 was published as two W3C Recommendations on 31 October 1996 [@pics-1-1-services; @pics-1-1-labels], with signatures added by DSig 1.0 in May 1998 [@pics-dsig-1-0].

<!-- qm research/0005-context/report.md L472-473 "DSig" .. "two years later." -->
> DSig [@pics-dsig-1-0] added signatures two years later.

<!-- qm research/0001-signatures-and-attestation/report.md L1733-1736 "PICS came closest" .. "two years later." -->
> PICS came closest by making the vocabulary a dereferenceable web resource, but its vocabulary was still owned by a *service*, not by a key, and it had no signature binding a vocabulary to its definer until DSig arrived two years later.

**What the sources say.** PICS 1.1 already defined `signature-RSA-MD5` and
`MIC-md5` (`pics-1-1-labels` §5, L79-81, L92-93; §13); DSig *replaces* them:

<!-- q L173-174 "DSig 1.0 replaces this option with the resinfo extension" .. "DSig replaces signature-RSA-MD5 with the sigblock extension." -->
> DSig 1.0 replaces this option with the resinfo extension, which permits a single label to include multiple hashes using multiple hash algorithms. PICS 1.1 also specified a signature option, signature-RSA-MD5, but its functionality was similarly limited. DSig replaces signature-RSA-MD5 with the sigblock extension.

And DSig does **not** bind a vocabulary to its definer: Appendix 1 names that as
the hole it leaves, and proposes a trust-engine policy (A-04, X-05). R-0006 §2.2's
cell (quoted in §7) repeats *"DSig 1.0 added signatures in 1998"*. The interval
is 573 days, about nineteen months (§8 check 5), which *two years later*
rounds up.

[outside this source] R-001 §6.2, R-0004 §6 and R-001's mini-report D say PICS
was retired *eleven weeks* after POWDER became a Recommendation. With the dates
the library records — POWDER 2009-09-01 (`powder-description-resources`
`record.yaml`) and PICS's retirement 2009-11-24 (this record's `record.yaml`) —
the interval is 84 days, twelve weeks.

---

## 11. Scope: the kinds this PR does not cover

The lead's scope gives `protocol` and `state-machine` as not applicable for
this record. **This reading agrees.** DSig defines a data format and no
exchange; Appendix 2 hands transport to PICS 1.1 (L618), and the bureau
constraint in §7.3.4.7 (L385) and the `complete-label` fetch (§6.2 L166; §8.3
L609) are PICS 1.1 protocol behaviour. DSig never states verification (S-05;
§8 check 7), so a state machine would be our invention. No design question in
this file needs a kind the PR does not cover. The one that comes close is
PICS 1.1's: how a delivered label's subject is fixed by the channel (C-02),
recorded in `pics-1-1-labels`'s design notes.

## 12. Method

- **Our documents** were read only from the `d7f7f89` snapshot. Every m-of-n id
  this file cites was checked to occur in the snapshot by a fixed-string search
  (`grep -rF`), by script over every id-shaped token in this file; every
  attribution was read, not only matched.
- **The source** is `.cache/pics-dsig-1-0.txt`, with the HTML `.cache/pics-dsig-1-0.bin`
  for the examples and identifiers, both sha256-checked against the brief and
  `record.yaml` in this pass. `bin/bcp14-count`: 0.
- **Quotations of the source** are `<!-- q -->` markers only, written by
  `bin/check-quotes --render --only` on this file and verified by
  `bin/check-quotes`.
- **Quotations of m-of-n** are `<!-- qm -->` markers, written and checked by
  `qm.py` against the snapshot, and re-checked by fixed-string containment in
  the whitespace-collapsed file.
- **Quotations of `pics-1-1-labels`**: none. It is cited by locator.
- **Unmarked source text.** Every 8-word window of this file's prose
  (blockquotes, marker lines and backtick spans removed) was searched in
  both sources' `.txt`: 9924 windows examined; every hit is a heading title
  quoted as a locator, as the locator rule requires.
- **Scripts** (lane scratch, not committed): `dsig_canon.py`, DSig's §8.1.2 from
  its text (a tokenizer for parentheses, quoted strings and bare tokens;
  inheritance with label options overriding service options; the sigblock
  dropped; options sorted by shortest name, extensions by URL; ratings sorted;
  symbols lowercased; one space between tokens), with switches for the example's
  two departures and for excluded fields.

## 13. What this file decides

Nothing. It records evidence and maps it. No requirement is added, amended or
withdrawn; no DEC-* is opened, ranked or accepted; `ADR-0004` and `ADR-0007` are
not reopened; the PICS row of `ARCH-0001` §6 keeps its priority. Each open
question below names the document or decision that would settle it.

## 14. Open questions

1. **Does R-I-01's PICS row ever need its profile?** If it does, §5 says it
   imports evidence that a key once signed a label, verified outside the KSA
   verifier under broken algorithms, with no R-M-07 target unless the importer
   re-binds the resource itself. Settle in the R-I-01 table for PICS, if one is
   ever written; until then the row's *"only if needed"* stands.
2. **Should DEC-007's record cite Appendix 1?** It is the primary-source
   statement of the hole option 2 closes by construction, and its remedy is
   option 2 without the citation by hash. `ADR-0007` is accepted and changes
   only by superseding; `SPEC-0003` §13.2's security consideration is where a
   citation could go. Settle in `SPEC-0003`.
3. **A digest set's verification rule.** If R-M-11's `aliases` gets a KSA form,
   does it require every supported digest to match and at least one to be
   supported, and which algorithms does it accept (D-01; mofn report R-0006
   §2.3)? DSig shows the set without the rule. Settle in `SPEC-0002`.
4. **Condition (5).** `SPEC-0002` still owes a canonical order for its
   set-valued arrays (`ADR-0004`; `ARCH-0001` §7). DSig is a precedent of the
   order decided by an example and contradicted by the text (C-05). Settle in
   `SPEC-0002`.
5. **Does P5.2 reach an unsigned region inside a foreign payload?** DSig's
   sigblock, like VC Data Integrity's proof, sits inside the payload's syntax and
   is unsigned; P5.2 speaks of an envelope's exterior. Does its import rule,
   reject what is unrecognised, extend to `include`, `exclude` and unknown
   SigData tokens? `w3c-vc-data-integrity-1-0`'s design notes ask the same of an
   embedded proof. Settle in P5.2's successor; P5.2 is accepted, so a change is
   a superseding ADR.
6. **DEC-008's boundary.** DSig let a suite, a document at a URL, decide part of
   the signature input and whether coverage may be partial (X-09). Is that the
   processing below the fixed core that DEC-008's proposed answer excludes? DSig
   is evidence for the answer. Settle under DEC-008.
7. **`ADR-0004` item 3's list.** Name DNS-rooted identifiers (URLs) beside the
   IANA registries, or leave each R-I-01 table to name its own? Shared with
   `w3c-vc-data-integrity-1-0`'s open question 10. Settle in `ADR-0004`'s
   successor or in the R-I-01 tables.
8. **Our documents' wording.** R-001 §6.1 and §11.4, R-0005 §5.4 and R-0006
   §2.2 say DSig added signatures, or bound a vocabulary to its definer (§10).
   Correct them when those reports are next revised? They are drafts; their
   owners decide.
9. **`issued` for an imported label.** Neither of DSig's two times is a signed
   signing time (C-03). If an import profile maps either to `valid.issued`, it
   asserts what the source does not sign. Settle in the R-I-01 table.
10. **Read claims from the verified form.** §3.2's rule — every claim of an
    imported object is read from what was verified, never from what was
    received — holds for any foreign format with unauthenticated coverage.
    R-O-05's last clause says it for our own forms. State it for imports too?
    Settle in R-I-01's general text or P5.2's successor.
11. **`ARCH-0001` §4.2's analogy.** *"issuer ≈ rating service"* fits PICS 1.1;
    under DSig the issuer is the signer and the rating service the definer
    (D-04). Refine it on the next revision of `ARCH-0001`? Not edited here.
12. **`bears_on`.** All eight ids stand. Warranted additions, within the field's
    vocabulary: R-M-11 (C-02), R-M-02 and R-O-01 (D-03), R-M-06 (A-06), R-O-02
    (S-02). P2, P5, P5.1 and P5.2, which this record presses hardest, are outside
    it. `record.yaml` is not edited here.
