---
record: rfc-5280
kind: index
title: "rfc-5280 — distilled artifacts"
extracted: "2026-10-13"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

Full extraction of **RFC 5280, Internet X.509 PKI Certificate and CRL
Profile** (Cooper et al., May 2008, Standards Track). Source
`.cache/rfc-5280.txt`, sha256 `a2f2628c0a83…633345d`, 8459 lines, read in
full. This is the text as published: RFC 6818, 9549, 9598, 9608 and 9618
update it, and none of their amendments is applied here.

**Status: passes 1–3 complete, at high effort, not max.** `record.yaml`
declares `distillation.profile: full` but stays `status: summarized`. FX-1
requires every pass at maximum effort. These passes ran at high by the record
owner's decision, with only the design-notes agents at max, and each pass
records the effort it actually ran at. So the artifacts are built in full but
do not meet the FX-1 bar. Issue #64 still owns the extraction until the
passes are redone at max. `reviewed_by` is empty on every artifact.

**532 BCP 14 keywords in the source, 450 in the requirement texts.** The
difference is reconciled keyword for keyword in `requirements.yaml`: 81 are
ASN.1 `OPTIONAL` type notation and one is prose naming that token. The ten
non-RFC 2119 `RECOMMENDS` count 0 and are extracted as RECOMMENDED or NOT
RECOMMENDED.

**No artifact is not-applicable.** The source has no wire protocol, so
`protocol.yaml` is partial and says so in-file. §3.4 and §3.5 defer
operational protocols to other PKIX specifications.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 519 verbatim entries, `N-001`–`N-517` plus `N-600`, `N-601` (added by pass 2 at their source positions), each one contiguous run of source lines with its range. Flags: 197 lowercase/implied, 53 page break removed, 35 ASN.1, 3 RECOMMENDS only. §11 references, overview, history and the RFC 3280 differences are omitted, each noted in place. Appendix A and C live in `schema/` and `examples/`. |
| requirements | `requirements.yaml` | 625 entries `R-0001`–`R-0701`; counts 532 source / 450 extracted, reconciled. 176 `verb: none` (151 §6 algorithm steps, 19 §7, 6 Appendix B). 623 stated, 2 inferred (`R-0334`, `R-0359`). 474 testable, 107 partial, 44 not. `R-0700` and `R-0701` were added by pass 2 and are out of source order. |
| schema | `schema/` | Appendix A.1 `PKIX1Explicit88` and A.2 `PKIX1Implicit88` verbatim, plus 32 inline ASN.1 regions from 30 sections, each with its line range and sha256. 13 inline-to-appendix findings `F-01`–`F-13`. 0 undefined references. Not compiled: no ASN.1 compiler offline. |
| messages | `messages.yaml` | 79 structures, 223 fields: 66 profiled, 6 retrieval formats, 5 validation inputs/outputs, 2 appendix-only. All 29 extension OIDs with stated criticality. DER TLV layout per structure. 459 requirements wired. 14 source defects. RFC 2797 CMS internals and ORAddress sub-structures excluded. |
| protocol | `protocol.yaml`, `protocol.md` | **Partial**: no wire protocol in the source. 11 roles. 13 flows (105 steps): issuance, CRL issuance, retrieval, trust anchors, validation, path discovery, rollover, CA compromise. 9 algorithms: §6.1 and §6.3 step by step, name constraints, §7 comparison, delta combination, critical extensions. 40 error paths, 37 source defects and ambiguities, 20 not-defined items. 15 Mermaid diagrams, not rendered. |
| state-machine | `state-machine.yaml` | 10 machines, 46 states, 92 transitions (25 inferred), 25 events: §6.1 path validation with the full §6.1.2 state vector, the policy tree, §6.3.3 CRL validation, validity, revocation status, CRL issuance and numbering, cached and delta CRLs, indirect CRLs, key rollover. 25 open questions. |
| examples | `examples/` | 4 Appendix C fixtures, byte-exact. All four decode against the schema with 0 schema or DER violations. C.1, C.2 and C.4 signatures verify; C.3's issuer key is not in the source. 86 vectors: 44 in-source, 42 constructed, 2 ambiguous. |
| design-notes | `design-notes.md` | 10 adopt, 7 adapt, 15 reject. A mapping row for every `bears_on` id plus R-M-04, ADR-0001, ARCH-0001 §4.2, §4.3 and §6, DEC-002/D-3, DEC-003, DEC-004 and DEC-008. 14 open questions, among them five `delegation-models` answer claims that #64 must correct. Decides nothing. |

## Known gaps, stated rather than hidden

- Passes 1–3 ran at high effort, not max (the design-notes agents excepted).
  The record cannot become `distilled` until they are redone at max.
- `reviewed_by` is empty throughout. No person has signed any artifact.
- No vector has been run through an implementation's path validator. The
  ASN.1 modules have not been compiled.
- The design notes cite our decisions as read from ARCH-0001 v0.1.1,
  ADR-0001, ARCH-0002 and the 2026-09-28 minute. A reviewer should check each
  mapping row against the current text.
- Correcting the `delegation-models` topic answer's five X.509 claims is part
  of issue #64. It belongs to the topic, not this record.
