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
| normative | normative.md | every stated entry of requirements.yaml as a quotation marker in source order (202 quotations, each the full text of the id under it, R-0054's among them; the 72 split children listed beside their parents; the 16 inferred entries named in place); the one keyword in non-normative text (L527); source defects SD-1 to SD-33 and SD-E. Not covered: notes, examples and sections marked non-normative, except as accounted for |
| requirements | requirements.yaml | all 106 BCP 14 keywords of the source placed by line, in the 78 keyword-bearing entries (one of them, R-0054, is withdrawn: its sentence sits in a Note, non-normative, and it binds nothing); 72 split children, 124 keyword-less stated entries, 16 inferred; 290 entries. Candidates: 212, every one with a verdict (49 stated, 163 rejected). Not covered: the 17 advisory sentences with no skeleton cue, read under the same policy and listed in the note |
| schema | schema/ | the source has no grammar: 14 formal displays copied verbatim (inline.verbatim.txt); 7 derived JSON Schemas, a rule index with 4 cross-field rules and 6 digest pins, 302 test cases (0 differing) and their runner. Not covered: the contents of proofValue, JSON-LD term mapping, calendar validity |
| messages | messages.yaml | 23 structures and 85 fields, 5 encoding rules, 9 source tensions; 211 of the 290 requirement ids wired (re-wired in pass 2; R-0054 added in pass 3), the other 79 listed with reasons. Not covered: Multibase, Multikey and verification methods beyond what this source says (Controlled Identifiers v1.0) |
| protocol | protocol.yaml, protocol.md | 12 roles, 19 flows (122 steps), one Mermaid diagram per flow, errors and their semantics, source defects D-01 to D-21; the source defines local algorithms and no wire exchange, so deliveries between parties are marked inferred |
| state-machine | state-machine.yaml | 11 machines, 91 states, 105 transitions: the five algorithms of §4.2 to §4.6, a document's proof structure, verification-method retrieval, the receiving pipeline of §4.1, the proof validity window, challenge use and context-document resolution; 8 things not modelled, each with a reason |
| examples | examples/ | all 14 examples as verbatim fixtures plus 12 derived (reproduce.py: 26 examined, 0 different); 26 vectors, 174 checks; 7 proof signatures tried with a recipe validated against the cryptosuite Recommendations' own vectors (verify-signatures.derived.py: 11 checks, 0 failing), none verifies; 6 digests of section 2.4 measured. Findings EXD-01 to EXD-11 |
| design-notes | design-notes.md | adopt, adapt and reject against ARCH-0001, ARCH-0002, ADR-0001 to ADR-0005, SPEC-0001, SPEC-0002, MD-3 and DEC-002 at m-of-n a56a3c0 (47 mapping rows, 55 m-of-n quotations checked by qm.py); MD-3 and option 5 member by member, with where the source cuts against them; R-O-05 clause by clause; the R-I-06 export table; 12 open questions |
| cross-check | crosscheck.yaml, crosscheck.derived.py | pass 3 joins, by script: the protocol-to-messages join table (33 message and returns items, 31 resolved to a structure, 2 with none, open question 12), the trigger join of the 105 state-machine transitions (45 step, 19 message, 41 named event, 0 unclassified), the 110 field atoms of requirements.yaml against messages.yaml and the schema, the 14 examples against the schema, and the defect-id inventory behind the crosswalk below. Re-run: `python3 -I crosscheck.derived.py [--lib DIR] [--write]` |

## Defect crosswalk

Five schemes record the source's defects, each in its own file, and the same defect is often recorded under
several ids. Cite with the prefix: **P:D-NN** (protocol.yaml `source_defects`; state-machine.yaml cites the same ids and
defines none), **N:SD-n** (normative.md), **M:T-nn** (messages.yaml `source_tensions`; schema/README.md repeats
them under the same ids), **DN:Dn** (design-notes.md section 9) and **X:EXD-nn** (examples/README.md). `D-01` and
`D1` are different spellings and not always the same defect (DN:D2 is P:D-03, not P:D-02); `T-07` (a tension) is not `T07`
(a transition id inside one state machine). Pass 3 renamed the examples' findings from `D-01` to `D-11` to `EXD-01` to
`EXD-11`, because protocol.yaml already used `D-01` to `D-11` for other defects; the three "see D-10" pointers in
examples/vectors.yaml named the vocabulary-digest finding, which is `EXD-09`, and now say so.

| source defect | P (protocol.yaml, state-machine.yaml) | N (normative.md) | M (messages.yaml, schema/README.md) | DN (design-notes.md) | X (examples) |
|---|---|---|---|---|---|
| §4.5 initialises `status`, sets `verified`, tests `status` | D-01 | SD-7 | T-05 | D1 | |
| §4.5 over an empty proof list reports status true | D-21 | SD-33 | | D1 (related) | |
| §4.5 reads a `mediaType` the cryptosuite result lacks; result members named differently | D-02 | SD-10 | T-05 | D3 | |
| §4.5 runs §4.4 steps 4 to 8 without their inputs and not on the proof under test | D-03 | SD-9 | T-07 | D2 | |
| §4.4 raises an error as a result, §4.5 as an exception | D-04 | SD-8 | | D8 | |
| §4.5 assumes `proof` is a list | D-05 | | | | |
| §4.4 step 9 returns the input `mediaType` when `verified` is false | D-06 | SD-30 | | D3 (related) | |
| §4.6 step 4 removes a property the result does not have | D-07 | SD-19 | T-06 | D3 (related) | |
| §4.6 step 1 initialises `compactionContext`, never used | D-08 | SD-31 | | | |
| `PARSING_ERROR`, `DATA_LOSS_DETECTION_ERROR` used, not defined in §4.7 | D-09 | SD-6 | T-04 | D5 | |
| `previousProof` elements are strings, then have an `id` | D-10 | SD-12 | | D4 | |
| nothing sets the new proof's `previousProof` from the options | D-11 | SD-17 (last sentence) | | | |
| §4.3 output omits the error case | D-12 | SD-18 | | | |
| an input document may carry a proof that Add Proof replaces | D-13 | SD-23 | | | |
| Appendix A prose against Example 14 (non-normative) | D-14 | | | | |
| `created` and `expires` checked by no step | D-15 | SD-14 | | | |
| proof purpose and domain checks: imperative, SHOULD, or run by the algorithm | D-16 | SD-15, SD-16 | | | |
| context validation order: MUST after, MAY reorder | D-17 | SD-29 | | | |
| §4.4 step 1 has no failure path | D-18 | SD-32 | | D7 (related) | |
| proof ids are not required to be distinct | D-19 | SD-28 | | | |
| `domain`: string, set or list; equality or membership | D-20 | SD-16 | T-08 | | |
| `verificationMethod` OPTIONAL in §2.1, required by §4.2 and §4.4 | | SD-3 | T-01 | D6 | |
| `proofValue` MUST in §3.1, replaceable in §2.1; "mandatory proof value properties" undefined | | SD-5 | T-02 | | |
| `revocation` or `revoked` | | SD-22 | T-03 | | |
| typographical and editorial errors, left as printed | | SD-E | T-09 | D10 | |
| §4.4: cryptosuite error, warnings and errors unhandled | | SD-13 | | | |
| one signature across syntaxes, one syntax in the algorithm | | | | D7 | |
| §1.3 and §1.4 inside a non-normative section | | SD-1 | | | |
| a BCP 14 keyword inside a Note (the withdrawn R-0054) | | SD-2 | | | |
| offset-less time values | | SD-4 | | | |
| §4.5 returns two values | | SD-11 | | | |
| `knownContext` a set by name, an exact value by use | | SD-20 | | | |
| the vocabulary URL and its hash named after the rule that uses them | | SD-21 | | | |
| "proof value" means two things | | SD-24 | | | |
| the poison-graph requirement has no keyword | | SD-25 | | | |
| cryptosuite identifiers have no closed list | | SD-26 | | | |
| `digestMultibase` has no verification procedure | | SD-27 | | | |
| Examples 1 and 3 end with `};` | | | | D9 | EXD-01 |
| Examples 5, 6, 7, 10 to 14 carry `//` comments | | | | D9 | EXD-02 |
| Example 8 elides with `...` | | | | D9 | EXD-03 |
| Examples 9 to 14 are symbolic | | | | D9 | EXD-04 |
| `proofValue` of Examples 2 and 7 decodes to 65 octets | | | | D9 | EXD-05 |
| `proofValue`s that rearrange one another's characters | | | | D9 | EXD-06 |
| second key of Examples 6 and 7 is a rearrangement and not a multikey | | | | D9 | EXD-07 |
| none of the 7 proofs verifies under its printed key | | | | D9 | EXD-08 |
| §2.4's vocabulary digests equal none of the documents served | | | | D9 | EXD-09 |
| Example 3 is Example 4 minus its proof and one context; Example 1 is Example 2 minus its proof | | | | D9 | EXD-10 |
| Examples 4 and 5 use the vc-di-ecdsa test-vector key | | | | D9 | EXD-11 |

Every id defined in the five schemes is in this table (85 ids, none defined twice; `crosscheck.derived.py` checks both).
