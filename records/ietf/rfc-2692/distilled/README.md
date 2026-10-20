---
record: rfc-2692
kind: index
title: "rfc-2692 — distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **RFC 2692, SPKI Requirements** (Ellison, September
1999, Experimental). Source `.cache/rfc-2692.txt`, sha256
`6a88c1563590…976d`, 787 lines, read in full.

**Status: passes 1–3 complete.** `record.yaml` declares
`distillation.profile: full`. `reviewed_by` is empty on every artifact. A
person signs it, and until then these are readable but not buildable-on.

**No BCP 14 keyword anywhere.** RFC 2692 never cites RFC 2119; its
requirements are lowercase prose and a brainstorm list. So both keyword counts
are a measured 0, every requirement carries `verb: none`, and
`requirements.yaml` `reconciliation` states the inclusion rule used instead.

**No wire format.** The source prints no grammar and rules ASN.1 out, so the
schema is derived, the messages are abstract and the protocol is partial. Each
says so in-file.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 104 verbatim entries `N-001`–`N-104` in source order, all `_[lowercase/implied]_`. 40 of 45 lowercase modals covered; the other 5 are in the Full Copyright Statement. Four entries cross a page break and are flagged. Front and back matter, Charter ¶1 and Background ¶1 excluded. |
| requirements | `requirements.yaml` | 158 entries `R-0001`–`R-0158`, all `verb: none`; counts 0 = 0, reconciled. 158 stated, 0 inferred. 34 testable, 109 partial, 15 not. Every certificate use is an entry (`R-0050`–`R-0150`). |
| schema | `schema/` | No verbatim schema. One **derived** JSON Schema 2020-12, `spki-requirements.derived.schema.json`: 33 `$defs`, five certificate profiles. 21 rules JSON Schema cannot express and 15 gaps, each quoted, in `README.md`. The derived file is ours, not the RFC's. |
| messages | `messages.yaml` | 48 structures, **abstract** by the source's design: certificate, keyholder identifier, encoding profile, name binding, CRL and CRL sequence, revalidation and one-use instruments, every certificate use. `constrained_by` on every field and variant. |
| protocol | `protocol.yaml`, `protocol.md` | **Partial**: CRL transmission and repositories are unspecified by the source. 26 roles, 26 flows with 88 steps (37 inferred), 34 error paths, 7 non-flows. One Mermaid sequence diagram per flow. |
| state-machine | `state-machine.yaml` | 16 machines, each with a source status (required / permitted / rejected / considered / brainstorm). Every trigger is a `messages.yaml` entry or a declared event. 12 `not_modelled` items, 18 open questions. |
| examples | `examples/` | 140 vectors: 95 from source text, 45 constructed. No byte-level vectors; the source prints none. 135 instances validated against the derived schema (127 valid, 8 invalid rejected). None run through an implementation. |
| design-notes | `design-notes.md` | 15 adopt, 11 adapt, 8 reject. A mapping row for every `bears_on` id. MD-3 addressed with a DEC-002 options table. 22 open questions. Main finding: a KSA revoke fails `R-0024`–`R-0028`'s determinism test (ADR-0003 D5). Decisions read from m-of-n `643fba2`. Decides nothing. |

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- No vector has been run through an implementation.
- The design notes read our decisions at m-of-n `643fba2`. A reviewer should
  check each mapping row against the current decisions.
- The design notes propose `bears_on` corrections; `record.yaml` was not
  edited for them.
