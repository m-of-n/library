---
record: slsa-vsa-1-2
kind: design-notes
title: "slsa-vsa-1-2 — bearing on our design"
extracted: "2026-11-17"
reviewed_by: ""
---

# SLSA Verification Summary Attestation v1.2 — bearing on our design

The record is the VSA page of the SLSA Specification v1.2 (OpenSSF), dated
2025-11-24, `maturity: standard` (all from `record.yaml`). The source of record
is `spec/verification_summary.md` at `slsa-framework/slsa` commit `ae7fc76`
(`content.url`), sha256
`71adb7cc46a537c5a9b81fa8b14ae11cbc61ac91cc62c66197d1c1da8d92ccb0`. That value
is `content.sha256`, it is the constant `render-source.py` checks, and this pass
recomputed it from `.cache/slsa-vsa-1-2.bin`. Every line number here is a line
of `.cache/slsa-vsa-1-2.txt` (432 lines, sha256
`9cfab2e205860f67ea6052450f0445dcbd31dcf754d8cf9becf8d8ef3d1056e8`, equal to
`source_digest` in `requirements.yaml`). That file is the Markdown line for
line, with level-2 and level-3 headings renumbered §1 to §7 and column-0 list
items indented one space (`render-source.py` docstring). `bin/bcp14-count`
finds 21 keywords. `bin/fx1-skeleton` wrote the 15 sentences carrying them as
`slsa-vsa-1-2#R-0001` to `R-0015`; the requirements lane added R-0016 to R-0092
and pass 2 (verify) R-0093 and R-0094. Pass 1 of this file cited the skeleton's
fifteen only. Pass 2 re-pointed every citation to the entry that carries the
statement cited, a split child in place of its parent and a step's own entry in
place of R-0011's lead-in (§11 lists every pair), and gave each source question
of §10 its id in normative.md's canonical list of source defects.

The document defines one in-toto predicate type (L10-15), its fields (§3, §3.2),
a summary of the in-toto parsing rules (§3.1), one example (§4), a consumer
procedure of seven required steps and one optional step (§5), two worked
consumer cases (§5.1), the conventions for `SlsaResult` strings (§6) and a
change history (§7). **It does not define** the envelope, a signature
algorithm, how a consumer obtains or retires its roots of trust, the request a
VSA answers, what a policy is, any validity period, expiry or revocation, or
what a verifier must check about another verifier's VSA before counting it.

Its purpose, in its own words:

<!-- q L28-32 "They can use it to delegate" .. "regarding the artifact." -->
> They can use it to delegate complex policy decisions to some trusted party and then simply trust that party's decision regarding the artifact.

It reaches us in five ways.

1. **R-I-01 and T-053** (`project/BACKLOG-0001.md:190`). T-053 is the task of
   writing down what interchange loses, in the `ARCH-0001` §6 matrix, and it
   names this record as an input. The matrix (`spec/ARCH-0001-authorization-attestation.md:486-505`)
   has twelve rows and none for the VSA. §3 below is the mapping a row would
   summarise, and ends with a candidate row.
2. **R-I-03 and T-051** (`project/BACKLOG-0001.md:188`, `MAP-0002`: in-toto
   Statement to `ArtifactStatement`). A VSA is a predicate inside an in-toto
   Statement, and the schema shows the four Statement-level fields MAP-0002
   must map (L65-74). No `MAP-0002` file exists at the pin; only the backlog
   names it.
3. **R-O-06 and `SPEC-0004` §10.3–§10.4.** A VSA is a verifier's result made
   into a signed statement that third parties rely on: the nearest external
   analogue of our separated verifier output (issue #136's framing). It is a
   single combined outcome, which is what R-O-06 rules out for our own verifier
   (K-01).
4. **Trust: `ADR-0003` D3 and D4, `SPEC-0004` §4 and §6, `ARCH-0002` P2.** The
   VSA delegates a decision by consumer configuration. We delegate by anchors
   and trust statements scoped to attribute ranges (§4 below).
5. **Recomputation: `SPEC-0005` §6.3 and `ARCH-0003` W-21.** A VSA is a
   summary its consumer is meant to accept without the inputs. Our aggregates
   are accepted only when they recompute (X-01, §5 below).

What it is not: an envelope, a signature format, a policy language or a
delegation object. It carries no key, no algorithm and no validity window.

## Things to hold while reading

1. **Our documents are read from m-of-n at `7c3c731`**
   (`7c3c73165197e9c63152a65ba51345d65a268b89`, HEAD of
   `/Users/nfn/Projects/mofn` on 2026-11-17), by `git show 7c3c731:<path>`,
   never from the working tree. A citation of ours is `path:line` at that
   commit. **No word of m-of-n is quoted here**: every reference to it is a
   paraphrase beside its location (§11 gives the sweep that checks this).

   | name | path at 7c3c731 | standing at 7c3c731 |
   |---|---|---|
   | ARCH-0001 0.3.1 | `spec/ARCH-0001-authorization-attestation.md` | draft. §4.3 verifier inputs, §5 requirements, §6 matrix, §7 decisions |
   | ARCH-0002 0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | draft. Accepted: P1 by `ADR-0001`; P2, P3, P5, P5.1, P5.2 and P6 by `ADR-0002`. Draft: P1.1, P4, P7. Open: DEC-008, DEC-009 |
   | ARCH-0003 0.3.1 | `spec/ARCH-0003-wallet-object-model.md` | draft. W-01 … W-25 are draft requirements, W-07 as `ADR-0003` D3 rewrote it |
   | ADR-0001, ADR-0003 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0003-ksa-core-decisions.md` | accepted, reviewed |
   | ADR-0002, ADR-0004, ADR-0005, ADR-0007 | `spec/ADR-000{2,4,5,7}-*.md` | accepted, `reviewed: false`. `ADR-0004` accepts DEC-002 as option 5 |
   | SPEC-0001 0.1.0, SPEC-0002 0.10.1, SPEC-0003 0.2.0, SPEC-0004 0.6.2, SPEC-0005 0.1.0 | `spec/SPEC-000{1..5}-*.md` | draft; they govern where they and an ARCH document differ (`ADR-0003`). Versions are the front matter's; the title lines of SPEC-0002 and SPEC-0004 still read 0.9.0 and 0.6.0 |
   | UC-0001 | `spec/UC-0001-ksa-use-cases.md` | draft use cases; UC-1 is the release-attestation case |
   | MD-1, MD-3 | `project/meetings/2026-09-28.md:37-54` | dated decisions; `ADR-0004` closes MD-3's narrowing |
   | BACKLOG-0001 0.15.1, PLAN-0001 0.7.1 | `project/BACKLOG-0001.md`, `project/PLAN-0001-project-plan.md` | T-051 L188, T-053 L190, L-041 L267; I4's acceptance at PLAN-0001 L487 |
   | mofn reports R-001 and R-0006 | `research/0001-signatures-and-attestation/report.md`, `research/0006-mechanism/report.md` | draft research: evidence, deciding nothing |

   `docs/extraction.md` (L128-131) still says that no DEC-002 ADR exists. At
   `7c3c731` `ADR-0004` accepts it. This source is not a COSE, CBOR or envelope
   document, so §8 treats MD-3 briefly and says where its costs fall instead.
2. **Numbering.** A bare `R-NNNN` is `slsa-vsa-1-2#R-NNNN`. `R-M-nn`, `R-I-nn`,
   `R-O-nn` and `R-D-nn` are `ARCH-0001` §5. `P1` … `P7` are `ARCH-0002`. `W-nn`
   are `ARCH-0003` §10. `V1` … `V9` are the steps of `SPEC-0002` §9.2. `D1` …
   `D5` are always written `ADR-0003` D*n*. `MD-n` are meeting decisions. m-of-n's
   research reports are always written *mofn report R-001* and *mofn report
   R-0006*; neither is an id of this record, and `slsa-vsa-1-2#R-0006` is never
   meant by the second. Row
   ids are `A-nn` adopt, `D-nn` adapt, `X-nn` reject, `C-nn` constrains, `K-nn`
   conflicts, `S-nn` silent.
3. **Quotation of the source.** Only by `<!-- q -->` markers, whose blockquotes
   `bin/check-quotes --render` wrote. Elsewhere a passage is cited as
   `§n Lx-y` and paraphrased, never set in quotation marks. Field names and
   string constants in backticks (`verifiedLevels`, `PASSED`,
   `SLSA_BUILD_LEVEL_3`) are identifiers, not quotations. The field types the
   source names (`TypeURI`, `ResourceURI`, `Timestamp`, `ResourceDescriptor`,
   `DigestSet`) are defined in in-toto at `7aefca35` (L425-430). This lane does
   not read them, so their constraints are not mapped here.
4. **Labels.** *(inferred)* marks a consequence the source does not state.
   **Ours** marks a proposal of this library, not a decision of m-of-n. A
   number carries the method that produced it (§9, §11).

---

## 1. Rows by verdict

31 rows: **5 adopt, 5 adapt, 2 reject, 8 constrains, 5 conflicts, 6 silent**.
*Adopt (confirms)* means the source does what a decision of ours already does,
recorded as independent evidence, not as a new commitment. Nothing here changes
a decision (§12).

| id | verdict | in the VSA | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt (confirms) | Trust in a verifier is the consumer's own configuration; nothing inside a VSA makes a key trusted | §5 L283-285, L316-318; §3.2 L130 | R-0004, R-0067, R-0013, R-0083 | `ADR-0003` D3, D4; `SPEC-0004` §4.3–§4.4; W-14; R-I-02 | a VSA is not a trust statement and names no key, so V's key becomes an anchor only by an act of the relying party, through one of `SPEC-0004` §4.3's three sources; an import must not derive one from the envelope's signer |
| A-02 | adopt (confirms) | A valid VSA shows who vouched, not that the claim holds; a compromised verifier is outside its protection | §5 L313-318 | R-0013 | `SPEC-0004` §10.4 limit line; `SPEC-0001` §10; `LIMITATIONS.md` | the same limit. We print it under every verdict; the VSA states it once, in prose |
| A-03 | adopt (confirms) | The consumer checks the subject against the artifact it holds | §5 L287-288; §5.1 L328, L352 | R-0068 | `SPEC-0004` §10.1, §10.4 *integrity*; R-M-07 | we require the digest to be computed from the file the relying party holds; the VSA leaves how the artifact in question is hashed to the consumer *(inferred)* |
| A-04 | adopt (confirms) | What verification checks depends on the consumer's goals | §5 L274-279; §5.1 L322-367 | R-0066, R-0011, R-0012 | `ADR-0003` D4; `SPEC-0004` §3, §4.1 | we make the context an explicit input of a deterministic evaluation; the VSA leaves it informal |
| A-05 | adopt (confirms) | Each input attestation is named by digest, with a URI only as a fetch hint | §3.2 L184-185 | R-0048, R-0049 | `SPEC-0003` §4.4; `SPEC-0002` §3 property 3; R-M-11 | digest first, as we name definitions and statements. `policy` does the reverse (K-05) |
| D-01 | adapt | The claim is P2's form: V says these subjects met these levels under policy P | §2 L42-48; §1 L28-32 | R-0019 | `ARCH-0001` §4.2–§4.3; `SPEC-0002` §8.5, §8.10; `SPEC-0004` §4.2, §10.2; UC-1 | imports as an `attestation` (or an `approve`) by V's key about each subject digest, trusted through an anchor about the VSA definition's types. We add the scope the VSA never states; C-01 says whose key can speak |
| D-02 | adapt | Levels are per track, and each implies the levels below it | §3.2 L199-202; §6 L378-381, L392-394 | R-0054, R-0055, R-0079, R-0014, R-0076, R-0077 | `SPEC-0003` §6 *integer*; `SPEC-0002` §7.4, §8.6; P3 | an integer type per track gives *L2 and above* as the trust scope `[2, 3]`; the enum kind cannot. `UNEVALUATED`, `FAILED` and custom values are not levels and need a type of their own |
| D-03 | adapt | `inputAttestations`, when non-empty, lists every attestation used | §3.2 L180-185 | R-0046, R-0047 | `SPEC-0004` §10.3; `SPEC-0005` §6.3; R-O-06 | our `because` lists every statement relied on, by digest and with its path, in every answer; the VSA lets the list be absent and gives no path |
| D-04 | adapt | `resourceUri` scopes the verdict to the resource the artifact is accepted as | §3.2 L155-164; §5 L298-300; §5.1 L322-323 | R-0094, R-0006, R-0071, R-0091 | R-M-11; `SPEC-0002` §7.2, §13.10; `SPEC-0004` §10.1; `ARCH-0001` §2.3.2 AR-3 | a locator attribute on the digest target, matched by an attribute in the ask. It holds one statement at a time only (C-04); §6 below |
| D-05 | adapt | The consumer procedure: seven required steps and one optional step, in no stated order | §5 L281-311 | R-0011, R-0012, R-0067 to R-0074 | R-O-05; `SPEC-0002` §9.2; `SPEC-0004` §10.2 | the steps map onto V1–V9 and coverage (§7 below). We fix the order and add the checks the VSA omits |
| X-01 | reject | Import a VSA as an `aggregate` (kind 11): `policy` as its process, `inputAttestations` as its inputs, `verificationResult` as its result | §1 L28-38; §2 L42-48; §3.2 L167-185 | R-0041, R-0042, R-0045, R-0047 | `SPEC-0002` §8.11; `SPEC-0005` §1, §6.3; W-21, W-22; DEC-008 | we believe an aggregate only once it recomputes. A VSA exists so that its consumer need not recompute, and its confidentiality purpose withholds the inputs |
| X-02 | reject | Custom `SlsaResult` values: any spelling that does not start `SLSA_` | §6 L396-397 | R-0080, R-0081 | P1; `ADR-0001` (private-use alternative, rejected) | an unscoped private space beside a reserved prefix: two verifiers' custom values with one spelling cannot be told apart. Under P1 a value belongs to some definer's type |
| C-01 | constrains | A VSA is signed in its envelope, so importing one yields no native statement by V | §5 L283-285; §5.1 L325-326, L349-350 | R-0067, R-0086 | P2; `SPEC-0002` §5, §9.2 V3–V4, §13.2; W-11; R-I-02; `ARCH-0001` §6 DSSE, SLSA provenance and SCITT receipt rows | three homes, each with a cost: V signs a KSA statement under a KSA key; the importer attests, so the relying party trusts the importer; or the VSA rides whole as evidence *(inferred)* |
| C-02 | constrains | `subject` is an array of `{name, digest}`, each digest a map of algorithms | §3 L67-70; §4 L234-237; §5 L287-288 | R-0068, R-0092 | R-M-07, R-M-11; `SPEC-0002` §7.2, §12.5; mofn report R-0006 §2.3; `ARCH-0001` §6 in-toto row | one target per statement, three registered digest algorithms; `name` has no target home; a non-cryptographic digest type meets R-M-07 in form only, as mofn report R-0006 points out |
| C-03 | constrains | A consumer checks that `verifiedLevels` contains a value, reading levels as cumulative, or accepts L2 or L3 | §5 L305-306; §5.1 L345-346, L362; §3.2 L199-202 | R-0054, R-0073, R-0084 | `SPEC-0004` §10.1, §10.2 item 1 | an ask assigns exact values, so *Build L2 and above* is two asks, unless the importer writes out the implied levels, which R-0054 forbids a VSA's writer to do *(inferred: it binds the writer, not an importer)* |
| C-04 | constrains | The VSA's checks hold together inside one VSA; our coverage holds attribute by attribute | §5 L298-306 | R-0071, R-0072, R-0073 | `SPEC-0004` §10.2; `prototype/wallet/engine/reduce.py:204-230` | two VSAs about one digest, for different resources at different levels, would jointly cover an ask that neither supports alone *(inferred)*. A T-053 loss |
| C-05 | constrains | No validity window, expiry or revocation; `timeVerified` is optional, since 1.1 | §3.2 L149-152; §7 L412 | R-0036, R-0037 | `SPEC-0002` §7.3; R-O-02; `SPEC-0004` §7.1, §8, §10.3; `SPEC-0001` §11 | an import has at most `issued`; any `not-on-or-after` is the importer's own, an *inferred* cell under R-I-01 |
| C-06 | constrains | The example's `timeVerified` carries hundredths of a second, and precedes 2026 | §4 L249 | — | `SPEC-0002` §4.4 | KSA time is whole seconds from 2026-01-01. The example is T = −2,570,059,100 with 0.52 s dropped; truncating the negative count toward zero lands one second late (§9 check 3) |
| C-07 | constrains | `dependencyLevels` and `verifier.version` are maps whose keys are open; `dependencyLevels` has three states: unset or null, empty, counts | §3.2 L145-147, L205-219 | R-0059, R-0060, R-0034, R-0035 | `SPEC-0003` §5.2, §6 *record*; `SPEC-0002` §4.1 | the data model admits text keys inside a value, but no base kind is a map with open keys: record fields are fixed labels, and `SLSA_BUILD_LEVEL_3` is not a label. Null is forbidden, which costs nothing: unset and null mean the same here |
| C-08 | constrains | `policy` is required, and its URI is the mandatory part | §3.2 L167-172 | R-0040, R-0042, R-0043 | `SPEC-0004` §4.2, §9, §12; R-I-03; R-O-06 | an answer exported as a VSA must publish an identifier for a policy we keep local: the context's anchors, the ask and the definitions |
| K-01 | conflicts | One combined result, `PASSED` or `FAILED` | §3 L95; §3.2 L188-190; §5 L302-303 | R-0050, R-0051, R-0072 | R-O-06; `ARCH-0001` §4.3; `SPEC-0004` §10.4 | it cannot express a statement that is authentic but unentitled, nor a check with nothing to examine. Step 1 also folds a known key into a trusted one (§7 below) |
| K-02 | conflicts | Consumers ignore fields they do not recognise; producers may add fields named by URI | §3.1 L110, L115 | R-0001, R-0002 | P5, P5.2; `SPEC-0002` §7.1, §13.5; `ADR-0003` D1 | an importer held to P5 rejects a conforming VSA that carries an extension. P5.2 settles only the DSSE exterior and treats the payload interior as ours, which a foreign predicate is not (open question 6) |
| K-03 | conflicts | The verifier is a URI identity apart from the signing key, and consumers accept configured (signer, verifier) pairs | §3.2 L123-142; §5 L294-296 | R-0093, R-0004, R-0031, R-0070, R-0082 | P2; P1; `ADR-0003` D1; R-M-02; `SPEC-0002` V6 | under P2 the pair collapses to one key. `verifier.id` keeps no identity role on import and has to be minted on export |
| K-04 | conflicts | One type identifier for every minor version, resolving to the latest | L17-20; §3.1 L111-114 | R-0016, R-0017, R-0018, R-0025, R-0026, R-0027 | `ADR-0003` D1; `SPEC-0003` §4.2; W-12; DEC-007's acceptance test | VSAs of two minor versions share one type, where a change to one of our definitions is a new identity. 1.1 also made a field optional (open question 9) |
| K-05 | conflicts | The policy is named by URI as a MUST, its digest only as a SHOULD | §3.2 L171-172 | R-0042, R-0043 | `SPEC-0003` §4.4; W-04; `SPEC-0002` §7.2; R-M-11 | a VSA without `policy.digest` names its policy by a place; an import has no hash identity to give it |
| S-01 | silent | The envelope, the signature algorithm and the key format | §5 L283-285, L294-296; §5.1 L325-326 | R-0067, R-0070 | `SPEC-0002` §6.1, §6.5; `SPEC-0001` §11; DEC-005; `ADR-0004` item 4; mofn report R-001 §10.4 | the predicate is signature-agnostic, so its post-quantum posture is wholly the envelope's and the consumer's (§8) |
| S-02 | silent | The request a VSA answers | §3 L69, L83 | R-0022, R-0023 | `SPEC-0004` §10.1, §12 | the placeholders imply a request; our ask is that request, kept local, and a remote evaluator appears only as a privacy note |
| S-03 | silent | Revoking or superseding a VSA; a VSA whose inputs are revoked later | whole source (§9 check 4) | — | `ADR-0003` D5; `SPEC-0004` §7.1; R-O-02 | nothing withdraws a VSA. With no expiry (C-05) it stands until consumers drop the pair that accepts it |
| S-04 | silent | What a verifier must check about a dependency's VSA before counting it | §2 L50-60 | R-0020 | R-M-10; `SPEC-0004` §6.3, §6.5, §10.3 | a relying party inherits V's undisclosed choice of dependency verifiers, where our paths are explicit, bounded and reported |
| S-05 | silent | What a policy is, and what `PASSED` means beyond passing it | §3.2 L169, L190 | R-0041 | DEC-008; `SPEC-0003` §8.3; W-22; `SPEC-0005` §5 | a result means whatever V's policy means |
| S-06 | silent | Serialisation, canonical form, and whether bytes are parsed before or after the signature is checked | whole source (§9 check 4) | — | R-O-03, R-O-05; P5.1; `SPEC-0002` §3 | left to the envelope and to the implementer |

---

## 2. Row details

Source passages are markers rendered by `bin/check-quotes`. Each row's
*finding* above is argued here or in the section it names.

### 2.1 Adopt

**A-01 — trust in a verifier is configured.** The first required step verifies
the envelope against keys the consumer already holds:

<!-- q L283-285 -->
> 1. Verify the signature on the VSA envelope using the preconfigured roots of trust. This step ensures that the VSA was produced by a trusted producer and that it hasn't been tampered with.

and the rules about which keys to hold are R-0004's limit to configured
(signer, verifier) pairs (K-03) and a SHOULD addressed to the consumer:

<!-- q L316-318 "Instead," .. "roots of trust." -->
> Instead, VSA consumers SHOULD carefully consider which verifiers they add to their roots of trust.

No field of the predicate names a key, and no VSA proposes one. Our position is
the same and stricter. An anchor is local and per context (`ADR-0003` D3, D4,
`spec/ADR-0003-ksa-core-decisions.md:49-50`). A signed statement proposing one
counts only after a person or organisation persona accepts it
(`spec/SPEC-0004-ksa-trust-evaluation.md:205-240`). Discovering a key confers
nothing (W-14, `spec/ARCH-0003-wallet-object-model.md:746`). R-I-02
(`spec/ARCH-0001-authorization-attestation.md:442`) therefore holds for a VSA
import by construction, provided the import profile does not create an anchor
from the envelope's signer. That is a rule the profile has to state
*(inferred)*.

**A-02 — the limit.** The source's whole security statement about the verifier:

<!-- q L316-317 "IMPORTANT:" .. "malicious insider." -->
> IMPORTANT: A VSA does not protect against compromise of the verifier, such as by a malicious insider.

Our verdict has to close on a sentence saying that it establishes who spoke
and their entitlement, not truth (`spec/SPEC-0004-ksa-trust-evaluation.md:613-615`),
and `SPEC-0001` §10 says that when a key with standing signs a false claim,
nothing catches it (`spec/SPEC-0001-ksa-architecture.md:410-411`;
`LIMITATIONS.md:5-8`). Same limit, different placement: ours is printed under
every answer, while the VSA's sits in the specification and never in a VSA.

**A-03 — the subject against the artifact in hand.**

<!-- q L287-288 -->
> 2. Verify the statement's `subject` matches the digest of the artifact in question. This step ensures that the VSA pertains to the intended artifact.

`SPEC-0004` §10.1 has the evaluator hash the relying party's file for a digest
subject and forbids reading the digest out of a statement (`spec/SPEC-0004-ksa-trust-evaluation.md:513-516`),
and the integrity line compares that copy (`:574` there). The VSA does not say
how the consumer obtains the digest it compares. Step 2 is only meaningful if
the consumer computes it *(inferred)*, which is our rule.

**A-04 — goals vary, so the procedure does.**

<!-- q L274-277 "Goals differ" .. "its context." -->
> Goals differ, as do levels of confidence in VSA producers, so the verification procedure changes to suit its context.

`ADR-0003` D4 has each evaluation use the anchors of a single context, and
`SPEC-0004` §3 requires one answer for one set of inputs, the context among them
(`spec/SPEC-0004-ksa-trust-evaluation.md:165-168`, `:172-177`). The two §5.1
cases (full delegation; a rule about Build L2 and above) are the same artifact
evaluated under two contexts. We would write them as two contexts, or two asks.

**A-05 — inputs by digest.**

<!-- q L184-185 "Each entry MUST" .. "the attestation." -->
> Each entry MUST contain a `digest` of the attestation and SHOULD contains a > `uri` that can be used to fetch the attestation.

The same shape as `SPEC-0003` §4.4: a locator is a retrieval hint and never an
identity (`spec/SPEC-0003-ksa-definitions.md:181-186`). The VSA's `policy` field
inverts it (K-05).

### 2.2 Adapt

**D-01 — the claim, and what it imports as.** The model:

<!-- q L42-48 "A Verification Summary Attestation (VSA) is an attestation" .. "determination." -->
> A Verification Summary Attestation (VSA) is an attestation that some entity (`verifier`) verified one or more software artifacts (the `subject` of an in-toto attestation [Statement]) by evaluating the artifact and a `bundle` of attestations against some `policy`. Users who trust the `verifier` may assume that the artifacts met the indicated SLSA level without themselves needing to evaluate the artifact or to have access to the attestations the `verifier` used to make its determination.

This is P2's form with V as speaker and the subject digests as targets. The
native candidates are `attestation` (kind 4, any target) and `approve` (kind 10,
a statement or a digest; `spec/SPEC-0002-ksa-core.md:532-538`). An approval
counts only when its speaker holds a delegation to approve (`:659-662` there), which
fits a VSA that a template or process requires. Coverage takes an
`attestation`, and another kind only when what is asked about is a review or an
approval (`spec/SPEC-0004-ksa-trust-evaluation.md:525-527`), and the
prototype looks at attestations alone (`prototype/wallet/engine/reduce.py:213`).
Pass 1 wrote that coverage accepts either, dropping that condition. An
`aggregate` is the third candidate and is rejected (X-01).

The delegated trust then becomes an anchor, or a delegation from one, about the
types of whatever definition carries the VSA's fields. That is `ARCH-0001` §4.3's
per-context trust in artifact services, a configured list of which issuer may
claim which type (`spec/ARCH-0001-authorization-attestation.md:393`). **We add a scope the VSA
never states.** An anchor's `about` may not be empty
(`spec/SPEC-0004-ksa-trust-evaluation.md:198`), so even §5.1's full delegation
becomes trust in V about those types only, unbounded within them. The VSA's
(signer, verifier) pair trusts V about everything it signs as that verifier
(K-03). UC-1 is our version of §5.1's second case with one more hop:
maintainer, then build bot, then the claim
(`spec/UC-0001-ksa-use-cases.md:56-96`).

**D-02 — levels.** The source's two statements of the implication:

<!-- q L199-202 "Users MUST NOT" .. "level per track." -->
> Users MUST NOT include more than one level per SLSA track. Note that each SLSA > level implies all levels below it (e.g. `SLSA_BUILD_LEVEL_3` implies > `SLSA_BUILD_LEVEL_2` and `SLSA_BUILD_LEVEL_1`), so there is no need to > include more than one level per track.

<!-- q L392-394 -->
> Note that each SLSA level implies the levels below it in the same track. For example, `SLSA_BUILD_LEVEL_3` means (`SLSA_BUILD_LEVEL_1` + `SLSA_BUILD_LEVEL_2` + `SLSA_BUILD_LEVEL_3`).

`SPEC-0003`'s integer base kind has ranges `[lo, hi]` and a within relation
that is interval containment (`spec/SPEC-0003-ksa-definitions.md:268`). So a
build-level type with values 0 to 3 lets a relying party trust V about `[2, 3]`,
which is the second §5.1 case's rule. The enum kind (`:267` there) relates ranges by
subset alone, so the same scope would have to list `L2` and `L3`, and nothing
would say that L3 includes L2. What does not fit an integer: `UNEVALUATED`
(L380-381), `FAILED` (L390), verified properties (L196) and custom values
(L396-397, X-02). **Ours:** one integer type per track, with a separate type for
the overall outcome; whether an ask can carry a range is C-03.

**D-03 — completeness of inputs.**

<!-- q L180-182 "This field MAY" .. "verification." -->
> This field MAY be absent if the verifier does not support this feature. > If non-empty, this field MUST contain information on _all_ the attestations > used to perform verification.

`SPEC-0004` §10.3 makes `because` list every statement relied on, by digest;
for every attribute it covered, the chain of anchor and trust statements and how the
scope narrowed at each step; what was checked; how many revocations were
consulted; and every departure from default policy
(`spec/SPEC-0004-ksa-trust-evaluation.md:556-562`). The VSA's rule is the first
of those only, and only when the list is present. `SPEC-0005` §6.3 condition 3
goes further and refuses an aggregate that omits an input the evaluator itself
holds (`spec/SPEC-0005-ksa-processes.md:217-222`). A VSA consumer cannot test
completeness at all: it does not know what V used *(inferred)*.

**D-04 — the resource.**

<!-- q L159-164 "The `resourceUri` SHOULD" .. "out-of-band channel." -->
> The `resourceUri` SHOULD be set to the URI from which the producer expects the > consumer to fetch the artifact for verification. This enables the consumer to > easily determine the expected value when [verifying](#how-to-verify). If the > `resourceUri` is set to some other value, the producer MUST communicate the > expected value, or how to determine the expected value, to consumers through > an out-of-band channel.

Mapped as **Ours**: a text attribute carrying the URI on the digest target, the
way `SPEC-0002` §7.2 carries a locator (`spec/SPEC-0002-ksa-core.md:479-486`) and
AR-3 carries one (`spec/ARCH-0001-authorization-attestation.md:215`). The
consumer's expected value goes into the ask's `has`. Two things do not carry
over. R-M-11 lets a locator count as evidence about a subject, never as authority over it
(`spec/ARCH-0001-authorization-attestation.md:434`), while here the URI is not
evidence about the bytes but a scope of the decision, and checking it is a
required step (L298-300). And coverage does not keep it tied to the same VSA's
levels (C-04). §6 below.

**D-05 — the procedure.**

<!-- q L281 -->
> Verification MUST include the following steps:

<!-- q L308-311 -->
> Verification MAY additionally contain the following step: 1. (Optional) Verify additional fields required to determine whether the VSA meets your goal.

The steps are listed and numbered, and nothing says they run in that order;
step 4 points back to step 1's key (L294-295), which is the only ordering the
text implies. `SPEC-0002` §9.2 fixes an order and stops at the first failure
(`spec/SPEC-0002-ksa-core.md:688-706`), and R-O-05 puts the signature check
before any decoding (`spec/ARCH-0001-authorization-attestation.md:457`). §7 below
maps the steps one by one.

### 2.3 Reject

**X-01 — a VSA is not an aggregate.** The source's two purposes:

<!-- q L28-32 "They can use it to delegate" .. "regarding the artifact." -->
> They can use it to delegate complex policy decisions to some trusted party and then simply trust that party's decision regarding the artifact.

<!-- q L34-35 "It also allows" .. "taken place." -->
> It also allows software producers to keep the details of their build pipeline confidential while still communicating that some verification has taken place.

Our `aggregate` carries a process reference, the digests of every input and a
boolean result (`spec/SPEC-0002-ksa-core.md:664-672`). It is believed only when
the evaluator obtains every cited input and recomputes the result, alone and
together with every qualifying input it holds; who signed it is provenance only
(`spec/SPEC-0005-ksa-processes.md:208-223`; W-21,
`spec/ARCH-0003-wallet-object-model.md:753`). The VSA's first purpose is that the
consumer need not hold the inputs, and its second is that the producer may keep
them confidential. Mapped to an aggregate, a VSA fails condition 1 of
`SPEC-0005` §6.3 by design. Its policy is also not a declarative process inside
DEC-008's boundary (W-22, `spec/ARCH-0003-wallet-object-model.md:754`). It is
opaque (S-05). `SPEC-0005` §1 names the alternative it was written against:
systems that bury the rule in a service, which the relying party then has no
choice but to trust (`spec/SPEC-0005-ksa-processes.md:55-64`). A VSA is that design, chosen
deliberately and for stated reasons. We can carry its meaning as trust in V
(D-01), or its bytes as evidence (C-01), never as a computation.

**X-02 — custom result values.**

<!-- q L396-397 -->
> Users MAY use custom values here but MUST NOT use custom values starting with `SLSA_`.

The `SLSA_` prefix is reserved by convention and everything else is open to
anyone. P1's argument against private-use ranges applies exactly: if two parties
pick one private label they collide, and with no principal attached the bytes
cannot separate them
(`spec/ARCH-0002-key-relative-naming.md:82-84`; `ADR-0001` rejected the
private-use alternative on the same ground, `spec/ADR-0001-key-relative-naming.md:64-68`).
On import a custom value becomes a value of a type in some definer's definition:
V's own, if V publishes one, otherwise the importer's. The spelling alone is
never the identity.

### 2.4 Constrains

**C-01 — importing does not carry V's signature.** The consumer verifies:

<!-- q L325-326 -->
> - The signature on the VSA envelope using V's public signing key from their preconfigured root of trust.

That signature is over the envelope, by whatever key and algorithm the envelope
uses. A KSA signature covers the received TBS, domain-separated, under
the suite the TBS names (`spec/SPEC-0002-ksa-core.md:296-328`, V3–V4 at
`:688-706`), and under P2 the
signature is the saying (`spec/ARCH-0002-key-relative-naming.md:146-148`). So an
imported VSA is never a native statement by V. The homes, all *(inferred)*:

1. **V signs natively** with a KSA key. Reusing V's envelope key is discouraged
   (`spec/SPEC-0002-ksa-core.md:900`; W-11 makes it off by default,
   `spec/ARCH-0003-wallet-object-model.md:743`). How the relying party links V's
   KSA key to the verifier it configured is out of band.
2. **The importer attests** to what V's VSA said. The speaker is then the
   importer, and the relying party's trust has to reach the importer, not V.
3. **The VSA rides whole as evidence.** That is the shape of `ARCH-0001` §6's SLSA
   provenance row (carried as a predicate) and its SCITT receipt row (a receipt
   kept beside the statement it is about)
   (`spec/ARCH-0001-authorization-attestation.md:499`, `:503`). A text attribute
   can carry the original bytes unaltered, because KSA text is preserved byte
   for byte (`spec/SPEC-0002-ksa-core.md:222`). It is still not verifiable by
   our verifier, which runs V1–V9 only.

Only the first keeps V as the speaker of a native statement. Only the third
keeps the VSA's own signature, which our verifier cannot check. The second and
third both make the importer a speaker the relying party has to trust.

**C-02 — subjects and digests.** The schema's subject is a list of name and
digest-map pairs (L67-70); the example's has one entry with one algorithm
(L234-237). Our target is one value per statement, and a digest target names
one algorithm from a registry of three, SHA-256, SHA-384 and SHA-512
(`spec/SPEC-0002-ksa-core.md:454`, `:852-854`). So a VSA with *n* subjects
becomes *n* statements, or loses every subject but the one the importer keeps,
and every algorithm beyond one per subject is dropped. `name` has no home in a
target. mofn report R-0006 §2.3 has already shown that an in-toto subject can carry
digests that are not cryptographic, so an import has to name the algorithms it
will take (`research/0006-mechanism/report.md:288-294`). This source shows the
same field and says nothing on the question.

**C-03 — exact values against cumulative levels.**

<!-- q L305-306 -->
> 7. Verify that `verifiedLevels` contains the expected value. This step ensures that the artifact is suitable for the consumer's purposes.

<!-- q L362 -->
> - `verifiedLevels` is `SLSA_BUILD_LEVEL_2` or `SLSA_BUILD_LEVEL_3`.

Our ask is a context, a subject, a list of attributes and a time
(`spec/SPEC-0004-ksa-trust-evaluation.md:504-511`). Coverage needs a statement
that assigns the asked value to the asked type
(`spec/SPEC-0004-ksa-trust-evaluation.md:525-527`). An ask carries values, never
ranges; ranges belong to trust scopes. L2 or L3 is therefore two asks. An importer could
write out the implied lower levels as extra attributes, which makes one ask
suffice. R-0054 limits the VSA's writer to a single level for each track; it
does not bind a translation into another format *(inferred)*. Whether
to do so is for MAP-0002.

**C-04 — one VSA, one conjunction; our coverage, per attribute.** §5 steps 5
to 7:

<!-- q L298-306 -->
> 5. Verify that the value for `resourceUri` in the VSA matches the expected value. This step ensures that the consumer is using the VSA for the producer's intended purpose. 6. Verify that the value for `verificationResult` is `PASSED`. This step ensures the artifact is suitable for the consumer's purposes. 7. Verify that `verifiedLevels` contains the expected value. This step ensures that the artifact is suitable for the consumer's purposes.

All three are checked against the same VSA. `SPEC-0004` §10.2 asks, for each
attribute in the ask separately, whether some statement assigns it
(`spec/SPEC-0004-ksa-trust-evaluation.md:521-536`), and the prototype loops over
the asked attributes and looks for candidates for each one on its own
(`prototype/wallet/engine/reduce.py:204-230`). Import VSA 1 (resource R1,
`PASSED`, Build L3) and VSA 2 (resource R2, `PASSED`, Build L1) for one digest.
The ask (resource R2, `PASSED`, Build L3) is then covered, with R2 from the
second and L3 from the first, though no VSA says that *(inferred)*. A template
can require attributes to appear together in one statement
(`spec/SPEC-0003-ksa-definitions.md:365-366`), but coverage still picks per
attribute. A record attribute carrying all three would hold them together, and
the ask would have to match the whole record exactly. **For T-053:** the
conjunction a VSA signs is lost unless the import encodes it as one value.

**C-05 — no validity.** `timeVerified` and its history:

<!-- q L150-152 -->
> `timeVerified` _string ([Timestamp]), optional_ > Timestamp indicating what time the verification occurred.

<!-- q L412 -->
> - Made `timeVerified` optional.

Our `valid` has three optional bounds, `not-before`, `not-on-or-after` and
`issued`, and `issued` is only what the speaker says about itself (`spec/SPEC-0002-ksa-core.md:488-501`). The
answer has to report its evaluation time (`spec/SPEC-0004-ksa-trust-evaluation.md:477-482`,
`:550`). R-O-02 favours short-lived statements over revocation
(`spec/ARCH-0001-authorization-attestation.md:454`). A VSA gives an import at
most an `issued`, and none when `timeVerified` is absent. Any bound on its
life is the importer's invention, which R-I-01's table must mark as inferred.

**C-06 — time precision.**

<!-- q L249 -->
> "timeVerified": "1985-04-12T23:20:50.52Z",

KSA time counts whole seconds from 2026-01-01T00:00:00Z, earlier instants
being negative, and carries no fraction (`spec/SPEC-0002-ksa-core.md:270-282`). The example's instant
is 1,285,029,549.48 s before that epoch. Dropping the fraction from the text
(23:20:50) gives s = −1,285,029,550, not a whole number of days, so the seconds
form T = 2s = −2,570,059,100. Converting the signed seconds count by truncation
toward zero gives −1,285,029,549, which is 23:20:51, one second late. An
importer must say which it does. Export to the example's form, a UTC date and
time in whole seconds, loses nothing, if in-toto's `Timestamp` admits whole
seconds (not read here).

**C-07 — open maps and three states.**

<!-- q L210-214 "Absence of a given level" .. "artifact's dependencies." -->
> Absence of a given level of > [SlsaResult] MUST be interpreted as reporting _0_ dependencies at that level. > A set but empty `dependencyLevels` object means that the artifact has **no** > dependency at all, while an unset or null `dependencyLevels` means that the > verifier makes no claims about the artifact's dependencies.

`SPEC-0002` §4.1 allows text-keyed maps inside values and forbids null
(`spec/SPEC-0002-ksa-core.md:214-229`), so encoding is not the obstacle.
`SPEC-0003` is: its twelve base kinds include no map with open keys. A record has
fields declared in advance whose names are labels of lower-case letters, digits
and hyphens (`spec/SPEC-0003-ksa-definitions.md:204`, `:275`), and a record type
may not be delegated (`:275` there). `SLSA_BUILD_LEVEL_3` is not a label. Unset
and null collapse into absence, which loses nothing, since the source gives the
two one meaning. The empty map survives only if the chosen type can be present
and empty *(inferred)*. `verifier.version` (L145-147) has the same shape and no
count semantics.

**C-08 — exporting an answer needs a policy name.**

<!-- q L171-172 "The entry MUST" .. "that policy." -->
> The entry MUST contain a `uri` identifying which policy was applied and > SHOULD contain a `digest` to indicate the exact version of that policy.

Our counterpart of a policy is the context's anchors, the ask and the definitions in use, plus
the non-default policy points `SPEC-0004` §9 makes the evaluator report
(`spec/SPEC-0004-ksa-trust-evaluation.md:484-498`). Anchors are local, and leave the
wallet only if the context's owner publishes them (`:200-203`, `:674-675`
there). An answer exported as a VSA must therefore mint a URI for state we keep
private, and the digest R-0043 recommends would commit to it. R-I-03 asks for an
export of statements (`spec/ARCH-0001-authorization-attestation.md:443`), and an
answer is not one: the ask is never signed or sent as a statement
(`spec/SPEC-0004-ksa-trust-evaluation.md:513-514`). Whether answers get an
export at all is open question 15.

### 2.5 Conflicts

**K-01 — one bit where we report six lines.**

<!-- q L190 -->
> > Either “PASSED” or “FAILED” to indicate if the artifact passed or failed the policy verification.

R-O-06 requires name resolution, authorization and acceptance to be reported as
distinct results rather than one combined outcome
(`spec/ARCH-0001-authorization-attestation.md:458`; the three procedures,
`:396-403`). `SPEC-0004` §10.4 reports six lines, each pass, fail or not
evaluated (`spec/SPEC-0004-ksa-trust-evaluation.md:564-579`). The rationale is
recorded in the superseded proposal: authenticity and entitlement can come
apart, and a single result hides which of them failed
(`spec/ARCH-0001-PROPOSAL-v0.2.0.md:447-452`). The golden output for exactly that
case passes five lines and fails authorization
(`prototype/wallet/fixtures/golden/unauthorized.txt:1-6`). `FAILED` cannot carry
it. Nor can `PASSED` or `FAILED` stand for *not evaluated*, the state our verdict gives a
line that had nothing to check
(`spec/SPEC-0004-ksa-trust-evaluation.md:566-570`). `UNEVALUATED` exists in the VSA
only per track (L380-381). §7 shows a second fold inside step 1.

**K-02 — ignoring the unknown.**

<!-- q L110 -->
> - Consumers MUST ignore unrecognized fields.

<!-- q L115 -->
> - Producers MAY add extension fields using field names that are URIs.

Against P5: in a signed payload an unknown field is an error, and skipping is
opt-in (`spec/ARCH-0002-key-relative-naming.md:394-397`). `SPEC-0002` closes
every statement map and allows no extension fields under namespaced names
(`spec/SPEC-0002-ksa-core.md:440-444`, `:918-922`), and `ADR-0003` D1 rules out
URN identifiers and namespaced extension fields
(`spec/ADR-0003-ksa-core-decisions.md:47`). Natively nothing changes. At import
it is a real choice. P5.2 settles DSSE's exterior: our importer rejects unknown
exterior fields, as a documented deviation from a rule that binds DSSE
consumers (`spec/ARCH-0002-key-relative-naming.md:498-511`). It also calls the
payload interior ours to govern, which is true of our own payloads and not of a
foreign predicate whose own rule, R-0001, says to ignore. An importer held to
P5 rejects a conforming VSA that uses R-0002; one that ignores the field
deviates from P5. Either way the deviation belongs in the R-I-01 table, as P5.2
says for DSSE (open question 6).

**K-03 — a verifier is a URI, not a key.**

<!-- q L127-128 "The identity MUST" .. "judgment call." -->
> The identity MUST reflect the trust base that consumers care about. How > detailed to be is a judgment call.

<!-- q L130-133 "Consumers MUST accept" .. "verifier." -->
> Consumers MUST accept only specific (signer, verifier) pairs. For example, > "GitHub" can sign provenance for the "GitHub Actions" verifier, and "Google" > can sign provenance for the "Google Cloud Deploy" verifier, but "GitHub" cannot > sign for the "Google Cloud Deploy" verifier.

<!-- q L294-296 -->
> 4. Verify that the `verifier` matches the public key (or equivalent) used to verify the signature in step 1. This step identifies the VSA producer in cases where their identity is not implicitly revealed in step 1.

P2: the key is the speaker, and signing and saying are one act (`spec/ARCH-0002-key-relative-naming.md:146-148`). R-M-02 lets a key
alone identify a principal (`spec/ARCH-0001-authorization-attestation.md:425`),
and `ADR-0003` D1 has no URN identifiers. The VSA needs step 4 because it keeps
the two apart. Our closest step is V6, which checks that the envelope's speaker
hint equals the speaker inside the signed bytes
(`spec/SPEC-0002-ksa-core.md:688-706`). Both checks bind an identity named in
signed content to the key that verified it. For us that identity is the key's
digest, and for the VSA it is a URI the consumer must map. On import
`verifier.id` can be kept as text, a display string or an attribute, never as
an identity, the way `self.label` is display and not a binding (`spec/SPEC-0002-ksa-core.md:561`). On export it must
be minted. The source also says the field may be implicit in the signer (L135):

<!-- q L135-136 "The field is required" .. "debugging." -->
> The field is required, even if it is implicit from the signer, to aid readability and > debugging.

which is our position, arrived at from the opposite direction.

**K-04 — one identifier, several versions.**

<!-- q L17-20 "The `predicateType` URI" .. "this specification." -->
> The `predicateType` URI will always resolve to the latest > minor version of this specification.

<!-- q L111-114 -->
> - The `predicateType` URI includes the major version number and will always change whenever there is a backwards incompatible change. - Minor version changes are always backwards compatible and "monotonic." Such changes do not update the `predicateType`.

`ADR-0003` D1 identifies a type by its definition's hash and a local label
(`spec/ADR-0003-ksa-core-decisions.md:47`). The DefinitionId is computed from the
body, never asserted (`spec/SPEC-0003-ksa-definitions.md:166-172`), and a changed
definition is a new one linked by `supersedes` (W-12,
`spec/ARCH-0003-wallet-object-model.md:744`). DEC-007's acceptance test requires
that a changed rendering be detectable as a new version of the vocabulary
(`spec/ARCH-0001-authorization-attestation.md:664-667`). The VSA's identifier
names a moving document, and a VSA carries nothing that says which minor
version wrote it. `slsaVersion` names the SLSA specification the verifier
applied (L224-225), which is a different thing (open question 9).

**K-05 — a policy named by place.**

<!-- q L171-172 "The entry MUST" .. "that policy." -->
> The entry MUST contain a `uri` identifying which policy was applied and > SHOULD contain a `digest` to indicate the exact version of that policy.

A locator only helps find content and never identifies it; what is fetched
through one counts only if its hash matches (`spec/SPEC-0003-ksa-definitions.md:181-186`;
W-04, `spec/ARCH-0003-wallet-object-model.md:736`). For `inputAttestations` the
source puts the digest first (A-05), and for `policy` it puts the URI first. A
VSA that omits the SHOULD names its policy only by where it can be found, so the
same VSA can refer to different policies on different days *(inferred, as
`SPEC-0002` §13.10 argues for locator targets,
`spec/SPEC-0002-ksa-core.md:947-955`)*.

### 2.6 Silent

**S-01 — no envelope, no algorithm.** Besides the (signer, verifier) rule
(L130-137), the source's words about the signing side are step 1 (above), step
4's public key or its equivalent (L294), and §5.1's signing key (L325, L349). The words *algorithm* and *DSSE* do not occur
(§9 check 4). §8 below.

**S-02 — the request.** The schema's subject digest and `resourceUri` are
placeholders for values given in a request (L69, L83). No request is defined.
Our ask is that request: context, subject, attributes, time. It is a local
query, never signed or sent as a statement
(`spec/SPEC-0004-ksa-trust-evaluation.md:513-514`). `SPEC-0004` §12 mentions a
remote evaluator only for what it would learn: the subject and the question
(`:676-677` there). A VSA service is a remote evaluator whose answers are
signed, a case we have not specified *(inferred)*.

**S-03 — nothing withdraws a VSA.** No word for revocation, expiry or freshness
occurs (§9 check 4). Ours: issuer revocation by digest (`ADR-0003` D5,
`spec/ADR-0003-ksa-core-decisions.md:51`), counted in every answer
(`spec/SPEC-0004-ksa-trust-evaluation.md:442-453`). A VSA whose input attestations
are later revoked or found false keeps its result.

**S-04 — dependencies, transitively.**

<!-- q L50-58 "The verifier does this by" .. "`vsa.dependencyLevels`." -->
> The verifier does this by either a) verifying the provenance of each non-source dependency listed in the [resolvedDependencies](build-provenance#resolvedDependencies) of the artifact being verified (recursively) or b) matching the non-source dependency listed in `resolvedDependencies` (`subject.digest` == `resolvedDependencies.digest` and, ideally, `vsa.resourceUri` == `resolvedDependencies.uri`) to a VSA _for that dependency_ and using `vsa.verifiedLevels` and `vsa.dependencyLevels`.

The relying party trusts V. V's counts may rest on dependency VSAs from other
verifiers, and the source sets no rule for which ones V may use. R-M-10 wants every
delegation written, with its bounds, on the statement that makes it
(`spec/ARCH-0001-authorization-attestation.md:433`). Our paths are walked from
the relying party's anchors (`spec/SPEC-0004-ksa-trust-evaluation.md:383-419`),
bounded (`:434-438`) and named in the answer (`:556-558`). In our terms a
dependency count is V's own one-hop claim. Whom V relied on for it is invisible
to the relying party, and `inputAttestations` may list it or may be absent
(D-03).

**S-05 — what a policy is.**

<!-- q L169 -->
> > Describes the policy that the `subject` was verified against.

That is all the source says. Our criteria are declarative: they terminate, stay
within set bounds and touch nothing but the value tested (DEC-008's boundary test,
`spec/ARCH-0002-key-relative-naming.md:582-593`; `spec/SPEC-0003-ksa-definitions.md:419-425`;
W-22). A VSA policy can be anything, because the consumer never evaluates it.
DEC-008's worry, a key defining itself as always valid, is V's problem, not the
consumer's *(inferred)*.

**S-06 — bytes.** No canonical form, no serialisation rule, and no statement on
whether the consumer reads the Statement before or after checking the signature
(§9 check 4; §7 below). R-O-05's verify-before-decode is satisfied or not by the
envelope and the implementer, and the source cannot tell us which.

---

## 3. Field by field: the VSA against our verifier output and `ArtifactStatement`

Two native targets are in play. **The separated verifier output** is
`SPEC-0004` §10.3's answer (answer, time, reasons, verdict) and §10.4's six
lines (`spec/SPEC-0004-ksa-trust-evaluation.md:545-579`). **An imported
`ArtifactStatement`** is an `attestation` (or `approve`) whose attributes are
typed by some definition (`spec/SPEC-0002-ksa-core.md:579-589`;
`spec/ARCH-0001-authorization-attestation.md:357`). In the table, *round-trips*
means the value can come back out unchanged, *lossy* means some of it cannot,
*no home* means it is dropped, and *inferred* means one direction has to
invent it. Every mapping is **Ours**: no import profile exists at the pin.

### 3.1 The Statement layer (for MAP-0002, T-051)

| field | in the VSA | verifier output | imported attestation | import | export |
|---|---|---|---|---|---|
| `_type` | constant (L66) | — | — : the Statement is wire, as `ARCH-0001` §6 says of DSSE (`:497`) | checked, then dropped | constant |
| `subject[].name` | shown (L68) | — | no target home; at most a text attribute | lossy or no home | inferred: nothing of ours supplies it |
| `subject[].digest` | a digest map (L69) | the ask's subject, which the relying party computes | `this = [2, alg, bytes]`, one per statement, three algorithms (C-02) | lossy | round-trips for a digest target; a description target has no digest-map form (`ARCH-0001` §6 in-toto row, `:496`) |
| `predicateType` | constant (L73) | — | a type reference into someone's definition (P1) | lossy, as the in-toto row says | constant |

### 3.2 The predicate

| field | presence | verifier output | imported attestation | import | export |
|---|---|---|---|---|---|
| `verifier.id` | required (L140) | — : the evaluator, a wallet that the relying party holds, is not named | none as an identity (K-03); a display string at most | no home | inferred: a URI minted for the exporting key |
| `verifier.version` | optional (L145) | — | no open-key map kind (C-07) | lossy or no home | omitted |
| `timeVerified` | optional (L150) | `at`, always reported | `valid.issued`, a time the speaker asserts for itself | lossy: whole seconds (C-06); nothing when absent | round-trips from `at` |
| `resourceUri` | required (L155) | — : our ask has no resource, and the context is local | a locator attribute on the target (D-04) | lossy: coverage per attribute (C-04) | inferred: we hold no resource for an answer |
| `policy.uri` | required, MUST (L167, L171) | — : our policy is local state (C-08) | a text attribute | lossy | inferred (C-08) |
| `policy.digest` | SHOULD (L172) | — | a digest attribute; a DefinitionId only if the policy is one of our definitions | lossy | from a DefinitionId when there is one |
| `inputAttestations[].digest` | MUST per entry (L184) | `because`: every statement relied on, by digest | digest attributes; not statement targets unless they hash one of our TBSs (open question 10) | lossy: foreign bytes our verifier cannot resolve | round-trips for the statement digests; paths, scopes and checks are dropped |
| `inputAttestations[].uri` | SHOULD (L184-185) | — | a hint; dropped or a text attribute | no home | omitted |
| `verificationResult` | required (L188) | `answer`; the meanings differ (below) | an attribute of an enum type: passed, failed | lossy: it becomes V's claim, never the relying party's answer | lossy: six lines and every reason become one bit (K-01) |
| `verifiedLevels` | required (L193) | — : nearest is the ask's `has`, what was asked | one attribute per track (D-02); verified properties in an unsourced vocabulary; `FAILED` as an outcome value | lossy (D-02, C-03, X-02) | only where the asked types are level types *(inferred)* |
| `dependencyLevels` | optional (L205) | — | no open-key map kind (C-07) | no home, or lossy as text | omitted: nothing of ours supplies it |
| `slsaVersion` | optional (L222) | — | a text attribute; unset stays unset, with no default inferred | round-trips as text | omitted or constant |
| fields named by URI | MAY (L115) | — | none: every map of ours is closed | rejected under P5, or dropped by a declared deviation (K-02) | none emitted *(inferred, as P5.2's export rule)* |
| the envelope signature | not a field (L283) | integrity and authenticity need one of our signatures | — | not carried (C-01) | a new signature, by the exporter |

**`verificationResult` against `answer`.** We answer yes only when all six
lines pass and each asked attribute is covered along a path that starts at one
of the relying party's anchors (`spec/SPEC-0004-ksa-trust-evaluation.md:521-536`).
A VSA's `PASSED` is V's finding against V's policy (L190). Imported, it is the
content of V's statement, and the relying party's answer about it is computed
afresh. The two never map into each other: one is an input to our evaluation,
the other is its output.

**The model's `bundle`** (L44) is not a schema field. Its nearest field is
`inputAttestations` *(inferred)*.

### 3.3 What our output has and a VSA cannot hold

The six lines, each pass, fail or not evaluated; for every covered attribute,
its chain of anchor and trust statements with the scope left after each step;
the checks performed; reasons with their codes (`SPEC-0004` §14.2); the number
of revocations considered; every non-default policy; every name used, with its
bindings and the keys each name came to (`spec/SPEC-0004-ksa-trust-evaluation.md:556-562`,
`:564-579`, `:694-700`); the context; the ask itself; and the closing limit
sentence (`:613-615` there).

### 3.4 What round-trips

Field by field, through an imported attestation with every VSA field kept:
`_type`, `predicateType` (constants), `slsaVersion`, `resourceUri`, `policy`
(as attributes), a single digest per subject in one of three algorithms,
`verificationResult` and the standard levels (given D-02's inverse), and
`timeVerified` when it is a whole second. Never: extension fields, a second
digest algorithm, a non-cryptographic digest, a fraction of a second,
`verifier.id` as an identity, and V's signature (C-01), except by carrying the
VSA's bytes whole (C-01, third home). So PLAN-0001's I4 acceptance, a real SLSA
attestation imported and round-tripped (`project/PLAN-0001-project-plan.md:487`),
can be met for a VSA field by field. It can be met byte for byte only through
the third home.

### 3.5 For T-053: a candidate §6 row

**Ours**, as evidence for T-053. Not an edit: changes to `ARCH-0001` go through a
proposal (`spec/ARCH-0001-authorization-attestation.md:699`). Written in
the matrix's legend (`:488` there).

| object | import | export | native home | losses and inferences |
|---|---|---|---|---|
| SLSA VSA v1 (in-toto predicate) | P | P | `attestation` (or `approve`) about each subject digest, fields as attributes of a definition; trust in V through an anchor about that definition's types | **Import loss:** V's envelope signature (the importer speaks, V re-signs, or the VSA rides as evidence); `verifier.id` as an identity (P2); fields named by URI (P5); digest algorithms beyond three, and non-cryptographic ones; `subject[].name`; fractions of a second; the `dependencyLevels` and `verifier.version` maps; the one-VSA conjunction of resource, result and levels (coverage is per attribute); level implication (asks are exact). **Inferred on import:** any validity bound. **Export loss:** six verdict lines, reasons, paths, revocation count, policy deviations. **Inferred on export:** `verifier.id`, `resourceUri`, `policy.uri` |

---

## 4. Delegated trust: who the consumer trusts, about what, how far

| | the VSA | m-of-n |
|---|---|---|
| who is trusted | a (signer, verifier) pair, configured by the consumer (L130; L283-285) | a key, or a threshold of keys, as an anchor of one context (`spec/SPEC-0004-ksa-trust-evaluation.md:179-203`) |
| how trust starts | the consumer adds a verifier to its roots of trust (L316-318) | an unsigned local choice, a trust statement of the owner's, or someone else's trust statement once a person or organisation persona has accepted it (`ADR-0003` D3; `SPEC-0004` §4.3–§4.4) |
| about what | everything V signs as that verifier; scoping is the consumer's expected values in steps 5 to 7 | the anchor's `about`, which may not be empty (`:198` there) |
| further delegation | none in the format. V may count dependency VSAs from verifiers it chooses (S-04) | explicit, by depth, ranges and key lists, every hop narrowing (`SPEC-0004` §6.3; R-M-10) |
| per purpose | `resourceUri`, written by the VSA's producer (D-04; open question 3) | the context, held by the relying party (`ADR-0003` D4) |
| withdrawn by | reconfiguring the consumer (S-03) | revocation of the trust statement, validity caps, compromise marks (`SPEC-0004` §6.3, §7) |

Two consequences. First, the VSA's delegation is total within a pair: §5.1's
first case delegates the whole decision and checks a pre-agreed level value
that carries no meaning of its own (L340-343):

<!-- q L340-343 "Note: This example" .. "fully delegates the decision to V." -->
> Note: This example is analogous to traditional code signing. The expected value for `verifiedLevels` is arbitrary but prenegotiated by the producer and the consumer. The consumer does not need to check additional fields, as C fully delegates the decision to V.

Our nearest form is an anchor trusting V, unbounded, about one outcome type,
with the relying party asking for one outcome value. Second, the VSA puts
purpose on the producer's side (`resourceUri`) and trust on the consumer's
(roots of trust). We put both on the relying party's side: the context is
purpose, and the anchors in it are trust. Purpose in the statement is
something we can carry as an attribute (D-04). Purpose that binds a decision
across attributes is something our coverage cannot carry yet (C-04).

---

## 5. A signed verification result, against our model of verification

We verify in two stages, neither signed. Single-statement verification is
local and yields verified, invalid or unverifiable
(`spec/SPEC-0002-ksa-core.md:674-706`). Trust evaluation is local and
deterministic over named inputs, with no network
(`spec/SPEC-0004-ksa-trust-evaluation.md:165-168`). The ask is never signed or
sent as a statement (`:513-514` there). For each statement it relied on, a wallet
records what the verdict was, in which context, from which anchors
(`spec/SPEC-0001-ksa-architecture.md:258`). Nowhere do we turn a trust-evaluation
answer into a statement for someone else to rely on. The nearest thing, an
aggregate, reports a process result that its reader must recompute (X-01).

A VSA turns a verifier's answer into a statement for others, and gives its two
reasons for doing so (X-01's markers). Our
model has three ways to carry it, and they are not equivalent:

| carried as | keeps | loses |
|---|---|---|
| `attestation` or `approve` by V, trusted through an anchor (D-01) | delegated trust; the confidentiality of the inputs | recomputation; the reasons behind the result |
| `aggregate` (X-01) | recomputation, as W-21 requires | the VSA's purpose: its inputs are absent by design |
| foreign evidence kept beside a statement (C-01, third home) | V's bytes and signature | any native evaluation of them |

`SPEC-0005` §1 states the position the VSA is the counter-example to: put the
rule in a definition so that it can be checked, not trusted
(`spec/SPEC-0005-ksa-processes.md:55-64`). The VSA's second purpose,
confidentiality (L34-38), is one an aggregate cannot meet and an attestation
can, because an attestation cites no inputs. So the VSA does not argue against
`SPEC-0005`. It shows a use, keeping a pipeline private, that our aggregates are
not for and our attestations already serve. Under R-O-06, whatever carries a
VSA arrives as one bit (K-01).

mofn report R-001 counts VSAs, read as delegated authority applied
recursively, among three recovery paths, and finds that none has settled
(`research/0001-signatures-and-attestation/report.md:1364-1366`). From this
source: the recursion is §2's dependency matching (S-04). The delegated
authority is configured, not stated (A-01). Nothing bounds it (S-04, S-03).

---

## 6. `resourceUri`: a scope, not a locator

What the source does with the URI:

<!-- q L322-323 -->
> 1. Suppose consumer C wants to delegate to verifier V the decision for whether to accept artifact A as resource R. Consumer C verifies that:

<!-- q L298-300 -->
> 5. Verify that the value for `resourceUri` in the VSA matches the expected value. This step ensures that the consumer is using the VSA for the producer's intended purpose.

and in dependency matching, as a non-normative ideal next to the digest
comparison (L55-57). Our rule for a URI on a statement is that it is a locator,
evidence carried as an attribute, never the target
(`spec/SPEC-0002-ksa-core.md:479-486`; R-M-11). The reason is that what a
locator resolves to can change (`:947-955` there). The VSA's subject is the
digest too (step 2), so on the binding to bytes the two agree. They differ on
what the URI is for. In the VSA it is a second key on the decision: this
artifact, accepted as this resource, for this purpose. Our attestations about
bytes are independent of where the bytes are found. Replay does a statement no
harm (`spec/SPEC-0002-ksa-core.md:936-940`), and a review is worth
something only for the object it is about (`spec/SPEC-0005-ksa-processes.md:263-266`).
The VSA's resource binding prevents a use our model does not consider an attack
on a statement: the same bytes accepted under a different name or purpose. In
our terms that is the relying party's context. Carrying it in the statement
needs the attribute of D-04 and runs into C-04.

Who sets the URI, and who owes the out-of-band channel when it is not a fetch
URI, depends on which producer R-0094 and R-0006 mean (open question 3).

---

## 7. The consumer procedure (§5) against R-O-05 and our verifier order

| VSA §5 | lines | ours | note |
|---|---|---|---|
| 1. signature, with preconfigured roots of trust | L283-285 | V2 suite, V3 key, V4 signature over the received bytes (`spec/SPEC-0002-ksa-core.md:688-706`); trust only later, in `SPEC-0004` | the VSA verifies **with trusted keys**. We verify with known keys, since holding a key in the store makes it known and nothing more (`:722` there), and then evaluate trust. A VSA signed by a known, untrusted key fails step 1 as a signature failure, where we report it verified, authenticity passing, authorization failing. That is K-01 again, inside step 1 |
| 2. subject against the artifact | L287-288 | `SPEC-0004` §10.1 subject hashed from the relying party's file; §10.2 item 1; the integrity line | A-03 |
| 3. `predicateType` | L290-292 | V7 (registered kind, closed maps); `SPEC-0004` §5.2 (types held and conforming); the semantics line | the VSA checks one constant. We check that the type's definition is held, conforming and attributed |
| 4. verifier against the key | L294-296 | V6 agreement; P2 makes it identity, not a check | K-03 |
| 5. `resourceUri` | L298-300 | an attribute in the ask (D-04) | C-04 |
| 6. `verificationResult` is `PASSED` | L302-303 | an attribute in the ask, covered by V's statement | K-01 |
| 7. `verifiedLevels` contains the expected value | L305-306 | an attribute in the ask, exact value | C-03 |
| optional: other fields | L310-311 | none optional: every field is understood or the statement is rejected (P5; V7) | K-02 |
| — | — | V1 envelope decode, V5 canonical decode, V8 kind rules, validity at the evaluation time, revocation, path and scope, template conformance, definitions | the VSA is silent on all of them (S-03, S-05, S-06, C-05) |

**Order.** R-0011 requires the steps to be *included*. Nothing makes the
numbering an order, except step 4's reference back to step 1. A consumer that
parses the Statement and checks `predicateType` before the signature conforms to
this source *(inferred)*. R-O-05 forbids it for us: the signature comes before
any decoding, and no canonicalisation runs while verifying
(`spec/ARCH-0001-authorization-attestation.md:457`; `spec/SPEC-0002-ksa-core.md:313-317`).
**Ours:** an importer checks the envelope's signature before it decodes the
Statement, then runs steps 2 to 7. The source permits that order, so it
records no deviation.

**The authenticated type indicator.** R-O-05 requires one. Here the type is
`predicateType` inside the signed Statement (step 3). Whether the Statement's own
type is authenticated is the envelope's business, and this source does not say
(S-01).

---

## 8. Post-quantum, the envelope, and MD-3

**Signature-agnostic.** The predicate holds no key, algorithm or signature. The
word *envelope* occurs three times, always as the VSA's own envelope, in a
verification step (L283, L325, L349), and the words *algorithm*, *DSSE* and
*canonical* not at all (§9 check 4). So everything about post-quantum readiness
sits outside this document: which algorithm signed a VSA, whether a consumer's
roots of trust include post-quantum keys, and what a consumer does with a VSA
whose algorithm has weakened. A VSA has no expiry (C-05), so a classically
signed VSA is acceptable until the consumer reconfigures. Its only time is
`timeVerified`, the verifier's own optional claim, which is not evidence of
existence before a break (*inferred*, as `SPEC-0001` §11 says of `valid.issued`,
`spec/SPEC-0001-ksa-architecture.md:415-422`).

Ours, for contrast: the suite sits inside the signed bytes
(`spec/SPEC-0002-ksa-core.md:350`). Suite 8, ML-DSA-65, is provisional
(`:409-422` there). A long-lived statement should be signed under a post-quantum
suite, failing which it needs an independent timestamp (`SPEC-0001` §11). mofn report R-001 §10.4 argues that an
envelope's silence about algorithms is a defect, since it can neither pin an
algorithm nor require quantum-resistant signers
(`research/0001-signatures-and-attestation/report.md:1597-1612`). That is
evidence and decides nothing. This source is an instance of the same silence one
layer up, in the predicate.

**MD-3 and `ADR-0004`.** MD-3, on 2026-09-28, cut DEC-002's choices down to option 5,
keeping COSE for export (`project/meetings/2026-09-28.md:51-54`). `ADR-0004` accepted it and made
COSE_Sign1 and DSSE export envelopes only, keeping every IANA registry out of
the native model (`spec/ADR-0004-dec-002-encoding.md:46-52`). This source carries **no evidence on
DEC-002's options**. It specifies no encoding, no canonical form and no signing
input, so nothing in it favours any of options 1 to 5. Its interchange costs land
on P1 (X-02, K-04), P2 (K-03, C-01), P5 (K-02) and `SPEC-0003`'s type system
(C-07, D-02), which every option would pay. Two small points touch the data
model. KSA-CBOR's ban on null costs nothing here (C-07). The fraction of a
second is lost (C-06), but that comes from our time type, not from CBOR.
`ADR-0004` item 3 lists the IANA registries that are never native. The VSA
uses none of them. Its global names are a URI type identifier and a reserved
string prefix. Neither is IANA, and both meet P1's argument at the boundary
(X-02, K-04) *(inferred)*.

---

## 9. Arithmetic, and every *only*, checked

1. **Keywords.** `bin/bcp14-count .cache/slsa-vsa-1-2.txt` prints 21. The
   skeleton's 15 sentences carry 2 in §3.1, 13 in §3.2, 3 in §5 and 3 in §6
   (`skeleton-report.txt`), and 2 + 13 + 3 + 3 = 21.
2. **The example's dependency counts** (L263-267): 5 + 7 + 1 = 13 Build-track
   dependencies, with no Build L0 key and no Source-track key. Under R-0059
   that reads as zero dependencies at Build L0 and at every Source level. So the
   example states that none of the 13 was verified at any Source level, which
   is indistinguishable from a Source track left unevaluated (open question 7).
3. **Time** (C-06), by `datetime` and checked again by `calendar.timegm`:
   1985-04-12T23:20:50Z is Unix 482,196,050, and 2026-01-01T00:00:00Z is
   1,767,225,600. So s = −1,285,029,550, and s mod 86,400 = 84,050 ≠ 0, which
   gives the seconds form, T = 2s = −2,570,059,100. Its magnitude is far inside
   ±(2^53 − 1). Truncating −1,285,029,549.48 toward zero gives −1,285,029,549:
   23:20:51.
4. **Occurrences**, by regular expression over the 432 lines:
   *envelope* 3 (L283, L325, L349); *signature* 4 (L283, L295, L325, L349);
   *algorithm* 0; *DSSE* 0; *canonical* 0; *expir*, *revoc*, *revok*,
   *freshness*, *not after*, *valid until* 0 between them; *roots of trust*
   plural twice (L283-284 across a line break, L318) and *root of trust* singular
   twice (L326, L350); `slsaResult` 3 (L336 and L360 as a field, L406 in the
   change history); *producer* or *producers* 8 (L34, L159, L162, L277, L284,
   L295, L300, L341); *Users* 4 (L45, L199, L216, L396); `FAILED` 4 (L95, L190,
   L197, L390); `UNEVALUATED` 3 (L338, L380, L385).
5. **Level implication** (D-02): with Build levels as integers 0 to 3, the scope
   `[2, 3]` contains 2 and 3 and nothing else, which is §5.1's second rule. An
   enum scope would have to list both values.
6. **The matrix** (`ARCH-0001` §6): `spec/ARCH-0001-authorization-attestation.md:492-503`
   hold 12 rows below the header, and none names the VSA.
7. **Every *only* in this file**, re-checked. *Three registered digest
   algorithms* (C-02): `SPEC-0002` §12.5 lists exactly codes 1 to 3. *The only
   ordering the text implies* (D-05): within L281-311 the only cross-references
   are step 4's two mentions of step 1 (L295, L296). *Only the first keeps V as
   speaker; only the third keeps the VSA's own signature* (C-01): true of the
   three homes listed, which are the ones considered, not a proof that no other
   exists. *An ask carries values, never ranges* (C-03): `SPEC-0004` §10.1's ask
   holds attributes, each a type and a value; ranges occur in trust scopes and
   in constraint expressions, never in an ask. *`UNEVALUATED` only per track*
   (K-01): its form names a track (L380-381). Two first-draft claims failed this
   check and were rewritten: that the only rule about roots of trust is a SHOULD
   (R-0004 is a MUST about the same choice, A-01), and that we nowhere sign an
   evaluation result (an aggregate is one, §5). *Our version adds one hop*
   (D-01): UC-1's path has an anchor, a trust statement and the claim. A first
   draft of D-01 called `attestation` the only home that keeps delegated trust.
   `approve` (kind 10) also does (`spec/SPEC-0002-ksa-core.md:659-662`), and the
   row now names both.

---

## 10. Open questions

**In the source: inconsistent or underspecified.**

1. **`slsaResult` survives in §5.1** (SD-15). The 1.2 change history records the fix:

   <!-- q L405-406 -->
> - Fixed a typo where the verificationResult was incorrectly referred to as slsaResult.

   Step 6 now says `verificationResult` (L302). Both §5.1 cases still check a
   field the schema does not have:

   <!-- q L336 -->
> - `slsaResult` is `PASSED`.

   (and again at L360). A consumer implementing §5.1 literally looks for a field
   that never occurs. Read as `verificationResult` *(inferred)*.
2. **The pair example is about provenance** (SD-5). K-03's marker: the example under
   `verifier` has organisations signing *provenance* for named verifiers
   (L130-133). The field is a VSA's. It reads as text carried over from a
   builder's definition *(inferred)*. Whether R-0004 binds VSA signers in
   exactly this way is left to inference.
3. **Two producers** (SD-21). *Producer* means the software producer at L34 and the
   VSA's producer at L277, L284 and L295. R-0094
   and R-0006 (L159, L162), step 5's intended purpose (L300) and §5.1's
   pre-agreed value (L341) do not say which. Who sets `resourceUri`, and who
   owes the out-of-band channel? For us the answer chooses between an attribute
   in V's statement and an expectation in the relying party's ask.
4. **Two kinds of user** (SD-9). *Users* are consumers at L45 and writers of the VSA at
   L199, L216 and L396. The actors of R-0054, R-0061, R-0080 and R-0081 are inferred
   (the requirements lane owns `actor`).
5. **Failure said twice** (SD-8, SD-17).

   <!-- q L195-197 "Indicates the highest" .. "policy verification failed." -->
> Indicates the highest level of each track verified for the artifact (and not > its dependencies) and any [verified properties](verified-properties) verified > for the artifact or "FAILED" if policy verification failed.

   With `verificationResult` (L190), a VSA has two places to say it failed, and
   the source gives neither precedence. What does `PASSED` with `["FAILED"]`
   mean, or `FAILED` with levels? `FAILED` is also listed as a `SlsaResult`
   example (L390), yet it is neither of R-0014's recommended forms (L378-381). It
   reads as a custom value R-0080 permits. Can it be a `dependencyLevels` key?
6. **P5 and a foreign predicate's interior** (K-02). Does our importer reject a
   VSA carrying an unrecognised field, deviating from R-0001 the way P5.2
   deviates from DSSE at the exterior? Or does it drop the field, deviating
   from P5? It belongs in R-I-01's table, beside P5.2's DSSE row
   (`spec/ARCH-0002-key-relative-naming.md:519-535`).
7. **Absence is zero** (SD-22). By R-0059 a VSA that evaluated only Build-track
   dependencies asserts zero at every Source level (§9 check 2). The nearest a
   VSA comes to making no claim about one track is an explicit
   `…_UNEVALUATED` count; making none at all needs an unset map. Counting once per track means that, with two
   tracks reported, the counts sum to more than the number of dependencies
   *(inferred)*.
8. **Several subjects, several algorithms** (SD-26, SD-1). Step 2 and §2's matching
   (L55-56) do not say whether every algorithm, any shared algorithm, or a
   named one must match. Nor do they say whether one VSA's result holds for
   each subject or for the set (C-02).
9. **Version identity** (K-04; SD-23). Minor versions keep the identifier and are
   called backwards compatible (L113-114), yet 1.1 made `timeVerified`
   optional (L412). A 1.0 consumer that required the field breaks on a change
   the source calls compatible. No field says which minor version of the VSA
   format a VSA follows:

   <!-- q L224-226 "Indicates the version" .. "version of `1.x`." -->
> Indicates the version of the SLSA specification that the verifier used, in the > form `<MAJOR>.<MINOR>`. Example: `1.0`. If unset, the default is an > unspecified minor version of `1.x`.

10. **Empty inputs, and digest of what** (SD-6, SD-24). Completeness binds only when the list
    is non-empty (L180-182, D-03), so an empty list may mean that none was
    used or that the feature is unsupported. The digest of an
    attestation (L184) is not tied to particular bytes: the envelope, the
    Statement or a line of a bundle. The example points
    at a `.intoto.jsonl` file (L257), a file of attestations rather than one
    *(inferred)*. For an import this decides whether an entry could ever equal
    one of our statement digests.
11. **No order** (D-05, §7; SD-25): steps included, not ordered (L281).
12. ***Is* against *contains*** (SD-14). §5.1's second case says `verifiedLevels` *is* L2
    or L3 (L362), while step 7 says *contains* (L305). Read literally, *is* fails
    a VSA that also lists a verified property (L196) or a Source level.
13. **The note's link** (SD-16) points at verifying-artifacts under `/spec/v1.0/` (L366)
    in a 1.2 document, so which threats each level addresses is not in this
    source.

**For m-of-n: owed elsewhere, not decided here.**

14. **Which kind, whose key.** Does an imported VSA become an `attestation` or
    an `approve`? Does V re-sign, does the importer speak, or does the VSA ride
    as evidence (C-01)? Bears on T-051, T-053 and R-I-02.
15. **An export for answers?** R-I-03 asks for statements. An answer is not
    one (C-08), and a VSA is one bit (K-01). If T-053 records that no export
    from an answer to a VSA is defined, that record is itself the row.
16. **A same-statement conjunction** (C-04). Does coverage need a way to
    require that attributes a source binds together come from one statement?
    It would change answers, which `SPEC-0004`'s version policy calls MAJOR
    (`spec/SPEC-0004-ksa-trust-evaluation.md:10-11`).
17. **Levels** (D-02, C-03). One integer type per track or an enum? May an ask
    carry a range? Today an ask carries values only.
18. **For this library.** `docs/extraction.md` still says no DEC-002 ADR exists.
    The title lines of `SPEC-0002` and `SPEC-0004` lag their front matter (0.9.0
    against 0.10.1, 0.6.0 against 0.6.2), an observation for m-of-n. Neither is
    edited here: this lane owns one file.
19. **`bears_on`.** The findings bear on R-O-06 (K-01), R-I-02 (A-01, C-01) and
    R-M-11 (D-04, K-05) as directly as on R-I-01 and R-I-03. `record.yaml`'s
    owner may want to add them; not edited here.

---

## 11. Method: how each claim here was produced

- **Our documents** were read only as blobs of `7c3c731`: exported with
  `git -C /Users/nfn/Projects/mofn show 7c3c731:<path>` into a scratch directory
  of this lane's own for reading, and with `git archive 7c3c731` for the sweep
  below. HEAD was `7c3c731` throughout.
- **The source** is `.cache/slsa-vsa-1-2.txt`. Its digest and the `.bin` digest
  were recomputed with `shasum -a 256` and compared with `record.yaml`,
  `render-source.py` and `requirements.yaml`.
- **Blind rules kept.** This lane did not read `summary.md`, any other lane's
  output in `distilled/`, or the `slsa-1-2`, `slsa-provenance-1-2` and `in-toto-*`
  extractions. It read `requirements.yaml` only for ids, locators and texts, as
  `bin/fx1-skeleton` wrote them at `a569508`. One listing of `record.yaml`'s keys
  displayed the one-line `usefulness.reason`. Nothing here rests on it, and every
  finding is argued from the source's lines.
- **Quotations of the source** are `<!-- q -->` markers only. The blockquotes
  were written by `bin/check-quotes --render --only` on this file, and
  `bin/check-quotes` verifies each against its lines (count below).
- **m-of-n is not quoted.** Every reference is a paraphrase with `path:line`.
  The prose (front matter, markers and rendered blockquotes removed, code spans
  treated as breaks) was swept for runs of six or more consecutive words that
  occur in any file of `git archive 7c3c731`. Every prose hit was rewritten: 36
  passages over two six-word sweeps, then 20 more that a five-word sweep showed
  to be distinctive m-of-n phrasing. The runs that remain are lists of
  identifiers: principle numbers, requirement ids and version numbers (count
  below). Kept as written, code spans add hits that are only paths.
- **Unmarked source text.** The same prose was swept for runs of six or more
  words that occur in the source, with code spans both as breaks and kept. The
  one hit of the first sweep was rewritten (count below).
- **Requirement ids.** Pass 1 took them from the skeleton by script under both
  of the library's YAML readers, which agree, and cited all fifteen; the
  statements it cited without an id of their own (the §5 steps through R-0011's
  lead-in, the optional step through R-0012's, the versioning rules, the field
  table's required and optional markings, the meaning of `verificationResult`,
  the level implication, the dependency matching and `slsaVersion`'s default)
  each have an entry now. Pass 2 re-pointed the citations to the full table by
  script and read each resolved pair; the table below is emitted from
  `requirements.yaml`. The verifier-compromise sentence (L316-317) and the §5.1
  lines other than the ones R-0082 and R-0084 rest on remain without an id: the
  requirements lane rejected them as a limitation and as illustration.

**Joins** (every id this file cites, beside where it is cited; emitted by script from
`requirements.yaml` by pass 2, and each resolved pair read. The opening paragraph names
R-0011, R-0015, R-0016, R-0092, R-0093, R-0094 as the ends of id ranges or in describing this pass;
those mentions are not citations and are left out):

| id | locator | cited at |
|---|---|---|
| `slsa-vsa-1-2#R-0001` | §3.1 L110 | K-02, open question 6 |
| `slsa-vsa-1-2#R-0002` | §3.1 L115 | K-02 |
| `slsa-vsa-1-2#R-0004` | §3.2 L127-130 | A-01, K-03, §9 check 7, open question 2 |
| `slsa-vsa-1-2#R-0006` | §3.2 L161-164 | D-04, §6, open question 3 |
| `slsa-vsa-1-2#R-0011` | §5 L281 | A-04, D-05, §7, §11 |
| `slsa-vsa-1-2#R-0012` | §5 L308 | A-04, D-05, §11 |
| `slsa-vsa-1-2#R-0013` | §5 L317-318 | A-01, A-02 |
| `slsa-vsa-1-2#R-0014` | §6 L376 | D-02, open question 5 |
| `slsa-vsa-1-2#R-0016` | Preamble L14 | K-04 |
| `slsa-vsa-1-2#R-0017` | Preamble L17-18 | K-04 |
| `slsa-vsa-1-2#R-0018` | Preamble L18-19 | K-04 |
| `slsa-vsa-1-2#R-0019` | §2 L42-45 | D-01 |
| `slsa-vsa-1-2#R-0020` | §2 L51-58 | S-04 |
| `slsa-vsa-1-2#R-0022` | §3 L69 | S-02 |
| `slsa-vsa-1-2#R-0023` | §3 L83 | S-02 |
| `slsa-vsa-1-2#R-0025` | §3.1 L111-112 | K-04 |
| `slsa-vsa-1-2#R-0026` | §3.1 L113 | K-04 |
| `slsa-vsa-1-2#R-0027` | §3.1 L113-114 | K-04 |
| `slsa-vsa-1-2#R-0031` | §3.2 L135-136 | K-03 |
| `slsa-vsa-1-2#R-0034` | §3.2 L145 | C-07 |
| `slsa-vsa-1-2#R-0035` | §3.2 L147 | C-07 |
| `slsa-vsa-1-2#R-0036` | §3.2 L150 | C-05 |
| `slsa-vsa-1-2#R-0037` | §3.2 L152 | C-05 |
| `slsa-vsa-1-2#R-0040` | §3.2 L167 | C-08 |
| `slsa-vsa-1-2#R-0041` | §3.2 L169 | X-01, S-05 |
| `slsa-vsa-1-2#R-0042` | §3.2 L171 | X-01, C-08, K-05 |
| `slsa-vsa-1-2#R-0043` | §3.2 L172 | C-08, K-05 |
| `slsa-vsa-1-2#R-0045` | §3.2 L177-178 | X-01 |
| `slsa-vsa-1-2#R-0046` | §3.2 L180 | D-03 |
| `slsa-vsa-1-2#R-0047` | §3.2 L181-182 | D-03, X-01 |
| `slsa-vsa-1-2#R-0048` | §3.2 L184 | A-05 |
| `slsa-vsa-1-2#R-0049` | §3.2 L184-185 | A-05 |
| `slsa-vsa-1-2#R-0050` | §3.2 L188 | K-01 |
| `slsa-vsa-1-2#R-0051` | §3.2 L190 | K-01 |
| `slsa-vsa-1-2#R-0054` | §3.2 L199 | D-02, C-03, open question 4 |
| `slsa-vsa-1-2#R-0055` | §3.2 L199-202 | D-02 |
| `slsa-vsa-1-2#R-0059` | §3.2 L210-211 | C-07, §9 check 2, open question 7 |
| `slsa-vsa-1-2#R-0060` | §3.2 L212-214 | C-07 |
| `slsa-vsa-1-2#R-0061` | §3.2 L216-217 | open question 4 |
| `slsa-vsa-1-2#R-0066` | §5 L274-276 | A-04 |
| `slsa-vsa-1-2#R-0067` | §5 L283-284 | A-01, D-05, C-01, S-01 |
| `slsa-vsa-1-2#R-0068` | §5 L287-288 | A-03, C-02 |
| `slsa-vsa-1-2#R-0070` | §5 L294-295 | K-03, S-01 |
| `slsa-vsa-1-2#R-0071` | §5 L298-299 | D-04, C-04 |
| `slsa-vsa-1-2#R-0072` | §5 L302 | C-04, K-01 |
| `slsa-vsa-1-2#R-0073` | §5 L305 | C-03, C-04 |
| `slsa-vsa-1-2#R-0074` | §5 L310-311 | D-05 |
| `slsa-vsa-1-2#R-0076` | §6 L378-379 | D-02 |
| `slsa-vsa-1-2#R-0077` | §6 L380-381 | D-02 |
| `slsa-vsa-1-2#R-0079` | §6 L392 | D-02 |
| `slsa-vsa-1-2#R-0080` | §6 L396 | X-02, open question 4, open question 5 |
| `slsa-vsa-1-2#R-0081` | §6 L396-397 | X-02, open question 4 |
| `slsa-vsa-1-2#R-0082` | §5, inferred | K-03, §11 |
| `slsa-vsa-1-2#R-0083` | §5, inferred | A-01 |
| `slsa-vsa-1-2#R-0084` | §5, inferred | C-03, §11 |
| `slsa-vsa-1-2#R-0086` | §5, inferred | C-01 |
| `slsa-vsa-1-2#R-0091` | §3.2, inferred | D-04 |
| `slsa-vsa-1-2#R-0092` | §2, inferred | C-02 |
| `slsa-vsa-1-2#R-0093` | §3.2 L127 | K-03 |
| `slsa-vsa-1-2#R-0094` | §3.2 L159-160 | D-04, §6, open question 3 |

**Counts, measured on the final text of this file** (each states what was
examined; recount after any edit). Pass 2 (verify) edited this file and re-measured
every row; pass 1's figures are kept beside its own where they differ:

| check | examined | result |
|---|---|---|
| `bin/check-quotes --only` this file | 45 source quotations | 0 mismatched |
| m-of-n six-word runs in our prose | 8,686 windows against 382 m-of-n text files, tokens being lower-case runs of letters and digits (pass 1, tokenizing its own way: 7,573) | 5 runs, every one a list of identifiers. Pass 1 reported 6, every one a list of identifiers; the sixth was an ordinary six-word phrase that also occurs in `UC-0001`, and pass 2 rewrote it, as it did one run its own D-01 correction first introduced |
| source six-word runs outside markers | 8,705 windows with code spans as breaks, 13,159 with them kept | 0 occur in the source |
| requirement ids cited | 117 matches of the bare pattern `\bR-\d{4}\b` before the joins table (pass 2 stated 109; pass 3 recounted 117, 122 with the five below), to 61 ids, 60 of them cited (R-0015 is only the end of a range in the opening paragraph); 5 more matches are mofn report R-0006, named as such. Pass 1: 15 distinct, 76 occurrences | 0 unresolved, every pair read |
| rows in §1 | 31 | 5 adopt, 5 adapt, 2 reject, 8 constrains, 5 conflicts, 6 silent |

---

## 12. What this file decides

Nothing. It records evidence and maps it. It adds, amends and withdraws no
requirement, and opens, ranks or accepts no DEC-*. `ADR-0004` stays closed.
No import profile is chosen: every mapping above marked **Ours** is a proposal
for MAP-0002 (T-051) and T-053 to weigh. A decision belongs to an ADR
(`ARCH-0001` §9 and R-D-02, `spec/ARCH-0001-authorization-attestation.md:465`,
`:694-699`; `CONTRIBUTING.md:108`).
