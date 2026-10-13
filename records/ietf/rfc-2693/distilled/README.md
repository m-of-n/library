---
record: rfc-2693
kind: index
title: "rfc-2693 — distilled artifacts"
extracted: "2026-10-11"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **RFC 2693, SPKI Certificate Theory** (Ellison et al.,
September 1999, Experimental). Source `.cache/rfc-2693.txt`, sha256
`6822d668195c…9098`, 2411 lines, read in full.

**Status: passes 1–3 complete.** `record.yaml` declares
`distillation.profile: full`. `reviewed_by` is empty on every artifact. A
person signs it, and until then these are readable but not buildable-on.

**No BCP 14 keyword anywhere.** RFC 2693 predates RFC 8174 and never cites
RFC 2119. Its binding content is lowercase prose, definitions, displayed rules
and working-group decisions. So both keyword counts are a measured 0, every
requirement carries `verb: none`, and `requirements.yaml` `reconciliation`
states the inclusion rule used instead.

**No artifact is not-applicable.** The source has no wire format, so the
schema, messages and protocol artifacts are abstract or partial. Each says so
in-file and says where the concrete forms live:
`draft-ietf-spki-cert-structure` for certificates, `rfc-9804` for
S-expressions.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 146 verbatim entries `N-001`–`N-146` in source order, from 54 of 68 headed sections; the other 14 say in place why they yield none. All flagged `_[lowercase/implied]_`, with a lowercase-modal census. References, history, quotations and boilerplate not reproduced. |
| requirements | `requirements.yaml` | 251 entries `R-0001`–`R-0251`, all `verb: none`; counts 0 = 0, reconciled. 250 stated, 1 inferred (`R-0122`). 152 testable, 58 partial, 41 not. `R-0251` was added by pass 2 and is the one entry out of source order. Exclusions (overview, history, the 4.1.1–4.1.3 arguments, ruled-out background, rule-less examples) are listed in `reconciliation`. |
| schema | `schema/` | The source prints **no formal grammar**. 5 verbatim files (names, subjects, tags, tuples, validity; 57 regions with line ranges and digests) and one **derived** JSON Schema 2020-12 of 63 productions. Source defects D-01–D-13 recorded, not repaired. The derived file is ours, not the RFC's. |
| messages | `messages.yaml` | 54 structures, **abstract** by the source's design: the tuples, certificates, ACL, validity instruments, CRC and the other structures, decomposed to the fields the source names; printed S-expression shapes; the eight §6.5 translation mappings. `constrained_by` on every field. Field order, dates, keys, signatures and CRL formats are not defined by the source. |
| protocol | `protocol.yaml`, `protocol.md` | **Partial**: §6 calls its plan an example. 14 flows, 11 algorithms (AIntersect, VIntersect, chain, name and threshold reduction among them), 9 design options, 40 error paths, 21 source defects and ambiguities, 25 Mermaid diagrams. Access request, proof of possession and reply are marked `inferred`. |
| state-machine | `state-machine.yaml` | 16 machines, 136 transitions: authorization computation, validity and CRL/revalidation lifecycles, the ruled-out anti-matter CRL, name/chain/threshold reduction, key empowerment and loss, threshold root keys. 26 open questions; `not_modelled` lists the rest. |
| examples | `examples/` | 94 vectors: 58 from source text (every S-expression display) and 36 constructed from stated rules. Computed results sit under `derived:`, marked `in_source: false`. 4 source defects recorded on their vectors. None run through an implementation. |
| design-notes | `design-notes.md` | 12 adopt, 8 adapt, 9 reject. A mapping row for every `bears_on` id plus DEC-002, DEC-003, ADR-0001 and ARCH-0001 §4.1. D-3 is addressed. 15 open questions. Main finding: DEC-004 option 1 cannot be implemented from §6.3.1 alone; six rules a profile must add. ARCH-0001 itself was not reread. Decides nothing. |

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- No vector has been run through an implementation. The candidates in
  `record.yaml` are archival or unmaintained.
- The design notes cite our decisions as the library restates them. A reviewer
  should check each mapping row against the current ARCH-0001.
- Re-reading the `delegation-models` topic answer against this extraction is
  part of issue #64's "Done when". It belongs to the topic, not this record.
