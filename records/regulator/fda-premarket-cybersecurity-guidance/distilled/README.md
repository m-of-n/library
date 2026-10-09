---
schema: "library-distilled-index/v1"
id: fda-premarket-cybersecurity-guidance-distilled
record: fda-premarket-cybersecurity-guidance
type: readme
updated: "2026-10-02"
---

# Distilled artifacts: FDA, Cybersecurity in Medical Devices (QMS / premarket), Feb 3 2026

Source: FDA PDF (64 pp., sha256 `d046fa836048933e1a8795bcf2f8224bcfa08789c2f3ef6f46ae53c2eb096c54`), converted with
`pdftotext -layout` and cleaned into `.cache/fda-premarket-cybersecurity-guidance.md`.

| Artifact | Kind | Coverage |
|---|---|---|
| `normative.md` | normative | Every paragraph or list item yielding a requirement, verbatim, in source order: §I-§VII, Appendices 1-4, normative footnotes. Background-only paragraphs are omitted. |
| `requirements.yaml` | requirements | 426 entries: 33 requirement (statute/regulation restated), 373 recommendation, 20 permission. Section-based ids (`#V.A.1-03`, `#App1.C-05`, `#fn65-01`). 38 sentences excluded with reasons. Own-form counts reconciled (should 175, must 19, shall 6, recommend-forms 66, requires 26, permission forms 32). BCP 14: 0/0. |
| `messages.yaml` | messages | 18 documentation structures (Table 1 elements and their substructures), 157 fields, each with locator and `constrained_by`. |
| `schema/` | schema | 4 derived JSON Schemas (2020-12): SBOM supplement, cybersecurity management plan, architecture view, premarket documentation index. FDA publishes no schema. |
| `examples/` | examples | the guidance's 22 illustrative examples as 40 stated fixture cases (with locators) + 3 constructed negative cases, each with its expected outcome; plus a constructed SBOM-supplement instance that validates against the derived schema. |
| `state-machine.yaml` | state-machine | `vulnerability-disposition` (15 states; stated + inferred transitions, fixtures in `examples/vulnerability-disposition.yaml`) and `device-support-lifecycle` (8 states). |
| `design-notes.md` | design-notes | Adopt A1-A6 / adapt D1-D5 / reject X1-X3 against R-040..R-044, DEC-009, ARCH §2-§5, §10; 5 open questions. |
| `object-model.yaml`, `object-model.md` | diagram | Object-model pass: 46 objects, 42 edges (2 inferred), 9 gaps; Mermaid class diagram. |

Not applicable: **protocol**. The guidance defines no exchange between parties. CVD procedures are required to be
*described* in the plan, and their flows belong to the separate Postmarket Cybersecurity Guidance (2016). The
FDA review interaction (Q-Sub, AI requests, SE/NSE) is agency procedure documented elsewhere.

Passes: extract (claude, lane D, max, 2026-10-02). Verify and cross-check: done 2026-10-02 by an independent verifier (see `verification.md`).
