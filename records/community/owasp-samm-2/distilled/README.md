---
schema: "library-distilled-index/v1"
id: owasp-samm-2-distilled
record: owasp-samm-2
kind: index
type: index
title: "owasp-samm-2 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — OWASP SAMM v2.2.0

FX-1 (`docs/extraction.md`) plus the object-model pass. Source: release asset
`samm.tar.gz` (sha256 `ec8dce3a…3b05`) = the 302 YAML files of `model/`, and
the release's toolbox spreadsheet for scoring. Passes: extract, then independent verify and cross-check (2026-10-03,
`verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | the whole model verbatim: 3 maturity levels, 24 answer sets, 5 functions, 15 practices + 45 level objectives, 30 streams, 90 activities, 90 questions, 295 quality criteria, each with its file locator |
| requirements | `requirements.yaml` | 415 entries = 30 streams + 90 activities + 295 quality criteria; `library-requirements/v2`; 506 `maps_to` links, all published by OWASP SAMM |
| requirements (crosswalk) | `crosswalk.yaml` | every row of the official SAMM mappings spreadsheet (SSDF 1.1 77, BSIMM14 125, IEC 62443-4-1 60, NIST CSF 2.0 83, Microsoft SDL 47, TMC 36) and the NIST-OLIR SSDF workbook (77 stream rows, 81 activity rows), with relationship vocabulary; IEC requirement texts deliberately not copied |
| schema | `schema/samm-core-model.derived.schema.json` | DERIVED JSON Schema (2020-12) for the 8 document types; validates all 302 files with 0 errors under a YAML 1.2 loader (under PyYAML/YAML 1.1 the 24 answer sets fail: unquoted `No` parses as boolean — source defect, see schema description); `x-references` names GUID targets. SAMM publishes no schema |
| messages | — | not applicable (see record.yaml) |
| protocol | — | not applicable (see record.yaml) |
| state-machine | `state-machine.yaml` | the 3 stated maturity levels (+ implied level 0) and the toolbox scoring function with cell formulas; finding: levels are summed, not gated |
| examples | `examples/` | 3 constructed scoring fixtures with expected scores + checker `score.py`; all 24 answer sets verbatim |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044, DEC-009, ARCH §2b/§3b/§4/§5, MAP-0001; 6 open questions incl. source defects |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report: methods, counts, defects found and fixed, residual issues |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 19 objects, 22 edges, Mermaid class diagram, 6 gaps |
