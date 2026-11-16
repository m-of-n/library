---
schema: "library-distilled/v1"
id: nist-sp-800-140b-design-notes
record: nist-sp-800-140b
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140B (CMVP security policy requirements, withdrawn): design notes for tmodel and mofn

This note covers how SP 800-140B bears on `tmodel:DEC-009`, the record's `bears_on`, and on mofn's key object, which no `bears_on` id can name (see the mofn item under Adapt).

- **Withdrawn.** The cached PDF opens with NIST's withdrawal notice:

<!-- q L13-15 -->
> Withdrawal Date November 17, 2023 Withdrawal Note NIST SP 800-140B is withdrawn and superseded in its entirety by NIST SP 800-140Br1 (Revision 1)

<!-- q L19-25 -->
> Series/Number NIST SP 800-140Br1 Title Cryptographic Module Validation Program (CMVP) Security Policy Requirements: CMVP Validation Authority Updates to ISO/IEC 24759 and ISO/IEC 19790 Annex B Author(s) David Hawes; Alexander Calis; Roy Crombie Publication Date(s) November 2023 URL/DOI https://doi.org/10.6028/NIST.SP.800-140Br1

- So everything below reads a template NIST withdrew on 2023-11-17. The library has no record for SP 800-140Br1 (`ls records/nist`). Read every item against Revision 1 before building on it.
- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** A template for the security policy, the public document every validated module publishes. It fixes the order of the policy, adds tables and figures to ISO/IEC 19790 Annex B, and leaves ISO/IEC 24759 §6.14 unchanged. Most of its content is table headings and bulleted instructions, not sentences with verbal forms.
- **Source.** `.cache/nist-sp-800-140b.txt`, sha256 `d563d0a22df0a11369732ba44e7c5f04393191550d93f96df7a59d634d506d28`, the pinned `source_text_digest`. It renders the PDF whose sha256, `60bc7223fa81f21724d0d4cd74e5a7e5df52cba928c8187803290ccaa398424c`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140b#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## Adopt

### Tested and vendor-affirmed environments are kept apart

This bears on `tmodel:DEC-009` (generic threat to product instance), on the review rule of `tmodel:ADR-0012`, and on the instance identity of `tmodel:ADR-0002` (`tmodel:DEC-005`).

<!-- q L400-402 -->
> o For software, firmware, and hybrid cryptographic modules, list the operating system(s) the module was tested on and the operating system(s) that the vendor affirms can be used by the module.

- R-0004 asks for two lists, and §B.2.2 gives each its own table: Tested Operational Environments (operating system, hardware platform, processor, acceleration) and Vendor Affirmed Operational Environments (operating system, hardware platform), at L405–L427.
- The second table is a claim of applicability that no laboratory tested. In tmodel a tested environment is a ProductInstance or a Deployment with Evidence. A vendor-affirmed one is an Assertion by the vendor with no test behind it, which tmodel's Assertion rule (`tmodel:ADR-0010`: provenance, and review before an assertion is accepted) keeps out of the slots until a person reviews it.
- An import must keep the two apart, as the template does. Merging them would turn the vendor's affirmation into a validated configuration.

### A hardware module's identity is not a digest

This bears on per-type instance identity (`tmodel:ADR-0002`, `tmodel:DEC-005`) and on `ProductInstance.identifiers` and `version` (`tmodel:DEC-001a`).

- For a hardware module, §B.2.2's Tested Configuration table (L431–L441) identifies each model by its hardware part number and version, its firmware version, and its distinguishing features. Footnote 1 gives ports and interfaces, memory devices and their sizes, and field-replaceable or fixed accessories as examples (L445–L447).
- `tmodel:ADR-0002` names firmware, buses and compute cores as hardware identity, and `tmodel:ADR-0010` keeps an identifier opaque in `identifiers`. The CMVP's tuple fits that slot as several scheme-prefixed values. It is also the identity a FIPS validation is bound to, so a tmodel ProductInstance that should match a validation needs it.

### One policy can cover several versions: a family scope

This bears on `applies_to_family` and `Product.classifications` (`tmodel:ADR-0012`) and on `tmodel:DEC-009`.

<!-- q L515-517 "If the security policy encompasses" .. "illustrated for all versions." -->
> If the security policy encompasses multiple versions of the module, each version is represented separately or annotated that the representation is illustrated for all versions.

- A validation can cover several module versions, each with its own distinguishing features. That is `tmodel:DEC-009`'s case of family members that differ. tmodel cannot scope Evidence to a family yet (`applies_to_family` is a slot of Requirement and RequirementSource only), so a validation that covers several versions is Evidence about each version, and each version's distinguishing features say where the members differ.

### Physical security is kept up by inspection

This bears on the mitigation lifecycle (`tmodel:DEC-009`, `tmodel:R-021`) and on `Evidence.fresh_until` (`tmodel:ADR-0013`).

<!-- q L706-708 -->
> ● Specify the actions required by the operator(s) to ensure that the physical security is maintained (e.g. periodic inspection of tamper-evident seals or testing of tamper response and zeroisation switches).

- §B.2.7's inspection table (L710–L721) pairs each physical security mechanism with a recommended frequency of inspection or test. A tamper-evident seal is a Mitigation whose status holds only while its inspection is current, and the operator is its `implementation_owner`.
- In tmodel the inspection record is Evidence with `fresh_until` set by that frequency. A missed inspection is then visible as stale evidence, without a separate status value.

## Adapt

### The SSP table and access rights against mofn's Key (mofn)

This bears on mofn's `ARCH-0003` §3.3 (the `Key` and `Capability` objects, draft), `SPEC-0001` §5.1, and `ARCH-0003` W-03 and W-18. None of them is a DEC.

<!-- q L809-812 -->
> ● Provide a key table specifying the key type(s), strength(s) in bits, security function(s), security function certification number(s), where and how the key(s) is generated, whether the key(s) is imported or exported, any SSP generation and establishment method used, and indicate any related keys.

<!-- q L650-662 -->
> G = Generate: The module generates or derives the SSP. R = Read: The SSP is read from the module (e.g. the SSP is output). W = Write: The SSP is updated, imported, or written to the module. E = Execute: The module uses the SSP in performing a cryptographic operation. Z = Zeroise: The module zeroises the SSP.

- A mofn `Key` records its id, suite, public key, custody, capabilities, validity, successor and state (active, retired or compromised). The SSP table (L820–L828) records strength, security function and certificate, generation, import and export, establishment, storage, zeroisation, and use with related keys.
- Custody is roughly storage, capabilities roughly use, and successor one kind of related key. Strength follows from the suite. Two things have no place in mofn's Key: whether it can be exported, and whether it has been destroyed. How it was generated has one only for a derived key, whose custody `derived(seed, path)` records it (`ARCH-0003`).
- The access rights make the same point from the other side. A mofn `Capability` says what a key may sign, in which context and syntax. The rights say what may be done to the key itself: generate it, read it out, write it in, use it, or zeroise it. mofn has no counterpart to read (export) or zeroise.
- **Proposal, if mofn records keys held in a module.** Add exportability to `Key`, and a destroyed state beside retired and compromised. `PLAN-0004` §6.1 puts non-exportable hardware keys out of scope for the CLI engine milestone, so neither is needed yet.

### Approved algorithm tables, and a path for functions the CAVP cannot test yet (mofn)

This bears on mofn's `SPEC-0002` §6 (the suite registry) and on the approved-mode question of the `nist-sp-800-140c` notes.

<!-- q L494 -->
> 3 This table includes vendor-affirmed algorithms that are approved but CAVP testing is not yet available.

<!-- q L488-492 "Only the algorithms" .. "approved service of the module." -->
> Only the algorithms, modes/methods, and key lengths/curves/moduli shown in this table are used by an approved service of the module.

- A mofn module's policy would list each suite's signature and digest functions in the Approved Algorithms table (L454–L465), with a CAVP certificate per row, or under footnote 3 where testing does not exist yet. Footnote 2 binds the table to what the approved services use, not to everything a certificate covers.
- So a newly approved function, such as EdDSA if FIPS 186-5 is read as approving it (`fips-140-3` notes, open question 4), has a way into a policy before the CAVP can test it.

### Security levels are a vector of twelve, with an overall rating

This bears on the deferred `RequirementProfile` (`tmodel:ADR-0013`, `tmodel:DEC-001b`) and on `tmodel:DEC-009`.

<!-- q L351-352 -->
> ● A table indicating the individual clause levels and overall level. ● Overall Security Rating of the module and the Security Levels of individual areas.

- The Security Levels table (L358–L388) has twelve rows, ISO/IEC 24759 §6.1 to §6.12, from General to Mitigation of other attacks. FIPS 140-3 lists eleven areas and General is not one of them, yet the table gives General a level too.
- A profile for a validated module therefore needs twelve per-area levels and one overall rating. The template does not say how the overall rating follows from the twelve.

## Reject or hold

### Reject: the template as the security policy requirements

This bears on `RequirementSource` (`tmodel:ADR-0013`).

<!-- q L344-347 "They are not intended to cover all" .. "for clarification purposes." -->
> They are not intended to cover all the requirements from Annex B but rather a subset for clarification purposes.

<!-- q L322-323 -->
> All requirements from ISO/IEC 24759 section 6.14 and ISO/IEC 19790 Annex B apply and are required in the security policy as applicable.

- The additions guide a subset of Annex B, and every requirement of Annex B and of ISO/IEC 24759 §6.14 still applies. Annex B is part of ISO/IEC 19790, which the library holds only as the queued `iso-iec-19790`. A RequirementSource built from this record alone would hold formatting guidance and miss the requirements.

### Hold: everything here, until Revision 1 is read

- The withdrawal notice says Revision 1 supersedes this edition in its entirety. Tables, columns or footnotes this note relies on may have changed.
- **What the library should hold.** SP 800-140Br1, as a new record that `supersedes` this one. `docs/scope.md` §5 folds a new version into the same record, but this record's requirement ids are built on the 2020 text, and CLAUDE.md forbids a citation that silently retargets. A new record keeps the id rule and departs from §5, which excepts only an RFC that obsoletes another; the library already does the same for a NIST revision (`fips-186-5` supersedes `fips-186-4`).

## Open questions and source defects

### 1. The Indicator column is never explained

- The Approved Services and Non-Approved Services tables each end with a column headed Indicator (L641, L666). Nothing in the record says what goes in it. The nearest text in the family is SP 800-140 AS02.20, which defines the approved mode by pointing at ISO/IEC 19790 subclause 7.4.3, a clause the library does not hold.

### 2. Where the authority to modify comes from

<!-- q L176-178 "may modify, add, or delete" .. "ISO/IEC 24759" -->
> may modify, add, or delete Vendor Evidence (VE) and/or Test Evidence (TE) specified under paragraph 6.14 of the ISO/IEC 24759

- This abstract cites paragraph 6.14 of ISO/IEC 24759. SP 800-140 cites paragraph 5.2 of ISO/IEC 24759, and SP 800-140A paragraph 5.2 of ISO/IEC 19790 (`nist-sp-800-140` notes, open question 5).

### 3. Footnotes sit under the wrong heading

- Footnotes print at the foot of the page, so several appear under a heading they do not belong to. Footnotes 8 to 10 (L681–L690) qualify the §B.2.4 services tables but follow the §B.2.5 heading in the text. Footnote 6 (L588) qualifies §B.2.2's last bullet (L556) and footnote 7 (L591–L593) §B.2.3's ports table, and both print in §B.2.4.
- A locator derived from position in the text therefore names the wrong clause for those footnotes, for example R-0005 and R-0010, and so does any tmodel `source_locator` copied from one.

### 4. A section reference without its point

<!-- q L727 -->
> lifecycle of the module: The reference photo or illustrations required in B 2.2 will

- B 2.2 stands for B.2.2, the clause that asks for the photograph.

### 5. The template numbers nothing

- Every table is Table x and every figure Figure x. A completed policy numbers them as its author chooses, so an importer has to key tables by their titles.

### 6. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 181 entries. 27 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it: the notation of §5.2 (8), scope and cross-references (7), the six "No change." sections and R-0035 (7), editions (2), definitions (2) and R-0176, the withdrawal status. The 3 inferred entries R-0179, R-0180 and R-0181 keep a `field` that names tables of `messages.yaml` (the B.2 items, the algorithm-to-service footnotes, the access-rights column) and no field cites them; each rests on stated entries in its `derived_from`, which are cited.
- `messages.yaml`: 301 citations from 22 structures and 87 fields. 67 cite an entry whose lines overlap the field's, 63 one that overlaps the structure's, 151 one within 40 lines of it, and 20 were read. 27 more had no word in common with their field and were read too. Five cite a footnote filed under a later clause than the structure (R-0102, R-0122, R-0123, R-0124 and R-0174); each footnote's own `note` says where its mark is, and each reads as meant. R-0057, a template label, is cited by `ModuleRepresentation.module_type` and also reads as meant.
- The record has no protocol or state machine (`record.yaml` `not_applicable`), so no work product, step or guard joins here.
