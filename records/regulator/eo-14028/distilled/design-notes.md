---
schema: "library-distilled/v1"
id: eo-14028-design-notes
record: eo-14028
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# EO 14028 §4 — design notes for tmodel

**Status (2026-10-02):** EO 14028 is in force. §4 has not been textually amended. EO 14144
(2025-01-16) built on it (RSAA machine-readable attestations, CISA validation, SSDF update) and
EO 14306 (2025-06-06) struck EO 14144's attestation-validation subsections while keeping a
re-dated SSDF-update directive. The OMB implementation of §4(k) (M-22-18 / M-23-16) was rescinded
by M-26-05 (2026-01-23). So: the *practices* of §4(e) remain the federal reference; the
*mandatory attestation* is gone.

## Adopt

- **§4(e)(i)–(x) as a crosswalk hub (R-044).** Ten stable, citable practice areas that the CISA
  form, SSDF and many vendor attestations map to. Add them as `Requirement` nodes in MAP-0001 and
  use the form's published mapping (form item → §4(e) id → SSDF task) as stated edges.
- **The one gate (R-041).** §4(e)(iv): vulnerability checks "shall operate regularly, or at a
  minimum prior to product, version, or update release" — a release-gate exit criterion that a
  tmodel SDL `Gate` can carry and evaluate from Evidence.
- **Public risk summary (R-043).** §4(e)(v) asks producers to make publicly available "a summary
  description of the risks assessed and mitigated" — exactly a redacted, governed projection of a
  threat model. tmodel's governed-view design should include a *public summary* view of a
  threat-model instance (assets/threats/mitigations at a disclosure-safe level).
- **Milestone chains (R-041).** §4 is a dependency graph of dated directives (`state-machine.yaml`).
  Milestones need `offset_from` another milestone, owner Party and deliverable.

## Adapt

- **Practice areas are not producer obligations by themselves.** The EO obliges NIST to issue
  guidance *regarding* them; producers are bound only through OMB/FAR. In the crosswalk, type
  them `practice-area` and attach normativity per implementing document (form, SSDF, CRA).
- **Critical software** is a classification with five defining factors (§4(g)); attach as a
  `Product` classification that can drive which Requirement profile applies (R-042).

## Reject

- Treating EO deadlines as live: all §4 milestones are historical (2021–2022).

## Bears on

R-041, R-042, R-043, R-044, DEC-009 (§4(e)(iv) remediate before release; §4(e)(viii) VDP as an
ongoing mitigation process).

## Open questions

1. Hold NISTIR 8397 (realises §4(r), developer verification minimum standards) and OMB M-21-30
   (§4(j), critical software) as records? Both are SDL-relevant and missing.
2. Record EO 14028's §4(e) ids as the canonical "US federal" profile in MAP-0001, or only via SSDF?
