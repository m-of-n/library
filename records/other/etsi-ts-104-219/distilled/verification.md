---
schema: "library-distilled/v1"
id: etsi-ts-104-219-verification
record: etsi-ts-104-219
type: verification
updated: "2026-10-03"
---

# Verification — ETSI TS 104 219 V1.1.1 (SSDIF): FX-1 passes 2 (verify) and 3 (cross-check)

By: claude (independent verifier, did not extract). Effort: max. Run 2026-10-02/03.
Every check below was scripted against the source (`.cache/etsi-ts-104-219.txt`, plus fresh `pdftotext -raw` and default
renderings of the same PDF), never against the summary. The scripts are in the session scratchpad (`verify-f/`):
`vb.py`/`vb2.py` (verbatim), `vbt.py` (task-row verbatim), `vnm.py` (normative.md), `loc2.py` (locator and DG scope),
`b2.py`/`b2cmp.py` (independent Annex B.2 re-parse), `b1.py` (Annex B.1), `ssdfcmp.py` (B.2 vs SP 800-218 v1.1),
`om.py` (object model), `xc.py` (cross-check).

## Pass 2 — verify

**Hash and currency.** The cached PDF and the lane copy (`sdlscan/ts104219.pdf`) both hash to `17aee144…7c15`,
matching `content.sha256`. The ETSI deliver directory `104219/` lists only `01.01.01_60` (dated 2026-03-19), and the
document's History lists only V1.1.1 (March 2026), so V1.1.1 is current. PDF metadata: created 2026-03-06, modified
2026-03-19, 78 pages. These match the summary. The SAFECode blog "A New International Standard for Software Security"
confirms that ETSI adopted the work item in January 2026, as a V0.0.7 draft.

**Verbatim.** Every check is a contiguous substring check after normalising whitespace, hyphenation, quotes and
ligatures. A token-subsequence check cannot catch splices, so it was not used.
- `requirements[].text`: 220/220 pass.
- Task rows: 328 texts (titles, DG artifacts, implementation examples). The first run found **1 miss, a splice**:
  - The PO.5.2 task title began "following a zero trust architecture. Secure and harden…". Those words are the tail of
    PO.5.1 implementation example 10, which had been truncated.
  - Fixed in `requirements.yaml` and `normative.md`. Example 10 is complete again and the PO.5.2 statement starts at
    "Secure and harden".
- `normative.md`: 949 quoted lines checked. The only misses are editorial notes and headings, not quotations.

**Locators.** All 186 task-table entries were checked, not a sample: each text lies inside its stated task region.
Each action's DG-scope header (DG 1/2/3, DG 2/3, DG 3) was also confirmed to be the one governing it in the source. 0
defects (three PO.3.2 "DG 2/3" hits were a false alarm: the source omits the colon). Of the 34 prose recommendations:
- 33 locators confirmed by line.
- R-0008 said "§5.0.2 (prose)", but the text is in the Table 5.0-2 DG3 Description cell. Fixed.

**Completeness.**
- `bin/bcp14-count` = 0. The ETSI baseline was recounted from the source: numbered actions in the clause 5.1.1–5.6.1
  tables = 183 (111 shall, 72 should). This matches `counts` and the requirements file.
- Every lower-case shall/should/must occurrence in the Introduction to 5.6.1 was walked line by line. Each is either
  extracted (R-0001…R-0034, DG actions), a definition or quoted term ("shall fix"), the modal clause, informative
  Implementation Examples, or descriptive.
- Bulleted cells in DG Specific Actions rows (PW.5.1, RV.2.2) were checked: they are DG Artifacts, and all are captured
  in `tasks[].dg_artifacts`.
- No drops found.

**Annex B.2, verified exhaustively.** It feeds the consolidated SDL crosswalk, so it was re-parsed independently from
the layout text: right column only, rows joined across page breaks, line-wrap hyphens rejoined, split on task ids.
- Result: 519 rows over 29 frameworks.
- This matches `requirements.yaml` `maps_to` and `normative.md` row-for-row (multiset of framework, task, ref).
- The only differences were 2 line-wrap artefacts in CNCF ("Securing Deployments— Verification" with a stray space,
  PO.3.1 and PS.2.1). Fixed in requirements.yaml, crosswalk.yaml and normative.md.

**Annex B.2 against its own upstream (SP 800-218 v1.1 References, from `records/nist/sp-800-218`).** This check found a
**source defect that matters for the crosswalk.**
- In ten framework rows the TS prints "PW.1.1" twice: BSAFSS SM.2, BSIMM SE3.6, CNCF "Securing Materials—Verification,
  Automation", EO 14028 4e(vi)/(vii)/(ix)/(x), NTIA SBOM "All", OWASP SCVS "1.4, 2", SAFECode SCSIC, SAFECode SCTPC
  MAINTAIN3, SP 800-53 "SA-8, SR-3, SR-4" and SP 800-161 "SA-8, SR-3, SR-4".
- The first of each pair sits between PS.3.1 and PW.1.1. Its provisions are exactly SSDF's **PS.3.2** references
  (provenance/SBOM).
- These rows are kept as printed, flagged `ssdf_1_1_task: "PS.3.2"` plus `source_defect`, and noted in
  `crosswalk.yaml` and design-notes item 7.
- Also flagged: MASVS PO.1.1 is printed "1.1" (SSDF: 1.10). ETSI also omits SSDF's BSIMM rows for PO.1.1–PO.1.3 and the
  SP 800-181 rows for PO.1.1–PO.2.3. Those omissions are recorded, not extraction drops.

**Annex A and B.1.**
- Annex A: all 54 task-bearing rows were checked against the source table. The "All" and "Not covered" rows and the
  trailing-comma cell I.II(1) "*PW.4.1, *PW.4.4," are carried faithfully.
- Annex B.1: all 70 claims match the source action-id cells. 1.1.4's parenthetical and 1.2.5's "*RV [all tasks]" are
  preserved; 5.1.5 is unmapped in the source.
- The CSC Safeguard and SAFECode rows of all 42 tasks were compared with the source: 0 defects.

**Typing.**
- verb equals the leading modal of every action, and shall ⇒ requirement, should ⇒ recommendation: 0 mismatches.
- One mixed sentence (PW.8.2 DG3 #7, "should consider … 'shall fix'") is correctly typed should.
- Residual: the 3 "same as" inheritance entries are typed requirement although they inherit both shall and should
  actions.

**Object model.** 60 objects and 36 edges, all with locators. 2 edges are inferred and flagged. Every edge endpoint is a
defined object. `tmodel_mapping` targets exist in ARCH-0001 v0.2.0 or DL-0009 (SecurityProgram and Evidence are DL-0009
terms). Sampled locators (DevelopmentGroup, Role, Artifact, SSDIFAction, ImplementationExample) all support their
objects.

**Claims (summary.md, design-notes.md).** The following were checked against the source:
- 42 tasks; 183 actions (111/72); 14 roles.
- "6 Essential Practices that group 42 SSDIF specific actions" (executive summary).
- The [i.100]/[i.101] misreferences in §5.6.0.
- "EO 14036" in [i.13]; "(APT)"; "echanisms"; "should should" (PW.4.2 #8).
- PW.1.1 → IEC SM-4/SR-1/SR-2/SD-1; RV.1.3 → DM-1…DM-5.
- PO.4.1 #4–#6 as the bug-bar gate; PW.8.2 DG3 #4 as the shall-fix list.
- Every claim is supported.

## Pass 3 — cross-check

- Every `constrained_by` id in messages.yaml, protocol.yaml and state-machine.yaml resolves to a requirements.yaml id
  (0 dangling).
- All 15 messages have a derived schema, and every schema has a message.
- protocol.yaml names 18 flow messages that messages.yaml did not define, such as VulnerabilityReport, TriageResult,
  SecurityAdvisory and SignedRelease. They were added to messages.yaml as `events` with
  `content_prescribed: false`, the flows and steps that use them, and their constraining ids. The TS prescribes no
  fields for them, so no schema was invented.
- `maps_to` targets name their edition (CRA = Regulation (EU) 2024/2847; CRT APC v1.0; the B.2 frameworks with their
  [i.n] refs). The 54 Annex A rows now carry `target_id` into `eu-cra-2024-2847` (`AnnexI-PartI(2)(x)`,
  `AnnexI-PartII(n)`), and all resolve.
- `not_applicable: examples` is true: the TS has no worked examples or vectors.

## Residual open issues

- State-machine triggers are prose descriptions tied to action locators, not ids of defined events. Only the protocol
  messages were promoted to `events`.
- B.2 refs for the CSC, SAFECode and B.2 frameworks are verbatim cell strings, not split into atomic provision ids (one
  ref may list several provisions). The consolidated crosswalk must split them, and must key the ten flagged rows to
  PS.3.2.
- Derived fields (actor, nature, phase, testable) still need human review (`reviewed_by` empty).
