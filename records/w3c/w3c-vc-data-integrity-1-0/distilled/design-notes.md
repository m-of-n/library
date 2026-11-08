---
record: w3c-vc-data-integrity-1-0
kind: design-notes
title: "w3c-vc-data-integrity-1-0 — bearing on our design"
extracted: "2026-11-07"
reviewed_by: ""
---

# VC Data Integrity 1.0 — bearing on our design

*Verifiable Credential Data Integrity 1.0* is the W3C Recommendation of 15 May
2025 (REC-vc-data-integrity-20250515; HTML, sha256
`ba5c4baf13fe3bab3ebd95ab6650d6fe83720e254b383bb444b4fbbae7bcf4fe`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass).
It secures a JSON or JSON-LD document by **embedding** a proof in it: a `proof`
member carrying the proof's parameters and its value. Every byte-level choice
(transformation, hashing, signing) is delegated to a named cryptographic suite
specified elsewhere. It is the other half of `w3c-vc-jose-cose`: that document
wraps a credential in an envelope and signs octets; this one leaves the
credential where it is and signs a transformation of it.

It reaches us in four ways.

1. **R-I-06** (Could): a W3C Verifiable Credential export of part of
   `AuthzCert`. This is the embedding route such an export could take. §6 says
   what it would require.
2. **R-O-05** (proposed, no force). Data Integrity is the counter-example to
   every clause of it, written as a Recommendation with its costs stated. §5.
3. **DEC-002, accepted by ADR-0004, and MD-3.** The source's whole design is a
   canonicalisation choice, so `docs/extraction.md`'s rule for signing
   documents applies: map it member by member and say where it cuts against
   option 5. §4.
4. **mofn report R-0006** leaves open whether VC Data Integrity runs a
   canonicaliser during verification. This record answers it (§5.3).

What it is not: an exchange protocol, a trust model, a status mechanism, a key
format or a cryptosuite. Multikey, JsonWebKey and verification-method retrieval
belong to Controlled Identifiers 1.0; the EdDSA, ECDSA and BBS suites are
separate Recommendations. The library holds none of them (`record.yaml` `cites`
lists their titles only).

**Things to hold while reading.**

1. **What binds.** The source's own rule:

<!-- q L165 -->
> As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

→ no requirement or candidate carries these words

   The HTML was measured over its 63 `section` elements: §1, §1.1, §1.2 and
   Appendices A, B and C carry class `informative`; §4.1, §4.2, §4.6 and §4.7
   carry class `normative`; the rest carry neither and are normative by the
   rule above. So the Security, Privacy and Accessibility Considerations (§5 to
   §7) are normative text, though they contain no BCP 14 keyword: they urge
   and advise rather than require. Notes and examples are non-normative
   wherever they sit.
   `bin/bcp14-count` finds 106 keywords in the `.txt`. The requirements are
   `requirements.yaml`'s, which pass 1 of this file did not read. **The verify
   pass joined every source quotation to the ids that carry its words**, by
   script against `requirements.yaml` (289 entries at that pass; pass 3 restored the withdrawn R-0054, which none of this file's quotations maps to, so 290): the `→` line under each
   quotation names them; where no requirement exists it names the rejected
   candidate or the non-normative status, or says that nothing carries the
   words (39 joined, 11 candidates only, 4 non-normative, 12 carried by
   nothing, of 66). A bare `R-0006` here is mofn report
   R-0006, written `mofn R-0006`; this record's own ids are written in full.
2. **Quotations are by reference, never typed.** A quotation of the source is a
   `<!-- q Lx-y -->` marker rendered by `bin/check-quotes --render` from
   `.cache/w3c-vc-data-integrity-1-0.txt` (1243 lines, sha256
   `2b7725f80e138ef943eff25050eee6a62f8887762ca9e1e03867c55ea5647beb`,
   rendered by the lane's `render_w3c.py`, one line per HTML block). A
   quotation of one of our documents is a `<!-- qm PATH Lx-y -->` marker:
   `PATH` is a file of the m-of-n repository at commit **`a56a3c0`**
   (2026-11-06), and the words are lines x to y of `git show a56a3c0:PATH`,
   whitespace collapsed, with a markdown blockquote margin (`> `) dropped. A
   pass script rendered them and checks each against **its own file only** —
   never another file, never this record. `bin/check-quotes` cannot see a `qm`
   marker. Optional anchors (`"starts" .. "ends"`) select a sub-span in both
   kinds. Names in backticks (`proofValue`, `eddsa-jcs-2022`) are identifiers,
   not quotations.
3. **Locators.** `§n` is the heading as the `.txt` prints it; `Lnnn` is the
   `.txt` line, which is exact. `step n` and `step n.m` are the items of a
   section's numbered algorithm as the HTML numbers them (checked against the
   HTML `ol` elements: 54 items over §4.1 to §4.6). A property of §2.1's
   definition list is named by its term (`§2.1 verificationMethod`). **No ¶
   counts are used:** a line number is exact, and a paragraph count would be a
   second convention to get wrong.
4. **Our decisions, and their standing at `a56a3c0`.**

   | name | path at a56a3c0 | standing |
   |---|---|---|
   | ARCH-0001 v0.1.8 | `spec/ARCH-0001-authorization-attestation.md` | draft. §5 R-M, R-I, R-O rows; §6 matrix; §7: DEC-002 and DEC-003 accepted, DEC-001, DEC-004, DEC-005 open |
   | proposal | `spec/ARCH-0001-PROPOSAL-v0.2.0.md` | proposed, nothing accepted. Source of R-O-05 |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P2, P3, P5 with P5.1 and P5.2, P6 accepted (ADR-0002); P1.1, P4, P7 draft |
   | ADR-0001 | `spec/ADR-0001-key-relative-naming.md` | accepted 2026-09-22 |
   | ADR-0002 | `spec/ADR-0002-provisional-principles.md` | accepted 2026-11-06, `reviewed: false` |
   | ADR-0003 | `spec/ADR-0003-ksa-core-decisions.md` | accepted 2026-10-14; the SPECs govern where they differ from an ARCH |
   | ADR-0004 | `spec/ADR-0004-dec-002-encoding.md` | accepted 2026-10-25, `reviewed: false`; DEC-002 option 5 |
   | ADR-0005 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted 2026-10-25, `reviewed: false`; DEC-003 |
   | SPEC-0001 v0.1.0, SPEC-0002 v0.5.0 | `spec/SPEC-0001-ksa-architecture.md`, `spec/SPEC-0002-ksa-core.md` | drafts; govern under ADR-0003 |
   | ARCH-0003 | `spec/ARCH-0003-wallet-object-model.md` | draft |
   | DECISIONS-0001 v0.5.0 | `project/DECISIONS-0001.md` | the register |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing, closed by ADR-0004 |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft; evidence, decides nothing |
   | CONTRIBUTING | `CONTRIBUTING.md` | process; §5 |

   **Moved since the sibling's pin.** `w3c-vc-jose-cose/distilled/design-notes.md`
   read our decisions at `db472d2` (2026-11-02). Between that and `a56a3c0`,
   ADR-0002 was accepted, so **P5.1 and P5.2 are now accepted** where the
   sibling mapped them as drafts; ARCH-0001 went from 0.1.6 to 0.1.8 and
   SPEC-0002 from 0.3.0 to 0.5.0, with no change that this file's mapping
   depends on. The register records the acceptance:

<!-- qm project/DECISIONS-0001.md L80 "P2, P3, P5 (with P5.1, P5.2) and P6 are normative" .. "stay draft." -->
> P2, P3, P5 (with P5.1, P5.2) and P6 are normative; P4 and P7 stay draft.

   **`docs/extraction.md` is stale on one point**, as the sibling found: its
   MD-3 paragraph says no DEC-002 ADR exists, and at `a56a3c0` ADR-0004 is
   that ADR. This file maps against ADR-0004 and still records where the
   source cuts against option 5, which is what the rule is for. `docs/` is not
   edited here.
5. **Labels.** *(inferred)* marks what the source implies rather than states,
   and every consequence drawn here. **Ours** marks the library's proposal.
   **[outside this source]** marks a statement resting on a document the source
   cites and the library does not hold (the cryptosuites, Controlled
   Identifiers 1.0, VC Extensions), or on the VC Data Model, which this PR
   extracts in `w3c-vc-data-model-2-0` and this file did not read. Such a
   statement is never quoted and never the sole ground of a verdict.
6. **Numbering.** `R-M-NN`, `R-I-NN` and `R-O-NN` are ARCH-0001 §5, except
   R-O-05, a proposal §7 row. `P1` to `P7`, `P1.1`, `P5.1` and `P5.2` are
   ARCH-0002. `MD-n` are dated meeting decisions; `DL-NNNN` are design-log
   entries. "Condition (n)" is one of mofn report R-0006 §3.2's six. `V1` to
   `V9` are SPEC-0002 §9.2's steps; `TV-n` its vectors. Sections of this file
   are written "§6 below"; a bare `§n` is the source's.

---

## 1. What we adopt

### A1. A dropped datum is an error, not a warning

The source overrides JSON-LD's tolerance, whose processors warn rather than
fail on an undefined term (§2.4.3, L450):

<!-- q L451 "This specification requires" .. "expectations of developers." -->
> This specification requires that any recoverable loss of data when performing JSON-LD transformations result in an error, to avoid a mismatch in the security expectations of developers.

→ `w3c-vc-data-integrity-1-0#R-0140`

<!-- q L452 -->
> Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.

→ `w3c-vc-data-integrity-1-0#R-0141`, `w3c-vc-data-integrity-1-0#R-0142`

and at the conformance level:

<!-- q L169 "Conforming processors MUST" .. "consumed." -->
> Conforming processors MUST produce errors when non-conforming documents are consumed.

→ `w3c-vc-data-integrity-1-0#R-0001`

Ours, P5 (accepted):

<!-- qm spec/ARCH-0002-key-relative-naming.md L391-396 "**All three are required." .. "other way round." -->
> **All three are required. None may be skipped, and a failure at any level is a rejection, never a repair.** Beyond the three: **an unknown field in a signed payload is an error, not something to skip.** The default is must-understand; skippability is opt-in and explicit, never the other way round.

and SPEC-0002 §13.5:

<!-- qm spec/SPEC-0002-ksa-core.md L847-849 "an unknown kind or field is invalid." .. "(ARCH-0002 P5)." -->
> an unknown kind or field is invalid. A verifier MUST NOT skip what it does not understand (ARCH-0002 P5).

**The same principle, reached from the canonicaliser's side (inferred).** P5
says a field nobody understands is an error; §2.4.3 says a field the
canonicaliser would silently drop is an error. **Consequence for an export
(§6 below):** every member we emit is defined by a context we publish, or the
document fails at every conforming JSON-LD processor that secures or verifies
it. Two places the source departs from P5 are rejected in §3 (R2, R3).

### A2. Hand the application only what the verifier returns

<!-- q L734 -->
> Implementers and developers are urged to not trust information that contains a data integrity proof unless the proof has been verified and the verified data is provided in a return value from a software library that has confirmed that all data returned has been successfully protected.

→ no requirement: candidate C-0144 (reject)

The cryptosuite's result carries that document (§3, L506):

<!-- q L506 -->
> A map that represents the secured data document with the verified proofs removed if verified is true, or null otherwise.

→ `w3c-vc-data-integrity-1-0#R-0158`

Ours: SPEC-0002 decodes only after the signature verifies, and its human form
is a view of the bytes, never itself signed:

<!-- qm spec/SPEC-0002-ksa-core.md L680-681 "The human form is never itself signed or hashed" .. "exact view of them." -->
> The human form is never itself signed or hashed — the bytes are the statement, and the YAML is an exact view of them.

**Same intent, different object (inferred).** Under a suite that canonicalises
to N-Quads, the returned map's JSON details (member order, compaction, number
spelling) are not what was signed:

<!-- q L731 "The data that is protected" .. "the transformed data." -->
> The data that is protected by any data integrity proof is the transformed data.

→ `w3c-vc-data-integrity-1-0#R-0281`

So an import (open question 4) reads a credential's claims from the verifier's
returned document **after** context validation (§2.4.1), never from the
received bytes, and never from JSON details the transformation discards.

### A3. A vocabulary at the boundary is pinned by hash

<!-- q L406 -->
> Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:

→ `w3c-vc-data-integrity-1-0#R-0124`

<!-- q L429 -->
> Implementations MAY load application-specific JSON-LD context files from the network during development, but SHOULD permanently cache JSON-LD context files used by conforming secured documents in production settings, to increase their security and privacy characteristics. Goals of processing speed MAY be achieved through caching approaches such as those described above or functionally equivalent mechanisms.

→ `w3c-vc-data-integrity-1-0#R-0137`, `w3c-vc-data-integrity-1-0#R-0138`, `w3c-vc-data-integrity-1-0#R-0028`

<!-- q L435 "Applications MUST use the algorithm" .. "Verify Proof Sets and Chains." -->
> Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document. Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.

→ `w3c-vc-data-integrity-1-0#R-0029`, `w3c-vc-data-integrity-1-0#R-0030`

Ours, ARCH-0001 §6's W3C VC row and R-I-06:

<!-- qm spec/ARCH-0001-authorization-attestation.md L356 "W3C VC |" .. "must be pinned" -->
> W3C VC | I | C | ArtifactStatement or NameCert depending on type | Context must be pinned

<!-- qm spec/ARCH-0001-authorization-attestation.md L318 "Export a subset" .. "documented context." -->
> Export a subset of `AuthzCert` as a W3C Verifiable Credential using a documented context.

**Adopted for the export.** Our context is a static, versioned file whose
SHA-256 we publish, exactly as the source prints its own three (L407 to L413).
Its terms are `@protected`: §3 requires that only of a cryptosuite's context
(L511); for ours it is a choice. Measured: the VC Data Model v2 base context
(`https://www.w3.org/ns/credentials/v2`, fetched 2026-11-07, 10131 octets,
sha256 `59955ced6697d61e03f2b2556febe5308ab16842846f5b586d7f1f7adec92734`)
is `@protected` at the top level, defines `proof` inside `VerifiableCredential`
as a graph container (`@container` `@graph`), and defines `DataIntegrityProof`
with a scoped, `@protected` context defining all twelve §2.1 properties
(`challenge`, `created`, `cryptosuite`, `domain`, `expires`, `id`, `nonce`,
`previousProof`, `proofPurpose`, `proofValue`, `type`, `verificationMethod`).
So an export under that context needs no injected Data Integrity context,
which §2.4.2 allows:

<!-- q L445 -->
> When an application is securing a document, if an @context property is not provided in the document or the Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations SHOULD inject or append an @context property with a value of https://w3id.org/security/data-integrity/v2 or one or more contexts with at least the same declarations, such as the Verifiable Credential Data Model v2.0 context (https://www.w3.org/ns/credentials/v2).

→ `w3c-vc-data-integrity-1-0#R-0032`

The vocabulary trust model behind A3 is **not** adopted; see R4.

### A4. A set of proofs is not a threshold

<!-- q L871 "A holder or any other intermediary" .. "will still verify." -->
> A holder or any other intermediary receiving a secured data document containing a proof set is able to remove any of the proof values within the set prior to passing it on to another entity and the secured data document will still verify.

→ non-normative text (no requirement): Appendix A

That is Appendix A, non-normative. The normative §4.5 permits the same:

<!-- q L618 "Other approaches are possible" .. "also considered verified." -->
> Other approaches are possible, particularly if it is only desired to verify a subset of the proofs contained in allProofs. If another approach is taken to verify only a subset of the proofs, then it is important to note that any proof in that subset with a previousProof can only be considered verified if the proofs it references are also considered verified.

→ `w3c-vc-data-integrity-1-0#R-0239`, `w3c-vc-data-integrity-1-0#R-0240`

Ours, mofn report R-0006 §5.1, reasoning from DSSE:

<!-- qm research/0006-mechanism/report.md L1227-1231 "under **every** DEC-002 option" .. "unsafe to infer**." -->
> under **every** DEC-002 option, `k` and the member set must travel **inside the signed payload**. And because the envelope is declared equivalent to separate envelopes, an intermediary may legitimately split or merge them — so threshold meaning inferred from signature count is not merely absent but **unsafe to infer**.

**A second source for the same result.** A proof set is n independent sayings,
any of which an intermediary may drop. KSA already carries `k` and the member
set inside the truster's signed statement (SPEC-0002 §8.6, the threshold form;
TV-9 to TV-11). **Consequence:** an export never encodes a threshold as a proof
set, and an import never infers one from proofs (§6.2 below drops it). R-M-06's
interchange story is unchanged by this source.

### A5. Purpose and audience are bound inside what is signed

<!-- q L372 "Proof purposes are expressions" .. "does not." -->
> Proof purposes are expressions on why a proof was created and its intended domain of usage whereas the other mechanisms mentioned are intended to limit what a private key can be used to do. A proof purpose "travels" with the proof while a key restriction does not.

→ no requirement: candidate C-0039 (reject), candidate C-0040 (reject)

<!-- q L181 "The protected declaration" .. "intended for." -->
> The protected declaration acts as a safeguard to prevent the proof from being misused for a purpose other than the one it was intended for.

→ no requirement: candidate C-0013 (reject)

§4.4 steps 5 to 7 (L604 to L606) reject a proof whose purpose, `domain` or
`challenge` differs from what the verifier expected. Ours: a DS label in every
signature input, and a presentation's audience and nonce:

<!-- qm spec/SPEC-0002-ksa-core.md L358-359 -->
> A DS label is a fixed ASCII string followed by one zero octet. It is prepended to the bytes being signed and is never transmitted.

<!-- qm spec/SPEC-0001-ksa-architecture.md L326-327 "A relying party that supplied a nonce" .. "its own kid." -->
> A relying party that supplied a nonce MUST check that the presentation carries it and that `audience` is its own kid.

**Corroboration, nothing to change.** `proofPurpose` is our DS label's job
(statement or proof of possession), and `domain` plus `challenge` are
SPEC-0001 §8.1's `audience` plus `nonce`. How the source protects the purpose
is the cryptosuite's business [outside this source]; ours is the signature
input itself. An export sets `proofPurpose` to `assertionMethod` and emits no
`domain` or `challenge`: it exports credentials, not presentations.

### A6. A proof's time is not the statement's validity

<!-- q L485 "Document authors and implementers" .. "validUntil properties." -->
> Document authors and implementers are advised to understand the difference between the validity period of a proof, which is expressed using the created and expires properties, and the validity period of a credential, which is expressed using the validFrom and validUntil properties.

→ no requirement: candidate C-0067 (reject)

Ours, SPEC-0002 §7.3:

<!-- qm spec/SPEC-0002-ksa-core.md L434 "`issued` is the speaker's statement" .. "when it signed." -->
> `issued` is the speaker's statement of when it signed.

**Consistent with the sibling's adopt 4.** On export, `created` is the export
signature's time, `expires` (if present) bounds that proof only, and the
statement's `not-before` and `not-on-or-after` become `validFrom` and
`validUntil` [outside this source]. The KSA `issued` is a second signer's
time and is not carried (§6.2 below).

### A7. A canonicaliser is cited, never invented

<!-- q L494 -->
> The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.

→ `w3c-vc-data-integrity-1-0#R-0039`

<!-- q L774 "Proper vetting includes" .. "is preferred." -->
> Proper vetting includes, at a minimum, association with a peer reviewed mathematical proof of algorithm correctness; multiple implementations and vetting by experts in a standards setting organization is preferred.

→ no requirement or candidate carries these words

Ours, R-O-03:

<!-- qm spec/ARCH-0001-authorization-attestation.md L327 "Canonicalization algorithm" .. "invented silently." -->
> Canonicalization algorithm for each concrete encoding SHALL be cited, not invented silently.

**Adopted as stated.** Every transformation the source names is a cited
Recommendation or RFC: RDF Dataset Canonicalization (`w3c-rdf-canon-1-0`) and
RFC 8785 (`rfc-8785`), both held. **A consequence for a JCS export
(inferred):** mofn report R-0006 §3.4 found RFC 8785's number algorithm
outside the cited document, and located its worked hazards in doubles beyond
the safe-integer range, in negative zero, and in numbers carried as strings.
KSA's data model has no floating-point value and keeps its integers inside
that range:

<!-- qm spec/SPEC-0002-ksa-core.md L181 "in the range" .. "inclusive" -->
> in the range −(2^53 − 1) … 2^53 − 1 inclusive

so a JSON document translated from a KSA statement carries only integers that
every IEEE 754 double represents exactly, none of them negative zero, and no
JCS number hazard mofn R-0006 lists can arise in it. Times go out as
`dateTimeStamp` strings in any case (§2.1).

### A8. A suite fixes the parameters; developers pick a suite

<!-- q L697 "Cryptographic library implementers are advised" .. "these pre-sets." -->
> Cryptographic library implementers are advised to, if possible, provide known good combinations of options and parameters to application developers. There would ideally be two pre-set default configurations for any algorithmic class, such as Elliptic Curve Digital Signatures, with no ability to fine tune parameters and options when using these pre-sets.

→ no requirement or candidate carries these words

§3's list of what every suite specification MUST detail (L492 to L511), and
§5.5's single opaque `proofValue` (L719, L720), are SPEC-0002 §6.1's table in
other words. **Corroboration, nothing to change.** One place the source's
suites do not fix their parameters is rejected in R5.

---

## 2. What we adapt, and how

### B1. Signer and speaker are one key, so an import checks the binding

The source makes the binding a use case, not a rule:

<!-- q L483 "Implementers that are addressing" .. "those types of documents." -->
> Implementers that are addressing those use cases are cautioned that additional checks might be appropriate when processing those types of documents.

→ no requirement or candidate carries these words

<!-- q L484 "One way to check" .. "given the proof's purpose." -->
> One way to check for such an association is to ensure that the value of the controller property of a proof's verification method matches the URL value used to identify the issuer or holder, respectively, and that the verification method is expressed under a verification relationship that is acceptable given the proof's purpose.

→ no requirement: candidate C-0066 (reject)

Ours, P2 (accepted):

<!-- qm spec/ARCH-0002-key-relative-naming.md L146-148 "Per SDSI and SPKI" .. "saying meaningful." -->
> Per SDSI and SPKI, **the speaker is the key.** There is no separate notion of "who signed this" versus "who said it", and no authority above A that makes A's saying meaningful.

**Adaptation (ours):** an importer requires §2.6's check, never treats it as
optional: the proof's verification method must belong to the credential's
issuer, under `assertionMethod`. A credential that verifies and fails the check
is not imported as a statement by its issuer. On export the binding holds by
construction, since the issuer is the export key's controller (§6.2 below).
That narrows what the source leaves open, so the verdict is **constrains**.

### B2. Resolve verification methods from the key store, never the network

<!-- q L211 "Note that when verificationMethod" .. "the verification method." -->
> Note that when verificationMethod is expressed in a data integrity proof, the value points to the actual location of the data; that is, the verificationMethod references, via a URL, the location of the public key that can be used to verify the proof. This public key data is stored in a controlled identifier document, which contains a full description of the verification method.

→ `w3c-vc-data-integrity-1-0#R-0091`, `w3c-vc-data-integrity-1-0#R-0092`

<!-- q L778 "This specification is designed in such a way" .. "conforming secured document." -->
> This specification is designed in such a way that no network requests are required when verifying a proof on a conforming secured document.

→ no requirement: candidate C-0163 (reject)

<!-- q L780 -->
> When it is not possible to use cached information, such as when a specific HTTP URL-based instance of a verification method is encountered for the first time, implementers are cautioned to use defensive measures to mitigate denial-of-service attacks during any process that might fetch a resource from the network.

→ no requirement or candidate carries these words

Ours, SPEC-0002 §10:

<!-- qm spec/SPEC-0002-ksa-core.md L651-653 "A key MUST NOT be" .. "a `rotate` names it." -->
> A key MUST NOT be added because a statement merely names it, because it appears as an envelope `pub` on a statement of another kind, or because a `rotate` names it.

**Adaptation (ours):** an import resolves `verificationMethod` only against
keys already in the key store, or against a form that carries the key itself
(open question 2). It never fetches. Fetching on first encounter, which L780
contemplates, would add a key because a document named it.

### B3. Verify first, then validate the schema

The source's receiving order (§4.1, steps 1 to 4):

<!-- q L542-545 -->
> The software transforms the incoming data into a document that can be understood by the applicable algorithm provided in Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains. The software uses JSON Schema or an equivalent mechanism to validate that the incoming document follows an expected schema used by the application. The software uses the applicable algorithm(s) provided in Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains to verify the integrity of the incoming document. If the document is a JSON-LD document, the software uses the algorithm provided in Section 4.6 Context Validation, or one providing equivalent protections, to validate all JSON-LD Context values used in the document.

→ `w3c-vc-data-integrity-1-0#R-0174`, `w3c-vc-data-integrity-1-0#R-0175`, `w3c-vc-data-integrity-1-0#R-0176`, `w3c-vc-data-integrity-1-0#R-0177`

Ours, SPEC-0002 §9.2's order (V4 signature before V5 decoding and V7
structure) and §13.6:

<!-- qm spec/SPEC-0002-ksa-core.md L855 "It MUST bound the work" .. "V4 succeeds." -->
> It MUST bound the work it performs on any input before V4 succeeds.

**Adaptation (ours):** run §4.1's receiving steps as 1, 3, 2, 4. Step 2 before
step 3 carries no keyword, so the reordering conforms (inferred). The
requirements file records the §4.1 steps as binding text all the same
(`w3c-vc-data-integrity-1-0#R-0174` to `#R-0177`, `verb: none`, made binding
by §4 ¶2, `w3c-vc-data-integrity-1-0#R-0169`), and §4.1 is one of the four
sections the HTML marks `normative`; whether their order binds neither
settles, so the reordering is a reading, recorded as one. Context
validation stays after verification, where L435 requires it. **What cannot be
reordered** is inside step 3: §4.4 parses before it verifies, and a suite that
canonicalises to N-Quads expands the document under its contexts before the
signature is checked. That is §5 below.

### B4. Map the source's outcomes onto our three results

<!-- q L599 -->
> When a step says "an error MUST be raised", it means that a verification result MUST be returned with a verified value of false and a non-empty errors list.

→ `w3c-vc-data-integrity-1-0#R-0218`

<!-- q L507 "If an error is produced" .. "would fail." -->
> If an error is produced, the verification process failed to complete. An error, such as a network error, does not mean that a future attempt at verification would fail.

→ `w3c-vc-data-integrity-1-0#R-0159`, `w3c-vc-data-integrity-1-0#R-0160`

Ours, SPEC-0002 §9.1:

<!-- qm spec/SPEC-0002-ksa-core.md L614-615 "**invalid**" .. "no key for `says`" -->
> **invalid** | it is malformed, or its signature does not verify; it MUST NOT be used | | **unverifiable** | it may be valid, but this verifier cannot tell: unsupported suite, or no key for `says`

**Adaptation (ours):** §4.4's result folds an error into `verified: false`, so
an importer classifies by error type. `PROOF_VERIFICATION_ERROR`,
`INVALID_DOMAIN_ERROR` and `INVALID_CHALLENGE_ERROR` are **invalid**; a
cryptosuite the importer does not support, or a failure L507 says may not
recur, is **unverifiable**; a data-loss error is **invalid** (A1). Two of the
error types the algorithms raise are not defined where §4.7 defines the others
(§9 below, D5), so the mapping names them by the algorithm that raises them.

### B5. Under a JCS suite, carry type identity inside the signed JSON

The source's own guidance on choosing a transformation:

<!-- q L765-766 -->
> If an application only uses JSON and does not depend on any form of RDF semantics, then using a cryptography suite that uses JSON Canonicalization Scheme [RFC8785] is an attractive approach. If an application uses JSON-LD and needs to secure the semantics of the document, then using a cryptography suite that uses RDF Dataset Canonicalization [RDF-CANON] is an attractive approach.

→ no requirement: candidate C-0158 (reject), candidate C-0159 (reject)

Ours, ADR-0003 D1, and P1:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L47 "**Type identity is key-relative and hash-identified." .. "that definition's definer." -->
> **Type identity is key-relative and hash-identified.** A type is identified by the `DefinitionId` — the hash of its definition's canonical encoding — and a label local to that definition's definer.

<!-- qm spec/ARCH-0002-key-relative-naming.md L67 "An extension point is a pair" .. "label)`**." -->
> An extension point is a pair: **`(defining key, local label)`**.

**The gap (inferred).** Under a JCS suite the signature covers the JSON text,
`@context` URL strings included, but not the documents those URLs name. What a
compacted term means to a JSON-LD consumer then rests on the verifier pinning
the context (A3), not on the signature. Under a suite that canonicalises to
N-Quads the expanded IRIs are what is signed. **Adaptation (ours):** whichever
suite an export uses, the DefinitionId and label of every exported type appear
in the signed JSON itself, as expanded IRIs or as members. Type identity is
then authenticated whatever a verifier does with contexts.

### B6. The export key is not the statement key

§3's list of what a suite specification MUST detail (L492 to L511) names no
domain separation. Ours, SPEC-0002 §13.2, whose guarantee has a proviso:

<!-- qm spec/SPEC-0002-ksa-core.md L824-826 "A key that is" .. "domain-separates." -->
> A key that is also used in another protocol cannot have a KSA signature replayed there, or a signature from there replayed as KSA, provided that protocol also domain-separates.

<!-- qm spec/SPEC-0001-ksa-architecture.md L226-227 "A wallet SHOULD use a separate key" .. "outside KSA." -->
> A wallet SHOULD use a separate key per protocol — derived from one seed where convenient — and MUST record on the key any use outside KSA.

**Adaptation (ours), as in the sibling's adapt 4:** a separate suite-1 key of
the persona signs the export, recorded as SPEC-0001 §5.3 requires, because this
source does not promise the proviso. Whether a given suite domain-separates is
that suite's matter [outside this source]. SPEC-0002 §12.7 has no usage code
for it (open question 7).

---

## 3. What we reject, and why

### R1. Verifying by re-canonicalising, inside our verifier

The source's verification, non-normatively:

<!-- q L140 -->
> To verify a cryptographic proof, the following steps are performed: 1) Transformation, 2) Hashing, and 3) Proof Verification.

→ non-normative text (no requirement): §1.1–§1.2

<!-- q L142 -->
> During verification, the transformation and hashing steps are conceptually the same as described above.

→ non-normative text (no requirement): §1.1–§1.2

Ours, ADR-0003's rejected alternative and SPEC-0002 §5 and §13.1:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L62-63 "**Sign a re-encoded statement." .. "(R-O-05)." -->
> **Sign a re-encoded statement.** It makes the verifier canonicalise during verification and run its decoder on unauthenticated input (R-O-05).

<!-- qm spec/SPEC-0002-ksa-core.md L284-289 "**Why carry the signed bytes" .. "(ARCH-0001 R-O-05)." -->
> **Why carry the signed bytes, rather than signing a re-encoded statement?** Because otherwise a verifier would have to decode, remove the signature, and re-encode before it could check it — canonicalising during verification, exposing its decoder to unauthenticated input, and creating a second encoder whose output must match the producer's byte for byte. Carrying the signed bytes intact removes all three (ARCH-0001 R-O-05).

**Rejected natively, as ADR-0003 already did.** This source is that rejected
alternative, built and standardised, with the mitigations it needs written
down (§5.2 below). Whether a Data Integrity credential may be imported at all,
and verified where, is open question 4; §5 below is the analysis.

### R2. The licence to repair a malformed time

<!-- q L215 "A conforming processor MAY chose" .. "interpreted as UTC." -->
> A conforming processor MAY chose to consume time values that were incorrectly serialized without an offset. Incorrectly serialized time values without an offset are to be interpreted as UTC.

→ `w3c-vc-data-integrity-1-0#R-0010`, `w3c-vc-data-integrity-1-0#R-0099`

§2.1 `expires` (L217) repeats it. Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L243 "Any other spelling" .. "not normalised." -->
> Any other spelling MUST be rejected, not normalised.

**Rejected, as a MAY declined.** Our importer rejects a `created` or `expires`
without an offset; our exporter always writes `Z`. No conformance is lost: the
source permits the repair and does not require it.

### R3. Recompacting a document whose contexts are unknown

<!-- q L653 -->
> If recompact is true, set result.validatedDocument to the result of running the JSON-LD Compaction Algorithm with the inputDocument and knownContext as inputs. If the compaction fails, add at least one error to result.errors.

→ `w3c-vc-data-integrity-1-0#R-0269`

**Rejected:** our importer runs §4.6 with `recompact` false, so an unknown
context is an error (step 3.2, L654). Turning unknown terms into full IRIs
makes them visible, not understood, and P5 (A1) asks for understanding.

### R4. Unsigned vocabulary documents, trusted by allow-list

The source's context validation trusts a context because its bytes match a
known value (§4.6 step 3, L652; §2.4.1, L438 and L439). Ours, ADR-0003:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L66-67 "**Unsigned vocabulary documents." .. "`define` statement." -->
> **Unsigned vocabulary documents.** Whether to rely on a vocabulary would not be a trust question; KSA publishes definitions with a signed `define` statement.

**Rejected as our vocabulary model; used at the boundary.** A foreign verifier
pins our published context by hash (A3), because that is the mechanism it has.
Our importer does not trust a VC's vocabulary because its context hashes to a
listed value. It maps the VC's terms to KSA definitions through the interchange
profile (R-I-01), and the definitions are trusted through `define` statements
and trust evaluation.

### R5. A suite whose curve and hash come from the key's format

<!-- q L707 "it has only two cryptosuite names" .. "used in validation." -->
> it has only two cryptosuite names: ecdsa-rdfc-2019 and ecdsa-jcs-2019. The security level and corresponding curves and hashes are determined from the multi-key format of the public key used in validation.

→ no requirement: candidate C-0124 (reject)

Ours, SPEC-0002 §6.1:

<!-- qm spec/SPEC-0002-ksa-core.md L311 -->
> A statement's suite is inside its TBS and is therefore covered by its signature.

**Rejected:** one KSA suite code is one key algorithm, one encoding and one
hash, inside the signed bytes. Under the pattern L707 describes, a suite name
covers two parameter sets and the key's format picks one [outside this source:
the Multikey header]. Condition (4)'s authenticated indicator would then name a
family, not a profile. The date-based naming §5.3 recommends (L705) is not
adopted either: our suite names are parametric (`ksa-ed25519-sha256`), and
§5.1's objection to that, that most developers cannot read parameters (L685),
is met by the registry's status column, the single default, and immutability
once SPEC-0002 leaves `0.x` (SPEC-0002 §6.1, §6.2).

### R6. Proof sets and proof chains, on import, this semester

§4.4 verifies a single proof and rejects anything else:

<!-- q L601 -->
> If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.

→ `w3c-vc-data-integrity-1-0#R-0220`, `w3c-vc-data-integrity-1-0#R-0221`

The set and chain algorithms of §4.3 and §4.5 are defective as printed (§9
below, D1 to D4). **Rejected for now:** our import profile accepts a `proof`
that is one map, as §4.4 does. KSA's own chains are separate statements: a
`review` or `approve` targets a statement by its digest (SPEC-0002 §8.10), so
nothing here is lost natively.

### R7. The selective-disclosure and unlinkability suites

<!-- q L820 -->
> If an application uses JSON-LD and might require selective disclosure of information in a secured document, then using a cryptography suite that uses RDF Dataset Canonicalization [RDF-CANON] is an attractive approach.

→ no requirement: candidate C-0191 (reject)

Ours:

<!-- qm spec/ARCH-0003-wallet-object-model.md L783-784 "**Selective disclosure" .. "out of scope this semester." -->
> **Selective disclosure** in presentations (SD-JWT, RFC 9901) — the `disclosure` policy is the hook; out of scope this semester.

<!-- qm spec/SPEC-0001-ksa-architecture.md L90-93 "Out of scope for this version" .. "DEC-009)." -->
> Out of scope for this version: the binary transport codec and fragmentation for constrained links, revocation distribution, selective disclosure, and multi-speaker contracts (ARCH-0002 DEC-009).

**Rejected this semester,** with SD-JWT (the sibling's reject 4) for the same
reason.

---

## 4. MD-3, ADR-0004 and DEC-002

MD-3 reads:

<!-- qm project/meetings/2026-09-28.md L51-53 "CBOR data model" .. "one-way mapping." -->
> CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping.

ADR-0004 accepted DEC-002 for option 5 on 2026-10-25 (ARCH-0001 §7, L375), and
nothing in this section reopens it:

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

The section exists because an extraction that can only confirm is not
evidence, and because ADR-0004 was taken without a second reader. This source
is a signing document but not an envelope document: its proof is a member of
the payload. So the header-by-header mapping `docs/extraction.md` asks for is
member by member, and its result is the same as the sibling's: **an export
mapping with no import into native form.** Nothing in a Data Integrity document
becomes a KSA statement; SPEC-0001 §5.3's external statement is the only route
in (open question 4).

### 4.1 Member by member

| source construct (locator) | our statement or envelope (SPEC-0002) | export mapping | mapping |
|---|---|---|---|
| the secured document, a JSON map with the proof inside it (§2.1 L203; §4 L531) | the TBS, KSA-CBOR, inside `[suite, says, tbs, sig, ? pub]` (§4, §5) | a translation of the statement, written once (§6 below) | **re-encoded and re-signed** |
| `proof`, one map (§4.4 step 2, L601) | `sig`, and the TBS fields that name signer and suite | exactly one proof | **shape only** |
| `proof.type` = `DataIntegrityProof` (§3.1 L519) | none: the envelope carries no type | always `DataIntegrityProof` | **label only** |
| `proof.cryptosuite` (§2.1 L213; §3.1 L521) | `suite`, inside the TBS (§6.1) | the export key's suite name [outside this source] | **not carried** |
| `proof.verificationMethod`, a URL (§2.1 L211) | `says` (a 32-octet `kid`); the envelope's `says` and `pub` hints | a URL form of the export key (open question 2) | **respelled; a locator the verifier dereferences, not a hint** |
| `proof.proofPurpose` (§2.1 L209; §2.2) | the DS label `KSA-STMT-SIG-v1` (§6.4) | `assertionMethod` | **same intent; ours in the signature input** (A5) |
| `proof.created` (§2.1 L215) | `valid.issued`, the speaker's own signing time (§7.3) | the export signature's time, written with `Z` | **export-only** (A6, R2) |
| `proof.expires` (§2.1 L217) | none: validity is the statement's `valid` | omitted, or no later than `not-on-or-after` (ours) | **export-only** |
| `proof.domain`, `proof.challenge` (§2.1 L219, L221) | SPEC-0001 §8.1 `audience`, `nonce`, on presentations | not emitted | — |
| `proof.proofValue`, Multibase (§2.1 L223) | `sig`, 64 octets for suite 1 (§6.3) | the export signature, Multibase-encoded [outside this source] | **re-signed** |
| `proof.id`, `proof.previousProof` (§2.1 L205, L225) | `review` and `approve` targeting a statement digest (§8.10) | not emitted (R6) | — |
| `proof.nonce` (§2.1 L227) | none | not emitted | — |
| `digestMultibase` on an object with an `id` (§2.3 L388) | target type 2, `[2, digest-alg, bytes]` (§7.2) | only for an artifact export, which needs an `id` (row 9 of §7) | **respelled**: SPEC-0002 §12.5's code 1 becomes a Multihash code |
| `@context` (§2 L195; §2.4.2 L445, L446) | `type-ref.definition`, a DefinitionId (§7.4) | the VC DM v2 context and our documented context, both hash-pinned (A3) | **boundary only**; type identity carried in the JSON too (B5) |
| the transformation, JCS or RDFC (§3 L494; §5.7 L731 to L733) | none: the verifier never re-encodes (§3) | by the exporter at authoring; **by every foreign verifier at verification** | **the cost of this route** (§5 below) |
| ProblemDetails error types (§4.7) | reason codes (§12.9) | not emitted | import only (B4) |

**What we deliberately do not carry, and why:** proof sets and chains (A4,
R6); `domain`, `challenge` and `nonce` (A5); a threshold, which the source
cannot express (A4); `may-delegate` (§6.2 below); any member a context does not
define (A1); an offset-less time (R2); the selective-disclosure suites (R7).

### 4.2 Where this source cuts against MD-3, ADR-0004 and option 5, or leaves them underdetermined

#### 1. An embedded proof forces canonicalisation at verification, under every option

The verifier parses the bytes, then hands the cryptosuite a map:

<!-- q L600 -->
> Let securedDocument be the result of running parse JSON bytes to an Infra value on documentBytes.

→ `w3c-vc-data-integrity-1-0#R-0219`

<!-- q L607 -->
> Let cryptosuiteVerificationResult be the result of running the cryptosuite.verifyProof algorithm with securedDocument provided as input.

→ `w3c-vc-data-integrity-1-0#R-0234`

<!-- q L502 "An algorithm that takes a secured data document (map securedDocument) as input" .. "or an error." -->
> An algorithm that takes a secured data document (map securedDocument) as input, and produces a cryptosuite verification result or an error.

→ `w3c-vc-data-integrity-1-0#R-0156`

**So whatever is hashed at verification is produced from the parsed map, that
is, re-encoded (inferred).** The received bytes are gone by step 8. §3 allows a
suite with no transformation at all (L494), but no suite can avoid serialising
the map again. That is structural to
embedding, not to any DEC-002 option, and it is the reason ADR-0004 item 4
names envelopes. **Not a cut against option 5.**

**Where an option would pay less, weakly: option 3.** Under option 3 a JCS
export would share its canonicaliser with the native encoding. Under option 5
the exporter ships a JSON canonicaliser, or a JSON-LD processor and an RDFC
implementation, that the native code never needs: a library cost of this
route that option 3 would not pay. Option 3 is withdrawn:

<!-- qm spec/ADR-0004-dec-002-encoding.md L121-124 "Withdrawn on the four grounds" .. "under R-O-03." -->
> Withdrawn on the four grounds of `DECISIONS-0001` item 2; the strongest is that RFC 8785 §3.2.3 prohibits the array reordering we need, so we would ship a modified JCS — a partly invented algorithm under R-O-03.

and this source corroborates the second of the four grounds rather than
answering it. mofn R-0006 §3.4 described RFC 8785's verification order:

<!-- qm research/0006-mechanism/report.md L462-466 "Applications MUST parse and" .. "then compare." -->
> Applications MUST parse and check I-JSON, verify correctness and locate the signature property, and only then verify the signature. Appendix F spells out the same scheme: parse, save the signature value, **remove** the signature property, re-serialise, re-canonicalise, then compare.

A JCS suite here is that scheme, deployed (inferred from L502, L600, L607 and
L732). **A cost, not a reason to reopen.**

#### 2. Serialisation flexibility is a driver ADR-0004 never scored

<!-- q L159 "This specification enables" .. "regenerate the cryptographic proof." -->
> This specification enables one to create cryptographic proofs that are not bound to the original document syntax, which enables more advanced use cases such as being able to use a single digital signature across a variety of serialization syntaxes such as JSON and CBOR without the need to regenerate the cryptographic proof.

→ non-normative text (no requirement): §1.1–§1.2

<!-- q L724 "This enables the same digital signature" .. "for every syntax." -->
> This enables the same digital signature over the information to be expressed in JSON, CBOR, YAML, and other compatible syntaxes without having to create a cryptographic proof for every syntax.

→ no requirement or candidate carries these words

<!-- q L725 "This leads to double-storing data" .. "database drift over time." -->
> This leads to double-storing data and can lead to increased security attack surface if the unsigned representation stored in databases accidentally deviates from the signed representation. By using transformations, the digital proof can live in the native data format to help prevent otherwise undetectable database drift over time.

→ no requirement or candidate carries these words

Ours, ADR-0004's rejection of option 4:

<!-- qm spec/ADR-0004-dec-002-encoding.md L125-126 "Two canonical forms" .. "does not meet." -->
> Two canonical forms and a bijection nobody has specified, for no driver the single form does not meet.

**The source names a driver ADR-0004 does not list, and meets it by
canonicalising to a third form at verification (inferred).** Option 5 does not
meet it: a KSA statement verifies only as its TBS, and MD-3's YAML form is a
view regenerated from those bytes (SPEC-0002 §11.1), so one signature never
spans two syntaxes. This names **option 4, and the canonicalising route,
weakly**: option 4 wanted two syntaxes through a bijection nobody specified,
and this source gets them through N-Quads, at a price ADR-0003 refuses (R1).
Our answer to the drift argument of L725 is SPEC-0002 §11.1's one-to-one rule:
store the bytes, regenerate the view. **A cost option 5 pays, and not a reason
to reopen** while ADR-0003's rejected alternative stands.

#### 3. ADR-0004 item 4 names envelopes, and this source is not one

<!-- qm spec/ADR-0004-dec-002-encoding.md L51-52 "**COSE_Sign1 and DSSE are export envelopes only." .. "does not decide." -->
> **COSE_Sign1 and DSSE are export envelopes only.** *Which* envelope remains DEC-005, which this ADR does not decide.

<!-- qm spec/ARCH-0001-authorization-attestation.md L485-487 "DEC-005" .. "payload schema." -->
> DEC-005 — Envelope for ArtifactStatement Options: DSSE (in-toto world), COSE_Sign1 (SCITT world), both with a single unsigned payload schema.

**Underdetermined, and the pressure is on DEC-005, not DEC-002.** Read as the
set of export mechanisms, item 4 excludes this route outright; read as a rule
about those two envelopes, it says nothing about an embedded proof. DEC-005 is
the envelope for `ArtifactStatement`, so nothing decides how R-I-06's
`AuthzCert` export is secured (the sibling's open question 1), and this source
shows the gap is wider than a choice between envelopes. Open question 1.

#### 4. ADR-0004 item 3 lists IANA registries, and this source's allocators are not IANA's

<!-- qm spec/ADR-0004-dec-002-encoding.md L46-50 "**No IANA registry is native." .. "lossily per R-I-01." -->
> **No IANA registry is native.** Named, because "no tags" was too narrow (`ARCH-0001` §7, inputs since v0.1.3): the native model depends on none of CBOR Tags, COSE Header Parameters, COSE Algorithms, CWT Claims, or CWT Confirmation Methods. Each may appear at an interchange boundary, mapped lossily per R-I-01.

What a Data Integrity export signs or carries names, from central allocators:
Security Vocabulary IRIs under `https://w3id.org/security#` (L415); the
context URLs and their digests (L406 to L413); cryptosuite names, whose
instantiation algorithms SHOULD be listed in the VC Extensions document (L498);
a Multibase header on `proofValue` (L223); and, on `digestMultibase`, a
Multihash code (L388; Example 8's value decodes from the HTML to 34 octets
opening `12 20`). The example keys carry a header too: decoded from the HTML,
`z6MkjLrk…` (Examples 2, 6, 7) is 34 octets opening `ed 01`, and `zDnaep…`
(Examples 4, 5) 35 octets opening `80 24` [what the headers mean is outside
this source]. Ours:

<!-- qm spec/ADR-0001-key-relative-naming.md L34-35 "The native model depends on no centrally allocated" .. "for their meaning." -->
> The native model depends on no centrally allocated registry for their meaning.

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L71 "the key type is named by a multicodec code" .. "by our reading of P1" -->
> the key type is named by a multicodec code, from a registry maintained outside the project — a registry in the identifier, by our reading of P1

<!-- qm spec/ADR-0001-key-relative-naming.md L55-56 "Registry identifiers" .. "per R-I-01." -->
> Registry identifiers **may** appear at interchange boundaries, and such mappings are documented as lossy per R-I-01.

**Underdetermined.** P1 excludes every central allocator, and ADR-0005 counts
multiformats as one; item 3's heading and list are IANA's alone. At the
boundary all of these are permitted, mapped lossily, so nothing conflicts. But
an R-I-01 table for this route must name them itself, as the sibling found for
the JOSE registries. Open question 10.

#### 5. Order-only divergence: invisible here by design

<!-- q L732 "One benefit of this approach is that adding or removing formatting characters" .. "does not invalidate the digital signature." -->
> One benefit of this approach is that adding or removing formatting characters that do not impact the meaning of the information being signed, such as spaces, tabs, and newlines, does not invalidate the digital signature.

→ no requirement: candidate C-0141 (reject)

Under option 5 a divergence in order alone fails at V5. Here two byte
strings that differ in order or whitespace carry one proof and both verify.
Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L170-171 "**Content addressing." .. "stable across transports." -->
> **Content addressing.** A statement is referred to by the SHA-256 of its TBS; a definition by the SHA-256 of its body. Both are stable across transports.

**Not a cut against option 5; a cost to the import profile (inferred).** An
imported credential has no unique byte form, so its identity cannot be the
digest of what was received the way a statement's is the digest of its TBS.
Open question 6.

**And on one of ADR-0004's own drivers it is evidence for option 5 over option
3.** ADR-0004 scored the driver this way:

<!-- qm spec/ADR-0004-dec-002-encoding.md L71 "order-only divergence detectable" .. "rejecting decoder**" -->
> order-only divergence detectable | in the grammar | §4.2.1 optional | RFC 8785 sorts keys | — | **stated rule + rejecting decoder**

A JCS suite here is option 3's cell in operation: the canonicaliser sorts the
members, so a reordered document is absorbed and verifies, and nothing records
that it diverged (L732, inferred). Under option 5 the same divergence is a
rejection at V5.

#### 6. Transparent payloads, against verifying before decoding

<!-- q L742 "While a digital signature needs to always be checked" .. "obviously bad requests." -->
> While a digital signature needs to always be checked before taking substantive action, other upstream checks can be performed on transparent payloads — such as identifier-based rate limiting, signature expiration checking, or nonce/challenge checking — to reject obviously bad requests.

→ `w3c-vc-data-integrity-1-0#R-0282`

Ours:

<!-- qm spec/SPEC-0002-ksa-core.md L274 "The envelope exists so that" .. "before it decodes**." -->
> The envelope exists so that a verifier can **verify before it decodes**.

**A cost of SPEC-0002 §5's envelope, recorded (inferred).** No KSA filter can
reject a statement for being expired, or for a stale nonce, before V4, because
those fields are decoded only after it. KSA bounds the work instead (§13.6) and
exposes `suite` and `says` as hints for routing and rate limiting. With Ed25519
verification cheap, the cost is small. It is an envelope property and names no
DEC-002 option.

**Searched and found not to cut against option 5:**

- **The CBOR data model, tags, deterministic encoding.** The source works on
  JSON maps (L531) and is silent on any native encoding.
- **Conditions (5) and (6).** The source never mentions Unicode normalisation:
  0 occurrences of `normaliz`, `normalis`, `Unicode` or `NFC` in the 1243
  lines. It states no ordering rule for arrays of ours.
- **Type identity `(defining key, label)`.** The source names types by IRIs,
  which are global names at the boundary (item 4 above); B5 keeps ours inside
  the signed JSON.

### 4.3 DEC-002's options, scored against this source

| this source | option 1 | option 2 | option 3 | option 4 | option 5 (KSA-CBOR) |
|---|---|---|---|---|---|
| **The form a foreign verifier reconstructs is a canonicalisation of JSON(-LD), on every suite** (L502, L731 to L733) | translates | translates | closest: JCS shared with the native form, but a statement is still not a VC (inferred); withdrawn | translates | translates, and ships JCS or RDFC for export only |
| **Canonicalisation at verification** (§4.2 item 1 above) | forced on foreign verifiers | forced | forced | forced | forced. No option avoids it on this route |
| **Global names in signed data** (§4.2 item 4) | boundary | native: fails P1 (ADR-0001) | boundary | ADR-0004's cell: fails through its option-2 half | boundary; item 3 underdetermined |
| **One signature, several syntaxes** (§4.2 item 2) | no | no | no | two syntaxes, by an unspecified bijection | no; the YAML form is a view |
| **Order-only divergence** (§4.2 item 5; L732) | in the grammar (ADR-0004) | optional (ADR-0004) | **absorbed**: a JCS suite sorts and verifies, as ADR-0004's cell predicts | — | **rejected** at V5 |
| **Profile named inside what is signed** | — | — | — | — | **unconditional**: `suite` and `kind` in the TBS, plus a DS label. Here: `type` and `cryptosuite` in the proof, signed or not as the suite decides [outside this source] |

### 4.4 Net, stated as evidence

On ADR-0004's own criteria this source is close to neutral: every option
translates and re-signs, and every option's export makes foreign verifiers
canonicalise. Against option 5 it leans toward **option 4** (serialisation
flexibility) and, weakly, **option 3** (a shared JSON canonicaliser), in both
cases only by way of canonicalising at verification, which ADR-0003 refuses
natively. For option 5 it supplies one instance: over option 3, on ADR-0004's
order-only-divergence driver, where a JCS suite absorbs what option 5 rejects
(§4.2 item 5). Its weight falls
**outside DEC-002**: on R-O-05, whose premise it contradicts (§5 below); on
ADR-0004 item 4 and DEC-005, which do not contemplate an embedded proof; on
item 3's IANA-only list; on P5.2, which presumes an envelope (open question 5);
and on the import profile's identity rule. Nothing here decides DEC-002 again.

---

## 5. R-O-05, tested against this source

`record.yaml` lists R-O-05 in `bears_on`. Its text:

<!-- qm spec/ARCH-0001-PROPOSAL-v0.2.0.md L433 "The signed payload SHALL" .. "verified canonical bytes." -->
> The signed payload SHALL be the canonical encoding verbatim, carried with an authenticated type indicator. A verifier SHALL verify the signature before decoding and SHALL NOT canonicalize input as part of verification. Any human-facing form SHALL be regenerated from verified canonical bytes.

and its standing:

<!-- qm project/DECISIONS-0001.md L79 "R-M-11/R-O-05/R-O-06 have no force" .. "no force" -->
> R-M-11/R-O-05/R-O-06 have no force

ADR-0003 nonetheless calls it accepted:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L53-57 "**Adopted by the specification" .. "not already canonical." -->
> **Adopted by the specification, under accepted ARCH-0001 R-O-05 rather than by this ADR:** the canonical binary is what is signed and transmitted. The producer encodes once, signs those bytes, and transmits them unchanged; the verifier checks the signature over the bytes received before decoding them, and rejects any that are not already canonical.

That inconsistency is already registered, not new here:

<!-- qm research/0006-mechanism/report.md L1382 "**`ADR-0003` calls R-O-05" .. "as proposed**" -->
> **`ADR-0003` calls R-O-05 *"accepted"*; `ARCH-0001` §5.3 stops at R-O-04, and `DECISIONS-0001` item 4 lists R-O-05 as proposed**

**So the rule has two standings, and this record meets both.** For KSA's own
statements it binds, through ADR-0003's rejected alternative (R1) and SPEC-0002
§5 and §13.1, which govern:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L72-73 "where they differ, the SPEC" .. "corrected." -->
> where they differ, the SPEC governs and the ARCH document is corrected.

As a requirement on every verifier, including ours when it imports, it is a
proposal.

### 5.1 Clause by clause

| R-O-05 clause | this source | verdict |
|---|---|---|
| clause 1: the signed form | what is protected is the transformed data (L731); under RDFC the canonical N-Quads are never transmitted (L733); under JCS the received document minus its proof is serialised again (inferred, §4.2 item 1) | **conflicts** |
| clause 2: the type indicator | `type` and `cryptosuite` name the profile (L519 to L521); whether they are signed is left to each suite (L494 to L497) | **underdetermined** in this source [outside this source] |
| clause 3: verify, then decode | §4.4 parses at step 1 and verifies at step 8 (L600, L607); §4.1 validates a schema before verifying (L543, L544) | **conflicts** (B3 reorders only the second) |
| clause 4: no canonicalising while verifying | verification is transformation, hashing and proof verification (L140, L142, non-normative), and the map interface forces it (L502) | **conflicts** |
| clause 5: the human-facing form | the verifier returns the received map minus its verified proofs (L506); L734 urges using only that | **constrains**: same intent, a different object (A2) |

**Conflicts on three of five clauses, underdetermined on one.** Not by defect:
the source states the trade-off and names the alternative it declines:

<!-- q L767 -->
> Implementers are also advised that other mechanisms that perform no transformations are available, that secure the data by wrapping it in a cryptographic envelope instead of embedding the proof in the data, such as JWTs [RFC7519] and CWTs [RFC8392]. These approaches have simplicity advantages in some use cases, at the expense of some of the benefits provided by the approach detailed in this specification.

→ no requirement or candidate carries these words

<!-- q L821 "Implementers are also advised" .. "detailed in this specification." -->
> Implementers are also advised that other selective disclosure mechanisms that perform no transformations are available, that secure the data by wrapping it in a cryptographic envelope instead of embedding the proof in the data, such as SD-JWTs [SD-JWT]. This approach has simplicity advantages in some use cases, at the expense of some of the benefits provided by the approach detailed in this specification.

→ no requirement or candidate carries these words

### 5.2 The DSSE critique, scored against the source's mitigations

R-O-05's ancestor is the proposal's §3.4:

<!-- qm spec/ARCH-0001-PROPOSAL-v0.2.0.md L219-225 "canonicalizing at verification time" .. "reads as another." -->
> canonicalizing at verification time forces the verifier to parse untrusted input *before* verifying it, which is error-prone and enlarges the attack surface; canonicalization schemes have been broken before; and a canonical form without an authenticated type indicator lets a signer produce a message in one encoding that a verifier reads as another.

| the critique | what this source does about it | net |
|---|---|---|
| **parse untrusted input before verifying** | parses (L600), and an RDFC suite expands under contexts first; mitigated by pinned contexts (L406, L429), dataset-poisoning detection (L727), resource-starvation mitigations every suite MUST state (L508), data-loss errors (L452) and a null base URL (L453) | **mitigated, not avoided** |
| **canonicalisation schemes have been broken** | vetting with a peer-reviewed proof of correctness (L772, L774); both named transformations are cited documents (A7) | **mitigated** by R-O-03's discipline |
| **no authenticated type indicator** | `cryptosuite` names the transformation; whether it is signed is each suite's (L494 to L497). One key type has two incompatible suites (L706): the case mofn R-0006 §3.3 raises when it reads condition (1) over a profile and its bytes together | **underdetermined here**; open question 3 |

The two mitigations worth stating once more: L727's dataset poisoning,

<!-- q L727 "This class of attack is called dataset poisoning" .. "halt processing." -->
> This class of attack is called dataset poisoning, and all modern RDF Dataset canonicalizers are required to detect these sorts of bad inputs and halt processing.

→ `w3c-vc-data-integrity-1-0#R-0279`

and L508's obligation on every suite:

<!-- q L508 -->
> The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.

→ `w3c-vc-data-integrity-1-0#R-0046`

**For the ADR that will decide R-O-05 (DECISIONS-0001 item 4):** this is the
one Recommendation in the library that takes the other side, with its price
listed. An acceptance that does not answer it by name has confirmed rather than
tested (open question 9). Ours, for comparison, on what rejection buys:

<!-- qm spec/ARCH-0002-key-relative-naming.md L440-443 "R-O-05 requires" .. "the separation is cosmetic." -->
> R-O-05 requires canonicalisation to run once, at authoring, on trusted input, and never as part of verification. **Rejection is what makes that separation real.** If a verifier may repair what it receives, the canonicaliser is back inside the verifier and the separation is cosmetic.

### 5.3 mofn report R-0006's open cell

<!-- qm research/0006-mechanism/report.md L259-262 "Where VC sits on this axis" .. "during verification." -->
> Where VC sits on this axis cannot be said from the library. RDF Canon's own text shows the risk — a canonicaliser with no rejection rule — but not whether VC Data Integrity runs it during verification.

**Answered: yes, structurally (inferred from L502, L600, L607, L731 to L733).**
Every suite that canonicalises to N-Quads runs RDF Dataset Canonicalization
over the received document during verification, and every JCS suite runs JCS
over it. Against mofn R-0006's condition (3):

<!-- qm research/0006-mechanism/report.md L389-390 "Canonicalisation runs" .. "part of verification." -->
> Canonicalisation runs **once, at authoring**, on trusted input, and never as part of verification.

**Condition (3) fails by construction on this route**, where it holds by
construction for vc+jwt and vc+cose (the sibling's adopt 1). For mofn R-0006 §2.2's
VC row this record supplies: canonicalised at authoring **and** at
verification, by JCS or RDFC 1.0 (L732, L733); signed, the transformed data
(L731) plus whatever the suite adds [outside this source]; carried, the
document with an embedded `proof` (L203) whose `proofValue` is Multibase
(L223); the verifier runs §4.4, then context validation (L435); the binding of
proof to issuer is left open (L484, B1). mofn R-0006 is not edited here.

---

## 6. R-I-06: what an export through Data Integrity would require (draft)

Every row is *(inferred)*: the source defines no import or export of anything.
ADR-0004 lists `trust` as the kind that carries the `AuthzCert` role (TV-5).

### 6.1 Decisions owed first

1. **That an embedded proof may carry R-I-06 at all** (§4.2 item 3; open
   question 1).
2. **A URL form for the export key**, since `verificationMethod` MUST be a URL
   string when present (L211) and the issuer must be its controller (B1).
   ADR-0005 defines none:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L37-38 "a 32-octet byte string" .. "(`SPEC-0002` §11)." -->
> a 32-octet byte string, `SHA-256(public-key encoding)` (`SPEC-0002` §4.5). Text renderings are presentation only (`SPEC-0002` §11).

   Open question 2.
3. **A cryptosuite.** For a suite-1 (Ed25519) export key the names the source
   gives are `eddsa-rdfc-2022` and `eddsa-jcs-2022` (L706); their algorithms
   are outside this source. The source's own guidance is L765 to L766 (B5) and
   L819 to L820. **A lean, not a decision (inferred):** JCS. It puts no
   JSON-LD processing inside the proof, it is the canonicaliser mofn R-0006 already
   analysed, and KSA's integers cannot meet its number hazards (A7). Its price
   is that the meaning of compacted terms is protected only by context pinning,
   which B5 closes. Open question 3.
4. **A documented context**, as A3: static, versioned, hash-published,
   `@protected`, defining every member (A1), with no relative URL:

<!-- q L453 "When deserializing to RDF" .. "set to null." -->
> When deserializing to RDF, implementations MUST ensure that the base URL is set to null.

→ `w3c-vc-data-integrity-1-0#R-0036`

5. **A separate export key and a usage code for it** (B6; open question 7).

### 6.2 The R-I-01 table for a `trust` statement on this route

Rows are aligned with the sibling's §5.1 so the two routes can be compared line
by line.

| KSA (SPEC-0002) | becomes, on this route | |
|---|---|---|
| the signed statement `[suite, says, tbs, sig, ? pub]` | nothing. The VC is a translation, signed again by the export key (B6) | **dropped, replaced** |
| statement digest, SHA-256(`tbs`) | the VC's `id`, as a URL spelling of the digest [outside this source] | **preserved by reference** (ours) |
| `kind` 5 and its DS label | the VC's `type` [outside this source], and the proof's `proofPurpose` `assertionMethod` (A5). No media-type indicator exists in a proof | **respelled** |
| `says` | `issuer` [outside this source], equal to the controller of the proof's `verificationMethod` (B1) | **preserved, respelled** |
| `suite` 1 | the cryptosuite name (§6.1 item 3) | **not carried** |
| the export key (B6) | `proof.verificationMethod`, a URL (open question 2): a locator the verifier dereferences, where the sibling's route had a `kid` hint | **respelled** |
| `this` = `[1, kid]` | `credentialSubject.id`, a URL spelling [outside this source] | **respelled** |
| the threshold form, `trusts` and `threshold` | nothing; a proof set is not a threshold (A4) | **dropped** |
| `body.about`, ranges typed by `(DefinitionId, label)` | claims under our documented context, with each DefinitionId inside the signed JSON (B5) | **inferred**: P1's identity survives only so |
| `may-delegate` | nothing. `capabilityDelegation` (L381) is a proof purpose for authorization capabilities, not a credential claim | **dropped** |
| `valid.not-before`, `valid.not-on-or-after` | `validFrom`, `validUntil` [outside this source] | **preserved** |
| `valid.issued` | nothing; `proof.created` is the export signature's time (A6) | **dropped** |
| a `revoke` (SPEC-0002 §8.7) | nothing in this source; `credentialStatus` is the data model's (L486) | **dropped**; a short `validUntil` instead (R-O-02) |
| holder binding | nothing in this source | **dropped** |
| — | one proof; no `previousProof`, `id`, `nonce`, `domain` or `challenge` (§4.1 above) | — |
| — | `created` written with `Z` (R2) | — |
| — | under JCS, the document emitted already in its own JCS form, so a receiver applying P5.1 can check it (open question 4) | — |

What every foreign verifier then does is fixed by the source: parse,
canonicalise (and, under RDFC, expand), hash, verify, then validate contexts.
**R-O-05's verifier clauses cannot hold on this route, and the R-I-01 table
records it as the route's property**, beside the sibling's route, where they
hold.

### 6.3 The same credential on the two routes

| property | this route (Data Integrity) | the sibling's route (vc+cose, `w3c-vc-jose-cose` §5.1) |
|---|---|---|
| what is signed | the transformed document: JCS text or N-Quads (L731 to L733) | the VC's JSON octets, unencoded |
| condition (3) at a foreign verifier | fails by construction (§5.3 above) | holds by construction |
| how the key is found | `verificationMethod`, a URL the verifier dereferences (L211) | `kid` as a hint, `iss` equal to `issuer` |
| how the profile is named | `type`, `cryptosuite`, `proofPurpose` in the proof | `typ`, a SHOULD |
| ADR-0004 item 4 | outside the set it names (§4.2 item 3) | inside it (COSE_Sign1) |
| central allocators at the boundary | W3C vocabularies, VC Extensions, multiformats (§4.2 item 4) | IANA COSE and CWT; JOSE |
| what an importer must run | a JSON canonicaliser, or a JSON-LD processor and RDFC (open question 4) | a COSE verifier; JSON is decoded after |

---

## 7. Mapping to our decisions

Verdicts, exactly six, one per row. **adopt**: we take the source's rule or
reasoning, or ours already says the same and the source corroborates it.
**adapt**: we take it with a stated change. **constrains**: one side narrows
what the other leaves open, and an implementation can satisfy both by taking
the narrower path. **conflicts**: no object or implementation satisfies both.
**silent**: one side does not reach the other's subject. **reject**: we decline
the source's rule, option or pattern, with a reason. Levels are the source's
as printed. Every locator of ours is at `a56a3c0`.

| # | ours (locator) | source (locator) | verdict | where |
|---|---|---|---|---|
| 1 | R-I-06 (ARCH-0001 §5.2, L318) | §2.1, §3.1, §4.2 | **constrains** | §6 |
| 2 | R-I-01 (ARCH-0001 §5.2, L313) | the proof members, contexts and allocators | **constrains** | §6.2, §4.2 item 4 |
| 3 | R-I-02 (ARCH-0001 §5.2, L314) | no trust model; context allow-lists are local (L438, L439) | **silent** | R4 |
| 4 | R-I-03 (ARCH-0001 §5.2, L315) | neither in-toto + DSSE nor COSE_Sign1 + CWT | **silent**: this route cannot count toward R-I-03 | §4.2 item 3 |
| 5 | §6 W3C VC row, its loss note (ARCH-0001 §6, L356) | §2.4 L406, L429; §2.4.1 L435 | **adopt** | A3 |
| 6 | §6 W3C VC row, import column `I` (ARCH-0001 §6, L356) | verification canonicalises (L502, L600, L607) | **constrains**: an import is possible only as open question 4 allows | §5, R1 |
| 7 | R-M-02 (ARCH-0001 §5.1, L299) | `verificationMethod` is a URL (L211) | **constrains**: a key-only principal survives only through a URL spelling | §6.1 item 2 |
| 8 | mofn R-0006 §5.1 and SPEC-0002 §8.6 (threshold inside the signed payload) | Appendix A L871; §4.5 L618 | **adopt** | A4 |
| 9 | R-M-07 (ARCH-0001 §5.1, L304) | `digestMultibase` MAY, on an object with an `id` (L388) | **constrains**: an artifact export needs an `id` for the digest's object | §4.1 |
| 10 | R-O-01 (ARCH-0001 §5.3, L325) | `verificationMethod` OPTIONAL (L211), yet required by §4.2 step 2 (L551) and §4.4 step 4 (L603) | **constrains**: always set; `KeyId` computed from the resolved key | §9 D6 |
| 11 | R-O-02 (ARCH-0001 §5.3, L326) | no status mechanism here (L486) | **adopt**: exports stay short-lived | §6.2 |
| 12 | R-O-03 (ARCH-0001 §5.3, L327) | §3 L494; §5.13 L774 | **adopt** | A7 |
| 13 | R-O-05 (proposal §7, L433; no force) | L502, L600, L607, L731 to L733 | **conflicts** | §5 |
| 14 | P5.1 (ARCH-0002, accepted, L412 to L415) | every suite re-encodes the received document (L502) | **conflicts** for an import verified by us: an RDFC credential is never received in canonical form; JCS only if received in its own JCS form (inferred) | open question 4 |
| 15 | P5 (ARCH-0002, accepted, L391 to L396) | §2.4.3 L451, L452; §1.3 L169 | **adopt** | A1 |
| 16 | P5.2 (ARCH-0002, accepted, L498 to L505) | an embedded proof has no envelope exterior | **silent**: P5.2 presumes an envelope | open question 5 |
| 17 | P2 (ARCH-0002, accepted, L146 to L148) | §2.6 L483, L484 | **constrains** | B1 |
| 18 | P1 and ADR-0001 (ARCH-0002 L67; ADR-0001 L55, L56) | global names in the signed data of a boundary object | **adopt**: permitted at the boundary, documented as lossy | §4.2 item 4 |
| 19 | P1.1 (ARCH-0002, draft, L117 to L119) | `verificationMethod` locates a key (L211) | **constrains**: the principal is the key, never the URL | B2 |
| 20 | ADR-0003 D1 (L47) | under JCS the contexts' meaning is unsigned (L765, L766) | **adapt** | B5 |
| 21 | ADR-0003 rejected alternative, signing a re-encoded statement (L62, L63); SPEC-0002 §5, §13.1 | the whole design (L140, L142, L502) | **reject** natively, as ADR-0003 did | R1 |
| 22 | ADR-0003 rejected alternative, unsigned vocabularies (L66, L67) | context validation by hash (L438, L439, L652) | **reject** as our model | R4 |
| 23 | ADR-0004 items 1 and 2 (L38 to L45) | the source works on JSON maps (L531) | **silent**: KSA-CBOR never enters a proof | §4.2 |
| 24 | ADR-0004 item 3 (L46 to L50) | non-IANA allocators (§4.2 item 4) | **constrains**: the list is narrower than P1 | open question 10 |
| 25 | ADR-0004 item 4 (L51, L52) | an embedded proof is not an envelope | **constrains**: read as exhaustive, it excludes this route | open question 1 |
| 26 | ADR-0004, option 4 rejected (L125, L126) | serialisation flexibility (L159, L724, L725) | **constrains**: the source names an unscored driver, met by a means R1 rejects | §4.2 item 2 |
| 27 | MD-3 (meeting 2026-09-28, L51 to L53) | as rows 23 to 26 | **constrains**: COSE is named, this route is not; closed by ADR-0004 | §4 |
| 28 | DEC-005 (ARCH-0001 §7, L485 to L487) | no envelope | **silent** | open question 1 |
| 29 | ADR-0005 item 1 (L37, L38) | `verificationMethod` MUST be a URL string if present (L211) | **constrains** | open question 2 |
| 30 | ADR-0005, `did:key` rejected (L71) | Multibase and Multikey headers (L223; the example keys, §4.2 item 4) | **reject** natively; a boundary-only candidate | open question 2 |
| 31 | ADR-0005, interchange (L89 to L92) | no `kid` anywhere in the source | **silent**: the import rule does not reach a URL | B2 |
| 32 | SPEC-0002 §3, content addressing (L170, L171) | reordered documents verify (L732) | **constrains**: an import must define identity | open question 6 |
| 33 | SPEC-0002 §4.4, time (L243) | MAY repair a time with no offset (L215, L217) | **reject** the MAY | R2 |
| 34 | SPEC-0002 §6.1, the suite inside the TBS (L311) | curve and hash chosen by the key's format (L707) | **reject** the pattern | R5 |
| 35 | SPEC-0002 §6.4 and SPEC-0001 §8.1 (L358, L359; L326, L327) | `proofPurpose`, `domain`, `challenge` (L372; §4.4 steps 5 to 7) | **adopt** | A5 |
| 36 | SPEC-0002 §7.3, `issued` (L434) | §2.6 L485 | **adopt** | A6 |
| 37 | SPEC-0002 §9.1 (L614, L615) | an error returned as `verified: false` (L599); L507 | **adapt** | B4 |
| 38 | SPEC-0002 §9.2 order, §13.6 (L855) | §4.1's receiving order (L542 to L545) | **constrains** | B3 |
| 39 | SPEC-0002 §10 (L651 to L653) | fetching a verification method on first encounter (L780) | **constrains** | B2 |
| 40 | SPEC-0002 §13.2 and SPEC-0001 §5.3 (L824 to L826; L226, L227) | no domain separation among §3's MUSTs | **adapt** | B6 |
| 41 | SPEC-0001 §5.3, the external statement (L229 to L232) | the protected data is not the received bytes (L731) | **constrains**: keeping the bytes does not keep what was signed | open questions 4, 6 |
| 42 | SPEC-0002 §5, verify before decoding (L274), and §11.1's view (L680, L681) | §5.8's transparent payloads (L742, L745) | **silent**: each governs its own objects; different answers to one problem | §4.2 item 6 |
| 43 | ARCH-0003 §12 item 4; SPEC-0001 §1.3 (L783, L784; L90 to L93) | the selective-disclosure suites (L801, L820) | **reject** this semester | R7 |
| 44 | mofn R-0006 §3.4, option 3's second ground (L462 to L466) | a JCS suite verifies in exactly that order | **adopt**: corroborates the withdrawal | §4.2 item 1 |
| 45 | SPEC-0002 §6.2, hybrid suites reserved (L324) | §5.4's layering by parallel proofs (L713, L714) | **silent** | open question 8 |
| 46 | SPEC-0002 §6.1, what a suite defines | §3's suite requirements (L492 to L511); §5.2 L697; §5.5 L719, L720 | **adopt** | A8 |
| 47 | ADR-0004's scoring, order-only divergence (L71) | a JCS suite absorbs reordering (L732) | **adopt**: corroborates option 3's cell, and option 5's | §4.2 item 5 |

**Count: adopt 11, adapt 3, constrains 17, conflicts 2, silent 8, reject 6, of
47 rows**, tallied from the verdict column by script (47 rows examined, each
with exactly one verdict). **Both conflicts fall on
canonicalisation at verification:** R-O-05, which has no force (row 13), and
P5.1, accepted, for an import verified by us (row 14). **None falls on
ADR-0004.** The rejections are of the source's options and patterns, never of a
requirement it imposes on us.

---

## 8. Open questions

1. **Which decision owns R-I-06's securing mechanism, and may it be an embedded
   proof?** ADR-0004 item 4 names COSE_Sign1 and DSSE; DEC-005 covers
   `ArtifactStatement`; R-I-03 does not reach a VC. The sibling asks the same
   for JOSE. Settle it by widening DEC-005 or in a new DEC.
2. **How is a KSA key spelled as a URL** for `verificationMethod`, `issuer` and
   `credentialSubject.id`? ADR-0005 makes text renderings presentation only and
   rejects `did:key` natively; ADR-0001 permits it at the boundary as a lossy
   mapping. An https controller document roots a foreign verifier's binding in
   the web PKI (inferred). Shared with the sibling's open question 2. Settle it
   in ADR-0005's successor or in the R-I-01 VC table.
3. **Which suite, and does it sign its own name and options?** JCS or RDFC
   (§6.1 item 3), and whether each suite covers `cryptosuite`, `proofPurpose`
   and the other proof options in what it signs [outside this source]. Two
   incompatible suites exist per key type (L706), the case mofn R-0006 §3.3 raises
   when it reads condition (1) over a profile and its bytes together. Settle it after
   the EdDSA and ECDSA suite documents are held (question 11). **Partly answered
   by the verify pass [outside this source]:** read on 2026-11-07, the Proof
   Configuration algorithms of `eddsa-rdfc-2022`, `eddsa-jcs-2022` and
   `ecdsa-rdfc-2019` canonicalise and hash a clone of the proof options, every
   member but `proofValue` (inferred requirement
   `w3c-vc-data-integrity-1-0#R-0288`), so those three suites sign their own
   name, `type`, `proofPurpose`, `created`, `domain` and `challenge`. The choice
   of suite stays open.
4. **May a Data Integrity credential be imported, and where is it verified?**
   (a) not at all, under P5.1; (b) JCS only, with the received bytes required
   to equal their own JCS form, which keeps to P5.1's letter (inferred) and not
   to R-O-05; (c) as SPEC-0001 §5.3's external statement, verified by an
   isolated component outside the KSA verifier, about which neither P5.1 nor
   P5.2 says anything yet. Settle it in P5.2's successor and in mofn#110's
   import column.
5. **Where does P5.2 put an embedded proof?** Its clause:

<!-- qm spec/ARCH-0002-key-relative-naming.md L503-505 "P5 governs the native model" .. "its exterior." -->
> P5 governs the native model and the payload interior, in both directions. At an interchange boundary the foreign envelope's own rules govern its exterior.

   A `proof` is a member of the payload, so by that text the whole document is
   interior and P5 governs it in both directions: an unknown proof member,
   which a suite MAY define (L524), is then a rejection on import. Is that
   intended? P5.2 was reasoned from DSSE and is already owed a COSE `crit`
   analysis:

<!-- qm spec/ARCH-0002-key-relative-naming.md L522-523 "**DEC-005 is open" .. "export envelope." -->
> **DEC-005 is open**, and the same analysis is owed for COSE `crit` if COSE is chosen as an export envelope.

   Settle it there; P5.2 is accepted, so a change is a superseding ADR.
6. **What is an imported credential's identity?** The digest of the received
   bytes is not stable (§4.2 item 5); the digest of the canonical form
   canonicalises for identity, which mofn R-0006's Group B allows; the `proofValue`
   keys on a signature, as SPEC-0002 §13.3 notes some systems do. Settle it in
   the import profile.
7. **Which key signs an export, and how is it linked to the persona?**
   SPEC-0002 §12.7 has no usage code for it. Shared with the sibling's open
   question 7. Settle it in SPEC-0002 §12.7 and §8, through an ADR.
8. **Layering for long-lived statements: one hybrid suite, or parallel proofs?**
   The source layers by parallel proofs:

<!-- q L714 "It also provides for cryptographic layering" .. "easy to use for developers." -->
> It also provides for cryptographic layering, which allows one to simultaneously use multiple cryptographic algorithms, typically in parallel, such that any of those used to protect information can be used without reliance on or requirement of the others, while still keeping the digital proof format easy to use for developers.

→ no requirement: candidate C-0128 (reject)

   and its own Appendix A shows any of them can be stripped (A4). A layered
   proof protects only a verifier whose policy demands the surviving
   algorithm's proof (inferred). A hybrid suite, in which both signatures must
   verify, puts that rule in the signed object; SPEC-0002 reserves its codes:

<!-- qm spec/SPEC-0002-ksa-core.md L324 "reserved: post-quantum and hybrid suites" .. "hybrid suites" -->
> reserved: post-quantum and hybrid suites

   Settle it when SPEC-0002 §6 specifies one (SPEC-0001 §11).
9. **The ADR that decides R-O-05 should answer this source by name.** Is
   canonicalising at verification, with §5.2's mitigations, acceptable on any
   foreign route we export to? And ADR-0003's calling R-O-05 accepted is still
   unresolved (§5 above). Settle it under DECISIONS-0001 item 4.
10. **ADR-0004 item 3's list.** Extend it beyond IANA (multiformats, W3C
    vocabularies, VC Extensions), or leave each R-I-01 table to name its own
    allocators? Settle it in ADR-0004's successor or in the R-I-01 tables.
11. **The library holds this source's dependencies weakly.** Controlled
    Identifiers 1.0 (Multikey, verification-method retrieval, verification
    relationships, the §5.10 check at L754), the EdDSA, ECDSA and BBS suites,
    and VC Extensions have no record. Ingest them before §6 is built on; the
    `artifact-statements` topic, which owns this record, is the natural owner.
    (The verify pass fetched vc-di-eddsa, vc-di-ecdsa and Controlled
    Identifiers 1.0 to check the examples' signatures and Multibase; their
    digests are in `examples/signatures.derived.json` and `schema/README.md`.
    That is evidence for this record, not a record of them.)
12. **Two steps of the protocol model name a message the source never
    defines.** Pass 3 joined all 33 message and returns items of
    `protocol.yaml` to `messages.yaml` (`crosscheck.yaml`): 31 resolve to a
    structure, two do not. F11 step 3 is an HTTP GET with an `Accept` header
    (§2.4); the source shows only a `curl` command for it (L414) and
    `messages.yaml` carries the response side (MSG-07, ENC-05) but no request.
    F17 step 1 is a request naming the expected context; §2.4.1 mentions a
    presentation request as an example and defines none (the step is
    inferred). Both are gaps in the source, not in the join. An export route
    that relies on either must define it. Settle it in the R-I-01 table for a
    `trust` statement, or in whichever record owns the exchange (VC
    Extensions or a presentation protocol).

---

## 9. Source defects and tensions met while mapping

Recorded, not repaired. This file did not read `normative.md`,
`requirements.yaml` or `protocol.yaml`; the verify pass reconciles these with
them. Each was re-read in the `.txt`, and the example measurements were taken
from the HTML.

- **D1. §4.5 sets one field and tests another.** Step 5 sets
  `combinedVerificationResult.status` to true (L630); step 6.1 sets
  `.verified` to false (L632); step 7 tests `.status` (L634), which nothing
  sets false. So the step that nulls the document on failure never fires.

<!-- q L634 -->
> If combinedVerificationResult.status is false, set combinedVerificationResult.document to null and combinedVerificationResult.mediaType to null.

→ `w3c-vc-data-integrity-1-0#R-0260`

- **D2. §4.5 never hands the cryptosuite the proof it is verifying.** Step 3.3
  builds the input document with `proof` set to the *previous* proofs (L625),
  and step 3.4 runs §4.4's steps 4 to 8 on it (L628), whose step 8 passes that
  document to the suite (L607). §4.5 takes one input (L619), so the
  `cryptosuite`, `expectedProofPurpose`, `domain` and `challenge` that steps 5
  to 8 use are unbound there.

<!-- q L625 -->
> Let inputDocument be a copy of securedDocument with the proof value removed and then set inputDocument.proof to matchingProofs.

→ `w3c-vc-data-integrity-1-0#R-0252`

<!-- q L628 -->
> Run steps 4 through 8 of the algorithm in section 4.4 Verify Proof on inputDocument; if no exceptions are raised, append cryptosuiteVerificationResult to verificationResults.

→ `w3c-vc-data-integrity-1-0#R-0253`

- **D3. Names drift between the result structures.** §4.4's result has
  `verifiedDocument` (L591); §4.5 writes `document` (L630, L633); §4.6 step 4
  removes a `document` property (L655) from a result whose member is
  `validatedDocument` (L643). §4.4 step 9 returns no `warnings` or `errors`
  (L608 to L614), which its result declares (L595 to L598).
- **D4. `previousProof` elements are strings, then have an `id`.** L225 makes
  them strings; §4.3 step 5 (L565) and §4.5 step 3.2 (L624) test an element's
  `id` attribute.

<!-- q L565 "If any element of previousProof list" .. "any element of allProofs" -->
> If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs

→ `w3c-vc-data-integrity-1-0#R-0202`

- **D5. Two raised error types are not defined in §4.7.** `PARSING_ERROR`
  (L601) and `DATA_LOSS_DETECTION_ERROR` (L452) are raised; §4.7 defines five
  others (L666 to L675).
- **D6. `verificationMethod` is OPTIONAL in the data model and required by both
  algorithms.**

<!-- q L211 "Inclusion of verificationMethod is OPTIONAL" .. "verify the proof." -->
> Inclusion of verificationMethod is OPTIONAL, but if it is not included, other properties such as cryptosuite might provide a mechanism by which to obtain the information necessary to verify the proof.

→ `w3c-vc-data-integrity-1-0#R-0007`

<!-- q L551 -->
> If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

→ `w3c-vc-data-integrity-1-0#R-0182`, `w3c-vc-data-integrity-1-0#R-0183`

- **D7. One signature across syntaxes, one syntax in the algorithm.** §1.2,
  §5.6 and §5.7 claim JSON, CBOR and YAML (L159, L724, L733); §4.4 step 1
  parses JSON bytes only (L600), and §1.3 defines a conforming secured document
  as convertible to JSON (L167). The `mediaType` input of §4.4 (L576 to L579)
  is never used except to be returned (L613, L614).
- **D8. Exceptions or results.** §4.4 defines a raised error as a returned
  result (L599); §4.3 step 7 (L569) and §4.5 step 3.4 (L628) branch on raised
  exceptions instead.
- **D9. Examples measured from the HTML** (the examples lane owns the
  fixtures). Decoded from base58btc after the `z` prefix: the `proofValue` of
  Example 2 (an `eddsa-jcs-2022` proof) and both of Example 7 (`eddsa-rdfc-2022`)
  are 65 octets, where an Ed25519 signature is 64 [outside this source: RFC
  8032]; Examples 4, 5 and 6 decode to 64. The second key of Examples 6 and 7,
  `z6MkGskx…`, decodes to 34 octets opening `ec ff`, where every other `z6Mk`
  key in the document opens `ed 01`. None of the 14 is usable as a positive
  fixture as printed: Examples 1 and 3 carry no proof; 2 and 7 have the wrong
  signature length; 4 and 5 are P-256, not a suite of ours; 6's second key
  opens `ec ff`; 8 is a fragment; 9 to 14 are symbolic. Example 6's first proof
  was not run through RDFC by this file; the examples lane ran it, and the
  verify pass re-ran all seven proofs with a recipe that reproduces the
  cryptosuite Recommendations' own test vectors
  (`examples/verify-signatures.derived.py`): none verifies. Examples 4 and 5
  name, as their `verificationMethod`, the P-256 test-vector key of vc-di-ecdsa
  A.1, whose secret key that document publishes [outside this source].
- **D10. Text**, each as printed: a doubled article (L195), a doubled
  preposition (L379), two wrong articles (L388, L531), three misspellings
  (L485, L517, L833), a past tense where an infinitive belongs (L215, L217),
  a dropped subject (L367), a wrong word (L713), and an unpaired backtick
  (L440):

<!-- q L195 "is the The" .. "Vocabulary." -->
> is the The Security Vocabulary.

→ `w3c-vc-data-integrity-1-0#R-0082`

<!-- q L379 "used for for" .. "protocols" -->
> used for for key agreement protocols

→ `w3c-vc-data-integrity-1-0#R-0119`

<!-- q L388 "or an list" .. "values" -->
> or an list of string values

→ `w3c-vc-data-integrity-1-0#R-0023`

<!-- q L531 "An input document is an map" .. "an map" -->
> An input document is an map

→ `w3c-vc-data-integrity-1-0#R-0055`

<!-- q L485 "betweeen" .. "validUntil)" -->
> betweeen validFrom and validUntil)

→ `w3c-vc-data-integrity-1-0#R-0153`

<!-- q L517 "When specifing" .. "design pattern" -->
> When specifing a cryptographic suite that utilizes this design pattern

→ `w3c-vc-data-integrity-1-0#R-0051`

<!-- q L833 "cultural normas" .. "normas" -->
> cultural normas

→ no requirement or candidate carries these words

<!-- q L215 "MAY chose" .. "chose" -->
> MAY chose

→ `w3c-vc-data-integrity-1-0#R-0010`

<!-- q L367 "as without these, is not possible" .. "possible" -->
> as without these, is not possible

→ `w3c-vc-data-integrity-1-0#R-0116`

<!-- q L713 "the failure or one or more" .. "primitives" -->
> the failure or one or more cryptographic algorithms or primitives

→ no requirement or candidate carries these words

<!-- q L440 "(e.g., `https://ontology.example/v1)" .. "v1)" -->
> (e.g., `https://ontology.example/v1)

→ no requirement or candidate carries these words

---

## 10. bears_on

`record.yaml` lists R-I-06, R-O-05 and R-O-03. Each was checked against
ARCH-0001 v0.1.8 and the proposal at `a56a3c0`. `record.yaml` is not edited
here.

- **All three stand.** R-I-06: §6. R-O-05: §5, the sharpest bearing in the
  record. R-O-03: A7.
- **Warranted additions:**
  - **DEC-002**: §4.
  - **DEC-003**: on this route a key is named by a URL (rows 29 to 31).
  - **DEC-005**: its scope leaves an embedded-proof export undecided (row 28).
  - **R-I-01**: §6.2 is the table it asks for.
  - **R-M-02**: a key-only principal needs a URL spelling (row 7).
  - **R-O-01**: `verificationMethod` is optional in the model (row 10).
  - **R-O-02**: no status mechanism, so exports stay short-lived (row 11).
- **Weak, optional:** R-M-07 (row 9), R-I-02 (row 3).
- **Outside the field's vocabulary.** `bears_on` takes ARCH-0001 DEC and R
  ids, so P2, P5, P5.1, P5.2, P1.1, ADR-0003's rejected alternatives and
  SPEC-0002 §3, §9 and §10 cannot be listed. They are rows 14 to 22 and 32 to
  46; P5.1 (row 14) and P5.2 (row 16) are the ones this record presses
  hardest.

## 11. What this file decides

Nothing.

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

Each adaptation and open question names the SPEC section, ADR or DEC that would
settle it. The conflicts in §7 are evidence for the ADR that decides R-O-05,
for P5.2's successor, and for mofn#110's import column. None of it reopens
DEC-002.
