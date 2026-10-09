---
schema: "library-distilled-index/v1"
id: eu-cra-2024-2847-distilled
record: eu-cra-2024-2847
type: readme
updated: "2026-10-02"
---

# Distilled artifacts — Regulation (EU) 2024/2847 (CRA)

Source: EUR-Lex English HTML of OJ L 2024/2847 (sha256 `628cb514…a5589`), captured to `.cache/eu-cra-2024-2847.md`.
The PDF (sha256 `e3ecaabd…1b0a`, 81 pp.) is the authentic rendering. Corrigendum OJ L 2025/90555 is applied to
Art 64(10).

| Artifact | Kind | Coverage |
|---|---|---|
| `normative.md` | normative | Verbatim: Art 3 definitions; Arts 13, 14, 15, 16, 17, 24, 31, 64(2)-(4),(10), 69, 71; Annex I Parts I-II, Annex II, Annex VII. A title-only ToC for every other article. Delegated Reg 2026/881 Arts 2-5 summarised. |
| `requirements.yaml` | requirements | 191 entries: 153 requirements, 4 prohibitions, 24 permissions, 10 definitions. In-scope lowercase baseline: shall 126, shall not 5, may 24, reconciled. BCP 14: 0/0. |
| `protocol.yaml`, `protocol.md` | protocol | 10 roles, timers, 12 flows, error paths; Mermaid sequence diagrams. |
| `state-machine.yaml` | state-machine | SM1 AEV reporting, SM2 severe-incident reporting, SM3 vulnerability handling, SM4 support lifecycle. |
| `messages.yaml` | messages | Art 14 notifications and user information, Art 15 voluntary reports, plus Annex II, Annex VII, SBOM and CVD-policy structures. |
| `schema/` | schema | One derived JSON Schema (Art 14 notification family). |
| `design-notes.md` | design-notes | Adopt / adapt / reject against R-040..R-044 and DEC-009; inferred crosswalk hooks; 9 open questions. |
| `object-model.yaml`, `object-model.md` | diagram | Object-model pass: 51 objects, 37 edges (3 added in verify), 8 gaps. |

Not applicable: **examples**. The Regulation has none; the 67 worked examples are in Commission guidance C(2026) 5252,
which is a separate document.

Passes: extract (claude, lane D, max, 2026-10-02). Verify and cross-check: done 2026-10-02 by an independent verifier (see `verification.md`).
