---
schema: "library-verification/v1"
id: sp-800-204d-verification
record: sp-800-204d
type: verification
kind: verification
title: "sp-800-204d — FX-1 verify and cross-check passes"
verified: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Verification of sp-800-204d (FX-1 passes 2 and 3)

All checks ran against the source PDF. Three renderings were used: `pdftotext` (reading order),
`pdftotext -raw` (content-stream order) and `pdftotext -tsv` (word coordinates). For Appendix A,
`pdftotext -layout` was used for pp. 35–40.

## Pass 2 — verify

| check | method | result |
|---|---|---|
| Hash | `shasum -a 256 .cache/sp-800-204d.pdf` | `74e404d9…74e8` = `content.sha256` ✔ |
| Currency | https://csrc.nist.gov/pubs/sp/800/204/d/final (2026-10-02) | Final 2024-02-12, draft 2023-08-30, no supersession ✔. The SSDF 1.2 IPD it would remap to is still a draft ✔ |
| Verbatim | All 126 `text` values and all 141 quoted statements in normative.md (plus 2 front-matter strings, which are not source quotes) were normalised to alphanumerics and checked as contiguous substrings, with running heads and page numbers removed | 267/267 source quotes pass. With the reading-order rendering alone, 126/126 requirement texts pass, so no text depends on column interleaving |
| Splices | Contiguity test as above | 0 spliced quotes |
| normative.md ↔ requirements | Each R-tagged quote was compared with its entry's text | 126/126 ids present, 0 mismatches |
| Locators | **All 126** entries: the text was located in the source and mapped to the enclosing numbered (sub)section or appendix | 126/126 correct (sub-locators such as "bullet 3" and "goal 2" are consistent with their section) |
| Counts | `bin/bcp14-count` | 0 ✔ |
| Modals | Lowercase modals counted by region | should 104 / must 32 / shall 1 / may 32. Front matter: should 2, must 0. Body: should 78, must 17. App. A: should 24, must 15. Refs and App. B: 0. Extracted body texts hold should 77 and must 14; App. A texts hold should 6 and must 6. All match the header reconciliation exactly ✔ |
| Native designators | Every `(PULL-PUSH\|COMMIT\|DEPLOY\|GitOps)[-_]REQ-n` was grepped | 15/15, with the mixed `-`/`_` spellings as printed ✔ |
| Completeness sweep | Every body sentence with should/must/shall/required/essential/need to/necessary, and every App. A should/must sentence, was checked for membership in an extracted text | Body: the only residue is lead-ins and descriptive scope sentences, all accounted for in the reconciliation or entry notes. App. A: 1 restatement not carried as its own entry (see below) |
| Appendix A mapping | Table 2 rows were rebuilt from `-tsv` coordinates and `-layout`, and each `basis: stated` `maps_to` was checked against the row that restates the text | 12 SSDF practices, 13 section cells, consistent with `maps_to`. The 3 `basis: inferred` mappings are flagged ✔ |
| Typing | Each entry's normativity was compared with the modals in its text | 1 weakening fixed. 1 mixed lead-in recorded as residual |
| Object model | Definitions were split into fragments and checked against the source. Locators and edge endpoints were checked | 62 objects / 45 edges / 7 gaps. Quoted definitions are verbatim; 4 paraphrased definitions are unquoted (acceptable). All endpoints are defined |

### Defects found and fixed

1. **Typing (weakening).** `R-0012` "It is crucial to assess security risks and implement
   appropriate defensive measures…" was typed `recommendation`. The record's own rule classes "is
   essential" as `requirement`, and "is crucial" is the same strength. It is now `requirement`.
   Counts went from 25 requirement / 67 recommendation to 26 / 66 in requirements.yaml,
   normative.md, README and record.yaml.
2. **Claim (design-notes item 7, summary Limits).** Both said the attestation requirements
   "R-0061–R-0066" have no SSDF mapping in Table 2. In fact R-0061 (environment attestation) is
   restated in the PO.5 and PW.6 rows and is mapped. Corrected to "R-0055, R-0062–R-0066".
3. **Cross-check (state machine).** 10 of the 15 distinct transition triggers (17 transitions) (`post-build-scan`,
   `periodic-pull-and-compare`, `automatic-resync`, `build-horizon-elapsed`, …) were neither a
   protocol.yaml message nor a defined event. An `events:` catalogue was added to
   state-machine.yaml. Each trigger now maps to a protocol flow step or is a named event with its
   source locator. Two inferred ones are flagged.
4. **Dropped restatement (minor).** App. A Table 2 (PO.1 row) restates DEPLOY-REQ-1's second
   sentence, ending "depending on repository visibility" where §5.2 says "the repository's
   visibility". The difference is editorial and the strength is the same. It is recorded in
   R-0097's notes, not as a new entry. This matches the record's rule of a separate entry only for
   wording that matters.

### Claims checked and found correct

The following were all checked against the source. The ERB approval date (2024-01-31, p. ii). The
authors and affiliations. The page count (41, pdfinfo). The front-matter count of one "shall" and
two "should". Source inconsistencies 1–6 in design-notes: the online-key "should not" vs "must
not" escalation, PULL-PUSH-REQ-3 option (a) dropped in App. A, the PULL-PUSH_REQ-1/-2 scope
drift, identifier spellings, the COMMIT-REQ-1 parenthetical, and the unexpanded "VSA" in Table 1
note b. The schema, messages and examples N/A reasons match §1.2 and §6.

## Pass 3 — cross-check

- protocol.yaml: all 4 flows use only the 15 declared roles, and every cited `R-NNNN` exists.
  The note also lists push protection as a flow, but it is folded into F3 step 2. That is
  consistent.
- state-machine.yaml: every R-id exists. Every trigger is now defined (fix 3). Guards cite
  entries whose text supports them (R-0099/R-0100/R-0101 admission, R-0113 build horizon, R-0109
  drift).
- object-model.yaml: every R-id or section locator resolves.
- `maps_to` targets use SSDF v1.1 native ids (`PO.1` …) and name `sp-800-218` (SSDF 1.1) as the
  edition.
- Messages and schema are N/A. The source names attestation contents only by category, which is
  true.

## Residual / open

- `R-0085` "Appropriate forms of testing should be performed before code commits, and the following
  requirements must be met:" is a compound lead-in typed `recommendation`. The "must" governs the
  bullets, which carry their own entries. A human should decide whether to split it.
- Derived fields (actor, nature, phase, verification) and the derived protocol and state machine
  are unreviewed. The source names no states or messages.
- Human review (pass 4) is outstanding.

Scripts: session scratchpad `verify/` (`vcheck.py`, `omcheck.py` and the inline checks). They are
not committed.
