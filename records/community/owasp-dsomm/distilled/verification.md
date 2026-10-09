---
record: owasp-dsomm
kind: verification
title: "owasp-dsomm — verify pass (secondary reference)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# OWASP DSOMM v5.1.0: verification report

This is a verify-only pass. The record is `status: summarized`, a secondary reference with no FX-1 extraction, so no cross-check pass is recorded.

## Checks

1. **Hash and currency.**
   - `.cache/owasp-dsomm.yaml` hashes to `319f86d7…8e55` = `content.sha256`.
   - A live re-download of `generated/model.yaml` at tag v5.1.0 on 2026-10-03 gives the same hash. ✔
   - `gh release list`: v5.1.0 is Latest (2026-09-21), and the tag resolves to `a2c1b7e6…`. ✔
   - The model's own `meta.version: 5.0.2` / `released: 2026-09-17` lag the tag. This is recorded correctly.
   - Licence: GitHub reports GPL-3.0. ✔
   - The README's AI-assistance statement was found verbatim. ✔
2. **Counts.** Recomputed from the model:
   - 6 dimensions, 24 sub-dimensions, 251 activities;
   - level distribution 1:29, 2:75, 3:80, 4:43, 5:24;
   - 78 activities carry `assessment`;
   - 12 activities carry D3FEND references (key `d3f`).
   - All match `summary.md` and `object-model.yaml`.
3. **Crosswalk (all 251 rows).** `crosswalk.yaml` was compared field by field with the model:
   - dimension, sub-dimension, name, level and uuid;
   - the verbatim `samm2` list, in order;
   - `iso27001-2022`;
   - `openCRE`.
   - **0 differences.**
   - SAMM normalisation: all 278 resolved references follow the `<F>-<PP>-<S>-<L>` → `<F>-<PP>-<L>-<S>` rule, and every target exists as a SAMM v2.2.0 activity file (checked against the unpacked `owasp-samm-2` release). The 2 unresolved references ("TODO" and "V-RT-AB-1") are correctly left unresolved.
4. **Object model.**
   - MaturityLevel labels were confirmed verbatim in `src/assets/YAML/meta.yaml` at v5.1.0: "Level 1: Basic understanding of security practices" … "Level 5: Advanced deployment of security practices at scale".
   - `teamsImplemented` and `teamsEvidence` exist in `src/assets/YAML/schemas/dsomm-schema-implementation.json`. The locators abbreviate the path as `schemas/…`, while the method line gives the full path.
   - Activity attribute keys match the model's keys.

## Defects

None found requiring a fix.

## Residual

- Locators abbreviate repository paths. They resolve under `src/assets/YAML/`.
- The `iso27001-2017` references in the model are not carried in the crosswalk, which is by design (2022 only). That choice is stated in the README coverage.
