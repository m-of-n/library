---
record: slsa-1-2
kind: index
title: "slsa-1-2 — distilled artifacts"
extracted: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — SLSA v1.2

FX-1 (`docs/extraction.md`) plus the object-model pass. Source: `slsa-framework/slsa`
`releases/v1.2` @ `ae7fc762` and the rendered single page https://slsa.dev/spec/v1.2/zonepage
(sha256 `d9e2a942…1d052`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | all 16 normative/technical pages verbatim (tracks; Build basics, terminology, requirements, distributing provenance, verifying artifacts, assessing build platforms; Source requirements, verifying source, assessing SCS, example controls; threats A–I + dependency/availability/verification threats; verified properties; attestation model; build provenance; VSA). Informative pages are summarized in `../summary.md` only |
| requirements | `requirements.yaml` | all 243 sentences carrying the 268 BCP 14 keywords (121 requirement, 88 recommendation, 34 permission); Build 124 / Source 87 / cross-track 32; actor, level, phase, nature, deliverables, verification typed; count reconciled (268 = 268) |
| schema | `schema/` | 3 verbatim (provenance cue + proto, VSA jsonc) + 3 derived JSON Schemas (provenance v1, VSA v1, Source VSA profile) |
| messages | `messages.yaml` | 18 structures: DSSE envelope, in-toto Statement, provenance v1 and its sub-messages, ResourceDescriptor, VSA, SlsaResult, Source VSA profile, source provenance, roots-of-trust entry, expectations, v0.2 migration; `constrained_by` → R-ids |
| protocol | `protocol.yaml`, `protocol.md` | 9 flows (build-and-attest, distribute, verify provenance, issue/verify VSA, source change, verify source revision, safe expunge, assess platform) with Mermaid sequence diagrams |
| state-machine | `state-machine.yaml` | 9 machines: Build and Source level ladders, control continuity, named reference, proposed-change review, attestation publication, provenance verification, VSA verification, expectations TOFU |
| examples | `examples/` | 21 indexed fixtures (verbatim, normalized, external, derived negatives) + 54 threat scenarios + 2 VSA verification cases |
| design-notes | `design-notes.md` | adopt/adapt/reject vs ARCH-0001 §2b/§3b/§4, DL-0009 R-040..R-044, DEC-009, ADR-0001; 5 open questions |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 80 objects, 81 edges (1 object + 3 edges inferred; 25 edges added by the verify pass), 8 gaps |
| verification | `verification.md` | FX-1 pass 2 (verify) and pass 3 (cross-check), 2026-10-02: checks, scripts, counts, defects fixed, residual issues |
