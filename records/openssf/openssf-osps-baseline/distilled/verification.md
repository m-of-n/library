---
record: openssf-osps-baseline
kind: verification
title: "openssf-osps-baseline — FX-1 pass 2 (verify) and pass 3 (cross-check)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# OSPS Baseline v2026.08.28: verification report

Passes 2 and 3 of FX-1, run on 2026-10-02 by an agent that did not do the extraction. Every
comparison was made against the tagged source YAML. The record's own text and the extractor's
`extract.py` were not used as a source.

The tarball `.cache/lane-e/osps/osps-v2026.08.28.tar.gz` was re-extracted into the scratchpad and
`diff -r` against `.cache/lane-e/osps/security-baseline-2026.08.28/`: the two are identical. The
scripts are `verify/osps.py`, `ospsmap.py`, `kwcover.py`, `reqcheck.py`, `typing.py` and
`normcheck.py`. `cue` v0.16.0 was fetched into the scratchpad to run the source's own schema.

## Pass 2: verify

### 1. Hash and currency

- `shasum -a 256` of the tarball = `406dca03…61b8` = `content.sha256`. The live page HTML is
  `d1d60388…176c`, as the record comment says. ✔
- The GitHub releases API shows `v2026.08.28` (2026-08-28T23:28:53Z) as the only and latest
  release.
- The tag ref resolves to `a26a7963f6fd098c1e82829322ec9e1196a4f294`, as `summary.md` says.
- The baseline.openssf.org index lists v2025.02.25, v2025.10.10, v2026.02.19 and v2026.08.28.
- Post-release PRs #558 (merged 2026-09-23) and #554 (merged 2026-09-08) are on `main` only.
- **The record tracks the current edition.** ✔

### 2. Verbatim

This was checked independently, field by field, from the tag's `baseline/OSPS-*.yaml`:

- 65/65 assessment requirements: `text`, `recommendation`, `applicability`, `state`, control title
  and locator are all identical (whitespace-collapsed);
- 41/41 control objectives, 8/8 family descriptions and 40/40 lexicon definitions are present
  verbatim in `normative.md`;
- 138/138 quoted strings in `normative.md` are substrings of the source corpus (tag YAML, Gemara
  v1.2.0 CUE, `docs/*.md`, site index);
- the two `-REC` permission entries ("The filename MAY have an extension.") are verbatim from the
  recommendations of OSPS-LE-03.01 and OSPS-LE-03.02.

No spliced quotes were found.

### 3. Locators

All 67 were checked mechanically: each `OSPS-XX.yaml <control> / <AR>` locator names the file and
control that hold the text. ✔

### 4. Completeness

- `bin/bcp14-count` over the concatenated tag YAML gives 66 (MUST 62, MUST NOT 2, MAY 2), matching
  the header. All 66 occurrences fall inside an extracted text: 0 uncovered.
- `.cache/openssf-osps-baseline.md` counts 130 because the page lists every AR twice (overview plus
  detail). The record correctly uses the YAML rendering.
- Header counts were recomputed and all hold:
  - 41 controls, 65 ARs (64 active + 1 retired);
  - per family AC 6 / BR 12 / DO 8 / GV 6 / LE 5 / QA 13 / SA 4 / VM 10;
  - applicable L1 24 / L2 41 / L3 62;
  - introduced 24 / 19 / 21.
- The live page (`site-2026-08-28.html`) has all 64 active AR texts identical once inline link
  markup is removed.
- The tag's `docs/versions/2026-08-28.md` is stale. 26 ARs differ, and "While active," still
  appears 52 times. PR #544, "Remove 'While active' qualifier", was merged 2026-08-28. This
  confirms design-notes Q4.

### 5. Typing

- 64 active ARs are `requirement`, each with exactly one MUST or MUST NOT.
- The two `-REC` entries are `permission`.
- OSPS-BR-01.02 is `retired`, with no verb.
- No requirement is weakened.
- `levels` equals `applicability` for all 67.
- The non-cumulative OSPS-BR-07.01 and OSPS-VM-02.01 (maturity-1 only) are faithful to the source
  and flagged in the design notes.

### 6. Object model

- **Defect V-1, fixed:** two edge endpoints were free text, not objects:
  - `defines → "domain objects"` became `defines_term_used_in → AssessmentRequirement | Control`;
  - `published_as → "advisory data"` now points to a new stated object, `VulnerabilityAdvisory`
    (OSPS-VM-04.01).
- **Defect V-2, fixed:** 7 objects had no edge. Nine stated edges were added, each with an AR or
  Gemara locator:
  - MappingDocument `has_mapping`;
  - Mapping `mapping_source` and `mapping_target`;
  - MappingDocument `targets_framework`;
  - User `accesses` SensitiveResource (AC-01.01);
  - SensitiveData `must_not_be_stored_in` VCS (BR-07.01);
  - DesignDocumentation `describes_actions_and_actors_of` (SA-01.01);
  - CICDPipeline `runs_test_suite` (QA-06.01);
  - ProvenanceInformation `verification_instructions_for` ReleasedSoftwareAsset (DO-03.01/.02).
- The ProvenanceInformation locator was tightened. No AR text says "provenance"; the support is
  the OSPS-DO-03 control title and the BR-06.01 recommendation.
- The total is 45 objects and 48 edges.

### 7. Claims

All of these were confirmed against sources:

- tag commit, release time, prior versions, #558 and #554, #544;
- `draft: true` and unset `metadata.version` (`metadata.yaml`);
- Gemara `#Lifecycle` values;
- "retired AR must not carry a recommendation" (`controlcatalog.cue` `if state == "Retired"`);
- 8 `#RelationshipType` values and 9 `#EntryType` values;
- "Controls only contain MUST entries, not SHOULD." (`docs/index.md`);
- the maintenance rules (`docs/maintenance.md`).

**Defect V-3, fixed.** Design-notes Q6 said "the 9 SLSA targets". The file has 9 mappings with 14
target entries over 6 distinct SLSA 1.0 names. Q6 was rewritten with the counts and the resolution
into `slsa-1-2` (see pass 3).

## Pass 3: cross-check

- **`cue vet`, the source's own CI procedure.** It was run with cue v0.16.0 and
  `github.com/gemaraproj/gemara@v1.2.0` fetched from the CUE registry:
  - all 14 `baseline/mappings/*.yaml` vet clean against `#OSPSMapping`;
  - the catalog assembled from `metadata.yaml` plus the 8 family files vets clean against
    `#OSPSBaseline` once the unquoted `mapping-references[].version` scalars are carried as
    strings. Raw YAML types `2024`, `2.0`, `1.1` and `1.0` as int or float, which
    `#MappingReference.version: string` rejects. This is a source observation, recorded in
    `schema/README.md`;
  - fixtures 01 and 02 vet clean when merged with the catalog `title` and `metadata`, and so does
    fixture 04;
  - fixture 03 is incomplete on its own (missing `mapping-references`). The `examples/README.md`
    expected result was corrected to say so;
  - fixtures 01–05 are byte-identical to their stated source line ranges.
- **Messages ↔ schema.** Every field in `messages.yaml` exists in the Gemara v1.2.0 CUE, except
  `LexiconEntry.term`. That is correct: `lexicon.yaml` is not a Gemara `#Lexicon`, as
  `examples/README.md` fixture 05 says.
- **`maps_to`:** 1 919 control-level mapping entries were checked against
  `baseline/mappings/*.yaml`. All match the target document's own entry ids, and every
  relationship is `relates-to`.
  - **Defect V-4, fixed:** no `maps_to` entry named the target edition. All 602 framework blocks
    now carry `target_edition`, taken from the mapping-reference `version`.
  - Three blocks also carry an `edition_note` where the linked library record holds a different
    edition:
    - SLSA 1.0 vs `slsa-1-2`. All 6 entry names still resolve in SLSA 1.2 `build-requirements.md`,
      mapped to R-ids in design-notes Q6;
    - Scorecard 5.0 vs v5.5.0. All 11 check names exist unchanged in v5.5.0;
    - BSI TR-03185-2 v1.1.0 vs `bsi-tr-03185` v1.1.1. The part and edition differ.
  - The retired OSPS-BR-01.02 carries no `maps_to`. That is acceptable for a tombstone; its
    control's mappings are on the active ARs.
- **State machine.** Every transition endpoint is a declared state, except two explicit
  pseudo-targets: `lower level` and `(successor)`. These are left as residual.
- **`not_applicable`.** The protocol reason is true: the source defines no exchange, roles or
  sequences.

## Counts after verification

| artifact | count |
|---|---|
| requirements | 67 entries (64 active, 1 retired, 2 `-REC`); BCP 14 66 = 66 |
| maps_to | 602 framework blocks / 1 919 entries, all with `target_edition` |
| object model | 45 objects, 48 edges (2 objects / 7 edges inferred), 8 gaps |

## Residual open issues

1. `object-model.md` diagrams do not draw the 9 added edges or `VulnerabilityAdvisory`.
2. Two pseudo-state targets in `state-machine.yaml`.
3. The int and float `version` scalars in the source's `metadata.yaml` would fail a naive
   `cue vet` of the raw YAML. This should be reported upstream.
4. Pass 4 (human `reviewed_by`) is outstanding.
