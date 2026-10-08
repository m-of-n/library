---
record: secure-systems-lab-dsse
kind: index
title: "secure-systems-lab-dsse — distilled artifacts"
extracted: "2026-10-08"
reviewed_by: ""
---

# Distilled artifacts

Distillation of the **Dead Simple Signing Envelope (DSSE)** at pinned commit
`1d3370f62565bca041e97c8310b873ac340edc2e`, source archive sha256
`88fc65fd66d7250445dc08a65a2cb68c942fb88517152246f859a70d6dac3ac1` (verified
against `content.sha256` on retrieval, 2026-10-08).

**FX-1 does not apply to this record.** It is type `repo`, and FX-1
(`docs/extraction.md`, `CLAUDE.md`) is scoped to `rfc` / `draft` / `spec` /
`ietf`; `bin/check-pr-extraction` enforces that scope by type. So this is not a
full extraction and does not claim to be: there is no `distillation` block on
`record.yaml`, no requirements reconciliation, and no state machine. What it
claims is that **the whole specification has now been read** — which is what
`status: distilled` means for a repo record, and is what the
`canonical-encoding` topic needed before it could close.

| Artifact | Covers |
|---|---|
| `normative.md` | Every keyword-bearing statement of `protocol.md` and `envelope.md`, verbatim, in source order, plus the three load-bearing claims of the attack notebook — 24 statements, 9 of which carry a BCP 14 keyword. |
| `design-notes.md` | The five findings that bear on our decisions, including **two corrections** to this record's own earlier summary. |

## Read scope

| File | Read | Note |
|---|---|---|
| `background.md` | full (2026-10-03) | the canonicalisation critique |
| `protocol.md` | full (2026-10-03, re-read 2026-10-08) | PAE, the protocol, multi-signature |
| `envelope.md` | **full (2026-10-08)** | previously unread — the JSON envelope and its parsing rules |
| `envelope.proto` | full (2026-10-08) | 35 lines; schema definition only, Protobuf used only to define the schema |
| `hypothetical_signature_attack.ipynb` | **full (2026-10-08)** | previously unread — Lodato's worked cross-encoding attack, Sept 2020 |
| `implementation/`, `governance/` | not read | implementations and project governance; neither is specification text |

The two files read on 2026-10-08 are the two the `canonical-encoding` topic note
named as the outstanding gap. Reading them changed the answer — see
`design-notes.md` §1 and §2.

`reviewed_by` is empty on both artifacts. A human signs that; until then these
are readable but not buildable-on (`docs/extraction.md` pass 4).
