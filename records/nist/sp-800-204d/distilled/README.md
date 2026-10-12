---
record: sp-800-204d
kind: index
title: "sp-800-204d — distilled artifacts"
extracted: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`), plus the Lane A object-model pass. Source: NIST SP 800-204D (final,
February 2024), sha256 `74e404d98c9dd74722b678246e5127ffeede71c4b80d0c631c995650128174e8`.
Each line says what an artifact covers and what it does not.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every modal or imperative statement in the Executive Summary, §1–§6 and Appendices A–B, verbatim with locator and R-id; 15 definitional statements; Tables 1–3; the Fig. 1 transcription. Excludes the FISMA authority boilerplate and §1.5/§6 narrative. |
| requirements | requirements.yaml | 126 entries `sp-800-204d#R-0001..R-0126`: 114 from the body, 10 Appendix A restatements that differ in wording or strength from §5, and 2 Appendix B scope exclusions. 26 requirement, 66 recommendation, 1 permission, 33 practice. All 15 native designators are included. Lowercase-modal baseline reconciled in the header (body: 78/78 should, 17/17 must). maps_to = Appendix A Table 2 → SSDF v1.1 (stated) plus 3 inferred. |
| protocol | protocol.yaml, protocol.md | 4 derived flows (build→attest→verify→admit; update-signing gate; PULL-PUSH contribution; GitOps reconcile), 15 roles, error paths, Mermaid sequence diagrams. Derived: the source defines no wire protocol or messages. |
| state-machine | state-machine.yaml | 3 machines: artifact admission (8 states), GitOps configuration drift (3 states), and the three-stage SSC attack (§2.4.2). State names are ours; each transition cites R-ids; inferred transitions are flagged. |
| design-notes | design-notes.md | Adopt / adapt / reject against tmodel R-040–R-044, DEC-009, ARCH §1/§3b/§4 and ADR-0001; 7 source inconsistencies; open questions. |
| diagram | object-model.yaml, object-model.md | Object-model pass: 62 objects, 45 edges (1 inferred), 7 gaps; Mermaid class diagram. |
| verification | verification.md | Verify and cross-check passes (2026-10-02). Covers methods, counts, the 4 defects found and fixed (typing, claim, state-machine events, App. A restatement), and residual issues. |

Not applicable (reasons in `record.yaml` `distillation.not_applicable`): **schema**, **messages**
and **examples**. SP 800-204D defines no data structures, encodings or test vectors, and it puts
SBOM and attestation formats explicitly out of scope (§1.2, §6).
