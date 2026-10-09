---
schema: "library-distilled/v1"
id: uk-software-security-code-of-practice-distilled
record: uk-software-security-code-of-practice
type: index
updated: "2026-10-02"
---

# Distilled artifacts — uk-software-security-code-of-practice

| File | Kind | Coverage |
|---|---|---|
| `normative.md` | normative | The whole Code principle block verbatim (4 themes, 14 principles, theme stems), the other normative Code statements (SRO, skills, scope, glossary "should"s), the Table 1 applicability, and Assurance and self-assessment. Per principle: the APC claims and every IG normative statement. The IG Appendix 1 mapping. |
| `requirements.yaml` | requirements | 166 entries, all verbatim and machine-checked. 14 Code principles, 11 other Code statements, 45 APC claims + 1 APC recommendation (added in verify), 95 IG statements. Header gives the BCP 14 count (0) and the source's own modal counts, with reconciliation. |
| `object-model.yaml` / `object-model.md` | diagram | Object-model pass: 46 objects, 42 edges, 6 gaps for tmodel. Every entry has a locator. Mermaid class diagram. |
| `protocol.yaml` / `protocol.md` | protocol | Information-exchange flows: vulnerability handling (3.2–3.5), incident communication (4.3), support and end of support (4.1–4.2). 6 roles, 14 named exchanges, Mermaid sequence diagrams. |
| `state-machine.yaml` | state-machine | Vulnerability lifecycle (triage: fix, acknowledge, investigate further), product support lifecycle (≥ 1 year notice guard), incident lifecycle. |
| `design-notes.md` | design-notes | Adopt, adapt and reject against R-040..R-044 and ARCH-0001 §2b and §3b, plus 6 open questions. |

Not applicable (reasons in record.yaml): schema, messages, examples.

## Verification

`verification.md` — independent verify (pass 2) and cross-check (pass 3), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues.

`apc-claim-trees.yaml` (diagram) — the APC Appendix claims trees, transcribed in the verify pass from the four NCSC SVGs (68 claim nodes).
