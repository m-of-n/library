---
record: owasp-asvs-5
kind: verification
title: "owasp-asvs-5 — FX-1 pass 2 (verify) and pass 3 (cross-check)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# OWASP ASVS 5.0.0: verification report

Passes 2 and 3 of FX-1, run on 2026-10-02 by an agent that did not do the extraction. Every
comparison was made against the release assets in `.cache/lane-e/asvs/` (JSON, CSV, flat, legacy,
CycloneDX, PDF) and the tag's English Markdown (`.cache/lane-e/asvs/md/`). The extractor's
`gen.py` was not used. The scripts are `verify/asvs.py`, `asvs_add.py`, `reqcheck.py`,
`kwcover.py`, `typing.py` and `revcheck.py`. The PDF was re-rendered with `pdftotext -layout`.

## Pass 2: verify

### 1. Hash and currency

- The sha256 of every release asset equals the value recorded in `record.yaml` or
  `requirements.yaml`: JSON `bcdbec21…cb35`, CSV, PDF, flat, cdx and xml. ✔
- The GitHub releases API shows `v5.0.0_release` (2025-05-30) as the latest stable release. The
  only newer release is the auto-rebuilt "Bleeding Edge" `latest` (2026-09-03), whose notes say
  "The latest stable release is v5.0.0". The tags list has no other `v5*` tag.
- The OWASP project page reads "Get the latest stable version of the ASVS (5.0.0)".
- **The record tracks the current edition.** ✔

### 2. Verbatim

- All 345 requirements were compared independently against the JSON export. Description, `L`,
  chapter and section ids and names, and `cite_as` are all identical. The Markdown table rows were
  re-parsed (345) and are byte-identical to the JSON. The level split is L1 70 / L2 183 / L3 92.
- All 66 non-row entries (F-*, AppC-*, AppD-*) are verbatim substrings of the Markdown.
- `normative.md` was walked in reverse: every source sentence of the framing chapters, V1–V17 and
  Appendices C and D is present. The only absences are the per-chapter "References" lists, a
  documented omission.
- No splices were found.

### 3. Locators

All 345 requirement locators were checked:

- the section name and row id are in the locator;
- the named Markdown file holds the row;
- the PDF page given holds the row id on that page (345/345). Seven rows have text wrapped across
  table columns, so the check fell back to finding the row id at line start on that page. All
  seven were on the stated page.

All AppC and F locators name the right file and heading.

### 4. Completeness

- `bin/bcp14-count` gives 11 (MUST 7, MUST NOT 3, MAY 1), all in `0x92-Appendix-C_Cryptography.md`.
  All 11 occurrences are covered by AppC texts, and the header's 11 = 11 holds.
- The document's own baseline, 345 requirement rows in 17 chapters and 80 sections, is fully
  extracted.
- **Lowercase normative sweep.** Every sentence in the framing and chapter Markdown containing
  must, shall, should, required, recommended, may not, must not or should not was checked against
  the requirement texts.
  - **Defect V-1, dropped, fixed:** two Appendix C statements were missing.
    - AppC-24: "While the usage of such these mechanisms … they should be replaced by more secure
      and future-proof mechanisms as soon as possible." This is the second sentence of the Legacy
      legend bullet; AppC-01 holds only the first.
    - AppC-25: "However, serious consideration should be given to understanding the nature … of the
      original key prior to committing to a wrap/unwrap procedure …" (Key Wrapping).
  - **Defect V-2, dropped, fixed:** 48 prescriptive chapter-prose statements in Control Objectives
    and section introductions were not itemized. They were added as **P-01..P-48**, verbatim, with
    computed heading-path locators and modal-derived normativity: 22 requirement (must, must not,
    shall), 26 recommendation. Examples:
    - "L2 applications must force the use of multi-factor authentication (MFA)." (V6.3)
    - "L3 applications must use hardware-based authentication, performed in an attested and trusted
      execution environment (TEE)."
    - "A risk analysis with documented security decisions related to session handling must be
      conducted as a prerequisite to implementation and testing." (V7.1)
    - the three OAuth "shall only be consumed by" token rules (V10)
    - "The application's default configuration must be secure for use on the Internet." (V13)
    - "Logging must not compromise privacy or system security." (V16)
    - the WebRTC signaling MUSTs (V17.3)

    Each is marked as chapter prose, not a verifiable ASVS row, with `testable: partial`. Purely
    descriptive sentences such as "This section describes which … should be set" were deliberately
    not itemized.
  - The header `counts` and `note`, `record.yaml` coverage, `distilled/README.md` and `summary.md`
    were updated: 25 AppC, 48 P-*.
  - No uppercase keyword was added, so `extracted_keyword_count` stays at 11.

### 5. Typing

- All 345 rows are `requirement` / `verify`. ASVS defines every row as a "must" requirement (F-04).
- The 11 BCP 14 AppC entries carry their strongest keyword. AppC-13 holds both MAY and MUST and is
  typed requirement / MUST, which is correct.
- Every `level` and `levels` value equals the JSON `L` and its cumulative expansion.
- No weakening was found.

### 6. Object model

- **Defect V-3, fixed:** `has_status.to` was free text, `ApprovalStatus (A|L|D)`. A stated
  `ApprovalStatus` object was added (Appendix C legend).
- **Defect V-4, fixed:** `RiskAnalysis` was `kind: inferred`, but the source names it explicitly:
  V7.3.1 says "according to risk analysis and documented security decisions", and the V7.1 prose
  is now P-18. It was re-typed to stated, with locators.
- **Defect V-5, fixed:** 7 objects had no edge. Eight stated edges were added:
  - CertifyingOrganization `issues_report` (F-20 wording, verbatim);
  - KeyManagementPolicy `governs_keys` (V11.1.1);
  - Application `relies_on` ExternalService (V13.1.1);
  - LogInventory `documents_logging_of` (V16.1.1);
  - Mapping `maps_from_v4` and `legacy_weakness`;
  - RiskAnalysis `informs` DocumentedSecurityDecision;
  - Recommendation `appendix_of` Standard.
- The total is 43 objects and 45 edges.

### 7. Claims

All of these were checked against the source:

- the 20% / 50% / 70% / ~30% level shares (`0x03`);
- "Get the latest stable version …";
- the CC BY-SA 4.0 licence and project leads (`0x01`);
- 17 chapters / 80 sections;
- removal of the V1 Architecture chapter and of the CWE/NIST mappings (`0x05`);
- 31 documentation requirements in the first section of 11 chapters;
- V13.3.1's L3 HSM clause;
- V13.1.4 as the only requirement naming a threat model;
- the empty CycloneDX `levels[].requirements` (all three levels have 0 requirements);
- the typos "execptions" and "onyly", which are in the source.

**Defect V-6, fixed.** `design-notes.md` claimed `related_documentation_section` on 27
implementation requirements. The file holds 26, and the text was corrected.

## Pass 3: cross-check

- **`maps_to` to v4.0.3, source-published.** This was recomputed independently from
  `5.0/mappings/mapping_v5.0.0_to_v4.0.3.yml`.
  - **Defect V-7, fixed.** 9 `v4_0_3_mapping` raw values were truncated: the pass-1 reader lost the
    YAML continuation lines, for example 6.5.1 ended "… SPLIT FROM". They are now verbatim.
  - The same truncation dropped or mis-typed `maps_to` links on 18 requirements. Continuation ids
    were tagged `(listed)` instead of inheriting the preceding relation, and trailing `SPLIT FROM` /
    `COVERS` clauses were lost. All 18 were regenerated.
  - Result: 265 link entries on 190 requirements (MOVED FROM 156, SPLIT FROM 44, COVERS 33,
    MERGED FROM 31, DEPRECATES 1). Every entry uses the target's own id form `v4.0.3-x.y.z`, and
    the scheme name carries the edition.
- **CWE, inferred.** The composition `v5.0.be_cwe_mapping.json × mapping_v5.0.be_to_v5.0.0.yml` was
  re-derived and equals the record on all 204 requirements. Eight `v5.0.be` ids with a CWE did not
  survive into 5.0.0 and are correctly absent.
- **Schemas and examples.** All three derived JSON Schemas validate their assets: export JSON 0
  errors, flat JSON 0 errors, legacy 345 items 0 errors. `examples/export-v1.1.1.json` excerpts are
  equal to the nested JSON, flat JSON, CSV lines, legacy item, CycloneDX requirements and levels.
  `examples/identifiers.yaml` checks out:
  - the expected text of `v5.0.0-1.2.5` is correct;
  - V1 has 5 sections, so `1.11.3` is unresolvable;
  - V1.2 ends at 1.2.10;
  - `v4.0.3-2.2.1` maps to 6.3.1 and 6.1.1 in the published 4→5 file.
- **Crypto registry.** All 14 tables and 120 rows of `crypto-registry.yaml` equal the Appendix C
  Markdown tables (134 source rows = 120 + 14 headers).
- **Messages ↔ exports.** Message field names equal the JSON, flat and legacy keys. Protocol flows
  reference only defined messages and roles. In the state machine, one transition targets `same
  level`, an explicit no-op pseudo-state; this is left as residual.
- **`not_applicable`:** empty. All artifact kinds are present.

## Counts after verification

| artifact | count |
|---|---|
| requirements | 461 entries = 345 rows + 27 F + 25 AppC + 16 AppD + 48 P; BCP 14 11 = 11 |
| maps_to | 265 v4.0.3 entries (190 reqs, stated) + 204 CWE (inferred) |
| object model | 43 objects, 45 edges (1 edge inferred), 9 gaps |

## Residual open issues

1. The `object-model.md` diagram does not draw `ApprovalStatus` or the 8 added edges.
2. The P-* entries carry derived actor and phase. They need human review, as the rest of the derived
   typing does.
3. Source defects to report upstream: the empty CycloneDX level membership, and the typos
   "execptions", "onyly" and "prganizations".
4. Pass 4 (human `reviewed_by`) is outstanding.
