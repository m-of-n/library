---
record: w3c-vc-data-model-2-0
kind: design-notes
title: "w3c-vc-data-model-2-0 — bearing on our design"
extracted: "2026-11-07"
reviewed_by: ""
---

# VC Data Model 2.0 — bearing on our design

*Verifiable Credentials Data Model v2.0* is the W3C Recommendation of 15 May
2025 (REC-vc-data-model-2.0-20250515; HTML, sha256
`a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8`, equal to
`content.sha256` in `record.yaml` and recomputed from `.cache/` in this pass).
It defines what a verifiable credential **is**: a compacted JSON-LD document
whose first context is a fixed, hash-pinned base context, with an `issuer` URL,
one or more subjects, an optional validity window, and optional status, schema,
evidence, terms-of-use, refresh and related-resource links. It secures nothing.
§4.12 names two classes of securing mechanism and RECOMMENDS one of each; §5.13
says what any mechanism must do; §7.1 is the verifier every mechanism plugs
into.

It is the third record of a set. `w3c-vc-jose-cose` **wraps** this data model
and signs its octets; `w3c-vc-data-integrity-1-0` **embeds** a proof in it and
signs a transformation of it. This record is what both of them secure, so it
holds everything an export owes **whichever route it takes**. Both siblings
marked such statements *[VC DM, outside this source]* or *[outside this
source]*; this file is where they are sourced.

It reaches us in six ways.

1. **R-I-06** (Could): a VC export of part of `AuthzCert`, under a documented
   context (quoted in §6.1). This is the data model it exports into. §6 maps a
   KSA `trust` statement (the `AuthzCert` role, ADR-0004 TV-5) field by field
   and says where it cannot be mapped.
2. **R-I-01**: §5.11 *Ecosystem Compatibility* is the source's own rule set for
   a transformation like ours, and it adds rows the mapping table owes (§6.2).
3. **DEC-002, accepted by ADR-0004, and MD-3.** §4 says what the data model fixes
   envelope-independently, clause by clause against MD-3, and where it cuts.
4. **The ARCH-0001 §6 W3C VC row** and its loss note on context pinning
   (quoted in B4). Appendix B.1 pins the base context by SHA-256; the context
   files were fetched, hashed and measured (§5).
5. **mofn report R-0006** §2.2 and §2.5. Its VC row is ∅ because no VC record
   existed; this record fills the data-model half (§4.5).
6. **§5.9** disclaims, non-normatively, authorization as a use unless a
   framework for it comes along. That bears on whether `AuthzCert` is the right
   thing to export at all (§6.1).

What it is not: a securing mechanism, a trust model (§5.1 places issuer trust
out of scope), a status scheme (§4.10), an authorization framework (§5.9), or an
exchange protocol.

**Things to hold while reading.**

1. **What binds.** The source's rule:

<!-- q L226 -->
> As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

   Measured over the HTML's 125 `section` elements: class `informative` on §1,
   §1.1, §1.2, §3 to §3.3, §4.1, §5.1, §5.9, the *Media Type Precision*
   subsection of §6.2, §6.3, all of §8, §9, §10 and §11, Appendices A, C, D and
   F, and B.4. Class `normative` on §1.3, §2, §4, §5.8, §5.10, §5.11, §7, §7.1,
   B.1 and B.2; the rest carry neither and are normative unless they sit inside
   an informative section. **So §5.9 (authorization), §5.1 (trust model),
   Appendix A (validation) and Appendix C (the media type registrations) are
   non-normative**, and §11.1 and §11.2, unclassed inside the informative §11,
   are non-normative although they carry 8 BCP 14 keywords (`skeleton-report.txt`:
   5 and 3). `bin/bcp14-count` finds 165 keywords in the `.txt`.
2. **Quotations are by reference, never typed.** A quotation of the source is a
   `<!-- q Lx-y -->` marker rendered by `bin/check-quotes --render` from
   `.cache/w3c-vc-data-model-2-0.txt` (5009 lines, sha256
   `73d91cc0b6a7d582512eb06d45a5fcfa8c696ab094b3db44f7a1495e9d3da548`, rendered
   by `bin/render-w3c`, one line per HTML block). A quotation of one of
   our documents is a `<!-- qm PATH Lx-y -->` marker: `PATH` is a file of the
   m-of-n repository at commit **`a56a3c0`** (2026-11-06), the words are lines x
   to y of `git show a56a3c0:PATH`, whitespace collapsed, a blockquote margin
   dropped; a pass script renders them and checks each against **its own file
   only**. Optional anchors (`"starts" .. "ends"`) select a sub-span in both
   kinds. The JSON-LD context files are **not** quoted: every value below that
   comes from them was read by a script and is stated with its method. Names in
   backticks (`validUntil`, `https://www.w3.org/ns/credentials/v2`) are
   identifiers, not quotations.
3. **Locators.** `§n` is the heading as the `.txt` prints it; `Lnnn` is the
   `.txt` line, which is exact. **No ¶ counts are used**, as in the Data Integrity
   sibling: a line number is exact, and a paragraph count would be a second
   convention to get wrong. A term of a definition list is named by its term
   (`§4.9 validUntil`). Requirement ids are wired at the end (§10), from
   `requirements.yaml`, by script.
4. **Our decisions, and their standing at `a56a3c0`** — the Data Integrity
   sibling's table, which read the same commit, plus three documents this
   source reaches (SPEC-0003, SPEC-0004, DL-0025) and less ARCH-0003, which it
   does not.

   | name | path at a56a3c0 | standing |
   |---|---|---|
   | ARCH-0001 v0.1.8 | `spec/ARCH-0001-authorization-attestation.md` | draft. §5 R-M, R-I, R-O rows; §6 matrix; §7: DEC-002, DEC-003 accepted; DEC-001, DEC-004, DEC-005 open |
   | proposal | `spec/ARCH-0001-PROPOSAL-v0.2.0.md` | proposed, nothing accepted. Source of R-O-05 and of DEC-007 |
   | ARCH-0002 v0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | P1 accepted (ADR-0001); P2, P3, P5 with P5.1 and P5.2, P6 accepted (ADR-0002); P1.1, P4, P7, DEC-008 draft |
   | ADR-0001, ADR-0003 | `spec/ADR-0001-key-relative-naming.md`, `spec/ADR-0003-ksa-core-decisions.md` | accepted; under ADR-0003 the SPECs govern where they differ from an ARCH |
   | ADR-0002 | `spec/ADR-0002-provisional-principles.md` | accepted 2026-11-06, `reviewed: false` |
   | ADR-0004, ADR-0005 | `spec/ADR-0004-dec-002-encoding.md`, `spec/ADR-0005-dec-003-key-identifier.md` | accepted 2026-10-25, `reviewed: false`; DEC-002 option 5, DEC-003 |
   | SPEC-0001 v0.1.0, SPEC-0002 v0.5.0 | `spec/SPEC-0001-ksa-architecture.md`, `spec/SPEC-0002-ksa-core.md` | drafts; govern under ADR-0003 |
   | SPEC-0003 v0.1.3, SPEC-0004 v0.3.0 | `spec/SPEC-0003-ksa-definitions.md`, `spec/SPEC-0004-ksa-trust-evaluation.md` | drafts; govern under ADR-0003. Definitions and their identity; trust evaluation |
   | DECISIONS-0001 v0.5.0 | `project/DECISIONS-0001.md` | the register |
   | MD-3 | `project/meetings/2026-09-28.md` | dated narrowing, closed by ADR-0004 |
   | DL-0025 | `design-log/0025-delegation-depth/question.md` | delegation is integer depth; `trust … about … may-delegate` is the name |
   | mofn report R-0006 v0.3.0 | `research/0006-mechanism/report.md` | draft; evidence, decides nothing |
   | CONTRIBUTING | `CONTRIBUTING.md` | process; §5 |

   **`docs/extraction.md` is stale on one point**, as both siblings found: its
   MD-3 paragraph says no DEC-002 ADR exists, and at `a56a3c0` ADR-0004 is that
   ADR. This file maps against ADR-0004 and still records where the source cuts
   against option 5, which is what the rule is for. `docs/` is not edited here.
5. **Labels.** *(inferred)* marks what the source implies rather than states,
   and every consequence drawn here. **Ours** marks the library's proposal.
   **[outside this source]** marks a statement resting on a document the source
   cites and the library does not hold — JSON-LD 1.1, Controlled Identifiers
   1.0, Subresource Integrity, the VC Extensions — never quoted and never the
   sole ground of a verdict. The two siblings are cited by section, never quoted:
   their words are their records', and resolving them here would be the foreign-
   quotation hazard.
6. **Numbering.** `R-M-NN`, `R-I-NN`, `R-O-NN` are ARCH-0001 §5, except R-O-05,
   a proposal §7 row. `P1` to `P7`, `P1.1`, `P5.1`, `P5.2` are ARCH-0002. `MD-n`
   are meeting decisions, `DL-NNNN` design-log entries. "Condition (n)" is one of
   mofn report R-0006 §3.2's six. `V1` to `V9` are SPEC-0002 §9.2's steps, `TV-n`
   its vectors, `DV-n` its definitions. A1… are this file's adoptions, B1…
   adaptations, R1… rejections, D1… source defects. "§6 below" is this file; a
   bare `§n` is the source's.

---

## 1. What we adopt

### A1. Verify, then check the data model, then validate

§7.1, after the securing mechanism has run:

<!-- q L3370 -->
> If result.status is set to false, add a CRYPTOGRAPHIC_SECURITY_ERROR to result.errors.

<!-- q L3371 -->
> If result.status is set to true, ensure that result.document is a conforming document. If it is not, set result.status to false, remove the document property from result, and add at least one MALFORMED_VALUE_ERROR to result.errors. Other warnings and errors MAY be included to aid any debugging process.

<!-- q L3373 -->
> The steps for verifying the state of the securing mechanism and verifying that the input document is a conforming document MAY be performed in a different order than that provided above as long as the implementation returns errors for the same invalid inputs. Implementations MAY produce different errors than described above.

and, non-normatively, Appendix A.7:

<!-- q L4075 "Because some credentials can be useful" .. "performed after verification." -->
> Because some credentials can be useful for secondary purposes even if their original validity period has expired, validity period, as expressed using the validFrom and validUntil properties, is always considered a component of validation, which is performed after verification.

Ours, SPEC-0002 §9.2:

<!-- qm spec/SPEC-0002-ksa-core.md L621-622 -->
> A verifier MUST perform these steps in this order, stopping at the first that fails.

<!-- qm spec/SPEC-0002-ksa-core.md L636-639 -->
> Checks that need other statements, definitions or time — revocation, validity at a time, whether a type exists, whether a value is in range, authorization — are **not** part of single-statement verification. They are trust evaluation (SPEC-0004).

**The same split, drawn in the same place (inferred).** §7.1 runs the securing
mechanism first and checks the data model only when it returned true; validity,
status and business rules are validation, after it. SPEC-0002 verifies at V4,
decodes at V5, checks structure at V7, and leaves validity and revocation to
trust evaluation. L3373 lets an implementation reorder only if the same inputs
fail; ours does not reorder. **One tension:** §2 puts the status check inside
verification (L276), while §7.1 has no status step and Appendix A.8 treats
status as validation (L4080). D3 records it; ours keeps revocation in trust
evaluation, as SPEC-0002 does.

### A2. Trust in an issuer is the verifier's, and local

<!-- q L2618 "How verifiers decide which issuers to trust" .. "out of scope for this recommendation." -->
> How verifiers decide which issuers to trust, and for what data or purposes, is out of scope for this recommendation.

<!-- q L2622 "In the Verifiable Credentials Data Model" .. "does not trust an issuer." -->
> In the Verifiable Credentials Data Model, a verifier either directly trusts or does not trust an issuer.

Both are in the non-normative §5.1. Ours, R-I-02 and SPEC-0004 §4.3:

<!-- qm spec/ARCH-0001-authorization-attestation.md L314 "Import SHALL NOT" .. "native trust anchor." -->
> Import SHALL NOT require the foreign object to become a native trust anchor.

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L180-181 "**A signature never makes an anchor.**" .. "only by acceptance." -->
> **A signature never makes an anchor.** A trust statement from a third party is a *proposal* that names who proposed it. It becomes an anchor only by acceptance.

**Corroboration.** Nothing in a VC can make itself an anchor; whether a foreign
verifier trusts our export's issuer is that verifier's decision, as whether ours
trusts a VC's issuer is a persona's (SPEC-0004 §4.4). The source's further point,
that it implies no transitive trust model, is the subject of R4.

### A3. Must-understand, at the grain of a context

<!-- q L391 "Application developers MUST understand" .. "used by their application." -->
> Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application.

<!-- q L2876 "If a conforming document does not use" .. "in the @context property." -->
> If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.

<!-- q L4105 "If such operations are performed" .. "verification failure." -->
> If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.

Ours, P5 (accepted):

<!-- qm spec/ARCH-0002-key-relative-naming.md L391-396 "**All three are required." .. "other way round." -->
> **All three are required. None may be skipped, and a failure at any level is a rejection, never a repair.** Beyond the three: **an unknown field in a signed payload is an error, not something to skip.** The default is must-understand; skippability is opt-in and explicit, never the other way round.

**Agreement in direction, at a coarser grain (inferred).** P5 makes an unknown
field an error. L391 makes it the application's duty to understand every
context it uses, L2876 makes a document that uses undefined terms say so in its
`@context`, and L4105 makes an expansion error a verification failure.
**Consequence for an import:** accept a VC only when every `@context` entry is
one our importer understands, known by URL and digest (§5.3 below), and reject
one that names the undefined-terms context (R2). Appendix A.1 points the other
way at the grain of a claim:

<!-- q L4024 "A verifier's validation of a verifiable credential will fail" .. "will be ignored." -->
> A verifier's validation of a verifiable credential will fail when mandatory claims are not included, and any claim that is not associated with the specific type will be ignored.

but A.1 is non-normative, so rejecting an unassociated claim costs no
conformance to **this** source. The normative ignore rule a VC importer meets is
VC-JOSE-COSE's, on that route only (the JOSE-COSE sibling's reject 2 and open
question 6).

### A4. The credential's validity window is the statement's

<!-- q L2030 -->
> If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past. Note that this value represents the earliest point in time at which the information associated with the credentialSubject property becomes valid. If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.

<!-- q L2267 -->
> If validFrom and validUntil are not present, the verifiable credential validity period is considered valid indefinitely. In such cases, the verifiable credential is assumed to be valid from the time the verifiable credential was created.

L2267 is a note. Ours, SPEC-0002 §7.3:

<!-- qm spec/SPEC-0002-ksa-core.md L430-432 -->
> A statement is **valid at time t** if and only if `not-before ≤ t` when `not-before` is present and `t < not-on-or-after` when `not-on-or-after` is present. A missing bound is unbounded on that side.

**Adopted, consistent with both siblings** (the JOSE-COSE sibling's adopt 4, the
DI sibling's A6): `not-before` becomes `validFrom`, `not-on-or-after` becomes
`validUntil`, and a missing bound stays missing. Two details are not exact —
the window's end point, and a window that is empty — and B3 takes them.

### A5. Times in UTC, written with `Z`

<!-- q L3168 "For this reason, implementers are urged" .. "Daylight Saving/Summer Time." -->
> For this reason, implementers are urged to use time values that are more universal, such as values anchored to the Z time zone over values that are affected by Daylight Saving/Summer Time.

<!-- q L3169 "In order to reduce misinterpretations" .. "with a time zone offset relative to UTC." -->
> In order to reduce misinterpretations between different time zones, all time values expressed in conforming documents SHOULD be specified in dateTimeStamp format, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

Ours, SPEC-0002 §4.4:

<!-- qm spec/SPEC-0002-ksa-core.md L241-243 -->
> In the human-review form (§11) a time is written exactly as `YYYY-MM-DDTHH:MM:SSZ`: upper-case `T` and `Z`, no fraction, no offset, seconds `00`–`59`. Any other spelling MUST be rejected, not normalised.

**Adopted for export.** Our human-form time is a valid `dateTimeStamp`: both of
TV-5's times, decoded from its TBS in this pass (`2026-10-06T00:00:00Z` and
`2026-10-06T11:00:00Z`), match Example 32's expression, reassembled from L3174
to L3178 and run by script (2 examined, 2 match). The export writes the string
unchanged. Import is B3.

### A6. A linked resource's digest is computed, never asserted

<!-- q L2889 -->
> Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.

<!-- q L2895 -->
> A conforming verifier implementation that makes use of a resource based on the id of a relatedResource object inside a conforming document with a corresponding cryptographic digest appearing in a relatedResource object value MUST compute the digest of the retrieved resource. If the digest provided by the issuer does not match the digest computed for the retrieved resource, the conforming verifier implementation MUST produce an error.

Ours, SPEC-0003 §4.2 and §4.4:

<!-- qm spec/SPEC-0003-ksa-definitions.md L163-167 "A verifier that obtains a definition body" .. "never asserted." -->
> A verifier that obtains a definition body MUST decode it with the validating decoder of SPEC-0002 §4.3 and MUST recompute its DefinitionId; if the result differs from the DefinitionId it was looking for, the body MUST be rejected. A DefinitionId is computed, never asserted.

<!-- qm spec/SPEC-0003-ksa-definitions.md L178-181 "Every such source" .. "accepted only by §4.2." -->
> Every such source is a **locator**: a hint for retrieval, never an identity. Content obtained from a locator is accepted only by §4.2.

**The same rule for linked content.** A conforming verifier that uses a related
resource recomputes its digest and fails on a mismatch, exactly as SPEC-0003
§4.2 treats a definition fetched from a locator. What differs is identity: here
the `id` URL names the resource and the digest checks it; there the digest *is*
the name. B4 uses the source's rule to carry ours.

### A7. No status mechanism: short validity instead

<!-- q L2340 "Defining the data model, formats, and protocols for status schemes" .. "out of the scope of this specification." -->
> Defining the data model, formats, and protocols for status schemes is out of the scope of this specification.

<!-- q L2341 "Credential status specifications MUST NOT enable tracking" .. "specific holder or subject." -->
> Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject.

Ours, R-O-02 and ADR-0003 D5:

<!-- qm spec/ARCH-0001-authorization-attestation.md L326 "Short-lived validity" .. "still representable." -->
> Short-lived validity preferred over revocation-heavy design; revocation still representable.

<!-- qm spec/ADR-0003-ksa-core-decisions.md L51 "Short validity remains recommended" .. "not solved here." -->
> Short validity remains recommended; revocation distribution is not solved here.

**Adopted, as both siblings did.** `credentialStatus` is defined only if present
(L2272), so an export omits it. KSA has `revoke` (SPEC-0002 §8.7) and no
distribution for it; the source defines no status scheme and forbids one that
reports a verifier's interest to the issuer. An exported VC is unrevocable in
practice, so its `validUntil` is short.

**And a limit no export can remove.** §1.3:

<!-- q L231 "Optional properties MAY be ignored" .. "conforming verifier implementations." -->
> Optional properties MAY be ignored by conforming issuer implementations and conforming verifier implementations.

`validFrom` and `validUntil` are optional (each is defined only when present,
L2030, L2032), and so is `relatedResource`. A conforming verifier may therefore
ignore the short window the export relies on instead of revocation, and the
digests B4 adds. R-O-02's preference still holds for what we emit; what a
foreign verifier enforces is its own policy *(inferred)*. Neither sibling's
mapping records this, because it is a property of the data model, not of a
route; the R-I-01 table should (§6.3).

### A8. The transformation is declared one-way

<!-- q L3199 "If conceptually aligned digital credential formats" .. "The transformation specification —" -->
> If conceptually aligned digital credential formats can be transformed into a conforming document according to the rules provided in this section, they are considered "compatible with the W3C Verifiable Credentials ecosystem". Specification authors are advised to adhere to the following rules when documenting transformations that enable compatibility with the Verifiable Credentials ecosystem. The transformation specification —

<!-- q L3200 -->
> MUST identify whether the transformation to this data model is one-way-only or round-trippable.

<!-- q L3201 -->
> MUST preserve the @context values when performing round-trippable transformation.

Ours, SPEC-0001 §5.3:

<!-- qm spec/SPEC-0001-ksa-architecture.md L229-232 -->
> A wallet MAY import a signed object from another protocol as an **external statement**, keeping its original bytes and mapping its speaker, subject and claims through an interchange profile (ARCH-0001 §6), so that it can be reasoned about by the same evaluation.

**Adopted.** Our export is a translation the export key signs; nothing in a VC
becomes a KSA statement, and an imported VC is an external statement that keeps
its bytes. So the R-I-01 table for VCs declares the transformation
**one-way-only**, and L3201 does not apply to it. The rest of §5.11 is §6.2
below.

### A9. Hand the application only what was secured

<!-- q L3219 "Securing mechanism specifications MUST provide a verification algorithm" .. "and signatures." -->
> Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures.

Ours, SPEC-0002 §11.1:

<!-- qm spec/SPEC-0002-ksa-core.md L680-681 "The human form is never itself signed or hashed" .. "exact view of them." -->
> The human form is never itself signed or hashed — the bytes are the statement, and the YAML is an exact view of them.

**Corroboration, nothing to change.** The DI sibling's A2 found the same intent
in Data Integrity; here it is a MUST on every securing mechanism. An importer
reads claims only from the `document` §7.1 returns (L3360).

### A10. A fixed core vocabulary, held rather than fetched

<!-- q L4103 "Implementations MUST treat the base context value" .. "as already retrieved;" -->
> Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved;

Ours, DEC-008's proposed answer (draft) and SPEC-0002 §8.1:

<!-- qm spec/ARCH-0002-key-relative-naming.md L576-580 "**Key-local is wrong for the core.**" .. "has no floor." -->
> **Key-local is wrong for the core.** Signature verification, canonicalization, the reduction algorithm, and **the definition of what "valid" means** must stay fixed. The reason is short: *if a key may define how its own statements are validated, it may define them as always-valid.* A model whose floor is key-relative has no floor.

<!-- qm spec/SPEC-0002-ksa-core.md L477 -->
> A verifier MUST reject a statement whose kind is not registered.

**The same floor (inferred).** The base context is not fetched, not chosen and
not key-local: every implementation holds it, named by URL and checked by a
digest the Recommendation prints. SPEC-0002's registry of kinds plays the same
part for KSA. Both keep the definition of *valid* out of any key's reach. What
the two do differently with the digest is §5 below.

---

## 2. What we adapt, and how

### B1. The signer is returned beside the issuer; our importer binds the two

§7.1's result carries the verification method's controller, not a judgement
about it:

<!-- q L3362 -->
> a controller of the verification method associated with the securing mechanism (string controller)

<!-- q L3363 -->
> a controlled identifier document that is associated with the verification method used to verify the securing mechanism (map controlledIdentifierDocument)

and the validation appendix, non-normatively, leaves the binding open:

<!-- q L4037 "This metadata includes identification" .. "respective issuer or holder." -->
> This metadata includes identification of the verified controller of the verification method used by the securing mechanism to secure each verifiable credential or verifiable presentation, of which the controller is typically the respective issuer or holder.

<!-- q L4038 -->
> Some ecosystems might have more complex relationships between issuers and controllers of verification methods and might use lists of verified issuers in addition to, or instead of, the mapping described above.

Ours, P2 (accepted):

<!-- qm spec/ARCH-0002-key-relative-naming.md L146-148 "Per SDSI and SPKI" .. "saying meaningful." -->
> Per SDSI and SPKI, **the speaker is the key.** There is no separate notion of "who signed this" versus "who said it", and no authority above A that makes A's saying meaningful.

**Adaptation (ours):** an importer requires §7.1's `controller` to equal
`issuer` (or `issuer.id`) and refuses to treat a VC that verifies and fails
the check as a statement by its issuer. On export the binding holds by
construction: the issuer is the export key's own URL form (B2). This is the
DI sibling's B1, here grounded in the data model's own verifier output rather
than in one securing mechanism. It narrows what the source leaves open:
**constrains**. One consequence for R-O-01 *(inferred)*: §7.1 returns a
controller and a controlled identifier document, not a key, and an imported
issuer key has a `KeyId` only if it is a key of a KSA suite — today Ed25519;
a P-256 issuer has none while suite 2 is reserved (SPEC-0002 §6.2).

### B2. The issuer is a URL, so a KSA `kid` needs a URL spelling

<!-- q L1280 -->
> A verifiable credential MUST have an issuer property.

<!-- q L1282 -->
> The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way. It is RECOMMENDED that the URL be one which, if dereferenced, results in a controlled identifier document, as defined in the Controlled Identifiers v1.0 specification, about the issuer that can be used to verify the information expressed in the credential.

<!-- q L425 "The id property is OPTIONAL." .. "which MAY be dereferenceable." -->
> The id property is OPTIONAL. If present, id property's value MUST be a single URL, which MAY be dereferenceable.

<!-- q L421 "Example id values include UUIDs" .. "DIDs (did:example:1234abcd)." -->
> Example id values include UUIDs (urn:uuid:0c07c1ce-57cb-41af-bef2-1b932b986873), HTTP URLs (https://id.example/things#123), and DIDs (did:example:1234abcd).

Ours, ADR-0005:

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L37-38 "a 32-octet byte string" .. "(`SPEC-0002` §11)." -->
> a 32-octet byte string, `SHA-256(public-key encoding)` (`SPEC-0002` §4.5). Text renderings are presentation only (`SPEC-0002` §11).

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L71 "the key type is named by a multicodec code" .. "by our reading of P1" -->
> the key type is named by a multicodec code, from a registry maintained outside the project — a registry in the identifier, by our reading of P1

<!-- qm spec/ADR-0005-dec-003-key-identifier.md L72 "a rendering of the same digest" .. "never signed" -->
> a rendering of the same digest; kept for display, never signed

**The gap (inferred), shared with both siblings' open question 2.** In a VC the
URL spelling of a `kid` **is** signed, inside the payload, by the export key —
the thing ADR-0005 rejected for natively signed bytes, with no boundary form
defined in its place. The source asks less than it seems to: an `id` MAY
dereference, and an issuer URL is only RECOMMENDED to dereference to a
controlled identifier document, so a non-dereferenceable form meets every MUST
here and declines one RECOMMENDED. L421 shows the source counting a `urn:uuid:`
and a DID as URLs. **Adaptation (ours):** one boundary URL form for a `kid` — a
fixed, lossless text spelling of the 32 octets under a URL scheme — recorded as
lossy per R-I-01 (the scheme and spelling are boundary-only), and used for
`issuer`, `credentialSubject.id` and every value of an `@id`-typed term (§5.4
below). Which scheme is open question 2.

### B3. Time: offsets, fractions, the end point, and an empty window

<!-- q L2032 -->
> If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future. Note that this value represents the latest point in time at which the information associated with the credentialSubject property is valid. If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.

Ours, SPEC-0002 §4.4:

<!-- qm spec/SPEC-0002-ksa-core.md L231-232 -->
> A time is an integer `T` derived from `s`, the number of seconds since 2026-01-01T00:00:00Z (negative before it):

**Import.** A `dateTimeStamp` with an offset maps to one KSA time. That is
reading a lexical form, not repairing one: the source declares no canonical
lexical form for time — its one canonical mapping is the `sriString`
datatype's (L4151, L4152) — so P5.1 does not reach it *(inferred)*:

<!-- qm spec/ARCH-0002-key-relative-naming.md L412-414 "Where a profile declares a canonical encoding" .. "canonical form." -->
> Where a profile declares a canonical encoding, a decoder SHALL **reject** input that is not in that profile's canonical form.

KSA has whole seconds, so a fraction is rounded **inward** — `validFrom` up,
`validUntil` down (ours) — and the imported window never widens. A time without
an offset is R1.

**The end point.** L2032 describes `validUntil` twice: as the moment validity
ends, and as the last moment at which the subject's information still holds.
Read by its second sentence the bound is inclusive (D4); KSA's `not-on-or-after` is
exclusive (A4). Exporting `T` as `T` lets a foreign verifier honour the
credential at instant `T` itself; exporting `T − 1 s` is exact under the
inclusive reading at KSA's one-second resolution. Both siblings' tables record
the mapping as preserved, which holds to within that one instant. Open
question 3.

**An empty window.** SPEC-0002 states no order between `not-before` and
`not-on-or-after` (§7.3 defines validity only), so a statement may be valid at
no time. L2030 and L2032 require `validFrom` no later than `validUntil`. With
equal bounds the plain mapping emits a credential valid at one instant under the
inclusive reading; with `T − 1 s` it emits a non-conforming document.
**Adaptation (ours):** the exporter refuses a statement whose window is empty.

### B4. `relatedResource` carries our DefinitionIds, and our context's digest

<!-- q L391 "Other specifications that build upon this specification MAY require" .. "effectively equivalent mechanism." -->
> Other specifications that build upon this specification MAY require that JSON-LD contexts be integrity protected by using the relatedResource feature described in Section 5.3 Integrity of Related Resources or any effectively equivalent mechanism.

<!-- q L2885 -->
> | id | The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers. The value MUST be unique among the list of related resource objects.

<!-- q L2893 -->
> Any object in the verifiable credential that contains an id property MAY be annotated with integrity information by adding either the digestSRI or digestMultibase property, either of which MAY be accompanied by the additionally optional mediaType property.

<!-- q L2896 "At the time of this writing sha384 SHOULD" .. "by implementers." -->
> At the time of this writing sha384 SHOULD be considered the minimum strength hash algorithm for use by implementers.

Ours, ARCH-0001 §6's W3C VC row, ADR-0003 D1 and SPEC-0002 §4.5:

<!-- qm spec/ARCH-0001-authorization-attestation.md L356 "W3C VC |" .. "must be pinned" -->
> W3C VC | I | C | ArtifactStatement or NameCert depending on type | Context must be pinned

<!-- qm spec/ADR-0003-ksa-core-decisions.md L47 "**Type identity is key-relative and hash-identified.**" .. "that definition's definer." -->
> **Type identity is key-relative and hash-identified.** A type is identified by the `DefinitionId` — the hash of its definition's canonical encoding — and a label local to that definition's definer.

<!-- qm spec/SPEC-0002-ksa-core.md L251 -->
> | **DefinitionId** | SHA-256 of the definition body's KSA-CBOR encoding (SPEC-0003 §4) | 32 octets |

**Adaptation (ours):** our export profile is a specification that builds on
this one, so it may require, as L391 allows, a `relatedResource` entry for our
documented context and for every definition an exported claim cites — `id` the
locator URL, `digestSRI` its SHA-256 [the SRI token syntax is outside this
source]. A verifier that fetches either then MUST recompute and compare
(L2895): SPEC-0003 §4.2's rule, enforced by a foreign verifier. On the
JOSE-COSE route this closes what that route leaves open — the payload's
`@context` URLs are signed, the bytes they name are not *(inferred: the signed
payload is the credential's own JSON, the JOSE-COSE sibling's adopt 1)*. **Costs.** A DefinitionId is SHA-256 and fixed, below
L2896's SHOULD; the source pins its own base context with SHA2-256 (L4103; D9).
A SHA-384 digest of the same bytes alongside meets the SHOULD without touching
the DefinitionId (L2887 allows more than one digest, *inferred*). And
`digestMultibase` names a multihash code from the multiformats tables, a
central allocator (the DI sibling's §4.2 item 4), where `digestSRI` names the
algorithm by a token SRI fixes [outside this source]: prefer `digestSRI`. So
the row's loss note becomes **context and definitions pinned by digest, inside
the signed credential**.

### B5. Type identity rides inside the term URL

<!-- q L2869 -->
> New terms MUST define a new URL for each term. When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular:

<!-- q L2870 -->
> Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.

<!-- q L2873 "Furthermore, a machine-readable description" .. "type of the property value." -->
> Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary. This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value.

Ours, P1 and SPEC-0003 §5.2:

<!-- qm spec/ARCH-0002-key-relative-naming.md L67 "An extension point is a pair" .. "label)`**." -->
> An extension point is a pair: **`(defining key, local label)`**.

<!-- qm spec/SPEC-0003-ksa-definitions.md L199-200 -->
> A label matches `[a-z][a-z0-9-]{0,62}`. Labels are local to their definer (ARCH-0002 P1): `(DefinitionId, label)` is globally unique; the label alone is not.

**Adaptation (ours), the DI sibling's B5 reached from the data model.** Every
exported type's term URL embeds its DefinitionId and label, so P1's pair
survives in the expanded IRI whatever a verifier does with contexts, and the
host in the URL is a locator, not the identity *(inferred)*. L2870's
documentation is the definition's own rendering (SPEC-0003 §10), which already
carries names and short and long descriptions in several languages (P3).

### B6. Our documented context, as the base context forces it

<!-- q L2875 -->
> When processing the active context defined by the base JSON-LD Context document defined in this specification, compliant JSON-LD-based processors produce an error when a JSON-LD context redefines any term. The only way to change the definition of existing terms is to introduce a new term that clears the active context within the scope of that new term. Authors that are interested in this feature should read about the @protected keyword in the JSON-LD 1.1 specification.

<!-- q L3257 "JSON-LD compacted document form MUST be used" .. "application/vp media type." -->
> JSON-LD compacted document form MUST be used for all representations of the data model using the application/vc or application/vp media type.

<!-- q L3262 -->
> In-line declaration of JSON-LD contexts in the @context property

Measured (§5.2 below): all 94 term definitions of the base context are
protected, among them 13 top-level names from the IANA JWT and JOSE registries,
`kid`, `iss` and `sub` included. **Adaptation (ours):** our context defines no
term the base context defines — a redefinition is an error — so no KSA field is
exported under the name `kid`, `iss` or `sub`. No `@vocab`, no `@base`, no
inline context, terms used in compacted form; a static, versioned file published
at a URL that embeds its own SHA-256 (L2862 lists content-addressed URLs among
the ways to keep a context available), and pinned by B4.

### B7. Arrays: sets as sets, sequences as lists

<!-- q L3269 -->
> In general, a JSON array is ordered, while a JSON-LD array is not ordered unless that array uses the @list keyword.

<!-- q L3272 -->
> If JSON structure or ordering is important to your application, we recommend you mark such elements as @json via an @context that is specific to your use case. An example of such a declaration is shown below.

Ours, SPEC-0002 §4.1, and what ADR-0004 left owed:

<!-- qm spec/SPEC-0002-ksa-core.md L185 -->
> | **array** | ordered; order is significant and signed |

<!-- qm spec/ADR-0004-dec-002-encoding.md L105-108 -->
> - **Condition (5), the order of set-valued arrays.** `SPEC-0003` sorts range values; `SPEC-0002`'s `trusts`, `allow-keys` and `exclude-keys` are arrays whose order is signed and unstated, so two producers can emit one set as two byte strings. Owed to `SPEC-0002`.

**Adaptation (ours, inferred).** A KSA array whose meaning is a set — `range`
values, `trusts`, `allow-keys`, `exclude-keys` — is exported as a plain array,
deduplicated and in one fixed order, so the JSON-LD reading (a set) is its
meaning and the octets under JOSE or COSE are deterministic. An array whose
order carries meaning is exported with `@list` or `@json`. **Why it matters:** one
exported array is a set under a Data Integrity suite that canonicalises RDF and
an ordered sequence under JOSE or COSE (L3269), and a duplicate, which an RDF
graph does not keep [outside this source], vanishes on one route and survives on
the other. ARCH-0001 records exactly such a value as passing V8:

<!-- qm spec/ARCH-0001-authorization-attestation.md L431-434 "**Still owed:**" .. "with condition (5)." -->
> **Still owed:** `trusts: [A, A]` with `threshold: 2` passes V8, since `SPEC-0002` has no distinctness rule and `SPEC-0004` §6.4 counts distinct kids. It fails closed; it goes to `SPEC-0002` with condition (5).

So the export needs condition (5)'s rule before ADR-0004's owed text exists.

### B8. §7.1's outcomes onto our three results

<!-- q L3358 "This section contains an algorithm that conforming verifier implementations MUST run" .. "returns a map that contains the following:" -->
> This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation. This algorithm takes a media type (string inputMediaType) and secured data (byte sequence inputData) and returns a map that contains the following:

<!-- q L3368 -->
> Set the verifyProof function by using the inputMediaType and the Securing Mechanisms section of the Verifiable Credential Extensions document, or other mechanisms known to the implementation, to determine the cryptographic suite to use when verifying the securing mechanism. The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.

Ours, SPEC-0002 §9.1:

<!-- qm spec/SPEC-0002-ksa-core.md L611-615 -->
> | result | meaning | |---|---| | **verified** | the statement is well-formed and was signed by the key named by `says` | | **invalid** | it is malformed, or its signature does not verify; it MUST NOT be used | | **unverifiable** | it may be valid, but this verifier cannot tell: unsupported suite, or no key for `says` |

**Adaptation (ours), as the DI sibling's B4 did for Data Integrity.**
`CRYPTOGRAPHIC_SECURITY_ERROR` is **invalid** `signature`;
`MALFORMED_VALUE_ERROR` and `RANGE_ERROR` are **invalid** `structure`;
`PARSING_ERROR` is **invalid** `encoding`; a media type for which no
`verifyProof` function can be determined is **unverifiable** `suite`. §7.1
defines no outcome for that last case — step 1 has no failure branch (D2) — and
no result that separates an undecided verification from a failed one, which
SPEC-0002 §9.1 requires *(inferred)*.

---

## 3. What we reject, and why

### R1. Reading a time without an offset as UTC

<!-- q L3169 "Time values that are incorrectly serialized" .. "interpreted as UTC." -->
> Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.

<!-- q L230 -->
> A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.

Ours, P5 (accepted):

<!-- qm spec/ARCH-0002-key-relative-naming.md L391-392 "a failure at any level is a rejection" .. "never a repair." -->
> a failure at any level is a rejection, never a repair.

**Rejected — and here the licence is a MUST, where the DI sibling's R2 declined
a MAY.** L2030 makes a `validFrom` without an offset non-conforming, L230
requires a conforming verifier to produce errors for a non-conforming document,
and L3169 requires the same value to be read as UTC. The source pulls both ways
(D5). Our importer rejects such a credential with an error and never uses the
repaired value; our exporter always writes `Z` (A5). Whether that meets L3169
turns on whether *interpreted* means *accepted*; it meets L230 as written
*(inferred)*.

### R2. Undefined terms, `@vocab` and the examples context, on import

<!-- q L415 "Implementations are expected to not use this URL" .. "production systems." -->
> Implementations are expected to not use this URL for any other purpose, such as in pilot or production systems.

<!-- q L3264 "they are urged to understand that any use of @vocab" .. "previous @vocab declaration(s)." -->
> they are urged to understand that any use of @vocab will disable reporting of "undefined term" errors, and later use(s) will override any previous @vocab declaration(s).

Measured: the undefined-terms context and the examples context are each one
`@vocab` mapping and nothing else (90 and 84 octets; `@vocab`
`https://www.w3.org/ns/credentials/undefined-term#` and
`https://www.w3.org/ns/credentials/examples#`). **Rejected on import, never
emitted.** An issuer that uses undefined terms MUST say so (L2876, quoted in A3),
and our importer reads that declaration as saying the payload carries fields
nobody defined, and rejects it (P5). The examples context is the same mechanism under
another IRI, which L415 keeps out of production. The MUST binds the producer;
what a consumer does with such a document is not stated, so rejecting it is a
choice the source leaves open *(inferred)*.

### R3. A JSON-LD context as our vocabulary; a vocabulary trusted by publication

<!-- q L2348 -->
> It is important to understand that data schemas serve a different purpose from the @context property, which neither enforces data structure or data syntax nor enables the definition of arbitrary encodings to alternate representation formats.

Ours, P3 (accepted), ADR-0003's rejected alternative, and the proposal's
DEC-007 option 4:

<!-- qm spec/ARCH-0002-key-relative-naming.md L201 -->
> A type is not a bare label. It is a **schema** that carries, together:

<!-- qm spec/ADR-0003-ksa-core-decisions.md L66-67 "**Unsigned vocabulary documents.**" .. "`define` statement." -->
> **Unsigned vocabulary documents.** Whether to rely on a vocabulary would not be a trust question; KSA publishes definitions with a signed `define` statement.

<!-- qm spec/ARCH-0001-PROPOSAL-v0.2.0.md L337 "Reuse an existing vocabulary mechanism" .. "SHACL)." -->
> Reuse an existing vocabulary mechanism (SKOS, JSON-LD contexts, SHACL).

**Rejected as our type system; used at the boundary.** By the source's own
account a context names terms and coerces values; structure belongs to
`credentialSchema` (§4.11) and meaning to the documentation at each term URL
(L2870). Measured: the base context's 94 term definitions — 76 IRI mappings and
18 aliases of `@id` and `@type` — carry 48 type coercions between them, and
nothing else: no description, no constraint beyond a datatype. P3's type carries representation, constraints,
semantics, review tags and multilingual short descriptions together; a context
carries the first, in part. And the base context is trusted because a
Recommendation prints its digest (A10): an unsigned vocabulary document trusted
by publication, the alternative ADR-0003 rejected, as the DI sibling's R4 found
for Data Integrity's context validation. **Evidence against DEC-007 option 4**
(a proposal): our definitions do the job, and an export's context is generated
from them (B5, B6).

### R4. Delegation and thresholds, exported as if a foreign verifier could evaluate them

<!-- q L2622 "The data model detailed in this specification does not imply" .. "Certificate Authority systems." -->
> The data model detailed in this specification does not imply a transitive trust model, such as that provided by more traditional Certificate Authority trust models. In the Verifiable Credentials Data Model, a verifier either directly trusts or does not trust an issuer. While it is possible to build transitive trust models using the Verifiable Credentials Data Model, implementers are urged to learn about the security weaknesses introduced by broadly delegating trust in the manner adopted by Certificate Authority systems.

<!-- q L3492 -->
> Verifiable credentials that are bearer credentials are made possible by not specifying the subject identifier, expressed using the id property, which is nested in the credentialSubject property. For example, the following verifiable credential is a bearer credential:

Both are notes or non-normative sections. Ours, SPEC-0004 §6.3 and SPEC-0002
§8.6:

<!-- qm spec/SPEC-0004-ksa-trust-evaluation.md L284-285 -->
> **Widening fails the path.** If any condition fails, `s` is not followed; no partial or repaired version of it is.

<!-- qm spec/SPEC-0002-ksa-core.md L538-542 "In the" .. "MUST be absent." -->
> In the **threshold form**, `this` is absent, `trusts` lists two or more keys, and `threshold` is an integer `n` with 1 ≤ n ≤ the number of keys: the trust is extended to any `n` of them acting together (SPEC-0004 §6.4). Otherwise `this` MUST be present and `trusts` and `threshold` MUST be absent.

**Rejected: no export claims that a foreign verifier honours `may-delegate`,
`trusts` or `threshold`.** The data model has no delegation and no threshold,
and its trust model is one hop by design. KSA's delegation is the narrowing kind
— depth, ranges, key lists and a validity cap, each of which can only narrow —
and none of that machinery is visible to a VC verifier. A threshold `trust` has
no `this`, so its subject would carry no `id`, which §8.10 calls a bearer
credential: the opposite of a statement that needs *n* named keys acting
together. §6.2 below drops both, or carries them as data a foreign verifier
cannot evaluate; open question 1 asks whether what remains is R-I-06's subset.

### R5. Deciding a payload's media type by reading it

<!-- q L3325 "Implementers are urged to not raise errors" .. "acceptable in the given protocol." -->
> Implementers are urged to not raise errors when it is possible to determine the intended media type from a payload, provided that the media type used is acceptable in the given protocol.

<!-- q L3326 -->
> Parse the payload as a JSON document.

Ours, SPEC-0002 §13.6:

<!-- qm spec/SPEC-0002-ksa-core.md L855 "It MUST bound the work" .. "V4 succeeds." -->
> It MUST bound the work it performs on any input before V4 succeeds.

**Rejected for our importer.** §7.1 chooses the verifier from `inputMediaType`
(L3368). Deciding the media type by parsing the payload first is processing
unauthenticated input in order to choose how to authenticate it. Our importer
takes the precise media type, or the securing mechanism's own type indicator
(the JOSE-COSE sibling's adapt 1), and rejects a mislabel. The leniency is urged
in a non-normative subsection, so no conformance is lost.

### R6. KSA presentations as verifiable presentations

<!-- q L2467 "Verifiable presentations SHOULD be extremely short-lived" .. "provided by a verifier." -->
> Verifiable presentations SHOULD be extremely short-lived and bound to a challenge provided by a verifier.

R-I-06 exports credentials. A KSA presentation already carries an audience and
a nonce under its own proof of possession (SPEC-0001 §8.1), and the siblings
leave presentations native for route-specific reasons (the JOSE-COSE sibling's
reject 5). This source adds none against it, and none for it. **Rejected this
semester, by scope** (inferred).

---

## 4. MD-3, ADR-0004 and DEC-002 — what the data model fixes, whatever secures it

MD-3 reads:

<!-- qm project/meetings/2026-09-28.md L51-53 "CBOR data model" .. "one-way mapping." -->
> CBOR data model, no IANA tags, COSE as export only; type identity is `(defining key, label)` per P1; YAML is the human form with a canonical one-way mapping.

ADR-0004 accepted DEC-002 for option 5, and nothing in this section reopens it:

<!-- qm spec/ARCH-0001-authorization-attestation.md L375 "**Status: accepted 2026-10-25" .. "(ADR-0004-dec-002-encoding.md).**" -->
> **Status: accepted 2026-10-25 — option 5, by [`ADR-0004`](ADR-0004-dec-002-encoding.md).**

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

The section exists because an extraction that can only confirm is not
evidence, and because ADR-0004 was taken without a second reader. This source
is neither an envelope nor a proof: it is the **payload** both siblings'
mechanisms secure. So the member-by-member mapping `docs/extraction.md` asks of
a signing document becomes a different question — what does the data model fix
that holds **whichever** mechanism secures it — and the answer is the same
in kind as both siblings': an **export mapping with no import into native
form** (A8).

### 4.1 What the data model fixes, whatever secures it

| rule (locator, level) | on the enveloping route (vc+cose) | on the embedding route (Data Integrity) | here |
|---|---|---|---|
| `@context` present, base URL first (L391, L393; MUST) | the URL strings are signed octets; the documents they name are not | under RDFC the expanded IRIs are signed; under JCS only the strings | A3, B4, B6 |
| compacted JSON-LD form (L228, L3257; MUST) | the payload is that JSON | the secured document is that JSON | written once, from the statement |
| base context held, digest printed (L4103; MUST) | a verifier need not expand at all | expansion runs with it | A10, §5 |
| an expansion error is a verification failure (L4105; MUST, *if* expansion is performed) | only if the verifier expands | always, under RDFC | A3, item 6 below |
| every context understood (L391; MUST, on developers) | same | same | A3 |
| undefined terms declared (L2876; MUST) | same | same | R2 |
| `type` includes `VerifiableCredential` (L660, L662, L892; MUST) | same | same | B5 |
| `issuer` one URL (L1280, L1282, L3240; MUST) | `iss`, if present, MUST match it (JOSE-COSE sibling, adopt 2) | its key is the controller of the proof's method (DI sibling, B1) | B1, B2 |
| `credentialSubject` present (L1772, L1774; MUST) | same | same | §6.2 |
| `validFrom`, `validUntil`: `dateTimeStamp`, ordered (L2030, L2032; MUST); UTC (L3169) | never `nbf` or `exp`, which time the signature (JOSE-COSE sibling, adopt 4) | never `created` or `expires` (DI sibling, A6) | A4, A5, B3, R1 |
| `relatedResource` digests; a verifier that uses one MUST check it (L2883 to L2896) | closes the unsigned-context gap | adds integrity for what lies outside the proof | B4 |
| `credentialStatus` typed if present; no tracking (L2272 to L2276, L2341) | same | same | A7 |
| secured by at least one mechanism (L228; MUST); return only what was secured (L3219); an embedded proof secures every graph but its own (L3229) | the VC-JOSE-COSE route | the Data Integrity route | A9 |
| the verifier: media type and bytes in; parse first if the mechanism wants a map; conformance checked after (L3358 to L3373; MUST run) | bytes in | a parsed map in (DI sibling, §4.2 item 1) | A1, B8 |
| authorization not appropriate without a framework (L3183; non-normative) | same | same | §6.1 |
| a transformation into the model: direction, conformance, media type, tests (L3200 to L3205) | same | same | A8, §6.2 |

**Every row binds on both routes; only what is signed differs.** Under vc+cose
the octets are signed and nothing else; under Data Integrity a transformation is.
So R-O-05's verifier clauses are settled by the route and not by this data model
(item 6 below).

### 4.2 MD-3, clause by clause

<!-- q L3239 "The data model as described in Sections 3." .. "in a specific format." -->
> The data model as described in Sections 3. Core Data Model, 4. Basic Concepts, and 5. Advanced Concepts is the canonical structural representation of a verifiable credential or verifiable presentation. All syntaxes are representations of that data model in a specific format.

<!-- q L3239 "Although syntactic mappings are only provided for JSON-LD" .. "processing, validation, or comparison." -->
> Although syntactic mappings are only provided for JSON-LD, applications and services can use any other data representation syntax (such as XML, YAML, or CBOR) that is capable of being mapped back to application/vc or application/vp. As the verification and validation requirements are defined in terms of the data model, all serialization syntaxes have to be deterministically translated to the data model for processing, validation, or comparison.

| MD-3 clause | the data model | bearing |
|---|---|---|
| CBOR data model | an abstract graph is the canonical *structure* (L3239); CBOR is allowed only as a syntax that maps back, and a conforming document is compacted JSON-LD (L228, L3257) | a KSA-CBOR statement is never a VC; every export translates (both siblings) |
| no IANA tags | no CBOR tag anywhere; but the base context defines 13 top-level IANA JWT and JOSE names (§5.2) | item 1 below |
| COSE as export only | two RECOMMENDED mechanisms, neither required (L2391, L2392, L3235) | item 2 below |
| type identity `(defining key, label)` | a type is a term or a URL (L662), and every new term MUST have a URL (L2869) | B5; ADR-0001 permits it at the boundary |
| YAML the human form, one-way | the inverse direction: the structure is canonical and every syntax is translated to it (L3239) | below |

**The translation is P1's cost, not option 5's** *(inferred)*. L2869 makes
every new term a URL and §6.1 makes the document compacted JSON-LD. A statement
under option 3, JSON natively, would still need a context mapping each field to
a URL before it could be a VC, and P1 forbids URL-named fields natively under
every option (ADR-0001). So an export translates under any DEC-002 option that
keeps P1. The cost lands on P1, at the boundary where ADR-0001 already permits
it: **not a cut against option 5.**

**The data model has no canonical bytes, by design** *(inferred)*. It makes the
abstract structure canonical and leaves byte identity to the securing
mechanism, which is why the two Recommendations it names disagree about what is
signed: the octets as produced on one route, a canonicalisation on the other.
KSA fixes the bytes first and makes the YAML a view of them (SPEC-0002 §11.1).
Evidence for MD-3's direction, the inverse of this source's; it names no other
option.

### 4.3 Where this source cuts against ADR-0004 and option 5, or leaves them underdetermined

#### 1. Item 3's list does not reach the registries every VC's vocabulary carries

<!-- qm spec/ADR-0004-dec-002-encoding.md L46-50 "**No IANA registry is native.**" .. "lossily per R-I-01." -->
> **No IANA registry is native.** Named, because "no tags" was too narrow (`ARCH-0001` §7, inputs since v0.1.3): the native model depends on none of CBOR Tags, COSE Header Parameters, COSE Algorithms, CWT Claims, or CWT Confirmation Methods. Each may appear at an interchange boundary, mapped lossily per R-I-01.

Measured (§5.2): the base context maps 15 term definitions to IRIs under
`https://www.iana.org/assignments/jwt#` (10) and
`https://www.iana.org/assignments/jose#` (5) — 13 at the top level (`...`,
`_sd`, `_sd_alg`, `aud`, `cnf`, `exp`, `iat`, `iss`, `jku`, `kid`, `nbf`,
`sub`, `x5u`) and `cnf`'s scoped `kid` and `jwk`. They sit in the payload's own
vocabulary, protected, on **every** route. **Underdetermined.** The JOSE-COSE
sibling found item 3 silent on the JOSE registries of that route's envelope (its
§6.4 item 2); here the same registries are inside the data model. At the
boundary they are permitted, mapped lossily, and our export emits none of them
(B6). Open question 6.

#### 2. Item 4's envelopes meet the source's two mechanisms at one point

<!-- qm spec/ADR-0004-dec-002-encoding.md L51-52 "**COSE_Sign1 and DSSE are export envelopes only.**" .. "does not decide." -->
> **COSE_Sign1 and DSSE are export envelopes only.** *Which* envelope remains DEC-005, which this ADR does not decide.

<!-- q L3235 "There are multiple acceptable securing mechanisms" .. "verifiable presentations." -->
> There are multiple acceptable securing mechanisms, and this specification does not mandate any particular securing mechanism for use with verifiable credentials or verifiable presentations.

**Underdetermined, and the pressure is on DEC-005, as both siblings found.** Of
the two mechanisms the source RECOMMENDS, only vc+cose is inside item 4's set,
and DSSE is not a mechanism this source names; whether the VC Extensions list
one is outside this source.

#### 3. Condition (5) is owed, and the export needs it now

B7. ADR-0004 leaves the order of set-valued arrays to SPEC-0002; JSON-LD reads
an unmarked array as a set (L3269), so an exporter must fix one order — and drop
duplicates — before that rule exists. **Owed under every option; not a cut
against option 5.**

#### 4. A pinned digest names a serialization, not a meaning

<!-- q L4115 "Implementations that depend on RDF vocabulary processing MUST ensure" .. "used by implementations." -->
> Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative. Other semantically equivalent serializations of the vocabulary files MAY be used by implementations.

Measured: both printed digests this pass could check match the files fetched
(the base context against L4103, the credentials vocabulary against L4119). The
security vocabulary of L4121 and L4122, fetched by pass 2 (verify), matches by no
route: the Resolved Document L4121 names hashes to `8a16b6b5…`, what
`https://w3id.org/security` now redirects to hashes to `02c4b488…`, and VC Data
Integrity 1.0, published the same day, pins the JSON-LD serialization of the same
vocabulary URL to `082434d5…` against this source's `689af6f3…` (`normative.md`
SD-26, `schema/contexts.yaml`). Two Recommendations pinning one vocabulary URL to
two digests is the point of this item made by the W3C itself. A semantically
equivalent re-serialization, which the second sentence permits, would fail the
printed digest. Under one canonical encoding a meaning has one byte string and
one digest; option 4's two canonical forms would have two, which is B.2's MAY in
miniature. Ours:

<!-- qm spec/ADR-0004-dec-002-encoding.md L125-126 "Two canonical forms" .. "does not meet." -->
> Two canonical forms and a bijection nobody has specified, for no driver the single form does not meet.

**Evidence for ADR-0004's rejection of option 4**, and neutral among the
single-form options. Not a cut against option 5.

#### 5. A pinned digest freezes a defect, and the fix keeps the name

<!-- q L4107 "However, if critical errata are found" .. "might change." -->
> However, if critical errata are found in the specification and corrections are required to ensure ecosystem stability, the cryptographic hash values might change.

Measured: 4 of the base context's 8 XSD datatype coercions use the namespace
`https://www.w3.org/2001/XMLSchema#` (the file's lines 199, 309, 313, 329:
`statusSize`, `exp`, `iat`, `nbf`), where the XSD namespace — and the
credentials vocabulary's own `xsd` prefix — is `http://www.w3.org/2001/XMLSchema#`
(D8). The bytes are pinned, so a correction changes the digest under the same
URL. Ours:

<!-- qm spec/SPEC-0003-ksa-definitions.md L471-475 "A definition is never edited" .. "deprecated by policy." -->
> A definition is never edited: any change produces a new DefinitionId. A definer replaces a definition by publishing the new one with `supersedes` naming the old (SPEC-0002 §8.9). Supersession is honoured only when both have the same definer. Statements made under the old definition keep their meaning; a relying party MAY treat a superseded definition as deprecated by policy.

**Evidence for P4 and SPEC-0003's hash-as-identity** — under it a fix is a new
name and the old one keeps its meaning — not about DEC-002.

#### 6. Canonicalising at verification is the route's choice, not the data model's

L4105 binds only where expansion or a transformation to RDF is performed, and
§6.3, non-normatively, describes a consumer that runs no JSON-LD library:

<!-- q L3338 "Type-specific credential processing is defined as a lighter-weight mechanism" .. "doesn't require a JSON-LD software library." -->
> Type-specific credential processing is defined as a lighter-weight mechanism for processing conforming documents, that doesn't require a JSON-LD software library.

**So the data model requires no canonicaliser in the verifier** *(inferred)*, and
condition (3) holds or fails with the route: it holds for vc+cose (the JOSE-COSE
sibling's adopt 1) and fails for Data Integrity (the DI sibling's §5.3).
R-O-05, which has no force, meets no conflict in this source.

**Searched and found not to cut against option 5:**

- **Canonicalisation.** `canonical` occurs 3 times in the 5009 lines
  (case-insensitive): L3239's canonical structure and the `sriString` canonical
  mapping (L4151, L4152). The data model canonicalises nothing.
- **Condition (6), Unicode normalisation.** `normaliz`, `normalis` and
  `Unicode` occur 0 times; the one case-insensitive hit for `nfc` is inside a
  base64 `proofValue` (L3155).
- **Order-only divergence.** No rule on member order; what a reordering does is
  the route's matter. Under option 5 it fails at V5.
- **The CBOR data model, tags, deterministic CBOR.** `CBOR` occurs on 4 lines:
  a syntax that maps back (L3239), CBOR Web Tokens among the aligned formats
  (L3198), a pointer to cross-syntax strings (L3931), and its reference entry
  (L4352) — RFC 7049, which the library's `rfc-8949` record supersedes (D14).
  Nothing here constrains a native encoding.

### 4.4 DEC-002's options, scored against this source

| this source | option 1 | option 2 | option 3 | option 4 | option 5 (KSA-CBOR) |
|---|---|---|---|---|---|
| **A VC is compacted JSON-LD with URL-named terms** (L228, L2869) | translates | translates | translates: JSON natively, but its fields are not URLs (P1) | translates | translates and re-signs |
| **Registry names in the vocabulary** (§4.3 item 1) | boundary | native: fails P1 (ADR-0001) | boundary | ADR-0004's cell: fails through its option-2 half | boundary; item 3 underdetermined |
| **One digest per meaning** (§4.3 item 4) | one | one, under a deterministic profile | one (JCS) | **two** | one |
| **Sets in arrays** (§4.3 item 3) | owed | owed | owed; RFC 8785 cannot reorder (ADR-0004's strongest ground) | owed | owed (condition (5)) |
| **Canonicalisation at verification** (§4.3 item 6) | the route decides | the route decides | the route decides | the route decides | the route decides |

### 4.5 mofn report R-0006's VC row: the data-model half

<!-- qm research/0006-mechanism/report.md L232 "**∅** for VC" .. "record exists." -->
> **∅** for VC — no VC Data Model, Data Integrity or VC-JOSE-COSE record exists.

<!-- qm research/0006-mechanism/report.md L345 "the securing mechanism is **unsourced**" .. "until it is" -->
> the securing mechanism is **unsourced** in the library; the row's mapping cannot be evidenced until it is

With all three records extracted, the row's cells can be written. This record
supplies the data model's part; the siblings supply each route's.

- **Hashed:** by the data model itself, its base context and two vocabularies,
  SHA2-256 (L4103, L4119, L4122); and whatever an issuer lists in
  `relatedResource` (L2883 to L2896).
- **Canonicalised, and when:** nothing; the route decides (§4.3 item 6).
- **Signed:** whatever the mechanism secures — every graph but its own proof
  graphs, for an embedded proof (L3229) — and only that is returned (L3219).
- **Carried:** compacted JSON-LD, base context first (L228, L393).
- **What the verifier does:** §7.1 — verify, then check conformance (A1).
- **Where trust is placed:** out of scope, one hop (L2618, L2622).
- **What it leaves undefined:** issuer trust, status schemes (L2340),
  authorization (§5.9), validation (Appendix A, non-normative).

R-0006 is not edited here.

### 4.6 Net, stated as evidence

On ADR-0004's own criteria the data model is close to neutral: every option
translates, because P1 forbids URL-named fields natively, and where it leans it
leans toward having **one** canonical encoding (§4.3 items 4 and 5), which every
option but 4 offers. Its weight falls **outside DEC-002**: on item 3's list
(item 1), on DEC-005 (item 2), on condition (5) (item 3), on P4's hash-as-identity
(item 5), and on R-I-06's choice of kind (§6.1). Nothing here decides DEC-002
again.

---

## 5. The JSON-LD context files, against our canonicalisation and ADR-0004

### 5.1 What was fetched and checked

Fetched 2026-11-07 into the lane's scratch, outside the repository; this lane
committed nothing, but the schema lane copied the first four files byte-exact into
`schema/` (`*.verbatim.jsonld`, digests in `schema/contexts.yaml`; pass 2, verify,
checked them identical). Octets and SHA-256 recomputed in this pass.

| file | URL | octets | sha256 | the source's digest |
|---|---|---|---|---|
| base context | `https://www.w3.org/ns/credentials/v2` | 10131 | `59955ced6697d61e03f2b2556febe5308ab16842846f5b586d7f1f7adec92734` | L4103: **equal** |
| credentials vocabulary | `https://www.w3.org/2018/credentials/index.jsonld` | 21677 | `9db03c54d69a8ec3944f10770e342b33e58a79045c957c35d51285976fc467c4` | L4119: **equal** |
| undefined-terms context | `https://www.w3.org/ns/credentials/undefined-terms/v2` | 90 | `82dab514ba44eb18f5d1b0f638c5e140c6a556fbfb5089601bdc0fa5eb8b2581` | none printed |
| examples context | `https://www.w3.org/ns/credentials/examples/v2` | 84 | `57393fbc69d6efb9b9b5dc9cb6b9880b0944360abfe2eaf459c9e58cf2279d7c` | none printed |
| security vocabulary | `https://w3c.github.io/vc-data-integrity/vocab/security/vocabulary.jsonld` | 35407 (pass 2) | `8a16b6b592eb99e7e266afd0f01c50b0c33826f7a45a737e8f3c8c0e90ceec8c` (pass 2; not committed) | L4122: **differs** (`689af6f3…`; VC Data Integrity §2.4 prints `082434d5…` for the same URL) |

### 5.2 The base context, measured

By a script walking every term definition, scoped contexts included; each
count says what it examined.

- **94 term definitions, all protected**: `@protected` is set at the top level
  and in every scoped context. They are 76 IRI mappings and 18 aliases of
  `@id` and `@type`.
- **The 76 IRIs by namespace:** `https://www.w3.org/2018/credentials#` 23,
  `https://w3id.org/security#` 18, `https://www.w3.org/ns/credentials/status#`
  14, `https://www.iana.org/assignments/jwt#` 10, `https://schema.org/` 5,
  `https://www.iana.org/assignments/jose#` 5, `http://purl.org/dc/terms/` 1.
  B.2 pins two of the seven namespaces by digest. `name`, `description` and
  `mediaType` resolve into schema.org, whose digest the source declines to give
  (L4125); `created` into Dublin Core; the status and IANA IRIs are pinned by
  nothing.
- **15 IANA-registry terms** (§4.3 item 1), 13 of them at the top level.
- **48 type coercions:** 31 `@id`, 8 XSD datatypes, 3 multibase, 3 `@json`, 1
  `sriString`, 1 `cryptosuiteString`, 1 `@vocab`. Of the 8 XSD coercions, 4 use
  `http://www.w3.org/2001/XMLSchema#` (`dateTime`: `validFrom`, `validUntil`,
  `created`, `expires`) and 4 use `https://www.w3.org/2001/XMLSchema#`
  (`integer`, `nonNegativeInteger` ×3) — D8.
- **`validFrom` and `validUntil` are coerced to `dateTime`**, and the credentials
  vocabulary gives both the range `xsd:dateTime`; L2030 and L2032 require a
  `dateTimeStamp`. The machine-readable files do not carry the normative
  constraint (D8).
- **`proof` is a `@graph` container**; inside `VerifiablePresentation`,
  `verifiableCredential` is a `@graph` container with a null `@context`, so an
  embedded credential carries its own.
- **No top-level `@vocab`.** No term named `credentialRefresh` in either file (0
  occurrences), against B.2's base-class table (L4132; D7).
- **The credentials vocabulary** lists 18 properties, 14 classes and 1 datatype;
  `issuanceDate` and `expirationDate` carry the term status *deprecated*, and
  `confidenceMethod` and `renderMethod` *reserved*.

### 5.3 Against our stance

| question | the context files (B.1, B.2) | ours | bearing |
|---|---|---|---|
| what names a vocabulary | its URL (L393, L4103) | its DefinitionId, the hash of its canonical encoding (ADR-0003 D1) | B4, B5 |
| what checks it | a SHA-256 of one file's octets, printed in the Recommendation (L4103, L4119) | the same hash, recomputed on every fetch (SPEC-0003 §4.2) | A6 |
| what a re-serialization does | a new digest for the same meaning, and B.2 permits one (L4115) | cannot happen: one canonical encoding and a rejecting decoder (ADR-0004 items 1 and 2) | §4.3 item 4 |
| what a fix does | new bytes, same URL, new digest (L4107) | a new definition, a new DefinitionId, `supersedes` (SPEC-0003 §11.3) | §4.3 item 5 |
| who vouches for it | nobody signs it; a Recommendation prints its digest | its definer signs a `define` statement (SPEC-0003 §11.1) | R3 |
| where it is held | already retrieved (L4103) | the SPEC's own registries; definitions fetched from locators and checked | A10 |
| what processes it | the JSON-LD 1.1 algorithms [outside this source], run by the verifier where expansion is performed (L4105) | nothing interprets a vocabulary during single-statement verification (SPEC-0002 §9.2) | §4.3 item 6 |

**Net.** The context files are content-addressed in the **weak** sense:
identity by URL, integrity by a digest of one serialization, authority by
publication. KSA's definitions are content-addressed in the **strong** sense:
the digest is the identity, it covers the one canonical encoding, and
authorship is a signature. ADR-0004's single canonical encoding is what makes
the strong sense possible, and this source's own files show the weak sense's two
costs: a re-serialization fails its digest, and a fix keeps its name. For an
export the weak sense is what foreign verifiers have; B4 lays the strong sense
over it, since a `relatedResource` digest of a locator that serves the
definition body **is** the DefinitionId *(inferred)*.

### 5.4 A KSA `kid` is not a value for the base context's `kid`

The base context coerces `kid`, `iss`, `sub`, `aud`, `jku`, `x5u` and `cnf`'s
`kid` to `@id`: their values are IRIs. A KSA `kid` written as 64 hexadecimal
digits is, to a JSON-LD processor, a relative IRI reference; with no base IRI —
Data Integrity requires a null base URL when deserializing to RDF (the DI
sibling's §6.1 item 4) — it cannot become absolute, and it is dropped from the
RDF, which Data Integrity makes an error [JSON-LD 1.1, outside this source].
On the JOSE-COSE route no JSON-LD processing runs and nothing is lost.
**Consequence (inferred):** one exported credential would verify on one route
and fail on the other. This is the quiet naming collision P1.1 describes, in a
new place:

<!-- qm spec/ARCH-0002-key-relative-naming.md L106-107 "The collision is quiet because it is a naming one:" .. "too." -->
> The collision is quiet because it is a naming one: `SPEC-0002` §4.5 calls its **derived** identifier `kid` too.

Hence B2 (a key is always written in its URL form) and B6 (no KSA field under a
base-context name).

### 5.5 What our documented context must therefore be (draft, ours)

1. **Static and versioned**, published at a URL that embeds its own SHA-256
   (L2862), and listed in every export's `relatedResource` with that digest (B4).
2. **Complete**: every term an export uses is defined (L2876; R2), each with a
   URL that embeds its DefinitionId and label (B5), and documented by the
   definition's rendering (L2870).
3. **`@protected`**, as the base context is, and redefining none of its 94
   terms (L2875; B6).
4. **Plain**: no `@vocab`, no `@base`, no inline context, no full URLs in place
   of terms (L3260 to L3263).
5. **Explicit about arrays**: sets as plain arrays in one fixed order,
   sequences as `@list` or `@json` (B7).
6. **Typed for UTC**: every time a `dateTimeStamp` written with `Z` (A5).

---

## 6. R-I-06: an `AuthzCert` into this data model (draft)

Every row below is *(inferred)* or **ours**: the source defines no import or
export of anything.

### 6.1 First, which kind

<!-- q L3183 -->
> Verifiable credentials are intended as a means of reliably identifying subjects. While it is recognized that Role Based Access Controls (RBACs) and Attribute Based Access Controls (ABACs) rely on this identification as a means of authorizing subjects to access resources, this specification does not provide a complete solution for RBAC or ABAC. Authorization is not an appropriate use for this specification without an accompanying authorization framework.

<!-- q L3184 -->
> The Working Group did consider authorization use cases during the creation of this specification and is pursuing that work as an architectural layer built on top of this specification.

§5.9 is non-normative. Ours, R-I-06, ARCH-0001 §6's W3C VC row (quoted in B4),
P6 and ADR-0004's acceptance test:

<!-- qm spec/ARCH-0001-authorization-attestation.md L318 "Export a subset" .. "documented context." -->
> Export a subset of `AuthzCert` as a W3C Verifiable Credential using a documented context.

<!-- qm spec/ARCH-0002-key-relative-naming.md L312-314 -->
> `NameCert` is therefore not a *kind* of object — it is P2's form with a particular predicate type. The same holds for `AuthzCert` (delegation), `ArtifactStatement` (attestation) and `Endorse`.

<!-- qm spec/ADR-0004-dec-002-encoding.md L92-94 "round-trips KSA statements" .. "(`attestation`, TV-4)" -->
> round-trips KSA statements whose kinds carry the AuthzCert role (`trust`, TV-5) and the ArtifactStatement role (`attestation`, TV-4)

**§5.9 sides with the §6 row, not with R-I-06** *(inferred)*. The data model is
for identifying subjects and attesting claims about them, and it disclaims
authorization unless a framework comes with it. ARCH-0001 §6 maps a W3C VC to
`ArtifactStatement` or `NameCert`, attestation roles; R-I-06 exports
`AuthzCert`. P6 makes all three functions over one form, so an `attestation`
(TV-4's role, and TV-13's `NameCert` role) exports to a VC a foreign verifier
can take at its word, while a `trust` exports to a VC whose claim — in TV-5,
that Carol trusts Alice about a range of build-provenance values — is an
authorization only to a verifier that runs SPEC-0004. **The framework §5.9
asks for exists: it is SPEC-0004.** To any other verifier a `trust` export is an
attestation by Carol about Alice. Evidence for the JOSE-COSE sibling's open
question 9 and this file's open question 1; it decides neither.

### 6.2 TV-5, field by field

TV-5 is the vector ADR-0004 names for the `AuthzCert` role. Its TBS was decoded
in this pass, and its SHA-256 recomputed:
`723436bf3ca419bc57fdea0f2b6518f65d280d04c1928b618e9f70a58ce785e6`, equal to the
statement digest SPEC-0002 prints for it. It holds `kind` 5 (`trust`), `suite`
1, `says` Carol (`c7b66369…10e207`), `this` `[1, Alice]` (`21fe31df…9721b9`);
`valid` with `not-before` 2026-10-06T00:00:00Z and `issued`
2026-10-06T11:00:00Z, and no `not-on-or-after`; `about`, one range of DV-1's
`build-provenance` (`517007…3a7175`) over {`reproducible`, `attested`}; and
`may-delegate`, `depth` 1, `ranges` {`reproducible`}, `not-on-or-after`
2026-12-01T00:00:00Z.

| KSA (SPEC-0002) | TV-5 | VC 2.0 (locator) | mapping |
|---|---|---|---|
| the signed statement `[suite, says, tbs, sig, ? pub]` | — | nothing: the VC is a translation, secured by a §4.12 mechanism under the export key (L228) | **dropped, replaced** |
| statement digest, SHA-256(`tbs`) | `7234…85e6` | `id`: one URL, which MAY dereference (L425) — a URL spelling of the digest | **preserved by reference** (ours) |
| `kind` 5 and its DS label | `trust` | `type`: `VerifiableCredential` and our type's URL (L660, L662, L892; B5) | **respelled** |
| `suite` | 1 | nothing in the data model; the mechanism's own algorithm (siblings) | **not carried** |
| `says` | Carol | `issuer`, in the URL form (L1280, L1282; B2), equal to the securing key's controller (B1) | **respelled** |
| `this` = `[1, kid]` | Alice | `credentialSubject.id`, in the URL form (L1774; B2) | **respelled** |
| threshold form: `this` absent, `trusts`, `threshold` | — (TV-9) | no counterpart; a subject with no `id` reads as a bearer credential (L3492; R4) | **cannot be given foreign meaning** |
| `body.about` | build-provenance ∈ {reproducible, attested} | a claim on `credentialSubject` under our context: a term URL embedding DV-1's DefinitionId and the label (B5), the set as a plain array (B7), DV-1 pinned in `relatedResource` (B4) | **preserved as data**; its meaning only through DV-1 |
| `body.may-delegate` | depth 1 within {reproducible}, until 2026-12-01 | no counterpart: one-hop trust (L2622; R4) | **dropped**, or carried as data no foreign verifier evaluates (open question 1) |
| `valid.not-before` | 2026-10-06T00:00:00Z | `validFrom`, the same string (L2030; A4, A5) | **preserved** |
| `valid.not-on-or-after` | absent | `validUntil` absent: unbounded on both sides of the map (L2267; A4). When present: B3's end point | **preserved** |
| an empty window | — | refused (B3) | — |
| `valid.issued` | 2026-10-06T11:00:00Z | nothing: version 2 has no issuance property, and the vocabulary marks `issuanceDate` deprecated (§5.2); the mechanism's own time is the export's (siblings) | **dropped** |
| a `revoke` (§8.7) | — | `credentialStatus` needs a scheme (L2340) that does not track (L2341); we define none | **dropped**; short `validUntil` (A7) |
| the definitions cited | DV-1 | `relatedResource`: `id` a locator, `digestSRI` the DefinitionId (B4) | **preserved by digest**; below L2896's SHOULD |
| our documented context | — | `@context`: the base URL first, ours second (L393; §5.5), ours also in `relatedResource` | **ours** |
| a definition's language maps | DV-1's `names`, `short` | `name`, `description` of the credential, OPTIONAL (L922, L924), as language value objects (§11.1; D6) | **optional**: display text translated from the definition, signed by the export key |
| holder binding; presentations | — | none for a credential (R6) | **not exported** |
| — | — | no `@vocab`, no undefined-terms context (R2), no base-context term redefined (B6) | — |
| the transformation itself | — | §5.11 (L3200 to L3205), below | **owed** |

**What §5.11 adds to the R-I-01 table.**

<!-- q L3202 -->
> MUST result in a conforming document when transforming to the data model described by this specification.

<!-- q L3203 -->
> MUST specify a registered media type for the input document.

<!-- q L3204 -->
> SHOULD provide a test suite that demonstrates that the specified transformation algorithm to the data model in this specification results in a conforming document.

Ours, R-I-01, and the one media type our documents name:

<!-- qm spec/ARCH-0001-authorization-attestation.md L313 "Publish a mapping table" .. "dropped, or inferred." -->
> Publish a mapping table for each supported foreign format: what is preserved, dropped, or inferred.

<!-- qm spec/SPEC-0001-ksa-architecture.md L341 "a presentation carried as an attachment of media type" .. "`application/ksa-presentation`" -->
> a presentation carried as an attachment of media type `application/ksa-presentation`

**Constrains R-I-01.** A table that wants the label L3199 defines for KSA owes
three things a bare mapping does not: the direction (A8), a media type for
what it transforms that is **registered** (L3203), and a test suite. KSA statements have no media type in our
documents; the one they name is for presentations carried by email, and nothing
records its registration. Registering one with IANA is a registry act at the
boundary, which ADR-0001 permits; making it is a project decision (open
question 7). Without it the export still produces conforming documents — what
counts, in the note at L3207, is a conforming document under a securing
mechanism — but the transformation does not earn the label.

### 6.3 What a foreign verifier then has

- **It can** run §7.1; learn that the key behind Carol's URL issued a credential
  about the key behind Alice's, valid from 2026-10-06, carrying one claim under
  our context; and fetch DV-1 and check it against the digest (B4).
- **It cannot** follow `may-delegate`, evaluate a threshold (R4), learn of a
  revocation (A7) or a rotation (SPEC-0004 §7), tell that `issuer` names a KSA
  key unless it knows our URL form (B2), or tell an authorization from an
  attestation without SPEC-0004 (§6.1).
- **It need not** honour `validUntil` or check `relatedResource`: both are
  optional properties, which a conforming verifier MAY ignore (L231; A7). The
  R-I-01 table records the window and the digests as **emitted, not
  enforced**.

**So R-I-06's subset, read against this source** *(inferred, ours)*: the
one-hop, single-subject `trust` — or an `attestation` — with its `about` as
claims and its window as `validFrom` and `validUntil`, and nothing that needs
SPEC-0004 to be read correctly. Everything else is dropped or carried as data.
Open question 1.

---

## 7. Mapping to our decisions

Verdicts, exactly six, one per row, as the DI sibling defines them. **adopt**: we
take the source's rule or reasoning, or ours already says the same and the
source corroborates it. **adapt**: we take it with a stated change.
**constrains**: one side narrows what the other leaves open, and an
implementation can satisfy both by taking the narrower path. **conflicts**: no
object or implementation satisfies both. **silent**: one side does not reach
the other's subject. **reject**: we decline the source's rule, option or
pattern, with a reason. Levels are the source's as printed. Every locator of
ours is a line at `a56a3c0`.

| # | ours (locator) | source (locator) | verdict | where |
|---|---|---|---|---|
| 1 | R-I-06 (ARCH-0001 §5.2, L318) | §4.2 to §4.9; §5.9 L3183 | **constrains**: the data model fixes the export's shape, and §5.9 presses the choice of kind | §6 |
| 2 | R-I-01 (ARCH-0001 §5.2, L313) | §5.11 L3200 to L3205 | **constrains**: a direction, a registered input media type and a test suite are owed | §6.2 |
| 3 | R-I-02 (L314); SPEC-0004 §4.3 (L180, L181) | §5.1 L2618, L2622 (non-normative) | **adopt** | A2 |
| 4 | R-I-03 (ARCH-0001 §5.2, L315) | §4.12 L2391, L2392 | **silent**: the data model secures nothing; the envelopes are the siblings' matter | §4.1 |
| 5 | §6 W3C VC row, its native mapping (ARCH-0001 §6, L356) | §5.9 L3183 | **adopt**: the row's attestation roles are the use the source admits | §6.1 |
| 6 | §6 W3C VC row, its loss note on pinning (L356) | B.1 L4103; §4.3 L391; §5.3 L2883 to L2896 | **adapt**: context and definitions pinned by digest inside the credential | B4, §5 |
| 7 | R-M-02 (ARCH-0001 §5.1, L299) | §4.7 L1280, L1282 | **constrains**: a key-only principal survives only through a URL spelling | B2 |
| 8 | R-M-06 (L303) | no threshold construct; §8.10 L3492 | **silent**: the data model does not reach thresholds; the export drops them | R4 |
| 9 | R-M-07 (L304) | §5.3 L2885, L2893, L2896 | **constrains**: a digest needs an `id` URL, and SHA-384 is the SHOULD | B4 |
| 10 | R-M-10 (L307), as DL-0025 resolves it (integer depth) | §5.1 L2622 | **silent**: no delegation in the data model | R4 |
| 11 | R-O-01 (ARCH-0001 §5.3, L325) | §7.1 L3362, L3363 | **constrains**: an imported issuer key has a `KeyId` only under a KSA suite | B1 |
| 12 | R-O-02 (L326); ADR-0003 D5 (L51) | §4.10 L2340, L2341; §1.3 L231 | **adopt**, with a limit: the window is emitted, not enforced | A7 |
| 13 | R-O-03 (L327) | nothing canonicalised (L3239) | **adopt**: nothing to cite; the export states how it writes its JSON | §4.3 |
| 14 | R-O-05 (proposal §7, L433; no force) | L4105, conditional; §6.3 L3338; §7.1 L3369 | **silent**: the data model leaves the verifier's clauses to the route | §4.3 item 6 |
| 15 | P1 (ARCH-0002 L67) and ADR-0001 (L55, L56) | L662, L2869: types and terms are URLs | **constrains**: global names at the boundary, documented as lossy | B5 |
| 16 | ADR-0003 D1 (L47) | §4.5 L662; §4.3 L391 | **adapt**: identity embedded in the term URL and pinned by digest | B4, B5 |
| 17 | ADR-0003, rejected: unsigned vocabulary documents (L66, L67) | B.1 L4103; B.2 L4119 | **reject** as our model | R3 |
| 18 | ADR-0003, rejected: signing a re-encoded statement (L62, L63) | L3239 | **silent**: the data model takes no position; each route does (siblings) | §4.2 |
| 19 | ADR-0003 D2; ADR-0004 items 1 and 2 (L38 to L45) | L228, L3257 | **silent**: KSA-CBOR never enters a VC | §4.2 |
| 20 | ADR-0004 item 3 (L46 to L50) | the base context's 15 IANA terms (§5.2); L393, L4103 | **constrains**: the list is narrower than what every VC's vocabulary carries | §4.3 item 1 |
| 21 | ADR-0004 item 4 (L51, L52) | L2391, L2392, L3235 | **constrains**: read as exhaustive, it admits vc+cose alone | §4.3 item 2 |
| 22 | ADR-0004, owed: condition (5) (L105 to L108) | L3269 | **constrains**: the export needs the owed rule now | B7 |
| 23 | ADR-0004, option 4 rejected (L125, L126) | B.2 L4115 | **adopt**: corroborates the rejection | §4.3 item 4 |
| 24 | MD-3 (meeting 2026-09-28, L51 to L53) | L3239 | **constrains**: closed by ADR-0004; the source runs the other way | §4.2 |
| 25 | DEC-005 (ARCH-0001 §7, L485 to L487) | §4.12 | **silent** | §4.3 item 2 |
| 26 | ADR-0005 item 1 (L37, L38) | L1282, L425, L421 | **constrains**: a URL form is owed at the boundary | B2 |
| 27 | ADR-0005, rejected: `did:key` and hash-URI (L71, L72) | L1767: an issuer may be a DID or a key's URL | **constrains**: rejected natively; candidates at the boundary | open question 2 |
| 28 | ADR-0005, interchange (L89 to L92) | no `kid` of the data model's own; the base context's is JOSE's (§5.4) | **silent**: the import rule does not reach a URL issuer | §5.4 |
| 29 | P1.1 (draft, L106, L107) | the base context's `kid`, `@id`-typed (§5.4) | **constrains**: no KSA key rides in a `kid` term | §5.4 |
| 30 | P2 (ARCH-0002 L146 to L148) | §7.1 L3362; A.3 L4037, L4038 | **constrains** | B1 |
| 31 | P3 (L201) and DEC-007 option 4 (proposal L337) | L2348 | **reject** | R3 |
| 32 | P4 (draft, L230 to L233) | B.1 L4103; B.2 L4119 | **adapt**: pin by digest, with the digest in the URL so it names as well as checks | §5.3, §5.5 |
| 33 | SPEC-0003 §4.2, §4.4 (L163 to L167; L178 to L181) | §5.3 L2889, L2895 | **adopt**: the same verifier rule | A6 |
| 34 | SPEC-0003 §11.3 (L471 to L475) | B.1 note L4107 | **silent**: each governs its own documents; two answers to one problem | §4.3 item 5 |
| 35 | P5 (ARCH-0002 L391 to L396) | L391, L2876, L4105 | **adopt** | A3 |
| 36 | P5, never a repair (L391, L392) | §5.8 L3169 | **reject** the repair | R1 |
| 37 | P5.1 (L412 to L415) | no canonical lexical form for time (L4151, L4152) | **silent**: P5.1 does not reach a form nobody declared canonical | B3 |
| 38 | P5.2 (L503 to L505) | a VC is a payload interior that is the data model's | **silent**: P5.2 reasons about an interior that is ours; L391 gives must-understand per context | A3 |
| 39 | P6 (L312 to L314) | §5.9 L3183 | **constrains**: of the functions over one form, attestation exports cleanly and delegation does not | §6.1 |
| 40 | DEC-008, proposed answer (draft, L576 to L580) | B.1 L4103 | **adopt** | A10 |
| 41 | SPEC-0002 §4.4, time (L231, L232; L241 to L243) | L2030, L2032, L3169, L3174 to L3178 | **adapt**: offsets read, fractions rounded inward, the end point and the empty window decided | A5, B3 |
| 42 | SPEC-0002 §7.3, validity (L430 to L432) | L2030, L2032; L2267 | **adopt** | A4 |
| 43 | SPEC-0002 §4.1, arrays ordered and signed (L185) | L3269, L3272 | **adapt**: sets exported as sets, sequences as lists | B7 |
| 44 | SPEC-0002 §9.2's order and its split from trust evaluation (L621, L622; L636 to L639) | §7.1 L3370 to L3373; A.7 L4075 | **adopt** | A1 |
| 45 | SPEC-0002 §9.1, three results (L611 to L615) | §7.1 L3368; §7.2 L3385 to L3392 | **adapt** | B8 |
| 46 | SPEC-0002 §11.1, the view never signed (L680, L681) | §5.13 L3219 | **adopt** | A9 |
| 47 | SPEC-0002 §13.6, bounded work before V4 (L855) | §6.2 L3325, L3326 (non-normative) | **reject** the leniency | R5 |
| 48 | SPEC-0002 §8.6, the threshold form (L538 to L542); SPEC-0004 §6.3 (L284, L285) | §5.1 L2622; §8.10 L3492 | **reject**: no export claims they are honoured | R4 |
| 49 | SPEC-0001 §5.3, the external statement (L229 to L232) | §5.11 L3200, L3201 | **adopt** | A8 |
| 50 | SPEC-0001 §8.1, presentations (L324 to L329) | §4.13 L2467 | **reject** exporting them, this semester | R6 |
| 51 | SPEC-0001 §8.2, the one media type our documents name (L341) | §5.11 L3203 | **constrains**: a registered media type is owed for the label | §6.2 |
| 52 | SPEC-0003 §5.3, language maps (L204 to L211) | §4.6 L922, L924; §11.1 L3941 | **adopt**: one language value object per entry | §6.2 |

**Count: adopt 13, adapt 6, constrains 16, conflicts 0, silent 11, reject 6, of
52 rows**, tallied from the verdict column by script (52 rows examined, each
with exactly one verdict). **No conflict.** What the data model requires of a
verifier, ours can satisfy in every row; its cuts against our decisions arrive
as narrowing — ADR-0004 items 3 and 4, condition (5), ADR-0005's missing URL
form, §5.11's media type — or as options we decline. The conflicts the siblings
found stay where they were found, because they belong to a route, not to the
data model: the JOSE route's ignore rule and ADR-0005's import rule (the
JOSE-COSE sibling's rows 11 and 14), and canonicalising during verification (the
DI sibling's rows 13 and 14). **None falls on ADR-0004.** Three findings carry
the weight: §5.9 presses R-I-06's choice of kind (row 1), §1.3 lets a foreign
verifier ignore the window an export relies on (row 12), and the base context
carries IANA registries ADR-0004's list does not name (row 20).

---

## 8. Open questions

1. **Which kind does R-I-06 export, and what is its subset?** §5.9 sides with
   the §6 row's attestation roles over `AuthzCert` (§6.1), and TV-5's
   `may-delegate` and the threshold form have no foreign meaning (R4, §6.3).
   Shared with the JOSE-COSE sibling's question 9. Settle it in R-I-06's
   rewrite and mofn#110's W3C VC row.
2. **How is a KSA key spelled as a URL** — for `issuer`, `credentialSubject.id`
   and every `@id`-typed value? The source asks only for a URL (L1282, L425) and
   counts URNs and DIDs as URLs (L421); ADR-0005 rejects `did:key` natively and
   a signed text rendering. Shared with both siblings' question 2. Settle it in
   ADR-0005's successor or the R-I-01 VC table.
3. **`validUntil`'s end point, and the empty window.** Export `T` or `T − 1 s`;
   refuse an empty window (B3, D4)? Settle it in the R-I-01 VC table.
4. **Our documented context: where, under what URL, vouched for by whom?** A
   content-addressed URL (L2862) makes the digest a name as well as a check
   (§5.5). A signed statement about the context's digest would give it the signer
   the base context lacks (ours). Settle it in R-I-06's mapping document.
5. **Condition (5) before export.** The order and the distinctness of `trusts`,
   `allow-keys` and `exclude-keys` (B7), owed to SPEC-0002 by ADR-0004 and, for
   distinctness, by ARCH-0001's open item. Settle it in SPEC-0002.
6. **ADR-0004 item 3's list.** Add the JWT Claims and JOSE Header Parameters
   registries, which every VC's base vocabulary carries (§4.3 item 1), or leave
   each R-I-01 table to name them? Shared with the JOSE-COSE sibling's §6.4
   item 2 and the DI sibling's question 10. Settle it in ADR-0004's successor or
   the R-I-01 tables.
7. **A registered media type for KSA statements**, to earn §5.11's label
   (§6.2)? A registration is a boundary act ADR-0001 permits. Settle it as a
   project decision recorded in the R-I-01 VC table.
8. **The import profile.** Which contexts our importer understands (A3), the
   controller–issuer binding (B1), how times are read (B3), and what an imported
   VC's identity is (the DI sibling's question 6). Settle it in mofn#110's import
   column.
9. **Digest strength in `relatedResource`.** Carry SHA-384 beside the SHA-256
   DefinitionId to meet L2896's SHOULD, or record the deviation (B4)? Settle it
   in the R-I-01 VC table.
10. **Expiry a foreign verifier must enforce.** `validUntil` may be ignored
    (L231; A7). Should the export's own signature expire no later than
    `not-on-or-after` — `exp` on the JOSE-COSE route, `expires` on the Data
    Integrity route, each the export signature's time as the siblings map it —
    so that a verifier that ignores the window still stops? Whether those must be
    honoured is each mechanism's rule [outside this source]. Settle it in the
    R-I-01 VC table, per route.
11. **The library holds this source's dependencies weakly.** JSON-LD 1.1, on
    whose algorithms every meaning in §5 depends; Controlled Identifiers 1.0
    (§7.1's controller and controlled identifier document); Subresource
    Integrity (`digestSRI`); Bitstring Status List; VC JSON Schema; and the VC
    Extensions have no record under `records/w3c/` (listed in this pass). Ingest
    them before §5 and §6 are built on; the `artifact-statements` topic, which
    owns this record, is the natural owner.
12. **Eight of the 26 messages the protocol model names have no structure in
    the source.** Pass 3 joined every message of `protocol.yaml` to
    `messages.yaml` (`crosscheck.yaml`): 16 resolve to a structure and 2 to a
    member of one (the proof property; the controlled identifier document that
    §7.1 returns). Eight resolve to none, because the source defines none:
    status information (§4.10 leaves it to the status type), the refresh
    request (§5.4 shows Example 27 and says no more), the presentation request
    (Appendix A.1 and §9.5.2 mention one), the derived credential and its proof
    (§4.13 and §5.7 delegate them to the securing mechanism), the transformation
    input document (§5.11 asks only for a registered media type), the verifiable
    data registry entry (Appendix A.4, non-normative), the HTTP response for a
    related resource (HTTP's), and the enveloping serialization (VC-JOSE-COSE's).
    These are gaps in the source, not in the join. An export route that relies on
    one must take it from the specification that owns it. Settle it in the
    R-I-01 VC table, per route. (A ninth, the verification algorithm's input, was
    a gap of this record's pass 1 and is now the structure `VerificationInput`.)
13. **Does a `credentialSubject` object holding only `id` conform?** §4.8 says
    each object MUST be the subject of one or more claims, MUST be serialized
    inside the property (L1774), and MAY carry an `id`. An object with only an
    `id` identifies a subject and asserts nothing inside itself. The derived
    schema rejects it (`subjectObject`), on that reading of R-0173 and R-0174;
    the inferred R-0175 names only the empty object, and its note says the
    id-only case fails on the same reading. The source prints no such object (76
    fixture subject objects checked, none holds only `id`), so no example settles
    it. A foreign verifier may take the other reading. Settle it in the import
    profile (question 8): accept an id-only subject on import, or refuse it as
    the schema does.

---

## 9. Source defects and tensions met while mapping

Recorded, not repaired. This file did not read `normative.md`, `protocol.yaml`
or any other artifact of this record but `requirements.yaml`, read last to wire
ids (§10); the verify pass reconciles these with them. Each was re-read in the
`.txt`; the context-file findings were measured from the files of §5.1.

- **D1. §5.13 and §7.1 describe the verification result differently.** §5.13
  requires three items named `verified`, `verifiedDocument` and `mediaType`
  (L3220 to L3225); §7.1 expects seven, two of them under other names:

<!-- q L3369 "If the call was successful, result will contain" .. "and errors properties." -->
> If the call was successful, result will contain the status, document, mediaType, controller, controlledIdentifierDocument, warnings, and errors properties.

- **D2. §7.1 has no outcome when no mechanism can be chosen.** Step 1 (L3368)
  sets `verifyProof` and has no branch for the case where none is found (B8).
- **D3. Status: inside verification, or outside it?** §2 defines verification
  to include it:

<!-- q L276 "This includes checking that the credential" .. "the status check succeeds." -->
> This includes checking that the credential or presentation conforms to the specification, the securing mechanism is satisfied, and, if present, the status check succeeds.

  while §7.1 has no status step and Appendix A.8, non-normatively, treats
  status as part of validation (L4080). A1 follows §7.1.
- **D4. `validUntil`'s end point.** L2032 describes it as the moment validity
  ends and as the last moment at which the information still holds (B3).
- **D5. A time without an offset: an error, or UTC?** L2030 makes it
  non-conforming, L230 requires errors for non-conforming documents, L3169
  requires it to be read as UTC (R1).
- **D6. A normative rule rests on a non-normative definition.** §4.6 makes
  `name` and `description` either plain text or a language value object, for
  which it points to §11.1 (L922, L924); §11.1's own requirements on that object
  (L3941) sit inside the informative §11, with 8 keywords across §11.1 and
  §11.2 (`skeleton-report.txt`: 5 and 3).
- **D7. A property that does not exist.** B.2's base-class table:

<!-- q L4132 -->
> | RefreshService | Serves as a superclass for specific refresh service types that are placed into the credentialRefresh property.

  The property is `refreshService` (§5.4, L2925, L2926), and `credentialRefresh`
  occurs 0 times in the base context and the credentials vocabulary (measured).
- **D8. The hashed context files do not carry what the text requires**
  (measured, §5.2): 4 of the base context's 8 XSD coercions use the namespace
  `https://www.w3.org/2001/XMLSchema#`, which is not XSD's; and `validFrom` and
  `validUntil` are coerced to `dateTime`, with that range in the vocabulary,
  where L2030 and L2032 require a `dateTimeStamp`. Both files are pinned by
  digest (L4103, L4119), so a fix changes the digest (§4.3 item 5).
- **D9. A minimum the source does not meet.** L2896 makes sha384 the SHOULD
  minimum; the source's own digests are SHA2-256 (L4103, L4119, L4122), and
  Example 26 is captioned SHA2-256 (L2910).
- **D10. A MUST and a MAY on one set of files.** B.2 requires the vocabulary
  URLs to resolve to the files it lists and permits semantically equivalent
  serializations, which its printed digests cannot verify (L4115; §4.3 item 4).
- **D11. The media types are registered in a non-normative appendix.** Appendix
  C carries the HTML class `appendix informative`, as VC-JOSE-COSE's do (that
  record's SD-16).
- **D12. Opposite advice on `@json`.** §6.1 recommends it where order matters
  (L3272); B.4, non-normatively:

<!-- q L4162 "is useful for leaving the semantics open-ended" .. "and is expected not to be used." -->
> is useful for leaving the semantics open-ended and not strictly defined. This can be dangerous if the implementer is looking to constrain the data type of the claims in the credential, and is expected not to be used.

  The base context itself uses `@json` three times (§5.2).
- **D13. Text**, each as printed — a missing verb (L215), a clause stated twice
  (L300), a missing full stop (L423), a doubled preposition (L2609), a number
  disagreement (L2926), a garbled clause (L3072), and a misspelt property name
  (L3170). A scan for doubled words and article errors over 805 prose lines
  found none.

<!-- q L215 "Often, more than one type" .. "used in an ecosystem." -->
> Often, more than one type of verifiable data registry used in an ecosystem.

<!-- q L300 "More information is expected to be added to the graph in order" .. "added to the graph." -->
> More information is expected to be added to the graph in order to be able to trust claims, more information is expected to be added to the graph.

<!-- q L423 "Identifier-Based Correlation carefully" .. "There are also" -->
> Identifier-Based Correlation carefully There are also

<!-- q L2609 "integrity-protected by being secured using with" .. "private key." -->
> integrity-protected by being secured using with the entity's private key.

<!-- q L2926 "one or more refresh services that provides" .. "provides" -->
> one or more refresh services that provides

<!-- q L3072 "The evidence property provides information that is different from" .. "securing mechanism used." -->
> The evidence property provides information that is different from and information to the securing mechanism used.

<!-- q L3170 "had a validUtil value" .. "validUtil value" -->
> had a validUtil value

- **D14. A superseded reference.** L3931 points to CBOR as RFC 7049, and the
  reference list gives that RFC (L4351, L4352); `rfc-8949`'s `record.yaml`
  lists `rfc-7049` under `supersedes`. Informative only.

---

## 10. Requirement ids

Wired last, from `requirements.yaml` as its agent left it (298 entries, every
`actor` and `testable` filled, untouched for 40 minutes when read), by script:
each source quotation above was joined to the entries whose `source_lines`
overlap it **and** whose text lies inside the quotation or contains it; where a
parent and its `split_of` children both matched, only the children are listed.
**80 quotations examined; 46 joined, to 65 distinct ids; 34 joined none** — 17
in sections the source marks non-normative, 6 in notes, and 11 in normative
text that carries no BCP 14 keyword (L226, L421, L2340, L2348, L3168, L3170,
L3239's first span, L3262, L3264, L3272, L4132; checked by grep). Every pair
below was printed and read. Verbs are shown where an entry has one; ids are
`w3c-vc-data-model-2-0#R-NNNN`.

| item | quoted lines | requirement ids |
|---|---|---|
| A1 | L3370 | R-0279 |
| A1 | L3371 | R-0112 (MAY), R-0281, R-0282 |
| A1 | L3373 | R-0113 (MAY), R-0114 (MAY) |
| A3 | L391 | R-0009 (MUST) |
| A3 | L2876 | R-0064 (MUST) |
| A3 | L4105 | R-0125 (MUST) |
| A4 | L2030 | R-0178 (MUST), R-0179, R-0180 (MUST) |
| A5 | L3169 | R-0082 (SHOULD) |
| A6 | L2889 | R-0067 (MUST) |
| A6 | L2895 | R-0071 (MUST), R-0072 (MUST) |
| A7 | L2341 | R-0031 (MUST NOT) |
| A7 | L231 | R-0007 (MAY) |
| A8 | L3199 | R-0251 |
| A8 | L3200 | R-0090 (MUST) |
| A8 | L3201 | R-0091 (MUST) |
| A9 | L3219 | R-0098 (MUST) |
| A10 | L4103 | R-0124 (MUST) |
| B1 | L3362 | R-0273 |
| B1 | L3363 | R-0273 |
| B2 | L1280 | R-0167 (MUST) |
| B2 | L1282 | R-0168 (MUST), R-0169, R-0170 (RECOMMENDED) |
| B2 | L425 | R-0146 (OPTIONAL), R-0147 (MUST), R-0148 (MAY) |
| B3 | L2032 | R-0027 (MUST), R-0181 (MUST), R-0182 |
| B4 | L391 | R-0140 (MAY) |
| B4 | L2885 | R-0224 (REQUIRED), R-0225 (MUST) |
| B4 | L2893 | R-0229 (MAY), R-0230 (MAY) |
| B4 | L2896 | R-0073 (SHOULD) |
| B5 | L2869 | R-0057 (MUST) |
| B5 | L2870 | R-0058 (MUST) |
| B5 | L2873 | R-0060 (MUST), R-0061 (MUST) |
| B6 | L3257 | R-0108 (MUST) |
| B7 | L3269 | R-0266 |
| B8 | L3358 | R-0110 (MUST) |
| B8 | L3368 | R-0111 (MUST), R-0275 |
| R1 | L3169 | R-0083 (MUST) |
| R1 | L230 | R-0132 (MUST), R-0133 (MUST), R-0134 (MUST) |
| R2 | L415 | R-0144 |
| R6 | L2467 | R-0037 (SHOULD) |
| §4.2 below | L3239 | R-0259, R-0260 |
| §4.3 item 4 below | L4115 | R-0126 (MUST), R-0127 (MAY) |
| §6.2 below | L3202 | R-0092 (MUST) |
| §6.2 below | L3203 | R-0093 (MUST) |
| §6.2 below | L3204 | R-0094 (SHOULD) |
| D1 | L3369 | R-0277 |
| D3 | L276 | R-0137 |
| D13 | L2926 | R-0234 (MUST) |

---

## 11. bears_on

`record.yaml` lists R-I-06, R-I-01 and R-M-07. Each was checked against
ARCH-0001 v0.1.8 at `a56a3c0`. `record.yaml` is not edited here.

- **All three stand.** R-I-06: §6, and §6.1 presses its choice of kind. R-I-01:
  A8 and §6.2, where §5.11 adds rows. R-M-07: B4, where a digest needs an `id`
  URL and SHA-384 is the SHOULD.
- **Warranted additions:**
  - **DEC-002**: §4.
  - **DEC-003**: a key is named by a URL here (B2; rows 26 to 28).
  - **DEC-005**: item 4's envelopes meet this source's mechanisms at vc+cose
    alone (§4.3 item 2; row 25).
  - **R-I-02**: trust is local and one hop (A2; row 3).
  - **R-M-02**: a key-only principal needs a URL spelling (row 7).
  - **R-O-01**: an imported issuer has a `KeyId` only under a KSA suite (row 11).
  - **R-O-02**: no status, short validity — emitted, not enforced (A7; row 12).
- **Weak, optional:** R-O-03 (row 13); R-O-05, R-M-06 and R-M-10, on which the
  source is silent (rows 14, 8, 10).
- **Outside the field's vocabulary.** `bears_on` takes ARCH-0001 DEC and R ids,
  so P1, P1.1, P2 to P6, P5.1, P5.2, DEC-007 (a proposal), DEC-008 (ARCH-0002)
  and the SPEC sections cannot be listed. They are rows 15 to 52; P4 (row 32),
  P5 (rows 35, 36) and P6 (row 39) are the ones this record presses hardest.

## 12. What this file decides

Nothing.

<!-- qm CONTRIBUTING.md L107-108 "Only an ADR" .. "decision." -->
> Only an ADR accepts a decision.

Each adaptation and open question names the SPEC section, ADR or DEC that would
settle it. The findings are evidence for R-I-06's rewrite and mofn#110's W3C VC
row (§6.1), for ADR-0005's successor (B2), for ADR-0004's successor or the R-I-01
tables (§4.3 items 1 and 2), for SPEC-0002's condition-(5) rule (B7), and for the
R-I-01 VC table (§6.2). None of it reopens DEC-002.
