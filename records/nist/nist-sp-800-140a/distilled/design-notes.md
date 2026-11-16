---
schema: "library-distilled/v1"
id: nist-sp-800-140a-design-notes
record: nist-sp-800-140a
type: design-notes
updated: "2026-11-15"
---

# NIST SP 800-140A (CMVP documentation requirements): design notes for tmodel and mofn

This note covers how SP 800-140A bears on `tmodel:DEC-009`, the record's `bears_on`. It found nothing that bears on a mofn decision.

- **Read against** tmodel@ddac1b9 and mofn@10e357f, as the `fips-140-3` notes are. A tmodel id is written `tmodel:…`; a bare id is mofn's.
- **What it is.** The CMVP's change to the documentation requirements of ISO/IEC 19790 Annex A and to their tests in ISO/IEC 24759 §6.13. The change is one assertion, ASA.01, with one vendor-evidence item and one test procedure.
- **Source.** `.cache/nist-sp-800-140a.txt`, sha256 `d8ec47e2b448ca8a055f7d55e8aa69c7ca9ff70e55ede4bb0213ef737ae27154`, the pinned `source_text_digest`. It renders the PDF whose sha256, `0fc31c5fdb7bd4a33a2490897d509da1fdedba59e10c46729ce11831fb611fd1`, equals `content.sha256` and the skeleton's `source_digest`. All three were recomputed in this pass.
- **Ids.** `R-NNNN` means `nist-sp-800-140a#R-NNNN`. A script emits every id from `requirements.yaml`: it selects the entry whose `source_lines` start on a given line, narrowed by a phrase of its text, and raises unless exactly one matches.

## Adopt

### A documentation floor is a requirement of kind documentation

This bears on `RequirementKind` (`tmodel:ADR-0012`, `tmodel:DEC-001a`), on `Evidence` (`tmodel:ADR-0013`) and on `tmodel:DEC-009`.

<!-- q L260-262 -->
> This annex {ISO/IEC 19790 Annex A} specifies the minimum documentation which shall be required for a cryptographic module that is to undergo an independent verification scheme {and the documentation shall meet those requirements}.

<!-- q L266-268 -->
> VEA.01.02: The vendor shall provide documentation for a cryptographic module that fulfils but is not limited to the minimum documentation requirements as specified in the validation authority requirement and management documentation.

- R-0003 and R-0004 make documentation a requirement with a floor. R-0005 has the tester verify it. In tmodel that is a Requirement with `requirement_kind: documentation`. The vendor's documents are `Evidence` with `evidence_kind: document`, which records a link to the Requirement, not that it is met: tmodel discharges a Requirement through `satisfied_by` a Mitigation, or through an SdlPractice that `implements` it and `produces` the Evidence.
- The floor is a minimum, not a list: the vendor's documentation fulfils the requirements but is not limited to them. A RequirementSource built from this record holds one obligation, stated three times (ASA.01, VEA.01.02 and TEA.01.02). The documents it asks for are named elsewhere.

## Adapt

### The floor is defined in a document nobody names

This bears on `RequirementSource.source_ref` (`tmodel:ADR-0013`).

- R-0004 sets the floor by the validation authority requirement and management documentation. The record gives no title, number or edition for it, and its references are only ISO/IEC 19790, ISO/IEC 24759 and FIPS 140-3 (§2).
- The library has no record that could be it. A search of every `record.yaml` for CMVP finds the eight records of this family, four algorithm standards (FIPS 186-4, FIPS 186-5, SP 800-186, SP 800-56A Rev. 3) and the CNSA 2.0 FAQ.
- So a tmodel Requirement from VEA.01.02 can point `source_ref` at this record and VEA.01.02, but its floor has no RequirementSource to name (`tmodel:ADR-0013`). Carry the floor as unresolved, rather than guessing a document.

## Reject or hold

### mofn: nothing to take

- The record governs what a vendor hands a testing laboratory. mofn submits no module for validation, and the `fips-140-3` notes record that no route to a validated deployment is open today. No mofn decision, specification section or proposal rests on it.

### Hold: Annex A itself

- ASA.01 has ISO/IEC 19790 Annex A specify the minimum documentation, a second floor beside VEA.01.02's. The library holds Annex A only as the record `iso-iec-19790`: not fetched, no digest, and under a licence that forbids AI processing, so it is not read here. tmodel can carry the CMVP's change but not the Annex A documents the change applies to.

## Open questions and source defects

### 1. Which paragraph gives the CMVP its authority

<!-- q L124-126 "As a validation authority" .. "ISO/IEC 19790." -->
> As a validation authority, the Cryptographic Module Validation Program (CMVP) may modify, add, or delete Vendor Evidence (VE) and/or Test Evidence (TE) as specified under paragraph 5.2 of the ISO/IEC 19790.

- This abstract cites paragraph 5.2 of ISO/IEC 19790. SP 800-140's abstract cites paragraph 5.2 of ISO/IEC 24759 for the same authority (`nist-sp-800-140` notes, open question 5). VE and TE items are ISO/IEC 24759's, so one of the two citations is probably wrong. Both ISO/IEC standards are paywalled, so the library cannot check which.

### 2. The §6.1 lead-in is garbled

<!-- q L255-256 -->
> ISO/IEC 24759 6.13 A- and ISO/IEC 24759 Documentation requirements are modified as indicated below:

- The sentence (R-0019) names ISO/IEC 24759 twice and leaves A- hanging. §5.1 (R-0001) calls the clause 6.13 A – Documentation requirements of ISO/IEC 24759. The lead-in reads like that title with an added or a deleted fragment beside it, the marks lost in the text layer (`nist-sp-800-140` notes).

### 3. The braces are not explained

- R-0003 puts two phrases in braces. SP 800-140 uses braces the same way, and there AS10.01 and AS10.02 brace the two halves of one sentence, which suggests a brace marks a clause another assertion tests. Neither record says so; the convention belongs to ISO/IEC 24759.

### 4. Pass 3 joins: what our artifacts do not yet agree on

These are differences between our own artifacts, found by script in the cross-check. None is a source defect.

- `requirements.yaml` `field`: 22 entries. 12 stated entries name no structure, step or state and keep a descriptive `field`: what they constrain is real, but no message structure, flow step or state models it (the notation of §5.2, scope, editions, definitions and the ASA.01 heading, whose levels 1 to 4 no field carries). The 2 inferred entries R-0021 and R-0022 keep a `field` and no field cites them; each rests on stated entries in its `derived_from`.
- `messages.yaml`: 12 citations from 1 structure and 5 fields; 3 cite an entry whose lines overlap the field's, 3 one that overlaps the structure's, 6 one within 40 lines, all read as meant.
- `protocol.yaml` `work_products`: 1 of 2 carries a `structure` (`module documentation` holds `MinimumDocumentation`); `documentation verification` carries `structure: none`, because the source defines no record of the tester's check.
- Ids added by pass 3: R-0006 and R-0008, the children that carry the shall of R-0001 and R-0003, in F01.
