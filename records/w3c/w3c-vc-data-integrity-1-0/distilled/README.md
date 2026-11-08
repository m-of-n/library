---
record: w3c-vc-data-integrity-1-0
kind: index
title: "w3c-vc-data-integrity-1-0 — distilled artifacts"
extracted: "2026-11-07"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | every stated entry of requirements.yaml as a quotation marker in source order (201 quotations, each the full text of the id under it; the 72 split children listed beside their parents; the 16 inferred entries named in place); the one keyword in non-normative text (L527); source defects SD-1 to SD-33 and SD-E. Not covered: notes, examples and sections marked non-normative, except as accounted for |
| requirements | requirements.yaml | all 106 BCP 14 keywords of the source placed by line: 105 in the 77 keyword-bearing entries, 1 in the retired R-0054 (a Note, non-normative); 72 split children, 124 keyword-less stated entries, 16 inferred; 289 entries. Candidates: 212, every one with a verdict (49 stated, 163 rejected). Not covered: the 17 advisory sentences with no skeleton cue, read under the same policy and listed in the note |
| schema | schema/ | the source has no grammar: 14 formal displays copied verbatim (inline.verbatim.txt); 7 derived JSON Schemas, a rule index with 4 cross-field rules and 6 digest pins, 302 test cases (0 differing) and their runner. Not covered: the contents of proofValue, JSON-LD term mapping, calendar validity |
| messages | messages.yaml | 23 structures and 85 fields, 5 encoding rules, 9 source tensions; 210 of the 289 requirement ids wired (re-wired in pass 2), the other 79 listed with reasons. Not covered: Multibase, Multikey and verification methods beyond what this source says (Controlled Identifiers v1.0) |
| protocol | protocol.yaml, protocol.md | 12 roles, 19 flows (122 steps), one Mermaid diagram per flow, errors and their semantics, source defects D-01 to D-21; the source defines local algorithms and no wire exchange, so deliveries between parties are marked inferred |
| state-machine | state-machine.yaml | 11 machines, 91 states, 105 transitions: the five algorithms of §4.2 to §4.6, a document's proof structure, verification-method retrieval, the receiving pipeline of §4.1, the proof validity window, challenge use and context-document resolution; 8 things not modelled, each with a reason |
| examples | examples/ | all 14 examples as verbatim fixtures plus 12 derived (reproduce.py: 26 examined, 0 different); 26 vectors, 174 checks; 7 proof signatures tried with a recipe validated against the cryptosuite Recommendations' own vectors (verify-signatures.derived.py: 11 checks, 0 failing), none verifies; 6 digests of section 2.4 measured. Findings D-01 to D-11 |
| design-notes | design-notes.md | adopt, adapt and reject against ARCH-0001, ARCH-0002, ADR-0001 to ADR-0005, SPEC-0001, SPEC-0002, MD-3 and DEC-002 at m-of-n a56a3c0 (47 mapping rows, 55 m-of-n quotations checked by qm.py); MD-3 and option 5 member by member, with where the source cuts against them; R-O-05 clause by clause; the R-I-06 export table; 11 open questions |
