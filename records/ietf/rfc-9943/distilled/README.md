---
record: rfc-9943
kind: index
title: "rfc-9943 — distilled artifacts"
extracted: "2026-09-30"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

Source: RFC 9943, 1772 lines, `sha256:204aea02…`, cached and digest-verified.
`bin/bcp14-count` on it gives **50** BCP 14 keywords — MUST 30, MAY 17,
REQUIRED 1, OPTIONAL 1, SHOULD 1 — and the extraction reconciles to 50 exactly.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | Every normative statement verbatim with locator. Every section walked, §1 through §11.2, with 128 locators; all 50 BCP 14 keywords; plus the §10 IANA tables and both CDDL figures, reproduced with the RFC's uniform three-space left margin removed and nothing else changed (`schema/` keeps the margin). §1/§2 narrative and the ASCII diagrams are excluded as motivation; the §1.1 boilerplate is reproduced once as the interpretation clause and excluded from the tally. Records separately the lowercase-"must" obligations that carry no keyword. |
| requirements | `requirements.yaml` | All 50 BCP 14 keywords across 48 `stated` entries, plus 16 `inferred` entries carrying none — 64 entries, R-0001…R-0064, in source order. `source_keyword_count` 50, `extracted_keyword_count` 50, `reconciliation` empty because they agree. Every `text` verified a verbatim and contiguous substring. The `note:` states the promotion threshold for keyword-free obligations and the R-0039/R-0040 tiling convention. R-0064 (§6.3 step 1) was added in pass 3 and sits in source order between R-0038 and R-0039; ids are never renumbered. Excludes nothing normative. |
| schema | `schema/` | Both CDDL blocks verbatim and byte-verified: Figure 3 (§6.1, 7 rules) and Figure 7 (§7, 2 rules) — ~38 lines, the entire formal syntax of the RFC. Covers no Registration Policy (§5.1.1 leaves encoding to the operator), no request/response, no verifiable data structure and no proof structures; all deferred to RFC 9942. Five source CDDL defects recorded, not repaired, plus the two undefined types `COSE_CertHash`/`COSE_X509`. |
| messages | `messages.yaml` | 10 structures field by field with COSE labels, types, requirement levels and byte layout, with 80 `constrained_by` links to 54 real requirement ids. Includes the §10 media types and CoAP content formats 277/278, 18 things the RFC references but never defines, and four internal inconsistencies as INC-1…INC-4. Labels 395/396/−1/−2 are carried but marked example-derived — they are normatively RFC 9942's. |
| protocol | `protocol.yaml`, `protocol.md` | 5 flows with 5 Mermaid sequence diagrams: information flow (§5), registration (§6.3, all five steps), Transparent Statement assembly (§7), validation (§7.1), bootstrapping (§5.1.2 with §9.4.3's ranking). Error paths are **absent from the source**, not from this artifact: every `on_error` states where the RFC is silent. |
| state-machine | `state-machine.yaml` | **Not applicable** — the RFC names no states. The file holds the search evidence (including every spelling of *life-cycle*, all four of them motivational §2 prose about the software component, not the protocol), the four ordering constraints that stand in for a lifecycle each tied to the requirement id that carries it (R-0064, R-0046, R-0044, R-0024), and §9.4.2's sanctioned rollback. |
| examples | `examples/` | **Not applicable** — all 14 `h'…'` literals are elided, zero complete 32-hex runs, so nothing is reproducible. The file inventories the 6 EDN figures, says per label whether it comes from a figure or from §7 prose (`-2` and the name `RFC9162_SHA256` are prose-only), and records the two defects in the figures. |
| design-notes | `design-notes.md` | The D-3 header-by-header mapping and export mapping; adopt A1–A9, adapt B1–B8, reject C1–C7; DEC-002 / DEC-007 / R-M-12 assessed; open questions O1–O7. Flags every reconstructed decision gloss as a reconstruction, and ranks the five unextracted dependency records with RFC 9162 first. |

## Status

Pass 1 (extract) is complete: one agent per artifact kind, each reading the
source and never a summary. Pass 2 (verify) recounted and re-quoted the
extraction against the source. Pass 3 (cross-check) walked the artifacts
against each other: every requirement that names a field or structure resolves
to `messages.yaml` or `schema/`, every message named in a `protocol.yaml` flow
is defined or explicitly flagged `message_defined: false`, and every ordering
constraint in `state-machine.yaml` now carries its requirement id. All three
passes are recorded in `record.yaml` under `distillation.passes`.
**`reviewed_by` is empty on every artifact** — no human has signed any of them,
so these are readable but not yet buildable-on.
