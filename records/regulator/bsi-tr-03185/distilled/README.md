---
schema: "library-distilled/v1"
id: bsi-tr-03185-distilled
record: bsi-tr-03185
type: index
updated: "2026-10-02"
---

# bsi-tr-03185: distilled artifacts (FX-1)

Source: BSI TR-03185 *Secure Software Lifecycle*, **Version 1.1.1**, English. Table 1 dates it 2026-07-02;
the PDF was created on 2026-08-20.
sha256 `199c87754dec3eab884c18da6c3f6030e6fa7ced282f06e87fed7fe7841e8329`, 51 pages. Local renderings are
`.cache/bsi-tr-03185.txt` (pdftotext -layout) and `.cache/bsi-tr-03185.md` (faithful Markdown).
The secondary source, BSI's *Anforderungen und Prüfspezifikation v1.0* (2026-01-09), is in
`.cache/lane-d/bsi/Hilfsmittel.zip` (sha256 `d85508799c9ff34c27be399c08f157f674bcfd9c7aae32d16672f5d8edb1dc4d`).

| Artifact | Coverage |
|---|---|
| `normative.md` | Every requirement cell, verbatim, in source structure (Tables 5–32 and 35–40) with each table's Additional information, Keywords and Glossary rows. Also the framing prose: §0.1 AI, §1.1 scope, §1.2.1 terms, §1.2.2 modal verbs, §1.3 basis, §2.1.1, §2.2.1–2.2.3, §2.3 and the "Induced by" rule. Includes the cited footnotes and the glossary terms the requirements rely on. |
| `requirements.yaml` | 191 entries: 169 Part 1 native ids, 20 Part 2 ids and 2 prose statements (R-0001/R-0002, inferred). Header counts: source 352, extracted 338; the 14 missing are the modal-verb definitions, explained in `reconciliation`. Typed `library-requirements/v2`: normativity, actor, nature, phase, expects_deliverables, verification, testable. `maps_to` holds the BSI-published mappings: 34 chapter-level, 164 requirement-level from the Prüfspezifikation, and 31 Induced-by. |
| `crosswalk.yaml` | Inverse index of those mappings: target → TR ids, covering IT-Grundschutz (62 refs), IEC 62443-4-1 (42 ids), NESAS (20), SSDF (40), plus in-document mappings. Generated from requirements.yaml. |
| `messages.yaml` | 17 work-product and communication structures whose content the TR prescribes, each field with `constrained_by` ids. Examples: threat model, interface secure design, issue analysis, resolution decision, security-update documentation, release record, user docs, OSS documentation set, audit row. |
| `schema/` | 7 derived JSON Schemas generated from messages.yaml. The TR has no schema of its own. |
| `protocol.yaml`, `protocol.md` | 6 process flows with roles, steps and error paths, with Mermaid sequence diagrams: issue handling and disclosure, proactive discovery, test→release→delivery, tool patch intake, end of support, OSS reporting. |
| `state-machine.yaml` | 5 machines: security issue (SM1), release (SM2), tool patch (SM3), threat model (SM4), product support lifecycle (SM5). |
| `object-model.yaml`, `object-model.md` | Object-model pass: 67 objects, 45 edges, 8 gaps against ARCH-0001 and DL-0009. Includes a Mermaid class diagram. |
| `design-notes.md` | Adopt / adapt / reject against R-040 to R-044 and DEC-009, plus 7 open questions, including 4 source defects. |

Not applicable: `examples/` — see `record.yaml` distillation.not_applicable.

Passes recorded: extract only, by lane D, on 2026-10-02. Verify and cross-check: done 2026-10-02 by an independent verifier (see `verification.md`). Every derived field (actor, nature, phase, deliverables, verification, testable) needs
human review.
