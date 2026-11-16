---
schema: "library-distilled/v1"
id: fips-140-3-design-notes
record: fips-140-3
type: design-notes
updated: "2026-11-15"
---

# FIPS 140-3: design notes for tmodel and mofn

This note covers how FIPS 140-3 bears on `tmodel:DEC-005` and `tmodel:DEC-009`, the record's `bears_on`. It also covers mofn's cipher suites and key custody, which no `bears_on` id can name yet (see the mofn item under Reject or hold).

- **Read against** tmodel@ddac1b9 (`tmodel:ARCH-0001` v0.1.11, `project/DECISIONS-0001.md` v0.1.9, `spec/schema/tmodel-object-model.linkml.yaml`) and mofn@10e357f. A tmodel id is written `tmodel:…` (`docs/scope.md`, Two registers); a bare id is mofn's.
- **What it is.** The announcement, ¶1 to ¶14, and a body of three sections. The body adopts ISO/IEC 19790 and ISO/IEC 24759 by reference (§2, §3.2) and names the seven SPs that modify them (§3.3, §3.4, Table 1). It defines no message, format or protocol. Its binding text is short: the announcement's few provisions, and the body's statements of what it adopts and which SPs modify it.
- **What the library does not hold.** The two ISO/IEC standards are records `iso-iec-19790` and `iso-iec-24759`, both `status: queued` with no content digest. Every security requirement a module must meet is in them, so this record and its seven SP siblings are the CMVP's changes to a base the library cannot quote.
- **Source.** `.cache/fips-140-3.txt`, sha256 `c9562602f7aea504fabe59c4065f0c904f6c0d44a7be1cdf11848227ffc79605`, which is the pinned `source_text_digest`. It renders the PDF whose sha256, `942a4f929dfbd2b4af2e4e03df7f6e6377054346afd9bee346ed0ebac5db384b`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN`, `RQ-NN` and `AREA-NN` mean `fips-140-3#…`. A script emits every id from the named record's `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text or an id prefix, and raises unless exactly one matches. Ids of sibling records are written in full and selected from their own files the same way.
- **Two pairs share a text.** RQ-01 and R-0007 are the same ¶10 sentence, and RQ-02 and R-0005 the same ¶7 sentence. The RQ ids are the ones `main` carried; this note cites them.

## Adopt

### ¶13: a validated module is evidence, and the owner still accepts the risk

This bears on `tmodel:DEC-009` (mitigation lifecycle), on `Requirement.conformance_status` in `tmodel:DEC-001b` (the proposed `tmodel:R-042`), and on `tmodel:R-019`.

<!-- q L241-246 "While the security requirements" .. "acknowledged and accepted." -->
> While the security requirements specified in this standard are intended to maintain the security provided by a cryptographic module, conformance to this standard is not sufficient to ensure that a particular module is secure. The operator of a cryptographic module is responsible for ensuring that the security provided by a module is sufficient and acceptable to the owner of the information that is being protected and that any residual risk is acknowledged and accepted.

- FIPS 140-3 says of its own conformance what tmodel says of its R-042 verdict: `RequirementConformanceStatus` records linkage and approval, not adequacy. R-0012 then leaves the last word with the responsible authority in each agency.
- R-0042 makes the operator responsible for it. The residual risk the operator accepts is `MitigationStatus.accepted_risk` with a human `Review` (`tmodel:R-018`). It belongs to the system the module is used in, not to the validation.
- So a FIPS 140-3 validation enters tmodel as `Evidence` about a module, never as a `conformant` verdict on its own.

### ¶3 and ¶9: CMVP validates a module, and a product contains it

This bears on `tmodel:DEC-009` (generic threat to product), on Component composition (`tmodel:DEC-001a`, `tmodel:ADR-0011`) and on `Evidence` (`tmodel:ADR-0013`).

<!-- q L116-118 "The goal of the CMVP" .. "validated cryptographic modules." -->
> The goal of the CMVP is to promote the use of validated cryptographic modules and provide Federal agencies with a security metric to use in procuring equipment containing validated cryptographic modules.

<!-- q L159-162 "This standard covers implementations" .. "conforming to this standard." -->
> This standard covers implementations of cryptographic modules including, but not limited to, hardware components or modules, software/firmware programs or modules or any combination thereof. Cryptographic modules that are validated under the CMVP will be considered as conforming to this standard.

- R-0027 and R-0028 hold the two ¶9 sentences. The unit of validation is the module. Agencies buy equipment that contains one. In tmodel the module is a `Component` that a Product is `composed_of`, and the validation is `Evidence` with `evidence_kind: attestation` and `about_version` set to the validated version.
- ¶9's embodiments are hardware, software or firmware, or a combination. SP 800-140 §6.2 modifies the boundary assertions for hardware, firmware and hybrid modules (AS02.15, AS02.17, AS02.18); the software module's, AS02.16, it leaves as ISO/IEC 24759 has it (`nist-sp-800-140` notes). They line up with the three instance types `tmodel:ADR-0002` uses for `tmodel:DEC-005`: software, hardware and system.
- ¶12 keeps two lists, and R-0010 says the historical one is not for procurement. A validation therefore goes stale as evidence. `Evidence.fresh_until` (`tmodel:ADR-0013`) is the slot for that.

### ¶7: a level is a set of requirements, not a score

This bears on `RequirementSource` (`tmodel:ADR-0013`, which lets one named level of a source be a RequirementSource) and on `tmodel:DEC-009`.

<!-- q L152-154 "The security requirements for a particular" .. "regardless of the level." -->
> The security requirements for a particular security level include both the security requirements specific to that level and the security requirements that apply to all modules regardless of the level.

- RQ-02 has the level chosen for the application and its environment. The sentence quoted above, R-0026, then defines a level's requirements as its own plus those that apply at every level.
- A RequirementSource per level, as `tmodel:ADR-0013` allows for SLSA Build L2, fits only a module rated at one level in every area. SP 800-140B §B.2.1 asks for the level of each area as well as the overall level, so the areas of one module can carry different levels. The deferred `RequirementProfile` (`tmodel:ADR-0013`) is where a level per area would go.
- Nor is a level every requirement at or below it. Of the 22 assertion headings in SP 800-140, three name a single level: AS06.11 (Level 2), and AS07.81 and AS09.23 (Level 3). A script counted the `ASnn.nn: (… – Level…)` headings (`nist-sp-800-140` notes).

## Adapt

### The family is a source that edits another source

This bears on the Requirement edges of `tmodel:ADR-0012` (`tmodel:DEC-001a`), on `RequirementSource` (`tmodel:ADR-0013`, part of `tmodel:DEC-001b`), and on the link predicates `tmodel:RPT-0017` allows.

<!-- q L350-352 "These documents modify the annex requirements" .. "validation authority." -->
> These documents modify the annex requirements of the technical requirements document ISO/IEC 19790:2012(E) as specified by the CMVP validation authority.

<!-- q L380-382 "These documents modify the vendor documentation" .. "validation authority." -->
> These documents modify the vendor documentation and testing requirements of ISO/IEC 24759:2017(E) as specified by the CMVP validation authority.

- R-0054 and R-0061 hold the two sentences; the rows of §3.3 and §3.4 are entries too, from R-0055 to R-0068. Table 1 (L401–L420) maps each SP to what it changes. SP 800-140 changes ISO/IEC 24759 §6.1 to §6.12. SP 800-140A to 800-140F each change one annex of ISO/IEC 19790 and one subclause of ISO/IEC 24759, §6.13 to §6.18. SP 800-140C and 800-140D replace their annex outright, by their own abstracts.
- tmodel has no edge for this. `refines` narrows a requirement, `derived_from` may change its intent, `maps_to` is overlap and `conflicts_with` asks a person to choose. A deletion, which SP 800-140 §5.2 marks by strikethrough, or a whole-annex replacement is none of them. `tmodel:RPT-0017` also sends every link between two sources to `tmodel:MAP-0001` as overlap.
- **Proposal.** A `modifies` relation from a RequirementSource to the source and locator it changes, with the kind of change: adds, deletes or replaces. Until one exists, model the edition in force as one RequirementSource whose `source_members` are the resulting requirements, and record in its description which SP changed which clause.
- **Licence.** The ISO/IEC base can only be paraphrased (`tmodel:ADR-0012`; `tmodel:RPT-0017` lists ISO and IEC as paraphrase only). The NIST layer can be verbatim: `tmodel:RPT-0017` lists NIST among the free sources, and each SP's Authority section disclaims US copyright (`nist-sp-800-140` notes). So `text_origin` must be set per Requirement, not per source.

### Which edition is in force: the document gives two rules

This bears on `RequirementSource.version` (`tmodel:ADR-0013`).

<!-- q L332-335 -->
> When referring to ISO/IEC 19790:2012(E) and ISO/IEC 24759:2017(E), the latest edition of the referenced document (including any amendments) applies. “NIST SP” denotes a NIST Special Publication series document. For those NIST SP documents that are not referenced by a specific version or date, the latest edition of the referenced document (including any amendments) applies.

<!-- q L318-319 "Therefore, FIPS 140-3 is based on" .. "24759:2017(E)." -->
> Therefore, FIPS 140-3 is based on ISO/IEC 19790:2012/Cor.1:2015(E) and ISO/IEC 24759:2017(E).

- §3.1 (R-0050) lets both ISO/IEC references float to their latest edition. §2 (R-0048) pins ISO/IEC 19790:2012 with its 2015 corrigendum, and §3.2 lists ISO/IEC 19790:2012(E) without it. Each of the seven SPs pins ISO/IEC 19790:2012 and ISO/IEC 24759:2017 in its own §2. The library's `iso-iec-19790` and `iso-iec-24759` records carry `maturity: historic`, and their notes record from ISO's catalogue that both editions were withdrawn on 2025-02-26 and revised by 2025 editions. So §3.1's rule already points past every edition the eight documents were written against.
- §3.1's last sentence (R-0052) floats the SPs too, because Table 1 names each without a revision. Three of the seven are withdrawn by their own cover pages: SP 800-140B on 2023-11-17, in favour of SP 800-140Br1, and SP 800-140C and 800-140D on 2022-05-20, in favour of SP 800-140Cr1 and SP 800-140Dr1. The library holds only the withdrawn editions (`ls records/nist`).
- So a FIPS 140-3 RequirementSource needs its `version` to say which rule was applied and on what date. The document does not settle it (open question 2).

## Reject or hold

### Hold: FIPS conformance is not in the tmodel MVP

This bears on `tmodel:DEC-005`, accepted by `tmodel:ADR-0002`.

- `tmodel:ADR-0002` cites the FIPS 140 family among its evidence and puts full compliance and audit outside the MVP. What the MVP takes from this family is identity by embodiment: the boundaries of SP 800-140 §6.2 and the tested configuration of SP 800-140B. It does not take the conformance regime.
- Nothing in this record asks the MVP to change. The Adapt items are inputs to `tmodel:DEC-009` and to the open part of `tmodel:DEC-001b`.

### Reject: FIPS 140-3 as a product classification

This bears on `Product.classifications` and `applies_to_family` (`tmodel:ADR-0012`) and on `tmodel:DEC-009`.

- A validation covers one module version (¶9), with a level per area (¶7), on the operational environments that were tested (SP 800-140B), and it is not sufficient for security (¶13). A classification such as `family:fips-140-3` on a Product would assert all four with none of their detail. It would also not go stale when the validation does.
- Keep the validation as Evidence on the module Component, and derive any statement about a product by querying its composition.

### mofn: voluntary, and no route to a validated deployment is open today

This bears on mofn's `SPEC-0001` §5.1 and §5.2, `SPEC-0002` §6, `ARCH-0003` §3.3, and `PLAN-0004` §6.1 and §6.2. None of these is a DEC or an `ARCH-0001` requirement: `ARCH-0001` NG3 leaves algorithms unfrozen, and the suite rules are in the SPECs.

R-0002 applies the standard to modules the federal government runs, itself or through contractors. ¶6 then opens it to everyone else (R-0025):

<!-- q L140-141 "The adoption and use" .. "commercial organizations." -->
> The adoption and use of this standard is available to private and commercial organizations.

A mofn wallet that holds its own keys is a software cryptographic module in FIPS terms. RQ-01 requires a conforming module to use Approved security functions, and ¶10 says where they come from. R-0029 holds the lead-in, and R-0030, R-0073, R-0031 and R-0032 hold items a to d:

<!-- q L172-185 "Approved security functions include" .. "establishment method." -->
> Approved security functions include those that are either: a. specified in a Federal Information Processing Standard (FIPS), b. adopted in a FIPS and specified either in an appendix to the FIPS or in a document referenced by the FIPS, c. specified in NIST SP 800-140C as an Approved security function, or d. specified in NIST SP 800-140D as an Approved sensitive security parameter establishment method.

Item b (R-0073) was out of reach of pass 1's reader until library#137 fixed it (open question 5).

There are three routes to a validated deployment. Each is closed today:

| route | what FIPS 140-3 needs | mofn today |
|---|---|---|
| the engine itself as a validated software module | approved functions in the approved mode (RQ-01; `nist-sp-800-140` AS02.20) | suite 1 (Ed25519), Argon2id and libsodium SecretBox are absent from the cached SP 800-140C and 800-140D (`PLAN-0004` §6.2 records engine v0's choices; see those records' notes) |
| a key held in local hardware (`custody: hardware`, `ARCH-0003` §3.3) | a validated module, which the wallet signs through | out of scope for the CLI engine milestone (`PLAN-0004` §6.1) |
| a key held by a remote signer (`custody: remote-signer`) | the same | `PLAN-0004` §6.1 rules out cloud custody, and mofn's wallet survey (`research/0002-wallets/report.md`) recommends refusing cloud HSM custody |

Read through ¶10 item a alone, both mofn signature suites would already be approved security functions. FIPS 186-5 §7 specifies EdDSA, with Ed25519 (record `fips-186-5`; its PDF was fetched for this note and matched `content.sha256`). FIPS 204 specifies ML-DSA, which suite 8 cites. The cached SP 800-140C lists neither. Whether item a alone makes a function approved, or the CMVP also needs it listed in SP 800-140C and tested by the CAVP, is open question 4.

## Open questions and source defects

### 1. ¶13 does not say who decides that a module's security is sufficient

- The quoted paragraph makes the operator responsible for ensuring the security is acceptable to the owner of the information, and R-0012 makes the agency's responsible authority ensure it. Operator, owner and responsible authority are three parties, and the paragraph does not say how they relate.
- For tmodel, the `Review` that accepts the residual risk needs a reviewer who holds that authority (`tmodel:R-018`, `tmodel:R-019`). The standard does not name the role, so tmodel cannot take it from here.

### 2. Two rules for the edition in force

See the edition item under Adapt. §3.1 floats every reference to its latest edition, §2 and each SP's §2 pin editions, and §2 and §3.2 disagree about the corrigendum.

### 3. ¶12 and Figure 1 give different starts for testing

<!-- q L194-196 "This standard becomes effective" .. "FIPS 140-3 testing." -->
> This standard becomes effective six months after approval by the Secretary of Commerce. A minimum transition period of 6 months after approval is provided for testing labs to develop and implement FIPS 140-3 testing.

<!-- q L217-218 -->
> FIPS 140-3 TESTING BEGINS (18 months after approval date)

- The text gives testing labs at least 6 months after approval (R-0035). The figure starts FIPS 140-3 testing at 18 months (R-0040). A minimum does not contradict a later start, but neither says which date governs. The figure gives the end of FIPS 140-2 testing no date at all (L223–L224).

### 4. ¶10's list is open; the annexes' lists are closed

- ¶10 gives four ways for a function to be approved, and item a is any FIPS. SP 800-140C §6.1 supersedes the functions named in ISO/IEC 19790 and 24759, and SP 800-140D §6.1 precludes every method it does not list.
- A function that a FIPS specifies and SP 800-140C omits is therefore approved under item a and unlisted in the annex. Against the cached annex that is EdDSA (FIPS 186-5) and ML-DSA (FIPS 204). The family does not say which rule wins.
- For mofn this decides whether suites 1 and 8 can run in an approved mode before the annex lists them (`nist-sp-800-140c` notes).

### 5. Our rendering dropped a line of ¶5, ¶10 and ¶13 (ours, not a source defect; fixed)

- Until library#137 (63d708e), `bin/_source_text`, in its PDF profile, blanked the first line of every page after the first (`normative.md` TD-1). On the announcement pages that was body text: L131 (the first line of ¶5), L181 (¶10 item b) and L237 (the second line of ¶13's first paragraph). It kept the page numbers iii, iv and v as prose instead (TD-2).
- `bin/check-quotes` read through the same function, so it could not see the gap, and pass 1 quoted around those lines. Under the fixed reader item b is R-0073 and is quoted above, and every marker in this note checks.

### 6. The family names one area two ways

- FIPS 140-3 calls the fifth area of its list operating environment (Abstract L70, ¶3 L106; AREA-05). SP 800-140 §6.6 and SP 800-140B §B.2.6 call it operational environment. A RequirementSource keyed by area name has to pick one; ISO/IEC 19790, which the library does not hold, decides.
- The Abstract covers secure design, implementation and operation (L67–L68); ¶3 covers design and implementation only (L103–L104). Both then list the same eleven areas.

### 7. Three of the seven SPs are withdrawn, and the library holds none of their successors

- SP 800-140B, 800-140C and 800-140D are withdrawn by their own cover pages (see the edition item under Adapt). The library has no record for SP 800-140Br1, 800-140Cr1 or 800-140Dr1, or for any later revision.
- §3.1 makes the latest revision of each the one that applies. Every note in this family that reads those three annexes therefore reads an edition FIPS 140-3 no longer points to.

### 8. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 88 entries. 25 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it: the Table 1 map and its lead-in (R-0049, R-0054 to R-0060 and R-0062 to R-0068; R-0061 is cited by F01 step 1), scope and applicability (R-0004, R-0015, R-0025, R-0027, R-0043), reading rules for the ISO/IEC and SP texts (R-0045, R-0047, R-0050, R-0052) and one definition (R-0051). The 6 inferred entries (R-0069 to R-0072, RQ-03, security-policy) keep a `field` that names a thing, an effective date, the start and end of testing, a deliverable, and no message field, step or guard cites them: each rests on the stated entries in its `derived_from`, which are cited. RQ-03 and security-policy name the non-proprietary security policy of SP 800-140B (`SecurityLevelsTable` and the structures around it in `nist-sp-800-140b`); this record holds no structure for it.
- `messages.yaml`: 18 citations from 2 structures and 5 fields. 12 cite an entry whose lines overlap the field's, 4 more one that overlaps the structure's, and 2 (R-0005 and R-0026 from `SecurityLevelClaim`, whose quotation is ¶3) cite ¶7, where the level is chosen and a level's requirements are described. That is a deliberate reading of the claim's `security_level`, not a wrong id.
- `protocol.yaml` `work_products`: 2 of 14 carry a `structure` (`module and vendor evidence` holds `ApprovedSecurityFunctionBasis`, only through F01 step 1's citation of R-0007; `security level selection` holds `SecurityLevelClaim`); 12 carry `structure: none` with a reason, because the source names the product and prescribes none. `CMVP Historical list` is a work product of no step: F02.E1 and M03 use it.
- Ids added by pass 3: 25 in `protocol.yaml` and 13 in `state-machine.yaml`, each where a quotation carries an entry's whole text (R-0022, R-0023, R-0026, R-0040, R-0046 and R-0061 among them). F02.E1 and M03.T06 quote ¶12's whole sentence but rest on the Historical-list note R-0010, so R-0038 (may purchase) is not added there. A split parent stays cited beside its child where a step uses one verb: F01 step 6 and F02 step 2 R-0038 (may), F02 step 1 R-0037 (should).
